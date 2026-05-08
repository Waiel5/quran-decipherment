#!/usr/bin/env python3
"""
Q026 al-Shuʿarāʾ novel-findings runner — Q026-F-01..F-05.

Pre-reg SHAs locked at top.  fail-fast on mismatch (per INVESTIGATION-PROTOCOL §1.2).

Tests:
  Q026-F-01  7-prophet-refrain-cycle structure
  Q026-F-02  TSM-cluster (Q 26, 27, 28) joint cohesion
  Q026-F-03  Anti-poetry coda lexical distinctness
  Q026-F-04  Moses-Pharaoh twin (Q 26 vs Q 28 vs Q 20)
  Q026-F-05  Verse-length shortness vs corpus + poetry baseline

Outputs JSON to /Users/grey/Downloads/quran/surahs/Q026-al-shuara/csv/.
"""

import json
import hashlib
import math
import os
import random
import sys
import re
from collections import Counter
from itertools import combinations

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q026-F-01": "3a99c8aa3b55f856fba0bc849ed06a50d65d181d19353249fdc06a8babb765f8",
    "Q026-F-02": "8ad5f22dbc800889e6bfedadc136339cc25004f699ac5a982ffeca860e731b6c",
    "Q026-F-03": "c2a39ef90ec770d9932ad2549067fd774b21b9f9e4ee147e9bf687170d8fc4a2",
    "Q026-F-04": "2f5a07f6792215a41ccfbcec7d70ef1e6171e84a6611f56d0f376d14c909d8f4",
    "Q026-F-05": "dce525681887541a802d1ee319a84dc1a30e88c9db17c1667bceb33d678a25a6",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q026-al-shuara")
PREREG_FILES = {
    "Q026-F-01": "Q026-F-01-prophet-refrain-cycle-prereg.md",
    "Q026-F-02": "Q026-F-02-tsm-cluster-cohesion-prereg.md",
    "Q026-F-03": "Q026-F-03-anti-poetry-coda-prereg.md",
    "Q026-F-04": "Q026-F-04-moses-twin-prereg.md",
    "Q026-F-05": "Q026-F-05-verse-shortness-prereg.md",
}

OUT_DIR = os.path.join(BASE, "surahs/Q026-al-shuara/csv")
os.makedirs(OUT_DIR, exist_ok=True)

SEED = 20260507


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_prereg_shas():
    for fid, expected in PREREG_SHAS.items():
        p = os.path.join(PREREG_DIR, PREREG_FILES[fid])
        actual = sha256_file(p)
        if actual != expected:
            sys.stderr.write(f"SHA MISMATCH for {fid}: expected {expected}, got {actual}\n")
            sys.exit(2)
        print(f"[OK] {fid} SHA verified: {actual[:16]}...")


def load_no_tashkeel():
    with open(os.path.join(BASE, "quran-text/quran-no-tashkeel.json")) as f:
        return json.load(f)


# =================================================================
# QAC root loading
# =================================================================

def load_qac_roots():
    """Returns dict (surah, verse, word_idx) -> root.
       Also returns dict (surah, verse) -> [root, ...] (in word order, for words that have roots)."""
    path = os.path.join(BASE, "data/morphology/quranic-corpus-morphology-0.4.txt")
    by_loc = {}
    with open(path, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.strip() == "":
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]  # (s:v:w:p)
            features = parts[3]
            # Extract ROOT:xxx
            m = re.search(r"ROOT:([^|]+)", features)
            if not m:
                continue
            root = m.group(1)
            # Parse loc — strip parens
            loc_clean = loc.strip("()")
            try:
                s, v, w, p = [int(x) for x in loc_clean.split(":")]
            except Exception:
                continue
            # only first segment per word (avoid duplicate roots from suffixes)
            if (s, v, w) not in by_loc:
                by_loc[(s, v, w)] = root
    # build per-verse list
    by_verse = {}
    for (s, v, w), root in by_loc.items():
        by_verse.setdefault((s, v), []).append((w, root))
    for k in by_verse:
        by_verse[k] = [r for _, r in sorted(by_verse[k])]
    return by_verse


# =================================================================
# Q026-F-01 — prophet-refrain cycle
# =================================================================

