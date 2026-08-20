# =====================================================================
# NIPPON FIT — the main pages
#
# Edit the words in here, then run:  python tools/build.py
# =====================================================================

from build import (page, crumbs, breadcrumb_ld, cta_band, ROOT,
                   PHONE_DISPLAY, PHONE_LINK, WHATSAPP, EMAIL)


WA = f"https://wa.me/{WHATSAPP}"


# =====================================================================
# Shared blocks
# =====================================================================

AFFILIATION_STRIP = """
  <section class="section section-warm" style="padding-top:44px;padding-bottom:44px">
    <div class="wrap">
      <p class="text-centre" style="font-size:11.5px;letter-spacing:.18em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:26px">
        Affiliated to
      </p>
      <div style="display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:38px 52px">
        <img src="/assets/affiliations/ioc.png" alt="International Olympic Committee" height="46" style="height:46px;width:auto;opacity:.8">
        <img src="/assets/affiliations/wkf.jpg" alt="World Karate Federation" height="46" style="height:46px;width:auto;opacity:.8">
        <img src="/assets/affiliations/akf.jpg" alt="Asian Karate Federation" height="46" style="height:46px;width:auto;opacity:.8">
        <img src="/assets/affiliations/kio.jpg" alt="Karate India Organization" height="46" style="height:46px;width:auto;opacity:.8">
        <img src="/assets/affiliations/akska.jpg" alt="Akhila Karnataka Sports Karate Association" height="46" style="height:46px;width:auto;opacity:.8">
      </div>
    </div>
  </section>
"""


