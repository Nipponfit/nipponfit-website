# Publishing nipponfit.com

Follow these three stages in order. Stage 1 and 2 are safe — nothing visible
changes for anyone until stage 3.

**Your domain stays with GoDaddy throughout.** You are not moving it. You are only
changing where it points.

---

## Before you start

The site has been checked and is ready:

| | |
|---|---|
| Pages | 17 |
| Broken links | none |
| Missing images | none |
| Titles and descriptions | all within Google's limits |
| Structured data | all valid |
| Sitemap | matches the site exactly |
| Total size | 17 MB |

---

## Stage 1 — Put the files on GitHub

1. Go to **github.com** and sign in.
2. Click the **+** in the top right, then **New repository**.
3. Repository name: `nipponfit-website`
4. Leave it **Public**. Do not tick "Add a README".
5. Click **Create repository**.
6. On the next page click **uploading an existing file**.
7. Open `F:\Nipponfit\NipponFit_website` in File Explorer, select **everything**
   inside it (`Ctrl` + `A`), and drag it onto the GitHub page.
8. Wait for every file to finish uploading — the gallery photographs take a minute.
9. Click **Commit changes**.

**What success looks like:** the repository page lists `index.html`, `assets`, `css`,
`js`, `tools`, `vercel.json` and the rest.

---

## Stage 2 — Connect it to Vercel

1. Go to **vercel.com** and sign in — use **Continue with GitHub** so it can see your
   repository.
2. Click **Add New** → **Project**.
3. Find `nipponfit-website` in the list and click **Import**.
4. **Change nothing on the settings page.** There is no framework and nothing to build.
5. Click **Deploy**.

**What success looks like:** after about thirty seconds you get an address like
`nipponfit-website.vercel.app`. Open it.

### Check these six things on that address

1. The home page shows the moving gallery under the headline, and it changes by itself.
2. **Programmes**, **Karate Club**, **Instructors**, **Gallery**, **Blog**, **Locations**
   and **Contact** all open.
3. The Instructors page shows four faces.
4. The Gallery page shows all 44 photographs.
5. On the Karate Club page, the registration form opens WhatsApp when you submit it.
6. **Login** takes you to the app.

If anything is wrong, stop here and tell me. The old site is still live and untouched.

---

## Stage 3 — Point nipponfit.com at the new site

**This is the only step that changes what the public sees.** Do it once you are happy
with stage 2.

### In Vercel

1. Open the project → **Settings** → **Domains**.
2. Type `nipponfit.com` and click **Add**.
3. Type `www.nipponfit.com` and click **Add**.
4. Vercel now shows you the DNS records it needs. **Leave this page open** — you need
   the values from it.

### In GoDaddy

5. Go to **godaddy.com** → **My Products** → find `nipponfit.com` → **DNS**.
6. Change the records to match what Vercel showed you. Usually:
   - An **A** record, name `@`, value `76.76.21.21`
   - A **CNAME** record, name `www`, value `cname.vercel-dns.com`
7. **Delete or replace any existing `@` and `www` records** left over from the GoDaddy
   Website Builder site — otherwise the old site keeps showing.
8. Save.

**What success looks like:** within an hour or two — occasionally up to a day — typing
`nipponfit.com` shows the new site, with a padlock beside the address. Vercel sets up
the security certificate on its own.

> **Nothing is lost.** GoDaddy keeps your old site. If anything goes wrong you can put
> the old DNS records back and the old site returns.

---

## Stage 4 — Tell Google about it

Do this the same day. **This is the part that decides your ranking**, more than anything
on the website itself.

### Google Search Console

1. Go to **search.google.com/search-console** and add `www.nipponfit.com`.
2. Verify it — Vercel makes this straightforward.
3. Open **Sitemaps** and submit `sitemap.xml`.

**What success looks like:** within a week, "Pages → Indexed" starts filling up.

### Google Business Profile — the biggest win available to you

1. Go to **google.com/business**.
2. Create or claim a profile for **Nippon Karate Club**.
3. Create **three** — one for each dojo: Panathur, Dravid CSE, Koramangala. Google ranks
   by distance from whoever is searching, so three pins beat one.
4. On each: category **Karate school**, phone `+91 99456 16005`, website
   `https://www.nipponfit.com`, real photographs, opening hours.
5. **Ask every current parent for a review.** Twenty honest reviews mentioning "karate"
   and "Bangalore" will lift you further than anything in the website's code.

### Get listed elsewhere

Justdial, Sulekha, the Karate India Organization member list, the Akhila Karnataka
association site. Write the name, address and phone number **identically** everywhere —
Google matches on exactly that.

---

## One separate job, when you are ready

The **Login** button hands people to `app.nipponfit.com` with their mobile number
already filled in. The website side is live and working. The matching change in the app
is sitting in `nipponfit-app-repo` but has **not been pushed or deployed** yet.

Until it is, Login still works — parents just land on the app's normal start screen and
type their number themselves. Push that repository when convenient and the number will
carry across.

---

## If something looks wrong after publishing

Press `Ctrl` + `Shift` + `R` first. Your browser keeps copies of pages and will show you
an old one. That explains most "it didn't work" moments.

If it still looks wrong, tell me what you see and I will check the file itself.
