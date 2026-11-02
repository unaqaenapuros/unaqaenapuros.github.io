#!/usr/bin/env python3
"""Fail on build errors or warnings, except remote images on sdos.es, which the author chose to ignore."""
import re
import subprocess
import sys

IGNORED_REMOTE = re.compile(r'^WARN  Failed to fetch remote resource "https?://(www\.)?sdos\.es/')
result = subprocess.run(['hugo', '--gc', '--minify'], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(result.stdout)
warnings = [line for line in result.stdout.splitlines() if line.startswith('WARN')]
unexpected = [line for line in warnings if not IGNORED_REMOTE.match(line)]
if unexpected:
    print('Unexpected build warnings:', *unexpected, sep='\n', file=sys.stderr)
sys.exit(result.returncode or bool(unexpected))
