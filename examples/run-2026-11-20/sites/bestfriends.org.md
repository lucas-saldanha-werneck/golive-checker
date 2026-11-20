# https://bestfriends.org/

**Status:** Ready, with warnings (Code is in <head>, last script)
**Checked:** 2026-11-20 08:55 UTC in 9.0s
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
| PASS | Page load under 6 s | load event at 4.8s |
| INFO | Console errors (any source) | 1 error(s) |

## Summary (AI, from the facts above)

The page https://bestfriends.org/ loaded in the headless browser with HTTP 200 and took 4.8 seconds to load. The FundraiseUp snippet is in the page source with one account ID, AFZUYXBL. The widget script loaded from the vendor host. The snippet sits in <head>, but 4 script tags follow it, and the docs recommend it be the last script. One donate link with a checkout form ID (FUNAVXCWESD) was found. The browser did not click the link, so checkout behavior was not tested. No known cookie consent tool was detected. One console error (HTTP 451) was recorded. The verdict is ready with warnings, with no blockers.

### Risks

- **medium** Script placement is not last in head: The FundraiseUp snippet is in <head>, but 4 script tags load after it. The vendor docs recommend it as the last script. _(checks: fu_in_head)_
- **medium** No cookie consent tool detected: No known consent tool was found on the page. Vendor cookies may need a consent setup for EU and UK visitors. _(checks: consent_banner)_
- **low** Console error on page load: One console error was recorded: the server responded with status 451 for a resource. The cause was not identified. _(checks: console_errors)_

### Next steps

- [customer] Move the FundraiseUp script so it is the last script in the head section, after the other 4 script tags, or ask the onboarding team to confirm the placement is acceptable. _(checks: fu_in_head)_
- [customer] Confirm whether the site serves EU or UK visitors. If it does, set up a cookie consent tool before vendor cookies load. _(checks: consent_banner)_
- [onboarding_team] Confirm with the customer which donate link (form FUNAVXCWESD) is the intended checkout and test it manually. _(checks: fu_checkout_links)_
- [onboarding_team] Re-run this check after the customer changes the script placement or adds a consent tool. _(checks: fu_in_head, consent_banner)_

### Draft email to the customer

**Subject:** Action needed: FundraiseUp script placement on bestfriends.org

```text
Hello,

Thank you for working with us to set up donations on your website. We checked https://bestfriends.org/ and the FundraiseUp code is installed with account ID AFZUYXBL. The widget loads correctly.

Please make these changes:

1. Move the FundraiseUp script so it is the last script in the head section. Right now, 4 script tags load after it.

2. If your site has visitors in the EU or UK, set up a cookie consent tool so vendor cookies load only after consent.

Once these are done, reply to this email and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://bestfriends.org/
- fu_code_in_source: for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AFZUYXBL');</script> <script type="application/ld+json"> { "@contex
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AFZUYXBL
- console_errors: Failed to load resource: the server responded with a status of 451 ()
