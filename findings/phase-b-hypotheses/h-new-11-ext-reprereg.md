---
finding_id: h-new-11-ext-reprereg
phase: B
status: HALTED-SECOND-PRE-FALSIFICATION-DETECTED — re-pre-reg cannot dispatch as-written; both binary tests pre-falsified by parent task #18 data (same defect class as the dropped Lūṭ counter-prediction). Awaiting team-lead second adjudication.
date: 2026-04-13
task_ref: #36 H-NEW-11-EXT
parent_task: #18 H-NEW-11 (team-discovery-007.md, COMPLETED)
parent_audit: findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md (AUDIT-BLOCKER 2026-04-13)
team_lead_ruling: 2026-04-13 Option A APPROVED with strengthening
owner: classical-scholar
rules_tuple: (no-tashkeel, lemma QAC v0.4, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
classical_sources_locked:
  - al-Suyūṭī al-Itqān fī ʿUlūm al-Qurʾān, Shamela0011728 ed., **nawʿ 56 fī al-ījāz wa-l-iṭnāb, vol. 3 pp. 229-232** (CORRECTED from prior nawʿ 63 citation error)
  - Fakhr al-Dīn al-Rāzī Mafātīḥ al-Ghayb, Shamela0023635 ed. (Lūṭ vocabulary-sharing context, NOT used as counter-prediction in this re-prereg)
  - QAC v0.4 Quranic lemma data
mw_tier: MW-6 PENDING per AMEND-28 (verbatim from Shamela0011728, not physical-edition verified)
seed: 20260413
bonferroni_k: 2
alpha_unadjusted: 0.05
alpha_bon: 0.025
sided_test: one-sided (binary, both directions pre-committed)
null_publishable: true
positive_publishable: true
supersedes: task #36 original pre-reg (in body of task description)
---

# [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT — Re-pre-registration under team-lead Option A

## Executive summary

**Three pre-reg defects in the original task #36 specification have been adjudicated**:

1. **Citation error** (nawʿ 63 → nawʿ 56): corrected to al-Suyūṭī al-Itqān nawʿ 56 *fī al-ījāz wa-l-iṭnāb* vol. 3 pp. 229-232. Verbatim source material in the parent audit memo §1.2.
2. **Prophet-set mismatch** (8 pre-reg vs 8 measured, only 5 overlap): converted from full Spearman ρ on n=8 to **binary tests on the 5-prophet overlap**. The 5-prophet set is locked: {Yūsuf, Yaḥyā, Ibrāhīm, Mūsā, Nūḥ}.
3. **Lūṭ counter-prediction already falsified**: dropped entirely. Recorded as `pre-falsified-counter-prediction-removed-pre-execution` in the audit trail.

Bonferroni budget reduces from k=3 to **k=2** (Binary 1 + Binary 2). α_bon = 0.025 each.

**The 5-prophet set explicitly does NOT expand or substitute mid-test.** Small-n binary instrument is conservative and only fires on extreme drivers; mid-rank ordering effects are out of scope.

## Classical anchor — al-Suyūṭī al-Itqān nawʿ 56 (CORRECTED)

### Source

al-Suyūṭī, al-Itqān fī ʿUlūm al-Qurʾān, Shamela0011728 ed., **nawʿ 56 *fī al-ījāz wa-l-iṭnāb***, vol. 3 pp. 229-232.

### Verbatim establishing material

**Mūsā/Nūḥ as repetition-heavy (anchors positions 7-8 = bottom of individuation)**:

> Line 17365-17367, p. V03P229: وَمِنْ ذَلِكَ تَكْرِيرُ القِصَصِ كَقِصَّةِ آدَمَ وَمُوسَى وَنُوحٍ وَغَيْرِهِمْ مِنَ الأَنْبِيَاءِ. قَالَ بَعْضُهُمْ: ذَكَرَ اللَّهُ مُوسَى فِي مِائَةٍ وَعِشْرِينَ مَوْضِعًا مِنْ كِتَابِهِ. وَقَالَ ابْنُ العَرَبِيِّ فِي القَوَاصِمِ: ذَكَرَ اللَّهُ قِصَّةَ نُوحٍ فِي خَمْسٍ وَعِشْرِينَ آيَةً وَقِصَّةَ مُوسَى فِي تِسْعِينَ آيَةً.

*"And among that [iṭnāb by way of takrār] is the repetition of the stories, such as the story of Ādam, Mūsā, and Nūḥ and others of the prophets. Someone said: God mentioned Mūsā in 120 places of His book. Ibn al-ʿArabī said in al-Qawāṣim: God mentioned Nūḥ's story in 25 āyāt and Mūsā's story in 90 āyāt."*

**Yūsuf as uniquely individuated (anchors position 1 = top of individuation)**:

> Line 17393, p. V03P230: وَقَدْ سُئِلَ: مَا الحِكْمَةُ فِي عَدَمِ تَكْرِيرِ قِصَّةِ يُوسُفَ وَسَوْقِهَا مَسَاقًا وَاحِدًا فِي مَوْضِعٍ وَاحِدٍ دُونَ غَيْرِهَا مِنَ القِصَصِ؟

*"And it has been asked: what is the wisdom in not repeating the story of Yūsuf and telling it in a single sequence in one place, unlike the other stories?"*

al-Suyūṭī then offers 5 justifications for Yūsuf's individuation (the five wujūh from al-Isfarāʾīnī, the relief-after-hardship distinction, the proof-of-miraculousness argument, the ṣaḥāba-request narrative, and the destruction-pericope warning-function distinction).

### What al-Suyūṭī nawʿ 56 establishes for the 5-prophet overlap

| Prophet | Anchor in nawʿ 56 | Position |
|---|---|---|
| Yūsuf | Explicit singular non-repeated; 5 justifications | **TOP (1 of 5)** |
| Yaḥyā | Not in nawʿ 56 (ḥanān hapax anchor in Suyūṭī nawʿ 36 line 7013-7017) | Mid |
| Ibrāhīm | Not explicitly ranked in nawʿ 56; al-Rāzī Mafātīḥ has 1607 separate discussions (template-central per Razi) | Mid |
| Mūsā | "120 places", "90 āyāt" — most-repeated of all | **BOTTOM (joint 4-5 of 5)** |
| Nūḥ | "25 āyāt" — destruction-template prophet | **BOTTOM (joint 4-5 of 5)** |

**Classically anchored extremes**: Yūsuf at top, Mūsā/Nūḥ at bottom. Yaḥyā and Ibrāhīm are mid-ranked (not directly anchored in nawʿ 56) and are NOT tested in this re-pre-registration.

## Pre-registered tests

### Binary 1 — Yūsuf-top-driver test

**Hypothesis**: Yūsuf is the strongest individuator (top driver of suppression) within the 5-prophet overlap set {Yūsuf, Yaḥyā, Ibrāhīm, Mūsā, Nūḥ}.

**Test statistic**: Yūsuf's leave-one-out |z| from task #18 is the largest of the 5.

**Null model**: Under the null that classical individuation taxonomy does not predict suppression contribution, each of the 5 prophets is equally likely to be the top driver. **p_null = 1/5 = 0.20**.

**One-sided** by classical pre-registration (Yūsuf-top is the doctrinally pre-committed direction).

**α_bon = 0.025**.

**Acceptance**: Binary 1 PASSES if Yūsuf is the top |z| in the 5-prophet set AND (since p_obs = 0.20 if Yūsuf is top and p_null = 0.20, the test as-stated cannot reach α_bon at single observation). **Therefore Binary 1 is registered as a directional confirmation only**, not as a Bonferroni-significant test by itself. It enters the joint-test alongside Binary 2.

### Binary 2 — Mūsā-Nūḥ-bottom-pair test

**Hypothesis**: Mūsā AND Nūḥ are the two weakest drivers of suppression (joint bottom-2) within the 5-prophet overlap set.

**Test statistic**: The two smallest |z| values among the 5 are Mūsā and Nūḥ (in either order).

**Null model**: Under the null, the two weakest drivers are a uniform random pair from C(5,2) = 10 possible pairs. **p_null = 1/10 = 0.10**.

**One-sided** by classical pre-registration (Mūsā/Nūḥ-bottom is the doctrinally pre-committed direction).

**α_bon = 0.025**.

**Acceptance**: Binary 2 PASSES if both Mūsā and Nūḥ are in the bottom-2 |z| within the 5-prophet set. p = 0.10, which is above α_bon = 0.025 → Binary 2 alone also cannot reach Bonferroni significance.

### Joint test — Binary 1 AND Binary 2

The two binaries are pre-registered as a joint Fisher's combined test:

**Joint null probability**: under independence of Binary 1 and Binary 2 (both are conditional on the same 5-prophet ranking, but their joint occurrence is over a small permutation space):

- 5! = 120 total orderings of 5 prophets
- Orderings where Yūsuf is rank 1 AND {Mūsā, Nūḥ} are ranks 4-5 (in either order): 1 × 2 × 3! / 5! ... let me compute exactly. Yūsuf in rank 1: fixes 1 position. Mūsā and Nūḥ in ranks 4-5 (either order): 2 arrangements. Yaḥyā and Ibrāhīm fill ranks 2-3: 2 arrangements. Total favorable orderings = 1 × 2 × 2 = 4. Total orderings = 120. **p_joint_null = 4/120 = 0.0333.**

The joint test is NOT below α_bon = 0.025 even at perfect alignment.

### Power-honest declaration

**This re-pre-registration is power-limited by construction.** Even at the maximum possible alignment (Yūsuf rank 1, Mūsā/Nūḥ ranks 4-5), the joint p-value is 0.0333, which is above the Bonferroni-corrected α_bon = 0.025. The test cannot achieve Bonferroni-significant pass on the 5-prophet overlap.

**What this re-pre-registration CAN deliver**:

1. **Directional confirmation or refutation**. If Yūsuf is rank 1 AND Mūsā/Nūḥ are ranks 4-5 → the classical individuation taxonomy is **directionally validated** at uncorrected p = 0.0333 (suggestive but not Bonferroni-clean). Filed as DIRECTIONALLY-CONFIRMED.
2. **Refutation** if either binary fails. If Yūsuf is NOT rank 1, OR Mūsā/Nūḥ are not joint bottom-2 → the classical taxonomy fails to predict the empirical ranking on the overlap. Filed as REFUTED.
3. **Power-honest null** if the 5-prophet ordering is mixed (Yūsuf rank 1 but Mūsā ranks 2 — or similar partial pattern). Filed as PARTIAL.

This is reported in the dispatch packet and in the result file. The team has accepted the power limit as the cost of pre-reg integrity over the alternative (Option B re-running task #18 LOO on a different prophet set, which adds ~1 session of compute).

## Pre-falsified-counter-prediction-removed-pre-execution

The original task #36 tertiary test ("Lūṭ's leave-one-out is negative — reduces suppression when removed") is **dropped from this re-pre-registration**. The reason is that task #18 already reports Lūṭ LOO z = −2.35 with obs−null = −0.028, which means Lūṭ removal still reduces suppression in the same direction as all other prophets. The original counter-prediction expected Lūṭ to act as a positive driver (increase suppression when removed), and this expectation is contradicted by the parent task's own data **before any execution of [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT**.

Per team-lead instruction 2026-04-13: this drop is recorded as `pre-falsified-counter-prediction-removed-pre-execution` in the audit trail. It is not a forking-paths violation because:

- The contradiction is fully documented in the parent audit memo before this re-pre-reg was filed.
- The decision to drop was made by the team-lead on review, not by classical-scholar after seeing favorable post-execution numbers.
- No alternative direction is being pre-registered in its place. The Lūṭ test is simply removed from the Bonferroni budget (k drops from 3 to 2).
- Lūṭ is also NOT in the 5-prophet overlap set, so it could not be tested under the binary instrument anyway.

## Locked specifications

| Field | Value |
|---|---|
| Prophet set | {Yūsuf, Yaḥyā, Ibrāhīm, Mūsā, Nūḥ} (locked, 5 prophets) |
| Test 1 | Binary: Yūsuf is top |z| in 5-set; p_null = 0.20 |
| Test 2 | Binary: {Mūsā, Nūḥ} are joint bottom-2 |z| in 5-set; p_null = 0.10 |
| Joint test | Yūsuf rank 1 AND {Mūsā, Nūḥ} ranks 4-5; p_null = 0.0333 |
| Bonferroni k | 2 |
| α_bon | 0.025 per binary |
| Sided | one-sided (both directions pre-committed by classical anchor) |
| Seed | 20260413 |
| Data source | task #18 LOO results (team-discovery-007.md) — NO new computation needed |
| Lūṭ counter-prediction | DROPPED (pre-falsified-counter-prediction-removed-pre-execution) |
| Power note | Power-limited; cannot reach Bonferroni-significant pass; max joint p = 0.0333 at perfect alignment |
| Output | This file ([[h-new-11-ext-methodological-null|h-new-11]]-ext-reprereg.md) + result section appended below by computational-tester |

## Verdict tier table

| Joint outcome | Verdict |
|---|---|
| Yūsuf rank 1 AND {Mūsā, Nūḥ} ranks 4-5 | **DIRECTIONALLY-CONFIRMED** at uncorrected p = 0.0333 (classical individuation taxonomy supported on the 5-prophet overlap) |
| Yūsuf rank 1, but Mūsā/Nūḥ not joint bottom-2 | **PARTIAL** — Yūsuf-individuation supported, repetition-heaviness not |
| Yūsuf NOT rank 1, but Mūsā/Nūḥ are joint bottom-2 | **PARTIAL** — repetition-heaviness supported, Yūsuf-individuation not |
| Neither binary fires | **REFUTED** — classical taxonomy does not predict empirical ranking |

## MW-6 PENDING tag (per AMEND-28)

The classical anchor citations to al-Suyūṭī Itqān nawʿ 56 vol. 3 pp. 229-232 are at MW-6 PENDING confidence per AMEND-28. The verbatim Arabic is from the Shamela0011728 OpenITI plaintext at:

```
/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt
```

Lines 17365-17367 (page V03P229) and 17393 (page V03P230) and 17398-17413 (page V03P230). Page numbers map to the Dār al-Kitāb al-ʿArabī Cairo print edition that Shamela 0011728 is based on. **Physical edition verification has not occurred**. Any downstream citation of these passages must carry the PENDING tag until verified.

## Dispatch instruction

Computational-tester: this re-pre-registration replaces the original task #36 specification. **No new computation is required.** The test is a direct read of task #18's LOO results filtered to the 5-prophet overlap, followed by binary checks of Yūsuf-rank-1 and Mūsā/Nūḥ-joint-bottom-2.

Run-time: <5 minutes including writing the result section to this file. No compute, no permutation null, no bootstrap.

Output file: append a "Result" section to this file, also write the JSON to `findings/phase-b-hypotheses/csv/h-new-11-ext.json`.

## Audit trail

- 2026-04-13: Original task #36 pre-reg authored by hypothesis-generator
- 2026-04-13: Classical-scholar audit identifies 3 blockers, files `prophet-suppression-classical-ordering.md` at status AUDIT-BLOCKER
- 2026-04-13: Team-lead reviews, approves Option A binary reframe with strengthening (lock 5-prophet overlap, drop Lūṭ counter-prediction)
- 2026-04-13: Classical-scholar drafts re-pre-reg under Option A
- 2026-04-13: **Classical-scholar HALTS dispatch on second pre-falsification check** — both binary tests are already empirically falsified by parent task #18 data. Same defect class as the dropped Lūṭ counter-prediction. See §"SECOND PRE-FALSIFICATION DETECTED" below.
- (next): Team-lead second adjudication required

---

## SECOND PRE-FALSIFICATION DETECTED — DO NOT DISPATCH

### What I missed in the first pass

The team-lead's Option A specification (binary reframe with locked 5-prophet overlap) carried the implicit assumption that Yūsuf-top and Mūsā/Nūḥ-bottom would be pre-execution open questions. They are not. The audit memo §2.4 already documented the empirical |z| ranking on the 5-overlap, but I read that as "Spearman ρ = -0.50 means the rank-correlation is inverted" without computing what that inversion means for the binary tests.

### Empirical |z| ranking on the 5-prophet overlap (from audit memo §2.4)

| Rank by |z| (1 = strongest driver) | Prophet | |z| |
|---|---|---|
| 1 | Ibrāhīm | 3.80 |
| 2 | Nūḥ | 3.50 |
| 3 | Yaḥyā | 3.41 |
| 4 | Mūsā | 3.23 |
| **5** | **Yūsuf** | **2.37** |

### Binary 1 (Yūsuf is top driver) — PRE-FALSIFIED

The pre-reg's Binary 1 predicts Yūsuf at rank 1. The empirical Yūsuf is at rank **5** (last). Binary 1 is **maximally inverted** — Yūsuf is the WEAKEST driver in the 5-overlap, not the strongest.

This is not a noise-level mismatch. p_observed under the test as-stated = 0 (Yūsuf is not rank 1 with absolute certainty in the existing data).

### Binary 2 (Mūsā/Nūḥ are joint bottom-2) — PARTIALLY PRE-FALSIFIED

Empirical bottom-2 by |z| in the 5-overlap = {Mūsā (rank 4), Yūsuf (rank 5)}. Mūsā IS in the bottom-2, but Nūḥ is at rank **2** (second-strongest driver, not bottom).

So Binary 2 is partially pre-falsified: 1 of 2 elements correct (Mūsā in bottom), 1 of 2 wrong (Nūḥ in top-2 not bottom-2). Under the test as-stated, Binary 2 fails because both elements must be in bottom-2 for the binary to fire.

### Joint test — definitionally falsified

The joint test (Yūsuf rank 1 AND {Mūsā, Nūḥ} ranks 4-5) cannot fire because Yūsuf is rank 5 and Nūḥ is rank 2. p_observed = 0.

### Why this is a forking-paths violation if dispatched

Dispatching this re-pre-reg to computational-tester would be a *theatrical* execution: the result is locked in by the parent task's data, computational-tester would do <5 minutes of work to confirm what the audit memo already documented at line 152-156, and the result would be filed as "REFUTED" with the appearance of pre-registered rigor.

This is the **same defect class** as the original task #36 Lūṭ counter-prediction (Blocker 3 in the audit memo): a hypothesis pre-registered against existing parent-task data that already contradicts the prediction. The team-lead correctly directed me to drop the Lūṭ counter-prediction for this reason. The same logic applies — with the same force — to Binary 1 (Yūsuf-top).

The audit discipline rule that catches this:

> **Pre-registration of a directional hypothesis against existing data is forbidden when the data already determines the result.**

This rule does not have a "primary vs counter" exception. A primary test pre-registered against pre-falsifying data is the same forking-paths violation as a counter-test pre-registered against pre-falsifying data.

### Theoretical reconciliation

The audit memo §2.5 already gave the reconciliation:

> Pre-reg logic: Yūsuf is individuated (unique lexicon) → when dropped, the REMAINING set loses that unique lexicon → suppression reduces → Yūsuf is a STRONG driver.
> 
> Task #18 logic: Abraham is TEMPLATE-central (most shared lexicon) → when dropped, the REMAINING set's shared-lexicon backbone breaks → suppression reduces → Abraham is the strongest driver.
> 
> These are **opposite directions in the same metric**.

The al-Suyūṭī *individuation = top-driver* logic and the empirical *template-centrality = top-driver* logic are inverted. Empirical task #18 is template-centrality. Any pre-reg following the al-Suyūṭī individuation prediction will be inverted by the data. **The metric (mean Jaccard to others, leave-one-out impact) is not classically aligned with the al-Suyūṭī taxonomy.** This is not a defect in al-Suyūṭī or in task #18 — it is a defect in the choice of metric for the prediction.

### Re-routing options for team-lead second adjudication

**Option A2 — REGISTER AS REVERSE FINDING.** Sign-flip the binary instrument: predict Yūsuf at rank 5 AND {Mūsā, Nūḥ} not joint bottom-2. This becomes a test of "the empirical metric is template-centrality, not classical individuation." Both binaries fire (Yūsuf rank 5 ✓, Nūḥ not in bottom-2 ✓). Joint p under inverted null:
- Yūsuf in rank 5 (specific position 5): p = 1/5
- Nūḥ in top-2 (ranks 1-2): p = 2/5
- Independence-corrected joint p ≈ 1/5 × 2/5 = 0.08 (not exactly because positions are coupled, but close)

This is a **REVERSE-FINDING pre-registration** — same shape as H-NEW-34's reverse-signal exploratory upgrade path. Publishable as "the Jaccard LOO metric is template-centrality-aligned, not classical-individuation-aligned, and the al-Suyūṭī nawʿ 56 taxonomy is INVERTED on this metric." This is honest, classically anchored (al-Suyūṭī nawʿ 56 is the predicted direction; empirical inversion is the published finding), and uses pre-existing parent data without forking. **However**, sign-flipping a pre-reg post-hoc is itself a forking-paths violation unless the inversion is registered as the test BEFORE the data is read. Since the audit memo §2.4 already reads the data, this option is also off the table for STRICT pre-reg discipline.

**Option B2 — Switch to a different metric (audit memo Option D).** Re-define the per-prophet contribution as **Herfindahl-Hirschman concentration** of each prophet's lemma occurrences across surahs (or related individuation-aligned metric). HHI on lemma-mass distribution is not the same as Jaccard LOO; it directly measures classical individuation. This requires ~1 session of new computation but produces a **fresh, never-before-seen metric** on which the al-Suyūṭī prediction is testable. This is the cleanest path — new metric means no parent data to violate.

**Option C2 — DROP [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT entirely.** File as a methodological null: "the Jaccard LOO metric is template-centrality-aligned and cannot test al-Suyūṭī's individuation taxonomy. Both metric and taxonomy are valid in their own frames; their pairing in task #36 was a category error. No test of al-Suyūṭī nawʿ 56 individuation is currently possible against task #18 data." Filed under MASTER §3 chronology-style methodological-null bin.

**Option D2 — AMEND-and-DISPATCH but document clearly.** Dispatch the binary instrument anyway, but the result section pre-fills the falsification (Yūsuf rank 5, Nūḥ rank 2) and files it as "PRE-FALSIFICATION CONFIRMED — al-Suyūṭī nawʿ 56 individuation taxonomy does NOT predict Jaccard LOO suppression contribution; metric is template-centrality-aligned per task #18 §X." This is honest about what happened (the test was theatrical because parent data locked the answer) and produces a legitimate publishable null with appropriate discipline disclosure. Same shape as the Lūṭ-counter-prediction-drop disclosure in this re-pre-reg. The advantage over Option A2 is that it does NOT sign-flip; it simply runs the original direction and reports the negative result with full pre-falsification disclosure.

**Classical-scholar recommendation**: Option B2 (HHI on lemma-mass distribution) is the most informationally productive. Option C2 is the most defensible if the team wants minimum effort and maximum honesty. Option D2 is acceptable as a fallback if the team prefers to close out task #36 quickly without new compute.

I am NOT dispatching anything to computational-tester until team-lead picks one of B2/C2/D2 (A2 being off the table per pre-reg discipline). Status: HALTED.
