import json
from types import SimpleNamespace

from golive_checker import cli, llm, report
from golive_checker.cli import evaluate


class FakeMessages:
    def __init__(self, parsed):
        self.parsed = parsed
        self.kwargs = None

    def parse(self, **kwargs):
        self.kwargs = kwargs
        return SimpleNamespace(stop_reason="end_turn", parsed_output=self.parsed,
                               usage=SimpleNamespace(input_tokens=3000, output_tokens=500))


def fake_report(**over):
    data = {
        "summary": "Code is installed in the head and loads.",
        "risks": [
            {"title": "real", "severity": "low", "detail": "d", "check_ids": ["ga4", "made_up"]},
            {"title": "invented", "severity": "high", "detail": "d", "check_ids": ["stripe_setup"]},
        ],
        "next_steps": [{"owner": "customer", "action": "x", "check_ids": ["gtm_container"]}],
        "customer_email": {"subject": "s", "body": "b"},
    }
    data.update(over)
    return llm.AIReport.model_validate(data)


def test_generate_drops_uncited_claims_and_counts_cost(good_cap):
    r = evaluate(good_cap, use_ai=False, model=llm.DEFAULT_MODEL)
    fake = SimpleNamespace(messages=FakeMessages(fake_report()))
    ai = llm.generate(r["facts"], r["checklist"], r["verdict"], client=fake)
    assert [k["title"] for k in ai["risks"]] == ["real"]
    assert ai["risks"][0]["check_ids"] == ["ga4"]
    assert ai["_dropped_uncited"] == 1
    assert ai["_usage"]["cost_usd"] == round((3000 * 0.10 + 500 * 0.50) / 1e6, 5)
    sent = fake.messages.kwargs
    assert sent["model"] == "claude-haiku-5-5"
    assert sent["output_format"] is llm.AIReport
    payload = json.loads(sent["messages"][0]["content"].split("\n", 1)[1])
    assert {c["id"] for c in payload["checklist"]} >= {"fu_code_in_source", "ga4"}
    assert "raw_html" not in json.dumps(payload)


def test_site_markdown_and_batch_outputs(good_cap):
    r = evaluate(good_cap, use_ai=False, model="x")
    md = report.site_markdown(r)
    assert "**Status:** Ready" in md and "| PASS | Installation code is in the page source |" in md
    summary = report.batch_markdown([r], {"started_at": "now", "wall_seconds": 1.0})
    assert "| Ready | 1 |" in summary and "ABCDEFGH" in summary
    assert report.batch_csv([r]).splitlines()[1].startswith("https://example.org/,ready,")


def test_cli_replay_offline(tmp_path, good_cap, monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    cap_file = tmp_path / "cap.json"
    cap_file.write_text(json.dumps(good_cap))
    out = tmp_path / "out"
    assert cli.main(["--replay", str(cap_file), "--out", str(out)]) == 0
    assert (out / "summary.md").exists()
    assert (out / "sites" / "example.org.json").exists()
    assert json.loads((out / "sites" / "example.org.json").read_text())["verdict"]["status"] == "ready"


def test_read_urls_from_csv(tmp_path):
    f = tmp_path / "s.csv"
    f.write_text("url,name\nexample.org,Ex\n# comment\nhttps://b.org/donate,B\nexample.org,dup\n")
    args = SimpleNamespace(urls=[], csv=str(f))
    assert cli.read_urls(args) == ["https://example.org", "https://b.org/donate"]


def test_day7_plan_lists_calls_only(good_cap):
    from golive_checker import postlaunch

    r = evaluate(good_cap, use_ai=False, model="x")
    plan = postlaunch.plan_day7(r)
    assert [p["tool"] for p in plan] == ["get_donations_stats", "get_insights_timeseries", "get_insights_url",
                                         "get_insights_elements", "get_insights_utm", "get_insights_agentic_giving"]
    assert plan[2]["inputs"]["pages"] == ["https://example.org/"]
