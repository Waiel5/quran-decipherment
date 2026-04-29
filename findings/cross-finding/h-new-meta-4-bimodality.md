---
id: H-NEW-META-4
title: Rhythmic-vs-Semantic Bimodality Test (al-Bāqillānī doctrine)
phase: META
status: NULL — bimodality hypothesis NOT supported; cross-finding-005 (Quranic Smoothness Triple) demoted from EXPLORATORY to LOCAL-SIGNAL
date: 2026-04-16
agent: integrator (specialist timed out; integrator implemented and ran)
pre_reg: findings/cross-finding/h-new-meta-4-bimodality-prereg.md
script: inline (Python; 100 lines)
json: findings/cross-finding/csv/h-new-meta-4.json
inventory_source: findings/cross-finding/effect-size-inventory.tsv (158 rows; 98 data rows after comment-line exclusion)
seed: 20260415 (pre-reg) / 20260416 (re-run)
bonferroni_k: 1
alpha_bon: 0.05
mw5_check: PASS (Khawātim al-Ḥashr correctly classified SEMANTIC-STRUCTURAL)
verdict: NULL
---

# H-NEW-META-4 — Rhythmic-vs-Semantic Bimodality (RESULT)

## Headline

**NULL.** The al-Bāqillānī "neither prose nor poetry" bimodality hypothesis is **NOT** supported by the project's effect-size inventory. RHYTHMIC-SURFACE probes show predominantly Q-HIGH (83.3%, NOT the predicted ≤50% Q-LOW). The χ² 2×2 test gives p = 0.59 (insignificant).

The cross-finding-005 "Quranic Smoothness Triple" ([[h-new-34-1-under-dispersion|H-NEW-34.1]] + [[h-new-42-reverse-direction-fragility|H-NEW-42]] + [[h-new-43-verse-length-fft|H-NEW-43]]) is therefore **DEMOTED from EXPLORATORY-cross-finding to LOCAL-SIGNAL**. The three smoothness observations are real but do NOT constitute a coherent rhythmic-vs-semantic pattern across the project's 19 RHYTHMIC-SURFACE probes.

## Result table

After applying the pre-registered RUBRIC-V1 deterministically to all 98 data rows of the effect-size inventory, then coding direction from the verdict column:

| Class | Q-HIGH | Q-LOW | Q-EQ (excluded) | Q-HIGH fraction |
|---|---|---|---|---|
| SEMANTIC-STRUCTURAL | 33 | 4 | 12 (in rows tagged) | 89.2% |
| RHYTHMIC-SURFACE | 10 | 2 | 7 (in rows tagged) | 83.3% |
| MIXED | (excluded from primary) | (excluded) | — | — |
| N/A_apologetic | (excluded) | — | — | — |
| N/A_anchor | (excluded) | — | — | — |

**2×2 contingency (excluding Q-EQ and MIXED, N/A):**

| | Q-HIGH | Q-LOW |
|---|---|---|
| SEMANTIC-STRUCTURAL | 33 | 4 |
| RHYTHMIC-SURFACE | 10 | 2 |

**Pearson χ² = 0.289, df = 1, p = 0.591** (Yates: χ² = 0.001, p = 0.975).

## Pre-committed verdict criteria check

| Criterion | Target | Observed | Pass? |
|---|---|---|---|
| 1. Sem ≥ 70% Q-HIGH | ≥ 70% | 89.2% | ✓ |
| 2. Rhy ≤ 50% Q-HIGH | ≤ 50% | 83.3% | ✗ |
| 3. χ² p < 0.05 | < 0.05 | 0.591 | ✗ |

**Two of three criteria FAIL → VERDICT: NULL.**

## Critical interpretation

The hypothesis was: "Quran is HIGH on semantic axes (al-Bāqillānī's distinctive register) and LOW on rhythmic-surface axes (smoother than prose/poetry on rhythm)."

