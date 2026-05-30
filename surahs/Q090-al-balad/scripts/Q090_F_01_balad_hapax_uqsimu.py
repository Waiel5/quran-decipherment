#!/usr/bin/env python3
"""
Q090-F-01 — Q 90 al-Balad corpus-hapax-root enrichment test.

Pre-registration: surahs/Q090-al-balad/Q090-F-01-balad-hapax-uqsimu-prereg.md
SHA-256 (locked)  : 5ab5e79bb7e3dcf20a36e1e7e5fccc0d64cdcbe6ac27d52c0925d7d988411d18

Verdict-bearing arms (Bonferroni k=2, alpha_bon=0.025, one-sided ENRICHMENT, LOCKED direction):
  H1 (Arm A): #corpus-exclusive roots assigned to Q90  >  length-preserving label-perm null
  H2 (Arm B): exclusive-root DENSITY (T/distinct)        >  same null
Null model: Fisher-Yates shuffle of the surah-label column over the full root-occurrence stream
            (preserves per-surah token counts and per-root total frequency).
MW-5 replication: second seed. MW-6: Q91 al-Shams negative control.

Stdlib only.
"""
import json, os, re, random, hashlib

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
PREREG = os.path.join(ROOT, "surahs", "Q090-al-balad",
                      "Q090-F-01-balad-hapax-uqsimu-prereg.md")
