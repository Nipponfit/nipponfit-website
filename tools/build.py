# =====================================================================
# NIPPON FIT — page builder (the engine)
#
# WHAT THIS IS FOR
# ----------------
# Every page carries the same menu at the top and the same footer at the
# bottom. This file holds one copy of each, plus the page template, and
# stamps out finished HTML files.
#
# The .html files it writes are ordinary, complete, standalone pages.
# Nothing on the live site depends on Python.
#
# TO REBUILD THE WHOLE SITE:
#     python tools/build.py
#
# The page CONTENT lives in the files next to this one:
#     pages_main.py   home, club, instructors, locations, contact, login,
#                     registration, classes, 404
#     pages_blog.py   the blog index, the articles, and the gallery
# =====================================================================

import pathlib

ROOT = pathlib.Path(__file__).resolve().parent.parent

PHONE_DISPLAY = "+91 99456 16005"
PHONE_LINK = "+919945616005"
WHATSAPP = "919945616005"
EMAIL = "contactus@nipponfit.com"


# ---------------------------------------------------------------------
# The menu. Add a page here and it appears on every page of the site.
# ---------------------------------------------------------------------
MENU = [
    ("/", "Home"),
    ("/karate-classes-bangalore", "Programmes"),
    ("/nippon-karate-club", "Karate Club"),
    ("/instructors", "Instructors"),
    ("/gallery", "Gallery"),
    ("/blog", "Blog"),
    ("/locations", "Locations"),
    ("/contact", "Contact"),
]

MENU_HTML = "\n".join(
    f'      <li><a href="{href}">{label}</a></li>' for href, label in MENU
)

HEADER = f"""<a class="skip-link" href="#main">Skip to content</a>

<header class="site-header">
  <nav class="wrap nav" aria-label="Main">
    <a class="brand" href="/">
      <img src="/assets/logo.png" alt="Nippon Fit" width="40" height="40">
      <span class="brand-text">
        <span class="brand-name">NIPPON FIT</span>
        <span class="brand-tag">Bengaluru</span>
      </span>
    </a>

    <button class="nav-toggle" type="button" aria-expanded="false" aria-controls="menu">
      <span></span><span></span><span></span>
      <span class="sr-only">Menu</span>
    </button>

    <ul class="nav-links" id="menu">
{MENU_HTML}
      <li><a class="nav-cta" href="/login">Login</a></li>
    </ul>
  </nav>
</header>"""


SOCIAL = f"""<div class="social">
          <a href="https://www.facebook.com/Nipponfit" target="_blank" rel="noopener" aria-label="Nippon Fit on Facebook">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M22 12a10 10 0 1 0-11.6 9.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.2c-1.2 0-1.6.8-1.6 1.6V12h2.7l-.4 2.9h-2.3v7A10 10 0 0 0 22 12z"/></svg>
          </a>
          <a href="https://www.instagram.com/nippon_fit" target="_blank" rel="noopener" aria-label="Nippon Fit on Instagram">
            <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8"><rect x="2.5" y="2.5" width="19" height="19" rx="5"/><circle cx="12" cy="12" r="4.2"/><circle cx="17.4" cy="6.6" r="1.1" fill="currentColor" stroke="none"/></svg>
          </a>
          <a href="https://www.linkedin.com/company/nipponfit" target="_blank" rel="noopener" aria-label="Nippon Fit on LinkedIn">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M4.98 3.5a2.5 2.5 0 1 1 0 5 2.5 2.5 0 0 1 0-5zM3 9h4v12H3zM9 9h3.8v1.7h.05c.53-1 1.83-2.05 3.77-2.05 4.03 0 4.78 2.65 4.78 6.1V21h-4v-5.5c0-1.3-.02-3-1.83-3-1.83 0-2.11 1.43-2.11 2.9V21H9z"/></svg>
          </a>
        </div>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">

      <div class="footer-brand">
        <img src="/assets/logo.png" alt="Nippon Fit" width="46" height="46">
        <p>
          Karate training, fitness and self defence in Bengaluru, and the home of
          Nippon Karate Club.
        </p>
        {SOCIAL}
      </div>

      <div>
        <h4>Programmes</h4>
        <ul>
          <li><a href="/karate-classes-bangalore#karate">Karate Training</a></li>
          <li><a href="/karate-classes-bangalore#self-defence">Self Defence Training</a></li>
          <li><a href="/karate-classes-bangalore#strength">Strength &amp; Conditioning</a></li>
          <li><a href="/karate-classes-bangalore#weight-loss">Weight Loss</a></li>
          <li><a href="/karate-classes-bangalore#wellness">Wellness &amp; Fitness</a></li>
        </ul>
      </div>

      <div>
        <h4>Explore</h4>
        <ul>
          <li><a href="/nippon-karate-club">Nippon Karate Club</a></li>
          <li><a href="/nippon-karate-club#registration">Registration Form</a></li>
          <li><a href="/instructors">Instructors</a></li>
          <li><a href="/gallery">Gallery</a></li>
          <li><a href="/blog">Blog</a></li>
          <li><a href="/locations">Locations</a></li>
        </ul>
      </div>

      <div>
        <h4>Contact</h4>
        <address>
          Active Arena, Munnireddy Layout,<br>
          Panathur, Bengaluru, Karnataka<br><br>
          <a href="tel:{PHONE_LINK}">{PHONE_DISPLAY}</a><br>
          <a href="mailto:{EMAIL}">{EMAIL}</a>
        </address>
      </div>

    </div>

    <div class="footer-bottom">
      <span>&copy; <span data-year>2026</span> Nippon Fit. All rights reserved.</span>
      <span>Bengaluru, Karnataka, India</span>
    </div>
  </div>
</footer>

<a class="whatsapp-float"
   href="https://wa.me/{WHATSAPP}?text=Hello%20Nippon%20Fit%2C%20I%20would%20like%20to%20know%20more%20about%20your%20programmes."
   target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">
  <svg viewBox="0 0 24 24" fill="currentColor"><path d="M17.5 14.4c-.3-.15-1.77-.87-2.04-.97-.27-.1-.47-.15-.67.15-.2.3-.77.97-.94 1.17-.17.2-.35.22-.65.07-.3-.15-1.26-.46-2.4-1.48-.89-.79-1.49-1.76-1.66-2.06-.17-.3-.02-.46.13-.61.13-.13.3-.35.45-.52.15-.17.2-.3.3-.5.1-.2.05-.37-.02-.52-.08-.15-.67-1.61-.92-2.21-.24-.58-.49-.5-.67-.51h-.57c-.2 0-.52.07-.79.37-.27.3-1.04 1.02-1.04 2.48s1.06 2.88 1.21 3.08c.15.2 2.1 3.2 5.08 4.49.71.3 1.26.49 1.69.63.71.22 1.36.19 1.87.12.57-.09 1.77-.72 2.02-1.42.25-.7.25-1.3.17-1.42-.07-.13-.27-.2-.57-.35zM12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.6 0-3.2-.43-4.55-1.25l-.33-.19-3 .79.8-2.92-.21-.34A8.2 8.2 0 1 1 12 20.2z"/></svg>
</a>"""


