#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
SITE_DIR="$ROOT_DIR"

if [[ ! -d "$SITE_DIR" ]]; then
  echo "[ERROR] site directory not found: $SITE_DIR" >&2
  exit 1
fi

if ! command -v ruby >/dev/null 2>&1; then
  echo "[ERROR] ruby command not found." >&2
  echo "Install Ruby first, then rerun this script." >&2
  exit 1
fi

if ! ruby -e 'exit(Gem::Version.new(RUBY_VERSION) >= Gem::Version.new("3.1.0") ? 0 : 1)'; then
  echo "[ERROR] Ruby 3.1+ is required for current github-pages dependencies." >&2
  echo "Current: $(ruby -e 'print RUBY_VERSION')" >&2
  echo "Upgrade Ruby (recommended: rbenv), then rerun this script." >&2
  exit 1
fi

if ! command -v bundle >/dev/null 2>&1; then
  echo "[ERROR] bundle command not found." >&2
  echo "Install Bundler: gem install bundler" >&2
  exit 1
fi

cd "$SITE_DIR"
bundle config set --local path vendor/bundle
bundle install

echo "[OK] Bundles installed in $SITE_DIR/vendor/bundle"
echo "Run site locally:"
echo "  cd $SITE_DIR"
echo "  bundle exec jekyll serve --livereload"
