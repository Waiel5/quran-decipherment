#!/usr/bin/env python3
"""
H-NEW-2880 POST-HOC. Declared post-hoc; gates nothing; run AFTER the locked verdict was
computed and printed.

It asks the one question that can only DEFLATE the primary result, never support it:

    Does the exact-concentration null get beaten by ANY vowel-truncating reduction, or
    specifically by the waqf rules?

P3 is the deliberately-WRONG pausal tuple pre-registered by H-NEW-2870 §5 — it drops tanwin
fath without the compensatory alif, which is not what waqf does in any reading. If P3 also
sits far outside its own exactly-matched null, then what the primary result establishes is a
property of the whole family of final-vowel-truncating reductions and not of waqf's specific
rules, and the finding must say so.

Also reports the split of waqf's merged cross-type adjacent pairs into those a bare
truncation could merge and those that require the transformational rule -an -> a:.

Reads nothing from the run directory and writes nothing into it.
"""
import json
import os
import random
import sys
from collections import Counter, defaultdict

import numpy as np

REPO = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", ".."))
os.chdir(REPO)

RUNNER = "findings/phase-b-hypotheses/scripts/h-new-2880.py"
src = open(RUNNER, encoding="utf-8").read()
cut = src.index("# ---------------------------------------------------------------- 4. ANTI-GAMING AUDIT")
ns = {"__name__": "instrument-2880", "__file__": RUNNER}
_argv = sys.argv
sys.argv = [_argv[0], "--smoke"]          # loads the machinery only; writes nothing
exec(compile(src[:cut], "h-new-2880-machinery", "exec"), ns)
sys.argv = _argv

TUP, Tuple2, run_exact_null = ns["TUP"], ns["Tuple2"], ns["run_exact_null"]
AGREE, DELTA, FLOOR = ns["AGREE"], ns["DELTA"], ns["FLOOR"]
N_PERM, SEED, SEED_REP = 10000, ns["SEED"], ns["SEED_REP"]
ns["N_PERM"] = N_PERM
STEM_MASK, PAIRS, N_PAIRS = ns["STEM_MASK"], ns["PAIRS"], ns["N_PAIRS"]
PA, PB = ns["PA"], ns["PB"]

print("\n" + "=" * 78)
print("H-NEW-2880 POST-HOC — declared post-hoc, gates nothing")
print("=" * 78)

# ---- 1. the deflation check: does the WRONG pausal tuple also beat its matched null?
out = {"note": "POST-HOC; gates nothing", "n_perm": N_PERM, "seed": SEED, "arms": {}}
print("\n(1) Does the exact null get beaten by the deliberately-WRONG pausal tuple P3?")
# the null of prereg §5 is defined only when the tuple's partition is a coarsening of the
# citation partition; checked here rather than assumed
F2 = ns["FLATS"]["R2"]
for conv in ("P1", "P2", "P3"):
    seen = defaultdict(set)
    for ct, pt in zip(F2["C"], F2[conv]):
        seen[ct].add(pt)
    nsplit = sum(1 for v in seen.values() if len(v) > 1)
    print(f"   {conv}: citation types split across classes = {nsplit} "
          f"({'coarsening — null well posed' if nsplit == 0 else 'NOT a coarsening — null ill posed, arm skipped'})")
    if nsplit:
        out["arms"][conv] = {"skipped": "not a coarsening of the citation partition"}
for conv in ("P1", "P2", "P3"):
    if out["arms"].get(conv, {}).get("skipped"):
        continue
    T = TUP[conv] if conv in TUP else Tuple2(conv)
    r = run_exact_null("S2", T, SEED, N_PERM, want_ari=False)
    r2 = run_exact_null("S2", T, SEED_REP, N_PERM, want_ari=False)
    out["arms"][conv] = {"primary": r, "replication": r2,
                         "delta_vs_citation": DELTA["R2"][conv],
                         "K": T.K, "floor": T.floor_obs}
    print(f"   {conv}: K={T.K:4d}  floor={T.floor_obs:.4f}  Δ vs citation="
          f"{DELTA['R2'][conv]:+.4f}")
    print(f"        E_obs={r['observed_E']:.4f} | null E mean={r['null_E_mean']:.4f} "
          f"sd={r['null_E_sd']:.4f} max={r['null_E_max']:.4f} | #>=obs="
          f"{r['n_ge_observed_E']} p={r['p_E']:.5f} z={r['z_E']:+.2f}  "
          f"(replication p={r2['p_E']:.5f} z={r2['z_E']:+.2f})")
        # floor exactness is re-asserted for every post-hoc arm too
    assert r["null_floor_max_abs_dev"] == 0.0, "post-hoc arm lost floor exactness"

# ---- 2. how much of waqf's merging needs the transformational rule?
print("\n(2) The merged cross-type adjacent pairs, split by what rule merges them")
for conv in ("P1", "P2"):
    T = TUP[conv]
    same_cit = int((PA == PB).sum())
    merged = (T.OBS[PA] == T.OBS[PB])
    cross_merged = int((merged & (PA != PB)).sum())
    need_transform = int((merged & STEM_MASK).sum())
    trunc_only = cross_merged - need_transform
    out.setdefault("merge_split", {})[conv] = {
        "adjacent_pairs": N_PAIRS, "same_citation_type": same_cit,
        "cross_type_merged_by_waqf": cross_merged,
        "mergeable_by_truncation_alone": trunc_only,
        "require_transformational_rule": need_transform,
        "transformational_share": need_transform / cross_merged}
    print(f"   {conv}: {cross_merged} cross-type pairs merged by waqf; "
          f"{trunc_only} of them a bare truncation would also merge, "
          f"{need_transform} ({100 * need_transform / cross_merged:.1f}%) require the "
          f"transformational rule -an -> a:")

os.makedirs("findings/phase-b-hypotheses/csv", exist_ok=True)
with open("findings/phase-b-hypotheses/csv/h-new-2880-posthoc.json", "w", encoding="utf-8") as f:
    json.dump(out, f, ensure_ascii=False, indent=2, default=float)
print("\n[WROTE] findings/phase-b-hypotheses/csv/h-new-2880-posthoc.json")
