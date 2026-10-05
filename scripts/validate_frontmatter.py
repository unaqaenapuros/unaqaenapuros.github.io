#!/usr/bin/env python3
import datetime
import sys
from pathlib import Path
import yaml

errors = []
urls = {}
missing = 0
for path in Path('content/posts').rglob('*.md'):
    if path.name == '_index.md':
        continue
    text = path.read_text()
    if not text.startswith('---'):
        errors.append(f'{path}: YAML front matter required')
        continue
    try:
        meta = yaml.safe_load(text.split('---', 2)[1])
        if not meta.get('title') or not meta.get('date'):
            raise ValueError('title and date are required')
        datetime.datetime.fromisoformat(str(meta['date']).replace('Z', '+00:00'))
        url = meta.get('url')
        if url:
            if not url.startswith('/'):
                raise ValueError('url must start with /')
            if url in urls:
                raise ValueError(f'duplicate url, also in {urls[url]}')
            urls[url] = path
        description = meta.get('description')
        if description:
            if len(description) > 180 or '\n' in description or '\\n' in description:
                raise ValueError('description must be a single line, at most 180 characters')
        else:
            # Legacy descriptions are editorial work, not fabricated in CI.
            missing += 1
    except Exception as error:
        errors.append(f'{path}: {error}')
print(f'Existing posts without explicit description: {missing} (non-blocking)')
print('\n'.join(errors))
sys.exit(bool(errors))
