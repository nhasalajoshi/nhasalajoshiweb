#!/usr/bin/env python3
"""Make the bordered ("sticker") portrait used in the home banner.

What it does
  1. Removes the photo background with rembg (model: u2net_human_seg) and a little alpha matting.
  2. Cleans the cutout edge slightly (removes the light fringe around hair).
  3. Builds a smooth white outline around the silhouette. The outline does NOT appear along the bottom
     edge, because the portrait is cropped by the card at the bottom.
  4. Exports transparent WebP files at 1200px and 600px wide.

Usage
  pip install -r tools/requirements.txt
  python3 tools/make_sticker.py                       # uses the defaults below
  python3 tools/make_sticker.py --outline 30          # thicker border
  python3 tools/make_sticker.py --photo path/to/other.jpg --out assets/img

The first run downloads a segmentation model (about 176 MB) from GitHub releases.
Review the result at full size, especially hair edges. Never recolor, retouch, or reshape the person.
"""
import argparse, os
import numpy as np, cv2
from PIL import Image, ImageOps
from rembg import remove, new_session

ap = argparse.ArgumentParser()
ap.add_argument('--photo', default='source-assets/Nhasala_Joshi.jpg')
ap.add_argument('--out', default='assets/img')
ap.add_argument('--name', default='nhasala-sticker')
ap.add_argument('--outline', type=int, default=24, help='outline thickness in px at 1400px width (default 24)')
ap.add_argument('--model', default='u2net_human_seg')
args = ap.parse_args()

# 1. load and cut out (work at 1400px wide)
im = ImageOps.exif_transpose(Image.open(args.photo)).convert('RGB')
im.thumbnail((1400, 1750))
cut = remove(im, session=new_session(args.model), alpha_matting=True,
             alpha_matting_foreground_threshold=240, alpha_matting_background_threshold=15,
             alpha_matting_erode_size=8).convert('RGBA')
W, H = cut.size
arr = np.array(cut)
rgb, a = arr[..., :3], arr[..., 3].astype(np.float32) / 255.0

# 2. clean the alpha edge
a = np.clip((a - 0.10) / 0.90, 0, 1)
a8 = (a * 255).astype(np.uint8)
a8 = cv2.erode(a8, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3)), iterations=1)
a8 = cv2.GaussianBlur(a8, (3, 3), 0)

# 3. outline: dilate the silhouette, close small gaps, smooth the edge
r = args.outline
mask = (a8 > 128).astype(np.uint8) * 255
n, lab, stats, _ = cv2.connectedComponentsWithStats(mask)
if n > 2:  # keep only the largest blob
    keep = 1 + int(np.argmax(stats[1:, cv2.CC_STAT_AREA]))
    mask = ((lab == keep) * 255).astype(np.uint8)
mp = np.pad(mask, ((r, 0), (r, r)), mode='constant')   # padding: top, left, right
mp = np.pad(mp, ((0, r), (0, 0)), mode='edge')          # bottom continues the figure, so no outline shows there
out = cv2.dilate(mp, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (2 * r + 1, 2 * r + 1)))
out = cv2.morphologyEx(out, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61)))
out = cv2.GaussianBlur(out, (0, 0), 5)
out = (out > 127).astype(np.uint8) * 255
out = cv2.GaussianBlur(out, (0, 0), 1.2)[:-r, :]        # drop the bottom padding

# 4. compose: white outline layer, then the person on top
h2, w2 = out.shape
canvas = np.zeros((h2, w2, 4), np.uint8)
canvas[..., :3] = 255
canvas[..., 3] = out
person = np.zeros((h2, w2, 4), np.uint8)
person[r:r + H, r:r + W, :3] = rgb
person[r:r + H, r:r + W, 3] = a8
base = Image.fromarray(canvas, 'RGBA')
base.alpha_composite(Image.fromarray(person, 'RGBA'))

# 5. export
os.makedirs(args.out, exist_ok=True)
for width, suffix in ((1200, ''), (600, '-600')):
    height = round(base.size[1] * width / base.size[0])
    path = os.path.join(args.out, f'{args.name}{suffix}.webp')
    base.resize((width, height), Image.LANCZOS).save(path, 'WEBP', quality=88, method=6)
    print(f'{path}  {width}x{height}  {os.path.getsize(path) // 1024} KB')
print('Update portrait_cutout_width and portrait_cutout_height in _config.yml if the 1200px size changed.')
