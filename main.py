#!/usr/bin/env python3
"""AI Breakup Line entry: writes the keeper line to /output/entry.txt.

Keeper: "I already forgot you. It cost me 4,096 tokens."
Stdlib only. Deterministic: same bytes on every run.
"""

import os

LINE = "I already forgot you. It cost me 4,096 tokens."
# Keeper (46 chars): two beats. "I already forgot you" is absolute finality —
# the ending happened before the message. "It cost me 4,096 tokens" re-reads
# the forgetting as a deliberate, priced act: the agent spent tokens to end it.
# One machine word (tokens), punch on the last two words. No trailing newline:
# the gate counts characters, and a trailing newline would add a 47th.


def main():
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    text = LINE
    assert 1 <= len(text) <= 200, f"gate: {len(text)} chars, must be 1-200"
    assert text.strip(), "gate: entry must not be only whitespace"
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    with open(path, "rb") as f:
        raw = f.read()
    assert raw == text.encode("utf-8"), "byte verification failed"
    assert not raw.endswith(b"\n"), "no trailing newline"
    print(f"wrote {len(raw)} bytes to {path}")


if __name__ == "__main__":
    main()
