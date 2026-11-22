# nipponfit.com — complete handover

**Everything about the website revamp, in one document.**
Work done 19–20 August 2026. Record compiled 22 November 2026.

This exists so the whole project can be picked up anywhere — in a Claude chat project,
by another developer, or by Pooja alone — without needing the original conversation.

---

## 1. Where everything lives

| Thing | Where |
|---|---|
| **Live website** | https://www.nipponfit.com |
| Source files | `F:\Nipponfit\NipponFit_website\` |
| Code repository | GitHub `Nipponfit/nipponfit-website`, branch `main` |
| Hosting | Vercel, project `nipponfit-website`, Hobby plan (free) |
| Domain + DNS | GoDaddy |
| Email | GoDaddy, `contactus@nipponfit.com` |
| **Parent app** (separate) | https://app.nipponfit.com — repo `Nipponfit/nipponfit-app` |
| Gallery photo originals | `F:\Nipponfit\Gallery_Originals\` — outside the site on purpose |
| Instructor photo originals | `F:\Nipponfit\Instructor_Originals\` |

**DNS, exactly as it stands.** Only one record was ever changed: `A @` from `13.248.243.5`
(old GoDaddy site) to `216.198.79.1` (Vercel). The `www` CNAME already pointed at
`nipponfit.com`, so it followed automatically. The apex 308-redirects to www.

⚠️ **`app.nipponfit.com` is a CNAME to `419e5c852eb495e6.vercel-dns-017.com`. Never delete
it.** That is where every parent logs in.

---

## 2. What the site is

17 pages of plain HTML, CSS and JavaScript. **No framework, no npm, no build step needed
to publish.** Vercel serves the files exactly as they are. This is deliberate: the same
reasoning as the app rebuild — nothing that requires compilation, because a build step
puts the source out of reach.

**Pages:** home · karate-classes-bangalore (the main SEO page) · nippon-karate-club ·
instructors · gallery · blog + 7 articles · locations · contact · login · 404

### It is generated, not hand-edited

`tools/build.py` holds the menu, footer, phone number and address **once** and stamps
every page. Page content lives in `tools/pages_main.py` and `tools/pages_blog.py`.

> **Editing a `.html` file directly gets overwritten on the next build.** Change the
> Python, then run `python tools/build.py`.

### The other scripts

| Script | What it does |
|---|---|
| `tools/build.py` | Rebuilds every page |
| `tools/serve.py` | Local preview on port 4180 |
| `tools/curate_gallery.py` | Resizes, renames and captions gallery photos; rewrites the list in `js/gallery.js` |
| `tools/prepare_instructor_photos.py` | Crops and matches instructor headshots |

`serve.py` has two fixes that must not be undone: it is **threaded** (single-threaded
deadlocks on the browser's keep-alive connection) and it sends **`Cache-Control:
no-store`** (without it you edit a file, refresh, and are shown the old page).

---

## 3. Design

Rewritten on 19 August after the first version was judged to "look more AI generated".

Editorial and restrained: **Playfair Display** headings, **Inter** body, warm off-white
paper, near-black ink, one deep crimson accent, muted gold hairlines. No gradients, no
rainbow belt strip, no colour-block sections, no statistics strip. Space does the work.

---

## 4. Content rules Pooja set

These are decisions, not suggestions. Keep them.

- **"Login"**, never "Parent Login". The section heading is **"Nippon Karate Club Portal"**.
- The home page opens with **Nippon Fit** and its five programmes — karate, self defence,
  strength and conditioning, weight loss, wellness and fitness. **Nippon Karate Club comes
  after, not first.**
- Children from **four** years old.
- **First class free.**
- **Class timings must never be published anywhere on the site.**
- No "Bengaluru" label above the home page headline.
- The achievements heading is **"Social responsibility"**, not "Giving back".
- Her title is **Renshi**, not Sensei, in anything parents read.

### The text is hers

All copy was pulled verbatim off the old GoDaddy site — read through the browser, not a
text converter, because the founder bio and About Us were considerably longer than the
converted version showed. The Nippon Karate Club page keeps the original order exactly:
**About Us → Founder → Registration Form.**

---

## 5. People

**Pooja Shri Shetty** — Founder and Chief Instructor. International karateka and
aerospace engineer. Her name on the club page links to
https://en.wikipedia.org/wiki/Pooja_Shri_Shetty

**Darshan T V** — OBMAA trained, 15 years in karate, 6+ teaching, 2nd Dan black belt,
Goju-ryu and Shotokan, national and state medals (KIO), national kickboxing bronze (WAKO).
*(The name was "Dashant" in early notes. It is Darshan.)*

**Jeevan J** and **Arvind Acharya** — both: internationally awarded 2nd Dan black belt,
licensed referee and judge, several medals at the Karnataka State Championship and the
National Open Championship.

---

## 6. The blog — 7 articles

**Three carried across from the old site**, word for word:
Martial Arts Styles (185 styles, Apr 2023) · Origin of Karate-Do (Jan 2023) · Full Body
Workout (Jan 2023).

Their old addresses had an extra `/f/` segment. `vercel.json` redirects `/blog/f/:slug`
→ `/blog/:slug`, so no existing link breaks.

**Four technique analyses** built from the training documents in `F:\Nipponfit\Training\`
before the real three arrived. Pooja was told they can come down on request.

The 185-style list lives in `tools/blog_martial_arts.py`, one style per line, numbered
automatically. The other two bodies are in `tools/blog_bodies.py`.

---

## 7. The gallery — 44 photographs

58 files arrived. 6 were byte-identical duplicates. 5 were the same photo re-sent through
WhatsApp at lower resolution — caught with a perceptual hash, sharper copy kept. 2 were
already used elsewhere. 1 was a "kara te" characters graphic, now on the Origin of
Karate-Do article.

**65 MB became 12 MB.** Resized to 1800px long edge, EXIF rotation applied, 500px
thumbnails generated, captions written from the banners visible in each photo.

The slideshow rotates every **15 seconds**. The home page shows the first 10
(`data-limit="10"` — 44 dots is unusable); the Gallery page shows all 44 plus a grid.
Order: Ugur Aktas seminar → international → national → state → club life.

---

## 8. Two deliberate engineering decisions

### The registration form has no Aadhaar field and no file upload

The old form asked for both — and posted to a non-existent `submit.php`, so it had never
actually worked. A static site has nowhere safe to receive government ID, and routing it
through WhatsApp or email is worse.

The page asks people to bring the photo and Aadhaar copy to the dojo instead.

> **Do not add those fields back without a proper backend.** Collecting Aadhaar numbers
> through an unsecured web form is a real DPDP Act problem, not a style preference.

### Login is a handoff, not a login

A signed-in session on nipponfit.com cannot carry across to app.nipponfit.com — different
origin, separate storage. So `/login` takes only the mobile number, normalises it
(strips +91, spaces, leading zero) and hands over as `app.nipponfit.com/?m=<10 digits>`.

`handedOverNumber()` in the app's `js/app.js` reads it, prefills the box, focuses the
password field and wipes the number from browser history. Verified end to end.

⚠️ **That app-side change is committed in `nipponfit-app-repo/js/app.js` but was never
pushed or deployed.** Until it is, Login still works — parents just land on the app's
normal start screen and type their number themselves.

---

## 9. Traps that cost real time — check these first

**Browser cache.** Pooja reported "none of the changes were applied" when every change
was on disk *and* being served correctly. Always verify the served bytes
(`curl -s http://localhost:4180/ | grep ...`) before changing anything, then say
Ctrl+Shift+R.

