#!/usr/bin/env python3
"""
Q013-F-07 — raʿd-substring corpus rank.

Pre-reg: /Users/grey/Downloads/quran/surahs/Q013-al-rad/Q013-F-07-raʿd-corpus-rank-prereg.md
SHA256:  02f15efbee43f3f288b346c2f3d05f5efb167f7b75fc5afdd10587ba26c57f8d

Method: enumerate رعد substring matches across 114 surahs, compute raw rank (Cell A)
and length-normalized density rank (Cell B), and permutation null (Cell C).

Direction LOCKED: Q 13 = rank-1 in both Cell A and Cell B.
"""

from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q013-al-rad/Q013-F-07-raʿd-corpus-rank-prereg.md"
EXPECTED_SHA = "02f15efbee43f3f288b346c2f3d05f5efb167f7b75fc5afdd10587ba26c57f8d"
OUT = ROOT / "surahs/Q013-al-rad/csv/Q013-F-07.json"
SEED = 20260509
N_PERM = 10000

TARGET_LEXEME = "رعد"


def sha_verify():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FATAL: SHA mismatch.\n  expected: {EXPECTED_SHA}\n  actual:   {actual}", file=sys.stderr)
        sys.exit(1)
    return actual


def main():
    sha_actual = sha_verify()
    with (ROOT / "quran-text/quran-no-tashkeel.json").open(encoding="utf-8") as f:
        q = json.load(f)

    # Per-surah raw counts + per-verse occurrences (for permutation null)
    surah_counts = []   # length 114
    surah_words = []    # length 114
    verse_records = []  # list of (surah_idx_0based, has_target_count)
    detail_attestations = []
    for s_idx, surah in enumerate(q):
        s = s_idx + 1
        cnt = 0
        words = 0
        for v in surah["verses"]:
            txt = v["text"]
            occ = txt.count(TARGET_LEXEME)
            cnt += occ
            words += len(txt.split())
            verse_records.append((s_idx, occ))
            if occ > 0:
                detail_attestations.append({
                    "surah": s, "verse": v.get("verse", v.get("id")),
                    "text": txt,
                    "raʿd_substring_count": occ,
                })
        surah_counts.append(cnt)
        surah_words.append(words)

    # Cell A — raw counts, rank Q13
    sorted_idx_desc = sorted(range(114), key=lambda i: -surah_counts[i])
    rank_q13_a = sorted_idx_desc.index(12) + 1  # 1-based
    q13_count = surah_counts[12]

    # Cell B — density (per 1000 words)
    densities = [surah_counts[i] / surah_words[i] * 1000 if surah_words[i] > 0 else 0.0 for i in range(114)]
    sorted_idx_desc_b = sorted(range(114), key=lambda i: -densities[i])
    rank_q13_b = sorted_idx_desc_b.index(12) + 1
    q13_density = densities[12]

    # Cell C — permutation null: shuffle verse-level raʿd-counts across all 6,236 verses
    rng = random.Random(SEED)
    occ_vector = [r[1] for r in verse_records]
    surah_of_verse = [r[0] for r in verse_records]
    n_total = len(occ_vector)

    rank1_count = 0
    for _ in range(N_PERM):
        permuted = occ_vector.copy()
        rng.shuffle(permuted)
        # tally per surah
        tally = [0] * 114
        for i, oc in enumerate(permuted):
            if oc:
                tally[surah_of_verse[i]] += oc
        # rank of Q13 (index 12)
        sorted_perm = sorted(range(114), key=lambda j: -tally[j])
        if sorted_perm.index(12) == 0:
            rank1_count += 1
    p_perm_rank1 = rank1_count / N_PERM

    # Top 5 surahs from each cell
    top5_a = [{"surah": i + 1, "count": surah_counts[i]} for i in sorted_idx_desc[:5]]
    top5_b = [{"surah": i + 1, "density_per_1k_words": round(densities[i], 4)} for i in sorted_idx_desc_b[:5]]

    pass_a = rank_q13_a == 1
    pass_b = rank_q13_b == 1
    pass_c = p_perm_rank1 <= 0.025

    if pass_a and pass_b and pass_c:
        verdict = "PASS-DIRECTED (all 3 cells passed)"
    elif pass_a and pass_b:
        verdict = "PASS-DIRECTED on direction; Cell C did not pass at α_bon"
    else:
        verdict = "NULL — DIRECTION REVERSED"

    out = {
        "test_id": "Q013-F-07",
        "title": "raʿd-substring corpus rank — Q 13 corpus-rank-1 prediction",
        "prereg_sha_expected": EXPECTED_SHA,
        "prereg_sha_actual": sha_actual,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": 0.025,
        "target_lexeme": TARGET_LEXEME,
        "cell_A_raw_count": {
            "q13_count": q13_count,
            "q13_rank": rank_q13_a,
            "top5": top5_a,
            "pass_direction_rank1": pass_a,
            "total_corpus_count": sum(surah_counts),
        },
        "cell_B_density_per_1k_words": {
            "q13_density": round(q13_density, 4),
            "q13_rank": rank_q13_b,
            "top5": top5_b,
            "pass_direction_rank1": pass_b,
        },
        "cell_C_permutation_null": {
            "n_perm": N_PERM,
            "p_q13_rank1": p_perm_rank1,
            "pass_alpha_bon": pass_c,
            "interpretation": ("If raʿd-positions were randomly shuffled across verses, the fraction of "
                               "permutations in which Q 13 still ranks #1 corpus-wide."),
        },
        "attestations": detail_attestations,
        "verdict": verdict,
        "note": ("The target lexeme is corpus-rare. Q 13:13 contains *al-raʿd* in the construction "
                 "*yusabbiḥu al-raʿdu bi-ḥamdihi* — verified corpus-unique syntactic role by Q013-F-02."),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"WROTE {OUT}")
    print(f"verdict: {verdict}")
    print(f"Q13 raw rank: {rank_q13_a}; count={q13_count}; density rank: {rank_q13_b}; density={q13_density:.4f}; p_perm(rank-1)={p_perm_rank1:.4f}")


if __name__ == "__main__":
    main()
