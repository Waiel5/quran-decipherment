#!/usr/bin/env python3
"""Q054-F-05 — Q 54 *wa-laqad* opener density test.

Pre-reg: surahs/Q054-al-qamar/preregs/Q054-F-05-walaqad-density-prereg.md
SHA256:  88278d98f579d7742df1315c079548f606ae396f32aa386c5d04caa91deadd12
Seed:    20260509  | n_perm: 10000  | Bonferroni-2 α_bon = 0.025
"""
from __future__ import annotations
import hashlib
import json
import random
import sys
from pathlib import Path

PROJECT_ROOT = Path("/Users/grey/Downloads/quran")
PREREG_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/preregs/Q054-F-05-walaqad-density-prereg.md"
EXPECTED_SHA = "88278d98f579d7742df1315c079548f606ae396f32aa386c5d04caa91deadd12"
QURAN_PATH = PROJECT_ROOT / "quran-text/quran-no-tashkeel.json"
OUTPUT_PATH = PROJECT_ROOT / "surahs/Q054-al-qamar/csv/Q054-F-05.json"

SEED = 20260509
N_PERM = 10000


def verify_prereg() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected: {EXPECTED_SHA}\n  observed: {sha}")
    return sha


def main() -> None:
    sha = verify_prereg()
    print(f"[Q054-F-05] pre-reg SHA verified: {sha[:16]}…")

    with open(QURAN_PATH) as f:
        corpus = json.load(f)

    # Per-surah wa-laqad opener counts
    walaqad_prefix = "ولقد "
    surah_walaqad = {}
    for s in corpus:
        s_id = s["id"]
        n_verses = len(s["verses"])
        walaqad_count = sum(1 for v in s["verses"] if v["text"].startswith(walaqad_prefix))
        density_per100 = (walaqad_count / n_verses * 100) if n_verses > 0 else 0.0
        surah_walaqad[s_id] = {
            "surah": s_id,
            "n_verses": n_verses,
            "walaqad_count": walaqad_count,
            "density_per100": density_per100,
        }

    # H5a: corpus rank by density_per100
    sorted_density = sorted(surah_walaqad.values(), key=lambda x: -x["density_per100"])
    rank_q54 = next(i + 1 for i, e in enumerate(sorted_density) if e["surah"] == 54)
    q54_entry = surah_walaqad[54]
    h5a_pass = rank_q54 <= 2
    print(f"  H5a: Q 54 wa-laqad count = {q54_entry['walaqad_count']}; density per 100 verses = {q54_entry['density_per100']:.2f}")
    print(f"  H5a: Q 54 corpus rank = {rank_q54}/114; pass (≤2): {h5a_pass}")
    print(f"  Top-10 by density:")
    for i, e in enumerate(sorted_density[:10]):
        print(f"    rank {i+1}: Q{e['surah']:3d}  count {e['walaqad_count']:2d}  /  {e['n_verses']:3d} verses  =  {e['density_per100']:6.2f}/100")

    # Permutation null for H5a (length-weighted)
    total_walaqad = sum(e["walaqad_count"] for e in surah_walaqad.values())
    total_verses = sum(e["n_verses"] for e in surah_walaqad.values())
    rng = random.Random(SEED)
    weights = [e["n_verses"] / total_verses for e in [surah_walaqad[s["id"]] for s in corpus]]
    n_q54_obs = q54_entry["walaqad_count"]
    perm_p_lw = 0
    for _ in range(N_PERM):
        draws = rng.choices(range(114), weights=weights, k=total_walaqad)
        if sum(1 for d in draws if d == 53) >= n_q54_obs:
            perm_p_lw += 1
    perm_p_lw /= N_PERM
    print(f"  H5a perm_p (length-weighted): {perm_p_lw:.5f}")

    # H5b: refrain-paired density - of Q 54's wa-laqad-opener verses, how many are within ±1 verse of a yassarna OR kayfa kana ʿadhābī wa-nudhur OR fa-dhūqū verse?
    q54 = corpus[53]
    verses_q54 = q54["verses"]
    refrain_yassarna = "ولقد يسرنا القرآن للذكر فهل من مدكر"
    refrain_kayfa = "فكيف كان عذابي ونذر"
    refrain_fadhuqu = "فذوقوا عذابي ونذر"
    refrain_muddakir_terminal = "فهل من مدكر"

    walaqad_verses = [v["id"] for v in verses_q54 if v["text"].startswith(walaqad_prefix)]
    refrain_verses = []
    for v in verses_q54:
        text = v["text"]
        if text == refrain_yassarna:
            refrain_verses.append((v["id"], "yassarna"))
        elif text.endswith(refrain_kayfa):
            refrain_verses.append((v["id"], "kayfa-kana"))
        elif text.endswith(refrain_fadhuqu):
            refrain_verses.append((v["id"], "fa-dhuqu"))
        elif text.endswith(refrain_muddakir_terminal):
            refrain_verses.append((v["id"], "muddakir-terminal"))

    paired = []
    for w_id in walaqad_verses:
        v_text = verses_q54[w_id - 1]["text"]
        # Direct: this verse ends with muddakir-terminal
        if v_text.endswith(refrain_muddakir_terminal):
            paired.append({"v": w_id, "type": "self-muddakir-terminal"})
            continue
        # Adjacent: ±1 verse contains a refrain
        adj_match = None
        for r_id, r_type in refrain_verses:
            if abs(r_id - w_id) <= 1:
                adj_match = (r_id, r_type)
                break
        if adj_match:
            paired.append({"v": w_id, "type": f"adj-{adj_match[1]}", "refrain_v": adj_match[0]})
        else:
            paired.append({"v": w_id, "type": "unpaired"})

    n_paired = sum(1 for p in paired if p["type"] != "unpaired")
    h5b_pass = n_paired >= 6
    print(f"  H5b: wa-laqad-opener verses in Q 54: {walaqad_verses}")
    print(f"  H5b: refrain verses in Q 54: {refrain_verses}")
    print(f"  H5b: pairing detail:")
    for p in paired:
        print(f"    v{p['v']:2d} → {p['type']}")
    print(f"  H5b: paired = {n_paired}/{len(walaqad_verses)}; pass (≥6): {h5b_pass}")

    # Aggregate
    n_passed = sum([h5a_pass, h5b_pass])
    if n_passed == 2:
        verdict = "CONFIRMED"
    elif n_passed == 1:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"
    print(f"  Aggregate: {n_passed}/2 → {verdict}")

    output = {
        "test_id": "Q054-F-05",
        "title": "Q 54 wa-laqad opener density",
        "prereg_sha256": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": 2,
        "alpha_bon": 0.025,
        "Q54_walaqad_count": q54_entry["walaqad_count"],
        "Q54_walaqad_density_per100": q54_entry["density_per100"],
        "Q54_corpus_rank": rank_q54,
        "corpus_total_walaqad_openers": total_walaqad,
        "top10_by_density": sorted_density[:10],
        "Q54_walaqad_verses": walaqad_verses,
        "Q54_refrain_verses": refrain_verses,
        "pairing_detail": paired,
        "H5a": {
            "rank": rank_q54,
            "density_per100": q54_entry["density_per100"],
            "perm_p_length_weighted": perm_p_lw,
            "pass": h5a_pass,
        },
        "H5b": {
            "n_paired": n_paired,
            "n_walaqad_total": len(walaqad_verses),
            "threshold": 6,
            "pass": h5b_pass,
        },
        "aggregate": {"n_passed": n_passed, "verdict": verdict},
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print(f"  Output: {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
