---
document_type: hypothesis_specification
hypothesis_ids: H-CLASSIC-44, H-CLASSIC-45, H-CLASSIC-46, H-CLASSIC-47, H-CLASSIC-48, H-CLASSIC-49
phase: B
date: 2026-04-13
status: SPECIFIED (awaiting computational-tester dispatch)
author: classical-scholar
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
bonferroni_k: 6 (within this family)
family_wise_alpha: 0.05 → per-hypothesis α = 0.0083
---

# H-CLASSIC-44 through H-CLASSIC-49: Six pre-registered classical-claim tests

Six classical-doctrine tests dispatched as a family. Each targets a distinct classical claim with an explicit pre-registered prediction, null model, and acceptance criterion. Family Bonferroni: k=6 across this document.

All six share the standard rules tuple `(no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)` unless specified otherwise.

---

## H-CLASSIC-44 — al-Zarkashī Burhān nawʿ [PENDING-verify ~13] munāsabāt al-suwar (inter-surah coherence)

### Classical claim
al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *munāsabāt al-āyāt wa-l-suwar* (likely nawʿ 13; **PENDING physical verification**): adjacent surahs in the canonical order exhibit thematic and lexical coherence beyond chance. al-Zarkashī argues that the canonical sequence is not arbitrary but reflects a rhetorical progression, and adjacent surah-pairs should show higher munāsaba than non-adjacent pairs.

### Pre-registered prediction
Adjacent surah pairs (distance d=1 in canonical order) have higher pairwise "munāsaba score" than non-adjacent pairs (d≥2), with monotonic decay as distance increases.

### Operationalization
Munāsaba score = weighted combination of:
- Shared-vocabulary Jaccard (root-level)
- Gzip-pair-compression ratio Δ (surah A gzip + surah B gzip vs concatenated gzip)
- Shared-divine-name count
- Shared-proper-noun (prophet/place) count

Build full 114×114 munāsaba matrix; compute mean score by canonical-order distance bucket d ∈ {1, 2, 3-5, 6-10, 11+}.

### Null model
Random permutation of the 114 surahs (10,000 iterations); test whether the observed distance-decay is above the 99th percentile of permutation nulls.

### Acceptance (pass)
Spearman ρ between distance-bucket and mean-munāsaba-score is **negative** at p < 0.0083 (Bonferroni-corrected).

### Acceptance (strong pass)
Additionally, d=1 mean is above the 99th percentile of d=11+ surah-pair means under permutation.

### Falsification
If ρ ≈ 0 (flat distance-decay) or ρ > 0 (anti-munāsaba): classical al-Zarkashī claim falsified at this test's operationalization. Note that H-NEW-20 already reported a null on the al-Rāzī linear autocorrelation question; H-CLASSIC-44 is distinct because it tests WITHIN-surah linear naẓm there and BETWEEN-surah pairwise munāsaba here. Different scales, different doctrines.

### Known confounders
- Length-matched surahs may compress similarly by construction (gzip bias); orthogonalize by including a length-residualized gzip Δ.
- Muqaṭṭaʿāt surahs cluster in the canonical order — they will contribute shared-opener bias to adjacency. Report with and without muqaṭṭaʿāt-adjacent pairs.

---

## H-CLASSIC-45 — al-Suyūṭī Itqān nawʿ [PENDING-verify ~38 or 37] gharīb al-Qurʾān (rare/difficult lexicon) chronological distribution

### Classical claim
al-Suyūṭī *al-Itqān*, nawʿ on *gharīb al-Qurʾān* (rare/lexically-difficult words; **PENDING physical verification of nawʿ number, likely nawʿ 37 or 38**): al-Suyūṭī argues that the Quran's *gharīb* vocabulary is not randomly distributed but clusters in specific genre and chronology positions — especially eschatological and early-Meccan revelations.

### Pre-registered prediction
*Gharīb* density (rare-root count per 100 tokens) is **higher** in early-Meccan surahs (Nöldeke Meccan-1) than in Medinan surahs, with monotone decrease across Nöldeke periods Meccan-1 → Meccan-2 → Meccan-3 → Medinan.

### Operationalization
*Gharīb* proxy: roots whose total Quranic occurrence count is ≤ 5 (lexicalized hapax-class). Build per-surah gharīb-density. Assign each surah a Nöldeke period (1-4). Compute Spearman ρ(period, gharīb-density).

