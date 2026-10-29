#!/usr/bin/env python3
"""Ankora Linux sitesini sifirdan uretir.

Bes dil (tr, en, de, es, ru), iki tema (acik, koyu), uc vurgu rengi.
Sayfa iskeletleri ve SEO dosyalari bu betikten uretilir.
"""

import json
import pathlib

ROOT = pathlib.Path(__file__).parent
SITE = "https://ankora-linux.github.io/"
REPO = "https://github.com/Ankora-Linux/Ankora"
REL = REPO + "/releases"
ISSUES = REPO + "/issues"
LICENSE = REPO + "/blob/main/LICENSE"
FORUM = "https://ankalab.flarum.cloud"
MAIL = "linuxankora@gmail.com"
SECMAIL = "linuxankora@gmail.com"

LANGS = ["tr", "en", "de", "es", "ru"]
FOLDER = {"tr": "", "en": "en", "de": "de", "es": "es", "ru": "ru"}
OGLOCALE = {"tr": "tr_TR", "en": "en_US", "de": "de_DE",
            "es": "es_ES", "ru": "ru_RU"}
INLANG = {"tr": "tr-TR", "en": "en-US", "de": "de-DE",
          "es": "es-ES", "ru": "ru-RU"}
CODELABEL = {"tr": "TR", "en": "EN", "de": "DE", "es": "ES", "ru": "RU"}
LANGNAME = {"tr": "Türkçe", "en": "English", "de": "Deutsch",
            "es": "Español", "ru": "Русский"}

KEYS = ["home", "features", "install", "security", "changelog", "faq", "contact"]
NAVORDER = ["home", "features", "security", "changelog", "contact"]

FILES = {
    "tr": {"home": "index.html", "features": "ozellikler.html", "install": "kurulum.html",
           "security": "guvenlik.html", "changelog": "surum-gecmisi.html",
           "faq": "sss.html", "contact": "iletisim.html"},
    "en": {"home": "index.html", "features": "features.html", "install": "install.html",
           "security": "security.html", "changelog": "changelog.html",
           "faq": "faq.html", "contact": "contact.html"},
    "de": {"home": "index.html", "features": "funktionen.html", "install": "installieren.html",
           "security": "sicherheit.html", "changelog": "versionen.html",
           "faq": "faq.html", "contact": "kontakt.html"},
    "es": {"home": "index.html", "features": "funciones.html", "install": "instalar.html",
           "security": "seguridad.html", "changelog": "versiones.html",
           "faq": "faq.html", "contact": "contacto.html"},
    "ru": {"home": "index.html", "features": "vozmozhnosti.html", "install": "ustanovka.html",
           "security": "bezopasnost.html", "changelog": "versii.html",
           "faq": "faq.html", "contact": "kontakty.html"},
}

THEME_SCRIPT = ("<script>(function(){var r=document.documentElement;"
                "function g(k){var v=null;try{v=localStorage.getItem(k)}catch(e){}"
                "if(!v){var m=(document.cookie||'').match(new RegExp('(?:^|; )'+k+'=([^;]*)'));"
                "if(m){try{v=decodeURIComponent(m[1])}catch(e){v=m[1]}}}return v}"
                "var t=g('ankora-theme')||'auto';"
                "if(['light','dark','auto'].indexOf(t)<0)t='auto';"
                "var a=g('ankora-accent')||'blue';"
                "if(['blue','green','purple'].indexOf(a)<0)a='blue';"
                "r.dataset.themePref=t;"
                "r.dataset.theme=(t==='auto'?(matchMedia('(prefers-color-scheme:dark)').matches?'dark':'light'):t);"
                "r.dataset.accent=a;})();</script>")

U = {
    "tr": {"settings": "Görünüm", "language": "Dil", "theme": "Tema",
           "tLight": "Açık", "tDark": "Koyu", "tAuto": "Sistem",
           "accent": "Vurgu rengi", "aBlue": "Mavi", "aGreen": "Yeşil", "aPurple": "Mor",
           "download": "İndir", "skip": "İçeriğe geç", "menu": "Menüyü aç",
           "nav": "Ana gezinme", "navm": "Ana gezinme (mobil)", "brand": "Ankora Linux",
           "copy": "Kopyala", "copied": "Kopyalandı",
           "about": "Son kullanıcı için sade, Devuan tabanlı ve Türkçe bir işletim sistemi.",
           "c1": "Dağıtım", "c2": "Yardım", "c3": "Kaynak",
           "short": "Ankora Linux 4.0 · GPL-3.0", "sitemap": "Site haritası",
           "col_link": "Kaynak kod",
           "bayram": "29 Ekim Cumhuriyet Bayramı'nız kutlu olsun"},
    "en": {"settings": "Appearance", "language": "Language", "theme": "Theme",
           "tLight": "Light", "tDark": "Dark", "tAuto": "System",
           "accent": "Accent colour", "aBlue": "Blue", "aGreen": "Green", "aPurple": "Purple",
           "download": "Download", "skip": "Skip to content", "menu": "Open menu",
           "nav": "Main navigation", "navm": "Main navigation (mobile)", "brand": "Ankora Linux",
           "copy": "Copy", "copied": "Copied",
           "about": "A simple, Turkish operating system built on Devuan.",
           "c1": "Distribution", "c2": "Help", "c3": "Source",
           "short": "Ankora Linux 4.0 · GPL-3.0", "sitemap": "Sitemap",
           "col_link": "Source code",
           "bayram": "Happy Republic Day of Türkiye (29 October)"},
    "de": {"settings": "Darstellung", "language": "Sprache", "theme": "Design",
           "tLight": "Hell", "tDark": "Dunkel", "tAuto": "System",
           "accent": "Akzentfarbe", "aBlue": "Blau", "aGreen": "Grün", "aPurple": "Violett",
           "download": "Herunterladen", "skip": "Zum Inhalt springen", "menu": "Menü öffnen",
           "nav": "Hauptnavigation", "navm": "Hauptnavigation (mobil)", "brand": "Ankora Linux",
           "copy": "Kopieren", "copied": "Kopiert",
           "about": "Ein schlichtes türkisches Betriebssystem auf Devuan-Basis.",
           "c1": "Distribution", "c2": "Hilfe", "c3": "Quellcode",
           "short": "Ankora Linux 4.0 · GPL-3.0", "sitemap": "Sitemap",
           "col_link": "Quellcode",
           "bayram": "Frohen Tag der Republik der Türkei (29. Oktober)"},
    "es": {"settings": "Apariencia", "language": "Idioma", "theme": "Tema",
           "tLight": "Claro", "tDark": "Oscuro", "tAuto": "Sistema",
           "accent": "Color de acento", "aBlue": "Azul", "aGreen": "Verde", "aPurple": "Morado",
           "download": "Descargar", "skip": "Ir al contenido", "menu": "Abrir el menú",
           "nav": "Navegación principal", "navm": "Navegación principal (móvil)",
           "brand": "Ankora Linux", "copy": "Copiar", "copied": "Copiado",
           "about": "Un sistema operativo turco, sencillo y basado en Devuan.",
           "c1": "Distribución", "c2": "Ayuda", "c3": "Código",
           "short": "Ankora Linux 4.0 · GPL-3.0", "sitemap": "Mapa del sitio",
           "col_link": "Código fuente",
           "bayram": "Feliz Día de la República de Turquía (29 de octubre)"},
    "ru": {"settings": "Оформление", "language": "Язык", "theme": "Тема",
           "tLight": "Светлая", "tDark": "Тёмная", "tAuto": "Системная",
           "accent": "Акцентный цвет", "aBlue": "Синий", "aGreen": "Зелёный", "aPurple": "Фиолетовый",
           "download": "Скачать", "skip": "Перейти к содержимому", "menu": "Открыть меню",
           "nav": "Основная навигация", "navm": "Основная навигация (мобильная)",
           "brand": "Ankora Linux", "copy": "Копировать", "copied": "Скопировано",
           "about": "Простая турецкая операционная система на базе Devuan.",
           "c1": "Дистрибутив", "c2": "Помощь", "c3": "Код",
           "short": "Ankora Linux 4.0 · GPL-3.0", "sitemap": "Карта сайта",
           "col_link": "Исходный код",
           "bayram": "С Днём Республики Турции (29 октября)"},
}

NAVL = {
    "tr": {"home": "Ana sayfa", "features": "Özellikler", "security": "Güvenlik",
           "changelog": "Sürümler", "contact": "İletişim", "faq": "SSS"},
    "en": {"home": "Home", "features": "Features", "security": "Security",
           "changelog": "Releases", "contact": "Contact", "faq": "FAQ"},
    "de": {"home": "Startseite", "features": "Funktionen", "security": "Sicherheit",
           "changelog": "Versionen", "contact": "Kontakt", "faq": "FAQ"},
    "es": {"home": "Inicio", "features": "Funciones", "security": "Seguridad",
           "changelog": "Versiones", "contact": "Contacto", "faq": "Preguntas"},
    "ru": {"home": "Главная", "features": "Возможности", "security": "Безопасность",
           "changelog": "Версии", "contact": "Контакты", "faq": "FAQ"},
}

# Ayaz DE 4.0 sistem temalari (src/style.css ve src/index.html ile birebir)
AYAZ_THEMES = [
    ("Nordik Açık", "#f8fafc", "#2563eb", "Aydınlık gümüş ve beyaz", "Bright silver and white"),
    ("Modern Grafit", "#12151e", "#3b82f6", "Dengeli antrasit koyu tema", "Balanced anthracite dark"),
    ("Derin Gece", "#050811", "#6366f1", "OLED uyumlu lacivert gece kipi", "OLED navy night mode"),
    ("Kuzey Fjordu", "#242933", "#88c0d0", "Nord esintili buz mavisi koyu", "Nord-inspired frost blue"),
    ("Çam Ormanı", "#0f1914", "#10b981", "Göz yormayan derin yeşil", "Deep forest green"),
    ("Kor Ateşi", "#180d10", "#f43f5e", "Sıcak bordo ve kızıl gece", "Warm crimson dark"),
    ("Arktik Serinlik", "#eef6ff", "#0284c7", "Buz mavisi ferah açık tema", "Ice-blue light theme"),
    ("Çınar", "#f4efe6", "#2f5d41", "Sıcak kağıt dokusu, yosun yeşili", "Warm paper, moss green"),
    ("Meltem", "#edf2f6", "#0b6477", "Soğuk deniz grisi, petrol mavisi", "Sea grey, teal accent"),
    ("Kor", "#16120e", "#d96b27", "Koyu kahve zemin, kor turuncusu", "Dark espresso, ember orange"),
    ("Dem", "#17171a", "#c83e37", "Düz grafit, sert kırmızı vurgu", "Flat graphite, red accent"),
    ("Boğaz", "#0e171b", "#d49b35", "Koyu deniz yeşili, pirinç sarısı", "Deep sea green, brass gold"),
    ("Ayna", "#0c0e14", "#33ccff", "Keskin camgöbeği çerçeveli koyu", "Crisp cyan-bordered dark"),
    ("Cumhuriyet", "#1d0e10", "#e23744", "29 Ekim özel: bayrak kırmızısı zemin, ay-yıldız beyazı", "Republic Day special: flag-red base, crescent white"),
]

