# Assets

Everything image-related for the current design: what exists, how it was made, how to change it.

## Inventory

| File | Purpose | Size | Notes |
|---|---|---|---|
| `assets/img/nhasala-sticker.webp` | Hero portrait: transparent cutout with a white outline baked in | 1200 x 1470, 177 KB | Used with `srcset`; `portrait_cutout` in `_config.yml` |
| `assets/img/nhasala-sticker-600.webp` | Same, for small screens | 600 x 735, 52 KB | `portrait_cutout_small` |
| `assets/img/nhasala-joshi.jpg` | Plain portrait photo, used on the About page | 1400 x 1750, 284 KB | `portrait`; JPEG quality 82, progressive |
| `assets/img/nhasala-joshi-700.jpg` | Same, for `srcset` | 700 x 875, 72 KB | `portrait_small` |
| `assets/img/og.png` | Social preview (Open Graph and Twitter card) | 1200 x 630 | **Draft.** Light layout: name and tagline left, the gold portrait card right, four-color band along the bottom. Text is set in a system font, not the site fonts. Replace with final artwork. |
| `assets/img/favicon.svg` | Browser tab icon | vector | A black rounded square with a gold dot and magenta and green rings. **Not yet updated for the light design.** Pending client decision (see `docs/TASKS.md`). |
| `source-assets/Nhasala_Joshi.jpg` | The client's original photo | 2415 x 3019, about 1 MB | **Private.** Git-ignored and excluded from the Jekyll build. Do not commit it to a public repository. |

All of `assets/img` is published. `source-assets/`, `tools/`, and `docs/` are not.

## The portrait

- Original: a studio portrait of Nhasala on a near-white warm background, in a black and white striped shirt, 4:5 ratio.
- Alt text (`portrait_alt` in `_config.yml`): "Portrait of Nhasala Joshi". The client may want something more descriptive.
- The plain photo is used on the About page. The hero uses the bordered cutout.
- Never retouch, recolor, filter, or reshape the person. Crop and position only.
- Consent: the client supplied this photo of herself for the site. Any other person's photo (participants, event photos) needs permission and a funder-logo check before use.

## The bordered cutout (how it was made)

Script: `tools/make_sticker.py`. Dependencies: `tools/requirements.txt` (rembg, onnxruntime, opencv-python-headless, pillow, numpy). The script is the only Python in the project and is not part of the site build.

Steps the script performs:
1. Load the original, correct orientation, scale to 1400px wide.
2. Remove the background with `rembg` using the `u2net_human_seg` model, with alpha matting (foreground threshold 240, background threshold 15, erode size 8). The first run downloads about 176 MB of model data.
3. Clean the alpha edge: clip faint values, erode one pixel, blur lightly. This removes the pale fringe around the hair.
4. Build the outline: keep the largest connected shape, pad the canvas (the figure continues downward so no outline shows along the bottom edge), dilate by 24px, close small gaps, smooth, and soften.
5. Compose a white outline layer under the person and export transparent WebP at 1200px and 600px wide (quality 88).

To regenerate or adjust:

```
pip install -r tools/requirements.txt
python3 tools/make_sticker.py                 # defaults: source-assets/Nhasala_Joshi.jpg to assets/img
python3 tools/make_sticker.py --outline 30    # thicker border
```

Running it with the defaults reproduces the shipped files exactly (verified pixel for pixel). If the 1200px output size changes, update `portrait_cutout_width` and `portrait_cutout_height` in `_config.yml`.

Quality notes: a small amount of light fringe can remain on fine hair strands; the white outline hides it. Check the result at full size before accepting a new version.

## The hero card

- Card: `.hero__card`, 4:5, background `--card-bg` `#FFD670` (a soft gold), 28px radius. The cutout is bottom-aligned, centered, 104% of the card width, so the sleeves bleed past the sides and the bottom edge is cropped by the card.
- Backdrop colors tested with the cutout: gold `#F5B82E` (too saturated), soft gold `#FFD670` (chosen), pastel violet `#C4B0FC`, pastel pink `#F7AACD`, pastel mint `#A0DEC4`. Change `--card-bg` to switch.
- Sparkles: `_includes/sparkles.html`. Three bursts of short black strokes (upper left, right middle, upper right), one plus sign, and three dots (violet, magenta, green). Positions are in an SVG viewBox of 480 by 600. The right-middle burst and the plus were placed clear of the shoulder; re-check if the cutout, card size, or crop changes.
- The style (cutout with a white border, colored card, sparkle strokes) was inspired by a reference image of another person that the client shared. **That person's image is not used anywhere.**

## Icons

`_includes/icon.html` holds all icons as one inline SVG per name (`{% include icon.html name="data" %}`). 24 by 24 viewBox, stroke 1.8, round caps and joins, `currentColor`, `aria-hidden`. Names: `community`, `inclusion`, `data`, `governance`, `calendar`, `layers`, `users`, `ticket`, `arrow`. To add one, add a `{% when "name" %}` branch with stroke-only paths in the same style. Icons are decorative; any control that contains only an icon needs an accessible name on its link or button.

The footer's email and LinkedIn icons are written inline in `_includes/footer.html` (the LinkedIn mark is a filled glyph; the email icon is a stroke icon).

## Project and card images

None yet. Cards show a labelled placeholder until `image` and `image_alt` are set on a project in `_data/projects.yml`. Guidance: JPG or WebP, about 1200px wide, compressed, 16:10 on home cards and 4:3 on the Projects page. Check every photo for funder logos on banners and backdrops. Add `width` and `height` attributes when real images arrive to avoid layout shift.

## Fonts

Bricolage Grotesque (500, 700) and Atkinson Hyperlegible (400, 700, 400 italic) load from Google Fonts in `_includes/head.html`. Self-hosting as WOFF2 (both are SIL Open Font License) is a planned task. Noto Sans Devanagari is in the font stacks but not loaded; add the file when Nepali content arrives.
