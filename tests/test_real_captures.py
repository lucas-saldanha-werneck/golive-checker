"""Regression tests on pages recorded from real sites on 2026-11-20 (see examples/).

Captures are gzip JSON written by `golive-checker --save-captures`. No network."""

import gzip
import json
from pathlib import Path

from golive_checker import checklist as ck
from golive_checker import detect

FIX = Path(__file__).parent / "fixtures"


def load(name):
    with gzip.open(FIX / name, "rt") as fh:
        cap = json.load(fh)
    facts = detect.analyze(cap)
    items = ck.build_checklist(facts)
    return facts, {i.id: i for i in items}, ck.verdict(items, facts)


def test_wildaid_install_in_head():
    facts, items, v = load("wildaid.org.json.gz")
    assert facts["fundraiseup"]["account_ids"] == ["AQTMUHNH"]
    assert facts["fundraiseup"]["in_head"] and facts["fundraiseup"]["scripts_after_in_head"] == 0
    assert items["fu_widget_loads"].status == ck.PASS
    assert v["status"] == "ready"


def test_mercyforanimals_widget_added_by_site_plugin_not_gtm():
    facts, items, v = load("mercyforanimals.org.json.gz")
    fu = facts["fundraiseup"]
    assert not fu["installed_in_source"] and fu["loaded_at_runtime"]
    assert fu["inserted_by"]["kind"] == "script"
    assert "mfa-fundraiseup" in fu["inserted_by"]["script"]
    assert items["fu_code_in_source"].status == ck.WARN
    assert v["status"] == "ready_with_warnings"


def test_ifaw_widget_released_by_consent_tool():
    facts, items, _ = load("www.ifaw.org.json.gz")
    assert [c["name"] for c in facts["tags"]["consent"]] == ["Usercentrics"]
    assert items["fu_consent_gated"].status == ck.WARN
    assert items["fu_in_head"].status == ck.WARN  # 3 scripts after the code in <head>
