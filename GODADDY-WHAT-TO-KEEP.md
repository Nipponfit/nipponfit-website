# What to keep and what to drop at GoDaddy

Now that the website runs on Vercel — which is free at your size — GoDaddy is only doing
two jobs for you instead of three.

---

## Keep — these are essential

### 1. The domain: `nipponfit.com`

**Never let this lapse.** It is the name itself. Everything hangs off it:

- the website
- **`app.nipponfit.com`** — where every parent logs in
- **your email** — `contactus@nipponfit.com`

If the domain expires, all three stop at once. Set it to auto-renew and, if GoDaddy
offers a multi-year renewal at a sensible price, take it — it removes the risk of a
missed renewal email.

### 2. Professional Email Pro Light — `contactus@nipponfit.com`

Your email is still hosted by GoDaddy and still working. I checked the records after the
DNS change and every one of them is intact:

| Record | Status |
|---|---|
| MX → `mailstore1.secureserver.net`, `smtp.secureserver.net` | working |
| SPF (stops your mail landing in spam) | working |
| `email.nipponfit.com` webmail | working |

That address is printed on the website, on the registration form and inside the app.
Keep it.

---

## Cancel — but not yet

### Websites + Marketing Standard Intl — `NIPPONFIT.COM`

**This is the old website builder. It is the one you no longer need.** The new site
replaces it entirely and costs nothing to host.

**Wait two to four weeks before cancelling.** Right now it is your safety net: if
anything unexpected turns up on the new site, changing one DNS record back to
`13.248.243.5` brings the old site straight back. Cancel the plan and that option is
gone for good.

Once you are confident — the site has been up a few weeks, enquiries are coming through,
nothing is missing — cancel it and stop paying for it.

### ⚠️ One thing to confirm before you cancel

GoDaddy sometimes bundles an email account into a Websites + Marketing plan. Yours is
listed as a separate product, which suggests it is billed separately and safe — but the
cost of being wrong is your email going down.

**Before you cancel, use the Contact Us button on that page and ask them plainly:**

> "If I cancel my Websites + Marketing Standard plan, will my Professional Email
> account contactus@nipponfit.com be affected in any way?"

Get the answer in writing, then cancel.

---

## Ignore

### Website Builder Free 1-Page

It is free and you have never set it up. It costs nothing. Leave it alone.

---

## Your call

### Full Protection plan on the domain

This is optional. It usually covers two things:

- **Privacy** — keeps your name, address and phone number out of the public domain
  register. Without it, anyone can look up the owner of nipponfit.com and see your
  personal details.
- **Protection against unauthorised transfer** — makes it harder for somebody to move
  the domain away from you.

For a business with a public phone number, the privacy matters less than it would for a
private individual, but the transfer protection is genuinely worth having. It is usually
a small amount per year. **My suggestion: keep it.** Losing control of the domain would
take down your website, your app and your email at the same time, and it is not the
place to save a few hundred rupees.

---

## What you will be paying for, from now on

| | |
|---|---|
| Domain `nipponfit.com` | GoDaddy, yearly |
| Email `contactus@nipponfit.com` | GoDaddy, yearly |
| Domain protection | GoDaddy, yearly — optional |
| **Website hosting** | **Vercel — free** |
| **App hosting** | **Vercel — free** |
| **Database** | **Supabase — free** |

The website hosting line is the one that has gone away.

---

## A useful thing I noticed

Your domain already carries a `google-site-verification` record, so Google has verified
this domain for you at some point in the past. That may make setting up **Google Search
Console** quicker than expected — try the DNS verification method first, it may pass
straight away.
