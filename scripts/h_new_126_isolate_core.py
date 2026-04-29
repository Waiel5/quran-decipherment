"""H-NEW-126 — True-isolate-core characterization.

Pre-reg: findings/phase-b-hypotheses/h-new-126-isolate-core-prereg.md
Family:  h-new-126-isolate-core
Bonferroni k=4, α_bon=0.0125.
N_PERM=10,000.
Seed=20260417.

Four cells:
  Cell A — Shared content: pairwise root-Jaccard mean over the 5-core
           vs null of 5 random non-core surahs (10K perms; one-sided upper).
  Cell B — Genre coherence: classify each surah name category; descriptive.
  Cell C — Rhetorical mode: compute (imp, int, dec) per-surah triple;
           mean pairwise Euclidean distance within core vs null
           (10K perms; one-sided lower).
  Cell D — Per-surah uniqueness: 9-axis descriptive profile; identify
           single most-distinctive axis per core surah (percentile).

MW-5 positive controls:
  - Cell A: ḥawāmīm core {Q 40, 41, 42, 43, 44}
  - Cell C: musabbiḥāt inner-5 {Q 57, 59, 61, 62, 64}
"""
from __future__ import annotations

import collections
import csv
import json
import math
import random
import sys
import time
from itertools import combinations
from pathlib import Path
from statistics import mean

sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")

from tools.loader import load_quran  # noqa: E402
from tools.tokenize import real_words  # noqa: E402

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260417
N_PERM = 10_000
N_SURAHS = 114
BONFERRONI_K = 4
ALPHA_BON = 0.05 / BONFERRONI_K  # 0.0125

# ----------------------------------------------------------------------
# Core locked sets
# ----------------------------------------------------------------------

CORE_5 = [16, 21, 22, 23, 25]  # al-Naḥl, al-Anbiyāʾ, al-Ḥajj, al-Muʾminūn, al-Furqān
HAWAMIM_MW5 = [40, 41, 42, 43, 44]   # Cell A positive control
MUSABBIHAT_INNER_5 = [57, 59, 61, 62, 64]  # Cell C positive control

# Surah names (transliteration + category for Cell B)
SURAH_NAMES = {
    16: ("al-Naḥl", "the Bee"),
    21: ("al-Anbiyāʾ", "the Prophets"),
    22: ("al-Ḥajj", "the Pilgrimage"),
    23: ("al-Muʾminūn", "the Believers"),
    25: ("al-Furqān", "the Criterion"),
}

# Cell B pre-committed category classification
# Categories: concept-name, object-name, prophet-name, event-name,
#             attribute-name, letter-name
CATEGORIES_CORE = {
    16: ("object-name", "al-Naḥl = 'the Bee' — a creature; concrete object; NOT a prophet/event/attribute/letter. Allied to concept-class for our purposes."),
    21: ("concept-name", "al-Anbiyāʾ = 'the Prophets' — plural-concept referring to prophethood as a category; NOT any specific prophet."),
    22: ("concept-name", "al-Ḥajj = 'the Pilgrimage' — concept/ritual-institution."),
    23: ("concept-name", "al-Muʾminūn = 'the Believers' — plural-concept referring to believers as a category."),
    25: ("concept-name", "al-Furqān = 'the Criterion' — abstract concept/epithet for revelation."),
}


# ----------------------------------------------------------------------
# Data loading
# ----------------------------------------------------------------------

def load_surah_root_counts() -> dict[int, dict[str, int]]:
    """Return {surah_id: {root: count}} from surah-root-graph.json."""
    path = REPO / "data" / "morphology" / "surah-root-graph.json"
    with path.open("r", encoding="utf-8") as fh:
        d = json.load(fh)
    out = {}
    for s_str, roots_dict in d["surahs"].items():
        out[int(s_str)] = dict(roots_dict)
    assert all(s in out for s in range(1, N_SURAHS + 1)), "missing surahs"
    return out


def load_noldeke() -> dict[int, int]:
    """Return {surah_id: noldeke_rank (1..114)}."""
    path = REPO / "data" / "revelation-order.csv"
    out = {}
    with path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            sid = int(row["mushaf_order"])
            rank = int(row["noldeke_order"])
            out[sid] = rank
    assert len(out) == N_SURAHS
    return out


