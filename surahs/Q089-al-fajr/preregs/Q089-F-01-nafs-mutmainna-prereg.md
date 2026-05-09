---
surah: 89
test_id: Q089-F-01
title: Q 89:27 *al-nafs al-muṭmaʾinna* corpus-EXACT phrase test + 4-instance soul-classification cohort
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q089-F-01-soul-classification
alpha_bon: 0.025
---

# Q089-F-01 — Pre-registration: *al-nafs al-muṭmaʾinna* corpus-EXACT phrase + soul-classification cohort

## 1. Hypothesis (locked before observation)

The phrase *yā ayyatuhā al-nafs al-muṭmaʾinna* ("O soul at peace") at Q 89:27 is widely cited in classical funerary practice as a foundational soul-rest formula. The Quran lexicon contains a small fixed list of *al-nafs* compound-classifications:

- *al-nafs al-muṭmaʾinna* (the soul at peace) — Q 89:27
- *al-nafs al-lawwāma* (the self-reproaching soul) — Q 75:2
- *al-nafs al-ammāra bi-l-sūʾ* (the soul that commands evil) — Q 12:53
- *al-nafs al-wāḥida* (the single soul) — multiple (Q 4:1, Q 6:98, Q 7:189, Q 31:28, Q 39:6)
- *anfusakum* / pronominal soul-references — non-classifications

**H1 (locked direction)**: Q 89:27 carries the corpus's UNIQUE *al-nafs al-muṭmaʾinna* form: there is exactly **1** corpus-occurrence of this exact 4-token phrase (with definite article + adjective). EXACT-PHRASE-COUNT=1.

**H2 (locked direction)**: among the 3 named-classification *al-nafs* compounds (*muṭmaʾinna* / *lawwāma* / *ammāra bi-l-sūʾ*), each occurs **exactly once** in the corpus (3 distinct terms, 3 distinct surahs); each is corpus-EXACT-1. The 3 surahs that carry these classifications are {Q 12, Q 75, Q 89} — a corpus-EXACT 3-surah classification-triplet.

**H0**: the *al-nafs al-muṭmaʾinna* form appears more than once OR is not corpus-unique to Q 89; the 3-classification cohort overlaps on more than 3 surahs.

## 2. Operational definitions

- **Source**: `data/alt-text/quran-uthmani-consonantal.json` (no-tashkeel, hamza-normalized).
- **H1 phrase-pattern (locked)**: the 4-token sequence *al-nafs al-muṭmaʾinna* is matched as `النفس المطمئنة` with optional preceding *yā ayyatuhā* (vocative). Hamza variants (إ ↔ ا), final-yā variants (ى ↔ ي) normalized.
- **H2 cohort**: the 3 classification phrases are searched independently:
  - *al-nafs al-muṭmaʾinna* → `النفس المطمئنة`
  - *al-nafs al-lawwāma* → `النفس اللوامة`
  - *al-nafs al-ammāra bi-l-sūʾ* → `النفس بالسوء` or `للنفس الأمارة` or full string with hamza-variant tolerance
- Count distinct corpus-occurrences per phrase. The cohort is the SET of distinct surahs containing ≥1 of these.

## 3. Test statistic

- **H1**: integer count of *al-nafs al-muṭmaʾinna* corpus-occurrences. PASS if = 1.
- **H2**: number of distinct surahs containing at least one of the 3 classification phrases. PASS if = 3, AND that set is exactly {Q 12, Q 75, Q 89}.

## 4. Success / Failure

- **CONFIRMED**: H1 PASS (= 1) AND H2 PASS (= {Q 12, Q 75, Q 89}).
- **DIRECTIONAL**: only one of H1/H2 passes.
- **NULL**: neither passes.
- **Pre-commit violation**: count > 1 for H1, OR cohort size ≠ 3 with surahs different from prediction.

## 5. Honest limits known a priori

- Post-hoc origin DISCLOSED: the *al-nafs al-muṭmaʾinna* uniqueness of Q 89:27 was already noted in the task brief (per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed" protocol). Single-test α=0.05 cap applies; verdict ceiling is **PASS-DIRECTED** until INDEPENDENT REPLICATION on a different operationalization.
- The classical *aqsām al-nafs* triadic typology (al-Ghazālī *Iḥyāʾ ʿulūm al-dīn*, Ibn al-Qayyim *al-Rūḥ*) recognizes exactly these three Quranic-classification phrases. The empirical question is whether the textual basis is corpus-EXACT.
- This is an inverse of the "monopoly" pattern: rather than concentration in one surah (like Q037-F-01's salām-monopoly), the prediction is corpus-EXACT-1 per phrase with exactly 3 distinct surahs holding the trio.
- The classification is a corpus-INHERENT taxonomy (the Quran provides a 3-class soul-typology); the empirical-corpus test is whether that taxonomy is materialized as corpus-EXACT-3.

## 6. Rules-tuple

`(no-tashkeel, hamza-normalized, final-yā-normalized, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (H1 phrase-uniqueness; H2 cohort-equality). α_bon = 0.025.

## 8. SHA256 lock

Embedded in `scripts/Q089_F_01_nafs_mutmainna.py`; verified at runtime.
