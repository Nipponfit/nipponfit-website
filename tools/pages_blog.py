# =====================================================================
# NIPPON FIT — the blog and the gallery
#
# THE BLOG
# --------
# The articles below are Pooja's own technique analyses, taken from the
# training documents. The words are hers; they have been laid out for the
# web and the references to "Video 1 / Video 2" and to numbered images
# have been turned into plain descriptions, because those files are not
# on the website.
#
# TO ADD A NEW ARTICLE: copy one of the entries in ARTICLES, change the
# slug, title, date, summary and body, then run  python tools/build.py
#
# THE GALLERY
# -----------
# The photographs shown are listed in js/gallery.js. Add a picture to
# assets/gallery/ and add one line to that list. Nothing else to do.
# =====================================================================

from build import page, crumbs, breadcrumb_ld, cta_band, PHONE_DISPLAY, PHONE_LINK, WHATSAPP
from blog_bodies import MARTIAL_ARTS_BODY, ORIGIN_BODY, WORKOUT_BODY

WA = f"https://wa.me/{WHATSAPP}"

AUTHOR = "Pooja Shri Shetty"


# =====================================================================
# The articles
#
# Newest first — that is the order they appear on the blog page.
# =====================================================================

ARTICLES = [
    {
        "slug": "kumite-analysis",
        "title": "Kumite Analysis: What Two Years of Footage Actually Showed Me",
        "seo_title": "Kumite Analysis: What My Own Footage Showed Me",
        "date": "2026-02-14",
        "date_label": "14 February 2026",
        "category": "Kumite",
        "summary": "Comparing my own competition footage across two tournaments — what improved, what quietly got worse, and why footwork turned out to be the thing that mattered most.",
        "body": """
        <p>
          Every athlete thinks they know what they are doing on the mat. Then you sit down
          with two videos of yourself, eighteen months apart, and find out how much of that
          was a story you were telling yourself.
        </p>
        <p>
          This is my own analysis of two competition performances. I am writing it down
          because the students I coach are asked to do exactly this, and it would be a poor
          thing to ask of them if I were not willing to do it myself.
        </p>

        <h2>1. Fighting stance and posture</h2>
        <p>
          In the more recent footage I appear more willing to move forward, more dynamic
          between attacks, more frequently changing my distance, and less static. All of
          that is progress.
        </p>
        <p>
          But I also noticed that my hands occasionally drop when I am waiting, particularly
          after an exchange. So: movement improved; static guard and posture slightly less
          consistent. That is an honest trade, and it is the kind of thing that only shows
          up on video. Nobody feels their own hands drop.
        </p>

        <h2>2. Footwork — one of my biggest improvements</h2>
        <p>
          This is where I see a meaningful change.
        </p>
        <p>
          In the earlier footage I sometimes spend relatively long periods establishing
          distance before initiating. In the recent footage I am much more prepared to
          <strong>close, attack, recover, reposition</strong>.
        </p>
        <blockquote>
          <p>My movement has become less "stand and react" and more "create the exchange."</p>
        </blockquote>
        <p>
          That matters for a &minus;61 kg kumite athlete, because I don't want to depend
          entirely on reacting to my opponent. Reacting is a losing strategy against
          somebody faster than you. Creating the exchange means you choose the moment.
        </p>

        <h2>What I would tell a student reading this</h2>
        <p>
          Film yourself. Not once — regularly, and at competition rather than in training,
          because training is where you are comfortable and competition is where the truth
          is. Then watch it with somebody who will tell you what they actually see.
        </p>
        <p>
          The improvements will not be where you expect them. Mine were not in technique.
          They were in the willingness to move first.
        </p>
        """,
    },

    {
        "slug": "reverse-punch-mechanics",
        "title": "Reverse Punch: Where the Power Leaks Away",
        "date": "2026-01-22",
        "date_label": "22 January 2026",
        "category": "Technique",
        "summary": "Two photographs of the same technique — one with the mechanics wrong and one with them right — and exactly what separates a punch that lands from one that only looks like it should.",
        "seo_summary": "The same reverse punch with the mechanics wrong and then right, and exactly what separates a punch that lands from one that only looks right.",
        "body": """
        <p>
          Gyaku-zuki, the reverse punch, is the first technique every karateka learns and
          one of the last they get right. Below is a breakdown of the same punch performed
          two ways: once with the mechanics wrong, once with them correct.
        </p>

        <h2>Wrong mechanics</h2>

        <h3>1. Over-striding and loss of base</h3>
        <p>
          The lead leg is too far ahead of the centre of gravity. The hips are behind the
          strike instead of driving it. This creates a braking effect rather than
          acceleration.
        </p>
        <p><strong>Result:</strong> power leaks into the ground instead of into the target.</p>

        <h3>2. Centre of gravity outside the base</h3>
        <p>
          The centre of gravity is not between the feet. On sand this is even worse, because
          the surface absorbs force. Any push back means a loss of balance or a delay in
          recovery.
        </p>
        <p><strong>Result:</strong> unstable, slow recovery, easy to counter.</p>

        <h3>3. Upper and lower body disconnect</h3>
        <p>
          The arm is thrown first. Hips and torso rotate after, not before. There is no
          kinetic chain — no ground, legs, hips, torso, arm.
        </p>
        <p><strong>Result:</strong> an arm-dominant strike. Low impact, and stress on the shoulder.</p>

        <h3>4. Heel not driving</h3>
        <p>
          The rear foot is passive. There is no ground reaction force. You are
          <em>reaching</em> instead of <em>driving</em>.
        </p>

        <h2>Correct mechanics</h2>

        <h3>1. Strong base and correct stride length</h3>
        <p>
          Feet shoulder-width apart with controlled depth. Front knee bent, rear leg active.
          The centre of gravity stays inside the base.
        </p>
        <p><strong>Result:</strong> maximum stability at the moment of impact.</p>

        <h3>2. A complete kinetic chain</h3>
        <p>Force starts from the rear foot push, then hip rotation, torso rotation, shoulder snap, arm extension. This is ground-up power, not arm power.</p>

        <h3>3. Hip dominance</h3>
        <p>
          The hips lead the technique. The arm follows the body, not the other way around.
          Body mass moves through the opponent.
        </p>
        <p><strong>Result:</strong> penetration power, not surface contact.</p>

        <h3>4. Instant recovery</h3>
        <p>
          Knees flexed. Weight distribution allows an immediate pull-back or follow-up.
          Ready for the next action.
        </p>

        <h2>Side by side</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Aspect</th><th>Wrong mechanics</th><th>Correct mechanics</th></tr>
            </thead>
            <tbody>
              <tr><td>Base</td><td>Overstretched</td><td>Compact and strong</td></tr>
              <tr><td>Centre of gravity</td><td>Outside the feet</td><td>Inside the feet</td></tr>
              <tr><td>Power source</td><td>Arm</td><td>Ground and hips</td></tr>
              <tr><td>Stability</td><td>Low</td><td>High</td></tr>
              <tr><td>Recovery</td><td>Slow</td><td>Immediate</td></tr>
            </tbody>
          </table>
        </div>

        <blockquote>
          <p>The first throws the body at the technique. The second drives the technique through the body.</p>
        </blockquote>
        """,
    },

    {
        "slug": "kumite-stance-analysis",
        "title": "Kumite Stance: The Difference Between Elite and Almost",
        "date": "2025-12-18",
        "date_label": "18 December 2025",
        "category": "Kumite",
        "summary": "Setting my own kumite stance against an elite competitor's, point by point — centre of gravity, heel position, knee load — and what each one costs in reaction time.",
        "body": """
        <p>
          Stance is not a pose you hold. It is the machine that produces every technique you
          throw, and if the machine is set up wrong then nothing downstream of it can be
          right.
        </p>
        <p>
          What follows is a comparison between my own kumite stance and that of an elite
          competitor, Anzhelika. It is not flattering to me, which is rather the point.
        </p>

        <h2>My stance — what I was doing wrong</h2>
        <p>Leaning back. Weight on the heels. A high stance. Hips not aligned. Feet too close together.</p>
        <ul>
          <li>Centre of gravity too high, and too far back</li>
          <li>Knees not loaded — no spring</li>
          <li>Rear heel too flat</li>
          <li>Stance not compact; body upright, giving slow responsiveness</li>
          <li>Head outside the base of support</li>
          <li>Rear leg too straight</li>
          <li>Hips rotated away unnecessarily</li>
          <li>Shoulders over-rotated, or leaned back</li>
        </ul>

        <h2>The elite stance — what it does instead</h2>
        <p>Hips facing the opponent. Weight on the balls of the feet. A lower centre of gravity, and a proper angle.</p>
        <ul>
          <li>Low, forward centre of gravity</li>
          <li>Spring-loaded front knee</li>
          <li>Raised heels for speed</li>
          <li>Correct stance width</li>
          <li>A continuous kinetic chain</li>
          <li>Low inertia, giving instant motion</li>
          <li>A light bounce always possible</li>
          <li>Rear leg bent enough to push</li>
          <li>Balanced weight distribution, arms staying within the centreline for guard</li>
        </ul>

        <h2>Component by component</h2>
        <div class="table-wrap">
          <table>
            <thead>
              <tr><th>Component</th><th>Elite stance</th><th>My stance</th></tr>
            </thead>
            <tbody>
              <tr><td>Centre of gravity</td><td>Low and forward</td><td>High and backward</td></tr>
              <tr><td>Heel</td><td>Raised, ready</td><td>Often flat</td></tr>
              <tr><td>Front knee</td><td>Loaded and bent</td><td>Almost straight</td></tr>
              <tr><td>Hip</td><td>Angled for speed</td><td>Too open, too upright</td></tr>
              <tr><td>Stability</td><td>High</td><td>Medium to low</td></tr>
              <tr><td>Speed</td><td>Very high</td><td>Slower</td></tr>
              <tr><td>Explosive step</td><td>Instant</td><td>Delayed weight shift</td></tr>
              <tr><td>Reaction time</td><td>Faster</td><td>Slower</td></tr>
              <tr><td>Momentum</td><td>Builds instantly</td><td>Builds late</td></tr>
              <tr><td>Inertia</td><td>Low</td><td>High</td></tr>
            </tbody>
          </table>
        </div>

        <h2>Why the heel decides so much</h2>
        <p>
          When the centre of gravity sits high and behind the base of support, the push-off
          is slow. Explosiveness is lost because a flat heel is dead weight. Momentum breaks,
          because the kinetic chain cannot start efficiently.
        </p>
        <p>
          A raised heel is not a stylistic preference. It is the difference between being
          already moving and having to start moving — and at this level, that gap is the
          whole match.
        </p>
        """,
    },

    {
        "slug": "chudan-mawashi-geri-analysis",
        "title": "Chudan Mawashi Geri: Why Judges Reward One Kick and Not the Other",
        "seo_title": "Chudan Mawashi Geri: Why One Kick Scores",
        "date": "2025-11-30",
        "date_label": "30 November 2025",
        "category": "Technique",
        "summary": "Two roundhouse kicks to the body, broken down frame by frame — centre of gravity, hip and shoulder sequencing, and what separates a technique that scores from one that does not.",
        "seo_summary": "Two roundhouse kicks broken down frame by frame: centre of gravity, hip and shoulder sequencing, and what makes a technique score.",
        "body": """
        <p>
          The chudan mawashi geri — the roundhouse kick to the body — is one of the highest
          scoring techniques in competition kumite. It is also one of the easiest to throw
          in a way that a judge will not reward.
        </p>
        <p>Here are two versions of the same kick, compared.</p>

        <h2>Lower-body mechanics and centre of gravity</h2>
        <p><strong>The weaker version:</strong> the centre of gravity rises during the attack. The rear heel lifts early, so power leaks upward. The hips travel after the hand, and the weight shifts too late.</p>
        <p><strong>The stronger version:</strong> the centre of gravity stays low and stable. The rear leg drives first — ground, then hip, then hand. The hips initiate before the arm, leading to a clean forward weight transfer.</p>
        <blockquote>
          <p>In kumite, power must come from horizontal drive, not vertical bounce.</p>
        </blockquote>

        <h2>Hip and shoulder sequencing — the kinetic chain</h2>
        <p><strong>The weaker version:</strong> the arm leads the technique. The shoulder rotates independently. The hip line and the shoulder line are disconnected.</p>
        <p><strong>The stronger version:</strong> the hips rotate first, and the shoulder and arm follow naturally. One connected kinetic chain.</p>
        <p>
          This is the part that decides the score. Judges reward techniques that show
          body-driven force, not arm punching. A kick that arrives without the body behind
          it reads, correctly, as a touch rather than a technique.
        </p>

        <h2>What to work on</h2>
        <p>
          If your kick is not scoring, the problem is very rarely the leg. Look at whether
          the hips are arriving before the limb or after it, and whether your centre of
          gravity is travelling forward through the target or upward away from it.
        </p>
        <p>
          Fix the order in which your body parts move, and the kick fixes itself.
        </p>
        """,
    },

    # -----------------------------------------------------------------
    # The three articles carried across from the old website.
    # Their old addresses were /blog/f/<slug>; vercel.json redirects
    # those to the new ones so no existing link breaks.
    # -----------------------------------------------------------------
    {
        "slug": "martial-arts-styles",
        "title": "Martial Arts Styles",
        "date": "2023-04-20",
        "date_label": "20 April 2023",
        "category": "Karate",
        "summary": "There are 180+ martial arts styles, from the well known to the genuinely obscure. A complete list, with what each one focuses on and where it came from.",
        "body": MARTIAL_ARTS_BODY,
    },

    {
        "slug": "origin-of-karate-do",
        "title": "Origin of Karate-Do",
        "date": "2023-01-31",
        "date_label": "31 January 2023",
        "category": "Karate",
        "summary": "Where karate came from, how it reached Japan and then the world, and the dates and people that shaped it along the way.",
        "body": ORIGIN_BODY,
    },

    {
        "slug": "full-body-workout",
        "title": "Full Body Workout",
        "date": "2023-01-31",
        "date_label": "31 January 2023",
        "category": "Fitness",
        "summary": "A seven-minute full body tabata workout for intermediate and advanced fitness enthusiasts — and how beginners and professionals can adapt it.",
        "body": WORKOUT_BODY,
    },
]


