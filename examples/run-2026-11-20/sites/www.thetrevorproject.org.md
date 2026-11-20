# https://www.thetrevorproject.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 13.4s
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
| WARN | Page load under 6 s | load event at 7.5s |
| INFO | Console errors (any source) | 2 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| WARN | Donate page readable without JavaScript | https://give.thetrevorproject.org/campaign/867704/donate?c_src=UCGOF271150105&c_src2=dt-20261116-28-c-FY27-WEBHeader-Footer-4x-225kMatch-donate-button&utm_medium=fundraising&utm_source=websitebutton6&utm_campaign=yearend is blocked or errors for a plain HTTP client (HTTP 403). |

## Summary (AI, from the facts above)

The page https://www.thetrevorproject.org/ loaded in the headless browser with HTTP 200 in about 7.5 seconds. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed. Google Tag Manager, GA4, and Meta Pixel were found and loaded. No other donation tool was found on the page. The page load time is over the 6 second threshold. A plain HTTP client received HTTP 403 from the linked donate page, so that page could not be read without JavaScript. No consent tool was detected. The browser did not click any buttons, so it did not test whether any checkout or donate button works. Two console errors were recorded.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The verdict is not installed. _(checks: fu_code_in_source)_
- **medium** Page load is slow: The load event was recorded at 7.5 seconds, above the 6 second threshold. _(checks: page_speed)_
- **medium** Donate page returned HTTP 403 to a plain HTTP client: The linked donate page at give.thetrevorproject.org returned HTTP 403 without JavaScript. The browser did not test it with JavaScript enabled, so the cause is not confirmed. _(checks: donate_no_js)_
- **low** No consent tool detected: No known cookie consent tool was detected. Vendor cookies may need a consent setup for EU and UK visitors. _(checks: consent_banner)_

### Next steps

- [onboarding_team] Confirm with the customer that the FundraiseUp installation code is not yet on the page and that they plan to add it. _(checks: fu_code_in_source)_
- [customer] Add the FundraiseUp installation code to the page source so it loads on https://www.thetrevorproject.org/. _(checks: fu_code_in_source)_
- [customer] Check why the donate page at give.thetrevorproject.org returns HTTP 403 to non-browser requests, and confirm it loads for visitors. _(checks: donate_no_js)_
- [onboarding_team] Re-run this check after the customer adds the installation code. _(checks: fu_code_in_source, page_speed)_

### Draft email to the customer

**Subject:** Next steps for installing FundraiseUp on thetrevorproject.org

```text
Hello,

Thank you for working with us on your FundraiseUp launch. We checked https://www.thetrevorproject.org/ in a headless browser. The FundraiseUp installation code was not found in the page source, so the widget is not yet installed.

Please do the following:

1. Add the FundraiseUp installation code to the page source so it loads on https://www.thetrevorproject.org/.
2. Check the donate page at give.thetrevorproject.org. It returned HTTP 403 to our non-browser check. Please confirm it loads normally for visitors.

Once the code is in place, we will run the check again. Please reply if you have questions.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.thetrevorproject.org/
- console_errors: requestStorageAccess: Permission denied.
- console_errors: Failed to load resource: the server responded with a status of 451 ()
- donate_no_js: https://give.thetrevorproject.org/campaign/867704/donate?c_src=UCGOF271150105&c_src2=dt-20261116-28-c-FY27-WEBHeader-Footer-4x-225kMatch-donate-button&utm_medium=fundraising&utm_source=websitebutton6&utm_campaign=yearend
