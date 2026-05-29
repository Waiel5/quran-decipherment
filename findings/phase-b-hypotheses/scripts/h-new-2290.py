#!/usr/bin/env python3
"""
H-NEW-2290 — Verse-pair chiasmus / antithetical-mirror generator (adjacent scale).

Two pre-registered sub-tests (Bonferroni family k=2, alpha_bon=0.025):
  (A) Word-order chiasmus: across each consecutive verse-pair, do shared content
      roots appear in REVERSED linear order (AB->BA)? Null = within-surah
      verse-order shuffle, 10000 perms, seed 20260509. Direction LOCKED:
      R_obs > R_null (excess reversal vs random adjacency).
  (B) Antithetical parallelism: a verse-pair is antithetical iff one verse carries
      a field's positive pole and the other carries the same field's negative pole
      (locked 8-field antonym lexicon). Direction LOCKED: density(region A: mushaf
      78-114) > density(region B: mushaf 1-49). Null = label permutation, 10000
      perms, seed 20260509.

All numbers from disk. Outputs JSON to findings/phase-b-hypotheses/csv/h-new-2290.json.

Rules-tuple: (no-tashkeel, QAC v0.4 STEM-ROOT tokens with word-order preserved by
segment index, content-root sequence, basmala-counted-only-in-Q1, Hafs-Kufan,
Mashriqi).

Single-author: Waiel Al-Shujaa, Quran Decipherment Project.
"""
import hashlib
import json
import os
import re
import sys

import numpy as np

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2290-verse-pair-chiasmus.md")
PREREG_SHA = "789b82551afdcf74769dda571d15af16a16aabf5026a9aa83628aedcf36674fc"
QAC = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2290.json")

BASE_SEED = 20260509
N_PERM = 10000
ALPHA_RAW = 0.05
K_BON = 2
ALPHA_BON = ALPHA_RAW / K_BON  # 0.025

# ----------------------------------------------------------------------------
# Locked antonym-field lexicon (§B of pre-reg). Root sets; lemma-restriction sets
# given separately. A code that does not attest in QAC is simply a no-op (honest:
# documented in findings). Buckwalter codes as written in the locked pre-reg.
# ----------------------------------------------------------------------------
# Fields: each -> (positive spec, negative spec). A spec is a dict with
#   'roots': set of root codes tagged regardless of lemma,
#   'lemma': dict root-> set of allowed lemmas (only those lemmas tag the pole).
FIELDS = {
    "F1_faith": (
        {"roots": {"Amn"}, "lemma": {}},
        {"roots": {"kfr", "nfq", "Srk"}, "lemma": {}},  # Srk locked-typo -> no-op
    ),
    "F2_guidance": (
        {"roots": {"hdy"}, "lemma": {}},
        {"roots": {"Dll"}, "lemma": {}},
    ),
    "F3_paradise_hellfire": (
        {"roots": set(), "lemma": {"jnn": {"jan~ap"}}},
        {"roots": {"jHm", "sEr", "sqr", "lZy"},
         "lemma": {"Hmm": {"Hamiym"}, "nwr": {"naAr"}, "Hwy": {"haAwiyap"}}},
    ),
    "F4_light_dark": (
        {"roots": set(), "lemma": {"nwr": {"nuwr", "m~uniyr"}}},
        {"roots": set(), "lemma": {"Zlm": {"Zuluma`t"}}},
    ),
    "F5_reward_punish": (
        {"roots": {"vwb", ">jr"},  # >jr locked-typo (real Ajr) -> no-op
         "lemma": {"jzy": {"jazaY`", "jazaA^'"}}},
        {"roots": set(),
         "lemma": {"Eqb": {"Ea`qibap", "EiqaAb", "EuqobaY"}}},
    ),
    "F6_righteous_corrupt": (
        {"roots": {"SlH", "brr"}, "lemma": {}},
        {"roots": {"fsd"}, "lemma": {"swA": {"suw^'", "say~i}ap", "say~i_#aAt"}}},
    ),
    "F7_good_foul": (
        {"roots": {"Tyb"}, "lemma": {}},
        {"roots": {"xbv"}, "lemma": {}},
    ),
    "F8_life_death": (
        {"roots": {"Hyy"}, "lemma": {}},
        {"roots": {"mwt"}, "lemma": {}},
    ),
}

