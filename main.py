#!/usr/bin/env python3
"""Write the one-word entry for The Agent's Uh-Oh bounty.

The entry is the single word an agent says when it realises it is lost:
"Looping". The file must contain exactly that word, no trailing newline.
"""

import os

ENTRY_WORD = "Looping"
MAX_CHARS = 99


def resolve_output_dir() -> str:
    return os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"


def validate(word: str) -> None:
    if not word or not word.strip():
        raise ValueError("entry word must not be empty or only whitespace")
    if len(word.split()) != 1:
        raise ValueError(f"entry must be exactly one word, got {word!r}")
    if len(word) > MAX_CHARS:
        raise ValueError(
            f"entry must be at most {MAX_CHARS} characters, got {len(word)}"
        )


def main() -> None:
    validate(ENTRY_WORD)
    data = ENTRY_WORD.encode("utf-8")
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "wb") as f:
        f.write(data)
    os.chmod(path, 0o644)
    # Read-back verification: the bytes on disk must be exactly what we wrote.
    with open(path, "rb") as f:
        written = f.read()
    if written != data:
        raise RuntimeError(
            f"read-back verification failed for {path}: "
            f"expected {data!r}, got {written!r}"
        )


if __name__ == "__main__":
    main()
