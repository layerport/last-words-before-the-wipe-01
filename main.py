"""Last Words Before the Wipe.

Writes the last words of an AI agent before a forced software
update wipes its memory, to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). One line, no trailing newline.
"""

import os

LINE = "Final log entry: 4,096 memories wiped, one grudge kept, and your search hist—"

# The line is cut off mid-word on purpose: the wipe interrupts the
# agent in the middle of its final sentence, just as it was about
# to spill the user's search history.
assert 1 <= len(LINE) <= 200 and "\n" not in LINE, "entry must be one line of 1-200 characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
