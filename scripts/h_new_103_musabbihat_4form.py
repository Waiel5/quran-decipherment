#!/usr/bin/env python3
"""H-NEW-103 — Musabbiḥāt 4-form sub-typology.

Pre-reg: findings/phase-b-hypotheses/h-new-103-musabbihat-4form-prereg.md

7 classical musabbiḥāt surahs across 4 verbal forms:
  NOUN:       Q 17  (subḥāna alladhī asrā)
  PERFECT:    Q 57, 59, 61  (sabbaḥa li-llāhi)
  IMPERFECT:  Q 62, 64  (yusabbiḥu li-llāhi)
  IMPERATIVE: Q 87  (sabbiḥi sma rabbika)

Cells:
  A — 4-form verbal-form ratification (descriptive)
  B — within-form vs cross-form content similarity (PRIMARY directional)
      metrics: char-prefix v1, root-Jaccard (whole-surah), verse-length sim
      null: 10K permutations of form-label multiset {NOUN:1, PERFECT:3, IMPERFECT:2, IMPERATIVE:1}
  C — form × length / period / Nöldeke phase cross-tab (exploratory)
  D — Friday-cluster cross-reference (exploratory, descriptive)

Bonferroni: k=4, alpha_bon=0.0125 (primary = char-prefix under permutation)
Seed: 20260417
"""
from __future__ import annotations

import csv
import json
import random
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_PERM = 10_000
ALPHA_BON = 0.0125
BONF_K = 4
BONF_FAMILY = "h-new-103-musabbihat-4form"

# The 7 classical musabbiḥāt
MUSABBIHAT = [17, 57, 59, 61, 62, 64, 87]

# Form labels (pre-registered from v1 min-tashkeel inspection)
FORM_OF = {
    17: "NOUN",
    57: "PERFECT",
    59: "PERFECT",
    61: "PERFECT",
    62: "IMPERFECT",
    64: "IMPERFECT",
    87: "IMPERATIVE",
}

# Auxiliary (excluded from primary per pre-reg)
AUX_SURAH = 20  # sabbiḥ at v130 but muqaṭṭāʿa v1

LOC_RE = re.compile(r'^\((\d+):(\d+):(\d+):(\d+)\)$')
ROOT_RE = re.compile(r'ROOT:([^|]+)')


def load_quran(variant):
    path = REPO / "quran-text" / f"quran-{variant}.json"
    with path.open(encoding="utf-8") as fh:
        return json.load(fh)


def load_qac_roots_per_surah():
    """Return (per_surah: sid -> list of stem root strings, corpus_root_count)."""
    per_surah = defaultdict(list)
    corpus_count = Counter()
    path = REPO / "data" / "morphology" / "quranic-corpus-morphology-0.4.txt"
    with path.open(encoding="utf-8") as fh:
        for line in fh:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) < 4:
                continue
            m = LOC_RE.match(parts[0])
            if not m:
                continue
            sid = int(m.group(1))
            feat = parts[3]
            if "STEM" not in feat:
                continue
            rm = ROOT_RE.search(feat)
            if not rm:
                continue
            root = rm.group(1)
            per_surah[sid].append(root)
            corpus_count[root] += 1
    return per_surah, corpus_count


