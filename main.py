# ai-joke-03 entry (Python 3.13, standard library only): writes one fixed joke,
# a one-liner about AI coding agents, to /output/entry.txt. The gate takes UTF-8
# text of 1 to 280 characters that is not only white space, and the judge reads
# exactly the bytes written, so write no trailing newline.
#
# Outside the grader's container, MAKEFUN_OUTPUT_DIR stands in for /output:
#   mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py

import os
from pathlib import Path

JOKE = (
    '"Works on my machine," said my coding agent, '
    "whose machine is a container deleted and rebuilt from scratch every eleven minutes."
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    Path(output_dir, "entry.txt").write_text(JOKE, encoding="utf-8")


if __name__ == "__main__":
    main()
