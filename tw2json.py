#!/usr/bin/env python3
"""Extract tiddlers from a TiddlyWiki HTML file into TiddlyWiki 5 JSON,
ready for DifflyWiki's "Import JSON".

Reads TiddlyWiki Classic and TiddlyWiki 5 files: the <div><pre> store of
Classic and TW5 before 5.2, and the JSON store of TW5 5.2+.
System tiddlers ($:/...) and Classic plugins (tagged systemConfig) are skipped.

To import TiddlyWiki 5 JSON: open DifflyWiki, click the gear and use Import JSON with the created `old-wiki.json`.
The note text will be imported as is, TiddlyWiki markup (`!!` headings, `''bold''`) is not converted to markdown.

Usage: python3 tw2json.py old-wiki.html [out.json]
       (default output: old-wiki.json next to the input)
"""
import html
import json
import re
import sys
from pathlib import Path

DIV_TIDDLER = re.compile(r'\s*<div ([^>]*)>\s*(?:<pre>(.*?)</pre>)?\s*</div>', re.S)
ATTR = re.compile(r'([\w.:-]+)="([^"]*)"')
JSON_STORE = re.compile(r'<script class="tiddlywiki-tiddler-store" type="application/json">(.*?)</script>', re.S)


def div_tiddlers(page):
    """<div title=".." created=".." ...><pre>escaped text</pre></div>, one after another."""
    start = page.find('<div id="storeArea"')
    if start < 0:
        return []
    pos = page.index('>', start) + 1
    tiddlers = []
    while m := DIV_TIDDLER.match(page, pos):
        fields = {k: html.unescape(v) for k, v in ATTR.findall(m.group(1))}
        fields['text'] = html.unescape(m.group(2) or '')  # &lt; &gt; &amp; &quot; back to characters
        tiddlers.append(fields)
        pos = m.end()
    return tiddlers


def tw5_date(value):
    """Classic dates are YYYYMMDDHHMM; TW5 wants YYYYMMDDHHmmssSSS."""
    return value.ljust(17, '0') if re.fullmatch(r'\d{12,17}', value or '') else value


def convert(page):
    tiddlers = [t for block in JSON_STORE.findall(page) for t in json.loads(block)]
    tiddlers += div_tiddlers(page)
    out = []
    for t in tiddlers:
        title = t.get('title', '')
        if not title or title.startswith('$:/') or 'systemConfig' in t.get('tags', '').split():
            continue
        for key in ('created', 'modified'):
            if key in t:
                t[key] = tw5_date(t[key])
        out.append(t)
    return out


def main():
    if len(sys.argv) not in (2, 3):
        sys.exit(__doc__.strip())
    src = Path(sys.argv[1])
    dst = Path(sys.argv[2]) if len(sys.argv) == 3 else src.with_suffix('.json')
    tiddlers = convert(src.read_text(encoding='utf-8'))
    dst.write_text(json.dumps(tiddlers, indent=4, ensure_ascii=False) + '\n', encoding='utf-8')
    print(f'{len(tiddlers)} tiddlers -> {dst}')


if __name__ == '__main__':
    main()
