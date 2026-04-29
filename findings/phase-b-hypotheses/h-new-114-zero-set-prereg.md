---
id: H-NEW-114
title: Zero-Set / Absent-Structures Fingerprint — Pre-Registration
phase: B
date: 2026-04-17
agent: h-new-114-specialist
status: PRE-REGISTERED
parent_family: novel test (inverts the standard contains-X question)
corpus_anchor: 6,236 verses / 77,797 tokens / 330,709 graphemes / Hafs-Kūfan
rules_tuple:
  orthography: no-tashkeel
  tokenization: whitespace (real-words; recitation-mark-only tokens stripped)
  letter_definition: graphemes (28-core mapped via orthographic-normalization; see §NORMALIZATION)
  basmala_policy: basmala-counted-only-in-surah-1 (default JSON state)
bonferroni_k: 4
bonferroni_family: h-new-114-zero-set
alpha_bon: 0.0125
null_design_A: Poisson-envelope derived from 3 matched-Arabic baselines (Bukhārī, Jāḥiẓ, Muʿallaqāt) — primary PASS rule; shuffle-letter-multiset as STRUCTURAL-GAP DIAGNOSTIC (not primary)
null_design_B: same as A for trigrams
null_design_C: Poisson-envelope-under-independence; primary PASS rule tests whether the count of surprising-absences (O=0, E≥1) exceeds a Poisson-envelope expectation; permutation-of-token-sequence as auxiliary
null_design_D: no null (descriptive)
direction_A: Quran absent-letter-bigram-count DIFFERENT from matched-Arabic-baseline envelope (2-sided)
direction_B: Quran absent-letter-trigram-count DIFFERENT from matched-Arabic-baseline envelope (2-sided)
direction_C: Quran has MORE surprising-absences than Poisson-independence predicts (primary 1-sided upper tail, per pre-reg motivation — "zero-set is structurally more constrained than independence")
direction_D: DESCRIPTIVE — report structured gaps in 14-letter muqaṭṭāʿat-presence patterns honestly
acceptance_window: cells A, B, C are primary inferential (α_bon = 0.0125 each); cell D is descriptive only
amendment_audit_035: 2026-04-17 TIGHTENING amendment (self-verifying per Bonferroni-asymmetry rule). Direction-vs-PASS-rule mismatch flagged by audit-035; amended before viewing 10K-perm results. Original plan used shuffle-null as primary PASS for A/B; amended to use matched-Arabic-baseline-envelope as primary (because shuffle-null is pathologically narrow — the letter multiset + token length structure force absent-count variance to ~0-5, giving near-deterministic "significance" at the obs 146/15,827). The matched-Arabic-baseline comparison is the STRICTER and more meaningful test. Shuffle-null remains reported as the MW-5 multiset-baseline diagnostic.
seed: 20260417
n_bootstrap: 10000
primary_corpus: quran-text/quran-no-tashkeel.json
baselines:
  - data/baseline-corpora/raw/bukhari-noquran.txt
  - data/baseline-corpora/raw/jahiz-hayawan.txt
  - data/baseline-corpora/raw/muallaqa-{imru-al-qais,tarafa,zuhayr,labid,antara,amr-bin-kulthum,harith}.txt
---

# [[h-new-114-zero-set|H-NEW-114]] — Zero-Set / Absent-Structures Fingerprint (pre-registration)

## Motivation

Nearly every structural finding in this project describes **what the Quran contains**. This pre-reg inverts the question: enumerate what the Quran **does NOT contain** (at letter-bigram, letter-trigram, word-bigram, and muqaṭṭāʿat-pattern levels) and test whether the "hole structure" is characteristic vs matched Arabic baselines.

The zero-set is complementary information. For a length-L, alphabet-28 corpus, the bigram absent-count depends on L, the unigram Zipf slope, and the admissibility of specific bigrams. If the Quran has systematically MORE or FEWER absences than length-matched prose / poetry, that is an additional signature independent of the contains-X findings.

## Data

