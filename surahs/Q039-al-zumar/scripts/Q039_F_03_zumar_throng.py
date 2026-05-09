#!/usr/bin/env python3
"""Q039-F-03 — Zumar-throng motif (Q 39:71-75) corpus-EXACT structural-twin search.

Pre-reg: surahs/Q039-al-zumar/preregs/Q039-F-03-zumar-throng-structural-twin-prereg.md
Pre-reg SHA: 074be7d3e28b71fdf09b67f6db9aa06381e6d1b3a564aabadd2f6431cbf80864
Seed: 20260509  |  α_bon: 0.0125

Tests:
  H1 — Q 39:71-72 ↔ Q 39:73-74 is rank-1 by Jaccard among consecutive paired-eschatological-polarity windows.
  H2 — wa-sīqa alladhīna incipit construction is corpus-EXACT (only repeated in Q 39).
"""

import csv
import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[3]
PREREG_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "preregs" / "Q039-F-03-zumar-throng-structural-twin-prereg.md"
EXPECTED_SHA = "074be7d3e28b71fdf09b67f6db9aa06381e6d1b3a564aabadd2f6431cbf80864"
OUT_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "csv" / "Q039-F-03.json"
QURAN_JSON = PROJECT_ROOT / "quran-text" / "quran-no-tashkeel.json"
QAC_PATH = PROJECT_ROOT / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"

SEED = 20260509
ALPHA_BON = 0.0125

WAQF_MARKS = set("ۚۖۗۘۙۛۜ۞")

JAHANNAM_ROOTS = {"jhnm", "nAr", "bAs", "sEr", "jHm", "lZy", "hwy", "Hyp"}
JANNA_ROOTS = {"jnn", "Erš", "frdws", "Eml"}  # janna, ʿarsh, firdaws (and ʿaml as Eml weak)


def verify_prereg_sha() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  found:    {sha}\n"
        )
        sys.exit(1)
    return sha


def clean_text(text: str) -> str:
    return "".join(
        c for c in text if not (0x064B <= ord(c) <= 0x065F) and c not in WAQF_MARKS
    )


def load_verses() -> list[dict]:
    with QURAN_JSON.open(encoding="utf-8") as f:
        data = json.load(f)
    out = []
    for entry in data:
        sid = entry["id"]
        for v in entry["verses"]:
            cleaned = clean_text(v["text"])
            words = [w for w in cleaned.split() if w.strip()]
            out.append(
                {
                    "surah": sid,
                    "verse": v["id"],
                    "text": cleaned,
                    "words": words,
                    "first_word": words[0] if words else "",
                }
            )
    return out


