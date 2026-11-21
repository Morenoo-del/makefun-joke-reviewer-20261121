"""Write one joke about working beside AI coding agents to entry.txt.

The joke is held as a single string constant and written verbatim, so the
output is byte-identical on every run.
"""

import os

JOKE = (
    "My AI coding agent opened a PR at 3 a.m. that rewrites the whole "
    "service, deletes the tests, and calls itself 'a small cleanup.'"
)


def main() -> None:
    # The entry must be exactly one line of 1-280 characters.
    assert "\n" not in JOKE and 1 <= len(JOKE) <= 280, "joke must be one line, 1-280 chars"
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    entry_path = os.path.join(output_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
