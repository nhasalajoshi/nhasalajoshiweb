# Design spec (version 3: light design with a bordered portrait)

This describes the design as built. The screenshots in `docs/reference/` are the visual source of truth; this file explains the intent and the rules behind them.

## 1. Intent

**Subject.** A personal site for an engineer turned development practitioner who leads a women-in-tech nonprofit in Nepal and works on inclusion, digital rights, data, and internet governance.

**Audience.** Partners, event organizers who might invite her to speak, journalists, collaborators, and prospective fellows. Many will use phones on variable connections.

**Primary jobs.** (1) Show clearly what Nhasala does and has built. (2) Make it easy to invite her to speak or collaborate. (3) Give organizers a ready speaker kit.

**Character.** Light, warm, confident, and friendly. A warm-white page with black text, and one accent color per area of work (gold, magenta, green, violet). The hero portrait is a bordered cutout on a pale gold card with sparkle strokes: a playful, sticker-like touch that keeps the site human. The base colors come from the black and white shirt in her portrait, and fine vertical stripes (used once, on the call-to-action band) nod to the shirt's stripe.

**Text discipline.** The site should feel quick to scan. Home is icon-led and uses very little copy (see section 4). Longer prose lives on the About page.

**Avoid** (calibrated against generic generated design): dark sections, cream-and-terracotta palettes, stock or generated imagery in place of her real portrait, monospace labels, all-caps eyebrow labels, numbered markers on non-sequences, arrow characters in link text, middle dots between meta items, gradient washes as decoration, heavy shadows, scroll-triggered fade-ins.

## 2. Design tokens

All tokens are CSS custom properties at the top of `assets/css/main.css`.

### Color

| Token | Value | Use |
|---|---|---|
| `--bg` | `#FCF9F6` | Page background (warm white) |
| `--photo-bg` | `#FDFAF7` | Backdrop tone of the original photo (kept for reference) |
| `--surface` | `#FFFFFF` | Cards, stats band, footer |
| `--tint` | `#F2EEE9` | Alternate section background, icon bubbles on stats |
| `--text` | `#151413` | Body text |
| `--muted` | `#5A544E` | Secondary text |
| `--line` | `#DDD7D0` | Borders and dividers |
| `--ink` | `#121110` | Black buttons and the arrow-circle hover state (never a section background) |
| `--ink-2` | `#272320` | Hover on black buttons |
| `--on-ink` | `#FBF8F5` | Text on black buttons |
| `--focus` | `#121110` | Focus outline |
| `--card-bg` | `#FFD670` | The pale gold card behind the hero portrait |
| `--stripes` | two repeating vertical line gradients, dark at 5% and 3% | Quiet texture on the call-to-action band only |

### Areas of work (one color each)

| Area | id | Color | Tint | Icon |
|---|---|---|---|---|
| Community and ecosystem building (lead area) | `community` | `--c-community` `#F5B82E` gold | `--t-community` `#FDF0CF` | three connected nodes |
| Inclusion | `inclusion` | `--c-inclusion` `#E0408F` magenta | `--t-inclusion` `#FCDDEB` | two overlapping circles |
| Digital rights, data, and civic tech | `data` | `--c-data` `#16906A` green | `--t-data` `#D7F0E6` | bar chart |
| Internet governance | `governance` | `--c-governance` `#8B5CF6` violet | `--t-governance` `#E7DEFB` | globe |

Apply with `.p-community`, `.p-inclusion`, `.p-data`, `.p-governance`. They set `--pc` (color) and `--pt` (tint) for the element and its children.

Rules:
- Area colors are never used for text. Every area is also named in words (badge, heading), so color is never the only signal.
- Where a brighter variant is needed for the thin four-color bands, the band uses the same four tokens.
- Re-check contrast for any new pair.

Measured contrast (WCAG ratios): body text on page 17.5:1; muted text on page 7.1:1, on tint 6.5:1, on white 7.5:1; text on the area tints 14.2 to 16.3:1; white text on a black button 17.8:1; focus ring on page 18:1. Icons on the area bubbles (black on color) are 10.6:1 on gold, 4.8:1 on magenta, 4.7:1 on green, and 4.5:1 on violet, all above the 3:1 needed for graphics. The gold edge against the pale page (1.7:1) is acceptable only because it is decorative and always paired with a text label.

### Type

