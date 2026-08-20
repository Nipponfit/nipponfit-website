/* =====================================================================
   NIPPON FIT — the enquiry form on the Contact page.

   HOW THIS WORKS
   --------------
   A website made of plain files has nowhere to store a form submission
   and no way to send an email by itself — that would need a server, a
   monthly bill and something else that can break.

   So this form does something simpler and, for a Bengaluru karate club,
   better: it writes the enquiry out as a tidy message and opens it in
   WhatsApp, already addressed to the club, so the parent just presses
   send. The enquiry lands in the same WhatsApp you already watch all
   day. Nothing to check, nothing to maintain, nothing to pay for.

   There is an email link underneath for anyone who prefers email. It
   works the same way — it opens their email app with everything filled
   in.

   TO CHANGE THE NUMBER OR ADDRESS the enquiries go to, edit the two
   lines marked below. Nothing else.
   ===================================================================== */

(function () {
  "use strict";

  var WHATSAPP_NUMBER = "919945616005";          // country code, no + and no spaces
  var EMAIL_ADDRESS = "contactus@nipponfit.com";

  var form = document.getElementById("contact-form");
  if (!form) return;

  var message = document.getElementById("contact-message");
  var emailLink = document.getElementById("contact-email-link");

  function show(kind, text) {
    message.className = "notice notice-" + kind;
    message.textContent = text;
    message.hidden = false;
  }

  function hideMessage() {
    message.hidden = true;
    message.textContent = "";
  }

  /* Read the form and check the two fields we actually need.
     Returns null and shows a red message if something is missing. */
  /* Fields are looked up by id, not as form.name — a form already has its
     own built-in "name" property, so form.name would give us the form
     rather than the box the visitor typed into. */
  function field(id) { return document.getElementById(id); }

  function collect() {
    var name = field("name").value.trim();
    var phone = field("phone").value.trim();
    var interest = field("interest").value;
    var area = field("area").value.trim();
    var note = field("note").value.trim();

    if (!name) {
      show("error", "Please tell us your name.");
      field("name").focus();
      return null;
    }

    if (phone.replace(/\D/g, "").length < 10) {
      show("error", "Please give us a 10-digit mobile number so we can call you back.");
      field("phone").focus();
      return null;
    }

    hideMessage();

    return { name: name, phone: phone, interest: interest, area: area, note: note };
  }

  /* Build the message text that gets sent, either way. */
  function compose(d) {
    var lines = [
      "Hello Nippon Karate Club,",
      "",
      "Name: " + d.name,
      "Mobile: " + d.phone,
      "Enquiry about: " + d.interest
    ];

    if (d.area) lines.push("Area: " + d.area);
    if (d.note) lines.push("", d.note);

    return lines.join("\n");
  }

  /* ---- The WhatsApp button ---------------------------------------- */
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var d = collect();
    if (!d) return;

    show("ok", "Opening WhatsApp — press send there and we will reply shortly.");

    window.open(
      "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(compose(d)),
      "_blank",
      "noopener"
    );
  });

  /* ---- The "send it as an email instead" link ---------------------- */
  emailLink.addEventListener("click", function (e) {
    e.preventDefault();

    var d = collect();
    if (!d) return;

    show("ok", "Opening your email app — press send there and we will reply shortly.");

    window.location.href =
      "mailto:" + EMAIL_ADDRESS +
      "?subject=" + encodeURIComponent("Enquiry: " + d.interest) +
      "&body=" + encodeURIComponent(compose(d));
  });

  /* Clear a red message as soon as they start fixing the problem. */
  form.addEventListener("input", function () {
    if (!message.hidden && message.classList.contains("notice-error")) hideMessage();
  });
})();
