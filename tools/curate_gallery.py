# =====================================================================
# NIPPON FIT — gallery photo preparation
#
# WHAT THIS DOES
# --------------
# Takes the photographs as they come off a phone or WhatsApp — 4, 6, even
# 7 megabytes each — and turns them into web-sized copies that load fast,
# with tidy names and the right way up.
#
# It also writes out the photo list for js/gallery.js so the captions and
# the files can never drift apart.
#
# WHEN TO RUN IT
# --------------
# Only when you add new photographs. Put the new pictures in
# F:\Nipponfit\Gallery_Originals\ — which sits OUTSIDE the website folder
# on purpose, so 65 MB of phone photographs never get published — then
# add a line for each in PHOTOS below and run:
#
#     python tools/curate_gallery.py
#
# The originals are never touched or deleted — only copied and shrunk.
# =====================================================================

import pathlib
import shutil
from PIL import Image, ImageOps

ROOT = pathlib.Path(__file__).resolve().parent.parent
GALLERY = ROOT / "assets" / "gallery"
THUMBS = GALLERY / "thumbs"
ORIGINALS = ROOT.parent / "Gallery_Originals"   # deliberately outside the website

# Long edge in pixels. 1800 is plenty for a full-width photo on a large
# screen, and about a twentieth of the file size of a phone original.
MAX_EDGE = 1800
QUALITY = 82

# A second, much smaller copy of every photograph, for the grid of little
# squares. Loading 44 full-size pictures there would be painfully slow.
THUMB_EDGE = 500
THUMB_QUALITY = 78


