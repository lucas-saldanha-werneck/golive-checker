"""Open a page in headless Chromium and record what actually loads.

The result is a plain dict (JSON-serialisable) so it can be saved and replayed
in tests without a network connection.
"""

from __future__ import annotations

import asyncio
import re
import time
from urllib.parse import urlparse
from typing import Any

from playwright.async_api import Browser, async_playwright

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/131.0.0.0 Safari/537.36"
)

# Globals read from the page after load. Only types / small values, never page data.
GLOBALS_JS = """
() => {
  const t = (x) => typeof x;
  const out = {
    FundraiseUp: t(window.FundraiseUp),
    dataLayer: Array.isArray(window.dataLayer) ? window.dataLayer.length : null,
    google_tag_manager: window.google_tag_manager
      ? Object.keys(window.google_tag_manager).filter(k => /^(GTM|G|AW)-/.test(k))
      : [],
    gtag: t(window.gtag),
    fbq: t(window.fbq),
    OneTrust: t(window.OneTrust),
    Cookiebot: t(window.Cookiebot),
    __tcfapi: t(window.__tcfapi),
  };
  return out;
}
"""

NAV_TIMING_JS = """
() => {
  const n = performance.getEntriesByType('navigation')[0];
  if (!n) return null;
  return {
    dom_content_loaded_ms: Math.round(n.domContentLoadedEventEnd),
    load_ms: Math.round(n.loadEventEnd),
    transfer_bytes: n.transferSize || null,
  };
}
"""


LINKS_JS = """
() => Array.from(document.querySelectorAll('a[href]')).slice(0, 2000)
  .map(a => ({href: a.href, text: (a.innerText || a.getAttribute('aria-label') || '').trim().slice(0, 60)}))
"""

BUTTON_TEXT = re.compile(r"^(donate|give)( now| today| monthly)?!?$", re.I)
DONATE_WORDS = re.compile(r"\bdonat|\bgive\b|\bgive now|\bgiving\b", re.I)


def pick_donate_link(page_url: str, links: list[dict]) -> str | None:
    """First link that looks like a donate page. Prefers links whose text says donate."""
    page = urlparse(page_url)
    scored = []
    for i, l in enumerate(links or []):
        href = l.get("href") or ""
        u = urlparse(href)
        if u.scheme not in ("http", "https"):
            continue
        if u._replace(fragment="").geturl() == page._replace(fragment="").geturl():
            continue
        text_hit = bool(DONATE_WORDS.search(l.get("text") or ""))
        href_hit = bool(DONATE_WORDS.search(u.path + "?" + u.query)) or "form=" in u.query
        if text_hit or href_hit:
            text = (l.get("text") or "").strip()
            button = bool(BUTTON_TEXT.match(text))  # "Donate", "Give now", "Donate today"
            says_donate = "donat" in (text + u.path).lower()
            scored.append((0 if button else 1, 0 if says_donate else 1, 0 if text_hit and href_hit else 1 if text_hit else 2, i, href))
    return min(scored)[4] if scored else None


async def _get(context, url: str, limit: int = 300_000) -> dict:
    try:
        r = await context.request.get(url, timeout=15000, max_redirects=5)
        body = (await r.text())[:limit]
        return {"url": url, "status": r.status, "final_url": r.url, "content_type": r.headers.get("content-type", ""), "body": body}
    except Exception as e:
        return {"url": url, "status": None, "error": str(e).splitlines()[0][:200], "body": ""}


async def fetch_agent_files(context, page_url: str, links: list[dict]) -> dict:
    """What an AI agent or crawler sees without running JavaScript."""
    origin = "{0.scheme}://{0.netloc}".format(urlparse(page_url))
    out = {"robots": await _get(context, origin + "/robots.txt", 100_000),
           "llms": await _get(context, origin + "/llms.txt", 2_000)}
    donate = pick_donate_link(page_url, links)
    out["donate"] = await _get(context, donate) if donate else None
    return out