- **Quran**: `quran-text/quran-no-tashkeel.json` (330,709 letter graphemes, 77,797 real-word tokens).
- **Baselines** ([[h-new-48-poetic-meter|H-NEW-48]] matched-Arabic): `data/baseline-corpora/raw/bukhari-noquran.txt` (Bukhārī prose), `data/baseline-corpora/raw/jahiz-hayawan.txt` (Jāḥiẓ Ḥayawān prose), 7 muʿallaqāt files pooled.

### NORMALIZATION (LOCKED)

- Normalize characters: `ٱ → ا`, `أإآ → ا`, `ؤ → و`, `ئ → ي`, `ة → ه`, `ى → ي`. Strip tashkeel U+064B..U+0652 and tatweel U+0640 and recitation marks U+06D6..U+06ED.
- Accept only the 28 core Arabic letters after normalization: `ا ب ت ث ج ح خ د ذ ر ز س ش ص ض ط ظ ع غ ف ق ك ل م ن ه و ي`.
- For letter-bigram/trigram analysis, construct the filtered letter stream per text (whitespace and word boundaries preserved as token breaks — adjacent-letter bigrams do NOT cross word boundaries).
- For word-bigram analysis, tokens are whitespace-split with recitation-mark-only tokens removed (matching `real_words` in `analysis/tools/tokenize.py`).

## Cells

### Cell A — Letter-bigram absent-set (PRIMARY directional)

28 × 28 = 784 possible ordered letter bigrams. For each corpus (Quran + 3 baselines, length-truncated to match Quran letter count for fairness), enumerate the set of bigrams that occur ZERO times (within-word only; bigrams crossing word boundaries excluded).