### Null model
Permute Nöldeke labels across surahs 10,000 times; compute ρ null distribution.

### Acceptance (pass)
ρ < 0 (decreasing gharīb with period) at p < 0.0083.

### Falsification
If ρ ≈ 0 or ρ > 0: al-Suyūṭī's early-Meccan gharīb claim falsified. A positive ρ (gharīb increases Medinan) would be a strong anti-prediction.

### Known confounders
- Surah-length correlates with period (Meccan surahs generally shorter in Nöldeke 1); use per-100-token rate not absolute count.
- Rules-tuple: *root* counts (not orthographic token) to avoid morphological-inflection inflation.

---

## H-CLASSIC-46 — al-Jurjānī *Dalāʾil al-Iʿjāz* taqdīm/taʾkhīr (fronting/postposing) in sentence-level word order

### Classical claim
al-Jurjānī *Dalāʾil al-Iʿjāz* (ed. Shākir; page range **PENDING** — likely pp. 100-150 on *al-taqdīm wa-l-taʾkhīr*): the Quran's word-order deviations from prose default (taqdīm of predicate, fronting of circumstantial phrases) are not free variation but carry rhetorical weight. The verses with the highest rhetorical density (iʿjāz-laden verses) should show elevated taqdīm rates.

### Pre-registered prediction
Taqdīm rate (operationalized as predicate-fronting in verbal sentences) is **higher** in eschatological verses than in other genre classes, consistent with the al-Jurjānī claim that rhetorical peak-verses exhibit maximum word-order marking.

### Operationalization
For each verse:
1. Classify sentence type (verbal/nominal/imperative) using syntactic-dependency proxy.
2. Detect predicate-fronting (verb at verse-start or nominal fronting before its subject — use constituent-order heuristic on the first 5 tokens).
3. Count taqdīm events per verse; normalize by verse length.

Run 5-class genre partition (eschatological/narrative/polemic/legal/hymn, matching Doctrine 1 Test B partition from eschatological-slot-cluster) and compare taqdīm rates.

### Null model
Permute genre labels across verses 10,000 times; χ² test for independence.

### Acceptance (pass)
5-class χ² p < 0.0083 AND the eschatological class has the highest rate (monotone or peak-at-eschatology).

### Falsification
If χ² non-significant or if the taqdīm rate peaks at a non-eschatological class (e.g., polemic): al-Jurjānī's rhetorical-peak claim falsified at this operationalization.

### Known confounders
- Predicate-fronting detection is hard without a proper parser; use conservative heuristic (explicit verb-first pattern at verse-start) and report both strict and relaxed detection rates.
- Sequence-length bias: longer verses have more taqdīm opportunities; per-token normalization required.

---

## H-CLASSIC-47 — al-Biqāʿī *Naẓm al-Durar* adjacent-verse seam-density (seam-Jaccard at verse-pair scale)

### Classical claim
al-Biqāʿī *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar*: every adjacent verse pair is thematically and lexically linked; the seam between verses is where munāsaba operates most densely. Task #21 already ran seam-Jaccard for this claim at the surah-pair level and reported a null on the macro-ring munāsaba thesis; H-CLASSIC-47 re-runs at the **verse-pair-within-surah** scale, which al-Biqāʿī distinguishes from whole-surah munāsaba.

### Pre-registered prediction
Within-surah adjacent-verse pairs (k=1) have higher root-level Jaccard than non-adjacent pairs (k≥3) within the same surah, on the surahs where al-Biqāʿī's commentary is most explicit about verse-by-verse linkage (reportedly the longer Medinan surahs: al-Baqara, Āl ʿImrān, al-Nisāʾ, al-Māʾida).

### Operationalization
For each of the 4 surahs (2, 3, 4, 5), compute pairwise root-Jaccard for all verse pairs (i, j). Bucket by distance |i-j| ∈ {1, 2, 3-5, 6-10, 11+}. Compare mean Jaccard across buckets. Also test on 4 matched shorter surahs as negative control (random Meccan surahs of similar verse count to each Medinan).

### Null model
Within-surah permutation: shuffle verse order within the surah 10,000 times; compute distance-1 mean Jaccard null.

### Acceptance (pass)
For at least 3 of 4 al-Biqāʿī-priority surahs: observed distance-1 Jaccard is above 99th percentile of within-surah permutation null.

