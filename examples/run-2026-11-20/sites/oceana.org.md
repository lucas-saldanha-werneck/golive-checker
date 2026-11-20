# https://oceana.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 7.8s
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
| PASS | Page load under 6 s | load event at 3.4s |
| INFO | Console errors (any source) | 3 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://oceana.org/resources/ways-to-give-donate-now/ returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://oceana.org/ loaded over HTTPS with HTTP 200 in a headless browser. The FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request was recorded. The verdict status is not_installed, with the reason that installation code is missing. Google Tag Manager container GTM-NGMV83 was found, three GA4 measurement IDs were found, and the Meta Pixel was loaded. CookieYes was found as the consent tool. Engaging Networks is linked from the page, with a link to a waystogive page. The donate page at https://oceana.org/resources/ways-to-give-donate-now/ returns HTTP 200 with donation content in the HTML. The browser did not click any buttons, so this check does not show whether any checkout or donate button works. Three console errors were recorded, and one request failed to resolve.

### Risks

- **high** FundraiseUp installation code is missing: No FundraiseUp snippet or widget request was recorded on the page. The verdict is not_installed. _(checks: fu_code_in_source)_
- **medium** Donation links point to another platform: Engaging Networks is linked from the page with a waystogive tracking parameter. This check did not confirm how the links are used. _(checks: other_platforms)_
- **low** Console errors were recorded: Three console errors were recorded, including a name resolution failure and two refused scripts from media6degrees.com. _(checks: console_errors)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://oceana.org/ and confirm it loads on the page. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer whether the Engaging Networks links on the page are still in use and whether they should remain after FundraiseUp is installed. _(checks: other_platforms)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is added. _(checks: fu_code_in_source)_

### Draft email to the customer

**Subject:** Next steps to set up donations on oceana.org

```text
Hello,

Thank you for working with us on your online donation setup. We checked https://oceana.org/ and the installation code for the donation platform is not in the page source yet.

Please add the installation code to the page at https://oceana.org/ so it loads on the page. Once it is added, let us know and we will run the check again.

We also found links to Engaging Networks on the page. Please tell us whether those links should stay in place.

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
- donate_no_js: https://oceana.org/resources/ways-to-give-donate-now/
