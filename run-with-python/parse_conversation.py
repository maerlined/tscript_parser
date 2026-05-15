#!/usr/bin/env python3
import re
import sys
from pathlib import Path

import pandas as pd

# Matches a full speaker turn (Me/Them) including any indented continuation lines.
TURN_RE = re.compile(
    r'^[ \t]*(Me|Them):\s*(.*?)(?=^[ \t]*(?:Me|Them):|\Z)',
    re.MULTILINE | re.DOTALL,
)

# Split on sentence-ending punctuation followed by whitespace
SENTENCE_RE = re.compile(r'(?<=[.!?])\s+')


def find_transcript(text: str) -> str:
    """Return text starting from the first speaker line, skipping any header."""
    m = re.search(r'^[ \t]*(Me|Them):', text, re.MULTILINE)
    if not m:
        raise ValueError("No transcript found in file")
    return text[m.start():]


def split_sentences(raw: str) -> list[str]:
    """Split a turn into sentences. Fragments under 3 words are merged into
    the preceding sentence. Single-sentence turns are returned as-is."""
    cleaned = re.sub(r'\s+', ' ', raw).strip()
    parts = [s.strip() for s in SENTENCE_RE.split(cleaned) if s.strip()]

    if len(parts) <= 1:
        return parts

    result = []
    pending = None
    for s in parts:
        if pending is not None:
            s = pending + " " + s
            pending = None
        if len(s.split()) < 3:
            pending = s
        else:
            result.append(s)

    if pending is not None:
        if result:
            result[-1] = result[-1] + " " + pending
        else:
            result.append(pending)

    return result


def parse_conversation(filepath) -> pd.DataFrame:
    """Parse a transcript file into a DataFrame (one row per sentence).

    Columns: passage_id, speaker ('Me'/'Them'), sentence_idx, sentence.
    """
    text = Path(filepath).read_text(encoding="utf-8")
    transcript = find_transcript(text)

    rows = []
    for passage_id, m in enumerate(TURN_RE.finditer(transcript), start=1):
        speaker = m.group(1)
        for sentence_idx, sentence in enumerate(split_sentences(m.group(2)), start=1):
            rows.append((passage_id, speaker, sentence_idx, sentence))

    cols = ["passage_id", "speaker", "sentence_idx", "sentence"]
    return pd.DataFrame(rows, columns=cols)


INPUT_DIR = Path("input_data")
OUTPUT_DIR = Path("parsed")


def parse_one(input_path: Path, *, verbose: bool = True) -> None:
    """Parse one transcript and write parsed/<stem>_parsed.csv."""
    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
    output_path = OUTPUT_DIR / (input_path.stem + "_parsed.csv")
    df = parse_conversation(input_path)
    if verbose:
        print(df.to_string(index=False))
        print()
    df.to_csv(output_path, sep=";", index=False)
    print(f"Saved {len(df)} rows -> {output_path}")


def run_batch() -> None:
    """Parse every input_data/*.txt that doesn't yet have a parsed/<stem>_parsed.csv."""
    if not INPUT_DIR.is_dir():
        print(f"{INPUT_DIR}/ not found (run from inside run-with-python/)", file=sys.stderr)
        sys.exit(1)
    todo = sorted(p for p in INPUT_DIR.glob("*.txt")
                  if not (OUTPUT_DIR / (p.stem + "_parsed.csv")).exists())
    if not todo:
        print(f"Nothing to do — every {INPUT_DIR}/*.txt already has a {OUTPUT_DIR}/<stem>_parsed.csv.")
        return
    print(f"Parsing {len(todo)} file(s):")
    for p in todo:
        parse_one(p, verbose=False)


def main():
    """Parse a single transcript, or — with no args — every unparsed input_data/*.txt."""
    if len(sys.argv) == 1:
        run_batch()
        return
    if len(sys.argv) != 2:
        print(f"Usage: {sys.argv[0]} [conversation.txt]", file=sys.stderr)
        sys.exit(1)
    parse_one(Path(sys.argv[1]))


if __name__ == "__main__":
    main()