def build():
    print("Main pages:")

    # =================================================================
    # HOME
    #
    # The page opens with NIPPON FIT and what Nippon Fit offers. Nippon
    # Karate Club comes later, as one part of it.
    # =================================================================
    page(
        slug="",
        title="Nippon Fit — Karate, Fitness &amp; Self Defence in Bangalore",
        description="Karate training, self defence, strength and conditioning, weight loss and wellness in Bengaluru. Children from four, adults any age. First class free.",
        extra_scripts='<script src="/js/gallery.js" defer></script>\n',
        extra_head="""<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@graph": [
    {
      "@type": ["HealthAndBeautyBusiness", "SportsActivityLocation"],
      "@id": "https://www.nipponfit.com/#organisation",
      "name": "Nippon Fit",
      "alternateName": ["Nippon Karate Club", "Nippon Karate Club Bangalore"],
      "description": "Karate training, self defence, strength and conditioning, weight loss and wellness programmes in Bengaluru. Home of the WKF-affiliated Nippon Karate Club.",
      "url": "https://www.nipponfit.com/",
      "logo": "https://www.nipponfit.com/assets/logo.png",
      "image": "https://www.nipponfit.com/assets/founder-pooja.jpg",
      "telephone": "+91-9945616005",
      "email": "contactus@nipponfit.com",
      "priceRange": "$$",
      "areaServed": [
        { "@type": "City", "name": "Bengaluru" },
        { "@type": "Place", "name": "Panathur" },
        { "@type": "Place", "name": "Bellandur" },
        { "@type": "Place", "name": "Whitefield" },
        { "@type": "Place", "name": "Marathahalli" },
        { "@type": "Place", "name": "Koramangala" }
      ],
      "address": {
        "@type": "PostalAddress",
        "streetAddress": "Active Arena, Munnireddy Layout, Panathur",
        "addressLocality": "Bengaluru",
        "addressRegion": "Karnataka",
        "addressCountry": "IN"
      },
      "sameAs": [
        "https://www.facebook.com/Nipponfit",
        "https://www.instagram.com/nippon_fit",
        "https://www.linkedin.com/company/nipponfit"
      ],
      "memberOf": [
        { "@type": "Organization", "name": "World Karate Federation" },
        { "@type": "Organization", "name": "Asian Karate Federation" },
        { "@type": "Organization", "name": "Karate India Organization" },
        { "@type": "Organization", "name": "Akhila Karnataka Sports Karate Association" }
      ],
      "founder": { "@id": "https://www.nipponfit.com/nippon-karate-club#pooja" },
      "department": [
        {
          "@type": "SportsActivityLocation",
          "name": "Nippon Karate Club \\u2014 Active Arena, Panathur",
          "telephone": "+91-9945616005",
          "address": { "@type": "PostalAddress", "streetAddress": "Active Arena, Munnireddy Layout, Panathur", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN" },
          "hasMap": "https://www.google.com/maps/search/?api=1&query=Active+Arena+Munnireddy+Layout+Panathur+Bengaluru"
        },
        {
          "@type": "SportsActivityLocation",
          "name": "Nippon Karate Club \\u2014 Dravid Centre for Sports Excellence",
          "telephone": "+91-9945616005",
          "address": { "@type": "PostalAddress", "streetAddress": "Dravid Centre for Sports Excellence", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN" },
          "hasMap": "https://www.google.com/maps/search/?api=1&query=Dravid+Centre+for+Sports+Excellence+Bengaluru"
        },
        {
          "@type": "SportsActivityLocation",
          "name": "Nippon Karate Club \\u2014 Koramangala Club",
          "telephone": "+91-9945616005",
          "address": { "@type": "PostalAddress", "streetAddress": "Koramangala Club, Koramangala", "addressLocality": "Bengaluru", "addressRegion": "Karnataka", "addressCountry": "IN" },
          "hasMap": "https://www.google.com/maps/search/?api=1&query=Koramangala+Club+Bengaluru"
        }
      ],
      "hasOfferCatalog": {
        "@type": "OfferCatalog",
        "name": "Nippon Fit programmes",
        "itemListElement": [
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Karate Training" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Self Defence Training" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Strength and Conditioning" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Weight Loss Programme" } },
          { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Wellness and Fitness Programmes" } }
        ]
      }
    },
    {
      "@type": "WebSite",
      "@id": "https://www.nipponfit.com/#website",
      "url": "https://www.nipponfit.com/",
      "name": "Nippon Fit",
      "publisher": { "@id": "https://www.nipponfit.com/#organisation" },
      "inLanguage": "en-IN"
    },
    {
      "@type": "FAQPage",
      "mainEntity": [
        {
          "@type": "Question",
          "name": "What programmes does Nippon Fit offer?",
          "acceptedAnswer": { "@type": "Answer", "text": "Karate training, self defence training, strength and conditioning, a weight loss programme, and wellness and fitness programmes. Karate is taught through Nippon Karate Club, which is affiliated to the World Karate Federation." }
        },
        {
          "@type": "Question",
          "name": "Where are your classes in Bangalore?",
          "acceptedAnswer": { "@type": "Answer", "text": "We train at Active Arena in Munnireddy Layout, Panathur; at the Dravid Centre for Sports Excellence; and at Koramangala Club. Panathur is convenient for Bellandur, Whitefield, Marathahalli and Sarjapur Road." }
        },
        {
          "@type": "Question",
          "name": "What age can my child start karate?",
          "acceptedAnswer": { "@type": "Answer", "text": "Children can start with us from four years old. Our youngest beginners work on balance, coordination and listening first, then move on to full kihon, kata and kumite training. Adults are welcome to begin at any age." }
        },
        {
          "@type": "Question",
          "name": "Is the first class free?",
          "acceptedAnswer": { "@type": "Answer", "text": "Yes. The first class is free and there is no obligation afterwards. Fill in the registration form and we will book you a demo session at the dojo nearest you." }
        },
        {
          "@type": "Question",
          "name": "Do you teach self defence for women?",
          "acceptedAnswer": { "@type": "Answer", "text": "Yes. We run women's self defence workshops, including on-site workshops for corporate teams, led by female instructors. They cover reading a violent situation, using your body's reflexes, and creating the time and distance that make a physical defence work." }
        }
      ]
    }
  ]
}
</script>
""",
        body=f"""
  <!-- ============================================================
       HERO — Nippon Fit, and what Nippon Fit offers
       ============================================================ -->
  <section class="hero">
    <div class="wrap">
      <div class="hero-grid">
        <div>
          <h1>Karate, Fitness and Self Defence in Bangalore</h1>
          <p class="hero-lede">
            Nippon Fit offers karate training, self defence training, strength and
            conditioning, a weight loss programme, and wellness and fitness programmes —
            for children from four years old and adults at any age.
          </p>

          <div class="hero-actions">
            <a class="btn btn-primary" href="/nippon-karate-club#registration">Book a free demo class</a>
            <a class="link-more" href="/karate-classes-bangalore">See all programmes</a>
          </div>

          <ul class="hero-credentials">
            <li>Three dojos across Bengaluru</li>
            <li>First class free</li>
            <li>Female instructors for girls and women</li>
          </ul>
        </div>

        <div class="hero-figure">
          <img src="/assets/hero-dojo.jpg"
               alt="Students and instructors of Nippon Karate Club at the dojo in Bengaluru"
               width="1280" height="720" fetchpriority="high">
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       MOVING GALLERY — the rotating photographs, high up the page the
       way the old website had them. It changes by itself every 15
       seconds. The photographs are listed at the top of js/gallery.js.
       ============================================================ -->
  <section class="section section-paper" style="padding-top:clamp(40px,5vw,64px);padding-bottom:clamp(40px,5vw,64px)">
    <div class="wrap">
      <div class="gallery" id="gallery" data-interval="15000" data-limit="10">
        <div class="gallery-stage" id="gallery-stage" aria-live="polite">
          <!-- filled in by js/gallery.js -->
        </div>

        <button class="gallery-arrow" data-dir="prev" type="button" aria-label="Previous photograph">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M15 18l-6-6 6-6"/></svg>
        </button>
        <button class="gallery-arrow" data-dir="next" type="button" aria-label="Next photograph">
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><path d="M9 6l6 6-6 6"/></svg>
        </button>

        <div class="gallery-dots" id="gallery-dots"></div>
      </div>

      <p class="text-centre" style="margin-top:26px;margin-bottom:0">
        <a class="link-more" href="/gallery">See the full gallery</a>
      </p>
    </div>
  </section>

  <!-- ============================================================
       WHAT THE CLUB HAS DONE
       ============================================================ -->
  <section class="section section-dark">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Achievements</span>
        <hr class="rule">
        <h2>What this club has done</h2>
      </div>

      <div class="grid grid-3 grid-gap">
        <article>
          <h3>A first for India</h3>
          <p>
            We were the first in India to host <strong>Ugur Aktas</strong>, the Tokyo
            Olympic bronze medallist from Turkey, and organised an elite kumite seminar
            with him at the Dravid Centre for Sports Excellence.
          </p>
        </article>

        <article>
          <h3>Athletes at the Nationals</h3>
          <p>
            Several of our athletes are state champions and South Zonal medallists, and
            have gone on to represent <strong>Karnataka at the Nationals</strong>.
          </p>
        </article>

        <article>
          <h3>Social responsibility</h3>
          <p>
            We run <strong>free classes at Bethany Special School</strong>, training their
            students for para competitions. It is the part of the work we are proudest of,
            and it is not something we charge for.
          </p>
        </article>
      </div>
    </div>
  </section>

  <!-- ============================================================
       WHAT WE OFFER — the five Nippon Fit programmes
       ============================================================ -->
  <section class="section section-paper">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">What we offer</span>
        <hr class="rule">
        <h2>Five programmes, one standard</h2>
        <p>
          Whether you have come for a black belt or simply to get fit, you are taught by
          people who have competed at the level they are teaching you to reach.
        </p>
      </div>

      <div class="grid grid-3 grid-flush">
        <article class="card">
          <span class="card-number">01</span>
          <h3>Karate Training</h3>
          <p>
            Traditional and sports karate on a WKF-aligned syllabus, taught through
            Nippon Karate Club. Kihon, kata and kumite, from a first white belt to
            national competition.
          </p>
        </article>

        <article class="card">
          <span class="card-number">02</span>
          <h3>Self Defence Training</h3>
          <p>
            Understanding a violent situation, your body reflexes, and how to create
            time and distance to make your physical defence techniques effective. Women's
            workshops led by female instructors.
          </p>
        </article>

        <article class="card">
          <span class="card-number">03</span>
          <h3>Strength &amp; Conditioning</h3>
          <p>
            The physical base underneath everything else — mobility, power and the
            conditioning that lets an athlete train hard without breaking down.
          </p>
        </article>

        <article class="card">
          <span class="card-number">04</span>
          <h3>Weight Loss</h3>
          <p>
            A structured programme built around activity you can keep doing, rather than
            a punishing few weeks you abandon. Progress measured, not guessed at.
          </p>
        </article>

        <article class="card">
          <span class="card-number">05</span>
          <h3>Wellness &amp; Fitness</h3>
          <p>
            Understanding fitness and your body — how your body reacts to different
            physical activities, and how to adopt them into your lifestyle to remain fit.
          </p>
        </article>

        <article class="card" style="display:flex;flex-direction:column;justify-content:center;background:var(--paper-warm)">
          <h3 style="margin-bottom:14px">Not sure which suits you?</h3>
          <p style="margin-bottom:20px">Tell us the age and what you are hoping for, and we will say honestly where to start.</p>
          <a class="link-more" href="/contact" style="align-self:flex-start">Ask us</a>
        </article>
      </div>
    </div>
  </section>

  <!-- ============================================================
       PHILOSOPHY — kept from the original website
       ============================================================ -->
  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Our Philosophy</span>
        <hr class="rule">
        <h2>Fitness is not the destination, but a journey and a lifestyle</h2>
        <p>
          You don't need to be enormously talented, highly intelligent, rich or gifted.
          You need to turn up, and keep turning up. That is what we teach first, long
          before anybody earns a coloured belt.
        </p>
      </div>
    </div>
  </section>

  <!-- ============================================================
       NIPPON KARATE CLUB — comes after Nippon Fit, not before it
       ============================================================ -->
  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-2 grid-gap" style="align-items:center;gap:clamp(36px,5vw,72px)">
        <div>
          <span class="eyebrow">Nippon Karate Club</span>
          <hr class="rule">
          <h2>A professional karate club, under the aegis of Nippon Fit</h2>
          <p>
            Nippon Karate Club is affiliated to the World Karate Federation, Madrid,
            Spain; the Karate India Organization, Delhi; and the Akhila Karnataka Sports
            Karate Association in Bangalore, Karnataka.
          </p>
          <p>
            Karate India Organization is the only National Federation of Karate Sport in
            India, which is affiliated with the IOC recognised International Federation,
            World Karate Federation. What that means for a student here is simple: the
            belt you earn is the belt the rest of the karate world recognises.
          </p>
          <p style="margin-bottom:0">
            <a class="link-more" href="/nippon-karate-club">About the club</a>
          </p>
        </div>
        <div>
          <img src="/assets/pooja-india-team.jpg"
               alt="Pooja Shri Shetty in India Karate Team kit at an international championship"
               width="1100" height="768" loading="lazy"
               style="border-radius:var(--radius-lg)">
        </div>
      </div>
    </div>
  </section>

{AFFILIATION_STRIP}

  <!-- ============================================================
       LOCATIONS
       ============================================================ -->
  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Branches</span>
        <hr class="rule">
        <h2>Find your nearest dojo</h2>
        <p>Three training venues across east and south Bengaluru.</p>
      </div>

      <div class="grid grid-3 grid-gap">

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Active%20Arena%20Munnireddy%20Layout%20Panathur%20Bengaluru&amp;output=embed"
                  title="Map of Active Arena, Panathur" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Active Arena, Panathur</h3>
            <address>Munnireddy Layout, Panathur, Bengaluru, Karnataka</address>
            <p>Closest for Bellandur, Whitefield, Marathahalli and Sarjapur Road.</p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Active+Arena+Munnireddy+Layout+Panathur+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Dravid%20Centre%20for%20Sports%20Excellence%20Bengaluru&amp;output=embed"
                  title="Map of the Dravid Centre for Sports Excellence" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Dravid Centre for Sports Excellence</h3>
            <address>Bengaluru, Karnataka</address>
            <p>A national-standard sports facility, shared with India's leading athletes.</p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Dravid+Centre+for+Sports+Excellence+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Koramangala%20Club%20Bengaluru&amp;output=embed"
                  title="Map of Koramangala Club" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Koramangala Club</h3>
            <address>Koramangala, Bengaluru, Karnataka</address>
            <p>For Koramangala, HSR Layout, Indiranagar and central Bengaluru.</p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Koramangala+Club+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

      </div>
    </div>
  </section>

  <!-- ============================================================
       PORTAL — heading and button only, nothing else
       ============================================================ -->
  <section class="section section-dark" style="text-align:center">
    <div class="wrap">
      <span class="eyebrow">Nippon Karate Club Portal</span>
      <hr class="rule" style="margin-left:auto;margin-right:auto">
      <p style="margin-bottom:30px"></p>
      <a class="btn btn-light" href="/login">Login</a>
    </div>
  </section>

  <!-- ============================================================
       FAQ
       ============================================================ -->
  <section class="section section-paper">
    <div class="wrap-narrow">
      <div class="section-head">
        <span class="eyebrow">Questions</span>
        <hr class="rule">
        <h2>What people ask us first</h2>
      </div>

      <div class="prose" style="max-width:none">
        <h3>What programmes does Nippon Fit offer?</h3>
        <p>
          Karate training, self defence training, strength and conditioning, a weight
          loss programme, and wellness and fitness programmes. Karate is taught through
          Nippon Karate Club, which is affiliated to the World Karate Federation.
        </p>

        <h3>Where are your classes in Bangalore?</h3>
        <p>
          We train at Active Arena in Munnireddy Layout, Panathur; at the Dravid Centre
          for Sports Excellence; and at Koramangala Club. Panathur is convenient for
          Bellandur, Whitefield, Marathahalli and Sarjapur Road.
        </p>

        <h3>What age can my child start karate?</h3>
        <p>
          Children can start with us from four years old. Our youngest beginners work on
          balance, coordination and listening first, then move on to full kihon, kata and
          kumite training. Adults are welcome to begin at any age.
        </p>

        <h3>Is the first class free?</h3>
        <p>
          Yes. The first class is free and there is no obligation afterwards. Fill in the
          <a href="/nippon-karate-club#registration">registration form</a> and we will
          book you a demo session at the dojo nearest you.
        </p>

        <h3>Do you teach self defence for women?</h3>
        <p>
          Yes. We run women's self defence workshops, including on-site workshops for
          corporate teams, led by female instructors. They cover reading a violent
          situation, using your body's reflexes, and creating the time and distance that
          make a physical defence work.
        </p>
      </div>
    </div>
  </section>

{cta_band(
    "Come and watch a class",
    "Bring your child along, sit at the side, and see the dojo for yourself before you decide anything. There is no obligation and no charge for the first session.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Book a free demo class</a>'
    f'<a class="btn btn-ghost" href="{WA}?text=Hello%20Nippon%20Fit%2C%20I%20would%20like%20to%20book%20a%20free%20demo%20class." target="_blank" rel="noopener">WhatsApp us</a>'
)}
""",
    )

    _classes()
    _club()
    _instructors()
    _locations()
    _contact()
    _login()
    _not_found()