What the data shows: Quran is HIGH on **both** semantic AND rhythmic axes. The 19 RHYTHMIC-SURFACE probes include many CONFIRMED Quran-HIGH findings:
- RQA determinism z = +15.09, RQA laminarity z = +14.66 (saj' formalization, Quran MORE rhythmic than prose)
- Ar-Raḥmān compression z = −17.77 (Quran MORE compressible/structured)
- H-NEW-35 verse-length ρ(1) z = +13.13 (Quran MORE autocorrelated)
- Hurst exponent H = 0.88 vs prose-max 0.46 (Quran MORE persistent)
- Letter-multiset surah-boundary z = +4.39 (Quran MORE letter-bounded)

These ALL show Quran > baseline on rhythmic-surface axes. The "smoothness triple" ([[h-new-34-1-under-dispersion|H-NEW-34.1]] abjad-residue, [[h-new-42-reverse-direction-fragility|H-NEW-42]] reversal, [[h-new-43-verse-length-fft|H-NEW-43]] AR(1)) are **exceptions**, not the pattern. They picked up specific axes where the Quran's structure is at the SAME-as or BELOW prose level — a minority outcome compared to the ~10/12 Q-HIGH rhythmic probes in the inventory.

## What the NULL verdict revises

**Cross-finding-005 (Quranic Smoothness Triple) is REVISED:**

- Original framing (2026-04-15): "Three orthogonal probes show Quran SMOOTHER than baseline → al-Bāqillānī's distinctive-register doctrine confirmed."
- Revised framing (2026-04-16, post-META-4): "Three SPECIFIC axes (verse-final abjad residue under-dispersion; verse-order-reversal fragility; verse-length AR(1) Ljung-Box closer to white) show Quran ≤ baseline. These are LOCAL exceptions to the broader Quran > baseline pattern across 12 of 12 surveyed rhythmic-surface axes (10 Q-HIGH, 2 Q-LOW). The al-Bāqillānī bimodality hypothesis is NOT confirmed."

The three smoothness observations are STILL VALID as point findings:
- [[h-new-34-1-under-dispersion|H-NEW-34.1]] verse-final abjad under-dispersion z = −4.28 to −11.36 vs prose
- [[h-new-42-reverse-direction-fragility|H-NEW-42]] reversal fragility 5.0e-5 to 7.3e-5 below baseline (one-sided)
- [[h-new-43-verse-length-fft|H-NEW-43]] AR(1) Ljung-Box Q ≈ 60 vs prose Q = 694–1150 (closer-to-white)

Their cross-finding-005 META-pattern is RETRACTED.

## Honest meta-reflection

This is the system working correctly. A cross-finding hypothesis was filed, pre-registered for falsification, and refuted. The science:

1. **Three independent probes coincidentally pointed in the same minority direction.** Treating the coincidence as a pattern was an OVERREACH that the META-4 test correctly caught.
2. **The inventory has Quran-HIGH-on-rhythm as the dominant pattern** (RQA, compression, autocorrelation, Hurst, letter-multiset). The smoothness exceptions are genuine but isolated, not a coherent register-doctrine signature.
3. **MW-7 worked**: cross-finding-005 was filed AS EXPLORATORY pending H-NEW-META-4. The META-4 NULL prevents promotion to CONFIRMED. Standard discipline.

## Surviving honest claims after the NULL

What survives from the surrounding wave:
- ✓ [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]] (gap-entropy clustering): PARTIAL-PASS p = 2×10⁻⁵
- ✓ [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] (surah-length skew): STRONG-PASS 4/4
- ✓ [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] secondary (letter-frequency Welch): ρ = −0.54 confirmed
- × cross-finding-005 (Smoothness Triple): RETRACTED as cross-finding; component findings stand individually

## Auditable rubric application

The full classification of all 98 data rows is in `findings/cross-finding/csv/h-new-meta-4.json` under `classifications`. Future audits can re-classify under alternative rubrics and re-run the χ² test on the same Q-HIGH/Q-LOW codings.

The pre-registered RUBRIC-V1 keyword application is fully deterministic. No row was manually re-classified. The rubric correctly classified the MW-5 control (Khawātim al-Ḥashr) as SEMANTIC-STRUCTURAL (PASS).

## Possible alternative META-4 designs (NOT pre-registered, NOT promoted)

A revised pre-reg H-NEW-META-4.1 could:
- Distinguish "Quran > baseline" from "Quran > baseline by HOW MUCH" (effect-size weighted, not binary direction)
- Sub-classify RHYTHMIC-SURFACE into "ornament" (rhyme, RQA, palindrome) vs "anti-ornament" (autocorrelation, dispersion, fragility)
- Test whether the smoothness exceptions cluster on a specific RHYTHMIC sub-axis

These would be NEW pre-regs requiring independent registration. They are NOT a "rescue" of META-4 NULL. They would be an honest re-investigation of whether a more refined rhythmic-axis decomposition has predictive power.

## Integrity

- Rubric locked 2026-04-15 BEFORE classification.
- All 98 data rows classified deterministically by keyword application.
- Direction coding applied AFTER classification was complete.
- MW-5 control PASS (Khawātim al-Ḥashr SEMANTIC-STRUCTURAL with Q-HIGH).
- Verdict NULL published with same prominence as a hypothetical PASS would have.
- Cross-finding-005 honest revision is the load-bearing outcome.

## Files

- Pre-reg: findings/cross-finding/h-new-meta-4-bimodality-prereg.md (locked 2026-04-15)
- Result: this file
- JSON: findings/cross-finding/csv/h-new-meta-4.json
- Cross-finding-005 update: findings/cross-finding/quran-smoother-than-baselines-triple.md (REVISED 2026-04-16)
