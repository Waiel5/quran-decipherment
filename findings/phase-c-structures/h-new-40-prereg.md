---
finding_id: h-new-40-prereg
phase: B-execution
status: PRE-REGISTERED, execution gated on QAC ḥadhf-detector TSV (#123) delivery
date: 2026-04-13
locked_at: 2026-04-13
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
parent_finding: h-new-40 al-Jurjānī ḥadhf predicted-elision clustering at rhetorical-peak verses
classical_anchor: findings/classical-sources/h-new-40-convergence-analysis.md (CONVERGENCE-GATE-PASSED 37.3% at 2026-04-13)
pre_registration_reference: THIS FILE (locked 2026-04-13 BEFORE QAC detector run, per PRE-REG-STANDARD-04)
bonferroni_k: 5
bonferroni_family: 3 ḥadhf subtypes (subject, addressee, apodosis) + aggregate (any-subtype) + 28-row STRICT sub-test
alpha_unadjusted: 0.05 family-wise
alpha_bon: 0.01 per test (0.05 / 5)
seed: 20260414
null_publishable: true
positive_publishable: true
one_sided_justification: one-tailed (predicted direction is ENRICHMENT of ḥadhf at peak verses, per al-Jurjānī Dalāʾil thesis that elision concentrates at points of maximal rhetorical compression)
---

# H-NEW-40 — Pre-registration

al-Jurjānī ḥadhf (predicted elision) clustering at rhetorical-peak verses.

## 1. Hypothesis

**Primary:** Verses identified by both al-Biqāʿī and al-Rāzī as rhetorical peaks (138-row HIGH intersection) exhibit ENRICHED ḥadhf-construction density relative to non-peak verses from the same surah-pool, after residualizing on verse length.

**Theoretical basis:** al-Jurjānī, *Dalāʾil al-Iʿjāz*, treats *ḥadhf* (deletion / elision) as one of the highest-precision indicators of *naẓm*-density: when a sentence has reached maximum rhetorical compression, the speaker can omit (subject, addressee, apodosis) constituents because the surrounding semantic field is dense enough to recover the deleted element unambiguously. The predicted observation: *ḥadhf concentrates at points of maximal rhetorical compression* — i.e., the rhetorical peaks of a surah.

**Scope of test:** This pre-reg locks the EXECUTION of H-NEW-40 only; the classical convergence gate has already PASSED (see `findings/classical-sources/h-new-40-convergence-analysis.md`).

## 2. Pre-registered direction

**Direction (one-sided):** Peak verses exhibit HIGHER ḥadhf density than length-matched non-peak verses. Sign: ḥadhf_rate(peak) > ḥadhf_rate(non-peak).

**Reverse signal as separate finding:** A reverse signal (peaks have LOWER ḥadhf density) would be filed as an exploratory side-finding `h-new-40-reverse-suppression.md`, NOT as the primary finding. Sign-flip post-hoc into the primary is prohibited.

## 3. Test sets (locked from classical-scholar deliverable)

All sets are derived from `findings/classical-sources/h-new-40-classical-peak-verses-intersection.tsv` (138 rows) per the convergence-analysis memo §5.2.

| Set | N | Source | Confidence | Use |
|---|---|---|---|---|
| **PRIMARY** | 138 | Exact (surah, verse) intersection of Biqāʿī + Rāzī peak-keyword tagging | HIGH | Primary 4 tests (subject, addressee, apodosis, aggregate) |
| **STRICT** | 28 | Both scholars use strong peak keyword (`المقصود`/`مقصود`/`المقصد`/`مقصد`) | HIGHEST | 5th test as sensitivity check |
| **ROBUSTNESS** | 269 | Fuzzy ±2-verse-window intersection | MEDIUM | Robustness/power-boost only, NOT in Bonferroni family |

**Contrast set:** Drawn live during execution from the 84 surahs co-covered by both scholars. For each peak verse, draw all non-peak verses from the same surah, stratified into the same length-decile (length-deciles per H-NEW-META-3 protocol: 9 break-points computed over pooled Quran of 6236 verses). The contrast set is by-construction matched on surah-id and verse-length-decile.

## 4. ḥadhf detector (input dependency)

**Source:** `data/h_new_40/qac_hadhf_detector.tsv` — to be delivered by arabic-specialist (task #123).

**Required schema:**
```
verse_id    surah    aya    subtype    confidence    source_method
```

Where:
- `subtype ∈ {subject, addressee, apodosis}` — the three al-Jurjānī ḥadhf classes locked for this pre-reg.
- `confidence ∈ [0, 1]` — detector-internal confidence score.
- `source_method` — one of `qac_morph_rule`, `dependency_parse`, `manual_seed`, etc.

**Confidence threshold:** Pre-reg locks `confidence ≥ 0.5` for the primary test. Robustness sweep over `{0.3, 0.5, 0.7}` is permitted as a sensitivity check NOT in the Bonferroni family.

**Multiple-subtype handling:** A verse can have ≥1 subtype tags. The aggregate test counts the verse as ḥadhf-positive if it has ≥1 tag of ANY subtype above the threshold.

## 5. Statistical tests (Bonferroni family k=5)

All five tests share the same null hypothesis: peak-verse ḥadhf rate equals length-matched non-peak ḥadhf rate from the same surahs.

### Test 1 — Subject ḥadhf (one-tailed Fisher exact)

**2×2 table:**
```
                    subject_hadhf=1    subject_hadhf=0
peak_verses (138)   a                  b
non_peak_matched    c                  d
```

**Statistic:** Fisher exact one-sided p-value, alternative = "greater" (peak > non-peak in odds-ratio direction).

**PASS:** p_one-sided < α_bon = 0.01.

### Test 2 — Addressee ḥadhf (one-tailed Fisher exact)

Same as Test 1 with `subtype = addressee`.

### Test 3 — Apodosis ḥadhf (one-tailed Fisher exact)

Same as Test 1 with `subtype = apodosis`.

### Test 4 — Aggregate any-ḥadhf (one-tailed Fisher exact)

Same as Test 1 with `verse has ≥1 ḥadhf tag of ANY subtype`.

### Test 5 — STRICT sub-test (one-tailed Fisher exact)

Same 2×2 construction but using the **28-row STRICT set** (both scholars use strong keyword) as the peak set, drawing length-matched non-peak contrast from the strict set's covered surahs.

**Bonferroni:** α_bon = 0.05 / 5 = **0.01**.

## 6. Length residualization (MW-2 audit-013 mandate)

The 2×2 Fisher exact above stratifies on length-decile via the contrast-set construction, but classical findings have repeatedly required additional **OLS residualization** on verse length per MW-2 / audit-013. This is added as a **mandatory secondary check** for each test that PASSES Fisher exact:

**Specification:**
1. Define `y = 1[verse has ḥadhf-tag of given subtype, confidence ≥ 0.5]`.
2. Define `x_peak = 1[verse ∈ peak set]`, `x_length = verse word-count`.
3. Fit OLS: `y ~ x_peak + x_length + intercept` over the union (peak ∪ matched non-peak) verse pool.
4. Report the coefficient on `x_peak` and its t-statistic.

**Secondary PASS:** The OLS coefficient on `x_peak` must be (a) positive in the predicted direction, (b) significant at p < α_bon = 0.01 one-tailed.

**Combined verdict:**
- **STRONG PASS:** Both Fisher exact (p < 0.01) AND OLS (coeff > 0, p < 0.01) pass.
- **PRIMARY PASS:** Fisher exact passes; OLS direction is correct but p ∈ [0.01, 0.05]. Classed as PRIMARY PASS WITH WEAK RESIDUALIZATION.
- **OLS-DEMOTED:** Fisher passes but OLS direction REVERSES — demotes Fisher to artifact-suspect; verdict NULL.
- **NULL:** Fisher exact fails (p ≥ 0.01).

## 7. Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| All 5 Fisher tests PASS at α_bon = 0.01, all 5 OLS residualizations confirm direction at p < 0.01 | **STRONG PASS** — al-Jurjānī ḥadhf-at-peaks thesis confirmed across all three subtypes + aggregate + STRICT |
| 4/5 Fisher PASS + matching OLS direction | **PASS** — al-Jurjānī thesis confirmed, with subtype-specific note for the failing cell |
| 2-3/5 Fisher PASS | **PARTIAL** — file as "subtype-specific evidence for al-Jurjānī ḥadhf-at-peaks" |
| 1/5 Fisher PASS | **WEAK / NULL-LEANING** — exploratory only, do not claim primary |
| 0/5 Fisher PASS | **NULL** — al-Jurjānī thesis not confirmed at peak-verse granularity |
| Any cell OLS-DEMOTED (Fisher passes, OLS reverses) | **DEMOTE** that cell only; remaining cells judged independently |
| Any aggregate REVERSE direction (peak < non-peak at p < 0.01) | **REVERSE-SIGNAL** — file separately as `h-new-40-reverse-suppression.md`; do NOT claim as primary |

## 8. Robustness checks (NOT in Bonferroni family)

These supplement the locked tests but cannot upgrade the verdict:

1. **269-row fuzzy ±2-window set** — re-run all 5 tests; expected to be slightly weaker due to noise but directionally consistent.
2. **Confidence threshold sweep** — re-run primary at `{0.3, 0.5, 0.7}`; report monotonic improvement as confidence rises (predicted).
3. **Per-source attribution** — split intersection rows by which scholar's strong-keyword status drives each tag; check whether the effect is symmetric across Biqāʿī and Rāzī halves.
4. **Surah-stratum drop-out** — drop the largest-N surah (al-Baqara) and re-run primary; effect should remain in the same sign and rough magnitude.
5. **Length-decile uniformity** — verify that peak verses are not concentrated in any one length decile that drives the result.

## 9. Compute and reproducibility

- **Script (to be authored):** `scripts/h_new_40_hadhf_peak.py`
- **Input deps:**
  - `findings/classical-sources/h-new-40-classical-peak-verses-intersection.tsv` (138 rows, ready)
  - `data/h_new_40/qac_hadhf_detector.tsv` (pending #123)
  - `quran-text/quran-no-tashkeel.json` (rules-tuple compliant)
- **Output JSON:** `findings/phase-b-hypotheses/csv/h-new-40.json`
- **Findings narrative:** `findings/phase-b-hypotheses/h-new-40-hadhf-peak-clustering.md`
- **Conditional reverse-finding:** `findings/phase-b-hypotheses/h-new-40-reverse-suppression.md` (only if reverse signal fires)
- **Seed:** 20260414
- **Compute estimate:** < 30 seconds (no permutation null required; Fisher exact is closed-form). OLS residualization is also closed-form.

## 10. Garden-of-forking-paths discipline

- Confidence threshold 0.5 is locked; sweep is reported as robustness only.
- Length-decile stratification follows the H-NEW-META-3 protocol exactly (9 break-points pooled-Quran-derived).
- The contrast set is constructed live and deterministically from seed 20260414 so re-runs are bit-identical.
- One-tailed direction is locked by Section 2; sign-flip post-hoc is prohibited.
- Bonferroni k = 5 includes the STRICT sub-test by team-lead specification (38.4% gain in stringency vs k=4 baseline).
- All 5 tests are reported regardless of outcome.

## 11. Audit-031 forward watches (analogues from META-3)

These watches apply to H-NEW-40 execution at result-stage:

1. Fisher exact p-values must be one-sided ("greater" alternative) and report the exact 2×2 table for reproducibility.
2. OLS residualization must use the union of (peak ∪ matched non-peak) verse pool, not the full corpus.
3. Length-decile breakpoints must match H-NEW-META-3's pooled-Quran derivation (9 values).
4. JSON output must include rules_tuple + seed + confidence_threshold in metadata block.
5. STRICT sub-test must use ONLY the 28-row strong-strong intersection, not the 138-row primary subset filtered post-hoc.
6. No "per pre-registered fallback clause" language at the result stage unless an explicit fallback clause exists in this pre-reg file (it does NOT).

## 12. Expected execution timeline

| Step | Owner | Status | ETA |
|---|---|---|---|
| Classical convergence gate | classical-scholar | DONE 2026-04-13 | — |
| QAC ḥadhf-subtype detector TSV | arabic-specialist (#123) | in_progress | TBD |
| H-NEW-40 pre-reg (this file) | computational-tester | DONE 2026-04-13 | — |
| `scripts/h_new_40_hadhf_peak.py` authoring | computational-tester | pending | unblocked by TSV |
| Execution + JSON + findings | computational-tester | pending | < 1 hour after script |
| skeptical-auditor review | skeptical-auditor | pending | post-execution |

## 13. Reporting commitment

Both directions publishable:
- PASS / STRONG PASS → al-Jurjānī ḥadhf-at-peaks thesis confirmed; integrate to MASTER §1.
- NULL → al-Jurjānī thesis not confirmed at this granularity; the test had power for the predicted effect but the predicted effect did not appear.
- REVERSE-SIGNAL → file as separate exploratory finding; recommend follow-up to discriminate (a) detector artifact from (b) genuine ḥadhf suppression at peaks.
- PARTIAL (2-3/5) → file with explicit subtype attribution and exploratory recommendation for which subtype-mechanism is doing the work.
