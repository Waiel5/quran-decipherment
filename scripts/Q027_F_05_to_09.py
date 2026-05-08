#!/usr/bin/env python3
"""
Q027 al-Naml NEW novel-findings runner — Q027-F-05..F-09.

Pre-reg SHAs locked at top.  fail-fast on mismatch (per INVESTIGATION-PROTOCOL §1.2).

Tests:
  Q027-F-05  Second-basmala STRUCTURAL ROLE (verbatim uniqueness; window distinctiveness;
             embedded-quotative-divine-name extension)
  Q027-F-06  Hud-hud narrative (Q 27:20-28) lexical isolation; hapax inventory
  Q027-F-07  2-letter muqaṭṭaʿ family {Q 20 ṬH, Q 27 ṬS, Q 36 YS} joint cohesion vs random 3-tuples
  Q027-F-08  Solomon-narrative twin pair: Q 27 ↔ Q 34 vs Q 27 ↔ Q 38
  Q027-F-09  Ant-of-Solomon (Q 27:18) verse-level hapax + distinctiveness

Outputs JSON to /Users/grey/Downloads/quran/surahs/Q027-al-naml/csv/.
Discipline: seed 20260507; 10000 perms (where applicable); Bonferroni k=5, alpha_bon=0.01.
"""

import json
import hashlib
import math
import os
import random
import sys
from collections import Counter
from itertools import combinations

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q027-F-05": "f91bcf50d15d191009f429d7a34a542132e8f74b57bb0b56dd754ce891c70344",
    "Q027-F-06": "bcfaed030d0ef6d63f5fd01b154307ca1696495cfa2c4addb4a150ae4aa00469",
    "Q027-F-07": "d67a2635549de3077a8a0c75aa7aba7bd5fd7da0f3d66af60e2465319a1a32b3",
    "Q027-F-08": "7dd3e7ab8649fda6fd756a83f8238551431a483c86309ae8cebe29c43144becb",
    "Q027-F-09": "698ce38531228d1d10d50a11874ce9b5d840f984aeb267c563e823863bb5b715",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q027-al-naml")
PREREG_FILES = {
    "Q027-F-05": "Q027-F-05-second-basmala-structural-role-prereg.md",
    "Q027-F-06": "Q027-F-06-hudhud-narrative-lexical-isolation-prereg.md",
    "Q027-F-07": "Q027-F-07-2letter-muqattaat-family-prereg.md",
    "Q027-F-08": "Q027-F-08-solomon-narrative-twin-prereg.md",
    "Q027-F-09": "Q027-F-09-ant-narrative-verse-hapax-prereg.md",
}

OUT_DIR = os.path.join(BASE, "surahs/Q027-al-naml/csv")
os.makedirs(OUT_DIR, exist_ok=True)

SEED = 20260507
N_PERM = 10000
BONFERRONI_K = 5
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.01

# 29 muqaṭṭaʿāt-opened surahs (al-Suyūṭī al-Itqān nawʿ 43)
MUQATTAAT_29 = [2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29,
                30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68]


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
            sys.stderr.write(f"FAIL-FAST per protocol §1.2\n")
            sys.exit(2)
        print(f"[OK] {fid} SHA verified: {actual[:16]}...")


# ---------- corpus loaders ----------

def load_no_tashkeel():
    with open(os.path.join(BASE, "quran-text/quran-no-tashkeel.json")) as f:
        return json.load(f)


def load_qac_roots_per_verse():
    """Parse QAC v0.4 morphology to map (sura, verse) -> set of roots and stem-roots."""
    qac_path = os.path.join(BASE, "data/morphology/quranic-corpus-morphology-0.4.txt")
    per_verse = {}  # (s, v) -> set of roots (stems only)
    with open(qac_path) as f:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#"):
                continue
            parts = line.split("\t")
            if len(parts) < 4:
                continue
            loc = parts[0]  # (s:v:w:seg)
            tag = parts[2] if len(parts) > 2 else ""
            features = parts[3] if len(parts) > 3 else ""
            # Parse location (s:v:w:seg)
            try:
                loc_clean = loc.strip("()")
                s_str, v_str, w_str, seg_str = loc_clean.split(":")
                s, v = int(s_str), int(v_str)
            except Exception:
                continue
            # Extract ROOT tag from features
            root = None
            for feat in features.split("|"):
                if feat.startswith("ROOT:"):
                    root = feat[5:]
                    break
            if root:
                per_verse.setdefault((s, v), set()).add(root)
    return per_verse


# ---------- Q027-F-05: second-basmala STRUCTURAL ROLE ----------