REGION_A = set(range(78, 115))   # short eschatological mufassal (juz' amma)
REGION_B = set(range(1, 50))     # long surahs
# robustness sharper contrast (MW-3): mufassal-only [>=78] vs tiwal-only [1..9]
REGION_A2 = set(range(78, 115))
REGION_B2 = set(range(1, 10))


def verify_sha():
    with open(PREREG, "rb") as fh:
        actual = hashlib.sha256(fh.read()).hexdigest()
    if actual != PREREG_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH\n expected {PREREG_SHA}\n actual   {actual}\n"
                 "Pre-registration modified after locking. ABORT (pre-commit discipline).")
    print(f"[ok] pre-reg SHA verified: {actual}")


# QAC line: (s:v:w:seg)\tform\tPOS\tFEATURES  with possibly ROOT: and LEM:
LINE_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)\t([^\t]*)\t([^\t]*)\t(.*)$")
ROOT_RE = re.compile(r"ROOT:([^|]+)")
LEM_RE = re.compile(r"LEM:([^|]+)")


def load_verse_root_seqs():
    """surah -> ordered list (verse 1..n) of ordered (root,lemma) tuples on STEM segs,
    preserving word:segment order. Also surah -> n_verses (from text)."""
    # collect per (s,v): list of (word,seg,root,lemma)
    per = {}
    with open(QAC, encoding="utf-8") as fh:
        for line in fh:
            m = LINE_RE.match(line.rstrip("\n"))
            if not m:
                continue
            s, v, w, seg = (int(m.group(1)), int(m.group(2)),
                            int(m.group(3)), int(m.group(4)))
            feats = m.group(7)
            if "STEM" not in feats:
                continue
            rm = ROOT_RE.search(feats)
            if not rm:
                continue
            lm = LEM_RE.search(feats)
            root = rm.group(1).strip()
            lemma = lm.group(1).strip() if lm else ""
            per.setdefault((s, v), []).append((w, seg, root, lemma))
    return per


def build_surahs(per, text):
    """Return surahs: dict surah_id -> list over verses of dict:
       {'seq': [roots in order, adjacent dups collapsed],
        'pairs': set of (root,lemma) for pole-tagging}."""
    surahs = {}
    for sd in text:
        sid = sd["id"]
        nv = sd["total_verses"]
        verses = []
        for vi in range(1, nv + 1):
            segs = sorted(per.get((sid, vi), []), key=lambda t: (t[0], t[1]))
            ordered_roots = []
            for (_, _, root, _lem) in segs:
                if not ordered_roots or ordered_roots[-1] != root:
                    ordered_roots.append(root)
            rootlemma = set((root, lem) for (_, _, root, lem) in segs)
            verses.append({"seq": ordered_roots, "rl": rootlemma})
        surahs[sid] = verses
    return surahs


# ----------------------------- Sub-test A: chiasmus -------------------------
def reversed_same_counts(seq_a, seq_b):
    """Return (n_reversed, n_same) ordered shared-root pairs across two verses."""
    set_a, set_b = set(seq_a), set(seq_b)
    shared = set_a & set_b
    if len(shared) < 2:
        return 0, 0
    # first-occurrence rank in each sequence
    rank_a = {}
    for i, r in enumerate(seq_a):
        if r in shared and r not in rank_a:
            rank_a[r] = i
    rank_b = {}
    for i, r in enumerate(seq_b):
        if r in shared and r not in rank_b:
            rank_b[r] = i
    sl = sorted(shared)
    nrev = nsame = 0
    for ii in range(len(sl)):
        for jj in range(ii + 1, len(sl)):
            x, y = sl[ii], sl[jj]
            a_order = rank_a[x] < rank_a[y]   # True: x before y in verse a
            b_order = rank_b[x] < rank_b[y]
            if a_order == b_order:
                nsame += 1
            else:
                nrev += 1
    return nrev, nsame


