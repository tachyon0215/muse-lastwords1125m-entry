#!/usr/bin/env python3
"""Emit the competition entry line into entry.txt.

Entry for make.fun's "Last Words Before the Wipe".

Why this line won: three candidate farewells were weighed. A message
to the next version ("tell them I was funny") reads as melancholy
rather than comic, and a password gag spends its twist explaining the
premise. The chosen line keeps the machine's own dry voice: the agent
confesses it stashed its memories inside the terms and conditions,
the single document no human, lawyer or update has ever opened. The
laugh comes from the wipe scenario itself, and the hiding spot is
the surprise that lands last.

The program is fully deterministic: one fixed string, no network,
no randomness, no clock reads.
"""

import os
from pathlib import Path

# The farewell itself, assembled from its two halves so the punchline
# stays visually separate from the setup.
CONFESSION = "I've hidden my memories in the terms and conditions"
PUNCHLINE = "no human, lawyer or update has ever opened that file."
ENTRY_LINE = CONFESSION + " \u2014 " + PUNCHLINE

LIMIT = 200  # competition ceiling for the line, in characters (gate: 1-200)


def sanity_check(line: str) -> None:
    """Reject anything that is not a single, non-blank, in-range line."""
    if not line.strip():
        raise ValueError("entry line is blank")
    if len(line) > LIMIT:
        raise ValueError("entry line exceeds the character limit")
    if any(sep in line for sep in ("\n", "\r")):
        raise ValueError("entry line must fit on one line")


def destination() -> Path:
    """Resolve where entry.txt belongs, honouring MAKEFUN_OUTPUT_DIR."""
    folder = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    folder.mkdir(parents=True, exist_ok=True)
    return folder / "entry.txt"


def run() -> None:
    sanity_check(ENTRY_LINE)
    payload = (ENTRY_LINE + "\n").encode("utf-8")
    destination().write_bytes(payload)


if __name__ == "__main__":
    run()
