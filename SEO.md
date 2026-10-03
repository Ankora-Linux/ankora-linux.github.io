# Arama motoru ve yayın rehberi

Bu dosya, `ankora-linux.github.io` adresinde yayımlanan site için eklenen arama motoru
kodlarının ne olduğunu ve Google'ın siteyi indekslemesi için hâlâ ne yapılması gerektiğini
anlatır. Kısa tutuldu: kod ne yapıyor, sen ne yapıyorsun.

## Dürüst uyarı

Kod tek başına sıralamayı belirlemez. Google sıralamasının ana girdileri hâlâ şunlardır:
başka sitelerden gelen bağlantılar, arama talebinin gerçekten karşılanması ve sayfanın
kullanıcıya faydalı olması. Buradaki kodlar "Google botu gelsin ve sayfayı doğru anlasın"
kısmını çözer. Botları çağırmak için Search Console'a kayıt olmak gerekir, robots.txt tek
başına yetmez.

Ayrıca: Google, Ağustos 2023'ten beri SSS (FAQ) yapılandırılmış verisini zengin sonuç olarak
yalnızca devlet ve sağlık sitelerine gösteriyor. Buradaki `FAQPage` işaretlemesi geçerli ve
anlamsal olarak yardımcıdır, ancak bu sitede görsel bir SSS kutusu olarak çıkmayı
garanti etmez.

## Eklenen dosyalar

| Dosya | Ne yapar |
| --- | --- |
| `robots.txt` | Tüm botlara açık. Googlebot, Googlebot-Image, Googlebot-News ve Bingbot grupları açıkça yazıldı. Reklam botları (AdsBot-Google) engellendi, bu sitede reklam sayfası yok. Sitemap adresi bildirildi. |
| `sitemap.xml` | Tek sayfa, `lastmod` ve öncelik bilgisiyle. Google'a "şu adresi tara" demenin en temiz yolu. |
| `site.webmanifest` | Ad, kısa ad, tema rengi ve ikon. Mobilde "uygulamaya ekle" davranışı için. |
| `favicon.svg` | Logo jestinin tek başına dosya hâli. Sekme ikonu ve manifest ikonu bunu kullanıyor. |
| `og-cover.png` | 1200x630 paylaşım görseli. WhatsApp, X, Facebook ve LinkedIn'de bağlantı paylaşıldığında görünür. |
| `index.html` | Semantik yapı, meta etiketleri, yapılandırılmış veri, performans düzeltmeleri. |

## `index.html` içinde yapılanlar

**Meta ve paylaşım:** `canonical`, `robots` (tüm önizleme açık), `author`, `referrer`,
`color-scheme`, `theme-color`, tam Open Graph seti (`og:title`, `og:description`, `og:url`,
`og:image` ve boyutları), Twitter kartı `summary_large_image`. Hepsi 2.0 AyazDE sürüm
adını taşıyor.

**Yapılandırılmış veri (JSON-LD):** Tek bir `@graph` içinde altı düğüm:
`WebSite`, `Organization`, `WebPage`, `SoftwareApplication`, `SoftwareSourceCode` (Ayaz) ve
`FAQPage`. Görünen metinlerle birebir eşleşecek şekilde yazıldı; Google bu uyumsuzluğu cezalandırır.
`SoftwareApplication` içinde `downloadUrl`, `Organization.sameAs` içinde ise
`Ankora-Linux/Ankora-Linux` (indirme deposu) ve `Ankora-Linux/Ayaz` (kaynak kodu) ayrı ayrı
listeleniyor.

**Semantik:** Bölümler `<section aria-labelledby>` ile etiketlendi, sürüm kartı `<article>`,
ekran görüntüleri `<figure>`/`<figcaption>`, teknik yığın ve sürüm özeti `<dl>`/`<dt>`/`<dd>`.
Başlık sırası h1 → h2 → h3 olarak kesintisiz. Görsellerde `alt`, boyut (`width`/`height`) ve
`loading="lazy"` var.