# --------------------------------------------------------------------- metinler

T = {
    "tr": {
        "m_home": ("Ankora Linux 4.0: Eski bilgisayarınızı yeniden kullanın",
                   "Ankora Linux 4.0, Devuan 5.0 Daedalus ve Ayaz DE 4.0 üzerine kurulu sade ve Türkçe bir işletim sistemidir. Eco RAM kipi, 14 sistem teması ve 278 mağaza paketiyle gelir."),
        "m_features": ("Özellikler · Ankora Linux 4.0",
                       "Ankora Linux 4.0 ile neler yapabilirsiniz: 18 yerleşik pencere, 14 tam sistem teması, Eco RAM kipi, yerel Ankora AI asistanı, 278 paketli mağaza ve tek düğmeli güncelleme."),
        "m_install": ("İndir ve kur · Ankora Linux 4.0",
                      "Ankora Linux 4.0 sürümünü indirin ve kurun. Bir USB belleğe yazıp başlatın ya da zaten Linux kullanıyorsanız uçbirimden doğrulayıp yazdırın."),
        "m_security": ("Güvenlik · Ankora Linux 4.0",
                       "Ankora Linux 4.0 sizi nasıl korur: 31 izinli uçbirim komutu, 59 yasaklı ikili dosya, tek kullanımlık jetonlu 15 AI eylemi ve doğrulanmış güncellemeler."),
        "m_changelog": ("Sürümler · Ankora Linux 4.0",
                        "Ankora Linux'un bugüne kadarki sürümleri: 3.6, 3.5, 3.0, 2.0 AyazDE, 02.0 Zümrüt ve 01.0. En yeni sürümü indirin."),
        "m_faq": ("Sık sorulan sorular · Ankora Linux 4.0",
                  "Ankora Linux 4.0 hakkında sık sorulan sorular: kurulum, eski bilgisayarlar, Eco RAM kipi, güncellemeler, dil ve katkı."),
        "m_contact": ("İletişim · Ankora Linux",
                      "Ankora Linux topluluğu: forum, proje e-postası, hata bildirimi ve güvenlik açığı bildirimi için kanallar."),
        "hero_meta": ("Ankora Linux 4.0.0", "Ayaz DE 4.0", "Devuan 5.0 Daedalus", "SysVinit · ~750 MB RAM"),
        "h1": "Eski bilgisayarınızı yeniden kullanın",
        "lede": "Ankora Linux 4.0, son kullanıcı ve eğitim kurumları için geliştirilmiş sade, Devuan tabanlı ve Türkçe bir işletim sistemidir. 4 GB altı bilgisayarlarda otomatik devreye giren Eco RAM kipi, 14 tam sistem teması ve 278 paketli mağazasıyla kurulduğu anda çalışmaya hazırdır. Bu sürüm 29 Ekim Cumhuriyet Bayramı için özel olarak hazırlanmış bayrak kırmızısı Cumhuriyet temasıyla gelir.",
        "shot_alt": "Ayaz DE 4.0 masaüstü: solda masaüstü simgeleri ve açık Başlat menüsü, sağda Ankora Karşılayıcı penceresi ile saat ve bellek göstergesi",
        "shot_tabs": [
            ("01", "Masaüstü ve Başlat", "ayaz-masaustu.png",
             "Ayaz DE 4.0 masaüstü: açık Başlat menüsü, Ankora Karşılayıcı penceresi, ortalanmış görev çubuğu ve 748 MB bellek kullanımı",
             "Ayaz DE 4.0 masaüstü ve Başlat menüsü", "Modern Grafit · 748 MB / 8.0 GB RAM"),
            ("02", "14 Sistem Teması", "ankora-temalar.jpg",
             "Ankora Linux 4.0 Sistem Ayarları: Nordik Açık'tan Cumhuriyet'e kadar 14 tam sistem tema paketi",
             "14 tam sistem tema paketi", "Pencere, alt panel, simge seti ve duvar kağıdı tek tıkla değişir"),
            ("03", "Mağaza ve Sistem", "ankora-karsilayici.jpg",
             "Solda 278 paketli Ankora Yazılım Mağazası, sağda Devuan 5 ve Ayaz DE 4.0 sistem bilgileri",
             "Yazılım Mağazası ve Sistem Bilgisi", "278 seçilmiş paket · Devuan 5.0 Daedalus"),
            ("04", "Dosyalar ve Güncelleyici", "ankora-duvar.jpg",
             "Solda üst menü çubuklu Dosyalar yöneticisi, sağda Ayaz Güncelleyici v4.0.0 penceresi",
             "Dosyalar yöneticisi ve Ayaz Güncelleyici", "Otomatik USB bağlama · Ayaz Güncelleyici v4.0.0"),
            ("05", "Ankora AI ve Uçbirim", "ankora-ai.jpg",
             "Çınar temasında solda yerel Ollama destekli Ankora AI Sistem Asistanı, sağda yerleşik Linux uçbirimi",
             "Ankora AI Sistem Asistanı ve Uçbirim", "Yerel Ollama ve çoklu model · Çınar teması"),
        ],
        "specs": [
            ("~750 MB", "Boşta bellek kullanımı (Eco RAM kipi)"),
            ("18", "Yerleşik Ayaz DE masaüstü penceresi"),
            ("13", "Tam sistem tema paketi"),
            ("278", "Yazılım mağazası paketi ve ETAP aracı"),
        ],
        "why_eyebrow": "Neden Ankora 4.0", "why_h2": "Düşük bellekli bilgisayarlar ve günlük kullanım için üretildi",
        "cards3": [
            ("Hafif ve Eco RAM kipi", "Masaüstü boştayken yaklaşık 750 MB bellek kullanır. 4 GB altı belleğe sahip bilgisayarlarda Eco RAM kipi otomatik açılır; kapatılan pencereler 30 saniye sonra bellekten temizlenir."),
            ("Baştan sona Türkçe", "Kurulum sihirbazından 18 yerleşik pencereye, yerel AI sistem doktorundan ETAP akıllı tahta araçlarına kadar her yer Türkçedir. İngilizce terim aramak zorunda kalmazsınız."),
            ("Kolay kurulum ve bakım", "ISO dosyasını USB belleğe yazıp başlatmanız yeterlidir. Yerleşik USB ve ISO yazıcı, Başlat menüsü düzenleyici ve tek düğmeli Ayaz Güncelleyici uçbirim ihtiyacını ortadan kaldırır."),
        ],
        "inside_eyebrow": "İçinde neler var", "inside_h2": "Kurduğunuz anda kullanmaya başlarsınız",
        "inside_lede": "Ayrı ayrı program aramanız gerekmez. Günlük işler, okul tahtaları ve ofis belgeleri için gereken araçlar Ayaz DE 4.0 içinde hazır gelir.",
        "inside": [
            "Web tarayıcı (Ayaz ve Brave) ile üst menü çubuklu, otomatik USB bağlamalı Dosyalar yöneticisi",
            "278 paketli Yazılım Mağazası (MEB Sertifikası, Scratch, GCompris, GeoGebra ve ETAP araçları dahil)",
            "14 tam sistem teması (Çınar, Meltem, Kor, Dem, Boğaz, Ayna dahil), 15 duvar kağıdı ve 8 ikon seti",
            "Ankora AI Sistem Asistanı (yerel Ollama veya kendi API anahtarınızla, tek kullanımlık jeton onaylı)",
            "Yerleşik USB ve ISO yazıcı, Başlat menüsü düzenleyici, PDF/belge görüntüleyici ve Ankora Ofis",
            "Tek düğmeli Ayaz Güncelleyici ve ankora-doctor sistem sağlık taraması",
        ],
        "inside_alt": "Ankora Linux 4.0 Yazılım Mağazası ve Sistem Dağıtım Bilgisi pencereleri",
        "step_eyebrow": "Kurulum", "step_h2": "Üç adımda hazır",
        "steps3": [("İndirin", "ISO dosyasını indirin. Yanında doğrulama dosyası da bulunur."),
                   ("USB belleğe yazın", "Ücretsiz bir programla ISO'yu boş bir USB belleğe yazın."),
                   ("Başlatın ve kurun", "Bilgisayarı USB'den açın, kurulum sihirbazı gerisini anlatır.")],
        "faq_eyebrow": "Sık sorulan sorular", "faq_h2": "Merak edilenler",
        "faq4": [("Ankora Linux nedir?", "Ücretsiz ve Türkçe bir işletim sistemidir. Devuan 5.0 Daedalus (SysVinit) üzerine kuruludur ve kendi masaüstü ortamı Ayaz DE 4.0 ile birlikte gelir."),
                 ("Eski bir bilgisayarda çalışır mı?", "Evet. Boştayken yaklaşık 750 MB bellek kullanır ve 4 GB altı bellekte Eco RAM kipini otomatik açar. 2 GB bellekli dizüstü bilgisayarlarda rahat çalışır; 1 GB bellekli çok eski makineler için önerilmez."),
                 ("Ücretli mi?", "Hayır, tamamen ücretsizdir. Kaynak kodu GPL-3.0 lisansıyla açıktır."),
                 ("Nasıl kurulur?", "ISO dosyasını bir USB belleğe yazıp bilgisayarı ondan başlatın. Kurulum sihirbazı adım adım yönlendirir.")],
        "all_q": "Tüm sorular",
        "cmp_eyebrow": "Boşta bellek",
        "cmp_h2": "Popüler dağıtımlarla karşılaştırma",
        "cmp_lede": "Masaüstü boştaki bellek kullanımı. Ankora ölçümü kurulu sistemde free -m ile alındı; diğer değerler sitede belirtilen kaynaklardan.",
        "cmp_head": ("Dağıtım", "Boşta bellek"),
        "cmp_rows": [("Ankora Linux 4.0 (Ayaz DE)", "~750 MB"),
                     ("Ubuntu 24.04 (GNOME)", "830 MB"),
                     ("Linux Mint 22.1 (Cinnamon)", "888 MB"),
                     ("Xubuntu 24.04 (Xfce)", "668 MB"),
                     ("Lubuntu 24.04 (LXQt)", "464 MB"),
                     ("Debian 12 (GNOME)", "1 GB'nin üzerinde")],
        "cmp_note": "Ankora: kurulu sistemde, masaüstüne giriş sonrası free -m çıktısı (Ekim 2026). Diğer: Android Authority, Ekim 2024 ölçümleri; Mint için bağımsız inceleme (888 MB). Donanım, sürüm ve yöntem farklıdır; değerler yaklaşıktır.",
        "f_h1": "Ankora Linux 4.0 özellikleri",
        "f_lede": "Ayaz DE 4.0; 18 yerleşik masaüstü penceresi, 14 tam sistem teması, 278 paketli yazılım mağazası ve Eco RAM kipini hafif bir WebKitGTK ve Rust Tauri çekirdeğinde birleştirir.",
        "f_hl_eyebrow": "Bir bakışta", "f_hl_h2": "3.6 sürümünde öne çıkanlar",
        "f_cards": [("Eco RAM kipi ve ~750 MB bellek", "4 GB altı sistemlerde arka plan yükünü kısar ve kapatılan pencereleri 30 saniye sonra DOM'dan ayırarak belleği korur."),
                    ("Baştan sona Türkçe", "Kurulum sihirbazı, masaüstü, dosya yöneticisi, AI sistem asistanı ve tüm ayarlar tamamen Türkçedir."),
                    ("18 yerleşik pencere", "Dosyalar, tarayıcı, Ankora Ofis, PDF görüntüleyici, hesap makinesi, USB/ISO yazıcı ve menü düzenleyici kurulu gelir."),
                    ("278 paket ve ETAP desteği", "Yazılım mağazasında günlük uygulamaların yanında MEB Sertifikası, Scratch, GCompris, GeoGebra ve akıllı tahta dokunmatik sürücüsü bulunur."),
                    ("14 tam sistem teması", "Tek seçimle pencere yüzeyleri, görev çubuğu, duvar kağıdı, ikon seti ve vurgu rengi birlikte değişir."),
                    ("Ankora AI ve tek tıkla güncelleme", "Yerel Ollama veya çoklu model API desteğiyle sistem teşhisi yapar; sistem eylemlerinde tek kullanımlık güvenlik jetonu ister.")],
        "f_themes_eyebrow": "14 sistem teması", "f_themes_h2": "Tek seçimle tüm masaüstü kimliği değişir",
        "f_themes_lede": "Ayaz DE 4.0 içinde her tema paketi görev çubuğunu, pencere renklerini, duvar kağıdını ve simge paketini bir bütün olarak günceller.",
        "f_apps_eyebrow": "Uygulamalar", "f_apps_h2": "Kurulu gelen 18 yerleşik araç",
        "f_apps_lede": "Temel işler için ayrı ayrı paket aramanız gerekmez.",
        "f_apps": ["Web tarayıcı (Ayaz ve Brave)", "Üst menü çubuklu ve otomatik USB bağlamalı Dosyalar yöneticisi", "Belge, PDF ve fotoğraf görüntüleyici",
                   "Ankora Ofis ve not defteri", "Hesap makinesi ve ekran görüntüsü aracı", "USB ve ISO yazıcı / biçimlendirici",
                   "Yazılım mağazası (278 paket)", "Ankora AI Sistem Asistanı", "Sistem ayarları, Ayaz Güncelleyici ve görev yöneticisi"],
        "f_apps_alt": "Ankora Linux 4.0 Dosyalar yöneticisi ve Ayaz Güncelleyici pencereleri",
        "f_cta_h2": "Ankora Linux 4.0'yı denemek ister misiniz?", "f_cta_lede": "Kurulum bir USB bellek ve birkaç adımdan ibaret.",
        "i_h1": "İndir ve kur",
        "i_lede": "Bir USB bellek ve birkaç dakika yeterli. Zaten Linux kullanıyorsanız uçbirimden doğrulayıp yazdırabilirsiniz.",
        "i_dl": "Ankora Linux 4.0 sürümlerini aç", "i_src": "Kaynak kodu",
        "i_req_eyebrow": "Gereksinimler", "i_req_h2": "Neye ihtiyacınız var?",
        "i_req": ["64 bit (amd64) işlemci", "En az 2 GB bellek (4 GB altı sistemlerde Eco RAM kipi otomatik açılır)",
                  "ISO için boş bir USB bellek (en az 4 GB)", "İnternet bağlantısı (indirme için)"],
        "i_step_eyebrow": "Kurulum", "i_step_h2": "Üç adımda hazır",
        "i_steps": [("İndirin", "Sürümler sayfasından ISO dosyasını ve yanındaki SHA-256 doğrulama dosyasını indirin."),
                    ("USB belleğe yazın", "Ankora USB Yazıcı, BalenaEtcher veya Rufus gibi ücretsiz bir programla ISO'yu boş bir USB belleğe yazın."),
                    ("Başlatın ve kurun", "Bilgisayarı USB'den başlatın. Kurulum sihirbazı adım adım ilerler ve sonunda sistem yeniden başlar.")],
        "i_cli_eyebrow": "Komut satırı", "i_cli_h2": "Terminalden yapmak isterseniz",
        "i_note_b": "Dikkat", "i_note_p": "/dev/sdX yolunu kendiniz doğrulayın. Yanlış sürücü seçilirse o diskin içeriği silinir.",
        "s_h1": "Ankora Linux 4.0 güvenlik mimarisi",
        "s_lede": "Ankora Linux 4.0, arayüz ile sistem çekirdeğini birbirinden ayırır. Rust ile yazılmış 137 Tauri IPC komutu her işlemi sabit izin listelerine göre denetler.",
        "s_core_eyebrow": "Üç temel koruma", "s_core_h2": "Bu, sizin için ne anlama geliyor?",
        "s_cards": [("Programlar kafasına göre iş yapamaz", "Yerleşik uçbirim yalnızca izin verilen 31 komutu ve 26 yardımcı aracı çalıştırır; 59 tehlikeli ikili dosyanın doğrudan başlatılması engellenir."),
                    ("Güncellemeler ve AI eylemleri doğrulanır", "Paket ve sistem güncellemeleri izole yardımcı betiklerle kontrol edilir; AI ajanının 15 sistem eylemi tek kullanımlık güvenlik jetonu olmadan çalışmaz."),
                    ("Kişisel dosyalarınız korunur", "Belge görüntüleyici yalnızca 20 güvenli dosya uzantısını kabul eder; parola, anahtar ve gölge dosyaları içeren 17 hassas dosya deseni engellenir.")],
        "s_tech_eyebrow": "Kaynak kodda doğrulanabilir", "s_tech_h2": "Rust çekirdeğinde (main.rs) uygulanan sınırlar",
        "s_notes": [
            "Yerleşik uçbirim yalnızca önceden tanımlı 31 tam komutu ve 26 sistem aracını zincirleme operatörleri olmadan çalıştırır.",
            "Uygulama başlatıcıda 59 sistem ve ağ ikili dosyası yasaklı listesindedir.",
            "Ankora AI asistanı yalnızca 15 tanımlı sistem eylemini yürütebilir ve her eylem öncesinde tek kullanımlık güvenlik jetonu doğrulaması ister.",
            "Belge görüntüleyici yalnızca 20 belge uzantısını açar ve 17 hassas dosya desenine erişimi reddeder.",
            "Arayüz ile sistem arasındaki köprü 137 Tauri IPC komutu ve 13 otomatik Rust birim testi ile denetlenir.",
        ],
        "s_vuln": "Bir açık mı buldunuz? Herkese açık kayıt açmadan {mail} adresine yazın. Raporlar 48 saat içinde yanıtlanır.",
        "c_h1": "Sürümler", "c_lede": "Ankora Linux'un bugüne kadarki sürümleri. Güncel 4.0 sürümü en üstte yer alır.",
        "c_dl": "4.0 sürümünü indir",
        "c_rows": [("4.0", "AyazDE", "Güncel sürüm: 29 Ekim Cumhuriyet Bayramı özel sürüm. Güvenlik sertleştirmeleri (kilit ekranı girişim sınırlayıcı, pano koruması, IPC token), USB başlatma için hibrit ISO doğrulaması, h2 CVE yaması ve Cumhuriyet teması."),
                   ("3.7", "AyazDE", "Masaüstü kategori klasörleri, canlı hava durumu, modern cam Yazılım Merkezi, görev çubuğu mini AI sohbeti ve vizyon ekran analizi, MEB sertifikası tam temizleme ve .deb sistem güncelleyicisi."),
                   ("3.6", "AyazDE", "Menü çubuklu Dosyalar yöneticisi, USB/ISO yazıcı ve ETAP akıllı tahta desteği."),
                   ("3.5", "AyazDE", "4 GB altı bilgisayarlar için Eco RAM kipi, udisks ile otomatik USB bağlama ve kapatılan pencereler için 30 saniyede bellek boşaltma."),
                   ("3.0", "AyazDE", "Devuan 5.0 Daedalus (SysVinit) üzerinde yeni Rust ve Tauri 1.5 masaüstü çekirdeği."),
                   ("2.0", "AyazDE", "Masaüstü ortamı Ayaz DE oldu; sistem daha da hafifledi."),
                   ("02.0", "Zümrüt", "Masaüstü entegrasyonları güncellendi, ayarlar yenilendi."),
                   ("01.0", "İlk sürüm", "İlk kararlı sürüm. Sade ve telemetrisiz bir temel.")],
        "c_foot": "Tüm sürümlerin dosyaları GitHub sürümler sayfasında yer alır.",
        "row_go": "indir",
        "q_h1": "Sık sorulan sorular",
        "q_lede": "Aradığınızı bulamazsanız iletişim sayfasına bakın.",
        "q_qas": [("Ankora Linux nedir?", "Ücretsiz ve Türkçe bir işletim sistemidir. Devuan 5.0 Daedalus üzerine kuruludur ve kendi masaüstü ortamı Ayaz DE 4.0 ile birlikte gelir."),
                  ("Eski bir bilgisayarda çalışır mı?", "Evet. Boştayken yaklaşık 750 MB bellek kullanır ve 4 GB altı belleğe sahip makinelerde Eco RAM kipini otomatik açar. 2 GB bellekli dizüstü bilgisayarlarda rahat çalışır; 1 GB bellekli çok eski makineler için önerilmez."),
                  ("Diskimi silmeden deneyebilir miyim?", "Evet. ISO'yu USB belleğe yazıp açtığınızda diskteki sisteminize dokunulmaz. Denemek için güvenli bir yoldur."),
                  ("Nasıl kurulur?", "ISO dosyasını bir USB belleğe yazıp bilgisayarı ondan başlatın. Kurulum sihirbazı adım adım yönlendirir. Ayrıntılar indir sayfasında."),
                  ("Ücretli mi?", "Hayır, tamamen ücretsizdir. Kaynak kodu GPL-3.0 lisansıyla açıktır, dilediğiniz gibi inceleyip değiştirebilirsiniz."),
                  ("Güncellemeler nasıl geliyor?", "Güncellemeler Ayaz Güncelleyici üzerinden doğrulanmış Ankora ve Devuan depolarından gelir. Her paketin bütünlüğü kontrol edilir."),
                  ("Arayüz dili nedir?", "Arayüz tamamen Türkçedir. Klavye düzeni olarak Türkçe, İngilizce, Almanca, Fransızca ve İngiliz (GB) arasından seçim yapabilirsiniz."),
                  ("Nasıl katkı yapabilirim?", "GitHub deposunu çatallayıp çekme isteği gönderebilir, ya da forumda soru ve öneri paylaşabilirsiniz.")],
        "q_forum": "Forumda sorun", "q_contact": "İletişim",
        "k_h1": "İletişim",
        "k_lede": "Sorunuzun türüne göre doğru kanalı seçin. Forum genel sorular için en hızlı yer.",
        "k_rows": [("Ankora Lab forumu", "kurulum, ayar, kullanım", "foruma git"),
                   ("Proje e-postası", MAIL, "e-posta gönder"),
                   ("Hata bildir", "github.com/Ankora-Linux/Ankora", "kayıt aç"),
                   ("Güvenlik açığı", SECMAIL, "e-posta gönder")],
        "k_bug_eyebrow": "Hata bildirirken", "k_bug_h2": "Şunları eklerseniz hızlı yardım alırsınız",
        "k_items": ["Sürüm bilgisi (Ankora Linux 4.0)", "Hatanın oluştuğu adımlar",
                    "Varsa hata çıktısı", "İşlemci ve bellek bilgisi"],
    },
    "en": {
        "m_home": ("Ankora Linux 4.0: Bring your old computer back to life",
                   "Ankora Linux 4.0 is a free Turkish operating system built on Devuan 5.0 Daedalus with Ayaz DE 4.0, Eco RAM mode, 14 system themes, and 278 store packages."),
        "m_features": ("Features · Ankora Linux 4.0",
                       "What you can do with Ankora Linux 4.0: 18 built-in windows, 14 full-system themes, Eco RAM mode, local Ankora AI assistant, 278 store packages, and one-button updates."),
        "m_install": ("Download and install · Ankora Linux 4.0",
                      "Download and install Ankora Linux 4.0. Write it to a USB stick and boot, or verify and flash from the terminal."),
        "m_security": ("Security · Ankora Linux 4.0",
                       "How Ankora Linux 4.0 protects you: 31 allowed terminal commands, 59 blocked binaries, 15 one-time-token AI actions, and verified updates."),
        "m_changelog": ("Releases · Ankora Linux 4.0",
                        "Every Ankora Linux release so far: 3.6, 3.5, 3.0, 2.0 AyazDE, 02.0 Zümrüt and 01.0. Download the newest release."),
        "m_faq": ("Frequently asked questions · Ankora Linux 4.0",
                  "Common questions about Ankora Linux 4.0: installation, old computers, Eco RAM mode, updates, language and contributing."),
        "m_contact": ("Contact · Ankora Linux",
                      "The Ankora Linux community: channels for the forum, project email, bug reports and security disclosures."),
        "hero_meta": ("Ankora Linux 4.0.0", "Ayaz DE 4.0", "Devuan 5.0 Daedalus", "SysVinit · ~750 MB RAM"),
        "h1": "Bring your old computer back to life",
        "lede": "Ankora Linux 4.0 is a clean, Devuan-based Turkish operating system built for everyday users and classrooms. With Eco RAM mode enabled automatically under 4 GB of RAM, 14 full-system themes, and a 278-package software store, it is ready the moment you boot. This release marks Republic Day (29 October) with the flag-red Cumhuriyet theme.",
        "shot_alt": "Ayaz DE 4.0 desktop: desktop icons and open Start menu on the left, Ankora Welcome window on the right, clock and memory widgets at top right",
        "shot_tabs": [
            ("01", "Desktop & Start Menu", "ayaz-masaustu.png",
             "Ayaz DE 4.0 desktop with open Start menu, Welcome window, centred taskbar, and 748 MB RAM usage",
             "Ayaz DE 4.0 desktop and Start menu", "Modern Grafit · 748 MB / 8.0 GB RAM"),
            ("02", "14 System Themes", "ankora-temalar.jpg",
             "Ankora Linux 4.0 System Settings showing all 14 full-system theme packs from Nordik Açık to Ayna",
             "14 full-system theme packs", "Windows, taskbar, icon pack, and wallpaper switch together"),
            ("03", "Store & System Info", "ankora-karsilayici.jpg",
             "Ankora Software Store with 278 packages on the left and System Settings with Devuan 5 and Ayaz DE 4.0 details on the right",
             "Software Store and System Overview", "278 curated packages · Devuan 5.0 Daedalus"),
            ("04", "Files & Updater", "ankora-duvar.jpg",
             "Ayaz File Manager with menu bar on the left and Ayaz Updater v4.0.0 on the right",
             "File Manager and One-Button Updater", "Automatic USB mounting · Ayaz Updater v4.0.0"),
            ("05", "Ankora AI & Terminal", "ankora-ai.jpg",
             "Ankora AI System Assistant with local Ollama mode on the left and native Linux terminal on the right on the Çınar theme",
             "Ankora AI Assistant and Terminal", "Local Ollama & multi-model · Çınar theme"),
        ],
        "specs": [
            ("~750 MB", "Idle memory usage (Eco RAM mode)"),
            ("18", "Built-in Ayaz DE desktop windows"),
            ("13", "Full-system theme bundles"),
            ("278", "Curated store packages & ETAP tools"),
        ],
        "why_eyebrow": "Why Ankora 3.6", "why_h2": "Engineered for modest hardware and daily reliability",
        "cards3": [
            ("Light & Eco RAM mode", "Uses about 750 MB of memory when idle. On machines with under 4 GB of RAM, Eco RAM mode turns on automatically and unmounts closed windows from memory after 30 seconds."),
            ("Turkish throughout", "From the installer to all 18 built-in windows and smartboard classroom packages (ETAP), everything is written in clear Turkish."),
            ("Easy to install and maintain", "Write the ISO to a USB stick and boot. The built-in USB & ISO flasher, Start menu editor, and one-button Ayaz Updater remove the need for terminal commands."),
        ],
        "inside_eyebrow": "What is inside", "inside_h2": "Ready to use from the very first boot",
        "inside_lede": "You do not have to hunt for basic utilities; everyday tools for home, office, and classrooms are built right into Ayaz DE 4.0.",
        "inside": [
            "Web browser (Ayaz & Brave) plus File Manager with menu bar and automatic USB drive mounting",
            "278-package Software Store (including MEB Certificate, Scratch, GCompris, GeoGebra, and ETAP smartboard tools)",
            "14 full-system theme bundles (including Çınar, Meltem, Kor, Dem, Boğaz, and Ayna), 14 wallpapers, and 8 icon sets",
            "Ankora AI System Assistant (local Ollama or bring-your-own API key with one-time security token confirmation)",
            "Built-in USB & ISO Flasher, Start Menu Editor, PDF/document viewer, and Ankora Office notes",
            "One-button Ayaz Updater and ankora-doctor system health diagnostics",
        ],
        "inside_alt": "Ankora Linux 4.0 Software Store and System Distribution Information windows",
        "step_eyebrow": "Install", "step_h2": "Ready in three steps",
        "steps3": [("Download", "Get the ISO file. A verification file sits next to it."),
                   ("Write it to a USB stick", "Write the ISO to an empty USB stick with a free tool."),
                   ("Boot and install", "Start the computer from the USB stick. The wizard explains the rest.")],
        "faq_eyebrow": "FAQ", "faq_h2": "Common questions",
        "faq4": [("What is Ankora Linux?", "It is a simple Turkish operating system for everyday users. It is built on Devuan 5.0 Daedalus (systemd-free) and comes with its own desktop environment, Ayaz DE 4.0."),
                 ("Does it run on an old computer?", "Yes. It uses about 750 MB of memory when idle and enables Eco RAM mode automatically under 4 GB of RAM. It runs comfortably on a laptop with 2 GB of memory."),
                 ("Does it cost anything?", "No, it is completely free and open-source under the GPL-3.0 license."),
                 ("How do I install it?", "Write the ISO to a USB stick and boot the computer from it. The installer guides you step by step.")],
        "all_q": "All questions",
        "cmp_eyebrow": "Idle memory",
        "cmp_h2": "Comparison with popular distributions",
        "cmp_lede": "Idle desktop memory usage. The Ankora figure was measured on the installed system with free -m; the other figures come from the sources listed on the page.",
        "cmp_head": ("Distribution", "Idle memory"),
        "cmp_rows": [("Ankora Linux 4.0 (Ayaz DE)", "~750 MB"),
                     ("Ubuntu 24.04 (GNOME)", "830 MB"),
                     ("Linux Mint 22.1 (Cinnamon)", "888 MB"),
                     ("Xubuntu 24.04 (Xfce)", "668 MB"),
                     ("Lubuntu 24.04 (LXQt)", "464 MB"),
                     ("Debian 12 (GNOME)", "over 1 GB")],
        "cmp_note": "Ankora: output of free -m on the installed system after signing in to the desktop (October 2026). Others: measurements published by Android Authority in October 2024; for Mint, an independent review (888 MB). Hardware, versions and methods differ; these are approximate figures.",
        "f_h1": "Ankora Linux 4.0 features",
        "f_lede": "Ayaz DE 4.0 combines 18 built-in desktop windows, 14 full-system theme bundles, a 278-package software store, and Eco RAM mode on a lightweight WebKitGTK and Rust Tauri core.",
        "f_hl_eyebrow": "At a glance", "f_hl_h2": "What stands out in release 4.0",
        "f_cards": [("Eco RAM mode & ~750 MB idle", "Automatically trims background load on machines under 4 GB of RAM and unmounts closed windows from the DOM after 30 seconds."),
                    ("Turkish throughout", "The installer, desktop, file manager, AI system assistant, and all settings are written in Turkish."),
                    ("18 built-in windows", "Files, browser, Ankora Office, PDF viewer, calculator, USB/ISO flasher, and Start menu editor come preinstalled."),
                    ("278 packages & ETAP support", "The Software Store includes everyday apps alongside MEB Certificate, Scratch, GCompris, GeoGebra, and smartboard touch drivers."),
                    ("14 full-system themes", "A single click updates window surfaces, the taskbar, wallpaper, icon set, and accent colour together."),
                    ("Ankora AI & one-click updater", "Runs local diagnostics via Ollama or cloud API models with one-time security token confirmation, plus passwordless system updates.")],
        "f_themes_eyebrow": "14 system themes", "f_themes_h2": "One click switches the entire desktop identity",
        "f_themes_lede": "Each theme bundle in Ayaz DE 4.0 coordinates the taskbar, window palette, desktop wallpaper, and icon pack as a single package.",
        "f_apps_eyebrow": "Apps", "f_apps_h2": "18 built-in tools ready out of the box",
        "f_apps_lede": "You do not have to install separate programs for daily tasks.",
        "f_apps": ["Web browser (Ayaz & Brave)", "File Manager with menu bar & automatic USB mounting", "Document, PDF, and photo viewer",
                   "Ankora Office & notepad", "Calculator & screenshot tool", "USB & ISO flasher and formatter",
                   "Software Store (278 packages)", "Ankora AI System Assistant", "System Settings, Ayaz Updater & Task Manager"],
        "f_apps_alt": "Ankora Linux 4.0 File Manager and Ayaz Updater windows",
        "f_cta_h2": "Want to try Ankora Linux 4.0?", "f_cta_lede": "Installation is a USB stick and a few steps.",
        "i_h1": "Download and install",
        "i_lede": "A USB stick and a few minutes are enough. If you already use Linux, you can also verify and write the ISO from the terminal.",
        "i_dl": "Open the Ankora Linux 4.0 releases", "i_src": "Source code",
        "i_req_eyebrow": "Requirements", "i_req_h2": "What you need",
        "i_req": ["A 64-bit (amd64) processor", "At least 2 GB of memory (Eco RAM mode activates automatically under 4 GB)",
                  "An empty USB stick (at least 4 GB) for the ISO", "An internet connection (for the download)"],
        "i_step_eyebrow": "Install", "i_step_h2": "Ready in three steps",
        "i_steps": [("Download", "Get the ISO file and its SHA-256 verification file from the releases page."),
                    ("Write it to a USB stick", "Write the ISO to an empty USB stick with Ankora USB Flasher, BalenaEtcher, or Rufus."),
                    ("Boot and install", "Start the computer from the USB stick. The installer runs step by step and the system restarts at the end.")],
        "i_cli_eyebrow": "Command line", "i_cli_h2": "If you prefer the terminal",
        "i_note_b": "Careful", "i_note_p": "Check the /dev/sdX path yourself. If you pick the wrong drive, the contents of that disk are erased.",
        "s_h1": "Ankora Linux 4.0 security architecture",
        "s_lede": "Ankora Linux 4.0 strictly separates the user interface from the system core: 137 Rust Tauri IPC commands validate every operation against fixed allowlists.",
        "s_core_eyebrow": "Three core protections", "s_core_h2": "What does this mean for you?",
        "s_cards": [("Strict command allowlists", "The built-in terminal permits exactly 31 verified commands and 26 utilities, while 59 dangerous binaries are blocked from direct launch."),
                    ("Verified updates & AI actions", "System updates run through isolated helper scripts, and the AI agent's 15 permitted actions require a one-time security token."),
                    ("Protected personal files", "The document viewer accepts only 20 safe file extensions and blocks 17 sensitive file patterns including keys and password files.")],
        "s_tech_eyebrow": "Verifiable in source code", "s_tech_h2": "Guardrails enforced in the Rust core (main.rs)",
        "s_notes": [
            "The built-in terminal executes only 31 fixed commands and 26 diagnostic utilities without command-chaining operators.",
            "59 system and network binaries are blocked on the application launch denylist.",
            "The Ankora AI agent is restricted to 15 defined system actions and requires one-time security token confirmation before execution.",
            "The document viewer validates 20 permitted extensions and denies access to 17 sensitive path patterns.",
            "137 Tauri IPC commands and 13 automated Rust unit tests guard the bridge between the interface and the operating system.",
        ],
        "s_vuln": "Found a vulnerability? Write to {mail} without opening a public issue. Reports are answered within 48 hours.",
        "c_h1": "Releases", "c_lede": "Every Ankora Linux release so far. Current release 4.0 is at the top.",
        "c_dl": "Download 4.0",
        "c_rows": [("4.0", "AyazDE", "Current release: Republic Day special (29 October). Security hardening (lock screen rate limiting, clipboard protection, IPC tokens), hybrid ISO verification for USB boot, h2 CVE fix, and the Cumhuriyet theme."),
                   ("3.7", "AyazDE", "Desktop category folders, live weather widget, redesigned glass Software Store, taskbar mini AI chat & vision screen analysis, MEB certificate clean uninstall, and .deb update channel."),
                   ("3.6", "AyazDE", "Enhanced File Manager, USB/ISO flasher, and ETAP smartboard support."),
                   ("3.5", "AyazDE", "Eco RAM mode for systems under 4 GB RAM, automatic USB mounting via udisks, and 30-second lazy DOM unmounting for closed windows."),
                   ("3.0", "AyazDE", "New Rust and Tauri 1.5 desktop core on Devuan 5.0 Daedalus (SysVinit) with 17 built-in windows."),
                   ("2.0", "AyazDE", "The desktop environment became Ayaz DE and the system got lighter."),
                   ("02.0", "Zümrüt", "Desktop integrations were updated and the settings were refreshed."),
                   ("01.0", "First release", "The first stable release. A plain base with no telemetry.")],
        "c_foot": "All release files live on the GitHub releases page.",
        "row_go": "download",
        "q_h1": "Frequently asked questions",
        "q_lede": "If you cannot find your answer, see the contact page.",
        "q_qas": [("What is Ankora Linux?", "It is a simple Turkish operating system for everyday users. It is built on Devuan 5.0 Daedalus and comes with its own desktop environment, Ayaz DE 4.0."),
                  ("Does it run on an old computer?", "Yes. It uses about 750 MB of memory when idle and automatically enables Eco RAM mode on machines with under 4 GB of RAM. It runs comfortably on a laptop with 2 GB of memory; very old machines with 1 GB are not recommended."),
                  ("Can I try it without erasing my disk?", "Yes. When you write the ISO to a USB stick and boot it, the system on the disk is not touched."),
                  ("How do I install it?", "Write the ISO to a USB stick and boot the computer from it. The installer guides you step by step. Details are on the download page."),
                  ("Does it cost anything?", "No, it is completely free. The source code is open under GPL-3.0, so you can study and change it as you wish."),
                  ("How do updates arrive?", "Updates arrive through Ayaz Updater from the verified Ankora and Devuan repositories."),
                  ("What is the interface language?", "The interface is entirely in Turkish. For the keyboard you can pick Turkish, English, German, French or British (GB)."),
                  ("How can I contribute?", "Fork the GitHub repository and send a pull request, or share questions and suggestions on the forum.")],
        "q_forum": "Ask on the forum", "q_contact": "Contact",
        "k_h1": "Contact",
        "k_lede": "Pick the right channel for your question. The forum is the fastest place for general questions.",
        "k_rows": [("Ankora Lab forum", "setup, settings, usage", "go to forum"),
                   ("Project email", MAIL, "send email"),
                   ("Report a bug", "github.com/Ankora-Linux/Ankora", "open an issue"),
                   ("Security vulnerability", SECMAIL, "send email")],
        "k_bug_eyebrow": "When reporting a bug", "k_bug_h2": "Include these for a faster answer",
        "k_items": ["Version information (Ankora Linux 4.0)", "The steps that lead to the bug",
                    "Any error output", "Processor and memory information"],
    },
}

