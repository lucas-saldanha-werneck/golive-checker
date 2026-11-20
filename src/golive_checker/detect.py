"""Turn a page capture into facts. Pure functions, no network.

Every fact keeps the evidence it came from (a URL, an HTML fragment, a console
line) so the report and the LLM can only talk about what was recorded.
"""

from __future__ import annotations

import re
from typing import Any
from urllib.parse import parse_qs, urlparse

# --- Fundraise Up -----------------------------------------------------------
# Installation code, as copied from the dashboard (seen on live customer sites):
#   (function(w,d,s,n,a){...j.src='https://cdn.fundraiseup.com/widget/'+a...})
#   (window,document,'script','FundraiseUp','ABCDEFGH');
FU_SNIPPET_RE = re.compile(
    r"\(\s*window\s*,\s*document\s*,\s*['\"]script['\"]\s*,\s*['\"]FundraiseUp['\"]\s*,\s*['\"]([A-Z0-9]{4,16})['\"]\s*\)"
)
FU_WIDGET_URL_RE = re.compile(r"https?://cdn\.fundraiseup\.com/widget/([A-Z0-9]{4,16})")
FU_HOSTS = ("fundraiseup.com", "fndrsp.net")
# Checkout links: "?form=XXXX" opens the Checkout modal on a page with the code installed.
FU_FORM_LINK_RE = re.compile(r"""href=["'][^"']*[?&]form=([A-Za-z0-9_-]{3,40})""")

# --- Tags ---------------------------------------------------------------------
GTM_ID_RE = re.compile(r"\bGTM-[A-Z0-9]{4,9}\b")
GA4_ID_RE = re.compile(r"\bG-[A-Z0-9]{6,12}\b")

CMP_SIGNATURES = {
    "OneTrust": ("cdn.cookielaw.org", "optanon.blob.core.windows.net", "onetrust.com"),
    "Cookiebot": ("consent.cookiebot.com", "consentcdn.cookiebot.com"),
    "Osano": ("cmp.osano.com",),
    "CookieYes": ("cdn-cookieyes.com",),
    "Termly": ("app.termly.io",),
    "iubenda": ("cdn.iubenda.com", "cs.iubenda.com"),
    "Usercentrics": ("app.usercentrics.eu", "web.cmp.usercentrics.eu"),
    "Didomi": ("sdk.privacy-center.org",),
    "TrustArc": ("consent.trustarc.com", "consent-pref.trustarc.com"),
    "Civic Cookie Control": ("cc.cdn.civiccomputing.com",),
    "Quantcast Choice": ("cmp.quantcast.com", "quantcast.mgr.consensu.org"),
    "Complianz": ("complianz-gdpr",),
    "CookieScript": ("cdn.cookie-script.com",),
    "Ketch": ("global.ketchcdn.com",),
    "Enzuzo": ("app.enzuzo.com",),
    "Klaro": ("klaro.js",),
}

# Other donation tools. Seen as loaded scripts/frames or as donate links.
DONATION_PLATFORMS = {
    "Classy (GoFundMe Pro)": ("classy.org", "classy-cdn", "gofundme.com/pro"),
    "Donorbox": ("donorbox.org",),
    "Blackbaud Luminate Online": ("convio.net", "luminateonline.com", "/site/Donation2"),
    "Blackbaud (BBMS / Online Express / NetCommunity)": ("bbox.blackbaudhosting.com", "blackbaud.com", "blackbaudcdn.net"),
    "Engaging Networks": ("e-activist.com", "engagingnetworks.app"),
    "Bonterra / EveryAction": ("secure.everyaction.com", "act.ngpvan.com", "ngpvan.com"),
    "Give Lively": ("givelively.org",),
    "Givebutter": ("givebutter.com",),
    "RaiseDonors": ("raisedonors.com",),
    "iDonate": ("idonate.com",),
    "Funraise": ("funraise.io", "funraise.org"),
    "Qgiv": ("qgiv.com",),
    "GiveWP": ("givewp", "give-donation-form"),
    "DonorPerfect": ("donorperfect.net", "donorperfect.com"),
    "Bloomerang": ("bloomerang.co",),
    "Kindful": ("kindful.com",),
    "JustGiving": ("justgiving.com",),
    "Network for Good": ("networkforgood.com", "networkforgood.org"),
    "Springboard (Jackson River)": ("springboardplatform",),
    "Tiltify": ("tiltify.com",),
    "Stripe Payment Links": ("buy.stripe.com", "donate.stripe.com"),
    "PayPal Donate": ("paypal.com/donate", "paypalobjects.com/donate"),
}

SLOW_LOAD_MS = 6000


def _host(url: str) -> str:
    try:
        return (urlparse(url).hostname or "").lower()
    except ValueError:
        return ""