# =====================================================================
# PROGRAMMES
# =====================================================================
def _classes():
    programmes = [
        ("karate", "Karate Training",
         """<p>
            Karate training by International and National team karateka and experts.
            Separate female instructors for girls and females. We provide the opportunity
            to attend workshops and training camps delivered by globally acclaimed
            coaches and athletes.
          </p>
          <p>
            Two streams run side by side on the same syllabus. <strong>Traditional
            karate</strong> follows the Shotokan and Shito-Ryu lines the club was built
            on — stance, breathing and etiquette first, then the kata that carry a
            student through every coloured belt to black, together with self defence
            technique and oriental weapons training. <strong>Sports karate</strong> is the
            competition stream: kumite and kata, the WKF match rules learned from a
            national A-graded referee, and entry to district, state and national
            championships as a student is ready. Nobody is pushed into competing before
            they want to.
          </p>
          <ul>
            <li><strong>Who it is for:</strong> children from four years old, and adult beginners at any age.</li>
            <li><strong>Where:</strong> all three dojos.</li>
            <li><strong>Leads to:</strong> WKF-aligned grading, through to Black Belt certification.</li>
          </ul>"""),

        ("self-defence", "Self Defence Training",
         """<p>
            We offer self defence workshops for corporate women. The workshop helps in
            understanding a violent situation, your body reflexes, and how to create time
            and distance to make your physical defence techniques effective.
          </p>
          <p>
            Workshops are led by female instructors and run at your office or at our dojo.
            They are built around what actually happens — being followed, being cornered,
            being grabbed — and around the two things that decide the outcome long before
            any technique does: distance, and the willingness to use your voice.
          </p>
          <ul>
            <li><strong>Who it is for:</strong> corporate teams, colleges, and groups of women and girls.</li>
            <li><strong>Format:</strong> half-day or full-day workshop, at your premises or ours.</li>
          </ul>"""),

        ("strength", "Strength &amp; Conditioning",
         """<p>
            The physical base underneath everything else. Mobility, power, and the
            conditioning that lets somebody train hard several times a week without
            breaking down.
          </p>
          <p>
            For competitors it is what turns good technique into a technique that scores
            under pressure. For everybody else it is simply the difference between
            exercising and getting stronger.
          </p>"""),

        ("weight-loss", "Weight Loss Programme",
         """<p>
            A structured programme built around activity you can keep doing, rather than a
            punishing few weeks you abandon. Progress is measured rather than guessed at,
            and the training is adjusted as you change.
          </p>"""),

        ("wellness", "Wellness &amp; Fitness Programmes",
         """<p>
            The programme focuses on understanding fitness and your body — how your body
            reacts to different physical activities, and how to adopt them into your
            lifestyle to remain fit.
          </p>
          <p>
            This is where most adults start when they want the conditioning and the
            discipline without the sparring.
          </p>"""),
    ]

    blocks = []
    for i, (anchor, title, content) in enumerate(programmes, 1):
        blocks.append(f"""
      <article id="{anchor}" class="prose" style="max-width:none;margin-bottom:64px">
        <span class="eyebrow">Programme {i:02d}</span>
        <hr class="rule">
        <h2 style="margin-top:0">{title}</h2>
        {content}
      </article>""")

    page(
        slug="karate-classes-bangalore",
        title="Karate Classes &amp; Fitness Programmes in Bangalore | Nippon Fit",
        description="Karate classes in Bangalore for kids and adults, plus self defence, strength, weight loss and wellness. Three dojos. First class free.",
        extra_head=breadcrumb_ld("Programmes", "karate-classes-bangalore"),
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Programmes")}
      <h1>Karate Classes and Fitness Programmes in Bangalore</h1>
      <p>
        Five programmes across three Bengaluru dojos — from a four-year-old's first white
        belt to national-level competition karate, and everything in between.
      </p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      {"".join(blocks)}
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Who trains with us</span>
        <hr class="rule">
        <h2>Karate for every age in Bengaluru</h2>
      </div>

      <div class="grid grid-3 grid-flush">
        <article class="card">
          <h3>Kids karate (4&ndash;12)</h3>
          <p>
            The largest group at every dojo. Short drills, constant correction, and a
            coloured belt to work towards each term. Parents watch from the side.
          </p>
        </article>
        <article class="card">
          <h3>Teens (13&ndash;17)</h3>
          <p>
            Where the competition stream usually begins. Harder conditioning, real
            kumite, and the school and state championships that come with it.
          </p>
        </article>
        <article class="card">
          <h3>Adults</h3>
          <p>
            Beginners welcome at any age. Train for fitness, for self defence, or take
            the full grading syllabus through to black belt.
          </p>
        </article>
      </div>
    </div>
  </section>

{cta_band(
    "Not sure which programme suits you?",
    "Tell us the age and what you are hoping for, and we will tell you honestly which to start with &mdash; or that we are not the right fit.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Register for a free demo class</a>'
    f'<a class="btn btn-ghost" href="{WA}?text=Hello%2C%20which%20programme%20would%20suit%20us%3F" target="_blank" rel="noopener">WhatsApp us</a>'
)}
""",
    )


# =====================================================================
# NIPPON KARATE CLUB
#
# The text in this page is taken word for word from the original
# website. The order is the same too: About Us, then Founder, then the
# Registration Form.
# =====================================================================
def _club():
    page(
        slug="nippon-karate-club",
        title="Nippon Karate Club, Bangalore — WKF Affiliated Karate School",
        description="Professional karate club in Bengaluru, affiliated to the World Karate Federation and Karate India Organization. Founded by Pooja Shri Shetty. Register here.",
        extra_head=breadcrumb_ld("Nippon Karate Club", "nippon-karate-club") + """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Person",
  "@id": "https://www.nipponfit.com/nippon-karate-club#pooja",
  "name": "Pooja Shri Shetty",
  "jobTitle": "Founder and Chief Instructor",
  "description": "International karateka and Aerospace Engineer. Black Belt 4th Dan (Karate Budokan International), 4th Dan (World Karate Federation), 5th Dan (Karate India Organization) and 1st Dan Shotokan (Turkish Karate Federation). National A-graded referee accredited by the Ministry of Youth Affairs and Sports.",
  "image": "https://www.nipponfit.com/assets/founder-pooja.jpg",
  "worksFor": { "@id": "https://www.nipponfit.com/#organisation" },
  "knowsAbout": ["Karate", "Shotokan", "Shito-Ryu", "Self defence", "Bharatanatyam"],
  "nationality": { "@type": "Country", "name": "India" },
  "sameAs": [
    "https://www.facebook.com/Nipponfit",
    "https://www.instagram.com/nippon_fit",
    "https://www.linkedin.com/company/nipponfit"
  ]
}
</script>
""",
        extra_scripts='<script src="/js/registration.js" defer></script>\n',
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Nippon Karate Club")}
      <h1>Nippon Karate Club</h1>

      <img src="/assets/nkc-emblem.png" alt="Nippon Karate Club emblem"
           width="150" height="165"
           style="width:150px;height:auto;margin:22px auto 24px">

      <p>
        Affiliated to the World Karate Federation, the Karate India Organization
        (KIO) and the Akhila Karnataka Sports Karate Association
      </p>
    </div>
  </section>

  <!-- ============================================================
       ABOUT US
       ============================================================ -->
  <section class="section section-paper">
    <div class="wrap-narrow">
      <div class="prose" style="max-width:none">
        <span class="eyebrow">About Us</span>
        <hr class="rule">
        <h2 style="margin-top:0">Nippon Karate Club</h2>

        <p>
          NIPPON KARATE CLUB is a professional karate club affiliated to World Karate
          Federation, Madrid, Spain, Karate India Organization, Delhi and Akhila Karnataka
          Sports Karate Association in Bangalore, Karnataka.
        </p>

        <p>
          Karate India Organization is the only National Federation of Karate Sport in
          India, which is affiliated with IOC recognized International Federation, World
          Karate Federation. Most of the National champions and Internationally renowned
          Players, WKF &amp; AKF qualified Judges/Referees, Coaches and Masters are
          associated with KIO. The KIO is a martial art institute of international repute,
          with members and authorized instructors throughout the world. The Organization
          maintains a high standard in Karate-Do and Oriental weapons training among its
          members, and every effort is made to ensure that the members undergo a rigid test
          before being promoted to each higher rank.
        </p>

        <h3>Objective of the Nippon Karate Club is:</h3>
        <ol>
          <li>To organize and conduct karate classes for members throughout the world and to train them in the Shotokan and Shito-Ryu style of Karate-Do.</li>
          <li>To train athletes capable of competing at higher levels on global Platform.</li>
          <li>To train candidates to participate in karate championships, tournaments, exhibitions, meetings, demonstrations and other karate activities.</li>
          <li>To promote good will, fellowship and social gatherings among the members.</li>
          <li>To act and do any other lawful things conductive to the attainment of the objectives of the institute.</li>
        </ol>

        <h3>Benefits from the institute</h3>
        <ul>
          <li>The karateka will be permitted to take part in the championship tournaments.</li>
          <li>The institute also takes the responsibility of teaching Self Defense, overcoming mental and physical stress along with the curriculum to be dealt as mentioned by WKF to receive a Black Belt.</li>
          <li>The other personal benefits include both mental and physical benefits.</li>
        </ul>
      </div>
    </div>
  </section>

{AFFILIATION_STRIP}

  <!-- ============================================================
       FOUNDER
       ============================================================ -->
  <section class="section section-paper">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Founder</span>
        <hr class="rule">
        <h2>
          <a href="https://en.wikipedia.org/wiki/Pooja_Shri_Shetty"
             target="_blank" rel="noopener"
             style="color:inherit;border-bottom:1px solid var(--gold)">Pooja Shri Shetty</a>
        </h2>
      </div>

      <div class="grid grid-2" style="gap:clamp(36px,5vw,64px);align-items:start">
        <div>
          <img src="/assets/founder-pooja.jpg"
               alt="Pooja Shri Shetty, founder of Nippon Karate Club"
               width="1650" height="2475" loading="lazy"
               style="border-radius:var(--radius-lg);background:var(--paper-warm)">

          <div style="margin-top:26px">
            <p style="font-size:11.5px;letter-spacing:.16em;text-transform:uppercase;color:var(--ink-faint);margin-bottom:12px">Follow us</p>
            <div style="display:flex;gap:16px">
              <a href="https://www.facebook.com/Nipponfit" target="_blank" rel="noopener" aria-label="Nippon Fit on Facebook" style="color:var(--ink-soft)">
                <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
              </a>
              <a href="https://www.instagram.com/nippon_fit" target="_blank" rel="noopener" aria-label="Nippon Fit on Instagram" style="color:var(--ink-soft)">
                <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" width="22" height="22"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>
              </a>
              <a href="https://www.linkedin.com/company/nipponfit" target="_blank" rel="noopener" aria-label="Nippon Fit on LinkedIn" style="color:var(--ink-soft)">
                <svg viewBox="0 0 24 24" fill="currentColor" width="22" height="22"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.5c0-1.3-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21H9z"/></svg>
              </a>
            </div>
          </div>
        </div>

        <div class="prose" style="max-width:none">
          <p>
            Pooja Shri Shetty is an International karateka and an Aerospace Engineer who
            started training in karate from a tender age of 6 and was selected to represent
            India in the World Karate Championship in Germany. She has represented India in
            several WKF Karate Series A tournaments and International Championships. Her
            Tokyo Olympics 2020 standing is 181.
          </p>

          <p>
            Pooja has won a silver in the Munich Open and two bronze at Bosporus Open and
            Helsinki Open Karate Championships respectively. Having secured Black Belt 4th
            Dan in Budokan Style from the Karate Budokan International, she also has Black
            Belt 4th Dan from the World Karate Federation, Black Belt 5th Dan from the
            Karate India Organization and Black belt 1st Dan from the Turkish Karate
            Federation (TKF) in the Shotokan Style. She has won several gold, silver and
            bronze medals in National and State Karate Championships. She draws experience
            and expertise from her trainings under Olympic medal winning coaches across
            Turkey and United Kingdom apart from India. She is an authorized instructor and
            examiner and national A graded referee accredited by the Ministry of youth and
            sports affairs.
          </p>

          <p>
            A vivid Bharatanatyam dancer and having completed her Vidwath in Bharatanatyam;
            Pooja has rendered over 800 performances all over India and Turkey; Spic Macay,
            Kannada Sahithya Sammelanas, ICCR Programs, to name a few.
          </p>
        </div>
      </div>
    </div>
  </section>

  <!-- ============================================================
       REGISTRATION FORM — sits after the founder, as it did on the
       original website.
       ============================================================ -->
  <section id="registration" class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Registration Form</span>
        <hr class="rule">
        <h2>Join Nippon Karate Club</h2>
        <p>
          The first class is free. Fill this in and we will confirm a day and time at the
          dojo you choose. Children from four years old, adults at any age.
        </p>
      </div>

      <div class="grid grid-2" style="gap:clamp(36px,5vw,56px);align-items:start;max-width:980px;margin:0 auto">

        <div>
          <!-- JOTFORM: if you would rather use a JotForm registration form, delete this
               whole <form> block and paste the JotForm embed code here instead. -->
          <form id="registration-form" novalidate>
            <div id="registration-message" class="notice" hidden></div>

            <div class="form-field">
              <label for="student">Full Name</label>
              <input type="text" id="student" name="student" autocomplete="name" required>
            </div>

            <div class="form-field">
              <label for="dob">Date of Birth</label>
              <input type="date" id="dob" name="dob" required>
            </div>

            <div class="form-field">
              <label for="gender">Gender</label>
              <select id="gender" name="gender">
                <option value="">-- Select Gender --</option>
                <option>Male</option>
                <option>Female</option>
                <option>Other</option>
              </select>
            </div>

            <div class="form-field">
              <label for="mobile">Contact Number</label>
              <input type="tel" id="mobile" name="mobile" inputmode="tel" autocomplete="tel" required>
            </div>

            <div class="form-field">
              <label for="parent">Parent or Guardian&rsquo;s Name <span class="hint">&mdash; leave blank if the student is an adult</span></label>
              <input type="text" id="parent" name="parent">
            </div>

            <div class="form-field">
              <label for="email">Email <span class="hint">&mdash; optional</span></label>
              <input type="email" id="email" name="email" autocomplete="email">
            </div>

            <div class="form-field">
              <label for="address">Address</label>
              <textarea id="address" name="address" rows="3"></textarea>
            </div>

            <div class="form-field">
              <label for="bloodgroup">Blood Group</label>
              <select id="bloodgroup" name="bloodgroup">
                <option value="">-- Select --</option>
                <option>A+</option><option>A-</option>
                <option>B+</option><option>B-</option>
                <option>AB+</option><option>AB-</option>
                <option>O+</option><option>O-</option>
              </select>
            </div>

            <div class="form-field">
              <label for="dojo">Preferred Dojo</label>
              <select id="dojo" name="dojo">
                <option>Active Arena, Panathur</option>
                <option>Dravid Centre for Sports Excellence</option>
                <option>Koramangala Club</option>
                <option>Not sure &mdash; please advise</option>
              </select>
            </div>

            <div class="form-field">
              <label for="programme">Programme</label>
              <select id="programme" name="programme">
                <option>Karate Training</option>
                <option>Self Defence Training</option>
                <option>Strength &amp; Conditioning</option>
                <option>Weight Loss</option>
                <option>Wellness &amp; Fitness</option>
                <option>Not sure &mdash; please advise</option>
              </select>
            </div>

            <div class="form-field">
              <label for="notes">Medical Conditions <span class="hint">&mdash; anything an instructor should know</span></label>
              <textarea id="notes" name="notes" rows="2"></textarea>
            </div>

            <button class="btn btn-primary btn-wide" type="submit" id="registration-submit">Submit registration</button>

            <p style="text-align:center;margin:16px 0 0">
              <a href="#" id="registration-email-link">or send it as an email instead</a>
            </p>
          </form>
        </div>

        <div>
          <div class="card" style="margin-bottom:20px">
            <h3>What happens next</h3>
            <ol style="padding-left:1.2em;color:var(--ink-soft);margin-bottom:0;font-size:.97rem">
              <li style="margin-bottom:.6em">You send the form.</li>
              <li style="margin-bottom:.6em">We reply with a day and time at your chosen dojo.</li>
              <li style="margin-bottom:.6em">You come along. The first class is free, and there is no obligation afterwards.</li>
              <li>If you join, we set up your portal login.</li>
            </ol>
          </div>

          <div class="card" style="margin-bottom:20px">
            <h3>Bring on the day</h3>
            <p>
              Comfortable clothes and a water bottle. A karate gi is not needed for the
              demo class. Please bring the student&rsquo;s photograph and Aadhaar copy to
              the dojo &mdash; we complete that part of the enrolment in person rather
              than over the internet, so your documents are never sent through a web form.
            </p>
          </div>

          <div class="card">
            <h3>Rather just talk to someone?</h3>
            <p><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></p>
            <p style="margin-bottom:0">
              <a class="btn btn-outline" href="{WA}?text=Hello%20Nippon%20Karate%20Club%2C%20I%20would%20like%20to%20register%20for%20a%20free%20demo%20class." target="_blank" rel="noopener">WhatsApp us</a>
            </p>
          </div>
        </div>

      </div>
    </div>
  </section>
""",
    )


