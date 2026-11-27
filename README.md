# DifflyWiki

A tiny, git-diff-friendly single-file wiki - an empty wiki is about 48 KB.

## Why

* Git-diff-friendly file format
  * Notes are stored at the beginning of the file; saving without changes gives a byte-identical file
  * Saving preserves note formatting and keeps notes sorted alphabetically (A-Z by title)
* Bare-bones functionality: notes (title, content, update date), recent notes, visit history, search (title and content), tag filter
* Bare-bones tag support: tags are auto-discovered from note content
* Basic import/export in TiddlyWiki 5 JSON format
* Very slim - the HTML file is basically just your wiki content plus a minimum of vanilla JS

## Tradeoffs
* File export only
* Basic Markdown only
* Basic set of settings
* Default theme only (TiddlyWiki 5-like)
* No plugins or add-ons - hack the source if needed

## Getting started

* Download the [empty wiki](diffly-wiki.html) and open it in any browser, or work with it from the command line using XML tools like xmlstarlet

## More details

* Visit history for fast navigation (instead of a TiddlyWiki-style story river)
* New notes: customizable title format
* Markdown: basic support for formatting, links, fenced code blocks and inline HTML
* Tags: filter the note list by tags (always sorted A-Z); the selected filter is saved in the file
* Tags: tag-like words inside code and links are not counted as tags
* Index note: the note with the fixed id `.index`; it opens at start and is recreated if missing
* Internals: unlike TiddlyWiki 5 and FeatherWiki (which store content as a JSON string), DifflyWiki uses an XML vault inside XHTML file
  * The wiki HTML file is also well-formed XML (XHTML-style), and saving keeps it that way
  * Note content is wrapped in CDATA when saved, so file source stays readable (no escaped entities)
  * In some ways it resembles TiddlyWiki Classic, with improvements
* Internals: all UI strings are collected in one STRINGS table for easy localization
* Works in [Tiddloid](https://github.com/donmor/Tiddloid) (Android)
  * Tested with v2.5.4: in-place save, exit warning, share-to-wiki
  * Reports the Index note's title and content as the wiki name and description

## Side benefits of XML

The wiki file is also well-formed XML, which makes editing from the command line possible: popular XML tools can read and change notes directly, without a browser.
For example, a script or service can write periodic summaries straight into diffly-wiki.html, out of the box.

```
# xmllint: read only; comes with macOS and most Linux distros
# list titles / print one note
xmllint --xpath '//note/title/text()' diffly-wiki.html
xmllint --xpath 'string(//note[title="Index"]/content)' diffly-wiki.html

# xmlstarlet: read and edit
# -L edits the file in place, -O skips the <?xml?> line, -P keeps the file's layout
xmlstarlet sel -t -m '//note' -v 'title' -n diffly-wiki.html
xmlstarlet ed -L -O -P -d '//note[title="Old note"]' diffly-wiki.html
xmlstarlet ed -L -O -P -u '//note[title="Index"]/title' -v 'Home' diffly-wiki.html
xmlstarlet ed -L -O -P -s '//vault' -t elem -n note \
  -s '//vault/note[last()]' -t elem -n title -v 'From CLI' \
  -s '//vault/note[last()]' -t elem -n content -v 'Some text #cli' diffly-wiki.html

# yq (mikefarah/yq): read only, with JSON or YAML output; don't write with it (see below)
# [...] | flatten: yq returns a single note as an object and several as a list
yq -p xml -oy '[.html.head.script.vault.note] | flatten | .[].title' diffly-wiki.html
yq -p xml -oy '[.html.head.script.vault.note] | flatten | .[] | select(.title == "Index") | .content' diffly-wiki.html
yq -p xml -oj '[.html.head.script.vault.note] | flatten | map({"id": .["+@id"], "title": .title})' diffly-wiki.html
```

* A new note needs only `<title>` and `<content>`; a missing `id` or `updated` is filled in when the wiki is opened, and a missing title becomes "Untitled"
* Order and layout don't matter: the next Save in the browser writes the file back in its usual sorted form
* xmlstarlet: always pass `-P`. Without it the whole page is re-indented, and the indentation stays in the file after browser saves
* xmlstarlet: a `&` in a `-v` value must be written as `&amp;`
* yq: read-only. When writing XML, it drops the CDATA around the page's script and style, so the page stops working
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
