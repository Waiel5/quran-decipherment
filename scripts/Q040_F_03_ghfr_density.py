#!/usr/bin/env python3
"""Q040-F-03 — Q 40 *ghfr*-root density corpus rank."""

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q040-ghafir/preregs/Q040-F-03-ghfr-density-rank-prereg.md"
EXPECTED_SHA = "3854e00736e0ff4534212d21d7149048afc61daef100f828ed9322db1d8c721d"
ROOT_INDEX = ROOT / "data/morphology/root-index.json"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "surahs/Q040-ghafir/csv/Q040-F-03.json"
TARGET_ROOT = "gfr"
TARGET_SURAH = 40


def main():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual}")

    ri = json.loads(ROOT_INDEX.read_text())
    text = json.loads(QURAN.read_text())

    tokens = {}
    for e in text:
        s = int(e["id"])
        n = 0
        for v in e["verses"]:
            n += len(v["text"].split())
        tokens[s] = n

    counts = [0] * 115
    for s, v, w in ri[TARGET_ROOT]:
        counts[s] += 1

    rows = []
    for s in range(1, 115):
        if tokens[s] > 0:
            density = counts[s] / tokens[s] * 1000
            rows.append((density, -s, counts[s], s))  # tie-break: lower surah # first
    # rank descending by density; ties broken by raw count desc, then lower surah # first
    rows.sort(key=lambda x: (-x[0], -x[2], x[3]))

    rank_of_40 = None
    for i, (d, _, c, s) in enumerate(rows, 1):
        if s == TARGET_SURAH:
            rank_of_40 = i
            q40_density = d
            q40_count = c
            break

    top_10 = [{"rank": i, "surah": rows[i - 1][3], "density": rows[i - 1][0],
               "count": rows[i - 1][2], "tokens": tokens[rows[i - 1][3]]}
              for i in range(1, 11)]

    if rank_of_40 <= 5:
        verdict = "DIRECTIONAL VINDICATION (rank ≤ 5)"
    elif rank_of_40 <= 20:
        verdict = "PARTIAL (naming-density-weak)"
    else:
        verdict = "NULL — naming-density does not drive ranking"

    out = {
        "id": "Q040-F-03",
        "title": "Q 40 *ghfr*-root density corpus rank",
        "prereg_sha": EXPECTED_SHA,
        "target_root": TARGET_ROOT,
        "q40_count": q40_count,
        "q40_tokens": tokens[TARGET_SURAH],
        "q40_density": q40_density,
        "q40_rank": rank_of_40,
        "n_surahs": len(rows),
        "top_10": top_10,
        "verdict": verdict,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Q040-F-03: {verdict}")
    print(f"  Q40 density = {q40_density:.3f}/1000, count={q40_count}, rank={rank_of_40}/{len(rows)}")
    print(f"  Top 5: {[(r['surah'], round(r['density'],2)) for r in top_10[:5]]}")


if __name__ == "__main__":
    main()
