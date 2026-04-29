---
id: audit-038
phase: B
status: AUDIT
date: 2026-04-17
auditor: adversarial-wave-4-review
target: Wave-4 findings (late 2026-04-17)
target_findings:
  - H-NEW-165 (phonological predictor, PASS-PRIMARY)
  - H-NEW-189 / 189.1 (Medinan inclusio, STRONG-PASS)
  - H-NEW-192 (mushaf position decomposition)
  - H-NEW-222 (more chronologies)
  - H-NEW-225 (adversarial search)
  - H-NEW-227 (wrap-edge chronologies)
  - H-NEW-230 (block-decomposition; inline-only)
  - H-NEW-231 (KL-divergence per surah)
  - cross-finding-020 (Complete Equation)
  - cross-finding-021 (Mushaf information-theoretic optimality)
related_audits:
  - audit-034 (Wave-4 early integrity snapshot)
  - audit-037 (H-NEW-139 retraction precedent)
precedent_standard: "audit-037 caused H-NEW-139 retraction via adversarial null; apply same discipline"
---

# Audit-038 — Wave-4 Methodological Review

## 0. Executive Summary

Wave-4 (2026-04-17) landed 11+ findings in parallel plus two terminal-synthesis cross-findings (CF-020, CF-021). Of the ten targets audited:

- **5 CLEAR** ([[h-new-165-phonological-predictor|H-NEW-165]] with caveat; [[h-new-222-more-chronologies|H-NEW-222]]; [[h-new-225-adversarial-search|H-NEW-225]]; [[h-new-227-wrap-edge-chronologies|H-NEW-227]]; [[h-new-231-kl-divergence-per-surah|H-NEW-231]])
- **4 FLAG-WITH-RECOMMENDATION** ([[h-new-189-medinan-inclusio|H-NEW-189]] missing pre-reg file; [[h-new-192-mushaf-position-decomposition|H-NEW-192]] LOOCV-R² optimism; [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] inline-only; CF-020 "93% derivable" arithmetic)
- **1 FLAG** (CF-021 "DEFINITIVE SYNTHESIS" framing over single-feature chronology axis; descriptive-layer CLOSED overclaim)

**No finding rises to a retraction candidate comparable to [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]].** All verdicts are in the correct direction; the flags concern bounding, framing, and missing-artifact discipline rather than false-direction results.

**Top-3 cross-cutting concerns**:
1. Several Wave-4 findings ([[h-new-189-medinan-inclusio|H-NEW-189]], [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]], [[h-new-231-kl-divergence-per-surah|H-NEW-231]]) were filed as INLINE / team-lead autonomous without standalone pre-reg files — conflicts with PRE-REG-STANDARD-04 even under post-hoc-noticed discipline.
2. Bonferroni k=1 is the default Wave-4 pattern even for multi-cell findings ([[h-new-189-medinan-inclusio|H-NEW-189]] primary muq-cell + secondary Medinan cell = 2 cells; [[h-new-192-mushaf-position-decomposition|H-NEW-192]] two-model family Ridge+RF; CF-020 13-residual inventory). Using k=1 loosens α; the audit-037 precedent requires honest k-counts.
3. "Classical validation" framing in CF-020 and CF-021 conflates SECONDARY-TRIANGULATED (modern-secondary-cited) with QUANTITATIVELY-VINDICATED. The project's MW-6 classical-citation discipline requires scholar + work + passage; several anchors pass that bar but others (al-Ghazālī *Iḥyāʾ* Book 8, al-Suyūṭī *Itqān* III §36 muq-letter arithmetic) are cited without verse-specific anchoring.

---

## 1. Per-finding verdicts

### 1.1 [[h-new-165-phonological-predictor|H-NEW-165]] — Phonological predictor (CLEAR-WITH-CAVEAT)

**Status**: CLEAR (Bonferroni OK, MW-5 present, pre-reg locked).

**Pre-commitment check**:
- Direction pre-committed (top-1 > 0.50). ✓
- Feature codebook pre-committed with 15 locked dimensions. ✓
- Classical sources cited: al-Khalīl *Kitāb al-ʿAyn*, Ibn Jinnī *Sirr Ṣināʿat al-Iʿrāb* I.46ff, al-Suyūṭī *Itqān* III §36, Watson 2002, Holes 2004. Scholar + work + passage-level citation: GOOD.
- Bonferroni k=2 (primary + singleton), α_bon = 0.025. Correct.
- MW-5 cheat_surah_id = 0.517. ✓ pipeline sanity.
- Garden-of-forking-paths log PRESENT (§10 of pre-reg, 10 items). ✓

