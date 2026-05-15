# tscript_parser

Parses a conversation transcript (plain text with `Me:` / `Them:` speaker labels)
into a sentence-level CSV — one row per sentence with `passage_id`, `speaker`,
`sentence_idx`, `sentence`.

Two equivalent versions live in this repo:
- **`index.html`** — self-contained browser page. No install, no server, no Python.
- **`run-with-python/`** — the original Python CLI.

## Browser version

Open `index.html` in a browser, then:

1. Drop a `.txt` transcript on the upload area (or click **Upload file**).
2. Check the preview that appears to confirm it parsed correctly.
3. Click **Download .csv** to save `<filename>_parsed.csv`.

Best run in **Chrome or Chromium**. Firefox has a quirk where repeated downloads
in the same tab can come out 0 KB; reloading the page works around it, but
Chrome is smoother.

## Python CLI

```bash
cd run-with-python

# First time only: create a venv and install pandas (the only dependency)
python3 -m venv .venv
source .venv/bin/activate
pip install pandas

# Parse a transcript
python3 parse_conversation.py input_data/sample.txt
```

Prints the parsed table and writes `parsed/<stem>_parsed.csv`
(semicolon-delimited). Run from inside `run-with-python/` — the script writes
output relative to the current directory.

## Input format

A text file with `Me:` / `Them:` speaker turns. Any header above the first
speaker line is ignored. A turn may span multiple (indented) lines. See
`run-with-python/input_data/sample.txt` for an example.

## Output

The CSV has four columns:

- `passage_id` — increments by 1 per speaker turn
- `speaker` — `Me` or `Them`
- `sentence_idx` — sentence number within the turn (resets at 1)
- `sentence` — the sentence text

`run-with-python/parsed/sample_parsed.csv` is checked in as a reference of the
expected output for `run-with-python/input_data/sample.txt`. Other files in
`run-with-python/parsed/` are generated and ignored by git.
