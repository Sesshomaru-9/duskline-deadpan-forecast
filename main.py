#!/usr/bin/env python3
"""Duskline Deadpan Forecast — make.fun bounty u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.

Writes one deadpan weather line (at most 160 characters) for an invented
city to $MAKEFUN_OUTPUT_DIR/entry.txt. Python 3.13 standard library only,
deterministic, no network, no randomness.

Hard rule, learned from a rejected entry: the program only ever writes
into $MAKEFUN_OUTPUT_DIR. If that directory is the repository directory
(or inside it), or cannot be written, the program writes nothing and
exits 0. It never raises.
"""

import os
import tempfile

# The entry: a straight-faced broadcast line. The city name is the first
# joke (a harbour town named after the inability to feel pleasure); the
# forecast then treats apologies and regret as ordinary weather, with
# real numbers (18 degrees, 40 km/h) so the invented place feels mapped.
ENTRY = (
    "In Port Anhedonia, expect 18\u00b0 and a steady drizzle of apologies "
    "from the sky, with gusts of regret reaching 40 km/h by evening."
)

MAX_CHARS = 160

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _valid(text):
    """Gate mirror: UTF-8, 1..MAX_CHARS characters, not only whitespace."""
    if not text or not text.strip():
        return False
    if not 1 <= len(text) <= MAX_CHARS:
        return False
    try:
        text.encode("utf-8")
    except UnicodeEncodeError:
        return False
    return True


def _is_in_repo(path):
    """True when path is the repo dir or inside it (resolved, symlinks out)."""
    try:
        resolved = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(REPO_DIR)
    return resolved == repo or resolved.startswith(repo + os.sep)


def main():
    try:
        if not _valid(ENTRY):
            return 0

        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-deadpan-forecast-")
        if _is_in_repo(out_dir):
            return 0

        try:
            os.makedirs(out_dir, exist_ok=True)
        except Exception:
            return 0
        target = os.path.join(out_dir, "entry.txt")
        if _is_in_repo(target):
            return 0

        try:
            with open(target, "w", encoding="utf-8", newline="") as f:
                f.write(ENTRY)
        except Exception:
            return 0

        # Read back and confirm the bytes are exactly the entry; if the
        # round-trip differs, remove the file rather than leave bad output.
        try:
            with open(target, "r", encoding="utf-8") as f:
                back = f.read()
        except Exception:
            return 0
        if back != ENTRY:
            try:
                os.remove(target)
            except Exception:
                pass
            return 0
    except Exception:
        return 0
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
