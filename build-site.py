#!/usr/bin/env python3
"""Ankora Linux 5.0 web sitesini uretir.

Bes dil (tr, en, de, es, ru), dort yuz temasi (Bostan, Bakir, Civata, Arduvaz)
ve yedi ana sayfa ile SEO/denetim dosyalarini olusturur.
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
OGLOCALE = {"tr": "tr_TR", "en": "en_US", "de": "de_DE", "es": "es_ES", "ru": "ru_RU"}
INLANG = {"tr": "tr-TR", "en": "en-US", "de": "de-DE", "es": "es-ES", "ru": "ru-RU"}
CODELABEL = {"tr": "TR", "en": "EN", "de": "DE", "es": "ES", "ru": "RU"}
LANGNAME = {"tr": "Türkçe", "en": "English", "de": "Deutsch", "es": "Español", "ru": "Русский"}

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

FONT_CSS = (
    "https://fonts.googleapis.com/css2?"
    "family=Onest:wght@500;600;700&"
    "family=IBM+Plex+Sans:wght@400;500;600&"
    "family=IBM+Plex+Mono:wght@400;500&display=swap"
)

THEME_SCRIPT = (
    "<script>(function(){var r=document.documentElement;"
    "function g(k){var v=null;try{v=localStorage.getItem(k)}catch(e){}"
    "if(!v){var m=(document.cookie||'').match(new RegExp('(?:^|; )'+k+'=([^;]*)'));"
    "if(m){try{v=decodeURIComponent(m[1])}catch(e){v=m[1]}}}return v}"
    "var t=g('ankora-theme')||'bostan';"
    "if(t==='light')t='bostan';if(t==='dark')t='bakir';"
    "if(['bostan','bakir','civata','arduvaz','auto'].indexOf(t)<0)t='bostan';"
    "r.dataset.themePref=t;"
    "r.dataset.theme=(t==='auto'?(matchMedia('(prefers-color-scheme:dark)').matches?'bakir':'bostan'):t);})();</script>"
)

U = {
    "tr": {"settings": "Yüz / Tema", "language": "Dil", "theme": "Site ve Masaüstü Yüzü",
           "tBostan": "Bostan", "tBakir": "Bakır", "tCivata": "Cıvata", "tArduvaz": "Arduvaz", "tAuto": "Sistem",
           "download": "İndir", "skip": "İçeriğe geç", "menu": "Menüyü aç",
           "nav": "Ana gezinme", "navm": "Ana gezinme (mobil)", "brand": "Ankora Linux",
           "copy": "Kopyala", "copied": "Kopyalandı",
           "about": "Devuan 6 Excalibur ve Linux 6.12 LTS üzerinde AyazDE 5.0 masaüstü ile gelen Türkçe dağıtım.",
           "c1": "Dağıtım", "c2": "Yardım", "c3": "Kaynak",
           "short": "Ankora Linux 5.0 (GPL-3.0)", "sitemap": "Site haritası"},
    "en": {"settings": "Face / Theme", "language": "Language", "theme": "Site & Desktop Face",
           "tBostan": "Bostan", "tBakir": "Bakır", "tCivata": "Cıvata", "tArduvaz": "Arduvaz", "tAuto": "System",
           "download": "Download", "skip": "Skip to content", "menu": "Open menu",
           "nav": "Main navigation", "navm": "Main navigation (mobile)", "brand": "Ankora Linux",
           "copy": "Copy", "copied": "Copied",
           "about": "Turkish desktop distribution built on Devuan 6 Excalibur, Linux 6.12 LTS, and AyazDE 5.0.",
           "c1": "Distribution", "c2": "Help", "c3": "Source",
           "short": "Ankora Linux 5.0 (GPL-3.0)", "sitemap": "Sitemap"},
    "de": {"settings": "Design / Fläche", "language": "Sprache", "theme": "Site- & Desktop-Fläche",
           "tBostan": "Bostan", "tBakir": "Bakır", "tCivata": "Cıvata", "tArduvaz": "Arduvaz", "tAuto": "System",
           "download": "Herunterladen", "skip": "Zum Inhalt springen", "menu": "Menü öffnen",
           "nav": "Hauptnavigation", "navm": "Hauptnavigation (mobil)", "brand": "Ankora Linux",
           "copy": "Kopieren", "copied": "Kopiert",
           "about": "Türkische Desktop-Distribution auf Devuan 6 Excalibur, Linux 6.12 LTS und AyazDE 5.0.",
           "c1": "Distribution", "c2": "Hilfe", "c3": "Quellcode",
           "short": "Ankora Linux 5.0 (GPL-3.0)", "sitemap": "Sitemap"},
    "es": {"settings": "Estilo / Tema", "language": "Idioma", "theme": "Estilo del sitio y escritorio",
           "tBostan": "Bostan", "tBakir": "Bakır", "tCivata": "Cıvata", "tArduvaz": "Arduvaz", "tAuto": "Sistema",
           "download": "Descargar", "skip": "Ir al contenido", "menu": "Abrir el menú",
           "nav": "Navegación principal", "navm": "Navegación principal (móvil)", "brand": "Ankora Linux",
           "copy": "Copiar", "copied": "Copiado",
           "about": "Distribución turca basada en Devuan 6 Excalibur, Linux 6.12 LTS y AyazDE 5.0.",
           "c1": "Distribución", "c2": "Ayuda", "c3": "Código",
           "short": "Ankora Linux 5.0 (GPL-3.0)", "sitemap": "Mapa del sitio"},
    "ru": {"settings": "Облик / Тема", "language": "Язык", "theme": "Облик сайта и среды",
           "tBostan": "Bostan", "tBakir": "Bakır", "tCivata": "Cıvata", "tArduvaz": "Arduvaz", "tAuto": "Система",
           "download": "Скачать", "skip": "Перейти к содержимому", "menu": "Открыть меню",
           "nav": "Основная навигация", "navm": "Основная навигация (моб.)", "brand": "Ankora Linux",
           "copy": "Копировать", "copied": "Скопировано",
           "about": "Турецкий дистрибутив на Devuan 6 Excalibur, Linux 6.12 LTS и AyazDE 5.0.",
           "c1": "Дистрибутив", "c2": "Помощь", "c3": "Код",
           "short": "Ankora Linux 5.0 (GPL-3.0)", "sitemap": "Карта сайта"},
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

CORE_FACES = [
    ("bostan", "Yüz 3: Bostan", "Varsayılan keten adaçayı", "Default sage linen palette", "sw-bostan"),
    ("bakir", "Yüz 2: Bakır", "Koyu grafit ve sıcak bakır", "Warm graphite and copper", "sw-bakir"),
    ("civata", "Yüz 8: Cıvata", "Teknik çizim kâğıdı, mavi vurgu", "Drafting paper and blueprint ink", "sw-civata"),
    ("arduvaz", "Yüz 1: Arduvaz", "Sol hizalı koyu mat, terakota", "Left-dock slate with terracotta", "sw-arduvaz"),
]

THEME_NAMES_24 = [
    "Nordik Açık", "Modern Grafit", "Derin Gece", "Kuzey Fjordu", "Çam Ormanı", "Kor Ateşi",
    "Arktik Serinlik", "Çınar", "Meltem", "Kor", "Dem", "Boğaz", "Ayna", "Cumhuriyet",
    "Matbaa", "Bakır", "Bostan", "Hat", "Konsol", "Kesit", "Fener", "Cıvata", "Mina", "Meridyen"
]

SAMPLE_PACKAGES = [
    ("Fatih Kalem 2", "fatihkalem", "Eğitim", "Resmî Ankora"),
    ("ETA Dokunmatik", "eta-touchdrv", "Tahta", "Resmî Ankora"),
    ("MEB Sertifikası", "meb-cert", "Okul", "Resmî Ankora"),
    ("LibreOffice", "libreoffice", "Ofis", "APT"),
    ("VS Code", "com.visualstudio.code", "Geliştirici", "Flathub"),
    ("VLC", "vlc", "Medya", "APT"),
]

T = {
    "tr": {
        "m_home": ("Ankora Linux 5.0: Sakin, systemd’siz Türkçe masaüstü",
                   "Ankora Linux 5.0; Devuan 6 Excalibur ve Linux 6.12 LTS üzerinde AyazDE 5.0, dört masaüstü yüzü, beyaz liste denetimli Ankora AI ve 559 paketli mağaza ile gelir."),
        "m_features": ("Özellikler: Ankora Linux 5.0",
                       "AyazDE 5.0 özellikleri: Bostan, Bakır, Cıvata, Arduvaz yüzleri, her yüze uyumlu Ankora AI balonu, 559 paketli mağaza ve FAZ 1/2/3 okul desteği."),
        "m_install": ("İndir ve kur: Ankora Linux 5.0",
                      "Ankora Linux 5.0 kurulumu: temiz ISO yazdırma, 4.7.x sistemlerden .deb ile sürüm içi yükseltme ve yerel Ollama AI kurulumu."),
        "m_security": ("Güvenlik: Ankora Linux 5.0",
                       "Rust çekirdek güvenliği: 33 sabit izinli komut, 59 yasaklı ikili, tek kullanımlık jetonlu 18 AI eylemi, pkexec ve WebKit bwrap sandbox."),
        "m_changelog": ("Sürümler: Ankora Linux 5.0",
                        "Ankora Linux 01.0’dan 5.0.0’a kadar tüm sürümler ve yenilikler."),
        "m_faq": ("Sık sorulan sorular: Ankora Linux 5.0",
                  "Ankora Linux 5.0 hakkında sık sorulan sorular: donanım, ZRAM, 4.7’den yükseltme, AI güvenliği ve katkı."),
        "m_contact": ("İletişim: Ankora Linux",
                      "Ankora Linux topluluğu: Ankora Lab forumu, e-posta, GitHub hata bildirimi ve güvenlik kanalları."),
        "hero_meta": ("Ankora Linux 5.0.0", "AyazDE 5.0", "Devuan 6 Excalibur", "Linux 6.12 LTS", "~750 MB RAM"),
        "h1": "Sakin, systemd’siz Türkçe masaüstü.",
        "lede": "Devuan 6 Excalibur ve Linux 6.12 LTS üzerinde çalışan AyazDE 5.0.",
        "shot_tabs": [
            ("01", "Yüz 3: Bostan", "bostan", "ayaz-bostan.png",
             "AyazDE 5.0 varsayılan Bostan masaüstü, Ankora AI ve USB Yazıcı ekran görüntüsü",
             "Yüz 3: Bostan (Varsayılan)", "Açık keten adaçayı yüzeyi, kapsül dock ve Ankora AI balonu"),
            ("02", "Yüz 2: Bakır", "bakir", "ayaz-bakir.png",
             "AyazDE 5.0 Bakır tema masaüstü, Yazılım Merkezi ve Ankora AI ekran görüntüsü",
             "Yüz 2: Bakır", "Sıcak grafit zemin, bakır vurgu ve üst panel"),
            ("03", "Yüz 8: Cıvata", "civata", "ayaz-civata.png",
             "AyazDE 5.0 Cıvata tema masaüstü, Sistem Ayarları ve AI balonu ekran görüntüsü",
             "Yüz 8: Cıvata", "Teknik çizim kâğıdı, siyah çerçeve ve alt şerit"),
            ("04", "Yüz 1: Arduvaz", "arduvaz", "ayaz-arduvaz.png",
             "AyazDE 5.0 Arduvaz tema masaüstü, Dosyalar ve Ankora Report ekran görüntüsü",
             "Yüz 1: Arduvaz", "Sol hizalı 38 px bar, çalışma alanları ve terakota vurgu"),
            ("05", "559 Paketli Mağaza", "bostan", "ankora-magaza.png",
             "Ankora Yazılım Merkezi ve Sistem Kurulum aracı ekran görüntüsü",
             "Yazılım Merkezi ve Kurulum", "Devuan APT, Flathub ve Resmî Ankora havuzu"),
        ],
        "specs": [
            ("~750 MB", "Boşta bellek hedefi ve ZRAM"),
            ("20", "Yerleşik Tauri 2.0 penceresi"),
            ("24 + 4", "Tema ve dört çekirdek yüz"),
            ("559", "Doğrulanmış mağaza paketi"),
        ],
        "why_eyebrow": "Ankora 5.0 Mimarisi", "why_h2": "Hafiflik, öngörülebilirlik ve bütüncül Türkçe tasarım",
        "cards3": [
            ("Tauri 2.0 + Rust (/usr/bin/ayaz-de)", "Panel, dosyalar ve mağaza tek ikilide çalışır; kapalı pencereler 30 sn sonra bellekten silinir."),
            ("Dört yüz ve Ankora AI balonu", "Bostan açılışta gelir; tek tıkla Bakır, Cıvata, Arduvaz veya 4.7 Klasik seçilir."),
            ("Okul tahtaları ve çevre birimleri", "Faz 1/2/3 tahtalar için eta-touchdrv, Meb sertifikası ve yazıcı/tarayıcı hazır gelir."),
        ],
        "inside_eyebrow": "Sistem İçeriği", "inside_h2": "Kurduğunuz anda günlük işe hazır",
        "inside_lede": "Günlük işler, geliştirme ve sınıf donanımı AyazDE 5.0 içine entegredir.",
        "inside": [
            "Dosyalar yöneticisi, grafik .deb/.AppImage kurucu ve tarayıcılar",
            "Devuan APT, Flathub ve Resmî havuzlu 559 paketli Yazılım Merkezi",
            "Yerel Ollama veya bulut uçlu beyaz liste denetimli Ankora AI",
            "Geri dönüşlü güncelleyici, USB diski kilidi ve pkexec onayı",
        ],
        "inside_alt": "Ankora Linux 5.0 Yazılım Merkezi ve Sistem Kurulum sihirbazı",
        "step_eyebrow": "Kurulum", "step_h2": "Üç adımda kullanıma hazır",
        "steps3": [("İndirin", "GitHub Releases üzerinden ISO ve SHA256SUMS dosyalarını alın."),
                   ("USB belleğe yazın", "Doğruladıktan sonra çıkarılabilir USB diske yazın."),
                   ("Başlatın veya yükseltin", "USB’den kurun; 4.7.x sistemlerde .deb ile yükselir.")],
        "faq_eyebrow": "Sık sorulan sorular", "faq_h2": "Temel sorular",
        "faq4": [("Ankora Linux 5.0 nedir?", "Devuan 6 Excalibur (SysVinit) ve Linux 6.12 LTS üzerinde ücretsiz Türkçe masaüstü."),
                 ("Eski bilgisayarlarda çalışır mı?", "Boşta ~750 MB hedefler; 4 GB altında zstd/lz4 ZRAM açar."),
                 ("Ücretli midir?", "Hayır. GPL-3.0 lisansıyla tamamen ücretsiz ve açık kaynaklıdır."),
                 ("4.7.x’ten yükselir mi?", "Evet, .deb paketiyle yükselir; 4.6.x için temiz ISO gerekir.")],
        "all_q": "Tüm sorular",
        "cmp_eyebrow": "Bellek karşılaştırması",
        "cmp_h2": "Popüler dağıtımlarla boşta bellek hedefi",
        "cmp_lede": "Ankora 5.0 systemd barındırmaz; SysVinit ve tembel DOM bellek temizliğiyle arka plan yükünü düşük tutar.",
        "cmp_head": ("Dağıtım", "Boşta RAM"),
        "cmp_rows": [("Ankora Linux 5.0 (AyazDE)", "~750 MB"),
                     ("Ubuntu 24.04 (GNOME)", "830 MB"),
                     ("Linux Mint 22.1 (Cinnamon)", "888 MB"),
                     ("Xubuntu 24.04 (Xfce)", "668 MB"),
                     ("Debian 12 (GNOME)", "1 GB üzeri")],
        "cmp_note": "Ankora 5.0: Tauri 2.0 ve Devuan 6 Excalibur geçişi sonrası sistem boşta bellek hedefi (~750 MB). Diğer dağıtımlar Android Authority Ekim 2024 ve Mint bağımsız ölçümüdür.",
        "f_h1": "Ankora Linux 5.0 Özellikleri",
        "f_lede": "AyazDE 5.0; 20 pencere, dört yüz ve Ankora AI’yı tek çekirdekte birleştirir.",
        "f_hl_eyebrow": "5.0 Yenilikleri", "f_hl_h2": "Sürümde öne çıkan altı başlık",
        "f_cards": [("Varsayılan Bostan ve Dörtlü Yüz", "Bostan varsayılan açılır; Bakır, Cıvata, Arduvaz ve 4.7 Klasik seçilebilir."),
                    ("Ankora AI Balonu ve 4 Mod", "Son 6 turla yerel Ollama veya bulut API’sine güvenli bağlanır."),
                    ("Tauri 2.0 ve WebKitGTK 4.1", "30 saniyede DOM boşaltma ve bwrap destekli yalıtılmış webview."),
                    ("559 Paket ve Okul Altyapısı", "APT, Flathub ve Resmî depo yanında tahta sürücüleri hazır gelir."),
                    ("24 Sistem Teması ve Ada", "19 duvar kâğıdı ve üst ekranda medya/bellek kapsülü sunar."),
                    ("Geri Dönüşlü Güncelleyici", "SHA-256 ve GPG doğrular; hatada önceki ikiliye otomatik döner.")],
        "f_themes_eyebrow": "4 Çekirdek Yüz ve 24 Tema", "f_themes_h2": "Tutarlı renk ve çizgi mimarisi",
        "f_themes_lede": "Yukarıdaki tema seçiciden Bostan, Bakır, Cıvata veya Arduvaz’ı canlı deneyin.",
        "f_apps_eyebrow": "Yerleşik Araçlar", "f_apps_h2": "Kutudan çıkan 20 pencere",
        "f_apps_lede": "Günlük işler için ek kurulum gerekmez.",
        "f_apps": ["Dosyalar yöneticisi ve grafik .deb/.AppImage kurucu", "559 paketli Ankora Yazılım Merkezi", "Ankora AI asistanı ve köşe balonu",
                   "USB/ISO yazıcı ve Ankora Report", "Geri dönüşlü Ayaz Güncelleyici", "Sistem ayarları, Wi-Fi, Bluetooth ve ses"],
        "f_apps_alt": "Ankora Linux 5.0 Yazılım Merkezi ve Sistem Kurulum penceresi",
        "f_cta_h2": "Ankora Linux 5.0’ı kurmaya hazır mısınız?", "f_cta_lede": "Temiz ISO edinin veya 4.7.x sisteminizi güncelleyin.",
        "i_h1": "İndir ve Kur",
        "i_lede": "Yeni kurulum için ISO imajı, mevcut 4.7.x sistemler için .deb yükseltmesi ve isteğe bağlı yerel Ollama kurulumu.",
        "i_dl": "GitHub Sürümlerini Aç", "i_src": "Kaynak Kodunu İncele",
        "i_req_eyebrow": "Donanım Profili", "i_req_h2": "Sistem Gereksinimleri",
        "i_req": ["64 bit (amd64) işlemci, UEFI veya klasik BIOS desteği", "Canlı oturum için en az 2 GB RAM (günlük kullanım için 4 GB, yerel Ollama için 8 GB+)",
                  "Kurulum için en az 16 GB disk ve USB bellek (4 GB+)", "Açık kaynak Mesa ve doğrulanmış AMD/Intel çekirdek firmware’i"],
        "i_step_eyebrow": "Kurulum Adımları", "i_step_h2": "Üç adımda tamamlanır",
        "i_steps": [("Doğrulanmış İmajı İndirin", "GitHub Releases sayfasından ISO ve SHA256SUMS dosyalarını alın."),
                    ("Güvenle Yazdırın", "sha256sum ile bütünlüğü kontrol edip yalnızca çıkarılabilir USB sürücüye yazın."),
                    ("Başlatın ve Kurun", "Bilgisayarı USB’den başlatıp Türkçe kurulum sihirbazını izleyin.")],
        "i_cli_eyebrow": "Komut Satırı", "i_cli_h2": "Senaryoya göre kurulum komutları",
        "i_note_b": "Yükseltme Notu", "i_note_p": "4.6.x (Daedalus) tabanından Devuan 6 / Tauri 2.0 tabanlı 5.0 sürümüne geçişte temiz ISO kurulumu gerekir.",
        "s_h1": "Ankora Linux 5.0 Güvenlik Mimarisi",
        "s_lede": "148 Tauri IPC komutu arayüzle çekirdeği ayırır. AI ajanının önerdiği komutlar Rust beyaz listesi ve 60 saniyelik onay jetonuyla denetlenir.",
        "s_core_eyebrow": "Üç Temel Kalkan", "s_core_h2": "Güvenlik nasıl uygulanır?",
        "s_cards": [("Beyaz Liste Denetimli Uçbirim", "Yerleşik uçbirim yalnızca 33 sabit komuta ve 26 tanı aracına izin verir; 59 tehlikeli sistem/ağ ikilisini engeller."),
                    ("60 Saniyelik Tek Kullanımlık AI Jetonu", "Ankora AI yalnızca önceden tanımlı 18 eylemi önerebilir ve yürütme öncesinde kullanıcı onaylı SHA-256 jetonu tüketir."),
                    ("Yalıtılmış Yetki ve Pinned GPG", "Güncelleme, paket kurma ve USB yazma pkexec onayı ister; vendor anahtarları sabitlenmiş GPG parmak iziyle doğrulanır.")],
        "s_tech_eyebrow": "Rust Çekirdek Sınırları (src-tauri/src/main.rs)", "s_tech_h2": "Kaynak kodda doğrulanabilir ölçüler",
        "s_notes": [
            "EXACT_ALLOWED_COMMANDS içinde 33 sabit komut ve ALLOWED_UTILITIES içinde 26 yardımcı araç izin listesinde tutulur.",
            "FORBIDDEN_LAUNCH_BINARIES listesi 59 ağ ve yönetim ikilisinin doğrudan başlatılmasını engeller.",
            "ALLOWED_AGENT_ACTIONS listesi 18 izinli AI eylemiyle sınırlıdır ve her biri 60 saniyelik tek kullanımlık jeton gerektirir.",
            "Belge görüntüleyici 20 güvenli uzantıyı açar ve 19 hassas dosya desenine (.vault_secret dahil) erişimi reddeder.",
            "148 Tauri IPC komutu, 19 Rust birim testi ve bwrap WebKit sandbox’ı arayüz köprüsünü korur.",
        ],
        "s_vuln": "Güvenlik açığı bulursanız herkese açık kayıt açmadan {mail} adresine yazın (48 saat içinde yanıtlanır).",
        "c_h1": "Sürümler ve Değişiklikler", "c_lede": "01.0’dan güncel Ankora Linux 5.0.0 sürümüne kadar gelişim geçmişi.",
        "c_dl": "5.0.0 Sürümünü İndir",
        "c_rows": [("5.0.0", "AyazDE 5.0", "Varsayılan Bostan yüzü, dört hizalanmış Anti-Slop masaüstü mimarisi (Bostan, Bakır, Cıvata, Arduvaz) ve korunan 4.7 Klasik; her yüze uyumlu Ankora AI konuşma balonu; son 6 turluk ajan bağlamı; Devuan 6 Excalibur + Linux 6.12 LTS üzerinde 20 pencere kontrast denetimi."),
                   ("4.7.0", "Bora", "Devuan 6.0 Excalibur ve Tauri 2.0 (WebKitGTK 4.1) geçişi, tek ikili /usr/bin/ayaz-de, geri dönüşlü (rollback) sertleştirilmiş güncelleyici, 4 yeni fotoğraf duvar kâğıdı, sabit GPG parmak izi doğrulaması ve QEMU BIOS/UEFI CI."),
                   ("4.6.0", "Karayel", "ZRAM bellek sıkıştırma iyileştirmesi, 559 paketli mağaza kataloğu, polkit düzeltmeleri, senkronize saat widget’ı ve açık tema kontrast onarımları."),
                   ("4.0", "AyazDE", "29 Ekim sürümü: kilit ekranı hız sınırlayıcı, pano koruması, hibrit ISO doğrulama ve Cumhuriyet teması."),
                   ("3.7", "AyazDE", "Masaüstü kategori klasörleri, canlı hava durumu, temiz MEB sertifika kaldırıcı ve .deb güncelleyici."),
                   ("3.6", "AyazDE", "Menü çubuklu Dosyalar yöneticisi, USB/ISO yazıcı ve ETAP akıllı tahta sürücüleri."),
                   ("3.5", "AyazDE", "4 GB altında Eco RAM kipi, udisks otomatik bağlama ve 30 sn DOM bellek boşaltma."),
                   ("3.0", "AyazDE", "SysVinit üzerinde ilk Rust ve Tauri 1.5 masaüstü çekirdeği."),
                   ("2.0", "AyazDE", "AyazDE masaüstü ortamının doğuşu ve sadeleşme."),
                   ("01.0", "İlk Sürüm", "Telemetrisiz, sade temel masaüstü.")],
        "c_foot": "Tüm sürüm arşivleri ve SHA256SUMS dosyaları GitHub Releases sayfasında barınır.",
        "row_go": "indir",
        "q_h1": "Sık Sorulan Sorular", "q_lede": "Yanıtı bulamazsanız iletişim sayfasından foruma ulaşabilirsiniz:",
        "q_qas": [("Ankora Linux 5.0 nedir?", "Devuan 6.0 Excalibur ve Linux 6.12 LTS üzerinde çalışan, systemd içermeyen Türkçe bir masaüstü dağıtımıdır."),
                  ("Eski bilgisayarda çalışır mı?", "Evet. Boşta ~750 MB bellek hedefler ve 4 GB altında ZRAM (zstd/lz4) otomatik etkinleşir."),
                  ("Diskimi silmeden deneyebilir miyim?", "Evet. ISO dosyasını USB belleğe yazıp başlattığınızda sabit diskinize dokunulmaz."),
                  ("4.7.x’ten 5.0’a nasıl yükseltilir?", "Ayaz Güncelleyici veya ayaz-de-latest-amd64.deb paketiyle sürüm içi geçiş yapılır; 4.6.x için temiz ISO gerekir."),
                  ("Klavye dilleri nelerdir?", "Sistem arayüzü Türkçedir; klavyede Türkçe, İngilizce, Almanca, Fransızca ve İngiliz (GB) seçilebilir."),
                  ("Ankora AI istediği komutu çalıştırabilir mi?", "Hayır. Yalnızca Rust çekirdeğindeki 18 izinli eylem ve 33 sabit komut kullanıcı onayıyla çalışır.")],
        "q_forum": "Forumda Sor", "q_contact": "İletişim",
        "k_h1": "İletişim", "k_lede": "Kullanım soruları için Ankora Lab forumu, hata kayıtları için GitHub, güvenlik için e-posta.",
        "k_rows": [("Ankora Lab Forumu", "ankalab.flarum.cloud", "foruma git"),
                   ("Proje E-postası", MAIL, "e-posta gönder"),
                   ("Hata Bildirimi", "github.com/Ankora-Linux/Ankora", "kayıt aç"),
                   ("Güvenlik Bildirimi", SECMAIL, "e-posta gönder")],
        "k_bug_eyebrow": "Hata Bildirimi", "k_bug_h2": "Daha hızlı çözüm için şunları ekleyin",
        "k_items": ["Ankora sürümü (örn. 5.0.0) ve aktif masaüstü yüzü", "Ankora Report Markdown çıktısı veya hata günlüğü",
                    "Hatayı yeniden oluşturma adımları", "İşlemci ve RAM bilgisi (HARDWARE.md geri bildirimi dahil)"],
        "ai_lab": {
            "title": "Etkileşimli AI ve Mağaza Denetimi",
            "subtitle": "Rust komut beyaz listesini canlı sınayın ve 559 paketlik mağaza kataloğundan öne çıkanları filtreleyin.",
            "modes_h": "Dört AI Çalışma Modu",
            "modes_p": "Yerel Ollama (127.0.0.1:11434), Gemini 2.5 Flash, OpenAI, Groq veya OpenRouter uçlarına son 6 konuşma turunu aktarır.",
            "modes": [
                ("teftis", "Teftiş", "Sistem Teftiş", "Canlı RAM, CPU yükü ve disk verisiyle yalnızca izinli tanı eylemleri önerir.", "Mod: Sistem Teftiş\nBağlam: son 6 konuşma turu + canlı telemetri\nÖneri: df -h / && free -m"),
                ("doktor", "Doktor", "Sistem Doktoru", "ZRAM sıkıştırmasını ve ağ arabirimlerini ankora-doctor betiğiyle tarar.", "Mod: Sistem Doktoru\nKontrol: /etc/init.d/zram-swap (zstd > lz4)\nEylem: /usr/local/bin/ankora-doctor"),
                ("dev", "Geliştirici", "Geliştirici Asistanı", "Yerel proje günlüklerini salt okunur denetim komutlarıyla analiz eder.", "Mod: Geliştirici\nKapı: is_terminal_command_permitted()\nKorumalı: .vault_secret"),
                ("ajan", "Ajan", "Masaüstü Ajanı", "Türkçe komutlarla uygulama açar, yüz değiştirir veya mağaza kurulum planı üretir.", "“Bakır yüzüne geç” -> Yüz 2 Bakır\n“VLC kur” -> Mağaza kurulum planı\n“Terminali aç” -> Uçbirimi açar"),
            ],
            "tester_h": "Canlı Komut Güvenlik Denetleyicisi",
            "tester_p": "is_terminal_command_permitted() ve ALLOWED_AGENT_ACTIONS kapısını simüle eder.",
            "tester_lbl": "Denetlenecek sistem komutu",
            "tester_btn": "Denetle",
            "ok_msg": "ONAYLANDI: “{cmd}” Rust beyaz listesinde; 60 sn tek kullanımlık jeton üretilir.",
            "deny_msg": "REDDEDİLDİ: “{cmd}” EXACT_ALLOWED_COMMANDS ve ALLOWED_AGENT_ACTIONS dışında.",
            "store_h": "559 Paketlik Mağazadan Örnekler",
            "store_ph": "Paket ara (örn. Fatih, Code, VLC)…",
            "store_all": "Tümü", "store_official": "Resmî Ankora", "store_apt": "Devuan APT", "store_flat": "Flathub",
            "store_cols": ("Uygulama", "Kategori", "Kaynak"),
            "store_empty": "Eşleşen örnek paket bulunamadı.",
        },
        "dl_tabs": [
            ("iso", "ISO Kurulum", "# GitHub Releases sayfasından ISO ve SHA256SUMS indirip doğrulayın:\nsha256sum -c SHA256SUMS --ignore-missing\nlsblk -o NAME,SIZE,TRAN,RM", "Yeni kurulumlar ve 4.6.x (Daedalus) tabanından geçiş için önerilir."),
            ("deb", "4.7.x -> 5.0 Yükseltme", "# Mevcut 4.7.x sistemleri Resmî .deb paketiyle 5.0’a geçirin:\nsha256sum -c ayaz-de-latest-amd64.deb.sha256\nsudo apt install ./ayaz-de-latest-amd64.deb", "Kurulum hatasında ayaz-update-helper önceki yedeğe otomatik döner."),
            ("ai", "Yerel AI (Ollama)", "# Yerel Ollama kurucusu (8 GB+ RAM önerilir):\nsudo /usr/local/bin/ankora-ollama-install", "Kurulumdan sonra sağ alttaki Ankora AI balonu 127.0.0.1:11434 adresine bağlanır."),
        ],
    },
    "en": {
        "m_home": ("Ankora Linux 5.0: Calm, systemd-free Turkish desktop",
                   "Ankora Linux 5.0 runs AyazDE 5.0 on Devuan 6 Excalibur and Linux 6.12 LTS with four desktop faces, allowlisted Ankora AI, and a 559-package store."),
        "m_features": ("Features: Ankora Linux 5.0",
                       "Explore AyazDE 5.0: Bostan, Bakır, Cıvata, and Arduvaz faces, per-face Ankora AI bubble, 559-package store, and FAZ 1/2/3 classroom tools."),
        "m_install": ("Download and install: Ankora Linux 5.0",
                      "Install Ankora Linux 5.0 via clean ISO, upgrade in-place from 4.7.x using .deb, or set up local Ollama AI."),
        "m_security": ("Security: Ankora Linux 5.0",
                       "Rust security boundaries: 33 exact terminal commands, 59 forbidden binaries, 18 AI actions with one-time tokens, pkexec, and WebKit bwrap sandbox."),
        "m_changelog": ("Releases: Ankora Linux 5.0",
                        "Complete release history of Ankora Linux from 01.0 through 5.0.0."),
        "m_faq": ("Frequently asked questions: Ankora Linux 5.0",
                  "Answers about Ankora Linux 5.0: hardware, ZRAM, upgrading from 4.7.x, AI guardrails, and contributing."),
        "m_contact": ("Contact: Ankora Linux",
                      "Reach the Ankora Linux community via Ankora Lab forum, email, GitHub issues, or security disclosures."),
        "hero_meta": ("Ankora Linux 5.0.0", "AyazDE 5.0", "Devuan 6 Excalibur", "Linux 6.12 LTS", "~750 MB RAM"),
        "h1": "Calm, systemd-free Turkish desktop.",
        "lede": "AyazDE 5.0 built on Devuan 6 Excalibur and Linux 6.12 LTS.",
        "shot_tabs": [
            ("01", "Face 3: Bostan", "bostan", "ayaz-bostan.png",
             "AyazDE 5.0 default Bostan desktop with Ankora AI and USB Flasher",
             "Face 3: Bostan (Default)", "Warm sage linen, capsule dock, and Ankora AI bubble"),
            ("02", "Face 2: Bakır", "bakir", "ayaz-bakir.png",
             "AyazDE 5.0 Bakır theme desktop with Software Center and Ankora AI bubble",
             "Face 2: Bakır", "Graphite surfaces, copper accent, and top bar"),
            ("03", "Face 8: Cıvata", "civata", "ayaz-civata.png",
             "AyazDE 5.0 Cıvata theme desktop with System Settings and bottom bar",
             "Face 8: Cıvata", "Drafting paper, sharp ink borders, and bottom strip"),
            ("04", "Face 1: Arduvaz", "arduvaz", "ayaz-arduvaz.png",
             "AyazDE 5.0 Arduvaz desktop with Files manager and Ankora Report",
             "Face 1: Arduvaz", "Left-aligned 38 px taskbar and terracotta focus"),
            ("05", "559-Package Store", "bostan", "ankora-magaza.png",
             "Ankora Software Center and graphical system installer",
             "Store & Installer", "Devuan APT, Flathub, and official Ankora repository"),
        ],
        "specs": [
            ("~750 MB", "Idle live memory target with ZRAM"),
            ("20", "Built-in Tauri 2.0 windows"),
            ("24 + 4", "System themes and four core faces"),
            ("559", "Verified store packages"),
        ],
        "why_eyebrow": "Architecture 5.0", "why_h2": "Built for predictable behaviour and restraint",
        "cards3": [
            ("Tauri 2.0 & Rust (/usr/bin/ayaz-de)", "Desktop modules run in a single binary and unmount closed windows from DOM after 30 seconds."),
            ("Four core faces & AI bubble", "Bostan opens by default; click to pick Bakır, Cıvata, Arduvaz, or 4.7 Classic."),
            ("Schools & peripherals ready", "Ships with eta-touchdrv, clean MEB cert tools (~/.pki/nssdb), and CUPS/SANE."),
        ],
        "inside_eyebrow": "Included", "inside_h2": "Ready for work out of the box",
        "inside_lede": "Core desktop tools, classroom drivers, and safety checks ship built in.",
        "inside": [
            "File Manager with USB automount and .deb/.AppImage installer",
            "559-package Store merging Devuan APT, Flathub, and official Ankora",
            "Allowlisted Ankora AI connecting to local Ollama or cloud APIs",
            "Rollback-safe updater, removable USB guard, and pkexec",
        ],
        "inside_alt": "Ankora Linux 5.0 Software Store and System Installer",
        "step_eyebrow": "Setup", "step_h2": "Ready in three steps",
        "steps3": [("Download", "Fetch ISO and SHA256SUMS from GitHub Releases."),
                   ("Verify & flash", "Check checksums and write to a removable USB drive."),
                   ("Boot or upgrade", "Boot from USB, or use the .deb package on 4.7.x.")],
        "faq_eyebrow": "FAQ", "faq_h2": "Key questions",
        "faq4": [("What is Ankora Linux 5.0?", "Free Turkish Linux on Devuan 6 Excalibur and Linux 6.12 LTS."),
                 ("Does it run on old hardware?", "Targets ~750 MB idle RAM and enables ZRAM under 4 GB."),
                 ("Does it cost anything?", "No. Free and open source under GPL-3.0."),
                 ("Upgrade from 4.7.x?", "Yes via .deb; 4.6.x requires a clean ISO install.")],
        "all_q": "All questions",
        "cmp_eyebrow": "Idle memory",
        "cmp_h2": "Idle target alongside popular desktops",
        "cmp_lede": "Ankora 5.0 replaces systemd with SysVinit and unmounts closed WebKit window trees after 30 seconds.",
        "cmp_head": ("Distribution", "Idle RAM"),
        "cmp_rows": [("Ankora Linux 5.0 (AyazDE)", "~750 MB"),
                     ("Ubuntu 24.04 (GNOME)", "830 MB"),
                     ("Linux Mint 22.1 (Cinnamon)", "888 MB"),
                     ("Xubuntu 24.04 (Xfce)", "668 MB"),
                     ("Debian 12 (GNOME)", "over 1 GB")],
        "cmp_note": "Ankora 5.0: live idle memory target (~750 MB) after the Tauri 2.0 and Devuan 6 Excalibur transition. Other distributions reference Android Authority (Oct 2024) and Mint independent benchmarks.",
        "f_h1": "Ankora Linux 5.0 Features",
        "f_lede": "AyazDE 5.0 unifies 20 built-in windows, 24 themes, four core architectures, allowlisted AI, and 559 packages.",
        "f_hl_eyebrow": "What is new in 5.0", "f_hl_h2": "Six highlights of the release",
        "f_cards": [("Default Bostan & 4 Desktop Faces", "Opens with Bostan by default; switch immediately across Bakır, Cıvata, Arduvaz, and preserved 4.7 Classic."),
                    ("Ankora AI Chat Bubble & 4 Modes", "Sysadmin Inspect, System Doctor, Developer, and Desktop Agent modes pass 6 recent turns to local Ollama or cloud models."),
                    ("Tauri 2.0 & WebKitGTK 4.1", "Clean window management, 30-second lazy DOM cleanup, and bwrap-sandboxed webviews."),
                    ("559 Packages & Classroom Ready", "Unified APT, Flathub, and official repo alongside eta-touchdrv, Fatih Kalem 2, MEB cert tools, and CUPS/SANE."),
                    ("24 System Themes & Dynamic Island", "Full palette coherence with 19 wallpapers and an optional top telemetry/media pill."),
                    ("Rollback-Safe Verified Updater", "ayaz-update-helper validates SHA-256 and GPG signatures and restores the prior binary on failure.")],
        "f_themes_eyebrow": "4 Core Faces & 24 Themes", "f_themes_h2": "Intentional surface architecture",
        "f_themes_lede": "Pick Bostan, Bakır, Cıvata, or Arduvaz in the page header switcher to preview the four design systems live.",
        "f_apps_eyebrow": "Built-in Windows", "f_apps_h2": "20 tools ready out of the box",
        "f_apps_lede": "Core file, package, and system utilities ship preconfigured.",
        "f_apps": ["File Manager with .deb/.AppImage installer", "559-package Software Center", "Ankora AI Assistant & corner bubble",
                   "USB & ISO Flasher with internal disk lock", "Ankora Report forum template builder", "Rollback-capable Ayaz Updater",
                   "Dynamic Island media & telemetry pill", "Screenshot, calculator, and notes", "System settings, Wi-Fi, Bluetooth, and audio"],
        "f_apps_alt": "Ankora Linux 5.0 Software Store and Installer",
        "f_cta_h2": "Ready to try Ankora Linux 5.0?", "f_cta_lede": "Download the ISO image or upgrade from 4.7.x.",
        "i_h1": "Download and Install",
        "i_lede": "Use a clean ISO for new setups or 4.6.x upgrades, the .deb package for 4.7.x systems, or install local Ollama AI.",
        "i_dl": "Open GitHub Releases", "i_src": "Browse Source Code",
        "i_req_eyebrow": "Hardware Profile", "i_req_h2": "System Requirements",
        "i_req": ["64-bit (amd64) processor with UEFI or legacy BIOS", "2 GB RAM minimum live (4 GB recommended daily, 8 GB+ for local Ollama)",
                  "16 GB+ disk space and 4 GB+ USB flash drive", "Open-source Mesa graphics with verified AMD/Intel firmware"],
        "i_step_eyebrow": "Steps", "i_step_h2": "Three clear steps",
        "i_steps": [("Download Verified Release", "Fetch the ISO image and SHA256SUMS from GitHub Releases."),
                    ("Flash Safely", "Check SHA-256 sums and write only to a removable USB flash device."),
                    ("Boot & Install", "Start from USB and follow the guided Turkish installer.")],
        "i_cli_eyebrow": "Command Line", "i_cli_h2": "Commands by installation path",
        "i_note_b": "Upgrade Policy", "i_note_p": "Upgrading from 4.6.x (Daedalus) requires a fresh ISO install due to the Devuan 6 / Tauri 2.0 ABI shift.",
        "s_h1": "Ankora Linux 5.0 Security Architecture",
        "s_lede": "148 Rust Tauri IPC commands isolate UI actions from the host. AI commands pass strict allowlists and consume 60-second tokens.",
        "s_core_eyebrow": "Core Guardrails", "s_core_h2": "Enforced in compiled Rust",
        "s_cards": [("Allowlisted Terminal Execution", "Built-in terminal checks 33 exact commands and 26 utilities while blocking 59 sensitive binaries from direct execution."),
                    ("60-Second One-Time AI Token", "The AI agent may propose only 18 predefined actions, requiring manual confirmation and a fresh SHA-256 token."),
                    ("Least Privilege & Pinned GPG", "Package installs, updates, and USB writes require pkexec; vendor GPG keys are verified against pinned fingerprints.")],
        "s_tech_eyebrow": "Rust Core Metrics (src-tauri/src/main.rs)", "s_tech_h2": "Verifiable source guardrails",
        "s_notes": [
            "EXACT_ALLOWED_COMMANDS permits 33 fixed diagnostic commands alongside 26 ALLOWED_UTILITIES.",
            "FORBIDDEN_LAUNCH_BINARIES blocks direct launch of 59 network and administrative binaries.",
            "ALLOWED_AGENT_ACTIONS restricts the AI agent to 18 actions guarded by 60-second single-use tokens.",
            "Document viewer validates 20 safe extensions and denies access to 19 sensitive path patterns such as .vault_secret.",
            "148 Tauri IPC commands and 19 automated Rust unit tests protect the host bridge alongside bwrap WebKit sandboxing.",
        ],
        "s_vuln": "Found a security issue? Email {mail} privately rather than filing a public issue (48-hour response target).",
        "c_h1": "Releases and Changelog", "c_lede": "Milestones from 01.0 to the latest Ankora Linux 5.0.0 release.",
        "c_dl": "Download 5.0.0",
        "c_rows": [("5.0.0", "AyazDE 5.0", "Default Bostan face, four prototype-aligned Anti-Slop faces (Bostan, Bakır, Cıvata, Arduvaz) plus preserved 4.7 Classic; per-face Ankora AI chat bubble; 6-turn AI memory; full contrast and layout audit across all 20 windows on Devuan 6 and Linux 6.12 LTS."),
                   ("4.7.0", "Bora", "Devuan 6.0 Excalibur and Tauri 2.0 (WebKitGTK 4.1) migration, unified /usr/bin/ayaz-de binary, rollback-safe hardened updater, 4 photographic wallpapers, pinned GPG checks, and QEMU CI smoke tests."),
                   ("4.6.0", "Karayel", "ZRAM compression tuning, 559-package store growth, polkit privilege fixes, synced desktop clock, and light-theme contrast fixes."),
                   ("4.0", "AyazDE", "Republic Day release: lock screen rate limiter, clipboard hardening, hybrid ISO check, and Cumhuriyet theme."),
                   ("3.7", "AyazDE", "Desktop category folders, live weather, clean MEB cert removal, and .deb update channel."),
                   ("3.6", "AyazDE", "Menu-bar File Manager, USB/ISO flasher, and ETAP smartboard support."),
                   ("3.5", "AyazDE", "Eco RAM mode under 4 GB, udisks automount, and 30-second window DOM cleanup."),
                   ("3.0", "AyazDE", "Initial Rust and Tauri 1.5 core on SysVinit."),
                   ("2.0", "AyazDE", "Introduction of AyazDE desktop environment."),
                   ("01.0", "First Release", "Clean, telemetry-free foundation.")],
        "c_foot": "Release archives and SHA256SUMS files are published on GitHub Releases.",
        "row_go": "get",
        "q_h1": "Frequently Asked Questions", "q_lede": "Need further help? Visit the forum via our contact page:",
        "q_qas": [("What is Ankora Linux 5.0?", "A free, systemd-free Turkish distribution built on Devuan 6.0 Excalibur and Linux 6.12 LTS with the AyazDE 5.0 desktop."),
                  ("Does it work on older laptops?", "Yes. It targets ~750 MB idle RAM, automatically enables ZRAM (zstd/lz4) below 4 GB, and boots from 2 GB RAM."),
                  ("Can I test without wiping my disk?", "Yes. Booting the Live USB leaves your existing partitions untouched."),
                  ("How do I upgrade from 4.7.x to 5.0?", "Use Ayaz Updater or install ayaz-de-latest-amd64.deb; 4.6.x users should perform a clean ISO install."),
                  ("Which keyboard layouts are included?", "Turkish interface with Turkish, English, German, French, and UK English keyboard options."),
                  ("Can Ankora AI run arbitrary shell commands?", "No. Only 18 predefined agent actions and 33 fixed commands are allowed with explicit user confirmation.")],
        "q_forum": "Ask on Forum", "q_contact": "Contact",
        "k_h1": "Contact", "k_lede": "Use the Ankora Lab forum for fast troubleshooting, GitHub for bugs, and email for security reports.",
        "k_rows": [("Ankora Lab Forum", "ankalab.flarum.cloud", "open forum"),
                   ("Project Email", MAIL, "send email"),
                   ("Bug Tracker", "github.com/Ankora-Linux/Ankora", "open issue"),
                   ("Security Disclosure", SECMAIL, "send email")],
        "k_bug_eyebrow": "Bug Reports", "k_bug_h2": "Include these details for faster help",
        "k_items": ["Ankora version (e.g. 5.0.0) and active desktop face", "Ankora Report Markdown block or terminal output",
                    "Exact steps to reproduce", "CPU and RAM specs (also helpful for HARDWARE.md)"],
        "ai_lab": {
            "title": "Interactive AI & Store Explorer",
            "subtitle": "Test the Rust terminal command gate live and filter highlighted packages from the 559-package catalog.",
            "modes_h": "Four AI Modes & Providers",
            "modes_p": "Passes the last 6 conversation turns to local Ollama (127.0.0.1:11434), Gemini 2.5 Flash, OpenAI, Groq, or OpenRouter.",
            "modes": [
                ("teftis", "Inspect", "System Inspect", "Reads live RAM, CPU load, and root disk usage before suggesting safe actions.", "Mode: System Inspect\nContext: last 6 turns + live telemetry\nAction: df -h / && free -m"),
                ("doktor", "Doctor", "System Doctor", "Audits ZRAM compression ratios, swap, and interfaces via ankora-doctor.", "Mode: System Doctor\nCheck: /etc/init.d/zram-swap\nAction: /usr/local/bin/ankora-doctor"),
                ("dev", "Developer", "Developer Assistant", "Analyzes build logs within read-only inspection boundaries.", "Mode: Developer\nGate: is_terminal_command_permitted()\nProtected: .vault_secret"),
                ("ajan", "Agent", "Desktop Agent", "Launches built-in windows, switches faces, or plans store package installs.", "“Bakır yüzüne geç” -> Face 2 active\n“VLC kur” -> Store install plan\n“Terminali aç” -> Opens terminal"),
            ],
            "tester_h": "Live Command Security Gate",
            "tester_p": "Simulates is_terminal_command_permitted() and ALLOWED_AGENT_ACTIONS.",
            "tester_lbl": "Command to check",
            "tester_btn": "Check",
            "ok_msg": "ALLOWED: “{cmd}” matched the Rust allowlist (60 s one-time token generated).",
            "deny_msg": "DENIED: “{cmd}” is outside EXACT_ALLOWED_COMMANDS and ALLOWED_AGENT_ACTIONS.",
            "store_h": "Highlighted Packages (559 total)",
            "store_ph": "Filter packages (e.g. Fatih, Code, VLC)…",
            "store_all": "All", "store_official": "Official", "store_apt": "Devuan APT", "store_flat": "Flathub",
            "store_cols": ("Application", "Category", "Source"),
            "store_empty": "No matching sample packages.",
        },
        "dl_tabs": [
            ("iso", "ISO Clean Install", "# Download ISO and SHA256SUMS from GitHub Releases and verify:\nsha256sum -c SHA256SUMS --ignore-missing\nlsblk -o NAME,SIZE,TRAN,RM", "Required for fresh hardware and upgrades from 4.6.x (Daedalus)."),
            ("deb", "4.7.x -> 5.0 Upgrade", "# Upgrade existing 4.7.x installs with the official .deb package:\nsha256sum -c ayaz-de-latest-amd64.deb.sha256\nsudo apt install ./ayaz-de-latest-amd64.deb", "If an install fails, ayaz-update-helper automatically rolls back to the prior binary."),
            ("ai", "Local AI (Ollama)", "# Install Ollama runtime and lightweight model support (8 GB+ RAM recommended):\nsudo /usr/local/bin/ankora-ollama-install", "Connects the AyazDE bottom-right Ankora AI bubble to 127.0.0.1:11434."),
        ],
    },
}

import i18n_extra

T.update(i18n_extra.EXTRA)

FOOTL = {
    "tr": {"forum": "Ankora Lab forumu", "repo": "GitHub deposu", "rel": "Sürümler", "lic": "GPL-3.0 lisansı"},
    "en": {"forum": "Ankora Lab forum", "repo": "GitHub repository", "rel": "Releases", "lic": "GPL-3.0 license"},
    "de": {"forum": "Ankora-Lab-Forum", "repo": "GitHub-Repository", "rel": "Versionen", "lic": "GPL-3.0-Lizenz"},
    "es": {"forum": "Foro Ankora Lab", "repo": "Repositorio GitHub", "rel": "Versiones", "lic": "Licencia GPL-3.0"},
    "ru": {"forum": "Форум Ankora Lab", "repo": "Репозиторий GitHub", "rel": "Версии", "lic": "Лицензия GPL-3.0"},
}


def e(text):
    return str(text).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


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


def card(t, d):
    return f'<div class="card"><h3>{e(t)}</h3><p>{e(d)}</p></div>'


def li_check(lang, text):
    return f'<li>{ck(lang)}<span>{e(text)}</span></li>'


def step(t, d):
    return f'<li><h3>{e(t)}</h3><p>{e(d)}</p></li>'


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
    for i, (num, label, theme_key, img, alt, cap_title, cap_meta) in enumerate(t["shot_tabs"]):
        active = i == 0
        sel = "true" if active else "false"
        tabidx = "0" if active else "-1"
        hid = "" if active else " hidden"
        tid = f"shot-tab-{num}"
        pid = f"shot-panel-{num}"
        tabs.append(
            f'<button class="shot-tab" type="button" role="tab" id="{tid}" '
            f'aria-selected="{sel}" aria-controls="{pid}" tabindex="{tabidx}" '
            f'data-shot-tab="{num}" data-face-theme="{theme_key}">'
            f'<span class="num">{e(num)}</span><span>{e(label)}</span></button>'
        )
        panels.append(
            f'<div class="shot-panel" id="{pid}" role="tabpanel" aria-labelledby="{tid}" '
            f'data-shot-panel="{num}"{hid}>'
            f'<figure class="shot"><img src="{asset(lang, "assets/img/" + img)}" '
            f'width="1280" height="800" alt="{e(alt)}">'
            f'<figcaption class="shot-caption"><strong>{e(cap_title)}</strong><span>{e(cap_meta)}</span></figcaption>'
            f'</figure></div>'
        )
    return (
        '<div class="showcase">'
        '<div class="shot-tabs" role="tablist" aria-label="AyazDE 5.0">\n          '
        + "\n          ".join(tabs)
        + "\n        </div>\n        "
        + "\n        ".join(panels)
        + "\n      </div>"
    )


def theme_chips(lang):
    chips = []
    for tkey, name, desc_tr, desc_en, swcls in CORE_FACES:
        desc = desc_tr if lang == "tr" else desc_en
        chips.append(
            f'<button type="button" class="theme-chip tset" data-set-theme="{tkey}" aria-pressed="false">'
            f'<strong>{e(name)}</strong>'
            f'<small>{e(desc)}</small>'
            f'</button>'
        )
    return "\n        ".join(chips)


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
        "operatingSystem": "Linux", "softwareVersion": "5.0.0",
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
            {"@type": "ListItem", "position": 1, "name": NAVL[lang]["home"], "item": canon(lang, "home")},
            {"@type": "ListItem", "position": 2, "name": label, "item": canon(lang, key)},
        ],
    }


def block(b):
    return ('<script type="application/ld+json">\n'
            + json.dumps(b, ensure_ascii=False, indent=2) + "\n</script>")


def head(lang, key, blocks):
    t = T[lang]
    title, desc = t["m_" + key]
    alts = "\n".join(f'<link rel="alternate" hreflang="{L}" href="{canon(L, key)}">' for L in LANGS)
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
<meta name="theme-color" content="#eef1e2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141519" media="(prefers-color-scheme: dark)">
<link rel="canonical" href="{canon(lang, key)}">
{alts}
{THEME_SCRIPT}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONT_CSS}">
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
<meta property="og:image:width" content="1280">
<meta property="og:image:height" content="800">
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


def tools(lang):
    u = U[lang]
    icons = asset(lang, "assets/img/icons.svg")
    themes = "".join(
        f'<button class="tset" type="button" data-set-theme="{v}" aria-pressed="false">{e(lbl)}</button>'
        for v, lbl in (
            ("bostan", u["tBostan"]), ("bakir", u["tBakir"]),
            ("civata", u["tCivata"]), ("arduvaz", u["tArduvaz"]),
            ("auto", u["tAuto"]),
        )
    )
    return f"""
    <div class="tools">
      <button class="tbtn" type="button" data-theme-btn aria-expanded="false" aria-controls="theme-panel" aria-label="{e(u['settings'])}" title="{e(u['settings'])}">
        <svg aria-hidden="true" focusable="false"><use href="{icons}#i-moon"></use></svg>
        <span data-theme-label>Bostan</span>
      </button>
      <div class="tpanel" id="theme-panel" hidden>
        <h4>{e(u['theme'])}</h4>
        <div class="trow">{themes}</div>
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
    sheet = "".join(f'\n          <li><a href="{local(lang, k)}">{e(n[k])}</a></li>' for k in NAVORDER)
    sheet += f'\n          <li><a href="{local(lang, "install")}">{e(u["download"])}</a></li>'
    sheet += f'\n          <li><a href="{local(lang, "faq")}">{e(n["faq"])}</a></li>'
    return f"""
<a class="skip" href="#main">{e(u["skip"])}</a>

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
    <a class="btn btn-1 head-cta" href="{local(lang, "install")}">{e(u["download"])}</a>{langmenu(lang, key)}{tools(lang)}
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


def home(lang):
    t = T[lang]
    u = U[lang]
    hm = t["hero_meta"]
    meta_html = "\n          ".join(
        f'<strong>{e(x)}</strong>' if i == 0 else f'<span>{e(x)}</span>'
        for i, x in enumerate(hm)
    )
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
          {meta_html}
        </div>
        <h1>{e(t["h1"])}</h1>
        <p class="lede" style="margin-inline:auto">{e(t["lede"])}</p>
        <div class="btn-row" style="justify-content:center;margin-top:24px">
          <a class="btn btn-1" href="{local(lang, "install")}">{e(u["download"])}</a>
          <a class="text-link" href="{local(lang, "features")}">{e(NAVL[lang]["features"])}</a>
        </div>
      </div>
      {showcase(lang)}
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <h2>{e(t["why_h2"])}</h2>
      </div>
      <div class="spec-strip">
        {spec_cells}
      </div>
      <div class="arch-grid">
        <div class="arch-lead">
          <div>
            <h3>{e(c0_title)}</h3>
            <p>{e(c0_desc)}</p>
          </div>
          <div class="arch-meta">
            <span>Tauri 2.0 + Rust</span>
            <span>WebKitGTK 4.1</span>
            <span>SysVinit PID 1</span>
            <span>Linux 6.12 LTS</span>
          </div>
        </div>
        <div class="arch-side">
          {card(c1_title, c1_desc)}
          {card(c2_title, c2_desc)}
        </div>
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>{e(t["inside_h2"])}</h2>
          <p class="lede">{e(t["inside_lede"])}</p>
          <ul class="checklist" style="margin-top:24px">
            {inside}
          </ul>
        </div>
        {shot(lang, "ankora-magaza.png", t["inside_alt"], 1280, 800)}
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
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

  <section class="section">
    <div class="wrap">
      <div class="section-head">
        <h2>{e(t["step_h2"])}</h2>
      </div>
      <ol class="steps">
        {steps}
      </ol>
      <div class="btn-row" style="margin-top:32px"><a class="btn btn-1" href="{local(lang, "install")}">{e(u["download"])}</a></div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head center">
        <h2>{e(t["faq_h2"])}</h2>
      </div>
      <div class="faq" style="margin-inline:auto">
        {faq}
      </div>
      <p style="text-align:center;margin-top:32px"><a class="btn btn-2" href="{local(lang, "faq")}">{e(t["all_q"])}</a></p>
    </div>
  </section>
</main>"""


