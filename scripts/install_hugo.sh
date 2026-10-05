#!/usr/bin/env bash
set -euo pipefail
version=0.164.0
archive="hugo_extended_${version}_linux-amd64.tar.gz"
release="https://github.com/gohugoio/hugo/releases/download/v${version}"
work=$(mktemp -d)
trap 'rm -rf "$work"' EXIT
curl --fail --location --silent --show-error "$release/$archive" -o "$work/$archive"
checksum=fea17b8c076f950bb2e9f9486667bdaa29422883888d509d63931c73e8a9b3a4
(cd "$work"; printf '%s  %s\n' "$checksum" "$archive" | sha256sum --check --strict -)
tar -xzf "$work/$archive" -C "$work" hugo
sudo install -m 0755 "$work/hugo" /usr/local/bin/hugo
hugo version
