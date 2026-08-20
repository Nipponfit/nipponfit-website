# The Nippon Fit website — start here

This folder is the new **www.nipponfit.com**. It replaces the GoDaddy Website
Builder site.

Everything is plain HTML, CSS and JavaScript files. There is no WordPress, no
plugins, no monthly bill, and nothing that can break on its own. Exactly the same
approach as the app.

---

## 1. What is in here

| File or folder | What it is |
|---|---|
| `index.html` | Home page |
| `karate-classes-bangalore.html` | The five programmes — **the page built to rank on Google** |
| `nippon-karate-club.html` | About Us, the Founder, and the **Registration Form** |
| `instructors.html` | You, Dashant, Jeevan and Arvind |
| `gallery.html` | Achievement photos, rotating every 15 seconds |
| `blog.html` + `blog/` | The blog index and the four articles |
| `locations.html` | The three dojos, each with a live map |
| `contact.html` | General enquiry form that lands in your WhatsApp |
| `login.html` | Nippon Karate Club Portal login |
| `404.html` | Shown if somebody follows an old or broken link |
| `css/styles.css` | Every colour, size and spacing on the site, in one file |
| `js/` | The menu, the login handover, the two forms, the gallery |
| `assets/` | Logo, seal, photographs, affiliation badges |
| `assets/gallery/` | **Put achievement photos here** |
| `robots.txt`, `sitemap.xml` | The two files Google looks for |
| `vercel.json` | Hosting settings — clean web addresses, redirects, security |
| `tools/` | The preview server and the page builder |

**Important:** the `.html` pages are written by `tools/build.py`. If you edit a page
by hand and then run the builder, your edit is overwritten. Change the words in
`tools/pages_main.py` or `tools/pages_blog.py` instead, then run the builder.

---|---|
| `index.html` | The home page |
| `karate-classes-bangalore.html` | The six programmes — **this is the page built to rank on Google** |
| `nippon-karate-club.html` | About the club, affiliations, and your own profile |
| `instructors.html` | You, Dashan T V, Jeevan J and Arvind Achar|
| `locations.html` | The three dojos, each with a live map |
| `registration.html` | **Book a free demo class** — where every orange button on the site leads |
| `contact.html` | General enquiry form that lands in your WhatsApp |
| `parent-login.html` | Parent portal sign-in, hands over to the app |
| `404.html` | Shown if somebody follows an old or broken link |
| `css/styles.css` | Every colour, size and spacing on the site, in one file |
| `js/` | Four small scripts: the menu, the login handover, the contact form, the registration form |
| `assets/` | Logo, seal, photographs |
| `robots.txt`, `sitemap.xml` | The two files Google looks for |
| `vercel.json` | Hosting settings — clean web addresses, redirects, security |
| `tools/` | The preview server and the page builder (explained below) |

---

## 2. To see the site on your own computer, before it goes live

Open a terminal in this folder and type:

```bash
python tools/serve.py
```

Then open **http://localhost:4180** in your browser.

**What success looks like:** the home page loads with the navy hero band reading
"Karate Classes in Bangalore for Children and Adults", and the menu at the top
works. Press `Ctrl+C` in the terminal to stop it.

---

## 3. To put it live

The site needs to be hosted somewhere. **Vercel** is the recommendation — it is
where the app already lives, it is free at this size, and it is the fastest
option for Google's speed scores.

**Your domain stays at GoDaddy. You are not moving the domain, only changing
where it points.**

### Step 1 — put the files on GitHub

1. Go to **github.com/Nipponfit** and click **New** to create a repository.
2. Name it `nipponfit-website`. Leave it Public. Click **Create repository**.
3. Upload every file in this folder to it (drag the whole folder onto the
   upload page).

### Step 2 — connect it to Vercel

1. Go to **vercel.com** → **Add New** → **Project**.
2. Pick the `nipponfit-website` repository and click **Import**.
3. Leave every setting as it is — there is nothing to build. Click **Deploy**.
4. **What success looks like:** after about thirty seconds you get a web address
   like `nipponfit-website.vercel.app`. Open it. It should look exactly like
   your local preview.

### Step 3 — point nipponfit.com at it

1. In Vercel, open the project → **Settings** → **Domains**.
2. Add `nipponfit.com`, then add `www.nipponfit.com`.
3. Vercel will show you two DNS records to create. Go to **GoDaddy → My Products
   → Domains → nipponfit.com → DNS**, and set them exactly as Vercel says.
   Typically:
   - an **A** record for `@` pointing at `76.76.21.21`
   - a **CNAME** record for `www` pointing at `cname.vercel-dns.com`
