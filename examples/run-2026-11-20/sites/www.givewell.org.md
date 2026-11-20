# https://www.givewell.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 7.7s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.givewell.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-MKLT9TL |
| PASS | GA4 measurement ID | G-5Y1K5KX9ZG |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.1s |
| INFO | Console errors (any source) | 2 error(s) |

## Summary (AI, from the facts above)

The page https://www.givewell.org/ loaded in the headless browser with HTTP 200 and no bot challenge. The load event was at 2.1 seconds. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded at runtime. The verdict is not installed, because the installation code is missing. Google Tag Manager container GTM-MKLT9TL and GA4 measurement ID G-5Y1K5KX9ZG were found. No other donation tool was found on the page. The Meta Pixel was not seen, and no cookie consent tool was detected. The browser recorded 2 console errors and 1 failed request. The browser did not click any buttons, so checkout behavior was not tested. Only links that were found are reported.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The donation widget does not load on this page. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was detected. Visitors from the EU and UK need a consent setup for vendor cookies. _(checks: consent_banner)_
- **low** Console errors and a failed request on the page: The browser recorded 2 console errors: a permissions policy violation for unload, and a 403 response from a resource. One request failed. _(checks: console_errors)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.givewell.org/ and confirm the code is in the served HTML. _(checks: fu_code_in_source)_
- [customer] Confirm whether a cookie consent tool is in use for EU and UK visitors. If one is needed, set it up so vendor cookies wait for consent. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which FundraiseUp account the installation code should use, then re-run this check after the customer updates the page. _(checks: fu_code_in_source, gtm_container, ga4)_
- [onboarding_team] Review the 403 response and the permissions policy message with the customer to see if they affect donation forms. _(checks: console_errors)_

### Draft email to the customer

**Subject:** Next steps to launch donations on givewell.org

```text
Hello,

Thank you for working with us to set up online donations. We checked your homepage at https://www.givewell.org/. The page loads correctly. We did not find the donation installation code on the page yet.

Please do the following:

1. Add the donation installation code to the page source of https://www.givewell.org/. We will send you the exact code and where to place it.
2. Confirm whether you use a cookie consent tool for visitors in the EU and UK. If you do, make sure vendor cookies wait for consent.
3. Let us know if the 403 error on the page is expected. It may affect donation forms.

Once the code is in place, reply to this email and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.givewell.org/
- console_errors: Permissions policy violation: unload is not allowed in this document.
- console_errors: Failed to load resource: the server responded with a status of 403 ()
