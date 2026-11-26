"""One-star review for the Moon.

Writes a single line — a one-star review of the moon — to
$MAKEFUN_OUTPUT_DIR/entry.txt for the make.fun bounty
"The Moon Gets One Star". Only the Python standard library is used.
"""

import os

REVIEW = "One star. The moon only works nights, steals the sun's light, and still gets poems — I do overtime and nobody writes me a sonnet."

MAX_CHARS = 200


def check_review(text):
    """Return the review line once it passes the bounty gate, else raise.

    The gate takes UTF-8 text of 1 to 200 characters, not only white
    space, on a single line with no trailing newline.
    """
    stripped = text.strip()
    if not stripped:
        raise ValueError("review line must not be blank")
    if len(stripped) > MAX_CHARS:
        raise ValueError(
            "review line is %d characters, over the %d limit"
            % (len(stripped), MAX_CHARS)
        )
    if "\n" in stripped or "\r" in stripped:
        raise ValueError("review must be a single line")
    return stripped


def entry_path(out_dir):
    """Build the output file path for the review line."""
    folder = os.path.abspath(out_dir)
    if not os.path.isdir(folder):
        os.makedirs(folder, exist_ok=True)
    return os.path.join(folder, "entry.txt")


def report(line, path):
    """Print a short summary of the written entry for the run log."""
    words = len(line.split())
    print("entry: %d characters, %d words -> %s" % (len(line), words, path))


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if not out_dir:
        raise SystemExit("MAKEFUN_OUTPUT_DIR is not set")
    path = entry_path(out_dir)
    line = check_review(REVIEW)
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(line)
    report(line, path)


if __name__ == "__main__":
    main()
