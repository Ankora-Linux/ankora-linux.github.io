#!/usr/bin/env python3
"""Ankora Linux web sitesi gorsel varliklarini hazirlar.

Kaynak dosyalar kullanicinin deposundan gelir; burada yalnizca boyutlandirma,
sikistirma ve kucuk ikon turetilir. Yeni gorsel tasarlanmaz.

Kaynaklar:
  logo.png               -> logo-128.png, logo-512.png, apple-touch-icon.png
  ayazde-masaustu.png    -> ayaz-masaustu.png
  desktop-preview.jpg    -> ankora-karsilayici.jpg
  wallpaper-mountain.jpg -> ankora-duvar.jpg

Calistirma:  python3 assets/make-images.py <kaynak-dizini>
"""

import os
import sys
from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "img")

MAX_W = {
    "ayaz-masaustu.png": 1400,
    "ankora-karsilayici.jpg": 1360,
    "ankora-duvar.jpg": 1360,
}


def scaled_logo(src, size, out):
    im = Image.open(src).convert("RGBA")
    im = im.resize((size, size), Image.LANCZOS)
    im.save(os.path.join(OUT, out), "PNG", optimize=True)
    return out


def photo(src, out, max_w, quality=82):
    im = Image.open(src).convert("RGB")
    if im.width > max_w:
        h = round(im.height * max_w / im.width)
        im = im.resize((max_w, h), Image.LANCZOS)
    im.save(os.path.join(OUT, out), "JPEG", quality=quality, optimize=True, progressive=True)
    return out, im.size


def main():
    src_dir = sys.argv[1] if len(sys.argv) > 1 else os.path.join(HERE, "..", "brand")
    os.makedirs(OUT, exist_ok=True)
    made = []

    logo = os.path.join(src_dir, "logo.png")
    if os.path.exists(logo):
        made += [
            scaled_logo(logo, 128, "logo-128.png"),
            scaled_logo(logo, 384, "logo-512.png"),
            scaled_logo(logo, 180, "apple-touch-icon.png"),
        ]

    for name, source in (
        ("ayaz-masaustu.png", "ayazde-masaustu.png"),
        ("ankora-karsilayici.jpg", "desktop-preview.jpg"),
        ("ankora-duvar.jpg", "wallpaper-mountain.jpg"),
    ):
        p = os.path.join(src_dir, source)
        if not os.path.exists(p):
            print(f"ATLANDI (bulunamadi): {source}")
            continue
        if name.endswith(".jpg"):
            out, size = photo(p, name, MAX_W[name])
            print(f"{out:28} {size[0]}x{size[1]}")
        else:
            im = Image.open(p).convert("RGB")
            if im.width > MAX_W[name]:
                h = round(im.height * MAX_W[name] / im.width)
                im = im.resize((MAX_W[name], h), Image.LANCZOS)
            im.save(os.path.join(OUT, name), "PNG", optimize=True)
            print(f"{name:28} {im.width}x{im.height}")
        made.append(name)

    for name in made:
        p = os.path.join(OUT, name)
        print(f"  {name:28} {os.path.getsize(p) // 1024} KB")


if __name__ == "__main__":
    main()