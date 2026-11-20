# https://www.care.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 12.7s
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
| PASS | Page load under 6 s | load event at 6.0s |
| INFO | Console errors (any source) | 5 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://my.care.org/site/Donation2?df_id=53752&mfc_pref=T&53752.donation=form1&s_src=1727230NNC00&s_subsrc=FY27DFWEBNOVGAZALB returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The FundraiseUp installation code was not found on https://www.care.org/. The page loaded (HTTP 200) in the headless browser. No installation code appeared in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, with the reason: installation code missing. The browser did not click any button, so it did not test whether the donate flow works. Links found: the page links to a Blackbaud Luminate Online donation form at my.care.org. That donation form returned HTTP 200 without JavaScript. Google Tag Manager (GTM-WMMPLB), GA4 (G-BE6GP7SC1M), and the Meta Pixel (312340198960624) were found and loaded. No known cookie consent tool was detected. The page load event was at 6.0 seconds. Five console errors were recorded.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. This blocks the install. _(checks: fu_code_in_source)_
- **medium** Donate links point to another platform: The page links to a Blackbaud Luminate Online donation form, not a FundraiseUp form. The browser did not test whether that form works. _(checks: other_platforms, donate_no_js)_
- **medium** No cookie consent tool detected: No known consent tool was found. Visitors in the EU and UK may need a consent setup for vendor cookies. _(checks: consent_banner)_
- **low** Page load is close to the limit: The load event fired at 6.0 seconds, just over the 6 second target. _(checks: page_speed)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.care.org/ and tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer which donation form should be used on the site, since the page links to a Blackbaud Luminate Online form. _(checks: other_platforms)_
- [customer] Decide whether a cookie consent tool is needed for EU and UK visitors, and add one if so. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the installation code is added. _(checks: fu_code_in_source, page_reachable)_

### Draft email to the customer

**Subject:** Next steps for installing donations on care.org

```text
Hello,

Thank you for working with us on your online donation setup. We checked https://www.care.org/ and found that the donation installation code is not on the page yet.

Please do the following:

1. Add the installation code to the page source of https://www.care.org/. We will send the exact code separately.
2. Let us know which donation form you want visitors to use. The page currently links to a Blackbaud Luminate Online form.
3. If you have visitors in the EU or UK, consider adding a cookie consent tool.

Once the code is live, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.care.org/
- other_platforms: https://my.care.org/site/Donation2?df_id=53752&amp;mfc_pref=T&amp;53752.donation=form1&amp;s_src=1727230NNC00&amp;s_subsrc=FY27DFWEBNOVGAZALB
- console_errors: requestStorageAccess: Permission denied.
- console_errors: requestStorageAccess: Permission denied.
- console_errors: Permissions policy violation: unload is not allowed in this document.
- donate_no_js: https://my.care.org/site/Donation2?df_id=53752&mfc_pref=T&53752.donation=form1&s_src=1727230NNC00&s_subsrc=FY27DFWEBNOVGAZALB
