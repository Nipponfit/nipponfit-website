/* =====================================================================
   NIPPON FIT — shared behaviour for every page.

   There are only three small jobs here:
     1. Open and close the menu on phones.
     2. Highlight the page you are currently on in the menu.
     3. Put the current year in the footer so it never goes out of date.

   Nothing on this site depends on JavaScript to be readable. If this
   file fails to load, every page still shows all of its text — which is
   exactly what Google wants.
   ===================================================================== */

(function () {
  "use strict";

  /* ---- 1. The menu button on phones ------------------------------- */
  var toggle = document.querySelector(".nav-toggle");
  var links = document.querySelector(".nav-links");

  if (toggle && links) {
    toggle.addEventListener("click", function () {
      var open = links.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });

    /* Tapping any menu item closes the menu again. */
    links.addEventListener("click", function (e) {
      if (e.target.tagName === "A") {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      }
    });

    /* Escape closes it too, for keyboard users. */
    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && links.classList.contains("open")) {
        links.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
        toggle.focus();
      }
    });
  }

  /* ---- 2. Highlight the current page ------------------------------ */
  /* Marks the matching menu link. An article at /blog/kumite-analysis
     highlights "Blog", so a reader can always see where they are. */
  var here = location.pathname.replace(/\.html$/, "").replace(/\/+$/, "") || "/";

  document.querySelectorAll(".nav-links a").forEach(function (a) {
    var target = (a.getAttribute("href") || "").split("#")[0].replace(/\/+$/, "") || "/";

    var match = target === "/"
      ? here === "/"
      : here === target || here.indexOf(target + "/") === 0;

    if (match) a.setAttribute("aria-current", "page");
  });

  /* ---- 3. The year in the footer ---------------------------------- */
  document.querySelectorAll("[data-year]").forEach(function (node) {
    node.textContent = String(new Date().getFullYear());
  });
})();
