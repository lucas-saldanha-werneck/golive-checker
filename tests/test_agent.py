"""AI agent readiness checks (robots.txt, llms.txt, JSON-LD, donate page without JS)."""

import json

from conftest import make_cap

from golive_checker import checklist as ck
from golive_checker import detect
from golive_checker.capture import pick_donate_link


def resp(body, status=200, url="https://example.org/x", ctype="text/plain"):
    return {"url": url, "final_url": url, "status": status, "content_type": ctype, "body": body}


def run(cap):
    facts = detect.analyze(cap)
    items = ck.build_checklist(facts)
    return facts, {i.id: i for i in items}, ck.verdict(items, facts)


def with_agent(cap, robots=None, llms=None, donate=None):
    cap["agent"] = {"robots": robots or resp("", 404), "llms": llms or resp("", 404), "donate": donate}
    return cap


def test_blocking_assistant_fetchers_warns():
    robots = resp("User-agent: Claude-User\nDisallow: /\n\nUser-agent: GPTBot\nDisallow: /\n\nUser-agent: *\nAllow: /\n")
    facts, items, _ = run(with_agent(make_cap(), robots=robots))
    bots = facts["agent_readiness"]["robots"]["bots"]
    assert bots["Claude-User"] == "blocked" and bots["GPTBot"] == "blocked"
    assert bots["ClaudeBot"] == "allowed" and bots["PerplexityBot"] == "allowed"
    assert items["ai_crawlers"].status == ck.WARN
    assert "Claude-User" in items["ai_crawlers"].detail.split("(")[0]


def test_blocking_only_training_crawlers_is_info():
    robots = resp("User-agent: GPTBot\nDisallow: /\n\nUser-agent: Google-Extended\nDisallow: /\n")
    _, items, _ = run(with_agent(make_cap(), robots=robots))
    assert items["ai_crawlers"].status == ck.INFO


def test_wildcard_disallow_blocks_everyone_and_no_robots_allows_everyone():
    facts, items, _ = run(with_agent(make_cap(), robots=resp("User-agent: *\nDisallow: /\n")))
    assert set(facts["agent_readiness"]["robots"]["bots"].values()) == {"blocked"}
    assert items["ai_crawlers"].status == ck.WARN
    facts, items, _ = run(with_agent(make_cap()))
    assert facts["agent_readiness"]["robots"]["present"] is False
    assert items["ai_crawlers"].status == ck.PASS


def test_llms_txt_present_vs_html_soft_404():
    _, items, _ = run(with_agent(make_cap(), llms=resp("# Example Org\n> We plant trees.\n")))
    assert items["llms_txt"].status == ck.PASS
    _, items, _ = run(with_agent(make_cap(), llms=resp("<!doctype html><html>Not found</html>", 200, ctype="text/html")))
    assert items["llms_txt"].status == ck.INFO


def test_jsonld_graph_with_ngo_and_donate_action():
    ld = {"@context": "https://schema.org", "@graph": [
        {"@type": "WebSite", "name": "Ex"},
        {"@type": "NGO", "name": "Ex", "potentialAction": {"@type": "DonateAction", "target": "https://example.org/donate"}}]}
    cap = make_cap(raw_head=f'<script type="application/ld+json">{json.dumps(ld)}</script>')
    facts, items, _ = run(with_agent(cap))
    ag = facts["agent_readiness"]
    assert ag["organization_markup"] == ["NGO"] and ag["donate_action_markup"] is True
    assert items["structured_data"].status == ck.PASS and "DonateAction: yes" in items["structured_data"].detail


def test_broken_jsonld_is_ignored():
    cap = make_cap(raw_head='<script type="application/ld+json">{not json</script>')
    _, items, _ = run(with_agent(cap))
    assert items["structured_data"].status == ck.INFO


def test_donate_page_states():
    shell = resp('<html><body><div id="root"></div><script src="/app.js"></script></body></html>', url="https://example.org/donate")
    _, items, _ = run(with_agent(make_cap(), donate=shell))
    assert items["donate_no_js"].status == ck.WARN and "do not run JavaScript" in items["donate_no_js"].detail
    ok = resp('<html><body><a href="?form=spring">Give</a></body></html>', url="https://example.org/donate")
    _, items, _ = run(with_agent(make_cap(), donate=ok))
    assert items["donate_no_js"].status == ck.PASS
    blocked = resp("<title>Just a moment...</title>", 403, url="https://example.org/donate")
    facts, items, _ = run(with_agent(make_cap(), donate=blocked))
    assert facts["agent_readiness"]["donate_page"]["without_javascript"] == "blocked"
    assert items["donate_no_js"].status == ck.WARN
    _, items, _ = run(with_agent(make_cap(), donate=None))
    assert items["donate_no_js"].status == ck.INFO


def test_agent_warnings_do_not_change_go_live_verdict(good_cap):
    _, _, v = run(with_agent(good_cap, robots=resp("User-agent: *\nDisallow: /\n")))
    assert v["status"] == "ready"
    assert v["agent_warnings"] == ["ai_crawlers"]


def test_old_captures_without_agent_data_still_work(good_cap):
    good_cap.pop("agent", None)
    _, items, _ = run(good_cap)
    assert items["donate_no_js"].status == ck.INFO


def test_pick_donate_link():
    links = [{"href": "https://example.org/", "text": "Home"},
             {"href": "https://example.org/about", "text": "About"},
             {"href": "https://example.org/ways-to-give", "text": "Ways to give"},
             {"href": "https://example.org/donate", "text": "Donate now"},
             {"href": "mailto:give@example.org", "text": "Give"}]
    assert pick_donate_link("https://example.org/", links) == "https://example.org/donate"
    assert pick_donate_link("https://example.org/", links[:2]) is None
    # a "Donate" button wins over an article link that mentions donations (seen on a real site)
    links = [{"href": "https://example.org/about/your-donation-at-work", "text": "Your Donation at Work"},
             {"href": "https://act.example.org/a/givetoday", "text": "Donate"}]
    assert pick_donate_link("https://example.org/", links) == "https://act.example.org/a/givetoday"
