---
surah: 64
test_id: Q064-F-03
title: Q 64:9 *taghābun* hapax-status — corpus-EXACT root g-b-n attestation count
file_type: pre-registration
date_locked: 2026-05-09
seed: n/a (deterministic count)
n_perm: 0
bonferroni_k: 1
bonferroni_family: Q064-F-03-hapax-status
alpha_bon: 0.05
---

# Q064-F-03 — Pre-registration: *taghābun* root g-b-n hapax-status verification

## 1. Hypothesis (locked before observation)

The eponymous *al-taghābun* in Q 64:9 (*dhālika yawmu al-taghābun* — "that is the day of mutual disillusion") is conspicuous among the 5,236+ root-attestations of the QAC v0.4 corpus root index. Specifically, classical lexicography (al-Rāghib al-Iṣfahānī, *Mufradāt al-Qurʾān*, root g-b-n entry) treats it as a NEAR-HAPAX. Pre-reg formalizes this.

**H1 (locked direction):** The QAC v0.4 root g-b-n (gh-b-n / غ-ب-ن) appears in EXACTLY 1 corpus location (corpus-EXACT-strict-hapax).

**H2 (locked direction):** Q 64:9 is the unique attestation location.

**H3 (locked direction, exploratory):** No other surface-form variant with the literal substring `غبن` (g-b-n root letters in standard order) appears anywhere in the 6,236-verse no-tashkeel corpus, EXCLUDING the canonical Q 64:9 *al-taghābun* token itself.

**H0:** Root g-b-n attests at >1 corpus location.

## 2. Operational definitions

- **QAC root index source**: `data/morphology/root-index.json`, key `gbn` (Buckwalter encoding for غ-ب-ن).
- **Surface-form check**: iterate all word tokens in `quran-text/quran-no-tashkeel.json` and check for substring `غبن`, `غابن`, or `تغابن`.
- **Hapax determination**: H1 PASS if `len(root_index['gbn']) == 1`. H2 PASS if the location is `(64, 9, 7)` (Q 64:9, word #7). H3 PASS if surface-form occurrences = 1 across all 6,236 verses.

## 3. Test statistic

- N_root_locations (count of QAC root-attestations).
- Location coordinates of any attestation.
- N_surface_occurrences (count of surface-form matches).

## 4. Success / Failure

- **CORPUS-EXACT-HAPAX CONFIRMED**: H1 + H2 + H3 all PASS.
- **PARTIAL**: Some pass.
- **REFUTED**: Multiple corpus attestations.

## 5. Honest limits known a priori

- This is a DETERMINISTIC corpus-count, not a permutation test. p-value is irrelevant: either the count is 1 or it isn't.
- The QAC root index (Dukes 2010, v0.4) is the canonical source; classical lexicography is consistent with it but predates it. al-Rāghib's classification of g-b-n as singular-attestation aligns with QAC v0.4 if both PASS.
- **No MW residualization needed**: hapax-counts are length-invariant scalars.
- **No MW-5 positive control needed**: hapax-determination is deterministic.
- The phrase *yawm al-taghābun* (without the article) is not a separate root-attestation; it is a syntactic re-parse of the same surface form. The root-attestation count is the operative metric.

## 6. Rules-tuple

`(no-tashkeel, QAC-v0.4-root-index, basmala-counted-only-in-Q1, Hafs-Kufan)`.

## 7. Bonferroni

k = 1 (single deterministic count). α_bon = 0.05.

## 8. SHA256 lock

Embedded in `scripts/Q064_F_03_taghabun_hapax.py`.
