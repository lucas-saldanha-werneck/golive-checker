# https://wck.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 16.9s
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
| WARN | Page load under 6 s | load event at 10.4s |
| INFO | Console errors (any source) | 1 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| WARN | Donate page readable without JavaScript | https://donate.wck.org/campaign/749360/donate?c_src=site-navbar is blocked or errors for a plain HTTP client (HTTP 403). |

## Summary (AI, from the facts above)

The page https://wck.org/ loaded in a headless browser with HTTP 200 and no load error. No installation code was found in the page source, and no widget request was recorded. The verdict is not installed. Google Tag Manager (GTM-MKV74FD), GA4 (G-5WKVY8503C), and the Meta Pixel (2145340818891888) were found. OneTrust is the cookie consent tool. No other donation tool was found. The page took 10.4 s to load its load event, above the 6 s check. One console error was recorded, a 451 status on a resource. The donate link https://donate.wck.org/campaign/749360/donate?c_src=site-navbar returned HTTP 403 to a plain HTTP client. The browser did not click any button, so checkout behavior was not tested. Only the links were found.

### Risks

- **high** Installation code missing from page source: No installation code was found in the source and no widget request was recorded. The install is not present on this page. _(checks: fu_code_in_source)_
- **medium** Page load time above 6 s: The load event was recorded at 10.4 s. _(checks: page_speed)_
- **medium** Donate page returned HTTP 403 to a plain HTTP client: The donate link https://donate.wck.org/campaign/749360/donate?c_src=site-navbar returned HTTP 403 to a plain HTTP client. The check cannot read this page without JavaScript. _(checks: donate_no_js)_
- **low** One console error recorded: A resource returned status 451 during page load. The source of the resource was not identified. _(checks: console_errors)_

### Next steps

- [customer] Add the installation code to the page source of https://wck.org/ and confirm it appears in the head of the page. _(checks: fu_code_in_source)_
- [customer] Review the page load time of https://wck.org/ and reduce the load event time below 6 s. _(checks: page_speed)_
- [customer] Check that https://donate.wck.org/campaign/749360/donate?c_src=site-navbar is reachable for visitors and does not block plain HTTP requests with HTTP 403. _(checks: donate_no_js)_
- [onboarding_team] Confirm with the customer that the installation code was added, then re-run this check. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm the 451 console error source with the customer and note whether it affects donations. _(checks: console_errors)_

### Draft email to the customer

**Subject:** Next steps to finish your donation page setup

```text
Hello,

Thank you for working with us. We checked https://wck.org/ and found that the donation installation code is not in the page yet. Please add the installation code to the page source so it appears in the head of the page. We will confirm once it is in place.

We also found two items to review on your site:

1. The page takes about 10.4 seconds to load. Please review it and aim for under 6 seconds.
2. The donate page at https://donate.wck.org/campaign/749360/donate?c_src=site-navbar returned an access error (HTTP 403) to our check. Please confirm that visitors can open this page.

Once these changes are made, reply to this email and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://wck.org/
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js
- console_errors: Failed to load resource: the server responded with a status of 451 ()
- donate_no_js: https://donate.wck.org/campaign/749360/donate?c_src=site-navbar
