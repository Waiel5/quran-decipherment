#!/usr/bin/env python3
"""
H-NEW-62 — Comprehensive analysis of surah CLOSING verses (ḥusn al-intihāʾ).

Pre-reg: findings/phase-b-hypotheses/h-new-62-closings-prereg.md
Seed: 20260416
Locked taxonomy: see prereg (priority order PRAYER > GLORIFICATION > TAKBĪR-PAIR
> QADĪR > WARNING > PROMISE > TAWḤĪD > QUL > SALAM > NARRATIVE > OTHER).
"""

from __future__ import annotations

import csv
import json
import math
import os
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text" / "quran-no-tashkeel.json"
REVELATION_CSV = ROOT / "data" / "revelation-order.csv"
OUT_JSON = ROOT / "findings" / "phase-b-hypotheses" / "csv" / "h-new-62.json"

SEED = 20260416
random.seed(SEED)

MUQATTAAT_SURAHS = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30,
                    31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
PROPHET_NAMED = {10, 11, 12, 14, 47, 71}

# Locked closing-class taxonomy (priority order from prereg).
PAIRED_ATTRIBUTES = {
    "الحكيم العليم", "العليم الحكيم", "الغفور الرحيم", "الرحيم الغفور",
    "العزيز الحكيم", "الحكيم العزيز", "السميع البصير", "البصير السميع",
    "العزيز الرحيم", "الرحيم العزيز", "الغفور الودود", "الودود الغفور",
    "التواب الرحيم", "الرحيم التواب", "الرءوف الرحيم", "الرحيم الرءوف",
    "الغفور الحليم", "الحليم الغفور", "الواسع العليم", "العليم الواسع",
    "العزيز الغفور", "الغفور العزيز", "الرحمن الرحيم", "الرحيم الرحمن",
    "البر الرحيم",
}

PRAYER_TRIGGERS = {
    "ربنا اغفر", "ربنا تقبل", "ربنا انصرنا", "ربنا اهدنا", "ربنا آتنا",
    "ربنا لا تؤاخذنا", "ربنا لا تحملنا", "ربنا لا تجعلنا", "ربنا اجعل",
    "أنت مولانا", "انت مولانا", "اغفر لنا", "اهدنا الصراط",
}

GLORIFICATION_TRIGGERS = {
    "سبحان", "تسبيح", "تبارك", "الحمد لله", "رب العالمين",
}
GLORIFICATION_PREFIXES = ("سبح", )  # token-initial prefix triggers

QADIR_TRIGGERS = {
    "على كل شيء قدير", "بكل شيء عليم", "بكل شيء محيط", "بكل شيء قدير",
}

WARNING_TRIGGERS = {
    "النار", "جهنم", "العذاب", "عذاب اليم", "عذاب أليم", "يوم القيامة",
    "يوم الدين", "يصلى", "يصلون", "الكافرين", "الظالمين", "يخسرون",
    "الخاسرين", "بئس", "نار جهنم",
}

PROMISE_TRIGGERS = {
    "الجنة", "جنات", "النعيم", "الفائزين", "المفلحون", "يفلحون",
    "أجر", "أجرا", "الصالحين", "المحسنين", "حسنا",
}

TAWHID_TRIGGERS = {
    "لا اله الا", "لا إله إلا", "هو الله", "هو الواحد", "هو القهار", "هو الحق",
    "هو الواحد القهار", "هو الأول والآخر",
}

QUL_TRIGGERS = {"يا أيها النبي", "يا أيها الرسول", "فقل"}
SALAM_TRIGGERS = {"سلام", "السلام"}

NARRATIVE_TRIGGERS = {
    "كان", "كانوا", "قال", "قالوا", "أرسلنا", "جعلنا", "خلقنا", "أنزلنا",
}


def normalize(s: str) -> str:
    """Already no-tashkeel; just collapse whitespace."""
    return " ".join(s.strip().split())


def has_any(text: str, patterns) -> bool:
    return any(p in text for p in patterns)


def starts_with_token(text: str, tok: str) -> bool:
    toks = text.split()
    return bool(toks) and toks[0] == tok


def trailing_two(text: str) -> str:
    toks = text.split()
    if len(toks) < 2:
        return ""
    return f"{toks[-2]} {toks[-1]}"


