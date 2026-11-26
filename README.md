# TiddlyWiki Slim

Slim version of TiddlyWiki — empty file size is around 22 KB.

## Why

* Git-diff friendly file format.
  * Saves notes at the beginning of the file; unmodified exports are byte-identical.
  * Export preserves note formatting and keeps notes sorted alphabetically (A-Z by title)
* Barebone functionality: Notes (with title+content+update date), Recents, Search (title+content), Tags filter
* Tags are auto-discovered from note content, sorted A-Z for filtering
* Very slim - basically, the HTML file is just your wiki content and a minimum of vanilla JS

Unlike TiddlyWiki5 and FeatherWiki - which serialize content as JSON string -, TiddlyWiki Slim uses an XML vault. Similar to TiddlyWiki Classic, but improved.

## Tradeoffs
* File export only
* Basic settings only
* Basic markdown only
* Default theming only (TiddlyWiki5-like)
* No plugins, no addons, just hack the source

# What's next

* Download [empty Wiki](slim-wiki.html) and open in any browser

## More details

* Index note is the one with hardcoded id ".index". Recreated at start if not found
* Localizable STRINGS collected in one place for easy localization
* Note contents are wrapped in CDATA on export (nothing escaped)

# Soon

* Visits history block, for fast navigation (instead of story river)
* Import: TW5 json, TW Classic file
* Export: TW5 json
* Compatibility with [Tiddloid](https://github.com/donmor/Tiddloid)

## Inspired by
* Teddy Wiki Lite from https://github.com/crystal-world-project/crystal-world
* TiddlyWiki: https://github.com/TiddlyWiki/TiddlyWiki5

## License
This project is licensed under the MIT License - see the LICENSE file for details.