| Role | Family | Notes |
|---|---|---|
| Display (headings, tagline, statements, stat numbers) | Bricolage Grotesque, 500 and 700 | `--font-display`, tight tracking (-0.015em to -0.035em) |
| Text | Atkinson Hyperlegible, 400, 700, 400 italic | `--font-text`, chosen for legibility by low-vision readers |
| Devanagari | Noto Sans Devanagari | In both font stacks as a fallback. Load the web font when Nepali content is added. |

Scale (fluid):

| Element | Size |
|---|---|
| Body | 1.125rem (18px), line-height 1.65 |
| Hero h1 | `clamp(2.7rem, 11vw, 3.75rem)`; from 52.01rem `clamp(2.6rem, 4.6vw, 4.25rem)` |
| Page h1 | `clamp(2.4rem, 6.5vw, 4.25rem)` |
| h2 | `clamp(1.7rem, 3.6vw, 2.4rem)` |
| h3 | 1.25rem (tile 1.3rem, lead tile `clamp(1.6rem, 3.2vw, 2.2rem)`, card 1.2rem) |
| Lede | `clamp(1.15rem, 2.2vw, 1.4rem)`, muted |
| Statement | display face 500, `clamp(1.2rem, 2.4vw, 1.5rem)`, max 44ch |
| Stat number | display face 700, `clamp(1.6rem, 3vw, 2.1rem)` |

Prose line length is capped at 62 to 68ch.

### Space, shape, layout

- Container `.wrap`: max 1120px, horizontal padding `--gutter` = `clamp(1rem, 4.5vw, 2.25rem)`.
- Section rhythm `.band`: vertical padding `clamp(2.75rem, 7vw, 5rem)`.
- Radius `--radius` 6px for images, cards, tiles, panels. Buttons are pills (999px). Icon buttons and bubbles are circles. **One deliberate exception:** the hero portrait card uses 28px to read as a sticker card.
- No heavy shadows. The only shadow is a soft `drop-shadow` under the cutout portrait. Depth otherwise comes from color blocks, borders, and the colored top edge on cards.
- Alternate section backgrounds: `--bg`, `--tint`; stats band and footer on `--surface`; call-to-action on `--t-community`.

### Breakpoints (rem)

| Breakpoint | Behavior |
|---|---|
| max 52rem (832px) | Menu collapses behind a "Menu" button (when JS is on). Hero stacks: text first, then the portrait card centered. Tiles, about columns, and area blocks stack. |
| min 52.01rem | Hero becomes two columns (text 1.1fr, card 0.9fr; card aligned right). Tiles become 3 across with the lead tile full width and horizontal. About page becomes two columns with a sticky aside. Area blocks become two columns. |
| min 40rem (640px) | `.row` and `.entry` gain a left meta column (11rem and 12.5rem). |
| min 64rem (1024px) | `.entry` gains a third column for the project image (15rem). |

Test widths: 320, 390, 768, 1024, 1280, 1440.

### Motion

None, except `scroll-behavior: smooth` when the user has not asked for reduced motion. Hover states are color, underline thickness, outline, and the arrow bubble turning black. Do not add scroll-triggered or entrance animations without asking.

## 3. Imagery and icons

Details and regeneration steps are in `docs/ASSETS.md`.

- **Hero portrait:** a transparent WebP cutout with a white outline baked into the image (`assets/img/nhasala-sticker.webp` at 1200px wide and `-600.webp` at 600px). It sits bottom-aligned and centered in the gold card at 104% of the card width, so it bleeds slightly past the sides.
- **Sparkles:** `_includes/sparkles.html`, a decorative SVG over the card (viewBox 480 by 600, `slice`): three short black stroke bursts, one plus sign, and three small colored dots (magenta, green, violet). `aria-hidden`.
- **Icons:** `_includes/icon.html`, one inline SVG per name, 24 by 24, stroke 1.8, round caps, `currentColor`, `aria-hidden`.

| Icon name | Used for |
|---|---|
| `community`, `inclusion`, `data`, `governance` | The four area tiles and the About page area headings |
| `calendar`, `layers`, `users`, `ticket` | The four stats (years, cohorts, professionals, attendees) |
| `arrow` | The "go" circles on tiles and cards |

- **Plain portrait:** the About page uses the regular photo (`assets/img/nhasala-joshi.jpg`, with a 700px copy for `srcset`) at 4:5. Restyling it as a bordered cutout is a pending design decision (see `docs/TASKS.md`).

## 4. Components

All class names are in `assets/css/main.css`. Markup lives in `_includes/` and the page files.