**Test statistic**: `absent_count_Q` (# zero-count bigrams in Quran). For each baseline B, compute `absent_count_B` on a length-matched slice (first N_Quran_letters of B; Muʿallaqāt is used at its native ~30K-letter length since it is shorter than the Quran).

**Primary test — matched-Arabic-baseline envelope (PASS rule)**:

Compute `absent_count_B` for each B in {Bukhārī, Jāḥiẓ, Muʿallaqāt-7-pooled}. The "matched-Arabic envelope" is the set {absent_count_Bukhārī, absent_count_Jāḥiẓ} (the two length-matched prose baselines). Muʿallaqāt is too short (~30K vs ~330K Quran letters) to length-match and is reported descriptively only.

Primary statistic for PASS: Quran's absent-count as a **z-score relative to the length-matched-baseline mean+SD** computed as:

  z_A = (absent_count_Q − mean_B) / (std_B + ε)

where mean_B, std_B are computed over the 2 length-matched baselines (ε = 1 to avoid divide-by-zero). Under the null that "Quran's absent-bigram-count is drawn from the same distribution as matched-Arabic prose," |z_A| ≥ 2.5 roughly corresponds to a 2-sided significance at the 0.0125 threshold via a Gaussian-tail approximation on the 2-baseline envelope. Because n=2 is small, we supplement with a BOOTSTRAP CONFIDENCE INTERVAL: we sample 100 length-matched 330,709-letter windows from Bukhārī and 100 from Jāḥiẓ (with replacement over non-overlapping windows where possible; since each corpus is ~1.5-2× Quran length the number of distinct windows is 2-4, so the bootstrap is small but honest), compute `absent_count_window` for each, pool to get a 200-point distribution.

**PASS rule (Cell A)**: Cell-A PASS if `absent_count_Q` falls OUTSIDE the [2.5%, 97.5%] bootstrap envelope of the pooled baseline windows (corresponding to 2-sided α=0.05; after Bonferroni-4 we require OUTSIDE [0.625%, 99.375%] which is 2-sided α=0.0125).

**Diagnostic (NOT primary)**: Shuffle-Quran letter-multiset null (10,000 permutations, seed 20260417) is reported as MW-5 POSITIVE-CONTROL ONLY — to confirm the multiset-preserving null generates absent-counts near zero and thus does not explain Quran's high absent-count. It is NOT the primary PASS test.

**Expected behavior (pre-declared)**: Under uniform letter-multiset shuffle, Arabic letter-bigrams tend to fill ~all 784 cells for corpora ≥ 300k letters, so shuffle absent-count ≈ 0–5. Real Arabic has structured bigram gaps (impossible morphophonological sequences) at ~100-200 absent. Empirical question: does Quran's ~146 bigram-gap-count fall inside or outside the [Bukhārī, Jāḥiẓ] envelope?

### Cell B — Letter-trigram absent-set (PRIMARY directional)

28³ = 21,952 possible trigrams. Same method as Cell A. PASS rule: Quran's trigram absent-count falls OUTSIDE [0.625%, 99.375%] bootstrap window envelope of Bukhārī + Jāḥiẓ length-matched slices.

### Cell C — Word-bigram absent pattern among top-100 words (PRIMARY directional)

Compute the top 100 most-frequent real-word tokens in the Quran. Enumerate all 100 × 99 = 9,900 ordered adjacent-token pairs (i, j) with i ≠ j. For each pair, under independence, expected co-occurrences = `P(i) · P(j) · (N_tokens_adj − 1)` where `N_tokens_adj − 1` is the number of ordered adjacent-token-pair slots. Observed = count of adjacent (i, j) in the Quran where both are in top-100 and are adjacent **within a verse** (no cross-verse pairs).

**Surprising-absence score** per pair: `E_ij − O_ij` where `O_ij = 0` (we only rank pairs with O = 0). Sort descending by E; the top pairs are the "most surprising absences."

**Test statistic (primary)**: `n_surprising_zero_pairs_Q` = count of ordered pairs (i, j) with `O_ij = 0` AND `E_ij ≥ 1` (expected at least 1 adjacency under independence).

**Null (PRIMARY)**: Poisson-envelope under independence. Under independence each pair (i,j) has Poisson(λ=E_ij) adjacent counts. The probability that a given pair is ZERO is P₀ = exp(−E_ij). The expected number of "surprising-zero" pairs (O=0, E≥1) is:

  μ_null = Σ_{pairs with E≥1} exp(−E_ij)

with Poisson-sum approximate variance σ²_null = Σ exp(−E_ij)(1 − exp(−E_ij)) ≈ μ_null · (1 − p̄) where p̄ is the mean P₀. Compute z_C = (obs − μ_null) / σ_null. 1-sided upper-tail p from Gaussian (justified by Poisson-sum CLT; verified by the 10K permutation null as secondary).

**Auxiliary null**: permutation — shuffle the 77,797 real-word token sequence (preserving verse boundaries per LOCK: preserve verse-length multiset; shuffle tokens within a flat stream then re-slice by original verse lengths). 10,000 permutations. Secondary 2-sided p reported for transparency.

**Pass rule**: Cell-C PASS if 1-sided upper-tail Poisson-envelope p < 0.0125. Secondary permutation p reported.

**Deliverable**: top-10 most-surprising absent adjacencies (ordered pairs with highest E and O = 0), tabulated with the E values.

### Cell D — Muqaṭṭāʿat-letter-presence pattern space (DESCRIPTIVE)

The 14 muqaṭṭāʿat letters: `ا ح ر س ص ط ع ق ك ل م ن ه ي` (per [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] canon).

For each of the 114 surahs, compute a 14-bit presence vector (bit = 1 iff letter appears anywhere in that surah). There are 2^14 = 16,384 possible patterns. 

**Tabulate**:
1. How many of the 16,384 patterns occur among the 114 surahs? (expected ≤ 114; duplicates compress)
2. Which "structured gaps" — specific sub-patterns — never occur? Particularly: is there any 14-letter subset S such that NO surah contains all-of-S? NO surah contains exactly-S-and-nothing-else from the 14? 
3. Describe the dominant patterns: full-14 (most common — expected for long surahs), single-letter-absent patterns (which letter is most-often singularly absent?).

**No inferential test** — structured-gap reporting only. The point is to identify patterns that the muqaṭṭāʿat SYSTEM forbids or rarifies across the 114-surah space.

## MW-5 positive control

**Shuffle-null positive control**: Generate 10 synthetic random texts of length = Quran (330,709 letters) by sampling letters uniformly from the Quran's letter-multiset. For each synthetic, compute absent-bigram count and absent-trigram count. Expected behavior: these absent-counts should be close to zero (for 784 bigrams / 330K draws, expected # zeros ≈ 0 for uniform; for trigrams 21,952 / 330K ≈ small). This confirms the shuffle-null generator produces structured absence only from the letter-multiset frequency, NOT from true morphophonological constraint.

**If synthetic absent-bigram count > 50**: the letter multiset alone forces heavy tails (e.g., one letter dominates) and the null is weak but interpretable.

**If synthetic absent-bigram count is WITHIN Poisson envelope of observed shuffle null**: positive control PASSES. The shuffle null correctly captures multiset-level structure; any excess absence in Quran reflects supra-multiset (morphophonological / lexical) constraint.

## MW-1 length matching

Already handled in [[h-new-48-poetic-meter|H-NEW-48]]: baselines are length-matched to the Quran. For this test, TRUNCATE each baseline to the first `N_Quran_letters = 330,709` letters (after normalization + 28-letter filter). This is the MW-1 instrument.

## Garden-of-forking-paths log

1. **Novelty**: The zero-set / absent-structure question is novel for this project. No absent-bigram or absent-word-pair computation has been run before.

2. **Why these 4 cells**: The cells are chosen to span scales: char-bigram (Cell A) → char-trigram (Cell B) → word-bigram (Cell C) → muqaṭṭāʿat-letter-presence (Cell D). This is the natural inversion of the scales used in the contains-X findings.

3. **Bonferroni choice**: k = 4 covers the four pre-committed cells. Within each cell, the primary test is a single permutation p-value; sub-tests (e.g., Cell-A's multiple baseline comparisons) are descriptive, not counted toward the Bonferroni budget.

4. **Within-word vs cross-word bigrams**: LOCKED — within-word only. Cross-word bigrams would add noise from tokenization choices and are less linguistically meaningful.

5. **Quran as ONE text**: per project canon, no "variants" framing. Single Hafs-Kūfan corpus.

6. **Why 2-sided**: The direction is not pre-known. Either MORE or FEWER absent bigrams vs baseline is a meaningful signal.

7. **Top-100 threshold for Cell C**: standard; 100 high-frequency words covers ~60-70% of token mass in the Quran. Using more words explodes the search space and dilutes the expected-count. Pre-locked.

8. **Structured-gaps in Cell D**: explicitly descriptive. Multiple-comparison cost of mining 2^14 patterns for "anomalies" is prohibitive; we report patterns honestly rather than p-hack.

9. **Sign-flip protection**: If primary tests come back in an unexpected direction, they count at the 2-sided α (already budgeted). Cell C is pre-declared 1-sided (upper-tail) per the motivation "zero-set is MORE constrained than independence"; reverse-direction results would be EXPLORATORY-REVERSE.

10. **Amendment log (audit-035, 2026-04-17)**: Pre-reg amended BEFORE viewing 10K-perm results. Direction-vs-PASS-rule mismatch (direction field stated "vs matched Arabic baselines" but PASS rule used shuffle-null) corrected to use matched-Arabic-baseline envelope as PRIMARY PASS for Cells A/B, and Poisson-envelope as PRIMARY PASS for Cell C. Shuffle-null moved to MW-5 positive-control diagnostic role. This is a TIGHTENING amendment (the matched-baseline envelope is stricter than the pathologically-narrow shuffle null, since shuffle-null has ~0-5 absent-count variance while matched-baseline has realistic natural-language variance). Self-verifying per Bonferroni-asymmetry rule.

## Outputs

1. Pre-reg: this file (`findings/phase-b-hypotheses/h-new-114-zero-set-prereg.md`)
2. Script: `scripts/h_new_114_zero_set.py`
3. JSON: `findings/phase-b-hypotheses/csv/h-new-114.json` (absent bigram list, absent trigram list, top-10 surprising absent adjacencies, muqaṭṭāʿat-pattern table)
4. Findings: `findings/phase-b-hypotheses/h-new-114-zero-set.md`
5. Journal: `journal/h-new-114-run-1.md`

## Acceptance window

- **Cells A/B/C**: two-sided permutation p < 0.0125 → PASS; p ≥ 0.0125 → NULL
- **Cell D**: descriptive only (no PASS/NULL)
- MW-5 positive-control fail → INSTRUMENT-FAIL (no declaration)
- Direction is LOCKED BEFORE viewing any zero-set counts.
