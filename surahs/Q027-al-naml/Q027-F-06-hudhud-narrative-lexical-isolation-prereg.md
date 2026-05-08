---
finding_id: Q027-F-06
title: Hud-hud-bird-narrative lexical isolation (Q 27:20-28); hapax inventory of bird-informant cycle
date_preregistered: 2026-05-07
phase: B+
seed: 20260507
bonferroni_k: 5
bonferroni_family: Q027-F-05..F-09
alpha_bon: 0.01
acceptance_window: see §6
---

# Q027-F-06 — Hud-hud-Bird-Narrative Lexical Isolation

## 0. Origin

Q 27:20-28 is the only Quranic narrative in which a **bird acts as messenger/informant** between a prophet and a foreign sovereign. Classical commentary (al-Ṭabarī, al-Rāzī, Ibn Kathīr) treats the *al-hudhud* episode as the textual hinge of the Solomon-Sheba cycle. F-06 tests whether this 9-verse block carries an empirically distinctive lexical signature relative to (a) the rest of Q 27 and (b) the rest of the corpus, with explicit hapax inventory.

This is a NEW test, distinct from Q027-F-01 (naml-concentration) and Q027-F-03 (Sulaymān-concentration). F-06 targets a **specific 9-verse narrative-block** rather than a name-concentration measure.

## 1. Hypothesis (locked before observation)

**H1.a — hapax count**: The orthographic-exact tokens `الهدهد`, `عرشها`, `الصرح`, `صرح` appear in Q 27:20-28 (or the broader Solomon-Sheba block Q 27:15-44 for `الصرح` v.44) and are corpus-wide hapaxes (count = 1) or near-hapaxes (count ≤ 2 with all attestations in Q 27). Pre-committed prediction: **≥ 2 hapaxes** in the bird-informant block.

**H1.b — block-vs-rest-of-Q-27 lexical distinctiveness**: The 9-verse block [Q 27:20..28] has lower Jaccard root-set similarity to (Q 27 minus block) than the median 9-verse block of Q 27 has to its complement. Direction: one-sided lower-tail.

