#!/usr/bin/env python3
"""Compare Hugo's eligible post URLs with the public sitemap. Fail closed."""
import argparse
import csv
import json
import subprocess
import sys
from datetime import datetime, timezone
from urllib.request import Request, urlopen
from xml.etree import ElementTree

def pending(rows, published, now):
    urls = []
    for row in rows:
        if row['kind'] != 'page' or row['section'] != 'posts' or row['draft'].lower() == 'true':
            continue
        published_at = datetime.fromisoformat(row['publishDate'].replace('Z', '+00:00'))
        expires = row.get('expiryDate', '')
        expired = expires and not expires.startswith('0001-') and datetime.fromisoformat(expires.replace('Z', '+00:00')) <= now
        if published_at <= now and not expired and row['permalink'] not in published:
            urls.append(row['permalink'])
    return sorted(set(urls))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--sitemap', default='https://unaqaenapuros.com/sitemap.xml')
    parser.add_argument('--output')
    args = parser.parse_args()
    rows = list(csv.DictReader(subprocess.check_output(['hugo', 'list', 'all'], text=True).splitlines()))
    # One bounded read. An unreachable/invalid sitemap is an error, not "all OK".
    with urlopen(Request(args.sitemap, headers={'User-Agent': 'Blog-publication-check'}), timeout=30) as response:
        document = response.read(5_000_000)
    root = ElementTree.fromstring(document)
    if root.tag != '{http://www.sitemaps.org/schemas/sitemap/0.9}urlset':
        raise ValueError('Expected a sitemap URL set')
    published = {node.text for node in root.findall('{*}url/{*}loc')}
    if not published:
        raise ValueError('Empty sitemap')
    urls = pending(rows, published, datetime.now(timezone.utc))
    print(json.dumps(urls))
    if args.output:
        with open(args.output, 'a', encoding='utf-8') as output:
            output.write('pending_count=' + str(len(urls)) + '\n')
            output.write('post_url=' + (urls[0] if urls else '') + '\n')

if __name__ == '__main__':
    main()