async def capture_page(browser: Browser, url: str, timeout_s: float = 45.0, settle_ms: int = 4000) -> dict[str, Any]:
    """Load `url` and return a capture dict. Never raises for page problems; records them."""
    started = time.monotonic()
    cap: dict[str, Any] = {
        "url": url,
        "final_url": None,
        "status": None,
        "error": None,
        "raw_html": "",
        "rendered_html": "",
        "requests": [],
        "failed_requests": [],
        "console": [],
        "page_errors": [],
        "globals": {},
        "timing": {},
        "initiators": {},  # vendor script URL -> script that inserted it (from Chrome DevTools Protocol)
        "agent": {},  # robots.txt, llms.txt, donate page fetched without JavaScript
    }
    context = await browser.new_context(user_agent=USER_AGENT, viewport={"width": 1366, "height": 900}, locale="en-US")
    page = await context.new_page()
    by_url: dict[str, dict[str, Any]] = {}

    def on_request(req):
        entry = {"url": req.url, "type": req.resource_type, "status": None}
        cap["requests"].append(entry)
        by_url.setdefault(req.url, entry)

    def on_response(resp):
        entry = by_url.get(resp.url)
        if entry is not None and entry["status"] is None:
            entry["status"] = resp.status

    def on_failed(req):
        cap["failed_requests"].append({"url": req.url, "type": req.resource_type, "failure": req.failure})

    def on_cdp_request(ev):
        u = ev.get("request", {}).get("url", "")
        if "fundraiseup.com/widget/" not in u or u in cap["initiators"]:
            return
        ini = ev.get("initiator") or {}
        frames = [f.get("url") for cf in [ini.get("stack") or {}] for f in cf.get("callFrames", []) if f.get("url")]
        parent = (ini.get("stack") or {}).get("parent") or {}
        frames += [f.get("url") for f in parent.get("callFrames", []) if f.get("url")]
        cap["initiators"][u] = {"type": ini.get("type"), "url": ini.get("url"), "stack_urls": list(dict.fromkeys(frames))[:5]}

    try:
        cdp = await context.new_cdp_session(page)
        await cdp.send("Network.enable")
        cdp.on("Network.requestWillBeSent", on_cdp_request)
    except Exception:
        pass  # not Chromium; initiators stay empty

    page.on("request", on_request)
    page.on("response", on_response)
    page.on("requestfailed", on_failed)
    page.on("console", lambda m: cap["console"].append({"type": m.type, "text": m.text[:500]}) if m.type in ("error", "warning") else None)
    page.on("pageerror", lambda e: cap["page_errors"].append(str(e)[:500]))

    try:
        resp = await page.goto(url, wait_until="load", timeout=timeout_s * 1000)
        if resp is not None:
            cap["status"] = resp.status
            try:
                cap["raw_html"] = await resp.text()
            except Exception:
                # Body is gone when the page navigated again (JS redirect). Fetch the final URL once more.
                cap["raw_html_refetched"] = True
        await page.wait_for_timeout(settle_ms)
        cap["final_url"] = page.url
        if cap.get("raw_html_refetched"):
            try:
                r2 = await context.request.get(page.url, timeout=20000)
                cap["raw_html"] = await r2.text()
            except Exception as e:
                cap["error"] = f"could not read server HTML: {str(e).splitlines()[0][:200]}"
        cap["rendered_html"] = await page.content()
        cap["globals"] = await page.evaluate(GLOBALS_JS)
        cap["timing"] = await page.evaluate(NAV_TIMING_JS) or {}
        links = await page.evaluate(LINKS_JS)
        cap["agent"] = await fetch_agent_files(context, page.url, links)
    except Exception as e:
        cap["error"] = f"{type(e).__name__}: {str(e).splitlines()[0][:300]}"
        try:
            cap["final_url"] = page.url
            cap["rendered_html"] = await page.content()
        except Exception:
            pass
    finally:
        cap["timing"]["check_seconds"] = round(time.monotonic() - started, 1)
        await context.close()
    return cap


async def capture_many(urls: list[str], concurrency: int = 3, timeout_s: float = 45.0, on_done=None) -> list[dict[str, Any]]:
    sem = asyncio.Semaphore(concurrency)
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--disable-dev-shm-usage"])

        async def one(u: str):
            async with sem:
                cap = await capture_page(browser, u, timeout_s=timeout_s)
                if on_done:
                    on_done(cap)
                return cap

        results = await asyncio.gather(*(one(u) for u in urls))
        await browser.close()
    return list(results)