**Dizinlenebilirlik:** TR içerik sunucuda gelen HTML'de tam ve okunur durumda. JavaScript çalışmasa
da metinler yerinde. Dil geçişi JavaScript ile çalışıyor (senin tercihin: tek adres), bu yüzden
Google yalnızca TR sürümü indeksler. İngilizce metinler sayfada var ama ayrı adres olmadığı için
İngilizce aramalarda çıkmaz.

**Performans:** Yazı tipleri `display=swap`, hero görselinde `fetchpriority="high"`, alt
görselde tembel yükleme, satır kaymasını (CLS) önlemek için görsel boyutları, okuma ilerleme
çubuğu için `transform` kullanımı, kaydırma dinleyicilerinde `passive`.

## Senin yapman gerekenler (kod değil, hesap adımı)

1. **Dosyaları yükle.** Bu klasördeki 6 dosyanın tamamı, değişmeden `ankora-linux.github.io`
   deposunun köküne gitmeli. `index.html` tek başına yetmez; `sitemap.xml` ve `robots.txt`
   depoda olmazsa Google sitemap'i bulamaz.
2. **Görselleri ekle.** `ayazde-masaustu.png` (Ayaz masaüstü görüntüsü) ve `logo.png`
   dosyalarını köke koy. Şu an yer tutucu metinleri görünüyor, bu bilinçli ve dürüst bir
   durum: dosya yokken sahte görsel gösterilmiyor. Görselleri ekleyince yer tutucular kendiliğinden
   kaybolur.
3. **Search Console'a kaydol.** `search.google.com/search-console` adresine gir, alan adı olarak
   `ankora-linux.github.io` ekle. GitHub Pages siteleri için "URL öneki" (URL prefix) yöntemini
   seç. Doğrulama için `index.html` başındaki yorum satırlarına Search Console'un verdiği kodu
   yapıştır:
   ```html
   <meta name="google-site-verification" content="VERİLEN_KOD">
   ```
4. **Sitemap'i bildir.** Search Console → Sitemaps → `sitemap.xml` adresini gir. `robots.txt`
   içinde de yazılı, ikisi birlikte en hızlı sonucu verir.
5. **Bing Webmaster Tools.** Aynı işlem Bing için de yapılır. `bing-site-verification` satırı
   `index.html` başında hazır bekliyor.
6. **Dış bağlantı iste.** Bu tek başına kod değil: GitHub deposu, forum ve paket açıklamalarından
   siteye bağlantı ekle. Sıralamadaki en büyük fark buradadır.
7. **Güncelleme sonrası** Search Console'da "URL Denetleme" ile sayfayı tekrar taranmaya gönder.

## Alan adı değişirse

`https://ankora-linux.github.io/` adresi üç dosyada geçiyor: `index.html` (canonical, `og:url`,
yapılandırılmış veri içindeki tüm adresler), `robots.txt` (Sitemap satırı) ve `sitemap.xml`
(`<loc>`). Üçünü birlikte güncelle, aksi halde Google eski adresi kanonik kabul eder.

## Düzenli olarak yapılacaklar

- Sürüm değiştiyse `sitemap.xml` içindeki `lastmod` tarihini güncelle. Şu an 2.0 AyazDE
  yayınıyla aynı olan tarih yazılı.
- İndirme bağlantısı tek yerden yönetiliyor: `https://github.com/Ankora-Linux/Ankora-Linux/releases`.
  Sitede 5 ayrı yerde geçiyor (hero butonu, sürüm kartı, ISO kartı, .deb kartı, iletişim
  listesi) ve JSON-LD'de `downloadUrl` ile `sameAs` olarak. Depo adı değişirse hepsini birlikte
  güncelle.
- `index.html` içindeki `<title>` ve `meta description` metinini sürüme göre tazele.
- Forumda veya depoda yeni bir sürüm duyurusu yaparsan, o sayfayı siteya bağla. Sitede
  bağlantısı olmayan içerik indekslenme açısından değersizdir.