"""
Q001-F-01 — Chiastic-symmetry score for Q 1 al-Fātiḥa.

Pre-reg: surahs/Q001-al-fatiha/Q001-F-01-chiastic-symmetry-prereg.md
Pre-reg SHA256 (locked): 84c6157b63be6718ddc999a08f698ab843c0b2369b704a1fb6d09b82473608da

Run: python3 Q001_F_01_chiastic_symmetry.py
Output: surahs/Q001-al-fatiha/csv/Q001-F-01.json
"""

import json
import hashlib
import itertools
import os
import random

PROJECT = "/Users/grey/Downloads/quran"
PREREG_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/Q001-F-01-chiastic-symmetry-prereg.md"
PREREG_SHA_EXPECTED = "84c6157b63be6718ddc999a08f698ab843c0b2369b704a1fb6d09b82473608da"
OUT_PATH = f"{PROJECT}/surahs/Q001-al-fatiha/csv/Q001-F-01.json"


def sha256_file(p):
    with open(p, "rb") as f:
        return hashlib.sha256(f.read()).hexdigest()


def jaccard(a, b):
    A, B = set(a), set(b)
    if not A and not B:
        return 1.0
    if not A or not B:
        return 0.0
    return len(A & B) / len(A | B)


def all_pairings(items):
    """Yield all set-partitions of items into pairs (items has even length)."""
    items = list(items)
    if len(items) == 0:
        yield ()
        return
    first = items[0]
    for i in range(1, len(items)):
        pair = (first, items[i])
        rest = items[1:i] + items[i+1:]
        for sub in all_pairings(rest):
            yield (pair,) + sub


def main():
    sha = sha256_file(PREREG_PATH)
    assert sha == PREREG_SHA_EXPECTED, f"PRE-REG SHA MISMATCH: {sha} != {PREREG_SHA_EXPECTED}"

    data = json.load(open(f"{PROJECT}/quran-text/quran-no-tashkeel.json"))
    q1 = data[0]
    verses = {v["id"]: v["text"].split() for v in q1["verses"]}
    chars = {v["id"]: set(v["text"].replace(" ", "")) for v in q1["verses"]}

    # Mirror pairing (V1↔V7, V2↔V6, V3↔V5); V4 is pivot.
    mirror_pairs = [(1, 7), (2, 6), (3, 5)]
    M_obs_word = sum(jaccard(verses[a], verses[b]) for a, b in mirror_pairs) / 3
    M_obs_letter = sum(jaccard(chars[a], chars[b]) for a, b in mirror_pairs) / 3

    # All 15 pairings of {1,2,3,5,6,7} into 3 pairs
    items = [1, 2, 3, 5, 6, 7]
    all_p = list(all_pairings(items))
    assert len(all_p) == 15, f"expected 15, got {len(all_p)}"

    word_scores = []
    letter_scores = []
    pairing_records = []
    for pairing in all_p:
        ws = sum(jaccard(verses[a], verses[b]) for a, b in pairing) / 3
        ls = sum(jaccard(chars[a], chars[b]) for a, b in pairing) / 3
        word_scores.append(ws)
        letter_scores.append(ls)
        is_mirror = sorted([tuple(sorted(p)) for p in pairing]) == sorted([tuple(sorted(p)) for p in mirror_pairs])
        pairing_records.append({"pairing": [list(p) for p in pairing], "word_jaccard_mean": ws, "letter_jaccard_mean": ls, "is_mirror": is_mirror})

    # Rank from top (1 = highest)
    word_rank = sorted(word_scores, reverse=True).index(M_obs_word) + 1
    letter_rank = sorted(letter_scores, reverse=True).index(M_obs_letter) + 1

    # NB: ties — use rank-of-equal-or-higher
    word_rank_strict = sum(1 for s in word_scores if s > M_obs_word) + 1  # 1 = strictly highest
    letter_rank_strict = sum(1 for s in letter_scores if s > M_obs_letter) + 1

    # p-value: # >= obs / 15
    word_p = sum(1 for s in word_scores if s >= M_obs_word) / 15
    letter_p = sum(1 for s in letter_scores if s >= M_obs_letter) / 15

    result = {
        "test_id": "Q001-F-01",
        "title": "Chiastic-symmetry score for Q 1 al-Fātiḥa",
        "prereg_sha_expected": PREREG_SHA_EXPECTED,
        "prereg_sha_runtime": sha,
        "rules_tuple": {"tashkeel": "no-tashkeel", "token": "orthographic-word", "basmala": "counted-V1", "reading": "Hafs-Kufan"},
        "verse_words": {str(k): v for k, v in verses.items()},
        "mirror_pairs": [list(p) for p in mirror_pairs],
        "M_obs_word_jaccard": M_obs_word,
        "M_obs_letter_jaccard": M_obs_letter,
        "n_pairings": 15,
        "word_rank_top1is_highest": word_rank_strict,
        "letter_rank_top1is_highest": letter_rank_strict,
        "word_p_one_tailed": word_p,
        "letter_p_one_tailed": letter_p,
        "all_pairings_records": pairing_records,
        "verdict_word": "VINDICATED" if word_rank_strict == 1 else ("DIRECTIONAL" if word_rank_strict <= 2 else "NULL"),
        "verdict_letter": "VINDICATED" if letter_rank_strict == 1 else ("DIRECTIONAL" if letter_rank_strict <= 2 else "NULL"),
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w") as f:
        json.dump(result, f, indent=2, ensure_ascii=False)

    print(f"M_obs_word_jaccard = {M_obs_word:.4f}")
    print(f"M_obs_letter_jaccard = {M_obs_letter:.4f}")
    print(f"word rank: {word_rank_strict}/15 (p={word_p:.3f})")
    print(f"letter rank: {letter_rank_strict}/15 (p={letter_p:.3f})")
    print(f"Verdict (word): {result['verdict_word']}")
    print(f"Verdict (letter): {result['verdict_letter']}")
    print(f"Output: {OUT_PATH}")


if __name__ == "__main__":
    main()
