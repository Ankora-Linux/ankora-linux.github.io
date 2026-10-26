#!/usr/bin/env python3
"""Ankora Linux web sitesi gorsel varliklarini hazirlar.

Kaynak dosyalar kullanicinin deposundan gelir; burada yalnizca boyutlandirma,
sikistirma ve kucuk ikon turetilir. Yeni gorsel tasarlanmaz.

Kaynaklar:
  logo.png               -> logo-128.png, logo-512.png, apple-touch-icon.png
  ayazde-masaustu.png    -> ayaz-masaustu.png
  desktop-preview.jpg    -> ankora-karsilayici.jpg
  wallpaper-mountain.jpg -> ankora-duvar.jpg
  ankora-temalar.jpg     -> ankora-temalar.jpg
  ankora-ai.jpg          -> ankora-ai.jpg

Calistirma:  python3 assets/make-images.py <kaynak-dizini>
"""

import os
import shutil
import struct
import sys

try:
    from PIL import Image
except ImportError:
    Image = None

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "img")

MAX_W = {
    "ayaz-masaustu.png": 1400,
    "ankora-karsilayici.jpg": 1400,
    "ankora-duvar.jpg": 1400,
    "ankora-temalar.jpg": 1400,
    "ankora-ai.jpg": 1400,
}


def image_dims(path):
    with open(path, "rb") as f:
        data = f.read(32768)
    if data[:8] == b"\x89PNG\r\n\x1a\n":
        w, h = struct.unpack(">II", data[16:24])
        return w, h
    if data[:2] == b"\xff\xd8":
        i = 2
        while i < len(data) - 9:
            if data[i] != 0xFF:
                i += 1
                continue
            marker = data[i + 1]
            if marker in (0xC0, 0xC1, 0xC2):
                h, w = struct.unpack(">HH", data[i + 5 : i + 9])
                return w, h
            length = struct.unpack(">H", data[i + 2 : i + 4])[0]
            i += 2 + length
    return (1400, 875)


def scaled_logo(src, size, out):
    dst = os.path.join(OUT, out)
    if Image is not None:
        im = Image.open(src).convert("RGBA")
        im = im.resize((size, size), Image.LANCZOS)
        im.save(dst, "PNG", optimize=True)
    elif not os.path.exists(dst):
        shutil.copy2(src, dst)
    return out


def photo(src, out, max_w, quality=82):
    dst = os.path.join(OUT, out)
    if Image is not None:
        im = Image.open(src).convert("RGB")
        if im.width > max_w:
            h = round(im.height * max_w / im.width)
            im = im.resize((max_w, h), Image.LANCZOS)
        im.save(dst, "JPEG", quality=quality, optimize=True, progressive=True)
        return out, im.size
    shutil.copy2(src, dst)
    return out, image_dims(dst)


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
        ("ankora-temalar.jpg", "ankora-temalar.jpg"),
        ("ankora-ai.jpg", "ankora-ai.jpg"),
    ):
        p = os.path.join(src_dir, source)
        if not os.path.exists(p):
            print(f"ATLANDI (bulunamadi): {source}")
            continue
        if name.endswith(".jpg"):
            out, size = photo(p, name, MAX_W[name])
            print(f"{out:28} {size[0]}x{size[1]}")
        else:
            dst = os.path.join(OUT, name)
            if Image is not None:
                im = Image.open(p).convert("RGB")
                if im.width > MAX_W[name]:
                    h = round(im.height * MAX_W[name] / im.width)
                    im = im.resize((MAX_W[name], h), Image.LANCZOS)
                im.save(dst, "PNG", optimize=True)
                size = (im.width, im.height)
            else:
                shutil.copy2(p, dst)
                size = image_dims(dst)
            print(f"{name:28} {size[0]}x{size[1]}")
        made.append(name)

    for name in made:
        p = os.path.join(OUT, name)
        print(f"  {name:28} {os.path.getsize(p) // 1024} KB")


if __name__ == "__main__":
    main()
