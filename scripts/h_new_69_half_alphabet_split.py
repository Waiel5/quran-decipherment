"""H-NEW-69 — Half-alphabet split: muqaṭṭaʿāt vs classical 14-of-28 groupings.

Pre-reg: findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md

Closed-form exact hypergeometric test for each of 8 locked classical groupings.
Bonferroni-8 family (α_per_grouping = 0.05/8 = 0.00625).

Question: does the 14 muqaṭṭaʿāt letter selection match a classical Arabic
phonological 14-of-28 partition (sun/moon, voiced/voiceless, etc.)?

Auxiliary phonotactic descriptors (sonorant/stop/fricative counts) reported
descriptively only — NOT in Bonferroni family.

MW-5 positive control: planted U_planted = G1 (sun letters); pipeline must
detect at p < 1e-7. MW-5b: G1 with 1 swap; pipeline must detect at p < 1e-3.

MW-7 internal-error gate.

Seed 20260415 reserved (closed-form test, no sampling needed for primary).
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
from math import comb

REPO = "/Users/grey/Downloads/quran"

# ---------------------------------------------------------------------------
# Locked alphabet + muqaṭṭaʿāt set
# ---------------------------------------------------------------------------

# 28-letter Arabic orthographic alphabet (alif first, yāʾ last; hamza folded into alif)
ALPHABET_28 = list("ابتثجحخدذرزسشصضطظعغفقكلمنهوي")
assert len(ALPHABET_28) == 28, f"alphabet has {len(ALPHABET_28)} letters, expected 28"
ALPHABET_28_SET = set(ALPHABET_28)

# 14 muqaṭṭaʿāt letters (Ḥafṣ-Kūfan; bare-alif normalized)
MUQ_14 = set("احرسصطعقكلمنهي")
assert len(MUQ_14) == 14, f"muqaṭṭaʿāt has {len(MUQ_14)} letters, expected 14"
assert MUQ_14.issubset(ALPHABET_28_SET), "muqaṭṭaʿāt not subset of alphabet"

NON_MUQ_14 = ALPHABET_28_SET - MUQ_14
assert len(NON_MUQ_14) == 14

# ---------------------------------------------------------------------------
# Locked classical groupings (per pre-reg §3)
# ---------------------------------------------------------------------------

# G1 — shamsiyyah (sun letters, 14): assimilate the lām of al-
G1_SHAMSIYYAH = set("تثدذرزسشصضطظلن")
assert len(G1_SHAMSIYYAH) == 14, f"G1 has {len(G1_SHAMSIYYAH)}, expected 14"
assert G1_SHAMSIYYAH.issubset(ALPHABET_28_SET)

# G2 — qamariyyah (moon letters, 14): complement of shamsiyyah
G2_QAMARIYYAH = set("ابجحخعغفقكمهوي")
assert len(G2_QAMARIYYAH) == 14, f"G2 has {len(G2_QAMARIYYAH)}, expected 14"
assert G2_QAMARIYYAH == ALPHABET_28_SET - G1_SHAMSIYYAH, "G2 must be complement of G1"

# G3 — majhūra per Sibawayh (al-Kitāb IV ch. 565), hamza folded into alif
# Sibawayh's voiced: ء, ا, ب, ج, د, ذ, ر, ز, ض, ط, ظ, ع, غ, ق, ل, م, ن, و, ي
# After folding ء → ا (already in set), distinct = 18 letters
G3_MAJHURA_SIBAWAYH = set("ابجدذرزضطظعغقلمنوي")
assert len(G3_MAJHURA_SIBAWAYH) == 18, f"G3 has {len(G3_MAJHURA_SIBAWAYH)}, expected 18"

# G4 — mahmūsa per Sibawayh: ت, ث, ح, خ, س, ش, ص, ف, ك, ه (10 letters)
G4_MAHMUSA_SIBAWAYH = set("تثحخسشصفكه")
assert len(G4_MAHMUSA_SIBAWAYH) == 10, f"G4 has {len(G4_MAHMUSA_SIBAWAYH)}, expected 10"
assert G3_MAJHURA_SIBAWAYH | G4_MAHMUSA_SIBAWAYH == ALPHABET_28_SET, \
    "G3 ∪ G4 must = alphabet"
assert G3_MAJHURA_SIBAWAYH & G4_MAHMUSA_SIBAWAYH == set(), \
    "G3 ∩ G4 must = empty"

# G5 — modern-voiced (Watson 2002): ب, ج, د, ذ, ر, ز, ض, ظ, ع, غ, ل, م, ن, و, ي
# (ا locked to G5 per pre-reg §3.3 — alif as vowel-bearer phonologically neutral
#  but functionally voiced in vocalic realization)
G5_MODERN_VOICED = set("ابجدذرزضظعغلمنوي")
assert len(G5_MODERN_VOICED) == 16, f"G5 has {len(G5_MODERN_VOICED)}, expected 16"

# G6 — modern-voiceless: ت, ث, ح, خ, س, ش, ص, ط, ف, ق, ك, ه (12 letters)
G6_MODERN_VOICELESS = set("تثحخسشصطفقكه")
assert len(G6_MODERN_VOICELESS) == 12, f"G6 has {len(G6_MODERN_VOICELESS)}, expected 12"
assert G5_MODERN_VOICED | G6_MODERN_VOICELESS == ALPHABET_28_SET
assert G5_MODERN_VOICED & G6_MODERN_VOICELESS == set()

# G7 — ḥurūf al-ṣafīr (sibilants): ز, س, ص (3 letters)
G7_SAFIR = set("زسص")
assert len(G7_SAFIR) == 3
assert G7_SAFIR.issubset(ALPHABET_28_SET)

# G8 — ḥurūf al-iṭbāq (strict emphatic): ص, ض, ط, ظ (4 letters)
G8_ITBAQ = set("صضطظ")
assert len(G8_ITBAQ) == 4
assert G8_ITBAQ.issubset(ALPHABET_28_SET)

GROUPINGS = [
    ("G1_shamsiyyah", G1_SHAMSIYYAH, "sun letters (al-Zamakhsharī Mufaṣṣal §82)"),
    ("G2_qamariyyah", G2_QAMARIYYAH, "moon letters (complement of shamsiyyah)"),
    ("G3_majhura_Sibawayh", G3_MAJHURA_SIBAWAYH, "voiced per Sibawayh al-Kitāb IV ch. 565"),
    ("G4_mahmusa_Sibawayh", G4_MAHMUSA_SIBAWAYH, "voiceless per Sibawayh al-Kitāb IV ch. 565"),
    ("G5_modern_voiced", G5_MODERN_VOICED, "voiced per Watson 2002 modern phonetic"),
    ("G6_modern_voiceless", G6_MODERN_VOICELESS, "voiceless per Watson 2002 modern phonetic"),
    ("G7_safir", G7_SAFIR, "sibilants (Sibawayh / al-Khalīl)"),
    ("G8_itbaq", G8_ITBAQ, "strict emphatic / iṭbāq (Sibawayh / al-Mubarrad)"),
]

K_BONF = 8
ALPHA_FAMILY = 0.05
ALPHA_PER_GROUPING = ALPHA_FAMILY / K_BONF  # 0.00625

N_ALPHABET = 28
N_MUQ = 14

# ---------------------------------------------------------------------------
# Hypergeometric closed-form
# ---------------------------------------------------------------------------

def hyperg_pmf(k: int, c: int) -> float:
    """P(K = k | hypergeom(N=28, K=c, n=14))."""
    if k < 0 or k > c or k > N_MUQ or (N_MUQ - k) > (N_ALPHABET - c):
        return 0.0
    return comb(c, k) * comb(N_ALPHABET - c, N_MUQ - k) / comb(N_ALPHABET, N_MUQ)


def hyperg_cdf_ge(k_obs: int, c: int) -> float:
    """P(K >= k_obs)."""
    return sum(hyperg_pmf(k, c) for k in range(k_obs, min(c, N_MUQ) + 1))


def hyperg_cdf_le(k_obs: int, c: int) -> float:
    """P(K <= k_obs)."""
    return sum(hyperg_pmf(k, c) for k in range(0, k_obs + 1))


def two_sided_p(k_obs: int, c: int) -> float:
    """Doubled-smaller-tail two-sided exact p."""
    p_enrich = hyperg_cdf_ge(k_obs, c)
    p_deplete = hyperg_cdf_le(k_obs, c)
    return min(2.0 * min(p_enrich, p_deplete), 1.0)


# ---------------------------------------------------------------------------
# Per-grouping evaluation
# ---------------------------------------------------------------------------

def evaluate_grouping(name: str, G: set, source: str) -> dict:
    """Evaluate one classical grouping against U_muq."""
    c = len(G)
    intersection = MUQ_14 & G
    union = MUQ_14 | G
    k_obs = len(intersection)
    expected = N_MUQ * c / N_ALPHABET
    jaccard = len(intersection) / len(union) if len(union) > 0 else 0.0
    p_enrich = hyperg_cdf_ge(k_obs, c)
    p_deplete = hyperg_cdf_le(k_obs, c)
    p_two = two_sided_p(k_obs, c)
    sig_bon = p_two < ALPHA_PER_GROUPING
    sig_unprotected = p_two < 0.05
    return {
        "name": name,
        "source": source,
        "grouping_size": c,
        "grouping_letters": sorted(G),
        "muq_intersect_grouping": sorted(intersection),
        "muq_only": sorted(MUQ_14 - G),
        "grouping_only": sorted(G - MUQ_14),
        "k_observed": k_obs,
        "k_expected": expected,
        "jaccard_overlap": jaccard,
        "p_one_sided_enrichment": p_enrich,
        "p_one_sided_depletion": p_deplete,
        "p_two_sided": p_two,
        "significant_bonferroni_8": sig_bon,
        "significant_unprotected_05": sig_unprotected,
        "direction": (
            "ENRICHED" if p_enrich < p_deplete
            else "DEPLETED" if p_deplete < p_enrich
            else "NEUTRAL"
        ),
    }


# ---------------------------------------------------------------------------
# MW-5 positive controls
# ---------------------------------------------------------------------------

def mw5_planted_full() -> dict:
    """Planted: U_planted = G1 (sun letters) exactly. Should detect p ≈ 5e-8."""
    U_planted = G1_SHAMSIYYAH.copy()
    k_obs = len(U_planted & G1_SHAMSIYYAH)  # = 14
    p_two = two_sided_p(k_obs, len(G1_SHAMSIYYAH))
    return {
        "name": "MW5_planted_full_G1",
        "k_observed": k_obs,
        "p_two_sided": p_two,
        "expected_threshold": 1e-7,
        "passes": p_two < 1e-7,
    }


def mw5b_planted_one_swap() -> dict:
    """Planted: U_planted = G1 with 1 swap (ت → ك). k_obs vs G1 = 13."""
    U_planted = (G1_SHAMSIYYAH - {"ت"}) | {"ك"}
    assert len(U_planted) == 14
    k_obs = len(U_planted & G1_SHAMSIYYAH)  # = 13
    p_two = two_sided_p(k_obs, len(G1_SHAMSIYYAH))
    return {
        "name": "MW5b_planted_one_swap_G1",
        "k_observed": k_obs,
        "p_two_sided": p_two,
        "expected_threshold": 1e-3,
        "passes": p_two < 1e-3,
    }


# ---------------------------------------------------------------------------
# Phonotactic descriptors (auxiliary, NOT Bonferroni-counted)
# ---------------------------------------------------------------------------

def phonotactic_side_test() -> dict:
    """Descriptive counts of sonorant/stop/fricative letters in U_muq vs U_non.
    Per pre-reg §8 — REPORTED DESCRIPTIVELY, not a verdict input."""
    sonorants = set("رلمنوي")
    # Stops: voiced+voiceless plosives. Per Watson 2002:
    # ب /b/, ت /t/, د /d/, ط /tˤ/, ك /k/, ق /q/, ا (as glottal-stop carrier in some contexts)
    stops = set("ابتدطكق")
    # Fricatives: ث/ḥ/خ/ذ/ز/س/ش/ص/ض/ظ/ع/غ/ف/ه (14)
    fricatives = set("ثحخذزسشصضظعغفه")
    return {
        "sonorants_total": len(sonorants),
        "sonorants_in_muq": sorted(sonorants & MUQ_14),
        "sonorants_in_muq_count": len(sonorants & MUQ_14),
        "sonorants_in_non_muq": sorted(sonorants & NON_MUQ_14),
        "sonorants_in_non_muq_count": len(sonorants & NON_MUQ_14),
        "stops_total": len(stops),
        "stops_in_muq": sorted(stops & MUQ_14),
        "stops_in_muq_count": len(stops & MUQ_14),
        "stops_in_non_muq": sorted(stops & NON_MUQ_14),
        "stops_in_non_muq_count": len(stops & NON_MUQ_14),
        "fricatives_total": len(fricatives),
        "fricatives_in_muq": sorted(fricatives & MUQ_14),
        "fricatives_in_muq_count": len(fricatives & MUQ_14),
        "fricatives_in_non_muq": sorted(fricatives & NON_MUQ_14),
        "fricatives_in_non_muq_count": len(fricatives & NON_MUQ_14),
    }


# ---------------------------------------------------------------------------
# MW-7 internal error gate
# ---------------------------------------------------------------------------

def mw7_gate(results: list, mw5: dict, mw5b: dict) -> list:
    err = []
    for r in results:
        if not (0.0 <= r["p_two_sided"] <= 1.0):
            err.append(f"p_oob_{r['name']}={r['p_two_sided']}")
        if not (0.0 <= r["p_one_sided_enrichment"] <= 1.0):
            err.append(f"p_enrich_oob_{r['name']}")
        if not (0.0 <= r["p_one_sided_depletion"] <= 1.0):
            err.append(f"p_deplete_oob_{r['name']}")
    if not mw5["passes"]:
        err.append(f"MW5_planted_failed_p={mw5['p_two_sided']}")
    if not mw5b["passes"]:
        err.append(f"MW5b_planted_failed_p={mw5b['p_two_sided']}")
    # Verify alphabet partitions
    if len(ALPHABET_28_SET) != 28:
        err.append("alphabet_size_wrong")
    if len(MUQ_14) != 14:
        err.append("muq_size_wrong")
    return err


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    print("[H-NEW-69] === Half-alphabet split test ===")
    print(f"[H-NEW-69] U_muq (14): {''.join(sorted(MUQ_14))}")
    print(f"[H-NEW-69] U_non (14): {''.join(sorted(NON_MUQ_14))}")
    print()

    # 1. Per-grouping hypergeometric
    print("[H-NEW-69] Computing per-grouping exact hypergeometric tests...")
    results = []
    for name, G, source in GROUPINGS:
        r = evaluate_grouping(name, G, source)
        results.append(r)
        sig_marker = "***Bonferroni***" if r["significant_bonferroni_8"] \
                     else "*unprotected*" if r["significant_unprotected_05"] \
                     else "n.s."
        print(f"  {name:30s} c={r['grouping_size']:2d} k={r['k_observed']:2d} "
              f"E={r['k_expected']:.1f} jaccard={r['jaccard_overlap']:.3f} "
              f"p_two={r['p_two_sided']:.5f} [{r['direction']}] {sig_marker}")

    # Best-matching
    best_r = min(results, key=lambda x: (x["p_two_sided"], x["name"]))
    print(f"\n[H-NEW-69] BEST-MATCHING: {best_r['name']} (p={best_r['p_two_sided']:.6f})")

    # 2. MW-5 positive controls
    print("\n[H-NEW-69] MW-5 positive controls...")
    mw5 = mw5_planted_full()
    mw5b = mw5b_planted_one_swap()
    print(f"  MW5  (G1 planted full):     k={mw5['k_observed']}/14 p={mw5['p_two_sided']:.2e} "
          f"PASS={mw5['passes']}")
    print(f"  MW5b (G1 planted 1 swap):   k={mw5b['k_observed']}/14 p={mw5b['p_two_sided']:.2e} "
          f"PASS={mw5b['passes']}")

    # 3. Phonotactic descriptors
    print("\n[H-NEW-69] Phonotactic descriptors (descriptive only)...")
    phono = phonotactic_side_test()
    print(f"  sonorants in muq: {phono['sonorants_in_muq_count']}/{phono['sonorants_total']} "
          f"({''.join(phono['sonorants_in_muq'])})")
    print(f"  stops     in muq: {phono['stops_in_muq_count']}/{phono['stops_total']} "
          f"({''.join(phono['stops_in_muq'])})")
    print(f"  fricatives in muq: {phono['fricatives_in_muq_count']}/{phono['fricatives_total']} "
          f"({''.join(phono['fricatives_in_muq'])})")

    # 4. MW-7 gate
    err = mw7_gate(results, mw5, mw5b)
    if err:
        print(f"\n[MW-7] INTERNAL ERROR GATE: {err}")
        verdict = "NULL-BROKEN"
    else:
        # Verdict per pre-reg §7
        n_sig_bon = sum(1 for r in results if r["significant_bonferroni_8"])
        n_sig_unp = sum(1 for r in results if r["significant_unprotected_05"])
        if n_sig_bon >= 1:
            # Check classical interpretability
            verdict = "STRONG-PASS"
        elif n_sig_unp >= 1:
            verdict = "PASS-DIRECTED"
        else:
            verdict = "NULL"

    print(f"\n[H-NEW-69] === VERDICT: {verdict} ===")
    print(f"  n_significant_Bonferroni-8: {sum(1 for r in results if r['significant_bonferroni_8'])} / 8")
    print(f"  n_significant_unprotected:  {sum(1 for r in results if r['significant_unprotected_05'])} / 8")

    # Integrity hashes
    quran_path = os.path.join(REPO, "quran-text/quran-no-tashkeel.json")
    with open(quran_path, "rb") as f:
        quran_sha = hashlib.sha256(f.read()).hexdigest()
    with open(__file__, "rb") as f:
        script_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-69",
        "title": "Half-alphabet split: muqaṭṭaʿāt vs classical 14-of-28 groupings",
        "run_date": "2026-04-15",
        "agent": "h-new-69-specialist",
        "pre_reg": "findings/phase-b-hypotheses/h-new-69-half-alphabet-split-prereg.md",
        "rules_tuple": [
            "28-letter Arabic orthographic alphabet",
            "hamza folded into alif",
            "classical Sibawayh/al-Khalīl/al-Zamakhsharī classifications",
        ],
        "bonferroni_family": "2026-04-15-Wave-Half-Alphabet",
        "bonferroni_k": K_BONF,
        "alpha_family": ALPHA_FAMILY,
        "alpha_per_grouping": ALPHA_PER_GROUPING,
        "alphabet_28": ALPHABET_28,
        "muq_14": sorted(MUQ_14),
        "non_muq_14": sorted(NON_MUQ_14),
        "groupings_tested": [
            {
                "name": name,
                "source": source,
                "size": len(G),
                "letters": sorted(G),
            }
            for name, G, source in GROUPINGS
        ],
        "per_grouping_results": results,
        "best_matching_grouping": best_r["name"],
        "best_matching_p_two_sided": best_r["p_two_sided"],
        "mw5_positive_control": mw5,
        "mw5b_positive_control": mw5b,
        "phonotactic_side_test": phono,
        "mw7_internal_error_gate": err if err else "PASS",
        "verdict": verdict,
        "integrity_sha256": {
            "quran_json": quran_sha,
            "script": script_sha,
        },
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-69.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[H-NEW-69] Wrote {out_path}")


if __name__ == "__main__":
    main()
