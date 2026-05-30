#!/usr/bin/env python3
"""
Q092-F-01 — the giver/miser antithetical pair as a shared-frame jadal instance.

Direction-locked replication of H-NEW-2360 at the single-surah hand-block scale:
 Arm A  content-overlap (permutation, seed 20260509, 10000 perms): J(G,M) > null  [LOCKED OVERLAP-positive]
 Arm B  frame-vs-pole decomposition (deterministic)
 Arm C  title-density-independence: Q92 lyl-root rank > 1 (deterministic, H-NEW-1820)

Rules-tuple: (no-tashkeel, orthographic-token, QAC v0.4 stem-roots,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Pre-reg SHA-256 is verified at runtime (fail-fast). No external dependencies.
"""
import json, random, hashlib, os, sys
from collections import defaultdict

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "surahs/Q092-al-layl/Q092-F-01-giver-miser-antithesis-prereg.md")
EXPECTED_SHA = "6e41fd080525daf5d638f84416339584e3bd6143da457850afc75363d01981b8"
SEED = 20260509
SEED_REPL = 20260601
N_PERM = 10000
OUT = os.path.join(ROOT, "surahs/Q092-al-layl/csv/Q092-F-01.json")

# ---- runtime SHA verification (fail-fast) ----
with open(PREREG, "rb") as f:
    got = hashlib.sha256(f.read()).hexdigest()
if got != EXPECTED_SHA:
    sys.exit(f"PRE-REG SHA MISMATCH\n expected {EXPECTED_SHA}\n got      {got}")
print(f"[ok] pre-reg SHA verified: {got}")

# ---- load QAC roots: (surah,verse) -> set(roots) ----
ri = json.load(open(os.path.join(ROOT, "data/morphology/root-index.json")))
v2roots = defaultdict(set)
surah_maxverse = defaultdict(int)
for root, atts in ri.items():
    for a in atts:
        s, v = a[0], a[1]
        v2roots[(s, v)].add(root)
        surah_maxverse[s] = max(surah_maxverse[s], v)

def block_roots(s, verses):
    out = set()
    for v in verses:
        out |= v2roots[(s, v)]
    return out

def jac(a, b):
    u = a | b
    return (len(a & b) / len(u)) if u else 0.0

# ---- observed blocks ----
G = block_roots(92, [5, 6, 7])    # giver: aʿṭā/ittaqā/ṣaddaqa/yusrā
M = block_roots(92, [8, 9, 10])   # miser: bakhila/istaghnā/kadhdhaba/ʿusrā
J_obs = jac(G, M)
print(f"[obs] G={sorted(G)} (|G|={len(G)})")
print(f"[obs] M={sorted(M)} (|M|={len(M)})")
print(f"[obs] shared={sorted(G & M)}  J(G,M)={J_obs:.4f}")

# ============== ARM A — content-overlap permutation null ==============
# Build pool of same-surah disjoint 3-consecutive-verse blocks, root-cardinality
# matched to (|G|,|M|) within ±2. Surah must have >=6 verses.
TOL = 2
nG, nM = len(G), len(M)

def all_3blocks(s):
    """all 3-consecutive-verse blocks of surah s with their root-cardinality"""
    out = []
    mx = surah_maxverse[s]
    for start in range(1, mx - 1):
        verses = [start, start + 1, start + 2]
        r = block_roots(s, verses)
        out.append((start, r))
    return out

# eligible surahs (>=6 verses so two disjoint 3-blocks can exist)
elig = [s for s in surah_maxverse if surah_maxverse[s] >= 6]

def run_null(seed):
    rng = random.Random(seed)
    null = []
    attempts = 0
    while len(null) < N_PERM and attempts < N_PERM * 200:
        attempts += 1
        s = rng.choice(elig)
        blocks = all_3blocks(s)
        if len(blocks) < 2:
            continue
        # pick two disjoint blocks matched to (nG,nM) within TOL
        cand_a = [b for b in blocks if abs(len(b[1]) - nG) <= TOL]
        cand_b = [b for b in blocks if abs(len(b[1]) - nM) <= TOL]
        if not cand_a or not cand_b:
            continue
        a = rng.choice(cand_a)
        # b must be disjoint in verse-range from a
        b_ok = [b for b in cand_b if abs(b[0] - a[0]) >= 3]
        if not b_ok:
            continue
        b = rng.choice(b_ok)
        null.append(jac(a[1], b[1]))
    return null

null_a = run_null(SEED)
null_mean = sum(null_a) / len(null_a)
null_std = (sum((x - null_mean) ** 2 for x in null_a) / len(null_a)) ** 0.5
n_ge = sum(1 for x in null_a if x >= J_obs)
p_upper = (n_ge + 1) / (len(null_a) + 1)
z = (J_obs - null_mean) / null_std if null_std > 0 else float("nan")
direction = "OVERLAP-positive (TIGHTER)" if J_obs > null_mean else "REVERSED (disjoint)"

# replication seed
null_a2 = run_null(SEED_REPL)
null_mean2 = sum(null_a2) / len(null_a2)
n_ge2 = sum(1 for x in null_a2 if x >= J_obs)
p_upper2 = (n_ge2 + 1) / (len(null_a2) + 1)

