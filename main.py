#!/usr/bin/env python3
"""One Emoji, One Smile — make.fun entry.

Writes exactly one emoji to /output/entry.txt: the hugging face.
No words, no caption, no explanation — the brief asks for one emoji
and nothing else.
"""

import os

EMOJI = "\U0001f917"  # 🤗 Hugging Face: open arms, a warm hug.
OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(EMOJI)
    # Self-check: the gate wants UTF-8 text of 1 to 8 characters,
    # not only white space. Fail loudly here rather than in grading.
    with open(OUTPUT_PATH, encoding="utf-8") as f:
        written = f.read()
    assert 1 <= len(written) <= 8 and written.strip(), "entry.txt must hold 1-8 non-blank characters"
    assert written == EMOJI, "entry.txt must hold exactly the chosen emoji"


if __name__ == "__main__":
    main()
