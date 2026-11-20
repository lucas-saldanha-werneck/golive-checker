# https://www.care.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 11.9s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.care.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-WMMPLB |
| PASS | GA4 measurement ID | G-BE6GP7SC1M |
| PASS | Meta Pixel | loaded, pixel id(s): 312340198960624 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| INFO | No other donation tool on the page | Blackbaud Luminate Online (linked from page) |
| WARN | Page load under 6 s | load event at 7.3s |
| INFO | Console errors (any source) | 5 error(s) |

## Summary (AI, from the facts above)

The check loaded https://www.care.org/ in a headless browser (HTTP 200, load time 7.3 s). No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed because the installation code is missing. Google Tag Manager (GTM-WMMPLB), GA4 (G-BE6GP7SC1M), and Meta Pixel (312340198960624) were found. No cookie consent tool was detected. The page links to a Blackbaud Luminate Online donation form. The browser did not click anything, so the donation form and checkout were not tested.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The platform cannot run on this page until the code is added. _(checks: fu_code_in_source)_
- **medium** Donation form links to another platform: The page links to a Blackbaud Luminate Online donation form. Donors may be sent there instead of a FundraiseUp form. _(checks: other_platforms)_
- **low** Page load is slow: The load event was recorded at 7.3 s, above the 6 s target. _(checks: page_speed)_
- **low** No cookie consent tool detected: No known consent tool was found. Visitors in the EU and UK need a consent setup for vendor cookies. _(checks: consent_banner)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.care.org/ and confirm the code is in the page HTML. _(checks: fu_code_in_source)_
- [customer] Tell us whether the Blackbaud Luminate Online donation link on the page should stay, be removed, or be replaced. _(checks: other_platforms)_
- [customer] Set up a cookie consent tool if EU or UK visitors are in scope. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which donation form is intended for the page and whether the Blackbaud link is still in use. _(checks: other_platforms)_
- [onboarding_team] Re-run this check after the customer adds the installation code. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** Next steps to connect your donation form on care.org

```text
Hello,

Thank you for working with us to set up donations on your website. We checked https://www.care.org/ and found that the donation software code is not on the page yet.

Please do the following:

1. Add the donation software installation code to the page source of https://www.care.org/. We will send the code and placement details separately.
2. Let us know whether the Blackbaud Luminate Online donation link on the page should stay, be removed, or be replaced.
3. If you have visitors in the EU or UK, set up a cookie consent tool for them.

Once the code is in place, we will run the check again and confirm the result with you.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.care.org/
- other_platforms: https://my.care.org/site/Donation2?df_id=53752&amp;mfc_pref=T&amp;53752.donation=form1&amp;s_src=1727230NNC00&amp;s_subsrc=FY27DFWEBNOVGAZALB
- console_errors: requestStorageAccess: Permission denied.
- console_errors: requestStorageAccess: Permission denied.
- console_errors: Permissions policy violation: unload is not allowed in this document.
