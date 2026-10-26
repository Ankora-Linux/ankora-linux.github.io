#!/usr/bin/env python3
"""Ankora Linux web sitesi denetimi.

Kapsam: baglanti, erisilebilirlik, SEO, tasarim kurallari, cok dilli icerik
ve antislop sert kapilari (R-02 em dash, R-16 buzzword, R-15 jenerik CTA,
R-24 menu, R-25 kontrast, R-17 kaynaksiz sayi).

Site bes dillidir (tr, en, de, es, ru), iki teması (acik, koyu) ve uc
vurgu rengi (mavi, yesil, mor) vardir. Kontrast her tema/vurgu bileşimi icin
CSS'teki gercek degerlerden olculur.

Calistirma:  python3 check-site.py
Cikis kodu 0: temiz.  1: en az bir sorun.
"""

import json
import pathlib
import re
import sys
import xml.etree.ElementTree as ET

ROOT = pathlib.Path(__file__).parent
BASE = "https://ankora-linux.github.io/"

LANGS = ["tr", "en", "de", "es", "ru"]

FILES = {
    "tr": {"home": "index.html", "features": "ozellikler.html",
           "install": "kurulum.html", "security": "guvenlik.html",
           "changelog": "surum-gecmisi.html", "faq": "sss.html",
           "contact": "iletisim.html"},
    "en": {"home": "index.html", "features": "features.html",
           "install": "install.html", "security": "security.html",
           "changelog": "changelog.html", "faq": "faq.html",
           "contact": "contact.html"},
    "de": {"home": "index.html", "features": "funktionen.html",
           "install": "installieren.html", "security": "sicherheit.html",
           "changelog": "versionen.html", "faq": "faq.html",
           "contact": "kontakt.html"},
    "es": {"home": "index.html", "features": "funciones.html",
           "install": "instalar.html", "security": "seguridad.html",
           "changelog": "versiones.html", "faq": "faq.html",
           "contact": "contacto.html"},
    "ru": {"home": "index.html", "features": "vozmozhnosti.html",
           "install": "ustanovka.html", "security": "bezopasnost.html",
           "changelog": "versii.html", "faq": "faq.html",
           "contact": "kontakty.html"},
}

KEYS = ["home", "features", "install", "security", "changelog", "faq", "contact"]

# Tek satir menude gosterilen sayfalar. Bu sayfalarda aria-current isaretlenir.
NAV_KEYS = ["home", "features", "security", "changelog", "contact"]


def page_path(lang, key):
    name = FILES[lang][key]
    return name if lang == "tr" else lang + "/" + name


ALL_PAGES = [page_path(lang, key) for lang in LANGS for key in KEYS] + ["404.html"]

EXTERNAL = re.compile(r"^(https?:|mailto:|tel:|data:)")
HREF = re.compile(r'(?:href|src)\s*=\s*"([^"]+)"')
ICON_USE = re.compile(r'href="([^"]*icons\.svg)#([^"]+)"')
JSONLD = re.compile(r'<script type="application/ld\+json">\s*(.*?)\s*</script>', re.S)
HEADINGS = re.compile(r"<h([1-6])\b", re.I)
IMG = re.compile(r"<img\b[^>]*>", re.I)
ALT = re.compile(r'\balt\s*=\s*"([^"]*)"', re.I)

problems = []
notes = []


def fail(where, msg):
    problems.append((str(where), msg))


def note(where, msg):
    notes.append((str(where), msg))


# ------------------------------------------------------------------ varliklar

icons = (ROOT / "assets/img/icons.svg").read_text("utf-8")
icon_ids = set(re.findall(r'<symbol id="([^"]+)"', icons))
css = (ROOT / "assets/site.css").read_text("utf-8")
js = (ROOT / "assets/site.js").read_text("utf-8")

tree = ET.parse(ROOT / "sitemap.xml")
NS = {"s": "http://www.sitemaps.org/schemas/sitemap/0.9"}
sitemap_locs = {u.find("s:loc", NS).text for u in tree.getroot()}

robots = (ROOT / "robots.txt").read_text("utf-8")
if BASE + "sitemap.xml" not in robots:
    fail("robots.txt", "sitemap adresi tutarsiz")

# ------------------------------------------------------------------- sayfalar