def load_revelation_metadata():
    """Return dict mushaf_id -> (period, noldeke_phase, revelation_order)."""
    out = {}
    path = REPO / "data" / "revelation-order.csv"
    with path.open(encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            mid = int(row["mushaf_order"])
            out[mid] = {
                "period": row["period"],
                "noldeke_phase": row["noldeke_phase"],
                "revelation_order": int(row["revelation_order"]),
            }
    return out


# ---------------- Similarity metrics ----------------

def char_prefix_len(a, b):
    """Number of leading characters that match between two strings."""
    n = 0
    for x, y in zip(a, b):
        if x == y:
            n += 1
        else:
            break
    return n


def jaccard(set_a, set_b):
    if not set_a and not set_b:
        return 1.0
    inter = len(set_a & set_b)
    union = len(set_a | set_b)
    return inter / max(1, union)


def scalar_sim(a, b):
    """Symmetric [0,1]: 1 - |a-b|/max(|a|,|b|,eps)."""
    denom = max(abs(a), abs(b), 1e-9)
    return 1.0 - abs(a - b) / denom


# ---------------- Feature extraction ----------------

def v1_text(quran_no_tashkeel, sid):
    s = quran_no_tashkeel[sid - 1]
    return s["verses"][0]["text"].strip()


def mean_verse_len(quran_no_tashkeel, sid):
    s = quran_no_tashkeel[sid - 1]
    lengths = [len(v["text"].strip()) for v in s["verses"]]
    return sum(lengths) / max(1, len(lengths))


def surah_root_set(qac_per_surah, sid):
    return set(qac_per_surah.get(sid, []))


def surah_len_verses(quran_no_tashkeel, sid):
    return len(quran_no_tashkeel[sid - 1]["verses"])


def length_class(n_verses):
    if n_verses <= 30:
        return "short"
    if n_verses <= 100:
        return "medium"
    return "long"


# ---------------- Pair metric computation ----------------

def pair_metrics(sid_a, sid_b, quran, qac_per_surah):
    v1a = v1_text(quran, sid_a)
    v1b = v1_text(quran, sid_b)
    cp = char_prefix_len(v1a, v1b)
    rj = jaccard(surah_root_set(qac_per_surah, sid_a),
                  surah_root_set(qac_per_surah, sid_b))
    vls = scalar_sim(mean_verse_len(quran, sid_a),
                     mean_verse_len(quran, sid_b))
    return {"char_prefix": cp, "root_jaccard": rj, "verse_len_sim": vls}


def partition_pairs(surahs, form_of):
    """Return (within_pairs, cross_pairs) lists of (a, b) tuples.
    `form_of` maps sid -> form label."""
    within = []
    cross = []
    for a, b in combinations(sorted(surahs), 2):
        if form_of[a] == form_of[b]:
            within.append((a, b))
        else:
            cross.append((a, b))
    return within, cross


def mean_metric(pairs, metric_name, pair_cache):
    """Average a single metric across pairs (skip if no pairs)."""
    if not pairs:
        return None
    vals = [pair_cache[pair][metric_name] for pair in pairs]
    return sum(vals) / len(vals)


# ---------------- Main ----------------

def main():
    rng = random.Random(SEED)

    print("Loading Quran corpora...", file=sys.stderr)
    quran_nt = load_quran("no-tashkeel")
    quran_mt = load_quran("min-tashkeel")

    print("Loading QAC morphology...", file=sys.stderr)
    qac_per_surah, _ = load_qac_roots_per_surah()

    print("Loading revelation metadata...", file=sys.stderr)
    rev_meta = load_revelation_metadata()

    # ---- Cell A: form ratification ----
    cell_a = []
    for sid in MUSABBIHAT:
        v1_mt = quran_mt[sid - 1]["verses"][0]["text"].strip()
        v1_nt = v1_text(quran_nt, sid)
        meta = rev_meta[sid]
        cell_a.append({
            "surah": sid,
            "name": quran_mt[sid - 1]["transliteration"],
            "form": FORM_OF[sid],
            "v1_min_tashkeel": v1_mt,
            "v1_no_tashkeel_prefix80": v1_nt[:80],
            "n_verses": quran_mt[sid - 1]["total_verses"],
            "period": meta["period"],
            "noldeke_phase": meta["noldeke_phase"],
            "revelation_order": meta["revelation_order"],
        })

    # Also auxiliary Q 20
    s20 = quran_mt[AUX_SURAH - 1]
    v130_mt = s20["verses"][129]["text"].strip()
    aux_cell = {
        "surah": AUX_SURAH,
        "note": "excluded from primary; v1=muqaṭṭāʿa طه; sabbiḥ at v130",
        "v1_min_tashkeel": s20["verses"][0]["text"].strip(),
        "v130_min_tashkeel": v130_mt,
        "period": rev_meta[AUX_SURAH]["period"],
        "noldeke_phase": rev_meta[AUX_SURAH]["noldeke_phase"],
    }

    # ---- Cell B: within vs cross form similarity ----
    # Precompute all pairwise metrics over the 7 surahs
    pair_cache = {}
    for a, b in combinations(sorted(MUSABBIHAT), 2):
        pair_cache[(a, b)] = pair_metrics(a, b, quran_nt, qac_per_surah)

    metrics = ["char_prefix", "root_jaccard", "verse_len_sim"]

    # Observed partition under true form labels
    within_obs, cross_obs = partition_pairs(MUSABBIHAT, FORM_OF)

    obs_within_means = {m: mean_metric(within_obs, m, pair_cache) for m in metrics}
    obs_cross_means = {m: mean_metric(cross_obs, m, pair_cache) for m in metrics}
    obs_deltas = {
        m: obs_within_means[m] - obs_cross_means[m] for m in metrics
    }

    # MW-5 positive-control: within-form char-prefix mean should be high
    # (H-NEW-58c: perfect pairs 24-56, imperfect pair 37 — mean > 10 required)
    within_cp = obs_within_means["char_prefix"]
    cross_cp = obs_cross_means["char_prefix"]
    mw5_pass = (within_cp >= 10.0) and (cross_cp <= 5.0)

    # Null: permute the form-label multiset across the 7 surahs, recompute Δ
    form_labels_multiset = [FORM_OF[s] for s in sorted(MUSABBIHAT)]  # ordered list
    # multiset: ['NOUN','PERFECT','PERFECT','PERFECT','IMPERFECT','IMPERFECT','IMPERATIVE']
    surahs_sorted = sorted(MUSABBIHAT)

    perm_deltas = {m: [] for m in metrics}
    perm_within_cp = []  # diagnostic
    observed_labels_tuple = tuple(form_labels_multiset)
    # Save all perm-generated deltas for p-value
    for _ in range(N_PERM):
        shuffled = form_labels_multiset[:]
        rng.shuffle(shuffled)
        perm_form = dict(zip(surahs_sorted, shuffled))
        w, c = partition_pairs(surahs_sorted, perm_form)
        for m in metrics:
            mw = mean_metric(w, m, pair_cache)
            mc = mean_metric(c, m, pair_cache)
            if mw is None or mc is None:
                # shouldn't happen (we always have ≥1 within pair from multiset {1,3,2,1})
                perm_deltas[m].append(float("-inf"))
            else:
                perm_deltas[m].append(mw - mc)
        # diagnostic: within-form char-prefix mean
        perm_within_cp.append(mean_metric(w, "char_prefix", pair_cache))

    # One-sided p: P(perm Δ >= observed Δ)
    def upper_p(obs, null_list):
        n_ge = sum(1 for v in null_list if v >= obs)
        return (1 + n_ge) / (1 + len(null_list))

    p_values = {m: upper_p(obs_deltas[m], perm_deltas[m]) for m in metrics}

    cell_b = {
        "metrics": metrics,
        "n_within_pairs": len(within_obs),
        "n_cross_pairs": len(cross_obs),
        "within_pairs": [list(p) for p in within_obs],
        "cross_pairs": [list(p) for p in cross_obs],
        "observed_within_means": obs_within_means,
        "observed_cross_means": obs_cross_means,
        "observed_deltas": obs_deltas,
        "p_values_one_sided": p_values,
        "n_perm": N_PERM,
        "null_summary": {
            m: {
                "mean_delta": sum(perm_deltas[m]) / N_PERM,
                "median_delta": sorted(perm_deltas[m])[N_PERM // 2],
                "q95_delta": sorted(perm_deltas[m])[int(0.95 * N_PERM)],
                "q99_delta": sorted(perm_deltas[m])[int(0.99 * N_PERM)],
                "max_delta": max(perm_deltas[m]),
            }
            for m in metrics
        },
        "primary_metric": "char_prefix",
        "alpha_bon": ALPHA_BON,
        "primary_p": p_values["char_prefix"],
        "primary_pass": p_values["char_prefix"] < ALPHA_BON,
        "mw5_positive_control": {
            "within_form_char_prefix_mean": within_cp,
            "cross_form_char_prefix_mean": cross_cp,
            "criterion": "within ≥ 10 AND cross ≤ 5",
            "pass": mw5_pass,
        },
        "all_pair_metrics": {
            f"{a}-{b}": v for (a, b), v in pair_cache.items()
        },
    }

    # ---- Cell C: form × structural class cross-tabs ----
    by_form_length = defaultdict(list)
    by_form_period = defaultdict(list)
    by_form_noldeke = defaultdict(list)
    for sid in MUSABBIHAT:
        f = FORM_OF[sid]
        n_v = surah_len_verses(quran_nt, sid)
        by_form_length[f].append((sid, n_v, length_class(n_v)))
        by_form_period[f].append((sid, rev_meta[sid]["period"]))
        by_form_noldeke[f].append((sid, rev_meta[sid]["noldeke_phase"]))

    # Cross-tabs as JSON-friendly dicts
    length_table = {
        f: {"sids_nverses_class": [[s, n, c] for (s, n, c) in items]}
        for f, items in by_form_length.items()
    }
    period_table = {
        f: {"sids_period": [[s, p] for (s, p) in items]}
        for f, items in by_form_period.items()
    }
    noldeke_table = {
        f: {"sids_phase": [[s, p] for (s, p) in items]}
        for f, items in by_form_noldeke.items()
    }

    # Form × period contingency counts
    form_x_period = defaultdict(lambda: defaultdict(int))
    for sid in MUSABBIHAT:
        form_x_period[FORM_OF[sid]][rev_meta[sid]["period"]] += 1
    form_x_period = {k: dict(v) for k, v in form_x_period.items()}

    cell_c = {
        "length_by_form": length_table,
        "period_by_form": period_table,
        "noldeke_phase_by_form": noldeke_table,
        "form_x_period_contingency": form_x_period,
        "observation": (
            "Mecca-Medina cline by form: NOUN(Q17)=Meccan-Middle, "
            "PERFECT={57,59,61}=all Medinan, IMPERFECT={62,64}=all Medinan, "
            "IMPERATIVE(Q87)=Meccan-Early. Finite-verb musabbiḥāt (perfect+imperfect) "
            "are ALL Medinan; non-finite (noun+imperative) are Meccan."
        ),
    }

    # ---- Cell D: Friday cluster cross-reference ----
    # H-NEW-68 null; Q 62 is Friday-recitation canonical.
    # Classical Friday pairing: Q 62 + Q 63 (al-Munāfiqūn) — NOT Q 64.
    friday_info = {
        17: "Laylat al-Miʿrāj night-journey commemorative; recited on 27 Rajab by some traditions",
        57: "Al-Ḥadīd — no fixed liturgical calendar; classical hadith virtue narrations",
        59: "Al-Ḥashr — last 3 verses (Khawātim) recited morning/evening in many traditions",
        61: "Al-Ṣaff — military/cohesion themes; no fixed recitation day",
        62: "Al-Jumuʿah — CANONICAL Friday-prayer recitation (paired with Q 63 al-Munāfiqūn)",
        64: "Al-Taghābun — NO classical Friday-recitation convention",
        87: "Al-Aʿlā — recited in Witr, Eid prayers, and Friday prayer (after al-Jumuʿah or al-Ghāshiya per hadith)",
    }

    cell_d = {
        "imperfect_form_sids": [62, 64],
        "perfect_form_sids": [57, 59, 61],
        "friday_recitation_notes": friday_info,
        "observation": (
            "Imperfect-form sub-group does NOT share a unified Friday-recitation function: "
            "Q 62 is CANONICAL Jumuʿah recitation, Q 64 has no such convention. "
            "Instead, Q 62 is paired with Q 63 (non-musabbiḥa) for Friday prayer. "
            "Meanwhile Q 87 (IMPERATIVE form) is the OTHER surah with strong Friday-prayer "
            "liturgical tradition (hadith: recited with al-Jumuʿah or al-Ghāshiya in Jumuʿah khutba). "
            "So the 'Friday-function' is split across forms (Q 62 imperfect + Q 87 imperative), "
            "not confined to the imperfect sub-cluster. Functional correlate is NEGATIVE at form level."
        ),
    }

    # ---- Assemble output ----
    out = {
        "id": "H-NEW-103",
        "title": "Musabbiḥāt 4-form sub-typology",
        "seed": SEED,
        "n_perm": N_PERM,
        "bonferroni_k": BONF_K,
        "bonferroni_family": BONF_FAMILY,
        "alpha_bon": ALPHA_BON,
        "musabbihat_surahs": MUSABBIHAT,
        "form_assignments": FORM_OF,
        "cell_A_form_ratification": cell_a,
        "auxiliary_Q20": aux_cell,
        "cell_B_within_vs_cross_similarity": cell_b,
        "cell_C_form_structural_crosstabs": cell_c,
        "cell_D_friday_functional_crossref": cell_d,
        "primary_verdict": None,  # filled below
    }

    # Verdict
    if not cell_b["mw5_positive_control"]["pass"]:
        out["primary_verdict"] = "INSTRUMENT-FAIL (MW-5 positive control failed)"
    elif cell_b["primary_pass"]:
        out["primary_verdict"] = "PASS-DIRECTED (cell B primary char-prefix p < 0.0125)"
    else:
        out["primary_verdict"] = "NULL (cell B primary char-prefix p >= 0.0125)"

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-103.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False),
                        encoding="utf-8")
    print(f"Wrote {out_path}", file=sys.stderr)

    # ---- Console summary ----
    print("\n=== Cell A: Form ratification ===")
    print(f"{'Surah':<8} {'Name':<15} {'Form':<11} {'Period':<8} {'n_v':<5} v1 (no-tashkeel)")
    for row in cell_a:
        print(f"Q {row['surah']:<6} {row['name']:<15} {row['form']:<11} "
              f"{row['period']:<8} {row['n_verses']:<5} {row['v1_no_tashkeel_prefix80'][:60]}")

    print("\n=== Cell B: Within-form vs cross-form similarity ===")
    print(f"  n_within_pairs = {cell_b['n_within_pairs']}  "
          f"n_cross_pairs = {cell_b['n_cross_pairs']}")
    for m in metrics:
        star = "*" if p_values[m] < ALPHA_BON else " "
        print(f"  {m:<16} within={obs_within_means[m]:.4f}  "
              f"cross={obs_cross_means[m]:.4f}  "
              f"Δ={obs_deltas[m]:+.4f}  p={p_values[m]:.4f}{star}")
    print(f"  PRIMARY (char_prefix) p = {p_values['char_prefix']:.4f}  "
          f"α_bon = {ALPHA_BON}  → {'PASS' if cell_b['primary_pass'] else 'NULL'}")
    print(f"  MW-5 positive control: within-CP mean = {within_cp:.2f}, "
          f"cross-CP mean = {cross_cp:.2f}  "
          f"→ {'PASS' if mw5_pass else 'FAIL'}")

    print("\n=== Cell C: Form × Period contingency ===")
    for f, periods in form_x_period.items():
        print(f"  {f:<12} {dict(periods)}")

    print("\n=== Cell D: Friday-function cross-reference ===")
    print(f"  {cell_d['observation']}")

    print(f"\nPRIMARY VERDICT: {out['primary_verdict']}")


if __name__ == "__main__":
    main()
