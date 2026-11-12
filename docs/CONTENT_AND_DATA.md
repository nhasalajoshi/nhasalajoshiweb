# Content and data

Almost all content lives in `_data/*.yml`. A small amount of short copy lives in the page templates (listed below). Templates render the data; do not hard-code content that has a data home.

YAML rule: wrap any value that contains a colon followed by a space in quotes, in data files **and** in page front matter. A bare colon breaks the Jekyll build (this happened twice during the prototype).

## Data files

### `pillars.yml` (the four areas of work, in display order, community first)

| Field | Type | Used by | Notes |
|---|---|---|---|
| `id` | string | everything | `community`, `inclusion`, `data`, `governance`. Also the CSS class suffix (`p-<id>`), the icon name, and the anchor id on the About page. |
| `name` | string | tiles, About, projects filter | Full name, for example "Digital rights, data, and civic tech" |
| `badge` | string | badges, filter chips | Short label |
| `url` | string | tiles | `/about/#<id>` |
| `line` | string | tiles | One short sentence for the home tile (about 4 to 7 words) |
| `featured` | boolean | tiles, About | `true` only for `community`; it becomes the wide lead tile and the tinted lead block |
| `statement` | string | About | Longer description of the area |
| `looks_like` | list of strings | About | "What this looks like" bullets |
| `orgs` | list of organization ids | About | Resolved against `organizations.yml` |

### `projects.yml` (one entry per project)

| Field | Type | Notes |
|---|---|---|
| `id` | string | Unique, never equal to an area id. Used as the anchor on the projects page and in card links. |
| `title`, `summary` | string | Summary is one or two sentences; it appears on the Projects page |
| `blurb` | string | One short line for the home page card. Falls back to `summary` if empty. Set on the four featured projects. Keep it under about 12 words. |
| `pillar` | area id | Primary area. Drives color, badge, and which About block lists it. |
| `also` | list of area ids | Secondary areas. Used for badges and for the projects filter. |
| `role` | string | Use an honest verb: Led, Initiated, Designed and directed, Facilitated, Contributed, Mentor |
| `org` | string | Organization name shown under the title on the Projects page |
| `years` | string | Free text such as `2019 to 2023` or `To be confirmed` |
| `featured` | boolean | `true` shows the project as a card on the home page. Keep it to three or four, one per area. |
| `verified` | boolean | `false` shows the dashed "Check" flag while `show_draft_flags` is on |
| `problem`, `approach`, `result` | string | Shown in the "Problem, approach, and result" disclosure. Empty falls back to "To be added." |
| `image`, `image_alt` | path, string | Empty shows a placeholder. When set, `image_alt` is required. |
| `links` | list of `{label, url}` | Optional. Never link to pages that show funder names or logos. |

### `organizations.yml`

`id`, `name` (full), `short` (used in lists), `role`, `years`, `url` (`"#"` means no public link yet, so no link is rendered), `verified`.

### `writing.yml` (publications)

`title`, `year`, `type`, `role`, `outlet`, `url` (empty means no link), `summary`, `verified`. The home page shows the first three as year and title only.

### `talks.yml` (speaking and convening)

`title`, `role`, `year` (free text), `note`, `verified`.

### `kit.yml` (speaker kit)

`topics` (list), `short_bio`, `long_bio` (both third person, copied by the copy buttons), `recognition` (list of `{title, year, by, verified}`).

### `about.yml`

`path`: four `{title, text}` steps (engineer, community builder, institution leader, policy voice). `glance`: `{label, value}` facts shown beside the portrait.

### `expertise.yml`

List of `{title, pillar, items}`. `pillar` is an area id, or an empty string for the "Leadership and operations" group, which renders as the last plain block on the About page.

### `nav.yml`

List of `{title, url}`: About, Projects, Writing and speaking, Contact.

### `_config.yml` (site-level)

| Key | Notes |
|---|---|
| `title`, `tagline`, `description` | Used in titles, meta tags, the footer tagline, and JSON-LD |
| `url`, `baseurl` | `url` must become the booked domain with https and no trailing slash. Currently `https://www.example.com`. |
| `email` | Public contact address: `nhasala.joshi@gmail.com` (confirmed by the client). |
| `linkedin`, `wlit_url` | External links |
| `license_name`, `license_url` | Footer license line. Currently CC BY 4.0. |
| `portrait`, `portrait_small`, `portrait_width`, `portrait_height`, `portrait_alt` | The plain photo (About page) and its 700px copy, intrinsic size, and alt text |
| `portrait_cutout`, `portrait_cutout_small`, `portrait_cutout_width`, `portrait_cutout_height` | The bordered cutout used in the hero (1200px and 600px WebP) and its intrinsic size |
| `robots_noindex`, `show_draft_flags` | Draft switches. Keep both `true` until the client signs off. |
| `og_image` | Social preview image |
| `plugins`, `exclude`, `defaults` | `exclude` keeps `docs`, `tools`, `source-assets`, `CONTRIBUTING.md`, and `README.md` off the published site |

## Short copy that lives in the templates