for page in ALL_PAGES:
    p = ROOT / page
    src = p.read_text("utf-8")
    is404 = p.name == "404.html"
    key = next((k for k in KEYS if page in (page_path(L, k) for L in LANGS)), None)
    lang = page.split("/")[0] if "/" in page else "tr"

    def check_link(raw, where):
        if EXTERNAL.match(raw) or raw.startswith("#") or raw.startswith("//"):
            return
        path = raw.split("#")[0].split("?")[0]
        if not path:
            return
        if path.startswith("/"):
            dest = ROOT / path.lstrip("/")
        else:
            dest = (p.parent / path)
        if not dest.exists():
            fail(where, f"krik baglanti: {raw}")

    for raw in HREF.findall(src):
        check_link(raw, page)

    anchors = set(re.findall(r'\sid="([^"]+)"', src))
    for raw in HREF.findall(src):
        if raw.startswith("#") and raw != "#" and raw[1:] not in anchors:
            fail(page, f"bulunmayan anca: {raw}")

    for path, sym in ICON_USE.findall(src):
        if sym not in icon_ids:
            fail(page, f"tanimsiz ikon: #{sym}")
        check_link(path, page)

    for block_ in JSONLD.findall(src):
        try:
            json.loads(block_)
        except json.JSONDecodeError as exc:
            fail(page, f"gecersiz JSON-LD: {exc}")

    # --- R-02 em dash (sert kapi)
    if "\u2014" in src:
        for i, line in enumerate(src.split("\n"), 1):
            if "\u2014" in line:
                fail(page, f"R-02 em dash, satir {i}: {line.strip()[:80]}")

    # --- dil ve temel SEO
    for pat, label in (
        (r'<html lang="(tr|en|de|fr|es|ru)"', "lang"),
        (r"<title>.+?</title>", "title"),
        (r'<meta name="description" content="[^"]{60,}"', "description (60+ karakter)"),
        (r'<link rel="canonical" href="https://ankora-linux\.github\.io/', "canonical"),
        (r'hreflang="tr"', "hreflang tr"),
        (r'hreflang="en"', "hreflang en"),
        (r'hreflang="de"', "hreflang de"),
        (r'hreflang="es"', "hreflang es"),
        (r'hreflang="ru"', "hreflang ru"),
        (r'<meta property="og:title"', "og:title"),
        (r'<meta property="og:image"', "og:image"),
        (r'<meta property="og:locale"', "og:locale"),
        (r"prefers-color-scheme: light", "theme-color acik"),
        (r"prefers-color-scheme: dark", "theme-color koyu"),
        (r'class="skip"', "atlama baglantisi"),
        (r"<(nav|main|footer|header)\b", "landmark"),
        (r'<html lang="(?:tr|en|de|fr|es|ru)" class="no-js"', "no-js sinifi"),
    ):
        if not re.search(pat, src, re.S):
            fail(page, f"eksik: {label}")

    if not is404:
        if 'name="robots" content="index' not in src:
            fail(page, "404 disindaki sayfalar indexlenmeli")
        if 'hreflang="x-default"' not in src:
            fail(page, "hreflang x-default yok")
    else:
        if 'name="robots" content="noindex' not in src:
            fail(page, "404 sayfasi noindex olmali")
        if '<base href="/">' not in src:
            fail(page, "404 sayfasi base href icermeli")

    # --- baslik sirasi
    if len(re.findall(r"<h1\b", src, re.I)) != 1:
        fail(page, "tam olarak bir h1 olmali")
    levels = [int(h) for h in HEADINGS.findall(src)]
    for a, b in zip(levels, levels[1:]):
        if b > a + 1:
            fail(page, f"baslik sirasi atladi: h{a} -> h{b}")

    # --- goreller
    for img in IMG.findall(src):
        if not ALT.search(img):
            fail(page, f"alt metni yok: {img[:60]}")
        if 'width="' not in img or 'height="' not in img:
            fail(page, f"genislik/yukseklik yok (CLS): {img[:60]}")

    # --- erisilebilirlik / gezinme
    if 'id="main"' not in src:
        fail(page, "#main hedefi yok")
    if 'class="site-head"' not in src:
        fail(page, "ust cubuk (.site-head) yok")
    if not re.search(r'<nav class="nav".*?</nav>', src, re.S):
        fail(page, "ana gezinme (.nav) yok")
    if 'data-menu-btn' not in src:
        fail(page, "mobil menu dugnesi yok")
    if 'id="menu-sheet"' not in src:
        fail(page, "mobil menu paneli yok")
    if 'data-theme-btn' not in src:
        fail(page, "ayar/tema dugmesi yok")
    if 'id="theme-panel"' not in src:
        fail(page, "ayar paneli yok")
    if 'class="langmenu"' not in src:
        fail(page, "gorunur dil menusu (.langmenu) yok")
    for ctrl in ('data-set-theme', 'data-set-accent'):
        if ctrl not in src:
            fail(page, f"ayar denetimi yok: {ctrl}")
    if src.count('aria-current="page"') != (1 if (key in NAV_KEYS) else 0):
        fail(page, "aktif sayfa menude tam bir kez isaretlenmeli")
    if src.count('aria-current="true"') != 1:
        fail(page, "dil seciminde aria-current bir kez olmali")

    # --- sitemap kapsami
    canonical = re.search(r'<link rel="canonical" href="([^"]+)"', src)
    if canonical:
        loc = canonical.group(1)
        if is404:
            if loc not in sitemap_locs:
                note(page, "canonical sitemap'te degil (noindex, sorun degil)")
        elif loc not in sitemap_locs:
            fail(page, f"canonical sitemap'te yok: {loc}")

    # --- R-15 jenerik CTA / R-16 buzzword
    low = src.lower()
    for banned in ("get started", "learn more", "try now", "seamless",
                   "revolutionary", "cutting edge", "next generation",
                   "effortless", "powerful", "unlock the", "dive in"):
        if banned in low:
            fail(page, f"R-15/R-16 yasak ifade: {banned}")

    # --- emoji
    for m in re.finditer("[\U0001F300-\U0001FAFF\U00002600-\U000027BF]", src):
        fail(page, f"emoji: {m.group()!r}")

    # --- kirilmis karakter (homoglif tuzagi); ru sayfalari ve gorunur dil
    # menusu (Rusca ad) Kiril kullanir, bu yuzden ikisi taranmaz.
    if lang != "ru":
        scan = re.sub(r'<details class="langmenu".*?</details>', "", src, flags=re.S)
        cyr = set("абвгдежзийклмнопрстуфхцчшщъыьэюя")
        for ch in set(scan):
            if ch in cyr:
                fail(page, f"kirilmis karakter: {ch!r}")

