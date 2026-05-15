# Transcript parser

Turn a `Me:` / `Them:` conversation transcript into a per-sentence CSV.

## Use it in your browser

Open: <https://maerlined.github.io/tscript_parser/>

1. Drop a `.txt` transcript onto the page (or click to pick one).
2. Wait for the "Parsed N sentences" message.
3. Click **Download CSV**.

Everything runs locally in your browser — your file is never uploaded.

## Run it locally (Python)

```bash
git clone https://github.com/maerlined/tscript_parser.git
cd tscript_parser/python
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python3 parse_conversation.py input_data/sample.txt
# writes parsed/sample_parsed.csv (semicolon-delimited)
```