def run_F05(corpus, qac_roots):
    out = {
        "finding_id": "Q027-F-05",
        "prereg_sha": PREREG_SHAS["Q027-F-05"],
        "rules_tuple": "(no-tashkeel, orthographic-substring + QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "method": "verbatim-substring + window-Jaccard + extended-quotative substring",
        "seed": SEED,
        "n_perm": "deterministic for H1.a/H1.c; rank-percentile over corpus 5-windows for H1.b",
    }

    # ---- H1.a: verbatim 6-token basmala substring search ----
    target6 = "بسم الله الرحمن الرحيم"
    h1a_hits = []
    for s in corpus:
        sid = s["id"]
        for v in s["verses"]:
            if target6 in v["text"]:
                h1a_hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    h1a_count = len(h1a_hits)
    h1a_pass = (h1a_count == 2)
    out["H1a_verbatim_basmala_count"] = h1a_count
    out["H1a_hits"] = h1a_hits
    out["H1a_pass"] = h1a_pass

    # ---- H1.c: extended quotative-divine-name substring search ----
    target_short = "بسم الله"
    h1c_hits = []
    for s in corpus:
        sid = s["id"]
        for v in s["verses"]:
            if target_short in v["text"]:
                h1c_hits.append({"surah": sid, "verse": v["id"], "text": v["text"]})
    h1c_count = len(h1c_hits)
    h1c_pass = (h1c_count <= 4)
    out["H1c_quotative_basmala_count"] = h1c_count
    out["H1c_hits"] = h1c_hits
    out["H1c_pass"] = h1c_pass

    # ---- H1.b: 5-verse window distinctiveness, Q 27:28-32 ----
    # Build per-surah verse->roots mapping
    target_window_verses = [(27, v) for v in [28, 29, 30, 31, 32]]
    target_roots = set()
    for sv in target_window_verses:
        target_roots.update(qac_roots.get(sv, set()))

    # Build all 5-verse windows
    all_windows = []
    for s in corpus:
        sid = s["id"]
        verse_ids = [v["id"] for v in s["verses"]]
        for k in range(len(verse_ids) - 4):
            window_ids = verse_ids[k:k+5]
            all_windows.append((sid, tuple(window_ids)))

    # Compute Jaccard for target window vs (corpus minus target window)
    def jaccard_block_vs_complement(block_verses, full_corpus_roots):
        block_roots = set()
        for sv in block_verses:
            block_roots.update(qac_roots.get(sv, set()))
        complement_roots = full_corpus_roots - block_roots
        union = block_roots | complement_roots
        inter = block_roots & complement_roots
        return (len(inter) / len(union)) if union else 0.0, len(block_roots), len(complement_roots)

    # full corpus roots
    full_corpus_roots = set()
    for sv_roots in qac_roots.values():
        full_corpus_roots.update(sv_roots)

    target_jacc, _, _ = jaccard_block_vs_complement(target_window_verses, full_corpus_roots)

    # Compute Jaccard for ALL windows
    window_scores = []
    for sid, window_ids in all_windows:
        block_verses = [(sid, v) for v in window_ids]
        j, _, _ = jaccard_block_vs_complement(block_verses, full_corpus_roots)
        window_scores.append((sid, window_ids, j))

    # Rank target window's Jaccard (lower = MORE distinctive — block is more disjoint from rest)
    sorted_scores = sorted(window_scores, key=lambda x: x[2])
    # find target window's rank
    target_idx = None
    for i, ws in enumerate(sorted_scores):
        if ws[0] == 27 and tuple(ws[1]) == (28, 29, 30, 31, 32):
            target_idx = i
            break
    target_pct_lower_tail = (target_idx + 1) / len(sorted_scores) * 100 if target_idx is not None else None
    h1b_pass = (target_pct_lower_tail is not None and target_pct_lower_tail <= 30)
    out["H1b_target_jaccard"] = target_jacc
    out["H1b_target_window_index_in_sorted"] = target_idx
    out["H1b_target_lower_tail_percentile"] = target_pct_lower_tail
    out["H1b_n_windows"] = len(window_scores)
    out["H1b_pass"] = h1b_pass

    # Aggregate verdict
    n_pass = int(h1a_pass) + int(h1b_pass) + int(h1c_pass)
    if n_pass == 3:
        verdict = "CONFIRMED"
    elif n_pass == 2:
        verdict = "DIRECTIONAL"
    elif n_pass == 1:
        verdict = "MIXED"
    else:
        verdict = "NULL"
    if h1a_count != 2:
        verdict = f"PRE-COMMIT-VIOLATION (H1.a count={h1a_count}, expected 2)"
    out["verdict"] = verdict
    out["n_pass_of_3"] = n_pass
    out["bonferroni_k"] = BONFERRONI_K
    out["alpha_bon"] = ALPHA_BON
    return out


