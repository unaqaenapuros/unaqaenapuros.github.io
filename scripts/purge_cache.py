#!/usr/bin/env python3
"""Purge generated page URLs, never the whole Cloudflare zone."""
import json
import os
from pathlib import Path
from urllib.request import Request, urlopen
from urllib.parse import quote

def main():
    base = 'https://unaqaenapuros.com/'
    urls = set()
    for path in Path('public').rglob('*'):
        if path.is_file():
            relative = path.relative_to('public').as_posix()
            urls.add(base + quote(relative, safe='/'))
            if relative.endswith('index.html'):
                urls.add(base + quote(relative[:-10], safe='/'))
    if not urls:
        raise ValueError('Missing generated files; refusing an empty purge')
    endpoint = f"https://api.cloudflare.com/client/v4/zones/{os.environ['CLOUDFLARE_ZONE_ID']}/purge_cache"
    ordered = sorted(urls)
    for start in range(0, len(ordered), 30):
        body = json.dumps({'files': ordered[start:start + 30]}).encode()
        request = Request(endpoint, data=body, method='POST', headers={
            'Authorization': 'Bearer ' + os.environ['CLOUDFLARE_API_TOKEN'],
            'Content-Type': 'application/json'})
        with urlopen(request, timeout=30) as response:
            result = json.load(response)
        if not result.get('success'):
            raise RuntimeError('Cloudflare rejected the URL purge')
    print(f'Purged {len(ordered)} generated URLs')

if __name__ == '__main__':
    main()