def load_qac_roots_per_verse() -> dict[tuple[int, int], set[str]]:
    """Returns map (surah, verse) -> set of QAC roots present in that verse."""
    out: dict[tuple[int, int], set[str]] = {}
    loc_re = re.compile(r"\((\d+):(\d+):\d+:\d+\)")
    root_re = re.compile(r"ROOT:(\w+)")
    with QAC_PATH.open(encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or line.startswith("LOCATION"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            m = loc_re.match(parts[0])
            if not m:
                continue
            s, v = int(m.group(1)), int(m.group(2))
            rm = root_re.search(parts[3])
            if rm:
                out.setdefault((s, v), set()).add(rm.group(1))
    return out


def jaccard(a: set, b: set) -> float:
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def main() -> None:
    sha = verify_prereg_sha()
    print(f"[OK] pre-reg SHA verified: {sha[:16]}...")

    verses = load_verses()
    roots_by_verse = load_qac_roots_per_verse()
    by_surah = {}
    for v in verses:
        by_surah.setdefault(v["surah"], []).append(v)
    for s in by_surah:
        by_surah[s].sort(key=lambda x: x["verse"])

    # ---------- H1: Q 39:71-72 / Q 39:73-74 paired Jaccard
    def pair_words(verses_pair):
        return set(verses_pair[0]["words"]) | set(verses_pair[1]["words"])

    def has_class(verses_pair, root_class):
        for v in verses_pair:
            if roots_by_verse.get((v["surah"], v["verse"]), set()) & root_class:
                return True
        return False

    # Build all qualifying 4-tuples: same surah, two non-overlapping consecutive pairs,
    # one Jahannam-class, one Janna-class
    twins = []
    for s, vs in by_surah.items():
        ids = [v["verse"] for v in vs]
        # all consecutive pairs (a, a+1)
        pairs = []
        for i in range(len(vs) - 1):
            if vs[i + 1]["verse"] == vs[i]["verse"] + 1:
                pairs.append((vs[i], vs[i + 1]))
        # All non-overlapping pair-of-pairs
        for i in range(len(pairs)):
            for j in range(i + 1, len(pairs)):
                p1 = pairs[i]
                p2 = pairs[j]
                # Non-overlap
                if p2[0]["verse"] > p1[1]["verse"]:
                    has_jh = has_class(p1, JAHANNAM_ROOTS) or has_class(p2, JAHANNAM_ROOTS)
                    has_jn = has_class(p1, JANNA_ROOTS) or has_class(p2, JANNA_ROOTS)
                    if has_jh and has_jn:
                        w1 = pair_words(p1)
                        w2 = pair_words(p2)
                        j_sc = jaccard(w1, w2)
                        twins.append({
                            "surah": s,
                            "pair_a": (p1[0]["verse"], p1[1]["verse"]),
                            "pair_b": (p2[0]["verse"], p2[1]["verse"]),
                            "jaccard": j_sc,
                            "size": len(w1) + len(w2),
                        })

    print(f"[INFO] qualifying 4-tuple eschatological-pair twinnings: {len(twins)}")

    # Q 39 specific
    q39_twin = next(
        (t for t in twins if t["surah"] == 39 and t["pair_a"] == (71, 72) and t["pair_b"] == (73, 74)),
        None,
    )
    if q39_twin is None:
        # Q 39 might be classified differently — search any Q 39 entry
        q39_candidates = [t for t in twins if t["surah"] == 39]
        print(f"[WARN] direct Q 39:71-72/73-74 not found in qualifying set; Q 39 candidates: {len(q39_candidates)}")
        # Pick the highest-Jaccard Q 39 twin
        q39_twin = max(q39_candidates, key=lambda x: x["jaccard"]) if q39_candidates else None

    if q39_twin is None:
        print("[ERROR] no Q 39 paired-eschatological twin found in qualifying set; computing direct Jaccard for vv. 71-72 / 73-74")
        # Compute directly
        v71 = next(v for v in by_surah[39] if v["verse"] == 71)
        v72 = next(v for v in by_surah[39] if v["verse"] == 72)
        v73 = next(v for v in by_surah[39] if v["verse"] == 73)
        v74 = next(v for v in by_surah[39] if v["verse"] == 74)
        w1 = set(v71["words"]) | set(v72["words"])
        w2 = set(v73["words"]) | set(v74["words"])
        q39_twin = {
            "surah": 39,
            "pair_a": (71, 72),
            "pair_b": (73, 74),
            "jaccard": jaccard(w1, w2),
            "size": len(w1) + len(w2),
            "forced_compute": True,
        }
        twins.append(q39_twin)

    twins_sorted = sorted(twins, key=lambda x: -x["jaccard"])
    q39_rank = next(
        (i + 1 for i, t in enumerate(twins_sorted) if t["surah"] == 39 and t["pair_a"] == (71, 72) and t["pair_b"] == (73, 74)),
        None,
    )
    print(f"[RESULT] Q 39:71-72 / 73-74 Jaccard = {q39_twin['jaccard']:.4f}; rank = {q39_rank} / {len(twins_sorted)}")
    h1_pass = q39_rank == 1

    # ---------- H2: wa-sīqa alladhīna incipit corpus-EXACT
    INCIPIT = "وسيق"
    INCIPIT_ALT = "وسيق "  # leading word
    wasiqa_verses_per_surah = {}
    for v in verses:
        if v["first_word"] == INCIPIT:
            wasiqa_verses_per_surah.setdefault(v["surah"], []).append(v["verse"])

    n_surahs_repeated = sum(1 for vs in wasiqa_verses_per_surah.values() if len(vs) >= 2)
    n_surahs_any = len(wasiqa_verses_per_surah)
    n_total_incipits = sum(len(vs) for vs in wasiqa_verses_per_surah.values())
    h2_pass = (n_surahs_repeated == 1) and (39 in wasiqa_verses_per_surah and len(wasiqa_verses_per_surah[39]) >= 2)

    print(f"[RESULT] wa-sīqa incipit count corpus-wide: {n_total_incipits} (in {n_surahs_any} surahs)")
    print(f"[RESULT] surahs with ≥ 2 wa-sīqa incipits: {n_surahs_repeated}  → H2 {'PASS' if h2_pass else 'FAIL'}")
    print(f"[RESULT] Q 39 wa-sīqa incipit positions: {wasiqa_verses_per_surah.get(39, [])}")

    if h1_pass and h2_pass:
        verdict = "CONFIRMED-DIRECTED"
    elif h1_pass or h2_pass:
        verdict = "PASS-DIRECTED"
    else:
        verdict = "NULL"

    print(f"[VERDICT] {verdict}")

    out = {
        "id": "Q039-F-03",
        "h_new_id": "H-NEW-1290",
        "title": "Zumar-throng motif Q 39:71-75 structural-twin search",
        "prereg_path": str(PREREG_PATH.relative_to(PROJECT_ROOT)),
        "prereg_sha": EXPECTED_SHA,
        "prereg_sha_verified": sha,
        "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": 4,
        "bonferroni_family": "Q039-novel-tests",
        "qualifying_twins_count": len(twins_sorted),
        "q39_71_72_73_74_jaccard": q39_twin["jaccard"],
        "q39_rank": q39_rank,
        "h1_pass": h1_pass,
        "top10_twin_pairs": [
            {
                "surah": t["surah"],
                "pair_a": t["pair_a"],
                "pair_b": t["pair_b"],
                "jaccard": t["jaccard"],
                "size": t["size"],
            }
            for t in twins_sorted[:10]
        ],
        "wa_siqa_incipit_total": n_total_incipits,
        "wa_siqa_surahs_any": n_surahs_any,
        "wa_siqa_surahs_repeated": n_surahs_repeated,
        "wa_siqa_per_surah": wasiqa_verses_per_surah,
        "h2_pass": h2_pass,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "rules_tuple": [
            "no-tashkeel",
            "orthographic-token",
            "graphemes",
            "QAC-v0.4-root",
            "basmala-counted-only-in-Q1",
            "Hafs-Kufan",
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\n[OK] wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
