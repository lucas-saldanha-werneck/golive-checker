# https://www.nature.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 09:07 UTC in 8.4s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.nature.org/en-us/ |
| FAIL | Installation code is in the page source | No installation code found in the source and no widget request recorded. |
| WARN | Google Tag Manager container | No GTM container. Checkout events (donation, open, close) reach GA4 through a GTM container template. |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| PASS | Meta Pixel | loaded, pixel id(s): not seen |
| PASS | Cookie consent tool | OneTrust |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 2.4s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| INFO | schema.org organization markup | No Organization/NGO JSON-LD on the home or donate page (types seen: none). |
| PASS | Donate page readable without JavaScript | https://tnc.colabore.org/analytics-test/single_step returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://www.nature.org/en-us/ loaded with HTTP 200 in a headless browser. No FundraiseUp installation code was found in the page source, and no FundraiseUp widget request was recorded. The FundraiseUp global object is not defined at runtime. No Google Tag Manager container and no GA4 measurement ID were seen loading or sending hits. A Meta Pixel and a OneTrust consent tool were found. No other donation tool was found. The browser did not click any buttons, so checkout behavior was not tested. A donate page at https://tnc.colabore.org/analytics-test/single_step returned HTTP 200 with donation content in the HTML. Verdict: not installed, because installation code is missing.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. The verdict is not installed. _(checks: fu_code_in_source)_
- **medium** No Google Tag Manager container seen: No GTM container was found. Checkout events such as donation, open, and close reach GA4 through a GTM container template. _(checks: gtm_container)_
- **medium** No GA4 property seen: No GA4 measurement ID was seen loading or sending hits. GA4 may load only after consent, so this may need a check with consent accepted. _(checks: ga4)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source of https://www.nature.org/en-us/ as provided by the onboarding team. _(checks: fu_code_in_source)_
- [customer] Confirm whether a Google Tag Manager container and a GA4 measurement ID are in use on the site, and share the IDs if so. _(checks: gtm_container, ga4)_
- [onboarding_team] Confirm with the customer which GA4 and GTM setup they use, then re-run this check after the installation code is added. _(checks: fu_code_in_source, gtm_container, ga4)_

### Draft email to the customer

**Subject:** Next steps to connect donations on your website

```text
Hello,

Thank you for working with us to set up online donations. We checked your page at https://www.nature.org/en-us/. The check did not find the donation installation code in the page source, so donations cannot be connected yet.

Please do the following:

1. Add the installation code to the page source. We will send you the code.
2. Share your Google Tag Manager container ID and your GA4 measurement ID, if you use them. If you do not use them, please let us know.

Once these are in place, we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.nature.org/en-us/
- consent_banner: https://cdn.cookielaw.org/scripttemplates/otSDKStub.js
- donate_no_js: https://tnc.colabore.org/analytics-test/single_step
