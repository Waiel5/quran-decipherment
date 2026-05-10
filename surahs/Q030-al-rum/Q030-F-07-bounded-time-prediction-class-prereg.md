---
surah: 30
test_id: Q030-F-07
title: Bounded-time-window prophetic-prediction structural class — corpus-wide enumeration
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perms: not-applicable (deterministic morphological-frame enumeration)
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (single planned pre-registered enumeration; independent replication on a 2nd time-lexeme set required for promotion)
hypothesis_anchor: al-Bāqillānī iʿjāz al-ghayb framing on Q 30:2-5; the bounded-time-window prediction is a rare structural class
---

# Q030-F-07 — Pre-registration: Bounded-time-prediction structural class

## 1. Hypothesis (LOCKED before observation)

**H1:** The structural class **bounded-time-window prophetic-prediction verse** — defined as a single Quranic verse containing BOTH (a) a time-window quantifier lexeme and (b) a future-tense or imminent-action verb form predicting a not-yet-actualized event — has **FEWER THAN 10 attestations corpus-wide**.

This makes Q 30:2-5 (3 of those <10 verses: Q 30:3 carries the future *sa-yaghlibūn*; Q 30:4 carries the bounded window *fī biḍʿi sinīn*; combined-verse-level the predicates anchor at vv 3-4) a member of a corpus-rare structural class.

**H0:** ≥ 10 verses in the corpus contain both (a) bounded-time language and (b) future-tense prediction.

**Direction:** count < 10 (LOCKED).

## 2. Operational definition

### Time-window quantifier lexemes (LOCKED feature-set, drawn from the project's existing time-lexicon)

Set Q (quantifiers + temporal-units):
- Lemma `biDoE` (root `bDE`, "a few" = 3-9 per Tirmidhī #3275)
- Lemma `siniyn` (root `snw`, "years")
- Lemma `sanap` (root `snw`, "year"; feminine singular)
- Lemma `yawom` (root `ywm`, "day") **WHEN modified by a numerical or possessive determiner** (NOT bare *yawm*, which is too common)
- Lemma `Hiyn` (root `Hyn`, "a while; until a time")

The set Q is LOCKED before observation. Lemmas outside Q (e.g., `>aHoqab`, `EaSor`) are excluded from this pre-reg; future pre-regs may extend.

### Future-tense / imminent-action verb forms (LOCKED)

A verb form qualifies as "future / imminent" if it is:
- Imperfect verb (POS:V with imperfect aspect) prefixed by sīn (*sa-*) or *sawfa* — direct future marker.
- Imperfect verb (POS:V) governed by an explicit future-frame in the same verse (e.g., *li-yaqdiyanna*, *layakuwnan*).
- Locked: only imperfect-aspect verbs counted. Perfect-aspect verbs (which can express past-completed actions or general-truths) are EXCLUDED unless paired with an explicit future-tense-marker like *sa-*.

For tractability, we operationalize "future-tense prediction" PRAGMATICALLY as: presence of the prefix `sa-` (the proclitic FUT particle, encoded in QAC as a separate token with `PREFIX|+sa+`) anywhere in the verse. This is an over-inclusive proxy (some *sa-* prefixes attach to non-prediction imperfects), so the verdict is REPORTED CONSERVATIVELY — every match is hand-verified post-run for narrative role.

### Test statistic

Count of corpus verses (s, v) where:
- ≥ 1 token in the verse has a LEM in set Q, AND
- ≥ 1 token in the verse has the FUT proclitic *sa-* attached.

The two conditions need not attach to the same syntactic constituent — only co-occur within the same verse.

## 3. Bonferroni and α

k=1. α_bon = 0.05. No permutation — the count is deterministic.

## 4. Success / Failure

| Count of bounded-time + future-prediction verses corpus-wide | Verdict |
|:-:|:--|
| < 10 | **PASS-DIRECTED** (rare structural class; Q 30:3-4 is a member) |
| 10 – 20 | **DIRECTIONAL** (uncommon but not rare) |
| > 20 | **NULL** (the class is common, not rare) |

## 5. Rules-tuple

`(QAC v0.4 LEM + POS + segment-level prefix tags, hafs-kufan, no-tashkeel, verse-as-unit-of-cooccurrence)`.

## 6. SHA256 lock

Computed at run-time. Embedded in `scripts/Q030_F_07_bounded_time_prediction_class.py`.

## 7. Honest a-priori limits

- The Q-set is curated from Q 30:4 surface form. Including alternate temporal lexemes (e.g., `yawom`, `Eaomr`) would shift the count upward; including only the strict 3-element set `{biDoE, siniyn, sanap, Hiyn}` would shift it downward. The LOCKED 5-lemma set is a reasonable middle-ground.
- The *sa-* prefix proxy for future-tense over-counts (because it captures non-predictive uses like *sa-yaqūlu* "he will say" introducing direct discourse). Hand-verification of each match for narrative-role (does the verse make a NOT-YET-ACTUALIZED claim?) is performed post-enumeration and reported, but DOES NOT alter the pre-registered count.
- The class "bounded-time-window prophetic prediction" is a literary-architectural category that QAC tags alone cannot fully diagnose; the morphological proxy captures only the surface-structural correlate.
- The Q 30:2-5 pericope spans 4 verses; under the verse-as-unit rule it could contribute up to 4 matches (vv 2, 3, 4, 5 each evaluated separately). We report per-verse and aggregate to surah.

## 8. Connection to existing findings

- Q030-F-06 locks the lemma-level rarity of `biDoE`. The present Q030-F-07 extends to the structural class.
- The bounded-time-window prediction class is the empirical correlate of **al-Bāqillānī's iʿjāz al-ghayb** doctrine. If the class is rare corpus-wide (<10 verses), then Q 30:2-5 is membership in a corpus-distinctive structural category — providing an empirical anchor for the classical iʿjāz-al-ghayb claim beyond what Q030-F-02 (lexical hapax) already established.
- A complementary pre-reg would be Q012-F-XX, examining Q 12:42 (Yūsuf prison-time) under the same structural-class probe, since it is the only OTHER `biḍʿ + sinīn` co-occurrence. If both are rare-class members, the *biḍʿ + sinīn* lemma pair becomes a structural-class anchor.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
