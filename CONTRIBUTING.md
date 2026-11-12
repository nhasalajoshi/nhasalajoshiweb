# Contributing

Project guide for anyone working on this site. Read this first. It is short on purpose; the detail is in `docs/`.

## What this is

A personal website for **Nhasala Joshi**, co-founder and Executive Director of Women Leaders in Technology (WLiT), Nepal. She works on inclusive tech ecosystems, digital rights, gender data, civic tech, and internet governance. It is a Jekyll site hosted on **GitHub Pages**. It is written in the **third person**.

The current design is **version 3: a light design with a bordered portrait**.

## Where to look

| File | What it covers |
|---|---|
| `docs/REDESIGN_V3_BRIEF.md` | The change request for the current design: what changed from version 2, file by file, with acceptance criteria |
| `docs/DESIGN_SPEC.md` | The design as built: tokens, type, layout, components, pages, interaction, accessibility |
| `docs/CONTENT_AND_DATA.md` | Every data file and field, where copy lives, content rules, open content items |
| `docs/ASSETS.md` | The portrait, the bordered cutout, icons, sparkles, social image, and how to regenerate them |
| `docs/DECISION_LOG.md` | What the client decided, what was tried and rejected, and why. Read before proposing a change. |
| `docs/TASKS.md` | Ordered work plan with acceptance criteria |
| `docs/reference/*.png` | Screenshots of every page at 1280px and 390px. **This is the visual source of truth.** |
| `docs/reference/v2-previous-black-and-white/` | The previous version, for before and after comparison only. Do not restore it. |
| `README.md` | Client-facing guide: editing content, deploying, launch checklist |

## Stack and constraints

- Jekyll via the `github-pages` gem (Jekyll 3.x, Liquid 4, GitHub-approved plugins only; `jekyll-sitemap` is used).
- **Plain CSS** (`assets/css/main.css`) and **plain JavaScript** (`assets/js/main.js`). No Sass, npm, bundlers, or frameworks on the site. Do not add any unless the client asks.
- All content lives in `_data/*.yml`. Templates render it. Do not hard-code content that has a data home. (Short copy that lives in templates is listed in `docs/CONTENT_AND_DATA.md`.)
- Fonts come from Google Fonts (Bricolage Grotesque, Atkinson Hyperlegible). Self-hosting is a planned task.
- The site must work with JavaScript disabled. JavaScript only enhances (menu toggle, project filter, copy buttons).
- `tools/` (Python, for regenerating the portrait cutout), `source-assets/` (private original photo), `docs/`, and this file are excluded from the published site in `_config.yml`.

## Commands

```
bundle install
bundle exec jekyll serve      # http://localhost:4000
bundle exec jekyll build
sh tools/check.sh             # style and rules check: dashes, funder names, leftovers, first person
```

`tools/check.sh` reads the funder names it searches for from `tools/blocked-names.txt`, which is private and git-ignored. Ask the site owner for it. Never write the names into a tracked file.

## Hard rules (client decisions; do not reverse without asking)

1. **No donor, funder, development agency, bank, embassy, or ministry is named anywhere**: copy, data, alt text, file names, comments, images, docs. Use generic phrases ("development partners", "national government bodies"). Do not link to pages that show funder names or logos.
2. **Third person throughout.** Never "I", "my", or "we" for Nhasala. Use "Nhasala" after the first mention on a page. Spell out "Women Leaders in Technology (WLiT), Nepal" at first mention on each page.
3. **Light design, no dark mode, no theme toggle.** Header, hero, call-to-action band, and footer are all light. Black is used for text and buttons only. No black or dark sections.
4. **Header:** the text "Nhasala Joshi" only (no logo mark, no placeholder). Menu items: About, Projects, Writing and speaking, Contact. There is no Work page; the four areas of work live on the About page.
5. **Home banner:** headline, short subline, one short line of introduction, and two buttons on the left. On the right, the **bordered portrait cutout** on a pale gold rounded card with sparkle strokes. A four-color band runs along the bottom edge. No illustration, no rings or circles, no black panel, no photo background.
6. **Home is deliberately light on text and icon-led.** Stats are icon, number, and a short label. Area tiles are icon, name, and one short line. Project cards are tag, title, and a one-line blurb, with an arrow icon (no "Learn more" text). Recent writing is year and title only. Do not add paragraphs back.
7. **No pull quote and no "Working with and through" strip** on the home page.
8. **Footer:** the tagline "Building inclusive tech ecosystems.", an email icon button, a LinkedIn icon button, and the Creative Commons line (CC BY 4.0). No name, no copyright line, no navigation.
9. **Selected projects on the home page:** a row of equal cards modeled on the Open Knowledge Nepal home page, one per area of work (`featured: true`).
10. **Portrait:** never retouch, recolor, filter, or reshape the person. The cutout border, the card color, and the sparkles are approved; change them only on request. Keep the full-size original out of any public repository (`source-assets/` is git-ignored on purpose).
11. **Copy style:** American spelling. Sentence case. **No em dashes or en dashes anywhere** (content, code comments, docs); use commas, colons, or parentheses. No all-caps labels, no middle dots between meta items, no arrow characters in link text (arrow icons are fine).
12. **Do not invent facts.** Unconfirmed items carry `verified: false` and show a "Check" flag.
13. **Draft safety:** `robots_noindex: true` and `show_draft_flags: true` in `_config.yml` stay on until the client confirms the content is verified.
14. A phone number is never published.

## Conventions

- CSS: custom properties at the top of `main.css` are the design tokens. Use them; do not add new hex values to rules without adding a token. Area color classes are `.p-community`, `.p-inclusion`, `.p-data`, `.p-governance`; they set `--pc` (color) and `--pt` (tint). Area colors never carry text, and color is never the only signal.
- Include variable names must be unique (`proj`, `pil`, `area`, `org`). Liquid `assign` inside an include **leaks into the parent scope** in Jekyll.
- YAML: wrap any value that contains a colon followed by a space in quotes, in data files and in page front matter.
- Accessibility is a requirement, not polish: visible focus, 44px tap targets, WCAG AA text contrast, semantic headings, labelled landmarks, accessible names for icon-only controls.
- Keep pages light: compress images, lazy-load below the fold, no large JavaScript.

## Definition of done for any change

- `bundle exec jekyll build` succeeds with no warnings, and `sh tools/check.sh` passes.
- Checked at 320, 390, 768, 1024, 1280, and 1440px: no horizontal scroll, nothing overlaps.
- Keyboard-only walkthrough works and focus is always visible.
- Matches `docs/reference/*.png` unless the change is intentional and noted in the commit message.
