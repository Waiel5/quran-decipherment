---
finding_id: h-new-91
phase: B
status: PRE-REGISTERED — same-session computational-tester self-pre-reg per PRE-REG-STANDARD-04
pre_registered_by: h-new-91-specialist
registration_date: 2026-04-15
parent_task: H-NEW-91 (project queue)
rules_tuple: (no-tashkeel, STEM-root tokens, QAC-roots v0.4, basmala-counted-only-in-surah-1, mushaf order, Hafs-Kufan verse numbering)
seed: 20260415
sided_test: two-sided for all primary tests; one-sided POSITIVE for Q26 al-Shuʿarāʾ pre-committed direction
bonferroni_k: 5
alpha_bon: 0.01    # = 0.05 / 5
null_publishable: true
positive_publishable: true
classical_anchor: al-Bāqillānī Iʿjāz al-Qurʾān §3 (jamāl wa-tafannun fī l-alfāẓ — vocabulary-range as eloquence index); al-Suyūṭī Itqān nawʿ 49 al-gharīb fī l-Qurʾān (lexical-rarity catalog)
parent_finding: MASTER:finding-#7 hapax-final z=10.61; H-NEW-23 hapax-slot mechanism PARTIAL-CONFIRMED
---

# [[h-new-91-rare-root-density|H-NEW-91]] — Rare-root density per surah (PRE-REG)

## Question

Each Quranic surah has a vocabulary "rarity profile". Some surahs are dominated by ultra-frequent roots (kwn, qwl, Allāh-class function vocabulary). Others recruit rare-roots (hapax + low-count) at much higher rates.

