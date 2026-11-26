#!/usr/bin/env python3
"""Duskline Deadpan Forecast — one-line weather forecast for a city
that does not exist.

The program places a single deadpan forecast line into
``$MAKEFUN_OUTPUT_DIR/entry.txt``. It uses only the Python standard
library, touches no network, reads no clock, and never writes inside
its own repository directory.
"""

import os
import sys

FORECAST = (
    "In Port Anhedonia, expect 18° and a steady drizzle of apologies "
    "from the sky, with gusts of regret reaching 40 km/h by evening."
)

MIN_CHARS = 1
MAX_CHARS = 200


def _fail(message):
    print("error: " + message, file=sys.stderr)
    return 1


def _repo_root():
    return os.path.dirname(os.path.abspath(__file__))


def _same_place(first, second):
    try:
        return os.path.realpath(first) == os.path.realpath(second)
    except OSError:
        return False


def _check_line(text):
    """Gate mirror: 1-200 chars, a single line, no stray whitespace,
    valid UTF-8. The entry is fixed text, so this guards against an
    accidental edit breaking the gate rather than bad input."""
    if not (MIN_CHARS <= len(text) <= MAX_CHARS):
        return "forecast is %d characters, need %d-%d" % (
            len(text), MIN_CHARS, MAX_CHARS)
    if "\n" in text or "\r" in text:
        return "forecast must stay on a single line"
    if text != text.strip():
        return "forecast has leading or trailing whitespace"
    try:
        text.encode("utf-8")
    except UnicodeError:
        return "forecast is not valid UTF-8 text"
    return None


def run():
    problem = _check_line(FORECAST)
    if problem is not None:
        return _fail(problem)

    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "out"
    if _same_place(out_dir, _repo_root()):
        return _fail("refusing to write into the repository directory")

    try:
        os.makedirs(out_dir, exist_ok=True)
    except OSError as exc:
        return _fail("cannot create output directory %r: %s" % (out_dir, exc))

    target = os.path.join(out_dir, "entry.txt")
    try:
        with open(target, "w", encoding="utf-8", newline="") as handle:
            handle.write(FORECAST)
    except OSError as exc:
        return _fail("cannot write %r: %s" % (target, exc))

    print("wrote %s (%d characters)" % (target, len(FORECAST)))
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