# ---------- Q027-F-06: hud-hud narrative lexical isolation ----------

def run_F06(corpus, qac_roots):
    out = {
        "finding_id": "Q027-F-06",
        "prereg_sha": PREREG_SHAS["Q027-F-06"],
        "rules_tuple": "(no-tashkeel, orthographic-exact-match for tokens; QAC-stem-roots for Jaccard, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "seed": SEED,
    }

    # corpus-wide token-frequency (orthographic exact match)
    token_count = Counter()
    for s in corpus:
        for v in s["verses"]:
            for tk in v["text"].split():
                token_count[tk] += 1

    # H1.a — locked candidate hud-hud-block tokens
    hudhud_locked = ["الهدهد", "عرشها", "الخبء", "سبإ", "بنبإ",
                     "لأذبحنه", "لأعذبنه", "الصرح", "بكتابي"]
    hudhud_corpus_counts = {t: token_count.get(t, 0) for t in hudhud_locked}
    hudhud_hapax = [t for t, c in hudhud_corpus_counts.items() if c == 1]
    stat_a = len(hudhud_hapax)
    h1a_pass = (stat_a >= 2)
    out["H1a_locked_tokens"] = hudhud_locked
    out["H1a_token_corpus_counts"] = hudhud_corpus_counts
    out["H1a_hapax_count"] = stat_a
    out["H1a_hapax_tokens"] = hudhud_hapax
    out["H1a_pass"] = h1a_pass

    # H1.b — block-vs-rest-of-Q-27 Jaccard
    block_verses = [(27, v) for v in range(20, 29)]  # 20..28 inclusive
    block_roots = set()
    for sv in block_verses:
        block_roots.update(qac_roots.get(sv, set()))

    # Q 27 minus block
    q27_complement_verses = [(27, v) for v in range(1, 94) if v < 20 or v > 28]
    q27_complement_roots = set()
    for sv in q27_complement_verses:
        q27_complement_roots.update(qac_roots.get(sv, set()))

    inter = block_roots & q27_complement_roots
    union = block_roots | q27_complement_roots
    target_jacc = len(inter) / len(union) if union else 0.0

    # Build all 9-verse contiguous blocks of Q 27 and compute Jaccard each vs Q 27 minus block
    block_jacs = []
    for k in range(1, 94 - 9 + 2):  # k=1..85, block = [k..k+8]
        bv = [(27, v) for v in range(k, k + 9)]
        b_roots = set()
        for sv in bv:
            b_roots.update(qac_roots.get(sv, set()))
        cv = [(27, v) for v in range(1, 94) if v < k or v > k + 8]
        c_roots = set()
        for sv in cv:
            c_roots.update(qac_roots.get(sv, set()))
        u = b_roots | c_roots
        i = b_roots & c_roots
        j = len(i) / len(u) if u else 0.0
        block_jacs.append((k, j))

    sorted_blocks = sorted(block_jacs, key=lambda x: x[1])
    target_block_rank = None
    for i, (k, j) in enumerate(sorted_blocks):
        if k == 20:
            target_block_rank = i + 1
            break
    pct_lower = (target_block_rank / len(block_jacs) * 100) if target_block_rank else None
    h1b_pass = (pct_lower is not None and pct_lower <= 50)
    out["H1b_target_block_jaccard"] = target_jacc
    out["H1b_n_q27_9blocks"] = len(block_jacs)
    out["H1b_target_block_rank"] = target_block_rank
    out["H1b_target_block_pct_lower_tail"] = pct_lower
    out["H1b_pass"] = h1b_pass

    # H1.c — Q 12 wolf-block hapax count
    wolf_locked = ["الذئب", "يأكله"]
    wolf_corpus_counts = {t: token_count.get(t, 0) for t in wolf_locked}
    wolf_hapax = [t for t, c in wolf_corpus_counts.items() if c == 1]
    stat_c = stat_a - len(wolf_hapax)
    h1c_pass = (stat_c > 0)
    out["H1c_wolf_locked_tokens"] = wolf_locked
    out["H1c_wolf_corpus_counts"] = wolf_corpus_counts
    out["H1c_wolf_hapax_count"] = len(wolf_hapax)
    out["H1c_hudhud_minus_wolf"] = stat_c
    out["H1c_pass"] = h1c_pass

    # Aggregate
    n_pass = int(h1a_pass) + int(h1b_pass) + int(h1c_pass)
    if n_pass == 3:
        verdict = "CONFIRMED"
    elif n_pass == 2:
        verdict = "DIRECTIONAL"
    elif n_pass == 1:
        verdict = "MIXED"
    else:
        verdict = "NULL"
    out["verdict"] = verdict
    out["n_pass_of_3"] = n_pass
    out["bonferroni_k"] = BONFERRONI_K
    out["alpha_bon"] = ALPHA_BON
    return out