**Hypothesis (intuition; no fixed number)**: rare-root density is **not uniform** across surahs and clusters in (a) short oath-cluster eschatological surahs, (b) the narrative-vocabulary outlier Q 26 al-Shuʿarāʾ (the prompt's `narrative-vocabulary` claim).

This pre-registration LOCKS the metric, the comparison classes, the length-control, and the cross-reference design BEFORE running.

## Metric definitions (LOCKED 2026-04-15)

For each surah s with N_s STEM root-bearing tokens (one count per word with a ROOT field; PREFIX/SUFFIX excluded; basmala counted only in surah 1):

1. **mean_freq(s)** = (1/N_s) · Σ_{i∈s} f(root_i)
   where f(r) = global QAC count of root r (from data/morphology/root-stats.csv).
   LOWER value = MORE rare-root concentration.

2. **geom_mean_freq(s)** = exp((1/N_s) · Σ log f(root_i))
   Less length-sensitive than arithmetic mean (compresses heavy tail of common roots).
   PRIMARY metric for ranking.

3. **rare_density_5(s)** = (#tokens whose root has global f ≤ 5) / N_s
   Per-surah RARE-ROOT density (where "rare" is defined as global count ≤ 5).
   Threshold `5` is locked to match H-NEW-29 minimum-count rule.

4. **hapax_density(s)** = (#tokens whose root has global f = 1) / N_s
   Per-surah HAPAX density.

5. **common_only_density(s)** = (#tokens whose root has global f ≥ 100) / N_s
   Per-surah COMMON-vocabulary density.
   Threshold `100` matches the prompt's "common (>100 uses)" definition.

These five metrics are computed per surah and ranked.

## Pre-registered tests (5 tests; Bonferroni k=5, α_bon=0.01)

### Test 1 — Heterogeneity vs uniform-vocabulary null (primary)

**Null**: per-surah `geom_mean_freq` is consistent with uniform random sampling from the global root distribution at each surah's N_s.
**Alternative**: per-surah `geom_mean_freq` heterogeneity exceeds uniform-sampling expectation.
**Procedure**: For each surah, simulate 10,000 random samples of N_s tokens from the global root distribution (weighted by global root counts); compute simulated `geom_mean_freq`; the per-surah z-score of the observed value vs simulated mean. Aggregate via Σ z² (sum of squared z), test against null via permutation (random reshuffling of root labels across the entire token sequence, 10,000 perms, holding per-surah N_s fixed).
**Verdict criterion**: two-sided permutation p < α_bon = 0.01 → PASS heterogeneity.
**Effect-size report**: per-surah z-score for top-15 and bottom-15 surahs.

### Test 2 — Length confound (Spearman length partial)

**Question**: is `geom_mean_freq` mostly determined by N_s (length confound, like Zipf α was in zipf-per-surah)?
**Procedure**: Spearman ρ(geom_mean_freq, log N_s) and partial Spearman ρ(geom_mean_freq, X_genre | log N_s) where X_genre is dummy-coded genre (using H-NEW-23 genre coding, see §Genre).
**Verdict criterion**: 
- |ρ_raw| > 0.5: report as "primary signal length-confounded; report length-residualized rank only."
- partial ρ_genre > 0.20 with permutation p < α_bon: PASS genre clustering.
**Note**: This test FOLLOWS THE LESSON FROM zipf-per-surah-run-1 — length confound suspected upfront.

### Test 3 — Q 26 al-Shuʿarāʾ rank claim (PRE-COMMITTED ONE-SIDED)

**Pre-committed direction**: Q 26 al-Shuʿarāʾ is in the BOTTOM 15 by `geom_mean_freq` rank (i.e., among the 15 surahs with the lowest mean-frequency = most rare-vocabulary). This is the prompt's "most narrative-vocabulary surah" claim, operationalized.
**Procedure**: After computing `geom_mean_freq` for all 114 surahs, check Q 26's rank.
- IF Q 26 in bottom 15 → PASS.
- IF Q 26 in bottom 30 → PARTIAL-PASS (the directional intuition holds at coarser bin).
- IF Q 26 above median → FAIL the prompt claim.
**Length-controlled variant**: also report Q 26's residualized rank (after removing log-N_s effect via 5-quintile binning).
**Note**: The pre-committed direction is published in the prompt; this is a confirmatory directional test with no slack.

### Test 4 — H-NEW-23 hapax-final cross-reference

**Question**: Do surahs with high rare-root density also have high hapax-FINAL placement rate (the H-NEW-23 mechanism)?
**Procedure**: For each surah, compute (a) `rare_density_5` rank, (b) per-surah hapax-final rate (from H-NEW-23's per-verse data: # hapaxes at verse-final / # total hapaxes in surah; surahs with 0 hapaxes excluded).
**Test**: Spearman ρ between rare_density_5 rank and hapax-final-rate.
**Verdict**: |ρ| > 0.30 with permutation p < α_bon = 0.01 → PASS convergence.
**Note**: The expected direction is POSITIVE (high-rare-density surahs more often place hapaxes at verse-final), but we are using two-sided p because H-NEW-23 found the slot mechanism is PRESENT but uniform across surahs, not necessarily more concentrated in rare-vocab surahs.

### Test 5 — Genre clustering (categorical ANOVA)

**Question**: Do `geom_mean_freq` and `rare_density_5` cluster by surah genre/Itqān-style class?
**Procedure**: Use H-NEW-23 genre coding (narrative / eschatological / legal / hymn / polemic; surah-level, mode of constituent verses). Compute per-genre mean of `geom_mean_freq` and `rare_density_5`. Permutation ANOVA: shuffle genre labels across surahs 10,000 times; compute observed F = between-group var / within-group var; p = fraction of perms with F ≥ observed.
**Verdict**: permutation p < α_bon = 0.01 for either `geom_mean_freq` or `rare_density_5` → PASS genre clustering.

## Bonferroni family

5 tests, α_per = 0.05 / 5 = 0.01. This is a closed family (locked at 5 tests in this pre-reg).

Per [Bonferroni tightening vs loosening](feedback_bonferroni_tightening_vs_loosening.md): we may TIGHTEN by adding more tests (which would lower α_bon) but we may NOT loosen by removing tests after seeing results.

## Composite verdict

- 0 tests significant → composite NULL
- 1 test significant → composite WEAK-EXPLORATORY
- 2-3 tests significant → composite PARTIAL-PASS
- 4-5 tests significant → composite STRONG-PASS

## Genre coding (LOCKED, copied from H-NEW-23)

Coarse Itqān nawʿ-65 surah-level coding:
- **eschatological**: Meccan surahs 78+ (78–114)
- **hymn**: short Meccan hymn surahs 1, 87, 94, 112, 113, 114
- **narrative**: Meccan known narrative 12, 18, 19, 20, 28, plus default for un-classified Meccan
- **legal**: Medinan with known legal focus {2, 3, 4, 5, 24, 33, 58, 60, 65, 66}
- **polemic**: Medinan {8, 9, 47, 48, 49, 59}
- All other Medinan default to **narrative**.

Note: This coding is COARSE. It is not optimized for this hypothesis; it is the same coding that H-NEW-23 used and that finding's eschatological cluster is well-attested.

## Garden-of-forking-paths log (BEFORE running)

Decisions made BEFORE seeing results:

1. **PRIMARY metric is `geom_mean_freq`**, not arithmetic mean. Rationale: heavy-tailed root distribution (kwn = 1390 at top, hapaxes at bottom) makes arithmetic mean dominated by 1-2 ultra-frequent roots in any surah. Geometric mean is the standard logarithm-of-Zipf average, gives equal weight to log-rarity. Locking this BEFORE seeing any per-surah numbers prevents post-hoc choice of "which mean."

2. **Rare = global count ≤ 5**. Rationale: matches H-NEW-29's min-count rule (n=5 is the standard "support enough to compute CV" threshold). I considered ≤ 3 (matches "rare" in al-Suyūṭī gharīb tradition) and ≤ 10 (smoother estimator). Locking ≤ 5 prevents threshold-shopping.

3. **Common = global count ≥ 100**. Locked at the prompt's threshold ("common >100 uses").

4. **Length confound**: predicted UPFRONT (per zipf-per-surah-run-1 lesson). Test 2 reports both raw and residualized statistics. We commit BEFORE seeing the data that if |ρ_raw| > 0.5, only the residualized rank is interpreted as the heterogeneity claim.

5. **Q 26 direction**: ONE-SIDED locked downward (rare-vocab heavy = bottom rank). The prompt asserts Q 26 is "the most narrative-vocabulary surah"; we interpret "most narrative-vocabulary" as "highest fraction of low-frequency content roots" (because narrative requires rare proper-noun and characteristic-action vocabulary). If this interpretation is incorrect, the test fails.

6. **Surah-1 al-Fāṭiḥah handling**: Fāṭiḥah has only 29 lemma tokens (per zipf-per-surah CSV) and 26 STEM root-tokens. We will INCLUDE it in the per-surah ranking (no min-N filter), but flag any insufficient-data caveats in the report. Filtering-by-N would create a preferential exclusion.

7. **Basmala policy**: counted-only-in-surah-1 (Leeds default; same as all parent findings).

8. **Permutation seed**: 20260415, 10,000 perms across all permutation tests.

9. **NOT pre-registered (and NOT to be added post-hoc)**: per-juzʾ analysis, per-rukūʿ analysis, mufaṣṣal-only sub-analysis. If observed results suggest these as follow-ups, they go in §FOLLOW-UPS as new [[h-new-91-rare-root-density|H-NEW-91]]-X spinoffs requiring fresh pre-reg.

## Outputs

- Script: `scripts/h_new_91_rare_root_density.py`
- Per-surah CSV: `findings/phase-b-hypotheses/csv/h-new-91-per-surah.csv`
- Summary JSON: `findings/phase-b-hypotheses/csv/h-new-91.json`
- Findings: `findings/phase-b-hypotheses/h-new-91-rare-root-density.md`
- Journal: `journal/h-new-91-run-1.md`
- This pre-reg: `findings/phase-b-hypotheses/h-new-91-rare-root-density-prereg.md`

## Pre-reg SHA cross-reference

The script will compute SHA-256 of THIS pre-reg file at run time and embed it in the JSON output for tamper-evidence.
