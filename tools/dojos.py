# =====================================================================
# NIPPON FIT — the three dojos, held ONCE
#
# Every address, map and directions link on the site comes from here:
# the home page branch cards, the Locations page, the Contact page, the
# footer, the schema code and the three dojo pages.
#
# The addresses are copied exactly from each place's Google Maps listing
# (checked 22 November 2026). If an address ever changes, change it here
# and on Google, word for word, then run:  python tools/build.py
#
# Disha Central Park (Balagere) is deliberately NOT here: it is an
# apartment class, not a public dojo, and stays off the website.
#
# Class timings are deliberately NOT here either. Renshi Pooja's rule:
# timings are never published on the site.
# =====================================================================

from urllib.parse import quote_plus

DOJOS = [
    {
        "key": "panathur",
        "slug": "dojo-panathur",
        "name": "Active Arena",
        "label": "Active Arena, Kadubeesanahalli",
        "venue": "Active Arena",
        "street": "Outer Ring Road, opposite Prestige Tech Park, behind Croma",
        "area": "Kadubeesanahalli, Marathahalli",
        "postcode": "560087",
        "lat": 12.9428141,
        "lng": 77.6999966,
        # Our own Google Business Profile ("Nippon Fit")
        "maps_name": "Nippon Fit",
        "place_id": "ChIJiw8sHnMTrjsRi9263tgCKN8",
        "cid": "16080105599999335819",
        "embed_query": "Nippon Fit, Active Arena, Outer Ring Road, Kadubeesanahalli, Bengaluru 560087",
        "near": ["Panathur", "Kadubeesanahalli", "Marathahalli", "Bellandur",
                 "Whitefield", "Sarjapur Road", "Varthur", "Brookefield"],
        "card": "Our main dojo, on the Outer Ring Road. Closest for Bellandur, "
                "Marathahalli, Whitefield, Sarjapur Road and Varthur.",
    },
    {
        "key": "koramangala",
        "slug": "dojo-koramangala",
        "name": "The Koramangala Club",
        "label": "The Koramangala Club, Koramangala",
        "venue": "The Koramangala Club",
        "street": "CA-17, 6th Cross Road, 6th Block",
        "area": "Koramangala",
        "postcode": "560095",
        "lat": 12.9383302,
        "lng": 77.6241678,
        # The venue's own Google listing
        "maps_name": "The Koramangala Club",
        "place_id": "ChIJM3G8ZkQUrjsRfIBt5twkcjg",
        "cid": "4067353944646320252",
        "embed_query": "The Koramangala Club, CA-17, 6th Cross Road, 6th Block, Koramangala, Bengaluru 560095",
        "near": ["Koramangala", "HSR Layout", "Indiranagar", "Ejipura",
                 "Domlur", "BTM Layout"],
        "card": "Inside The Koramangala Club, 6th Block. For families in Koramangala, "
                "HSR Layout, Indiranagar and central Bengaluru.",
    },
    {
        "key": "yelahanka",
        "slug": "dojo-dravid-cse",
        "name": "Dravid Centre for Sports Excellence",
        "label": "Dravid Centre for Sports Excellence, Yelahanka",
        "venue": "Padukone-Dravid Centre for Sports Excellence",
        "street": "",
        "area": "Bettahalsoor",
        "postcode": "562157",
        "lat": 13.1683121,
        "lng": 77.5945365,
        # Our own verified Google Business Profile, "Nippon Karate Club",
        # pinned on our dedicated floor inside the campus (checked 22 Nov 2026).
        # Directions go to these coordinates, as no place ID was available.
        "maps_name": "Nippon Karate Club",
        "place_id": None,
        "cid": "17382461994412505121",
        "embed_query": "Nippon Karate Club, Padukone-Dravid Centre for Sports Excellence, Bettahalsoor, Bengaluru 562157",
        "near": ["Yelahanka", "Jakkur", "Hebbal", "Sahakar Nagar",
                 "Thanisandra", "Devanahalli"],
        "card": "Our own dedicated floor inside the Padukone-Dravid Centre for Sports "
                "Excellence, a national-standard campus in Yelahanka. For north Bengaluru.",
    },
]

DOJO = {d["key"]: d for d in DOJOS}


def address_lines(d):
    """The address as it appears on Google, split for display."""
    lines = [d["venue"], d["street"], f'{d["area"]}, Bengaluru, Karnataka {d["postcode"]}']
    return [x for x in lines if x]


def address_html(d, sep="<br>"):
    return sep.join(address_lines(d))


def address_text(d):
    return ", ".join(address_lines(d))


def embed_url(d):
    """Google's keyless map embed, centred on the place by name and address."""
    return "https://maps.google.com/maps?q=" + quote_plus(d["embed_query"]) + "&amp;z=16&amp;output=embed"


def directions_url(d):
    """Google Maps directions straight to the exact listing (place ID)."""
    if not d["place_id"]:
        return f'https://www.google.com/maps/dir/?api=1&amp;destination={d["lat"]},{d["lng"]}'
    return ("https://www.google.com/maps/dir/?api=1&amp;destination=" + quote_plus(d["maps_name"])
            + "&amp;destination_place_id=" + d["place_id"])


def maps_url(d):
    """The listing itself on Google Maps (used in the schema code)."""
    return "https://www.google.com/maps?cid=" + d["cid"]


def page_url(d):
    return "https://www.nipponfit.com/" + d["slug"]


def postal_ld(d):
    return (
        '{ "@type": "PostalAddress", '
        f'"streetAddress": "{", ".join(x for x in (d["venue"], d["street"], d["area"]) if x)}", '
        '"addressLocality": "Bengaluru", "addressRegion": "Karnataka", '
        f'"postalCode": "{d["postcode"]}", "addressCountry": "IN" }}'
    )


def geo_ld(d):
    return f'{{ "@type": "GeoCoordinates", "latitude": {d["lat"]}, "longitude": {d["lng"]} }}'


def department_ld(d):
    """One dojo as a schema.org SportsActivityLocation, for the home page graph."""
    return f"""{{
          "@type": "SportsActivityLocation",
          "@id": "{page_url(d)}#dojo",
          "name": "Nippon Karate Club \\u2014 {d["name"]}",
          "url": "{page_url(d)}",
          "telephone": "+91-9945616005",
          "address": {postal_ld(d)},
          "geo": {geo_ld(d)},
          "hasMap": "{maps_url(d)}"
        }}"""


def branch_card(d, more_link=True):
    """The map card used on the home page and the Locations page."""
    more = (f'<p style="margin-bottom:18px"><a class="link-more" href="/{d["slug"]}">'
            f'About this dojo</a></p>') if more_link else ""
    return f"""
        <article class="branch">
          <iframe class="branch-map"
                  src="{embed_url(d)}"
                  title="Map of {d["label"]}" loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"></iframe>
          <div class="branch-body">
            <h3><a href="/{d["slug"]}" style="color:inherit">{d["name"]}</a></h3>
            <address>{address_html(d)}</address>
            <p>{d["card"]}</p>
            {more}
            <a class="btn btn-outline" href="{directions_url(d)}" target="_blank" rel="noopener">Directions</a>
          </div>
        </article>
"""