def run_F01(corpus):
    q26 = corpus[25]
    R1_substr = "أكثرهم مؤمنين"
    R2_substr = "وإن ربك لهو العزيز الرحيم"

    R1_hits_q26 = []
    R2_hits_q26 = []
    for v in q26["verses"]:
        if R1_substr in v["text"]:
            R1_hits_q26.append(v["id"])
        if R2_substr in v["text"]:
            R2_hits_q26.append(v["id"])

    R1_total_corpus = 0
    R2_total_corpus = 0
    R1_outside_q26 = []
    R2_outside_q26 = []
    for s in corpus:
        for v in s["verses"]:
            if R1_substr in v["text"]:
                R1_total_corpus += 1
                if s["id"] != 26:
                    R1_outside_q26.append((s["id"], v["id"]))
            if R2_substr in v["text"]:
                R2_total_corpus += 1
                if s["id"] != 26:
                    R2_outside_q26.append((s["id"], v["id"]))

    # Cycles: cycle 0 = prologue (1..R2[0]); cycle i = (R2[i-1]+1 .. R2[i]); cycle last = (R2[-1]+1..227)
    R2 = R2_hits_q26
    cycles = []
    if R2:
        cycles.append((1, R2[0]))  # cycle 0 = prologue
        for i in range(1, len(R2)):
            cycles.append((R2[i - 1] + 1, R2[i]))
        cycles.append((R2[-1] + 1, q26["total_verses"]))  # coda

    # Prophet cycles = cycles 1..(len-2)
    prophet_cycles = cycles[1:-1] if len(cycles) >= 3 else []

    cycle_lengths = [b - a + 1 for a, b in prophet_cycles]
    n_pc = len(prophet_cycles)

    # Spearman rho between cycle_index (1..n_pc) and cycle_length
    def spearman(x, y):
        # ranks
        def rank(arr):
            sorted_vals = sorted(enumerate(arr), key=lambda t: t[1])
            r = [0] * len(arr)
            for i, (orig_idx, _) in enumerate(sorted_vals, start=1):
                r[orig_idx] = i
            # handle ties (avg-rank)
            from collections import defaultdict
            buckets = defaultdict(list)
            for i, val in enumerate(arr):
                buckets[val].append(i)
            for val, indices in buckets.items():
                if len(indices) > 1:
                    avg_rank = sum(r[i] for i in indices) / len(indices)
                    for i in indices:
                        r[i] = avg_rank
            return r

        rx = rank(x)
        ry = rank(y)
        n = len(x)
        d2 = sum((rx[i] - ry[i]) ** 2 for i in range(n))
        rho = 1 - 6 * d2 / (n * (n * n - 1))
        return rho

    indices = list(range(1, n_pc + 1))
    rho_obs = spearman(indices, cycle_lengths) if n_pc >= 3 else None

    # Permutation null on rho (LOWER tail per pre-reg)
    rng = random.Random(SEED)
    n_perm = 10000
    p_perm_lower = None
    if rho_obs is not None:
        leq = 0
        for _ in range(n_perm):
            shuffled = cycle_lengths[:]
            rng.shuffle(shuffled)
            rho_p = spearman(indices, shuffled)
            if rho_p <= rho_obs:
                leq += 1
        p_perm_lower = (1 + leq) / (1 + n_perm)

    # Direction-locked rho < 0; |rho|>=0.50
    direction_passed = (rho_obs is not None and rho_obs < 0 and abs(rho_obs) >= 0.50 and p_perm_lower < 0.01)
    corpus_unique = (R2_total_corpus == len(R2_hits_q26)) and len(R2_hits_q26) >= 6

    if corpus_unique and direction_passed:
        verdict = "CONFIRMED"
    elif corpus_unique and (rho_obs is not None and rho_obs < 0):
        verdict = "DIRECTIONAL"
    elif corpus_unique:
        verdict = "PARTIAL_CORPUS_UNIQUE_ONLY"
    else:
        verdict = "NULL_OR_VIOLATION"

    out = {
        "finding_id": "Q026-F-01",
        "prereg_sha": PREREG_SHAS["Q026-F-01"],
        "rules_tuple": "(no-tashkeel, orthographic-substring-match, pause-tolerated, Hafs-Kufan, Mashriqi)",
        "method": "substring search for R1/R2; cycle = (R2[i-1]+1..R2[i]); Spearman on prophet-cycles only",
        "R1_substring": R1_substr,
        "R2_substring": R2_substr,
        "R1_hits_q26": R1_hits_q26,
        "R2_hits_q26": R2_hits_q26,
        "R1_total_corpus": R1_total_corpus,
        "R2_total_corpus": R2_total_corpus,
        "R1_outside_q26": R1_outside_q26,
        "R2_outside_q26": R2_outside_q26,
        "cycles_all": cycles,
        "prophet_cycles_only": prophet_cycles,
        "cycle_lengths_prophet": cycle_lengths,
        "n_prophet_cycles": n_pc,
        "spearman_rho_obs": rho_obs,
        "p_perm_one_sided_lower_tail": p_perm_lower,
        "n_perm": n_perm,
        "seed": SEED,
        "R2_corpus_unique_to_Q26": corpus_unique,
        "rho_direction_passed": direction_passed,
        "verdict": verdict,
        "alpha_bonferroni": 0.01,
    }
    return out