# ---------------------------------------------------------------------
# THE PHOTOGRAPHS, in the order they appear on the site.
#
#   (original file, new name, title, caption)
#
# The title is the bold line over the photo; the caption is the smaller
# grey line under it.
# ---------------------------------------------------------------------
PHOTOS = [
    # --- The Ugur Aktas seminar: our strongest story, so it leads ------
    ("WhatsApp Image 2026-08-19 at 10.57.32 PM.jpeg", "01-ugur-aktas-seminar-group",
     "The Ugur Aktas seminar",
     "A first for India — hosting the Tokyo Olympic bronze medallist from Turkey"),

    ("WhatsApp Image 2026-08-19 at 10.57.34 PM (3).jpeg", "02-ugur-aktas-with-team",
     "Ugur Aktas with our team",
     "Dravid Centre for Sports Excellence, Bengaluru"),

    ("WhatsApp Image 2026-08-19 at 10.57.33 PM.jpeg", "03-seminar-in-progress",
     "Elite kumite seminar",
     "Working through the drills at the Dravid Centre for Sports Excellence"),

    ("WhatsApp Image 2026-08-19 at 10.57.34 PM (2).jpeg", "04-seminar-full-group",
     "Everyone who trained that day",
     "The full seminar group"),

    ("WhatsApp Image 2026-08-19 at 10.57.34 PM (1).jpeg", "05-seminar-students",
     "Our students at the seminar",
     "Training alongside an Olympic medallist"),

    ("WhatsApp Image 2026-08-19 at 10.57.34 PM.jpeg", "06-ugur-aktas",
     "Ugur Aktas",
     "Tokyo 2020 Olympic bronze medallist, Turkey"),

    ("WhatsApp Image 2026-08-19 at 10.57.32 PM (1).jpeg", "07-seminar-organisers",
     "Behind the seminar",
     "Organisers at the Dravid Centre for Sports Excellence"),

    # --- International ------------------------------------------------
    ("IMG_20230130_150007 (1).jpg", "08-india-karate-team",
     "Representing India",
     "Nippon Karate Club on the international circuit"),

    ("WhatsApp Image 2026-08-19 at 10.44.37 PM (1).jpeg", "09-karate1-series-a-kuala-lumpur",
     "Karate 1 Series A",
     "Kuala Lumpur, 2025"),

    ("WhatsApp Image 2026-08-19 at 10.57.26 PM (2).jpeg", "10-silent-knight-karate-cup",
     "Silent Knight Karate Cup 2024",
     "On the podium in Kuala Lumpur"),

    ("WhatsApp Image 2026-08-19 at 10.44.38 PM (1).jpeg", "11-international-karate-championship",
     "15th International Karate Championship",
     "With masters and officials"),

    # --- National -----------------------------------------------------
    ("IMG_2834.jpeg", "12-10th-national-championship",
     "10th National Karate Championship 2024",
     "Our squad with their medals"),

    ("WhatsApp Image 2026-08-19 at 10.44.37 PM.jpeg", "13-all-india-national-open",
     "All India National Open Karate Championship",
     "Nippon Karate Club at the Nationals"),

    ("WhatsApp Image 2026-08-19 at 10.57.30 PM (3).jpeg", "14-all-india-national-level-open",
     "All India National Level Open Championship",
     "Medallists from the club"),

    ("WhatsApp Image 2026-08-19 at 10.57.31 PM (1).jpeg", "15-inter-zonal-championship",
     "IV All India Inter-Zonal Championship",
     "Organised by the Karate India Organisation"),

    ("WhatsApp Image 2026-08-19 at 10.57.31 PM (2).jpeg", "16-inter-zonal-medallists",
     "Inter-Zonal medallists",
     "IV All India Inter-Zonal Karate Championship"),

    ("WhatsApp Image 2026-08-19 at 10.57.31 PM.jpeg", "17-inter-zonal-presentation",
     "Receiving the award",
     "IV All India Inter-Zonal Karate Championship"),

    ("IMG_1524 (1).jpeg", "18-kio-national-podium",
     "On the national podium",
     "Karate India Organisation championship, Chennai"),

    ("WhatsApp Image 2026-08-19 at 10.57.30 PM (2).jpeg", "19-united-martial-arts",
     "United Martial Arts — Evolution of Karate",
     "Trophies and medals for the club"),

    ("fcb4a0f3-8fb9-42dd-a43e-3a5596d1f2a3.jpeg", "20-state-level-open-2024",
     "1st State Level Open Karate Championship",
     "Bengaluru, November 2024"),

    # --- State (AKSKA) -------------------------------------------------
    ("IMG_7051.jpeg", "21-akska-16th-state-championship",
     "16th State Level Karate Championship",
     "Akhila Karnataka Sports Karate Association"),

    ("IMG_7053.jpeg", "22-akska-16th-certificates",
     "State championship certificates",
     "16th State Level Karate Championship"),

    ("IMG_7058.jpeg", "23-akska-16th-medallists",
     "State medallists",
     "16th State Level Karate Championship"),

    ("IMG_7061.jpeg", "24-akska-16th-squad",
     "Our state squad",
     "16th State Level Karate Championship"),

    ("WhatsApp Image 2026-08-19 at 10.57.35 PM (1).jpeg", "25-akska-17th-state-championship",
     "17th State Level Karate Championship",
     "National selection tournament"),

    ("WhatsApp Image 2026-08-19 at 10.57.35 PM (2).jpeg", "26-akska-17th-certificates",
     "Certificates at the state championship",
     "17th State Level Karate Championship"),

    ("WhatsApp Image 2026-08-19 at 10.57.35 PM.jpeg", "27-akska-17th-award",
     "Receiving a state award",
     "17th State Level Karate Championship"),

    ("WhatsApp Image 2026-08-19 at 10.57.36 PM.jpeg", "28-akska-17th-officials",
     "With the officials",
     "17th State Level Karate Championship"),

    ("2b15be96-acf4-4616-985d-40223072f5c5 (1).jpeg", "29-akska-award-ceremony",
     "Award ceremony",
     "Akhila Karnataka Sports Karate Association"),

    ("IMG_1983 (1).jpeg", "30-district-championship",
     "District championship",
     "Medals for the club"),

    ("WhatsApp Image 2026-08-19 at 10.57.28 PM.jpeg", "31-state-certificates",
     "State championship certificates",
     "Akhila Karnataka Sports Karate Association"),

    ("WhatsApp Image 2026-08-19 at 10.44.38 PM (2).jpeg", "32-tournament-winner",
     "Tournament winner",
     "Certificate and trophy"),

    # --- The club, the students, the everyday --------------------------
    ("IMG_5076 (1).jpeg", "33-trophy-haul",
     "A season of trophies",
     "The club's haul from one year of competition"),

    ("WhatsApp Image 2026-08-19 at 10.57.27 PM (2).jpeg", "34-trophy-haul-squad",
     "The squad behind the trophies",
     "Nippon Karate Club, Bengaluru"),

    ("259489A2-6012-4851-939D-60A87F96AD3D.jpeg", "35-students-with-trophies",
     "Bringing them home",
     "Students with the season's trophies"),

    ("AFBD0C32-C3AB-4BB4-BCC2-A681F473A82A.jpeg", "36-junior-squad",
     "Our junior squad",
     "Nippon Karate Club, Bengaluru"),

    ("IMG_5485 (1).jpeg", "37-certificates",
     "Certificates earned",
     "Students of Nippon Karate Club"),

    ("IMG_5073.jpeg", "38-young-champion",
     "A young champion",
     "With his instructor and his first trophy"),

    ("IMG_2659.jpeg", "39-dojo-line-up",
     "Ready to begin",
     "Students lined up at the dojo"),

    ("IMG_2672.jpeg", "40-instructors-and-students",
     "Instructors and students",
     "At the dojo"),

    ("WhatsApp Image 2026-08-19 at 10.57.30 PM (1).jpeg", "41-medal-winners",
     "Medal winners",
     "Nippon Karate Club"),

    ("2c5e054a-39ca-47ae-b39f-840b680efc84.jpeg", "42-medal-and-trophy",
     "Medal and trophy",
     "A proud day"),

    ("WhatsApp Image 2026-08-19 at 11.37.34 PM.jpeg", "43-all-india-open-2026",
     "All India Open Karate Championship 2026",
     "Champions are not born, they are built"),

    ("WhatsApp Image 2026-08-19 at 10.44.38 PM.jpeg", "44-certificates-pair",
     "Two of our students",
     "Certificates from the championship"),
]


