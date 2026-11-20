from conftest import GTM_HEAD, GTM_JS, WIDGET, make_cap, req, snippet

from golive_checker import checklist as ck
from golive_checker import detect


def run(cap):
    facts = detect.analyze(cap)
    items = ck.build_checklist(facts)
    return facts, {i.id: i for i in items}, ck.verdict(items, facts)


def test_good_install_is_ready(good_cap):
    facts, items, v = run(good_cap)
    fu = facts["fundraiseup"]
    assert fu["installed_in_source"] and fu["in_head"]
    assert fu["account_ids"] == ["ABCDEFGH"]
    assert fu["scripts_after_in_head"] == 0
    assert fu["checkout_form_links"] == ["spring2026"]
    assert facts["tags"]["gtm"]["container_ids"] == ["GTM-ABC1234"]
    assert facts["tags"]["ga4"]["measurement_ids"] == ["G-TEST12345"]
    assert [c["name"] for c in facts["tags"]["consent"]] == ["OneTrust"]
    assert items["fu_widget_loads"].status == ck.PASS


def test_good_install_has_no_warnings(good_cap):
    _, items, v = run(good_cap)
    assert [i.id for i in items.values() if i.status in (ck.WARN, ck.FAIL)] == []
    assert v["status"] == "ready"


def test_installed_through_gtm_is_flagged():
    cap = make_cap(raw_head=GTM_HEAD, rendered_extra=snippet(), requests=[req(GTM_JS), req(WIDGET)])
    facts, items, v = run(cap)
    assert not facts["fundraiseup"]["installed_in_source"]
    assert facts["fundraiseup"]["loaded_at_runtime"]
    assert items["fu_code_in_source"].status == ck.WARN
    assert "tag manager" in items["fu_code_in_source"].detail
    assert v["status"] == "ready_with_warnings"


def test_code_in_body_and_not_last_script():
    cap = make_cap(raw_head=snippet() + "<script src='/late.js'></script>", requests=[req(WIDGET)])
    _, items, _ = run(cap)
    assert items["fu_in_head"].status == ck.WARN and "1 <script>" in items["fu_in_head"].detail
    cap = make_cap(raw_body=snippet(), requests=[req(WIDGET)])
    facts, items, _ = run(cap)
    assert not facts["fundraiseup"]["in_head"]
    assert "body" in items["fu_in_head"].detail


def test_two_accounts_blocks_launch():
    cap = make_cap(raw_head=snippet("ABCDEFGH") + snippet("ZZZZYYYY"), requests=[req(WIDGET), req("https://cdn.fundraiseup.com/widget/ZZZZYYYY")])
    facts, items, v = run(cap)
    assert facts["fundraiseup"]["account_ids"] == ["ABCDEFGH", "ZZZZYYYY"]
    assert items["fu_single_account"].status == ck.FAIL
    assert v["status"] == "blocked"


def test_widget_blocked_by_csp():
    cap = make_cap(
        raw_head=snippet(),
        failed=[{"url": WIDGET, "type": "script", "failure": "net::ERR_BLOCKED_BY_CLIENT"}],
        console=[{"type": "error", "text": "Refused to load the script 'https://cdn.fundraiseup.com/widget/ABCDEFGH' because it violates the following Content Security Policy directive: script-src 'self'"}],
    )
    _, items, v = run(cap)
    assert items["fu_widget_loads"].status == ck.FAIL
    assert items["fu_no_console_errors"].status == ck.FAIL
    assert v["status"] == "blocked"
    assert "fu_widget_loads" in v["blockers"]


def test_code_present_but_never_requested():
    cap = make_cap(raw_head=snippet(), requests=[req("https://example.org/")])
    _, items, v = run(cap)
    assert items["fu_widget_loads"].status == ck.FAIL
    assert v["status"] == "blocked"