# =====================================================================
# INSTRUCTORS
#
# NOTE: every credential on this page came from the founder. Nothing
# about these instructors is inferred or invented.
# =====================================================================
def _instructors():
    def instructor_photo(slug, name, initials):
        """Use the photograph if one has been saved, otherwise show the
        initials. Drop a file at assets/instructor-<slug>.jpg, run the
        builder, and it appears — no HTML to edit."""
        photo = ROOT / "assets" / f"instructor-{slug}.jpg"

        if photo.exists():
            from PIL import Image
            w, h = Image.open(photo).size
            return (f'<img src="/assets/instructor-{slug}.jpg" '
                    f'alt="{name}, karate instructor at Nippon Karate Club" '
                    f'width="{w}" height="{h}" loading="lazy">')

        return f'<span class="person-initials">{initials}</span>'

    def placeholder(initials, name):
        """Jeevan and Arvind. Their credentials are the same, so the card is
        written once and used for both."""
        slug = name.split()[0].lower()
        first = name.split()[0]
        return f"""
        <article class="person">
          <!-- PHOTO: save a picture as assets/instructor-{slug}.jpg and run
               python tools/build.py — it is picked up automatically. -->
          <div class="person-photo">{instructor_photo(slug, name, initials)}</div>
          <div class="person-body">
            <h3>{name}</h3>
            <p class="person-role">Karate Instructor</p>
            <p>
              {first} holds an internationally awarded 2nd Dan black belt and is a licensed
              referee and judge, so students here learn the competition rules from someone
              who officiates under them. He has taken several medals at the Karnataka State
              Championship and at the National Open Championship.
            </p>
            <ul class="person-tags">
              <li>2nd Dan black belt</li>
              <li>Licensed referee &amp; judge</li>
              <li>State medallist</li>
              <li>National Open medallist</li>
            </ul>
          </div>
        </article>"""

    page(
        slug="instructors",
        title="Our Karate Instructors in Bangalore | Nippon Fit",
        description="Meet the karate instructors at Nippon Karate Club, Bengaluru: Pooja Shri Shetty, Darshan T V, Jeevan J and Arvind Acharya. Female instructors for girls.",
        extra_head=breadcrumb_ld("Instructors", "instructors"),
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Instructors")}
      <h1>Our Instructors</h1>
      <p>
        You are trusting us with your child's Saturday mornings, and often with their
        confidence. These are the people who will be standing in front of them.
      </p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-2 grid-gap">

        <article class="person">
          <div class="person-photo">
            <img src="/assets/founder-pooja.jpg" alt="Pooja Shri Shetty, founder and chief instructor" width="1650" height="2475" loading="lazy" style="object-fit:contain;background:var(--paper-warm)">
          </div>
          <div class="person-body">
            <h3>Pooja Shri Shetty</h3>
            <p class="person-role">Founder &amp; Chief Instructor</p>
            <p>
              International karateka and Aerospace Engineer, training in karate since the
              age of six, and selected to represent India in the World Karate Championship
              in Germany. Silver at the Munich Open, bronze at the Bosporus and Helsinki
              Opens, and a Tokyo Olympics 2020 standing of 181.
            </p>
            <ul class="person-tags">
              <li>4th Dan &mdash; Karate Budokan International</li>
              <li>4th Dan &mdash; WKF</li>
              <li>5th Dan &mdash; KIO</li>
              <li>1st Dan Shotokan &mdash; TKF</li>
              <li>National A-graded referee</li>
            </ul>
            <p style="margin-top:16px;margin-bottom:0">
              <a class="link-more" href="/nippon-karate-club">Full profile</a>
            </p>
          </div>
        </article>

        <article class="person">
          <!-- PHOTO: save a picture as assets/instructor-darshan.jpg and run
               python tools/build.py — it is picked up automatically. -->
          <div class="person-photo">{instructor_photo("darshan", "Darshan T V", "DT")}</div>
          <div class="person-body">
            <h3>Darshan T V</h3>
            <p class="person-role">Karate Instructor</p>
            <p>
              Fifteen years in karate and more than six of them teaching, trained at the
              Okinawa Bukodai Martial Arts Academy. Darshan works across Goju-ryu and
              Shotokan, and has medalled at national and state level in karate under the
              Karate India Organization, as well as taking a national bronze in kickboxing
              under WAKO.
            </p>
            <ul class="person-tags">
              <li>2nd Dan black belt</li>
              <li>15 years training</li>
              <li>6+ years teaching</li>
              <li>Goju-ryu &amp; Shotokan</li>
              <li>OBMAA trained</li>
            </ul>
            <p style="font-size:.92rem;color:var(--ink-faint);margin-top:16px;margin-bottom:0">
              National and state medals (KIO) &middot; National kickboxing bronze (WAKO)
            </p>
          </div>
        </article>
{placeholder("JJ", "Jeevan J")}
{placeholder("AA", "Arvind Acharya")}

      </div>
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">How we teach</span>
        <hr class="rule">
        <h2>What every instructor here works to</h2>
      </div>

      <div class="grid grid-3 grid-flush">
        <article class="card">
          <h3>Female instructors for girls</h3>
          <p>
            Separate female instructors are available for girls and women across the
            karate and self defence programmes. Nobody has to ask twice for it.
          </p>
        </article>
        <article class="card">
          <h3>One correction at a time</h3>
          <p>
            Classes are kept to a size where an instructor can watch a single stance and
            fix it, rather than call the room through a routine.
          </p>
        </article>
        <article class="card">
          <h3>The same syllabus everywhere</h3>
          <p>
            A student who moves between our dojos picks up exactly where they left off.
            One WKF-aligned syllabus, one grading standard, three venues.
          </p>
        </article>
      </div>
    </div>
  </section>

{cta_band(
    "Come and meet them",
    "The best way to judge an instructor is to watch them teach for twenty minutes. Turn up and do exactly that.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Book a free demo class</a>'
    '<a class="btn btn-ghost" href="/locations">See the dojos</a>'
)}
""",
    )


# =====================================================================
# LOCATIONS
# =====================================================================
def _locations():
    page(
        slug="locations",
        title="Karate Classes Near You in Bangalore — Our Dojos | Nippon Fit",
        description="Karate dojos in Bengaluru: Active Arena Panathur (for Bellandur, Whitefield, Marathahalli), Dravid Centre for Sports Excellence, and Koramangala Club.",
        extra_head=breadcrumb_ld("Locations", "locations"),
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Locations")}
      <h1>Karate Classes Near You in Bangalore</h1>
      <p>Three dojos across east and south Bengaluru. Same syllabus, same grading standard, at all of them.</p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-3 grid-gap">

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Active%20Arena%20Munnireddy%20Layout%20Panathur%20Bengaluru&amp;output=embed"
                  title="Map of Active Arena, Panathur" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Active Arena, Panathur</h3>
            <address>Munnireddy Layout, Panathur,<br>Bengaluru, Karnataka</address>
            <p>
              Our main dojo, and the easiest to reach from <strong>Bellandur, Whitefield,
              Marathahalli, Sarjapur Road, Kadubeesanahalli and Varthur</strong>. Indoor
              matted floor, parking, and space for parents to sit and watch.
            </p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Active+Arena+Munnireddy+Layout+Panathur+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Dravid%20Centre%20for%20Sports%20Excellence%20Bengaluru&amp;output=embed"
                  title="Map of the Dravid Centre for Sports Excellence" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Dravid Centre for Sports Excellence</h3>
            <address>Bengaluru, Karnataka</address>
            <p>
              A national-standard facility shared with some of India's leading athletes.
              This is where our competition squad does much of its preparation.
            </p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Dravid+Centre+for+Sports+Excellence+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

        <article class="branch">
          <iframe class="branch-map"
                  src="https://maps.google.com/maps?q=Koramangala%20Club%20Bengaluru&amp;output=embed"
                  title="Map of Koramangala Club" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3>Koramangala Club</h3>
            <address>Koramangala,<br>Bengaluru, Karnataka</address>
            <p>
              For families in <strong>Koramangala, HSR Layout, Indiranagar and central
              Bengaluru</strong>.
            </p>
            <a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Koramangala+Club+Bengaluru" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>

      </div>
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Areas we serve</span>
        <hr class="rule">
        <h2>Where our students travel from</h2>
        <p>If your area is on this list, one of our three dojos is a reasonable drive away.</p>
      </div>
      <p class="text-centre" style="max-width:46em;margin:0 auto;color:var(--ink-soft)">
        Panathur &middot; Bellandur &middot; Whitefield &middot; Marathahalli &middot;
        Sarjapur Road &middot; Kadubeesanahalli &middot; Varthur &middot; Koramangala &middot;
        HSR Layout &middot; Indiranagar &middot; Domlur &middot; Brookefield
      </p>
    </div>
  </section>

{cta_band(
    "Find your dojo",
    "Tell us where you live and we will tell you which of the three suits you.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Register for a free demo class</a>'
    f'<a class="btn btn-ghost" href="tel:{PHONE_LINK}">Call {PHONE_DISPLAY}</a>'
)}
""",
    )


