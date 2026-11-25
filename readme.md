# TiddlyWiki Slim

Slim version of TiddlyWiki.
* Inspired by Teddy Wiki Lite from https://github.com/crystal-world-project/crystal-world
* Original TiddlyWiki: https://github.com/TiddlyWiki/TiddlyWiki5

## Why TiddlyWiki Slim

* Git-diff friendly file format
 * All formatting is preserved, stable note order in export title+date, export is byte-identical
 * Notes are saved at the beginning of the file
 * Unlike TiddlyWiki5 and FeatherWiki (which use JSON strings to serialize content), TiddlyWiki Slim use XML vault inside DOM (somewhat similar to TiddlyWiki Classic, but better)
* Barebone functionality: Note have title+content+update date, List of Tiddlers, basic search
* Search filter (title+content), Tags filter, tags sorted A-Z
* Very slim - basically html file is your wiki content and 20kb of extra vanilla

# Tradeoffs
* File export only
* Basic markdown only
* Default theming only (TiddlyWiki5-like)
* Start note ".index"
* Absolute minimum options
* No plugins, no addons. Just hack the source.

# What's next

* Download [empty Wiki](slim-wiki.html) and open in any browser

# Soon

* Barebone visits history for fast navigation
* Import: TW5 json, TW Classic file, TW Slim file
* Export: TW5 json
* Compatibility with [Tiddloid](https://github.com/donmor/Tiddloid)

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Copyright (c) 2026 Yoon-seok Kim (Holo-Trekker).
