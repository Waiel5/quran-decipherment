---
id: H-NEW-123
title: Heap's law type-token exponent — is the Quran's vocabulary-growth rate β distinctive?
status: PRE-REGISTERED (locked before any β, K, V(N), or log-log slope viewed)
registered: 2026-04-17
spec_locked_at: 2026-04-17
bonferroni_family: h-new-123-heap-law
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-surah-1, hafs-kufan, mashriqi)
primary_corpus: quran-text/quran-no-tashkeel.json
baselines:
  - data/baseline-corpora/raw/matched-bukhari-77k.txt
  - data/baseline-corpora/raw/jahiz-hayawan.txt
  - data/baseline-corpora/raw/muallaqa-*.txt (7 muʿallaqāt concatenated)
direction_primary: β_Quran < β_Bukhari AND β_Quran < β_Jahiz AND β_Quran < β_Muallaqat (all one-sided, 3 cells, indexed for Bonferroni)
direction_secondary_shuffle: β_Quran == β_shuffled-Quran (null is equality; two-sided)
direction_tertiary_muq: β_muq < β_nonmuq (muqaṭṭāʿat surahs have more compressed lexicon, one-sided; EXPLORATORY not in Bonferroni family)
seed: 20260417
fit_function: log-log OLS on (log N, log V)
alpha_per_cell: 0.0125
---

# [[h-new-123-heap-law|H-NEW-123]] — Heap's law type-token exponent, Quran vs matched Arabic corpora

## Question

Heap's law: V(N) = K · N^β, where V is vocabulary (distinct types) and N is tokens. The exponent β is a standard measure of lexical-diversity growth:
- β → 1: every new token is a new type (maximal diversity)
- β → 0: vocabulary saturates fast (compressed, repetitive lexicon)
- Typical English prose β ≈ 0.4–0.6
- Theoretical limit for Zipf-distributed text: β = 1 / α (Heaps-Zipf duality)

Classical Arabic tradition (al-Suyūṭī, al-Rāghib al-Iṣfahānī) notes the Quran has a COMPACT root-lexicon (~1,636 roots across ~77K tokens). We ask: does this compactness show up as a distinctively LOW Heap's-law β compared to matched-length Arabic prose and poetry? And is it a function of ORDERING or only of the type-token multiset?

## Pre-committed test family (k=4, α_per = 0.0125)

**Cell A1**: β_Quran < β_Bukhari (matched-77K prose), one-sided, bootstrap.
**Cell A2**: β_Quran < β_Jahiz-Hayawan, one-sided, bootstrap.
**Cell A3**: β_Quran < β_Muallaqat (7 poems concatenated), one-sided, bootstrap.
**Cell B**: β_Quran ≠ β_Quran-shuffled (random word-order null on the same multiset), two-sided, bootstrap.

Cell B tests whether β depends on TOKEN ORDERING (a structural property) or only on the type-token frequency multiset (invariant under shuffle). If β is shuffle-invariant, Heap's law is not detecting anything beyond Zipfian frequency distribution; if it differs, ordering contains additional Heap-level information.

Bonferroni family = 4. α_Bonferroni = 0.05 / 4 = 0.0125 per cell.

## Secondary (EXPLORATORY, NOT in Bonferroni family)

**Cell C (exploratory)**: per-surah β ranking; β_muqaṭṭāʿat-surahs vs β_non-muqaṭṭāʿat-surahs, one-sided Mann-Whitney, single-test α=0.05. Flagged as EXPLORATORY because surah-level β is noisy for small surahs.

## Method — LOCKED

