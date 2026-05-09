#!/usr/bin/env python3
"""Q054-F-01 — Q 54 dual-refrain 5-section architecture test.

Pre-reg: surahs/Q054-al-qamar/preregs/Q054-F-01-dual-refrain-architecture-prereg.md
SHA256:  fd1e8281a0955f7c3b1e84082bcd521e22aa58841b1939bfd40bbf9735c33413
Seed:    20260509  | n_perm: 10000  | Bonferroni-3 α_bon = 0.0167
"""
from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/preregs/Q054-F-01-dual-refrain-architecture-prereg.md"
EXPECTED_SHA = "fd1e8281a0955f7c3b1e84082bcd521e22aa58841b1939bfd40bbf9735c33413"
QURAN_PATH = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/csv/Q054-F-01.json"

SEED = 20260509
N_PERM = 10000


def verify_prereg() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  observed: {sha}")
    return sha


def main() -> None:
    sha = verify_prereg()
    print(f"[Q054-F-01] pre-reg SHA verified: {sha[:16]}…")

    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    # Q 54 verses
    q54 = corpus[53]
    verses_q54 = q54["verses"]
    n_q54 = len(verses_q54)

    # H1a: corpus-share of `فهل من مدكر` terminal-string
    refrain_a = "فهل من مدكر"
    n_total = 0
    n_q54_a = 0
    locations = []
    for s in corpus:
        for v in s["verses"]:
            text = v["text"].rstrip()
            if text.endswith(refrain_a):
                n_total += 1
                if s["id"] == 54:
                    n_q54_a += 1
                locations.append((s["id"], v["id"]))
    share_q54 = n_q54_a / n_total if n_total > 0 else 0.0
    print(f"  H1a: {n_q54_a}/{n_total} corpus instances of '{refrain_a}' in Q 54 → share = {share_q54:.4f}")
    print(f"  Locations: {locations}")

    # Permutation nulls for H1a
    rng = random.Random(SEED)
    surah_lengths = [len(s["verses"]) for s in corpus]
    total_verses = sum(surah_lengths)
    weights_lw = [n / total_verses for n in surah_lengths]
    weights_uniform = [1.0 / 114] * 114
    perm_p_a_lw = 0
    perm_p_a_uniform = 0
    for _ in range(N_PERM):
        # length-weighted draw
        draws = rng.choices(range(114), weights=weights_lw, k=n_total)
        if sum(1 for d in draws if d == 53) >= n_q54_a:
            perm_p_a_lw += 1
        # uniform draw
        draws_u = rng.choices(range(114), weights=weights_uniform, k=n_total)
        if sum(1 for d in draws_u if d == 53) >= n_q54_a:
            perm_p_a_uniform += 1
    perm_p_a_lw /= N_PERM
    perm_p_a_uniform /= N_PERM
    h1a_pass = (share_q54 >= 0.95) and (perm_p_a_lw <= 0.0167)
    print(f"  H1a: perm_p_lw = {perm_p_a_lw:.5f}; perm_p_uniform = {perm_p_a_uniform:.5f}")
    print(f"  H1a pass (share≥0.95 AND p≤0.0167): {h1a_pass}")

    # H1b: 5 pre-committed pericopes — closure by either yassarnā OR ʿadhābī wa-nudhur
    pericopes = [
        ("Nūḥ", 9, 17),
        ("ʿĀd", 18, 22),
        ("Thamūd", 23, 32),
        ("Lūṭ", 33, 40),
        ("āl-Firʿawn", 41, 42),
    ]
    yassarna_text = "ولقد يسرنا القرآن للذكر فهل من مدكر"
    kayfa_text = "فكيف كان عذابي ونذر"
    fadhuqu_text = "فذوقوا عذابي ونذر"
    closures = {}
    for name, lo, hi in pericopes:
        closed = False
        # check final verse of pericope OR within ±1 verse range
        for vi in range(max(1, lo - 1), min(n_q54, hi + 1) + 1):
            v_text = verses_q54[vi - 1]["text"]
            if (v_text == yassarna_text) or (v_text.endswith(kayfa_text)) or (v_text.endswith(fadhuqu_text)):
                closed = True
                break
        closures[name] = closed
    n_closed = sum(closures.values())
    h1b_pass = n_closed >= 4
    print(f"  H1b: pericope closures = {closures} → {n_closed}/5; pass (≥4): {h1b_pass}")

    # H1c: compression ratio Q26 / Q54 mean verses-per-pericope
    q26 = corpus[25]
    verses_q26 = q26["verses"]
    q26_pericopes = [
        ("Mūsā", 10, 68),
        ("Ibrāhīm", 69, 104),
        ("Nūḥ", 105, 122),
        ("Hūd", 123, 140),
        ("Ṣāliḥ", 141, 159),
        ("Lūṭ", 160, 175),
        ("Shuʿayb", 176, 191),
    ]
    mean_v_q54 = sum(hi - lo + 1 for _, lo, hi in pericopes) / len(pericopes)
    mean_v_q26 = sum(hi - lo + 1 for _, lo, hi in q26_pericopes) / len(q26_pericopes)
    ratio_v = mean_v_q26 / mean_v_q54
    h1c_pass = ratio_v >= 2.0
    print(f"  H1c: Q26 mean verses/pericope = {mean_v_q26:.2f}; Q54 = {mean_v_q54:.2f}; ratio = {ratio_v:.3f}; pass (≥2): {h1c_pass}")

    # Aggregate
    n_passed = sum([h1a_pass, h1b_pass, h1c_pass])
    if n_passed == 3:
        verdict = "CONFIRMED"
    elif n_passed == 2:
        verdict = "PARTIAL"
    elif n_passed == 1:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    if share_q54 < 0.50 or ratio_v < 1.0:
        verdict = "PRE-COMMIT VIOLATION"
    print(f"  Aggregate: {n_passed}/3 passed → {verdict}")

    output = {
        "test_id": "Q054-F-01",
        "title": "Q 54 dual-refrain 5-section architecture",
        "prereg_sha256": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": 3,
        "alpha_bon": 0.0167,
        "H1a": {
            "n_q54": n_q54_a,
            "n_total_corpus": n_total,
            "share_q54": share_q54,
            "locations": locations,
            "perm_p_length_weighted": perm_p_a_lw,
            "perm_p_uniform": perm_p_a_uniform,
            "pass": h1a_pass,
        },
        "H1b": {
            "pericope_closures": closures,
            "n_closed": n_closed,
            "threshold": 4,
            "pass": h1b_pass,
        },
        "H1c": {
            "q54_mean_verses_per_pericope": mean_v_q54,
            "q26_mean_verses_per_pericope": mean_v_q26,
            "compression_ratio": ratio_v,
            "threshold": 2.0,
            "pass": h1c_pass,
        },
        "aggregate": {
            "n_passed": n_passed,
            "verdict": verdict,
        },
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