import i18n_extra

T.update(i18n_extra.EXTRA)

FOOTL = {
    "tr": {"forum": "Ankora Lab forumu", "repo": "GitHub deposu",
           "rel": "Sürümler", "lic": "GPL-3.0 lisansı"},
    "en": {"forum": "Ankora Lab forum", "repo": "GitHub repository",
           "rel": "Releases", "lic": "GPL-3.0 license"},
    "de": {"forum": "Ankora-Lab-Forum", "repo": "GitHub-Repository",
           "rel": "Versionen", "lic": "GPL-3.0-Lizenz"},
    "es": {"forum": "Foro Ankora Lab", "repo": "Repositorio de GitHub",
           "rel": "Versiones", "lic": "Licencia GPL-3.0"},
    "ru": {"forum": "Форум Ankora Lab", "repo": "Репозиторий GitHub",
           "rel": "Версии", "lic": "Лицензия GPL-3.0"},
}

CODE = """gh release download --repo Ankora-Linux/Ankora \\
  --pattern '*.iso*'

sha256sum -c *.iso.sha256

lsblk -d -o NAME,SIZE,MODEL
sudo dd if=ankora-linux.iso of=/dev/sdX bs=4M status=progress conv=fsync"""


def e(text):
    return (str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def rel_root(lang):
    return "" if lang == "tr" else "../"


def asset(lang, path):
    return rel_root(lang) + path


def local(lang, key):
    return FILES[lang][key]


def to_lang(lang, tlang, key):
    if tlang == lang:
        return FILES[lang][key]
    if lang == "tr":
        return FOLDER[tlang] + "/" + FILES[tlang][key]
    if tlang == "tr":
        return "../" + FILES["tr"][key]
    return "../" + FOLDER[tlang] + "/" + FILES[tlang][key]


def canon(lang, key):
    if key == "home":
        return SITE if lang == "tr" else SITE + lang + "/"
    name = FILES[lang][key]
    return (SITE + name) if lang == "tr" else (SITE + lang + "/" + name)


def ck(lang):
    return ('<svg aria-hidden="true" focusable="false"><use href="'
            + asset(lang, "assets/img/icons.svg") + '#i-check"></use></svg>')


def card(t, d, idx=None):
    tag = f'<span class="card-tag">{e(idx)}</span>' if idx else ""
    return f'<div class="card">{tag}<h3>{e(t)}</h3><p>{e(d)}</p></div>'


def li_check(lang, text):
    return f'<li>{ck(lang)}<span>{e(text)}</span></li>'


def step(t, d):
    return f'<li><div><h3>{e(t)}</h3><p>{e(d)}</p></div></li>'


def faq_item(q, a, open_=False):
    o = " open" if open_ else ""
    return f'<details{o}><summary>{e(q)}</summary><div class="answer"><p>{e(a)}</p></div></details>'


def shot(lang, src, alt, w, h, lazy=True, caption=None):
    l = ' loading="lazy"' if lazy else ""
    cap = ""
    if caption:
        cap = f'<figcaption class="shot-caption"><strong>{e(caption[0])}</strong><span>{e(caption[1])}</span></figcaption>'
    return (f'<figure class="shot"><img src="{asset(lang, "assets/img/" + src)}" '
            f'width="{w}" height="{h}"{l} alt="{e(alt)}">{cap}</figure>')


def showcase(lang):
    t = T[lang]
    tabs = []
    panels = []
    for i, (num, label, img, alt, cap_title, cap_meta) in enumerate(t["shot_tabs"]):
        active = i == 0
        sel = "true" if active else "false"
        tabidx = "0" if active else "-1"
        hid = "" if active else " hidden"
        tid = f"shot-tab-{num}"
        pid = f"shot-panel-{num}"
        tabs.append(
            f'<button class="shot-tab" type="button" role="tab" id="{tid}" '
            f'aria-selected="{sel}" aria-controls="{pid}" tabindex="{tabidx}" '
            f'data-shot-tab="{num}"><span class="num">{e(num)}</span><span>{e(label)}</span></button>'
        )
        panels.append(
            f'<div class="shot-panel" id="{pid}" role="tabpanel" aria-labelledby="{tid}" '
            f'data-shot-panel="{num}"{hid}>'
            f'<figure class="shot"><img src="{asset(lang, "assets/img/" + img)}" '
            f'width="1400" height="875" alt="{e(alt)}">'
            f'<figcaption class="shot-caption"><strong>{e(cap_title)}</strong><span>{e(cap_meta)}</span></figcaption>'
            f'</figure></div>'
        )
    return (
        '<div class="showcase">'
        '<div class="shot-tabs" role="tablist" aria-label="Ayaz DE 4.0">\n          '
        + "\n          ".join(tabs)
        + "\n        </div>\n        "
        + "\n        ".join(panels)
        + "\n      </div>"
    )


def theme_chips(lang):
    chips = []
    for name, bg_hex, acc_hex, desc_tr, desc_en in AYAZ_THEMES:
        desc = desc_tr if lang == "tr" else desc_en
        chips.append(
            f'<div class="theme-chip">'
            f'<div class="theme-preview" style="background:{bg_hex}">'
            f'<span style="font-family:var(--fm);font-size:0.72rem;color:{acc_hex};font-weight:600">{e(bg_hex)}</span>'
            f'<span class="theme-dot" style="background:{acc_hex}"></span>'
            f'</div>'
            f'<strong>{e(name)}</strong>'
            f'<small>{e(desc)}</small>'
            f'</div>'
        )
    return "\n        ".join(chips)


# ------------------------------------------------------------------- json-ld

def jsonld_website(lang):
    return {
        "@context": "https://schema.org", "@type": "WebSite",
        "@id": SITE + "#website", "url": SITE, "name": "Ankora Linux",
        "inLanguage": [INLANG[L] for L in LANGS],
        "publisher": {"@id": SITE + "#org"},
    }


def jsonld_org():
    return {
        "@context": "https://schema.org", "@type": "Organization",
        "@id": SITE + "#org", "name": "Ankora Linux Projesi", "url": SITE,
        "logo": {"@type": "ImageObject", "url": SITE + "assets/img/logo-512.png"},
        "email": MAIL, "sameAs": [REPO, FORUM],
    }


def jsonld_software(lang):
    return {
        "@context": "https://schema.org", "@type": "SoftwareApplication",
        "name": "Ankora Linux", "applicationCategory": "OperatingSystem",
        "operatingSystem": "Linux", "softwareVersion": "4.0.0",
        "inLanguage": INLANG[lang], "isAccessibleForFree": True,
        "license": "https://www.gnu.org/licenses/gpl-3.0.html",
        "downloadUrl": REL, "codeRepository": REPO,
        "author": {"@id": SITE + "#org"},
    }


def jsonld_faq(lang):
    return {
        "@context": "https://schema.org", "@type": "FAQPage",
        "inLanguage": INLANG[lang],
        "mainEntity": [{"@type": "Question", "name": q,
                        "acceptedAnswer": {"@type": "Answer", "text": a}}
                       for q, a in T[lang]["q_qas"]],
    }


def jsonld_breadcrumb(lang, key, label):
    return {
        "@context": "https://schema.org", "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1,
             "name": NAVL[lang]["home"], "item": canon(lang, "home")},
            {"@type": "ListItem", "position": 2, "name": label, "item": canon(lang, key)},
        ],
    }


