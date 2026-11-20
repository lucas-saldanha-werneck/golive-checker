# golive-checker

Checks whether a nonprofit's website is ready to take donations through an embedded donation widget, and drafts the go-live checklist and the email to the customer. Works on one URL or a CSV of hundreds.

It currently knows the [Fundraise Up](https://fundraiseup.com/docs/installation/) installation code. This is an independent tool, not affiliated with that company.

## The problem

When a new customer installs a donation widget, someone on the onboarding team has to open the site, view the source, look for the install code, check that it is in `<head>`, check that it is not injected through Google Tag Manager, find the GTM container and GA4 property for checkout tracking, notice the consent banner, notice the old donation form still linked from the menu, and then write to the customer. With hundreds of launches a month, that is a lot of manual checks.

This tool does those checks in a real browser, reports what it found with the evidence, and uses an LLM only to write the summary and the customer email from those findings.

## What it checks

It opens each page in headless Chromium (Playwright), waits for scripts to run, and records the server HTML, the rendered DOM, every network request, console errors, and a few page globals. From that:

| Check | Rule (from the vendor's public install docs) |
|---|---|
| Install code in page source | The code must be in the server HTML. If the widget only appears at runtime, the tool records which script inserted it (Chrome DevTools Protocol initiator): a GTM container, a site plugin, or a consent tool. |
| In `<head>`, last script | Docs ask for the global `<head>`, as the last script. |
| One account ID | Two different account IDs on one page is a launch blocker. |
| Widget loads | `cdn.fundraiseup.com/widget/<ID>` returned 2xx; no failed or CSP-blocked vendor requests. |
| Consent tool releases the widget | If a consent tool (OneTrust, Usercentrics, Cookiebot, ...) inserted the widget, it may not load for visitors who decline cookies. |
| Checkout links | `?form=` links on the page. |
| GTM container, GA4, Meta Pixel | Checkout events reach GA4 through a GTM container template. |
| Other donation tools | Classy, Donorbox, Blackbaud Luminate, Engaging Networks, EveryAction, Givebutter, and 15 more, loaded or linked. |
| Page health | HTTP status, bot challenge, load time, console errors. |
| AI agent readiness | robots.txt rules for AI bots, llms.txt, schema.org JSON-LD, donate page without JavaScript. Reported separately; see below. |

Statuses are set by fixed rules in `checklist.py`. The verdict per site is `ready`, `ready_with_warnings`, `blocked`, `not_installed` or `unreachable`.

The LLM step (`claude-haiku-5-5`, structured output) receives only the recorded facts and the checklist. It returns a summary, risks, next steps and a draft customer email. Every risk and step must cite checklist item ids; entries that cite no real item are dropped before the report is written. It cannot change a status.

## Run it

Python 3.12+ and [uv](https://docs.astral.sh/uv/).

```sh
git clone https://github.com/lucas-saldanha-werneck/golive-checker.git
cd golive-checker
uv sync
uv run playwright install chromium

# one site, no LLM
uv run golive-checker https://www.rainforesttrust.org/ --no-ai

# a batch, with the summary and email draft (needs ANTHROPIC_API_KEY)
export ANTHROPIC_API_KEY=...
uv run golive-checker --csv examples/sites.csv --concurrency 3 --out out
```

Output in `out/`: `summary.md` and `summary.csv` for the batch, and `sites/<host>.md` + `.json` per site. Add `--save-captures` to keep the raw captures, and `--replay out/captures/*.json.gz` to re-run the checks and the LLM step without opening the pages again.

Without a local browser, use the official Playwright image:

```sh
scripts/run-docker.sh --csv examples/sites.csv --out out
```

Tests (no network; they use hand-made captures and three pages recorded from real sites):

```sh
uv run pytest -q
```

## Example: 19 real sites, 2026-11-20

Full output in [`examples/run-2026-11-20/`](examples/run-2026-11-20/). Seven sites came from a curl search for the vendor's name in homepage HTML; twelve were nonprofits I expected not to use it. The browser found the widget on two of those twelve: `rescue.org` loads it from a site bundle, and `pih.org` has it in `<head>` (curl got HTTP 403 there, the browser did not).

```
Run: 2026-11-20 09:05 UTC | sites: 19 | total run time: 106.6s | median browser check per site: 12.7s | AI cost: $0.0175 (claude-haiku-5-5)

| Status               | Sites |
|----------------------|-------|
| Ready, with warnings | 9     |
| Not installed        | 10    |
```

What the warnings were, on the 9 sites with the widget:

- 3 sites load the widget at runtime instead of from the page source. On `mercyforanimals.org` the recorded initiator is a WordPress plugin file (`mfa-fundraiseup.min.js`), not GTM.
- On `ifaw.org` the widget script was inserted by Usercentrics, so whether it loads depends on consent settings.
- 3 sites have scripts after the install code in `<head>`; 2 have no GTM container; 2 had no GA4 property seen on the page.
- 6 had a load event over 6 s. This run used a shared 4-core server with 3 pages at a time, so treat load times as relative, not as field data.

AI agent readiness across the 19 sites: no site blocks the listed AI bots in robots.txt, 2 publish `llms.txt`, 14 have Organization/NGO JSON-LD, 2 have `DonateAction`, and 8 donate pages either need JavaScript to show any way to give or return 403 to a plain HTTP client (several are hosted donation forms on a subdomain).

Excerpt from [`sites/mercyforanimals.org.md`](examples/run-2026-11-20/sites/mercyforanimals.org.md):

```
| WARN | Installation code is in the page source | Widget loads at runtime but the code is not in the server HTML.
         Inserted by: JavaScript from https://mercyforanimals.org/wp-content/plugins/mfa-blocks-2024/assets/js/
         mfa-fundraiseup/mfa-fundraiseup.min.js?ver=1.0.0 (not a tag manager). ... |
| PASS | Widget script loads                     | HTTP 200, 24 requests to vendor hosts. |
| PASS | Google Tag Manager container            | GTM-K524TFT, GTM-M3LDFJ, GTM-MGT2PJQJ, GTM-YV5D9SSG31 |
```

## AI agent readiness

More donations will start in AI assistants and AI search. A separate section of each report (not part of the go-live verdict) checks whether those agents can read the organization and reach the donate page:

| Check | How |
|---|---|
| AI bots in robots.txt | Python's robots.txt parser on the home and donate URLs for GPTBot, ClaudeBot, Google-Extended (training crawlers: blocking them is a policy choice, reported as info) and Claude-User, OAI-SearchBot, PerplexityBot (fetch pages when a person asks: blocking them is a warning). |
| llms.txt | `/llms.txt` returns 200 with text, not an HTML error page. |
| schema.org markup | JSON-LD on the home page and the donate page: Organization / NGO / NonprofitOrganization, and `DonateAction`. |
| Donate page without JavaScript | The first "Donate"/"Give" link on the page is fetched with a plain HTTP client. "Readable" means the HTML has a form, a `?form=` checkout link or the install code; otherwise it needs JavaScript, or it is blocked (4xx / bot challenge). |

## After go-live: close the loop with the vendor's MCP server (design, not tested)

This part is a plan. It has not been run, because it needs an organization account.

The vendor publishes an MCP server for organizations at `https://mcp.fundraiseup.com/org` (listed as a Claude connector). Without a token it answers `401` with `WWW-Authenticate: Bearer resource_metadata=".../.well-known/oauth-protected-resource/org"`, and that metadata names OAuth with scope `mcp` (both checked 2026-11-20). The connector listing names tools including `get_donations_stats`, `get_insights_timeseries`, `get_insights_url`, `get_insights_elements`, `get_insights_utm` and `get_insights_agentic_giving`.

A day-7 check would take each site this tool marked ready and ask:

1. `get_donations_stats`, `get_insights_timeseries`: did live donations start after go-live, and did they keep coming? A start followed by a gap points to a page or script that broke.
2. `get_insights_url`: do the exact pages this tool scanned show up as donation sources? A ready page with no donations is worth a look.
3. `get_insights_elements`: which Elements (buttons, forms, overlays) convert on those pages, to suggest the next one to add.
4. `get_insights_utm`: do UTM-tagged campaign links arrive with source and medium, so attribution works end to end.
5. `get_insights_agentic_giving`: are AI-referred donations recorded, and do sites that pass the AI agent readiness checks get more of them?

[`postlaunch.py`](src/golive_checker/postlaunch.py) builds that list of calls for a scan result. It makes no calls and returns no data; argument names must be read from the server's `tools/list` first.

## Limits

- It checks the URLs you give it, one page each. It does not crawl the site, so a code missing on the donate page but present on the homepage is not caught unless you list both.
- It only sees what loads for a first-time visitor in a US-English headless browser with no consent given. Tags that wait for consent are reported as missing, with that caveat.
- Sites behind Cloudflare or similar bot protection can return a challenge page; those are reported as "Could not check", not as "not installed". The same site can pass one run and be challenged the next (`pih.org` did this during testing).
- It does not click donate buttons or open the checkout, and it cannot see dashboard settings (Stripe, campaigns, emails, Apple Pay domain). The go-live checklist covers only what is visible on the page.
- "Who inserted the widget" relies on Chromium's initiator data; it is missing for some requests.
- The tag detection uses URL and HTML signatures. A self-hosted GTM or a renamed consent script will be missed.
- The donate page for the agent checks is the first link that reads like a donate button. On some sites that is not the main donate page (on `nature.org` it was a regional form).
- "Readable without JavaScript" is an HTML heuristic. It does not prove an agent can complete a donation.
- The LLM text is a draft for a person to review before sending.
