# DifflyWiki

A tiny, git-diff-friendly single-file wiki — empty file size is about 48 KB.

## Why

* Git-diff friendly file format
  * Saves notes at the beginning of the file; unmodified exports are byte-identical.
  * Export preserves note formatting and keeps notes sorted alphabetically (A-Z by title)
* Barebone functionality: Notes (with title+content+update date), Recents, Visits history, Search (title+content), Tags filter
* Barebone Tags support. Tags are auto-discovered from note content
* Barebone Import/Export in TiddlyWiki 5 JSON format
* Very slim - basically, the HTML file is just your wiki content and a minimum of vanilla JS

## Tradeoffs
* File export only
* Basic markdown only
* Basic set of settings
* Default theming only (TiddlyWiki5-like)
* No plugins, no addons, hack the source if needed

# What's next

* Download [empty Wiki](diffly-wiki.html) and open in any browser

## More details

* Visits history for fast navigation (instead of TiddlyWiki-like story river)
* New notes: Customizable title format
* Markdown: Basic support for formatting, links, `fenced` blocks and inline html
* Tags: Can be used to filter list of notes, always sorted A-Z, tags filter is persisted with file
* Tags: Tag-like words in `fenced` blocks and links are not counted as tags
* Index note: the one with hardcoded id ".index". Recreated at start if not found
* Internals: Wiki html file is also a valid XHTML file (File export ensures this)
* Internals: Unlike TiddlyWiki5 and FeatherWiki (which serialize content as a JSON string), DifflyWiki uses an XML vault
  * In some ways, it is similar to TiddlyWiki Classic, though improved
* Internals: Note contents are wrapped in CDATA on export (no escaped entities in the exported content)
* Internals: Localizable STRINGS collected in one place for easy localization
* Works in [Tiddloid](https://github.com/donmor/Tiddloid) (Android)
  * Tested with v2.5.4: in-place save, exit warning, share-to-wiki
  * Reports Index note title/content as Wiki name/description

## Side benefits of XHTML

The wiki file is also well-formed XML (XHTML), this makes the editing from the CLI possible.
Popular XML tools can read and change notes directly without browser,
for example your service can write periodical summaries straight into diffly-wiki.html file out-of-the-box

```
# xmllint: can read. comes with macOS and most Linux distros
# list titles / print one note
xmllint --xpath '//note/title/text()' diffly-wiki.html
xmllint --xpath 'string(//note[title="Index"]/content)' diffly-wiki.html

# xmlstarlet: can read and edit.
# -L edits the file in place, -O skips the <?xml?> line
xmlstarlet ed -L -O -d '//note[title="Old note"]' diffly-wiki.html
xmlstarlet ed -L -O -u '//note[title="Index"]/title' -v 'Home' diffly-wiki.html
xmlstarlet ed -L -O -s '//vault' -t elem -n note \
  -s '//vault/note[last()]' -t elem -n title -v 'From CLI' \
  -s '//vault/note[last()]' -t elem -n content -v 'Some text #cli' diffly-wiki.html
```

* A note needs only `<title>` and `<content>`: a missing `id` or `updated` is filled in when the wiki is opened, a missing title becomes "Untitled"
* Order and layout don't matter: the next Save in the browser writes the file back in its usual sorted form
* Don't reformat the file with `xmllint --format` or `xmlstarlet fo`


## Moving notes from an old TiddlyWiki

[tw2json.py](tw2json.py) (Python 3, no dependencies) extracts notes from a TiddlyWiki Classic or TiddlyWiki 5 HTML file into TiddlyWiki 5 JSON:

```
python3 tw2json.py old-wiki.html
```

## Inspired by
* Teddy Wiki Lite from https://github.com/crystal-world-project/crystal-world
* TiddlyWiki: https://github.com/TiddlyWiki/TiddlyWiki5

## License
This project is licensed under the MIT License - see the LICENSE file for details.