def block(b):
    return ('<script type="application/ld+json">\n'
            + json.dumps(b, ensure_ascii=False, indent=2) + "\n</script>")


# --------------------------------------------------------------------- iskelet

def head(lang, key, blocks):
    t = T[lang]
    title, desc = t["m_" + key]
    alts = "\n".join(f'<link rel="alternate" hreflang="{L}" href="{canon(L, key)}">'
                     for L in LANGS)
    alts += f'\n<link rel="alternate" hreflang="x-default" href="{canon("tr", key)}">'
    ogalts = "\n".join(f'<meta property="og:locale:alternate" content="{OGLOCALE[L]}">'
                       for L in LANGS if L != lang)
    ld = "\n".join(block(b) for b in blocks)
    return f"""<!doctype html>
<html lang="{lang}" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1">
<meta name="author" content="Ankora Linux Projesi">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e1420" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{canon(lang, key)}">
{alts}
{THEME_SCRIPT}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="{asset(lang, "assets/site.css")}">
<script>document.documentElement.classList.remove('no-js');</script>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ankora Linux">
<meta property="og:locale" content="{OGLOCALE[lang]}">
{ogalts}
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{canon(lang, key)}">
<meta property="og:image" content="{SITE}assets/img/ayaz-masaustu.png">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="875">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{e(title)}">
<meta name="twitter:description" content="{e(desc)}">
<meta name="twitter:image" content="{SITE}assets/img/ayaz-masaustu.png">
<link rel="icon" href="{asset(lang, "assets/img/favicon.svg")}" type="image/svg+xml">
<link rel="apple-touch-icon" href="{asset(lang, "assets/img/apple-touch-icon.png")}">
<link rel="manifest" href="{asset(lang, "site.webmanifest")}">
{ld}
</head>
<body>"""


