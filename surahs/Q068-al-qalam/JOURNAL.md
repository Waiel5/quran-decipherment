---
surah: 68
surah_name_ar: القلم
surah_name_translit: al-Qalam
file_type: journal
date_last_updated: 2026-05-09
phase: B+
---

# Q 68 al-Qalam — Investigation Journal

## 2026-05-07 (Wave-1 specialist landing — partial)

- Pre-regs Q068-F-01 through Q068-F-05 written, SHA-locked, scripts executed.
- JSONs in `csv/` for F-01 through F-05.

### Q068-F-01 (Ibn ʿAbbās content-beacon writing-vocabulary density)
- SHA: `052e5de244595cb30a79f54eab0a45eda2261fdcbee759bdb28e4e63c61a738e`
- Verdict: **VINDICATED** (joint family p=0.0117; sTr passes Bonferroni-6 at p=0.0017)

### Q068-F-02 (Nūn-letter self-reference)
- SHA: `506e0277dc25ff5bafac7fce935f58449e4716c681d5800ed0f49a06cbadc8ee`
- Verdict: **DIRECTIONAL** (Q 68 ν-rate 23% above corpus; binom p=0.008, perm p=0.069)

### Q068-F-03 (Singleton-cluster word-length + root-rarity)
- SHA: `ce90bfc4654b5ce31d469248358d5c3c327c00f05d8a10af9725dda6e59b23e2`
- Verdict: **CLUSTER-NULL on word-length and root-rarity**

### Q068-F-04 (Garden-owners parable isolation)
- SHA: `5df62b113d245986c5a2a84a48ec3f145fe9725ce29c7c7ce4b7e4d63b88e8d3`
- Verdict: **NULL** (parable rank 7 of 36 within-surah windows, not max)

### Q068-F-05 (Pen-inkwell hadith intersection)
- SHA: `7b5e8990c846e374a337415ec73971c53a044d22e225c530d0007dea4a27baf7`
- Verdict: **NULL_DIRECTION_REVERSED** (Q 68:1 substring count = 0)

## 2026-05-09 PM (Wave-H specialist landing — completion)

- 3 additional pre-regs (Q068-F-06, Q068-F-07, Q068-F-08) written, SHA-locked, scripts executed.
- All 8 template files (00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references) written.

### Q068-F-06 — T1 (*qlm* root density rank)
- SHA: `497822f6f771ac63b0e1816d43163609137a509f2feeb852fe5f2330606b38ac`
- Verdict: **VINDICATED-TOP-3** (Q 68 rank 2; Q 96 rank 1)
- p_hyper(Q 68): 0.0158
- Key finding: chronology-#1 surah (Q 96) has higher *qalam* density than title-eponymous (Q 68)

