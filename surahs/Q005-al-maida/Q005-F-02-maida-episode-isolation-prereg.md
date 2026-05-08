---
finding_id: Q005-F-02
prereg_date: 2026-05-07
prereg_type: lexical-isolation hapax test
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q005 deep-dive (F-01..F-05)
alpha_bon: 0.01
rules_tuple: "(no-tashkeel, QAC-LEMMA tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi)"
---

# Q005-F-02 — al-Māʾida episode (Q 5:112-115) lexical isolation

## 1. Background

Q 5:112-115 narrates a *table-from-heaven* miracle requested by the disciples (al-ḥawāriyyūn) of ʿĪsā b. Maryam — a story with no analogue elsewhere in the Quran and traceable to extracanonical Christian tradition (ʿActs of John–style or *Kitāb al-Hāwī* fragments cited by al-Thaʿlabī in *al-Kashf wa-l-bayān*). Classical mufassirūn (Ibn Kathīr at Q 5:114; al-Ṭabarī at Q 5:112-115; al-Qurṭubī at Q 5:114) all agree the surah is named after this māʾida.

Empirical question: how isolated is the māʾida-episode vocabulary at the corpus level? In particular: (a) is the lemma `maA^}idap` a corpus-hapax in lemma-attestation; (b) does Q 5:112-115 contain ≥ 2 corpus-hapax lemmas?

## 2. Frozen lemma family

| Lemma | Token form |
|:--|:--|
| māʾida | `maA^}idap` |
| ḥawāriyyūn | `HawaAriy~uwn` |
| akma (blind-from-birth, Q 5:110) | `>akomah` |
| abraṣ (leper, Q 5:110) | `>aborS` (token form `>aboraS`) |

(salām is excluded because it has many corpus attestations and is not a Q 5:112-115 distinctive marker; tahli is similarly broad. We restrict to lemmas that are confined to / sharply concentrated in the Q 5 ʿĪsā-narrative.)

## 3. Hypothesis (DIRECTION-LOCKED)

**H1 (primary)**: At least 2 of {māʾida, ḥawāriyyūn, akma, abraṣ} are *corpus-hapax* lemmas — i.e., attested in EXACTLY ONE surah, that surah being Q 5.

**H2 (secondary, descriptive)**: All 4 markers above either have ALL their attestations in Q 5 OR are restricted to ≤ 2 surahs corpus-wide.

## 4. Null

**H0**: < 2 of these markers are corpus-hapax lemmas.

## 5. Method

1. For each lemma in the family, query the QAC v0.4 lemma index for surah-level attestation.
2. Mark "corpus-hapax" iff the lemma's surah-set has cardinality 1 AND that surah is Q 5.
3. Tally the count.
4. Permutation null: 10000 random 4-lemma samples drawn from the global QAC v0.4 lemma inventory weighted by attestation count; the empirical p-value is the fraction of random 4-lemma samples in which ≥ 2 lemmas are corpus-hapax with all attestations in Q 5.

## 6. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| ≥ 2 corpus-hapax in family AND p_perm < α_bon = 0.01 | VINDICATED corpus-unique māʾida narrative |
| ≥ 2 corpus-hapax but p_perm ≥ α_bon | DIRECTIONAL |
| < 2 corpus-hapax | NULL |

## 7. Garden-of-forking-paths log

- Lemma family frozen BEFORE running. The `maA^}idap` lemma form was confirmed via QAC scan: 2 attestations, both in Q 5 (verses 112, 114 by direct text inspection of `quran-no-tashkeel.json`; lemma-form has no other surah).
- The other 3 lemmas (ḥawāriyyūn, akma, abraṣ) were chosen because they appear in the Q 5:110-114 narrative cluster and are uncommon in Quranic vocabulary (eyeball pre-flight: ḥawāriyyūn appears in Q 3, Q 5, Q 61 only).
- Note: ḥawāriyyūn will likely NOT be a corpus-hapax (Q 3 and Q 61 attest), so the H1 success path requires at least 2 of the remaining 3.

## 8. Pre-commit locked.
