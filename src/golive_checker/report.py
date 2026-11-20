"""Markdown / CSV / JSON output for one site and for a batch."""

from __future__ import annotations

import csv
import io
import re
from collections import Counter
from typing import Any
from urllib.parse import urlparse

ICON = {"pass": "PASS", "warn": "WARN", "fail": "FAIL", "info": "INFO"}
STATUS_LABEL = {
    "ready": "Ready",
    "ready_with_warnings": "Ready, with warnings",
    "blocked": "Blocked",
    "not_installed": "Not installed",
    "unreachable": "Could not check",
}


def slug(url: str) -> str:
    p = urlparse(url if "://" in url else "https://" + url)
    s = (p.hostname or "site") + (p.path.rstrip("/") or "")
    return re.sub(r"[^a-zA-Z0-9.-]+", "-", s).strip("-").lower()[:80]


def site_markdown(r: dict[str, Any]) -> str:
    v, facts = r["verdict"], r["facts"]
    fu = facts["fundraiseup"]
    lines = [
        f"# {r['url']}",
        "",
        f"**Status:** {STATUS_LABEL[v['status']]}" + (f" ({v['reason']})" if v["reason"] else ""),
        f"**Checked:** {r['checked_at']} in {facts['page']['check_seconds']}s",
        f"**Account ID(s):** {', '.join(fu['account_ids']) or 'none found'}",
        "",
        "## Checklist",
        "",
        "| Status | Check | Detail |",
        "|---|---|---|",
    ]
    for c in r["checklist"]:
        detail = c["detail"].replace("|", "\\|")
        lines.append(f"| {ICON[c['status']]} | {c['title']} | {detail} |")
    ai = r.get("ai")
    if ai:
        lines += ["", "## Summary (AI, from the facts above)", "", ai["summary"], ""]
        if ai["risks"]:
            lines += ["### Risks", ""]
            for k in ai["risks"]:
                lines.append(f"- **{k['severity']}** {k['title']}: {k['detail']} _(checks: {', '.join(k['check_ids'])})_")
            lines.append("")
        if ai["next_steps"]:
            lines += ["### Next steps", ""]
            for s in ai["next_steps"]:
                lines.append(f"- [{s['owner']}] {s['action']} _(checks: {', '.join(s['check_ids'])})_")
            lines.append("")
        e = ai["customer_email"]
        lines += ["### Draft email to the customer", "", f"**Subject:** {e['subject']}", "", "```text", e["body"].strip(), "```", ""]
    elif r.get("ai_error"):
        lines += ["", f"_AI summary not generated: {r['ai_error']}_", ""]
    ev = [f"- {c['id']}: {x}" for c in r["checklist"] for x in c["evidence"] if x]
    if ev:
        lines += ["## Evidence", ""] + [e.replace("\n", " ")[:300] for e in ev] + [""]
    return "\n".join(lines)


def batch_markdown(results: list[dict[str, Any]], meta: dict[str, Any]) -> str:
    counts = Counter(r["verdict"]["status"] for r in results)
    reasons = Counter()
    installed = [r for r in results if r["verdict"]["status"] not in ("not_installed", "unreachable")]
    titles = {}
    for r in installed:
        for c in r["checklist"]:
            titles[c["id"]] = c["title"]
        for b in r["verdict"]["blockers"] + r["verdict"]["warnings"]:
            reasons[b] += 1
    secs = [r["facts"]["page"]["check_seconds"] or 0 for r in results]
    lines = [
        "# Go-live check: batch summary",
        "",
        f"Run: {meta['started_at']} | sites: {len(results)} | total run time: {meta['wall_seconds']}s | "
        f"median browser check per site: {sorted(secs)[len(secs)//2] if secs else 0}s | AI cost: ${meta.get('ai_cost_usd', 0):.4f}"
        + (f" ({meta['model']})" if meta.get("model") else ""),
        "",
        "| Status | Sites |",
        "|---|---|",
    ]
    for k in STATUS_LABEL:
        if counts.get(k):
            lines.append(f"| {STATUS_LABEL[k]} | {counts[k]} |")
    lines += ["", f"Sites with the widget: {len(installed)}. Checks that failed or warned on them:", "", "| Check | Sites |", "|---|---|"]
    for k, n in reasons.most_common():
        lines.append(f"| {titles.get(k, k)} (`{k}`) | {n} |")
    lines += ["", "| Site | Status | Account | GTM | GA4 | CMP | Other donation tools | Reason | Time |", "|---|---|---|---|---|---|---|---|---|"]
    for r in results:
        f = r["facts"]
        lines.append("| {u} | {s} | {a} | {g} | {ga} | {c} | {o} | {why} | {t}s |".format(
            u=r["url"], s=STATUS_LABEL[r["verdict"]["status"]],
            a=", ".join(f["fundraiseup"]["account_ids"]) or "-",
            g=", ".join(f["tags"]["gtm"]["container_ids"][:2]) or "-",
            ga=", ".join(f["tags"]["ga4"]["measurement_ids"][:2]) or "-",
            c=", ".join(c["name"] for c in f["tags"]["consent"][:1]) or "-",
            o=", ".join(o["name"] for o in f["other_donation_platforms"][:3]) or "-",
            why=(r["verdict"]["reason"] or "-").replace("|", "/")[:120],
            t=f["page"]["check_seconds"],
        ))
    return "\n".join(lines) + "\n"


def batch_csv(results: list[dict[str, Any]]) -> str:
    buf = io.StringIO()
    w = csv.writer(buf)
    w.writerow(["url", "status", "reason", "account_ids", "gtm", "ga4", "meta_pixel", "consent", "other_donation_tools", "load_ms", "check_seconds"])
    for r in results:
        f = r["facts"]
        w.writerow([
            r["url"], r["verdict"]["status"], r["verdict"]["reason"],
            " ".join(f["fundraiseup"]["account_ids"]),
            " ".join(f["tags"]["gtm"]["container_ids"]),
            " ".join(f["tags"]["ga4"]["measurement_ids"]),
            f["tags"]["meta_pixel"]["loaded"],
            " ".join(c["name"] for c in f["tags"]["consent"]),
            "; ".join(o["name"] for o in f["other_donation_platforms"]),
            f["page"]["load_ms"], f["page"]["check_seconds"],
        ])
    return buf.getvalue()
