---
finding_id: Q027-F-08
title: Solomon-narrative twin pair — Q 27 ↔ Q 34 vs Q 27 ↔ Q 38 (jinn-creatures sub-thematic alignment)
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q027-F-05..F-09
alpha_bon: 0.01
acceptance_window: see §6
---

# Q027-F-08 — Solomon-Narrative Inner Twin Structure

## 0. Origin

The Quran's three extended Solomon narratives are:

| Surah | Verses | Solomon material | Sub-theme |
|:-:|:-:|:-:|:--|
| Q 27 al-Naml | 15–44 (30 vv.) | Bird-informant, throne-of-Sheba (jinn-bringer), pavilion-of-glass | jinn-creatures + bird |
| Q 34 Sabaʾ | 12–14 (3 vv.) | Wind, fountain of brass, jinn-builders, throne-of-Sheba (Sabaʾ) | jinn-creatures |
| Q 38 Ṣād | 30–40 (11 vv.) | Horses, satans/jinn (`mardūd`), wind, satans-divers (`ghawwāṣ`) | horses + jinn-as-builders |

Pre-committed prediction: Q 27 ↔ Q 34 is **lexically/root closer** than Q 27 ↔ Q 38 — because Q 27 + Q 34 share **jinn-as-bringers-of-throne / non-horse-creatures**, whereas Q 38's Solomon material is dominated by horses.

This is a **directional twin-pair** test, classically anchored in al-Biqāʿī's *Naẓm al-Durar* (which discusses Solomon-cycle structural distribution across the Quran) and al-Rāzī's *Mafātīḥ al-ghayb*.

## 1. Hypothesis (locked before observation)

**H1**: D_FR(Q 27, Q 34) < D_FR(Q 27, Q 38) — at the whole-surah QAC-stem-root Fisher-Rao distance level.

**H1.b** (root-set Jaccard, robustness): J_root(Q 27 Solomon-block ∩ Q 34 Solomon-block) > J_root(Q 27 Solomon-block ∩ Q 38 Solomon-block).

**H1.c** (token-string concordance): The number of high-frequency content-tokens shared between the Q 27 Solomon-block (vv. 15-44) and the Q 34 Solomon-block (vv. 12-14) is greater than between the Q 27 Solomon-block and the Q 38 Solomon-block (vv. 30-40), per-verse-normalized.

**H0**: D_FR(Q 27, Q 34) ≥ D_FR(Q 27, Q 38), i.e., Q 38 closer than (or equal to) Q 34.

## 2. Operational definitions

- **D_FR(s_a, s_b)**: Fisher-Rao distance from `h-new-111.json` D-matrix.
- **Solomon-block(s)**:
  - Q 27 Solomon-block = vv. 15-44 (30 verses, the inner Sulaymān-Bilqīs cycle).
  - Q 34 Solomon-block = vv. 12-14 (3 verses, Sulaymān + jinn + throne reveal).
  - Q 38 Solomon-block = vv. 30-40 (11 verses, Sulaymān + horses + winds + satans).
- **J_root(block_a, block_b)** = |QAC-roots(block_a) ∩ QAC-roots(block_b)| / |QAC-roots(block_a) ∪ QAC-roots(block_b)|.
- **token-string concordance**: per-verse-normalized count of tokens (no-tashkeel orthographic) appearing in both blocks. Excludes the 50 most-frequent corpus stop-words (e.g., الله, قال, إن, etc.). Pre-committed stop-list: top-50 token frequencies in the corpus, locked before observation.

## 3. Test statistics

- **stat_a** = D_FR(Q 27, Q 38) − D_FR(Q 27, Q 34). Positive ⇒ Q 34 closer (predicted direction).
- **stat_b** = J_root(Q 27-block, Q 34-block) − J_root(Q 27-block, Q 38-block). Positive ⇒ Q 34 closer.
- **stat_c** = (token-concordance Q 27-block ↔ Q 34-block per Q 34 verse) − (token-concordance Q 27-block ↔ Q 38-block per Q 38 verse). Positive ⇒ Q 34 closer.

## 4. Direction (LOCKED before observation)