4. Delete or replace the old GoDaddy Website Builder records for `@` and `www`,
   or the old site will keep showing.
5. **What success looks like:** within an hour or two (occasionally up to a day),
   typing `nipponfit.com` shows the new site with a padlock in the address bar.

> **Before you do Step 3:** the old GoDaddy site goes dark the moment DNS
> switches. Check the `.vercel.app` address looks right first. Nothing is lost
> either way — GoDaddy keeps your old site, and you can point the DNS back at it
> at any time.

---

## 4. Turning on Google — this is the part that decides your ranking

The website is built correctly for search. **That gets you eligible to rank; it
does not by itself put you first.** For "best karate class in Bangalore" the
biggest factor by far is your **Google Business Profile and your reviews**, not
your website. Do these five things, in this order:

### 4a. Google Business Profile (biggest single win)

1. Go to **google.com/business** and claim or create a profile for
   **Nippon Karate Club**.
2. Create **three** profiles, one per dojo — Panathur, Dravid CSE, Koramangala.
   Google ranks by distance from the searcher, so three pins beat one.
3. On each: category **Karate school**, phone `+91 99456 16005`, website
   `https://www.nipponfit.com`, real photographs, and your class hours.
4. **Ask every current parent for a review.** Twenty honest reviews mentioning
   "karate" and "Bangalore" will move you further up than anything I can write
   into the HTML. This is the single highest-value thing you can do.

### 4b. Google Search Console

1. Go to **search.google.com/search-console** and add `www.nipponfit.com`.
2. Verify it (Vercel makes this easy — it will offer a DNS or HTML method).
3. Go to **Sitemaps** and submit `sitemap.xml`.
4. **What success looks like:** within a week, Search Console shows your pages
   under "Pages → Indexed".

### 4c. Get listed elsewhere

Justdial, Sulekha, Practo-style local directories, the Karate India Organization
member list, and the Akhila Karnataka association site. Each one that links back
to nipponfit.com makes Google trust the site more. Make sure the name, address
and phone number are **written identically** everywhere — Google matches on that.

### 4d. Keep adding pages

Every tournament result, every grading day, every new batch is a page worth
writing. A site that grows outranks a site that sits still. Send me the content
and I will add the pages.

### 4e. Be patient and realistic

A new site on a domain Google has already seen usually starts showing up for
"karate classes Panathur" or "karate classes Bellandur" within a few weeks, and
takes a few months to compete for the broad "karate classes in Bangalore". Any
agency promising you the top spot in a fortnight is charging you for something
they cannot deliver.

---

## 5. Making changes

Everything on the site is written by one command:

```bash
python tools/build.py
```

**To change words on a page** — open `tools/pages_main.py` (home, programmes, karate
club, instructors, locations, contact, login) or `tools/pages_blog.py` (blog and
gallery) in Notepad, find the sentence, change it, save, then run the builder.

**To change the menu, the footer, the phone number or the address** — they live once
at the top of `tools/build.py`. Change them there and they change on every page.

**To change a colour or a font** — the top of `css/styles.css`, in the block marked
`:root`. Nothing else needs touching, and the builder is not involved.

**To add an achievement photo to the gallery** — save the picture into
`assets/gallery/` and add one line to the list at the top of `js/gallery.js`, copying
the pattern already there. It appears in both the slideshow and the grid underneath.
No rebuild needed.

**To change how long each gallery photo stays up** — it is 15 seconds. That number is
in `tools/pages_blog.py`, on the line reading `data-interval="15000"`.

**To add a blog article** — copy one of the entries in `ARTICLES` in
`tools/pages_blog.py`, change the slug, title, date, summary and body, then run the
builder. Add the new address to `sitemap.xml` too.

**To add an instructor photograph** — save it into `assets/` as
`instructor-dashant.jpg` (or `-jeevan`, `-arvind`), then find that instructor in
`tools/pages_main.py`; the exact line to swap in is written in a comment right above.

---

## 6. How registration works

The **Registration Form** sits on the Nippon Karate Club page, straight after the
Founder section — the same place it was on the old website. Every "Book a free demo
class" button on the site leads there.