A_confirms = (J_obs > null_mean) and (p_upper < 0.05)
A_violation = (J_obs < null_mean)

print(f"\n[Arm A] null n={len(null_a)} mean={null_mean:.5f} std={null_std:.5f}")
print(f"[Arm A] J_obs={J_obs:.4f}  z={z:+.3f}  p_upper={p_upper:.4f}  dir={direction}")
print(f"[Arm A] replication seed {SEED_REPL}: null_mean={null_mean2:.5f} p_upper={p_upper2:.4f}")
print(f"[Arm A] CONFIRMS H-NEW-2360 overlap={A_confirms}  pre-commit-violation={A_violation}")

# ============== ARM B — frame-vs-pole decomposition ==============
FRAME = {"Hsn", "ysr"}                       # al-ḥusnā + nuyassiruhu...yusrā/ʿusrā scaffold
giver_poles = {"ETw", "wqy", "Sdq"}          # aʿṭā, ittaqā, ṣaddaqa
miser_poles = {"bxl", "gny", "k*b"}          # bakhila, istaghnā, kadhdhaba (QAC romanizes dhāl as *)
shared = G & M
shared_subset_frame = shared <= FRAME
poles_disjoint = len(giver_poles & miser_poles) == 0
# verify our partition matches the data
giver_poles_in_data = (giver_poles <= G)
miser_poles_in_data = (miser_poles <= M)
frame_in_both = FRAME <= (G & M)
B_pass = shared_subset_frame and poles_disjoint and giver_poles_in_data and miser_poles_in_data and frame_in_both
print(f"\n[Arm B] shared={sorted(shared)} ⊆ frame{sorted(FRAME)}: {shared_subset_frame}")
print(f"[Arm B] giver-poles {sorted(giver_poles)} ∩ miser-poles {sorted(miser_poles)} = ∅: {poles_disjoint}")
print(f"[Arm B] frame in both blocks: {frame_in_both} | PASS={B_pass}")

# ============== ARM C — title-density-independence (lyl rank) ==============
lyl = ri["lyl"]
cnt = defaultdict(int)
for a in lyl:
    cnt[a[0]] += 1
ranked = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))
q92_rank = next(i for i, (s, _) in enumerate(ranked, 1) if s == 92)
q92_count = cnt[92]
rank1 = ranked[0]
n_surahs_with_lyl = len(cnt)
total_lyl = len(lyl)
C_confirms = q92_rank > 1
print(f"\n[Arm C] lyl total attestations={total_lyl} across {n_surahs_with_lyl} surahs")
print(f"[Arm C] rank-1 in lyl = Q{rank1[0]} ({rank1[1]}×); Q92 count={q92_count} rank={q92_rank}/{n_surahs_with_lyl}")
print(f"[Arm C] CONFIRMS H-NEW-1820 title-density-independence: {C_confirms}")

# ============== write JSON ==============
result = {
    "test_id": "Q092-F-01",
    "title": "giver/miser antithetical pair as shared-frame jadal (H-NEW-2360 replication) + H-NEW-1820 lyl-rank",
    "prereg_sha256": EXPECTED_SHA,
    "seed": SEED, "seed_replication": SEED_REPL, "n_perm": N_PERM,
    "rules_tuple": "(no-tashkeel, orthographic-token, QAC v0.4 stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
    "bonferroni_k": 1, "alpha_bon": 0.05,
    "blocks": {
        "giver_v5_7_roots": sorted(G), "miser_v8_10_roots": sorted(M),
        "shared_roots": sorted(shared), "J_obs": J_obs,
    },
    "arm_A_content_overlap": {
        "J_obs": J_obs, "null_mean": null_mean, "null_std": null_std,
        "z": z, "p_upper_tail": p_upper, "n_ge": n_ge, "n_null": len(null_a),
        "direction_locked": "OVERLAP-positive (TIGHTER than random)",
        "direction_observed": direction,
        "replication_seed": SEED_REPL, "repl_null_mean": null_mean2, "repl_p_upper": p_upper2,
        "tolerance_roots": TOL, "block_cardinalities": [nG, nM],
        "confirms_h_new_2360_overlap": A_confirms, "pre_commit_violation": A_violation,
    },
    "arm_B_frame_pole": {
        "frame": sorted(FRAME), "giver_poles": sorted(giver_poles), "miser_poles": sorted(miser_poles),
        "shared_subset_frame": shared_subset_frame, "poles_disjoint": poles_disjoint,
        "PASS": B_pass,
    },
    "arm_C_title_density": {
        "lyl_total_attestations": total_lyl, "n_surahs_with_lyl": n_surahs_with_lyl,
        "rank1_surah": rank1[0], "rank1_count": rank1[1],
        "q92_lyl_count": q92_count, "q92_lyl_rank": q92_rank,
        "confirms_h_new_1820": C_confirms,
    },
}
os.makedirs(os.path.dirname(OUT), exist_ok=True)
json.dump(result, open(OUT, "w"), ensure_ascii=False, indent=2)
print(f"\n[done] wrote {OUT}")
