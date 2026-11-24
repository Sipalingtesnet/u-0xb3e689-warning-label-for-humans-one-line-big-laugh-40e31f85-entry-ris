#!/usr/bin/env python3
"""Write this entry's one-line warning label to /output/entry.txt.

The competition asks for a single line of at most 160 characters: the
safety warning label that should come printed on every human being. This
program writes exactly that text and nothing else, so the bytes on disk
are a pure function of the source below: no clock, no randomness, no
network, no arguments, no settings read from outside the file. Two runs
write identical bytes.
"""

from __future__ import annotations

import os
import sys

# The entry. One line, no internal newline, ASCII only, so the character
# count and the byte count agree at every length check.
#
# Revision history. The first draft read:
#   "...the unit will defend them for forty minutes, then change the subject."
# The second is the sharper line:
#   "...the unit will argue for forty minutes, then change the subject,
#    undefeated."
# "Defend" is the expected verb for an opinion and it clashes with the
# label's own machinery; "argue" is what people actually do. And the first
# draft stopped on the neutral phrase "change the subject", which let the
# joke fade out. Trailing ", undefeated." puts the last word on the unit's
# own self-assessment, so the punch is the final word and it names the exact
# behaviour: nobody concedes, everybody leaves believing they won.
LABEL = (
    "CAUTION: Opinions installed at seventeen, never serviced. "
    "Do not challenge them; the unit will argue for forty minutes, "
    "then change the subject, undefeated."
)

# The gate accepts UTF-8 text of 1 to 160 characters that is not only
# white space. Asserting the ceiling here means a bad edit fails loudly
# instead of shipping an entry the gate would throw out.
MAX_CHARS = 160

OUTPUT_DIR = "/output"
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


def validate(text: str) -> str:
    """Check the label against the gate, or raise with the reason.

    The gate is a sealed scorer, so this mirrors the published wording: one
    to 160 characters of UTF-8 text, not only white space, on a single line.
    """
    if "\n" in text or "\r" in text:
        raise SystemExit("label must be a single line")
    if not text.strip():
        raise SystemExit("label must not be only white space")
    if len(text) > MAX_CHARS:
        raise SystemExit(
            f"label is {len(text)} characters, over the {MAX_CHARS} limit"
        )
    if len(text.strip()) != len(text):
        raise SystemExit("label must not start or end with white space")
    # Only fails on lone surrogates, which cannot be written as UTF-8.
    text.encode("utf-8").decode("utf-8")
    return text


def write_entry(path: str = OUTPUT_PATH) -> str:
    """Write the label as exactly one line and return the text written."""
    text = validate(LABEL)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    # newline="\n" keeps the byte on disk identical on every platform.
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(text + "\n")
    return text


def main() -> int:
    text = write_entry()
    # Progress goes to stderr so stdout stays clean in case a caller reads it.
    print(f"wrote {len(text)} characters to {OUTPUT_PATH}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
