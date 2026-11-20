"""One LLM call per site: turn the checklist into risks, next steps and a customer email.

The model gets only the recorded facts and the rule-based checklist. It does not
set statuses. Every risk and step must cite checklist item ids; anything that
cites an unknown id is dropped before it reaches the report.
"""

from __future__ import annotations

import json
from typing import Any, Literal

from pydantic import BaseModel, Field

DEFAULT_MODEL = "claude-haiku-5-5"
# USD per million tokens (input, output), prompts under 100K tokens.
PRICES = {"claude-haiku-5-5": (0.10, 0.50), "claude-sonnet-5-5": (2.0, 10.0)}

SYSTEM = """You help an onboarding team launch nonprofit customers on an online donation platform.
You receive facts recorded by a headless browser on one web page and a checklist whose statuses were set by fixed rules.

Rules:
- Use only the facts given. Do not guess about things that were not recorded (Stripe setup, campaigns, emails, other pages).
- Do not change any checklist status.
- Every risk and next step must cite one or more checklist item ids from the input in `check_ids`.
- If the page could not be loaded, say that and do not speculate about the install.
- The browser did not click anything. Do not say the checkout or donate button works; say which links were found.
- Only the customer can change their website. Onboarding-team steps are things like checking dashboard settings, confirming with the customer, or re-running this check.
- Do not promise work on behalf of anyone.
- Plain, short sentences. No marketing words.
- The customer email is a draft for the onboarding manager to review: friendly, under 150 words, lists only concrete fixes the customer must make, and does not mention internal tooling."""


class Risk(BaseModel):
    title: str
    severity: Literal["high", "medium", "low"]
    detail: str
    check_ids: list[str] = Field(min_length=1)


class Step(BaseModel):
    owner: Literal["customer", "onboarding_team"]
    action: str
    check_ids: list[str] = Field(min_length=1)


class Email(BaseModel):
    subject: str
    body: str


class AIReport(BaseModel):
    summary: str
    risks: list[Risk]
    next_steps: list[Step]
    customer_email: Email


def _compact_facts(facts: dict[str, Any]) -> dict[str, Any]:
    """Facts without bulky fields; keeps the prompt small and the cost low."""
    f = json.loads(json.dumps(facts))
    f["page"].pop("console_errors_sample", None)
    f["page"].pop("page_errors_sample", None)
    return f


def generate(facts: dict[str, Any], checklist: list[dict[str, Any]], verdict: dict[str, Any], model: str = DEFAULT_MODEL, client=None) -> dict[str, Any]:
    import anthropic

    client = client or anthropic.Anthropic()
    payload = {"verdict": verdict, "checklist": checklist, "facts": _compact_facts(facts)}
    resp = client.messages.parse(
        model=model,
        max_tokens=4000,
        system=SYSTEM,
        output_config={"effort": "low"},
        messages=[{"role": "user", "content": "Recorded data (JSON):\n" + json.dumps(payload, ensure_ascii=False)}],
        output_format=AIReport,
    )
    if resp.stop_reason == "refusal" or resp.parsed_output is None:
        raise RuntimeError(f"model returned no report (stop_reason={resp.stop_reason})")
    report = resp.parsed_output.model_dump()
    report = drop_unsupported(report, {c["id"] for c in checklist})
    u = resp.usage
    pin, pout = PRICES.get(model, (0.0, 0.0))
    report["_usage"] = {
        "model": model,
        "input_tokens": u.input_tokens,
        "output_tokens": u.output_tokens,
        "cost_usd": round((u.input_tokens * pin + u.output_tokens * pout) / 1e6, 5),
    }
    return report


def drop_unsupported(report: dict[str, Any], valid_ids: set[str]) -> dict[str, Any]:
    """Remove risks/steps that cite no real checklist item; keep only real ids."""
    dropped = 0
    for key in ("risks", "next_steps"):
        kept = []
        for entry in report.get(key, []):
            ids = [i for i in entry.get("check_ids", []) if i in valid_ids]
            if ids:
                entry["check_ids"] = ids
                kept.append(entry)
            else:
                dropped += 1
        report[key] = kept
    report["_dropped_uncited"] = dropped
    return report
