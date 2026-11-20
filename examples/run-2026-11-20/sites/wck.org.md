# https://wck.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 14.3s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://wck.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-MKV74FD |
| PASS | GA4 measurement ID | G-5WKVY8503C |
| PASS | Meta Pixel | loaded, pixel id(s): 2145340818891888 |
| PASS | Cookie consent tool | OneTrust |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 9.2s |
| INFO | Console errors (any source) | 1 error(s) |

## Summary (AI, from the facts above)

The page https://wck.org/ loaded in a headless browser with HTTP 200 over HTTPS. The FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, with the installation code missing. Google Tag Manager (GTM-MKV74FD), GA4 (G-5WKVY8503C), and Meta Pixel (2145340818891888) were found. OneTrust was found as the cookie consent tool. No other donation tool was found. The page load event took 9.2 seconds, which is above the 6 second target. The browser recorded one console error, a 451 status response. The browser did not click any buttons, so checkout behavior was not tested. No checkout form links were found.

### Risks

- **high** Installation code is missing: No installation code was found in the page source and no widget request was recorded. The page cannot accept donations through the platform until the code is added. _(checks: fu_code_in_source)_
- **medium** Page load is slow: The load event fired at 9.2 seconds. The check target is under 6 seconds. _(checks: page_speed)_
- **low** Console error on the page: The browser recorded one resource failure with a 451 status. The resource was not identified in the recorded data. _(checks: console_errors)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://wck.org/, then tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm the FundraiseUp account ID with the customer and check it in the dashboard settings once the code is added. _(checks: fu_code_in_source)_
- [customer] Review the page load time and reduce the scripts or assets that slow the load event below 6 seconds. _(checks: page_speed)_
- [onboarding_team] Re-run this check after the customer reports the code is added, and confirm the widget request appears. _(checks: fu_code_in_source, page_speed)_

### Draft email to the customer

**Subject:** Next steps to set up donations on wck.org

```text
Hello,

We checked https://wck.org/ to prepare your donation platform setup. The page loads, but the donation installation code was not found in the page source.

Please do the following:

1. Add the donation installation code to the page source of https://wck.org/. We will send the exact code and placement details separately if you need them.
2. Reduce the page load time. The main page currently takes about 9 seconds to finish loading. Please aim for under 6 seconds.
3. Let us know when the code is live, and we will confirm it.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://wck.org/
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js
- console_errors: Failed to load resource: the server responded with a status of 451 ()
