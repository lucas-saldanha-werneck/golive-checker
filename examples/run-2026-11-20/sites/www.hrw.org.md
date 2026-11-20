# https://www.hrw.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:55 UTC in 7.7s
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
| PASS | Page load under 6 s | load event at 3.3s |
| INFO | Console errors (any source) | 2 error(s) |

## Summary (AI, from the facts above)

The page https://www.hrw.org/ loaded in the headless browser (HTTP 200, load event at 3.3s). No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The FundraiseUp global object is not defined. The browser did not click anything, so no checkout or donate button was tested. Google Tag Manager container GTM-W5D7ZP, GA4 IDs G-7G2G6XTV4C and G-8G7WH8R2Z8, and Meta Pixel 1179892355551430 were found. No other donation tool was found. No known cookie consent tool was detected. Two console errors were recorded, both Content Security Policy blocks on third-party scripts (bat.bing.com and conversions.digitalwerksautomation.com). Verdict: not installed, because installation code is missing.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The verdict is not installed. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was detected. Consent is needed for EU and UK visitors, and vendor cookies need a consent setup. _(checks: consent_banner)_
- **low** Content Security Policy blocks two third-party scripts: The browser recorded two CSP errors blocking bat.bing.com and conversions.digitalwerksautomation.com scripts. The cause was not checked. _(checks: console_errors)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.hrw.org/. Make sure it is in the head of the page. _(checks: fu_code_in_source)_
- [customer] Set up a cookie consent tool for EU and UK visitors, and make sure vendor cookies respect it. _(checks: consent_banner)_
- [customer] Review the Content Security Policy on the site so the Bing and Meta scripts are allowed or removed, if they are needed. _(checks: console_errors)_
- [onboarding_team] Confirm with the customer that the installation code change is live, then re-run this check. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** Next steps for installing FundraiseUp on hrw.org

```text
Hello,

Thank you for working with us to set up donations on your site. We checked https://www.hrw.org/ and found that the FundraiseUp installation code is not in the page source yet.

Please make these changes:

1. Add the FundraiseUp installation code to the head of the page at https://www.hrw.org/. We will send you the exact code to copy.
2. Set up a cookie consent tool for visitors in the EU and UK, and make sure vendor cookies respect the visitor's choice.
3. Review your Content Security Policy. Two third-party scripts, bat.bing.com and conversions.digitalwerksautomation.com, are being blocked. Allow them or remove them if you no longer use them.

Once these are done, let us know and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.hrw.org/
- console_errors: Loading the script 'https://bat.bing.com/bat.js' violates the following Content Security Policy directive: "script-src 'self' 'report-sample' 'unsafe-inline' 'u
- console_errors: Loading the script 'https://conversions.digitalwerksautomation.com/api/fb.min.js' violates the following Content Security Policy directive: "script-src 'self' '