- H1: stat_a > 0.
- H1.b: stat_b > 0.
- H1.c: stat_c > 0.

(All three predicted positive, i.e., Q 34 LEXICALLY/ROOT/TOKEN-CLOSER to Q 27 than Q 38 is.)

## 5. Permutation null

For H1 (D_FR difference): the test is deterministic from the FR matrix — no permutation needed. We DO compute a permutation-null over random 3-surah tuples to contextualize: how often does a random surah pair-difference exceed |stat_a| under the null of random selection from the 29-muqaṭṭaʿāt set or the 114-set? This is a SECONDARY test (diagnostic, not primary).

For H1.b and H1.c: deterministic, no probabilistic null.

For an **across-prophets robustness null**: shuffle the assignment of "Q 27" to "either Q 34 or Q 38" 10000 times under random permutation of the 29-set; pre-committed seed 20260507. p_aux = #(stat_a_null ≥ stat_a) / 10000.

## 6. Bonferroni and acceptance

- bonferroni_k = 5 (Q027-F-05..F-09); α_bon = 0.01.
- **Acceptance windows** (LOCKED before observation):
  - **CONFIRMED** = stat_a > 0 AND stat_b > 0 AND stat_c > 0 (all 3 directional). Exact deterministic — no p-value applies; the directional unanimity is the verdict.
  - **DIRECTIONAL** = 2 of 3 stat values positive.
  - **MIXED** = 1 of 3.
  - **NULL** = 0 of 3 (Q 38 closer than Q 34 on majority axes).
  - **PRE-COMMIT VIOLATION** = stat_a < 0 (Q 38 closer at the FR axis).

## 7. Rules-tuple

`(no-tashkeel, orthographic + QAC-stem-roots, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

- FR D-matrix: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-111.json`.
- Roots: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- Verse boundaries: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json` (each verse object has `id`).
- Solomon-block boundaries cited from the project's existing `surahs/Q027-al-naml/00-overview.md` §9 (vv. 15-44).

## 9. Honest a-priori limits

- The block sizes differ massively (30 vs 3 vs 11 verses); the per-verse-normalized concordance partly addresses this; the FR-distance is whole-surah, not block-specific (so block-size differences don't directly affect H1).
- Classical commentary (al-Biqāʿī, al-Rāzī) supports the Q 27 + Q 34 jinn-creatures alignment but does not commit to a quantitative ordering. Our pre-commit is empirical.
- The reverse direction (Q 38 closer than Q 34) would be SURPRISING, since horses are the dominant Q 38 Solomon-motif and absent from Q 27.
- D_FR is a whole-surah measure; it averages over Q 27's non-Solomon content (vv. 1-14, 45-93). The block-Jaccard and token-concordance tests sharpen the Solomon-specific signal.
- 50 stop-words for the token-concordance pre-committed before computation — same list across all three pairwise comparisons.

## 10. Cross-references

- Q027-F-03 (Sulaymān-token concentration in Q 27, CONFIRMED) — F-08 zooms in on the Solomon-block twin-pairing.
- [[Q034-saba]] (if exists) — sister jinn-throne narrative.
- [[Q038-sad]] (if exists) — sister Solomon-horses narrative.
- al-Biqāʿī *Naẓm al-Durar* on Solomon-cycle distribution.
- al-Rāzī *Mafātīḥ al-ghayb* Q 27, Q 34, Q 38 Solomon-pericopes.

## 11. Garden-of-forking-paths log

- The 3-pair test family is locked: only Q 27 ↔ Q 34, Q 27 ↔ Q 38 are compared (not Q 21, Q 2, Q 4, Q 6 — those are catalog-mentions, not extended Solomon narratives). This is a directed thematic-similarity test.
- The Solomon-block boundaries (vv. 15-44, 12-14, 30-40) are taken from classical commentary and the project's existing content-analysis (00-overview.md §9). No post-hoc shifting.
- The 50-most-frequent stop-list is computed from the corpus before observation; this is a one-time corpus-derived constant.
- The directional prediction (Q 34 closer) is anchored in jinn-creatures-shared content and locked before observing the FR matrix values.
