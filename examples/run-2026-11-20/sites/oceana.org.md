# https://oceana.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:55 UTC in 9.0s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://oceana.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-NGMV83 |
| PASS | GA4 measurement ID | G-05PMM8GBNZ, G-9HNNDLLPKR, G-HT8KYEQFRH |
| PASS | Meta Pixel | loaded, pixel id(s): 1519122081743399 |
| PASS | Cookie consent tool | CookieYes |
| INFO | No other donation tool on the page | Engaging Networks (linked from page) |
| PASS | Page load under 6 s | load event at 4.7s |
| INFO | Console errors (any source) | 3 error(s) |

## Summary (AI, from the facts above)

The page at https://oceana.org/ loaded in the headless browser (HTTP 200, load event at 4.7 s). No FundRaiseUp installation code was found in the page source, and no FundRaiseUp widget request was recorded. The verdict is not installed, with the reason 'installation code missing'. GTM, GA4, Meta Pixel and CookieYes were found on the page. A link to Engaging Networks was found on the page. The browser did not click any buttons, so this check does not say whether any donate or checkout button works. The page had 3 console errors and 1 failed request.

### Risks

- **high** FundRaiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. This is the blocking item for the install. _(checks: fu_code_in_source)_
- **medium** Another donation tool is linked from the page: A link to Engaging Networks was found on the page. The check does not show whether this link is used for donations. _(checks: other_platforms)_
- **low** Console errors on the page: Three console errors were recorded, including one failed network name lookup and scripts refused for MIME type reasons from media6degrees.com. _(checks: console_errors)_

### Next steps

- [onboarding_team] Confirm with the customer whether Engaging Networks is still their active donation tool and whether they plan to move to FundRaiseUp. _(checks: other_platforms)_
- [customer] Add the FundRaiseUp installation code to the page source of https://oceana.org/ as provided during onboarding. _(checks: fu_code_in_source)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is added, and confirm the widget request and installation code appear. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** Next step to install FundRaiseUp on oceana.org

```text
Hello,

Thank you for working with us to set up FundRaiseUp on your website. We checked https://oceana.org/ and the FundRaiseUp installation code was not found in the page source.

Please do the following:

1. Add the FundRaiseUp installation code to the page source of https://oceana.org/. We will send you the code if you do not have it.
2. Let us know once the change is live so we can run the check again.
3. Tell us whether the Engaging Networks donation link on your page is still in use, so we can plan the next steps.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://oceana.org/
- consent_banner: https://cdn-cookieyes.com/client_data/2fb46d9a45eba8b7a4df2e60/script.js
- other_platforms: https://ca-p2p.engagingnetworks.app/24225/diy?ea.tracking.id=waystogive
- console_errors: Failed to load resource: net::ERR_NAME_NOT_RESOLVED
- console_errors: Refused to execute script from 'https://action.media6degrees.com/orbserv/nspix?adv=cl174113446236656&ns=9207&nc=MCOHP&ncv=49' because its MIME type ('image/gif'
- console_errors: Refused to execute script from 'https://action.media6degrees.com/orbserv/nspix?adv=cl174113446236656&ns=9207&nc=MCOAPS&ncv=49' because its MIME type ('image/gif
