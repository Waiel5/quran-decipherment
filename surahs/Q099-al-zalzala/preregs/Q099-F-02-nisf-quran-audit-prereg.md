---
surah: 99
test_id: Q099-F-02
title: Q 99 = "niṣf al-Qurʾān" (HALF the Qurʾān) classical-claim empirical audit — analog to H-NEW-84
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 7
bonferroni_family: Q099-F-02-nisf-audit
alpha_bon: 0.00714
---

# Q099-F-02 — Pre-registration: Q 99 = "niṣf al-Qurʾān" (HALF) empirical audit

## 1. Hypothesis (locked before observation)

The al-Tirmidhī 2976 + 2977 hadith claim that *idhā zulzilat ʿudilat lahu bi-niṣf al-Qurʾān* — "Q 99 equals HALF the Qurʾān" — is testable as a quantitative-content equivalence claim (parallel to H-NEW-84 Q 112 = 1/3).

**H1 (locked direction):** Q 99 / corpus ratio for at least 3 of 7 axes is in the band [0.45, 0.55] (the literal "HALF" band, ±10% pre-locked tolerance).

**H0:** Q 99 / corpus ratio for fewer than 3 of 7 axes is in [0.45, 0.55].

**Direction:** PRE-LOCKED prediction = REFUTED-STRONG (analog to H-NEW-84 pattern). Per the brief: "Direction: NULL expected by classical-numerology REFUTATION-pattern (cross-finding-015)." This is pre-stated as a NULL expected outcome.

## 2. Operational definition — 7 axes (mirror of H-NEW-84)

| Axis | Operationalization | Q 99 numerator | Corpus denominator | Locked PASS band |
|:--|:--|:--:|:--:|:--:|
| 1 | Letter graphemes (no-tashkeel) | Q 99 letters | corpus letters (330,709) | [0.45, 0.55] |
| 2 | Word tokens (no-tashkeel) | Q 99 words | corpus words (77,797) | [0.45, 0.55] |
| 3 | Shannon information bits | Q 99 H | corpus H | [0.45, 0.55] |
| 4 | Distinct roots covered | Q 99 distinct-roots | corpus distinct-roots (~1,642) | [0.45, 0.55] |
| 5 | Eschatology-dominant verses (al-Ghazālī-schema-analog: keyword schema for eschatological-content) | Q 99 eschat-verses | corpus eschat-verses | [0.45, 0.55] |
| 6 | Eschatology concentration factor (inverse) | 1 / (Q 99 density / corpus density) | (Q 99 density / corpus density) | [0.45, 0.55] for inverse, equivalently density-ratio in [1/0.55, 1/0.45] = [1.82, 2.22] |
| 7 | Divine-names coverage (99 names) | Q 99 distinct-names | 99 | [0.45, 0.55] |

## 3. Test statistic

For each axis: the ratio = numerator / denominator. PASS if in [0.45, 0.55].

**OVERALL VERDICT**:
- **CONFIRMED**: ≥ 5 of 7 axes PASS.
- **PASS-WEAK**: 3-4 of 7 PASS.
- **REFUTED-WEAK**: 1-2 of 7 PASS.
- **REFUTED-STRONG**: 0 of 7 PASS.

## 4. Permutation null (not applicable per H-NEW-84 protocol)

This is a **literal-content-equivalence test**, not a permutation-test. The pre-locked tolerance band [0.45, 0.55] formally tests the literal interpretation of the niṣf-al-Qurʾān claim. Per the H-NEW-84 protocol (which used the same literal-band methodology), permutation-null is not applicable; the test is a direct ratio-comparison against the pre-locked band.

The "permutation null" analog is the CLASSICAL-NUMEROLOGY refutation pattern (cross-finding-015): classical-numerological claims have a strong prior of failing literal-quantitative tests. The pre-locked band specification + ±10% tolerance is the standardized methodology.

## 5. Success / Failure

Per the verdict-criteria above.

## 6. Honest limits known a priori

- This test mirrors H-NEW-84 methodology directly. H-NEW-84 was REFUTED-STRONG (0/7 axes for Q 112 thuluth claim). The expectation per cross-finding-015 is that Q099-F-02 will also be REFUTED-STRONG.
- The Q 99 niṣf claim has a chain-authentication weakness in addition to potential quantitative-content failure (see `04-hadith-corpus.md`). The empirical-content failure (this test) and chain-failure (the hadith-isnad evidence) are TWO INDEPENDENT axes of refutation. Even if quantitative-content surprisingly passed, the chain-authentication weakness would remain.
- The al-Ghazālī-schema-analog (Axis 5: eschatology-dominant verse fraction) requires a pre-locked keyword schema. Locked schema below.
- Direction is pre-locked but EXPLORATORY-on-axis-5: theology-eschatology might be over-represented in Q 99 the way theology-doctrines were over-represented for Q 112 in H-NEW-84.

### Locked eschatology-keyword schema for Axis 5

A verse is **ESCHATOLOGY-DOMINANT** if its content matches at least one of the following keyword categories (locked before observation):
- **Day of Judgment terms**: yawm al-dīn, yawm al-qiyāma, yawmaʾidhin, al-yawm al-ākhir, al-sāʿa.
- **Cosmic-event terms**: zalzala, qāriʿa, ṭāmma, ṣākhkha, ḥāqqa, infiṭār, inshiqāq, takwīr, al-wāqiʿa.
- **Resurrection terms**: baʿth, nushūr, baʿtha, ḥashr, ḥushira.
- **Hell/Paradise terms**: jahannam, al-nār, jaḥīm, al-janna, al-firdaws, al-naʿīm.
- **Reckoning terms**: ḥisāb, al-mīzān, kitāb (in eschatological context only — pre-locked exclusion: kitāb-as-Quran reference).

Operational rule: 5 mufaṣṣal-qiṣār-keyword categories; verse PASSES if matches ≥1 category.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 7 (7 axes tested). α_bon = 0.05/7 = 0.00714 per-axis. Used in axis-by-axis interpretation; overall verdict by axis-count thresholds (≥5 = CONFIRMED).

## 9. Coordination

This is a Q 99-specific classical-claim test. H-NEW-84 (Q 112) is the methodological parent. Future similar tests for Q 109 (rubʿ claim, same chain) and Q 36 already-tested (qalb claim, H-NEW-82) form a coordinated cross-surah classical-fadāʾil-fraction audit family.

## 10. SHA256 lock

Computed at write-time, embedded in `scripts/Q099_F_02_nisf_quran_audit.py`, verified at runtime.