# =================================================================
# Q026-F-02 — TSM cluster cohesion
# =================================================================

def run_F02():
    # Load h-new-* artefacts
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-111.json")) as f:
        d111 = json.load(f)
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-750.json")) as f:
        d750 = json.load(f)
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-840.json")) as f:
        d840 = json.load(f)

    N = 114
    D = [[0.0] * (N + 1) for _ in range(N + 1)]
    for a, b, val in d111["D_matrix_upper_triangular"]:
        D[a][b] = val
        D[b][a] = val

    per_surah_750 = {it["surah"]: it for it in d750["per_surah"]}
    per_surah_840 = {it["surah"]: it for it in d840["all_uas"]}

    MUQ_SURAHS = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
                  36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]

    TSM = (26, 27, 28)

    def axis_values(triplet):
        s1, s2, s3 = triplet
        # A1 = mean pairwise FR distance
        a1 = (D[s1][s2] + D[s1][s3] + D[s2][s3]) / 3.0
        # A2 = spread of top_final_letter_frac
        rhymes = [per_surah_750[s]["top_final_letter_frac"] for s in (s1, s2, s3)]
        a2 = max(rhymes) - min(rhymes)
        # A3 = spread of sig_A
        sigs = [per_surah_750[s]["sig_A"] for s in (s1, s2, s3)]
        a3 = max(sigs) - min(sigs)
        # A4 = spread of UAS
        uas = [per_surah_840[s]["UAS"] for s in (s1, s2, s3)]
        a4 = max(uas) - min(uas)
        return a1, a2, a3, a4

    obs = axis_values(TSM)

    # Enumerate all C(29,3) muqaṭṭaʿ triplets
    all_triplets = list(combinations(MUQ_SURAHS, 3))
    A1, A2, A3, A4 = [], [], [], []
    for trip in all_triplets:
        v = axis_values(trip)
        A1.append(v[0])
        A2.append(v[1])
        A3.append(v[2])
        A4.append(v[3])

    def percentile_rank(obs_v, all_v):
        # returns fraction of values <= obs_v (lower = more cohesive => low percentile)
        n = len(all_v)
        leq = sum(1 for x in all_v if x <= obs_v)
        return leq / n

    pcts = [
        percentile_rank(obs[0], A1),
        percentile_rank(obs[1], A2),
        percentile_rank(obs[2], A3),
        percentile_rank(obs[3], A4),
    ]
    axis_names = ["A1_mean_FR", "A2_rhyme_spread", "A3_sigA_spread", "A4_UAS_spread"]

    # CONFIRMED if >= 3 axes pct <= 0.05
    n_pass = sum(1 for p in pcts if p <= 0.05)
    n_violate = sum(1 for p in pcts if p >= 0.95)

    if n_pass >= 3:
        verdict = "CONFIRMED"
    elif n_pass == 2:
        verdict = "DIRECTIONAL"
    elif n_violate >= 2:
        verdict = "PRE_COMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "Q026-F-02",
        "prereg_sha": PREREG_SHAS["Q026-F-02"],
        "rules_tuple": "(h-new-111 FR-roots, h-new-750 sig_A/rhyme, h-new-840 UAS)",
        "method": "TSM (26,27,28) pct-rank vs C(29,3) muqaṭṭaʿ triplets on 4 axes; lower=more cohesive",
        "TSM_triplet": list(TSM),
        "n_muqattaʿ_surahs": len(MUQ_SURAHS),
        "n_triplets_enumerated": len(all_triplets),
        "axis_values_TSM": dict(zip(axis_names, obs)),
        "percentile_TSM_per_axis": dict(zip(axis_names, pcts)),
        "n_axes_passing_top5pct": n_pass,
        "n_axes_violating_bottom5pct": n_violate,
        "alpha_bonferroni_per_axis": 0.0125,
        "alpha_family": 0.01,
        "verdict": verdict,
        "axis_means_over_triplets": {
            "A1_mean_FR_mean": sum(A1) / len(A1),
            "A1_mean_FR_min": min(A1),
            "A1_mean_FR_max": max(A1),
            "A2_rhyme_spread_mean": sum(A2) / len(A2),
            "A3_sigA_spread_mean": sum(A3) / len(A3),
            "A4_UAS_spread_mean": sum(A4) / len(A4),
        },
    }
    return out