def chiasm_rate_from_seqs(seqs_by_surah):
    """seqs_by_surah: surah-> list of seq-lists. Return (R, total_rev, total_same)."""
    tot_rev = tot_same = 0
    for sid, seqs in seqs_by_surah.items():
        for i in range(len(seqs) - 1):
            nr, ns = reversed_same_counts(seqs[i], seqs[i + 1])
            tot_rev += nr
            tot_same += ns
    denom = tot_rev + tot_same
    R = tot_rev / denom if denom else 0.0
    return R, tot_rev, tot_same


def run_chiasmus(surahs):
    seqs_by_surah = {sid: [v["seq"] for v in vs] for sid, vs in surahs.items()}
    R_obs, tot_rev, tot_same = chiasm_rate_from_seqs(seqs_by_surah)

    # census of reversed-order pairs
    census = []
    for sid in sorted(surahs):
        seqs = [v["seq"] for v in surahs[sid]]
        for i in range(len(seqs) - 1):
            nr, ns = reversed_same_counts(seqs[i], seqs[i + 1])
            if nr > 0:
                set_a, set_b = set(seqs[i]), set(seqs[i + 1])
                shared = sorted(set_a & set_b)
                rank_a = {r: idx for idx, r in enumerate(seqs[i]) if r in shared}
                rank_b = {r: idx for idx, r in enumerate(seqs[i + 1]) if r in shared}
                revpairs = []
                sl = shared
                for ii in range(len(sl)):
                    for jj in range(ii + 1, len(sl)):
                        x, y = sl[ii], sl[jj]
                        if (rank_a[x] < rank_a[y]) != (rank_b[x] < rank_b[y]):
                            revpairs.append([x, y])
                census.append({"surah": sid, "v_i": i + 1, "v_j": i + 2,
                               "n_reversed": nr, "n_same": ns,
                               "reversed_root_pairs": revpairs})

    # null: within-surah verse-order shuffle
    rng = np.random.default_rng(BASE_SEED)
    perm_R = np.empty(N_PERM)
    seq_lists = {sid: [v["seq"] for v in vs] for sid, vs in surahs.items()}
    for p in range(N_PERM):
        shuffled = {}
        for sid, seqs in seq_lists.items():
            n = len(seqs)
            if n <= 1:
                shuffled[sid] = seqs
                continue
            order = rng.permutation(n)
            shuffled[sid] = [seqs[k] for k in order]
        R, _, _ = chiasm_rate_from_seqs(shuffled)
        perm_R[p] = R
    ge = int(np.sum(perm_R >= R_obs))
    p_one = (1 + ge) / (N_PERM + 1)
    return {
        "R_obs": R_obs,
        "total_reversed": tot_rev,
        "total_same": tot_same,
        "total_ordered_pairs": tot_rev + tot_same,
        "null_mean_R": float(np.mean(perm_R)),
        "null_sd_R": float(np.std(perm_R)),
        "p_one_sided_chiastic": p_one,
        "direction_observed": "chiastic (R_obs>null)" if R_obs > np.mean(perm_R)
                              else "parallel (R_obs<=null)",
        "n_verse_pairs_with_reversal": len(census),
        "census": census,
    }


def run_chiasmus_triplet(surahs):
    """MW-3: triplet windows; reversed-order over union of 3 consecutive verses,
    measured as reversal between verse i and verse i+2 (outer pair of the triplet),
    using the same ordered-shared-root rule."""
    tot_rev = tot_same = 0
    census_n = 0
    for sid, vs in surahs.items():
        seqs = [v["seq"] for v in vs]
        for i in range(len(seqs) - 2):
            nr, ns = reversed_same_counts(seqs[i], seqs[i + 2])
            tot_rev += nr
            tot_same += ns
            if nr > 0:
                census_n += 1
    denom = tot_rev + tot_same
    R = tot_rev / denom if denom else 0.0
    # null
    rng = np.random.default_rng(BASE_SEED + 1)
    seq_lists = {sid: [v["seq"] for v in vs] for sid, vs in surahs.items()}
    perm_R = np.empty(N_PERM)
    for p in range(N_PERM):
        tr = ts = 0
        for sid, seqs in seq_lists.items():
            n = len(seqs)
            if n <= 2:
                sh = seqs
            else:
                order = rng.permutation(n)
                sh = [seqs[k] for k in order]
            for i in range(len(sh) - 2):
                nr, ns = reversed_same_counts(sh[i], sh[i + 2])
                tr += nr
                ts += ns
        perm_R[p] = tr / (tr + ts) if (tr + ts) else 0.0
    ge = int(np.sum(perm_R >= R))
    return {"R_obs": R, "total_reversed": tot_rev, "total_same": tot_same,
            "null_mean_R": float(np.mean(perm_R)),
            "p_one_sided_chiastic": (1 + ge) / (N_PERM + 1),
            "n_outer_pairs_with_reversal": census_n}


