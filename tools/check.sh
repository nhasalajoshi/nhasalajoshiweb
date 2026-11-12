#!/bin/sh
# Quick style and rules check for the published site files. Run from the repository root:  sh tools/check.sh
# Exits with a non-zero status if anything is found. It checks only files that are published (not docs/ or tools/).
cd "$(dirname "$0")/.." || exit 1
FILES="index.html about.html projects.html writing.html contact.html 404.html robots.txt _config.yml _includes _layouts _data assets/css assets/js"
fail=0

echo "1. Em dashes and en dashes (also checked in docs and README)"
EM=$(printf '\342\200\224'); EN=$(printf '\342\200\223')
if grep -rIn -e "$EM" -e "$EN" $FILES README.md CONTRIBUTING.md docs --include="*.html" --include="*.css" --include="*.js" --include="*.yml" --include="*.md" --include="*.txt" 2>/dev/null | grep -v "docs/reference"; then fail=1; else echo "   none"; fi

echo "2. Funder, agency, bank, embassy, or ministry names (site files, docs, and tools)"
# The names themselves are never stored in the repository. Keep them, one per line, in tools/blocked-names.txt,
# which is git-ignored. Ask the site owner for the list.
NAMES=tools/blocked-names.txt
if [ ! -s "$NAMES" ]; then
  echo "   skipped: $NAMES is missing or empty (it is private and git-ignored; ask the site owner for it)"
elif grep -rInwiF -f "$NAMES" $FILES README.md CONTRIBUTING.md docs tools 2>/dev/null | grep -v "^$NAMES:"; then fail=1; else echo "   none"; fi

echo "3. Leftovers from earlier versions"
if grep -rInE -e '\.on-ink|class="[^"]*on-ink' -e "btn--gold" -e "ring-glyph" -e "hero_layout" -e "hero__panel" -e "hero-art" -e "theme-toggle" $FILES; then fail=1; else echo "   none"; fi

echo "4. First person for Nhasala in published copy (heuristic; review any hits)"
if grep -rIn -e ">I " -e " I'm " -e " my " -e " our " index.html about.html projects.html writing.html contact.html _data | grep -v "I don't believe"; then fail=1; else echo "   none"; fi

echo "5. Placeholders that must change before launch (warnings only)"
grep -n "example.com\|^url:\|^baseurl:" _config.yml | sed 's/^/   /'
grep -n "robots_noindex\|show_draft_flags" _config.yml | sed 's/^/   /'

[ $fail -eq 0 ] && echo "OK" || echo "Problems found above"
exit $fail
