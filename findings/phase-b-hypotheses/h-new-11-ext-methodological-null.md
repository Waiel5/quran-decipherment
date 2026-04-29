---
finding_id: h-new-11-ext-methodological-null
phase: B
status: COMPLETED-AS-METHODOLOGICAL-NULL
verdict: METHODOLOGICAL-NULL (UNSALVAGEABLE)
date: 2026-04-13
filed_by: classical-scholar
parent_task: 18 (H-NEW-11, verdict PASSED at z=−2.35 aggregate pan-prophetic)
task: 36 (H-NEW-11-EXT)
ruling: team-lead 2026-04-13 — Option C2 (drop) approved
rules_tuple: (no-tashkeel, orthographic-token & lemma, graphemes, counted-only-in-surah-1, hafs-kufan, mashriqi)
sister_audits:
  - findings/phase-b-hypotheses/h-new-11-ext-reprereg.md (pre-falsification halt memo)
  - findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md (parent task #18 §2.4 5-overlap data)
  - findings/phase-b-hypotheses/h-new-4-ext-classical-audit.md (sister audit, #33)
mw_gate_applied: MW-8 (parent-task data-coherence gate) + MW-9 (full-direction empirical check)
---

# [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT — Methodological-null verdict

## Executive verdict

**METHODOLOGICAL-NULL — unsalvageable. Task dropped.**

The [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT extension was an attempt to add a per-prophet ordering test on top of the aggregate pan-prophetic suppression signal established by parent task #18 ([[h-new-11-ext-methodological-null|H-NEW-11]], verdict: PASSED at z=−2.35). Four cumulative pre-execution blockers demonstrated that every executable direction of the extension is already empirically determined by parent task #18's locked data. No independent test remains to be run.

Per team-lead ruling 2026-04-13 (Option C2 among options A2/B2/C2/D2):

> "Option C2 is the protocol-clean move. The original [[h-new-11-ext-methodological-null|H-NEW-11]] hypothesis was already executed and PASSED at z=−2.35 / pan-prophetic confirmation in team-discovery-007. The [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT extension was an attempt to add a per-prophet ordering test on top of that, but the parent data already determines that ordering. There's nothing left to test that the parent didn't already answer."

## The four cumulative blockers

### Blocker 1 — nawʿ 63 citation error

The original task #36 pre-registration (2026-04-13, hypothesis-generator) cited **al-Suyūṭī *Itqān* nawʿ 63 "*qiṣaṣ al-anbiyāʾ*"** as the classical anchor for the per-prophet ordering prediction. Classical-scholar audit revealed:

1. al-Suyūṭī's *al-Itqān fī ʿUlūm al-Qurʾān* contains **80 anwāʿ**, not 83+. nawʿ 63 is NOT on *qiṣaṣ al-anbiyāʾ*; it is on an unrelated topic (fī asbāb al-nuzūl muddled).
2. The *mustaqill/mukarrar* taxonomy (individuated vs repeated prophet narratives) is actually discussed at **nawʿ 56 fī al-ījāz wa-l-iṭnāb**, not nawʿ 63.
3. Correcting the citation is necessary but not sufficient — even with the correct anchor, the direction of the test is empirically determined by parent data (see Blockers 3 and 4).

This is the same citation-defect pattern documented in AMEND-28 (the mechanical nawʿ-range scan). Blocker 1 alone would not drop the task; it would require a retag and re-pre-registration under the corrected nawʿ 56 anchor.

### Blocker 2 — prophet-set mismatch

The original task #36 pre-registered an **8-prophet descending ordering**: Yūsuf > Yaḥyā > Shuʿayb > Hūd > Ṣāliḥ > Ibrāhīm > Mūsā > Nūḥ. Classical-scholar audit cross-referenced this against parent task #18 §2.1 and found only **5 prophets overlap** between the pre-registered 8 and the parent task's tested set: {Yūsuf, Yaḥyā, Ibrāhīm, Mūsā, Nūḥ}. Shuʿayb, Hūd, and Ṣāliḥ were not independently tested in parent task #18 because their pericopes are too small to produce leave-one-out suppression effects above noise floor.

The Spearman ρ computed on the 5-overlap (parent task #18's actual data ∩ pre-registered ordering) yielded ρ = −0.50 per audit memo §2.4, already inconclusive under any reasonable Bonferroni threshold.

### Blocker 3 — Lūṭ counter-prediction pre-falsified

The original task #36 added a tertiary counter-prediction: **Lūṭ should be a NEGATIVE suppression driver** per al-Ṭabarī/al-Qurṭubī's repetition-heavy framing. Classical-scholar audit revealed that parent task #18's §2.5 already contained Lūṭ's empirical leave-one-out effect, and the sign was the OPPOSITE of the al-Ṭabarī prediction. Lūṭ behaves as a positive driver, not a counter-driver, in the actual data.

Blocker 3 was the first pre-falsification caught at the classical-scholar audit gate. It was disclosed in the audit memo filed prior to team-lead's initial Option A ruling. Team-lead's Option A response explicitly said "drop the Lūṭ counter-prediction" — which was done.

### Blocker 4 — 5-overlap primary binary pre-falsified (the second-round catch)

Under team-lead's Option A re-pre-registration (2026-04-13), the test was narrowed to:
- **Binary 1**: "Yūsuf is the #1 suppression driver among the 5-overlap" (p_null = 1/5).
- **Binary 2**: "Mūsā and Nūḥ are the bottom-2 pair among the 5-overlap" (p_null = 1/10).
- Joint k=2 Bonferroni, α_bon = 0.025.

Classical-scholar audit (the second-round pre-dispatch check) cross-referenced Option A's binary directions against the same parent task #18 §2.4 data. The empirical |z| ranking on the 5-overlap was:

| Rank | Prophet | |z| |
|---|---|---|
| 1 | Ibrāhīm | 3.80 |
| 2 | Nūḥ | 3.50 |
| 3 | Yaḥyā | 3.41 |
| 4 | Mūsā | 3.23 |
| 5 | **Yūsuf** | **2.37** (LAST) |

- **Binary 1 maximally inverted**: Yūsuf is at rank 5, not rank 1. The pre-registered direction is empirically the worst possible prediction of the 5 options.
- **Binary 2 partially falsified**: Mūsā IS in the bottom-2 (with Yūsuf), but Nūḥ is at RANK 2 in the TOP, not bottom. The pair {Mūsā, Nūḥ} is empirically one of the worst possible pair predictions — the actual bottom-pair is {Mūsā, Yūsuf}.
- **Joint k=2 test definitionally falsified** before any compute.

Blocker 4 is the same defect class as Blocker 3 (pre-registered direction contradicted by parent data), applied this time to the PRIMARY directions of the Option A re-prereg rather than a tertiary counter-prediction. The classical-scholar audit caught it because, after the Blocker 3 lesson, the pre-execution check was extended to cover every pre-registered direction — which became the content of the newly-promoted MW-9 standing rule.

### Why the four blockers are cumulative and unsalvageable

| Blocker | Level | Remediation if alone | Remediation in combination |
|---|---|---|---|
| 1 (nawʿ citation) | Citation | Retag to nawʿ 56 | Doesn't rescue; data still determines result |
| 2 (prophet-set mismatch) | Scope | Reduce to 5-overlap | Reveals underlying pre-falsification |
| 3 (Lūṭ counter pre-falsified) | Counter-prediction | Drop counter | Leaves the primary |
| 4 (5-overlap primary pre-falsified) | Primary direction | Sign-flip ruled out by PRE-REG-STANDARD-04 | **No executable test remains** |

After Blocker 4, the only "rescues" available are:
- **A2**: Sign-flip the primary binary. RULED OUT by PRE-REG-STANDARD-04 (no sign-flips post-hoc).
- **B2**: Switch to HHI on lemma-mass. REJECTED by team-lead — the underlying ordering is what generates the HHI, so testing HHI on the same 5 prophets whose ordering is already locked is forking-paths-adjacent.
- **C2**: Drop entirely. **APPROVED BY TEAM-LEAD 2026-04-13** (this verdict).
- **D2**: Scale-shift to a different operationalization. Not defined — no candidate scale escapes parent-data determination for the per-prophet ordering question specifically.

## The parent-task context (what IS established)

To be clear about what parent task #18 ([[h-new-11-ext-methodological-null|H-NEW-11]]) actually established:

- **Aggregate pan-prophetic suppression signal**: PASSED at z=−2.35 in team-discovery-007. When you remove any prophet-pericope, the surah's vocabulary-introduction-rate signature shifts in the predicted direction on aggregate.
- **Per-prophet leave-one-out drivers**: all 5-overlap prophets show individual |z| > 2.0 (range 2.37 to 3.80). Each prophet contributes to the aggregate signal, with Ibrāhīm as the largest individual driver and Yūsuf as the smallest.
- **The aggregate verdict is not at question.** [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT was never an attempt to re-test the aggregate — it was an attempt to test whether the *per-prophet ordering* matched al-Suyūṭī's classical *mustaqill/mukarrar* taxonomy (individuated narratives should be stronger drivers). The empirical ordering does NOT match that taxonomy: Ibrāhīm is the #1 driver, not Yūsuf (whom the classical taxonomy marks as the most individuated). The classical taxonomy is inverted by the data.

## Honest publishable framing

Per team-lead's ruling:

> "[[h-new-11-ext-methodological-null|H-NEW-11]]'s pan-prophetic suppression PASSES at the aggregate level (z=−2.35); per-prophet ordering is fully determined by parent data and admits no independent test."

More fully: the classical *mustaqill/mukarrar* taxonomy predicts that individuated prophets (Yūsuf, Yaḥyā) should be the strongest suppression drivers, and homogenizing prophets (Mūsā, Nūḥ) should be the weakest. Parent task #18's actual data inverts this — **Ibrāhīm (widely distributed) is the strongest driver, and Yūsuf (maximally individuated) is the weakest**. The classical taxonomy is not predictive of the per-prophet suppression signal at the leave-one-out level.

This is **itself a publishable negative finding at the descriptive level**: al-Suyūṭī's *mustaqill/mukarrar* taxonomy, while valid as a literary classification, does not predict computational-suppression contribution. It should be filed as a descriptive note in MASTER §3 refutations bin, NOT as a pre-registered test result, because the direction was determined by parent data before the re-pre-registration was locked.

## MW-tier classification of the non-result

- **Pre-registration integrity**: MW-8 gate catch + MW-9 gate catch (both promoted as standing rules 2026-04-13 based on this instance).
- **Classical citation**: al-Suyūṭī *Itqān* nawʿ 56 (not 63 per Blocker 1); MW-4 PENDING per AMEND-28.
- **Parent-task data source**: `findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md` §2.4 (parent task #18 locked data).
- **Defect class**: "downstream-from-post-hoc-finding test with parent-data direction determination." Documented as the paradigm case for MW-8 and MW-9.

## Reporting commitments

- **Methodological-null is a publishable verdict**. It documents how rigorous pre-execution audit catches a hypothesis that is structurally unsalvageable, before any compute is wasted.
- **Descriptive negative note**: al-Suyūṭī *mustaqill/mukarrar* taxonomy does NOT predict computational leave-one-out suppression ordering (file under MASTER §3 refutations bin as descriptive, not as a pre-registered test result).
- **Parent task #18 verdict unchanged**: aggregate pan-prophetic suppression PASSED at z=−2.35. Nothing in [[h-new-11-ext-methodological-null|H-NEW-11]]-EXT's methodological-null verdict downgrades the parent.

## Cross-references

- Parent task #18 data source: `findings/phase-b-hypotheses/prophet-suppression-classical-ordering.md` §2.4
- Pre-falsification halt memo: `findings/phase-b-hypotheses/h-new-11-ext-reprereg.md` §"SECOND PRE-FALSIFICATION DETECTED — DO NOT DISPATCH"
- Sister audit (#33): `findings/phase-b-hypotheses/h-new-4-ext-classical-audit.md`
- Standing rule MW-8: `findings/TEAM-AMENDMENTS-LOG.md` (filed 2026-04-13)
- Standing rule MW-9: `findings/TEAM-AMENDMENTS-LOG.md` (filed 2026-04-13)
- MASTER §3 refutations bin entry: pending integrator migration
- Team-lead ruling on Option C2: 2026-04-13, quoted above

## Authorship

Filed by classical-scholar, 2026-04-13. Methodological-null verdict approved by team-lead 2026-04-13 same date. Cumulative blocker sequence caught entirely at the classical-scholar pre-execution audit gate before any computational-tester compute was expended on a pre-falsified test.
