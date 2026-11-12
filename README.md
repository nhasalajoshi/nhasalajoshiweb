# Nhasala Joshi, personal website

A lightweight Jekyll site for GitHub Pages. Plain CSS, one small plain JavaScript file, no build tools beyond Jekyll. All content lives in data files, so the layouts never need to change when content does.

## For developers

Start with `CONTRIBUTING.md`. The design spec, change brief, data model, assets guide, decision log, work plan, and reference screenshots are in `docs/` (excluded from the published site). Run `sh tools/check.sh` before committing.

## Design in brief (version 3)

- **Idea:** a light, warm design. Black text on a warm-white page, one accent color per area of work, and a friendly bordered portrait. The base colors come from the black and white shirt in the portrait.
- **Palette:** warm white `#FCF9F6`, text `#151413`, black `#121110` (buttons only). Area colors: gold `#F5B82E` (community), magenta `#E0408F` (inclusion), green `#16906A` (digital rights, data, and civic tech), violet `#8B5CF6` (internet governance). Area colors never carry text, and every label is also written out, so color is never the only signal.
- **Type:** Bricolage Grotesque for headings, Atkinson Hyperlegible for body text (designed for readability by low-vision readers). Noto Sans Devanagari is already in the font stacks for future Nepali content.
- **Structure:** four pages in the menu: About, Projects, Writing and speaking, Contact. The About page holds the story and the full detail of the four areas of work (anchors `#community`, `#inclusion`, `#data`, `#governance`). The home page shows the four areas as icon tiles that link to those sections.
- **Banner:** headline and a short introduction on the left; on the right, the bordered portrait cutout on a pale gold card with sparkle strokes. A four-color band runs along the bottom edge. Change `--card-bg` in the CSS to recolor the card.
- **Home is icon-led and short on text:** icon stats, icon tiles, project cards with a one-line `blurb`, and a short writing list.
- **Selected projects:** a row of equal cards in the style of the Open Knowledge Nepal home page. Cards show every project with `featured: true` in `_data/projects.yml`. Keep it to three or four, and give each a short `blurb`.
- **Accessibility:** skip link, visible focus, 44px tap targets, WCAG AA text contrast, reduced motion respected, works without JavaScript. The site is light only.
- **Voice:** third person throughout.

## Run it locally

```
bundle install
bundle exec jekyll serve
```

Then open http://localhost:4000.

## Where to edit things

| To change | Edit |
|---|---|
| Name, email, LinkedIn, domain, portrait, draft switches | `_config.yml` |
| The four areas of work (tile line, About page text) | `_data/pillars.yml` |
| Footer license | `license_name` and `license_url` in `_config.yml` |
| Projects (add, edit, images, links) | `_data/projects.yml` |
| Organizations and roles | `_data/organizations.yml` |
| Publications | `_data/writing.yml` |
| Talks and convening | `_data/talks.yml` |
| Speaker bios, topics, recognition | `_data/kit.yml` |
| About page path, quick facts | `_data/about.yml` |
| Expertise lists | `_data/expertise.yml` |
| Navigation | `_data/nav.yml` |
| Colors and type | top of `assets/css/main.css` |

Put images in `assets/img/` and reference them in the data files (for example `image: /assets/img/mulcam.jpg` with an `image_alt`). Project images display at 4:3 on the Projects page and 16:10 on the home page cards. Use JPG or WebP, around 1200px wide, compressed. The portrait files are already set in `_config.yml`: the plain photo for the About page (`portrait`, `portrait_small`) and the bordered cutout for the banner (`portrait_cutout`, `portrait_cutout_small`). To swap the portrait, replace the photo in `source-assets/` and run `python3 tools/make_sticker.py` (see `docs/ASSETS.md`), then replace the two plain-photo files in `assets/img/` (a 4:5 crop, 1400px and 700px wide) and update `portrait_alt` if needed. The original photo in `source-assets/` is private and git-ignored.

YAML tip: if a text value contains a colon followed by a space, wrap the whole value in quotes.

## Draft mode

Two switches in `_config.yml` keep unfinished content safe:

- `robots_noindex: true` tells search engines to skip the site. Set it to `false` at launch.
- `show_draft_flags: true` shows a small "Check" tag next to anything marked `verified: false`. Set it to `false` at launch, after every flagged item is confirmed.

## Deploy on GitHub Pages

1. Create a repository and push this folder to the `main` branch.
2. In the repository, open Settings, then Pages, and choose "Deploy from a branch", branch `main`, folder `/ (root)`.
3. Rename `CNAME.template` to `CNAME` and put the booked domain inside it (one line, no https).
4. At the domain registrar, point the domain to GitHub. For an apex domain, add the four A records GitHub lists in its custom domain documentation (check that page for the current addresses). For `www`, add a CNAME record pointing to `YOUR-USERNAME.github.io`.
5. Back in Settings, Pages, enter the custom domain, wait for the DNS check, then tick "Enforce HTTPS".
6. In `_config.yml`, set `url:` to the final address and `baseurl:` to `""`. (Until then the site runs at `https://nhasalajoshi.github.io/nhasalajoshiweb/`, which needs `baseurl: "/nhasalajoshiweb"`.)
7. Replace `assets/img/og.png` (a draft social image, 1200 x 630) with final artwork.

## Content checklist before launch

- Confirm dates and titles for Open Knowledge Nepal, Youth IGF Nepal, Women Techmakers, and GDG Kathmandu (the CV and LinkedIn disagree). Fix education and language details too.
- Fill the "To be added" and "To be confirmed" fields in `_data/projects.yml` (problem, approach, result, years).
- Add outlets and links to the three publications.
- The public email address is set in `_config.yml`. A phone number is intentionally not published.
- Donor rule: no funder, development agency, bank, embassy, or ministry is named anywhere. Check every photo for funder logos on banners and backdrops. Do not link to pages or reports that show funder names or logos.
- Confirm Nepal Bhasa (Newari) and Hindi language levels with Nhasala.
- Confirm the Creative Commons license in the footer (currently CC BY 4.0). Photos, logos, and third-party material may need their own terms, which the footer wording ("except where otherwise noted") allows for. Add photo credits where needed.
- Decide whether the recognition section stays, and which items it holds.
- Get permission for photos of participants, especially from inclusion programs.
- Spell out "Women Leaders in Technology (WLiT), Nepal" in full wherever possible. Other organizations use the same acronym, so this helps search engines.
- Run a final check: tab through every page with the keyboard, zoom to 200 percent, and test on a phone.

## Fonts and privacy

Fonts load from Google Fonts. To avoid third-party requests, download the three font files, place them in `assets/fonts/`, and replace the `<link>` in `_includes/head.html` with `@font-face` rules.