| Component | Classes and file | Behavior and rules |
|---|---|---|
| Header | `.site-header`, `.brand`, `.nav`, `.hbtn.nav-toggle` in `_includes/header.html` | Sticky, `--bg` background, bottom border. Brand is text only. Current page has `aria-current="page"` and a gold underline (a gold left bar in the mobile menu). The "Menu" button appears only when JS is on and width is 52rem or less. Escape closes it. |
| Hero | `.hero`, `.hero__inner`, `.hero__text`, `.hero__card`, `.hero--nophoto` in `index.html` | Left: h1, subline with a pale gold highlighter underline (`.hero__sub span`), one muted line (max 40ch), two buttons (black solid, black outline). Right: `.hero__card`, 4:5, `--card-bg`, 28px radius, `overflow: hidden`, holding `.sparkles` and the cutout `img` (soft drop-shadow). A four-color band (`.hero::after`, 8px) runs along the bottom. `hero--nophoto` is added automatically when `portrait_cutout` is empty. |
| Stats | `.stats-band`, `.stats`, `.stat`, `.stat__icon`, `.stat__num`, `.stat__label` | One row on `--surface`: a 52px circular icon bubble (on `--tint`), a big number, a short label. Four items in an auto-fit grid. |
| Section heading rule | `main h2:not(.row__year)::after` | A 4.5rem by 6px four-color rule under every `h2` in `main` except `.row__year`. |
| Icon bubble | `.icon-bubble` | A 56px circle in the area color (`--pc`) with a black icon. Used on tiles (72px on the lead tile) and About area headings. |
| Area tiles | `.tiles`, `.tile`, `.tile--lead`, `.tile__text`, `.tile__line`, `.tile__go` in `_includes/tile.html` | The whole tile is one link to `/about/#<area id>`. Tint background, icon bubble, name, one short line, and a white arrow circle at the bottom right that turns black on hover. Hover also adds a 2px area-colored inset outline on a white background. The lead tile (community) spans all columns and lays out horizontally on wide screens. |
| Project cards | `.cards`, `.card`, `.card__media`, `.card__body`, `.card__text`, `.card__go` in `_includes/card.html` | Equal cards in an auto-fit grid (min 15rem), colored top edge. Image slot (16:10), area badge, title, a one-line blurb (`blurb` field, falls back to `summary`, clamped to 3 lines), and an arrow circle. The whole card is clickable through a stretched pseudo-element on the title link; the arrow is `aria-hidden`. Focus shows an outline around the whole card. |
| Badge | `.badges`, `.badge` in `_includes/badge.html` | Area tint background, colored dot, area label. Renders as `<li>`; always place it inside `<ul class="badges">`. |
| Draft flag | `.draft` in `_includes/flag.html` | A small dashed "Check" tag on any item with `verified: false`, shown only while `show_draft_flags` is true. |
| Image placeholder | `.ph` in `_includes/placeholder.html` | Dashed box with a label. Replaced by a real image when the data field is filled. |
| Rows | `.rows`, `.row`, `.row__year`, `.row__title`, `.row__meta`, `.rows--compact` | Left meta column (year or label), right content, hairline dividers. Used for writing, talks, roles, recognition, contact options. |
| Buttons | `.btn`, `.btn--ink`, `.btn--line`, `.btn--sm` | Pills, 48px minimum height (44px small). Black solid and black outline only. |
| Text link | `.textlink` | Bold, underlined. Link text names the destination. |
| Call to action | `.cta` | Pale gold (`--t-community`) band with the faint stripe texture, a large heading with the four-color rule, and one black button. |
| Footer | `.site-footer`, `.footer__tagline`, `.footer__links`, `.icon-link`, `.footer__base` | `--surface` background, top border. Tagline on the left. Email and LinkedIn as 48px circular outline icon buttons on the right (icon-only, with `aria-label` and `title`); they turn black on hover. License line below. |
| About layout | `.about`, `.about__aside`, `.about__main`, `.facts`, `.path` | Portrait and quick facts in a sticky left column on wide screens; story and a four-step vertical path (engineer, community builder, institution leader, policy voice) on the right. The path is a real sequence, so a timeline is appropriate there. |
| Area block | `.area-block`, `.area-block--lead`, `.area-block--plain`, `.area-cols`, `.inline-list`, `.statement` | One per area on the About page, with an anchor id equal to the area id. Heading with an icon bubble sticks on the left on wide screens. The community block has a gold left edge and tint background. |
| Projects page | `.filters`, `.chip`, `.count`, `.entries`, `.entry`, `details`, `.steps` | Filter chips (JS only). Each entry has a meta column, body with a "Problem, approach, and result" disclosure, and an image slot. `:target` gives the entry a white background. |
| Speaker kit | `.topics`, `.bios`, `.bio`, `.copy-status` | Topics list, short and long bio each with a copy button, and a status line announced politely to screen readers. |

