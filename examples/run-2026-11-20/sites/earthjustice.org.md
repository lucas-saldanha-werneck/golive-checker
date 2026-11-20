# https://earthjustice.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 5.5s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://earthjustice.org/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| PASS | Google Tag Manager container | GTM-MXDNZTW |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| PASS | Cookie consent tool | Civic Cookie Control |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 0.9s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| PASS | llms.txt published | /llms.txt found. |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| WARN | Donate page readable without JavaScript | https://act.earthjustice.org/a/givetoday?ms=web_menu_header is blocked or errors for a plain HTTP client (HTTP 403). |

## Summary (AI, from the facts above)

The page https://earthjustice.org/ loaded in the headless browser with HTTP 200 and no load errors. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request or runtime global was recorded. The verdict is not installed. Google Tag Manager container GTM-MXDNZTW was found. No GA4 measurement ID was seen loading or sending hits, which may be because it loads only after consent. Civic Cookie Control was found as the consent tool. No other donation tool was found. The donate page at act.earthjustice.org returned HTTP 403 to a plain HTTP client without JavaScript, so it could not be read. The browser did not click any buttons, so checkout and donate button behavior was not tested. No checkout form links were recorded.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. This is a blocker for launch. _(checks: fu_code_in_source)_
- **medium** GA4 measurement ID not seen: No GA4 property was seen loading or sending hits. It may load only after cookie consent, so this needs confirmation. _(checks: ga4)_
- **medium** Donate page blocked for plain HTTP clients: The donate page returned HTTP 403 without JavaScript. The page could not be checked for readable donation content. _(checks: donate_no_js)_

### Next steps

- [customer] Add the FundraiseUp installation code to the website pages where donations are offered, then tell the onboarding team. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer whether GA4 is installed and whether it loads only after consent. _(checks: ga4)_
- [onboarding_team] Confirm with the customer that the donate page at act.earthjustice.org is meant to be reachable by automated clients, then re-run this check after the installation code is added. _(checks: donate_no_js, fu_code_in_source)_

### Draft email to the customer

**Subject:** Next steps to finish your donation platform setup

```text
Hello,

Thank you for working with us to launch online donations on your website. We ran a check on https://earthjustice.org/ and found that the donation platform code is not yet on the page.

To finish setup, please add the FundraiseUp installation code to the pages where you want donation forms to appear. Once it is added, please let us know so we can run the check again.

We also could not read your donate page at act.earthjustice.org from an automated check. It returned an access block. Please let us know if this page is meant to be public, and if any access rules apply to it.

Please also confirm whether your Google Analytics 4 property is set up and whether it loads only after visitors accept cookies.

Thank you. Please reply with any questions.

Best regards,
Onboarding Team
```

## Evidence

- page_reachable: https://earthjustice.org/
- consent_banner: https://cc.cdn.civiccomputing.com/9/cookieControl-9.x.min.js
- donate_no_js: https://act.earthjustice.org/a/givetoday?ms=web_menu_header