# =================================================================
# Q026-F-03 — anti-poetry coda lexical distinctness
# =================================================================

def run_F03(corpus, qac_by_verse):
    q26 = corpus[25]
    n_verses = q26["total_verses"]  # 227

    # Verse -> root list
    verse_roots = {}
    for v in q26["verses"]:
        vid = v["id"]
        verse_roots[vid] = list(qac_by_verse.get((26, vid), []))

    # Surah-mean TF
    surah_tf = Counter()
    for vid in range(1, n_verses + 1):
        for r in verse_roots.get(vid, []):
            surah_tf[r] += 1
    total_surah_tokens = sum(surah_tf.values())

    # Build window 4-verse TF
    def window_tf(start_vid):
        c = Counter()
        for k in range(4):
            for r in verse_roots.get(start_vid + k, []):
                c[r] += 1
        return c

    # Cosine distance with Laplace smoothing on surah_tf
    # smoothed surah probabilities: (n_r + alpha) / (T + alpha * |V|)
    alpha = 1.0
    vocab = set(surah_tf.keys())  # tokens that appear at least once in surah
    # also include any window tokens (but they're a subset)
    V = len(vocab)

    def cos_dist(window_c):
        # Build vector over union of vocab and window keys
        all_keys = vocab.union(window_c.keys())
        # surah probs (smoothed)
        surah_probs = {}
        denom_s = total_surah_tokens + alpha * len(all_keys)
        for k in all_keys:
            surah_probs[k] = (surah_tf.get(k, 0) + alpha) / denom_s
        # window probs (raw)
        wt = sum(window_c.values())
        if wt == 0:
            return 1.0
        win_probs = {k: window_c.get(k, 0) / wt for k in all_keys}
        # cosine
        dot = sum(surah_probs[k] * win_probs[k] for k in all_keys)
        ns = math.sqrt(sum(surah_probs[k] ** 2 for k in all_keys))
        nw = math.sqrt(sum(win_probs[k] ** 2 for k in all_keys))
        if ns == 0 or nw == 0:
            return 1.0
        return 1.0 - dot / (ns * nw)

    n_windows = n_verses - 3  # 4-verse windows starting at v 1..224
    distances = []
    for start in range(1, n_windows + 1):
        wc = window_tf(start)
        d = cos_dist(wc)
        distances.append((start, d))
    distances.sort(key=lambda x: -x[1])  # rank 1 = max distinct
    coda_start = n_windows  # last window starts at v 224 → exactly v 224-227
    rank_coda = next(i + 1 for i, (s, _) in enumerate(distances) if s == coda_start)
    coda_dist = next(d for s, d in distances if s == coda_start)

    # Permutation null: shuffle root-tokens to verses preserving verse-token-counts
    # Pool all root tokens; per perm, redistribute to verses by their original counts.
    pool = []
    verse_token_counts = {}
    for vid in range(1, n_verses + 1):
        rs = verse_roots.get(vid, [])
        verse_token_counts[vid] = len(rs)
        pool.extend(rs)
    rng = random.Random(SEED)
    n_perm = 10000
    coda_rank_top1 = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        # rebuild verse -> tokens
        idx = 0
        v_tokens = {}
        for vid in range(1, n_verses + 1):
            cnt = verse_token_counts[vid]
            v_tokens[vid] = pool[idx:idx + cnt]
            idx += cnt
        # window dist for each
        # NB: surah_tf doesn't change under permutation (same total counts),
        # so surah_probs are identical. Only window_tf changes.
        max_d = -1.0
        coda_d = None
        for start in range(1, n_windows + 1):
            wc = Counter()
            for k in range(4):
                for r in v_tokens[start + k]:
                    wc[r] += 1
            d = cos_dist(wc)
            if start == coda_start:
                coda_d = d
            if d > max_d:
                max_d = d
        if coda_d == max_d:
            coda_rank_top1 += 1
    p_perm = (1 + coda_rank_top1) / (1 + n_perm)

    direction_passed = (rank_coda == 1 and p_perm < 0.01)
    if direction_passed:
        verdict = "CONFIRMED"
    elif rank_coda <= 5 and p_perm < 0.05:
        verdict = "DIRECTIONAL"
    elif rank_coda > 200:
        verdict = "PRE_COMMIT_VIOLATION"
    else:
        verdict = "NULL_OR_PARTIAL"

    out = {
        "finding_id": "Q026-F-03",
        "prereg_sha": PREREG_SHAS["Q026-F-03"],
        "rules_tuple": "(no-tashkeel, QAC-stem-roots, sliding-4-verse-windows)",
        "method": "Cosine distance per 4-verse window vs surah-mean (Laplace +1); rank coda among 224 windows",
        "n_windows": n_windows,
        "coda_window_start_verse": coda_start,
        "coda_distance_from_mean": coda_dist,
        "rank_coda": rank_coda,
        "max_distance": distances[0][1],
        "max_distance_window_start": distances[0][0],
        "top_5_distinct_windows": [(s, d) for s, d in distances[:5]],
        "p_perm_one_sided_top1": p_perm,
        "n_perm": n_perm,
        "seed": SEED,
        "alpha_bonferroni": 0.01,
        "verdict": verdict,
    }
    return out


