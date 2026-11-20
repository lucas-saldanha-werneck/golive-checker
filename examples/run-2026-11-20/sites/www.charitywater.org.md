# https://www.charitywater.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 14.3s
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
| WARN | Page load under 6 s | load event at 9.0s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | No robots.txt, so no bot is blocked. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| INFO | schema.org organization markup | No Organization/NGO JSON-LD on the home or donate page (types seen: none). |
| WARN | Donate page readable without JavaScript | https://www.charitywater.org/donate returns HTTP 200 but no form, checkout link or install code in the HTML; agents that do not run JavaScript see no way to give. |

## Summary (AI, from the facts above)

The home page at https://www.charitywater.org/ loaded in the headless browser with HTTP 200 and HTTPS. FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request or global object was recorded. The page load event took 9.0 s, which is above the 6 s target. Google Tag Manager (GTM-P6DJRR), GA4 (G-SKG6MDYX1T) and CookieScript were found. Meta Pixel was not seen, which is optional. The /donate page returned HTTP 200 but no form, checkout link or install code was found in the HTML without JavaScript. The browser did not click any buttons, so checkout behavior was not tested. Overall status is not installed because the installation code is missing.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The verdict is not installed. _(checks: fu_code_in_source)_
- **medium** Donate page has no HTML donation path: The /donate page returned HTTP 200 but its HTML had no form, checkout link or install code. Clients that do not run JavaScript see no way to give there. _(checks: donate_no_js)_
- **low** Slow page load: The load event was recorded at 9.0 s, above the 6 s target. _(checks: page_speed)_

### Next steps

- [customer] Add the FundraiseUp installation code to the home page source, in the head section, then tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [customer] Check that the /donate page includes a donation form or a donation link in its HTML, not only after JavaScript runs. _(checks: donate_no_js)_
- [customer] Review the page load time and reduce the load event time below 6 s. _(checks: page_speed)_
- [onboarding_team] Re-run this check after the customer confirms the installation code is live. _(checks: fu_code_in_source, page_speed, donate_no_js)_

### Draft email to the customer

**Subject:** Next steps to finish your donation page setup

```text
Hello,

Thank you for working with us on your online donation setup. We checked your website, and the donation platform code is not on the home page yet.

Please make these changes:

1. Add the donation platform installation code to the head section of your home page. We will send you the exact code.
2. Check that your /donate page includes a visible donation form or donation link in its HTML, so it works without JavaScript.
3. Reduce the home page load time to under 6 seconds. It currently takes about 9 seconds.

Please let us know when the code is live. We will run the check again after that.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.charitywater.org/
- consent_banner: https://cdn.cookie-script.com/s/2d3a4f9c11fdc0c16540dbcd802c5618.js
- donate_no_js: https://www.charitywater.org/donate
