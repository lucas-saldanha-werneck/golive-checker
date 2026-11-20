# https://www.thetrevorproject.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 12.2s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.thetrevorproject.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-K652FKQ |
| PASS | GA4 measurement ID | G-A2ABC2ABCD, G-BD80V9CE2Q, G-DZG3N29WTN |
| PASS | Meta Pixel | loaded, pixel id(s): 249611735914172 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 8.0s |
| INFO | Console errors (any source) | 2 error(s) |

## Summary (AI, from the facts above)

The page loaded (HTTP 200, final URL https://www.thetrevorproject.org/). No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, with one blocker: installation code missing. Tags found: Google Tag Manager container GTM-K652FKQ; GA4 measurement IDs G-A2ABC2ABCD, G-BD80V9CE2Q, G-DZG3N29WTN (hits recorded for G-BD80V9CE2Q and G-DZG3N29WTN); Meta Pixel 249611735914172 loaded. No other donation tool was found. No known cookie consent tool was detected. The page load event took 8.0 seconds, over the 6 second target. The browser did not click any links, so checkout behavior was not tested. Two console errors were recorded, and two requests failed.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The install is not in place on this page. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was detected. Visitors from the EU and UK need a consent setup for vendor cookies. _(checks: consent_banner)_
- **low** Slow page load: The load event fired at 8.0 seconds, over the 6 second target. _(checks: page_speed)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.thetrevorproject.org/, then tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [customer] Set up a cookie consent tool on the site so EU and UK visitors can accept or decline vendor cookies. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer that the installation code was added, then re-run this check. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer whether the cookie consent setup is planned, and note the answer in the account record. _(checks: consent_banner)_

### Draft email to the customer

**Subject:** Next steps to launch your donation page

```text
Hello,

Thank you for working with us to set up online donations. We ran a check on https://www.thetrevorproject.org/. The page loads, but the donation installation code was not found in the page source, so the donation tool is not live yet.

Please do the following:

1. Add the donation installation code to the page source of https://www.thetrevorproject.org/. Our team will send the code to you separately.
2. Set up a cookie consent tool so visitors in the EU and UK can accept or decline vendor cookies.

Once the code is added, please reply to this email so we can re-run the check.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.thetrevorproject.org/
- console_errors: requestStorageAccess: Permission denied.
- console_errors: Failed to load resource: the server responded with a status of 451 ()