1. **Normalize**. Apply standard project normalization: strip tashkeel (U+064B..U+065F, U+0670), strip tatweel (U+0640), strip recitation marks (U+06D6..U+06ED), keep only Arabic letter graphemes (U+0621..U+064A ∪ U+0671..U+06D3) and whitespace, split on whitespace. Matches `data/baseline-corpora/analyze.py` normalize() — same as [[h-new-48-poetic-meter|H-NEW-48]] baselines.
2. **Build token stream**. In canonical order per corpus. For Quran: surah 1..114 then verse 1..N; basmala counted only in surah 1 (native to JSON). For Bukhārī: file order. For Jāḥiẓ: file order. For Muʿallaqāt: concatenate the 7 cleaned files (imru-al-qais, tarafa, zuhayr, labid, antara, amr-bin-kulthum, harith) alphabetically. For shuffled-Quran: shuffle the Quran token list with seed 20260417.
3. **V(N) curve**. Starting at N=100 and stepping in increments of 50, walk N up to total-tokens; at each N record V(N) = |{distinct types seen in the first N tokens}|. LOCKED step=50 (not viewed; balances resolution and compute).
4. **Fit**. OLS on (log N, log V) → slope β, intercept log K. LOCKED. No lowess, no segmented, no weighted. Simple log-log OLS.
5. **Bootstrap for β**. For each corpus: draw 1,000 block-bootstrap resamples of the token stream (block size = 100, preserving local type-token correlation structure under contiguous-block resampling). For each resample, re-compute the V(N) curve and re-fit β. Use the bootstrap β distribution for CI and for cell-level p-values.
6. **Cell A p-value**. For each baseline B, one-sided p = fraction of (β_Quran_boot - β_B_boot) resamples ≥ 0. Bootstrapped difference is paired by resample index (not paired across corpora; independent resamples combined into the difference distribution).
7. **Cell B p-value**. shuffled Quran re-fit with SAME token multiset, different order. Two-sided p = 2 × min(left, right) tail of β_Quran_boot - β_shuffled_boot.
8. **Length matching**. All baselines are truncated to Quran token count (N_Quran) after normalization, to match length exactly for primary cells. This implements MW-1 at primary level (length CANNOT be a free variable).

## Positive control (MW-5)

On a random-uniform-over-N-types corpus (every token IID uniform over a fixed vocabulary V*), Heap's law β should be LOW (saturating fast as soon as all V* types are seen). As a POSITIVE CONTROL: generate 77K tokens IID uniform over 5,000 types (matches Quran's approximate type count); fit β; verify β < 0.5 (saturation signature). On a corpus where every token is a unique type (maximal diversity null), β should be ≈ 1.0. LOCKED before viewing any corpus β.

## Garden-of-forking-paths disclosure

- Heap's law is well-studied in computational linguistics but (to our knowledge) not previously applied to the Quran-vs-Arabic-baselines question. This is the NOVEL operationalization; β is the single locked statistic (no multiple β-definitions explored).
- Step size (50), bootstrap count (1000), block size (100), starting N (100) all LOCKED from methodology convention, not tuned.
- OLS vs MLE: OLS chosen because Heap's law fits are conventionally reported as log-log OLS slopes; MLE (Poisson or negative-binomial) would require distributional assumptions not universally granted.
- Concatenation order of 7 muʿallaqāt is ALPHABETICAL by poet-Latin-name. Sensitivity not explored.
- Muqaṭṭāʿat surah set (n=29) from [[h-new-61-opening-words|H-NEW-61]] / [[h-new-56-five-exceptions|H-NEW-56]] canonical list.
- The tertiary Cell C is EXPLORATORY (surah-N is small, 5–6000 tokens; β fits are noisy); any PASS there will be flagged post-hoc and queued for replication.

## Acceptance windows

- Cell A (each baseline): PASS if one-sided p < 0.0125 AND observed β_Quran < observed β_baseline.
- Cell B: PASS if two-sided p < 0.0125 (difference is nontrivial). NULL if p ≥ 0.0125 (i.e., β is effectively a function of type-token multiset alone).
- Cell C: PASS-EXPLORATORY if one-sided Mann-Whitney p < 0.05 AND β_muq median < β_nonmuq median. Queued for replication, NOT promoted.
- MW-5 positive controls: both IID-uniform (β < 0.5) and all-unique (β ≈ 1.0) must PASS before primary cells are interpretable. If either fails → report NULL-BROKEN, do not publish primary.

## Verdict ceiling

PASS-DIRECTED per H-NEW-N convention (this is a novel metric on the project corpus; replication requires an independent operationalization — e.g., type-token MATTR or moving-average-token-type-ratio — queued as H-NEW-124 if PASS).
