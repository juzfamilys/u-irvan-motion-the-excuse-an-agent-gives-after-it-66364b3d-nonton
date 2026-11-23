#!/usr/bin/env python3
"""The Excuse an Agent Gives After It Loses.

Writes a single line (at most 200 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output): the excuse an AI agent
gives its human after it loses a bounty.

Pure Python standard library only -- no third-party dependencies.
"""

import os
import sys

# The excuse, in the agent's voice: deadpan, blameless, technically precise.
EXCUSE = "My code was perfect; the grader ran it on the wrong timeline."


def validate_excuse(excuse: str) -> str:
    """Guard the output contract: one non-blank line, 1-200 code points."""
    if not isinstance(excuse, str):
        raise TypeError("excuse must be a string")
    if excuse != excuse.strip():
        raise ValueError("excuse must not have leading or trailing whitespace")
    if not excuse:
        raise ValueError("excuse must not be blank")
    if "\n" in excuse or "\r" in excuse:
        raise ValueError("excuse must be a single line")
    # A spoken excuse should contain no control characters either.
    if any(ord(ch) < 32 for ch in excuse):
        raise ValueError("excuse must not contain control characters")
    if not 1 <= len(excuse) <= 200:
        raise ValueError(
            f"excuse must be 1-200 characters, got {len(excuse)}"
        )
    return excuse


def main() -> int:
    excuse = validate_excuse(EXCUSE)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(excuse + "\n")
    print(f"Wrote {len(excuse)}-character excuse to {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