# --------------------------------------------------------- tasarim kurallari

for b in re.findall(r"blur\((\d+(?:\.\d+)?)px\)", css):
    if float(b) > 14:
        fail("assets/site.css", f"blur {b}px, sinir 14px")
for sat in re.findall(r"saturate\((\d+(?:\.\d+)?)\)", css):
    if float(sat) > 1.5:
        fail("assets/site.css", f"saturate {sat}, sinir 1.5")

if "linear-gradient(" in css:
    fail("assets/site.css", "bu sitede gradyan kullanilmaz")
if "backdrop-filter" in css:
    fail("assets/site.css", "bu sitede cam kullanilmaz")
if "prefers-reduced-motion" not in css:
    fail("assets/site.css", "prefers-reduced-motion desteği yok")
if css.count("@media") < 3:
    fail("assets/site.css", "yetersiz duyarli kirilim")
for need in ('(max-width: 1080px)', '(max-width: 860px)', '(max-width: 560px)'):
    if need not in css:
        fail("assets/site.css", f"kirilim eksik: {need}")
for need in (':root[data-theme="dark"]', ':root[data-accent="green"]',
             ':root[data-accent="purple"]'):
    if need not in css:
        fail("assets/site.css", f"tema/vurgu secici eksik: {need}")

for fn in ("data-menu-btn", "data-copy", "data-theme-btn",
           "data-set-theme", "data-set-accent"):
    if fn not in js:
        fail("assets/site.js", f"beklenen davranis eksik: {fn}")
for gone in ("ankora_theme", "IntersectionObserver"):
    if gone in js:
        fail("assets/site.js", f"kaldirilmasi gereken davranis duruyor: {gone}")

# ------------------------------------------------------------------ kontrast

