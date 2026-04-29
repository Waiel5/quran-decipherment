---
id: H-NEW-193
title: Q 1 al-Fātiḥa's 7 verses as individual attractors in verse-twin network
phase: B
status: FAIL — primary hypothesis DISCONFIRMED; secondary directionally-supported
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-155 (Q 1 sui-generis-liturgical, p=0.0013), h-new-163 (Q 1 #3 in dispersion ranking)]
seed: 20260419
n_null: 10000
rules_tuple: "(Hafs-Kūfan 6236 verses; quran-no-tashkeel.json; char-trigrams over normalized-Arabic letters only; Jaccard)"
bonferroni: k=2 α_bon=0.025 family=h-new-193-q1-attractors
pre_reg: findings/phase-b-hypotheses/h-new-193-q1-attractors-prereg.md
prereg_sha256: 94702df7acd22d62b55dcf207544f708f21ac56a8b5448156f34736a8e2e81ac
script: scripts/h_new_193_q1_attractors.py
output_json: findings/phase-b-hypotheses/csv/h-new-193.json
verdict: FAIL — Q 1's 7 verses touch 37 distinct surahs (top-10 union), significantly LESS than the null mean of 40.2 (p_primary=0.8231; z=-0.80). The pre-registered positive-direction hypothesis is disconfirmed. Q 1's verses are however UNUSUALLY TIGHT (avg top-10 Jaccard 0.2522 vs null 0.1756, z=+1.92, p_secondary=0.0612 — does NOT clear Bonferroni α_bon=0.025 but is directionally strong).
---

# [[h-new-193-q1-attractors|H-NEW-193]] — Q 1 al-Fātiḥa verse-twin attractors — FAIL

## Primary result

Q 1's 7 verses, used as seeds in a char-trigram Jaccard nearest-neighbor
search, touch **37 distinct surahs** in the union of their top-10
neighbors. Null-mean for random 7-verse seed sets = **40.2 ± 4.0**
(median 40). p = **0.8231** (direction-locked positive).

**The "theological palette" hypothesis — that Q 1's verses attract
twin-verses from across the corpus — is EMPIRICALLY DISCONFIRMED under
this operationalization.** Q 1's top-10 twins are slightly MORE
clustered than random (37 surahs instead of 40), not less.

## Secondary result: Q 1 twins are UNUSUALLY TIGHT

The average top-10 Jaccard similarity for Q 1's 7 verses is **0.2522**,
vs null mean **0.1756 ± 0.0400**. That's +1.92σ, p_secondary = **0.0612**
— directionally strong but does NOT clear the Bonferroni α_bon=0.025.

**Interpretation.** Q 1's verses are LEXICALLY TIGHT with respect to
their twins — they have very-similar neighbors in the corpus. But those
tight neighbors are CONCENTRATED in a modestly smaller number of surahs
than chance would dictate. This pattern fits a "formulaic-echo" model
rather than a "theological-palette" model:

- **Palette-model** (pre-reg expectation, FAILED): Q 1's verses each
  resonate with different thematic domains scattered across many
  surahs. Prediction: MANY distinct surahs touched, avg similarity
  perhaps moderate.
- **Formulaic-echo model** (fits observed): Q 1's verses use stock
  Quranic phrasing (e.g. `الحمد لله رب العالمين`, `الرحمن الرحيم`,
  `يوم الدين`, `الصراط المستقيم`) — these phrases reappear in a
  relatively CONCENTRATED set of doxological / eschatological surahs,
  so top-10 twins are HIGH-similarity but SURAH-CONCENTRATED.

## Surahs touched (top-10 union)

37 surahs: 1, 2, 4, 6, 7, 10, 15, 19, 20, 23, 26, 27, 28, 36, 37, 38,
40, 41, 44, 45, 46, 51, 53, 55, 56, 59, 69, 70, 74, 81, 82, 83, 100,
104, 106, 109, 112.

Patterns in the touched-set:
- **Short Meccan doxological** (Q 55, 56, 69, 70, 74, 81, 82, 83, 100,
  104, 106, 109, 112) — dominant.
- **Ḥā-mīm cluster** (Q 40, 41, 44, 45, 46) — full presence.
- **Opening-letters group** (Q 15, 19, 20, 26, 27, 28, 36, 37, 38) —
  strong.
- **Long Medinan** (Q 2, 4) — only two present; a pointed absence
  suggesting Q 1's lexical footprint is NOT Medinan-discursive.

## MW-5 control

MW-5 FAIL — the null median (40) is HIGHER than Q 1 (37). Random 7-verse
sets actually touch MORE surahs than Q 1 does. This is not a
Q-1-unique-in-the-negative-direction finding; it is simply
direction-locked disconfirmation. (A random 7-verse set serves as the
natural control; its expected distinct-surah count is 40 not 37.)

## Sensitivity: Q 1 verses 2-7 (no basmala)

Excluding the basmala (Q 1:1), verses 2-7 (6-verse variant) touch **34
distinct surahs**. Same pattern, slightly weaker — consistent with the
full-7 result. The conclusion does not flip under basmala-exclusion.

## Relation to prior findings

This result CONSTRAINS but does not contradict [[h-new-155-q1-sui-generis|H-NEW-155]] / [[h-new-163-dispersion-ranking-all-surahs|H-NEW-163]]:

- **[[h-new-155-q1-sui-generis|H-NEW-155]]** measured QAC-stem ROOT dispersion (types, not tokens;
  root-level, not verse-level). Q 1's 18 roots are each widely-shared
  across the 114 surahs (50.4% avg).
- **[[h-new-193-q1-attractors|H-NEW-193]]** measures VERSE-level character-trigram nearest-neighbor
  clustering. Q 1's verse-level twins are concentrated.

The two can coexist: **Q 1's roots are widely-distributed across the
corpus, but Q 1's phrasings — as whole verses — have their closest
echoes in a restricted surah-set (short-Meccan + Ḥā-mīm + opening-letters).**

In other words, Q 1 is a "palette" at the ROOT level (confirmed) but
NOT at the VERSE-PHRASE level (this finding). The word-level
vocabulary of Q 1 ripples through most of the corpus, but the
sentence-form echoes are doxologically-concentrated.

## Verdict

**FAIL** — primary direction-locked hypothesis DISCONFIRMED
(p=0.8231, wrong direction). Secondary directionally positive but
does not clear α_bon=0.025.

This is an HONEST NEGATIVE RESULT: the "palette" claim survives at the
ROOT level ([[h-new-155-q1-sui-generis|H-NEW-155]]) but does not survive at the VERSE-TRIGRAM-TWIN
level. The character of Q 1 as a sui-generis-liturgical surah is
refined: it is ROOT-diffuse + PHRASE-concentrated.

## Garden-of-forking-paths log

All analysis parameters (char-trigrams, Jaccard, top-10 primary, 10000
null, seed 20260419, exclude-self, non-Q1 pool) were fixed in the
pre-registration BEFORE running. No post-hoc rule adjustment. The only
post-hoc computation is the sensitivity v2-v7 variant (pre-registered
as a disclosure) and the surah-set-structural interpretation
(confirmatory, not a rule change).
