# https://www.pih.org/

**Status:** Could not check (bot challenge / access denied page (HTTP 403))
**Checked:** 2026-11-20 08:56 UTC in 5.3s
**Account ID(s):** none found

## Checklist

| Status | Check | Detail |
|---|---|---|
| FAIL | Page loads in a headless browser | bot challenge / access denied page (HTTP 403) |
| INFO | Installation code is in the page source | No installation code found in the source and no widget request recorded. |

## Summary (AI, from the facts above)

The headless browser could not load https://www.pih.org/. The page returned HTTP 403 with a bot challenge or access denied page. Because the page did not load, the check could not look for the FundraiseUp installation code. No installation code was found in the source, and no widget request was recorded. This does not show whether the code is missing from the live site, since the check never got past the challenge page. No checkout or donate links were found on the page the browser received.

### Risks

- **high** Page blocked for automated access: The page returned HTTP 403 with a bot challenge or access denied page. The browser could not load the real page content, so the install status is unknown. _(checks: page_reachable)_
- **medium** Installation status unknown: No installation code was found in the source and no widget request was recorded. The page was not loaded, so this result cannot confirm whether the code is installed. _(checks: fu_code_in_source)_

### Next steps

- [customer] Check whether your website blocks automated visitors or requires a challenge or login for public pages. If it does, allow the check to load the public donation page, or tell us which access rule applies. _(checks: page_reachable)_
- [onboarding_team] Confirm with the customer that the public page https://www.pih.org/ is meant to be accessible to outside visitors. Then re-run this check once access is confirmed. _(checks: page_reachable, fu_code_in_source)_

### Draft email to the customer

**Subject:** Next step for your donation platform setup

```text
Hello,

We tried to check your website, https://www.pih.org/, as part of setting up your online donation platform. The page returned an access denied message to our check, so we could not review it.

Please check whether your website blocks automated visitors or uses a challenge page for public pages. If it does, please let us know, or allow access to your public donation page so we can run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.pih.org/
