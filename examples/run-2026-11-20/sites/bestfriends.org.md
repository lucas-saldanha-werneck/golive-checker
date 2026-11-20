# https://bestfriends.org/

**Status:** Ready, with warnings (Code is in <head>, last script; Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 13.8s
**Account ID(s):** AFZUYXBL

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://bestfriends.org/ |
| PASS | Installation code is in the page source | account ID(s): AFZUYXBL |
| WARN | Code is in <head>, last script | In <head>, but 4 <script> tag(s) follow it. Docs recommend it as the last script. |
| PASS | One account ID on the page | AFZUYXBL |
| PASS | Widget script loads | HTTP 200, 21 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): FUNAVXCWESD |
| PASS | Google Tag Manager container | GTM-NMXDTP |
| PASS | GA4 measurement ID | G-7X412QBZQC, G-JDV4SZ13C8 |
| PASS | Meta Pixel | loaded, pixel id(s): 576668945811638 |
| INFO | Cookie consent tool | No known consent tool detected. Needed for EU/UK visitors; vendor cookies need a consent setup. |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 8.9s |
| INFO | Console errors (any source) | 1 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://bestfriends.org/donate returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://bestfriends.org/ loaded in a headless browser with HTTP 200. The FundraiseUp snippet is in the page source once, with account ID AFZUYXBL, and the widget script loaded with HTTP 200. The snippet is in <head>, but 4 script tags follow it. The load event fired at 8.9 seconds. One resource returned HTTP 451 and one console error was recorded. The browser did not click anything. It found one donate link to the checkout form (FUNAVXCWESD). No other donation tool was found. No consent tool was detected. The verdict is ready with warnings and no blockers.

### Risks

- **medium** FundraiseUp snippet is not the last script in head: The snippet is in <head>, but 4 script tags follow it. The FundraiseUp docs recommend it as the last script. _(checks: fu_in_head)_
- **medium** Slow page load: The load event fired at 8.9 seconds. The check threshold is 6 seconds. _(checks: page_speed)_
- **low** No consent tool detected: No known consent tool was found on the page. The check notes that EU and UK visitors need one, and vendor cookies need a consent setup. Whether the customer needs one was not recorded. _(checks: consent_banner)_
- **low** Resource returned HTTP 451: One request failed with HTTP 451 and one console error was recorded. The resource that failed was not identified. _(checks: console_errors)_

### Next steps

- [customer] Move the FundraiseUp snippet so it is the last script tag in <head>. _(checks: fu_in_head)_
- [customer] Review why the home page takes about 9 seconds to load, and reduce the load time below 6 seconds. _(checks: page_speed)_
- [customer] Confirm whether the site needs a cookie consent tool for EU and UK visitors. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which resource returns HTTP 451, and whether it affects donations. _(checks: console_errors)_
- [onboarding_team] Re-run this check after the customer makes the changes and confirm the warnings are cleared. _(checks: fu_in_head, page_speed)_

### Draft email to the customer

**Subject:** Next steps for your donation page

```text
Hi,

Thanks for working with us to set up donations on your website. Your donation code is on the home page and the widget loads correctly. We found a few things to fix:

1. In the page head, move the donation code so it is the last script tag. Right now four other scripts load after it.
2. Review your home page load time. It takes about 9 seconds, and it should be under 6 seconds.
3. Please let us know whether you need a cookie consent tool for visitors in the EU and UK.

Once these are done, let us know and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://bestfriends.org/
- fu_code_in_source: for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AFZUYXBL');</script> <script type="application/ld+json"> { "@contex
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AFZUYXBL
- console_errors: Failed to load resource: the server responded with a status of 451 ()
- donate_no_js: https://bestfriends.org/donate
