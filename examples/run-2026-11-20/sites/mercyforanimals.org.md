# https://mercyforanimals.org/

**Status:** Ready, with warnings (Installation code is in the page source)
**Checked:** 2026-11-20 08:55 UTC in 9.9s
**Account ID(s):** AVGENVAN

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://mercyforanimals.org/ |
| WARN | Installation code is in the page source | Widget loads at runtime but the code is not in the server HTML. Inserted by: JavaScript from https://mercyforanimals.org/wp-content/plugins/mfa-blocks-2024/assets/js/mfa-fundraiseup/mfa-fundraiseup.min.js?ver=1.0. (not a tag manager). Vendor docs ask for the code in the global <head> and confirm it by viewing the page source. |
| PASS | One account ID on the page | AVGENVAN |
| PASS | Widget script loads | HTTP 200, 23 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): donate |
| PASS | Google Tag Manager container | GTM-K524TFT, GTM-M3LDFJ, GTM-MGT2PJQJ, GTM-YV5D9SSG31 |
| PASS | GA4 measurement ID | G-B35EWX8EQ4, G-EN2Y9H0GJ5 |
| PASS | Meta Pixel | loaded, pixel id(s): 1516273432023152, 796754017021217, 822324977878230 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 5.6s |
| INFO | Console errors (any source) | 4 error(s) |

## Summary (AI, from the facts above)

The page at https://mercyforanimals.org/ loaded in a headless browser with HTTP 200. The FundraiseUp widget loads at runtime for account AVGENVAN, but its code is not in the server HTML. A JavaScript file from the site's mfa-blocks-2024 plugin inserts it. The browser found one donate link with a '?form=' checkout parameter. The browser did not click it, so checkout behavior was not tested. The verdict is ready with warnings, with no blockers. Four console errors were recorded, all about Content Security Policy blocking connections to two external event endpoints. No cookie consent tool was detected.

### Risks

- **medium** FundraiseUp code is not in the page source: The widget is inserted by JavaScript from the site's plugin, not by code in the global head. The vendor asks for the code in the global head and confirmation through the page source. The snippet count in source is 0. _(checks: fu_code_in_source)_
- **medium** No cookie consent tool detected: No known consent tool was found. A consent setup is needed for EU and UK visitors because vendor cookies are set on the page. _(checks: consent_banner)_
- **low** Content Security Policy blocks two event endpoints: The browser recorded four console errors. Two Content Security Policy errors refused connections to an external Cloud Run endpoint and an AWS endpoint. These errors do not involve the FundraiseUp widget, which had no console errors. _(checks: console_errors, fu_no_console_errors)_

### Next steps

- [customer] Add the FundraiseUp snippet for account AVGENVAN to the global head of the site, then view the page source to confirm it appears. _(checks: fu_code_in_source)_
- [customer] Set up a cookie consent tool for EU and UK visitors, since vendor cookies are used on the page. _(checks: consent_banner)_
- [customer] Review the Content Security Policy connect-src setting and decide whether the two blocked event endpoints should be allowed. _(checks: console_errors)_
- [onboarding_team] Confirm with the customer which plugin inserts the widget script and whether it can be changed. _(checks: fu_code_in_source)_
- [onboarding_team] Re-run this check after the customer's changes and confirm the snippet appears in the page source. _(checks: fu_code_in_source, consent_banner, console_errors)_

### Draft email to the customer

**Subject:** Action needed: add FundraiseUp code to your site head

```text
Hello,

Thank you for working with us to launch your donation page. We checked https://mercyforanimals.org/ and found your FundraiseUp widget loads, but its code is not in the global head of your site. Please take these steps:

1. Add the FundraiseUp snippet for account AVGENVAN to the global head of your site.
2. View the page source and confirm the snippet appears there.
3. Set up a cookie consent tool for EU and UK visitors, since vendor cookies are used on the page.
4. Review your Content Security Policy connect-src setting. Two external event endpoints were blocked, and you should decide whether to allow them.

Once these are done, let us know and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://mercyforanimals.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AVGENVAN
- fu_code_in_source: https://mercyforanimals.org/wp-content/plugins/mfa-blocks-2024/assets/js/mfa-fundraiseup/mfa-fundraiseup.min.js?ver=1.0.0
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AVGENVAN
- console_errors: Connecting to 'https://mpc-pilot-1-s6uit34pua-uc.a.run.app/events?cee=no' violates the following Content Security Policy directive: "connect-src 'self' doubleth
- console_errors: Fetch API cannot load https://mpc-pilot-1-s6uit34pua-uc.a.run.app/events?cee=no. Refused to connect because it violates the document's Content Security Policy.
- console_errors: Connecting to 'https://kw-f5e5ef3e54fb4122a3ba09a55357f9ab.ecs.us-west-1.on.aws/events?cee=no' violates the following Content Security Policy directive: "connec
