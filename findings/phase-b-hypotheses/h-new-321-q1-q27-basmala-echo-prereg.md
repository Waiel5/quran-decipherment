---
id: H-NEW-321
title: "Q 1 ↔ Q 27 Basmala-echo content-axis test — does the only in-corpus Basmala-repetition pair show distinctive Fisher-Rao proximity?"
phase: B
status: PRE-REGISTERED 2026-04-19
date: 2026-04-19
agent: team-lead (inline; ID 321 chosen to skip codex sequential range)
parent_1: H-NEW-155 (Q 1 sui-generis-liturgical)
parent_2: H-NEW-111 (Fisher-Rao content distance matrix)
related: H-NEW-263 (Q 27 al-Naml near-significant hub candidate in divine-name network)
seed: 20260428
bonferroni_k: 2
bonferroni_family: h-new-321-q1-q27-basmala-echo
alpha_bon: 0.025
n_perm: 1000
rules_tuple: "(Q 1 al-Fātiḥa + Q 27 al-Naml; Fisher-Rao root distance matrix from H-NEW-111; rank-based test — rank of Q 27 among Q 1's 113 content-neighbors AND rank of Q 1 among Q 27's 113 content-neighbors; two-sided unusualness under uniform-rank null; seed 20260428)"
direction: "Cell A: rank(Q 27 | Q 1) in top 10% (rank ≤ 11 of 113); Cell B: rank(Q 1 | Q 27) in top 10%"
verdict: PENDING
---

# [[h-new-321-q1-q27-basmala-echo|H-NEW-321]] — Q 1 ↔ Q 27 Basmala-echo content-axis test

## 1. Question

Q 1 al-Fātiḥa opens with *bi-smi Allāhi al-Raḥmāni al-Raḥīm* (the Basmala). Q 27:30, within Prophet Solomon's letter to Queen Bilqīs, contains the ONLY IN-CORPUS REPETITION of this exact phrase: *innahu min Sulaymāna wa-innahu bi-smi Allāhi al-Raḥmāni al-Raḥīm* (classical tafsīr notes this as the only surah with an in-body Basmala).

**Question**: does this scriptural / liturgical LINK between Q 1 and Q 27 manifest as a distinctive content-axis proximity in Fisher-Rao root-distribution space? Or is Q 27's Basmala repetition a narrative device whose content axis is unrelated to Q 1?

This tests a CLASSICAL INTUITION at the empirical content-axis level: do two surahs linked by a SPECIFIC SHARED PHRASE also cluster content-wise?

## 2. Hypothesis

**H1 (liturgical echo manifests at content-axis)**: rank(Q 27 | Q 1) in top 10% (rank ≤ 11 of 113 non-self neighbors) — content-axis proximity reflects the shared phrase. AND rank(Q 1 | Q 27) likewise.

**H0 (liturgical echo is phrase-specific, not content-clustering)**: rank ~ 56 median (no distinctive proximity).

Pre-committed direction: Cell A rank(Q 27 | Q 1) ≤ 11; Cell B rank(Q 1 | Q 27) ≤ 11.

## 3. Protocol

1. Load Fisher-Rao root distance matrix from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (same source as [[h-new-290-q42-block-vs-phonology-tension|H-NEW-290]]/310).
2. For Q 1: rank all 113 non-self surahs by FR distance; find rank of Q 27.
3. For Q 27: rank all 113 non-self surahs by FR distance; find rank of Q 1.
4. Two-sided permutation null: for 1000 trials, draw random pivot surah (not Q 1 or Q 27), compute rank of a random target surah among its neighbors. Compare observed ranks to null distribution.

## 4. Bonferroni + MW-5

k = 2 cells, α_bon = 0.025.

MW-5 positive control: test rank(Q 113 | Q 114) — the muʿawwidhatān pair explicitly classical. Expected rank = 1 or very low (they share ALMOST ALL content-words as a ritual formula pair).

## 5. Decision rules

| Cell A (rank 27|1 ≤ 11) | Cell B (rank 1|27 ≤ 11) | Verdict |
|---|---|---|
| PASS | PASS | **BASMALA-ECHO-MANIFESTS** |
| PASS | FAIL | **ASYMMETRIC-ECHO** (Q 1→Q 27 but not reverse) |
| FAIL | PASS | **REVERSE-ASYMMETRIC-ECHO** |
| FAIL | FAIL | **NULL — echo is phrase-specific, not content-clustering** |

## 6. Pre-committed expectations

Q 1's content profile: 7 short verses, ~30 tokens, prayer-register theological-core vocabulary (Allāh, Rabb, Raḥmān, Raḥīm, hidāya, ṣirāṭ mustaqīm).

Q 27's content profile: 93 verses, narrative-heavy (Solomon, Moses, Ṣāliḥ, Lūṭ stories), natural-world imagery (ant, hoopoe, jinn).

Content-axis PRIOR expectation: Q 27's narrative richness and long length likely place it CONTENT-FAR from Q 1's compact prayer. H0 is the modal expectation. PASS would be a surprising finding demonstrating that Basmala-phrase-sharing OVERRIDES content-axis length-difference.

Honestly: I expect NULL. But testing anyway because the classical tradition treats Q 27:30 as a SIGNIFICANT Basmala event worthy of theological discussion.

## 7. Honest limits

1. **Two-surah test** — not a generalizable pattern test.
2. **Fisher-Rao on QAC-STEM roots** — one content metric.
3. **Q 1 has low N** (~30 tokens, classified "insufficient-data" for Zipf per [[h-new-172-zipf-per-chapter|h-new-172]]); but [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D_matrix was computed on FULL corpus so Q 1 data exists in the distance matrix.
4. **Q 27 al-Naml was a near-significant hub candidate** in [[h-new-263-divine-name-surah-network|H-NEW-263]] (z=2.07, p_adj=0.136). This could reflect broad content-connectivity that affects both rank(27|*) calculations.

## 8. Classical-scholarship anchors

- **al-Ṭabarī *Jāmiʿ al-Bayān*** on Q 27:30 — discusses the Basmala's significance as Solomon's formal letter-opening.
- **al-Suyūṭī *Itqān*** — Q 27:30 noted as unique in-body Basmala.
- **Classical debate about whether Basmala is a VERSE of Q 1** (Sunnī/Shīʿī divergence) — not directly tested here.
- **al-Zarkashī *al-Burhān fī ʿUlūm al-Qurʾān*** on Basmala positioning.

## 9. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_321_q1_q27_basmala_echo.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-321.json`
- Findings: `findings/phase-b-hypotheses/h-new-321-q1-q27-basmala-echo.md`

Pre-reg locked 2026-04-19. Execution follows.
