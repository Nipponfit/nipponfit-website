# =====================================================================
# NIPPON FIT — instructor photograph preparation
#
# WHAT THIS DOES
# --------------
# Takes an instructor's photograph however it arrives — a phone snap, a
# passport photo, a scan with a blue-grey background — and makes a clean,
# consistent, web-sized version for the Instructors page. Every card then
# looks like it belongs with the others, which is most of what makes a
# team page look professional.
#
# HOW TO USE IT
# -------------
# 1. Save the photographs into  F:\Nipponfit\Instructor_Originals\
#    named after the instructor, lower case:
#
#         darshan.jpg      arvind.jpg      jeevan.jpg
#
# 2. Run:
#
#         python tools/prepare_instructor_photos.py
#
# 3. Then rebuild the site:
#
#         python tools/build.py
#
# The photographs are picked up automatically — there is no HTML to edit.
# The originals are never changed.
# =====================================================================

import pathlib
from PIL import Image, ImageOps, ImageEnhance, ImageFilter


def person_name(path):
    """The instructor's name from a file name.

    Copes with a file saved as gi-pair.jpg.png — Windows and some chat apps
    add a second extension, and the name we want is the part before all of
    them. Also lower-cases and trims, so Arvind.JPEG and arvind.jpg are
    treated as the same person."""
    stem = path.name
    while "." in stem:
        head, _, tail = stem.rpartition(".")
        if len(tail) > 5 or not tail.isalnum():
            break
        stem = head
    return stem.lower().strip()

ROOT = pathlib.Path(__file__).resolve().parent.parent
ORIGINALS = ROOT.parent / "Instructor_Originals"
ASSETS = ROOT / "assets"

# The cards are 3:4 — upright, like the passport photographs themselves.
# Cropping a tall headshot into a wide frame zooms right into the face and
# looks cramped, so the card matches the photograph instead.
WIDTH, HEIGHT = 900, 1200
QUALITY = 86

# A photograph cropped out of a group shot can be small. Enlarging it to the
# full card size would only make it blurry, so cap how far we stretch it.
MAX_UPSCALE = 2.5

# How far down the source the crop starts, when the photograph is taller
# than the card. 0.25 keeps a little headroom above the hair rather than
# slicing the top of the head off.
FACE_LINE = 0.25

# ---------------------------------------------------------------------
# CUTTING OFF THE BELT
#
# On some photographs the belt carries embroidery we do not want on the
# page. Name a file in BELT_CROP and everything below that fraction of
# its height is thrown away before anything else happens — so the belt,
# and whatever is written on it, never reaches the website at all.
#
# 0.74 means "keep the top 74%", which lands above the belt knot.
# Lower the number to cut higher; raise it to keep more.
# ---------------------------------------------------------------------
BELT_CROP = {
    "arvind": 0.74,
    "jeevan": 0.74,
}

# ---------------------------------------------------------------------
# SPLITTING A SIDE-BY-SIDE PICTURE
#
# One image with two people in it, side by side, gets cut down the middle.
# Name the file here and say who is on the left and who is on the right.
# ---------------------------------------------------------------------
SIDE_BY_SIDE = {
    "gi-pair": ("arvind", "jeevan"),
}


