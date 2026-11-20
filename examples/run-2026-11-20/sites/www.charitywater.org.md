# https://www.charitywater.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 12.2s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.charitywater.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-P6DJRR |
| PASS | GA4 measurement ID | G-SKG6MDYX1T |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| PASS | Cookie consent tool | CookieScript |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 7.6s |

## Summary (AI, from the facts above)

The page https://www.charitywater.org/ loaded in the headless browser with HTTP 200 and no load error. The FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, because the installation code is missing. Google Tag Manager (GTM-P6DJRR), GA4 (G-SKG6MDYX1T), and CookieScript were found. No other donation tool was found. The page load event took 7.6 s, which is over the 6 s target. The Meta Pixel was not seen, which is optional. The browser did not click any buttons, so checkout and donate behavior was not tested. No checkout form links were recorded.

### Risks

- **high** Installation code missing: No installation code was found in the page source and no widget request was recorded. The platform cannot run on this page until the code is added. _(checks: fu_code_in_source)_
- **low** Slow page load: The load event was recorded at 7.6 s, above the 6 s target. This is a warning and does not block installation. _(checks: page_speed)_

### Next steps

- [customer] Add the platform installation code to the page source of https://www.charitywater.org/ and tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [onboarding_team] Re-run this page check after the customer confirms the code is added, and confirm the installation code and widget request appear. _(checks: fu_code_in_source, page_reachable)_
- [onboarding_team] Review the page load time with the customer and confirm whether a slower load is acceptable before launch. _(checks: page_speed)_

### Draft email to the customer

**Subject:** Next step to set up donations on your website

```text
Hello,

Thank you for working with us to set up online donations. We checked https://www.charitywater.org/ and found that the donation platform code is not on the page yet.

Please add the platform installation code to the page source of https://www.charitywater.org/. Once it is added, please let us know so we can run the check again.

We also noticed the page took about 7.6 seconds to finish loading, which is slower than we would like. Please review this with your web team if you can.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.charitywater.org/
- consent_banner: https://cdn.cookie-script.com/s/2d3a4f9c11fdc0c16540dbcd802c5618.js
