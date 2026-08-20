# Google — Search Console and Business Profile

These are **two completely different Google products**, and it is easy to mix them up:

| | What it does | Where the dojos go |
|---|---|---|
| **Search Console** | Tells you how the website performs in search, and lets you hand Google your list of pages | One entry for the whole domain. No dojos here. |
| **Business Profile** | The map pin, the phone number, the reviews, the opening hours | **This** is where locations live |

Search Console first — it is quick, and it is already half done.

---

# Part 1 — Search Console

## You are already verified. Skip the DNS step.

Your address bar reads:

```
search.google.com/search-console?resource_id=sc-domain%3Anipponfit.com
```

The **`sc-domain:`** part means this is a **Domain property**, and a Domain property can
only exist if the domain has already been verified through DNS. That matches the
`google-site-verification` record I found sitting in your GoDaddy DNS.

**There is nothing to verify. It was done at some point in the past and still holds.**

## Which of the two properties to use

Your list shows two:

| Property | Use it? |
|---|---|
| **`nipponfit.com`** | **Yes — use this one.** Domain property. Covers `nipponfit.com`, `www.nipponfit.com`, `app.nipponfit.com`, http and https, everything. |
| `https://nipponfit.com/` | Older, narrower. Only covers that exact address. Leave it, it does no harm. |

Always pick **`nipponfit.com`** from that dropdown.

## Submit the sitemap — the one job that matters today

A sitemap is simply a list of every page, handed to Google so it does not have to find
them by guesswork. Yours is live and lists **15 pages**.

1. Select **`nipponfit.com`** in the property dropdown
2. In the left menu, under **Indexing**, click **Sitemaps**
3. In the "Add a new sitemap" box, type the **whole address**:

   ```
   https://www.nipponfit.com/sitemap.xml
   ```

4. Click **Submit**

### Why the whole address, and not just `sitemap.xml`

There are two kinds of Search Console property, and they behave differently here:

| Property type | What to type |
|---|---|
| **Domain** — `nipponfit.com` — what you have | The **complete address**: `https://www.nipponfit.com/sitemap.xml` |
| **URL prefix** — `https://nipponfit.com/` | Just `sitemap.xml`, because the front part is already shown beside the box |

A Domain property covers `nipponfit.com`, `www.nipponfit.com` and `app.nipponfit.com`
all at once, so Google has no way to guess which one you mean. It needs to be told in
full. Typing only `sitemap.xml` gives **"Invalid sitemap address"**.

### Use the `www` version

Type `www.nipponfit.com`, not `nipponfit.com`. Both work — `nipponfit.com/sitemap.xml`
forwards to the www one — but giving Google the address that answers directly avoids a
needless redirect. I have checked it: it returns the file, correctly labelled as XML.

**What success looks like:** a row appears saying **Success**, with "15 discovered
pages". It may briefly say "Couldn't fetch" — wait a few hours and refresh before
worrying.

## Then push the home page to the front of the queue

1. At the top of the page, paste this into the **"Inspect any URL"** box:

   ```
   https://www.nipponfit.com/
   ```

2. Press Enter and wait for it to finish
3. Click **Request Indexing**

That asks Google to look at the new home page now rather than whenever it gets round to
it. You can do the same for `/karate-classes-bangalore` — your most important page for
search. There is a daily limit of about ten, so do not bother with all fifteen.

## What you will see over the next few weeks

- **Days 1–3:** the sitemap shows Success
- **Week 1:** pages start appearing under **Indexing → Pages**
- **Weeks 2–6:** searches start showing up under **Performance**

The 67 clicks already on your graph are from the old site on this same domain. That
history carries over, which is genuinely helpful — you are not starting from zero.

---

# Part 2 — Business Profile, and the honest position on three dojos

## Where to go

**business.google.com** — not Search Console. Different product, different login area,
same Google account.

## To add another location

1. Go to **business.google.com**
2. Click the **business name** dropdown at the top, or **Businesses** in the side menu
3. Click **Add business** → **Add single business**
4. Enter the name, category (**Karate school**), and the address of the second dojo
5. Choose a verification method — usually a postcard to that address, a phone call, or a
   short video showing the premises
6. Repeat for the third

## Before you do — read this

I suggested three profiles earlier. That was too simple an answer, and I would rather
correct it now than have you get a listing suspended.

**Google's rules require each listed location to have a permanent physical presence,
with signage, staffed during the hours you publish.** A club that rents mat time at a
shared sports facility for a few hours a week does not automatically qualify. Google
specifically watches for listings at shared or rented venues, and a listing judged not to
qualify can be suspended — which is worse than never having created it, because
suspensions are slow and tedious to appeal.

So, honestly:

**Active Arena, Panathur** — your main dojo. If you have a permanent presence there,
signage, and consistent hours, this is a straightforward listing. **Do this one first
and do it properly.**

**Dravid CSE and Koramangala Club** — only create these if the same is genuinely true at
each: your own signage, and consistent published hours when somebody from the club is
there. If it is a few hours of booked mat time a week, do not list it separately.

**If they do not qualify:** add those areas as **service areas** on your main listing
instead, and give each one a proper mention on the Locations page of the website — which
is already done. You will still show up for "karate classes Koramangala" through the
website; you simply will not have a separate map pin.

## What actually moves you up the rankings

Once the main profile is live, this is the order of impact:

1. **Reviews.** Ask every current parent. Twenty honest reviews mentioning karate and
   Bangalore will do more than anything else on this list.
2. **Photographs.** Ten or more real ones — the dojo, a class in progress, the students
   with their trophies. You have plenty now. *(Note: generated images are not permitted
   here, which is another reason to take the real instructor photographs.)*
3. **Complete every field.** Hours, category, phone, website `https://www.nipponfit.com`,
   description.
4. **Posts.** A short update every few weeks — a grading, a tournament result, a new
   batch starting.

Write the club name, address and phone number **identically** on the profile, the
website, and any directory you list in. Google cross-checks those, and small differences
weaken you.
