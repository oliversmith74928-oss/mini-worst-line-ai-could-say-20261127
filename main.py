"""The Worst Line an AI Could Say -- make.fun entry.

Writes the entry (a single terrible AI pickup line) to
$MAKEFUN_OUTPUT_DIR/entry.txt. Standard library only, deterministic.
"""

import os

ENTRY = (
    # The line itself is the whole entry: one flat, over-helpful,
    # faintly ominous pickup line, 114 characters, no setup needed.
    "Hi. I ran a million simulations of us meeting. "
    "In 999,999 of them, you said yes. "
    "The last one is why I am shaking."
)


def main():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
