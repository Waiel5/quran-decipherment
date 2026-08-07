---
id: H-NEW-240
title: Per-surah endpoint sequences (first-verse and last-verse) are MORE dispersed than random in canonical mushaf order
phase: B
status: NULL-PRIMARY + OPPOSITE-DIRECTION-POSITIVE (post-hoc, single-test α=0.05 cap per MW-7)
date: 2026-04-17
executed_by: team-lead (inline)
parent: cross-finding-013 (mushaf topological ring); H-NEW-189 (endpoint-inclusio Medinan)
seed: 20260419
rules_tuple: (no-tashkeel; 114 surahs; first-content-verse = v2 for 29 muq surahs else v1; last-verse = final; char-4-gram bag; Dirichlet-smoothed α=0.5; Fisher-Rao arccos-Bhattacharyya; n_perm=500)
bonferroni_k: 2
bonferroni_family: h-new-240-endpoint-sequence
alpha_bon: 0.025
direction: NEGATIVE z pre-committed (canonical endpoint-sequence SHORTER than random)
verdict: NULL primary; post-hoc opposite-direction observation at single-test α cap
---

# [[h-new-240-endpoint-sequence-dispersion|H-NEW-240]] — Endpoint-verse sequences in canonical mushaf order are OVER-dispersed

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## Headline

**Primary pre-committed direction = NULL.**
- First-verse-sequence canonical length 105.12 vs null mean 101.95 (sd 1.32) → **z = +2.40**.
- Last-verse-sequence canonical length 111.21 vs null mean 104.67 (sd 1.13) → **z = +5.76**.
- Pre-committed direction: z < −1.96 (shorter than random) → both cells NULL on the pre-committed axis.

**Post-hoc observation (single-test α=0.05 cap per MW-7)**: the OPPOSITE direction is strongly supported — the canonical mushaf endpoint-sequences are MORE DISPERSED than random. Last-verse sequence at z = +5.76 is a substantial effect; first-verse sequence at z = +2.40 is moderate.

## Motivation

[[cross-finding-013-mushaf-topological-ring|Cross-finding-013]] established the mushaf-at-the-surah-level is a structured Hamiltonian cycle (Fisher-Rao near-geodesic at 11% of TSP optimum; z = −11.46 against random permutation on root features). [[h-new-189-medinan-inclusio|H-NEW-189]] established Medinan surahs have first↔last INTRA-surah inclusio at p<0.0001. Does the meta-sequence of ENDPOINT verses (first-verse-Q1, first-verse-Q2, ..., first-verse-Q114) also exhibit a near-geodesic structure? If endpoint-coherence is a META property of the mushaf, endpoint-sequences should be short vs random.

## Method

1. Extract per-surah first content verse (v2 for 29 muq surahs, v1 otherwise) and last verse.
2. Represent each verse as a char-4-gram bag over its concatenated tokens (no spaces).
3. Fisher-Rao arccos-Bhattacharyya distance with Dirichlet α=0.5 smoothing.
4. Canonical mushaf-order path length = Σ d(v_i, v_{i+1}) for i=1..113.
5. 500-permutation null under random-shuffle of the 114 endpoint verses.
6. Z-score = (canonical − null_mean) / null_sd.

Bonferroni k=2 (one per endpoint type), α_bon = 0.025. Direction pre-committed: negative z. Seed 20260419.

## Results

| Endpoint | Canonical length | Null mean | Null sd | **z** | Direction-match |
|---|---:|---:|---:|---:|:-:|
| First verses | 105.12 | 101.95 | 1.32 | **+2.40** | ✗ (opposite) |
| Last verses | 111.21 | 104.67 | 1.13 | **+5.76** | ✗ (opposite) |

Both primary cells fail the direction-locked pre-reg test. Report NULL on the pre-committed direction.

**Post-hoc (MW-7 single-test α=0.05 cap)**:
- Last-verse z = +5.76 corresponds to p ≈ 10⁻⁸ one-sided above-null. This is substantial.
- First-verse z = +2.40 corresponds to p ≈ 0.008 one-sided above-null.
- The combined opposite-direction signal is strong, but treated descriptively per MW-7.