def classify(text: str) -> tuple[str, list[str]]:
    """Return (primary_class, multi_class_flags) per locked taxonomy."""
    t = normalize(text)
    flags: list[str] = []

    # Track all hits as flags (for multi-label diagnostic).
    hits = {}
    hits["PRAYER"] = has_any(t, PRAYER_TRIGGERS) or starts_with_token(t, "رب") or t.startswith("ربنا")
    hits["GLORIFICATION"] = has_any(t, GLORIFICATION_TRIGGERS) or any(
        tok.startswith(p) for tok in t.split() for p in GLORIFICATION_PREFIXES
    )
    hits["TAKBIR_PAIR"] = trailing_two(t) in PAIRED_ATTRIBUTES
    hits["QADIR"] = has_any(t, QADIR_TRIGGERS)
    hits["WARNING"] = has_any(t, WARNING_TRIGGERS)
    hits["PROMISE"] = has_any(t, PROMISE_TRIGGERS)
    hits["TAWHID"] = has_any(t, TAWHID_TRIGGERS)
    hits["QUL"] = starts_with_token(t, "قل") or has_any(t, QUL_TRIGGERS)
    hits["SALAM"] = has_any(t, SALAM_TRIGGERS)
    hits["NARRATIVE"] = has_any(t, NARRATIVE_TRIGGERS)

    flags = [k for k, v in hits.items() if v]

    priority = ["PRAYER", "GLORIFICATION", "TAKBIR_PAIR", "QADIR", "WARNING",
                "PROMISE", "TAWHID", "QUL", "SALAM", "NARRATIVE"]
    for c in priority:
        if hits[c]:
            return c, flags
    return "OTHER", flags


def shannon_entropy(counter: Counter) -> float:
    n = sum(counter.values())
    if n == 0:
        return 0.0
    h = 0.0
    for v in counter.values():
        if v > 0:
            p = v / n
            h -= p * math.log2(p)
    return h


def wilcoxon_signed_rank(diffs):
    """Two-sided Wilcoxon signed-rank without scipy. Returns (W, p_normal_approx)."""
    nz = [d for d in diffs if d != 0]
    n = len(nz)
    if n == 0:
        return 0.0, 1.0
    abs_d = [abs(d) for d in nz]
    # Average ranks for ties.
    order = sorted(range(n), key=lambda i: abs_d[i])
    ranks = [0.0] * n
    i = 0
    while i < n:
        j = i
        while j + 1 < n and abs_d[order[j + 1]] == abs_d[order[i]]:
            j += 1
        avg = (i + j) / 2.0 + 1.0  # average rank (1-indexed)
        for k in range(i, j + 1):
            ranks[order[k]] = avg
        i = j + 1
    W_pos = sum(ranks[i] for i in range(n) if nz[i] > 0)
    W_neg = sum(ranks[i] for i in range(n) if nz[i] < 0)
    W = min(W_pos, W_neg)
    # Normal approximation
    mu = n * (n + 1) / 4.0
    sigma = math.sqrt(n * (n + 1) * (2 * n + 1) / 24.0)
    if sigma == 0:
        return W, 1.0
    z = (W - mu) / sigma
    # Two-sided p
    p = math.erfc(abs(z) / math.sqrt(2))
    return W, p


def chi_square(observed):
    """observed: 2D list (rows × cols). Returns (chi2, dof, p_normal_chi2_approx)."""
    rows = len(observed)
    cols = len(observed[0]) if rows else 0
    if rows == 0 or cols == 0:
        return 0.0, 0, 1.0
    row_sums = [sum(r) for r in observed]
    col_sums = [sum(observed[r][c] for r in range(rows)) for c in range(cols)]
    n = sum(row_sums)
    if n == 0:
        return 0.0, 0, 1.0
    chi2 = 0.0
    for r in range(rows):
        for c in range(cols):
            e = row_sums[r] * col_sums[c] / n
            if e > 0:
                chi2 += (observed[r][c] - e) ** 2 / e
    dof = (rows - 1) * (cols - 1)
    # Wilson-Hilferty approximation for chi2 -> normal
    if dof <= 0:
        return chi2, dof, 1.0
    h = 2.0 / (9.0 * dof)
    z = ((chi2 / dof) ** (1.0 / 3.0) - (1 - h)) / math.sqrt(h)
    p = 0.5 * math.erfc(z / math.sqrt(2))
    return chi2, dof, p


