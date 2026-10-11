// Ankora prototip — küçük etkileşimler
(function () {
  // Kaydırınca yumuşak açılma (kartlara otomatik uygulanır)
  var els = document.querySelectorAll('.card, .plan, .quote, .tcard, .appcard, .stats, .showcase, .cta');
  els.forEach(function (el) { el.classList.add('reveal'); });
  if ('IntersectionObserver' in window && els.length) {
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (e) {
        if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); }
      });
    }, { threshold: 0.12 });
    els.forEach(function (el) { io.observe(el); });
  } else {
    els.forEach(function (el) { el.classList.add('in'); });
  }

  // Mobil menü
  var btn = document.querySelector('.navtoggle');
  var links = document.querySelector('.navlinks');
  if (btn && links) {
    btn.addEventListener('click', function () {
      var open = links.classList.toggle('open');
      btn.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Ekran görüntüleri: uzantıdan bağımsız yükleyici + yumuşak görünme
  // (ayazdeokul.png gibi adı .png, içeriği JPEG olan dosyaları da bulur)
  (function () {
    var exts = ['.png', '.jpg', '.jpeg', '.webp'];
    document.querySelectorAll('img[data-shot]').forEach(function (img) {
      var base = img.getAttribute('data-shot'), i = 0;
      img.style.opacity = '0';
      img.style.transition = 'opacity .5s ease';
      (function next() {
        if (i >= exts.length) { img.remove(); return; }
        var url = base + exts[i++] + '?v=3';
        var t = new Image();
        t.onload = function () { img.src = url; img.style.opacity = '1'; };
        t.onerror = next;
        t.src = url;
      })();
    });
  })();

  // Kaydırınca üst menüye gölge
  var nav = document.querySelector('header.site');
  function sh() {
    if (!nav) return;
    if (window.scrollY > 8) nav.classList.add('scrolled');
    else nav.classList.remove('scrolled');
  }
  window.addEventListener('scroll', sh, { passive: true });
  sh();

  // Tema: karanlık / aydınlık (tercih saklanır, sistem varsayılanı)
  var MOON = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 12.8A9 9 0 1 1 11.2 3a7 7 0 0 0 9.8 9.8z"/></svg>';
  var SUN = '<svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="4"/><path d="M12 2v2M12 20v2M4.9 4.9l1.4 1.4M17.7 17.7l1.4 1.4M2 12h2M20 12h2M4.9 19.1l1.4-1.4M17.7 6.3l1.4-1.4"/></svg>';
  function paintTheme() {
    var dark = document.documentElement.getAttribute('data-theme') === 'dark';
    var b = document.getElementById('themeToggle');
    if (b) {
      b.innerHTML = dark ? SUN : MOON;
      var tr = document.documentElement.getAttribute('lang') === 'tr';
      b.title = tr ? 'Karanlık / aydınlık tema' : 'Dark / light theme';
      b.setAttribute('aria-label', b.title);
    }
  }
  (function initTheme() {
    var t = 'light';
    try {
      t = localStorage.getItem('ankora-theme') ||
        (window.matchMedia('(prefers-color-scheme: dark)').matches ? 'dark' : 'light');
    } catch (e) {}
    document.documentElement.setAttribute('data-theme', t === 'dark' ? 'dark' : 'light');
    paintTheme();
    var b = document.getElementById('themeToggle');
    if (b) b.addEventListener('click', function () {
      var next = document.documentElement.getAttribute('data-theme') === 'dark' ? 'light' : 'dark';
      document.documentElement.setAttribute('data-theme', next);
      try { localStorage.setItem('ankora-theme', next); } catch (e) {}
      paintTheme();
    });
  })();
  window.AnkoraPaintTheme = paintTheme;

  // Yukarı dön
  var toTop = document.getElementById('toTop');
  window.addEventListener('scroll', function () {
    if (toTop) toTop.classList.toggle('show', window.scrollY > 600);
  }, { passive: true });
  if (toTop) toTop.addEventListener('click', function () {
    window.scrollTo({ top: 0, behavior: 'smooth' });
  });

  // Yıl
  document.querySelectorAll('[data-year]').forEach(function (el) {
    el.textContent = new Date().getFullYear();
  });
})();
