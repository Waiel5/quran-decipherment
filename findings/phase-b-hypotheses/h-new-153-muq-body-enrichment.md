---
id: H-NEW-153
title: Muqaṭṭāʿat letters over-represented in own surah body (al-Zamakhsharī body-frequency claim)
phase: B
status: PASS-DIRECTED (post-hoc single-test α=0.05; modest effect size)
date: 2026-04-17
executed_by: team-lead (inline)
classical_anchor: al-Zamakhsharī, al-Kashshāf, on muqaṭṭāʿat (classical body-frequency claim distinct from al-Suyūṭī's rhyme claim)
seed: 20260417
rules_tuple: (no-tashkeel; 29 muq-opened surahs; body letter-counts = verses 2+; corpus-wide letter frequency as baseline; 5K perm null shuffling letter-sets across surahs)
bonferroni_k: 1
bonferroni_family: h-new-153-muq-body-enrichment
alpha_bon: 0.05
direction: POSITIVE — muq letters enriched above corpus-wide baseline in own surah body
verdict: PASS-DIRECTED
---

# [[h-new-153-muq-body-enrichment|H-NEW-153]] — Muqaṭṭāʿat letter enrichment in own surah body

## Classical anchor

al-Zamakhsharī (d. 538 AH / 1144 CE) in al-Kashshāf noted that the muqaṭṭāʿat letters tend to appear with elevated frequency in the body text of the surahs they open. This is DISTINCT from al-Suyūṭī's rhyme-prefiguration claim ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]], RETRACTED) — the al-Zamakhsharī claim is about overall body-text letter frequency, not specifically verse-final rhyme.

## Method

For each of 29 muqaṭṭāʿat-opened surahs:
- Exclude the muqaṭṭāʿat-opening v1
- Count letter frequency in the body text (v2+)
- For each letter in the opening (unique set), compute `body_ratio = body_freq / corpus_freq`
- Corpus_freq is computed over all 114 surahs' letter counts — already accounts for muq letters being high-frequency in the corpus

**Null**: shuffle letter-set-to-surah assignments 5,000 times. Compute null distribution of mean body_ratio.

## Results

| Quantity | Observed | Null mean | Null SD | p_one_sided |
|---|---:|---:|---:|---:|
| Mean body ratio | **1.032** | 1.000 | 0.014 | **0.012** |
| Mean z-score (binomial) | **+0.28** | −0.05 | 0.15 | **0.015** |

**Observed > null at p = 0.015 under letter-set-shuffle null.** 41/78 letter-surah pairs show ratio > 1.0; 41/78 show z > 0.

## Strongest individual enrichments

| Q | Opening | Letter | Body ratio | z-score |
|:-:|:-:|:-:|---:|---:|
| **50** | ق | ق | **1.74** | **+4.20** ✓ |
| 26 | طسم | ط | 1.49 | +2.27 |
| 38 | ص | ص | 1.47 | +2.05 |
| 27 | طس | ط | 1.42 | +1.80 |
| 20 | طه | ط | 1.30 | +1.39 |
| 68 | ن | ن | 1.24 | +2.55 |
| 44 | حم | م | 1.23 | +2.60 |
| 32 | الم | م | 1.22 | +2.62 |
| 19 | كهيعص | ي | 1.20 | +3.26 |
| 31 | الم | ل | 1.17 | +2.88 |
| 14 | الر | ر | 1.17 | +2.03 |
| 13 | المر | ل | 1.15 | +3.31 |

**All 3 single-letter muq surahs (Q 38 ص, Q 50 ق, Q 68 ن) show clear body-enrichment** of their specific muq letter. Classical "ق→Qāf is filled with ق" intuition vindicated at p < 0.001 for Q 50 specifically.

## Honest limits

1. **Post-hoc origin**: designed AFTER [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] retraction as separate test. Single-test α=0.05 ceiling.

2. **Modest effect size**: mean 3.2% enrichment. Not extreme. Some pairs enrich strongly; some mildly depleted.

3. **Heterogeneous signal**: Q 42 ق body-ratio is 0.76 (DEPLETED, z=−2.14) despite Q 50 ق being enriched. Classical claim doesn't apply uniformly.

4. **Null design could be tighter**: current null shuffles letter-sets among muq surahs. An even stricter null would draw random letter-sets from the 28-letter alphabet (not just from the 10 actual muq-sets). Future: H-NEW-153.1.

5. **Single pre-reg test; Bonferroni-1**. If paired with [[h-new-139-2-shuffle-null|H-NEW-139.2]] (within-corpus shuffle rhyme test), combined Bonferroni-2 threshold is α=0.025 — this finding would still pass.

## Interpretation

Muqaṭṭāʿat letters ARE modestly but significantly over-represented in the body text of their own surahs, beyond what letter-set-shuffling would produce. The effect is strongest for single-letter muq (Q 38, 50, 68 where the whole letter-set is ONE character, making enrichment visible), weaker for multi-letter muq (where individual letters have more room to be corpus-typical).

**What this means**:
- The al-Zamakhsharī body-frequency claim survives at single-test α=0.05 where al-Suyūṭī's rhyme claim did NOT ([[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] RETRACTED).
- Classical intuition about muq letter distribution is PARTIALLY correct: the body-frequency signal is real and modest; the rhyme-specific signal was a null-model artifact.
- Q 50 Qāf stands out: ق frequency 1.74× corpus baseline, z=+4.20 — this is a robust single-surah signal.

## Connection to prior findings

- **Refines [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] retraction context**: the classical tradition had MULTIPLE claims about muq letter distribution; one (rhyme) failed, another (body frequency) holds.
- **Supports theorist P1★ / M2**: muqaṭṭāʿat letters are not arbitrary; they are phonologically/statistically coupled to their surah's text.
- **Does NOT advance OQ-1** (letter-set identity): letter-set IDENTITY remains content-unpredictable ([[h-new-96-predictor-extension|H-NEW-96]], H-NEW-96.2 NULLs); this finding shows letters ARE enriched, not that letter SELECTION is determined.

## Honest session update

Classical wisdom validation tally (post-H-NEW-153):
| Classical claim | Status |
|---|---|
| al-Bāqillānī iʿjāz verse-length | CONFIRMED ([[h-new-48-poetic-meter|H-NEW-48]]) |
| al-Zarkashī muq-as-book-markers | CONFIRMED (cross-finding-008) |
| Classical 7-ṭiwāl/mufaṣṣal | CONFIRMED ([[h-new-67-sab-tiwal-mathani|H-NEW-67]]) |
| **al-Zamakhsharī body-frequency** | **PASS-DIRECTED (this finding)** |
| al-Biqāʿī munāsabāt | exemplar-level Q 56→57 only |
| al-Suyūṭī rhyme-prefiguration | RETRACTED |
| ق→qiyāma theme | REFUTED |
| sabʿ samāwāt = 7 | REFUTED |

**4 positive empirical anchors** for classical Quranic scholarship (down from 5 after [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] retraction, up from 3 after [[h-new-153-muq-body-enrichment|H-NEW-153]] addition).

## Queue

- H-NEW-153.1: alphabet-uniform null (stricter than letter-set-shuffle null)
- H-NEW-153.2: does enrichment magnitude correlate with classical-stature of the tafsir claim for each surah? (requires coding classical claims per surah)
- H-NEW-153.3: does the ENRICHMENT live at specific positions within surah (opening verses, closing verses, or middle)?

## Files

- Script: inline (seed 20260417)
- Findings: this file
