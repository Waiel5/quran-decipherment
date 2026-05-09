---
surah: 73
test_id: Q073-F-01
title: Q 73:20 ↔ Q 96:1+3 IMPV-qrA prophetic-revelation pair — verse-twin test
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
bonferroni_k: 2
bonferroni_family: Q073-F-01-iqra-pair
alpha_bon: 0.025
---

# Q073-F-01 — Pre-registration: Q 73:20 ↔ Q 96:1+3 IMPV-qrA prophetic-revelation pair (verse-twin test)

## 1. Hypothesis (locked before observation)

**H1a (one-tailed, locked direction):** The pair-of-verses {Q 73:20, Q 96:1, Q 96:3} — i.e. the 3 verses that contain the corpus's IMPV-qrA segments classified as the "prophetic-revelation pair" per H-NEW-1300 — exhibit elevated co-occurrence of *iqraʾ* + *qurʾān*-or-*kitāb* + an addressee-marker (a 2-person pronominal suffix or vocative form), relative to a length-and-position-matched permutation null over verse-pairs.

**H1b (one-tailed, locked direction):** The H-NEW-66-style verse-twin similarity score between Q 73:20 and Q 96:1+3 (treated as a 3-verse cluster, with the pair-comparison computed as max-similarity over the 2 cross-pairs Q 73:20↔Q 96:1 and Q 73:20↔Q 96:3) is in the **top 5%** of all Q 73:20 ↔ {arbitrary surah-N verse} pair similarities.

**H0 (joint):** The lexical co-occurrence is no greater than null AND the cross-pair similarity is below the 95th percentile.

**Direction:** elevated co-occurrence + elevated similarity (LOCKED).

## 2. Operational definition

- **Source text**: `quran-text/quran-no-tashkeel.json` (default rules-tuple).
- **IMPV-qrA reference inventory**: from H-NEW-1300, the 6 corpus IMPV-qrA segments are at Q 17:14, Q 69:19, Q 73:20×2 (words 26 & 49), Q 96:1, Q 96:3. The pair is operationalized as the **3 verses** {Q 73:20, Q 96:1, Q 96:3} per the brief.
- **Co-occurrence test (H1a)**: count the joint occurrence of the 3 token-classes in each test verse:
  - Class A (IMPV-qrA): the literal grapheme-string `اقرء` or `اقرأ` (with optional fa-/wa- prefixes at word-initial position).
  - Class B (qurʾān-or-kitāb stem): the literal substrings `قرءان` (or `قرآن`) + `كتاب`.
  - Class C (addressee-marker): any of `يا أيها`, `إنك`, `لك` followed by a verb in 2-person singular, or any 2MS pronominal suffix `ك` immediately following a possessable noun within the same verse.
  - **Co-occurrence score** = number of distinct classes present (max 3) in each verse. Q 73:20, Q 96:1, Q 96:3 expected to score 2-3; null distribution = scores under randomly-drawn 3-verse samples from the corpus matched on length-band.
- **Verse-twin similarity (H1b)**: H-NEW-66 mutashābih-style char-Levenshtein similarity (`rapidfuzz.fuzz.ratio` over no-tashkeel text), computed for the 2 cross-pairs (Q 73:20 vs Q 96:1; Q 73:20 vs Q 96:3) and reported as max + mean.
- **Reference distribution (H1b)**: the 6,235 similarity scores between Q 73:20 and every other corpus verse. The pair-similarity must place Q 96:1 OR Q 96:3 in the top 5% of these 6,235 scores for H1b to PASS.

## 3. Test statistic

- N_co = co-occurrence-score for {Q 73:20, Q 96:1, Q 96:3}.
- p_perm_co (H1a) = fraction of length-matched random 3-verse samples scoring ≥ N_co.
- sim_max = max(sim(Q 73:20, Q 96:1), sim(Q 73:20, Q 96:3)).
- pct_q96 = max(percentile_of_sim(Q 73:20, Q 96:1), percentile_of_sim(Q 73:20, Q 96:3)) over the 6,235-sim distribution.

## 4. Permutation null

**Null model A (length-matched 3-verse sample, H1a)**: draw 3 verses from the corpus, each within ±25% of the matched verse's word-count band (Q 73:20 has ~76 words; Q 96:1 has 5; Q 96:3 has 4). Compute co-occurrence-score under null. n_perm = 10000, seed = 20260509.