# ---------- Q027-F-07: 2-letter muqaṭṭaʿ family joint cohesion ----------

def run_F07():
    out = {
        "finding_id": "Q027-F-07",
        "prereg_sha": PREREG_SHAS["Q027-F-07"],
        "rules_tuple": "(no-tashkeel, FR-roots from h-new-111 D-matrix; sig_A from h-new-750; UAS from h-new-840; rhyme top-letter from h-new-700; Hafs-Kufan)",
        "seed": SEED,
    }

    # Load FR D-matrix
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-111.json")) as f:
        fr = json.load(f)
    D = {}
    for entry in fr["D_matrix_upper_triangular"]:
        i, j, d = entry
        D[(i, j)] = d
        D[(j, i)] = d
    def fr_dist(a, b):
        if a == b:
            return 0.0
        return D.get((a, b), None)

    # Load h-new-750 sig_A per surah (canonical schema: per_surah list)
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-750.json")) as f:
        h750 = json.load(f)
    sig_A_per_surah = {}
    rhyme_top_per_surah = {}
    for entry in h750.get("per_surah", []):
        sid = int(entry["surah"])
        sig_A_per_surah[sid] = entry.get("sig_A")
        rhyme_top_per_surah[sid] = entry.get("top_final_letter")

    # Load h-new-840 UAS per surah (canonical schema: all_uas list)
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-840.json")) as f:
        h840 = json.load(f)
    uas_per_surah = {}
    for entry in h840.get("all_uas", []):
        sid = int(entry["surah"])
        uas_per_surah[sid] = entry.get("UAS")

    # If 750/840 schemas don't expose sig_A/UAS via "per_surah", fall back to direct keys
    # (we still attempt to use values; if any are None we'll mark axis MISSING)

    # Backfill missing values from h750 raw nested structure if needed
    def find_nested_per_surah(obj, key_name="surah"):
        if isinstance(obj, list):
            for item in obj:
                if isinstance(item, dict) and key_name in item:
                    return obj
            for item in obj:
                r = find_nested_per_surah(item, key_name)
                if r:
                    return r
        elif isinstance(obj, dict):
            for v in obj.values():
                r = find_nested_per_surah(v, key_name)
                if r:
                    return r
        return None

    if not sig_A_per_surah or any(s not in sig_A_per_surah for s in MUQATTAAT_29):
        rows = find_nested_per_surah(h750, "surah")
        if rows:
            for entry in rows:
                sid = int(entry.get("surah", -1))
                if sid > 0:
                    sig_A_per_surah.setdefault(sid, entry.get("sig_A"))
                    rhyme_top_per_surah.setdefault(sid, entry.get("top_final_letter"))
    if not uas_per_surah or any(s not in uas_per_surah for s in MUQATTAAT_29):
        rows = find_nested_per_surah(h840, "surah")
        if rows:
            for entry in rows:
                sid = int(entry.get("surah", -1))
                if sid > 0:
                    uas_per_surah.setdefault(sid, entry.get("UAS", entry.get("uas")))

    # Sanity: ensure we have all 29
    missing_sigA = [s for s in MUQATTAAT_29 if sig_A_per_surah.get(s) is None]
    missing_uas = [s for s in MUQATTAAT_29 if uas_per_surah.get(s) is None]
    missing_rhyme = [s for s in MUQATTAAT_29 if rhyme_top_per_surah.get(s) is None]
    out["data_audit"] = {
        "missing_sig_A": missing_sigA,
        "missing_UAS": missing_uas,
        "missing_rhyme_top": missing_rhyme,
    }

    # If any are missing, recompute rhyme_top from corpus directly
    if missing_rhyme:
        corpus = load_no_tashkeel()
        for sid_target in missing_rhyme:
            for s in corpus:
                if s["id"] == sid_target:
                    finals = []
                    for v in s["verses"]:
                        toks = v["text"].split()
                        if toks:
                            last = toks[-1]
                            if last:
                                finals.append(last[-1])
                    if finals:
                        c = Counter(finals)
                        rhyme_top_per_surah[sid_target] = c.most_common(1)[0][0]
                    break

    # Enumerate all 3-tuples of MUQATTAAT_29
    tuples = list(combinations(MUQATTAAT_29, 3))
    n_tuples = len(tuples)

    # Per-axis raw values
    def mean_pair_fr(a, b, c):
        ds = [fr_dist(a, b), fr_dist(a, c), fr_dist(b, c)]
        if any(x is None for x in ds):
            return None
        return sum(ds) / 3

    def sig_A_spread(a, b, c):
        vs = [sig_A_per_surah.get(a), sig_A_per_surah.get(b), sig_A_per_surah.get(c)]
        if any(v is None for v in vs):
            return None
        return max(vs) - min(vs)

    def uas_spread(a, b, c):
        vs = [uas_per_surah.get(a), uas_per_surah.get(b), uas_per_surah.get(c)]
        if any(v is None for v in vs):
            return None
        return max(vs) - min(vs)

    def rhyme_disagreement(a, b, c):
        vs = [rhyme_top_per_surah.get(a), rhyme_top_per_surah.get(b), rhyme_top_per_surah.get(c)]
        if any(v is None for v in vs):
            return None
        c0 = Counter(vs)
        max_share = max(c0.values()) / 3
        return 1 - max_share

    # Compute per-axis raw values for all tuples
    raws_fr, raws_sigA, raws_uas, raws_rhy = [], [], [], []
    keep_idx = []
    for idx, T in enumerate(tuples):
        fr_v = mean_pair_fr(*T)
        sa_v = sig_A_spread(*T)
        ua_v = uas_spread(*T)
        rh_v = rhyme_disagreement(*T)
        if any(x is None for x in (fr_v, sa_v, ua_v, rh_v)):
            continue
        raws_fr.append(fr_v)
        raws_sigA.append(sa_v)
        raws_uas.append(ua_v)
        raws_rhy.append(rh_v)
        keep_idx.append(idx)

    def zscore(values, x):
        m = sum(values) / len(values)
        var = sum((v - m) ** 2 for v in values) / len(values)
        sd = math.sqrt(var) if var > 0 else 1.0
        return (x - m) / sd

    # Per-axis means/SDs
    n = len(raws_fr)
    m_fr, m_sa, m_ua, m_rh = (sum(x)/n for x in (raws_fr, raws_sigA, raws_uas, raws_rhy))
    sd_fr, sd_sa, sd_ua, sd_rh = (math.sqrt(sum((v-m)**2 for v in arr)/n) for arr, m in
                                  zip((raws_fr, raws_sigA, raws_uas, raws_rhy),
                                      (m_fr, m_sa, m_ua, m_rh)))
    # Normalize SD to 1 if 0 to avoid div-by-zero
    sd_fr = sd_fr if sd_fr > 0 else 1.0
    sd_sa = sd_sa if sd_sa > 0 else 1.0
    sd_ua = sd_ua if sd_ua > 0 else 1.0
    sd_rh = sd_rh if sd_rh > 0 else 1.0

    # Composite score for each kept tuple
    composite = []
    for fr_v, sa_v, ua_v, rh_v in zip(raws_fr, raws_sigA, raws_uas, raws_rhy):
        z = (
            0.25 * (fr_v - m_fr) / sd_fr
            + 0.25 * (sa_v - m_sa) / sd_sa
            + 0.25 * (ua_v - m_ua) / sd_ua
            + 0.25 * (rh_v - m_rh) / sd_rh
        )
        composite.append(z)

    # Find target tuple {20, 27, 36}
    target = (20, 27, 36)
    target_pos = None
    for ki, idx in enumerate(keep_idx):
        if tuples[idx] == target:
            target_pos = ki
            break
    if target_pos is None:
        out["error"] = "target tuple {20,27,36} not found in kept tuples (data missing)"
        out["verdict"] = "DATA_GAP"
        return out

    target_score = composite[target_pos]
    target_fr = raws_fr[target_pos]
    target_sa = raws_sigA[target_pos]
    target_ua = raws_uas[target_pos]
    target_rh = raws_rhy[target_pos]

    rank_lower = sum(1 for s in composite if s <= target_score)
    p_perm = rank_lower / n
    pct = rank_lower / n * 100

    # Per-axis percentiles (lower-tail)
    pct_fr = sum(1 for v in raws_fr if v <= target_fr) / n * 100
    pct_sa = sum(1 for v in raws_sigA if v <= target_sa) / n * 100
    pct_ua = sum(1 for v in raws_uas if v <= target_ua) / n * 100
    pct_rh = sum(1 for v in raws_rhy if v <= target_rh) / n * 100

    out["target_tuple"] = list(target)
    out["target_pairwise_FR"] = {
        "Q20-Q27": fr_dist(20, 27), "Q20-Q36": fr_dist(20, 36), "Q27-Q36": fr_dist(27, 36),
        "mean": target_fr,
    }
    out["target_sig_A_values"] = {str(s): sig_A_per_surah.get(s) for s in target}
    out["target_sig_A_spread"] = target_sa
    out["target_UAS_values"] = {str(s): uas_per_surah.get(s) for s in target}
    out["target_UAS_spread"] = target_ua
    out["target_rhyme_top_letters"] = {str(s): rhyme_top_per_surah.get(s) for s in target}
    out["target_rhyme_disagreement"] = target_rh
    out["target_composite_z"] = target_score
    out["n_kept_tuples"] = n
    out["target_lower_tail_p"] = p_perm
    out["target_lower_tail_pct"] = pct
    out["per_axis_lower_tail_pct"] = {
        "FR_mean_pair": pct_fr,
        "sig_A_spread": pct_sa,
        "UAS_spread": pct_ua,
        "rhyme_disagreement": pct_rh,
    }

    # Acceptance
    n_axes_below_30 = sum(1 for x in (pct_fr, pct_sa, pct_ua, pct_rh) if x <= 30)
    if pct < 1 and n_axes_below_30 >= 3:
        verdict = "CONFIRMED"
    elif pct < 5 or n_axes_below_30 >= 3:
        verdict = "DIRECTIONAL"
    elif pct > 70:
        verdict = "PRE-COMMIT-VIOLATION"
    elif pct > 30 and n_axes_below_30 <= 2:
        verdict = "NULL"
    else:
        verdict = "WEAK_DIRECTIONAL"
    out["n_axes_below_30pct"] = n_axes_below_30
    out["verdict"] = verdict
    out["bonferroni_k"] = BONFERRONI_K
    out["alpha_bon"] = ALPHA_BON
    return out


