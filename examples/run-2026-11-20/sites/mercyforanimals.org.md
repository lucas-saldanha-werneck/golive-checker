# https://mercyforanimals.org/

**Status:** Ready, with warnings (Installation code is in the page source; Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 15.7s
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
| WARN | Page load under 6 s | load event at 10.1s |
| INFO | Console errors (any source) | 4 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://mercyforanimals.org/?form=donate returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://mercyforanimals.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp widget script loads at runtime with account ID AVGENVAN. The widget code is not in the server HTML. A site script inserts it after load, and the vendor asks for the code in the global head and confirmation in the page source. The page load event took 10.1 seconds, above the 6 second target. Four console errors were recorded, all Content Security Policy refusals of connections to two external event endpoints. The browser did not click anything. One '?form=' donate link was found. The donate page returns readable HTML without JavaScript. Google Tag Manager, GA4, and Meta Pixel were found on the page. No consent tool was detected. The checklist verdict is ready with warnings, with no blockers.

### Risks

- **medium** Widget code is not in the page source: The FundraiseUp code is added by a site script at runtime, not in the server HTML. The vendor asks for the code in the global head and a source check to confirm it. _(checks: fu_code_in_source)_
- **medium** Slow page load: The load event fired at 10.1 seconds. The check target is under 6 seconds. _(checks: page_speed)_
- **low** Content Security Policy blocks event requests: Four console errors were recorded. Connections to two external event endpoints were refused by the page's Content Security Policy. _(checks: console_errors)_
- **low** No consent tool detected: No known cookie consent tool was found. Vendor cookies need a consent setup for EU and UK visitors. _(checks: consent_banner)_

### Next steps

- [customer] Ask your web developer to add the FundraiseUp installation code to the global head of the site, so it appears in the server HTML. Then view the page source to confirm it is there. _(checks: fu_code_in_source)_
- [customer] Ask your web developer to review the page load time, which was 10.1 seconds, against the 6 second target. _(checks: page_speed)_
- [customer] Ask your web developer to review the Content Security Policy so the two external event endpoints named in the console errors are allowed, or confirm they are not needed. _(checks: console_errors)_
- [onboarding_team] Confirm with the customer whether they use a cookie consent tool for EU and UK visitors and whether one is needed. _(checks: consent_banner)_
- [onboarding_team] Re-run this check after the customer updates the page to confirm the installation code appears in the page source. _(checks: fu_code_in_source, page_speed)_

### Draft email to the customer

**Subject:** Next steps for your donation page at mercyforanimals.org

```text
Hello,

Thank you for working with us to launch your online donations. Your donation page loads and the FundraiseUp widget is active. A few items need attention before we can mark the launch complete.

1. Add the FundraiseUp installation code to the global head of your website, so it appears in the page source. Please check the page source afterward to confirm it is there.

2. Ask your web developer to review page speed. The main page took about 10 seconds to finish loading. Our target is under 6 seconds.

3. Ask your web developer to review your Content Security Policy. Two external event endpoints were blocked, which caused console errors.

4. Let us know whether you use a cookie consent tool for visitors in the EU or UK.

Once these are updated, reply to this email and we will re-run the check.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://mercyforanimals.org/
- fu_code_in_source: https://cdn.fundraiseup.com/widget/AVGENVAN
- fu_code_in_source: https://mercyforanimals.org/wp-content/plugins/mfa-blocks-2024/assets/js/mfa-fundraiseup/mfa-fundraiseup.min.js?ver=1.0.0
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AVGENVAN
- console_errors: Connecting to 'https://mpc-pilot-1-s6uit34pua-uc.a.run.app/events?cee=no' violates the following Content Security Policy directive: "connect-src 'self' doubleth
- console_errors: Fetch API cannot load https://mpc-pilot-1-s6uit34pua-uc.a.run.app/events?cee=no. Refused to connect because it violates the document's Content Security Policy.
- console_errors: Connecting to 'https://kw-f5e5ef3e54fb4122a3ba09a55357f9ab.ecs.us-west-1.on.aws/events?cee=no' violates the following Content Security Policy directive: "connec
- donate_no_js: https://mercyforanimals.org/?form=donate