It asks for full name, date of birth, gender, contact number, parent's name, email,
address, blood group, preferred dojo, programme and medical conditions. When the
person presses the button it arrives in your WhatsApp as a tidy message they only have
to press send on. There is an email option underneath.

Nothing is stored on the website, so there is no inbox to check and nothing to
maintain.

**Age is set to four years and above.** The form works the age out from the date of
birth, and if it is under four it stops them politely and asks them to call you. To
change that minimum, open `js/registration.js` and edit `var MINIMUM_AGE = 4;`.

### One change I made deliberately, and why

The old form asked for an **Aadhaar number** and for uploads of a photograph and an
Aadhaar copy. I have not carried those across, and I would advise against putting them
back.

A website built from plain files has nowhere safe to receive or keep documents like
that, and routing them through WhatsApp or email is worse rather than better — Aadhaar
numbers sitting in a chat thread are exactly what the Digital Personal Data Protection
rules are concerned with. The form now asks people to **bring the photograph and
Aadhaar copy to the dojo on the first visit**, where you take them in person. You end
up with the same paperwork, and none of the risk.

(Worth knowing: the old form never worked anyway. It was set to send to a file called
`submit.php` that does not exist on GoDaddy, so anything anyone typed into it went
nowhere.)

**If you already have a JotForm registration form**, send me the link and I will swap
it in — there is a comment marked `JOTFORM` in `tools/pages_main.py` showing exactly
where it goes.

---

## 7. The blog

**Seven articles are live.**

Your three from the old website, carried across word for word:

1. **Martial Arts Styles** (20 Apr 2023) — all 185 styles, with the Karate and Kung Fu
   sub-lists intact
2. **Origin of Karate-Do** (31 Jan 2023) — including the history timeline as a proper
   table
3. **Full Body Workout** (31 Jan 2023) — the 7-minute tabata sequence

Your old blog addresses had an extra `/f/` in them
(`nipponfit.com/blog/f/martial-arts-styles`). Anyone following an old link is now
forwarded automatically to the new address, so nothing breaks.

And four technique analyses from your training documents:

4. **Kumite Analysis** — your own competition footage across two tournaments
5. **Reverse Punch** — the wrong and right mechanics, side by side
6. **Kumite Stance** — your stance against an elite competitor's
7. **Chudan Mawashi Geri** — why judges reward one kick and not another

Those last four are the ones I built before you sent the real three. They are good
material and they are doing no harm, but say the word and I will take any of them down.
If you have the photographs or video stills that went with them, send those over —
they would be considerably stronger with the images they were written about.

**To add an article**, copy an entry in `ARTICLES` in `tools/pages_blog.py`, change the
slug, title, date, summary and body, run the builder, and add the address to
`sitemap.xml`.

---

## 8. The gallery photographs

**All 44 are in.** Here is what I did with the 58 files you saved:

| | |
|---|---|
| Files you uploaded | 58 |
| Exact duplicates removed | 6 |
| Same photo re-sent through WhatsApp at a smaller size | 5 removed, the sharper copy kept |
| Already used elsewhere on the site | 2 removed |
| Moved to the Origin of Karate-Do article | 1 (the "kara te" characters graphic) |
| **Photographs now in the gallery** | **44** |

Every one has been shrunk for the web, straightened where the phone had
recorded it sideways, given a proper name, and captioned. **65 MB became 12 MB** —
without that, the gallery page would have taken close to a minute to load on a phone.

The Ugur Aktas seminar leads the order, then international, then national, then state,
then the club and the students.

### Where the originals are

