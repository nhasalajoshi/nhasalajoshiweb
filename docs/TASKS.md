# Tasks

Work through these in order. Make small commits with clear messages. After each task, summarize what changed and what you verified. Ask the client before reversing any hard rule in `CONTRIBUTING.md` or reopening anything marked Final in `docs/DECISION_LOG.md`.

## Task 1: Make version 3 build and match the references under real Jekyll

The prototype was tested only in a Liquid renderer, so Jekyll-specific problems may remain. If you only have the older version-2 repository, first apply `docs/REDESIGN_V3_BRIEF.md` (Mode B there).

Do:
- Run `bundle install` and `bundle exec jekyll build`. Fix every error and warning.
- Check the risk list in section 8 of `docs/REDESIGN_V3_BRIEF.md`: the `{% case %}` icon include, the compound `{% unless %}`, `default` filters on missing fields, `srcset` built from config, variable leakage between includes, and `where` filters (`where: "featured", true` and `where: "pillar", ""`).
- Confirm `docs/`, `tools/`, `source-assets/`, and `CONTRIBUTING.md` do not appear in `_site/`.
- Stay compatible with the GitHub Pages gem (Jekyll 3.x, Liquid 4). Do not use Jekyll 4-only features.
- Run `sh tools/check.sh` and fix anything it reports.

Done when:
- The build is clean and `bundle exec jekyll serve` shows all six pages (home, about, projects, writing, contact, 404).
- Each page matches `docs/reference/*.png` at 1280px and 390px (use Playwright or a browser to compare; list any differences).
- The acceptance criteria in section 6 of `docs/REDESIGN_V3_BRIEF.md` all pass.

## Task 2: Repository and hosting setup

Do:
- Initialize git if needed, make a first commit, and set the default branch to `main`. Confirm `source-assets/` is not committed (it is git-ignored).
- Provide exact steps for GitHub Pages (Settings, Pages, deploy from branch `main`, folder root), or set up a GitHub Actions workflow if the client prefers it. Start with branch deploy; it is simpler.
- Prepare the custom domain: rename `CNAME.template` to `CNAME` and fill it **only after the client gives the final domain**. Document the DNS records (apex A records to GitHub's four addresses, `www` CNAME to `<user>.github.io`) and tell the client to enable "Enforce HTTPS". Verify the current addresses against GitHub's documentation instead of trusting memory.

Done when: the site is live on the GitHub Pages default URL (or the custom domain), still `noindex`.

## Task 3: Automated quality checks (Actions only)

Do:
- Add a GitHub Actions workflow that builds the site, runs `sh tools/check.sh`, and runs `html-proofer` (internal links, images, scripts; skip external placeholders) on pull requests and pushes.
- Add an accessibility check (`pa11y-ci` or `axe` via Playwright) against the built pages at 390px and 1280px.
- Keep every dev dependency out of the site itself. The site must still build with only the `github-pages` gem.

Done when: the workflow passes on `main` and fails when a link, a rule in `check.sh`, or an accessibility rule is broken on purpose.

## Task 4: Accessibility and responsive audit

Do:
- Run Lighthouse and axe on every page. Fix all violations without changing the look.
- Walk each page by keyboard only. Check the stretched-link tiles and cards (a clear outline around the whole tile or card), the filter chips, the `details` disclosures, the mobile menu (Escape, focus return), and the footer icon buttons.
- Check the icon-only controls have accessible names, the decorative icons and sparkles are hidden from assistive technology, and the hero image has meaningful alt text.
- Check contrast for muted text, the `.draft` flag, and icon bubbles. Check 200% zoom and 320px width for reflow.
- Check `-webkit-line-clamp` on card text, and that long titles do not break the card layout.

Done when: Lighthouse accessibility is 100 on all pages, axe reports no violations, and no horizontal scroll appears at 320, 390, 768, 1024, 1280, or 1440px.

## Task 5: Self-host fonts

Do:
- Download Bricolage Grotesque (500, 700) and Atkinson Hyperlegible (400, 700, 400 italic) as WOFF2, Latin subset (both are SIL Open Font License). Add `@font-face` rules with `font-display: swap`, preload the two most important files, and remove the Google Fonts `<link>` tags and `preconnect` lines from `_includes/head.html`.
- Leave Noto Sans Devanagari in the font stacks. Do not add the file until Nepali content exists.

Done when: no request leaves the domain on a normal page load and there is no visible layout jump at font swap.

## Task 6: Content integration (when the client delivers material)

Do:
- Fill `_data/*.yml` from the client's material. Follow `docs/CONTENT_AND_DATA.md` for voice and the donor rule. Replace "To be added" and "To be confirmed" only with facts the client confirmed.
- Add project images to `assets/img/` (about 1200px wide, compressed) with alt text. Give every featured project a one-line `blurb`.
- Resolve the date conflicts listed in `docs/CONTENT_AND_DATA.md` with the client, not by guessing.
- Set `verified: true` only for items the client confirmed.

Done when: no placeholder text remains except items the client chose to leave, and every image has alt text and has been checked for funder logos.

## Task 7: Design follow-ups (only after the client decides; see "Open design questions" in `docs/DECISION_LOG.md`)

Do not start these without the client's answer. Each is small.
- **About page portrait:** restyle as a bordered cutout on a color card, matching the hero (reuse the cutout file and the `.hero__card` pattern).
- **Favicon:** redraw for the light design.
- **Social image:** replace the draft `assets/img/og.png` with final artwork (1200 by 630; name and tagline left, the gold portrait card right).
- **Hero card color:** show alternatives in context (`--card-bg`).
- **Stat icon colors:** neutral now; colored bubbles are an option.

## Task 8: Pre-launch (only with the client's sign-off)

Do:
- Set the real `url` (the `email` is already set), and replace the draft social image.
- Confirm the Creative Commons license wording with the client.
- Set `robots_noindex: false` and `show_draft_flags: false`.
- Confirm HTTPS works on the custom domain, the sitemap lists the pages, and the 404 page works. Check link previews on LinkedIn and WhatsApp.

Done when: the client approves a final walkthrough on a phone and a laptop.

## Later, only if the client asks

- A browser-based editor for content (for example Pages CMS or Decap CMS with the GitHub backend).
- Separate detail pages for projects (a Jekyll collection).
- A Nepali or Nepal Bhasa version and language switch.
- Privacy-friendly analytics (Plausible or GoatCounter).
- An internal section for making and art work.

## Questions to ask the client before starting

1. What is the final domain, and who controls its DNS?
2. Answered: the public email is `nhasala.joshi@gmail.com`.
3. Answered: yes, CC BY 4.0.
4. Answered: the government-funded fellowship stays off the site.
5. Answered: content is edited in the YAML files on GitHub.
6. The open design questions in `docs/DECISION_LOG.md` (About portrait, favicon, final social image).
