/* =====================================================================
   NIPPON FIT — the Parent Login panel on the website.

   HOW THIS WORKS, in plain words
   ------------------------------
   The real app lives at app.nipponfit.com. This page does NOT ask for a
   password. It asks only for the mobile number, checks it looks like a
   real Indian mobile number, and then opens the app with that number
   already filled in. The parent types their password on the app itself.

   WHY IT IS BUILT THIS WAY, and not as a full login here
   ------------------------------------------------------
   A browser keeps a signed-in session separately for each web address.
   A password typed on nipponfit.com could not carry the parent across
   to app.nipponfit.com — they would simply be asked to sign in again,
   which is worse, not better. Handing the number over means one tap
   here, then password on the app: no repeated typing, and the password
   is only ever typed on the app that owns it.

   TO CHANGE THE APP ADDRESS, edit APP_URL just below. Nothing else.
   ===================================================================== */

(function () {
  "use strict";

  var APP_URL = "https://app.nipponfit.com/";

  var form = document.getElementById("parent-login-form");
  if (!form) return;

  var mobile = document.getElementById("mobile");
  var message = document.getElementById("login-message");
  var submit = document.getElementById("login-submit");

  /* Show a red message above the form. */
  function problem(text) {
    message.className = "notice notice-error";
    message.textContent = text;
    message.hidden = false;
    mobile.focus();
  }

  /* Show a green message above the form. */
  function progress(text) {
    message.className = "notice notice-ok";
    message.textContent = text;
    message.hidden = false;
  }

  function clearMessage() {
    message.hidden = true;
    message.textContent = "";
  }

  /* Turn whatever the parent typed into ten digits, or return "" if it
     cannot be done. Accepts 9945616005, +91 99456 16005, 099456-16005
     and anything else with the right ten digits inside it. */
  function tenDigits(typed) {
    var digits = String(typed).replace(/\D/g, "");

    if (digits.length > 10) digits = digits.slice(-10);      // drop 91 / 0 prefix
    if (digits.length !== 10) return "";
    if (!/^[6-9]/.test(digits)) return "";                    // Indian mobiles start 6-9

    return digits;
  }

  form.addEventListener("submit", function (e) {
    e.preventDefault();
    clearMessage();

    var typed = mobile.value.trim();

    if (!typed) {
      problem("Please type the mobile number you gave the dojo.");
      return;
    }

    var number = tenDigits(typed);

    if (!number) {
      problem("That does not look like a 10-digit Indian mobile number. Please check and try again.");
      return;
    }

    progress("Opening the app — type your password on the next screen.");
    submit.disabled = true;
    submit.textContent = "Opening the app…";

    /* Off to the app, with the number already in the box. */
    window.location.href = APP_URL + "?m=" + encodeURIComponent(number);
  });

  /* Clear any red message as soon as they start correcting the number. */
  mobile.addEventListener("input", clearMessage);
})();
