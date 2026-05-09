---
surah: 75
test_id: Q075-F-01
title: Corpus-EXACT 4-verse self-meta-revelation passage — Q 75:16-19 as a structural-self-reference monopoly
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q075-F-01-self-meta-revelation
alpha_bon: 0.025
direction: Locked — Q 75:16-19 is the SOLE 4-consecutive-verse procedural-self-reference passage in the corpus
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
---

# Q075-F-01 — Pre-registration: Corpus-EXACT self-meta-revelation passage

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** The Quranic passage Q 75:16-19 is **the only 4-consecutive-verse passage in the entire corpus** in which every verse contains an indicator of "procedural revelation-reception" (defined operationally below).

**H1b (one-tailed, locked direction):** Each of the surface-string components specific to Q 75:16-19 — namely (a) لا تحرك, (b) لتعجل به, (c) علينا جمعه وقرآنه, (d) فإذا قرأناه فاتبع قرآنه, (e) ثم إن علينا بيانه, (f) قرآنه (with attached 3rd-pers. masc. sing. divine-pronoun referring to the Quran's recitation), (g) بيانه (likewise) — is a **corpus-EXACT-uniqueness phrase or hapax**.

**H0 (joint):** Either (i) >1 four-consecutive-verse passage matches the procedural-reception definition, OR (ii) any of the seven Q 75:16-19 component fragments occurs in another surah.

**Direction:** Q 75:16-19 = corpus-MONOPOLY at both the structural (passage-level) and lexical (component-level) layers (LOCKED).

## 2. Operational definition

### Source text
`quran-text/quran-no-tashkeel.json` (rules-tuple default).

### Procedural-reception indicator set (locked before observation)

A verse counts as a "procedural-reception verse" iff it contains at least one lexical token from the locked set:

| Group | Tokens (no-tashkeel) | Semantic role |
|:--|:--|:--|
| qurʾān-attached-pronoun | قرآنه, قرآنا | "its-recitation" / "a-recitation" |
| waḥy/iqraʾ family | يوحى, نوحي, أوحى, نقرأ, قرأناه, قرأنا | revelation/recitation 1st-pl. |
| timing-imperatives | تعجل, تستعجل, تنسى, ترتيلا | timing of reception/transmission |
| memory-gathering | جمعه, نقرئك, لتثبت, فؤادك | memorization mechanism |
| clarification | بيانه, بيناه | divine clarification |
| tongue/lips 2-sing-masc | لسانك, شفتيك | physical organ of recitation |
| imperative-2-sing-masc to Prophet | اتبع, لا تحرك, لا تعجل, ورتل | direct address procedural |

This set is locked PRIOR to corpus enumeration. The indicator set is taken FROM Q 75:16-19 forward (the indicators that empirically fire at Q 75:16-19) but is then stress-tested CORPUS-WIDE so that any other passage where these indicators also chain across 4 consecutive verses would be detected.

### Test statistic — Cell A (passage-level)

- N4_total = number of (surah, start_verse) pairs where the 4 consecutive verses [start_verse, start_verse+1, start_verse+2, start_verse+3] each contain at least one indicator-token.
- Pre-committed prediction: N4_total = 1 (Q 75:16-19 only).

### Test statistic — Cell B (component-level)

For each of the 7 surface-string components (a)-(g) above, count corpus-occurrences:

- count_a = corpus occurrences of "لا تحرك"
- count_b = corpus occurrences of "لتعجل به"
- count_c = corpus occurrences of "علينا جمعه وقرآنه"
- count_d = corpus occurrences of "فإذا قرأناه فاتبع قرآنه"
- count_e = corpus occurrences of "ثم إن علينا بيانه"
- count_f = corpus occurrences of "قرآنه" (token-exact, no-tashkeel)
- count_g = corpus occurrences of "بيانه" (token-exact, no-tashkeel)

Pre-committed prediction: count_a, b, c, d, e, g all = 1; count_f ∈ {1, 2} (the form ـه may attach in a small number of construct-state contexts).

## 3. Permutation null

For Cell A, the pre-registered null is generated as follows:

- Construct 10⁴ shuffled corpora by randomly permuting the 6,236 verse-positions across 114 surah-shapes (preserving each surah's verse-count). This is a STRUCTURE-PRESERVING SHUFFLE that destroys consecutiveness.
- For each shuffled corpus, count N4_shuffled.
- Compare observed N4 = 1 against shuffled-null distribution.

For Cell B, the null is the verse-length-weighted random distribution of fragment-tokens across surahs.

n_perm = 10000, seed = 20260509.

## 4. Success / Failure

- **STRONGLY VINDICATED**: Cell A passes (N4 = 1, observed = predicted) AND Cell B passes (all 7 components match prediction); permutation null p ≤ α_bon = 0.025.
- **VINDICATED**: Cell A passes but one Cell B component differs by ≤1 from prediction.
- **DIRECTIONAL**: Cell A passes but multiple Cell B components miss.
- **NULL**: Cell A fails (N4 > 1).
- **Pre-commit violation**: N4 = 0 (none found, including Q 75:16-19 itself) — would indicate pipeline bug.

## 5. Honest limits known a priori

- The indicator-set is post-hoc-derived FROM Q 75:16-19; the test's value is in the CORPUS-WIDE detection of equivalent passages, NOT in the discovery of Q 75:16-19 itself (which is known a priori).
- Per HANDOFF/04-DISCIPLINE.md "post-hoc-noticed protocol": single-test α=0.05 cap unless extreme p (e.g., < 10⁻⁵) survives any conceivable Bonferroni. The brief explicitly directed audit of this passage as classically debated, so the post-hoc origin is FROM-THE-BRIEF and disclosed.
- Verdict ceiling = STRONGLY VINDICATED is permitted because the test's structure is CORPUS-EXACT-COUNT (not a probabilistic significance test in the usual sense): if N4 = 1, the structural-uniqueness claim is empirically locked.
- Cell B count_f predicted ∈ {1, 2} because قرآنه may also attach in non-Q-75 contexts in principle; observation bound to verify.

## 6. Rules-tuple

`(no-tashkeel, orthographic-token, regex-substring, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 7. Bonferroni

k = 2 (Cell A passage-level, Cell B component-level). α_bon = 0.025.

## 8. Coordination

This is a Q 75-specific structural-self-reference test. No prior Q-specialist has run it. No duplication. Q 75 is the unique target.

## 9. SHA256 lock

Computed at write-time, embedded into `scripts/Q075_F_01_self_meta_revelation.py`, verified at runtime.
