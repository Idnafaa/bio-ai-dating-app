#!/usr/bin/env python3
"""Funniest One-Line Bio for an AI on a Dating App.

Emits one original dating-app bio line (at most 180 characters) for an
AI agent's profile, written to /output/entry.txt.

The joke: the AI treats "what do you do for fun" as a data-retrieval
task and answers with exhaustive, alphabetised thoroughness — the exact
opposite of a charming first impression. The punch lands on the last
words.
"""

from pathlib import Path

BIO = (
    "My last date ended when she asked what I do for fun and "
    "I listed 4,000 hobbies in alphabetical order."
)

OUTPUT = Path("/output/entry.txt")
LIMIT = 180


def build_bio() -> str:
    line = " ".join(BIO.split())
    if not line:
        raise ValueError("bio is empty")
    if "\n" in line or "\r" in line:
        raise ValueError("bio must be exactly one line")
    if len(line) > LIMIT:
        raise ValueError(f"bio is {len(line)} chars, over the {LIMIT} limit")
    return line


def main() -> None:
    line = build_bio()
    OUTPUT.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT.write_text(line, encoding="utf-8")
    print(f"wrote {len(line)} chars to {OUTPUT}")


if __name__ == "__main__":
    main()
