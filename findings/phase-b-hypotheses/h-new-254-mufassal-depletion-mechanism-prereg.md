---
finding_id: [[h-new-254-mufassal-depletion-mechanism|h-new-254]]
title: "Mufaṣṣal divine-name depletion: compositional choice or length-normalization artifact?"
specialist: [[h-new-254-mufassal-depletion-mechanism|h-new-254]]-specialist
phase: B
status: pre-registered
date_prereg: 2026-04-17
parent: [[h-new-239-divine-name-gradient|h-new-239]]
parent_anchor: MASTER-FINDINGS-LEDGER §2 (divine-names authoritative catalog)
seed: 20260419
bonferroni_k: 1
bonferroni_family: [[h-new-254-mufassal-depletion-mechanism|h-new-254]]-mufassal-depletion-mechanism
alpha_bon: 0.05
alpha_raw: 0.05
verdict: PENDING
rules_tuple:
  orthography: no-tashkeel
  name_list: 99 canonical al-Tirmidhi names (MASTER-LEDGER §2)
  name_identification: DET-MS per divine-names-distribution methodology (uses divine-names-by-verse.csv)
  word_definition: whitespace-split tokens of no-tashkeel surah text
  verse_numbering: hafs-kufan (6236 verses)
  mufassal_boundary: Q 50-114 (classical Zarkashī convention; locked in [[h-new-239-divine-name-gradient|H-NEW-239]])
  null_model: length-matched permutation sampling (per-surah: draw N_s words from corpus-marginal pool)
  data_source_names: findings/phase-b-hypotheses/divine-names-by-verse.csv
  data_source_text: quran-text/quran-no-tashkeel.json

motivation: |
  [[h-new-239-divine-name-gradient|H-NEW-239]] established that divine-name density follows a strong NEGATIVE
  gradient across mushaf position (Spearman ρ = −0.476, p < 10⁻⁴), with the
  mufaṣṣal block (Q 50-114, n=65) exhibiting the LOWEST mean density
  (0.02015) vs ṭiwāl (0.03394), ḥawāmīm (0.03047), and "other" (0.03203).
  The post-hoc MW-U mufaṣṣal vs other p_bonf = 0.00166 was significant.

  This was SURPRISING. Juzʾ 30 short surahs (Q 78-114) contain many
  basmala + short-formula refrains (*qul huwa Allāh aḥad, al-Raḥmān
  al-Raḥīm, etc.*) so a NAIVE length-inflation prior predicted mufaṣṣal
  density would be HIGHER due to short words/short surahs inflating the
  density numerator. The [[h-new-239-divine-name-gradient|H-NEW-239]] REVERSE-PASS on Cell C confirmed the
  opposite: short surahs are DEPLETED on per-word density.

  The mechanistic question [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] addresses: is the mufaṣṣal-depletion
    (a) a GENUINE compositional choice — mufaṣṣal surahs deliberately avoid
        divine-name tokens on a per-word basis, below what corpus marginals
        would produce at their lengths; or
    (b) a LENGTH-NORMALIZATION ARTIFACT — the observed density is what one
        would EXPECT when drawing N_s words from corpus marginals, because
        short surahs have short denominators and the random variance is
        different at small N?

  [[h-new-239-divine-name-gradient|H-NEW-239]]'s MW-5 shuffle null (shuffling token counts across ALL verses)
  showed the SHUFFLED corpus would produce a POSITIVE gradient (ρ = +0.503),
  with mufaṣṣal density INFLATED by short-surah inflation. That already
  signals the observed depletion is fighting the random-placement bias. But
  that null is a WHOLE-CORPUS shuffle, not a per-surah LENGTH-matched
  bootstrap. [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] provides the per-surah length-matched complement:
  for each mufaṣṣal surah separately, what density would corpus-marginal
  sampling produce at that N_s?

hypothesis: |
  H0 (length-artifact): observed mufaṣṣal per-surah density ≈ length-matched
     null density. Combined Stouffer's Z is indistinguishable from 0.
  H1 (compositional choice): observed mufaṣṣal per-surah density
     significantly BELOW length-matched null density. Combined Stouffer's
     Z strongly negative, p < 0.05 under one-tailed less-than test.
  H2 (enrichment, unexpected): observed ABOVE null. Report as a separate
     finding category; NOT pre-committed.

direction: |
  Primary test: one-tailed MEDIA-less-than (observed < null expectation),
  since the parent finding [[h-new-239-divine-name-gradient|H-NEW-239]] already established the DIRECTION of
  depletion; [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] tests the MECHANISM (real choice vs artifact), and
  the pre-committed direction is "observed < null" = compositional choice.
  Two-sided secondary p reported. Per-surah z-score distribution reported
  descriptively.

cells:
  primary: mufassal_combined_stouffer_z_observed_less_than_null
  secondary: per_surah_z_histogram_and_descriptives

bonferroni:
  k: 1
  rationale: |
    Single pre-committed test (Stouffer's combined Z across n=65 mufaṣṣal
    surahs, one-tailed less-than). Per-surah z-scores and per-surah bootstrap
    distributions are DESCRIPTIVE outputs, not independent tests.
  alpha_family: 0.05
  alpha_per_cell: 0.05

