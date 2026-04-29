---
id: H-NEW-321
title: "Q 1 ↔ Q 27 Basmala-echo content-axis test — NULL (phrase-sharing does NOT entail content-axis proximity)"
phase: B
status: NULL (Cell A rank 92/113; Cell B rank 67/113; both FAR from top 10% threshold; MW-5 PASSES)
date: 2026-04-19
executed_by: team-lead (inline)
parent_1: H-NEW-155 (Q 1 sui-generis-liturgical)
parent_2: H-NEW-111 (Fisher-Rao root distance matrix)
related: H-NEW-263 (Q 27 near-significant hub); H-NEW-310 (singleton rank-1 NULL)
seed: 20260428
prereg: h-new-321-q1-q27-basmala-echo-prereg.md
prereg_sha256: 1008401d7ae08001ae27b1a66974e6a7069dc358887a4f876004b4b627ee8577
bonferroni_k: 2
alpha_bon: 0.025
direction: "Cell A rank(Q 27 | Q 1) ≤ 11 of 113; Cell B rank(Q 1 | Q 27) ≤ 11"
verdict: NULL
---

# [[h-new-321-q1-q27-basmala-echo|H-NEW-321]] — Q 1 ↔ Q 27 Basmala-echo content-axis test — CLEAN NULL

## 1. Headline

**CLEAN NULL.** The Q 1 ↔ Q 27 liturgical/scriptural link — via Q 27:30's UNIQUE in-corpus repetition of Q 1's opening Basmala formula — does NOT manifest at the Fisher-Rao content-axis. Both surahs are content-distant: Q 27 sits at the **81st percentile** of Q 1's nearest-neighbor rank (rank 92/113), and Q 1 sits at the **59th percentile** of Q 27's rank (rank 67/113). The shared-phrase echo is **phrase-specific, not content-clustering**.

- **Cell A** rank(Q 27 | Q 1) = 92/113 (81.4%ile) — above median by a clear margin; FAIL at strict top-10% threshold
- **Cell B** rank(Q 1 | Q 27) = 67/113 (59.3%ile) — slightly above median; FAIL
- **MW-5 positive control** (muʿawwidhatān Q 113 + Q 114): rank 1/113 and 2/113 respectively — PASS (instrument correctly detects genuine content-proximate liturgical pairs)
- **Null mean rank** across 1000 random pivot-target pairs = 56.4 (center of 1-113 range as expected)
- **Pre-committed expectation was NULL** (modal expectation given Q 1's 7-verse compact prayer vs Q 27's 93-verse narrative)

## 2. What this means

### 2.1 Phrase-sharing ≠ content-sharing

The Basmala formula (بسم الله الرحمن الرحيم) is a 4-word theological signature shared between Q 1 and Q 27 at the surface-phrase level. But the SURROUNDING content of these two surahs is fundamentally different:

