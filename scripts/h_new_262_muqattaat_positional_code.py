#!/usr/bin/env python3
"""H-NEW-262 — Muqatta'at positional code.

Compare the within-verse position distribution of each of the 14
muqaṭṭaʿat letters inside muq-opened surahs versus non-muq-opened
surahs, using the canonical `load_quran("no-tashkeel")` pipeline.

Primary family:
  - 14 per-letter Mann-Whitney U tests
  - alternative = "greater"
  - direction = the same letter falls later within verses in
    muq-opened surahs than in non-muq-opened surahs
  - Bonferroni k = 14

Secondary / descriptive:
  - two-sided KS test per letter
  - mean/median position shift
  - bin-10 relative risk (p >= 0.9)

Positive control:
  - pooled-corpus bin-10 density should remain high for rhyme letters
    {ن, ر, ي} and low for prefix-heavy letters {ا, ل}.
"""

from __future__ import annotations

import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np
from scipy import stats

ROOT = Path("/Users/grey/Downloads/quran")
PREREG_FILE = (
    ROOT / "findings/phase-b-hypotheses/h-new-262-muqattaat-positional-code-prereg.md"
)
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-262.json"
SEED = 20260418
BON_K = 14
ALPHA_BON = 0.05 / BON_K

sys.path.insert(0, str(ROOT))
from analysis.tools.loader import load_quran  # noqa: E402

ALPHA28 = [
    "ا",
    "ب",
    "ت",
    "ث",
    "ج",
    "ح",
    "خ",
    "د",
    "ذ",
    "ر",
    "ز",
    "س",
    "ش",
    "ص",
    "ض",
    "ط",
    "ظ",
    "ع",
    "غ",
    "ف",
    "ق",
    "ك",
    "ل",
    "م",
    "ن",
    "ه",
    "و",
    "ي",
]

MUQ14 = ["ا", "ل", "م", "ص", "ر", "ك", "ه", "ي", "ع", "ط", "س", "ح", "ق", "ن"]
MUQ_SURAHS = {
    2,
    3,
    7,
    10,
    11,
    12,
    13,
    14,
    15,
    19,
    20,
    26,
    27,
    28,
    29,
    30,
    31,
    32,
    36,
    38,
    40,
    41,
    42,
    43,
    44,
    45,
    46,
    50,
    68,
}

NORMALIZE_MAP = {
    "أ": "ا",
    "إ": "ا",
    "آ": "ا",
    "ٱ": "ا",
    "ة": "ه",
    "ى": "ي",
    "ؤ": "و",
    "ئ": "ي",
}

EXCLUDED_MARKS = set("ۖۗۘۙۚۛۜ۞۩")

POSITIVE_CONTROL_THRESHOLDS = {
    "high_bin10_letters": {"ن": 0.13, "ر": 0.13, "ي": 0.13},
    "low_bin10_letters": {"ا": 0.10, "ل": 0.10},
}


def normalize_verse(text: str) -> str:
    """Map the canonical no-tashkeel verse to the 28-letter alphabet."""
    out: list[str] = []
    for ch in text:
        if ch == " " or ch in EXCLUDED_MARKS or ch == "ء":
            continue
        normalized = NORMALIZE_MAP.get(ch, ch)
        if normalized in ALPHA28:
            out.append(normalized)
    return "".join(out)


def median(values: np.ndarray) -> float:
    if values.size == 0:
        return math.nan
    return float(np.median(values))


