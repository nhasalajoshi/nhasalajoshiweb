# Decision log

What the client decided, what was tried and dropped, and why. Read this before proposing a design change: many obvious ideas were already tried. "Final" means the client confirmed it. "Open" means undecided; ask before choosing.

## Structure and content

| Topic | Decision | Status |
|---|---|---|
| Areas of work | Four: Community and ecosystem building (the lead), Inclusion, Digital rights, data, and civic tech, Internet governance. Leadership of WLiT is the through-line, not its own area. | Final |
| Pages | Home, About, Projects, Writing and speaking, Contact. Gallery removed. A separate Work page was merged into About (the four areas now live there). | Final |
| Voice | Third person throughout. | Final |
| Donors | No funder, agency, bank, embassy, or ministry named anywhere. | Final |
| Making and art work | Held back for a later internal section. | Final (deferred) |
| Date conflicts between CV and LinkedIn | Not guessed; settled by the client in the content update. | Final (deferred) |
| Government-funded fellowship (on the CV) | Left out of the site because it is government-funded. Not named in the repository either. | Final |
| Funder names in the repository | Removed from docs and tools too, not only from the site. `tools/check.sh` reads the names from a private, git-ignored `tools/blocked-names.txt`. | Final |
| Contact details | Public email `nhasala.joshi@gmail.com`; LinkedIn `https://www.linkedin.com/in/nhasalajoshi/`. No phone number. | Final |
| Content editing after launch | Editing the YAML files in `_data/` on GitHub is fine; no browser-based editor needed for now. | Final |
| Recognition section | Kept small, quiet. Whether it stays is unconfirmed. | Open |
| Content license | Creative Commons Attribution 4.0 (CC BY 4.0), shown in the footer. Matches the license on the Open Knowledge Nepal site. Reconfirmed by the client on 2026-11-12. | Final |
| Language | English first. Nepali or Nepal Bhasa content is a later phase. | Final (deferred) |

## Visual design history (newest decisions win)

| Topic | History | Status |
|---|---|---|
| Overall color | 1. Purple-led palette built on the suffrage colors (rejected after the portrait arrived). 2. Black and warm white matched to the black and white shirt, with black header, banner panel, call-to-action, and footer. 3. **Lighter overall: warm-white page, black only for text and buttons, area colors as accents.** | Final (3) |
| Dark mode | A dark mode toggle was built, then removed from the menu; the dark theme was dropped. | Final |
| Hero, early rounds | Ring graphic around a portrait placeholder (rejected); text-only full-width banner (replaced); text banner with a drawn illustration of people, a screen, chat, shield, and globe (replaced by the real portrait). | Dropped |
| Hero, photo rounds | Black and white split banner (black text panel beside the photo, with a light alternative). The client preferred the light alternative and asked for the whole site to follow it. | Dropped |
| Hero, current | Light banner. Text on the left. On the right, the **bordered cutout portrait** on a pale gold card with sparkle strokes, inspired by a reference style the client shared (white border, colored card, sparkles). | Final |
| Hero card color | Soft gold `#FFD670` chosen over saturated gold, pastel violet, pink, and mint. | Final, easy to change (`--card-bg`) |
| Hero vertical text (as in the reference) | Not used. | Final |
| Header | Text name only (no logo mark, no placeholder). Dark mode button removed. Work removed from the menu. | Final |
| Footer | Name removed. Tagline plus email and LinkedIn icon buttons plus the CC BY 4.0 line. Copyright line and navigation removed. | Final |
| Quote on home | "Technology is not neutral" pull quote removed from home. (A sentence with the same idea remains in the About prose and the speaker bio.) | Final |
| "Working with and through" organizations strip | Removed from home. | Final |
| Four-color rule | A short four-color rule under every section heading, and a four-color band along the hero's bottom edge. | Final |
| Selected projects | A featured project beside a list (rejected) became a row of equal cards modeled on the Open Knowledge Nepal home page; now slimmed to tag, title, one-line blurb, arrow icon. | Final |
| Text load | The client asked for much less text on the home page and for icons in the thematic parts. Stats, tiles, cards, and writing rows were all shortened, and icons added. | Final |
| Stripe texture | Fine vertical stripes, a nod to the shirt, used only on the call-to-action band. | Final |
| Hero card radius | 28px, a deliberate exception to the 6px radius used elsewhere, so it reads as a sticker card. | Final |

## Open design questions (need the client before changing)

1. **About page portrait:** keep the plain photo, or restyle it as a bordered cutout on a color card like the hero?
2. **Favicon:** it is still the black rounded square with rings. Update it to the light design, or leave it?
3. **Final social preview artwork:** the current `og.png` is a draft built from the portrait and site colors.
4. **Hero card color:** soft gold is the choice for now; the client may want to see violet or pink in context.
5. **Stat icon colors:** the stat bubbles are neutral so that color keeps meaning "area of work". The client may prefer colored bubbles.

## Working agreements

- The client reviews changes as screenshots first. Show a preview of any visible change before polishing.
- The client does not want the full documentation set regenerated for every small design tweak. Update docs when a direction is approved.
- No em dashes or en dashes anywhere, including documents and code comments.
- Honesty over polish: anything unconfirmed stays flagged as a draft.