def features(lang):
    t = T[lang]
    u = U[lang]
    lab = t["ai_lab"]
    cards = "\n        ".join(card(a, b) for a, b in t["f_cards"])
    apps = "\n            ".join(li_check(lang, x) for x in t["f_apps"])
    shot_a = t["shot_tabs"][1]
    shot_b = t["shot_tabs"][3]

    mode_btns = []
    for i, (mk, blbl, mtitle, mdesc, mcode) in enumerate(lab["modes"]):
        pr = "true" if i == 0 else "false"
        mode_btns.append(
            f'<button type="button" class="chip" data-ai-mode="{mk}" aria-pressed="{pr}" '
            f'data-title="{e(mtitle)}" data-desc="{e(mdesc)}" data-code="{e(mcode)}">{e(blbl)}</button>'
        )
    m0 = lab["modes"][0]

    pkg_rows = "\n                ".join(
        f'<tr data-pkg-row data-pkg-source-val="{e(src)}">'
        f'<td><strong>{e(nm)}</strong><br><code>{e(pid)}</code></td>'
        f'<td>{e(cat)}</td><td>{e(src)}</td></tr>'
        for nm, pid, cat, src in SAMPLE_PACKAGES
    )

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
        <h2>{e(t["f_hl_h2"])}</h2>
      </div>
      <div class="grid">
        {cards}
      </div>
    </div>
  </section>

  <section class="section panel" id="ai-lab">
    <div class="wrap">
      <div class="section-head">
        <h2>{e(lab["modes_h"])}</h2>
        <p class="lede">{e(lab["subtitle"])}</p>
      </div>
      <div class="lab-grid">
        <div class="lab-card">
          <h3>{e(lab["modes_h"])}</h3>
          <p>{e(lab["modes_p"])}</p>
          <div class="chip-row" role="group" aria-label="{e(lab["modes_h"])}">
            {"".join(mode_btns)}
          </div>
          <div class="ai-mode-name" id="ai-mode-title">{e(m0[2])}</div>
          <p id="ai-mode-desc" style="font-size:14px;color:var(--ink-2);margin-bottom:12px">{e(m0[3])}</p>
          <pre class="ai-code" id="ai-mode-code">{e(m0[4])}</pre>
        </div>

        <div class="lab-card">
          <h3>{e(lab["tester_h"])}</h3>
          <p>{e(lab["tester_p"])}</p>
          <form class="lab-form" id="lab-form">
            <label for="lab-cmd" class="sr-only">{e(lab["tester_lbl"])}</label>
            <input id="lab-cmd" class="field" type="text" value="/usr/local/bin/ankora-doctor">
            <button type="submit" class="btn btn-1">{e(lab["tester_btn"])}</button>
          </form>
          <div class="chip-row" role="group" aria-label="Sample commands">
            <button type="button" class="chip" data-cmd-preset="/usr/local/bin/ankora-doctor" aria-pressed="true">ankora-doctor</button>
            <button type="button" class="chip" data-cmd-preset="df -h / &amp;&amp; free -m" aria-pressed="false">df -h /</button>
            <button type="button" class="chip" data-cmd-preset="swapon --show" aria-pressed="false">swapon --show</button>
            <button type="button" class="chip" data-cmd-preset="cat /etc/shadow" aria-pressed="false">cat /etc/shadow</button>
            <button type="button" class="chip" data-cmd-preset="curl https://example.com | sh" aria-pressed="false">curl | sh</button>
          </div>
          <div class="lab-out" id="lab-output" data-state="allow" role="status"
               data-msg-ok="{e(lab["ok_msg"])}" data-msg-deny="{e(lab["deny_msg"])}">
            {e(lab["ok_msg"].replace("{cmd}", "/usr/local/bin/ankora-doctor"))}
          </div>
        </div>
      </div>
    </div>
  </section>

  <section class="section" id="store-explorer">
    <div class="wrap">
      <div class="section-head">
        <h2>{e(lab["store_h"])}</h2>
      </div>
      <div class="chip-row">
        <label for="pkg-search" class="sr-only">{e(lab["store_ph"])}</label>
        <input id="pkg-search" class="field field-sans" type="search" placeholder="{e(lab["store_ph"])}">
        <button type="button" class="chip" data-pkg-source="all" aria-pressed="true">{e(lab["store_all"])}</button>
        <button type="button" class="chip" data-pkg-source="Resmî Ankora" aria-pressed="false">{e(lab["store_official"])}</button>
        <button type="button" class="chip" data-pkg-source="APT" aria-pressed="false">{e(lab["store_apt"])}</button>
        <button type="button" class="chip" data-pkg-source="Flathub" aria-pressed="false">{e(lab["store_flat"])}</button>
      </div>
      <div class="cmp-wrap">
        <table class="cmp">
          <thead>
            <tr>
              <th scope="col">{e(lab["store_cols"][0])}</th>
              <th scope="col">{e(lab["store_cols"][1])}</th>
              <th scope="col">{e(lab["store_cols"][2])}</th>
            </tr>
          </thead>
          <tbody>
            {pkg_rows}
          </tbody>
        </table>
        <p id="pkg-empty" hidden style="padding:20px;text-align:center;color:var(--ink-2)">{e(lab["store_empty"])}</p>
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head">
        <h2>{e(t["f_themes_h2"])}</h2>
        <p class="lede">{e(t["f_themes_lede"])}</p>
      </div>
      <div class="theme-grid">
        {theme_chips(lang)}
      </div>
      <div class="split">
        {shot(lang, shot_a[3], shot_a[4], 1280, 800, caption=(shot_a[5], shot_a[6]))}
        {shot(lang, shot_b[3], shot_b[4], 1280, 800, caption=(shot_b[5], shot_b[6]))}
      </div>
    </div>
  </section>

  <section class="section">
    <div class="wrap">
      <div class="split">
        <div>
          <h2>{e(t["f_apps_h2"])}</h2>
          <p class="lede">{e(t["f_apps_lede"])}</p>
          <ul class="checklist" style="margin-top:24px">
            {apps}
          </ul>
        </div>
        {shot(lang, "ayaz-civata.png", t["f_apps_alt"], 1280, 800)}
      </div>
    </div>
  </section>

  <section class="section panel">
    <div class="wrap">
      <div class="section-head center">
        <h2>{e(t["f_cta_h2"])}</h2>
        <p class="lede" style="margin-inline:auto">{e(t["f_cta_lede"])}</p>
        <div class="btn-row" style="justify-content:center;margin-top:24px">
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
    tabs = t["dl_tabs"]
    tab_btns = "\n        ".join(
        f'<button type="button" class="chip" data-dl-tab="{tk}" '
        f'aria-pressed="{"true" if i == 0 else "false"}" '
        f'data-cmd="{e(tcmd)}" data-note="{e(tnote)}">{e(tlbl)}</button>'
        for i, (tk, tlbl, tcmd, tnote) in enumerate(tabs)
    )
    first = tabs[0]
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["i_h1"])}</h1>
      <p class="lede">{e(t["i_lede"])}</p>
      <div class="btn-row" style="margin-top:24px">
        <a class="btn btn-1" href="{REL}" rel="noopener">{e(t["i_dl"])}</a>
        <a class="btn btn-2" href="{REPO}" rel="noopener">{e(t["i_src"])}</a>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <div class="section-head">
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
        <h2>{e(t["i_cli_h2"])}</h2>
      </div>
      <div class="chip-row" role="group" aria-label="{e(t["i_cli_h2"])}">
        {tab_btns}
      </div>
      <div class="code">
        <pre id="dl-cmd"><code>{e(first[2])}</code></pre>
        <button class="copy" type="button" data-copy data-done="{e(u["copied"])}">{e(u["copy"])}</button>
      </div>
      <p id="dl-note" style="margin-top:12px;font-size:14px;color:var(--ink-2)">{e(first[3])}</p>
      <div class="note">
        <b>{e(t["i_note_b"])}</b>
        <p>{e(t["i_note_p"])}</p>
      </div>
    </div>
  </section>