def test_site_without_widget_and_with_other_platform():
    cap = make_cap(
        raw_body='<a href="https://give.classy.org/campaign/123">Give</a><script src="https://donorbox.org/widget.js"></script>',
        requests=[req("https://donorbox.org/widget.js")],
    )
    facts, items, v = run(cap)
    names = {o["name"]: o["how"] for o in facts["other_donation_platforms"]}
    assert names == {"Classy (GoFundMe Pro)": "linked from page", "Donorbox": "loaded on page"}
    assert v["status"] == "not_installed"
    assert items["gtm_container"].status == ck.WARN


def test_unreachable_page():
    cap = make_cap(status=None, error="TimeoutError: page.goto: Timeout 45000ms exceeded.")
    cap["raw_html"] = cap["rendered_html"] = ""
    _, items, v = run(cap)
    assert v["status"] == "unreachable"
    assert "Timeout" in v["reason"]
    assert items["fu_code_in_source"].status == ck.INFO
    assert set(items) == {"page_reachable", "fu_code_in_source"}  # no tag findings from a page that did not load


def test_bot_challenge_counts_as_unreachable():
    cap = make_cap(status=403, raw_body="<title>Just a moment...</title>")
    _, _, v = run(cap)
    assert v["status"] == "unreachable"


def test_meta_pixel_and_slow_page():
    cap = make_cap(
        raw_head=snippet(),
        requests=[req(WIDGET), req("https://connect.facebook.net/en_US/fbevents.js"),
                  req("https://www.facebook.com/tr/?id=1234567890&ev=PageView", 200, "image")],
        load_ms=9400,
    )
    facts, items, _ = run(cap)
    assert facts["tags"]["meta_pixel"] == {"loaded": True, "pixel_ids": ["1234567890"]}
    assert items["page_speed"].status == ck.WARN


def test_funraise_is_not_fundraiseup():
    # a different vendor with a similar name must not count as the install
    cap = make_cap(raw_body='<script src="https://assets.funraise.io/widget.js"></script>', requests=[req("https://assets.funraise.io/widget.js")])
    facts, _, v = run(cap)
    assert facts["fundraiseup"]["account_ids"] == []
    assert v["status"] == "not_installed"
    assert [o["name"] for o in facts["other_donation_platforms"]] == ["Funraise"]


def test_initiator_names_the_gtm_container():
    cap = make_cap(raw_head=GTM_HEAD, rendered_extra=snippet(), requests=[req(GTM_JS), req(WIDGET)])
    cap["initiators"] = {WIDGET: {"type": "script", "url": None, "stack_urls": [GTM_JS]}}
    facts, items, _ = run(cap)
    assert facts["fundraiseup"]["inserted_by"]["container"] == "GTM-ABC1234"
    assert "GTM-ABC1234" in items["fu_code_in_source"].detail


def test_initiator_from_site_bundle():
    cap = make_cap(rendered_extra=snippet(), requests=[req(WIDGET)])
    cap["initiators"] = {WIDGET: {"type": "script", "url": None, "stack_urls": ["https://example.org/assets/app.js"]}}
    _, items, _ = run(cap)
    assert "example.org/assets/app.js" in items["fu_code_in_source"].detail
    assert "not a tag manager" in items["fu_code_in_source"].detail


def test_widget_inserted_by_consent_tool_is_flagged():
    cap = make_cap(raw_head=snippet(), requests=[req(WIDGET)])
    cap["initiators"] = {WIDGET: {"type": "script", "url": None, "stack_urls": ["https://web.cmp.usercentrics.eu/ui/v/4.34.0/WebSdk.lib.js"]}}
    _, items, _ = run(cap)
    assert items["fu_consent_gated"].status == ck.WARN
    assert "Usercentrics" in items["fu_consent_gated"].detail


def test_ga4_hit_with_several_properties():
    cap = make_cap(globals_={"google_tag_manager": ["G-AAAA1111;G-BBBB2222"]}, requests=[req("https://www.google-analytics.com/g/collect?v=2&tid=G-AAAA1111;G-BBBB2222&en=page_view", 204, "fetch")])
    facts, _, _ = run(cap)
    assert facts["tags"]["ga4"]["measurement_ids"] == ["G-AAAA1111", "G-BBBB2222"]