MORPH = os.path.join(ROOT, "data", "morphology", "quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "surahs", "Q090-al-balad", "csv", "Q090-F-01.json")

EXPECTED_SHA = "5ab5e79bb7e3dcf20a36e1e7e5fccc0d64cdcbe6ac27d52c0925d7d988411d18"
SEED_PRIMARY = 20260509
SEED_REPLICATION = 20260530
N_PERM = 10000
ALPHA_BON = 0.025
TARGET = 90
CONTROL = 91  # MW-6 length-matched short-Meccan neighbour

def verify_sha():
    h = hashlib.sha256(open(PREREG, "rb").read()).hexdigest()
    if h != EXPECTED_SHA:
        raise SystemExit(f"FAIL-FAST: pre-reg SHA mismatch\n got {h}\n exp {EXPECTED_SHA}")
    print(f"[ok] pre-reg SHA verified: {h}")

def load_occurrences():
    """Ordered list of (surah, root) for every QAC token carrying a ROOT field."""
    occ = []
    pat = re.compile(r'\((\d+):\d+:\d+:\d+\)')
    rootpat = re.compile(r'ROOT:([^|\s]+)')
    with open(MORPH, encoding="utf-8") as f:
        for line in f:
            m = pat.match(line)
            if not m:
                continue
            rm = rootpat.search(line)
            if rm:
                occ.append((int(m.group(1)), rm.group(1)))
    return occ

def exclusive_count(surah_labels, roots, target):
    """OBSERVED-only helper: #roots whose every occurrence lands in `target`, and #distinct in target."""
    seen_other = set()   # roots seen in a surah != target
    seen_target = set()  # roots seen in target
    for s, r in zip(surah_labels, roots):
        if s == target:
            seen_target.add(r)
        else:
            seen_other.add(r)
    return sum(1 for r in seen_target if r not in seen_other), len(seen_target)

def _root_groups(roots):
    """Map each root -> sorted list of its occurrence indices (0..N-1)."""
    groups = {}
    for idx, r in enumerate(roots):
        groups.setdefault(r, []).append(idx)
    return groups

def run_null(surah_col, roots, target, seed):
    """
    Equivalent fast null. A label-column permutation that preserves per-surah token
    counts and per-root frequencies is, for the purpose of 'which roots are target-exclusive',
    identical to: choose WHICH n_target of the N occurrence-slots receive the target label
    (multivariate-hypergeometric). We realise this by assigning every occurrence a random
    priority key (one shuffle of 0..N-1) and declaring the n_target smallest-keyed slots to be
    'target'. A root is target-exclusive iff the MAX key over its occurrence-slots < n_target.
    This reproduces exclusive_count's count statistic exactly and is O(N) per permutation.
    """
    rng = random.Random(seed)
    N = len(surah_col)
    n_target = sum(1 for s in surah_col if s == target)
    groups = _root_groups(roots)            # root -> [occ indices]
    group_idx = list(groups.values())       # list of index-lists
    key = list(range(N))
    counts, dens = [], []
    for _ in range(N_PERM):
        rng.shuffle(key)                    # key[occ] = random priority rank
        # n_distinct_in_target = #roots with at least one occ-slot keyed < n_target
        # exclusive = #roots with ALL occ-slots keyed < n_target
        c = 0; d = 0
        for idxs in group_idx:
            mn = N; mx = -1
            for i in idxs:
                k = key[i]
                if k < mn: mn = k
                if k > mx: mx = k
            if mn < n_target:      # at least one occurrence in target -> distinct-in-target
                d += 1
                if mx < n_target:  # ALL occurrences in target -> exclusive
                    c += 1
        counts.append(c)
        dens.append(c / d if d else 0.0)
    return counts, dens

def perm_p(null_counts, obs):
    ge = sum(1 for c in null_counts if c >= obs)
    return (ge + 1) / (N_PERM + 1)

def main():
    verify_sha()
    occ = load_occurrences()
    surah_col = [s for s, _ in occ]
    roots = [r for _, r in occ]
    N = len(occ)
    print(f"[info] root-occurrences N={N}")

    # observed
    t_obs, n_distinct = exclusive_count(surah_col, roots, TARGET)
    dens_obs = t_obs / n_distinct if n_distinct else 0.0
    print(f"[obs ] Q{TARGET}: exclusive_roots={t_obs}, distinct_roots={n_distinct}, "
          f"density={dens_obs:.5f}")

    # which roots are the exclusives (for the write-up)
    seen_other, seen_target = set(), set()
    for s, r in occ:
        (seen_target if s == TARGET else seen_other).add(r)
    excl = sorted(r for r in seen_target if r not in seen_other)

    # primary null (H1 count + H2 density from the SAME permutation draws)
    null_counts, null_dens = run_null(surah_col, roots, TARGET, SEED_PRIMARY)
    p_H1 = perm_p(null_counts, t_obs)
    ge_d = sum(1 for x in null_dens if x >= dens_obs)
    p_H2 = (ge_d + 1) / (N_PERM + 1)

    null_mean = sum(null_counts) / len(null_counts)
    null_max = max(null_counts)

    # MW-5 replication (count arm)
    null_rep, _ = run_null(surah_col, roots, TARGET, SEED_REPLICATION)
    p_H1_rep = perm_p(null_rep, t_obs)

    # MW-6 negative control: Q91
    c_obs, c_distinct = exclusive_count(surah_col, roots, CONTROL)
    c_dens = c_obs / c_distinct if c_distinct else 0.0
    null_ctrl, _ = run_null(surah_col, roots, CONTROL, SEED_PRIMARY)
    p_ctrl = perm_p(null_ctrl, c_obs)

    # verdict
    pass_H1 = (p_H1 < ALPHA_BON) and (t_obs > null_mean)
    pass_H2 = (p_H2 < ALPHA_BON) and (dens_obs > (null_mean / n_distinct))
    violation = t_obs < null_mean
    if violation:
        verdict = "NULL (PRE-COMMIT VIOLATION: depletion direction)"
    elif pass_H1 and pass_H2 and (p_H1_rep < ALPHA_BON):
        verdict = "CONFIRMED"
    elif (p_H1 < 0.05) or (p_H2 < 0.05):
        verdict = "PARTIAL/DIRECTIONAL"
    else:
        verdict = "NULL"

    result = {
        "test_id": "Q090-F-01",
        "prereg_sha256": EXPECTED_SHA,
        "seed_primary": SEED_PRIMARY,
        "seed_replication": SEED_REPLICATION,
        "n_perm": N_PERM,
        "bonferroni_k": 2,
        "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, QAC-v0.4 STEM root-tokens, graphemes, "
                       "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "n_root_occurrences": N,
        "observed": {
            "T_obs_exclusive_roots": t_obs,
            "distinct_roots": n_distinct,
            "exclusive_density": dens_obs,
            "exclusive_roots": excl,
        },
        "H1_count": {
            "p_perm": p_H1, "null_mean": null_mean, "null_max": null_max,
            "direction": "enrichment (upper tail)", "pass_alpha_bon": pass_H1,
        },
        "H2_density": {
            "p_perm": p_H2, "pass_alpha_bon": pass_H2,
            "direction": "enrichment (upper tail)",
        },
        "MW5_replication": {"seed": SEED_REPLICATION, "p_perm_count": p_H1_rep},
        "MW6_control_Q91": {
            "T_obs": c_obs, "distinct_roots": c_distinct, "density": c_dens,
            "p_perm": p_ctrl,
        },
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    print(f"\n[done] wrote {OUT}")

if __name__ == "__main__":
    main()
