"""Generate responsive AVIF + WebP variants from the original source images.

Usage:  python tools/optimize_images.py <source-dir>
Source originals are NOT committed (they are 60+ MB); only the optimized output in
wwwroot/assets/img is. Each manifest entry: output name -> (source file, aspect ratio or None,
focal point y 0..1, list of widths).
"""
import sys, os
from PIL import Image, ImageOps

SRC = sys.argv[1] if len(sys.argv) > 1 else "source-images"
OUT = os.path.join(os.path.dirname(__file__), "..", "wwwroot", "assets", "img")
os.makedirs(OUT, exist_ok=True)

M = {
  # hero
  "hero-wide":        ("b1c9e9_2686bacb6f6c4775b1024e87e36065eb.jpg", 16/9, 0.42, [800, 1200, 1600, 2200]),
  "hero-tall":        ("b1c9e9_2686bacb6f6c4775b1024e87e36065eb.jpg", 4/5,  0.45, [480, 720, 1000]),
  # project cards (4:5)
  "prague-3-card":    ("b1c9e9_2686bacb6f6c4775b1024e87e36065eb.jpg", 4/5,  0.45, [480, 720, 1000, 1400]),
  "ussishkin-46-card":("b1c9e9_516bc2e7ddd94927952cffc79d1b9532.jpg", 4/5,  0.45, [480, 720, 1000, 1400]),
  "ussishkin-52-card":("b1c9e9_5f009ce0c96042b4bc03d67d8d77897c.jpg", 4/5,  0.45, [480, 720, 1000, 1400]),
  "bartenura-card":   ("b1c9e9_427c2d37f45f4f219af9fc77054a2229.png", 4/5,  0.5,  [480, 720, 1000]),
  "berdichevsky-card":("b1c9e9_611d758c40b140e8a8d02663668b93b1.jpg", 4/5,  0.45, [480, 720, 1000, 1400]),
  "marmorek-card":    ("b1c9e9_7db3eaf078f344cba8dd8446f027e760.png", 4/5,  0.5,  [288]),
  # project detail heroes (3:2)
  "prague-3-wide":    ("b1c9e9_2686bacb6f6c4775b1024e87e36065eb.jpg", 3/2,  0.42, [800, 1200, 1600, 2200]),
  "ussishkin-46-wide":("b1c9e9_516bc2e7ddd94927952cffc79d1b9532.jpg", 3/2,  0.42, [800, 1200, 1600, 2200]),
  "ussishkin-52-wide":("b1c9e9_5f009ce0c96042b4bc03d67d8d77897c.jpg", 3/2,  0.40, [800, 1200, 1600, 2200]),
  "bartenura-wide":   ("b1c9e9_427c2d37f45f4f219af9fc77054a2229.png", 3/2,  0.5,  [800, 1150]),
  "berdichevsky-wide":("b1c9e9_611d758c40b140e8a8d02663668b93b1.jpg", 3/2,  0.45, [800, 1200, 1600, 2200]),
  # galleries
  "ussishkin-46-roof":   ("b1c9e9_3876bb1fab6c412d936004bdd6b331e1.png", 16/9, 0.5, [600, 900, 1400, 1900]),
  "ussishkin-46-kitchen":("b1c9e9_916739c53cd34d0c8e8f24f96ab5c510.png", 16/9, 0.5, [600, 900, 1400, 1900]),
  "ussishkin-46-living": ("b1c9e9_a7e2994387464970a2481dc8820f6453.png", 16/9, 0.5, [600, 900, 1400, 1900]),
  "ussishkin-46-bedroom":("b1c9e9_20d16210dee04da3994184eba8d8a75d.png", 16/9, 0.5, [600, 900, 1400, 1900]),
  "yarkon-panorama":     ("b1c9e9_adf81ce82497490f8e69470e35ddf8a9.png", None, 0.5, [800, 1200, 1800, 2600]),
  "yarkon-aerial":       ("818116_b742e65307714e54a6341730226339d2.png", None, 0.5, [600, 900, 1200]),
  "bartenura-2":         ("b1c9e9_7b270db6a4984b85bb7dcb6da8f2cd16.jpg", 4/3,  0.5, [600, 900, 1150]),
  "interior-living":     ("b1c9e9_498a415a315d4b49840c801e8d8bffdd.jpg", 3/2,  0.5, [600, 900, 1200, 1600]),
}

def crop(im, ratio, fy):
    if not ratio: return im
    w, h = im.size
    if w / h > ratio:  # too wide
        nw = int(h * ratio); x = (w - nw) // 2; return im.crop((x, 0, x + nw, h))
    nh = int(w / ratio); y = int((h - nh) * fy); return im.crop((0, y, w, y + nh))

for name, (src, ratio, fy, widths) in M.items():
    im = Image.open(os.path.join(SRC, src)); im = ImageOps.exif_transpose(im).convert("RGB")
    im = crop(im, ratio, fy)
    sizes = []
    for w in widths:
        if w > im.width: continue
        r = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
        r.save(os.path.join(OUT, f"{name}-{w}.webp"), "WEBP", quality=76, method=6)
        r.save(os.path.join(OUT, f"{name}-{w}.avif"), "AVIF", quality=52, speed=4)
        sizes.append((w, r.height))
    print(name, sizes)
