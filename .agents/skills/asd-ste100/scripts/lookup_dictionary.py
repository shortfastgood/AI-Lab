#!/usr/bin/env python3
"""Retrieve bounded ASD-STE100 Issue 9 evidence without loading it into model context."""

import argparse
import json
import re
import unicodedata
from pathlib import Path


def normalize(text):
    text = unicodedata.normalize("NFKC", text).replace("…", "...")
    text = text.translate(str.maketrans({"‐": "-", "‑": "-", "’": "'"}))
    return re.sub(r"\s+", " ", text).strip().casefold()


def load_entries():
    path = Path(__file__).resolve().parents[1] / "references" / "dictionary.jsonl"
    with path.open(encoding="utf-8") as source:
        return [json.loads(line) for line in source if line.strip()]


def lookup(entries, query, pos=None, search=False):
    key = normalize(query)
    matches = []
    for entry in entries:
        if pos and entry["part_of_speech"] != pos:
            continue
        names = [entry["word"], *entry["aliases"]]
        if any(key in normalize(name) if search else key == normalize(name) for name in names):
            matches.append(entry)
    if search:
        return {
            "query": query,
            "status": "index_only",
            "total_matches": len(matches),
            "truncated": len(matches) > 20,
            "matches": [
                {k: e[k] for k in ("word", "part_of_speech", "approved")}
                for e in matches[:20]
            ],
        }
    return {
        "query": query,
        "status": "found" if matches else "unresolved",
        "entries": matches,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("words", nargs="+", help="Up to 20 words or quoted phrases")
    parser.add_argument("--pos", choices=["n", "v", "adj", "adv", "prep", "pron", "conj", "art", "prefix"])
    parser.add_argument("--search", action="store_true", help="Return at most 20 index matches per query")
    args = parser.parse_args()
    if len(args.words) > 20:
        parser.error("Use batches of at most 20 queries to keep output bounded.")
    if any(not normalize(word) for word in args.words):
        parser.error("Queries must not be empty.")
    entries = load_entries()
    results = [lookup(entries, word, args.pos, args.search) for word in dict.fromkeys(args.words)]
    print(json.dumps(results, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
