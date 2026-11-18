# Brief: Tallyroll

**Register:** technical, calm, precise. The opposite of [fennel-street.md](fennel-street.md).

**What it is:** Tallyroll is a usage-based billing API. It turns raw usage events into invoices. Engineers
integrate it; finance teams reconcile its line items every month.

**Audience:** engineering leads at software companies with usage-based pricing, and the finance leads who sign
off with them. They distrust marketing and want to see how it works.

**The page must:** make a careful buyer trust Tallyroll with their revenue, and send them to the docs or to
book a demo.

## Copy

Use this copy. You may cut it, but don't add claims, numbers or testimonials that aren't here.

- **Headline:** Every cent traces back to an event.
- **Subhead:** Tallyroll turns raw usage into invoices your finance team can reconcile line by line.
- **Primary action:** Read the docs. **Secondary action:** Book a demo.
- **How it works:**
  1. *Send events.* Post usage events from your product as they happen: `POST /v1/events`.
  2. *Define pricing.* Tiers, minimums, credits and commitments, written as rules you can read.
  3. *Invoice.* Each line on an invoice opens up into the events that produced it.
- **Example invoice line:** "API calls, March: 1,204,388 calls × $0.0004 = $481.76". Expands to the 31 daily
  totals behind it.
- **For finance:** Line-level audit trail. Exports to NetSuite and QuickBooks. Revenue recognition schedules.
- **For engineering:** Idempotent event ingestion. Webhooks for every invoice state. SDKs for TypeScript, Python
  and Go.
- **Pricing:** 0.5% of billed revenue, no platform fee. Free until you bill $10,000 a month.
- **Footer:** Docs · Pricing · Status · Security · Contact. © 2026 Tallyroll.

## Constraints

- One page, delivered as a single self-contained HTML file.
- No external images. Where a picture or screenshot would go, build it in HTML and CSS (for example the invoice
  line), or leave a clearly labelled placeholder.
- Web fonts may be loaded or self-hosted; say which ones you used.
