# https://www.hrw.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 7.2s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.hrw.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-W5D7ZP |
| PASS | GA4 measurement ID | G-7G2G6XTV4C, G-8G7WH8R2Z8 |
| PASS | Meta Pixel | loaded, pixel id(s): 1179892355551430 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.5s |
| INFO | Console errors (any source) | 2 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| INFO | schema.org organization markup | No Organization/NGO JSON-LD on the home or donate page (types seen: SpeakableSpecification, WebPage). |
| WARN | Donate page readable without JavaScript | https://donate.hrw.org/page/107245/donate/1?ea.tracking.id=EP2022EVpgdonate&promo_id=1000 is blocked or errors for a plain HTTP client (HTTP 403). |

## Summary (AI, from the facts above)

The FundraiseUp installation code was not found on https://www.hrw.org/. The page loaded with HTTP 200 in a headless browser. No FundraiseUp code, widget request, or global object was recorded. Google Tag Manager (GTM-W5D7ZP), two GA4 IDs, and a Meta Pixel were found. The browser did not click anything, so the checkout or donate button was not tested. The donate page at donate.hrw.org returned HTTP 403 to a plain HTTP client, so its content could not be read without JavaScript. Verdict: not installed.

### Risks

- **high** FundraiseUp code is missing from the home page: No installation code was found in the page source, and no widget request was recorded. The verdict is not installed. _(checks: fu_code_in_source)_
- **medium** Donate page blocks plain HTTP clients: The donate page returned HTTP 403 to a plain HTTP client. Its content could not be checked without JavaScript. _(checks: donate_no_js)_
- **low** Content Security Policy blocks two scripts: Two scripts were blocked by the Content Security Policy: bat.bing.com and conversions.digitalwerksautomation.com. Two console errors were recorded. _(checks: console_errors)_
- **low** No consent tool detected: No known cookie consent tool was detected. Vendor cookies need a consent setup for EU and UK visitors. _(checks: consent_banner)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.hrw.org/, then tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [customer] Confirm that the donate page at donate.hrw.org allows plain HTTP requests, or tell the onboarding team if access is blocked on purpose. _(checks: donate_no_js)_
- [onboarding_team] Confirm with the customer which consent tool they use, if any, for EU and UK visitors. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is live. _(checks: fu_code_in_source, page_reachable)_

### Draft email to the customer

**Subject:** FundraiseUp setup for hrw.org: next steps

```text
Hello,

Thank you for working with us on your donation platform setup. We checked https://www.hrw.org/ and could not find the FundraiseUp installation code in the page source. No widget request was recorded.

Please do the following:

1. Add the FundraiseUp installation code to the page source of https://www.hrw.org/.
2. Check that the donate page at https://donate.hrw.org/page/107245/donate/1 is reachable by standard web requests. It returned an access error (HTTP 403) during our check.
3. Let us know which cookie consent tool you use, if any, for visitors in the EU and UK.

Once these changes are live, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.hrw.org/
- console_errors: Loading the script 'https://bat.bing.com/bat.js' violates the following Content Security Policy directive: "script-src 'self' 'report-sample' 'unsafe-inline' 'u
- console_errors: Loading the script 'https://conversions.digitalwerksautomation.com/api/fb.min.js' violates the following Content Security Policy directive: "script-src 'self' '
- donate_no_js: https://donate.hrw.org/page/107245/donate/1?ea.tracking.id=EP2022EVpgdonate&promo_id=1000