**Concerns examined and dismissed**:
- **Structural ceiling framing**: the headline "hits the multi-member LOOCV ceiling exactly" is technically correct — LOOCV cannot reach singletons because they have exactly 1 sample. The ceiling is 19/29 = 0.6552. Observed = 0.6552. This is NOT post-hoc ceiling-fitting; it is a deterministic LOOCV upper bound that any perfect cluster-classifier must hit. The finding honestly discloses this.
- **letter_count circularity**: explicitly acknowledged in "Honest limits" §1; non-circular by the [[h-new-88-letter-set-predictor|H-NEW-88]] baseline comparison (0.414 vs 0.655 shows the other 14 features carry ~0.24 lift).
- **Phonological-coding sensitivity**: the pre-reg acknowledges Holes 2004 alternative coding for ح/ع pharyngeal vs glottal; sensitivity analysis is deferred to [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]]. This is acceptable forward-scoping.

**Recommendation**: the claim is correctly bounded (PASS-PRIMARY, not CONFIRMED). The [[cross-finding-020-the-complete-equation|cross-finding-020]] + ledger framing as "OQ-1 first positive signal" is defensible. Queue [[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] (phonological-codebook sensitivity) and H-NEW-165.4 (singleton prediction via extra-surah features) before any upgrade to CONFIRMED.

### 1.2 [[h-new-189-medinan-inclusio|H-NEW-189]] — Medinan inclusio (FLAG-WITH-RECOMMENDATION)

**Status**: FLAG — missing pre-reg file; post-hoc cell-split upgrade to STRONG-PASS.

**Pre-commitment check**:
- **No standalone pre-reg file exists** (`[[h-new-189-medinan-inclusio|h-new-189]]-*-prereg.md` absent). Frontmatter header of findings file states `bonferroni_k: 2, alpha_bon: 0.025, direction: pre-registered one-sided`, but without a separate pre-reg-locked artifact with SHA-256, the audit cannot verify that the Medinan-cell direction was pre-committed before data contact.
- The primary cell (muq vs non-muq) is NULL (p=0.90, heavily wrong-direction). The secondary Medinan cell is where the STRONG-PASS resides. This is the **classic garden-of-forking-paths hazard**: a pre-planned primary NULLs; a secondary cell PASSes extreme. The finding's frontmatter reports Bonferroni k=2 so both cells SHOULD have been jointly pre-registered.
- Partial correlation ρ = +0.483 with length-controlled p<0.0001 is legitimate and defensive.
- Classical anchor: al-Biqāʿī *Naẓm al-Durar*. The citation is scholar + work but NOT specific volume/passage. **MW-6 violation** at strict-verification level.

**What saves this finding**:
- p<10⁻⁴ on both Fisher one-sided and Mann-Whitney (under length residualization via partial ρ). Bonferroni k=2 or even k=10 leaves p<0.001.
- The Medinan/Meccan split is itself a classical primary distinction (not a data-dredged subgroup).
- 54.2% vs 11.1% effect size is very large.

**Recommendation**:
1. Back-fill a pre-reg-timestamped (or git-tagged) artifact stating that the Medinan-cell direction was committed before the team-lead inline run.
2. Cite al-Biqāʿī with specific *Naẓm al-Durar* volume (~v.1 p.6ff discusses first-last munāsabāt generally; specific surah-level discussions scatter across 22 volumes).
3. Honest k-count: if primary muq + secondary Medinan + continuous-MW + partial-ρ = 4 cells, α_bon=0.05/4=0.0125. Finding still PASSes but narrative should say "PASS-k=4" not "STRONG-PASS joint."

### 1.3 [[h-new-192-mushaf-position-decomposition|H-NEW-192]] — Mushaf position decomposition (FLAG-WITH-RECOMMENDATION)

**Status**: FLAG-WITH-RECOMMENDATION — LOOCV optimism + model-family size bias.

**Pre-commitment check**:
- Direction pre-committed R² > 0.5. ✓ (generously above actual 0.759-0.817.)
- 15 compositional features pre-selected from prior findings. ✓ but feature origin history is worth auditing ([[h-new-183-chronology-predictor|H-NEW-183]] used 12; [[h-new-192-mushaf-position-decomposition|H-NEW-192]] uses 15).
- Bonferroni k=1 reported, α_bon=0.05. This is **under-counted** — the finding reports BOTH Ridge (R²=0.759) and RF (R²=0.817). These are two distinct model families; the reported-best of two should use k≥2.

**Concerns**:
- **LOOCV optimism on 114 samples**: with 15 features and LOOCV, the effective training sample is 113. RF n_estimators=200 with default max_depth=None can overfit. RF R²=0.817 vs Ridge R²=0.759 — the 0.06 gap suggests the RF is modeling nonlinear-interaction noise. Honest limits §4 acknowledges this but the headline reports R²=0.817 as the primary framing.
- **Feature-selection bias**: the 15 features were chosen post-hoc from ~20+ candidate features in prior findings (verse_count, mean_verse_length, eschatological_density, TTR, divine_name_density, loanword_density, qul_density, legal_density, muq_cardinality, refrain_score, + 5 more). No pre-reg locks this 15-feature choice. This is a **garden-of-forking-paths concern**.
- **Circularity with Nöldeke comparison**: Nöldeke itself was predicted at R²=0.836 using a 12-feature subset ([[h-new-183-chronology-predictor|H-NEW-183]]). The "mushaf is 8% less predictable" claim compares LOOCV R² across different feature-counts and different model specs — should be controlled.

**Does it rise to retract**?: NO. R²=0.759 Ridge is above any pre-committed threshold; the directional finding (mushaf is predictable from compositional features) is solid. The FLAG concerns framing — particularly the "80/20 compositional/structural decomposition" which is REPORTED AS EXACT (~76% M2+M5, ~20% M1, ~4% P3) but is in reality a Ridge-R² rounding narrative.

**Recommendation**:
1. Rerun with Ridge-only (the more conservative primary) as the headline; report RF as SECONDARY.
2. Feature-set-sensitivity sweep: 10, 12, 15, 20 features; verify R² curve.
3. Direct feature-matched comparison with [[h-new-183-chronology-predictor|H-NEW-183]] (same 12 features on mushaf target). If mushaf R² drops to 0.75 vs Nöldeke 0.836 at matched features, the "8% gap" is cleanly isolated.

### 1.4 [[h-new-222-more-chronologies|H-NEW-222]] — More chronologies (CLEAR)

**Status**: CLEAR — methodologically clean.

- Bonferroni k=4, α_bon=0.0125 on 4-chronology family. Correct.
- D-matrix inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] with SHA-256 lock. ✓
- MW-1/MW-5 inherited from parent. ✓
- Two "historiographic surprises" (Watt-Bell ≡ Nöldeke; Suyūṭī Itqān ≡ Tanzil) are honestly disclosed as descriptive-side-results, not pre-registered claims.
- The "Ibn ʿAbbās list typo" (duplicate surah 4 → 41 correction) is transparently disclosed with sensitivity analysis.
- Verdict correctly framed as "PASS (family-level) / MUSHAF-STILL-WINS" with ceiling PASS (not CONFIRMED).

