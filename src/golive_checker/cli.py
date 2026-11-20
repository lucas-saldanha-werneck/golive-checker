"""golive-checker: check donation-widget installs on one site or a list of sites."""

from __future__ import annotations

import argparse
import asyncio
import csv
import gzip
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from . import checklist as ck
from . import detect, report


def evaluate(cap: dict[str, Any], use_ai: bool, model: str) -> dict[str, Any]:
    facts = detect.analyze(cap)
    items = ck.build_checklist(facts)
    verdict = ck.verdict(items, facts)
    result = {
        "url": cap["url"],
        "checked_at": datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        "verdict": verdict,
        "checklist": ck.to_dicts(items),
        "facts": facts,
    }
    if use_ai:
        from . import llm

        try:
            result["ai"] = llm.generate(facts, result["checklist"], verdict, model=model)
        except Exception as e:  # report still useful without the AI part
            result["ai_error"] = f"{type(e).__name__}: {str(e)[:200]}"
    return result


def read_urls(args) -> list[str]:
    urls = list(args.urls)
    if args.csv:
        with open(args.csv, newline="") as fh:
            rows = list(csv.reader(fh))
        if rows and rows[0] and rows[0][0].strip().lower() in ("url", "website", "site"):
            rows = rows[1:]
        urls += [r[0].strip() for r in rows if r and r[0].strip() and not r[0].startswith("#")]
    out = []
    for u in urls:
        u = u if "://" in u else "https://" + u
        if u not in out:
            out.append(u)
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(prog="golive-checker", description=__doc__)
    ap.add_argument("urls", nargs="*", help="page URLs to check")
    ap.add_argument("--csv", help="CSV file with one URL per row (first column)")
    ap.add_argument("--replay", nargs="+", metavar="CAPTURE", help="re-run the checks on saved capture files instead of opening pages")
    ap.add_argument("--out", default="out", help="output folder (default: out)")
    ap.add_argument("--concurrency", type=int, default=3)
    ap.add_argument("--timeout", type=float, default=45.0, help="seconds per page load")
    ap.add_argument("--no-ai", action="store_true", help="skip the LLM summary and email draft")
    ap.add_argument("--model", default=None, help="Anthropic model id (default: claude-haiku-5-5)")
    ap.add_argument("--save-captures", action="store_true", help="save raw captures (gzip JSON) for replay")
    args = ap.parse_args(argv)

    use_ai = not args.no_ai
    if use_ai and not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY not set: running without the AI summary (--no-ai).", file=sys.stderr)
        use_ai = False
    from .llm import DEFAULT_MODEL
    model = args.model or DEFAULT_MODEL

    out = Path(args.out)
    (out / "sites").mkdir(parents=True, exist_ok=True)
    started = time.monotonic()
    started_at = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC")

    if args.replay:
        caps = []
        for p in args.replay:
            opener = gzip.open if p.endswith(".gz") else open
            with opener(p, "rt") as fh:
                caps.append(json.load(fh))
    else:
        urls = read_urls(args)
        if not urls:
            ap.error("give at least one URL, --csv or --replay")
        from .capture import capture_many

        def progress(cap):
            print(f"  captured {cap['url']} ({cap['timing'].get('check_seconds')}s){' ERROR ' + cap['error'] if cap['error'] else ''}", file=sys.stderr)

        print(f"Checking {len(urls)} site(s), concurrency {args.concurrency}...", file=sys.stderr)
        caps = asyncio.run(capture_many(urls, concurrency=args.concurrency, timeout_s=args.timeout, on_done=progress))
        if args.save_captures:
            (out / "captures").mkdir(exist_ok=True)
            for c in caps:
                with gzip.open(out / "captures" / f"{report.slug(c['url'])}.json.gz", "wt") as fh:
                    json.dump(c, fh)

    from concurrent.futures import ThreadPoolExecutor

    with ThreadPoolExecutor(max_workers=4) as pool:  # LLM calls are I/O bound
        results = list(pool.map(lambda c: evaluate(c, use_ai, model), caps))
    for r in results:
        name = report.slug(r["url"])
        (out / "sites" / f"{name}.md").write_text(report.site_markdown(r))
        (out / "sites" / f"{name}.json").write_text(json.dumps(r, indent=2, ensure_ascii=False))
        print(f"{report.STATUS_LABEL[r['verdict']['status']]:<22} {r['url']}  {r['verdict']['reason'][:90]}")

    cost = sum((r.get("ai") or {}).get("_usage", {}).get("cost_usd", 0) for r in results)
    meta = {"started_at": started_at, "wall_seconds": round(time.monotonic() - started, 1), "ai_cost_usd": round(cost, 5), "model": model if use_ai else None}
    (out / "summary.md").write_text(report.batch_markdown(results, meta))
    (out / "summary.csv").write_text(report.batch_csv(results))
    (out / "run.json").write_text(json.dumps(meta, indent=2))
    print(f"\nWrote {out}/summary.md, summary.csv and {len(results)} site report(s) in {out}/sites/. AI cost ${cost:.4f}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