def _head(html: str) -> str:
    low = html.lower()
    end = low.find("</head>")
    return html[:end] if end != -1 else ""


def _snippet(text: str, idx: int, width: int = 120) -> str:
    s = text[max(0, idx - width // 2): idx + width]
    return re.sub(r"\s+", " ", s).strip()


def detect_fundraiseup(cap: dict[str, Any]) -> dict[str, Any]:
    raw = cap.get("raw_html") or ""
    rendered = cap.get("rendered_html") or ""
    requests = cap.get("requests") or []

    raw_ids = [m.group(1) for m in FU_SNIPPET_RE.finditer(raw)]
    raw_ids += [m.group(1) for m in FU_WIDGET_URL_RE.finditer(raw)]
    rendered_ids = [m.group(1) for m in FU_SNIPPET_RE.finditer(rendered)]

    widget_reqs = []
    for r in requests:
        m = FU_WIDGET_URL_RE.match(r["url"])
        if m:
            widget_reqs.append({"account_id": m.group(1), "url": r["url"], "status": r.get("status")})
    fu_requests = [r for r in requests if any(_host(r["url"]).endswith(h) for h in FU_HOSTS)]
    fu_failed = [f for f in cap.get("failed_requests") or [] if any(_host(f["url"]).endswith(h) for h in FU_HOSTS)]

    account_ids = sorted(set(raw_ids) | set(rendered_ids) | {w["account_id"] for w in widget_reqs})

    # Placement checks run on the server HTML (what "view source" shows).
    head = _head(raw)
    m_head = FU_SNIPPET_RE.search(head)
    in_head = m_head is not None
    scripts_after = 0
    if m_head:
        tail = head[m_head.end():]
        scripts_after = len(re.findall(r"<script\b", tail, flags=re.I))

    snippet_count = len(list(FU_SNIPPET_RE.finditer(raw)))
    m_any = FU_SNIPPET_RE.search(raw)

    console_fu = [c for c in cap.get("console") or [] if "fundraiseup" in c["text"].lower() or "fndrsp" in c["text"].lower()]
    csp_fu = [c for c in console_fu if "content security policy" in c["text"].lower()]

    form_ids = sorted(set(FU_FORM_LINK_RE.findall(rendered)))

    # Which script inserted the widget? (only known when recorded via DevTools Protocol)
    inserted_by = None
    for ini in (cap.get("initiators") or {}).values():
        urls = ([ini.get("url")] if ini.get("url") else []) + (ini.get("stack_urls") or [])
        gtm = next((u for u in urls if "googletagmanager.com/gtm.js" in u), None)
        if gtm:
            ids = parse_qs(urlparse(gtm).query).get("id", ["?"])
            inserted_by = {"kind": "gtm", "container": ids[0], "script": gtm}
        elif urls:
            inserted_by = {"kind": "script", "container": None, "script": urls[0]}
        break

    return {
        "installed_in_source": bool(raw_ids),
        "loaded_at_runtime": bool(widget_reqs) or bool(fu_requests),
        "account_ids": account_ids,
        "snippet_count_in_source": snippet_count,
        "in_head": in_head,
        "scripts_after_in_head": scripts_after,
        "source_excerpt": _snippet(raw, m_any.start()) if m_any else None,
        "widget_requests": widget_reqs[:5],
        "request_count": len(fu_requests),
        "failed_requests": fu_failed[:5],
        "console_errors": console_fu[:5],
        "csp_errors": csp_fu[:5],
        "global_object": (cap.get("globals") or {}).get("FundraiseUp"),
        "checkout_form_links": form_ids[:20],
        "inserted_by": inserted_by,
    }


def detect_tags(cap: dict[str, Any]) -> dict[str, Any]:
    raw = cap.get("raw_html") or ""
    rendered = cap.get("rendered_html") or ""
    requests = cap.get("requests") or []
    g = cap.get("globals") or {}

    gtm_loaded, ga4_loaded, ga4_hits = set(), set(), set()
    pixel_ids, pixel_loaded = set(), False
    for r in requests:
        u = r["url"]
        h = _host(u)
        q = parse_qs(urlparse(u).query)
        if h.endswith("googletagmanager.com") and "/gtm.js" in u:
            gtm_loaded.update(i for i in q.get("id", []) if i.startswith("GTM-"))
        if h.endswith("googletagmanager.com") and "/gtag/js" in u:
            ga4_loaded.update(i for i in q.get("id", []) if i.startswith("G-"))
        if ("google-analytics.com" in h or "analytics.google.com" in h) and "/g/collect" in u:
            # one hit can carry several properties: tid=G-AAA;G-BBB
            ga4_hits.update(i for v in q.get("tid", []) for i in re.split(r"[;,]", v) if i.startswith("G-"))
        if h == "connect.facebook.net" and "fbevents.js" in u:
            pixel_loaded = True
        if h.endswith("facebook.com") and urlparse(u).path.rstrip("/") == "/tr":
            pixel_ids.update(q.get("id", []))
        if h == "connect.facebook.net" and "/signals/config/" in u:
            pixel_ids.add(u.split("/signals/config/")[1].split("?")[0])

    gtm_globals = [k for k in g.get("google_tag_manager") or [] if k.startswith("GTM-")]
    gtm_source = set(GTM_ID_RE.findall(raw))
    gtm_ids = sorted(gtm_loaded | set(gtm_globals) | gtm_source)
    ga4_raw = ga4_loaded | ga4_hits | {k for k in g.get("google_tag_manager") or [] if k.startswith("G-")}
    ga4_ids = sorted({i for v in ga4_raw for i in re.split(r"[;,]", v) if GA4_ID_RE.fullmatch(i)})

    cmps = []
    haystack_urls = [r["url"] for r in requests]
    for name, sigs in CMP_SIGNATURES.items():
        hit = next((u for u in haystack_urls if any(s in u for s in sigs)), None)
        if hit is None and any(s in rendered for s in sigs):
            hit = "(found in page HTML)"
        if hit:
            cmps.append({"name": name, "evidence": hit[:200]})
    if not cmps and g.get("OneTrust") == "object":
        cmps.append({"name": "OneTrust", "evidence": "window.OneTrust"})
    if not cmps and g.get("Cookiebot") == "object":
        cmps.append({"name": "Cookiebot", "evidence": "window.Cookiebot"})
    if not cmps and g.get("__tcfapi") == "function":
        cmps.append({"name": "IAB TCF CMP (unknown vendor)", "evidence": "window.__tcfapi"})

    return {
        "gtm": {
            "container_ids": gtm_ids,
            "loaded_ids": sorted(gtm_loaded | set(gtm_globals)),
            "in_source_ids": sorted(gtm_source),
            "dataLayer_entries": g.get("dataLayer"),
        },
        "ga4": {"measurement_ids": ga4_ids, "collect_hits_for": sorted(ga4_hits)},
        "meta_pixel": {"loaded": pixel_loaded or g.get("fbq") == "function", "pixel_ids": sorted(pixel_ids)},
        "consent": cmps,
    }


def detect_other_platforms(cap: dict[str, Any]) -> list[dict[str, Any]]:
    rendered = cap.get("rendered_html") or ""
    requests = cap.get("requests") or []
    page_host = _host(cap.get("final_url") or cap.get("url") or "")
    hrefs = re.findall(r"""(?:href|src|action)=["']([^"']+)["']""", rendered)
    found = []
    for name, sigs in DONATION_PLATFORMS.items():
        loaded = next((r["url"] for r in requests if any(s in r["url"] for s in sigs) and not _host(r["url"]) == page_host), None)
        linked = next((h for h in hrefs if any(s in h for s in sigs)), None)
        if loaded or linked:
            found.append({
                "name": name,
                "how": "loaded on page" if loaded else "linked from page",
                "evidence": (loaded or linked)[:200],
            })
    return found


def detect_page_health(cap: dict[str, Any]) -> dict[str, Any]:
    timing = cap.get("timing") or {}
    console_errors = [c["text"] for c in cap.get("console") or [] if c["type"] == "error"]
    final = cap.get("final_url") or cap.get("url") or ""
    return {
        "status": cap.get("status"),
        "final_url": final,
        "https": final.startswith("https://"),
        "load_error": cap.get("error"),
        "load_ms": timing.get("load_ms"),
        "dom_content_loaded_ms": timing.get("dom_content_loaded_ms"),
        "check_seconds": timing.get("check_seconds"),
        "request_count": len(cap.get("requests") or []),
        "failed_request_count": len(cap.get("failed_requests") or []),
        "console_error_count": len(console_errors),
        "console_errors_sample": console_errors[:5],
        "page_errors_sample": (cap.get("page_errors") or [])[:3],
        "bot_challenge": _looks_like_challenge(cap),
    }


def _looks_like_challenge(cap: dict[str, Any]) -> bool:
    html = (cap.get("rendered_html") or "")[:20000].lower()
    return any(s in html for s in ("just a moment...", "cf-chl", "verify you are human", "attention required! | cloudflare", "access denied"))


def analyze(cap: dict[str, Any]) -> dict[str, Any]:
    return {
        "url": cap.get("url"),
        "page": detect_page_health(cap),
        "fundraiseup": detect_fundraiseup(cap),
        "tags": detect_tags(cap),
        "other_donation_platforms": detect_other_platforms(cap),
    }
