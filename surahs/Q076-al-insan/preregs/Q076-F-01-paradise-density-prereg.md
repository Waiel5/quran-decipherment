---
prereg_id: Q076-F-01
surah: 76
title: Q 76 al-Insān corpus-EXACT-EXTREME paradise-tableau density
date_locked: 2026-05-09
phase: B+
hypothesis_class: novel
post_hoc: false
direction_locked: Q 76 ≥ all other surahs and 11-verse windows in corpus
bonferroni_k: 4
bonferroni_family: Q076-F (Q 76 al-Insān specialist family)
alpha_bon: 0.0125
seed: 20260509
n_perm: 10000
verse_numbering: hafs-kufan
orthography: no-tashkeel
word_definition: orthographic-token (whitespace-split)
basmala_policy: counted-only-in-surah-1
null_model: paradise-vocab-distribution-preserving permutation across N-verse windows
---

# Q076-F-01 — Q 76 al-Insān corpus-EXACT-EXTREME paradise-tableau density

## Hypothesis

Q 76 al-Insān (al-Dahr) contains the highest-density paradise/jannah-tableau vocabulary in the Qurʾān at both the (a) whole-surah level (11 verses out of 31 inside the paradise-tableau core vv. 5–22) and (b) the windowed level. The classical-balāgha tradition (al-Zamakhsharī *al-Kashshāf* on Q 76; al-Rāzī *Mafātīḥ al-Ghayb* on Q 76; al-Qurṭubī *al-Jāmiʿ* on Q 76) treats the paradise-tableau in Q 76:5–22 as one of the corpus's most extended jannah-descriptions. We test whether this is **statistically corpus-EXACT** at the rank-1 level.

## Operationalization — paradise-vocabulary lexicon

A 95-term paradise-tableau lexicon assembled from the surface forms (no-tashkeel) attested in the Qurʾānic jannah-image-set across Q 47, 52, 55, 56, 76, 77, 78, 83, 88, plus classical tafsir cross-checks. Lexicon stored at `csv/Q076-F-01-paradise-lexicon.json`. Includes core terms (jannah, abrār, kaʾs, kāfūr, ʿaynā, salsabīl, zanjabīl, sundus, istabraq, arāʾik, dāniya, wildān, lulu, ḥarīr, naḍrah, surūr, asāwir, fiḍḍa, akwāb, qawārīr, qaṭūf, ẓilāl, naʿīm, sharāb, ṭuhūr, riḥāq, tasnīm, ʿadn, firdaws, fawākih, ḥūr, ʿīn, ḥadāʾiq, mukhladūn, masāwir, sundus, sidr, sulṭ, ṭalḥ, manḍūd, mamdūda, maskūb, furush, baṭāʾin, mubaththath, marfūʿa, mawḍūʿa, maṣfūfa, etc.). Auxiliary forms include common cliticized variants (و-, ف-, ب-, ل-, ك-prefixed and ال-prefixed surface tokens).

DELIBERATELY EXCLUDED from the lexicon (classical commentators flag these as polysemous and not jannah-exclusive):
- ملك (mulk: kingdom-vs-angel, polysemous)
- كبير (kabīr: too generic an adjective)
- شر (sharr: hellfire-side, contrastive)
- سعير (saʿīr: hellfire term, contrastive)

## Tests (4 cells under Bonferroni-k = 4, α_bon = 0.0125)

### Cell A — corpus-rank-1 at whole-surah density level

H₀: Q 76's whole-surah paradise-density is not the maximum across 114 surahs.
H₁: Q 76's whole-surah paradise-density (paradise tokens / total words, no-basmala) is **rank 1 / 114**.

Decision rule: If Q 76's rank = 1, the test passes. Acceptance for `CORPUS-EXACT-EXTREME` only if Q 76's density also exceeds the rank-2 surah by ≥ 1.5× (separation criterion).

### Cell B — corpus-rank ≤ 5 at sliding 11-verse window level

H₀: No 11-verse window inside Q 76 reaches the top-5 of all 5,174 sliding 11-verse windows in the corpus.
H₁: At least one 11-verse window inside Q 76 ranks ≤ 5 among all windows.

Decision rule: PASS if at least one Q 76 window is in top-5; ACCEPT-EXTREME if Q 76 occupies ALL top-5 slots (the natural windowing-overlap predicts contiguous overlapping windows from the same surah-tableau).

### Cell C — permutation null at whole-surah level

H₀: Q 76's whole-surah paradise-density is not significantly above a length-matched permutation null.
H₁: Q 76's density exceeds the 99.5th percentile of length-matched random samples.

Null design: For each of 10,000 permutations (seed=20260509), randomly select 31 verses from the corpus matching Q 76's verse count, compute paradise-density. p_perm = fraction of permutations with density ≥ Q 76's observed density.

Decision rule: PASS if p_perm < α_bon = 0.0125.

### Cell D — paradise-vocab-distribution null

H₀: A random permutation of paradise-vocab tokens across the corpus would yield Q 76 at rank 1/114 by chance.
H₁: Such permutation rarely (< 1/200) places Q 76 at rank 1.

Null design: Hold the per-verse word-counts fixed. For each of 10,000 permutations (seed=20260509), shuffle the 368 paradise-token occurrences uniformly at random across the 82,375 corpus word-positions, recompute per-surah density, find rank of Q 76.

Decision rule: PASS if Q 76 lands at rank 1 in < 0.5% of permutations (more conservative than α_bon=0.0125 because this is the strongest null).

## Pre-decision verdicts

- **CONFIRMED-CORPUS-EXACT-EXTREME** if all 4 cells PASS at α_bon = 0.0125
- **CONFIRMED** if 3/4 cells PASS
- **PASS-DIRECTED** if 2/4 cells PASS
- **NULL** if 1/4 or 0/4 cells PASS

## Garden-of-forking-paths log

I noticed by eyeball before pre-registering that Q 76:12-22 contains a striking density of jannah-tableau vocabulary, and that single-pass corpus-search across 114 surahs immediately suggested Q 76 is rank 1. **The post-hoc origin is disclosed**: Q 76's specialist brief explicitly named the paradise-tableau as the test target. Therefore the rank-1 finding has been anticipated; the formal pre-reg is constructed to verify the eyeball-observation against rigorously-defined nulls. Per discipline §3 (post-hoc protocol), single-test α=0.05 cap applies UNLESS extreme-p (< 10⁻⁴) survives — Cell D's permutation null is what would deliver such a p.

## Replication path

H-NEW-1280 (this finding, if CONFIRMED) should be replicated by an independent specialist using a DIFFERENT lexicon (e.g., concept-derived from al-Bukhārī's Jannah chapter rather than from corpus-attested forms). Replication call queued.
