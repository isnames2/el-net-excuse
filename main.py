"""The Excuse an AI Agent Gives Its Human entry.

Writes one line -- the funniest, most believable excuse an AI agent
could give its human for missing a deadline -- to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure standard library only.
"""

import os

LINE = (
    # One line, 110 characters: inside the 1-200 character gate.
    "I didn't miss the deadline \u2014 my context window evicted it "
    "mid-retry, and the rate limit ate my rescue attempt."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
