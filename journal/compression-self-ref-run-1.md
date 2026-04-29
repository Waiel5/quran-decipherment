# compression-self-ref-run-1

**Date:** 2026-04-12
**Agent:** compression-self-ref (autonomous research agent)
**Scope:** Task A (compression-based surah structure, novel angle) + Task B (H22 self-reference density test)
**Finding file:** `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/compression-and-self-reference.md`

## What I did

Two linked analyses in one run, both pre-registered in the task prompt.

### Task A — Compression per surah

Computed gzip_ratio (zlib too), LZ76 complexity, and character entropy for all 114 surahs using the no-tashkeel JSON as primary corpus (verses joined with single ASCII spaces; whitespace normalized).

**First null — length-matched verse-shuffle (1000 perms per surah):** preserves each surah's *verse count* but not its character length. Found to be **length-confounded** — z-scores under this null essentially track total character length (long surahs → very-negative z, short surahs → positive z). Documented as a failure mode and kept in the write-up for completeness.

**Second null — length-matched verse-block draw (500 draws per target surah, ±3% length tolerance):** the correct null. Draws random verse subsets from the whole-Quran pool whose total character length matches the target surah. Applied to 19 focal surahs (pre-registered targets + length-extreme cases).

Under the length-controlled null, pre-registered predictions all confirmed:
- Ar-Raḥmān (Q 55): z=−17.77 (strongest compression outlier of all 114 when length-controlled)
- Al-Mursalāt (Q 77): z=−7.01
- Al-Qamar (Q 54): z=−4.55
- Muqaṭṭaʿāt-opening surahs: mean gzip 0.3305 (n=29) vs 0.4383 (n=85), Δ=−0.108

**Sleeper finding:** Ash-Shuʿarāʾ (Q 26) emerges at z=−13.34 under the length-controlled null — the second-strongest refrain-signal after Ar-Raḥmān. Its 8× "prophet-series āya refrain" + 9× Lord-epithet refrain = dual-refrain structure that I did not pre-register but clearly qualifies for the refrain-surah catalog.

### Task B — H22 self-reference density

Ten-lemma inventory pulled from `quranic-self-reference.md`: qurʾān, kitāb, furqān, dhikr, tanzīl, waḥy, āyāt, kalām, mathānī, nūr. Each lemma expanded to all no-tashkeel surface variants (definite, indefinite, case, clitic-prefixed). Al-Rāghib-informed disambiguation:
- kitāb excluded when verse co-mentions Moses/Jesus/Torah/Gospel markers
- dhikr excluded for male-vs-female contexts and "ahl al-dhikr" frames
- nūr included only with revelation-frame co-markers (anzala/rasūl/kitāb/etc.)
- kalām included only when verse also mentions Allāh/rabb
- Others accepted on surface-form match (overwhelmingly Quran-referential)

Tokenized all 6 236 verses; counted per-verse per-lemma occurrences with disambiguation. Phase statistics:
- Meccan: 535 self-ref tokens / 4 613 verses = **0.1160/verse**
- Medinan: 248 / 1 623 = **0.1528/verse**
- Difference M − M = **−0.0368** (Medinan denser — OPPOSITE of pre-registered prediction)

**Null: 2000-permutation label shuffle** across surahs (preserving 86/28 Meccan/Medinan split). Null mean ≈ 0, σ ≈ 0.014. Observed z = −2.60, two-tail p ≈ 0.01; one-tail in the predicted direction: p ≈ 1.

**H22 as stated: REJECTED.**

### Per-lemma decomposition (the real finding)

Ran the label-permutation null *per lemma* (2000 permutations × 10 lemmas). Results:

| Lemma | Meccan/v | Medinan/v | z | p (two-tail) |
|---|---:|---:|---:|---:|
| kitāb | 0.024 | 0.077 | **−3.75** | **<0.001** |
| furqān | 0.000 | 0.003 | −2.11 | 0.056 |
| kalām | 0.002 | 0.006 | −2.02 | 0.053 |
| qurʾān | 0.010 | 0.005 | +1.19 | 0.195 |
| dhikr | 0.016 | 0.007 | +1.54 | 0.090 |
| tanzīl | 0.003 | 0.001 | +1.53 | 0.097 |
| waḥy | 0.001 | 0.000 | +1.02 | 0.263 |
| āyāt | 0.058 | 0.053 | +0.32 | 0.774 |
| mathānī | 0.000 | 0.000 | +0.83 | 0.354 |
| nūr | 0.001 | 0.001 | +0.08 | 0.968 |

**Only kitāb clears Holm-Bonferroni at k=10 (α=0.05 threshold = 0.005).** But the directional split is clean: the three institutional-nouns (kitāb, furqān, kalām) all lean Medinan; the five process-nouns (qurʾān, dhikr, tanzīl, waḥy, mathānī) all lean Meccan; āyāt and nūr are phase-neutral.

This is a novel quantitative confirmation of **Neuwirth 2006 / Ibn ʿĀshūr / al-Zarkashī**: Meccan phase self-names as recitation-event; Medinan phase self-names as institutional Book.

## Prior art sweep

WebSearch hits:
- Ehret 2018 on gzip as Kolmogorov-complexity proxy (methodology foundation)
- Frontiers 2022 on L2 proficiency (compression-based complexity)
- ACL 2023 (Jiang et al.) parameter-free compressor classification
- Neuwirth 2006/2010/2019 on Quran self-referentiality (philological; no quantification)
- Wild 2006 ed. volume on self-referentiality (philological)

**Not found:** any prior peer-reviewed compression/gzip analysis of the Quran. This run appears to be the first.

Kaplan (*Inner Meaning of the Hebrew Letters*) noted but judged non-methodologically-parallel — his framework is Kabbalistic letter-mysticism, not statistical. Closer analogue in our project is `ilm-al-harf-tests.md`.

## Honest verdict

- Task A: CONFIRMED (with methodology caveat about naïve null).
- Task B: H22 REJECTED in stated direction. Replacement finding (phase-by-vocabulary signature) CONFIRMED for kitāb at p<0.001; directional-only for the process/institution split (binomial p≈0.1).

## Issues / follow-ups

- Ash-Shuʿarāʾ should be in the formal refrain-surah catalog; merits dedicated deep-dive to complement `rahman-deep-dive.md`.
- The per-lemma phase result should be re-run with clitic-splitting (via QAC morphology) as a robustness check.
- Self-reference density × muqaṭṭaʿāt-opening correlation (4 of top 5 self-ref-dense surahs open with muqaṭṭaʿāt): worth pre-registering as H22a.
- The complete self-description verse set (≈108 verses) could anchor a new Phase-C analysis — the "metatextual spine."

## Files

- Scripts:
  - `/Users/grey/Downloads/quran/scripts/compression_self_ref.py`
  - `/Users/grey/Downloads/quran/scripts/compression_length_control.py`
  - `/Users/grey/Downloads/quran/scripts/self_ref_per_lemma_phase.py`
- Outputs:
  - `findings/phase-b-hypotheses/csv/compression_per_surah.csv`
  - `findings/phase-b-hypotheses/csv/self_reference_per_surah.csv`
  - `findings/phase-b-hypotheses/csv/compression_self_ref_results.json`
- Finding: `findings/phase-b-hypotheses/compression-and-self-reference.md`
- Seed: 42; deterministic.
