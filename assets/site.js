/* Ankora Linux 5.0 web sitesi: dort yuz temasi, mobil menu, ekran vitrini, AI ve magaza araclari. */
(function () {
  "use strict";

  var doc = document;
  var root = doc.documentElement;
  var VALID_THEMES = ["bostan", "bakir", "civata", "arduvaz", "auto"];

  function readCookie(key) {
    var m = doc.cookie && doc.cookie.match(new RegExp("(?:^|; )" + key + "=([^;]*)"));
    if (!m) return null;
    try { return decodeURIComponent(m[1]); } catch (e) { return m[1]; }
  }

  function writeCookie(key, value) {
    try {
      doc.cookie = key + "=" + value + "; path=/; max-age=31536000; samesite=lax";
    } catch (e) {}
  }

  var store = {
    get: function (key) {
      try {
        var v = localStorage.getItem(key);
        if (v !== null) return v;
      } catch (e) {}
      return readCookie(key);
    },
    set: function (key, value) {
      try { localStorage.setItem(key, value); } catch (e) {}
      writeCookie(key, value);
    }
  };

  /* ------------------------------------------------------------------ 4 Yuz Temasi */
  var themeBtns = doc.querySelectorAll("[data-set-theme]");
  var themeBtn = doc.querySelector("[data-theme-btn]");
  var themePanel = doc.getElementById("theme-panel");
  var mq = window.matchMedia("(prefers-color-scheme: dark)");

  function mapLegacy(val) {
    if (val === "light") return "bostan";
    if (val === "dark") return "bakir";
    return VALID_THEMES.indexOf(val) >= 0 ? val : "bostan";
  }

  function effective(pref) {
    if (pref === "auto") return mq.matches ? "bakir" : "bostan";
    return pref;
  }

  function setTheme(pref) {
    pref = mapLegacy(pref);
    var active = effective(pref);
    root.dataset.theme = active;
    root.dataset.themePref = pref;
    themeBtns.forEach(function (b) {
      b.setAttribute("aria-pressed", b.dataset.setTheme === pref ? "true" : "false");
    });
    if (themeBtn) {
      var lbl = themeBtn.querySelector("[data-theme-label]");
      if (lbl) lbl.textContent = active.charAt(0).toUpperCase() + active.slice(1);
    }
  }

  var savedPref = mapLegacy(store.get("ankora-theme") || "bostan");
  setTheme(savedPref);

  themeBtns.forEach(function (b) {
    b.addEventListener("click", function () {
      var pref = b.dataset.setTheme;
      store.set("ankora-theme", pref);
      setTheme(pref);
    });
  });

  if (mq.addEventListener) {
    mq.addEventListener("change", function () {
      if ((root.dataset.themePref || "bostan") === "auto") setTheme("auto");
    });
  }

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

  /* ------------------------------------------------------------------ Mobil Menu */
  var menuBtn = doc.querySelector("[data-menu-btn]");
  var sheet = doc.getElementById("menu-sheet");

  function setMenu(open) {
    if (!menuBtn || !sheet) return;
    menuBtn.setAttribute("aria-expanded", open ? "true" : "false");
    sheet.classList.toggle("open", open);
  }

  if (menuBtn && sheet) {
    menuBtn.addEventListener("click", function () {
      setMenu(!sheet.classList.contains("open"));
    });
    sheet.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () { setMenu(false); });
    });
  }

  /* ------------------------------------------------------------------ 4 Yuz Ekran Vitrini */
  var shotTabs = Array.prototype.slice.call(doc.querySelectorAll("[data-shot-tab]"));
  var shotPanels = Array.prototype.slice.call(doc.querySelectorAll("[data-shot-panel]"));

  function selectShot(num, syncTheme) {
    shotTabs.forEach(function (tab) {
      var isSel = tab.getAttribute("data-shot-tab") === num;
      tab.setAttribute("aria-selected", isSel ? "true" : "false");
      tab.setAttribute("tabindex", isSel ? "0" : "-1");
      if (isSel && syncTheme) {
        var themeAttr = tab.getAttribute("data-face-theme");
        if (themeAttr) {
          store.set("ankora-theme", themeAttr);
          setTheme(themeAttr);
        }
      }
    });
    shotPanels.forEach(function (panel) {
      var match = panel.getAttribute("data-shot-panel") === num;
      panel.hidden = !match;
    });
  }

  if (shotTabs.length) {
    shotTabs.forEach(function (tab, idx) {
      tab.addEventListener("click", function () {
        selectShot(tab.getAttribute("data-shot-tab"), true);
      });
      tab.addEventListener("keydown", function (e) {
        var next = null;
        if (e.key === "ArrowRight") next = shotTabs[(idx + 1) % shotTabs.length];
        else if (e.key === "ArrowLeft") next = shotTabs[(idx - 1 + shotTabs.length) % shotTabs.length];
        if (next) {
          e.preventDefault();
          next.focus();
          selectShot(next.getAttribute("data-shot-tab"), true);
        }
      });
    });
  }

  /* ------------------------------------------------------------------ Komut Kopyalama */
  doc.querySelectorAll("[data-copy]").forEach(function (btn) {
    var orig = btn.textContent;
    btn.addEventListener("click", function () {
      var wrap = btn.closest(".code");
      var pre = wrap && wrap.querySelector("pre");
      var txt = pre ? pre.textContent : "";
      if (navigator.clipboard && txt) {
        navigator.clipboard.writeText(txt).then(function () {
          btn.textContent = btn.getAttribute("data-done") || "OK";
          setTimeout(function () { btn.textContent = orig; }, 1600);
        });
      }
    });
  });

  /* ------------------------------------------------------------------ Kurulum Sekmeleri */
  var dlTabs = doc.querySelectorAll("[data-dl-tab]");
  var dlPre = doc.getElementById("dl-cmd");
  var dlNote = doc.getElementById("dl-note");
  if (dlTabs.length && dlPre) {
    dlTabs.forEach(function (tab) {
      tab.addEventListener("click", function () {
        dlTabs.forEach(function (t) {
          t.setAttribute("aria-pressed", t === tab ? "true" : "false");
        });
        dlPre.textContent = tab.getAttribute("data-cmd") || "";
        if (dlNote) dlNote.textContent = tab.getAttribute("data-note") || "";
      });
    });
  }

  /* ------------------------------------------------------------------ Ankora AI Laboratuvari */
  var aiModes = doc.querySelectorAll("[data-ai-mode]");
  var aiTitle = doc.getElementById("ai-mode-title");
  var aiDesc = doc.getElementById("ai-mode-desc");
  var aiCode = doc.getElementById("ai-mode-code");
  if (aiModes.length && aiTitle && aiDesc && aiCode) {
    aiModes.forEach(function (btn) {
      btn.addEventListener("click", function () {
        aiModes.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
        aiTitle.textContent = btn.getAttribute("data-title") || "";
        aiDesc.textContent = btn.getAttribute("data-desc") || "";
        aiCode.textContent = btn.getAttribute("data-code") || "";
      });
    });
  }

  var labForm = doc.getElementById("lab-form");
  var labInput = doc.getElementById("lab-cmd");
  var labOut = doc.getElementById("lab-output");
  if (labForm && labInput && labOut) {
    var ALLOWED = [
      "apt-get clean && rm -rf /tmp/*", "apt-get clean", "rm -rf /tmp/*",
      "df -h / && free -m", "df -h /", "df -h", "free -m", "free -h",
      "swapon --show", "ip -br addr", "uptime", "uname -a", "uname -r",
      "whoami", "ls", "ls -la", "ls -l", "ls -lh", "date", "hostname", "id",
      "lscpu", "lsblk", "ps aux", "top -b -n 1", "/usr/local/bin/ankora-doctor",
      "sync", "cat /etc/os-release"
    ];
    var msgOk = labOut.getAttribute("data-msg-ok") || "ALLOWED";
    var msgDeny = labOut.getAttribute("data-msg-deny") || "DENIED";

    function checkCmd(val) {
      var cmd = (val || "").trim();
      if (cmd && ALLOWED.indexOf(cmd) !== -1) {
        labOut.setAttribute("data-state", "allow");
        labOut.textContent = msgOk.replace("{cmd}", cmd);
      } else {
        labOut.setAttribute("data-state", "deny");
        labOut.textContent = msgDeny.replace("{cmd}", cmd || "-");
      }
    }

    labForm.addEventListener("submit", function (e) {
      e.preventDefault();
      checkCmd(labInput.value);
    });

    doc.querySelectorAll("[data-cmd-preset]").forEach(function (btn) {
      btn.addEventListener("click", function () {
        doc.querySelectorAll("[data-cmd-preset]").forEach(function (b) {
          b.setAttribute("aria-pressed", b === btn ? "true" : "false");
        });
        var cmd = btn.getAttribute("data-cmd-preset") || "";
        labInput.value = cmd;
        checkCmd(cmd);
      });
    });
  }

  /* ------------------------------------------------------------------ Magaza Filtresi */
  var pkgSearch = doc.getElementById("pkg-search");
  var pkgRows = Array.prototype.slice.call(doc.querySelectorAll("[data-pkg-row]"));
  var pkgEmpty = doc.getElementById("pkg-empty");
  var srcBtns = doc.querySelectorAll("[data-pkg-source]");
  if (pkgSearch && pkgRows.length) {
    var activeSrc = "all";
    function filterPkgs() {
      var q = (pkgSearch.value || "").trim().toLowerCase();
      var shown = 0;
      pkgRows.forEach(function (row) {
        var src = row.getAttribute("data-pkg-source-val") || "";
        var txt = (row.textContent || "").toLowerCase();
        var ok = (activeSrc === "all" || src === activeSrc) && (!q || txt.indexOf(q) !== -1);
        row.hidden = !ok;
        if (ok) shown++;
      });
      if (pkgEmpty) pkgEmpty.hidden = shown > 0;
    }
    pkgSearch.addEventListener("input", filterPkgs);
    srcBtns.forEach(function (btn) {
      btn.addEventListener("click", function () {
        activeSrc = btn.getAttribute("data-pkg-source") || "all";
        srcBtns.forEach(function (b) { b.setAttribute("aria-pressed", b === btn ? "true" : "false"); });
        filterPkgs();
      });
    });
  }
})();