def main() -> None:
    prereg_sha256 = hashlib.sha256(PREREG_FILE.read_bytes()).hexdigest()

    positions = {
        letter: {"muq_opened": [], "non_muq_opened": []}
        for letter in MUQ14
    }
    positive_control = {
        letter: {
            "overall_total": 0,
            "overall_bin10": 0,
            "muq_opened_total": 0,
            "muq_opened_bin10": 0,
            "non_muq_opened_total": 0,
            "non_muq_opened_bin10": 0,
        }
        for letter in {"ن", "ر", "ي", "ا", "ل"}
    }

    muq_opened_verses = 0
    non_muq_opened_verses = 0
    muq_opened_letters = 0
    non_muq_opened_letters = 0

    surahs = load_quran("no-tashkeel")
    for surah in surahs:
        group = "muq_opened" if surah.id in MUQ_SURAHS else "non_muq_opened"
        for verse in surah.verses:
            normalized = normalize_verse(verse.text)
            length = len(normalized)
            if group == "muq_opened":
                muq_opened_verses += 1
                muq_opened_letters += length
            else:
                non_muq_opened_verses += 1
                non_muq_opened_letters += length
            if length == 0:
                continue
            for idx, ch in enumerate(normalized):
                pos = (idx + 0.5) / length
                if ch in positions:
                    positions[ch][group].append(pos)
                if ch in positive_control:
                    rec = positive_control[ch]
                    rec["overall_total"] += 1
                    rec[f"{group}_total"] += 1
                    if pos >= 0.9:
                        rec["overall_bin10"] += 1
                        rec[f"{group}_bin10"] += 1

    letter_results: dict[str, dict[str, object]] = {}
    preregistered_hits: list[str] = []
    reverse_hits: list[str] = []
    pvals_greater: list[float] = []
    positive_delta_count = 0

    for letter in MUQ14:
        muq_arr = np.asarray(positions[letter]["muq_opened"], dtype=float)
        non_arr = np.asarray(positions[letter]["non_muq_opened"], dtype=float)

        if muq_arr.size == 0 or non_arr.size == 0:
            raise RuntimeError(f"empty sample for letter {letter}")

        mean_muq = float(muq_arr.mean())
        mean_non = float(non_arr.mean())
        delta_mean = mean_muq - mean_non
        if delta_mean > 0:
            positive_delta_count += 1

        mwu_greater = stats.mannwhitneyu(
            muq_arr,
            non_arr,
            alternative="greater",
            method="asymptotic",
        )
        mwu_less = stats.mannwhitneyu(
            muq_arr,
            non_arr,
            alternative="less",
            method="asymptotic",
        )
        ks = stats.ks_2samp(muq_arr, non_arr, alternative="two-sided")

        density_bin10_muq = float(np.mean(muq_arr >= 0.9))
        density_bin10_non = float(np.mean(non_arr >= 0.9))
        density_bin1_muq = float(np.mean(muq_arr < 0.1))
        density_bin1_non = float(np.mean(non_arr < 0.1))
        rr_bin10 = density_bin10_muq / density_bin10_non
        rr_bin1 = density_bin1_muq / density_bin1_non

        auc = float(mwu_greater.statistic / (muq_arr.size * non_arr.size))
        bonf_preregistered = bool(mwu_greater.pvalue < ALPHA_BON)
        bonf_reverse = bool(mwu_less.pvalue < ALPHA_BON)
        if bonf_preregistered:
            preregistered_hits.append(letter)
        if bonf_reverse:
            reverse_hits.append(letter)
        pvals_greater.append(max(float(mwu_greater.pvalue), 1e-300))

        letter_results[letter] = {
            "n_muq_opened": int(muq_arr.size),
            "n_non_muq_opened": int(non_arr.size),
            "mean_position_muq_opened": mean_muq,
            "mean_position_non_muq_opened": mean_non,
            "delta_mean_position": delta_mean,
            "median_position_muq_opened": median(muq_arr),
            "median_position_non_muq_opened": median(non_arr),
            "mann_whitney_u_greater": float(mwu_greater.statistic),
            "p_one_sided_greater": float(mwu_greater.pvalue),
            "p_one_sided_less": float(mwu_less.pvalue),
            "common_language_auc": auc,
            "ks_statistic": float(ks.statistic),
            "ks_p_two_sided": float(ks.pvalue),
            "density_bin10_muq_opened": density_bin10_muq,
            "density_bin10_non_muq_opened": density_bin10_non,
            "rr_bin10": rr_bin10,
            "density_bin1_muq_opened": density_bin1_muq,
            "density_bin1_non_muq_opened": density_bin1_non,
            "rr_bin1": rr_bin1,
            "bonferroni_survives_preregistered_direction": bonf_preregistered,
            "bonferroni_survives_reverse_direction_exploratory": bonf_reverse,
        }

    stouffer_z = float(
        sum(stats.norm.isf(p) for p in pvals_greater) / math.sqrt(len(pvals_greater))
    )
    stouffer_p = float(stats.norm.sf(stouffer_z))

    positive_control_results: dict[str, dict[str, object]] = {}
    positive_control_pass = True

    for letter, rec in positive_control.items():
        overall_density = rec["overall_bin10"] / rec["overall_total"]
        muq_density = rec["muq_opened_bin10"] / rec["muq_opened_total"]
        non_density = rec["non_muq_opened_bin10"] / rec["non_muq_opened_total"]

        if letter in POSITIVE_CONTROL_THRESHOLDS["high_bin10_letters"]:
            threshold = POSITIVE_CONTROL_THRESHOLDS["high_bin10_letters"][letter]
            direction = ">"
            passed = overall_density > threshold
        else:
            threshold = POSITIVE_CONTROL_THRESHOLDS["low_bin10_letters"][letter]
            direction = "<"
            passed = overall_density < threshold
        positive_control_pass = positive_control_pass and passed

        positive_control_results[letter] = {
            "overall_total": rec["overall_total"],
            "overall_bin10_density": overall_density,
            "muq_opened_bin10_density": muq_density,
            "non_muq_opened_bin10_density": non_density,
            "threshold": threshold,
            "direction": direction,
            "pass": passed,
        }

    if not positive_control_pass:
        overall_verdict = "INSTRUMENT-FAIL"
    elif len(preregistered_hits) >= 3:
        overall_verdict = "PASS-DIRECTED"
    elif len(preregistered_hits) >= 1:
        overall_verdict = "MIXED-LETTER-SPECIFIC"
    else:
        overall_verdict = "NULL"

    output = {
        "finding_id": "H-NEW-262",
        "title": "Muqatta'at positional code: per-letter within-verse positions in muq-opened vs non-muq-opened surahs",
        "date": "2026-04-18",
        "seed": SEED,
        "prereg_sha256": prereg_sha256,
        "rules_tuple": {
            "corpus": "analysis.tools.loader.load_quran('no-tashkeel')",
            "basmala_policy": "default canonical JSON state (counted only in surah 1 by construction)",
            "letter_definition": "character-level 28-letter normalization",
            "position_stat": "(i + 0.5) / verse_length",
        },
        "corpus_anchor": {
            "surahs_total": 114,
            "muq_opened_surahs": len(MUQ_SURAHS),
            "non_muq_opened_surahs": 114 - len(MUQ_SURAHS),
            "verses_total": muq_opened_verses + non_muq_opened_verses,
            "muq_opened_verses": muq_opened_verses,
            "non_muq_opened_verses": non_muq_opened_verses,
            "normalized_letters_total": muq_opened_letters + non_muq_opened_letters,
            "muq_opened_normalized_letters": muq_opened_letters,
            "non_muq_opened_normalized_letters": non_muq_opened_letters,
        },
        "bonferroni": {
            "k": BON_K,
            "alpha_bon": ALPHA_BON,
            "family": "h-new-262-letterwise-muq-positional-code",
            "primary_test": "14 one-sided Mann-Whitney U tests (muq-opened later than non-muq-opened)",
        },
        "preregistered_direction": (
            "later within-verse positions for the same letter inside muq-opened surahs"
        ),
        "letters_tested": MUQ14,
        "per_letter_results": letter_results,
        "family_summary": {
            "preregistered_hits_bonferroni_14": preregistered_hits,
            "reverse_direction_hits_bonferroni_14_exploratory": reverse_hits,
            "positive_delta_count": positive_delta_count,
            "negative_or_zero_delta_count": len(MUQ14) - positive_delta_count,
            "stouffer_z_preregistered_direction_descriptive": stouffer_z,
            "stouffer_p_preregistered_direction_descriptive": stouffer_p,
        },
        "positive_control": {
            "description": (
                "Pooled-corpus bin-10 densities should remain high for rhyme letters "
                "{ن, ر, ي} and low for prefix-heavy letters {ا, ل} under the same "
                "normalization and position-binning instrument."
            ),
            "thresholds": POSITIVE_CONTROL_THRESHOLDS,
            "per_letter": positive_control_results,
            "pass": positive_control_pass,
        },
        "overall_verdict": overall_verdict,
    }

    OUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False))

    print("=" * 72)
    print("H-NEW-262 — Muqatta'at positional code")
    print("=" * 72)
    print(
        f"Bonferroni-14 alpha = {ALPHA_BON:.9f}; "
        f"preregistered hits = {preregistered_hits or 'none'}"
    )
    print(f"Exploratory reverse hits = {reverse_hits or 'none'}")
    print(f"Positive control pass = {positive_control_pass}")
    print(f"Overall verdict = {overall_verdict}")
    print(f"Wrote {OUT_JSON}")


if __name__ == "__main__":
    main()