def build():
    print("Blog and gallery:")
    _blog_index()
    for a in ARTICLES:
        _article(a)
    _gallery()


# =====================================================================
# Blog index
# =====================================================================
def _blog_index():
    cards = []
    for a in ARTICLES:
        cards.append(f"""
        <article class="post-card">
          <p class="post-meta">{a['category']} &nbsp;&middot;&nbsp; {a['date_label']}</p>
          <h3><a href="/blog/{a['slug']}">{a['title']}</a></h3>
          <p>{a['summary']}</p>
          <a class="link-more" href="/blog/{a['slug']}">Read the article</a>
        </article>""")

    item_list = ",\n".join(
        f"""    {{ "@type": "ListItem", "position": {i}, "url": "https://www.nipponfit.com/blog/{a['slug']}" }}"""
        for i, a in enumerate(ARTICLES, 1)
    )

    page(
        slug="blog",
        title="Blog — Karate Technique Analysis | Nippon Fit",
        description="Technique analysis from Nippon Fit, Bengaluru. Kumite, stance, reverse punch and mawashi geri broken down by international karateka Pooja Shri Shetty.",
        extra_head=breadcrumb_ld("Blog", "blog") + f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "ItemList",
  "name": "Nippon Fit blog",
  "itemListElement": [
{item_list}
  ]
}}
</script>
""",
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Blog")}
      <h1>Blog</h1>
      <p>
        Technique analysis, written from competition footage and training video — the same
        analysis our competition squad is asked to do on their own performances.
      </p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <div class="grid grid-2 grid-gap">
        {"".join(cards)}
      </div>
    </div>
  </section>

{cta_band(
    "Train where the analysis happens",
    "Every competitor at Nippon Karate Club is taught to look at their own footage this way. The first class is free.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Book a free demo class</a>'
)}
""",
    )


