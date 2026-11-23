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


if __name__ == "__main__":
    main()
