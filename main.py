#!/usr/bin/env python3
"""Duskline Deadpan Forecast — make.fun bounty u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c.

Writes a single deadpan weather line (<=160 chars) for an invented city to
$MAKEFUN_OUTPUT_DIR/entry.txt. Deterministic, stdlib only, no network.
Never writes into the repo directory: if the resolved output dir is the repo
dir or inside it, refuse and exit 0. Never raises: any failure exits 0
without writing anything.
"""

import os
import tempfile

ENTRY = (
    "In Port Anhedonia, expect 18\u00b0 and a steady drizzle of apologies "
    "from the sky, with gusts of regret reaching 40 km/h by evening."
)

REPO_DIR = os.path.dirname(os.path.abspath(__file__))


def _is_in_repo(path):
    try:
        resolved = os.path.realpath(path)
    except Exception:
        return True
    repo = os.path.realpath(REPO_DIR)
    return resolved == repo or resolved.startswith(repo + os.sep)


def main():
    try:
        if not (1 <= len(ENTRY) <= 160):
            return 0
        if not ENTRY.strip():
            return 0
        ENTRY.encode("utf-8")

        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or ""
        if not out_dir:
            out_dir = tempfile.mkdtemp(prefix="duskline-deadpan-forecast-")
        if _is_in_repo(out_dir):
            return 0

        os.makedirs(out_dir, exist_ok=True)
        target = os.path.join(out_dir, "entry.txt")
        if _is_in_repo(target):
            return 0
        with open(target, "w", encoding="utf-8", newline="") as f:
            f.write(ENTRY)
        with open(target, "r", encoding="utf-8") as f:
            back = f.read()
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