# ---------------------------------------------------------------------
# Files that are NOT achievement photographs and should not be in the
# gallery. They are moved out rather than deleted.
# ---------------------------------------------------------------------
NOT_GALLERY = {
    # A text graphic explaining the characters for "kara te" — belongs
    # with the Origin of Karate-Do article, not in an achievements gallery.
    "C2DB6B0E-C4AC-43AB-8B8A-414E5B5EE2F4.jpeg": ROOT / "assets" / "karate-characters.jpg",
}

# Copies of pictures already used elsewhere on the site.
ALREADY_USED_ELSEWHERE = ["02-kumite.jpg", "03-training.jpg"]


def main():
    ORIGINALS.mkdir(exist_ok=True)
    THUMBS.mkdir(exist_ok=True)

    # ---- 1. Clear the gallery folder ----------------------------------
    # Anything this script made before is deleted, because it is about to
    # be made again. Anything else — a new photograph dropped straight
    # into assets/gallery/ — is moved into the originals folder so it is
    # kept, not lost.
    generated = {newname + ".jpg" for _, newname, _, _ in PHOTOS}

    for f in list(GALLERY.iterdir()):
        if not f.is_file():
            continue    # skips the thumbs/ folder
        if f.name in generated:
            f.unlink()
        else:
            shutil.move(str(f), str(ORIGINALS / f.name))
            print(f"  kept your new photo: moved {f.name} into Gallery_Originals")

    # ---- 2. Pull out the ones that are not gallery photographs --------
    for name, destination in NOT_GALLERY.items():
        src = ORIGINALS / name
        if src.exists():
            im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
            im.save(destination, "JPEG", quality=88, optimize=True)
            print(f"  moved out of the gallery: {name} -> {destination.name}")

    for name in ALREADY_USED_ELSEWHERE:
        src = ORIGINALS / name
        if src.exists():
            src.unlink()
            print(f"  removed (already used elsewhere on the site): {name}")

    # ---- 3. Shrink and rename the gallery photographs -----------------
    saved_before = saved_after = 0
    written = []

    for original, newname, title, note in PHOTOS:
        src = ORIGINALS / original
        if not src.exists():
            print(f"  !! MISSING: {original}")
            continue

        saved_before += src.stat().st_size

        im = Image.open(src)
        im = ImageOps.exif_transpose(im)        # honour the phone's rotation flag
        im = im.convert("RGB")
        im.thumbnail((MAX_EDGE, MAX_EDGE), Image.LANCZOS)

        out = GALLERY / (newname + ".jpg")
        im.save(out, "JPEG", quality=QUALITY, optimize=True, progressive=True)

        # the small square for the grid
        thumb = im.copy()
        thumb.thumbnail((THUMB_EDGE, THUMB_EDGE), Image.LANCZOS)
        thumb.save(THUMBS / (newname + ".jpg"), "JPEG",
                   quality=THUMB_QUALITY, optimize=True)

        saved_after += out.stat().st_size
        written.append((newname + ".jpg", title, note, im.size))

    print(f"\n  {len(written)} photographs prepared")
    print(f"  {saved_before/1e6:.1f} MB  ->  {saved_after/1e6:.1f} MB "
          f"({saved_after/saved_before*100:.0f}% of the original)")

    # ---- 4. Write the list into js/gallery.js -------------------------
    write_gallery_js(written)


def write_gallery_js(photos):
    """Rewrite only the PHOTOS list inside js/gallery.js, leaving the rest
    of that file exactly as it is."""
    js_path = ROOT / "js" / "gallery.js"
    text = js_path.read_text(encoding="utf-8")

    entries = []
    for filename, title, note, size in photos:
        entries.append(
            "    {\n"
            f'      src: "/assets/gallery/{filename}",\n'
            f'      title: "{title}",\n'
            f'      note: "{note}"\n'
            "    }"
        )

    block = "  var PHOTOS = [\n" + ",\n".join(entries) + "\n  ];"

    start = text.index("  var PHOTOS = [")
    end = text.index("\n  ];", start) + len("\n  ];")

    js_path.write_text(text[:start] + block + text[end:], encoding="utf-8")
    print(f"  js/gallery.js updated with {len(photos)} photographs")


if __name__ == "__main__":
    print("Preparing the gallery photographs...\n")
    main()
    print("\nDone.")