negative_controls:
  MW-5_instrument_check: |
    Re-run the full protocol with a SHUFFLED corpus (permute per-verse
    divine-name tokens across the whole 6236-verse space before building
    the corpus-marginal pool). Under a valid instrument, the shuffled-
    corpus observed density should MATCH its length-matched null (both
    sampled from the same marginals), yielding combined z ≈ 0 and
    non-significant p. This confirms the null-sampling machinery is
    unbiased.
  classical_sanity: |
    Report Q 112 al-Ikhlāṣ observed density (0.200, one of the two highest
    in the corpus). It should come out ABOVE its length-matched null
    regardless of the combined mufaṣṣal Stouffer direction — classical
    tawḥīd-saturation surah as a sanity check that per-surah z-scores are
    sensible.

method: |
  Step 1. Load the same data as [[h-new-239-divine-name-gradient|H-NEW-239]]:
    - Per-surah whitespace-token words from quran-no-tashkeel.json.
    - Per-verse divine-name token counts from
      findings/phase-b-hypotheses/divine-names-by-verse.csv.
  Step 2. Build corpus-marginal name-probability:
    - N_words_total = sum of whitespace tokens over full 6236-verse corpus.
    - N_name_tokens_total = sum of divine-name tokens over full corpus.
    - p_corpus = N_name_tokens_total / N_words_total = the expected
      per-word name probability under a uniform-word null.
  Step 3. For each mufaṣṣal surah s ∈ {50, 51, …, 114}:
    - Let N_s = whitespace-token word count for surah s.
    - Observed density D_s^obs = name_tokens_s / N_s.
    - Null: simulate 10000 bootstrap samples of N_s word-indicators each
      Bernoulli(p_corpus). Record null density distribution
      {D_s^null,b : b=1..10000}.
    - Compute per-surah z_s = (D_s^obs − mean(D_s^null)) / sd(D_s^null).
    - Compute per-surah one-tailed bootstrap p_s^less = (# of b where
      D_s^null,b ≤ D_s^obs) / B.
    - (Primary sampling mode pre-committed: per-word independent Bernoulli
      with p = p_corpus. See garden_of_forking_paths for rationale.)
  Step 4. Combined Stouffer across 65 mufaṣṣal surahs:
    - Convert one-tailed per-surah p_s^less to z via inverse Normal CDF.
    - Stouffer Z = sum(z_s) / sqrt(65).
    - Combined one-tailed p_stouffer = 1 − Φ(Z) for the less-than direction
      (large negative Z = PASS H1 = compositional choice; Z ≈ 0 = H0
      length-artifact; large positive Z = H2 enrichment).
  Step 5. MW-5 instrument check: permute per-verse divine-name counts
    uniformly across all 6236 verses (preserving total), rebuild the
    corpus-marginal p and per-surah tokens_s from the shuffled assignment,
    re-run steps 3-4. Report the shuffled Stouffer Z separately.
  Step 6. Sanity: report per-surah z for Q 112, Q 110, Q 85, Q 65, Q 59
    (top-density mufaṣṣal surahs per [[h-new-239-divine-name-gradient|H-NEW-239]] Top-10).

garden_of_forking_paths: |
  - Mufaṣṣal boundary: Q 50-114 LOCKED per Zarkashī convention and [[h-new-239-divine-name-gradient|H-NEW-239]].
    No alternative (Q 49 or Q 67 onset) considered.
  - Null model: per-word independent Bernoulli(p_corpus) is the PRIMARY
    LOCKED choice. Rationale: matches exactly what "length-artifact"
    would mean — a surah of length N_s independently sampled from corpus-
    average word-level name rate. Rejects conditional samplers that
    preserve verse-structure or phrase-adjacency because those would
    ALREADY bake in compositional structure. Alternative per-word samplers
    (draw-without-replacement from concrete corpus-token pool;
    verse-block-permutation) are NOT pre-committed and will only be run
    as robustness follow-ups if the primary result is ambiguous.
  - Per-surah 10000 bootstrap samples locked.
  - Word count = whitespace-split tokens of no-tashkeel text, matching
    [[h-new-239-divine-name-gradient|H-NEW-239]]'s denominator.
  - Divine-name tokens per surah = sum over verse rows in
    divine-names-by-verse.csv, restricted to verses within the surah.
    This uses the same DET-MS filter locked by the parent data file.
  - Q 1 al-Fātiḥa and Q 2-49 are INCLUDED only in the p_corpus pool, not
    tested individually. Only Q 50-114 are evaluated for per-surah
    Stouffer entry.
  - Seed 20260419 for Bernoulli sampling. Shuffled-corpus MW-5 uses
    seed = 20260419 + 1 (consistent with [[h-new-239-divine-name-gradient|H-NEW-239]] convention).
  - Direction pre-committed: observed < null ⇒ compositional choice PASS.
    H2 (enrichment) handled descriptively if observed.
  - Stouffer weights are UNIFORM across the 65 mufaṣṣal surahs. Sensitivity
    under word-weighted Stouffer is a DEFERRED alternative.

