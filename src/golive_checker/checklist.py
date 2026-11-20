"""Deterministic go-live checklist built from detected facts.

Statuses come from rules here, not from the LLM. The LLM only explains them.
Rules follow the vendor's public install docs:
  - installation code in the global <head>, ideally the last script there
  - do not install it through a tag manager such as GTM
  - GA4 / Meta tracking for the checkout goes through GTM (container template)
"""

from __future__ import annotations

from dataclasses import asdict, dataclass
from typing import Any

from .detect import CMP_SIGNATURES

PASS, WARN, FAIL, INFO = "pass", "warn", "fail", "info"
AGENT_IDS = {"ai_crawlers", "llms_txt", "structured_data", "donate_no_js"}


@dataclass
class Item:
    id: str
    title: str
    status: str
    detail: str
    evidence: list[str]
    blocking: bool = False  # a FAIL on a blocking item means "not ready to launch"


def build_checklist(facts: dict[str, Any]) -> list[Item]:
    page, fu, tags = facts["page"], facts["fundraiseup"], facts["tags"]
    items: list[Item] = []

    # 1. Page reachable
    if page["load_error"] or not page["status"] or page["status"] >= 400 or page["bot_challenge"]:
        why = page["load_error"] or (f"HTTP {page['status']}" if page["status"] else "no response")
        if page["bot_challenge"]:
            why = f"bot challenge / access denied page (HTTP {page['status']})"
        items.append(Item("page_reachable", "Page loads in a headless browser", FAIL, why, [page["final_url"]], True))
        reachable = False
    else:
        items.append(Item("page_reachable", "Page loads in a headless browser", PASS,
                          f"HTTP {page['status']}, final URL {page['final_url']}", [page["final_url"]], True))
        reachable = True

    # 2. Installation code present in server HTML
    gtm_present = bool(tags["gtm"]["container_ids"])
    if fu["installed_in_source"]:
        items.append(Item("fu_code_in_source", "Installation code is in the page source", PASS,
                          f"account ID(s): {', '.join(fu['account_ids'])}", [fu["source_excerpt"] or ""], True))
    elif fu["loaded_at_runtime"]:
        ib = fu.get("inserted_by")
        if ib and ib["kind"] == "gtm":
            via = f"Google Tag Manager container {ib['container']} (recorded initiator: gtm.js)"
        elif ib:
            via = f"JavaScript from {ib['script'][:120]} (not a tag manager)"
        elif gtm_present:
            via = "unknown script; a tag manager is present, so check the GTM container"
        else:
            via = "other JavaScript"
        rule = ("Vendor docs say not to install through script managers like GTM (affects conversion reporting)."
                if (ib and ib["kind"] == "gtm") or (not ib and gtm_present)
                else "Vendor docs ask for the code in the global <head> and confirm it by viewing the page source.")
        items.append(Item("fu_code_in_source", "Installation code is in the page source", WARN,
                          f"Widget loads at runtime but the code is not in the server HTML. Inserted by: {via}. {rule}",
                          [w["url"] for w in fu["widget_requests"]][:3] + ([ib["script"]] if ib else []), False))
    else:
        items.append(Item("fu_code_in_source", "Installation code is in the page source", FAIL if reachable else INFO,
                          "No installation code found in the source and no widget request recorded.", [], True))

    installed = fu["installed_in_source"] or fu["loaded_at_runtime"]
    if not reachable and not installed:
        return items  # nothing else on the page can be judged

    # 3. Placement in <head>
    if fu["installed_in_source"]:
        if fu["in_head"]:
            if fu["scripts_after_in_head"] == 0:
                items.append(Item("fu_in_head", "Code is in <head>, last script", PASS, "Found in <head> with no scripts after it.", [], False))
            else:
                items.append(Item("fu_in_head", "Code is in <head>, last script", WARN,
                                  f"In <head>, but {fu['scripts_after_in_head']} <script> tag(s) follow it. Docs recommend it as the last script.", [], False))
        else:
            items.append(Item("fu_in_head", "Code is in <head>, last script", WARN,
                              "Code is in the page body, not <head>. Docs recommend the global <head> so it runs on every page.", [], False))

    # 4. One account
    if len(fu["account_ids"]) > 1:
        items.append(Item("fu_single_account", "One account ID on the page", FAIL,
                          f"Several account IDs: {', '.join(fu['account_ids'])}. Donations may go to the wrong account.", fu["account_ids"], True))
    elif fu["snippet_count_in_source"] > 1:
        items.append(Item("fu_single_account", "One account ID on the page", WARN,
                          f"Same code pasted {fu['snippet_count_in_source']} times.", [], False))
    elif installed:
        items.append(Item("fu_single_account", "One account ID on the page", PASS, f"{fu['account_ids'][0] if fu['account_ids'] else 'unknown'}", [], False))

    # 5. Widget script actually loads
    if installed:
        bad = [w for w in fu["widget_requests"] if not w["status"] or w["status"] >= 400]
        if fu["failed_requests"] or (fu["widget_requests"] and len(bad) == len(fu["widget_requests"])):
            ev = [f"{f['url']} ({f.get('failure')})" for f in fu["failed_requests"]] + [f"{w['url']} (HTTP {w['status']})" for w in bad]
            items.append(Item("fu_widget_loads", "Widget script loads", FAIL, "Widget or its assets failed to load (blocked or error).", ev[:3], True))
        elif fu["widget_requests"]:
            w = fu["widget_requests"][0]
            items.append(Item("fu_widget_loads", "Widget script loads", PASS, f"HTTP {w['status']}, {fu['request_count']} requests to vendor hosts.", [w["url"]], True))
        else:
            items.append(Item("fu_widget_loads", "Widget script loads", FAIL,
                              "Code found in source but no widget request was made (script may be blocked, disabled by consent, or broken).", [], True))

    # 6. No vendor-related console / CSP errors
    if installed:
        if fu["csp_errors"]:
            items.append(Item("fu_no_console_errors", "No widget errors in console", FAIL,
                              "Content Security Policy blocks vendor resources.", [c["text"][:200] for c in fu["csp_errors"]], True))
        elif fu["console_errors"]:
            items.append(Item("fu_no_console_errors", "No widget errors in console", WARN,
                              "Console messages mention the widget.", [c["text"][:200] for c in fu["console_errors"]], False))
        else:
            items.append(Item("fu_no_console_errors", "No widget errors in console", PASS, "None recorded.", [], False))

    # 6b. Widget released by a consent tool
    ib = fu.get("inserted_by")
    if installed and ib and ib["kind"] == "script":
        cmp = next((name for name, sigs in CMP_SIGNATURES.items() if any(s in ib["script"] for s in sigs)), None)
        if cmp:
            items.append(Item("fu_consent_gated", "Widget not held back by the consent tool", WARN,
                              f"The widget script was inserted by {cmp}, so it depends on consent settings. It loaded in this run; "
                              "confirm it is set as strictly necessary, or visitors who decline cookies may not get the checkout.",
                              [ib["script"][:160]], False))

    # 7. Checkout links
    if installed:
        if fu["checkout_form_links"]:
            items.append(Item("fu_checkout_links", "Donate links open the checkout", PASS,
                              f"{len(fu['checkout_form_links'])} '?form=' link(s): {', '.join(fu['checkout_form_links'][:5])}", [], False))
        else:
            items.append(Item("fu_checkout_links", "Donate links open the checkout", INFO,
                              "No '?form=' links on this page. Fine if the page uses Elements or overlays instead.", [], False))

    # 8. GTM container (needed for checkout events -> GA4 / ads)
    if gtm_present:
        items.append(Item("gtm_container", "Google Tag Manager container", PASS, ", ".join(tags["gtm"]["container_ids"]), [], False))
    else:
        items.append(Item("gtm_container", "Google Tag Manager container", WARN,
                          "No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template.", [], False))

    # 9. GA4
    if tags["ga4"]["measurement_ids"]:
        items.append(Item("ga4", "GA4 measurement ID", PASS, ", ".join(tags["ga4"]["measurement_ids"]), [], False))
    else:
        items.append(Item("ga4", "GA4 measurement ID", WARN, "No GA4 property seen loading or sending hits (may load only after consent).", [], False))

    # 10. Meta Pixel
    mp = tags["meta_pixel"]
    items.append(Item("meta_pixel", "Meta Pixel", PASS if mp["loaded"] else INFO,
                      f"loaded, pixel id(s): {', '.join(mp['pixel_ids']) or 'not seen'}" if mp["loaded"] else "Not seen (optional; may load after consent).", [], False))

    # 11. Consent banner
    if tags["consent"]:
        items.append(Item("consent_banner", "Cookie consent tool", PASS, ", ".join(c["name"] for c in tags["consent"]), [c["evidence"] for c in tags["consent"]][:2], False))
    else:
        items.append(Item("consent_banner", "Cookie consent tool", INFO,
                          "No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup.", [], False))

    # 12. Other donation platforms
    others = facts["other_donation_platforms"]
    if others:
        items.append(Item("other_platforms", "No other donation tool on the page", WARN if installed else INFO,
                          "; ".join(f"{o['name']} ({o['how']})" for o in others), [o["evidence"] for o in others][:3], False))
    else:
        items.append(Item("other_platforms", "No other donation tool on the page", PASS, "None found.", [], False))

    # 13. Speed / general errors
    if reachable:
        lm = page["load_ms"]
        if lm and lm > 6000:
            items.append(Item("page_speed", "Page load under 6 s", WARN, f"load event at {lm/1000:.1f}s", [], False))
        elif lm:
            items.append(Item("page_speed", "Page load under 6 s", PASS, f"load event at {lm/1000:.1f}s", [], False))
        if page["console_error_count"]:
            items.append(Item("console_errors", "Console errors (any source)", INFO,
                              f"{page['console_error_count']} error(s)", [e[:160] for e in page["console_errors_sample"][:3]], False))

        items += agent_items(facts["agent_readiness"])

    return items