def langmenu(lang, key):
    u = U[lang]
    icons = asset(lang, "assets/img/icons.svg")
    opts = "".join(
        f'\n            <li><a href="{to_lang(lang, L, key)}" hreflang="{L}" lang="{L}"'
        + (' aria-current="true"' if L == lang else "")
        + f'>{e(LANGNAME[L])}</a></li>' for L in LANGS)
    return f"""
    <details class="langmenu">
      <summary aria-label="{e(u['language'])}" title="{e(u['language'])}">
        <svg aria-hidden="true" focusable="false"><use href="{icons}#i-globe"></use></svg>
        <span>{CODELABEL[lang]}</span>
      </summary>
      <ul class="menu">{opts}
      </ul>
    </details>"""


def tools(lang, key):
    u = U[lang]
    icons = asset(lang, "assets/img/icons.svg")
    themes = "".join(
        f'<button class="tset" type="button" data-set-theme="{v}" aria-pressed="false">{e(lbl)}</button>'
        for v, lbl in (("light", u["tLight"]), ("dark", u["tDark"]), ("auto", u["tAuto"])))
    accents = "".join(
        f'<button class="swatch swatch-{v}" type="button" data-set-accent="{v}" aria-pressed="false" aria-label="{e(lbl)}" title="{e(lbl)}"></button>'
        for v, lbl in (("blue", u["aBlue"]), ("green", u["aGreen"]), ("purple", u["aPurple"])))
    return f"""
    <div class="tools">
      <button class="tbtn" type="button" data-theme-btn aria-expanded="false" aria-controls="theme-panel" aria-label="{e(u['settings'])}" title="{e(u['settings'])}">
        <svg aria-hidden="true" focusable="false"><use href="{icons}#i-moon"></use></svg>
      </button>
      <div class="tpanel" id="theme-panel" hidden>
        <div class="grp">
          <h4>{e(u['theme'])}</h4>
          <div class="trow">{themes}</div>
        </div>
        <div class="grp">
          <h4>{e(u['accent'])}</h4>
          <div class="trow">{accents}</div>
        </div>
      </div>
    </div>"""