**No issues.**

### 1.5 [[h-new-225-adversarial-search|H-NEW-225]] — Adversarial search (CLEAR)

**Status**: CLEAR.

- Direction pre-committed: gap_rel > 1.01 → PASS. Observed 1.1079. ✓
- Bonferroni k=1 (existence test, not permutation). Correctly described as tightening amendment (self-verifying per feedback_bonferroni_tightening_vs_loosening).
- Honest limits §1 explicitly acknowledges heuristic-not-exact and that Concorde/LKH-3 might strictly improve.
- Does NOT demote parent M1 claims; correctly argues "near-optimal at 10.8% gap" is within [[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s pre-registered <1.2 threshold.

**No issues.**

### 1.6 [[h-new-227-wrap-edge-chronologies|H-NEW-227]] — Wrap-edge chronologies (CLEAR)

**Status**: CLEAR.

- Method simple and auditable: compute D[last, first] for 5 orderings vs 10K random-endpoint null.
- Bonferroni k=1, α=0.05. p_mushaf=0.0277 PASSes at α=0.05.
- Does not overclaim: only the mushaf PASSes the permutation null; Egyptian/Blachère p=0.0461 (borderline) and Nöldeke/Bell p=0.95 (wrong direction).
- The Δ/SD head-to-head table is descriptive; no pre-reg claim about head-to-head.

**Minor note**: Egyptian and Blachère both at p=0.0461 are uncomfortably close to α=0.05 without Bonferroni k=5 across the 5-ordering family. Under k=5 (α_bon=0.01), ONLY mushaf PASSes at 0.0277 (still PASS) — actually tightens the claim. Recommend this re-framing but it is OPTIONAL since the finding's verdict is correct either way.

### 1.7 [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] — Block decomposition (FLAG — inline-only)

**Status**: FLAG — no standalone finding file; no pre-reg artifact.

- Content is summarized only inline in MASTER-FINDINGS-LEDGER line 1132 ("Nöldeke wins front half (−16.54), mushaf wins back half (+18.01); Q 91-114 short-mufaṣṣal tail drives mushaf's advantage").
- [[cross-finding-021-mushaf-information-theoretic-optimality|Cross-finding-021]] does NOT cite or integrate [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] by ID.
- Under PRE-REG-STANDARD-04 this would normally trigger NEEDS-AMENDMENT, but this is a POST-EXECUTION descriptive block-decomposition, not an inferential test.

**Recommendation**:
1. Create standalone `[[h-new-230-mushaf-nöldeke-block-decomposition|h-new-230]]-block-decomposition.md` with: method, block-boundary (front/back split rule), numerical outputs, honest-limits, post-hoc-noticed disclosure.
2. Cross-link from CF-021 §4 (Principle D decomposition) and MASTER-FINDINGS-LEDGER.

### 1.8 [[h-new-231-kl-divergence-per-surah|H-NEW-231]] — KL-divergence per surah (CLEAR with Laplace-sensitivity caveat)

**Status**: CLEAR — ρ=−0.967 is essentially unassailable, but Laplace-smoothing sensitivity is UNTESTED.

- Correctly filed as POST-HOC-DESCRIPTIVE (no pre-reg direction; single-test α=0.05 cap per MW-7).
- Honest limits §2 explicitly acknowledges "math-of-estimation circularity" — long surahs drawn from corpus distribution have KL→0 as N→∞.
- Honest limits §3 flags Laplace α=0.5 sensitivity as UNTESTED — H-NEW-231.1 is queued but not yet run.

**Adversarial probe (unexecuted but specifiable)**: under MLE (no smoothing, only observed vocabulary per surah), short surahs would have UNDEFINED KL because p_corpus(w)>0 for vocabulary the surah doesn't contain. The choice of smoothing matters — Laplace (α=1) gives heavier mass to unseen words; MLE is undefined; Dirichlet α=0.5 is a compromise. This is a pre-registered choice in the finding's `rules_tuple` but not adversarially tested.

**Does ρ=−0.967 survive alternate smoothing**? Almost certainly yes — the EFFECT is length-driven, which any smoothing choice preserves. But the EXACT coefficient (−0.967 vs −0.92 under Laplace α=1) is unspecified. Not a retraction risk; a precision-bounding concern.

**Recommendation**: run H-NEW-231.1 (null test per finding's queue) and H-NEW-231.2 (α-sweep on {MLE, α=0.5, α=1.0}) to bound the coefficient.

### 1.9 [[cross-finding-020-the-complete-equation|cross-finding-020]] — Complete Equation (FLAG-WITH-RECOMMENDATION)

**Status**: FLAG — "~93% derivable" arithmetic is not cleanly auditable; classical-anchor conflation.

**Concerns**:
1. **The 93% figure is pedagogical-compression**: §2.2 reports ~76%+20%+6%+4%+7% = ~113% (non-orthogonal by admission). §6 reports "~94% of ~80 confirmed findings derivable". These are different quantities; the "93%" headline is a subjective blend. **The honesty section §10 explicitly acknowledges this** ("a subjective estimate") — which earns the FLAG-WITH-RECOMMENDATION (honest disclosure) rather than FLAG proper.
2. **"15+ validated, 8+ refuted, 1 retracted"**: the scorecard §7 table has 16 rows validated and 9 rows refuted. Some "validated" rows are SECONDARY-TRIANGULATED (al-Biqāʿī Naẓm al-Durar, al-Ghazālī 3-family typology) which is not the same bar as "empirically tested and PASS." The framing should distinguish SURVIVED (empirical PASS) vs SECONDARY-TRIANGULATED (modern secondaries cite).
3. **No new inferential test** (honestly stated) — this is a terminal synthesis. No Bonferroni concern for the synthesis itself.

**Does it rise to retract**?: NO. The document is honestly self-disclosing throughout; §10 acknowledges the subjective-estimate nature. The FLAG is a framing recommendation, not a finding challenge.

**Recommendation**:
1. Replace "~93% decoded" with "~76%-mushaf-position-variance Ridge-LOOCV + qualitative-mapping of ~16/~25 classical claims to principles."
2. Distinguish SURVIVED (empirical PASS) from SECONDARY-TRIANGULATED in the §7 table via a STATUS column.
3. Cite al-Biqāʿī and al-Ghazālī with volume/passage, not just scholar+work.

### 1.10 [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]] — Mushaf information-theoretic optimality (FLAG)

**Status**: FLAG — "DEFINITIVE SYNTHESIS" title + "OQ-15 DESCRIPTIVE LAYER CLOSED" status may be overstated.

**Concerns**:
1. **Chronology-beat is FEATURE-SPECIFIC**: Honest-limits §8 states plainly "L_mushaf < L_noldeke holds on roots; reverses on verse-length; ties on char-4-grams." The headline "ALL FOUR CHRONOLOGIES BEATEN" is true only on roots. The title "information-theoretically optimal" is robust across axes, but "beats all chronologies" is NOT. The §3 table and narrative minimize this.
2. **"DEFINITIVE SYNTHESIS" and "DESCRIPTIVE LAYER CLOSED"** are strong claims. The project's discipline distinguishes PASS from CONFIRMED; "CLOSED" suggests no further audit possible. Under audit-037's standard (where [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] was retracted after "CONFIRMED" framing), this language deserves bounding.
3. **Inflated-independence**: §8 acknowledges "effective independent axes ≈ 5-6, not 10-15." The §2 "10+ Convergent Axes of Evidence" table IS inflated. At 5 independent axes with Fisher's combined p, the conclusion still survives by large margins — so the FLAG is framing, not finding-invalidating.
4. **Classical-citation bar**: §7 list "Validated (≥16)" mixes SECONDARY-TRIANGULATED with empirically-tested. "Fāṣila rhyme prefigured by muqaṭṭāʿat (al-Suyūṭī balāgha) — [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]" is listed as VALIDATED, but [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] was RETRACTED per audit-037. **This is a direct error in the scorecard that should be corrected.**
5. **[[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] cited but not yet a standalone file** (see §1.7 above).

**Does it rise to retract**?: NO. The document's Principle A-D mechanism model and the 15-hinge triple-feature replication are empirically solid. The FLAG is bounded to framing, scorecard error ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] incorrectly listed), and the "CLOSED" overclaim.

**Recommendation**:
1. Fix §7 scorecard: [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] must be moved to Refuted/Retracted (it is both). It appears in the "Validated" column as item #4 — DIRECT SCORECARD ERROR.
2. Replace "DESCRIPTIVE LAYER CLOSED" with "DESCRIPTIVE LAYER SUBSTANTIALLY ANSWERED" (matching CF-020's careful language).
3. Retitle §3 "ALL Four Chronologies Beaten" to "Four Chronologies Beaten on Fisher-Rao Roots (Feature-Specific)" and cite §8 upfront.
4. Collapse §2 "10+ axes" to "≈5 independent axes × 2 benchmark types" per §8 honest limits.

---

## 2. Summary scorecard

| Finding | Direction pre-committed? | MW-5 present? | Bonferroni correct? | Garden-of-forking-paths disclosed? | Classical citations specific? | Honest limits? | Verdict |
|---|:-:|:-:|:-:|:-:|:-:|:-:|:-:|
| [[h-new-165-phonological-predictor|H-NEW-165]] | ✓ | ✓ | ✓ (k=2) | ✓ | ✓ | ✓ | **CLEAR** |
| [[h-new-189-medinan-inclusio|H-NEW-189]] | Frontmatter only | n/a (no MW-5 cell) | k=2 declared, arguably k≥4 | ✗ (no pre-reg file) | Partial | ✓ | **FLAG-REC** |
| [[h-new-192-mushaf-position-decomposition|H-NEW-192]] | ✓ (R²>0.5) | n/a | k=1 under-counts (2 models) | Partial | n/a | ✓ | **FLAG-REC** |
| [[h-new-222-more-chronologies|H-NEW-222]] | ✓ | Inherited | ✓ (k=4) | ✓ | ✓ (Suyūṭī + Ibn ʿAbbās chains) | ✓ | **CLEAR** |
| [[h-new-225-adversarial-search|H-NEW-225]] | ✓ | Inherited | ✓ (k=1 existence) | ✓ | ✓ | ✓ | **CLEAR** |
| [[h-new-227-wrap-edge-chronologies|H-NEW-227]] | ✓ | Inherited | ✓ (k=1; suggest k=5 for family) | ✓ | ✓ | ✓ | **CLEAR** |
| [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]] | N/A | N/A | N/A | N/A (inline-only) | N/A | N/A | **FLAG** (no file) |
| [[h-new-231-kl-divergence-per-surah|H-NEW-231]] | Descriptive (no dir.) | n/a | ✓ (single-test cap) | ✓ | ✓ | ✓ (Laplace deferred) | **CLEAR** |
| [[cross-finding-020-the-complete-equation|cross-finding-020]] | N/A (synthesis) | N/A | N/A | Partial (§10 honesty) | Partial (some anchors vague) | ✓ | **FLAG-REC** |
| [[cross-finding-021-mushaf-information-theoretic-optimality|cross-finding-021]] | N/A (synthesis) | N/A | N/A | Partial | Partial + ERROR ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] mis-listed) | Partial (some "CLOSED" language) | **FLAG** |

---

## 3. Cross-cutting observations

### 3.1 Wave-4 defaults to Bonferroni k=1 even for multi-cell findings

- [[h-new-192-mushaf-position-decomposition|H-NEW-192]]: two models (Ridge + RF) = k≥2 family.
- [[h-new-189-medinan-inclusio|H-NEW-189]]: primary muq-cell NULL + secondary Medinan-cell PASS + continuous MW + partial ρ = k≥4.
- [[h-new-227-wrap-edge-chronologies|H-NEW-227]]: 5 orderings + 1 null test = k≥5 or k=1 as pre-registered.
- Where observed effects are large (p<10⁻⁴), tightening k has no bearing on verdict. Where effects are borderline ([[h-new-227-wrap-edge-chronologies|H-NEW-227]] Egyptian p=0.0461, [[h-new-189-medinan-inclusio|H-NEW-189]] frontmatter k=2 on 4-cell test), honest k would actually clarify PASS-status.
- **Recommendation**: Wave-4 and prospective Wave-5 pre-regs should state k = (cells × models × readouts) explicitly, with the conservative-inflation principle (k-tightening is self-verifying per feedback_bonferroni_tightening_vs_loosening).

### 3.2 Inline / team-lead autonomous findings lack standalone pre-reg artifacts

[[h-new-189-medinan-inclusio|H-NEW-189]], [[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]], [[h-new-231-kl-divergence-per-surah|H-NEW-231]] are all "executed_by: team-lead (inline, autonomous-loop iteration)". None has a standalone pre-reg file with SHA-256 lock. This is faster for velocity but violates the reproducibility bar that project prior waves maintained.

**Recommendation**: promote these three to retroactive pre-reg artifacts (back-dated, hashed, with git commit showing the timestamp was pre-data).

### 3.3 Classical-anchor citation precision is variable

- **STRONG**: [[h-new-165-phonological-predictor|H-NEW-165]] cites al-Khalīl *Kitāb al-ʿAyn* (passage-specific via 8-tier makhraj), Ibn Jinnī *Sirr Ṣināʿat al-Iʿrāb* I.46ff (volume + page), al-Suyūṭī *Itqān* III §36 (volume + section). Also [[h-new-222-more-chronologies|H-NEW-222]] correctly traces Suyūṭī's Jābir-b-Zayd chain.
- **WEAK**: [[h-new-189-medinan-inclusio|H-NEW-189]] cites al-Biqāʿī *Naẓm al-Durar* without volume. CF-020 lists al-Ghazālī *Iḥyāʾ* Book 8 (book-level, acceptable) but al-Rāzī *Mafātīḥ al-ghayb* "paired divine names" without surah-level passage.
- **ERROR**: CF-021 §7 validated-list item #4 ("Fāṣila rhyme prefigured by muqaṭṭāʿat (al-Suyūṭī balāgha) — [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]], z = +5.96") incorrectly lists [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] as validated. [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] was RETRACTED per audit-037.

**Recommendation**: Wave-5 findings should pre-verify specific passages (scholar + work + volume/page/section) BEFORE writing the finding, and CF-021's scorecard requires an immediate fix.

### 3.4 "93% derivable" and "DESCRIPTIVE LAYER CLOSED" both carry pedagogical-compression weight

Both CF-020 (93%) and CF-021 (CLOSED) are framing moves that package findings for accessibility. The audit does not object to the framings per se — CF-020 §10 honestly acknowledges the subjective-estimate nature — but the READER-level impression conveyed by "93% DECODED" and "DEFINITIVE SYNTHESIS" exceeds what the underlying R²=0.76 and 5-effective-independent-axes can strictly support.

**Recommendation**: a short "Limits of this synthesis" paragraph in the opening abstract of each cross-finding (not buried in §8 or §10) would bring framing into alignment with the discipline.

---

## 4. Recommended follow-up pre-regs (priority order)

1. **[[h-new-189-medinan-inclusio|H-NEW-189]]-replication-prereg.md**: re-run Medinan-vs-Meccan inclusio with (a) alternative stemmer QAC-lemma, (b) alternative first/last boundaries (v1-3 vs v1 only, last vs last-3), (c) honest k=4 Bonferroni, (d) specific al-Biqāʿī *Naẓm al-Durar* Medinan-surah volume citations.
2. **[[h-new-165-2-codebook-sensitivity|H-NEW-165.2]] pre-reg**: phonological-codebook sensitivity sweep (Watson 2002 vs Holes 2004 vs classical Ibn Jinnī-only vs al-Khalīl-only); lock in feature codebook BEFORE seeing accuracy.
3. **H-NEW-231.1 pre-reg**: null test for the length-KL math-of-estimation artifact (sample N tokens from corpus-p, compute KL; compare to observed).
4. **H-NEW-192.1 pre-reg**: feature-matched rerun of Ridge on mushaf vs Nöldeke with SAME 12 features ([[h-new-183-chronology-predictor|H-NEW-183]]'s set) to cleanly isolate the 8% gap.
5. **[[h-new-230-mushaf-nöldeke-block-decomposition|H-NEW-230]]-standalone.md**: retroactive standalone file for block-decomposition finding.
6. **CF-021 correction amendment**: fix §7 scorecard ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] mis-listing); soften "CLOSED" → "SUBSTANTIALLY ANSWERED"; add §3 honest-caveat upfront.

---

## 5. Verdict

Wave-4's methodological discipline is **broadly defensible** — no finding meets the audit-037 retraction standard. The integrity defects are:

- 3 inline-only findings lacking standalone pre-regs ([[h-new-189-medinan-inclusio|H-NEW-189]], 230, 231).
- Pervasive k=1 Bonferroni default where honest k would be 2-5 (verdicts generally survive tighter k).
- CF-021 §7 scorecard factual error ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] mis-listed as validated).
- Classical-anchor citation precision inconsistent (strong in [[h-new-165-phonological-predictor|H-NEW-165]] and [[h-new-222-more-chronologies|H-NEW-222]]; weak in [[h-new-189-medinan-inclusio|H-NEW-189]] and CF-020/021).
- Framing moves in CF-020 ("93% derivable") and CF-021 ("DEFINITIVE"; "CLOSED") carry more rhetorical weight than the underlying numbers strictly support.

**None of these rises to retraction.** All are correctable by amendment / sensitivity follow-up / scorecard repair.

---

## 6. Files

- This audit: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/audit-038-wave-4-review.md`
- Precedent: audit-037 ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] retraction) and audit-034 (Wave-4 early integrity)
- Corrections to propagate: CF-021 §7 scorecard; CF-020 framing; [[h-new-192-mushaf-position-decomposition|H-NEW-192]] k-count; [[h-new-189-medinan-inclusio|H-NEW-189]] pre-reg back-fill
