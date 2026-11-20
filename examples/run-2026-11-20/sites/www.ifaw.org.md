# https://www.ifaw.org/

**Status:** Ready, with warnings (Code is in <head>, last script; Widget not held back by the consent tool; GA4 measurement ID; Page load under 6 s)
**Checked:** 2026-11-20 09:07 UTC in 15.5s
**Account ID(s):** AWMWZJRX

## Checklist

| Status | Check | Detail |
|---|---|---|
| PASS | Page loads in a headless browser | HTTP 200, final URL https://www.ifaw.org/ |
| PASS | Installation code is in the page source | account ID(s): AWMWZJRX |
| WARN | Code is in <head>, last script | In <head>, but 3 <script> tag(s) follow it. Docs recommend it as the last script. |
| PASS | One account ID on the page | AWMWZJRX |
| PASS | Widget script loads | HTTP 200, 11 requests to vendor hosts. |
| PASS | No widget errors in console | None recorded. |
| WARN | Widget not held back by the consent tool | The install code is in the page source, but Usercentrics sits in the call stack that inserted the widget script (consent tools can intercept and block scripts by domain). It loaded in this run; confirm it is set as strictly necessary, or visitors who decline cookies may not get the checkout. |
| PASS | Donate links open the checkout | 1 '?form=' link(s): join |
| PASS | Google Tag Manager container | GTM-W7GRNP |
| WARN | GA4 measurement ID | No GA4 property seen loading or sending hits (may load only after consent). |
| INFO | Meta Pixel | Not seen (optional; may load after consent). |
| PASS | Cookie consent tool | Usercentrics |
| PASS | No other donation tool on the page | None found. |
| WARN | Page load under 6 s | load event at 8.9s |

## AI agent readiness

Not part of the go-live verdict. Can AI assistants and AI search read the organization and reach the donate page?

| Status | Check | Detail |
|---|---|---|
| PASS | AI assistants and AI search can read the pages | robots.txt allows all listed AI bots. |
| INFO | llms.txt published | No /llms.txt (optional, still a proposal). |
| PASS | schema.org organization markup | JSON-LD types: Organization; DonateAction: no. |
| PASS | Donate page readable without JavaScript | https://www.ifaw.org/?form=join returns HTTP 200 with donation content in the HTML. |

## Summary (AI, from the facts above)

The page https://www.ifaw.org/ loaded in the headless browser with HTTP 200 and no load error. The FundraiseUp installation code for account AWMWZJRX is in the page source, and the widget script loaded at runtime from cdn.fundraiseup.com with HTTP 200. The verdict is ready with warnings and no blockers. The browser did not click any buttons, so it did not test whether checkout works. It found one donate link to the checkout form (?form=join), and that link returns donation content in the HTML without JavaScript. The code sits in the head, but 3 script tags follow it. Usercentrics sits in the call stack that inserted the widget script, so visitors who decline cookies may not get the widget unless it is set as strictly necessary. The page load event took 8.9 seconds. No GA4 measurement ID was seen loading or sending hits, which may be because it loads only after consent. The Meta Pixel was not seen, and it is optional.

### Risks

- **medium** Widget may depend on cookie consent: Usercentrics sits in the call stack that inserted the widget script. Visitors who decline cookies may not get the donation widget. Confirm the script is set as strictly necessary. _(checks: fu_consent_gated)_
- **low** Installation code is not last in head: Three script tags come after the FundraiseUp code in the head. The vendor docs recommend it as the last script. _(checks: fu_in_head)_
- **low** Slow page load: The load event fired at 8.9 seconds, above the 6 second target. This was one headless run. _(checks: page_speed)_
- **low** No GA4 hits seen: No GA4 measurement ID was seen loading or sending hits. It may load only after consent, so this is not confirmed either way. _(checks: ga4)_

### Next steps

- [customer] Ask your web developer to move the FundraiseUp code so it is the last script in the head, after the other three script tags. _(checks: fu_in_head)_
- [customer] Ask your web developer or consent tool administrator to mark the FundraiseUp widget as strictly necessary in Usercentrics, so it loads for visitors who decline cookies. _(checks: fu_consent_gated)_
- [onboarding_team] Confirm with the customer that the FundraiseUp widget and the donate link to the checkout form work when a visitor declines cookies. The browser did not click any buttons. _(checks: fu_consent_gated, fu_checkout_links)_
- [onboarding_team] Confirm with the customer whether they use a GA4 property and whether it loads after consent. Check the dashboard settings if needed. _(checks: ga4)_
- [onboarding_team] Re-run this check after the customer makes changes to confirm the warnings are cleared. _(checks: fu_in_head, fu_consent_gated, page_speed, ga4)_

### Draft email to the customer

**Subject:** Three quick fixes for your donation widget on ifaw.org

```text
Hello,

Thank you for working with us to launch donations on your website. Your FundraiseUp donation widget is installed and loads on https://www.ifaw.org/. Before launch, please make these three changes.

1. Move the FundraiseUp code so it is the last script in the page head. Right now, three other scripts load after it.

2. Ask your web developer or consent tool administrator to set the FundraiseUp widget as strictly necessary in Usercentrics. This makes sure visitors who decline cookies still see the donation widget.

3. Let us know whether you use a Google Analytics 4 property, so we can confirm it is set up on the page.

After you make these changes, reply to this email and we will run the check again.

Thank you,
The Onboarding Team
```

## Evidence

- page_reachable: https://www.ifaw.org/
- fu_code_in_source: tion.href;o.l=[]; for(i=0;i<7;i++)o[l[i]]=o(l[i]);w[n]=o} })(window,document,'script','FundraiseUp','AWMWZJRX');</script> <!-- End Fundraise Up --> <script src=https://www.f
- fu_widget_loads: https://cdn.fundraiseup.com/widget/AWMWZJRX
- fu_consent_gated: https://web.cmp.usercentrics.eu/ui/v/4.34.0/WebSdk.lib.fb4e0364.js
- consent_banner: https://web.cmp.usercentrics.eu/ui/loader.js
- donate_no_js: https://www.ifaw.org/?form=join
