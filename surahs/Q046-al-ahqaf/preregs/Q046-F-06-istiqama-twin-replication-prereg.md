---
prereg_id: Q046-F-06
title: Q 46 ↔ Q 41 *istiqāma* twin replication (Q041-F-01 from Q 46 direction)
date: 2026-05-10
seed: 20260509
locked_at: 2026-05-10T02:00:00Z
status: PRE-REG-LOCKED
---

# Pre-registration: Q046-F-06 — *istiqāma* twin Q 41:30 ↔ Q 46:13 replication

## 1. Hypothesis (direction-locked)

**H1 (direction-locked)**: The classical *istiqāma* twin claim (al-Suyūṭī notes Q 46 ↔ Q 41 as the "istiqāma twin," per Q041-F-01) is empirically lockable as a corpus-singleton-pair: the phrase **قالوا ربنا الله ثم استقاموا** (*qālū rabbu-nā Allāhu thumma istaqāmū*) appears in **exactly 2 loci**: Q 41:30 and Q 46:13.

This is a from-the-Q-46-side replication of Q041-F-01 (which approached from Q 41).

## 2. Null / negation

**H0**: The phrase appears more than 2× OR fewer than 2× OR not at both Q 41:30 and Q 46:13.

## 3. Operationalization

- Source: `quran-text/quran-no-tashkeel.json`.
- Search target: `قالوا ربنا الله ثم استقاموا` (literal).
- Enumerate all loci.

## 4. Direction lock

Pre-committed: **exactly 2 attestations at exactly (Q 41:30, Q 46:13)**.

## 5. Bonferroni

k=3 (Q 46 family). α_corrected = 0.0167. Test is exact.

## 6. Success / failure criteria

- **VINDICATED** (replicates Q041-F-01): observed == expected.
- **NULL_OR_DISCREPANCY**: any disagreement.

## 7. Seed

`20260509`.

## 8. Output

JSON to `csv/Q046-F-06.json`: attestation_loci, expected_loci, replicates_Q041_F_01 (bool), verdict.

## 9. Rationale

Q 41 al-Fuṣṣilat and Q 46 al-Aḥqāf are HM-cluster siblings classically linked by the *istiqāma* twin. The Q041-F-01 specialist verified the pair from Q 41's side; this is the independent replication from Q 46's side, executed by a different specialist with a separate pre-reg. Twin-finding cross-validation is a MW-5 (replication) protection.

## 10. Honest limits

- This is a string-match test; the search assumes consonantal stability across reading traditions.
- If a third locus exists with the phrase, the verdict is NULL (no longer a twin); the pre-commit allows for that honestly.