# ---------- Q027-F-08: Solomon-narrative twin pair ----------

def run_F08(corpus, qac_roots):
    out = {
        "finding_id": "Q027-F-08",
        "prereg_sha": PREREG_SHAS["Q027-F-08"],
        "rules_tuple": "(no-tashkeel orthographic + QAC stem-roots; FR distance from h-new-111; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)",
        "seed": SEED,
    }

    # Load FR D-matrix
    with open(os.path.join(BASE, "findings/phase-b-hypotheses/csv/h-new-111.json")) as f:
        fr = json.load(f)
    D = {}
    for entry in fr["D_matrix_upper_triangular"]:
        i, j, d = entry
        D[(i, j)] = d
        D[(j, i)] = d
    def fr_dist(a, b):
        return D.get((a, b))

    d_27_34 = fr_dist(27, 34)
    d_27_38 = fr_dist(27, 38)
    stat_a = d_27_38 - d_27_34  # positive ⇒ Q 34 closer (predicted)
    h1_pass = (stat_a > 0)

    # Block-Jaccard at QAC root level
    def block_roots(sid, vrange):
        s = set()
        for v in vrange:
            s.update(qac_roots.get((sid, v), set()))
        return s

    q27_block = block_roots(27, range(15, 45))    # vv. 15-44
    q34_block = block_roots(34, range(12, 15))    # vv. 12-14
    q38_block = block_roots(38, range(30, 41))    # vv. 30-40

    def jacc(a, b):
        u = a | b
        i = a & b
        return len(i) / len(u) if u else 0.0

    j_27_34 = jacc(q27_block, q34_block)
    j_27_38 = jacc(q27_block, q38_block)
    stat_b = j_27_34 - j_27_38
    h1b_pass = (stat_b > 0)

    # Token-string concordance, per-verse-normalized, with stop-list
    # Build top-50 stop tokens from corpus
    token_count = Counter()
    for s in corpus:
        for v in s["verses"]:
            for tk in v["text"].split():
                token_count[tk] += 1
    stop_set = set(t for t, _ in token_count.most_common(50))

    def block_tokens(sid, vrange):
        toks = set()
        for s in corpus:
            if s["id"] != sid:
                continue
            for v in s["verses"]:
                if v["id"] in vrange:
                    for tk in v["text"].split():
                        if tk not in stop_set:
                            toks.add(tk)
        return toks

    q27_toks = block_tokens(27, set(range(15, 45)))
    q34_toks = block_tokens(34, set(range(12, 15)))
    q38_toks = block_tokens(38, set(range(30, 41)))

    n_27_34 = len(q27_toks & q34_toks)
    n_27_38 = len(q27_toks & q38_toks)
    # Per-verse normalize by Q 34 (3 verses) vs Q 38 (11 verses)
    norm_27_34 = n_27_34 / 3
    norm_27_38 = n_27_38 / 11
    stat_c = norm_27_34 - norm_27_38
    h1c_pass = (stat_c > 0)

    # Aggregate
    n_pass = int(h1_pass) + int(h1b_pass) + int(h1c_pass)
    if n_pass == 3:
        verdict = "CONFIRMED"
    elif n_pass == 2:
        verdict = "DIRECTIONAL"
    elif n_pass == 1:
        verdict = "MIXED"
    else:
        verdict = "NULL"
    if not h1_pass:
        verdict = "PRE-COMMIT-VIOLATION (FR axis: Q 38 closer than Q 34) | aggregate: " + verdict

    # Diagnostic auxiliary null for stat_a
    rng = random.Random(SEED)
    n_aux = N_PERM
    geq = 0
    sids_pool = MUQATTAAT_29[:]
    sids_pool_no27 = [s for s in sids_pool if s != 27]
    for _ in range(n_aux):
        a, b = rng.sample(sids_pool_no27, 2)
        d27a = fr_dist(27, a)
        d27b = fr_dist(27, b)
        if d27a is None or d27b is None:
            continue
        delta = d27b - d27a
        if abs(delta) >= abs(stat_a):
            geq += 1
    p_aux_two_sided = (1 + geq) / (1 + n_aux)

    out["pair_FR_distances"] = {"Q27_Q34": d_27_34, "Q27_Q38": d_27_38, "Q34_Q38": fr_dist(34, 38)}
    out["stat_a_FR_difference_38_minus_34"] = stat_a
    out["block_root_jaccard"] = {"Q27_Q34_block": j_27_34, "Q27_Q38_block": j_27_38}
    out["stat_b_jaccard_difference_34_minus_38"] = stat_b
    out["block_token_concordance"] = {"Q27_Q34_normalized": norm_27_34, "Q27_Q38_normalized": norm_27_38,
                                       "Q27_Q34_raw_count": n_27_34, "Q27_Q38_raw_count": n_27_38,
                                       "Q34_block_size_verses": 3, "Q38_block_size_verses": 11}
    out["stat_c_token_concordance_difference"] = stat_c
    out["H1_pass"] = h1_pass
    out["H1b_pass"] = h1b_pass
    out["H1c_pass"] = h1c_pass
    out["n_pass_of_3"] = n_pass
    out["aux_p_two_sided_random_pair"] = p_aux_two_sided
    out["verdict"] = verdict
    out["bonferroni_k"] = BONFERRONI_K
    out["alpha_bon"] = ALPHA_BON
    return out