# =================================================================
# Q026-F-04 — Moses-Pharaoh twin
# =================================================================

def run_F04(corpus, qac_by_verse):
    # Block boundaries
    M26 = (26, 10, 67)
    M28 = (28, 3, 43)
    M20 = (20, 9, 79)

    def block_tf(s, a, b):
        c = Counter()
        for vid in range(a, b + 1):
            for r in qac_by_verse.get((s, vid), []):
                c[r] += 1
        return c

    tf26 = block_tf(*M26)
    tf28 = block_tf(*M28)
    tf20 = block_tf(*M20)

    def cos_dist(c1, c2):
        keys = set(c1.keys()).union(c2.keys())
        n1 = sum(c1.values())
        n2 = sum(c2.values())
        if n1 == 0 or n2 == 0:
            return 1.0
        v1 = [c1.get(k, 0) / n1 for k in keys]
        v2 = [c2.get(k, 0) / n2 for k in keys]
        dot = sum(a * b for a, b in zip(v1, v2))
        n_v1 = math.sqrt(sum(a * a for a in v1))
        n_v2 = math.sqrt(sum(a * a for a in v2))
        return 1.0 - dot / (n_v1 * n_v2)

    d_TSM = cos_dist(tf26, tf28)  # 26-28 (predicted closest)
    d_HEAD_26 = cos_dist(tf26, tf20)  # 26-20
    d_HEAD_28 = cos_dist(tf28, tf20)  # 28-20

    margin = min(d_HEAD_26, d_HEAD_28) - d_TSM  # >0 means TSM-pair closer

    # Permutation null: pool all root-tokens from M26 + M28 + M20, randomly partition into 3 blocks
    # of sizes (|M26|, |M28|, |M20|), recompute margin.
    pool = []
    sizes = [sum(tf26.values()), sum(tf28.values()), sum(tf20.values())]
    for c, s in zip([tf26, tf28, tf20], sizes):
        for r, n in c.items():
            pool.extend([r] * n)
    rng = random.Random(SEED)
    n_perm = 10000
    geq = 0
    for _ in range(n_perm):
        rng.shuffle(pool)
        idx = 0
        cs = []
        for sz in sizes:
            cs.append(Counter(pool[idx:idx + sz]))
            idx += sz
        d_a = cos_dist(cs[0], cs[1])
        d_b = cos_dist(cs[0], cs[2])
        d_c = cos_dist(cs[1], cs[2])
        # margin in same configuration: c[0] = M26, c[1] = M28 (TSM pair), c[2] = M20
        m = min(d_b, d_c) - d_a
        if m >= margin:
            geq += 1
    p_perm = (1 + geq) / (1 + n_perm)

    direction_passed = (margin > 0 and p_perm < 0.01)
    if direction_passed:
        verdict = "CONFIRMED"
    elif margin > 0 and p_perm < 0.05:
        verdict = "DIRECTIONAL"
    elif margin <= 0:
        verdict = "NULL_OR_VIOLATION"
    else:
        verdict = "NULL"

    # Also report whole-surah FR-distances for context
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-111.json")) as f:
        d111 = json.load(f)
    D = {}
    for a, b, val in d111["D_matrix_upper_triangular"]:
        D[(a, b)] = val
        D[(b, a)] = val

    out = {
        "finding_id": "Q026-F-04",
        "prereg_sha": PREREG_SHAS["Q026-F-04"],
        "rules_tuple": "(no-tashkeel, QAC-stem-roots, length-normalized-TF)",
        "method": "Cosine distance on 3 Moses-narrative blocks; permutation by 3-way root-token partition",
        "blocks": {
            "M26 (Q26 vv 10-67, ṬSM)": {"surah": 26, "v_start": 10, "v_end": 67, "n_root_tokens": sum(tf26.values())},
            "M28 (Q28 vv 3-43, ṬSM)": {"surah": 28, "v_start": 3, "v_end": 43, "n_root_tokens": sum(tf28.values())},
            "M20 (Q20 vv 9-79, ṬH)": {"surah": 20, "v_start": 9, "v_end": 79, "n_root_tokens": sum(tf20.values())},
        },
        "block_distances_root_cosine": {
            "d_M26_M28": d_TSM,
            "d_M26_M20": d_HEAD_26,
            "d_M28_M20": d_HEAD_28,
        },
        "margin": margin,
        "TSM_pair_closest": (d_TSM < d_HEAD_26 and d_TSM < d_HEAD_28),
        "p_perm_one_sided_upper": p_perm,
        "n_perm": n_perm,
        "seed": SEED,
        "alpha_bonferroni": 0.01,
        "verdict": verdict,
        "context_whole_surah_FR_distances": {
            "d_Q26_Q28": D[(26, 28)],
            "d_Q26_Q20": D[(26, 20)],
            "d_Q28_Q20": D[(28, 20)],
        },
    }
    return out