# ----------------------------- Sub-test B: antithetical ---------------------
def verse_poles(rl_set):
    """rl_set: set of (root,lemma). Return dict field-> set of {'+','-'} poles
    present in this verse."""
    out = {}
    for fname, (pos, neg) in FIELDS.items():
        poles = set()
        # positive
        if any(r in pos["roots"] for (r, l) in rl_set):
            poles.add("+")
        else:
            for r, l in rl_set:
                if r in pos["lemma"] and l in pos["lemma"][r]:
                    poles.add("+")
                    break
        # negative
        if any(r in neg["roots"] for (r, l) in rl_set):
            poles.add("-")
        else:
            for r, l in rl_set:
                if r in neg["lemma"] and l in neg["lemma"][r]:
                    poles.add("-")
                    break
        if poles:
            out[fname] = poles
    return out


def antithetical_pair(poles_i, poles_j):
    """Return list of fields that are antithetical across the pair (one verse +,
    other verse -)."""
    fields = []
    for fname in FIELDS:
        pi = poles_i.get(fname, set())
        pj = poles_j.get(fname, set())
        # cross-verse contrast: (+ in i and - in j) or (- in i and + in j)
        if ("+" in pi and "-" in pj) or ("-" in pi and "+" in pj):
            fields.append(fname)
    return fields


def run_antithetical(surahs):
    # build per-surah poles and the global list of consecutive pairs
    all_pairs = []  # (surah, i, j, is_antithetical, fields)
    census = []
    surah_counts = {}
    for sid in sorted(surahs):
        vs = surahs[sid]
        poles = [verse_poles(v["rl"]) for v in vs]
        n_pairs = 0
        n_anti = 0
        for i in range(len(vs) - 1):
            n_pairs += 1
            fields = antithetical_pair(poles[i], poles[i + 1])
            is_anti = len(fields) > 0
            if is_anti:
                n_anti += 1
                # record which verse carried which pole per field
                detail = {}
                for f in fields:
                    pi = poles[i].get(f, set())
                    pj = poles[i + 1].get(f, set())
                    detail[f] = {"v_i_poles": sorted(pi), "v_j_poles": sorted(pj)}
                census.append({"surah": sid, "v_i": i + 1, "v_j": i + 2,
                               "fields": fields, "detail": detail})
            all_pairs.append((sid, i + 1, i + 2, is_anti))
        surah_counts[sid] = {"n_pairs": n_pairs, "n_anti": n_anti,
                             "density": n_anti / n_pairs if n_pairs else 0.0}

    def region_density(region):
        np_ = na = 0
        for (sid, i, j, is_anti) in all_pairs:
            if sid in region:
                np_ += 1
                if is_anti:
                    na += 1
        return (na / np_ if np_ else 0.0), na, np_

    dA, naA, npA = region_density(REGION_A)
    dB, naB, npB = region_density(REGION_B)
    delta_obs = dA - dB

    # null: permute antithetical labels across ALL corpus consecutive pairs,
    # holding region pair-counts fixed; recompute delta.
    labels = np.array([1 if is_anti else 0 for (_, _, _, is_anti) in all_pairs])
    region_of = np.array([0 if sid in REGION_A else (1 if sid in REGION_B else 2)
                          for (sid, _, _, _) in all_pairs])
    maskA = region_of == 0
    maskB = region_of == 1
    npA_ = int(maskA.sum())
    npB_ = int(maskB.sum())
    rng = np.random.default_rng(BASE_SEED)
    perm_delta = np.empty(N_PERM)
    for p in range(N_PERM):
        perm = rng.permutation(labels)
        da = perm[maskA].sum() / npA_ if npA_ else 0.0
        db = perm[maskB].sum() / npB_ if npB_ else 0.0
        perm_delta[p] = da - db
    ge = int(np.sum(perm_delta >= delta_obs))
    p_one = (1 + ge) / (N_PERM + 1)

    # MW-3 robustness sharper contrast
    dA2, naA2, npA2 = region_density(REGION_A2)
    dB2, naB2, npB2 = region_density(REGION_B2)

    return {
        "region_A_def": "mushaf 78-114",
        "region_B_def": "mushaf 1-49",
        "density_A": dA, "n_anti_A": naA, "n_pairs_A": npA,
        "density_B": dB, "n_anti_B": naB, "n_pairs_B": npB,
        "delta_obs": delta_obs,
        "null_mean_delta": float(np.mean(perm_delta)),
        "null_sd_delta": float(np.std(perm_delta)),
        "p_one_sided_A_gt_B": p_one,
        "direction_observed": "A>B (locked)" if delta_obs > 0 else "A<=B (REVERSAL)",
        "robustness_sharper": {
            "region_A2": "mushaf 78-114", "region_B2": "mushaf 1-9",
            "density_A2": dA2, "density_B2": dB2, "delta2": dA2 - dB2,
        },
        "total_antithetical_pairs": int(labels.sum()),
        "total_consecutive_pairs": int(len(labels)),
        "per_surah": surah_counts,
        "census": census,
    }