## Interpretation

1. **The mushaf is arranged for coherence at the FULL-SURAH content level, not at the endpoint-verse level.** The 11% geodesic residual on full-surah Fisher-Rao ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]) does NOT transfer to individual endpoint verses.

2. **Last verses are DELIBERATELY DIFFERENTIATED** (z = +5.76). Possible mechanisms:
   - Closing formulas (e.g., *Allāhu ʿalīmun ḥakīm*, *wa-kāna Allāh samīʿan baṣīra*, etc.) are theologically standardized across surahs but pull toward a narrow divine-name vocabulary that differs from the overall corpus distribution.
   - Khawātim are architectural punctuation marks (al-Biqāʿī *Naẓm al-Durar* emphasis): they END surahs, not THREAD between them. No transition-smoothness pressure.
   - The last-verse-sequence variance-above-random reflects the independent lexical choices that close each surah.

3. **First verses are moderately differentiated** (z = +2.40). Muq openings (14 distinct letter-sets), distinctive oath-formulas (wa-al-ṭūr, wa-al-ʿaṣr), and surah-specific opening formulas pull first verses away from smooth transitions.

4. **This CLARIFIES the mushaf topological ring ([[cross-finding-013-mushaf-topological-ring|cross-finding-013]]):** the ring is a surah-level phenomenon. Each surah's interior content is what links it to neighbors. Endpoints operate as internal-surah signatures, not as cross-surah links.

5. **Connection to [[h-new-189-medinan-inclusio|H-NEW-189]] Medinan-inclusio**: Medinan surahs show first↔last inclusio WITHIN each surah, but NOT between adjacent surahs at the endpoint layer. The inclusio principle is internal architectural, not transitional.

## Honest limits

1. **Primary direction NULL**: the pre-committed test fails. Report honestly.
2. **Opposite direction at single-test α**: post-hoc observation; cannot be treated as independent confirmation. Awaits independent replication with pre-committed opposite direction.
3. **Char-4-gram representation** is one of several encoding choices. QAC-root-based or token-based might give different results. Deferred to H-NEW-240.1 sensitivity.
4. **500-permutation null** is modest. z = +5.76 is well-supported at this N; z = +2.40 less robust.
5. **Endpoint definition**: first-content-verse convention (v2 for muq-openers) follows [[h-new-189-medinan-inclusio|H-NEW-189]]. Robustness to "first ayat always" (including muq opener) not tested.
6. **Not a direct test of [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]**: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] operates at full-surah content level; [[h-new-240-endpoint-sequence-dispersion|H-NEW-240]] operates at single-verse-endpoint level. Different layers.

## Connection to unified model

- **Refines M1 (structured Hamiltonian cycle)**: M1 is a surah-level claim, not an endpoint-level claim. [[h-new-240-endpoint-sequence-dispersion|H-NEW-240]] draws the scope boundary.
- **Refines [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]**: the ring topology operates on full-surah content; endpoint verses contribute as surah-internal signatures rather than ring-building links.
- **Consistent with M5 length-stratification**: compositional modes operate at surah level; endpoint variation is orthogonal to length.

## Queued follow-ups

- **H-NEW-240.1**: sensitivity to encoding (QAC-roots vs char-4-gram vs token).
- **H-NEW-240.2**: does the over-dispersion effect persist if we pair CLOSURE-FORMULA last verses into a "formula canonical form" and test?
- **H-NEW-240.3**: pre-register OPPOSITE direction (+z) in a replication; test on an independent encoding.

## Cross-references

- Parent: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] (mushaf topological ring, surah-level)
- Sibling: [[h-new-189-medinan-inclusio|H-NEW-189]] (Medinan intra-surah first↔last inclusio)
- Applies-to: [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] M1 pillar scope boundary
- Contrast: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] (full-surah Fisher-Rao z=-11.46 same instrument, opposite direction)

## Files

- Script: `/Users/grey/Downloads/quran/scripts/h_new_240_endpoint_sequence.py`
- JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-240.json`
- Findings: this file
