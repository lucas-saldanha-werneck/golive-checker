# https://www.givedirectly.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 8.4s
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
| PASS | Page load under 6 s | load event at 3.8s |
| INFO | Console errors (any source) | 6 error(s) |

## Summary (AI, from the facts above)

The page https://www.givedirectly.org/ loaded in a headless browser with HTTP 200 and no load error. The FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, because the installation code is missing. Google Tag Manager (GTM-PJNMMGH), GA4 (G-GV8XF9FJ16), and Meta Pixel (1507191883453125) were found and loaded. No other donation tool was found on the page. No known cookie consent tool was detected. The page load event was at 3.8 s. The browser recorded 6 console errors, including Content Security Policy errors for inline scripts. The browser did not click any buttons, so checkout and donate behavior was not tested. No checkout form links were found.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The platform cannot run on this page until the code is added. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was detected. Vendor cookies from GTM, GA4, and Meta Pixel may need a consent setup for EU and UK visitors. _(checks: consent_banner)_
- **medium** Content Security Policy errors in console: The browser recorded 6 console errors. Some are Content Security Policy errors that block inline scripts. These may stop the installation code from running once it is added. _(checks: console_errors, fu_code_in_source)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source on https://www.givedirectly.org/. _(checks: fu_code_in_source)_
- [customer] Review the Content Security Policy so the FundraiseUp script is allowed to run. _(checks: console_errors)_
- [customer] Set up a cookie consent tool for EU and UK visitors if required. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer that the installation code has been added, then re-run this check. _(checks: fu_code_in_source, page_reachable)_

### Draft email to the customer

**Subject:** Next steps to install donation tools on givedirectly.org

```text
Hello,

Thank you for working with us to launch donations on your website. We checked https://www.givedirectly.org/ and the page loads correctly. The donation platform code is not on the page yet.

Please do the following:

1. Add the FundraiseUp installation code to the page source on https://www.givedirectly.org/. We will send the code to you separately.
2. Check the Content Security Policy on the site so the donation script is allowed to run. The page currently shows errors about inline scripts being blocked.
3. Set up a cookie consent tool for visitors in the EU and UK, if this applies to you.

Once the code is in place, please let us know and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.givedirectly.org/
- console_errors: Executing inline script violates the following Content Security Policy directive 'script-src 'self' 'nonce-yRVljQwnCGCiwus1qFgOyUx0OT6pcjxF862rkjqQ' *.js.stripe
- console_errors: Executing inline script violates the following Content Security Policy directive 'script-src 'self' 'nonce-yRVljQwnCGCiwus1qFgOyUx0OT6pcjxF862rkjqQ' *.js.stripe
- console_errors: Loading the image 'https://www.linkedin.com/px/li_sync?redirect=https%3A%2F%2Fpx.ads.linkedin.com%2Fcollect%3Fv%3D2%26fmt%3Djs%26pid%3D7359490%26time%3D17951649
