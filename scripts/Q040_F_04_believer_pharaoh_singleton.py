#!/usr/bin/env python3
"""Q040-F-04 — Believer-of-Pharaoh's-family pericope corpus-singleton."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q040-ghafir/preregs/Q040-F-04-believer-pharaoh-singleton-prereg.md"
EXPECTED_SHA = "cab6798de756be312cb96be7c19fb4049bdd737a1d285cc3b081486cc3331fe6"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "surahs/Q040-ghafir/csv/Q040-F-04.json"

NEEDLE_BELIEVER = "مؤمن"
NEEDLE_PHARAOH_FAMILY = "آل فرعون"


def main():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual}")

    text = json.loads(QURAN.read_text())
    hits = []
    for e in text:
        s = int(e["id"])
        for v in e["verses"]:
            vid = int(v["id"])
            t = v["text"]
            if NEEDLE_BELIEVER in t and NEEDLE_PHARAOH_FAMILY in t:
                hits.append({"surah": s, "verse": vid, "text": t})

    n = len(hits)
    if n == 1 and hits[0]["surah"] == 40 and hits[0]["verse"] == 28:
        verdict = "CORPUS-SINGLETON VINDICATED"
    elif n >= 2:
        verdict = "NULL — pattern not unique"
    else:
        verdict = "DEFINITIONAL ANOMALY (zero hits)"

    out = {
        "id": "Q040-F-04",
        "title": "Believer-of-Pharaoh's-family pericope (Q 40:28-44) corpus-singleton",
        "prereg_sha": EXPECTED_SHA,
        "needle_a": NEEDLE_BELIEVER,
        "needle_b": NEEDLE_PHARAOH_FAMILY,
        "n_hits": n,
        "hits": hits,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Q040-F-04: {verdict}")
    print(f"  hits: {[(h['surah'], h['verse']) for h in hits]}")


if __name__ == "__main__":
    main()