def header(lang, key):
    u = U[lang]
    n = NAVL[lang]
    icons = asset(lang, "assets/img/icons.svg")
    links = "".join(
        f'\n          <li><a href="{local(lang, k)}"'
        + (' aria-current="page"' if k == key else "") + f'>{e(n[k])}</a></li>'
        for k in NAVORDER)
    sheet = "".join(f'\n          <li><a href="{local(lang, k)}">{e(n[k])}</a></li>'
                    for k in NAVORDER)
    sheet += f'\n          <li><a href="{local(lang, "install")}">{e(u["download"])}</a></li>'
    sheet += f'\n          <li><a href="{local(lang, "faq")}">{e(n["faq"])}</a></li>'
    return f"""
<a class="skip" href="#main">{e(u["skip"])}</a>

<div class="bayram">{e(u["bayram"])}</div>

<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="{local(lang, "home")}">
      <img src="{asset(lang, "assets/img/logo-128.png")}" width="32" height="32" alt="Ankora Linux">
      <span>{e(u["brand"])}</span>
    </a>
    <nav class="nav" aria-label="{e(u["nav"])}">
      <ul>{links}
      </ul>
    </nav>
    <a class="btn btn-1 head-cta" href="{local(lang, "install")}">{e(u["download"])}</a>{langmenu(lang, key)}{tools(lang, key)}
    <button class="menu-btn" type="button" data-menu-btn aria-expanded="false"
            aria-controls="menu-sheet" aria-label="{e(u["menu"])}">
      <svg aria-hidden="true" focusable="false"><use href="{icons}#i-menu"></use></svg>
    </button>
  </div>
  <div class="sheet" id="menu-sheet">
    <nav class="wrap" aria-label="{e(u["navm"])}">
      <ul>{sheet}
      </ul>
    </nav>
  </div>
</header>"""


def footer(lang):
    u = U[lang]
    n = NAVL[lang]
    f = FOOTL[lang]
    dist = [(local(lang, "features"), n["features"]), (local(lang, "install"), u["download"]),
            (local(lang, "security"), n["security"]), (local(lang, "changelog"), n["changelog"])]
    help_ = [(local(lang, "faq"), n["faq"]), (local(lang, "contact"), n["contact"]),
             (FORUM, f["forum"])]
    src = [(REPO, f["repo"]), (REL, f["rel"]), (LICENSE, f["lic"])]

    icons = asset(lang, "assets/img/icons.svg")
    soc = [("https://www.instagram.com/ankoralinux/", "Instagram", "i-instagram"),
           ("https://x.com/ankoralinux", "X", "i-x"),
           ("https://www.youtube.com/@AnkoraLinux", "YouTube", "i-youtube")]

    def col(title, items):
        li = "".join(
            f'\n          <li><a href="{href}"{" rel=\"noopener\"" if href.startswith("http") else ""}>{e(lbl)}</a></li>'
            for href, lbl in items)
        return f'\n      <div>\n        <h2>{e(title)}</h2>\n        <ul>{li}\n        </ul>\n      </div>'

    return f"""
<footer class="foot">
  <div class="wrap">
    <div class="foot-cols">
      <div class="foot-about">
        <a class="brand" href="{local(lang, "home")}">
          <img src="{asset(lang, "assets/img/logo-128.png")}" width="32" height="32" alt="Ankora Linux">
          <span>{e(u["brand"])}</span>
        </a>
        <p>{e(u["about"])}</p>
        <div class="soc">{"\n          ".join(
            f'<a href="{href}" rel="noopener" aria-label="{lbl}" title="{lbl}">'
            f'<svg aria-hidden="true" focusable="false"><use href="{icons}#{sym}"></use></svg></a>'
            for href, lbl, sym in soc)}
        </div>
      </div>{col(u["c1"], dist)}{col(u["c2"], help_)}{col(u["c3"], src)}
    </div>
    <div class="foot-bar">
      <span>{e(u["short"])}</span>
      <span><a href="{asset(lang, "sitemap.xml")}">{e(u["sitemap"])}</a></span>
    </div>
  </div>
</footer>

<script src="{asset(lang, "assets/site.js")}" defer></script>
</body>
</html>
"""


# -------------------------------------------------------------------- sayfalar

