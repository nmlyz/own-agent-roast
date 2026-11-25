#!/usr/bin/env python3
"""Write one roast line about this program's own coding agent.

The line is a single sentence (82 characters): the agent "solves" a problem
by redefining it, then wants applause for the solution. It is written to
/output/entry.txt, byte for byte the same on every run.
"""

import os

LINE = "My agent solved the problem by redefining it, then asked why I wasn't celebrating."


def output_directory():
    return os.environ.get("OUTPUT_DIR", "/output")


def main():
    out_dir = output_directory()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(LINE + "\n")
    os.chmod(path, 0o644)
    with open(path, "r", encoding="utf-8", newline="\n") as handle:
        written = handle.read()
    if written != LINE + "\n":
        raise SystemExit("entry.txt does not match the roast line")


if __name__ == "__main__":
    main()
