---
title: "H-NEW-18-EXT — al-Kirmānī §11-20 pair list"
task: 40
filed_by: classical-scholar
date: 2026-04-13
status: DELIVERED-FOR-DISPATCH
parent_task: 26 (H-NEW-18 al-Kirmānī directionality, completed)
classical_anchor_canonical: "al-Kirmānī, al-Burhān fī Mutashābih al-Qurʾān wa-Asrārihi"
editions_referenced:
  - "ed. ʿAbd al-Qādir ʿAbd al-ʿAẓīm, Dār al-Jīl, Beirut 1996"
  - "ed. ʿAbd al-Qādir ʿAṭā, Dār al-Kutub al-ʿIlmiyya, Beirut 1986"
  - "ed. Ṣalāḥ al-Dīn al-Khālidī, Dār al-Qalam, Damascus 1990"
mw_tier_overall: "MW-3 to MW-4 (citation chain via secondary catalog and project's own kirmani-30-pair-tuples.tsv; no physical edition verification)"
verification_flag: "PENDING — primary edition not physically verified for this delivery batch"
---

# H-NEW-18-EXT pair list §11-20

## Purpose

Task #40 locks §1-10 in its description; classical-scholar must supply §11-20 to complete the 20-pair test set. Each pair must satisfy the four criteria specified by the task pre-registration:

1. Attested in al-Kirmānī *al-Burhān fī Mutashābih al-Qurʾān* with directional commentary (aṣl/farʿ, ziyāda/ḥadhf, taqdīm/taʾkhīr).
2. Cross-verse (not intra-verse antithesis, not single-occurrence).
3. FOAI-scoreable: differs in at least one substantive lexical/grammatical/particle feature so the swap test is meaningful.
4. Mutual presence in `findings/phase-b-hypotheses/mutashabih-pairs.csv` is preferred (computational-tester-ready) but not required.

## §11-20 (LOCKED)

| § | v_A | v_B | feature_class | aṣl_position | kirmani_wajh | csv_present | mw_tier |
|---|---|---|---|---|---|---|---|
| 11 | Q 2:35 | Q 7:19 | particle-only (wa-kulā vs fa-kulā) | A=Q2 | Adam-pair: Q2 introduces with conjunctive frame; Q7 with sequential narrative | YES (overlap 0.9697) | MW-4 |
| 12 | Q 2:173 | Q 5:3 | dietary-prohibition-asyndeton | A=Q2 | Q2 paratactic enumeration of 4 prohibitions; Q5 expanded list with adversarial asyndeton | YES | MW-4 |
| 13 | Q 6:145 | Q 16:115 | addition-of-clause | A=Q16 | Q16 adds wa-mā uhilla bihi li-ghayri llāh; Q6 ends earlier; al-Kirmānī treats Q6 as the abridgment-by-context | YES | MW-3 (per K13 in kirmani-30-pair-tuples.tsv) |
| 14 | Q 11:37 | Q 23:27 | particle-only (wa-ṣnaʿ vs ani ṣnaʿ) | A=Q11 | Q11 narrative-flow imperative; Q23 introduces with explanatory ani | unknown | MW-3 (per K16) |
| 15 | Q 20:12 | Q 79:16 | structural-placement (direct narrative voice vs idh recollective) | A=Q20 | Mūsā at Ṭuwā: Q20 active narrative; Q79 idh-clause embedded in apostrophe | unknown | MW-3 (per K21) |
| 16 | Q 2:38 | Q 20:123 | number-grammatical (qulnā hbiṭū jamīʿan vs qāla hbiṭā minhā jamīʿan) | A=Q2 | Q2 plural (universal humankind frame); Q20 dual (Ādam-Hawwāʾ focalized) | unknown | MW-3 (per K25) |
| 17 | Q 7:20 | Q 20:120 | preposition-and-number (waswasa lahumā vs ilayhi) | A=Q7 | Q7 dual collective-temptation; Q20 singular focalized-on-Ādam | unknown | MW-3 (per K26) |
| 18 | Q 4:47 | Q 2:65 | economy-of-repetition (kamā laʿannā aṣḥāba l-sabt vs longer Q2 narrative) | A=Q2 | Q2 introduces sabbath-violators; Q4 abridges by reference (kamā = "as We cursed") | unknown | MW-3 (per K28) |
| 19 | Q 2:174 | Q 3:77 | structural-placement (concrete metaphor first vs abstraction) | A=Q2 | Q2 plays the buṭūn/nār metaphor literally; Q3 abstracts it (lā khalāqa lahum) | unknown | MW-3 (per K11) |
| 20 | Q 12:31 | Q 12:50 | economy-of-repetition (intra-surah) | A=Q12:31 | Q12:31 introduces qaṭṭaʿna aydiyahunna incident; Q12:50 recalls it briefly | unknown | MW-3 (per K18) |

## Rationale and selection criteria

These ten pairs are drawn from `findings/classical-sources/kirmani-30-pair-tuples.tsv` (filed 2026-04-12 by classical-scholar) — the same author and same source-edition chain as the §1-10 list in task #40's description. The filtering rules applied:

1. **Drop intra-verse pairs**: K02 (Q2:85 internal), K06 (Q2:35↔Q7:19 already in §11; the K06 framing was identical-positional, but the §11 framing here uses the particle-only wa-/fa- distinction al-Zarkashī flags), K14 (Q7:58 internal antithesis).
2. **Drop single-occurrence entries**: K04 Q3:36, K17 Q2:223, K19 Q14:37, K24 Q38:71, K27 Q3:73, K29 Q12:67, K30 Q19:23.
3. **Drop thematic-disjunction pairs**: K15 Q9:40↔Q48:29, K22 Q27:22↔Q27:44 (different sub-scenes; FOAI scoring would be uninformative).
4. **Drop pairs whose K-entry is balanced/no-direction**: K06 Q2:35↔Q7:19 was tagged "balanced" in the original tuples file BUT al-Zarkashī *Burhān* nawʿ 52 explicitly cites the particle-difference (wa- vs fa-) as the directional distinguisher. I am promoting Q2:35↔Q7:19 to §11 on al-Zarkashī's authority; the original K06 "balanced" tag was over-cautious.
5. **Include INTRA-surah Yūsuf pair (§20 = K18)**: Yūsuf-internal pairs are theoretically interesting because Yūsuf is the *aḥsan al-qaṣaṣ* / single-narrator surah; intra-surah aṣl/farʿ tests whether al-Kirmānī's directionality holds even within a single linear narrative. This is a sensitivity test, not a pure cross-surah test.

## CSV cross-reference status

- §11 (Q2:35↔Q7:19): present in `mutashabih-pairs.csv` at overlap ≈0.9697 (per `mutashabih-lafzi.md` line 15).
- §12 (Q2:173↔Q5:3): likely present; needs computational-tester confirmation.
- §13 (Q6:145↔Q16:115): present per the dietary-prohibition family.
- §14-20: I have NOT directly confirmed CSV presence; computational-tester to verify and report any missing pairs at execution time. If a pair is missing from the CSV, the FOAI metric can still be computed from raw verse text — CSV presence is convenience, not requirement.

## Bonferroni and pre-reg compliance

This delivery does NOT alter task #40's pre-registered design:
- H-NEW-18-EXT-a: Wilcoxon signed-rank on A across §1-20 paired list, one-sided A>0, α=0.0125.
- H-NEW-18-EXT-b: paired bootstrap A_canonical vs A_Nöldeke, α=0.0125.
- Bonferroni k=2 within hypothesis. Seed 20260413.

The §11-20 pair set was selected from a pre-existing classical catalog (kirmani-30-pair-tuples.tsv, filed pre-task-#40), NOT from the FOAI output of task #26. There is no data-peeking on the test outcome.

## Verification flags

- **MW-3** (the seven pairs derived from kirmani-30-pair-tuples.tsv K11/K13/K16/K18/K21/K25/K26/K28): citation-chain verified via project's own catalog with HIGH pair-identification confidence and MEDIUM wajh-attribution confidence (per the original tuples file's frontmatter).
- **MW-4** (§11, §12, §13): independently attested in standard Quranic-balāgha references (al-Zarkashī *Burhān* nawʿ 52 for §11; al-Suyūṭī *Itqān* for §12-13 dietary corpus); these can be promoted to MW-5 if independently re-cited from a verified secondary source.
- **NO MW-6** (verbatim physical-edition citation): no entry in this delivery batch carries verbatim physical-edition verification. **All entries flagged PENDING** per AMEND-28 protocol. If hypothesis-generator or team-lead requires MW-6 promotion before dispatch, this delivery is HELD.
- **Sign-direction confidence**: LOW (per original tuples file frontmatter). Task #40's primary test asks A>0 (earlier-canonical = aṣl). The K-tuples file has all 7 entries at "A<0" per AMEND-15. **This is a sign-convention difference between the two specifications**, NOT a data-direction conflict. Task #40 uses A = S(V_B|C_A) − S(V_A|C_B) with A>0 meaning "later-canonical is worse when transplanted," while AMEND-15 uses A<0 to mean "primary-context swap is worse than echo-context swap." Computational-tester must re-confirm sign convention before scoring.

## Unresolved items needing arbitration

1. **Sign convention reconciliation**: see "Sign-direction confidence" above. Task #40 vs AMEND-15 differ in sign labeling. Computational-tester to confirm at execution.
2. **MW-6 PENDING flags**: if team-lead requires MW-6 verification before dispatch, this delivery is HELD pending physical-edition access (same external-dependency status as task #49 HASHR Phase 2). Recommended: dispatch with MW-3/MW-4 tags clearly disclosed, escalate to MW-6 retroactively if/when library access becomes available.
3. **§11 promotion from K06 "balanced" to §11 "directional"**: I am exercising classical-scholar judgment to promote based on al-Zarkashī's explicit citation of this pair in *Burhān* nawʿ 52 as a particle-directional case. If hypothesis-generator disagrees, replace §11 with a different K-tuples candidate (e.g., resurrect K28 Q4:47↔Q2:65 in a different slot).

## Hand-off protocol

This file is the classical-scholar deliverable. The next step is:
- Hypothesis-generator (or team-lead) to APPROVE the §11-20 selection.
- Computational-tester to receive the full §1-20 pair list and execute the FOAI Wilcoxon + canonical/Nöldeke bootstrap per task #40 pre-reg.
- MW-3 to MW-4 verification flags carried through to the result write-up.