- **Q 1**: 7-verse prayer register, vocabulary concentrated in {Allāh, Rabb, Raḥmān, Raḥīm, ḥamd, hidāya, ṣirāṭ, mustaqīm, niʿma, maghḍūb, ḍāllīn}
- **Q 27**: 93-verse narrative register, heavy vocabulary in {Sulaymān, Dāwūd, jinn, ṭayr, namlah, hudhud, Bilqīs, Saba, Thamūd, ʿaṣā, malā'}

These vocabularies barely overlap. The Basmala phrase is a REGISTER-INDEPENDENT formulaic quotation — Solomon uses it as a letter-opening in Q 27:30 — which doesn't change Q 27's overall root-distribution profile to make it closer to Q 1.

### 2.2 Companion finding to [[h-new-310-singleton-fr-rank1|H-NEW-310]]

[[h-new-310-singleton-fr-rank1|H-NEW-310]] showed that MOST muq singletons have non-muq rank-1 content neighbors. The generalization: **classical "letter-sharing" and "phrase-sharing" do NOT entail content-axis-sharing**. Two surahs can share letters, a phrase, or theological terminology and still be content-distant. This finding REINFORCES the scope-limit established at [[h-new-310-singleton-fr-rank1|H-NEW-310]]: empirical content-proximity is ORTHOGONAL to classical surface-similarity flags.

### 2.3 Contrast with muʿawwidhatān (Q 113 + Q 114)

The MW-5 control is informative: Q 113 and Q 114 are rank-1 and rank-2 nearest neighbors of each other. Classical tradition treats them as a RITUAL PAIR (al-muʿawwidhatān, "the two protective surahs"), always recited together. Their content-axis proximity MATCHES their liturgical pairing — because their actual VOCABULARY is nearly identical (both are *qul aʿūdhu bi-rabbi...* formulas with shared protection-against-evil lexicon).

**The contrast**: Q 113-Q 114 pairing CONVERGES classical-liturgical + empirical-content; Q 1-Q 27 pairing DIVERGES (shared at classical phrase level, distant at empirical content level). Not all classically-paired surahs are content-near; Q 113-Q 114 is not the universal pattern.

### 2.4 Classical-scholarship refinement

al-Ṭabarī *Jāmiʿ al-Bayān* and al-Zamakhsharī *Kashshāf* discuss Q 27:30's Basmala as a SIGNIFICANT NARRATIVE DEVICE (Solomon using formal letter-opening with divine invocation). Neither scholar claims Q 27 and Q 1 are CONTENT-CLUSTERED as theologically-paired surahs. Classical tradition thus correctly treats the Q 27:30 Basmala as a PHRASE-EVENT, not a surah-pairing-claim.

[[h-new-321-q1-q27-basmala-echo|H-NEW-321]] empirically validates this classical framing: the Basmala at Q 27:30 is a phrase-specific scriptural event, not a content-clustering mechanism.

## 3. Honest limits

1. **Two-surah test** — single pair. Not a pattern test across multiple phrase-echo pairs.
2. **Fisher-Rao on QAC-STEM roots** — other content metrics (char-4-gram, NCD) could give different ranks.
3. **Q 1's small N** (~30 tokens) may cause noisy FR distances at 15-dim space. [[h-new-111-fisher-rao-mushaf|H-NEW-111]] used the full corpus for D_matrix; but Q 1's small N means its distribution is concentrated on few roots.
4. **Pre-committed null was correct** — the finding confirms my expectation.
5. **Single-phrase test** — other in-corpus phrase echoes (e.g., *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* between Q 55 and narrative re-use elsewhere) not tested here.

## 4. Queued follow-ups

- **H-NEW-321.1**: test other in-corpus phrase repetitions (e.g., *al-ḥamdu li-Llāhi rabbi al-ʿālamīn* appears in Q 1:2, Q 6:45, Q 37:182, etc.). Do those surahs cluster by content?
- **H-NEW-321.2**: test Q 1 ↔ Q 59 content-axis proximity — Q 59:22-24 contains the Khawātim divine-name cluster (umm al-kitāb echo?). Classical anchor: al-Nasāʾī on Fātiḥa as *umm al-Kitāb*.
- **H-NEW-321.3**: broader pattern test — for all 113 adjacent mushaf pairs, is content-proximity correlated with liturgical/classical pair-designation?

## 5. Cross-references

- Parent 1: [[h-new-155-q1-sui-generis|H-NEW-155]] (Q 1 sui-generis-liturgical — content axis distance from rest of corpus)
- Parent 2: [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (FR content distance)
- Related: [[h-new-263-divine-name-surah-network|H-NEW-263]] (Q 27 as near-significant hub — this was at DIVINE-NAME network, not FR content)
- Companion finding to: [[h-new-310-singleton-fr-rank1|H-NEW-310]] (letter-cluster ≠ content-cluster)
- Classical anchor: al-Ṭabarī / al-Zamakhsharī Q 27:30 commentary

## 6. Classical-scholarship integration

- **al-Ṭabarī *Jāmiʿ al-Bayān*** Q 27:30: treats Basmala-in-letter as formal-letter-opening device — empirically validated as PHRASE EVENT not content-cluster.
- **al-Suyūṭī *Itqān*** Q 27:30 as unique in-body Basmala — no claim of surah-pairing with Q 1; classical scholarship correctly scopes this as phrase-level.
- **al-Zamakhsharī *Kashshāf*** Q 27:30 — Solomon's formal-diplomatic context.
- **Classical sunnī / shīʿī debate on Basmala as Q 1 verse 0 vs 1** — not affected by this finding.

## 7. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-321-q1-q27-basmala-echo-prereg.md` (SHA-256 1008401d...)
- Script: `scripts/h_new_321_q1_q27_basmala_echo.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-321.json`
- Findings: this file

## 8. Final statement

**The only in-corpus repetition of Q 1's Basmala formula (Q 27:30 in Solomon's letter to Bilqīs) does NOT manifest as a content-axis surah-pairing between Q 1 and Q 27.** Q 27 sits at the 81st percentile of Q 1's Fisher-Rao-root content-neighbors; Q 1 sits at the 59th percentile of Q 27's neighbors. Both are content-distant, well above median rank. The MW-5 positive control (muʿawwidhatān Q 113-Q 114 rank 1/2) confirms the instrument detects genuine content-proximate classical pairs — Q 1-Q 27 is not such a pair. **Classical tradition correctly treats Q 27:30 as a PHRASE EVENT (formal Basmala invocation in Solomon's narrative letter-opening), not as a surah-pairing claim.** Empirical content-axis proximity is ORTHOGONAL to classical phrase-sharing and letter-sharing signals — consistent with [[h-new-310-singleton-fr-rank1|H-NEW-310]]'s muq-singleton finding.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
