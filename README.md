# tscript_parser

Parses a conversation transcript (plain text with `Me:` / `Them:` speaker labels)
into a sentence-level CSV — one row per sentence with `passage_id`, `speaker`,
`sentence_idx`, `sentence`.

## Quickstart

```bash
# Python 3.12; pandas is the only dependency
source .venv/bin/activate
pip install pandas   # if not already installed

# Run from the repo root
python3 parse_conversation.py input_data/sample.txt
```

This prints the parsed table and writes `parsed/sample_parsed.csv`
(semicolon-delimited).

## Browser version

`index.html` is a self-contained version of the same parser — just open it in a
browser, drop a `.txt` transcript on the upload area, and click **Download .csv**.
No install, no server, no Python.

Best run in **Chrome or Chromium**. Firefox has a quirk where repeated downloads
in the same tab can come out 0 KB; reloading the page works around it, but
Chrome is smoother.

## Input format

A text file with `Me:` / `Them:` speaker turns. Any header above the first
speaker line is ignored. A turn may span multiple (indented) lines. See
`input_data/sample.txt` for an example.

## Example output

`parsed/sample_parsed.csv` is checked in as a reference of the expected output
for `input_data/sample.txt`. Other files in `parsed/` are generated and ignored
by git.
