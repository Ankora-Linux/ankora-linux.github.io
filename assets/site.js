/* Ankora Linux web sitesi. Tema, vurgu rengi, mobil menu ve kopyalama. */
(function () {
  "use strict";

  var doc = document;
  var root = doc.documentElement;
  /* localStorage kapaliysa (file:// vb.) cerezle devam et. */
  function readCookie(key) {
    var m = doc.cookie && doc.cookie.match(new RegExp("(?:^|; )" + key + "=([^;]*)"));
    if (!m) return null;
    try { return decodeURIComponent(m[1]); } catch (e) { return m[1]; }
  }

  function writeCookie(key, value) {
    try {
      doc.cookie = key + "=" + value + "; path=/; max-age=31536000; samesite=lax";
    } catch (e) { /* yok sayilir */ }
  }

  var store = {
    get: function (key) {
      try {
        var v = localStorage.getItem(key);
        if (v !== null) return v;
      } catch (e) { /* yok sayilir */ }
      return readCookie(key);
    },
    set: function (key, value) {
      try { localStorage.setItem(key, value); } catch (e) { /* yok sayilir */ }
      writeCookie(key, value);
    }
  };

  /* ------------------------------------------------------------------ tema */
  var themeBtns = doc.querySelectorAll("[data-set-theme]");
  var accentBtns = doc.querySelectorAll("[data-set-accent]");
  var themeBtn = doc.querySelector("[data-theme-btn]");
  var themePanel = doc.getElementById("theme-panel");
  var mq = window.matchMedia("(prefers-color-scheme: dark)");

  function effective(pref) {
    if (pref === "auto") return mq.matches ? "dark" : "light";
    return pref;
  }

  function setTheme(pref) {
    root.dataset.theme = effective(pref);
    root.dataset.themePref = pref;
    themeBtns.forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.setTheme === pref ? "true" : "false");
    });
    if (themeBtn) {
      var use = themeBtn.querySelector("use");
      if (use) {
        var base = use.getAttribute("href").split("#")[0];
        use.setAttribute("href", base + "#" + (root.dataset.theme === "dark" ? "i-sun" : "i-moon"));
      }
    }
  }

  function setAccent(name) {
    root.dataset.accent = name;
    accentBtns.forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.setAccent === name ? "true" : "false");
    });
  }

  var themePref = store.get("ankora-theme") || "auto";
  if (["light", "dark", "auto"].indexOf(themePref) < 0) themePref = "auto";
  var accentPref = store.get("ankora-accent") || "blue";
  if (["blue", "green", "purple"].indexOf(accentPref) < 0) accentPref = "blue";
  setTheme(themePref);
  setAccent(accentPref);

  themeBtns.forEach(function (b) {
    b.addEventListener("click", function () {
      var pref = b.dataset.setTheme;
      store.set("ankora-theme", pref);
      setTheme(pref);
    });
  });

  accentBtns.forEach(function (b) {
    b.addEventListener("click", function () {
      var name = b.dataset.setAccent;
      store.set("ankora-accent", name);
      setAccent(name);
    });
  });

  if (mq.addEventListener) {
    mq.addEventListener("change", function () {
      if ((root.dataset.themePref || "auto") === "auto") setTheme("auto");
    });
  }

  /* ----------------------------------------------------------- tema paneli */
  function setPanel(open) {
    if (!themeBtn || !themePanel) return;
    themeBtn.setAttribute("aria-expanded", open ? "true" : "false");
    themePanel.hidden = !open;
  }

  if (themeBtn && themePanel) {
    themeBtn.addEventListener("click", function (event) {
      event.stopPropagation();
      setPanel(themePanel.hidden);
    });
    themePanel.addEventListener("click", function (event) { event.stopPropagation(); });
    doc.addEventListener("click", function () { setPanel(false); });
    doc.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setPanel(false);
    });
  }

  /* ------------------------------------------------------------ mobil menu */
  var menuBtn = doc.querySelector("[data-menu-btn]");
  var sheet = doc.getElementById("menu-sheet");

  function setMenu(open) {
    if (!menuBtn || !sheet) return;
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    sheet.dataset.open = open ? "true" : "false";
    var use = menuBtn.querySelector("use");
    if (use) {
      var base = use.getAttribute("href").split("#")[0];
      use.setAttribute("href", base + "#" + (open ? "i-close" : "i-menu"));
    }
  }

  if (menuBtn && sheet) {
    menuBtn.addEventListener("click", function () {
      setMenu(sheet.dataset.open !== "true");
    });
    sheet.addEventListener("click", function (event) {
      if (event.target.closest("a")) setMenu(false);
    });
    doc.addEventListener("keydown", function (event) {
      if (event.key === "Escape") setMenu(false);
    });
  }

  /* --------------------------------------------------------- kopyala dugmesi */
  doc.querySelectorAll("[data-copy]").forEach(function (btn) {
    btn.addEventListener("click", function () {
      var box = btn.closest(".code");
      var codeEl = box ? box.querySelector("code") : null;
      if (!codeEl) return;
      var text = codeEl.innerText;
      var done = function () {
        var old = btn.textContent;
        btn.textContent = btn.dataset.done || old;
        setTimeout(function () { btn.textContent = old; }, 1600);
      };
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(text).then(done, done);
      } else {
        var field = doc.createElement("textarea");
        field.value = text;
        doc.body.appendChild(field);
        field.select();
        try { doc.execCommand("copy"); } catch (error) { /* yok sayilir */ }
        doc.body.removeChild(field);
        done();
      }
    });
  });
})();