def _lin(c):
    c /= 255
    return c / 12.92 if c <= 0.03928 else ((c + 0.055) / 1.055) ** 2.4


def _lum(h):
    h = h.lstrip("#")
    r, g, b = (int(h[i:i + 2], 16) for i in (0, 2, 4))
    return 0.2126 * _lin(r) + 0.7152 * _lin(g) + 0.0722 * _lin(b)


def ratio(a, b):
    la, lb = _lum(a), _lum(b)
    hi, lo = max(la, lb), min(la, lb)
    return (hi + 0.05) / (lo + 0.05)


def var_block(selector):
    m = re.search(re.escape(selector) + r"\s*\{(.*?)\}", css, re.S)
    if not m:
        return {}
    return {mm.group(1): mm.group(2).strip()
            for mm in re.finditer(r"--([a-z0-9-]+)\s*:\s*([^;]+);", m.group(1))}


base = var_block(":root")
light_green = var_block(':root[data-accent="green"]')
light_purple = var_block(':root[data-accent="purple"]')
dark = var_block(':root[data-theme="dark"]')
dark_green = var_block(':root[data-theme="dark"][data-accent="green"]')
dark_purple = var_block(':root[data-theme="dark"][data-accent="purple"]')

if not base:
    fail("assets/site.css", ":root degiskenleri okunamadi")

COMBOS = [
    ("acik/mavi", base),
    ("acik/yesil", {**base, **light_green}),
    ("acik/mor", {**base, **light_purple}),
    ("koyu/mavi", dark),
    ("koyu/yesil", {**dark, **dark_green}),
    ("koyu/mor", {**dark, **dark_purple}),
]

worst = 99.0
worst_label = ""
for label, V in COMBOS:
    for k in ("bg", "panel", "ink", "ink-2", "ink-3", "accent", "accent-ink"):
        if k not in V:
            fail("assets/site.css", f"{label}: --{k} tanimli degil")
    if not all(k in V for k in ("bg", "panel", "ink", "ink-2", "ink-3",
                                "accent", "accent-ink")):
        continue
    checks = [(V["ink"], "ink"), (V["ink-2"], "ink-2"), (V["ink-3"], "ink-3")]
    for fg, name in checks:
        for bgk in ("bg", "panel"):
            r = ratio(fg, V[bgk])
            if r < worst:
                worst, worst_label = r, f"{label} {name}/{bgk}"
            if r < 4.5:
                fail("assets/site.css",
                     f"{label}: {name} / {bgk} kontrast {r:.2f}, AA icin 4.5 gerekli")
    for a, b in (("accent", "bg"), ("accent", "panel"), ("accent-ink", "accent")):
        r = ratio(V[a], V[b])
        if r < worst:
            worst, worst_label = r, f"{label} {a}/{b}"
        if r < 4.5:
            fail("assets/site.css",
                 f"{label}: {a} / {b} kontrast {r:.2f}, AA icin 4.5 gerekli")

# ------------------------------------------------- kaynak kodla sayi dogrulama

