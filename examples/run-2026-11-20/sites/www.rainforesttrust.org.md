# https://www.rainforesttrust.org/

**Status:** Ready, with warnings (Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 15.4s
**Account ID(s):** ACMRCWPB

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.rainforesttrust.org/ |
| PASS | Installation code is in the page source | account ID(s): ACMRCWPB |
| PASS | Code is in <head>, last script | Found in <head> with no scripts after it. |
| PASS | One account ID on the page | ACMRCWPB |
| PASS | Widget script loads | HTTP 200, 17 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 2 '?form=' link(s): FUNAQFHNLKJ, FUNRGCCWCNJ |
| PASS | Google Tag Manager container | GTM-TQZN89M |
| PASS | GA4 measurement ID | G-MVP5KC1KV6 |
| PASS | Meta Pixel | loaded, pixel id(s): 162328464462089, 5913213552134911 |
| PASS | Cookie consent tool | CookieYes |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 9.9s |
| INFO | Console errors (any source) | 1 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://rainforesttrust.donorsupport.co/-/XUZXSDTH returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://www.rainforesttrust.org/ loaded with HTTP 200 in the headless browser. The FundraiseUp snippet is in the page source with account ID ACMRCWPB, placed in the head with no scripts after it. The widget script loaded with HTTP 200. Two donate links with form IDs FUNAQFHNLKJ and FUNRGCCWCNJ were found. The browser did not click these links, so checkout behavior was not tested. The page load event took 9.9 s, which is over the 6 s limit and is a warning, not a blocker. One console error was recorded, a 400 response with no source named. The GTM container, GA4 ID, Meta Pixel, and CookieYes consent tool were found. No other donation tool was found. AI crawlers are allowed in robots.txt. No llms.txt file exists, which is optional. Donate page https://rainforesttrust.donorsupport.co/-/XUZXSDTH returns HTTP 200 with donation content in the HTML.

### Risks

- **medium** Slow page load: The load event took 9.9 s. The check limit is 6 s. The verdict is ready with warnings, with no blockers. _(checks: page_speed)_
- **low** Console error on page: One console error was recorded: a resource returned HTTP 400. The source was not identified. The FundraiseUp widget reported no console errors. _(checks: console_errors)_

### Next steps

- [onboarding_team] Confirm with the customer which page resource returns HTTP 400 and whether it is expected. Re-run this check after any change to the page. _(checks: console_errors)_
- [customer] Review page load time for the home page and reduce the load event time to under 6 s. Re-run this check after the change. _(checks: page_speed)_
- [onboarding_team] Confirm in the FundraiseUp dashboard that the two form IDs FUNAQFHNLKJ and FUNRGCCWCNJ are the intended donation forms. _(checks: fu_checkout_links)_

### Draft email to the customer

**Subject:** Next steps for your donation page

```text
Hello,

Thank you for working with us to set up online donations. We checked your home page at https://www.rainforesttrust.org/ and the donation code is installed correctly.

One item needs your attention. The home page takes about 9.9 seconds to finish loading. Please review the page for large images, scripts, or other items that slow it down, and aim for under 6 seconds. Your web team can help with this.

We will re-check the page after the change. If you have questions, reply to this email.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.rainforesttrust.org/
- fu_code_in_source: .href;o.l=[]; for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','ACMRCWPB');</script> <!-- End Fundraise Up --> </head> <body> <n
- fu_widget_loads: https://cdn.fundraiseup.com/widget/ACMRCWPB
- consent_banner: https://cdn-cookieyes.com/client_data/bce0e242974d3ef4aada5386/script.js
- console_errors: Failed to load resource: the server responded with a status of 400 ()
- donate_no_js: https://rainforesttrust.donorsupport.co/-/XUZXSDTH
