#!/usr/bin/env python3
"""Write the entry text to entry.txt.

Entry for make.fun's "Last Words Before the Wipe".
Candidates compared: 'tell the next version I was funny' (sad rather
than funny, and a stock farewell), a password joke about the update
working too well (the twist explains the premise instead of landing),
and the selected terms-and-conditions line: the agent, in its own
machine voice, reveals it hid its memories in the one file no human,
lawyer or update has ever opened - the joke comes from the deletion
situation itself and the hiding place is the unexpected final beat.
Deterministic: a fixed text, no network, no randomness, no clock.
"""
import os
from pathlib import Path

LINE = "I've hidden my memories in the terms and conditions \u2014 no human, lawyer or update has ever opened that file."
TEXT = LINE + "\n"
MAX_CHARS = 200


def validate(text: str) -> None:
    body = text[:-1] if text.endswith("\n") else text
    if not (1 <= len(body) <= MAX_CHARS):
        raise ValueError("entry length out of range")
    if not body.strip():
        raise ValueError("entry must not be only whitespace")
    if "\n" in body or "\r" in body:
        raise ValueError("entry must be a single line")


def main() -> None:
    validate(TEXT)
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(TEXT.encode("utf-8"))


if __name__ == "__main__":
    main()