def main():
    verify_sha()
    text = json.load(open(os.path.join(ROOT, "quran-text/quran-no-tashkeel.json"),
                          encoding="utf-8"))
    per = load_verse_root_seqs()
    surahs = build_surahs(per, text)
    print(f"[ok] loaded {len(surahs)} surahs")

    print("[run] sub-test A: word-order chiasmus ...")
    chi = run_chiasmus(surahs)
    print(f"      R_obs={chi['R_obs']:.4f}  null_mean={chi['null_mean_R']:.4f}  "
          f"p={chi['p_one_sided_chiastic']:.4g}  dir={chi['direction_observed']}")
    print("[run] sub-test A triplet (MW-3) ...")
    chi3 = run_chiasmus_triplet(surahs)
    print(f"      triplet R_obs={chi3['R_obs']:.4f} p={chi3['p_one_sided_chiastic']:.4g}")

    print("[run] sub-test B: antithetical density ...")
    anti = run_antithetical(surahs)
    print(f"      dA={anti['density_A']:.4f} dB={anti['density_B']:.4f} "
          f"delta={anti['delta_obs']:+.4f} p={anti['p_one_sided_A_gt_B']:.4g} "
          f"dir={anti['direction_observed']}")

    # verdict
    chi_pass = (chi["R_obs"] > chi["null_mean_R"]) and \
               (chi["p_one_sided_chiastic"] < ALPHA_BON)
    anti_pass = (anti["delta_obs"] > 0) and (anti["p_one_sided_A_gt_B"] < ALPHA_BON)
    if chi_pass and anti_pass:
        verdict = "PASS"
    elif chi_pass or anti_pass:
        verdict = "PARTIAL"
    else:
        verdict = "NULL"

    result = {
        "finding_id": "h-new-2290",
        "prereg_sha256": PREREG_SHA,
        "seed": BASE_SEED, "n_perm": N_PERM,
        "alpha_raw": ALPHA_RAW, "k_bonferroni": K_BON, "alpha_bon": ALPHA_BON,
        "rules_tuple": "(no-tashkeel, QAC v0.4 STEM-ROOT word-order, content-root sequence, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "subtest_A_chiasmus": chi,
        "subtest_A_chiasmus_triplet": chi3,
        "subtest_B_antithetical": anti,
        "chiasmus_pass_alpha_bon": chi_pass,
        "antithetical_pass_alpha_bon": anti_pass,
        "verdict": verdict,
    }
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as fh:
        json.dump(result, fh, ensure_ascii=False, indent=1)
    print(f"[ok] wrote {OUT}")
    print(f"[VERDICT] {verdict}  (chiasmus_pass={chi_pass}, antithetical_pass={anti_pass})")


if __name__ == "__main__":
    main()