def home(lang):
    t = T[lang]
    u = U[lang]
    hm = t["hero_meta"]
    spec_cells = "\n        ".join(
        f'<div class="spec-cell"><span class="spec-val">{e(val)}</span><span class="spec-lbl">{e(lbl)}</span></div>'
        for val, lbl in t["specs"]
    )
    c0_title, c0_desc = t["cards3"][0]
    c1_title, c1_desc = t["cards3"][1]
    c2_title, c2_desc = t["cards3"][2]
    inside = "\n            ".join(li_check(lang, x) for x in t["inside"])
    steps = "\n        ".join(step(a, b) for a, b in t["steps3"])
    faq = "\n        ".join(faq_item(q, a, i == 0) for i, (q, a) in enumerate(t["faq4"]))
    cmp_rows = "\n        ".join(
        f'<tr{" data-self=\"true\"" if i == 0 else ""}><td>{e(nm)}</td><td>{e(val)}</td></tr>'
        for i, (nm, val) in enumerate(t["cmp_rows"]))
    return f"""
<main id="main">
  <section class="section">
    <div class="wrap">
      <div class="section-head center">
        <div class="hero-meta">
          <strong>{e(hm[0])}</strong>
          <span class="sep">·</span>
          <span>{e(hm[1])}</span>
          <span class="sep">·</span>
          <span>{e(hm[2])}</span>
          <span class="sep">·</span>
          <span>{e(hm[3])}</span>
        </div>
        <h1>{e(t["h1"])}</h1>
        <p class="lede" style="margin-inline:auto">{e(t["lede"])}</p>
        <div class="btn-row" style="justify-content:center;margin-top:30px">
          <a class="btn btn-1" href="{local(lang, "install")}">{e(u["download"])}</a>
          <a class="btn btn-2" href="{local(lang, "features")}">{e(NAVL[lang]["features"])}</a>
        </div>
      </div>
      {showcase(lang)}
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["why_eyebrow"])}</span>
        <h2>{e(t["why_h2"])}</h2>
      </div>
      <div class="spec-strip">
        {spec_cells}
      </div>
      <div class="arch-grid">
        <div class="arch-lead">
          <div>
            <span class="card-tag">01 · AYAZ DE 3.6</span>
            <h3>{e(c0_title)}</h3>
            <p>{e(c0_desc)}</p>
          </div>
          <div class="arch-meta">
            <span>Tauri 1.5 + Rust</span>
            <span>·</span>
            <span>WebKitGTK</span>
            <span>·</span>
            <span>SysVinit PID 1</span>
            <span>·</span>
            <span>Linux 6.1 LTS</span>
          </div>
        </div>
        <div class="arch-side">
          {card(c1_title, c1_desc, "02 · YEREL DENEYİM")}
          {card(c2_title, c2_desc, "03 · KURULUM & BAKIM")}
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <span class="eyebrow">{e(t["inside_eyebrow"])}</span>
          <h2>{e(t["inside_h2"])}</h2>
          <p class="lede">{e(t["inside_lede"])}</p>
          <ul class="checklist" style="margin-top:26px">
            {inside}
          </ul>
        </div>
        {shot(lang, "ankora-karsilayici.jpg", t["inside_alt"], 1400, 875)}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["cmp_eyebrow"])}</span>
        <h2>{e(t["cmp_h2"])}</h2>
        <p class="lede">{e(t["cmp_lede"])}</p>
      </div>
      <div class="cmp-wrap">
        <table class="cmp">
          <thead>
            <tr><th scope="col">{e(t["cmp_head"][0])}</th><th scope="col">{e(t["cmp_head"][1])}</th></tr>
          </thead>
          <tbody>
          {cmp_rows}
          </tbody>
        </table>
      </div>
      <p class="cmp-note">{e(t["cmp_note"])}</p>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["step_eyebrow"])}</span>
        <h2>{e(t["step_h2"])}</h2>
      </div>
      <ol class="steps">
        {steps}
      </ol>
      <div class="btn-row" style="margin-top:40px"><a class="btn btn-1" href="{local(lang, "install")}">{e(u["download"])}</a></div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head center">
        <span class="eyebrow">{e(t["faq_eyebrow"])}</span>
        <h2>{e(t["faq_h2"])}</h2>
      </div>
      <div class="faq" style="margin-inline:auto">
        {faq}
      </div>
      <p style="text-align:center;margin-top:40px"><a class="btn btn-2" href="{local(lang, "faq")}">{e(t["all_q"])}</a></p>
    </div>
  </section>
</main>"""


def features(lang):
    t = T[lang]
    u = U[lang]
    cards = "\n        ".join(card(a, b, f"0{i + 1}") for i, (a, b) in enumerate(t["f_cards"]))
    apps = "\n            ".join(li_check(lang, x) for x in t["f_apps"])
    shot_themes = t["shot_tabs"][1]
    shot_ai = t["shot_tabs"][4]
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["f_h1"])}</h1>
      <p class="lede">{e(t["f_lede"])}</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["f_hl_eyebrow"])}</span>
        <h2>{e(t["f_hl_h2"])}</h2>
      </div>
      <div class="grid">
        {cards}
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["f_themes_eyebrow"])}</span>
        <h2>{e(t["f_themes_h2"])}</h2>
        <p class="lede">{e(t["f_themes_lede"])}</p>
      </div>
      <div class="theme-grid">
        {theme_chips(lang)}
      </div>
      <div class="gallery-grid">
        {shot(lang, shot_themes[2], shot_themes[3], 1400, 875, caption=(shot_themes[4], shot_themes[5]))}
        {shot(lang, shot_ai[2], shot_ai[3], 1400, 875, caption=(shot_ai[4], shot_ai[5]))}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <span class="eyebrow">{e(t["f_apps_eyebrow"])}</span>
          <h2>{e(t["f_apps_h2"])}</h2>
          <p class="lede">{e(t["f_apps_lede"])}</p>
          <ul class="checklist" style="margin-top:26px">
            {apps}
          </ul>
        </div>
        {shot(lang, "ankora-duvar.jpg", t["f_apps_alt"], 1400, 875)}
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head center">
        <h2>{e(t["f_cta_h2"])}</h2>
        <p class="lede" style="margin-inline:auto">{e(t["f_cta_lede"])}</p>
        <div class="btn-row" style="justify-content:center;margin-top:30px">
          <a class="btn btn-1" href="{local(lang, "install")}">{e(u["download"])}</a>
        </div>
      </div>
    </div>
  </section>
</main>"""


def install(lang):
    t = T[lang]
    u = U[lang]
    req = "\n        ".join(li_check(lang, x) for x in t["i_req"])
    steps = "\n        ".join(step(a, b) for a, b in t["i_steps"])
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["i_h1"])}</h1>
      <p class="lede">{e(t["i_lede"])}</p>
      <div class="btn-row" style="margin-top:30px">
        <a class="btn btn-1" href="{REL}" rel="noopener">{e(t["i_dl"])}</a>
        <a class="btn btn-2" href="{REPO}" rel="noopener">{e(t["i_src"])}</a>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["i_req_eyebrow"])}</span>
        <h2>{e(t["i_req_h2"])}</h2>
      </div>
      <ul class="checklist">
        {req}
      </ul>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["i_step_eyebrow"])}</span>
        <h2>{e(t["i_step_h2"])}</h2>
      </div>
      <ol class="steps">
        {steps}
      </ol>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["i_cli_eyebrow"])}</span>
        <h2>{e(t["i_cli_h2"])}</h2>
      </div>
      <div class="code">
        <pre><code>{e(CODE)}</code></pre>
        <button class="copy" type="button" data-copy data-done="{e(u["copied"])}">{e(u["copy"])}</button>
      </div>
      <div class="note">
        <b>{e(t["i_note_b"])}</b>
        <p>{e(t["i_note_p"])}</p>
      </div>
    </div>
  </section>
</main>"""


def security(lang):
    t = T[lang]
    cards = "\n        ".join(card(a, b, f"0{i + 1}") for i, (a, b) in enumerate(t["s_cards"]))
    notes = "\n        ".join(li_check(lang, x) for x in t["s_notes"])
    vuln = t["s_vuln"].format(mail=f'<a href="mailto:{SECMAIL}">{SECMAIL}</a>')
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["s_h1"])}</h1>
      <p class="lede">{e(t["s_lede"])}</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["s_core_eyebrow"])}</span>
        <h2>{e(t["s_core_h2"])}</h2>
      </div>
      <div class="grid">
        {cards}
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["s_tech_eyebrow"])}</span>
        <h2>{e(t["s_tech_h2"])}</h2>
      </div>
      <ul class="checklist">
        {notes}
      </ul>
      <p style="margin-top:36px">{vuln}</p>
    </div>
  </section>
</main>"""


def changelog(lang):
    t = T[lang]
    rows = "\n        ".join(
        f'<li><a href="{REL}" rel="noopener"><span><b>{e(v)} · {e(nm)}</b><small>{e(d)}</small></span>'
        f'<span class="go">{e(t["row_go"])}</span></a></li>'
        for v, nm, d in t["c_rows"])
    foot = t["c_foot"]
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["c_h1"])}</h1>
      <p class="lede">{e(t["c_lede"])}</p>
      <div class="btn-row" style="margin-top:30px">
        <a class="btn btn-1" href="{REL}" rel="noopener">{e(t["c_dl"])}</a>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <ul class="rows">
        {rows}
      </ul>
      <p style="margin-top:36px">{e(foot)} <a href="{REL}" rel="noopener">GitHub</a>.</p>
    </div>
  </section>
</main>"""


def faq(lang):
    t = T[lang]
    items = "\n        ".join(faq_item(q, a, i == 0) for i, (q, a) in enumerate(t["q_qas"]))
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["q_h1"])}</h1>
      <p class="lede">{e(t["q_lede"])} <a href="{local(lang, "contact")}">{e(NAVL[lang]["contact"])}</a>.</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="faq">
        {items}
      </div>
      <div class="btn-row" style="margin-top:48px">
        <a class="btn btn-1" href="{FORUM}" rel="noopener">{e(t["q_forum"])}</a>
        <a class="btn btn-2" href="{local(lang, "contact")}">{e(t["q_contact"])}</a>
      </div>
    </div>
  </section>
</main>"""


def contact(lang):
    t = T[lang]
    urls = [FORUM, f"mailto:{MAIL}", ISSUES, f"mailto:{SECMAIL}"]
    rows = "\n        ".join(
        f'<li><a href="{urls[i]}"{" rel=\"noopener\"" if urls[i].startswith("http") else ""}>'
        f'<span><b>{e(nm)}</b><small>{e(sub)}</small></span>'
        f'<span class="go">{e(go)}</span></a></li>'
        for i, (nm, sub, go) in enumerate(t["k_rows"]))
    items = "\n        ".join(li_check(lang, x) for x in t["k_items"])
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["k_h1"])}</h1>
      <p class="lede">{e(t["k_lede"])}</p>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <ul class="rows">
        {rows}
      </ul>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <span class="eyebrow">{e(t["k_bug_eyebrow"])}</span>
        <h2>{e(t["k_bug_h2"])}</h2>
      </div>
      <ul class="checklist">
        {items}
      </ul>
    </div>
  </section>
</main>"""


CONTENT = {"home": home, "features": features, "install": install,
           "security": security, "changelog": changelog, "faq": faq, "contact": contact}