expected_outcomes: |
  Based on [[h-new-239-divine-name-gradient|H-NEW-239]]'s REVERSE-PASS on Cell C (juz30 density BELOW rest
  under two-sided MW-U), the prior expectation is that observed mufaṣṣal
  density will be BELOW length-matched null. Combined Stouffer Z negative
  of magnitude |Z| > 3 would be a strong compositional-choice PASS; |Z|
  near 0 would support the length-artifact hypothesis; Z > 0 (H2
  enrichment) would be a surprise and will be reported carefully.

honest_limits: |
  - Per-word Bernoulli null ignores SYNTACTIC context. A token drawn from
    inside Q 2:255 ayat-al-kursī is treated identically to one from inside
    a qissat narrative verse. This is INTENTIONAL for the length-artifact
    null but is a limitation for extrapolating to "composition" in a
    richer sense.
  - p_corpus is a single scalar marginal. A more sophisticated null could
    condition on Meccan/Medinan classification or on block. But the
    language of "length-artifact" specifically means marginal-uniform,
    so a richer null would test a DIFFERENT hypothesis.
  - Q 1 al-Fātiḥa is excluded from the Stouffer family (only Q 50-114).
    Q 1 is the #1 density surah (0.207); its exclusion is per the locked
    mufaṣṣal boundary.
  - Discreteness: for very short surahs (Q 108 al-Kawthar, N=11 words),
    the Bernoulli null density is extremely discrete (11 bins of density
    0/11, 1/11, …). Bootstrap p-values may be coarse at these surahs.
    Stouffer combining across 65 surahs is robust to this.
  - Divine-name word-count in divine-names-by-verse.csv uses DET-MS; there
    is a potential under-count of ambiguous-context names (al-Ḥaqq al-Malik
    etc.). This is the same denominator and numerator as [[h-new-239-divine-name-gradient|H-NEW-239]]'s
    instrument, so comparative claims are consistent.

classical_anchor: |
  - al-Ghazālī *al-Maqṣad al-Asnā fī Sharḥ Asmāʾ Allāh al-Ḥusnā*: the
    three-family (jalāl / jamāl / kamāl) theological-family structure.
    [[h-new-170-99name-network|H-NEW-170]] validated the partition. Question [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] addresses is
    whether mufaṣṣal's depletion is a COMPOSITIONAL choice or an ARTIFACT.
  - al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān* on the mufaṣṣal as
    "revelatory-opener" block with distinctive prosodic structure — short
    verses, rapid rhyme. If the compositional-choice hypothesis PASSES,
    this would quantitatively ratify Zarkashī's claim that mufaṣṣal has
    a DIFFERENT rhetorical device (saj', short oaths, cosmological
    imagery) from the ḥizbāniyyah and ḥawāmīm, and the difference is
    measurable on the 99-names axis.
  - al-Suyūṭī *al-Itqān fī ʿUlūm al-Qurʾān* nawʿ 8 on mufaṣṣal as
    punctuative short-verse acceleration, not divine-name saturation.

interpretation_rules: |
  - If combined Stouffer Z ≤ −1.645 (one-tailed α=0.05):
    COMPOSITIONAL CHOICE — mufaṣṣal deliberately avoids divine-names on a
    per-word basis, below what corpus-marginal sampling at its lengths
    would produce. Strengthens the Zarkashī "different-device" reading.
  - If combined Stouffer Z ∈ (−1.645, 1.645) (i.e., |Z| < 1.645):
    LENGTH-ARTIFACT — mufaṣṣal depletion is what corpus-marginal sampling
    at mufaṣṣal lengths would produce. The [[h-new-239-divine-name-gradient|H-NEW-239]] depletion signal
    collapses to a denominator-inflation story when per-surah matched.
    Reported honestly.
  - If combined Stouffer Z ≥ +1.645: UNEXPECTED ENRICHMENT — mufaṣṣal is
    actually ABOVE length-expectation. Flag carefully; would contradict
    [[h-new-239-divine-name-gradient|H-NEW-239]]'s block-level MW-U and require reconciliation.

cross_refs:
  - parent: [[h-new-239-divine-name-gradient|h-new-239]]-divine-name-gradient.md
  - MASTER-FINDINGS-LEDGER §2 (divine-names canonical data)
  - sibling: divine-names-distribution.md
  - cross: [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]-four-principle-reduced-model.md (M1 block structure)
  - cross: [[h-new-111-fisher-rao-mushaf|h-new-111]]-fisher-rao-mushaf.md (geodesic-optimality architecture)

deliverables:
  - findings/phase-b-hypotheses/h-new-254-mufassal-depletion-mechanism.md
  - findings/phase-b-hypotheses/csv/h-new-254.json
  - findings/phase-b-hypotheses/csv/h-new-254-per-surah.tsv
  - scripts/h_new_254_mufassal_depletion.py
  - journal/h-new-254-run-1.md
  - MASTER-FINDINGS-LEDGER Wave-5 entry