| Where | What |
|---|---|
| `index.html` | Hero h1, subline, one-line introduction, button labels; the four stat numbers and labels; section headings; call-to-action heading and button |
| `about.html` | Lede, the four story paragraphs, the "Areas of work" intro line |
| `projects.html`, `writing.html`, `contact.html`, `404.html` | Ledes, speaker kit intro, the four collaboration descriptions and mailto subjects, "what to include" list, accessibility line |
| `_includes/footer.html` | The license sentence (license name and URL come from config) |
| `_includes/head.html` | JSON-LD (job title, employer, location, `knowsAbout`) |

Current home copy, for reference:
- h1 "Building inclusive tech ecosystems." Subline "Digital rights and feminist tech advocate". Introduction "Co-founder and Executive Director of Women Leaders in Technology (WLiT), Nepal."
- Stats: "10+ years leading WLiT", "14 fellowship cohorts", "200+ women tech professionals", "1,000+ attendees at flagship events".
- Tile lines: "Fellowships, networks, and convenings." / "Room for everyone in tech." / "Open data and safer online spaces." / "Youth and women's voices in policy."

## Voice and copy rules

- Third person. "Nhasala Joshi is…", then "Nhasala" or "she". Her own words do not appear on the home page.
- Plain, specific, active. Say what she did and what happened, not adjectives. Prefer outcomes to duties.
- **Home copy stays short.** If a sentence can move to the About page, move it.
- Role labels must be honest. Do not let organization-wide results read as personal credit without a role verb.
- American spelling. Sentence case for headings and buttons. No em dashes or en dashes.
- Link and button text names the action ("Explore the work", "Invite Nhasala to speak", "See all projects"). No arrow characters.
- Spell out "Women Leaders in Technology (WLiT), Nepal" on first use per page.

## The donor rule

Do not name any funder, donor, development agency, multilateral bank, embassy, or ministry anywhere: copy, data, alt text, file names, comments. Use generic phrases such as "development partners", "multi-partner funding", "national government bodies". Check every photo for funder logos on banners and backdrops. Do not link to third-party report or fundraising pages that show funder names. Non-donor organizations (WLiT, Open Knowledge Nepal, Youth IGF Nepal, Internet Society Nepal Chapter, GDG Kathmandu, Women Techmakers, Global Shapers Kathmandu, Women LEAD Nepal, Purak Asia) may be named.

One fellowship on the CV is deliberately left out because it is government-funded. The client confirmed it stays off the site; do not name it anywhere in the repository.

The names to check for live in `tools/blocked-names.txt`, which is private and git-ignored. `sh tools/check.sh` searches the site files, docs, and tools for them. Never write the names into a tracked file.

## Draft content: what is known and what is not

The content was drafted from the client's CV and LinkedIn export (not stored in this repository). Anything unconfirmed is marked in the data, either with `verified: false` or with text such as "To be confirmed" or "To be added."

**Facts that conflict between the CV and LinkedIn (to be settled by the client in the content update, not by guessing):**
- Open Knowledge Nepal: CV says consultant from 2024; LinkedIn says strategic advisor and consultant from November 2025 (and the LinkedIn summary calls her a co-founder of the organization, which is not on the CV).
- Youth IGF Nepal: June 2024 (CV) or June 2025 (LinkedIn).
- GDG Kathmandu: 2018 to 2025 (CV) or organizing team from 2015, co-organizer from 2017, ending May 2026, plus an advisor role from 2025 (LinkedIn).
- Women Techmakers: 2016 or 2017 start, to 2023.
- Education dates and college name; WLiT start month (June or July 2015); end of the hardware engineering role (September or October 2018); language names and levels (Newari or Nepal Bhasa; Hindi appears only on the CV).
- Reach totals (4,000+ or 6,000+) differ, so they are not used. The figures 14 fellowship cohorts, 200+ women tech professionals, and 1,000+ attendees at flagship events are consistent in both sources.

**Delivered by the client:** the portrait photo (original 2415 by 3019 pixels, kept privately in `source-assets/`, not in git). See `docs/ASSETS.md` for the derived files.

**Still waiting on the client:**
- The final domain in `url`.
- Project images, and a one-line `blurb` for any additional featured project.
- Problem, approach, and result for most projects; years for several.
- Outlets and links for the three publications.
- Speaker kit downloads (headshot, one-page profile PDF).
- Final social preview artwork (`assets/img/og.png` is a draft).
- Whether the "Recognition" section stays and which items it holds.
- Permission for any photos of participants, especially from inclusion programs.
- Nepali or Nepal Bhasa content (a later phase). Load Noto Sans Devanagari when it arrives.
- Making and art work (public art, exhibitions) is intentionally held back for a later internal section.

## Confirmed client decisions on content

- Four areas: Community and ecosystem building (the lead), Inclusion, Digital rights, data, and civic tech, Internet governance.
- Leadership of WLiT runs through everything and is not its own area.
- Pages: Home, About, Projects, Writing and speaking, Contact. Gallery removed. Work details live on the About page.
- License for site content: Creative Commons Attribution 4.0 (CC BY 4.0).
- The date inconsistencies are handled later, in the content update.