**H1.c — comparison to Q 12 wolf-reference**: Q 12:13-17 (the wolf in Yūsuf's narrative — `الذئب` "the wolf" mentioned 3× in Q 12:13, 14, 17) is the cross-comparator — Quran's other prominent animal-actor scene. We compute the corpus-wide attestation count of the Q 12 wolf-block lexicon vs the Q 27 hud-hud-block lexicon. Pre-committed prediction: **Q 27 hud-hud block has MORE hapaxes than Q 12 wolf block** (because the hud-hud block introduces multiple novel narrative entities — bird-as-messenger, throne-of-Sheba, glass-pavilion — vs the wolf which is a generic Arabic noun).

**H0.a**: < 2 hapaxes in the hud-hud block.
**H0.b**: hud-hud block at-or-above median Jaccard similarity to Q 27 minus block.
**H0.c**: Q 12 wolf block has ≥ Q 27 hud-hud block hapaxes.

## 2. Operational definitions

- **Hud-hud block** = Q 27:20–28 (9 verses); reported reading: Solomon's discovery of the missing hoopoe + hoopoe's report of Sheba's queen + dispatch of Solomon's letter.
- **Wolf block (Q 12)** = Q 12:13–17 (5 verses); the brothers' deception with the false wolf-attack story.
- **Solomon-Sheba broader block** = Q 27:15–44 (30 verses), used for `الصرح` (v.44 — pavilion-of-glass).
- **Hapax-in-Q27** = a token appearing in Q 27 with corpus-wide count = 1.
- **Hapax-in-block** = a token appearing in the hud-hud block with corpus-wide count = 1.
- **Block lexical distinctiveness Jaccard**: Jaccard(root-set(block), root-set(Q 27 minus block)).
- **Block-vs-rest-of-Q-27 baseline**: median over all contiguous 9-verse blocks of Q 27 of Jaccard(root-set(block), root-set(Q 27 minus block)).
- **Tokens of interest** (pre-committed list):
  - From hud-hud block (Q 27:20–28): `الهدهد`, `عرشها`, `الخبء`, `سبإ`, `بنبإ`, `لأذبحنه`, `لأعذبنه`, `الصرح` (within v.44), `بكتابي`.
  - From Q 12 wolf block: `الذئب`, `يأكله`.
  - These are the LOCKED candidate hapax-screening lists (no post-hoc additions).

## 3. Test statistics

- **stat_a** = number of locked tokens from the hud-hud block list with corpus-wide count == 1.
- **stat_b_jacc** = Jaccard(root-set([Q 27:20..28]), root-set(Q 27 minus those verses)).
- **stat_b_pct** = percentile rank of stat_b_jacc among all 9-verse blocks of Q 27.
- **stat_c** = stat_a − (#hapaxes in Q 12 wolf block from the wolf-block locked list).

## 4. Direction (LOCKED before observation)

- H1.a: stat_a ≥ 2.
- H1.b: stat_b_pct ≤ 50 (lower-tail; block is more distinctive than Q 27 median 9-block).
- H1.c: stat_c > 0 (hud-hud block has strictly more hapaxes than Q 12 wolf block).

## 5. Permutation null

H1.b uses the empirical distribution of all 9-verse contiguous blocks of Q 27 (Q 27 has 93 verses → 85 blocks). Direct percentile rank — no further permutation needed for H1.b.

For H1.a and H1.c — deterministic counts. No probabilistic null.

For sanity-check power: an OPTIONAL null for H1.a (block-hapax-count under random 9-verse blocks of Q 27) — seed 20260507; 10000 random 9-verse blocks of Q 27; null distribution of (# tokens in block with corpus-wide count == 1).

## 6. Bonferroni and acceptance

- bonferroni_k = 5; α_bon = 0.01.
- **Acceptance windows** (LOCKED before observation):
  - **CONFIRMED** = H1.a AND H1.b AND H1.c all PASS.
  - **DIRECTIONAL** = 2 of 3 PASS.
  - **MIXED** = 1 of 3 PASS.
  - **NULL** = 0 of 3 PASS.

## 7. Rules-tuple

- H1.a, H1.c: `(no-tashkeel, orthographic-exact-match, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.
- H1.b: `(no-tashkeel, QAC-stem-roots, QAC v0.4, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Anti-hallucination

- Corpus: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Roots: `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`.
- Tafsir Q 12 wolf-block: `/Users/grey/Downloads/quran/surahs/Q012-yusuf/02-content-analysis.md` (already on disk).

## 9. Honest a-priori limits

- The locked token list is short (9 tokens for hud-hud block + 2 for wolf block); a longer list might surface more hapaxes. We deliberately constrain to a small a-priori list to avoid garden-of-forking-paths after observation.
- `الذئب` "the wolf" is a known Arabic noun appearing in Q 12 only — it IS a corpus-wide hapax. So Q 12 wolf block's hapax count is at least 1 (locked-before-observation: this is a known fact, since `ذئب` is not common in classical Arabic narrative outside the Yūsuf story).
- The 9-verse block size matches the empirical block (Q 27:20–28); the comparison to Q 12 uses 5 verses (v.13–17). Block sizes differ; we report stat_a (raw counts) and a length-normalized version (hapaxes per verse) as a sensitivity.
- Jaccard on root-sets is a coarse metric; alternative cosine-on-TF would shift values modestly.

## 10. Cross-references

- Q027-F-01 (naml concentration) — sister fact; F-06 expands to other hapax-fauna lexicon.
- [[Q012-yusuf/06-novel-findings]] — comparator surah.
- [[h-new-NEW-321]] — Q 1 ↔ Q 27 cross-finding (no relation to hud-hud-block).

## 11. Garden-of-forking-paths log

- Token list locked before observation; 9 + 2 entries.
- Block size 9 verses for Q 27 fixed by the bird-narrative scope.
- Hapax-vs-near-hapax distinction: count == 1 is hapax; count ≤ 2 with both in Q 27 is near-hapax. Reported separately.
- Wolf-block comparator chosen because it is the **only other prominent Quranic animal-as-narrative-actor** scene; this is a categorical, not gradient, comparison choice — locked.