# =================================================================
# Q026-F-05 — verse-length shortness
# =================================================================

def run_F05(corpus):
    # Q 26 mean tokens per verse (with v1)
    q26 = corpus[25]
    tokens_per_verse_q26 = [len(v["text"].split()) for v in q26["verses"]]
    mean_tpv_q26 = sum(tokens_per_verse_q26) / len(tokens_per_verse_q26)
    mean_tpv_q26_no_v1 = sum(tokens_per_verse_q26[1:]) / (len(tokens_per_verse_q26) - 1)

    # Per-surah means
    per_surah_means = []
    for s in corpus:
        toks = sum(len(v["text"].split()) for v in s["verses"])
        per_surah_means.append({"surah": s["id"], "mean_tpv": toks / s["total_verses"], "n_verses": s["total_verses"], "n_tokens": toks})

    # Rank Q26
    sorted_means = sorted(per_surah_means, key=lambda x: x["mean_tpv"])
    rank_q26 = next(i + 1 for i, item in enumerate(sorted_means) if item["surah"] == 26)

    # Corpus mean (token-weighted)
    total_tokens = sum(item["n_tokens"] for item in per_surah_means)
    total_verses = sum(item["n_verses"] for item in per_surah_means)
    corpus_mean_tpv = total_tokens / total_verses

    # Surah-mean SD
    surah_means_arr = [item["mean_tpv"] for item in per_surah_means]
    surah_mean_avg = sum(surah_means_arr) / len(surah_means_arr)
    surah_mean_sd = math.sqrt(sum((x - surah_mean_avg) ** 2 for x in surah_means_arr) / len(surah_means_arr))
    z_q26_corpus = (mean_tpv_q26 - surah_mean_avg) / surah_mean_sd

    # Permutation null over rank
    rng = random.Random(SEED)
    n_perm = 10000
    leq = 0
    # Build per-surah verse counts and token counts; permute token assignment via shuffling surah_tokens to surah_verse_counts
    surah_verse_counts = [item["n_verses"] for item in per_surah_means]
    surah_token_counts = [item["n_tokens"] for item in per_surah_means]
    # Find Q26 idx
    q26_idx = next(i for i, item in enumerate(per_surah_means) if item["surah"] == 26)
    for _ in range(n_perm):
        shuffled_tokens = surah_token_counts[:]
        rng.shuffle(shuffled_tokens)
        means_perm = [shuffled_tokens[i] / surah_verse_counts[i] for i in range(114)]
        # rank of permuted Q26 mean
        q26_perm_mean = means_perm[q26_idx]
        rank_perm = sum(1 for x in means_perm if x <= q26_perm_mean)
        if rank_perm <= rank_q26:
            leq += 1
    p_perm_rank = (1 + leq) / (1 + n_perm)

    # Poetry baseline from al-Muʿallaqāt — use baseline-stats.csv tokens / lines
    # Lines = count newlines in raw text
    poetry_means = []
    poetry_dir = os.path.join(BASE, "data/baseline-corpora/raw")
    muallaqa_files = [
        "muallaqa-amr-bin-kulthum.raw.txt",
        "muallaqa-antara.raw.txt",
        "muallaqa-harith.raw.txt",
        "muallaqa-imru-al-qais.raw.txt",
        "muallaqa-labid.raw.txt",
        "muallaqa-tarafa.raw.txt",
        "muallaqa-zuhayr.raw.txt",
    ]
    poetry_data = []
    for fn in muallaqa_files:
        path = os.path.join(poetry_dir, fn)
        if not os.path.exists(path):
            continue
        with open(path, encoding="utf-8") as f:
            txt = f.read()
        lines = [l for l in txt.split("\n") if l.strip()]
        # Count tokens (ws-split) per line
        line_tpv = [len(l.split()) for l in lines]
        if not line_tpv:
            continue
        # Hemistich approximation: many poetry lines contain both hemistichs separated by tab or wide space.
        # For conservative comparison, we use FULL-LINE token count (which is full bayt = 2 hemistichs).
        # Then we ALSO compute hemistich mean = full_mean / 2.
        m_full = sum(line_tpv) / len(line_tpv)
        poetry_data.append({
            "file": fn,
            "n_lines": len(lines),
            "mean_tokens_per_full_line": m_full,
            "mean_tokens_per_hemistich_estimate": m_full / 2.0,
        })
        poetry_means.append(m_full)
    if poetry_means:
        poetry_mean_full = sum(poetry_means) / len(poetry_means)
        poetry_mean_hemistich = poetry_mean_full / 2.0
        sd = math.sqrt(sum((x - poetry_mean_full) ** 2 for x in poetry_means) / len(poetry_means)) if len(poetry_means) > 1 else 0.0
        z_q26_poetry_full = (mean_tpv_q26 - poetry_mean_full) / sd if sd > 0 else None
        # Use hemistich for direct comparison since one Quran-verse ≈ one hemistich length
        sd_hem = sd / 2.0
        z_q26_poetry_hem = (mean_tpv_q26 - poetry_mean_hemistich) / sd_hem if sd_hem > 0 else None
    else:
        poetry_mean_full = None
        poetry_mean_hemistich = None
        z_q26_poetry_full = None
        z_q26_poetry_hem = None

    # H1.a passes: rank_q26 <= 57 AND z_q26_corpus < 0
    h1a_pass = (rank_q26 <= 57 and z_q26_corpus < 0 and p_perm_rank < 0.01)
    # H1.b passes: |z_q26_poetry_hem| > 1.0 AND poetry MEAN > Q26 (poetry longer)
    h1b_pass = False
    if poetry_mean_hemistich is not None and z_q26_poetry_hem is not None:
        h1b_pass = (mean_tpv_q26 < poetry_mean_hemistich and abs(z_q26_poetry_hem) > 1.0)

    if h1a_pass and h1b_pass:
        verdict = "CONFIRMED"
    elif h1a_pass or h1b_pass:
        verdict = "DIRECTIONAL"
    elif rank_q26 > 90:
        verdict = "PRE_COMMIT_VIOLATION"
    else:
        verdict = "NULL"

    out = {
        "finding_id": "Q026-F-05",
        "prereg_sha": PREREG_SHAS["Q026-F-05"],
        "rules_tuple": "(no-tashkeel, orthographic-token-ws-split, no-pause-strip)",
        "method": "Q26 mean tokens-per-verse vs corpus and pre-Islamic poetry (al-Muʿallaqāt) baseline",
        "Q26_mean_tpv_with_v1": mean_tpv_q26,
        "Q26_mean_tpv_without_muqattaa_v1": mean_tpv_q26_no_v1,
        "Q26_n_verses": len(tokens_per_verse_q26),
        "Q26_total_tokens": sum(tokens_per_verse_q26),
        "rank_q26_among_114": rank_q26,
        "rank_quintile": "shortest" if rank_q26 <= 22 else ("short" if rank_q26 <= 45 else ("median" if rank_q26 <= 68 else ("long" if rank_q26 <= 91 else "longest"))),
        "corpus_token_weighted_mean_tpv": corpus_mean_tpv,
        "surah_mean_avg_tpv": surah_mean_avg,
        "surah_mean_sd_tpv": surah_mean_sd,
        "z_q26_corpus": z_q26_corpus,
        "p_perm_rank": p_perm_rank,
        "n_perm": n_perm,
        "seed": SEED,
        "poetry_baseline": {
            "n_files": len(poetry_means),
            "per_file": poetry_data,
            "mean_tokens_per_full_line_avg": poetry_mean_full,
            "mean_tokens_per_hemistich_estimate_avg": poetry_mean_hemistich,
            "z_q26_vs_poetry_full_line": z_q26_poetry_full,
            "z_q26_vs_poetry_hemistich": z_q26_poetry_hem,
        },
        "h1a_corpus_short_passed": h1a_pass,
        "h1b_poetry_distinct_passed": h1b_pass,
        "alpha_bonferroni": 0.01,
        "verdict": verdict,
    }
    return out


