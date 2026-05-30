#!/usr/bin/env python3
"""
Q103-F-01 — al-ʿAṣr minimal qasam-architecture + emphatic-iconicity.
Pre-reg: surahs/Q103-al-asr/Q103-F-01-asr-minimal-prereg.md  (SHA-256 verified at runtime)
Seed 20260509, 10000 perms (Arm B only). Stdlib only.

Arm A — minimal-surah rā'-monorhyme structural twin (deterministic).
Arm B — emphatic-iconicity concentration vs length-matched corpus-window null (permutation).
Arm C — minimal tripartite qasam→jawāb→istithnāʾ skeleton (deterministic + within-corpus rank).
"""
import json, hashlib, random, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PREREG = os.path.join(ROOT, "surahs/Q103-al-asr/Q103-F-01-asr-minimal-prereg.md")
EXPECTED_SHA = "b6445946260ce8db4cbb424c8638ad5d5be030adbac6e47af6f9be130364037c"
OUT = os.path.join(ROOT, "surahs/Q103-al-asr/csv/Q103-F-01.json")
SEED = 20260509
N_PERM = 10000

ARABIC_LETTERS = set("ابتثجحخدذرزسشصضطظعغفقكلمنهوياءأإآؤئىة")
ISTILAA = set("خصضطظغق")  # Buckwalter x S D T Z g q

def verify_sha():
    h = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if h != EXPECTED_SHA:
        sys.exit(f"FAIL-FAST: pre-reg SHA mismatch\n expected {EXPECTED_SHA}\n got      {h}")
    return h

def letters_only(s):
    return [c for c in s if c in ARABIC_LETTERS]

