# Pointing nipponfit.com at the new site

## What your DNS looks like right now

| Record | Currently points to | What it is |
|---|---|---|
| `A` `@` | `13.248.243.5` | The **old** GoDaddy website. This is the one to change. |
| `CNAME` `www` | `nipponfit.com` | Sends www to the same place as above. Also changes. |
| `CNAME` `app` | `419e5c852eb495e6.vercel-dns-017.com` | **Your app.** Do not touch it. |
| `NS` `@` ×2 | `ns19/ns20.domaincontrol.com` | Leave alone. |
| `CNAME` `bounces...` | `...secureserver.net` | Your email. Leave alone. |

---

## ⚠️ The one thing not to do

**Do not delete or edit the `CNAME` record named `app`.**

That is `app.nipponfit.com` — where parents log in. It is already on Vercel and working
perfectly. If it is removed, every parent loses access to attendance, fees and gradings
until it is put back.

Only two records change. Everything else stays exactly as it is.

---

## Step 1 — Change the A record

1. In GoDaddy, find the row: **A** — **@** — **13.248.243.5**
2. Click the **pencil** (Edit) at the end of that row
3. Change the value to:

   ```
   216.198.79.1
   ```

   That is **two hundred sixteen, dot, one nine eight, dot, seven nine, dot, one** —
   four groups. Easiest to use the copy button next to it in Vercel rather than typing.

4. Leave Name as `@` and TTL as `1 Hour`
5. Save

---

## Step 2 — Change the www record

Vercel needs to tell you this one, because the value is unique to your project.

1. Go back to the Vercel **Domains** page
2. Scroll down to **www.nipponfit.com**
3. Under **DNS Records** it shows a row — almost certainly type **CNAME**, name **www**,
   and a value ending in `.vercel-dns-017.com` or `cname.vercel-dns.com`
4. Copy that value with the copy button
5. In GoDaddy, find the existing row: **CNAME** — **www** — **nipponfit.com**
6. Click the **pencil**, replace the value with what you copied, and save

If Vercel shows an **A** record for www instead of a CNAME, use the same value as
Step 1 and change the record type to A.

---

## Step 3 — Wait, then check

1. Back in Vercel, click **Refresh** next to each domain
2. The red **Invalid Configuration** turns into a green tick

This usually takes 10–30 minutes but can take a few hours. GoDaddy's records are set to
`1 Hour`, so allow at least that long before worrying.

**What success looks like:** typing `nipponfit.com` shows the new site with a padlock
beside the address. Vercel arranges the security certificate itself.

---

## After it goes live — check these

1. `nipponfit.com` shows the new site
2. `www.nipponfit.com` shows the new site
3. **`app.nipponfit.com` still opens the parent app** — this is the important one
4. The padlock appears on all three

---

## If you need to undo it

Change the `A` `@` record back to `13.248.243.5` and the `www` CNAME back to
`nipponfit.com`. The old GoDaddy site returns within the hour. Nothing is deleted at any
point.

---

## Note on what Vercel said

> "We're expanding our IP range. We recommend the records above. The legacy records
> cname.vercel-dns.com and 76.76.21.21 will continue to work."

That is why the address is `216.198.79.1` rather than the older `76.76.21.21` you may
see in guides online. Use the one Vercel is showing you now.