# =====================================================================
# CONTACT
# =====================================================================
def _contact():
    page(
        slug="contact",
        title="Contact Nippon Fit, Bangalore — Book a Free Demo Class",
        description="Contact Nippon Fit in Bengaluru. Call +91 99456 16005, WhatsApp us or email contactus@nipponfit.com to book a free demo class or arrange a self defence workshop.",
        extra_head=breadcrumb_ld("Contact", "contact") + """<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "ContactPage",
  "url": "https://www.nipponfit.com/contact",
  "about": { "@id": "https://www.nipponfit.com/#organisation" }
}
</script>
""",
        extra_scripts='<script src="/js/contact.js" defer></script>\n',
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Contact")}
      <h1>Get in Touch</h1>
      <p>Ask us anything, or arrange a self defence workshop for your team.</p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-2" style="gap:clamp(36px,5vw,64px);align-items:start">

        <div>
          <h2 class="mt-0">Send us a message</h2>
          <p class="form-note" style="margin-bottom:28px">
            Fill this in and it opens WhatsApp with your message already written, so you
            can send it in one tap. Prefer email? Use the link underneath.
          </p>

          <form id="contact-form" novalidate>
            <div id="contact-message" class="notice" hidden></div>

            <div class="form-field">
              <label for="name">Your name</label>
              <input type="text" id="name" name="name" autocomplete="name" required>
            </div>

            <div class="form-field">
              <label for="phone">Mobile number <span class="hint">&mdash; so we can call you back</span></label>
              <input type="tel" id="phone" name="phone" inputmode="tel" autocomplete="tel" required>
            </div>

            <div class="form-field">
              <label for="interest">What are you asking about?</label>
              <select id="interest" name="interest">
                <option>A free demo class</option>
                <option>Fees and joining</option>
                <option>Kids karate</option>
                <option>Adult karate</option>
                <option>Self defence workshop</option>
                <option>Strength &amp; conditioning</option>
                <option>Weight loss programme</option>
                <option>A workshop or camp at our school</option>
                <option>Something else</option>
              </select>
            </div>

            <div class="form-field">
              <label for="area">Which area do you live in? <span class="hint">&mdash; so we can suggest the nearest dojo</span></label>
              <input type="text" id="area" name="area" placeholder="e.g. Bellandur">
            </div>

            <div class="form-field">
              <label for="note">Anything else <span class="hint">&mdash; optional</span></label>
              <textarea id="note" name="note" rows="4" placeholder="e.g. My daughter is 7 and has never done karate before."></textarea>
            </div>

            <button class="btn btn-primary btn-wide" type="submit" id="contact-submit">Send on WhatsApp</button>

            <p style="text-align:center;margin:16px 0 0">
              <a href="#" id="contact-email-link">or send it as an email instead</a>
            </p>
          </form>
        </div>

        <div>
          <div class="card" style="margin-bottom:20px">
            <h3>Phone &amp; WhatsApp</h3>
            <p style="font-size:1.15rem"><a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a></p>
            <p style="margin-bottom:0"><a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">Open WhatsApp</a></p>
          </div>

          <div class="card" style="margin-bottom:20px">
            <h3>Email</h3>
            <p style="margin-bottom:0"><a href="mailto:{EMAIL}">{EMAIL}</a></p>
          </div>

          <div class="card" style="margin-bottom:20px">
            <h3>Main dojo</h3>
            <address style="font-style:normal;color:var(--ink-soft);font-size:.97rem">
              Active Arena, Munnireddy Layout,<br>
              Panathur, Bengaluru,<br>
              Karnataka, India
            </address>
            <p style="margin-bottom:0;margin-top:16px"><a class="btn btn-outline" href="https://www.google.com/maps/search/?api=1&amp;query=Active+Arena+Munnireddy+Layout+Panathur+Bengaluru" target="_blank" rel="noopener">Directions</a></p>
          </div>

          <div class="card">
            <h3>Ready to join?</h3>
            <p>The registration form is on the Nippon Karate Club page. First class free.</p>
            <p style="margin-bottom:0"><a class="btn btn-primary" href="/nippon-karate-club#registration">Registration form</a></p>
          </div>
        </div>

      </div>
    </div>
  </section>
""",
    )


# =====================================================================
# LOGIN
# =====================================================================
def _login():
    page(
        slug="login",
        title="Login — Nippon Karate Club Portal",
        description="Nippon Karate Club portal login. Sign in with the mobile number you gave the dojo.",
        robots="noindex, follow",
        extra_scripts='<script src="/js/login.js" defer></script>\n',
        body=f"""
  <section class="login-page">
    <div class="login-panel">
      <div class="login-body">
        <img class="seal" src="/assets/seal.png" alt="" width="84" height="96">
        <span class="eyebrow">Nippon Karate Club Portal</span>
        <h1>Login</h1>

        <form id="parent-login-form" novalidate style="margin-top:28px">
          <div id="login-message" class="notice" hidden></div>

          <div class="form-field">
            <label for="mobile">Your mobile number</label>
            <input type="tel" id="mobile" name="mobile" inputmode="numeric"
                   autocomplete="tel" placeholder="10-digit mobile number"
                   maxlength="15" required>
          </div>

          <button class="btn btn-dark btn-wide" type="submit" id="login-submit">Continue</button>
        </form>

        <p class="login-help">
          Use the mobile number you gave the dojo. You will type your password on the
          next screen.
        </p>

        <p class="login-help">
          Forgotten your password? Call <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a>
          and we will reset it for you.
        </p>

        <p class="login-help" style="margin-top:24px;padding-top:20px;border-top:1px solid var(--line)">
          New here? <a href="/nippon-karate-club#registration">Register for a free demo class</a>.
        </p>
      </div>
    </div>
  </section>
""",
    )


# =====================================================================
# 404
# =====================================================================
def _not_found():
    page(
        slug="404",
        title="Page not found | Nippon Fit",
        description="That page does not exist. Find programmes, dojo locations and contact details for Nippon Fit, Bengaluru.",
        robots="noindex, follow",
        body="""
  <section class="page-banner">
    <div class="wrap">
      <h1>We could not find that page</h1>
      <p>It may have moved when we rebuilt the site. Everything is still here — just in a slightly different place.</p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-3 grid-flush">
        <article class="card">
          <h3>Looking for programmes?</h3>
          <p>All five, with what each one covers and who it suits.</p>
          <p style="margin-top:18px;margin-bottom:0"><a class="link-more" href="/karate-classes-bangalore">See the programmes</a></p>
        </article>
        <article class="card">
          <h3>Looking for a dojo?</h3>
          <p>Panathur, the Dravid Centre for Sports Excellence, and Koramangala.</p>
          <p style="margin-top:18px;margin-bottom:0"><a class="link-more" href="/locations">See the locations</a></p>
        </article>
        <article class="card">
          <h3>Already with us?</h3>
          <p>The Nippon Karate Club portal is where attendance, fees and gradings live.</p>
          <p style="margin-top:18px;margin-bottom:0"><a class="link-more" href="/login">Login</a></p>
        </article>
      </div>
    </div>
  </section>
""",
    )