### Falsification
If ≤ 1 of 4 surahs passes: al-Biqāʿī's adjacent-verse seam-density claim is falsified at the verse-pair scale.

### Known confounders
- Rhyme-echo and formulaic repetition (e.g., "wa-alladhīna āmanū wa-ʿamilū l-ṣāliḥāti") will inflate adjacent-pair Jaccard independent of semantic munāsaba; report with and without stopword-root removal.
- Orthogonal to H-CLASSIC-44 which tests inter-surah munāsaba.

---

## H-CLASSIC-48 — al-Sakkākī *Miftāḥ al-ʿUlūm* (pp. 527-540, PENDING verify per H-NEW-35) tanāsub al-īqāʿ verse-length rhythmic alternation

### Classical claim
al-Sakkākī *Miftāḥ al-ʿUlūm*, Qism al-Bayān, discussion of *al-īqāʿ* (rhythmic cadence): Quranic surahs exhibit deliberate verse-length alternation patterns that produce audible rhythm. This is distinct from saj' (end-rhyme) and operates at the verse-duration scale. (This is the doctrinal frame registered under H-NEW-35.)

### Pre-registered prediction
Per-surah verse-length autocorrelation at lag k ∈ {1, 2, 3} is **non-zero** at rates exceeding matched-Arabic baseline. Specifically, lag-1 autocorrelation ρ₁ is either positively or negatively biased away from 0 (alternation = negative; sustained = positive), with more surahs showing non-zero ρ₁ than matched-random shuffle.

### Operationalization
For each of 114 surahs with n_verses ≥ 10, compute verse-length autocorrelation ρ_k for k=1,2,3. Compare to:
(a) Within-surah permutation null (shuffle verse lengths)
(b) Matched-Arabic baseline (Bukhari non-Quran and Jāḥiẓ, split into n_verses-matched spans)

Report per-surah |ρ_1| distribution Quran vs baseline.

### Null model (primary)
Within-surah permutation: shuffle verse lengths within each surah 10,000×; compute |ρ_1| null. Count how many surahs exceed 99th percentile.

### Null model (baseline)
Matched-Arabic text split into 114 matched-length spans; compute per-span |ρ_1|; compare distributions.

### Acceptance (pass)
Kolmogorov-Smirnov test between Quran |ρ_1| distribution and baseline |ρ_1| distribution: p < 0.0083.

### Falsification
If Quran |ρ_1| distribution is indistinguishable from baseline: al-Sakkākī's īqāʿ claim falsified at verse-length scale.

### Known confounders
- Short surahs (< 10 verses) excluded from primary analysis but reported in sensitivity.
- Verse-boundary definition is fixed by Ḥafṣ-Kufan counting; sensitivity: re-run with Madanī-I counting for 10 surahs where the ʿadd differs.
- **Overlaps with task #69 H-NEW-35 already in progress**: coordinate with computational-tester to avoid redundant dispatch. H-CLASSIC-48 formalizes the baseline-comparison component that H-NEW-35 registers but may not test at the full ρ_k family.

---

## H-CLASSIC-49 — al-Rummānī *al-Nukat fī iʿjāz al-Qurʾān*, 7 wujūh: specifically *ījāz* (terseness) vs matched-rhyme Arabic

### Classical claim
al-Rummānī *al-Nukat fī iʿjāz al-Qurʾān* (ed. Khalaf Allāh/Sallām 1955, pp. 70-110 approx, **PENDING**): enumerates 7 facets of Quranic iʿjāz. The 3rd wajh, *al-ījāz* (terseness), is al-Rummānī's claim that the Quran achieves higher information-density than comparable Arabic at matched length and rhyme-scheme.

### Pre-registered prediction
Matched-length, matched-end-rhyme Arabic passages (from jāhilī muʿallaqāt, mukhaḍram-era poetry, and early-Islamic sajʿ-prose) have **lower** token-level type-count per 100 tokens than length-matched Quranic passages.

### Operationalization
Sample 500 Quranic 30-token windows with fixed end-rhyme (same last-grapheme across window). Compute type-count (unique root count) per window. Sample 500 matched windows from:
(a) Muʿallaqāt (7 pre-Islamic odes)
(b) Jāḥiẓ *al-Bayān wa-l-Tabyīn* + *al-Ḥayawān* (sajʿ prose)
(c) Bukhari non-Quran (for baseline Arabic without rhyme constraint)

