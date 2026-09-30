# DESIGN.md — Ankora Linux 2.0 + Ayaz (tanıtım metni v1)

Kaynaklar (sahipleri kullanıcıdır, bu dosya yalnız formatlar):
1. Kullanıcının tanıtım metni: Devuan SysVinit tabanı, Ayaz masaüstü (Rust çekirdek, Tauri 1.5, WebKitGTK, openbox), gerçek sayılar ilkesi, oturum kaydı ve güvenli kip, atomik güncellemeler, izin listeli yapay zeka ajanı, hibrit canlı ISO ve .deb, SHA256, GPL-3.0, GitHub Ankora-Linux/Ayaz, güncel sürüm 2.0.
2. Kullanıcının sürüm şeması: eski 01.0 ve 02.0 Zümrüt, güncel 2.0.
3. Logo ve masaüstü fotoğrafı kullanıcıdan gelir.

## Kimlik
- Ürün: Ankora Linux 2.0 güncel, Ayaz masaüstü ortamıyla. Liste yok, tek sürüm anlatısı.
- Logo: mavi daire, A formu, iç dağlar. Header ve footerda aynı SVG jest olarak tekrarlanır.
- Motif: dağ silüeti çizgisi ve dev kontur numerals (bölüm numaraları, footer ANKORA). Neden: ürüne ait jestler, stok grid değil.

## Palet (2 core + 1 accent, R-29)
- Core 1 grafit: #070B12 (koyu tema). Neden: gece premium yönü.
- Core 2 kemik: #F2EFE7 (açık tema). Neden: ferah okuma zemini.
- Accent Ankora mavisi: koyu temada #2E9BEB, açık temada #005A9C (neden: açık zeminde kontrast, R-25). Yalnız birincil eylem, aktif durum ve gerçek durum noktasında.
- Yasak: mavi-mor gradyan, cam üstüne cam, her yerde parlama. Gradyan yok, düz renk var.

## Tipografi (R-06)
- Display Sora (700,800): Neden: köşeli A kesitleri logodaki A formunu andırır.
- Body IBM Plex Sans (400,500): Neden: teknik belge sesi, güçlü TR glif.
- Mono IBM Plex Mono (500): Neden: sürüm ve yol damgaları teknik etiket olarak okunur.

## Dial
Reading this as: distro landing for TR teknik kullanıcı, Ayaz dağ kimliği stili, dial ENERGY 3 / RHYTHM 3 / MOTION 2.
- ENERGY 3: dev manşet (9.5rem üstü değil, 8.5rem kapak), tam geniş hero.
- RHYTHM 3: hero, manifesto, bilet, düzyazı, satır listeler, vitrin, zaman çizgisi, SSS, liste. Hiçbir bölüm aynı kalıpta değil.
- MOTION 3: giriş koreografisi (hero kademeli belirir), hafif paralaks (hayalet sayılarda derinlik), imleç ışığı (odak), scrollspy (konum). Neden: hepsi tek seferlik veya konuma bağlı, sonsuz döngü yok. Azaltılmış hareket ve noscript yedeği var.

## Yön (kullanıcı seçimi, 29 Eyl 2026)
- Gece premium: koyu zemin, dev tipografi, mavi vurgu.
- Parlama yalnız hero penceresinde (R-13, 1 öğe, neden: ana odak). Footer noktasındaki mavi tek vurgu anıdır.

## Varlıklar (R-23, R-38)
- `logo.png`: kullanıcının logosu. Varsa img görünür, yoksa aynı jestteki inline SVG görünür.
- `ayazde-masaustu.png`: kullanıcının masaüstü fotoğrafı. Varsa img görünür, yoksa dosya adlı dürüst yer tutucu görünür.
- Sayılar yalnız metinden: sürüm 2.0, Ayaz, SysVinit, GPL-3.0, Tauri 1.5, 01.0 ve 02.0 Zümrüt geçmişi. Ölçülmemiş performans iddiası yok.
