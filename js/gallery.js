/* =====================================================================
   NIPPON FIT — the achievement gallery slideshow.

   TO ADD A PHOTOGRAPH
   -------------------
   1. Save the picture into  assets/gallery/
   2. Add one line to the PHOTOS list below, copying the pattern.
   3. Save. That is all — the slideshow and the grid underneath both
      pick it up automatically.

   Keep the file names simple: no spaces, lower case, ending .jpg or
   .png. Something like  2026-national-gold.jpg

   TO CHANGE HOW LONG EACH PHOTO STAYS ON SCREEN
   ---------------------------------------------
   It is set to 15 seconds. That number lives in gallery.html, on the
   line that reads  data-interval="15000"  (15000 = 15 seconds).
   ===================================================================== */

(function () {
  "use strict";

  /* ----------------------------------------------------------------
     THE PHOTOGRAPHS
     ----------------------------------------------------------------
     src     the file, inside assets/gallery/
     title   the bold line shown over the photo
     note    the smaller grey line underneath it
     ---------------------------------------------------------------- */
  var PHOTOS = [
    {
      src: "/assets/gallery/01-ugur-aktas-seminar-group.jpg",
      title: "The Ugur Aktas seminar",
      note: "A first for India — hosting the Tokyo Olympic bronze medallist from Turkey"
    },
    {
      src: "/assets/gallery/02-ugur-aktas-with-team.jpg",
      title: "Ugur Aktas with our team",
      note: "Dravid Centre for Sports Excellence, Bengaluru"
    },
    {
      src: "/assets/gallery/03-seminar-in-progress.jpg",
      title: "Elite kumite seminar",
      note: "Working through the drills at the Dravid Centre for Sports Excellence"
    },
    {
      src: "/assets/gallery/04-seminar-full-group.jpg",
      title: "Everyone who trained that day",
      note: "The full seminar group"
    },
    {
      src: "/assets/gallery/05-seminar-students.jpg",
      title: "Our students at the seminar",
      note: "Training alongside an Olympic medallist"
    },
    {
      src: "/assets/gallery/06-ugur-aktas.jpg",
      title: "Ugur Aktas",
      note: "Tokyo 2020 Olympic bronze medallist, Turkey"
    },
    {
      src: "/assets/gallery/07-seminar-organisers.jpg",
      title: "Behind the seminar",
      note: "Organisers at the Dravid Centre for Sports Excellence"
    },
    {
      src: "/assets/gallery/08-india-karate-team.jpg",
      title: "Representing India",
      note: "Nippon Karate Club on the international circuit"
    },
    {
      src: "/assets/gallery/09-karate1-series-a-kuala-lumpur.jpg",
      title: "Karate 1 Series A",
      note: "Kuala Lumpur, 2025"
    },
    {
      src: "/assets/gallery/10-silent-knight-karate-cup.jpg",
      title: "Silent Knight Karate Cup 2024",
      note: "On the podium in Kuala Lumpur"
    },
    {
      src: "/assets/gallery/11-international-karate-championship.jpg",
      title: "15th International Karate Championship",
      note: "With masters and officials"
    },
    {
      src: "/assets/gallery/12-10th-national-championship.jpg",
      title: "10th National Karate Championship 2024",
      note: "Our squad with their medals"
    },
    {
      src: "/assets/gallery/13-all-india-national-open.jpg",
      title: "All India National Open Karate Championship",
      note: "Nippon Karate Club at the Nationals"
    },
    {
      src: "/assets/gallery/14-all-india-national-level-open.jpg",
      title: "All India National Level Open Championship",
      note: "Medallists from the club"
    },
    {
      src: "/assets/gallery/15-inter-zonal-championship.jpg",
      title: "IV All India Inter-Zonal Championship",
      note: "Organised by the Karate India Organisation"
    },
    {
      src: "/assets/gallery/16-inter-zonal-medallists.jpg",
      title: "Inter-Zonal medallists",
      note: "IV All India Inter-Zonal Karate Championship"
    },
    {
      src: "/assets/gallery/17-inter-zonal-presentation.jpg",
      title: "Receiving the award",
      note: "IV All India Inter-Zonal Karate Championship"
    },
    {
      src: "/assets/gallery/18-kio-national-podium.jpg",
      title: "On the national podium",
      note: "Karate India Organisation championship, Chennai"
    },
    {
      src: "/assets/gallery/19-united-martial-arts.jpg",
      title: "United Martial Arts — Evolution of Karate",
      note: "Trophies and medals for the club"
    },
    {
      src: "/assets/gallery/20-state-level-open-2024.jpg",
      title: "1st State Level Open Karate Championship",
      note: "Bengaluru, November 2024"
    },
    {
      src: "/assets/gallery/21-akska-16th-state-championship.jpg",
      title: "16th State Level Karate Championship",
      note: "Akhila Karnataka Sports Karate Association"
    },
    {
      src: "/assets/gallery/22-akska-16th-certificates.jpg",
      title: "State championship certificates",
      note: "16th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/23-akska-16th-medallists.jpg",
      title: "State medallists",
      note: "16th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/24-akska-16th-squad.jpg",
      title: "Our state squad",
      note: "16th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/25-akska-17th-state-championship.jpg",
      title: "17th State Level Karate Championship",
      note: "National selection tournament"
    },
    {
      src: "/assets/gallery/26-akska-17th-certificates.jpg",
      title: "Certificates at the state championship",
      note: "17th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/27-akska-17th-award.jpg",
      title: "Receiving a state award",
      note: "17th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/28-akska-17th-officials.jpg",
      title: "With the officials",
      note: "17th State Level Karate Championship"
    },
    {
      src: "/assets/gallery/29-akska-award-ceremony.jpg",
      title: "Award ceremony",
      note: "Akhila Karnataka Sports Karate Association"
    },
    {
      src: "/assets/gallery/30-district-championship.jpg",
      title: "District championship",
      note: "Medals for the club"
    },
    {
      src: "/assets/gallery/31-state-certificates.jpg",
      title: "State championship certificates",
      note: "Akhila Karnataka Sports Karate Association"
    },
    {
      src: "/assets/gallery/32-tournament-winner.jpg",
      title: "Tournament winner",
      note: "Certificate and trophy"
    },
    {
      src: "/assets/gallery/33-trophy-haul.jpg",
      title: "A season of trophies",
      note: "The club's haul from one year of competition"
    },
    {
      src: "/assets/gallery/34-trophy-haul-squad.jpg",
      title: "The squad behind the trophies",
      note: "Nippon Karate Club, Bengaluru"
    },
    {
      src: "/assets/gallery/35-students-with-trophies.jpg",
      title: "Bringing them home",
      note: "Students with the season's trophies"
    },
    {
      src: "/assets/gallery/36-junior-squad.jpg",
      title: "Our junior squad",
      note: "Nippon Karate Club, Bengaluru"
    },
    {
      src: "/assets/gallery/37-certificates.jpg",
      title: "Certificates earned",
      note: "Students of Nippon Karate Club"
    },
    {
      src: "/assets/gallery/38-young-champion.jpg",
      title: "A young champion",
      note: "With his instructor and his first trophy"
    },
    {
      src: "/assets/gallery/39-dojo-line-up.jpg",
      title: "Ready to begin",
      note: "Students lined up at the dojo"
    },
    {
      src: "/assets/gallery/40-instructors-and-students.jpg",
      title: "Instructors and students",
      note: "At the dojo"
    },
    {
      src: "/assets/gallery/41-medal-winners.jpg",
      title: "Medal winners",
      note: "Nippon Karate Club"
    },
    {
      src: "/assets/gallery/42-medal-and-trophy.jpg",
      title: "Medal and trophy",
      note: "A proud day"
    },
    {
      src: "/assets/gallery/43-all-india-open-2026.jpg",
      title: "All India Open Karate Championship 2026",
      note: "Champions are not born, they are built"
    },
    {
      src: "/assets/gallery/44-certificates-pair.jpg",
      title: "Two of our students",
      note: "Certificates from the championship"
    }
  ];

  var gallery = document.getElementById("gallery");
  var stage = document.getElementById("gallery-stage");
  var dotsRow = document.getElementById("gallery-dots");
  var grid = document.getElementById("gallery-grid");

  if (!gallery || !stage) return;

  /* How long each photograph stays up. Read from the page, so it can be
     changed there without touching this file. */
  var INTERVAL = Number(gallery.dataset.interval) || 15000;

  /* The home page shows only the first few photographs — 44 dots along the
     bottom would be unusable. The Gallery page sets no limit and shows all
     of them. Set with data-limit="8" on the gallery element. */
  var LIMIT = Number(gallery.dataset.limit) || PHOTOS.length;
  if (LIMIT < PHOTOS.length) PHOTOS = PHOTOS.slice(0, LIMIT);

  var current = 0;
  var timer = null;
  var slides = [];
  var dots = [];

  /* ---- Build the slides and the dots ------------------------------ */
  PHOTOS.forEach(function (photo, i) {
    var slide = document.createElement("div");
    slide.className = "gallery-slide";
    slide.dataset.on = i === 0 ? "1" : "0";

    var img = document.createElement("img");
    img.src = photo.src;
    img.alt = photo.title + (photo.note ? " — " + photo.note : "");
    /* Only the first photograph loads straight away; the rest wait. */
    img.loading = i === 0 ? "eager" : "lazy";
    slide.appendChild(img);

    if (photo.title || photo.note) {
      var caption = document.createElement("div");
      caption.className = "gallery-caption";
      if (photo.title) {
        var strong = document.createElement("strong");
        strong.textContent = photo.title;
        caption.appendChild(strong);
      }
      if (photo.note) {
        var span = document.createElement("span");
        span.textContent = photo.note;
        caption.appendChild(span);
      }
      slide.appendChild(caption);
    }

    stage.appendChild(slide);
    slides.push(slide);

    var dot = document.createElement("button");
    dot.type = "button";
    dot.dataset.on = i === 0 ? "1" : "0";
    dot.setAttribute("aria-label", "Photograph " + (i + 1) + " of " + PHOTOS.length);
    dot.addEventListener("click", function () { goTo(i); restart(); });
    dotsRow.appendChild(dot);
    dots.push(dot);

    /* The plain grid underneath, which works even without JavaScript
       running the slideshow. */
    if (grid) {
      var thumb = document.createElement("img");
      /* the small copy, from assets/gallery/thumbs/ */
      thumb.src = photo.src.replace("/gallery/", "/gallery/thumbs/");
      thumb.alt = photo.title;
      thumb.loading = "lazy";
      thumb.style.cursor = "pointer";
      thumb.addEventListener("click", function () {
        goTo(i);
        restart();
        gallery.scrollIntoView({ behavior: "smooth", block: "center" });
      });
      grid.appendChild(thumb);
    }
  });

  /* A single photograph needs no slideshow at all. */
  if (PHOTOS.length < 2) {
    dotsRow.hidden = true;
    gallery.querySelectorAll(".gallery-arrow").forEach(function (a) { a.hidden = true; });
    return;
  }

  /* ---- Moving between photographs --------------------------------- */
  function goTo(next) {
    /* Wrap around at both ends. */
    current = (next + PHOTOS.length) % PHOTOS.length;

    slides.forEach(function (s, i) { s.dataset.on = i === current ? "1" : "0"; });
    dots.forEach(function (d, i) { d.dataset.on = i === current ? "1" : "0"; });
  }

  function step() { goTo(current + 1); }

  function start() {
    stop();
    timer = setInterval(step, INTERVAL);
  }

  function stop() {
    if (timer) { clearInterval(timer); timer = null; }
  }

  /* After somebody clicks, give them a full interval before it moves on
     by itself again — otherwise it can jump a moment after they choose. */
  function restart() { start(); }

  gallery.querySelectorAll(".gallery-arrow").forEach(function (arrow) {
    arrow.addEventListener("click", function () {
      goTo(current + (arrow.dataset.dir === "next" ? 1 : -1));
      restart();
    });
  });

  /* Pause while the pointer is over the gallery, or while a keyboard
     user is inside it — nobody wants a photo to change mid-read. */
  gallery.addEventListener("mouseenter", stop);
  gallery.addEventListener("mouseleave", start);
  gallery.addEventListener("focusin", stop);
  gallery.addEventListener("focusout", start);

  /* Stop entirely when the tab is in the background. */
  document.addEventListener("visibilitychange", function () {
    if (document.hidden) stop(); else start();
  });

  /* Left and right arrow keys, when the gallery has focus. */
  gallery.addEventListener("keydown", function (e) {
    if (e.key === "ArrowLeft") { goTo(current - 1); restart(); }
    if (e.key === "ArrowRight") { goTo(current + 1); restart(); }
  });

  /* Somebody who has asked their device to reduce motion gets the
     photographs, but no automatic movement. */
  if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) return;

  start();
})();
