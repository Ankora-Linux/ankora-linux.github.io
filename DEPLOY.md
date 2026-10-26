# Siteyi yayınlama: Ankora Linux

Bu klasör, `ankora-linux.github.io` deposunun kökünde yayımlanan statik sitedir.
Çerçeve, derleme adımı ve paket bağımlılığı yoktur. GitHub Pages dosyaları
olduğu gibi sunar.

Yayın adresi: `https://ankora-linux.github.io/`

## Dosya düzeni

```
.
├── index.html  ozellikler.html  kurulum.html  guvenlik.html
├── surum-gecmisi.html  sss.html  iletisim.html  404.html   # Türkçe (kök)
├── en/   de/   es/   ru/           # diğer diller (her biri 7 sayfa)
├── assets/
│   ├── site.css            # tasarım sistemi: iki tema, üç vurgu, ferah ölçek
│   ├── site.js             # tema, vurgu, ayar paneli, mobil menü, kopyalama
│   ├── make-images.py      # brand/ klasöründen web görsellerini üretir
│   └── img/                # logo, ekran görüntüleri, ikon seti, favicon
├── brand/                  # kullanıcının orijinal görselleri (değiştirilmez)
├── build-site.py           # sayfaları ve SEO dosyalarını üretir
├── i18n_extra.py           # de, es, ru metinleri (build-site.py içe alır)
├── llms.txt  robots.txt  sitemap.xml  site.webmanifest  .nojekyll
├── check-site.py           # denetim betiği
└── DEPLOY.md               # bu dosya
```

Sayfa adları dile göre yerelleşir (örnek: `de/funktionen.html`,
`es/seguridad.html`, `ru/ustanovka.html`). Türkçe kök
düzeyde kalır; `x-default` daima Türkçe sürüme işaret eder.

## Yayın adımları

1. Depoyu kopyalayın:

   ```bash
   git clone https://github.com/Ankora-Linux/ankora-linux.github.io.git
   cd ankora-linux.github.io
   ```

2. Bu klasörün içeriğini depo köküne kopyalayın.

3. GitHub'da **Settings → Pages** bölümünü açın.

4. **Source** olarak **Deploy from a branch**, **Branch** için `main`,
   klasör için `/ (root)` seçin, kaydedin.

5. Site `https://ankora-linux.github.io/` adresinde yayınlanır.

`.nojekyll` dosyası Jekyll'in `_` ile başlayan dizinleri gizlemesini engeller.
Site saf HTML, CSS, JS, SVG, PNG ve JPEG içerir.

## Sayfaları üretme

Sayfa iskeletleri ve SEO dosyaları `build-site.py` ile üretilir. Metni
değiştirmek için betiği düzenleyip yeniden çalıştırın; HTML dosyalarını elle
düzenlemeyin, çünkü bir sonraki üretimde üzerine yazılır.

```bash
python3 build-site.py
```

Bu komut beş dilde (tr, en, de, es, ru) yedişer sayfa, `404.html`,
`sitemap.xml`, `robots.txt`, `llms.txt` ve `site.webmanifest` dosyalarını
yeniden yazar. Toplam 36 sayfa, sitemap'te 35 URL.

## Denetim

```bash
python3 check-site.py
```

Denetlenenler:

- kırık iç bağlantı ve bulunmayan çapa
- `icons.svg` içinde tanımsız sembol
- geçersiz JSON-LD
- eksik `lang`, `title`, `description`, `canonical`, `og:*`, `hreflang`,
  `theme-color`, atlama bağlantısı, landmark
- `alt` metni olmayan görsel, `width`/`height` olmayan görsel (CLS)
- tam olarak bir `h1` ve başlık sırası atlamaması
- menüde tam olarak bir `aria-current="page"`, dil seçiminde bir
  `aria-current="true"`
- site haritası kapsamı ve `robots.txt` tutarlılığı
- **R-02** em dash yasağı
- **R-15/R-16** jenerik CTA ve pazarlama buzzword yasağı
- emoji ve kırık karakter (homoglif) taraması
- **DESIGN.md**: blur en çok 14px, saturate en çok 1,5, cam kullanımı yok,
  kırılım ve `prefers-reduced-motion` desteği
- **R-25** WCAG AA kontrastı: altı tema/vurgu bileşiminin (açık-koyu × mavi-yeşil-mor)
  tümü, CSS'teki gerçek renk değerlerinden ölçülür
- **R-17** sayı doğrulama: `ANKORA_AYAZ_DE_ALL_CODES.txt` depoda olduğu
  sürece sayfalardaki her sayı kaynak koddan okunan değerle karşılaştırılır

## Görselleri yeniden üretme

Web görselleri `brand/` klasöründeki orijinal dosyalardan türetilir:

```bash
python3 assets/make-images.py brand
```