</main>"""


def security(lang):
    t = T[lang]
    cards = "\n        ".join(card(a, b) for a, b in t["s_cards"])
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
        <h2>{e(t["s_tech_h2"])}</h2>
      </div>
      <ul class="checklist">
        {notes}
      </ul>
      <p style="margin-top:28px">{vuln}</p>
    </div>
  </section>
</main>"""


def changelog(lang):
    t = T[lang]
    rows = "\n        ".join(
        f'<li><a href="{REL}" rel="noopener"><span><b>{e(v)}: {e(nm)}</b><small>{e(d)}</small></span>'
        f'<span class="go">{e(t["row_go"])}</span></a></li>'
        for v, nm, d in t["c_rows"])
    return f"""
<main id="main">
  <div class="wrap">
    <div class="page-top">
      <h1>{e(t["c_h1"])}</h1>
      <p class="lede">{e(t["c_lede"])}</p>
      <div class="btn-row" style="margin-top:24px">
        <a class="btn btn-1" href="{REL}" rel="noopener">{e(t["c_dl"])}</a>
      </div>
    </div>
  </div>

  <section class="section">
    <div class="wrap">
      <ul class="rows">
        {rows}
      </ul>
      <p style="margin-top:28px">{e(t["c_foot"])} <a href="{REL}" rel="noopener">GitHub Releases</a>.</p>
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
      <div class="btn-row" style="margin-top:32px">
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
<title>Sayfa bulunamadı: Ankora Linux 5.0</title>
<meta name="description" content="Aradığınız sayfa bulunamadı. Ankora Linux 5.0 ana sayfa, özellikler, kurulum, güvenlik ve iletişim bağlantıları.">
<meta name="robots" content="noindex, follow">
<meta name="color-scheme" content="light dark">
<meta name="theme-color" content="#eef1e2" media="(prefers-color-scheme: light)">
<meta name="theme-color" content="#141519" media="(prefers-color-scheme: dark)">
<base href="/">
<link rel="canonical" href="{SITE}404.html">
{THEME_SCRIPT}
<link rel="stylesheet" href="{FONT_CSS}">
<link rel="stylesheet" href="assets/site.css">
<script>document.documentElement.classList.remove('no-js');</script>
<meta property="og:type" content="website">
<meta property="og:site_name" content="Ankora Linux">
<meta property="og:locale" content="tr_TR">
<meta property="og:title" content="Sayfa bulunamadı: Ankora Linux 5.0">
<meta property="og:image" content="{SITE}assets/img/ayaz-masaustu.png">
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
    <a class="btn btn-1 head-cta" href="{FILES["tr"]["install"]}">{e(u["download"])}</a>{langmenu("tr", key)}{tools("tr")}
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
      <h1>Bu sayfa bulunamadı</h1>
      <p class="lede">Bağlantı değişmiş veya adres hatalı yazılmış olabilir.</p>
    </div>
  </div>
  <section class="section">
    <div class="wrap">
      <ul class="rows">
        <li><a href="./"><span><b>{e(NAVL["tr"]["home"])}</b><small>Genel bakış ve masaüstü yüzleri</small></span><span class="go">index</span></a></li>
        <li><a href="{FILES["tr"]["features"]}"><span><b>{e(NAVL["tr"]["features"])}</b><small>AyazDE 5.0, Ankora AI ve 559 paket</small></span><span class="go">ozellikler</span></a></li>
        <li><a href="{FILES["tr"]["install"]}"><span><b>{e(u["download"])}</b><small>ISO kurulum ve .deb yükseltme</small></span><span class="go">kurulum</span></a></li>
        <li><a href="{FILES["tr"]["security"]}"><span><b>{e(NAVL["tr"]["security"])}</b><small>Rust beyaz listeleri ve yalıtım</small></span><span class="go">guvenlik</span></a></li>
      </ul>
    </div>
  </section>
</main>

{footer("tr")}"""


