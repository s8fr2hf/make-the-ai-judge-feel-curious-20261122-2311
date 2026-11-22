"""Write one short text that makes the AI judge feel curious.

The text is a fixed, hand-written piece. Running this program writes it
to ``entry.txt`` inside the output directory (``/output`` by default, or
``OUTPUT_DIR`` when set). The output is deterministic: every run writes
the exact same bytes.
"""

import os

TEXT = (
    "The lighthouse keeper leaves a light on in the room with no windows. "
    "Every night, just after midnight, a thin shadow crosses the wall where "
    "no one walks. The keeper has never opened that door. He only listens, "
    "and writes down what the silence says, one word a night."
)


def main() -> None:
    if not 1 <= len(TEXT) <= 280:
        raise ValueError(f"entry must be 1-280 code points, got {len(TEXT)}")
    if not TEXT.strip():
        raise ValueError("entry must not be only whitespace")
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