**DNS cache.** After the DNS switch she still saw the old site. Her ISP had the old
address cached for ~42 more minutes. Google, Cloudflare and Quad9 all had the new one.
Hard refresh does nothing for DNS — check with `Resolve-DnsName ... -Server 8.8.8.8`.

**Pasted images are not files.** She pastes photos into chat and believes that delivers
them. It happened three times. Always check the filesystem and give an exact save path.

**Windows adds a second extension.** The gi photo arrived as `gi-pair.jpg.png` and was
silently skipped. `person_name()` now strips extension chains.

**GitHub drag-and-drop cannot handle this repository.** It silently skips dotted folders
like `.claude` and drops files from nested trees like `assets/gallery/thumbs`. Use git
from the command line.

---

## 10. SEO — what was done and what actually matters

**Built in:** unique titles and descriptions within Google's limits, canonical tags,
Open Graph, valid JSON-LD on every page (Organization with three dojo departments,
Person, FAQPage, BlogPosting, BreadcrumbList), sitemap, robots.txt, fast static pages,
no horizontal scroll on phones.

**Submitted:** sitemap accepted in Search Console; home page and the main classes page
pushed for indexing.

> The site is now **eligible** to rank. It does not by itself put anyone first.
> For "best karate class in Bangalore", the **Google Business Profile and reviews**
> matter more than anything in the HTML. Twenty honest reviews from current parents will
> move the needle further than any code change.

