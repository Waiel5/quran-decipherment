#!/usr/bin/env python3
"""
Q083-F-01 — SIJJĪN (kitāb al-fujjār, Q 83:7-17) ↔ ʿILLIYYĪN (kitāb al-abrār, Q 83:18-28)
antithetical-pair structure: frame-root mirroring (H1, elevated, locked) vs destiny-content
disjunction (H3, disjoint=0, locked); overall Jaccard (H2, descriptive pivot, no locked direction).

Pre-reg SHA256 lock: acd67eb32847fa20631a37fedb608b04ef8f42152edcd618b51e4eaa7602ddc6
Seed: 20260509 | n_perm: 10000 | Bonferroni k=3, alpha_bon = 0.016667
Rules-tuple: (no-tashkeel, QAC-STEM root tokens, QAC v0.4, graphemes, basmala-counted-only-in-Q1,
              Hafs-Kūfan, Mashriqī)
"""
import json
import hashlib
import re
import sys
import random
from pathlib import Path

HERE = Path(__file__).resolve().parent
PREREG_PATH = HERE.parent / "preregs" / "Q083-F-01-sijjin-illiyyin-antithesis-prereg.md"
PREREG_SHA = "acd67eb32847fa20631a37fedb608b04ef8f42152edcd618b51e4eaa7602ddc6"
OUTPUT_PATH = HERE.parent / "csv" / "Q083-F-01.json"
SEED = 20260509
N_PERM = 10000
ALPHA_BON = 0.05 / 3  # 0.016667

QURAN_PATH = "/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json"
QAC_PATH = "/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt"

# Locked destiny-root sets (Buckwalter QAC roots), per pre-reg §1 H3
FUJJAR_DESTINY_ROOTS = {"sjn", "jHm", "Hjb"}          # sijjīn, jaḥīm, maḥjūbīn (QAC Buckwalter)
ABRAR_DESTINY_ROOTS = {"Elw", "nEm", "rHq", "msk", "snm", "Ark"}  # ʿilliyyīn, naʿīm, raḥīq, misk, tasnīm, arāʾik (QAC Buckwalter)


def verify_sha():
    h = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if h != PREREG_SHA:
        sys.exit(f"PREREG SHA MISMATCH: expected {PREREG_SHA}, got {h}")
    print(f"PREREG SHA verified: {h}")


