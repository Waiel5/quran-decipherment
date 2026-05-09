---
surah: 60
test_id: Q060-F-04
title: uswa hasana CORPUS-EXACT 3-instance + Q 33↔Q 60 paired-exemplar architecture
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q060-F-04-uswa-hasana
alpha_bon: 0.025
---

# Q060-F-04 — Pre-registration: *uswa ḥasana* paired-exemplar corpus-architecture

## 1. Hypothesis (locked before observation)

**H1a (corpus-EXACT):** The construct *uswa ḥasana* (Arabic surface-string `أسوة حسنة` / "good example") occurs in **EXACTLY 3 corpus verses**, distributed across **EXACTLY 2 surahs**: Q 33:21 (rasūl Allāh as exemplar) and Q 60:4 + Q 60:6 (Ibrāhīm as exemplar).

**H1b (paired-exemplar architecture):** Q 33:21 and Q 60:6 share a verbatim **≥7-word continuous phrase** (the closing clause *uswa ḥasana liman kāna yarjū Allāha wa-l-yawm al-ākhir*).

**H0 (joint):** Either the construct appears in additional surahs/verses, or Q 33:21 and Q 60:6 do not share the verbatim ≥7-word block.

**Direction (locked):** Both axes EXACT-MATCH the predicted state.

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json`.
- **Pattern (uswa ḥasana)**: regex `أسوة\s+حسنة` (with optional whitespace between the two words).
- **Block-comparison**: longest-common-substring (LCS) algorithm at character level between Q 33:21 text and Q 60:6 text (no diacritics).

## 3. Test statistic

- N_total = total corpus verses with *uswa ḥasana* match.
- For test 1b: char-LCS length and corresponding word-count in shared block.

## 4. Permutation null

The "corpus-EXACT to 3 verses" claim is a state-of-the-corpus discrete fact; not a probabilistic statistic. Documented limit per HONEST-LIMITS-LEDGER:

- For genuinely-EXACT discrete claims, the only meaningful null is the prior probability of co-location: under length-weighted random placement of N=3 occurrences across 6,236 verses, observing all 3 in 2 specific surahs (verse-pool {Q 33, Q 60} = 73 + 13 = 86 verses out of 6,236 = 1.38%) has prior probability ≈ (86/6236)^3 = 2.6×10⁻⁶. Even ignoring within-surah clustering, the empirical pattern is EXTREME relative to length-weighted prior. We report this as a heuristic, not a primary statistical result.

For test 1b: the null model for "shared verbatim block" is a Bernoulli-random-substring null. Under random word-level concatenation, P(any 7-word verbatim match between two specific verses) is small (≈10⁻⁹ for typical 20-word verses with corpus vocabulary). Reported as heuristic; not the primary test.

## 5. Decision rule

- **CORPUS-EXACT (verdict)**: pattern matches predicted 3-instance / 2-surah distribution; verbatim block ≥7 words.
- **PARTIAL**: pattern is corpus-EXACT but verbatim block <7 words.
- **NULL**: pattern occurs at ≥4 verses or ≤2 verses (off-by-one tolerated only for orthographic ambiguity).

## 6. Pre-commit violation handling

If pattern occurs in ≥4 verses or in surahs other than Q 33 + Q 60, file as REVERSED-DIRECTION NULL.

## 7. Rules-tuple

`(no-tashkeel, orthographic-token, regex-fixed-pattern + char-LCS, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 8. Bonferroni

k = 2 (count test + LCS test). α_bon = 0.025.

## 9. Honest limits known a priori

- Single-construct corpus-EXACT test; the empirical interest is uniqueness, not power.
- Q 33:21 = Muhammad-as-exemplar; Q 60:4-6 = Ibrāhīm-as-exemplar. The corpus-architecture interpretation is that the *uswa ḥasana* construct is JOINTLY allocated to two prophets — the eschatological-final prophet (Muhammad) and the proto-monotheist prophet (Ibrāhīm) — and to no others. This is a balāgha-architectural claim verified at the surface level.
- The test is in the same family as H-NEW-1160 (*salāmun ʿalā [PROPHET]* corpus-EXACT-with-Q-37) and H-NEW-1100 (*tanzīl al-kitāb* corpus-EXACT 6-cluster). It joins the typology of corpus-EXACT formula-distributions.

## 10. Coordination

Coordinated with the Q 33 al-Aḥzāb specialist (when dispatched). No duplication: this test queries the corpus-distribution of the formula; a Q 33-specialist test would query Q 33:21's role within Q 33's broader prophet-themed verses.

## 11. SHA256 lock

Computed at completion-time.
