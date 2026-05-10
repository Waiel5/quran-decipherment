---
surah: 29
test_id: Q029-F-03
title: *ʿankabūt* (spider) corpus-uniqueness — lemma + root + token-count across the 6,236-verse Quran
file_type: pre-registration
date_locked: 2026-05-10
seed: 20260509
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (single pre-registered test; corpus-singleton is a deterministic dictionary fact, not a probabilistic null — verdict is a structural-uniqueness verification)
hypothesis_anchor: al-Rāzī (*Mafātīḥ al-ghayb* on Q 29:41) — spider-parable as paradigmatic and corpus-distinctive *mathal*; al-Biqāʿī (*Naẓm al-durar*) — Q 29 semantically eponymous via the spider parable; tradition that the surah-name derives FROM the parable, not vice-versa.
direction_of_effect: corpus-SINGLETON or near-singleton (LOCKED): the *ʿankabūt* lemma + its root *Enkb* appear in exactly ONE surah of the Quran (Q 29) and at exactly ONE verse (Q 29:41).
origin: SESSION-HANDOFF-2026-05-09-PM specialist brief — Q 29 deep-dive T2.
rules_tuple:
  orthography: no-tashkeel
  word_definition: QAC v0.4 LEM-tag (lemma) AND ROOT-tag (root) — both axes
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  detection_rule: scan QAC v0.4 morphology for LEM:Eankabuwt and ROOT:Enkb across all 6,236 verses
  null_model: deterministic dictionary verification (no permutation needed); the corpus-singleton claim is a count-fact, verified by exhaustive QAC scan
---

# Q029-F-03 — Pre-registration: *ʿankabūt* corpus-uniqueness verification

## 1. Hypothesis (LOCKED before observation)

**H1**: The lemma *Eankabuwt* (LEM-tag in QAC v0.4 = "Eankabuwt"; English: "spider") appears in EXACTLY ONE surah of the Quran — Q 29 — and at EXACTLY ONE verse — Q 29:41. By extension, the root *Enkb* (ROOT-tag in QAC v0.4) is also corpus-confined to Q 29:41.

**H0**: The lemma *Eankabuwt* or root *Enkb* appears in more than one surah (i.e., is NOT corpus-singleton at the surah level).

**Direction (LOCKED):** corpus-singleton (1 surah, 1 verse).

## 2. Operational definition

For each of the two axes:
1. **Lemma axis**: scan QAC v0.4 `data/morphology/quranic-corpus-morphology-0.4.txt` for any morphological segment with `LEM:Eankabuwt`. Return list of (surah, verse, word, segment) attestations; collapse to distinct surahs and distinct verses.
2. **Root axis**: same, with `ROOT:Enkb`.

For comparison-anchor with other animal-parable lemmas in the Quran (T3-style comparator, but a strict subset of T2 for context):
- `LEM:n~aHol` (bee), Q 16:68 — comparison
- `LEM:namolap` (an ant), Q 27:18 — comparison
- `LEM:*ubaAb` (fly), Q 22:73 — comparison

The comparison is descriptive and supports interpretation; the primary verdict depends only on the *Eankabuwt* singleton claim.

## 3. Decision rule (locked)

| Outcome | Verdict |
|:--|:--|
| Eankabuwt lemma appears in EXACTLY 1 surah AND exactly 1 verse | **PASS-DIRECTED — corpus-singleton** |
| Eankabuwt lemma appears in EXACTLY 1 surah but ≥ 2 verses | **PASS-DIRECTED — surah-singleton, verse-near-singleton** |
| Eankabuwt lemma appears in ≥ 2 surahs | **NULL (pre-commit violated)** |

Bonferroni k=1 (single primary lemma); the comparison lemmas are descriptive, not part of the test family.

## 4. Why this is a "deterministic" rather than "probabilistic" test

The corpus-singleton claim is a count-fact about the 6,236-verse Quran. There is no permutation null because there is no random-resampling that bears on the fact "*Eankabuwt* appears in surah X and only surah X." The test is therefore a fact-verification with a pre-registered direction, not a hypothesis-test. The pre-registration ensures that:

1. The CLAIM (corpus-singleton) is locked before exhaustive QAC scan.
2. The DIRECTION (singleton) is locked.
3. The COMPARATORS (bee, ant, fly) are locked.

If the QAC scan returns ≥ 2 surahs, the pre-committed claim is FALSIFIED — published as NULL with prominence.

## 5. Pre-committed context for comparison

al-Rāzī (*Mafātīḥ al-ghayb* on Q 29:41) reads the spider-parable as paradigmatic of *mathal* whose vehicle and tenor are tightly bound. al-Bāqillānī's *iʿjāz al-tashbīh* doctrine (the inimitability of similitude) is empirically supported when the vehicle-lemma is corpus-distinctive — a unique-attestation lemma is a special case of vehicle-distinctiveness.

If T2 PASSES with corpus-singleton verdict, this empirically supports the classical reading that the spider-parable is a uniquely-marked rhetorical device in the Quran. If it FAILS (lemma appears in another surah), the parable is recurrence-typical and the classical singleness-claim is false.

## 6. Rules-tuple

`(QAC v0.4 LEM-tag + ROOT-tag, no-tashkeel, Hafs-Kufan, Mashriqi, basmala-counted-only-in-Q1)`.

## 7. Connection to Q029-F-01

Q029-F-01 (previous pre-reg, 2026-05-07) tested a 5-lemma hapax-count for the Q 29:41 surface verse and found 2 corpus-hapax lemmas (Eankabuwt + >awohan). Q029-F-03 is the dedicated SINGLE-LEMMA test for *Eankabuwt* corpus-uniqueness, with the comparison anchor at other animal-parable verses (which Q029-F-01 did not formally test).

T2 and Q029-F-01 are NOT independent (they share the *Eankabuwt* observation), but the framing differs: Q029-F-01 is a multi-lemma hapax-COUNT; Q029-F-03 is the formal corpus-singleton VERIFICATION of the eponymous lemma alone.

## 8. SHA256 lock

Computed at run-time. Embedded in `scripts/Q029_F_03_ankabut_corpus_singleton.py`. Verified before computation.

## 9. Honest a-priori limits

- "Corpus-singleton" depends on QAC v0.4 lemma-tagging conventions. If a future tagging update splits or merges the lemma, the verdict may shift. The verdict is locked to QAC v0.4.
- "Corpus-singleton" at lemma-level does not entail singleton at the SEMANTIC level — "spider" in the Quran is referenced ONLY via this lemma, so the two coincide here. (No alternative Arabic synonyms for "spider" appear elsewhere.)
- The Cave-of-Thawr tradition (a spider's web allegedly protecting the Prophet at the Hijra) is a sīra-tradition, NOT a Quranic reference — does not bear on this test.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