def render(lang, key):
    blocks = [jsonld_breadcrumb(lang, key, NAVL[lang].get(key, key))]
    if key == "home":
        blocks = [jsonld_website(lang), jsonld_org(), jsonld_software(lang), jsonld_faq(lang)]
    elif key == "faq":
        blocks = [jsonld_breadcrumb(lang, key, NAVL[lang]["faq"]), jsonld_faq(lang)]
    return head(lang, key, blocks) + header(lang, key) + CONTENT[key](lang) + footer(lang)


def page404():
    u = U["tr"]
    key = "home"
    icons = "assets/img/icons.svg"
    ld = block(jsonld_website("tr"))
    return f"""<!doctype html>
<html lang="tr" class="no-js">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Sayfa bulunamadı · Ankora Linux</title>
<meta name="description" content="Aradığınız sayfa bulunamadı. Ankora Linux ana sayfası, özellikler, indirme, güvenlik ve iletişim bağlantıları burada.">
<meta name="robots" content="noindex, follow">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#ffffff" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#0e1420" media="(prefers-color-scheme: dark)">
<base href="/">
<link rel="canonical" href="{SITE}404.html">
{THEME_SCRIPT}
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Sora:wght@600;700;800&family=IBM+Plex+Sans:wght@400;500;600&family=IBM+Plex+Mono:wght@400;500&display=swap">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.remove('no-js');</script>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ankora Linux">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="Sayfa bulunamadı · Ankora Linux">
<meta property="og:description" content="Aradığınız sayfa bulunamadı.">
<meta property="og:image" content="{SITE}assets/img/ayaz-masaustu.png">
<meta property="og:image:width" content="1400">
<meta property="og:image:height" content="875">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="assets/img/apple-touch-icon.png">
<link rel="manifest" href="site.webmanifest">
{ld}
</head>
<body>

<a class="skip" href="#main">{e(u["skip"])}</a>

<header class="site-head">
  <div class="wrap head-in">
    <a class="brand" href="./">
      <img src="assets/img/logo-128.png" width="32" height="32" alt="Ankora Linux">
      <span>{e(u["brand"])}</span>
    </a>
    <nav class="nav" aria-label="{e(u["nav"])}">
      <ul>
        <li><a href="./">{e(NAVL["tr"]["home"])}</a></li>
        <li><a href="{FILES["tr"]["features"]}">{e(NAVL["tr"]["features"])}</a></li>
        <li><a href="{FILES["tr"]["security"]}">{e(NAVL["tr"]["security"])}</a></li>
        <li><a href="{FILES["tr"]["changelog"]}">{e(NAVL["tr"]["changelog"])}</a></li>
        <li><a href="{FILES["tr"]["contact"]}">{e(NAVL["tr"]["contact"])}</a></li>
      </ul>
    </nav>
    <a class="btn btn-1 head-cta" href="{FILES["tr"]["install"]}">{e(u["download"])}</a>{langmenu("tr", key)}{tools("tr", key)}
    <button class="menu-btn" type="button" data-menu-btn aria-expanded="false"
            aria-controls="menu-sheet" aria-label="{e(u["menu"])}">
      <svg aria-hidden="true" focusable="false"><use href="{icons}#i-menu"></use></svg>
    </button>
  </div>
  <div class="sheet" id="menu-sheet">
    <nav class="wrap" aria-label="{e(u["navm"])}">
      <ul>
        <li><a href="./">{e(NAVL["tr"]["home"])}</a></li>
        <li><a href="{FILES["tr"]["features"]}">{e(NAVL["tr"]["features"])}</a></li>
        <li><a href="{FILES["tr"]["security"]}">{e(NAVL["tr"]["security"])}</a></li>
        <li><a href="{FILES["tr"]["changelog"]}">{e(NAVL["tr"]["changelog"])}</a></li>
        <li><a href="{FILES["tr"]["contact"]}">{e(NAVL["tr"]["contact"])}</a></li>
        <li><a href="{FILES["tr"]["install"]}">{e(u["download"])}</a></li>
        <li><a href="{FILES["tr"]["faq"]}">{e(NAVL["tr"]["faq"])}</a></li>
      </ul>
    </nav>
  </div>
</header>

<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>Bu sayfa yok</h1>
      <p class="lede">Adres yanlış yazılmış ya da sayfa taşınmış olabilir. Aşağıdaki bağlantılardan devam edebilirsiniz.</p>
    </div>
  </div>
  <section class="section">
    <div class="wrap">
      <ul class="rows">
        <li><a href="./"><span><b>{e(NAVL["tr"]["home"])}</b><small>Genel bakış ve indirme bağlantıları</small></span><span class="go">index</span></a></li>
        <li><a href="{FILES["tr"]["features"]}"><span><b>{e(NAVL["tr"]["features"])}</b><small>Hazır uygulamalar ve sistem</small></span><span class="go">ozellikler</span></a></li>
        <li><a href="{FILES["tr"]["install"]}"><span><b>{e(u["download"])}</b><small>ISO, USB bellek ve adım adım kurulum</small></span><span class="go">kurulum</span></a></li>
        <li><a href="{FILES["tr"]["security"]}"><span><b>{e(NAVL["tr"]["security"])}</b><small>Sizi neyden korur, nasıl</small></span><span class="go">guvenlik</span></a></li>
        <li><a href="{FILES["tr"]["faq"]}"><span><b>{e(NAVL["tr"]["faq"])}</b><small>Merak edilenler ve yanıtları</small></span><span class="go">sss</span></a></li>
        <li><a href="{FILES["tr"]["contact"]}"><span><b>{e(NAVL["tr"]["contact"])}</b><small>Forum, hata bildirimi, güvenlik bildirimi</small></span><span class="go">iletisim</span></a></li>
      </ul>
      <div class="btn-row" style="margin-top:48px">
        <a class="btn btn-1" href="{FORUM}" rel="noopener">Ankora Lab forumu</a>
        <a class="btn btn-2" href="{FILES["tr"]["install"]}">{e(u["download"])}</a>
      </div>
    </div>
  </section>
</main>

{footer("tr")}"""


def sitemap():
    prio = {"home": "1.0", "features": "0.9", "install": "0.9", "security": "0.8",
            "changelog": "0.7", "faq": "0.8", "contact": "0.6"}
    freq = {"changelog": "monthly"}
    out = ['<?xml version="1.0" encoding="UTF-8"?>',
           '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"',
           '        xmlns:xhtml="http://www.w3.org/1999/xhtml">']
    for key in KEYS:
        for lang in LANGS:
            out.append("  <url>")
            out.append(f"    <loc>{canon(lang, key)}</loc>")
            for L in LANGS:
                out.append(f'    <xhtml:link rel="alternate" hreflang="{L}" href="{canon(L, key)}"/>')
            out.append(f'    <xhtml:link rel="alternate" hreflang="x-default" href="{canon("tr", key)}"/>')
            out.append(f"    <changefreq>{freq.get(key, 'monthly')}</changefreq>")
            out.append(f"    <priority>{prio[key]}</priority>")
            out.append("  </url>")
    out.append("</urlset>")
    return "\n".join(out) + "\n"


def robots():
    return f"User-agent: *\nAllow: /\n\nSitemap: {SITE}sitemap.xml\n"


def llms():
    pages_tr = "\n".join(f"- [{T['tr']['m_' + k][0]}]({canon('tr', k)})" for k in KEYS)
    pages_en = "\n".join(f"- [{T['en']['m_' + k][0]}]({canon('en', k)})" for k in KEYS)
    langs = ", ".join(CODELABEL[L] for L in LANGS)
    return f"""# Ankora Linux

> Ankora Linux 4.0, son kullanıcı ve eğitim kurumları için sade, Devuan 5.0 Daedalus
> (SysVinit) tabanlı ve ücretsiz bir Türkçe işletim sistemidir. Kendi masaüstü ortamı
> Ayaz DE 4.0 ile birlikte gelir. GPL-3.0 lisanslıdır.
> Depo: {REPO}
> Sürümler: {REL}
> Forum: {FORUM}
> Güvenlik: {SECMAIL}
> Diller: {langs}
> Tema: açık ve koyu; üç vurgu rengi (mavi, yeşil, mor).

## Ne işe yarar

Hedef, son kullanıcı için sade bir dağıtım: 18 yerleşik pencere, 278 paketli
yazılım mağazası (ETAP akıllı tahta araçları dahil), 14 tam sistem teması,
4 GB altı makineler için otomatik Eco RAM kipi, yerel Ollama destekli Ankora AI
asistanı ve Türkçe arayüz. Kurulu sistemde masaüstü boştayken yaklaşık 750 MB
bellek kullanır.

## Kurulum

1. {REL} adresinden ISO dosyasını ve yanındaki SHA-256 doğrulama dosyasını indirin.
2. ISO'yu boş bir USB belleğe yazın.
3. Bilgisayarı USB bellekten başlatıp kurulum sihirbazını izleyin.

## Sürümler

- 01.0 (2024): ilk kararlı sürüm
- 02.0 Zümrüt (2025): masaüstü entegrasyonları ve ayarlar yenilendi
- 2.0 (2026): masaüstü ortamı Ayaz DE
- 3.0 (2026): Tauri 1.5 ve Rust çekirdeği
- 3.5 (2026): Eco RAM kipi ve otomatik USB bağlama
- 3.6 (2026): 14 tam sistem teması, 278 mağaza paketi, gelişmiş Dosyalar yöneticisi, USB/ISO yazıcı ve ETAP desteği

## Sayfalar (Türkçe)

{pages_tr}

## Pages (English)

{pages_en}

## Lisans

GNU General Public License v3.0. Değiştirilmiş sürümler aynı lisansla
dağıtılmalıdır. Tam metin depodaki LICENSE dosyasındadır.
"""


def webmanifest():
    return json.dumps({
        "name": "Ankora Linux 4.0", "short_name": "Ankora",
        "description": "Devuan tabanlı ücretsiz ve Türkçe işletim sistemi, Ayaz DE 4.0 masaüstü ortamı ile.",
        "lang": "tr", "dir": "ltr", "start_url": "./", "scope": "./", "id": "./",
        "display": "browser", "orientation": "any",
        "background_color": "#ffffff", "theme_color": "#ffffff",
        "categories": ["os", "utilities"],
        "icons": [
            {"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"},
            {"src": "assets/img/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
            {"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "maskable"},
        ],
    }, ensure_ascii=False, indent=2) + "\n"


def build():
    (ROOT / "404.html").write_text(page404(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(robots(), encoding="utf-8")
    (ROOT / "llms.txt").write_text(llms(), encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(webmanifest(), encoding="utf-8")
    print("yazıldı: 404.html, sitemap.xml, robots.txt, llms.txt, site.webmanifest")
    for lang in LANGS:
        for key in KEYS:
            out = render(lang, key)
            path = ROOT / (FILES[lang][key] if lang == "tr"
                           else lang + "/" + FILES[lang][key])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(out, encoding="utf-8")
            print("yazıldı:", path.relative_to(ROOT))


if __name__ == "__main__":
    build()
