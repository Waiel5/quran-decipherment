---
test_id: Q047-F-05
title: "Q 47 qitāl-root density — pre-registered top-3 prediction"
date_locked: 2026-05-10
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: Q047-F-05-qtl-density
alpha_bon: 0.05
direction_locked: true
rules_tuple: (no-tashkeel, QAC-stem-root, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
specialist: Q047-wave-J-specialist
parent_findings:
  - Q047-F-02 (war-vocabulary density, used 9-term cluster qiṭāl/jihād/riqāb/asr/fidāʾ/ḥarb/...)
classical_anchors:
  - al-Qurṭubī, *al-Jāmiʿ*, on Q 47 — names it *sūrat al-Qitāl*
  - Q008-F-03 (qitāl-cluster {Q 8, 9, 47, 48, 61})
  - al-Wāqidī, *Maghāzī* — places Q 47 in the late-Medinan war-instruction layer
---

# Q047-F-05 Pre-registration — Q 47 *qtl*-root density rank

## Hypothesis

Per al-Qurṭubī's identification of Q 47 as *sūrat al-Qitāl*, and the project's qitāl-cluster {Q 8, 9, 47, 48, 61} per Q008-F-03, Q 47 should show very-high concentration of the QAC stem-root *qtl* (ق-ت-ل, root for قاتل / قتال / قتل / قتلوا) per surah word-count.

**This is a NARROWER test than Q047-F-02** — F-02 used a 9-element "war-vocabulary" cluster (qiṭāl/jihād/riqāb/asr/fidāʾ/ḥarb/wathāq/darb-riqāb/kuffār-combatant) where Q 47 ranked 2/114. Here we restrict to ONE root: *qtl*. Per the brief, Q 47 is pre-registered to be in **top-3 by qtl-root density per 1000 words** (corpus-wide rank).

## Pre-committed prediction (DIRECTION LOCKED)

**Direction-locked**: rank(Q 47, qtl-root density per 1000 words) ≤ 3 among all 114 surahs.

## Rules-tuple specifics

- Root tokens: QAC v0.4 stem-root annotations (`data/morphology/root-index.json` entry `qtl`).
- Surah word-count: `quran-no-tashkeel.json` standard whitespace tokenization (with pause-marker stripping).
- Rate metric: count_of_qtl_attestations × 1000 / word_count.
- No min-count threshold (this is part of the test's brittleness — see honest-limits).

## Test (Bonferroni-1)

**T1**: rank(Q 47, qtl-rate-per-1000-w) ≤ 3.

Single test. α = 0.05.

## Direction-of-effect lock

Pre-committed:
- If Q 47 rank ≤ 3: VINDICATED.
- If Q 47 rank ∈ [4, 10]: DIRECTIONAL.
- If Q 47 rank > 10: NULL.

The brief specifies "top-3" — strict success threshold is rank ≤ 3.

## Garden-of-forking-paths log

- BEFORE running: acknowledged that small-N surahs (Q 80, 81, 85, 90 — ≤ 200 words with 1 qtl) will inflate per-1000-w rate. This is a KNOWN MW-3 alternative-model concern: had a per-100-w-with-min-count-3 variant been chosen instead, the rate-ranking would be more stable. The brief mandates the per-1000-w rate; this pre-reg honors that direction.
- BEFORE running: acknowledged Q047-F-02 already established Q 47 = #2 on a broader war-vocabulary cluster. This test is intentionally narrower (single-root) and harder.
- BEFORE running: acknowledged Q 47 contains "qutilu" (Q 47:4) and "al-qitāl" (Q 47:20) — exactly 2 *qtl* attestations. Q 47 word-count ≈ 547-570 (per rules-tuple). Rate ≈ 3.5-3.7 per-1000-w. For this to be top-3, the other surahs at higher rate must all have rate > 3.7. This is an aggressive pre-reg; small-N tail surahs are likely to outrank.
- BEFORE running: DECIDED NOT to switch metric post-hoc; commit to per-1000-w as specified.

## Honest limits (load-bearing)

1. The per-1000-w rate is sensitive to surah length. Surahs with 1-3 attestations and ≤ 300 words will mechanically rank high.
2. al-Qurṭubī's *sūrat al-Qitāl* designation is about narrative/legal content, not single-root density. A NULL on this narrow test does not refute the broader designation (Q047-F-02 already VINDICATED at the 9-term cluster level).
3. If NULL, the honest interpretation is: the *qtl* root is dispersed across the qitāl-cluster {Q 2, 3, 4, 5, 8, 9, 33, 47, ...} rather than concentrated in Q 47. Q 47's distinctiveness is its **density of war-INSTRUCTION** (with diverse vocabulary), not its raw *qtl* count.
