---
surah: 30
test_id: Q030-F-06
title: Lemma *biḍʿ* corpus-uniqueness — only 2 attestations corpus-wide bracketing bounded-time predictions
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perms: not-applicable (deterministic lemma-membership count)
bonferroni_k: 1
alpha_bon: 0.05
verdict_ceiling: PASS-DIRECTED (post-hoc single-test cap; replication queue: distinct rules-tuple under quran-uthmani-consonantal lemma re-tag)
hypothesis_anchor: al-Bāqillānī iʿjāz al-ghayb framing on Q 30:4 *fī biḍʿi sinīn*; al-Tirmidhī #3275 ("al-bidʿ refers to what is from three to nine") — bounded-time-window prediction class
---

# Q030-F-06 — Pre-registration: Lemma *biḍʿ* corpus-uniqueness

## 1. Hypothesis (LOCKED before observation)

**H1:** The QAC v0.4 lemma `biDoE` (the noun meaning "a few, several; specifically 3-to-9" per al-Tirmidhī #3275 transmission of the Prophetic gloss) has **EXACTLY 2 corpus attestations**: Q 12:42 (Yūsuf's prison-time, *fa-labitha fī al-sijni biḍʿa sinīn*) and Q 30:4 (Byzantine prophecy, *fī biḍʿi sinīn*).

**Additional structural claim** (locked): both attestations occur at the SYNTACTIC FRAME `biḍʿ + sinīn` (the noun followed by the lemma `siniyn`, "years"), constituting a corpus-EXACT 2-instance bounded-time-prediction frame.

**H0:** The `biDoE` lemma appears in either 1 or ≥ 3 surahs, OR the syntactic frame `biḍʿ + sinīn` is not present at both attestations.

**Direction:** EXACTLY-2-attestations + EXACTLY-2-surahs + frame-matched at both (LOCKED).

## 2. Operational definition

For lemma `biDoE` (QAC v0.4 LEM tag):
- Total token count corpus-wide via `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Distinct surahs containing the lemma.
- For each attestation: verify the immediately-following lemma is `siniyn` (root `snw`) within the same verse.

**Note on lemma scoping**: The QAC v0.4 lemma set distinguishes `biDoE` (the "few/several" noun, masculine) from `biDa`Eap` (the unrelated "merchandise" noun, feminine — appearing 6× in Q 12 as Yūsuf's brothers' trade-goods). Both share the same triliteral root `bDE` but are distinct lemmas. This pre-reg locks to the `biDoE` lemma specifically — the bounded-time-quantifier sense.

**Test statistic**: 3-cell tuple `(n_token, n_surah, frame_match_count)` compared against the locked target `(2, 2, 2)`.

## 3. Bonferroni and α

k=1 (single deterministic lemma-membership probe). α_bon = α_single = 0.05. No permutation applied — the test is a deterministic lookup.

## 4. Success / Failure

| Outcome | Verdict |
|:--|:--|
| `(n_token=2, n_surah=2, frame_match=2)` AND surah-set = {12, 30} | **PASS-DIRECTED** (corpus-EXACT bounded-time-prediction frame) |
| `(n_token=2, n_surah=2)` but frame_match ≠ 2 | **PARTIAL** (lexeme corpus-EXACT but frame divergent) |
| `(n_token ≠ 2)` OR `(n_surah ≠ 2)` | **NULL** (pre-registered count wrong) |

## 5. Rules-tuple

`(QAC v0.4 LEM tags, hafs-kufan, no-tashkeel, lemma-token-counts, syntactic-adjacency at within-verse-word-index level)`.

## 6. SHA256 lock

Computed at run-time. Embedded in `scripts/Q030_F_06_bidc_corpus_uniqueness.py` and verified by `verify_sha()` before any computation.

## 7. Honest a-priori limits

- The pre-registered count `(2, 2, 2)` derives from a memory-claim about the lemma's rarity in the corpus. If the actual count differs, the NULL verdict obtains and is reported with equal prominence per protocol §1.3.
- The QAC lemma distinction between `biDoE` and `biDa`Eap` is annotator-dependent; under a coarser-grain ROOT-only test (root `bDE`), the count would be higher (≈ 8 tokens). This pre-reg locks to LEM-level precision.
- The Tirmidhī #3275 gloss (*al-bidʿ min thalāth ilā tisʿ*) is the classical lexical anchor: the Prophet himself defined *biḍʿ* as a 3-to-9 range. The verse Q 30:4 thus carries a bounded-time-prediction with classical-attested numerical interpretation.
- The frame `biḍʿ + sinīn` claim is testable directly from the QAC location-tuple `(s:v:w:t)` of the two `biDoE` attestations + the lemma of `(s:v:w+1:1)`.

## 8. Connection to existing findings

- **Q030-F-02** already established that `biDoE` is near-hapax (2 surahs). This test sharpens the claim to a corpus-EXACT count + frame-match.
- **Iʿjāz al-ghayb classical doctrine**: the Q 30:2-5 prophecy's specificity rests on (a) the prediction direction (defeat → victory) and (b) the bounded time-window (*biḍʿi sinīn* = 3-9 years). Both anchors are corpus-rare-to-unique at the lemma level. The corpus only places this exact lemma at TWO sites — both of which are bounded-time predictions about future events:
  - Q 12:42 — Yūsuf's prediction to his cellmate that he would remain in prison "a few years" (came to pass).
  - Q 30:4 — the Roman victory prediction "in a few years" (came to pass per classical sīra).
- **Cross-finding-008 muqaṭṭāʿat exception**: Q 30's exception-status is partly compensated by this unique lexical anchor of bounded-time prophecy.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