# ---------- Q027-F-09: Q 27:18 verse-level hapax + distinctiveness ----------

def run_F09(corpus):
    out = {
        "finding_id": "Q027-F-09",
        "prereg_sha": PREREG_SHAS["Q027-F-09"],
        "rules_tuple": "(no-tashkeel, orthographic-exact-match for tokens; orthographic IDF; basmala-counted-only-in-Q1; Hafs-Kufan; Mashriqi)",
        "seed": SEED,
    }

    # Locked tokens from Q 27:18
    locked_tokens = ["نملة", "النمل", "مساكنكم", "يحطمنكم", "وجنوده"]

    token_count = Counter()
    verse_idf_count = Counter()  # token -> #verses containing it
    n_verses = 0
    all_verses = []  # list of (sid, vid, [tokens])
    for s in corpus:
        sid = s["id"]
        for v in s["verses"]:
            n_verses += 1
            toks = v["text"].split()
            for tk in toks:
                token_count[tk] += 1
            for tk in set(toks):
                verse_idf_count[tk] += 1
            all_verses.append((sid, v["id"], toks))

    # H1.a — locked-tokens hapax inventory
    locked_corpus_counts = {t: token_count.get(t, 0) for t in locked_tokens}
    hapax_set = [t for t, c in locked_corpus_counts.items() if c == 1]
    stat_a = len(hapax_set)
    h1a_pass = (stat_a >= 3)
    out["H1a_locked_tokens"] = locked_tokens
    out["H1a_locked_token_corpus_counts"] = locked_corpus_counts
    out["H1a_hapax_count"] = stat_a
    out["H1a_hapax_tokens"] = hapax_set
    out["H1a_pass"] = h1a_pass

    # H1.b — verse-distinctiveness IDF score
    # IDF(t) = log(N / df(t)); for tokens with df=0 fall back to log(N)
    def idf(t):
        df = verse_idf_count.get(t, 0)
        if df == 0:
            return math.log(n_verses)
        return math.log(n_verses / df)

    verse_scores = []
    target_score = None
    for sid, vid, toks in all_verses:
        if not toks:
            score = 0.0
        else:
            uniq = set(toks)
            score = sum(idf(t) for t in uniq) / len(uniq)  # mean IDF over unique tokens
        verse_scores.append((sid, vid, score, len(toks)))
        if sid == 27 and vid == 18:
            target_score = score

    sorted_scores = sorted(verse_scores, key=lambda x: x[2])  # ascending IDF
    target_rank = None
    for i, (sid, vid, sc, _) in enumerate(sorted_scores):
        if sid == 27 and vid == 18:
            target_rank = i + 1
            break
    pct_upper = (1 - (target_rank / len(sorted_scores))) * 100  # higher = more distinctive
    h1b_pass = (pct_upper >= 90)  # i.e., target in top 10%
    out["H1b_target_idf_mean"] = target_score
    out["H1b_target_rank_ascending"] = target_rank
    out["H1b_n_verses"] = len(verse_scores)
    out["H1b_target_upper_tail_pct"] = pct_upper
    out["H1b_pass"] = h1b_pass

    # H1.c — يحطمنكم corpus-wide count
    h1c_count = token_count.get("يحطمنكم", 0)
    h1c_pass = (h1c_count == 1)
    out["H1c_yahtimannakum_count"] = h1c_count
    out["H1c_pass"] = h1c_pass

    # Aggregate
    n_pass = int(h1a_pass) + int(h1b_pass) + int(h1c_pass)
    if n_pass == 3:
        verdict = "CONFIRMED"
    elif n_pass == 2:
        verdict = "DIRECTIONAL"
    elif n_pass == 1:
        verdict = "MIXED"
    else:
        verdict = "NULL"
    out["verdict"] = verdict
    out["n_pass_of_3"] = n_pass
    out["bonferroni_k"] = BONFERRONI_K
    out["alpha_bon"] = ALPHA_BON
    return out


