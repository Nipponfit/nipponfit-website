/* =====================================================================
   NIPPON FIT — the Nippon Karate Club registration form.

   HOW IT WORKS
   ------------
   It checks the few fields we really need, writes the registration out
   as a tidy message, and opens it in WhatsApp so the person just presses
   send. There is an email option underneath. Nothing is stored on the
   website and there is no server to maintain — registrations land in the
   WhatsApp you already watch.

   WHY THERE IS NO AADHAAR FIELD OR PHOTO UPLOAD
   ---------------------------------------------
   The old form asked for an Aadhaar number and copies of documents.
   Those must not travel through a plain web page: there is nowhere safe
   on a website like this to receive or keep them, and sending an Aadhaar
   number through WhatsApp or email is worse, not better. The form on the
   page therefore asks people to bring the photograph and Aadhaar copy to
   the dojo on the first visit, where you take them in person.

   TO CHANGE WHERE REGISTRATIONS GO, edit the two lines just below.
   ===================================================================== */

(function () {
  "use strict";

  var WHATSAPP_NUMBER = "919945616005";          // country code, no + and no spaces
  var EMAIL_ADDRESS = "contactus@nipponfit.com";

  var MINIMUM_AGE = 4;                            // we take children from four

  var form = document.getElementById("registration-form");
  if (!form) return;

  var message = document.getElementById("registration-message");
  var emailLink = document.getElementById("registration-email-link");

  /* Fields are looked up by id rather than as form.something, because a
     form has its own built-in properties that would get in the way. */
  function field(id) { return document.getElementById(id); }
  function value(id) { var f = field(id); return f ? f.value.trim() : ""; }

  function show(kind, text) {
    message.className = "notice notice-" + kind;
    message.textContent = text;
    message.hidden = false;
    message.scrollIntoView({ block: "nearest" });
  }

  function hideMessage() {
    message.hidden = true;
    message.textContent = "";
  }

  function problem(text, focusId) {
    show("error", text);
    var f = field(focusId);
    if (f) f.focus();
    return null;
  }

  /* Work out someone's age from a date of birth, in whole years. */
  function ageFrom(dateText) {
    var born = new Date(dateText);
    if (isNaN(born.getTime())) return null;

    var today = new Date();
    var years = today.getFullYear() - born.getFullYear();

    /* Take a year off if their birthday has not come round yet. */
    var monthGap = today.getMonth() - born.getMonth();
    if (monthGap < 0 || (monthGap === 0 && today.getDate() < born.getDate())) years--;

    return years;
  }

  /* Read the form and check what we genuinely need. */
  function collect() {
    var student = value("student");
    var dob = value("dob");
    var mobile = value("mobile");

    if (!student) return problem("Please give us the student's full name.", "student");

    if (!dob) return problem("Please give us the student's date of birth.", "dob");

    var years = ageFrom(dob);

    if (years === null || years < 0 || years > 120) {
      return problem("That date of birth does not look right. Please check it.", "dob");
    }

    if (years < MINIMUM_AGE) {
      return problem(
        "We take children from " + MINIMUM_AGE + " years old. If your child is nearly " +
        MINIMUM_AGE + ", call us on 99456 16005 and we will talk it through.",
        "dob"
      );
    }

    if (mobile.replace(/\D/g, "").length < 10) {
      return problem("Please give us a 10-digit contact number so we can confirm your class.", "mobile");
    }

    hideMessage();

    return {
      student: student,
      dob: dob,
      age: years,
      gender: value("gender"),
      mobile: mobile,
      parent: value("parent"),
      email: value("email"),
      address: value("address"),
      bloodgroup: value("bloodgroup"),
      dojo: value("dojo"),
      programme: value("programme"),
      notes: value("notes")
    };
  }

  /* Build the message that gets sent, whichever button was used. */
  function compose(d) {
    var lines = [
      "Hello Nippon Karate Club,",
      "",
      "I would like to register for a free demo class.",
      "",
      "Full name: " + d.student,
      "Date of birth: " + d.dob + " (age " + d.age + ")"
    ];

    if (d.gender) lines.push("Gender: " + d.gender);

    lines.push("Contact number: " + d.mobile);

    if (d.parent) lines.push("Parent/guardian: " + d.parent);
    if (d.email) lines.push("Email: " + d.email);
    if (d.address) lines.push("Address: " + d.address);
    if (d.bloodgroup) lines.push("Blood group: " + d.bloodgroup);

    lines.push("Preferred dojo: " + d.dojo);
    lines.push("Programme: " + d.programme);

    if (d.notes) lines.push("Medical conditions: " + d.notes);

    return lines.join("\n");
  }

  /* ---- The WhatsApp button ---------------------------------------- */
  form.addEventListener("submit", function (e) {
    e.preventDefault();

    var d = collect();
    if (!d) return;

    show("ok", "Opening WhatsApp — press send there and we will confirm your class shortly.");

    window.open(
      "https://wa.me/" + WHATSAPP_NUMBER + "?text=" + encodeURIComponent(compose(d)),
      "_blank",
      "noopener"
    );
  });

  /* ---- The "send it as an email instead" link ---------------------- */
  if (emailLink) {
    emailLink.addEventListener("click", function (e) {
      e.preventDefault();

      var d = collect();
      if (!d) return;

      show("ok", "Opening your email app — press send there and we will confirm your class shortly.");

      window.location.href =
        "mailto:" + EMAIL_ADDRESS +
        "?subject=" + encodeURIComponent("Registration: " + d.student) +
        "&body=" + encodeURIComponent(compose(d));
    });
  }

  /* Clear a red message as soon as they start fixing the problem. */
  form.addEventListener("input", function () {
    if (!message.hidden && message.classList.contains("notice-error")) hideMessage();
  });
})();
