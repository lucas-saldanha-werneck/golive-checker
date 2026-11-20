# https://www.givewell.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 7.7s
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
| PASS | Page load under 6 s | load event at 2.3s |
| INFO | Console errors (any source) | 2 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| INFO | schema.org organization markup | No Organization/NGO JSON-LD on the home or donate page (types seen: none). |
| PASS | Donate page readable without JavaScript | https://secure.givewell.org/ returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page at https://www.givewell.org/ loaded with HTTP 200 in the headless browser. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, because the installation code is missing. Google Tag Manager container GTM-MKLT9TL and GA4 measurement ID G-5Y1K5KX9ZG were found and loaded. No other donation tool was found on the page. The donate page at https://secure.givewell.org/ returned HTTP 200 with donation content in the HTML. The browser did not click any buttons, so checkout behavior was not tested. The page logged 2 console errors and 1 failed request.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. This is the only blocking item. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was detected. Visitors from the EU or UK may need one before vendor cookies are set. _(checks: consent_banner)_
- **low** Console errors and a failed request on the page: The page logged 2 console errors, including a permissions policy violation and a 403 response for one resource. _(checks: console_errors)_

### Next steps

- [customer] Add the FundraiseUp installation code to the website source on the home page and make sure it loads on the page. _(checks: fu_code_in_source)_
- [customer] Decide whether a cookie consent tool is needed for EU and UK visitors, and set one up if so. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which 403 resource and permissions policy issue come from their site. _(checks: console_errors)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is added. _(checks: fu_code_in_source, page_reachable)_

### Draft email to the customer

**Subject:** Next steps to connect your donation platform to givewell.org

```text
Hello,

Thank you for working with us to set up online donations. We checked https://www.givewell.org/ and found that the donation platform code is not on the page yet. Please add the installation code to the source of your home page. We will run the check again once it is in place.

Please also confirm whether you need a cookie consent tool for visitors from the EU or UK. If you do, let us know and we will help you choose a setup.

We also saw two console errors on the page, including a 403 response for one resource. Please check whether this comes from your site.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.givewell.org/
- console_errors: Permissions policy violation: unload is not allowed in this document.
- console_errors: Failed to load resource: the server responded with a status of 403 ()
- donate_no_js: https://secure.givewell.org/