# =================================================================
# Main
# =================================================================

def main():
    print("=" * 60)
    print("Q026 al-Shuʿarāʾ novel-findings runner")
    print("=" * 60)
    verify_prereg_shas()

    print("\nLoading corpus + QAC...")
    corpus = load_no_tashkeel()
    qac_by_verse = load_qac_roots()
    print(f"  loaded {len(corpus)} surahs, {len(qac_by_verse)} verse-roots")

    print("\nRunning Q026-F-01 (prophet-refrain cycle)...")
    out01 = run_F01(corpus)
    p = os.path.join(OUT_DIR, "Q026-F-01.json")
    with open(p, "w") as f:
        json.dump(out01, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out01['verdict']}")

    print("\nRunning Q026-F-02 (TSM-cluster cohesion)...")
    out02 = run_F02()
    p = os.path.join(OUT_DIR, "Q026-F-02.json")
    with open(p, "w") as f:
        json.dump(out02, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out02['verdict']}")

    print("\nRunning Q026-F-03 (anti-poetry coda distinctness)...")
    out03 = run_F03(corpus, qac_by_verse)
    p = os.path.join(OUT_DIR, "Q026-F-03.json")
    with open(p, "w") as f:
        json.dump(out03, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out03['verdict']}")

    print("\nRunning Q026-F-04 (Moses-Pharaoh twin)...")
    out04 = run_F04(corpus, qac_by_verse)
    p = os.path.join(OUT_DIR, "Q026-F-04.json")
    with open(p, "w") as f:
        json.dump(out04, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out04['verdict']}")

    print("\nRunning Q026-F-05 (verse-length shortness)...")
    out05 = run_F05(corpus)
    p = os.path.join(OUT_DIR, "Q026-F-05.json")
    with open(p, "w") as f:
        json.dump(out05, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out05['verdict']}")

    print("\nAll Q026 novel-findings tests complete.")


if __name__ == "__main__":
    main()
