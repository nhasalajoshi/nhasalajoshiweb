# Change request: version 3, light design with a bordered portrait

Use this when you need to **apply or verify** the latest design. It states what changed from the previous version (version 2), why, file by file, and how to check that it is right.

## How to use this document

- **Mode A, you have this whole repository.** Version 3 is already implemented in it. Your job is to verify it under real Jekyll, compare it to `docs/reference/*.png`, and fix anything that differs. Use sections 4 and 6.
- **Mode B, you only have the older version-2 repository** (black and white design with a black header, a black banner panel, `hero_layout`, and `ring-glyph`). Apply the changes in section 4 on top of it, then copy the binary files in section 5. (This repository is already on version 3, so the migration patch that came with the handoff is not kept here.) If you have that patch, apply it with:

  ```
  cd <your version-2 repo>
  patch -p1 --dry-run < v2-to-v3.diff    # check first
  patch -p1 < v2-to-v3.diff
  ```

  Then add the new image files, then run the checks in section 6.

## 1. Summary

The site moves from a black-and-white design (black header, black banner panel, black call-to-action band, black footer) to a **light design**. The hero portrait becomes a **bordered cutout on a pale gold card with sparkle strokes**. Home becomes **much less text-heavy** and gains **icons** in the thematic parts.

Reference images: `docs/reference/home-desktop.png` and `home-mobile.png` (after) and `docs/reference/v2-previous-black-and-white/home-desktop.png` (before).

## 2. Why (the client's feedback, in order)

1. The light banner alternative looked good; apply that lighter feel to the whole website.
2. Give the portrait a border like a shared reference (cutout, white outline, colored card, sparkle strokes) and make it look good.
3. Make the color coordination lighter overall.
4. Make the home page much less text-heavy; icons are fine in the thematic parts.

## 3. Before and after

| Area | Version 2 | Version 3 |
|---|---|---|
| Header | Black bar, white text | `--bg` bar with a bottom border, black text, gold underline on the current page |
| Hero | Black text panel beside the full photo; `hero_layout` option (`split` or `light`) | One layout. Text left; bordered cutout portrait on a pale gold card right; sparkles; four-color band along the bottom |
| Hero copy | Headline, subline, two-sentence introduction | Headline, subline (with pale gold highlight), one short line, two buttons |
| Buttons | Gold primary, white outline (on black) | Black solid and black outline only |
| At-a-glance | One long sentence with three highlighted figures | Stats band: four icon bubbles with number and short label |
| Area tiles | Tint tile, ring graphic, name, line, "Explore this area" | Tint tile, colored icon bubble, name, one short line, arrow circle |
| Tile lines | Sentences of 12 to 15 words | 4 to 7 words |
| Project cards | Image, tag, title, role and years, 3 to 5 lines of text, "Learn more" | Image, tag, title, one-line `blurb`, arrow circle |
| Recent writing | Year, title, type and role line | Year and title |
| Call to action | Black band with stripes, gold button | Pale gold band with faint dark stripes, black button |
| Footer | Black | `--surface` with a top border; icon buttons outlined in black |
| About page area headings | Ring glyph | Colored icon bubble |
| Social image | Dark layout | Light layout with the gold portrait card (draft) |

## 4. Changes, file by file

### Added
- `_includes/icon.html`: nine inline SVG icons (`community`, `inclusion`, `data`, `governance`, `calendar`, `layers`, `users`, `ticket`, `arrow`).
- `_includes/sparkles.html`: the decorative SVG over the portrait card.
- `tools/make_sticker.py`, `tools/requirements.txt`: regenerate the bordered portrait (see `docs/ASSETS.md`).

### Removed
- `_includes/ring-glyph.html` (replaced by `.icon-bubble` with `icon.html`).

### Changed
- `_config.yml`: remove `hero_layout`; add `portrait_cutout`, `portrait_cutout_small`, `portrait_cutout_width` (1200), `portrait_cutout_height` (1470); add `tools` and `source-assets` to `exclude`.
- `.gitignore`: add `source-assets/`.
- `_data/pillars.yml`: shorten every `line`; remove the unused `ring` and `highlights` fields.
- `_data/organizations.yml`: remove the unused `pillars` and `note` fields.
- `_data/projects.yml`: add `blurb` to the four featured projects; document the field in the header comment.
- `_includes/head.html`: `theme-color` becomes `#FCF9F6`.
- `_includes/header.html`, `_includes/footer.html`: remove the `on-ink` class.
- `_includes/tile.html`: icon bubble, name, line, arrow circle; the text wrapper is a `div` (valid inside the link). No "Explore" text.
- `_includes/card.html`: use `proj.blurb | default: proj.summary`; remove the role and years line; replace "Learn more" with an `aria-hidden` arrow circle (`.card__go`).
- `index.html`: new hero markup (`.hero__card` with `sparkles.html` and the cutout image with `srcset`), stats band replacing the long sentence, "Recent writing" without the meta line, call to action without `on-ink` and with a black button.
- `about.html`: area headings use `<span class="icon-bubble">` with `icon.html`.
- `assets/css/main.css`: see below.
- `assets/img/og.png`: redrawn (draft).