def agent_items(ag: dict[str, Any]) -> list[Item]:
    """AI agent readiness: can assistants and AI search read the org and reach the donate page?"""
    from .detect import AI_BOTS

    out: list[Item] = []
    bots = ag["robots"]["bots"]
    blocked = [b for b, s in bots.items() if s == "blocked"]
    fetchers = [b for b in blocked if AI_BOTS[b] != "training"]
    summary = ", ".join(f"{b}: {s}" for b, s in bots.items())
    if fetchers:
        out.append(Item("ai_crawlers", "AI assistants and AI search can read the pages", WARN,
                        f"robots.txt blocks {', '.join(fetchers)} (bots that fetch pages when a person asks an assistant or AI search). {summary}", [], False))
    elif blocked:
        out.append(Item("ai_crawlers", "AI assistants and AI search can read the pages", INFO,
                        f"Only training crawlers are blocked ({', '.join(blocked)}); a policy choice. {summary}", [], False))
    else:
        out.append(Item("ai_crawlers", "AI assistants and AI search can read the pages", PASS,
                        "robots.txt allows all listed AI bots." if ag["robots"]["present"] else "No robots.txt, so no bot is blocked.", [], False))

    out.append(Item("llms_txt", "llms.txt published", PASS if ag["llms_txt"] else INFO,
                    "/llms.txt found." if ag["llms_txt"] else "No /llms.txt (optional, still a proposal).", [], False))

    org, da = ag["organization_markup"], ag["donate_action_markup"]
    if org:
        out.append(Item("structured_data", "schema.org organization markup", PASS,
                        f"JSON-LD types: {', '.join(org)}; DonateAction: {'yes' if da else 'no'}.", [], False))
    else:
        out.append(Item("structured_data", "schema.org organization markup", INFO,
                        f"No Organization/NGO JSON-LD on the home or donate page (types seen: {', '.join(ag['jsonld_types'][:5]) or 'none'}).", [], False))

    dp = ag["donate_page"]
    state = dp["without_javascript"]
    if state is None:
        out.append(Item("donate_no_js", "Donate page readable without JavaScript", INFO, "No donate link found on this page.", [], False))
    elif state == "readable":
        out.append(Item("donate_no_js", "Donate page readable without JavaScript", PASS,
                        f"{dp['url']} returns HTTP {dp['http_status']} with donation content in the HTML.", [dp["url"]], False))
    elif state == "needs_javascript":
        out.append(Item("donate_no_js", "Donate page readable without JavaScript", WARN,
                        f"{dp['url']} returns HTTP {dp['http_status']} but no form, checkout link or install code in the HTML; agents that do not run JavaScript see no way to give.", [dp["url"]], False))
    else:
        out.append(Item("donate_no_js", "Donate page readable without JavaScript", WARN,
                        f"{dp['url']} is blocked or errors for a plain HTTP client (HTTP {dp['http_status']}).", [dp["url"] or ""], False))
    return out


def verdict(items: list[Item], facts: dict[str, Any]) -> dict[str, Any]:
    by_id = {i.id: i for i in items}
    blockers = [i for i in items if i.blocking and i.status == FAIL]
    warns = [i for i in items if i.status == WARN and i.id not in AGENT_IDS]
    if by_id["page_reachable"].status == FAIL:
        status, reason = "unreachable", by_id["page_reachable"].detail
    elif by_id.get("fu_code_in_source") and by_id["fu_code_in_source"].status == FAIL:
        status, reason = "not_installed", "installation code missing"
    elif blockers:
        status, reason = "blocked", "; ".join(b.title for b in blockers)
    elif warns:
        status, reason = "ready_with_warnings", "; ".join(w.title for w in warns)
    else:
        status, reason = "ready", ""
    agent_warns = [i.id for i in items if i.id in AGENT_IDS and i.status == WARN]
    return {"status": status, "reason": reason, "blockers": [b.id for b in blockers], "warnings": [w.id for w in warns],
            "agent_warnings": agent_warns}


def to_dicts(items: list[Item]) -> list[dict[str, Any]]:
    return [asdict(i) for i in items]