## 5. Pages

Reference screenshots: `docs/reference/<page>-desktop.png` and `<page>-mobile.png`.

### Home (`index.html`)
1. Hero (see Components).
2. Stats band: 10+ years leading WLiT, 14 fellowship cohorts, 200+ women tech professionals, 1,000+ attendees at flagship events.
3. "Four areas of work": tiles from `_data/pillars.yml` (community is the lead tile).
4. "Selected projects": heading with a "See all projects" link at the right, then cards for every project with `featured: true` (one per area, so four) on the `--tint` background.
5. "Recent writing": first three items of `_data/writing.yml` (year and title), then a link to the writing page.
6. Call to action: "Invite Nhasala to speak, advise, or collaborate."

### About (`about.html`)
1. Page head with lede.
2. Two columns: plain portrait and facts (`_data/about.yml` glance) beside four paragraphs of story and the four-step path.
3. "Areas of work" (`id="areas"`): one `.area-block` per area with the statement, "What this looks like", "Expertise" (`_data/expertise.yml`), "Organizations", "Selected projects", and a link to the filtered projects page. A final plain block lists "Leadership and operations".
4. "Roles and affiliations": rows from `_data/organizations.yml`.

### Projects (`projects.html`)
Filter chips, a live count, then one `.entry` per project from `_data/projects.yml`. Filtering is by hash (`#community`, `#inclusion`, `#data`, `#governance`); any other hash matching an entry id scrolls to that entry with everything visible. Without JS, all entries show.

### Writing and speaking (`writing.html`)
Publications, Speaking and convening, Speaker kit (topics, short and long bio with copy buttons, download placeholders), Recognition. Section ids: `publications`, `speaking`, `speaker-kit`, `recognition`.

### Contact (`contact.html`)
Four collaboration types (speaking, advisory, partnerships, mentoring), each with a `mailto:` link and a prefilled subject. A list of what to include in a first message. Email and LinkedIn. An accessibility contact line. No form, no phone number.

### 404 (`404.html`)
Short message and three links.

## 6. Interaction (`assets/js/main.js`)

1. **Menu toggle.** `.nav-toggle` toggles `.nav-open` on the header and `aria-expanded`. Escape closes it and returns focus. Clicking a nav link closes it.
2. **Project filter.** Reads and writes the URL hash with `history.replaceState`. Updates `aria-pressed` on chips and the polite count text. Responds to `hashchange`.
3. **Copy buttons.** `[data-copy="<element id>"]` copies that element's text with the Clipboard API, falls back to `execCommand`, and announces the result in `[data-copy-status]`.
4. The `js` class is added to `<html>` by an inline script in `head.html`; CSS uses `.js` to show or hide enhancements.

## 7. Accessibility requirements

- Skip link to `#main`; one `h1` per page; headings in order; landmarks labelled.
- Visible focus on every interactive element (3px outline, offset 3px). Stretched-link cards show the outline around the whole card.
- Touch targets at least 44px (icon buttons are 48px).
- Icon-only controls (footer email and LinkedIn) have `aria-label`s. Decorative icons and the sparkles are `aria-hidden`.
- The hero portrait has alt text from `portrait_alt` in `_config.yml`.
- Reduced motion respected. No autoplay.
- Color is never the only signal.
- Works at 200% zoom and 320px width without horizontal scroll.
- Target: Lighthouse accessibility 100, no axe violations.

## 8. SEO and sharing (`_includes/head.html`)

Title pattern `Page | Nhasala Joshi` (home: `Nhasala Joshi: Building inclusive tech ecosystems`). Meta description, canonical URL, Open Graph and Twitter card tags using `assets/img/og.png` (1200 by 630, a draft in the light design; replace with final artwork), `rel="license"`, `theme-color` `#FCF9F6`, and a schema.org `Person` JSON-LD block (job title, employer WLiT, location, LinkedIn). `robots.txt` and the `robots` meta tag follow `robots_noindex`. `jekyll-sitemap` generates the sitemap.

Disambiguation matters: other organizations use the acronym WLiT, so spell out "Women Leaders in Technology (WLiT), Nepal" wherever it first appears on a page.