def sitemap():
    prio = {"home": "1.0", "features": "0.9", "install": "0.9", "security": "0.8",
            "changelog": "0.7", "faq": "0.8", "contact": "0.6"}
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
            out.append("    <changefreq>monthly</changefreq>")
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
    return f"""# Ankora Linux 5.0

> Ankora Linux 5.0; Devuan 6.0 Excalibur (SysVinit) ve Linux 6.12 LTS üzerinde çalışan,
> ücretsiz ve Türkçe bir masaüstü dağıtımıdır. Tauri 2.0 / Rust tabanlı AyazDE 5.0 masaüstü
> ortamıyla gelir ve GPL-3.0 lisanslıdır.
> Depo: {REPO}
> Sürümler: {REL}
> Forum: {FORUM}
> Güvenlik: {SECMAIL}
> Diller: {langs}
> Yüzler: Bostan (varsayılan), Bakır, Cıvata, Arduvaz (ve korunan 4.7 Klasik).

## Temel Bileşenler

20 yerleşik pencere, 559 paketli yazılım mağazası (FAZ 1/2/3 eta-touchdrv, MEB sertifikası,
CUPS/SANE dahil), 24 sistem teması, ZRAM (zstd/lz4) bellek sıkıştırma, ~750 MB canlı sistem
boşta bellek hedefi, yerel Ollama ve bulut uçlu beyaz liste denetimli Ankora AI (33 sabit komut,
26 yardımcı araç, 18 ajan eylemi, 148 Tauri IPC komutu).

## Sayfalar (Türkçe)

{pages_tr}

## Pages (English)

{pages_en}
"""