# =====================================================================
# One article page
# =====================================================================
def _article(a):
    others = [x for x in ARTICLES if x["slug"] != a["slug"]][:3]
    more = "".join(f"""
        <article class="post-card">
          <p class="post-meta">{o['category']}</p>
          <h3><a href="/blog/{o['slug']}">{o['title']}</a></h3>
          <a class="link-more" href="/blog/{o['slug']}">Read</a>
        </article>""" for o in others)

    page(
        slug=f"blog/{a['slug']}",
        title=f"{a.get('seo_title', a['title'])} | Nippon Fit",
        description=a.get("seo_summary", a["summary"]),
        extra_head=f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BlogPosting",
  "headline": "{a['title']}",
  "description": "{a['summary']}",
  "datePublished": "{a['date']}",
  "author": {{ "@type": "Person", "name": "{AUTHOR}", "@id": "https://www.nipponfit.com/nippon-karate-club#pooja" }},
  "publisher": {{ "@id": "https://www.nipponfit.com/#organisation" }},
  "mainEntityOfPage": "https://www.nipponfit.com/blog/{a['slug']}",
  "image": "https://www.nipponfit.com/assets/founder-pooja.jpg",
  "articleSection": "{a['category']}",
  "inLanguage": "en-IN"
}}
</script>
""",
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      <p class="crumbs"><a href="/">Home</a> &nbsp;/&nbsp; <a href="/blog">Blog</a> &nbsp;/&nbsp; {a['category']}</p>
      <h1>{a['title']}</h1>
      <p>{a['summary']}</p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">
      <article class="article">
        <p class="post-meta" style="border-bottom:1px solid var(--line);padding-bottom:18px;margin-bottom:34px">
          By {AUTHOR} &nbsp;&middot;&nbsp; {a['date_label']} &nbsp;&middot;&nbsp; {a['category']}
        </p>
{a['body']}
        <p style="margin-top:44px;padding-top:26px;border-top:1px solid var(--line)">
          <a class="link-more" href="/blog">All articles</a>
        </p>
      </article>
    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">Also on the blog</span>
        <hr class="rule">
      </div>
      <div class="grid grid-3 grid-gap">{more}</div>
    </div>
  </section>
""",
    )