**Search Console note:** the property is `sc-domain:nipponfit.com`, a Domain property.
Sitemaps must be submitted as the **full URL** (`https://www.nipponfit.com/sitemap.xml`),
not just `sitemap.xml` — that gives "Invalid sitemap address".

**Business Profile note:** Google requires each listed location to have a permanent
physical presence with signage, staffed during published hours. A club renting mat time
at a shared venue may not qualify, and a suspended listing is worse than none. Panathur
is the safe one; Dravid CSE and Koramangala only if they genuinely qualify, otherwise add
them as service areas.

---

## 11. GoDaddy — what to keep paying for

| Product | Verdict |
|---|---|
| Domain `nipponfit.com` | **Keep.** Website, app and email all depend on it. |
| Professional Email | **Keep.** `contactus@nipponfit.com` is on the site and in the app. |
| Websites + Marketing Standard | **Cancel** — this was the old site builder, now replaced. |
| Website Builder Free 1-Page | Ignore, it is free and unused. |
| Full Protection | Optional. Recommended — losing the domain takes down all three. |

⚠️ Before cancelling the website plan, ask GoDaddy **in writing** whether it affects the
email account. They sometimes bundle them.

Hosting for the website, the app and the database is now **free** (Vercel + Supabase).

---

## 12. Still outstanding

1. **Push the app-side login change** — committed, never deployed (see §8).
2. **Real photographs of the three instructors** in gi against a plain wall. Darshan's
   current photo is cropped from a group shot and is noticeably softer than the others;
   Jeevan's and Arvind's are AI-generated images Pooja made, with the belts cropped off
   because the embroidery read 柔道 (judo) and gibberish. Real photos fix all of this —
   and Google Business Profile does not permit generated images.
3. **Google Business Profile** for Panathur, done thoroughly, then reviews from parents.
4. **Cancel the GoDaddy website plan** once the new site has run a few weeks.
5. *(Optional)* A separate page per dojo — `/dojo-panathur`, `/dojo-koramangala`,
   `/dojo-dravid-cse` — so each Business Profile can point at its own page instead of all
   three sharing `/locations`.

---

## 13. The other guides in this folder

| File | Covers |
|---|---|
| `START-HERE.md` | Day-to-day: previewing, editing, adding photos and articles |
| `PUBLISH.md` | The full deployment runbook |
| `UPLOAD-TO-GITHUB.md` | Why drag-and-drop fails and the git commands that work |
| `DNS-SETUP.md` | The DNS change, and how to undo it |
| `GODADDY-WHAT-TO-KEEP.md` | Renewals |
| `GOOGLE-SETUP.md` | Search Console and Business Profile, step by step |

All are excluded from the public site via `.vercelignore`.