# ---------- main ----------

def main():
    print("=" * 70)
    print("Q027 al-Naml — NEW novel-findings runner (F-05 .. F-09)")
    print(f"  Seed: {SEED}; Bonferroni k={BONFERRONI_K}; alpha_bon={ALPHA_BON}")
    print("=" * 70)
    verify_prereg_shas()

    print("\nLoading corpus (no-tashkeel)...")
    corpus = load_no_tashkeel()
    print(f"  loaded {len(corpus)} surahs")

    print("\nLoading QAC v0.4 root annotations (per (s,v))...")
    qac_roots = load_qac_roots_per_verse()
    print(f"  loaded roots for {len(qac_roots)} verse positions")

    print("\nRunning Q027-F-05 (second-basmala STRUCTURAL ROLE)...")
    out05 = run_F05(corpus, qac_roots)
    p = os.path.join(OUT_DIR, "Q027-F-05.json")
    with open(p, "w") as f:
        json.dump(out05, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out05['verdict']}")

    print("\nRunning Q027-F-06 (hud-hud narrative-block lexical isolation)...")
    out06 = run_F06(corpus, qac_roots)
    p = os.path.join(OUT_DIR, "Q027-F-06.json")
    with open(p, "w") as f:
        json.dump(out06, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out06['verdict']}")

    print("\nRunning Q027-F-07 (2-letter muqaṭṭaʿ family joint cohesion)...")
    out07 = run_F07()
    p = os.path.join(OUT_DIR, "Q027-F-07.json")
    with open(p, "w") as f:
        json.dump(out07, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out07['verdict']}")

    print("\nRunning Q027-F-08 (Solomon-narrative twin pair)...")
    out08 = run_F08(corpus, qac_roots)
    p = os.path.join(OUT_DIR, "Q027-F-08.json")
    with open(p, "w") as f:
        json.dump(out08, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out08['verdict']}")

    print("\nRunning Q027-F-09 (Q 27:18 verse-level hapax + distinctiveness)...")
    out09 = run_F09(corpus)
    p = os.path.join(OUT_DIR, "Q027-F-09.json")
    with open(p, "w") as f:
        json.dump(out09, f, ensure_ascii=False, indent=2)
    print(f"  wrote {p}  verdict={out09['verdict']}")

    print("\n" + "=" * 70)
    print("All Q027-F-05..F-09 tests complete.")
    print("=" * 70)


if __name__ == "__main__":
    main()