# =====================================================================
# Gallery
# =====================================================================
def _gallery():
    page(
        slug="gallery",
        title="Gallery — Championships and Achievements | Nippon Fit",
        description="Photographs from Nippon Karate Club, Bengaluru — championships, medals, gradings and training. International and national karate achievements.",
        extra_head=breadcrumb_ld("Gallery", "gallery"),
        extra_scripts='<script src="/js/gallery.js" defer></script>\n',
        body=f"""
  <section class="page-banner">
    <div class="wrap">
      {crumbs("Gallery")}
      <h1>Gallery</h1>
      <p>
        Championships, medals, gradings and the ordinary training days that made them
        possible.
      </p>
    </div>
  </section>

  <section class="section section-paper">
    <div class="wrap">

      <!-- The slideshow. The photographs themselves are listed at the top of
           js/gallery.js — add a picture there and it appears here. It moves on
           by itself every 15 seconds. -->
      <div class="gallery" id="gallery" data-interval="15000">
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

      <noscript>
        <p class="text-centre" style="margin-top:24px">
          The slideshow needs JavaScript. Every photograph is shown in the grid below.
        </p>
      </noscript>

      <!-- Every photograph, as a plain grid underneath -->
      <div class="gallery-grid" id="gallery-grid" style="max-width:940px;margin:36px auto 0"></div>

    </div>
  </section>

  <section class="section section-warm">
    <div class="wrap-narrow text-centre">
      <span class="eyebrow">Add to this page</span>
      <hr class="rule" style="margin-left:auto;margin-right:auto">
      <h2>More photographs are always welcome</h2>
      <p style="color:var(--ink-soft)">
        Tournament results, grading days, camps — send them over and they go up here.
      </p>
      <p style="margin-bottom:0">
        <a class="btn btn-outline" href="{WA}" target="_blank" rel="noopener">Send photos on WhatsApp</a>
      </p>
    </div>
  </section>

{cta_band(
    "Be in next year's photographs",
    "The first class is free, and there is no obligation afterwards.",
    '<a class="btn btn-light" href="/nippon-karate-club#registration">Book a free demo class</a>'
)}
""",
    )
