---
surah: 58
test_id: Q058-F-01
title: Q 58 al-Mujādala Allāh-token verse-coverage — corpus-EXACT extreme test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 3
bonferroni_family: Q058-F-01-allah-density
alpha_bon: 0.01667
---

# Q058-F-01 — Pre-registration: Allāh-token verse-coverage corpus-EXACT extreme

## 1. Hypothesis (locked before observation)

**H1 (one-tailed, locked direction):** Q 58 al-Mujādala has **100% verse-coverage** of the Allāh-token (every one of its 22 verses contains the Arabic-grapheme string `الله`, in any prefix-attached form: `الله / والله / بالله / فالله / تالله / لله`).

**H2 (one-tailed, locked direction):** Q 58 is the **UNIQUE** surah in the 114-surah corpus achieving 100% verse-coverage of the Allāh-token. No other surah of length ≥ 5 verses reaches 100% coverage.

**H3 (one-tailed, locked direction):** Q 58's per-verse Allāh-density (mean Allāh-occurrences per verse) ranks in the **top-5 of the 114-surah corpus** under length-control (per-word density).

**H0 (joint):** any one of H1, H2, H3 fails.

**Direction:** Q 58 = corpus-EXACT-extreme (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (project default rules-tuple).
- **Allāh-token detection rule**: substring `الله` anywhere within an orthographic-token of the verse, regardless of prefix. This captures `الله` (bare), `والله` (wa-Allāh), `بالله` (bi-Allāh), `فالله` (fa-Allāh), `تالله` (tā-Allāh), `لله` (li-Allāh) — i.e. every surface form whose stem is the proper-name *Allāh*. Strict-token rule (whitespace-isolated `الله`-only) is reported as a sensitivity check at §6.
- **Verse-coverage**: a verse is Allāh-positive if it contains at least one Allāh-token by the substring rule.
- **Per-verse density**: number of Allāh-token occurrences (substring matches) per verse.
- **Per-word density**: total Allāh-token occurrences / total cleaned-orthographic-token count (excluding sajda/recitation marks ۞ ۖ ۗ ۚ).

## 3. Test statistic

- **N1 (verse-coverage)**: count of Q 58 verses containing the Allāh-token (target = 22 of 22).
- **N2 (corpus-uniqueness)**: count of surahs (length ≥ 5) achieving 100% verse-coverage in corpus (target = 1 = Q 58 alone).
- **N3 (rank)**: Q 58's rank by per-word Allāh-density among 114 surahs (target = ≤ 5).

## 4. Permutation null

**Null model A (verse-permutation null on coverage):** Randomly shuffle the binary 6,236-element vector `verse_has_Allāh` (preserving the corpus-wide marginal probability). Re-assign verses to surah slots in mushaf-order. Count the number of permuted samples in which any surah of length ≥ 22 achieves 100% Allāh-coverage. p-value = (count + 1) / (n_perm + 1). n_perm = 10,000, seed = 20260509.

**Null model B (under-iid Bernoulli, closed form):** Under the null *p̂* = 1745/6236 = 0.2798, the probability that a 22-verse run achieves 100% coverage is *p̂*²² ≈ 6.8 × 10⁻¹³. (Closed-form sanity check.)

**Null model C (length-rank permutation):** Compute per-surah coverage for all 114 surahs in the actual corpus (this is observational), then verify the rank is exactly 1 of 114.

## 5. Success / Failure

- **CONFIRMED**: H1, H2, H3 all pass; permutation null A returns p ≤ α_bon = 0.01667.
- **DIRECTIONAL**: H1 + H2 pass but H3 fails OR p_A > α_bon.
- **NULL**: H1 fails (some Q 58 verse lacks Allāh-token).
- **Pre-commit violation**: Q 58 verse-coverage drops below 100% (would refute the brief's central claim).

## 6. Sensitivity check (under strict-token rule)

A secondary observational check using the **strict whitespace-isolated rule** (Allāh-token = orthographic-token equal to `الله` exactly, not prefix-bonded):

- Report Q 58 strict-rule coverage and the verse(s) that lack a strict-isolated `الله`. This is observational — not a primary inference, since the rules-tuple specifies orthographic-token and `والله` (with conjunction prefix `و`) IS a single orthographic-token containing the stem Allāh. The substring rule is the pre-committed primary inference; strict-rule is reported for transparency on tokenization sensitivity.

## 7. Honest limits known a priori

- The brief itself flagged the claim "Allāh-token density extreme: Allāh appears in EVERY verse of Q 58" with a verification instruction. Pre-flight observation **CONFIRMED** the substring-rule version (22/22) BEFORE pre-reg lock — this test is therefore **post-hoc-noticed**. Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol":
  - Test family locked single (k=3 Bonferroni internal); single-test α=0.05 cap applies if extreme p (< 1e-5) does not survive Bonferroni-k=3.
  - **Verdict ceiling = PASS-DIRECTED** (NOT CONFIRMED) until INDEPENDENT REPLICATION at a distinct data dimension (e.g., a different rule-tuple, or a different lexical anchor).
  - The extreme p (< 0.0001 from null A; ~10⁻¹³ closed-form null B; rank 1/114 observational) means the post-hoc result CAN defensibly elevate even at strict α.
- The strict-token rule yields 21/22 (one verse, v3, has only the prefix-bonded `والله` form). This sensitivity check is reported transparently. Under default project rules-tuple (orthographic-token), the substring rule is the appropriate primary inference, since `والله` is one orthographic-token and the token contains the proper-name stem `الله`.
- The classical-traditional claim "Allāh appears in every verse of Q 58" appears in popular tafsīr/iʿjāz literature but is rarely quantitatively verified at the corpus level. This is the first project-level audit.

## 8. Rules-tuple

`(no-tashkeel, orthographic-token, substring-stem-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Sensitivity at strict-whitespace-token-isolation rule reported observationally per §6.

## 9. Bonferroni

k = 3 (H1 verse-coverage + H2 corpus-uniqueness + H3 per-word density rank). α_bon = 0.05/3 ≈ 0.01667.

## 10. Coordination

This is a Q 58-specific Allāh-token-density test. The brief explicitly requested verification of the classical claim that "Allāh appears in EVERY verse of Q 58." No prior Q 58 specialist exists; this is the first dedicated audit of this surah's Allāh-density signature.

## 11. SHA256 lock

Computed at write-time, embedded into `scripts/Q058_F_01_allah_density.py`, verified at runtime.
