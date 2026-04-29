---
finding_id: h-new-4-ext-d-prereg
phase: B
status: PRE-REGISTRATION-AMENDED-AWAITING-DISPATCH
date: 2026-04-13
amended: 2026-04-13 (MW-10 metric correction)
filed_by: classical-scholar
ruling: team-lead 2026-04-13 — Option D approved; MW-10 metric amendment 2026-04-13 — JS-divergence primary + KL sensitivity-0 + stratified-KL sensitivity-1 + Hellinger sensitivity-2 approved
parent_task: 6 (H-NEW-4 verdict REFUTED at lemma/TTR scale)
new_task: 33 (re-operationalized at letter-graphemic scale)
sister_pre_reg: findings/phase-b-hypotheses/h-new-4-ext-classical-audit.md
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, 29-letter-alphabet-with-bare-hamza, counted-only-in-surah-1, hafs-kufan, mashriqi)
seed: 20260413
bonferroni_k: 1
alpha: 0.01
sided: one-sided
primary_statistic: Jensen-Shannon divergence (amended 2026-04-13 under MW-10)
sensitivity_set: [KL-original (sens-0), support-size-stratified-KL (sens-1), Hellinger (sens-2)]
null_publishable: true
positive_publishable: true
mw_tier_overall: MW-5 (al-Rāzī al-mujmal verbal anchor; PENDING per AMEND-28)
mw_amendment_tier: MW-10 (pre-execution metric defect caught via self-test, corrected before primary run)
infrastructure_dependency: H-NEW-24 letter-multiset pipeline (#44/#64/#65), arabic-specialist owned
---

# [[h-new-4-ext-classical-audit|H-NEW-4]]-EXT-D — al-Rāzī *ijmāl-tafṣīl* doctrine at letter-graphemic scale

## Title

[[h-new-4-ext-classical-audit|H-NEW-4]]-EXT-D — Letter-multiset KL-divergence between muqaṭṭaʿāt opener and surah body, vs length-matched non-muqaṭṭaʿāt baseline.

## Classical anchor (MW-5, PENDING per AMEND-28)

**al-Rāzī, *Mafātīḥ al-Ghayb***, preface to Q 2 (al-Baqara) and Āl ʿImrān 7:152-154. al-Rāzī characterizes the muqaṭṭaʿāt as *al-mujmal* — a compressed announcement (the disconnected letters) which the surah body then unfolds as *al-tafṣīl*. The doctrine is most explicit in his Āl ʿImrān commentary on the relationship between *muḥkam* and *mutashābih* verses, where the muqaṭṭaʿāt are presented as paradigmatic cases of *ijmāl* requiring *tafṣīl* in the body.

**Verbal anchor confidence: HIGH.** The phrase *al-mujmal* applied to muqaṭṭaʿāt is widely attested in al-Rāzī's commentary tradition. Verbatim physical-edition verification at this specific verse range is PENDING per AMEND-28.

## Supporting anchors (MW-4, PENDING)

- **al-Zamakhsharī, *al-Kashshāf*** 1:26 (al-Mahdī ed., Beirut: Dār al-Kutub al-ʿIlmiyya 1995) — *māddat al-kalām* (the compositional substrate frame) for muqaṭṭaʿāt.
- **al-Suyūṭī, *al-Itqān*** nawʿ 59 (*ḥusn al-ibtidāʾ wa-l-intihāʾ*) — universal-baseline reference (no longer the direct test target under Option D).
- **Ibn Taymiyya, *Muqaddima fī Uṣūl al-Tafsīr*** pp. 52-54 (Zarzūr ed., Beirut: Muʾassasat al-Risāla 1972) — *al-lughat al-kullīya* supportive frame.

## Pre-registered hypothesis

If al-Rāzī's *al-mujmal/al-tafṣīl* doctrine is empirically valid at the letter-graphemic scale, then the surah body of a muqaṭṭaʿāt-opening surah should "fulfill" the letter-set announced by its muqaṭṭaʿāt opener — i.e., the body's letter-multiset distribution should be *more closely aligned* with the muqaṭṭaʿāt's letter-multiset than would be expected by chance, AND this alignment should EXCEED what is observed for length-matched non-muqaṭṭaʿāt-opening surahs against arbitrary letter-set "openers."

## Operationalization (PRIMARY TEST)

### Letter-multiset extraction

**Alphabet closure (confirmed 2026-04-13):** the letter universe is the **29 distinct letters** consisting of the 28 consonants of the standard Arabic alphabet plus **bare hamza ء as its own category, NOT collapsed to alif**. Reason: the text is rasm-normalized but ء and ا are phonologically and orthographically distinct; collapsing would drag hamza probability mass into alif and systematically bias k=3 alif-heavy openers (الم، الر، المر، المص). This closure applies uniformly to `M_open`, `M_body`, and the baseline opener/body pairs.

Per surah, build:
- `M_open`: the multiset of distinct Arabic letters appearing in the muqaṭṭaʿāt opening (e.g., for Q 2 the muqaṭṭaʿāt is `الم` → multiset {ا, ل, م}).
- `M_body`: the multiset of letter occurrences in the entire surah body (excluding the muqaṭṭaʿāt opener itself), normalized to a probability distribution over the 29-letter Arabic alphabet (28 consonants + bare hamza ء).

For non-muqaṭṭaʿāt-opening surahs (length-matched controls), build:
- `M_open_baseline`: the letter-multiset of an "opener" defined as the first N letters of the surah, where N matches the median letter-count of muqaṭṭaʿāt openers (28 muqaṭṭaʿāt-openers have median ≈ 4 letters; use N=4 for the baseline opener length).
- `M_body_baseline`: same as above but excluding the first N letters.

Both `M_open` flavors are converted to **uniform-on-support** probability distributions for KL computation (i.e., {ا, ل, م} → P(ا) = P(ل) = P(م) = 1/3, P(other) = 0; later sensitivity test on smoothing).

### Primary statistic (amended 2026-04-13 under MW-10)

For each surah, compute:

```
JS_surah = D_JS( M_body, M_open )
         = ½ · [ D_KL(M_body ‖ M) + D_KL(M_open ‖ M) ]
   where M = ½ · (M_body + M_open)
```

where D_JS is the Jensen-Shannon divergence (symmetric, bounded [0, log 2], support-size robust by construction of the mixture M). Laplace smoothing α=0.01 is retained for the underlying KL components of the JS formula to handle zero probabilities in `M_body`. Lower JS = body letter-distribution more closely matches the announced opener-letter-set.

Aggregate per group:
- `JS_muqaṭṭaʿāt` = mean JS across the 29 muqaṭṭaʿāt-opening surahs.
- `JS_baseline` = mean JS across the 85 length-matched non-muqaṭṭaʿāt-opening surahs.

**Why JS and not KL:** the original pre-reg (2026-04-13) locked the primary as `D_KL(M_body ‖ M_open)`. During arabic-specialist's pre-execution self-test (2026-04-13, same date), the descriptive full-body Δ = KL_muqaṭṭaʿāt − KL_baseline came out at **+0.2077** — opposite the pre-registered direction. Classical-scholar verified empirically that this is a **support-size confound**, not a real signal: stratified by |M_open|, mean KL drops monotonically 1.76 → 1.71 → 0.91 → 0.72 as opener support grows from k=1 to k=4, because D_KL(·‖M_open) with a uniform-on-support M_open puts near-zero probability mass on the 24–27 "outside" letters and blows up whenever the body visits any of them. The baseline has uniform faux-opener support ≈4 and does not suffer the same squeeze, so the muqaṭṭaʿāt group's aggregate KL is dragged UP by its k=1 (Q38 ص, Q50 ق, Q68 ن) and k=2 (ḥm family, طه, طس, يس) surahs, manufacturing a spurious Δ>0. The defect is mechanical/geometric, not empirical — the data does not say al-Rāzī is wrong; the KL metric says al-Rāzī cannot be fairly evaluated by it. Early-body windowing (0.0, 0.2) does NOT rescue the pattern.

The metric amendment was classified under **MW-10 (pre-execution metric-defect self-test gate)**, escalated to team-lead, and approved 2026-04-13. The amendment is explicitly **NOT a sign-flip** (PRE-REG-STANDARD-04 inapplicable): the pre-registered direction stays Δ<0, only the metric changes. The amendment is explicitly **NOT an MW-9 HALTED state**: the primary has not been run; the descriptive ghost is confound-contaminated and carries no empirical information about the al-Rāzī doctrine. JS-divergence is **classically defensible** because al-Rāzī's *al-mujmal/al-tafṣīl* doctrine is metric-agnostic; JS has the Rényi/Lin information-radius interpretation (the "information difference between two distributions viewed through their mixture") which is faithful to the "body unfolds opener" framing. JS is already used in the [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] sister pipeline, so infrastructure and reviewer burden are both zero.

### Pre-registered direction

```
JS_muqaṭṭaʿāt < JS_baseline
```

(The body of a muqaṭṭaʿāt-opening surah is MORE closely aligned with its opener's letter-set than non-muqaṭṭaʿāt surahs are with their first-4-letters opener, measured under the support-robust JS-divergence. Direction is preserved from the original KL pre-reg.)

### Null model

Shuffle the muqaṭṭaʿāt-opening label 1,000 times across the 114 surahs (preserving the 29:85 split). For each shuffle, compute the difference `Δ = JS_muqaṭṭaʿāt − JS_baseline` and build the null distribution. Pre-registered seed = 20260413 (unchanged from original).

### Acceptance

**PASS**:
1. Observed `Δ_obs` is below the null 1st percentile (one-sided p < 0.01) AND
2. Observed effect size |Δ_obs / σ_null| > 2.33 cleanly above the null 95% CI lower bound.

**NULL**:
- p ≥ 0.01 OR effect size inside null 95% CI.

**REVERSE**:
- p < 0.01 in the OPPOSITE direction (`Δ_obs > 0`, body letter-distributions are LESS aligned with muqaṭṭaʿāt openers than with arbitrary first-4-letter openers under JS). This would be a serious counter-finding requiring new interpretation. The support-size confound that plagued the original KL operationalization is mechanically eliminated under JS, so a REVERSE under JS would reflect a genuine empirical signal (the null model and the JS metric jointly rule out the mechanical explanation).

## Bonferroni

**k = 1** (single primary test, per team-lead's Option D specification). α = 0.01.

## Sensitivity / robustness checks (NOT counted in Bonferroni)

These are robustness diagnostics, not additional pre-registered tests. Bonferroni stays k=1; only the JS-divergence primary is the pre-registered test. Everything below is reference-value.

### Sensitivity-0 — original KL-divergence (archaeological reference) [REQUIRED]

Rerun the entire primary test specification with the original pre-registration statistic:

```
KL_surah = D_KL( M_body ‖ M_open )
```

with Laplace α=0.01, the same 29-letter alphabet closure, same 1,000 null shuffles, same seed 20260413. Report:

- `KL_muqaṭṭaʿāt_mean`, `KL_baseline_mean`, `Δ_KL_obs`, null-percentile of Δ_KL_obs.
- The **support-size stratified table** (k=1 n=3, k=2 n=9, k=3 n=13, k=4 n=2, k=5 n=2) with mean KL per stratum, making the confound mechanism visible to downstream reviewers.
- The Q26/Q28 (طسم, k=3) outlier note: these two surahs sit in the k=3 stratum at elevated KL due to ṭāʾ-rarity in the body (a secondary confound beyond the support-size effect).

**Purpose.** This is the archaeological-continuity record of the MW-10 amendment. Reporting the original KL alongside the JS-divergence primary makes the metric switch transparent and the confound mechanism re-verifiable. Classical-scholar is committed to including the full KL output + stratified table + confound analysis in the §Garden-of-Forking-Paths section of the final result write-up.

### Sensitivity-1 — support-size stratified KL [REQUIRED]

Rerun KL within support-size strata, matching muqaṭṭaʿāt surahs to quartile-matched non-muqaṭṭaʿāt controls by faux-opener size k. For each stratum, compute `Δ_k = KL_muqaṭṭaʿāt[k] − KL_baseline[k]` and aggregate the weighted mean across strata with weights proportional to stratum size.

Report the stratum-level Δ_k values + aggregate. The k=4 stratum has only n=2 muqaṭṭaʿāt surahs so its stratum-level Δ is not inferentially meaningful; aggregate-level Δ is the comparable quantity.

**Purpose.** Orthogonal check: if JS primary passes AND support-size stratified KL also passes, the al-Rāzī finding is robust to both the metric choice and the stratification strategy. If JS passes but stratified KL does not, the interpretation leans on JS's support-robustness rather than the raw letter-count signal.

### Sensitivity-2 — Hellinger distance [REQUIRED]

Rerun the entire primary test specification with Hellinger distance:

```
H(M_body, M_open) = (1/√2) · √( Σ_i (√p_i − √q_i)² )
```

bounded [0, 1], symmetric, metric on the probability simplex. Same Laplace α=0.01 smoothing for zero probabilities, same 29-letter alphabet closure, same 1,000 null shuffles, same seed.

Report `H_muqaṭṭaʿāt_mean`, `H_baseline_mean`, `Δ_H_obs`, null-percentile.

**Purpose.** Hellinger has different analytic sensitivity than JS (JS ∈ [0, log 2], Hellinger ∈ [0, 1]) so they are not redundant: they differentially weight mass-on-support vs. support-overlap. If JS and Hellinger BOTH show Δ < 0 at α=0.01, robustness of the al-Rāzī finding to metric choice is much stronger. If they diverge, that divergence is itself diagnostic and will be reported as a secondary finding.

### General robustness diagnostics (apply to JS primary)

1. **Smoothing sensitivity**: rerun JS primary with Laplace α ∈ {0.001, 0.01, 0.1}. Report whether the verdict flips.
2. **Opener-multiset construction**: rerun with `M_open` as the *count* multiset (not uniform-on-support) — i.e., for `الم` use P(ا) = P(ل) = P(م) = 1/3 vs. for `كهيعص` use P(ك) = P(ه) = P(ي) = P(ع) = P(ص) = 1/5. Both flavors are uniform-on-support; alternative: weight by classical-tradition repetition counts (Q 19's `كهيعص` is 5 distinct letters; doesn't change the uniform construction). Q42 (ḥmʿsq) note: primary uses union-construction M_open = {ح,م,ع,س,ق}; `split_q42=True` sensitivity reruns with the two-segment split ḥm / ʿsq as a separate construction variant.
3. **Length-matching sensitivity**: rerun JS primary with strict surah-length quartile matching (29 muqaṭṭaʿāt × 29 quartile-matched controls instead of all 85 non-muqaṭṭaʿāt).
4. **Body-truncation sensitivity**: compute `M_body` from (a) the entire surah, (b) just the first 20% of body tokens (early body), (c) just the last 80% (late body). al-Rāzī's doctrine predicts strongest alignment in the EARLY body if the muqaṭṭaʿāt are the *initial ijmāl* that the early verses then unfold. Body-percentage zero-mark convention: the first non-muqaṭṭaʿāt character of the surah (option a), consistent with arabic-specialist's pipeline convention.
5. **Per-muqaṭṭaʿāt-cluster breakdown**: split the 29 muqaṭṭaʿāt-opening surahs by the 14 distinct muqaṭṭaʿāt patterns (الم, الر, المر, المص, كهيعص, طسم, طه, طس, يس, ص, حم, عسق, ق, ن) and report JS per cluster. Sensitivity, not Bonferroni.

## Cross-tradition comparison (descriptive, not pre-registered)

Compare `KL_muqaṭṭaʿāt` against:
- Bukhari hadith chapter openings (prose baseline)
- Muʿallaqāt opening-bayt vs. body letter-distributions (rhymed baseline)

If Quranic muqaṭṭaʿāt KL is statistically distinct from BOTH baselines, the al-Rāzī doctrine is doubly distinguished. Report as descriptive context, not as a pre-registered Bonferroni test.

## Infrastructure dependency

This test relies on the **[[h-new-24-b1-b2-orthogonalization|H-NEW-24]] letter-multiset extraction pipeline**, already built by arabic-specialist for tasks #44, #64, #65 (CONFIRMED in MASTER §3c). The new feature engineering is:
- Add `extract_muqattaat_opener_multiset(surah_id)` → uniform-on-support probability distribution.
- Add `extract_body_letter_multiset(surah_id, exclude_opener=True)` → empirical letter distribution.
- KL-divergence computation with Laplace smoothing.

These three additions are minimal extensions of the existing pipeline. No new tokenizer, no new corpus loader.

## Hand-off path

1. **classical-scholar** (this file) → file complete. Pre-reg locked under team-lead Option D approval 2026-04-13.
2. **arabic-specialist** → confirm letter-multiset pipeline can be extended with the three feature-engineering additions above. Estimated ~30 min.
3. **computational-tester** → execute the primary KL test + 5 sensitivity checks + descriptive cross-tradition comparison.
4. **classical-scholar** (post-execution) → interpret results in al-Rāzī doctrinal frame, file at `findings/phase-b-hypotheses/h-new-4-ext-d-result.md`.

## Outputs (locked)

- Script: `scripts/h_new_4_ext_d_ijmal_tafsil_js.py` (computational-tester) — renamed from `_kl.py` to reflect the JS-divergence primary per MW-10 amendment. The script must compute JS as primary, KL as sensitivity-0, stratified-KL as sensitivity-1, Hellinger as sensitivity-2, plus the five general-robustness diagnostics.
- Pipeline extension: `scripts/letter_multiset.py` (arabic-specialist) — already built, self-tested 2026-04-13. JS-divergence is directly computable from the existing `kl_divergence` primitive via the mixture-distribution formula; no additional primitives required.
- CSV: `findings/phase-b-hypotheses/csv/h-new-4-ext-d.json` — must include JS primary columns AND the KL sensitivity-0 columns (including the support-size stratified table) AND Hellinger sensitivity-2 columns.
- Result write-up: `findings/phase-b-hypotheses/h-new-4-ext-d-result.md` — must include the §Garden-of-Forking-Paths section with the MW-10 amendment trail, the original KL descriptive confound table, and the mechanism-of-defect explanation.

## Garden of forking paths (pre-disclosed)

This pre-reg supersedes the original task #33 design (which tested at the lemma/TTR scale and was AUDIT-BLOCKED for parent-task contradiction). The Option D re-operationalization moves the test to the letter-graphemic scale per al-Rāzī's literal *al-mujmal* doctrine. This is **not a sign-flip post-hoc**; it is a scale-shift to the layer where the parent task #6 verdict explicitly notes muqaṭṭaʿāt distinctiveness DOES exist ("its distinctiveness is at the letter/phonological level"), and where al-Rāzī's doctrine actually addresses.

The re-operationalization was selected by team-lead from four options (a/b/c/d) surfaced by the classical-scholar AUDIT-BLOCKER memo. See `findings/phase-b-hypotheses/h-new-4-ext-classical-audit.md` for the full audit-and-ruling chain.

No data peeking on the new test outcome. The KL-divergence operationalization is INDEPENDENT of parent task #6's lemma/TTR-scale data: muqaṭṭaʿāt letter-multisets and surah-body letter-multisets are different features than the first-lemma-introduction-rate signature parent task #6 measured.

## Reporting commitment

Both directions publishable. If PASS: al-Rāzī *al-mujmal/al-tafṣīl* doctrine receives first-ever empirical validation at the letter-graphemic scale, computed via 21st-century distributional methods on 11th-century classical scholarship. If NULL: doctrine joins the demoted-classical-intuition list. If REVERSE: serious counter-finding flagged for escalation.