`brand/` içindeki dosyalar kullanıcıya aittir, betik onları yalnızca
boyutlandırır ve sıkıştırır. Yeni görsel tasarlanmaz.

## Tasarım

Görsel yön `DESIGN.md` dosyasındadır ve bu sitenin kaynak gerçeğidir.

- **İki tema:** açık (varsayılan) ve koyu. Açık zemin `#FFFFFF`, panel `#F6F8FB`;
  koyu zemin `#0E1420`, panel `#161D2B`. Tema tercihi `localStorage` anahtarı
  `ankora-theme` ile korunur; varsayılan `auto` işletim sistemi ayarını izler.
- **Üç vurgu rengi:** mavi `#0073B8` (varsayılan), yeşil `#157347`, mor `#6D28D9`;
  koyu temada karşılıkları açılır. Tercih `ankora-accent` anahtarında saklanır.
  Zorin'in parlak mavisi `#0092D4` beyaz yazıyla WCAG AA'yı geçmiyor (3.46),
  bu yüzden daha koyu bir ton seçildi.
- **Tek satır menü:** solda marka, sağda bağlantılar, tek "İndir" düğmesi,
  her zaman görünen dil açılır listesi (dünya simgesi + dil kodu, beş dil),
  ayar düğmesi (tema, vurgu) ve mobil menü düğmesi. Dar ekranda gezinme
  katlanır menüye döner.
- **Sade hero ve etkileşimli vitrin:** ortalanmış üst bilgi rozeti (`3.6.0`), tek başlık, kısa açıklama ve iki düğme. Altında Ayaz DE 3.6'nın 5 gerçek ekran görüntüsü (`ayaz-masaustu.png`, `ankora-temalar.jpg`, `ankora-karsilayici.jpg`, `ankora-duvar.jpg`, `ankora-ai.jpg`) arasında geçiş sağlayan sekme vitrini.
- Gradyan ve cam yok. Kartlar açık/koyu yüzey çerçevesi, monospace sıra etiketi, başlık ve metinden oluşur.
- **Ferah ölçek:** bölüm dikey boşluğu `clamp(96px, 10.5vw, 176px)`, gövde
  satır yüksekliği 1,75, ölçü genişliği `64ch`, kabuk `1160px`.
- Giriş animasyonu yok; içerik doğrudan görünür.
- Yazı tipleri: Sora (başlık), IBM Plex Sans (gövde), IBM Plex Mono (etiket/kod).
- Kontrast alt sınırı 4,5; altı tema/vurgu bileşiminde ölçülen en düşük oran 4,76.
- Duyarlı kırılımlar: 1080px (gezinme katlanır), 860px, 560px. All etkileşimli öğeler en az 44×44px dokunma alanına sahiptir.

## Metin kuralları

- Türkçe sayfalar ana dildir (kök); İngilizce `/en/`, Almanca `/de/`,
  İspanyolca `/es/`, Rusça `/ru/` altındadır. En çok kullanılan beş dil.
- Her sayfada beş dilin `hreflang` bağlantısı ve `x-default` (Türkçe) bulunur.
- Metinde em dash kullanılmaz (antislop R-02).
- Süs sayıları ve dekoratif etiketler seyreltilir; kalabalık hissi yaratmaz.
- Sayısal iddialar kaynak kodla doğrulanır. Doğrulanamayan sayı yazılmaz.
- Boşta bellek: kurulu sistemde masaüstüne giriş sonrası `free -m` ölçümü,
  yaklaşık 750 MB. Karşılaştırma tablosu ana sayfada; diğer dağıtımların
  değerleri Android Authority (Ekim 2024) ve Mint incelemesinden alınmış
  yaklaşımlardır, sayfada yöntem ve tarih notuyla belirtilir.
- Uydurma referans, hayali yorum veya ölçülmemiş performans iddiası yok.

## Alan adı değişirse

Adres `https://ankora-linux.github.io/` üç yerde geçiyor:

```bash
grep -rl 'ankora-linux.github.io' --include='*.html' --include='*.xml' \
  --include='*.txt' --include='*.webmanifest' . \
  | xargs sed -i 's#ankora-linux\.github\.io#ayaz.ankora.org#g'
```

`404.html` içindeki `<base href="/">` satırı yeni kök yola göre güncellenir.
Değişiklikten sonra `python3 check-site.py` çalıştırın.

## Arama motoru kaydı

1. `search.google.com/search-console` adresine girin.
2. Alan adı olarak `ankora-linux.github.io` ekleyin, URL öneki yöntemini seçin.
3. Verilen kodu `index.html` içine ekleyin:
   ```html
   <meta name="google-site-verification" content="VERİLEN_KOD">
   ```
4. Sitemaps bölümüne `sitemap.xml` adresini girin.

Detaylı notlar için depodaki `SEO.md` dosyasına bakın.