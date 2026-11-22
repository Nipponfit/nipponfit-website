# =====================================================================
# NIPPON FIT — one page per dojo
#
#   /dojo-panathur      Active Arena, Kadubeesanahalli (our Google profile)
#   /dojo-koramangala   The Koramangala Club
#   /dojo-dravid-cse    Dravid Centre for Sports Excellence, Yelahanka
#
# Each page is what Google shows for "karate classes in <area>". The
# address and map come from dojos.py. The words are below.
#
# Two rules from Renshi Pooja, kept on purpose:
#   - no class timings anywhere (parents are asked to message instead)
#   - her title is Renshi, never Sensei
# =====================================================================

import json

from build import page, cta_band, PHONE_DISPLAY, PHONE_LINK, WHATSAPP
from dojos import (DOJOS, DOJO, address_html, embed_url, directions_url,
                   maps_url, page_url, postal_ld, geo_ld)

WA = f"https://wa.me/{WHATSAPP}"


# ---------------------------------------------------------------------
# The words for each dojo
# ---------------------------------------------------------------------
CONTENT = {
    "panathur": {
        "title": "Karate Classes in Marathahalli &amp; Panathur | Nippon Fit",
        "description": "Karate, self defence and fitness at Active Arena on the Outer Ring Road, Kadubeesanahalli. Kids from 4, adults any age, competition squad. First class free.",
        "h1": "Karate Classes at Active Arena, Kadubeesanahalli",
        "intro": "Our main dojo, on the Outer Ring Road opposite Prestige Tech Park. "
                 "Kids from four, adults of any age, and the club's Elite competition squad.",
        "about": [
            "Active Arena is the home of Nippon Karate Club and the dojo most of our "
            "students train at. Classes run on an indoor matted floor, there is parking, "
            "and parents have space to sit and watch.",
            "Children and adults follow the same WKF-aligned syllabus as every Nippon Fit "
            "dojo: kihon, kata and kumite, graded belt by belt from white belt upwards. "
            "Students who want to compete join the <strong>Elite squad</strong>, trained "
            "here by Renshi Pooja Shri Shetty, an international karateka with a Tokyo "
            "Olympics 2020 standing of 181.",
            "Alongside karate, Active Arena is where we run Nippon Fit's self defence "
            "workshops, strength and conditioning, and weight loss programmes.",
        ],
        "teachers": [
            ("Darshan T V", "2nd Dan black belt, Goju-ryu and Shotokan. Teaches the regular karate classes."),
            ("Renshi Pooja Shri Shetty", "Founder and Chief Instructor. Leads the Elite competition squad."),
        ],
        "getting_here": "On the Outer Ring Road in Kadubeesanahalli, opposite Prestige "
                        "Tech Park and behind Croma. Look for Active Arena; the dojo is inside.",
        "faq": [
            ("Where exactly is the dojo?",
             "Active Arena, Outer Ring Road, opposite Prestige Tech Park, behind Croma, "
             "Kadubeesanahalli, Marathahalli, Bengaluru 560087. Tap Directions above to open it in Google Maps."),
            ("What age can my child start?",
             "From four years old. Adults are welcome to start at any age."),
            ("Can parents watch the class?",
             "Yes. There is space for parents to sit and watch, and you are welcome to "
             "watch a full class before you decide anything."),
            ("Is there parking?", "Yes, there is parking at Active Arena."),
            ("What are the class timings?",
             "Message us on WhatsApp or call " + PHONE_DISPLAY + " and we will share the "
             "batches that suit your child's age and level."),
            ("Is the first class free?",
             "Yes. The first class is free, with no obligation afterwards."),
        ],
    },

    "koramangala": {
        "title": "Karate Classes in Koramangala &amp; HSR Layout | Nippon Fit",
        "description": "Karate classes at The Koramangala Club, 6th Block, Koramangala, for club members and non-members. Kids from 4 and adults. WKF syllabus. First class free.",
        "h1": "Karate Classes at The Koramangala Club",
        "intro": "Nippon Karate Club inside The Koramangala Club, 6th Block. "
                 "Open to club members and non-members alike.",
        "about": [
            "Our Koramangala dojo brings the full Nippon Karate Club syllabus to central "
            "Bengaluru. It suits families in Koramangala, HSR Layout, Indiranagar, Ejipura "
            "and BTM Layout who would rather not cross the city for a good karate class.",
            "Training follows the same WKF-aligned syllabus and grading standard as all our "
            "dojos: kihon, kata and kumite, from white belt upwards. Students who show "
            "promise can move up to the club's Elite competition squad.",
            "You do <strong>not</strong> need to be a member of The Koramangala Club to "
            "train with us. Members and non-members are both welcome.",
        ],
        "teachers": [
            ("Darshan T V", "2nd Dan black belt, Goju-ryu and Shotokan."),
            ("Renshi Pooja Shri Shetty", "Founder and Chief Instructor. International karateka, Tokyo Olympics 2020 standing of 181."),
        ],
        "getting_here": "The Koramangala Club, CA-17, 6th Cross Road, 6th Block, "
                        "Koramangala. Tell the club reception you are here for Nippon Karate Club.",
        "faq": [
            ("Do I need to be a member of The Koramangala Club?",
             "No. Club members and non-members can both join. Message us and we will "
             "tell you the fee that applies to you."),
            ("Where exactly is it?",
             "The Koramangala Club, CA-17, 6th Cross Road, 6th Block, Koramangala, "
             "Bengaluru 560095. Tap Directions above to open it in Google Maps."),
            ("What age can my child start?",
             "From four years old. Adults are welcome to start at any age."),
            ("What are the class timings?",
             "Message us on WhatsApp or call " + PHONE_DISPLAY + " and we will share the "
             "batches at Koramangala."),
            ("Is the first class free?",
             "Yes. The first class is free, with no obligation afterwards."),
        ],
    },

    "yelahanka": {
        "title": "Karate Classes in Yelahanka | Dravid Centre for Sports Excellence | Nippon Fit",
        "description": "Karate classes at the Dravid Centre for Sports Excellence, Yelahanka, taught by Renshi Pooja Shri Shetty. Kids from 4, adults, competition training. First class free.",
        "h1": "Karate Classes at the Dravid Centre for Sports Excellence, Yelahanka",
        "intro": "A national-standard sports facility in Yelahanka, shared with some of "
                 "India's leading athletes, and our dojo for north Bengaluru.",
        "about": [
            "Nippon Karate Club has its own dedicated floor, fully set up as a dojo, "
            "inside the Padukone-Dravid Centre for Sports Excellence in Yelahanka. It is the closest of our dojos for families in Yelahanka, Jakkur, "
            "Hebbal, Sahakar Nagar, Thanisandra and Devanahalli.",
            "This is where much of our competition preparation happens, and where we "
            "hosted Tokyo Olympic bronze medallist Ugur Aktas for an elite kumite "
            "seminar, a first for India. Beginners train here too, on the same "
            "WKF-aligned syllabus as every Nippon Fit dojo.",
            "Classes are taught by Renshi Pooja Shri Shetty, an international karateka "
            "with a Tokyo Olympics 2020 standing of 181, together with Jeevan J.",
        ],
        "teachers": [
            ("Renshi Pooja Shri Shetty", "Founder and Chief Instructor. International karateka, Tokyo Olympics 2020 standing of 181."),
            ("Jeevan J", "2nd Dan black belt, licensed referee and judge, Karnataka State and National Open medallist."),
        ],
        "getting_here": "Our dojo is on its own floor inside the Padukone-Dravid Centre for "
                        "Sports Excellence campus. Tap Directions: it goes straight to our building.",
        "faq": [
            ("Is Yelahanka only for competition students?",
             "No. Beginners from age four train here too. Competition students simply "
             "get the benefit of a national-standard facility."),
            ("Where exactly is it?",
             "Nippon Karate Club, Padukone-Dravid Centre for Sports Excellence, Bettahalsoor, "
             "Yelahanka, Bengaluru 562157. Tap Directions above to open it in Google Maps."),
            ("Who teaches at Yelahanka?",
             "Renshi Pooja Shri Shetty, our founder and chief instructor, with Jeevan J."),
            ("What are the class timings?",
             "Message us on WhatsApp or call " + PHONE_DISPLAY + " and we will share the "
             "batches at Yelahanka."),
            ("Is the first class free?",
             "Yes. The first class is free, with no obligation afterwards."),
        ],
    },
}


