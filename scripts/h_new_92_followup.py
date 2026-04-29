#!/usr/bin/env python3
"""H-NEW-92 follow-up: length-conditional analysis + raw light-root count rank.

The main run found Q 24:35 NOTABLE (5/8 PASS-DIRECTED, 0 STRONG-PASS) on the
length-naive density axes. This follow-up isolates two more honest tests:

(A) Raw light-root token count (not density): how many light-root word slots
    does Q 24:35 have, and how does that rank in absolute terms?

(B) Length-conditional light density: among verses with >= 30 words, where
    does Q 24:35's light-density rank?

Reads: same data sources as h_new_92_light_verse.py
Writes: appends to h-new-92.json under 'followup' key.
"""

from __future__ import annotations

import json
import os
import sys
from collections import Counter, defaultdict
from typing import Dict, List, Tuple

ROOT = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(ROOT, "analysis"))
from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words  # noqa: E402

LIGHT_ROOTS = {"nwr", "DwA", "srj", "qbs", "Swr", "wqd", "nfx", "shhb",
               "rmd", "SbH", "Dwq"}
TARGET = (24, 35)
MORPH_PATH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-92.json")


def parse_features(s):
    out = {}
    for p in s.split("|"):
        if ":" in p:
            k, _, v = p.partition(":")
            out[k] = v
        else:
            out[p] = ""
    return out


def load_morph():
    by = defaultdict(list)
    with open(MORPH_PATH) as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            inner = parts[0].strip("()")
            try:
                s, v, w, seg = inner.split(":")
                s, v, w = int(s), int(v), int(w)
            except ValueError:
                continue
            f = parse_features(parts[3])
            by[(s, v)].append({"w": w, "lem": f.get("LEM", ""),
                                "root": f.get("ROOT", "")})
    return by


def light_word_set(segs):
    s = set()
    for x in segs:
        if x["root"] in LIGHT_ROOTS:
            s.add(x["w"])
    return s


def main():
    print("H-NEW-92 follow-up: length-conditional + raw count")
    morph = load_morph()
    surahs = load_quran("no-tashkeel")
    word_counts = {}
    light_counts = {}
    for s in surahs:
        for v in s.verses:
            wc = len(real_words(v.text))
            word_counts[(s.id, v.id)] = wc
            segs = morph.get((s.id, v.id), [])
            light_counts[(s.id, v.id)] = len(light_word_set(segs))

    # (A) Raw light-token count rank
    print("\n(A) Raw light-root token count per verse — top 15:")
    by_count = sorted(light_counts.items(), key=lambda kv: kv[1], reverse=True)
    for (sv), c in by_count[:15]:
        wc = word_counts[sv]
        marker = " <-- Q 24:35" if sv == TARGET else ""
        print(f"  Q {sv[0]}:{sv[1]:>3}  count={c:>2}  words={wc:>3}{marker}")
    target_count = light_counts[TARGET]
    target_rank_count = next(i for i, (k, _) in enumerate(by_count, 1) if k == TARGET)
    print(f"  Q 24:35: count={target_count}, rank {target_rank_count}/6236")

    # (B) Length-conditional density: verses with >= 30 words
    print("\n(B) Length-conditional density (verses with >= 30 words):")
    long_verses = [k for k, w in word_counts.items() if w >= 30]
    print(f"    {len(long_verses)} verses with >=30 words")
    densities = sorted(
        ((k, light_counts[k] / word_counts[k]) for k in long_verses),
        key=lambda x: x[1], reverse=True,
    )
    for (sv), d in densities[:15]:
        wc = word_counts[sv]
        c = light_counts[sv]
        marker = " <-- Q 24:35" if sv == TARGET else ""
        print(f"  Q {sv[0]}:{sv[1]:>3}  density={d:.4f}  count={c:>2} / words={wc:>3}{marker}")
    target_rank_long = next(i for i, (k, _) in enumerate(densities, 1) if k == TARGET)
    print(f"  Q 24:35 length-conditional rank: {target_rank_long}/{len(long_verses)}")

    # (C) >=20 words
    print("\n(C) Length-conditional density (verses with >= 20 words):")
    long20 = [k for k, w in word_counts.items() if w >= 20]
    d20 = sorted(((k, light_counts[k] / word_counts[k]) for k in long20),
                 key=lambda x: x[1], reverse=True)
    for (sv), d in d20[:10]:
        wc = word_counts[sv]; c = light_counts[sv]
        marker = " <-- Q 24:35" if sv == TARGET else ""
        print(f"  Q {sv[0]}:{sv[1]:>3}  density={d:.4f}  count={c:>2} / words={wc:>3}{marker}")
    target_rank_20 = next(i for i, (k, _) in enumerate(d20, 1) if k == TARGET)
    print(f"  Q 24:35 length-conditional (>=20 words) rank: {target_rank_20}/{len(long20)}")

    # Patch h-new-92.json
    with open(OUT_JSON) as fh:
        d = json.load(fh)
    d["followup"] = {
        "raw_light_count_rank": target_rank_count,
        "raw_light_count": target_count,
        "raw_light_count_top_5": [
            {"verse": f"{sv[0]}:{sv[1]}", "count": c,
             "words": word_counts[sv]} for sv, c in by_count[:5]
        ],
        "length_conditional_30plus_rank": target_rank_long,
        "length_conditional_30plus_N": len(long_verses),
        "length_conditional_30plus_top_5": [
            {"verse": f"{sv[0]}:{sv[1]}",
             "density": dn, "count": light_counts[sv],
             "words": word_counts[sv]} for sv, dn in densities[:5]
        ],
        "length_conditional_20plus_rank": target_rank_20,
        "length_conditional_20plus_N": len(long20),
    }
    with open(OUT_JSON, "w") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False)
    print(f"\n  patched {OUT_JSON} with followup keys")


if __name__ == "__main__":
    main()