def hypergeom_sf(k, M, K, N):
    """P(X >= k) for hypergeometric(M, K, N). M=pop, K=successes-in-pop, N=draws."""
    # Sum k..min(K,N)
    upper = min(K, N)
    if k > upper:
        return 0.0
    total = 0.0
    log_C_M_N = log_choose(M, N)
    for x in range(k, upper + 1):
        log_p = log_choose(K, x) + log_choose(M - K, N - x) - log_C_M_N
        total += math.exp(log_p)
    return min(1.0, max(0.0, total))


def log_choose(n, k):
    if k < 0 or k > n:
        return float("-inf")
    return (math.lgamma(n + 1) - math.lgamma(k + 1) - math.lgamma(n - k + 1))


def main():
    quran = json.load(open(QURAN_JSON))
    rev = {}
    with open(REVELATION_CSV) as f:
        reader = csv.DictReader(f)
        for row in reader:
            rev[int(row["mushaf_order"])] = row

    # Per-surah: closing text + tokens + last token + class + flags + mean len
    rows = []
    all_last_tokens = Counter()
    closing_last_tokens = Counter()
    diffs = []  # (closing_len - surah_mean_len) for T1
    closings_by_period = defaultdict(list)
    closings_by_muq = defaultdict(list)
    closings_index = {}  # surah_id -> closing string
    surah_internal_lens = {}  # surah_id -> list of verse-len ints
    surah_internal_verses = {}  # surah_id -> list of verse strings

    for surah in quran:
        sid = surah["id"]
        verses = surah["verses"]
        lens = [len(normalize(v["text"]).split()) for v in verses]
        surah_internal_lens[sid] = lens
        surah_internal_verses[sid] = [normalize(v["text"]) for v in verses]
        mean_len = sum(lens) / len(lens) if lens else 0.0
        closing = normalize(verses[-1]["text"])
        closing_index = verses[-1]["id"]
        closing_tokens = closing.split()
        closing_len = len(closing_tokens)
        last_token = closing_tokens[-1] if closing_tokens else ""

        for vtext in surah_internal_verses[sid]:
            tokens = vtext.split()
            if tokens:
                all_last_tokens[tokens[-1]] += 1
        closing_last_tokens[last_token] += 1

        period = rev.get(sid, {}).get("period", "Unknown")
        is_muq = sid in MUQATTAAT_SURAHS
        is_proph = sid in PROPHET_NAMED
        primary_class, flags = classify(closing)

        diffs.append(closing_len - mean_len)
        closings_by_period[period].append(primary_class)
        closings_by_muq["MUQ" if is_muq else "NONMUQ"].append(primary_class)
        closings_index[sid] = closing

        rows.append({
            "surah_id": sid,
            "surah_name_ar": surah["name"],
            "surah_name_tl": surah["transliteration"],
            "period": period,
            "muqattaat": is_muq,
            "prophet_named": is_proph,
            "closing_verse_id": closing_index,
            "closing_text": closing,
            "closing_tokens": closing_len,
            "last_token": last_token,
            "primary_class": primary_class,
            "multi_class_flags": flags,
            "surah_mean_len": round(mean_len, 3),
            "diff_close_minus_mean": round(closing_len - mean_len, 3),
        })

    # ---- T1 paired Wilcoxon
    W, p_w = wilcoxon_signed_rank(diffs)
    median_diff = sorted(diffs)[len(diffs) // 2]
    # Bootstrap 95% CI on median diff
    rng = random.Random(SEED)
    boots = []
    for _ in range(5000):
        sample = [diffs[rng.randrange(len(diffs))] for _ in diffs]
        s = sorted(sample)
        boots.append(s[len(s) // 2])
    boots.sort()
    ci_lo, ci_hi = boots[int(0.025 * len(boots))], boots[int(0.975 * len(boots))]

    # ---- T2 closing word entropy vs all-verse-end entropy + bootstrap
    H_close = shannon_entropy(closing_last_tokens)
    H_all = shannon_entropy(all_last_tokens)
    # Bootstrap on H_close: resample 114 closings with replacement
    closing_last_list = [r["last_token"] for r in rows]
    boot_close = []
    for _ in range(5000):
        sample = [closing_last_list[rng.randrange(114)] for _ in range(114)]
        boot_close.append(shannon_entropy(Counter(sample)))
    boot_close.sort()
    H_close_lo = boot_close[int(0.025 * len(boot_close))]
    H_close_hi = boot_close[int(0.975 * len(boot_close))]
    # Reference distribution: sample 114 last-tokens of any verse
    boot_ref = []
    all_last_list = list(all_last_tokens.elements())
    for _ in range(5000):
        sample = [all_last_list[rng.randrange(len(all_last_list))] for _ in range(114)]
        boot_ref.append(shannon_entropy(Counter(sample)))
    boot_ref.sort()
    ref_lo, ref_hi = boot_ref[int(0.025 * len(boot_ref))], boot_ref[int(0.975 * len(boot_ref))]

    # ---- T3 paired-attribute fawāṣil at closings — Monte Carlo within surah
    obs_pair_close = sum(1 for r in rows if trailing_two(r["closing_text"]) in PAIRED_ATTRIBUTES)
    # MC: for each surah, pick a random verse uniformly; count how many trailing-two are paired-attr
    mc_counts = []
    for _ in range(5000):
        c = 0
        for sid, vlist in surah_internal_verses.items():
            v = vlist[rng.randrange(len(vlist))]
            if trailing_two(v) in PAIRED_ATTRIBUTES:
                c += 1
        mc_counts.append(c)
    mc_counts_sorted = sorted(mc_counts)
    mc_mean_pair = sum(mc_counts) / len(mc_counts)
    p_t3 = sum(1 for c in mc_counts if c >= obs_pair_close) / len(mc_counts)

    # ---- T4 omni-competence formula at closings
    formula = "على كل شيء قدير"
    obs_t4 = sum(1 for r in rows if formula in r["closing_text"])
    # Total verses with the formula across the corpus + total verses
    total_verses = sum(len(v) for v in surah_internal_verses.values())
    total_with_formula = sum(
        1 for vlist in surah_internal_verses.values() for v in vlist if formula in v
    )
    # Hypergeometric: 114 draws (closings) from total_verses, total_with_formula successes,
    # observed obs_t4 successes.
    p_t4 = hypergeom_sf(obs_t4, total_verses, total_with_formula, 114)

    # ---- T5 Meccan vs Medinan closing-class chi-square
    classes = sorted({r["primary_class"] for r in rows})
    periods = sorted({r["period"] for r in rows})
    table_p = [[sum(1 for r in rows if r["period"] == p and r["primary_class"] == c)
                for c in classes] for p in periods]
    chi_p, dof_p, p_t5 = chi_square(table_p)

    # ---- T6 muqaṭṭaʿāt vs non-muqaṭṭaʿāt
    table_m = [
        [sum(1 for r in rows if r["muqattaat"] == True and r["primary_class"] == c) for c in classes],
        [sum(1 for r in rows if r["muqattaat"] == False and r["primary_class"] == c) for c in classes],
    ]
    chi_m, dof_m, p_t6 = chi_square(table_m)

    # ---- T7 twin-closings: ≥4-token contiguous suffix shared between two surahs
    def suffix_tokens(text, n):
        toks = text.split()
        return tuple(toks[-n:]) if len(toks) >= n else None

    twin_pairs = []
    suffix4_map = defaultdict(list)
    for r in rows:
        sfx = suffix_tokens(r["closing_text"], 4)
        if sfx:
            suffix4_map[sfx].append(r["surah_id"])
    for sfx, ids in suffix4_map.items():
        if len(ids) >= 2:
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    twin_pairs.append({"surah_a": ids[i], "surah_b": ids[j],
                                       "suffix": " ".join(sfx)})
    obs_twin = len(twin_pairs)

    # MC null: shuffle closing-token sequences across surahs (choose random verse per surah)
    twin_null = []
    for _ in range(5000):
        sm = defaultdict(list)
        for sid, vlist in surah_internal_verses.items():
            v = vlist[rng.randrange(len(vlist))]
            sfx = suffix_tokens(v, 4)
            if sfx:
                sm[sfx].append(sid)
        c = 0
        for sfx, ids in sm.items():
            if len(ids) >= 2:
                c += len(ids) * (len(ids) - 1) // 2
        twin_null.append(c)
    twin_null_sorted = sorted(twin_null)
    p_t7 = sum(1 for c in twin_null if c >= obs_twin) / len(twin_null)

    # ---- 3-token sensitivity for twin pairs
    suffix3_map = defaultdict(list)
    for r in rows:
        sfx = suffix_tokens(r["closing_text"], 3)
        if sfx:
            suffix3_map[sfx].append(r["surah_id"])
    twin3_pairs = []
    for sfx, ids in suffix3_map.items():
        if len(ids) >= 2:
            for i in range(len(ids)):
                for j in range(i + 1, len(ids)):
                    twin3_pairs.append({"surah_a": ids[i], "surah_b": ids[j],
                                        "suffix": " ".join(sfx)})

    # ---- Last-token frequency report
    top_last = closing_last_tokens.most_common(20)

    # ---- Closing-class counts
    class_counts = Counter(r["primary_class"] for r in rows)

    # ---- Formulaic closings inventory: scan a list of candidate phrases
    candidate_formulas = [
        "على كل شيء قدير",
        "بكل شيء عليم",
        "بكل شيء محيط",
        "العزيز الحكيم",
        "الحكيم العليم",
        "الغفور الرحيم",
        "الرحيم الغفور",
        "السميع البصير",
        "الرحمن الرحيم",
        "العزيز الرحيم",
        "العزيز الغفور",
        "الواسع العليم",
        "التواب الرحيم",
        "الرءوف الرحيم",
        "الحمد لله",
        "الحمد لله رب العالمين",
        "رب العالمين",
        "لا اله الا",
        "سبحان",
        "تبارك",
        "اهدنا الصراط",
        "ربنا اغفر",
        "الجنة",
        "النار",
        "العذاب",
        "المفلحون",
        "يفلحون",
        "الفائزين",
        "الصراط المستقيم",
    ]
    formula_counts = []
    for ph in candidate_formulas:
        c_close = sum(1 for r in rows if ph in r["closing_text"])
        c_anywhere = sum(
            1 for vlist in surah_internal_verses.values() for v in vlist if ph in v
        )
        # Hypergeometric enrichment
        p = hypergeom_sf(c_close, total_verses, c_anywhere, 114) if c_anywhere > 0 else 1.0
        formula_counts.append({
            "phrase": ph,
            "in_closings": c_close,
            "in_corpus_verses": c_anywhere,
            "hypergeom_p_enrichment": p,
        })

    # ---- Bonferroni summary
    alpha_bonf = 0.05 / 7

    # Bootstrap p for T2 (whether H_close < H_all): compute fraction of boot_close >= ref_lo, etc.
    # Simpler: count how many bootstrap samples of 114-from-corpus-verse-endings yield H <= H_close
    p_t2 = sum(1 for h in boot_ref if h <= H_close) / len(boot_ref)

    summary = {
        "seed": SEED,
        "alpha_bonferroni_per_test": alpha_bonf,
        "n_surahs": len(rows),
        "n_verses_total": total_verses,
        "T1_length": {
            "wilcoxon_W": W,
            "p_two_sided_normal_approx": p_w,
            "median_diff_close_minus_mean": median_diff,
            "ci95_bootstrap": [ci_lo, ci_hi],
            "mean_diff": sum(diffs) / len(diffs),
            "PASS": (p_w < alpha_bonf and abs(median_diff) > 1),
        },
        "T2_closing_token_entropy": {
            "H_close": H_close,
            "H_all_verse_endings": H_all,
            "H_close_bootstrap_ci95": [H_close_lo, H_close_hi],
            "H_ref_bootstrap_ci95": [ref_lo, ref_hi],
            "p_one_sided_H_close_le_random": p_t2,
            "PASS": (p_t2 < alpha_bonf),
        },
        "T3_paired_attributes_at_closing": {
            "observed": obs_pair_close,
            "expected_mc": mc_mean_pair,
            "p_one_sided_mc": p_t3,
            "PASS": (p_t3 < alpha_bonf),
        },
        "T4_qadir_formula_at_closing": {
            "phrase": formula,
            "in_closings": obs_t4,
            "in_corpus_verses": total_with_formula,
            "p_hypergeom_one_sided": p_t4,
            "PASS": (p_t4 < alpha_bonf),
        },
        "T5_period_x_class": {
            "rows_periods": periods,
            "cols_classes": classes,
            "table": table_p,
            "chi2": chi_p,
            "dof": dof_p,
            "p_two_sided_approx": p_t5,
            "PASS": (p_t5 < alpha_bonf),
        },
        "T6_muqattaat_x_class": {
            "rows_muq": ["MUQ", "NONMUQ"],
            "cols_classes": classes,
            "table": table_m,
            "chi2": chi_m,
            "dof": dof_m,
            "p_two_sided_approx": p_t6,
            "PASS": (p_t6 < alpha_bonf),
        },
        "T7_twin_closings_4tok": {
            "observed_pairs": obs_twin,
            "twin_pairs": twin_pairs,
            "p_one_sided_mc": p_t7,
            "mc_mean": sum(twin_null) / len(twin_null),
            "PASS": (p_t7 < alpha_bonf),
        },
        "T7_sensitivity_3tok": {
            "observed_pairs": len(twin3_pairs),
            "twin_pairs": twin3_pairs,
        },
        "top_last_tokens_at_closing": top_last,
        "closing_class_counts": dict(class_counts.most_common()),
        "formulaic_closings_inventory": formula_counts,
        "MW5_check_prayer_at_closings": {
            "prayer_class_count": class_counts.get("PRAYER", 0),
            "prayer_class_surahs": [r["surah_id"] for r in rows
                                    if r["primary_class"] == "PRAYER"],
        },
    }

    output = {
        "metadata": {
            "id": "H-NEW-62",
            "seed": SEED,
            "rules_tuple": "no-tashkeel; canonical 1..114 mushaf order; "
                           "LAST verse = highest verse-id; whitespace tokenization",
            "prereg": "findings/phase-b-hypotheses/h-new-62-closings-prereg.md",
        },
        "per_surah": rows,
        "summary": summary,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    # Echo headline
    print(f"Wrote: {OUT_JSON}")
    print(f"Closing-class distribution: {class_counts.most_common()}")
    print(f"T1 length Wilcoxon W={W:.2f}, p={p_w:.4g}, median_diff={median_diff}, "
          f"ci95=[{ci_lo}, {ci_hi}], PASS={summary['T1_length']['PASS']}")
    print(f"T2 H_close={H_close:.4f}, H_all={H_all:.4f}, p={p_t2:.4g}, "
          f"PASS={summary['T2_closing_token_entropy']['PASS']}")
    print(f"T3 paired-attr at closings: obs={obs_pair_close}, mc_mean={mc_mean_pair:.2f}, "
          f"p={p_t3:.4g}, PASS={summary['T3_paired_attributes_at_closing']['PASS']}")
    print(f"T4 qadir-formula at closings: obs={obs_t4}, in_corpus={total_with_formula}, "
          f"p={p_t4:.4g}, PASS={summary['T4_qadir_formula_at_closing']['PASS']}")
    print(f"T5 period×class chi2={chi_p:.2f} dof={dof_p} p={p_t5:.4g} "
          f"PASS={summary['T5_period_x_class']['PASS']}")
    print(f"T6 muq×class chi2={chi_m:.2f} dof={dof_m} p={p_t6:.4g} "
          f"PASS={summary['T6_muqattaat_x_class']['PASS']}")
    print(f"T7 twin (4tok): obs={obs_twin} pairs, mc_mean={summary['T7_twin_closings_4tok']['mc_mean']:.2f}, "
          f"p={p_t7:.4g}, PASS={summary['T7_twin_closings_4tok']['PASS']}")
    print(f"T7 sensitivity (3tok): {len(twin3_pairs)} pairs")
    print(f"MW-5 prayer-closings: {class_counts.get('PRAYER', 0)} surahs")
    print(f"alpha_bonferroni = {alpha_bonf:.4g}")


if __name__ == "__main__":
    main()