DUMP = ROOT / "ANKORA_AYAZ_DE_ALL_CODES.txt"
if DUMP.exists():
    SRC = DUMP.read_text("utf-8")

    def rust_list(name):
        i = SRC.index(f"const {name}: &[&str] = &[")
        return len(re.findall(r'"([^"]+)"', SRC[i:SRC.index("];", i)]))

    idx_html = SRC[SRC.index("FILE: src/index.html"):SRC.index("FILE: src/style.css")]
    app_js = SRC[SRC.index("FILE: src/app.js"):SRC.index("FILE: src/index.html")]
    rust = SRC[SRC.index("FILE: src-tauri/src/main.rs"):]
    handler = rust[rust.index(".invoke_handler"):rust.index(".run(tauri::")]
    store_at = app_js.index("packages: [")

    truth = {
        "EXACT_ALLOWED_COMMANDS": rust_list("EXACT_ALLOWED_COMMANDS"),
        "ALLOWED_UTILITIES": rust_list("ALLOWED_UTILITIES"),
        "FORBIDDEN_LAUNCH_BINARIES": rust_list("FORBIDDEN_LAUNCH_BINARIES"),
        "ALLOWED_AGENT_ACTIONS": rust_list("ALLOWED_AGENT_ACTIONS"),
        "ALLOWED_DOC_EXTENSIONS": rust_list("ALLOWED_DOC_EXTENSIONS"),
        "SENSITIVE_FILE_PATTERNS": rust_list("SENSITIVE_FILE_PATTERNS"),
        "PENCERE": len(re.findall(r"<section[^>]*class=\"window", idx_html)),
        "RUST_TEST": len(re.findall(r"#\[test\]", rust)),
        "MODUL": len(re.findall(r"^  const [A-Za-z_]+ = \{", app_js, re.M)),
        "KISAYOL": len(re.findall(r"\{ id: '", re.search(
            r"defaults: \[(.*?)\n    \]", app_js, re.S).group(1))),
        "TAURI": len(re.findall(r"^\s+[a-z_][a-z_0-9]*,$", handler, re.M)),
        "MAGAZA": len(re.findall(r"\{ id: '", app_js[store_at:store_at + 60000])),
    }

    claims = [
        ("31 tam komutu", "31 fixed commands", "EXACT_ALLOWED_COMMANDS"),
        ("26 sistem aracını", "26 diagnostic utilities", "ALLOWED_UTILITIES"),
        ("59 sistem ve ağ ikili", "59 system and network binaries", "FORBIDDEN_LAUNCH_BINARIES"),
        ("15 tanımlı sistem eylemini", "15 defined system actions", "ALLOWED_AGENT_ACTIONS"),
        ("20 belge uzantısını", "20 permitted extensions", "ALLOWED_DOC_EXTENSIONS"),
        ("17 hassas dosya desenine", "17 sensitive path patterns", "SENSITIVE_FILE_PATTERNS"),
        ("13 otomatik Rust birim testi", "13 automated Rust unit tests", "RUST_TEST"),
        ("137 Tauri IPC komutu", "137 Tauri IPC commands", "TAURI"),
        ("18 yerleşik pencere", "18 built-in windows", "PENCERE"),
        ("176 paketli", "176-package", "MAGAZA"),
    ]

    corpus = "\n".join((ROOT / p).read_text("utf-8") for p in ALL_PAGES)
    corpus += (ROOT / "llms.txt").read_text("utf-8")

    for tr, en, key_ in claims:
        if tr in corpus or en in corpus:
            if str(truth[key_]) not in corpus:
                fail("check-site.py",
                     f"sayi tutarsiz: '{tr}' / '{en}' icin kaynak {truth[key_]} diyor")
    for stale in ("Yirmi yedi komut", "Twenty-seven commands", "111 Tauri", "114 Tauri",
                  "24 ikili", "22 belge", "80 ile 120", "80 and 120",
                  "80 bis 120", "80 a 120", "80\u2013120"):
        if stale in corpus:
            fail("check-site.py", f"eski sayi kalmis: {stale}")

    # Bostas bellek iddiasi: her dilde ana sayfada karsilastirma tablosu ve
    # 750 MB degeri bulunmali (kaynaksiz rakam yazilmaz, eskisi kalmaz).
    for Lg in LANGS:
        hpages = (ROOT / page_path(Lg, "home")).read_text("utf-8")
        if 'class="cmp"' not in hpages:
            fail(hpages, f"ana sayfada karsilastirma tablosu yok: {Lg}")
        if "750" not in hpages:
            fail(hpages, f"ana sayfada 750 MB degeri yok: {Lg}")

    print("Kaynak koddan okunan sayilar:")
    for k, v in truth.items():
        print(f"  {k:26} {v}")
    print()

# --------------------------------------------------------------------- rapor

print(f"Sayfa: {len(ALL_PAGES)}   Dil: {len(LANGS)}   Ikon: {len(icon_ids)}   "
      f"Sitemap: {len(sitemap_locs)}")
print(f"En dusuk kontrast orani: {worst:.2f} ({worst_label})"
      if worst < 99 else "Kontrast: okunamadi")

if notes:
    print("\nBILGI")
    for where, msg in notes:
        print(f"  {where}: {msg}")

if problems:
    print(f"\nSORUN ({len(problems)})")
    for where, msg in problems:
        print(f"  {where}: {msg}")
    sys.exit(1)

print("\nSorun yok.")