def load_qac_roots():
    """dict {(surah, verse): list[root]} (Buckwalter)."""
    out = {}
    with open(QAC_PATH, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION"):
                continue
            line = line.rstrip("\n")
            if not line:
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            m = re.match(r"\((\d+):(\d+):(\d+):(\d+)\)", parts[0])
            if not m:
                continue
            s, v = int(m.group(1)), int(m.group(2))
            for feat in parts[3].split("|"):
                if feat.startswith("ROOT:"):
                    out.setdefault((s, v), []).append(feat[5:])
    return out


def block_root_set(qac, sid, vstart, vend):
    s = set()
    for v in range(vstart, vend + 1):
        for r in qac.get((sid, v), []):
            s.add(r)
    return s


def all_blocks_of_size(corpus, n):
    out = []
    for s in corpus:
        sid, nv = s["id"], s["total_verses"]
        for vs in range(1, nv - n + 2):
            out.append((sid, vs, vs + n - 1))
    return out


def overlaps_target(blk):
    sid, vs, ve = blk
    if sid != 83:
        return False
    return not (ve < 7 or vs > 28)


def main():
    verify_sha()
    rng = random.Random(SEED)

    with open(QURAN_PATH) as f:
        corpus = json.load(f)
    qac = load_qac_roots()

    Bf = (83, 7, 17)
    Ba = (83, 18, 28)
    Rf = block_root_set(qac, *Bf)
    Ra = block_root_set(qac, *Ba)

    inter = Rf & Ra
    union = Rf | Ra
    n_shared = len(inter)
    jaccard_obs = len(inter) / len(union) if union else 0.0

    # H3 — destiny disjunction
    fuj_in_abrar = ABRAR_DESTINY_ROOTS & Rf  # abrār-destiny roots wrongly in fujjār block
    abr_in_fujjar = FUJJAR_DESTINY_ROOTS & Ra
    sets_intersect = FUJJAR_DESTINY_ROOTS & ABRAR_DESTINY_ROOTS
    fujjar_present = FUJJAR_DESTINY_ROOTS & Rf
    abrar_present = ABRAR_DESTINY_ROOTS & Ra
    destiny_disjoint = (len(fuj_in_abrar) == 0 and len(abr_in_fujjar) == 0 and len(sets_intersect) == 0)

    # Null: random pairs of 11-verse blocks (corpus-wide contiguous windows)
    blocks = [b for b in all_blocks_of_size(corpus, 11) if not overlaps_target(b)]
    block_root_cache = {b: block_root_set(qac, *b) for b in blocks}
    null_shared, null_jac = [], []
    for _ in range(N_PERM):
        b1 = rng.choice(blocks)
        b2 = rng.choice(blocks)
        while b2 == b1:
            b2 = rng.choice(blocks)
        s1, s2 = block_root_cache[b1], block_root_cache[b2]
        i = len(s1 & s2)
        u = len(s1 | s2)
        null_shared.append(i)
        null_jac.append(i / u if u else 0.0)

    p_h1 = sum(1 for x in null_shared if x >= n_shared) / len(null_shared)
    null_shared_mean = sum(null_shared) / len(null_shared)
    pct_low_h2 = sum(1 for x in null_jac if x <= jaccard_obs) / len(null_jac)
    pct_high_h2 = sum(1 for x in null_jac if x >= jaccard_obs) / len(null_jac)
    null_jac_mean = sum(null_jac) / len(null_jac)

    # Sensitivity: within-single-surah 11-verse-block-pair null
    ws_pairs_shared = []
    by_surah = {}
    for b in blocks:
        by_surah.setdefault(b[0], []).append(b)
    multi = [s for s, bs in by_surah.items() if len(bs) >= 2]
    for _ in range(N_PERM):
        s = rng.choice(multi)
        b1, b2 = rng.sample(by_surah[s], 2)
        ws_pairs_shared.append(len(block_root_cache[b1] & block_root_cache[b2]))
    p_h1_ws = sum(1 for x in ws_pairs_shared if x >= n_shared) / len(ws_pairs_shared)

    h1_pass = (p_h1 <= ALPHA_BON) and (n_shared > null_shared_mean)
    h3_pass = destiny_disjoint
    h1_reversed = n_shared < null_shared_mean

    n_pass = int(h1_pass) + int(h3_pass)
    if n_pass == 2:
        verdict = "CONFIRMED"
    elif n_pass == 1:
        verdict = "DIRECTIONAL"
    else:
        verdict = "NULL"
    if h1_reversed:
        verdict += " (PRE-COMMIT-VIOLATION on H1: shared-root count below null mean)"

    # H2 descriptive classification
    if pct_high_h2 <= 0.05:
        h2_class = "LEXICAL-MIRROR (Jaccard in top 5% of block pairs)"
    elif pct_low_h2 <= 0.05:
        h2_class = "LEXICAL-DISJUNCTION (Jaccard in bottom 5%)"
    else:
        h2_class = "TYPICAL (Jaccard within central 90% of block pairs)"

    out = {
        "test_id": "Q083-F-01",
        "title": "SIJJĪN(7-17) <-> ʿILLIYYĪN(18-28) antithetical-pair: frame-mirror vs destiny-disjunction",
        "prereg_sha256": PREREG_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, QAC-STEM root tokens, QAC v0.4, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "blocks": {"fujjar_B_f": list(Bf), "abrar_B_a": list(Ba),
                   "n_roots_Bf": len(Rf), "n_roots_Ba": len(Ra)},
        "h1_frame_mirror": {
            "n_shared_roots": n_shared,
            "shared_roots": sorted(inter),
            "null_shared_mean": null_shared_mean,
            "null_shared_max": max(null_shared),
            "perm_p_one_sided_elevated": p_h1,
            "perm_p_within_surah_null": p_h1_ws,
            "alpha_bon": ALPHA_BON,
            "reversed": h1_reversed,
            "pass": h1_pass
        },
        "h2_overall_jaccard_pivot": {
            "jaccard_obs": jaccard_obs,
            "null_jaccard_mean": null_jac_mean,
            "pct_le_obs_low_side": pct_low_h2,
            "pct_ge_obs_high_side": pct_high_h2,
            "classification": h2_class,
            "note": "descriptive pivot; no locked direction; NOT a pass/fail gate"
        },
        "h3_destiny_disjunction": {
            "fujjar_destiny_roots_locked": sorted(FUJJAR_DESTINY_ROOTS),
            "abrar_destiny_roots_locked": sorted(ABRAR_DESTINY_ROOTS),
            "fujjar_destiny_present_in_Bf": sorted(fujjar_present),
            "abrar_destiny_present_in_Ba": sorted(abrar_present),
            "abrar_destiny_leaking_into_Bf": sorted(fuj_in_abrar),
            "fujjar_destiny_leaking_into_Ba": sorted(abr_in_fujjar),
            "locked_sets_intersect": sorted(sets_intersect),
            "destiny_disjoint": destiny_disjoint,
            "pass": h3_pass
        },
        "bonferroni_k": 3,
        "verdict": verdict
    }
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(OUTPUT_PATH, "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"VERDICT: {verdict}")
    print(json.dumps(out, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
