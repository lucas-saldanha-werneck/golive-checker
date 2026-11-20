# https://earthjustice.org/

**Status:** Not installed (installation code missing)
**Checked:** 2026-11-20 08:56 UTC in 5.2s
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
| PASS | Page load under 6 s | load event at 0.7s |

## Summary (AI, from the facts above)

The page https://earthjustice.org/ loaded in the headless browser with HTTP 200 and no load error. The FundraiseUp installation code was not found in the page source, and no FundraiseUp widget request was recorded. The verdict is not installed, because the installation code is missing. Google Tag Manager container GTM-MXDNZTW was found in the source and loaded. Civic Cookie Control was found. No GA4 measurement ID was seen loading or sending hits, though GA4 may load only after consent. No Meta Pixel was seen, and it is optional. No other donation tool was found. The browser did not click any buttons, so checkout and donate behavior was not tested. No checkout form links were recorded.

### Risks

- **high** FundraiseUp installation code is missing: No installation code was found in the page source and no widget request was recorded. This blocks the install. _(checks: fu_code_in_source)_
- **low** No GA4 property seen: No GA4 measurement ID loaded or sent hits during the check. The tool may load only after consent, so this needs confirmation. _(checks: ga4)_

### Next steps

- [customer] Add the FundraiseUp installation code to the page source on https://earthjustice.org/, then tell the onboarding team when it is live. _(checks: fu_code_in_source)_
- [onboarding_team] Confirm with the customer whether GA4 is set up and whether it loads only after cookie consent. Then re-run this check. _(checks: ga4)_
- [onboarding_team] Re-run this check on https://earthjustice.org/ after the customer adds the installation code. _(checks: fu_code_in_source, page_reachable)_

### Draft email to the customer

**Subject:** Next step to finish your donation platform setup

```text
Hello,

Thank you for working with us to set up online donations. We checked https://earthjustice.org/ and the page loads fine. However, we did not find the donation platform installation code in the page source yet.

To finish setup, please add the installation code to the page source of https://earthjustice.org/. Once it is in place, please let us know so we can run the check again.

If you use Google Analytics 4, please also confirm the measurement ID and whether it loads after cookie consent. We did not see it sending data during our check.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://earthjustice.org/
- consent_banner: https://cc.cdn.civiccomputing.com/9/cookieControl-9.x.min.js
