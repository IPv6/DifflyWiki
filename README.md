# TiddlyWiki Slim

Slim version of TiddlyWiki — empty file size is around 22 KB.

## Why TiddlyWiki Slim

* Git-diff friendly file format
  * Notes are saved at the beginning of the file, whithout changes export is byte-identical
  * Formatting of the notes content is preserved, stable note order (A-Z, based on title)
  * Unlike TiddlyWiki5 and FeatherWiki (which use JSON strings to serialize content), TiddlyWiki Slim use XML vault inside DOM (somewhat similar to TiddlyWiki Classic, but better)
* Barebone functionality: Notes (with title+content+update date), List of Tiddlers, Search
* Tags auto-discovered from content, sorted A-Z for convenience
* Search filter (title+content), Tags filter
* Very slim - basically html file is your wiki content and minimum of vanilla js

# Tradeoffs
* Absolute minimum options
* File export only
* Basic markdown only
* Default theming only (TiddlyWiki5-like)
* Start note hardcoded to ".index" note
* No plugins, no addons. Just hack the source.

# What's next

* Download [empty Wiki](slim-wiki.html) and open in any browser

# Soon

* Visits history block, for fast navigation (instead of story river)
* Import: TW5 json, TW Classic file, TW Slim file
* Export: TW5 json
* Compatibility with [Tiddloid](https://github.com/donmor/Tiddloid)

## Inspired by
* Teddy Wiki Lite from https://github.com/crystal-world-project/crystal-world
* TiddlyWiki: https://github.com/TiddlyWiki/TiddlyWiki5

## License
This project is licensed under the MIT License - see the LICENSE file for details.