def load_period() -> dict[int, str]:
    """Return {surah_id: 'Meccan' or 'Medinan'}."""
    path = REPO / "data" / "revelation-order.csv"
    out = {}
    with path.open("r", encoding="utf-8") as fh:
        for row in csv.DictReader(fh):
            sid = int(row["mushaf_order"])
            out[sid] = row["period"].strip()
    return out


# ----------------------------------------------------------------------
# Cell A — Root-Jaccard within core vs random 5-sets
# ----------------------------------------------------------------------

def pairwise_mean_root_jaccard(surah_ids: list[int], root_sets: dict[int, frozenset]) -> float:
    scores = []
    for a, b in combinations(surah_ids, 2):
        ra, rb = root_sets[a], root_sets[b]
        inter = len(ra & rb)
        union = len(ra | rb)
        scores.append(inter / union if union > 0 else 0.0)
    return mean(scores) if scores else 0.0


def cell_a(root_sets: dict[int, frozenset], rng: random.Random) -> dict:
    """Cell A — shared content test.

    Observed = mean pairwise root-Jaccard over 10 pairs in CORE_5.
    Null    = 10K samples of 5 non-core surahs, same statistic.
    Direction = ONE-SIDED UPPER.
    """
    obs = pairwise_mean_root_jaccard(CORE_5, root_sets)
    non_core = [s for s in range(1, N_SURAHS + 1) if s not in CORE_5]
    null_vals = []
    for _ in range(N_PERM):
        sample = rng.sample(non_core, 5)
        null_vals.append(pairwise_mean_root_jaccard(sample, root_sets))
    # one-sided upper p-value
    ge = sum(1 for v in null_vals if v >= obs)
    p_one_sided = (1 + ge) / (1 + N_PERM)
    null_mean = mean(null_vals)
    null_median = sorted(null_vals)[N_PERM // 2]

    # MW-5 positive control: ḥawāmīm core
    pc_non = [s for s in range(1, N_SURAHS + 1) if s not in HAWAMIM_MW5]
    pc_obs = pairwise_mean_root_jaccard(HAWAMIM_MW5, root_sets)
    pc_null = []
    for _ in range(N_PERM):
        sample = rng.sample(pc_non, 5)
        pc_null.append(pairwise_mean_root_jaccard(sample, root_sets))
    pc_ge = sum(1 for v in pc_null if v >= pc_obs)
    pc_p = (1 + pc_ge) / (1 + N_PERM)

    return {
        "statistic": "mean_pairwise_root_jaccard",
        "direction": "one-sided upper",
        "core": CORE_5,
        "observed": obs,
        "null_mean": null_mean,
        "null_median": null_median,
        "p_one_sided_upper": p_one_sided,
        "alpha_bon": ALPHA_BON,
        "verdict": "PASS" if p_one_sided < ALPHA_BON else "NULL",
        "mw5_positive_control": {
            "cluster": "hawamim_core_Q40-44",
            "members": HAWAMIM_MW5,
            "observed": pc_obs,
            "null_mean": mean(pc_null),
            "p_one_sided_upper": pc_p,
            "fired_at_0.05": pc_p < 0.05,
        },
    }


# ----------------------------------------------------------------------
# Cell B — Genre coherence (descriptive)
# ----------------------------------------------------------------------

def cell_b() -> dict:
    # All 5 are concept-or-object-named per pre-commit.
    n_concept_or_object = sum(
        1 for s in CORE_5
        if CATEGORIES_CORE[s][0] in ("concept-name", "object-name")
    )
    per_surah = [
        {
            "surah": s,
            "name": SURAH_NAMES[s][0],
            "gloss": SURAH_NAMES[s][1],
            "category": CATEGORIES_CORE[s][0],
            "justification": CATEGORIES_CORE[s][1],
        }
        for s in CORE_5
    ]
    return {
        "description": "5/5 concept-or-object-named, 0 prophet/event/attribute/letter",
        "per_surah": per_surah,
        "n_concept_or_object": n_concept_or_object,
        "genre_coherent": n_concept_or_object == 5,
    }


# ----------------------------------------------------------------------
# Cell C — Rhetorical mode
# ----------------------------------------------------------------------

IMPERATIVE_TOKENS = {
    "قل", "قلنا", "اقرأ", "اعبدوا", "اتقوا", "آمنوا",
    "ادعوا", "اذكروا", "انظروا", "اسجدوا", "اركعوا",
    # common additional imperative forms
    "قولوا", "قلن", "اتبعوا", "ارجع", "ارجعوا", "اصبر", "اصبروا",
    "انفروا", "اشكر", "اشكروا", "اقم", "اقيموا", "اسمع", "اسمعوا",
    "كل", "كلوا", "اشرب", "اشربوا", "اخرج", "اخرجوا",
}

INTERROGATIVE_TOKENS = {"هل", "متى", "أين", "كيف", "من", "ما", "أ"}


def classify_verse(verse_tokens: list[str]) -> str:
    """Classify verse as 'imperative', 'interrogative', or 'declarative'.

    Priority: imperative > interrogative > declarative.
    - imperative: first token (or any token within first 3) matches IMPERATIVE_TOKENS
      OR verse starts with 'يا' + command-like pattern (we'll keep it strict).
    - interrogative: first token matches INTERROGATIVE_TOKENS OR starts with
      bare hamza followed by consonant (likely أ + verb/noun for interrogation).
    - else declarative.
    """
    if not verse_tokens:
        return "declarative"
    first = verse_tokens[0]
    # check imperative in first 2 tokens
    for tok in verse_tokens[:2]:
        if tok in IMPERATIVE_TOKENS:
            return "imperative"
    # interrogative
    if first in INTERROGATIVE_TOKENS:
        return "interrogative"
    # interrogative hamza prefix on first word — أ followed by ≥2 chars
    if len(first) >= 3 and first[0] == "أ":
        return "interrogative"
    return "declarative"


def compute_rhetorical_triples(surahs) -> dict[int, tuple[float, float, float]]:
    """For each surah, compute (imp%, int%, dec%) — each in [0,100]."""
    out = {}
    for s in surahs:
        counts = {"imperative": 0, "interrogative": 0, "declarative": 0}
        total = 0
        for v in s.verses:
            toks = real_words(v.text)
            cls = classify_verse(toks)
            counts[cls] += 1
            total += 1
        if total == 0:
            out[s.id] = (0.0, 0.0, 0.0)
            continue
        imp_pct = 100.0 * counts["imperative"] / total
        int_pct = 100.0 * counts["interrogative"] / total
        dec_pct = 100.0 * counts["declarative"] / total
        out[s.id] = (imp_pct, int_pct, dec_pct)
    return out


def pairwise_mean_euclidean(surah_ids: list[int], triples: dict[int, tuple[float, float, float]]) -> float:
    dists = []
    for a, b in combinations(surah_ids, 2):
        ta = triples[a]
        tb = triples[b]
        d = math.sqrt(sum((ta[i] - tb[i]) ** 2 for i in range(3)))
        dists.append(d)
    return mean(dists) if dists else 0.0


def cell_c(triples: dict[int, tuple[float, float, float]], rng: random.Random) -> dict:
    """Cell C — rhetorical-mode clustering.

    Direction = ONE-SIDED LOWER (core cluster-tight in 3-vector space).
    """
    obs = pairwise_mean_euclidean(CORE_5, triples)
    non_core = [s for s in range(1, N_SURAHS + 1) if s not in CORE_5]
    null_vals = []
    for _ in range(N_PERM):
        sample = rng.sample(non_core, 5)
        null_vals.append(pairwise_mean_euclidean(sample, triples))
    le = sum(1 for v in null_vals if v <= obs)
    p_one_sided = (1 + le) / (1 + N_PERM)
    null_mean = mean(null_vals)

    # MW-5 positive control: musabbiḥāt inner-5
    pc_non = [s for s in range(1, N_SURAHS + 1) if s not in MUSABBIHAT_INNER_5]
    pc_obs = pairwise_mean_euclidean(MUSABBIHAT_INNER_5, triples)
    pc_null = []
    for _ in range(N_PERM):
        sample = rng.sample(pc_non, 5)
        pc_null.append(pairwise_mean_euclidean(sample, triples))
    pc_le = sum(1 for v in pc_null if v <= pc_obs)
    pc_p = (1 + pc_le) / (1 + N_PERM)

    return {
        "statistic": "mean_pairwise_euclidean_in_imp_int_dec_space",
        "direction": "one-sided lower",
        "core": CORE_5,
        "core_triples": {s: list(triples[s]) for s in CORE_5},
        "observed": obs,
        "null_mean": null_mean,
        "p_one_sided_lower": p_one_sided,
        "alpha_bon": ALPHA_BON,
        "verdict": "PASS" if p_one_sided < ALPHA_BON else "NULL",
        "mw5_positive_control": {
            "cluster": "musabbihat_inner_5_Q57_59_61_62_64",
            "members": MUSABBIHAT_INNER_5,
            "observed": pc_obs,
            "null_mean": mean(pc_null),
            "p_one_sided_lower": pc_p,
            "fired_at_0.05": pc_p < 0.05,
        },
    }


# ----------------------------------------------------------------------
# Cell D — Per-surah uniqueness (9-axis descriptive profile)
# ----------------------------------------------------------------------

# Prophet-narrative lock list (same as H-NEW-125 axis 6)
PROPHET_NAME_TOKENS = {
    "موسى", "عيسى", "ابراهيم", "إبراهيم", "نوح", "يوسف", "يونس", "لوط",
    "هود", "صالح", "شعيب", "داود", "داوود", "سليمان", "زكريا", "يحيى",
    "اسماعيل", "إسماعيل", "اسحاق", "إسحاق", "يعقوب", "آدم", "ادم",
    "ايوب", "أيوب", "ادريس", "إدريس", "الياس", "إلياس", "اليسع",
    "ذا", "الكفل", "فرعون", "النبي", "نبي", "رسول", "مرسل",
}

ALLAH_TOKENS = {"الله", "لله", "اللهم"}
ALLAH_PROCLITICS = {"و", "ف", "ب", "ل", "ك", "وا", "فا", "با", "لا", "كا",
                    "وال", "فال", "بال", "لال"}


def is_allah_token(tok: str) -> bool:
    if tok in ALLAH_TOKENS:
        return True
    for p in ("و", "ف", "ب", "ل", "ك"):
        if tok.startswith(p) and tok[len(p):] in ALLAH_TOKENS:
            return True
        if tok.startswith(p + "ال") and ("ال" + tok[len(p)+2:]) in ALLAH_TOKENS:
            return True
    return False


def token_matches_prophet(tok: str) -> bool:
    if tok in PROPHET_NAME_TOKENS:
        return True
    # prefix-tolerant
    for p in ("و", "ف", "ب", "ل", "ك"):
        if tok.startswith(p) and tok[len(p):] in PROPHET_NAME_TOKENS:
            return True
    return False


def compute_profiles(
    surahs,
    root_counts: dict[int, dict[str, int]],
    noldeke: dict[int, int],
    period: dict[int, str],
    triples: dict[int, tuple[float, float, float]],
) -> dict[int, dict]:
    """9-axis descriptive profile per surah."""
    profiles = {}
    for s in surahs:
        n_verses = len(s.verses)
        all_tokens = []
        for v in s.verses:
            all_tokens.extend(real_words(v.text))
        total_tokens = len(all_tokens)
        mean_verse_len = total_tokens / n_verses if n_verses > 0 else 0.0

        allah_count = sum(1 for t in all_tokens if is_allah_token(t))
        allah_density = 100.0 * allah_count / n_verses if n_verses > 0 else 0.0

        prophet_count = sum(1 for t in all_tokens if token_matches_prophet(t))
        prophet_density = 100.0 * prophet_count / n_verses if n_verses > 0 else 0.0

        unique_roots = len(root_counts[s.id])
        root_density = unique_roots / total_tokens if total_tokens > 0 else 0.0

        # First word = first token of verse 1
        first_tok = ""
        if s.verses:
            toks0 = real_words(s.verses[0].text)
            if toks0:
                first_tok = toks0[0]

        imp, intr, dec = triples.get(s.id, (0.0, 0.0, 0.0))

        profiles[s.id] = {
            "surah_length": n_verses,
            "mean_verse_length": mean_verse_len,
            "allah_density": allah_density,
            "noldeke_rank": noldeke[s.id],
            "period": period[s.id],
            "unique_root_count": unique_roots,
            "root_density": root_density,
            "prophet_narrative_density": prophet_density,
            "first_word_token": first_tok,
            "imperative_ratio": imp,
            "interrogative_ratio": intr,
            "declarative_ratio": dec,
            "total_tokens": total_tokens,
        }
    return profiles


QUANTITATIVE_AXES = [
    "surah_length",
    "mean_verse_length",
    "allah_density",
    "noldeke_rank",
    "unique_root_count",
    "root_density",
    "prophet_narrative_density",
    "imperative_ratio",
    "interrogative_ratio",
]


def percentile_rank(value: float, all_values: list[float]) -> float:
    """Return percentile of value in all_values (0..100)."""
    n = len(all_values)
    below = sum(1 for v in all_values if v < value)
    equal = sum(1 for v in all_values if v == value)
    return 100.0 * (below + 0.5 * equal) / n


def cell_d(profiles: dict[int, dict]) -> dict:
    """For each core surah, find the axis with the most-extreme percentile
    (furthest from 50%). Report per-surah distinctive feature."""
    corpus_by_axis = {
        ax: [profiles[s][ax] for s in range(1, N_SURAHS + 1)]
        for ax in QUANTITATIVE_AXES
    }
    per_surah = []
    for s in CORE_5:
        extremes = []
        for ax in QUANTITATIVE_AXES:
            val = profiles[s][ax]
            pct = percentile_rank(val, corpus_by_axis[ax])
            extremity = abs(pct - 50.0)
            extremes.append({
                "axis": ax,
                "value": val,
                "percentile": pct,
                "extremity": extremity,
                "direction": "high" if pct >= 50 else "low",
            })
        extremes.sort(key=lambda e: -e["extremity"])
        per_surah.append({
            "surah": s,
            "name": SURAH_NAMES[s][0],
            "top_extremity_axis": extremes[0]["axis"],
            "top_extremity_direction": extremes[0]["direction"],
            "top_extremity_percentile": extremes[0]["percentile"],
            "top_extremity_value": extremes[0]["value"],
            "all_axes_sorted": extremes,
            "full_profile": {k: profiles[s][k] for k in profiles[s]},
        })
    return {
        "axes": QUANTITATIVE_AXES,
        "per_surah": per_surah,
    }


# ----------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------

def main() -> None:
    t0 = time.time()
    rng = random.Random(SEED)

    # Load data
    surahs = load_quran("no-tashkeel")
    root_counts = load_surah_root_counts()
    root_sets = {s: frozenset(root_counts[s].keys()) for s in range(1, N_SURAHS + 1)}
    noldeke = load_noldeke()
    period = load_period()

    # Compute rhetorical triples once (used by Cell C and Cell D)
    triples = compute_rhetorical_triples(surahs)

    # Cells
    # Use INDEPENDENT RNGs per cell to avoid cross-contamination
    rng_a = random.Random(SEED + 1)
    rng_c = random.Random(SEED + 3)

    a = cell_a(root_sets, rng_a)
    b = cell_b()
    c = cell_c(triples, rng_c)
    profiles = compute_profiles(surahs, root_counts, noldeke, period, triples)
    d = cell_d(profiles)

    # Profile summary table
    profile_table = []
    for s in CORE_5:
        p = profiles[s]
        profile_table.append({
            "surah": s,
            "name": SURAH_NAMES[s][0],
            "gloss": SURAH_NAMES[s][1],
            "period": p["period"],
            "noldeke_rank": p["noldeke_rank"],
            "surah_length_verses": p["surah_length"],
            "total_tokens": p["total_tokens"],
            "mean_verse_length": round(p["mean_verse_length"], 2),
            "allah_density_per_100v": round(p["allah_density"], 2),
            "unique_root_count": p["unique_root_count"],
            "prophet_narrative_density": round(p["prophet_narrative_density"], 2),
            "first_word": p["first_word_token"],
            "muqattaat_opened": False,  # pre-verified: none are muqaṭṭāʿat
            "imperative_ratio": round(p["imperative_ratio"], 2),
            "interrogative_ratio": round(p["interrogative_ratio"], 2),
            "declarative_ratio": round(p["declarative_ratio"], 2),
        })

    out = {
        "meta": {
            "id": "H-NEW-126",
            "title": "True-isolate-core characterization",
            "family": "h-new-126-isolate-core",
            "bonferroni_k": BONFERRONI_K,
            "alpha_bon": ALPHA_BON,
            "seed": SEED,
            "n_perm": N_PERM,
            "core_5": CORE_5,
            "date": "2026-04-17",
            "elapsed_seconds": None,
        },
        "profile_table": profile_table,
        "cell_a_shared_content": a,
        "cell_b_genre_coherence": b,
        "cell_c_rhetorical_mode": c,
        "cell_d_per_surah_uniqueness": d,
    }
    out["meta"]["elapsed_seconds"] = round(time.time() - t0, 3)

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-126.json"
    with out_path.open("w", encoding="utf-8") as fh:
        json.dump(out, fh, indent=2, ensure_ascii=False)

    # Print summary
    print(f"H-NEW-126 — True-isolate-core characterization")
    print(f"Seed={SEED}  n_perm={N_PERM}  alpha_bon={ALPHA_BON}")
    print(f"Elapsed: {out['meta']['elapsed_seconds']}s")
    print()
    print("=== PROFILE TABLE ===")
    for r in profile_table:
        print(f"  Q{r['surah']:3d} {r['name']:12s} ({r['gloss']:18s}) | "
              f"{r['period']:7s} | N={r['noldeke_rank']:3d} | "
              f"len={r['surah_length_verses']:3d}v "
              f"mvl={r['mean_verse_length']:5.1f} "
              f"Allah/100v={r['allah_density_per_100v']:5.1f} "
              f"roots={r['unique_root_count']:4d} "
              f"prophet={r['prophet_narrative_density']:5.2f} "
              f"first='{r['first_word']}' "
              f"imp/int/dec={r['imperative_ratio']:.1f}/{r['interrogative_ratio']:.1f}/{r['declarative_ratio']:.1f}")
    print()
    print("=== CELL A — Shared content (root-Jaccard) ===")
    print(f"  Observed mean pairwise root-Jaccard: {a['observed']:.4f}")
    print(f"  Null mean: {a['null_mean']:.4f}  p(one-sided upper)={a['p_one_sided_upper']:.4f}")
    print(f"  Verdict: {a['verdict']} (α_bon={ALPHA_BON})")
    print(f"  MW-5 ḥawāmīm {HAWAMIM_MW5}: obs={a['mw5_positive_control']['observed']:.4f} "
          f"null_mean={a['mw5_positive_control']['null_mean']:.4f} "
          f"p={a['mw5_positive_control']['p_one_sided_upper']:.4f} "
          f"fired_at_0.05={a['mw5_positive_control']['fired_at_0.05']}")
    print()
    print("=== CELL B — Genre coherence ===")
    for r in b["per_surah"]:
        print(f"  Q{r['surah']:3d} {r['name']:12s} [{r['category']:14s}] — {r['gloss']}")
    print(f"  n_concept_or_object / 5 = {b['n_concept_or_object']}")
    print(f"  Genre-coherent: {b['genre_coherent']}")
    print()
    print("=== CELL C — Rhetorical mode (3-vector Euclidean) ===")
    print(f"  Observed mean pairwise distance: {c['observed']:.3f}")
    print(f"  Null mean: {c['null_mean']:.3f}  p(one-sided lower)={c['p_one_sided_lower']:.4f}")
    print(f"  Verdict: {c['verdict']} (α_bon={ALPHA_BON})")
    print(f"  MW-5 musabbiḥāt-5 {MUSABBIHAT_INNER_5}: obs={c['mw5_positive_control']['observed']:.3f} "
          f"null_mean={c['mw5_positive_control']['null_mean']:.3f} "
          f"p={c['mw5_positive_control']['p_one_sided_lower']:.4f} "
          f"fired_at_0.05={c['mw5_positive_control']['fired_at_0.05']}")
    print()
    print("=== CELL D — Per-surah distinctive feature ===")
    for r in d["per_surah"]:
        print(f"  Q{r['surah']:3d} {r['name']:12s}: {r['top_extremity_axis']} "
              f"({r['top_extremity_direction']}, percentile={r['top_extremity_percentile']:.1f}, "
              f"value={r['top_extremity_value']})")
    print()
    print(f"JSON written: {out_path}")


if __name__ == "__main__":
    main()