def _faq_ld(faq):
    items = [
        {"@type": "Question", "name": q,
         "acceptedAnswer": {"@type": "Answer", "text": a.replace("<strong>", "").replace("</strong>", "")}}
        for q, a in faq
    ]
    return json.dumps({"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": items},
                      indent=2, ensure_ascii=False)


def _schema(d, c):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "SportsActivityLocation",
  "@id": "{page_url(d)}#dojo",
  "name": "Nippon Karate Club \\u2014 {d["name"]}",
  "description": "{c["description"]}",
  "url": "{page_url(d)}",
  "image": "https://www.nipponfit.com/assets/hero-dojo.jpg",
  "telephone": "+91-9945616005",
  "email": "contactus@nipponfit.com",
  "address": {postal_ld(d)},
  "geo": {geo_ld(d)},
  "hasMap": "{maps_url(d)}",
  "areaServed": {json.dumps([{"@type": "Place", "name": n} for n in d["near"]])},
  "parentOrganization": {{ "@id": "https://www.nipponfit.com/#organisation" }},
  "sport": "Karate"
}}
</script>
<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.nipponfit.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "Locations", "item": "https://www.nipponfit.com/locations" }},
    {{ "@type": "ListItem", "position": 3, "name": "{d["name"]}", "item": "{page_url(d)}" }}
  ]
}}
</script>
<script type="application/ld+json">
{_faq_ld(c["faq"])}
</script>
""".replace("&amp;", "&")


def _dojo_page(d):
    c = CONTENT[d["key"]]
    about = "\n".join(f"          <p>{p}</p>" for p in c["about"])
    teachers = "\n".join(
        f'        <article class="card"><h3>{n}</h3><p>{t}</p></article>'
        for n, t in c["teachers"])
    faq = "\n".join(f"        <h3>{q}</h3>\n        <p>{a}</p>" for q, a in c["faq"])
    areas = " &middot; ".join(d["near"])
    others = "\n".join(
        f'        <li><a href="/{o["slug"]}">{o["label"]}</a></li>'
        for o in DOJOS if o is not d)
    wa_text = f"Hello%20Nippon%20Fit%2C%20I%20would%20like%20a%20free%20demo%20class%20at%20{d['name'].replace(' ', '%20')}."

    page(
        slug=d["slug"],
        title=c["title"],
        description=c["description"],
        og_image="/assets/hero-dojo.jpg",
        extra_head=_schema(d, c),
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      <p class="crumbs"><a href="/">Home</a> &nbsp;/&nbsp; <a href="/locations">Locations</a> &nbsp;/&nbsp; {d["name"]}</p>
      <h1>{c["h1"]}</h1>
      <p>{c["intro"]}</p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-2" style="gap:clamp(32px,5vw,64px);align-items:start">

        <div class="prose" style="max-width:none">
          <h2 class="mt-0">About this dojo</h2>
{about}
        </div>

        <article class="branch">
          <iframe class="branch-map"
                  src="{embed_url(d)}"
                  title="Map of {d["label"]}" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Address</h3>
            <address>{address_html(d)}</address>
            <p>{c["getting_here"]}</p>
            <p style="display:flex;flex-wrap:wrap;gap:10px;margin:8px 0 0">
              <a class="btn btn-outline" href="{directions_url(d)}" target="_blank" rel="noopener">Directions</a>
              <a class="btn btn-primary" href="{WA}?text={wa_text}" target="_blank" rel="noopener">WhatsApp us</a>
            </p>
          </div>
        </article>

      </div>
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Instructors</span>
        <hr class="rule">
        <h2>Who teaches here</h2>
      </div>
      <div class="grid grid-2 grid-gap">
{teachers}
      </div>
      <p class="text-centre" style="margin-top:28px"><a class="link-more" href="/instructors">Meet all our instructors</a></p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Areas we serve</span>
        <hr class="rule">
        <h2>Where students travel from</h2>
      </div>
      <p class="text-centre" style="max-width:46em;margin:0 auto;color:var(--ink-soft)">{areas}</p>
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap-narrow">
      <div class="section-head">
        <span class="eyebrow">Questions</span>
        <hr class="rule">
        <h2>What parents ask about this dojo</h2>
      </div>
      <div class="prose" style="max-width:none">
{faq}
      </div>
      <div class="prose" style="max-width:none;margin-top:36px">
        <h3>Our other dojos</h3>
        <ul>
{others}
        </ul>
      </div>
    </div>
  </section>

{cta_band(
    "Come and watch a class",
    f"Book a free first class at {d['name']}. Sit at the side, watch, and decide afterwards. No obligation.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Book a free demo class</a>'
    f'<a class="btn btn-ghost" href="tel:{PHONE_LINK}">Call {PHONE_DISPLAY}</a>'
)}
""",
    )


def build():
    print("Dojo pages:")
    for d in DOJOS:
        _dojo_page(d)
