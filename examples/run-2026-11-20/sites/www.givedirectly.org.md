# https://www.givedirectly.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 10.0s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.givedirectly.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-PJNMMGH |
| PASS | GA4 measurement ID | G-GV8XF9FJ16 |
| PASS | Meta Pixel | loaded, pixel id(s): 1507191883453125 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.9s |
| INFO | Console errors (any source) | 6 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: yes. |
| WARN | Donate page readable without JavaScript | https://donate.givedirectly.org/ returns HTTP 200 but no form, checkout link or install code in the HTML; agents that do not run JavaScript see no way to give. |

## Summary (AI, from the facts above)

The page https://www.givedirectly.org/ loaded in a headless browser with HTTP 200 in about 2.9 seconds. No FundRaiseUp installation code was found in the page source, and no widget request was recorded. The verdict is not installed. GTM, GA4 and the Meta Pixel were detected. No other donation tool was found. The donate page at https://donate.givedirectly.org/ returned HTTP 200 but contained no form, checkout link or install code in its HTML without JavaScript. The browser did not click any buttons, so checkout behavior was not tested.

### Risks

- **high** FundRaiseUp is not installed on the main page: No installation code was found in the page source and no widget request was recorded. This is a blocking item. _(checks: fu_code_in_source)_
- **medium** Donate page has no readable donation path without JavaScript: https://donate.givedirectly.org/ returned HTTP 200, but its HTML had no form, checkout link or install code. Agents that do not run JavaScript cannot see a way to give. _(checks: donate_no_js)_
- **low** Console errors include CSP violations: Six console errors were recorded. Some are Content Security Policy violations on inline scripts that mention stripe. The cause was not determined. _(checks: console_errors)_
- **low** No cookie consent tool detected: No known consent tool was found. Visitors from the EU and UK may need a consent setup for vendor cookies. _(checks: consent_banner)_

### Next steps

- [customer] Add the FundRaiseUp installation code to the main page source, in the head section of https://www.givedirectly.org/. _(checks: fu_code_in_source)_
- [customer] Make the donate page at https://donate.givedirectly.org/ show its donation form or a checkout link in the HTML, so it works without JavaScript. _(checks: donate_no_js)_
- [customer] Review the Content Security Policy so inline scripts for the donation tool are allowed. _(checks: console_errors)_
- [onboarding_team] Confirm with the customer whether a cookie consent tool is in place for EU and UK visitors. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is added. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** Next steps to add donations to your website

```text
Hello,

Thank you for working with us on your online donation setup. We checked your main page at https://www.givedirectly.org/. The page loads well, and your analytics and Meta Pixel are in place. The donation tool is not installed yet.

To finish the setup, please:

1. Add the donation tool installation code to the head section of https://www.givedirectly.org/.
2. Update https://donate.givedirectly.org/ so the donation form or a checkout link appears in the page HTML, not only after JavaScript runs.
3. Ask your web developer to review the Content Security Policy so the donation tool's inline scripts are allowed. Our check recorded errors about this.

Once these changes are live, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.givedirectly.org/
- console_errors: Executing inline script violates the following Content Security Policy directive 'script-src 'self' 'nonce-12vuhIfaHKaD8190BymPpZCf1DWZwU5uwSVOzFZJ' *.js.stripe
- console_errors: Executing inline script violates the following Content Security Policy directive 'script-src 'self' 'nonce-12vuhIfaHKaD8190BymPpZCf1DWZwU5uwSVOzFZJ' *.js.stripe
- console_errors: Loading the image 'https://www.linkedin.com/px/li_sync?redirect=https%3A%2F%2Fpx.ads.linkedin.com%2Fcollect%3Fv%3D2%26fmt%3Djs%26pid%3D7359490%26time%3D17951655
- donate_no_js: https://donate.givedirectly.org/