def main():
    sha = verify_sha()
    qt = json.load(open(os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")))

    # ----- corpus letter stream + per-surah views -----
    full_stream = []
    surah_finals = {}   # sid -> list of verse-final arabic letters
    surah_letters = {}  # sid -> list of arabic letters
    for s in qt:
        sid = s["id"]
        finals = []
        slet = []
        for v in s["verses"]:
            toks = v["text"].split()
            lo = letters_only(v["text"])
            slet.extend(lo)
            last_tok_letters = letters_only(toks[-1])
            finals.append(last_tok_letters[-1] if last_tok_letters else None)
            full_stream.extend(lo)
        surah_finals[sid] = finals
        surah_letters[sid] = slet

    # ===== ARM A — minimal-surah rā'-monorhyme structural twin =====
    three_verse = [s["id"] for s in qt if s["total_verses"] == 3]
    ra_monorhyme = [sid for sid in three_verse
                    if surah_finals[sid] and all(f == "ر" for f in surah_finals[sid])]
    A_H1 = (sorted(ra_monorhyme) == [103, 108])

    # FR matrix — Q103 rank-1 neighbor
    fr = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-111.json")))
    dist = {}
    for i, j, d in fr["D_matrix_upper_triangular"]:
        if i == 103:
            dist[j] = d
        elif j == 103:
            dist[i] = d
    fr_order = sorted(dist, key=lambda k: dist[k])
    nn1 = fr_order[0]
    A_H2 = (nn1 == 108)
    arm_A = "CONFIRMED" if (A_H1 and A_H2) else "NULL"

    # ===== ARM B — emphatic-iconicity concentration =====
    q103 = surah_letters[103]
    n103 = len(q103)
    heavy103 = [c for c in q103 if c in ISTILAA]
    dens_obs = len(heavy103) / n103
    from collections import Counter
    heavy_break = dict(Counter(heavy103))
    sad_count = heavy_break.get("ص", 0)
    B_H1 = (round(dens_obs, 4) == 0.0959) and (sad_count >= len(heavy103) / 2.0)

    # corpus-window null: length-73 contiguous windows from full_stream
    rng = random.Random(SEED)
    N = len(full_stream)
    L = n103  # 73
    null = []
    max_start = N - L
    for _ in range(N_PERM):
        st = rng.randint(0, max_start)
        win = full_stream[st:st + L]
        null.append(sum(1 for c in win if c in ISTILAA) / L)
    null_mean = sum(null) / len(null)
    null_std = (sum((x - null_mean) ** 2 for x in null) / len(null)) ** 0.5
    n_ge = sum(1 for x in null if x >= dens_obs)
    p_perm = (n_ge + 1) / (N_PERM + 1)
    z_B = (dens_obs - null_mean) / null_std if null_std else float("nan")
    direction_ok = dens_obs > null_mean
    if not direction_ok:
        arm_B = "NULL (pre-commit violation)"
    elif B_H1 and p_perm < 0.05:
        arm_B = "CONFIRMED"
    elif B_H1:
        arm_B = "DIRECTIONAL"
    else:
        arm_B = "NULL"

    # ===== ARM C — minimal tripartite qasam→jawāb→istithnāʾ skeleton =====
    qj = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2210.json")))
    q103_cluster = None
    for c in qj["clusters"]:
        if c.get("surah") == 103:
            q103_cluster = c
            break
    # istithnāʾ particle at v3 from QAC
    morph = open(os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt"),
                 encoding="utf-8", errors="replace").read().splitlines()
    v3_exp = any(line.startswith("(103:3:1:1)") and "POS:EXP" in line for line in morph)
    C_H1 = (q103_cluster is not None
            and q103_cluster.get("qasam_to_jawab_verse_distance") == 1
            and q103_cluster.get("kinds") == ["waaw"]
            and v3_exp)

    sig = json.load(open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-750.json")))
    ps = sig["per_surah"]
    ps = ps if isinstance(ps, list) else list(ps.values())
    lc_sorted = sorted(ps, key=lambda x: -x["local_cohesion"])
    lc_rank = next(r for r, x in enumerate(lc_sorted, 1) if x["surah"] == 103)
    q103_lc = next(x["local_cohesion"] for x in ps if x["surah"] == 103)
    rhyme_ent = next(x["rhyme_entropy_nats"] for x in ps if x["surah"] == 103)
    C_H2 = (lc_rank <= 15)
    arm_C = "CONFIRMED" if (C_H1 and C_H2) else "NULL"

    result = {
        "test_id": "Q103-F-01",
        "prereg_sha256": sha,
        "seed": SEED, "n_perm": N_PERM,
        "rules_tuple": "(no-tashkeel, orthographic-token, graphemes/letters, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "arm_A": {
            "three_verse_surahs": three_verse,
            "ra_monorhyme_3verse": sorted(ra_monorhyme),
            "A_H1_pair_is_103_108": A_H1,
            "q103_fr_rank1_neighbor": nn1,
            "q103_fr_to_108": round(dist[108], 4),
            "A_H2_nn1_is_108": A_H2,
            "verdict": arm_A,
        },
        "arm_B": {
            "q103_total_letters": n103,
            "q103_heavy_count": len(heavy103),
            "q103_istilaa_density": round(dens_obs, 4),
            "heavy_breakdown": heavy_break,
            "sad_count": sad_count,
            "B_H1_dens_and_sad_dominant": B_H1,
            "null_mean": round(null_mean, 5),
            "null_std": round(null_std, 5),
            "z": round(z_B, 3),
            "p_perm": round(p_perm, 5),
            "direction_obs_gt_null": direction_ok,
            "verdict": arm_B,
        },
        "arm_C": {
            "qasam_cluster": q103_cluster,
            "v3_istithnaa_EXP_at_103_3_1_1": v3_exp,
            "C_H1_minimal_tripartite": C_H1,
            "q103_local_cohesion": round(q103_lc, 4),
            "q103_local_cohesion_rank_desc": lc_rank,
            "q103_rhyme_entropy_nats": rhyme_ent,
            "C_H2_top15_cohesion": C_H2,
            "verdict": arm_C,
        },
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))

if __name__ == "__main__":
    main()