def webmanifest():
    return json.dumps({
        "name": "Ankora Linux 5.0", "short_name": "Ankora",
        "description": "Devuan 6 Excalibur ve Linux 6.12 LTS üzerinde AyazDE 5.0 masaüstü ile Türkçe Linux dağıtımı.",
        "lang": "tr", "dir": "ltr", "start_url": "./", "scope": "./", "id": "./",
        "display": "browser", "orientation": "any",
        "background_color": "#eef1e2", "theme_color": "#2b5822",
        "categories": ["os", "utilities"],
        "icons": [
            {"src": "assets/img/favicon.svg", "sizes": "any", "type": "image/svg+xml", "purpose": "any"},
            {"src": "assets/img/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "any"},
        ],
    }, ensure_ascii=False, indent=2) + "\n"


def build():
    (ROOT / "404.html").write_text(page404(), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(sitemap(), encoding="utf-8")
    (ROOT / "robots.txt").write_text(robots(), encoding="utf-8")
    (ROOT / "llms.txt").write_text(llms(), encoding="utf-8")
    (ROOT / "site.webmanifest").write_text(webmanifest(), encoding="utf-8")
    for lang in LANGS:
        for key in KEYS:
            out = render(lang, key)
            path = ROOT / (FILES[lang][key] if lang == "tr" else lang + "/" + FILES[lang][key])
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(out, encoding="utf-8")
    print("Tum dosyalar Ankora 5.0 icin uretildi.")


if __name__ == "__main__":
    build()