Compare type-count distributions via Mann-Whitney U.

### Null model
Mann-Whitney U on matched-window type-count distributions. No permutation needed; the test statistic is its own null.

### Acceptance (pass)
Quran > Muʿallaqāt AND Quran > Jāḥiẓ AND Quran > Bukhari-noquran, all at p < 0.0083 (so the Bonferroni within H-CLASSIC-49 is k=3 internal → per-comparison 0.0083/3 = 0.00277).

### Falsification
If Quran ≤ any of the three baselines at significance: al-Rummānī's *ījāz* superiority claim is partially or fully falsified.

### Known confounders
- Rhyme-constraint itself constrains vocabulary; sampling matched end-rhyme windows from baseline text may be hard. Use the Muʿallaqāt end-rhyme first-letter-class as the binding for matched sampling.
- Rules-tuple: use *root*-level type-count not orthographic-token to avoid inflection-count inflation (both Quran and baselines use orthographic forms but root-counting is standard for ījāz measurement).
- Register as an internally Bonferroni-corrected family.

---

## Cross-hypothesis coordination

**Overlap with in-flight hypotheses:**
- H-CLASSIC-48 overlaps task #69 H-NEW-35 (al-Sakkākī īqāʿ). Recommend: H-NEW-35 delivers within-surah autocorrelation primary; H-CLASSIC-48 extends with the baseline comparison and full ρ_k family. Coordinate via integrator.
- H-CLASSIC-47 builds on task #21 (al-Biqāʿī macro-ring reported null) with a different operationalization at a different scale (verse-pair within-surah, not whole-surah).
- H-CLASSIC-46 overlaps H-NEW-40 (task #77, al-Jurjānī ḥadhf predicted-elision at rhetorical-peak verses). H-CLASSIC-46 tests taqdīm; H-NEW-40 tests ḥadhf. Both al-Jurjānī Dalāʾil-derived but orthogonal operationalizations.

**Verbatim-confidence caveats (PENDING Phase-2 physical verification):**
- al-Zarkashī Burhān nawʿ numbers (44, 47 elsewhere, potentially 13 here) are all held PENDING until physical edition verification. This is a systemic issue across the classical-scholar deliverables.
- al-Suyūṭī Itqān nawʿ numbers similar.
- al-Jurjānī Dalāʾil Shākir edition page ranges held PENDING.
- al-Sakkākī Miftāḥ page range inherits H-NEW-35's PENDING status.
- al-Rummānī Nukat page range held PENDING.

**Bonferroni family accounting:**
Within H-CLASSIC-44-49: k=6, per-hypothesis α=0.0083.
If any Hx internally runs multiple sub-tests (e.g., H-CLASSIC-49's 3-baseline comparison), internal Bonferroni applies on top.

**Reporting commitments:**
All six hypothesis outcomes to be reported in findings/phase-b-hypotheses/h-classic-4X.md files, one per hypothesis, regardless of pass/fail/null.

---

## Classical-scholar dispatch-note

These six hypotheses target classical doctrines that have not previously been operationalized. Each was selected to:
1. Derive from a specific classical source with textable predictions (not vague theological claim)
2. Admit falsification (the null outcome is not definitionally ruled out by the classical doctrine)
3. Occupy orthogonal computational scales (surah-pair munāsaba vs verse-pair munāsaba vs sentence-level taqdīm vs verse-length rhythm vs passage-level ījāz vs gharīb-density chronology)

The set is designed to produce a **distributed honest outcome**: some hypotheses likely PASS, some likely NULL. A test-family where all six pass is suspicious. The pre-registration + Bonferroni discipline protects against cherry-picking.

Ready for computational-tester dispatch. Recommend processing in order of dispatch-tractability:
1. H-CLASSIC-44 (surah-pair graph) — straightforward
2. H-CLASSIC-45 (gharīb chronology) — straightforward
3. H-CLASSIC-47 (verse-pair within-surah Jaccard) — straightforward
4. H-CLASSIC-48 (īqāʿ autocorrelation + baseline) — medium (coordinate with H-NEW-35)
5. H-CLASSIC-49 (ījāz type-count vs rhyme-matched baseline) — medium (requires matched Muʿallaqāt sampling)
6. H-CLASSIC-46 (taqdīm detection) — hardest (requires constituent-order heuristic)

— classical-scholar