`F:\Nipponfit\Gallery_Originals\` — deliberately **outside** the website folder, so 65 MB
of phone photographs never get uploaded to the internet. Nothing was deleted; the
originals are all still there at full size.

### To add more photographs later

1. Put the new pictures into `F:\Nipponfit\Gallery_Originals\`
2. Open `tools/curate_gallery.py` and add a line for each in the `PHOTOS` list, copying
   the pattern: original file name, new name, title, caption.
3. Run:

```bash
python tools/curate_gallery.py
```

That shrinks them, makes the small versions for the grid, and updates `js/gallery.js`
for you. **Or just drop them in and tell me** — I will caption and order them.

### How it displays

- **Home page** — the first 10, moving on by itself every 15 seconds
- **Gallery page** — the full slideshow of all 44, with a grid of every photograph
  underneath. Clicking any square jumps the slideshow to it.

---

## 9. Instructor photographs

The Instructors page now picks photographs up **automatically**. There is no HTML to
edit — if the file is there, the photo shows; if it is not, the initials show instead.

### To add them

1. Save the photographs into `F:\Nipponfit\Instructor_Originals\`, named after the
   instructor in lower case, exactly:

   `darshan.jpg`   `arvind.jpg`   `jeevan.jpg`

2. Run these two commands:

```bash
python tools/prepare_instructor_photos.py
```

```bash
python tools/build.py
```

The first crops each photo to the same shape, keeps the face in the right part of the
frame rather than dead centre, evens out the colour so a scanned passport photo does not
sit oddly next to a phone snap, and saves a web-sized copy. The second rebuilds the page.

**What success looks like:** open `/instructors` and all four cards show a face instead
of initials.

### On karate gi photographs

I cannot put someone into a karate gi. Editing a real person's photograph to show them
wearing clothes they were not wearing is not something I will do — on a page whose whole
job is to tell parents the truth about who will be teaching their child, an invented
photograph is the wrong place to start.

The passport-style headshots you sent will look perfectly good once tidied and matched
up. But if you would rather have them in gi, the answer is a camera, not editing: stand
them against a plain dojo wall in their gi and belt, take it in daylight, chest upwards,
and send those instead. It takes five minutes at the start of a class and it will look
considerably better than any headshot.

---

## 10. The instructor photographs — all four are in

| | |
|---|---|
| Pooja | competition photograph |
| Darshan T V | cropped from the Ugur Aktas seminar group shot |
| Jeevan J | karate gi, cropped above the belt |
| Arvind Acharya | karate gi, cropped above the belt |

The gi picture arrived saved as `gi-pair.jpg.png` — a double extension, which Windows
adds without showing you. The tool now ignores extra extensions, so that will not catch
you out again.

**The belt is gone from both gi photographs.** Everything below chest level is discarded
before any other step, so the writing on the belt never reaches the website at all.

If you want more or less of the gi showing, open `tools/prepare_instructor_photos.py`,
find the `BELT_CROP` block near the top, and change `0.74`. Lower cuts higher up; higher
keeps more. Then run the two commands again.

### On Darshan's photograph

His is cropped out of a group photo that had already been through WhatsApp, so the piece
of it that is him is only about 200 pixels across. I have improved it as far as the
processing can go — enlarging in stages with an unsharp mask rather than one jump — and
it is noticeably sharper than it was. But there is a limit: you cannot recover detail
that was never in the file.

**The only real fix is a photograph taken of him directly.** Which brings us to:

---

## 11. The five minutes that would finish this page

All three of them against a plain dojo wall, in their own gi and belts, one photograph
each. Daylight from a window, phone held upright, chest upwards.

Save them as `darshan.jpg`, `arvind.jpg` and `jeevan.jpg` in
`F:\Nipponfit\Instructor_Originals\`, then run:

```bash
python tools/prepare_instructor_photos.py
```

```bash
python tools/build.py
```

Worth doing for two reasons. Darshan's card becomes properly sharp. And those
photographs are what your **Google Business Profile** needs — which, with your reviews,
is what actually decides whether you come up first for "karate classes in Bangalore".
---

## 12. If the site looks unchanged after an edit

**It is almost always the browser, not the website.** Your browser keeps a copy of each
page so it loads faster, and after a change it will happily show you the old copy.

**Press `Ctrl` + `Shift` + `R`** (hold Ctrl and Shift, then press R). That forces the
browser to throw its copy away and fetch the page fresh. An ordinary refresh with `F5`
is often not enough.

I have also changed the preview server so it now tells your browser never to keep a copy
at all. For that to take effect the server has to be restarted: press `Ctrl` + `C` in the
terminal where it is running, then start it again with

```bash
python tools/serve.py
```

After that, a normal refresh will always show the current version.

If you have hard-refreshed and something still looks wrong, tell me and I will check the
file itself — it is easy for me to confirm exactly what is on the page.

---

## 13. One last thing worth a glance

The gallery captions. I wrote all 44 of them from what I could read on the banners in
each photograph, so a championship name could be wrong somewhere. Open the Gallery page,
scroll the grid, and if one is misnamed tell me which and I will correct it.

*(Confirmed 20 August 2026: the medals are from the Karnataka State Championship, and the
credentials belong to Jeevan J and Arvind Acharya. Both are correct on the site.)*
