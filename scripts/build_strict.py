#!/usr/bin/env python3
"""Fail on build errors or warnings, except the explicitly accepted old image."""
import subprocess
import sys

KNOWN_IMAGE = 'http://sdos.es/wp-content/uploads/2017/08/Jenkins.jpg'
result = subprocess.run(['hugo', '--gc', '--minify'], text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
print(result.stdout)
warnings = [line for line in result.stdout.splitlines() if line.startswith('WARN')]
unexpected = [line for line in warnings if not (line.startswith('WARN  Failed to fetch remote resource "' + KNOWN_IMAGE + '"'))]
if unexpected:
    print('Unexpected build warnings:', *unexpected, sep='\n', file=sys.stderr)
sys.exit(result.returncode or bool(unexpected))
