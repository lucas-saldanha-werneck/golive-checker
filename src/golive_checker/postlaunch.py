"""Day-7 follow-up plan against the vendor's MCP server. DESIGN ONLY, NOT TESTED.

Needs an organization account: the server at https://mcp.fundraiseup.com/org answers
401 without an OAuth token (checked 2026-11-20). Tool names below come from the
public connector listing; their argument names are not confirmed here and must be
read from the server's `tools/list` before any call is made.

This module only builds the list of calls from a scan result. It makes no calls
and returns no data.
"""

from __future__ import annotations

from typing import Any

MCP_URL = "https://mcp.fundraiseup.com/org"


def plan_day7(result: dict[str, Any]) -> list[dict[str, Any]]:
    """Planned MCP calls for one scanned site, each with the question it answers."""
    facts = result["facts"]
    url = facts["page"]["final_url"]
    donate = facts.get("agent_readiness", {}).get("donate_page", {}).get("url")
    pages = [u for u in (url, donate) if u]
    plan = [
        {"tool": "get_donations_stats", "question": "Did the account take live donations since go-live?",
         "inputs": {"period": "since go-live date"}},
        {"tool": "get_insights_timeseries", "question": "Daily donations since go-live: a start, then a gap, points to a broken page or blocked script.",
         "inputs": {"period": "since go-live date", "interval": "day"}},
        {"tool": "get_insights_url", "question": "Do the pages this scan checked appear as donation sources?",
         "inputs": {"pages": pages}},
        {"tool": "get_insights_elements", "question": "Which Elements (buttons, forms, overlays) convert on those pages?",
         "inputs": {"period": "since go-live date"}},
        {"tool": "get_insights_utm", "question": "Do UTM-tagged campaign links show up with source/medium, so attribution works?",
         "inputs": {"period": "since go-live date"}},
        {"tool": "get_insights_agentic_giving", "question": "Are AI-referred donations recorded? Compare with the AI agent readiness checks.",
         "inputs": {"period": "since go-live date"}},
    ]
    return plan