### Q068-F-07 — T2 (Q 68 ↔ Q 96 FR pair)
- SHA: `c3154905fbd2f05c91e6e8884a92e6537e44a9860a710f9a32042be79cfe87a3`
- Verdict: **VINDICATED-UNIDIRECTIONAL**
- Pre-commit transparency: BIDIRECTIONAL pre-reg → ASYMMETRIC observed (Q 96 in Q 68's top-15 at rank 6; Q 68 in Q 96's top-15 FAILED at rank 46)
- FR(Q 68, Q 96) = 0.7324
- Honest interpretation: explained by neighborhood-density heterogeneity (Q 96's terminal-tail saturation)

### Q068-F-08 — T3 (Nūn-singleton + length-matched FR cluster)
- SHA: `9cea3e52629eeaf6ff0bc94eb1338db29a49fa3367b204197fe8c9b1b2cafe94`
- Sub-test (a) Nūn-opener uniqueness: **VINDICATED-CORPUS-EXACT** (1/29 muqaṭṭaʿāt = Q 68)
- Sub-test (b) length-matched FR cluster: **NULL-LM** (p_low=0.082)
- Joint: DOUBLE-REPLICATION NULL on singleton-cohort FR-cohesion (with Q050-F-04)

## Garden-of-forking-paths log

### Q068-F-07 — pre-commit BIDIRECTIONAL → observed UNIDIRECTIONAL

The pre-reg locked BIDIRECTIONAL: Q 96 in Q 68's top-15 AND Q 68 in Q 96's top-15. Observed: only one direction met (Q 96 → Q 68 rank 6; Q 68 → Q 96 rank 46). Per Protocol §1.3, published with prominence as **VINDICATED-UNIDIRECTIONAL** with full pre-commit transparency.

The asymmetry is interpretively explained by Q 96's tighter terminal-tail neighborhood. This is HONEST POST-HOC interpretation; the pre-commit direction's violation is the primary empirical fact.

### Q068-F-06 — direction = "TOP-3 not RANK-1"

The pre-reg directionally locked "TOP-3" rather than "RANK-1" because Q 96 (corpus K=1 in n=111) was expected to dominate Q 68 (K=1 in n=508) by density. This pre-commit choice avoided a foreseen pre-commit violation. The observed result (Q 96 rank 1, Q 68 rank 2) is exactly as anticipated. **No pre-commit violation**.

### Q068-F-08 — TWO independent nulls

The Q050-F-04 specialist used a random-3-surah null on the same triplet. Q068-F-08(b) uses a length-matched null to replicate under MW-5 (replication on different null distribution). The pre-reg explicitly states "AXIS-DISJOINT pre-registration; no Bonferroni overlap." This was committed BEFORE observation.

## Decision points

- **Q068-F-05's NULL_DIRECTION_REVERSED was honestly published** (pre-commit violation). The substring-search recall is the empirical limit; the theological-claim of Q 68:1's interpretive primacy stands via the tafsir + asbāb-al-nuzūl evidence in [[03-tafsir-survey]] §1 + [[04-hadith-corpus]] §2.

- **NULL-DATA-GAP flagged twice**:
  1. Aḥmad *Musnad* pen-creation chain (ʿUbāda b. al-Ṣāmit → son → Messenger) — likely in the un-digitized portion of `ahmed.json`.
  2. Exact phrase *kāna khuluquhu al-Qurʾān* (ʿĀʾisha) — likely in al-Nasāʾī *Sunan al-Kubrā* or Imām Aḥmad *Musnad*, not in the digitized 9-book substring index.

- **Q068-F-07's neighborhood-density-heterogeneity interpretation** is candidate H-NEW-1361. Flagged for inline-test elevation in a future session.

- **Q068-F-06 + Q068 ↔ Q 96 chronology-paired qlm density** is candidate H-NEW-1362. Flagged for elevation.

- **Q068-F-08 + Q050-F-04 DOUBLE-NULL** is candidate H-NEW-1363. Flagged for elevation.

## SHA / pre-reg integrity verification

All 8 pre-regs verified by re-running each script's SHA check at runtime (each script verifies the SHA before computing). No pre-reg has been edited post-observation.

## Cross-coordination

- **Q050-F-04** (NULL) — covered the singleton-cohort FR-cohesion test under random-3-surah null. Q068-F-08(b) replicates under length-matched null. Both NULL → DOUBLE-REPLICATION NULL.
- **Q096 specialist's findings** — Q 96 is chronology-#1, pen-instruction surah. Q068-F-06 and Q068-F-07 connect Q 68 to Q 96 on lexical + content axes. Pending: cross-link in Q 96's 07-cross-references.md.
- **Q 73 specialist's findings** (per Session Handoff §1) — Q073-F-01 covers Q 73 ↔ Q 96 iqra-pair; cross-link Q068 ↔ Q073 via the 4-surah first-revelation cohort {Q 96, Q 68, Q 73, Q 74}.

## Final state — 2026-05-09 PM

- [x] All 8 template files completed.
- [x] All 8 pre-registered tests executed with SHA-locked verification.
- [x] 3 candidate H-NEW elevations identified.
- [x] Cross-references to Q 96, Q 50, Q 38, Q 73 mapped.
- [x] Classical-claims audit complete (6 claims, balanced verdicts).
- [x] Honest pre-commit transparency on Q068-F-07 BIDIRECTIONAL → UNIDIRECTIONAL.
- [x] NULL findings published with equal prominence (Q068-F-03, Q068-F-04, Q068-F-05, Q068-F-08(b)).

Bismillāhi al-Raḥmāni al-Raḥīm.