**Null model B (full Q 73:20 vs all corpus verses, H1b)**: rank the 6,235 similarities; check if Q 96:1 or Q 96:3 ranks in the top 312 (5th percentile).

## 5. Success / Failure

- **CONFIRMED**: H1a and H1b both pass; permutation p (length-matched A) ≤ α_bon = 0.025 AND pct_q96 ≤ 0.05.
- **DIRECTIONAL**: 1 of 2 sub-tests passes.
- **NULL**: both fail.

## 6. Honest limits known a priori

- Q 73:20 is a 76-word "long verse" whose length massively dominates the lexical-co-occurrence count. The length-matched null is critical to avoid spurious passes by length alone. The other pair-member verses (Q 96:1 = 5 words, Q 96:3 = 4 words) are extremely short — char-Levenshtein on disparate-length verses is inherently low. The H1b test is therefore conservative (almost-impossible-to-pass given length-asymmetry).
- The IMPV-qrA addressee-grammar differs across the pair: Q 73:20 has `iqraʾū` (2MP plural — community-wide), while Q 96:1+3 have `iqraʾ` (2MS singular — direct prophetic). This is a **structural mismatch** within the "prophetic-revelation pair" framing that H-NEW-1300 did not flag. The pre-reg discloses this prior observation; it does not affect the test design but is reported in the result interpretation.
- Class C (addressee-marker) is broad-grain; sensitivity check: require strict 2MS suffix-marker (matching Q 96 exactly, excluding Q 73:20's plural-addressed scope). Under strict 2MS, Q 73:20 may FAIL Class C — flagged as a robustness diagnostic, not the primary test.

## 7. Pre-commit attestation

- This pre-reg is being SHA-locked before the script's runtime SHA verification. The pair-membership and verse-text content were observed during pre-flight (per H-NEW-1300's published table); the specific co-occurrence-score / similarity-rank for the pair has NOT been computed prior to this lock.

## 8. Garden-of-forking-paths log

- The "prophetic-revelation pair" framing is taken DIRECTLY from H-NEW-1300's post-hoc descriptive note. H-NEW-1300 itself returned NULL by strict pre-reg (rank-1 tie). The post-hoc 4-surah inventory split into 2 surah-pairs is a **descriptive observation**, not a confirmed structural finding. Q073-F-01 here tests whether the pair has empirical mutual-similarity-or-co-occurrence beyond chance — i.e. whether the descriptive pairing has structural reality at the verse-level.
- H-NEW-1301 already tested cluster-level FR cohesion at the surah-aggregate; result NULL-BROKEN. The current test operates at the **verse level**, a distinct feature axis (per H-NEW-1303 sketch).

## 9. Decision rule

1. Compute N_co for {Q 73:20, Q 96:1, Q 96:3}.
2. Compute p_perm_co under length-matched null A.
3. Compute sim(Q 73:20, Q 96:1), sim(Q 73:20, Q 96:3), and percentile within Q 73:20-vs-all distribution.
4. Apply success matrix from §5.
5. If `direction reverses` (e.g., observed N_co < null mean), apply PRE-REG-STANDARD-01 violation flag.

## 10. Bonferroni declaration

- bonferroni_k = 2 (H1a, H1b).
- bonferroni_family = Q073-F-01-iqra-pair.
- alpha_bon = 0.025 per test.
- pre-committed acceptance: BOTH tests pass at 0.025 ⇒ CONFIRMED.

## 11. Connection to existing findings

- **H-NEW-1300** (NULL by strict pre-reg): the 6 IMPV-qrA segments split 4-surah inventory; Q 73 + Q 96 = "prophetic-revelation pair" descriptive cluster.
- **H-NEW-1301** (NULL-BROKEN): surah-level FR cohesion of {Q 17, 69, 73, 96} fails primary AND positive control. The current test operates at a distinct feature axis (verse-level lexical-twin), so a positive result HERE would not contradict H-NEW-1301 — the cluster could be verse-twin-cohesive but surah-aggregate-FR-incohesive.
- **H-NEW-66** (verse-twin network): rules-tuple compatible.
