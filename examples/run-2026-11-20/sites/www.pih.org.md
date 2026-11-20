# https://www.pih.org/

**Status:** Ready, with warnings (Code is in <head>, last script)
**Checked:** 2026-11-20 09:07 UTC in 7.3s
**Account ID(s):** AJDEFYWC

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.pih.org/ |
| PASS | Installation code is in the page source | account ID(s): AJDEFYWC |
| WARN | Code is in <head>, last script | In <head>, but 6 <script> tag(s) follow it. Docs recommend it as the last script. |
| PASS | One account ID on the page | AJDEFYWC |
| PASS | Widget script loads | HTTP 200, 12 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): donate |
| PASS | Google Tag Manager container | GTM-N2SDGSGB |
| PASS | GA4 measurement ID | G-76XL6SD9RS |
| PASS | Meta Pixel | loaded, pixel id(s): 186334911708838 |
| PASS | Cookie consent tool | CookieYes |
| PASS | No other donation tool on the page | None found. |
| PASS | Page load under 6 s | load event at 3.0s |
| INFO | Console errors (any source) | 5 error(s) |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | No robots.txt, so no bot is blocked. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| INFO | schema.org organization markup | No Organization/NGO JSON-LD on the home or donate page (types seen: none). |
| WARN | Donate page readable without JavaScript | https://www.pih.org/?form=donate&source=web_header_topright is blocked or errors for a plain HTTP client (HTTP 403). |

## Summary (AI, from the facts above)

The FundraiseUp code is installed in the page source for account AJDEFYWC. The widget script loads with HTTP 200. The code sits in the head, but 6 script tags follow it. The browser found one donate link with a ?form= parameter. The browser did not click the link, so checkout behavior is not verified. The donate page returned HTTP 403 to a plain HTTP client, so it could not be read without JavaScript. The page loaded in 3.0 seconds with HTTP 200. Five console errors were recorded, all HTTP 403 responses.

### Risks

- **medium** Code is not the last script in head: The FundraiseUp snippet is in head, but 6 script tags follow it. The vendor docs recommend it as the last script. _(checks: fu_in_head)_
- **medium** Donate page returns 403 to plain HTTP clients: The donate URL returned HTTP 403 without JavaScript. The browser did not confirm whether the checkout opens for a visitor. _(checks: donate_no_js)_
- **low** Console shows 403 errors: Five console errors were recorded, and the three listed are HTTP 403 responses. The source of these requests was not identified. _(checks: console_errors)_

### Next steps

- [customer] Move the FundraiseUp snippet so it is the last script tag in the head, or confirm with the onboarding team that the current position is acceptable. _(checks: fu_in_head)_
- [customer] Check that the donate page at https://www.pih.org/?form=donate&source=web_header_topright loads for a normal visitor and is not blocked by a firewall or bot rule. _(checks: donate_no_js)_
- [onboarding_team] Confirm with the customer that the donate link opens checkout, then re-run this check. _(checks: fu_checkout_links, donate_no_js)_

### Draft email to the customer

**Subject:** Next steps for your donation page setup

```text
Hello,

Thank you for working with us on your online donation setup. We checked https://www.pih.org/ and the FundraiseUp code is in place for your account. The widget script loads correctly.

We found two items to fix on your website:

1. Move the FundraiseUp code so it is the last script tag in the head section of your page. Right now six other script tags come after it.

2. Check the donate page at https://www.pih.org/?form=donate&source=web_header_topright. When we requested it without a browser, the server returned an error (HTTP 403). Please confirm that a normal visitor can open it. If a firewall or bot rule blocks it, please allow access.

Once these are done, let us know and we will run the check again.

Thank you,
Onboarding Team
```

## Evidence

- page_reachable: https://www.pih.org/
- fu_code_in_source: l=[]; for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AJDEFYWC');</script> <!-- End Fundraise Up --> <script async
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AJDEFYWC
- consent_banner: https://cdn-cookieyes.com/client_data/e2e10971d17a7d901143eac2a0810038/script.js
- console_errors: Failed to load resource: the server responded with a status of 403 ()
- console_errors: Failed to load resource: the server responded with a status of 403 ()
- console_errors: Failed to load resource: the server responded with a status of 403 ()
- donate_no_js: https://www.pih.org/?form=donate&source=web_header_topright