### `assets/css/main.css`, target state
- **Tokens:** add `--card-bg: #FFD670`; `--stripes` becomes dark lines at 5% and 3%; remove `--on-ink-muted`; remove the `.on-ink` focus helper. Everything else in `:root` is unchanged from version 2 (`--bg #FCF9F6`, `--text #151413`, `--ink #121110`, area colors and tints).
- **Buttons:** only `.btn--ink` (black solid) and `.btn--line` (black outline) plus `.btn--sm`. Remove `.btn--gold`.
- **Header:** `--bg` background, `--line` bottom border, text in `--text`; hover `--tint`; `.hbtn` outlined in `--text`; mobile menu borders use `--line`.
- **Hero:** light background; two columns from 52.01rem (1.1fr and 0.9fr); `.hero__card` 4:5, `--card-bg`, 28px radius, `overflow: hidden`, `isolation: isolate`; image absolutely positioned bottom center at 104% width with `filter: drop-shadow(0 10px 16px rgba(18, 17, 16, 0.16))`; `.sparkles` fills the card; `.hero::after` is the 8px four-color band using the four area tokens. Remove all `.hero__panel`, `.hero--split`, `.hero--light`, `.hero__photo` rules.
- **Stats:** `.stats-band`, `.stats`, `.stat`, `.stat__icon`, `.stat__num`, `.stat__label` (see `docs/DESIGN_SPEC.md`). Remove `.glance*`.
- **Tiles:** `.icon-bubble` (56px; 72px on the lead tile), `.tile a`, `.tile__go`, lead tile horizontal from 52.01rem. Remove `.tile__ring`, `.tile__cta`.
- **Cards:** colored top edge, `.card__text` clamped to 3 lines, `.card__go` arrow circle that turns black on hover. Remove `.card__cta`, `.card__meta`.
- **Call to action and footer:** light, as in the before and after table.
- **Delete dead rules:** `.ring-glyph`, `.expertise*`, `.card__meta`, anything referencing `on-ink`.

## 5. New binary files (copy these; they are not in the diff)

| File | Notes |
|---|---|
| `assets/img/nhasala-sticker.webp` | 1200 x 1470, 177 KB, transparent, white outline baked in |
| `assets/img/nhasala-sticker-600.webp` | 600 x 735, 52 KB |
| `assets/img/og.png` | Replaced (draft) |
| `source-assets/Nhasala_Joshi.jpg` | Private original; keep out of public git |

The plain portrait files from version 2 (`nhasala-joshi.jpg`, `nhasala-joshi-700.jpg`) are unchanged and still used on the About page.

## 6. Acceptance criteria and checks

**Visual** (compare to `docs/reference/*.png` at 1280px and 390px):
1. Header, call to action, and footer are light. No black section anywhere. Black appears only in text, buttons, and the arrow circles on hover.
2. Hero: headline, highlighted subline, one muted line, two black buttons on the left; the bordered portrait on a pale gold card with sparkles on the right; four-color band along the bottom. On phones the text comes first and the card follows, centered.
3. Stats band shows four icon bubbles with numbers 10+, 14, 200+, 1,000+ and short labels.
4. Four tiles with icon bubbles, names, and one short line each; community is the wide lead tile with a gold tint. The whole tile is clickable and goes to `/about/#<id>`.
5. Four project cards with area tag, title, one-line blurb, and an arrow circle; the whole card is clickable and goes to `/projects/#<project id>`.
6. Recent writing shows year and title only.
7. No horizontal scroll at 320, 390, 768, 1024, 1280, and 1440px.

**Code checks** (run from the repository root):

```
sh tools/check.sh      # dashes, funder names, leftovers from earlier versions, first person, launch placeholders
bundle exec jekyll build   # expect no errors or warnings
```

`tools/check.sh` covers these specific expectations for version 3: no `.on-ink` class, no `btn--gold`, `ring-glyph`, `hero_layout`, `hero__panel`, or `hero-art` anywhere; no em or en dashes; no funder names in published files. It prints the launch placeholders (`example.com`, the draft switches) as warnings only.

**Behavior:**
- Menu button opens and closes the mobile menu; Escape closes it and returns focus.
- `/projects/#governance` filters to governance projects; `/projects/#mulcam` scrolls to that project.
- Copy buttons on the Writing and speaking page copy the bios.
- Keyboard: Tab reaches every tile and card, and a clear outline appears around the whole tile or card.

**Accessibility:** footer icon buttons have accessible names ("Email Nhasala", "Nhasala on LinkedIn"); hero image has alt text; sparkles and icons are `aria-hidden`; Lighthouse accessibility 100.

## 7. Out of scope for this change

- Restyling the About page portrait as a bordered cutout (open question, `docs/DECISION_LOG.md`).
- A new favicon.
- Final social preview artwork.
- Any new content. Copy changes in this version are shortenings only.
- Self-hosting fonts (a planned task in `docs/TASKS.md`).

## 8. Known risks to check under real Jekyll

- `{% case include.name %}` inside `icon.html` and `{% include icon.html name=pil.id %}` (parameter passing).
- `{% unless cutout and cutout != "" %}` in `index.html` (compound condition in `unless`).
- `{{ proj.blurb | default: proj.summary }}` when `blurb` is missing.
- The `srcset` and `sizes` attributes built from config values.
- Variable names inside includes (`pil`, `proj`) must not collide with page variables (Liquid `assign` leaks).
- `-webkit-line-clamp` on `.card__text` renders correctly in current Chrome, Safari, and Firefox.