DEFAULT_ROBOTS = "index, follow, max-image-preview:large, max-snippet:-1"


def page(slug, title, description, body,
         extra_head="", extra_scripts="", robots=DEFAULT_ROBOTS,
         og_image="/assets/founder-pooja.jpg"):
    """Write one finished HTML page to disk.

    slug "" means the home page (index.html)."""

    url = "https://www.nipponfit.com/" + slug
    filename = "index.html" if slug == "" else slug + ".html"

    html = f"""<!doctype html>
<html lang="en-IN">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">

<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{url}">

<meta name="robots" content="{robots}">
<meta name="theme-color" content="#1a1d24">

<meta property="og:type" content="website">
<meta property="og:site_name" content="Nippon Fit">
<meta property="og:locale" content="en_IN">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="https://www.nipponfit.com{og_image}">
<meta name="twitter:card" content="summary_large_image">

<link rel="icon" href="/assets/icon-192.png">
<link rel="apple-touch-icon" href="/assets/icon-192.png">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="/css/styles.css">
{extra_head}</head>

<body>

{HEADER}

<main id="main">
{body}
</main>

{FOOTER}

<script src="/js/main.js" defer></script>
{extra_scripts}</body>
</html>
"""

    out = ROOT / filename
    out.parent.mkdir(parents=True, exist_ok=True)   # e.g. the blog/ folder
    out.write_text(html, encoding="utf-8")
    print("  wrote", filename)


# ---------------------------------------------------------------------
# Small helpers used by the page files
# ---------------------------------------------------------------------

def crumbs(name):
    return f'<p class="crumbs"><a href="/">Home</a> &nbsp;/&nbsp; {name}</p>'


def breadcrumb_ld(name, slug):
    return f"""<script type="application/ld+json">
{{
  "@context": "https://schema.org",
  "@type": "BreadcrumbList",
  "itemListElement": [
    {{ "@type": "ListItem", "position": 1, "name": "Home", "item": "https://www.nipponfit.com/" }},
    {{ "@type": "ListItem", "position": 2, "name": "{name}", "item": "https://www.nipponfit.com/{slug}" }}
  ]
}}
</script>
"""


def cta_band(heading, text, buttons):
    return f"""
  <section class="cta-band">
    <div class="wrap">
      <h2>{heading}</h2>
      <p>{text}</p>
      <div class="cta-actions">{buttons}</div>
    </div>
  </section>
"""


if __name__ == "__main__":
    print("Building the Nippon Fit website...\n")

    import pages_main
    import pages_blog

    pages_main.build()
    pages_blog.build()

    print("\nDone. Preview it with:  python tools/serve.py")
