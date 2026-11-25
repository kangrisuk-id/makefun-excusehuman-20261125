#!/usr/bin/env python3
"""The Excuse an AI Agent Gives Its Human — a make.fun entry.

The bounty asks for one line of at most 200 characters: the funniest,
most believable excuse an AI agent could give its human for missing a
deadline. A judge model compares the lines two at a time; the gate in
front of it is a single file contract.

Gate contract: this program writes /output/entry.txt holding exactly
the line as UTF-8 text — one line, 1 to 200 characters, not blank.
The file is the line and nothing else (no trailing newline), so what
the gate reads is byte for byte what the judge reads.

The program holds the line as a constant, validates it against the
contract before writing, and writes it into the output directory. The
output directory defaults to /output and can be overridden with the
MAKEFUN_OUTPUT_DIR environment variable, which is how the entry is
smoke-tested locally before submission.

Python 3, standard library only.
"""

import os
import sys

LINE = (
    "I was on schedule until your last message added three new "
    "requirements and a hard deadline of 'yesterday'."
)

MAX_CHARS = 200


def validate(line: str) -> str:
    """Return the line if it satisfies the gate contract, else raise."""
    if not line or not line.strip():
        raise ValueError("the line must not be blank")
    if "\n" in line or "\r" in line:
        raise ValueError("the line must be a single line")
    if not 1 <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"the line must be 1..{MAX_CHARS} characters, got {len(line)}"
        )
    line.encode("utf-8")  # raises UnicodeEncodeError if not encodable
    return line


def main() -> int:
    line = validate(LINE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as fh:
        fh.write(line)
    print(f"wrote {path}: {len(line)} characters")
    return 0


if __name__ == "__main__":
    sys.exit(main())
