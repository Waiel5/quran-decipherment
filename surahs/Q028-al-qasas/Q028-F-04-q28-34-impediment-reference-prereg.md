---
finding_id: Q028-F-04
title: Q 28:34 speech-impediment-reference verse — root-set diversity vs random 7-token windows
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q028-novel-findings
alpha_bon: 0.01
direction: ONE-SIDED-UPPER
status: PRE-REGISTERED
specialist: Q028-al-qasas-specialist
verdict: TBD
---

# Q028-F-04 — Q 28:34 impediment-reference root-diversity pre-reg

## 1. Garden-of-forking-paths CORRECTION FROM PROMPT

The dispatch prompt claimed Q 28:35 is "the speech-impediment-relief verse … قال ربي اشرح لي صدري ويسر لي أمري واحلل عقدة من لساني يفقهوا قولي". This is **incorrect at the verse-locator level** — that prayer is **Q 20:25-28** (Mūsā in Ṭā-Hā). Q 28 has **two adjacent verses** that **reference** the speech-impediment via the brother-Hārūn ʿaqdat-al-lisān motif, but neither is the prayer:

- Q 28:34: `وأخي هارون هو أفصح مني لسانا فأرسله معي ردءا يصدقني إني أخاف أن يكذبون` — Mūsā says "and my brother Hārūn is more eloquent than I in tongue, so send him with me as a helper to confirm me." This is the Q 28 *recapitulation* of the impediment, NOT the relief-prayer.
- Q 28:35: `قال سنشد عضدك بأخيك …` — God's answer.

The prompt's mis-locator does not invalidate the test, but the pre-reg is re-anchored to **Q 28:34**, the actual Q 28 impediment-reference verse. This re-anchoring is logged BEFORE observation.

## 2. Hypothesis

Q 28:34 is a **prophetic self-disclosure** verse (Mūsā confessing limitation, requesting brotherly support). It is structurally rare in the corpus — most prophet-self-disclosures of impediment are concentrated in Q 20.

**H1 (locked, one-sided upper-tail)**: The orthographic-token-set of Q 28:34 contains ≥ 2 lexemes that are **co-attested with Q 20:25-28** (Mūsā's relief prayer) and **rare** elsewhere. Specifically, we count tokens shared between Q 28:34 and Q 20:25-28 that have ≤ 5 corpus-wide attestations.

**H2 (locked)**: The Q 28:34–35 pair has **higher** cosine similarity to Q 20:25-28 (the relief prayer) than to a length-matched random pair drawn from outside-Mūsā material — at p_perm < 0.01 (one-sided).

## 3. Direction-locking

H1 direction = ≥ 2 shared low-frequency lexemes. Lower = NULL.
H2 direction = higher cosine to Q 20:25-28. Reverse = NULL.

## 4. Method

- Q 28:34-35 = 2-verse target window.
- Q 20:25-28 = 4-verse reference window.
- Tokenize on orthographic-no-tashkeel; strip prefixes (و ف ل ب ال).
- For H1: compute the intersection of token-sets, restrict to tokens with ≤ 5 corpus-wide attestations.
- For H2: TF-cosine on shared-root union vocabulary; permutation null = sample 10 000 length-matched random verse-pairs (2-verse + 4-verse) from non-Mūsā material; how often does a random pair exceed observed cosine?

## 5. Test family + Bonferroni

Family: Q028-novel-findings, k = 5. α_Bonferroni = 0.01.

## 6. Acceptance / failure

- **PASS** = H1 ≥ 2 shared low-freq lexemes AND H2 cosine_obs > random-pair-95th-percentile (p < 0.01).
- **DIRECTIONAL** = exactly 1 sub-hypothesis passes.
- **NULL** = 0 sub-hypotheses pass.

## 7. MW protections

- MW-1: length matched (2-verse + 4-verse).
- MW-2: 10 000 random pair samples.
- MW-3: TF vs prefix-stripped sensitivity.
- MW-5: positive-control = Q 7:138-141 (Mūsā/Hārūn fragment) cosine to Q 20:25-28; should be high.
- MW-6: instrument-control = how often random-pair cosines exceed `cos(Q28:34-35, Q7:138-141)`?
- MW-7: not invoked (test is pre-registered, not post-hoc; the verse-locator correction is logged before observation).

## 8. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
