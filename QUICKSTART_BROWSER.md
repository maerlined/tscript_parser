## How to use

1. Drop a `.txt` transcript on the upload area above (or click **Upload file**).

2. A preview appears showing the output (see formatting below)
   **Example:** 1;Me;1;The first sentence appears here.;
3. Click **Download .csv** to save `<filename>_parsed.csv`.

The CSV is semicolon-delimited and ready to import in Google Sheets, Excel, or
any other spreadsheet tool. Everything runs in your browser, nothing is
uploaded anywhere.

## Input format

A text file with `Me:` / `Them:` speaker turns. Any header above the first
speaker line is ignored. A turn may span multiple lines.

Example:

```
Me: Hey, how are you doing today? I hope everything's been going well.
        I was wondering if you wanted to grab lunch sometime this week.
Them: I'm doing really well, thanks for asking.
      Yes, that sounds like a great idea.
```

## Output

The CSV has four columns:

- `passage_id` — increments by 1 per speaker turn
- `speaker` — `Me` or `Them`
- `sentence_idx` — sentence number within the turn (resets at 1)
- `sentence` — the sentence text

## Browser

Best run in **Chrome or Chromium**. Firefox has a quirk where repeated downloads
in the same tab can come out 0 KB; reloading the page works around it, but
Chrome is smoother.