def prepare(src, destination, belt_crop=None):
    im = ImageOps.exif_transpose(Image.open(src)).convert("RGB")

    # Cut the belt off first, before any framing, so nothing written on it
    # can survive into the finished picture.
    if belt_crop:
        im = im.crop((0, 0, im.width, int(im.height * belt_crop)))

    # A passport photo is usually taller than it is wide, and the head sits
    # high in it. Crop to 4:3 around the upper part rather than the middle,
    # so we do not cut the top of the head off.
    target = WIDTH / HEIGHT
    w, h = im.size

    if w / h > target:
        # too wide — trim the sides evenly
        new_w = int(h * target)
        left = (w - new_w) // 2
        im = im.crop((left, 0, left + new_w, h))
    else:
        # too tall — keep the upper part, where the face is.
        # If we have already cut the belt off, the bottom is gone anyway, so
        # anchor right at the top: otherwise we trim from both ends and end
        # up cropping into the face.
        new_h = int(w / target)
        top = 0 if belt_crop else int((h - new_h) * FACE_LINE)
        top = max(0, min(top, h - new_h))
        im = im.crop((0, top, w, top + new_h))

    # Never blow a photograph up more than 2.5x. Darshan's is cropped out of
    # a group shot, so the source is small; forcing it to the full card size
    # would just make it mushy. The card scales it down to fit anyway.
    scale = min(WIDTH / im.width, MAX_UPSCALE)
    final = (round(im.width * scale), round(im.height * scale))

    if scale > 1.15:
        # Enlarging. Go up in two smaller steps rather than one big jump —
        # less detail is lost that way — and sharpen with an unsharp mask
        # after each. An unsharp mask lifts edges specifically, where a
        # blanket sharpness boost also amplifies the grain.
        half = (round(im.width * scale * 0.65), round(im.height * scale * 0.65))
        im = im.resize(half, Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(radius=1.4, percent=105, threshold=3))
        im = im.resize(final, Image.LANCZOS)
        im = im.filter(ImageFilter.UnsharpMask(radius=0.9, percent=85, threshold=2))
        im = ImageEnhance.Color(im).enhance(1.05)
        im = ImageEnhance.Contrast(im).enhance(1.08)
    else:
        # Shrinking, or barely changing size. A gentle lift is all it needs —
        # scanned passport photos are usually flat and slightly cold.
        im = im.resize(final, Image.LANCZOS)
        im = ImageEnhance.Color(im).enhance(1.06)
        im = ImageEnhance.Contrast(im).enhance(1.06)
        im = ImageEnhance.Sharpness(im).enhance(1.15)

    im.save(destination, "JPEG", quality=QUALITY, optimize=True, progressive=True)
    return im.size, destination.stat().st_size


def main():
    if not ORIGINALS.exists():
        ORIGINALS.mkdir(parents=True)
        print(f"Created {ORIGINALS}")
        print("Put the instructor photographs in there, named darshan.jpg,")
        print("arvind.jpg and jeevan.jpg, then run this again.")
        return

    found = 0

    # ---- First, cut any side-by-side picture into two -----------------
    for src in sorted(ORIGINALS.iterdir()):
        if not src.is_file():
            continue
        pair = SIDE_BY_SIDE.get(person_name(src))
        if not pair:
            continue

        whole = ImageOps.exif_transpose(Image.open(src)).convert("RGB")
        mid = whole.width // 2
        halves = [whole.crop((0, 0, mid, whole.height)),
                  whole.crop((mid, 0, whole.width, whole.height))]

        for person, half in zip(pair, halves):
            single = ORIGINALS / f"{person}.jpg"

            # An older photograph of the same person — Arvind.jpeg beside
            # arvind.jpg — would fight this one for the same output file, and
            # which won would come down to alphabetical order. Put any such
            # file out of the way first.
            for other in ORIGINALS.iterdir():
                if (other.is_file() and other != single
                        and person_name(other) == person
                        and not other.name.startswith("_")):
                    other.rename(ORIGINALS / f"_superseded_{other.name}")
                    print(f"  set aside older photo: {other.name}")

            half.save(single, "JPEG", quality=95)
            print(f"  split {src.name}: {person} -> {single.name}  {half.size[0]}x{half.size[1]}")

        # keep the original pair, but out of the way of the next loop
        src.rename(ORIGINALS / f"_{src.name}")

    # ---- Then prepare each individual photograph ----------------------
    for src in sorted(ORIGINALS.iterdir()):
        if not src.is_file() or src.suffix.lower() not in (".jpg", ".jpeg", ".png", ".webp"):
            continue
        if src.name.startswith("_"):        # the stored-away pair original
            continue

        name = person_name(src)
        out = ASSETS / f"instructor-{name}.jpg"
        size, filesize = prepare(src, out, belt_crop=BELT_CROP.get(name))
        print(f"  {src.name:24} ->  assets/{out.name:26} {size[0]}x{size[1]}  {filesize/1000:.0f} KB")
        found += 1

    if not found:
        print(f"No photographs found in {ORIGINALS}")
    else:
        print(f"\n{found} photograph(s) prepared.")
        print("Now run:  python tools/build.py")


if __name__ == "__main__":
    print("Preparing instructor photographs...\n")
    main()
