# TiddlyWiki Slim

Slim version of TiddlyWiki — empty file size is less than 50 KB.

## Why

* Git-diff friendly file format
  * Saves notes at the beginning of the file; unmodified exports are byte-identical.
  * Export preserves note formatting and keeps notes sorted alphabetically (A-Z by title)
* Barebone functionality: Notes (with title+content+update date), Recents, Visits history, Search (title+content), Tags filter
* Barebone Tags support. Tags are auto-discovered from note content, sorted A-Z for filtering
* Import/Export in TW5 json format
* Very slim - basically, the HTML file is just your wiki content and a minimum of vanilla JS

## Tradeoffs
* File export only
* Basic markdown only
* Basic set of settings
* Default theming only (TiddlyWiki5-like)
* No plugins, no addons, hack the source if needed

# What's next

* Download [empty Wiki](slim-wiki.html) and open in any browser

## More details

* Visits history for fast navigation (instead of TW-like story river)
* New notes: Customizable title format
* Index note: the one with hardcoded id ".index". Recreated at start if not found
* Basic markdown support: formatting, links, `fenced` blocks and inline html
* Internals: Unlike TiddlyWiki5 and FeatherWiki (which serialize content as a JSON string), TiddlyWiki Slim uses an XML vault
  * In some ways, it is similar to TiddlyWiki Classic, though improved
* Internals: Note contents are wrapped in CDATA on export (no escaped entities in the exported content)
* Internals: Localizable STRINGS collected in one place for easy localization
* Internals: Tag-like words in `fenced` blocks and links are not counted as tags
* Works in [Tiddloid](https://github.com/donmor/Tiddloid) (Android)
  * Tested with v2.5.4: in-place save, exit warning, share-to-wiki
  * Reports Index note title/content as Wiki name/description

## Inspired by
* Teddy Wiki Lite from https://github.com/crystal-world-project/crystal-world
* TiddlyWiki: https://github.com/TiddlyWiki/TiddlyWiki5

## License
This project is licensed under the MIT License - see the LICENSE file for details.