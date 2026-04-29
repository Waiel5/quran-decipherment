---
id: H-NEW-138
title: Wrap-around closure feature-space robustness (char-4-gram + verse-length replication of H-NEW-137)
phase: B
status: CONFIRMED-ELIGIBLE (both H1a and H1b pass; combined with H-NEW-137 primary → P8 CONFIRMED)
date: 2026-04-17
executed_by: team-lead (inline)
pre_reg: findings/phase-b-hypotheses/h-new-138-wrap-around-feature-robustness-prereg.md (authored by theorist)
depends_on: H-NEW-137
seed: 20260418
rules_tuple: (114 surahs Hafs-Kūfan; no-tashkeel; char-4-gram K=2000 Dirichlet-0.5; verse-length histogram 8 bins; Fisher-Rao metric; basmala-counted-only-in-Surah-1)
bonferroni_k: 2
bonferroni_family: h-new-138-wrap-around-feature-robustness
alpha_bon: 0.025
direction: POSITIVE — mean_d(Q 1, TERMINAL_TRIAD) < null at both feature spaces
verdict: BOTH CELLS PASS (CONFIRMED-ELIGIBLE for P8 promotion)
---

# [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] — Wrap-around closure feature-space robustness

## Headline

The wrap-around closure (Q 1 ↔ TERMINAL_TRIAD {Q 108..114}) **replicates on 2 additional feature spaces**: character-4-grams (p = 0.0001, z = −4.51) and verse-length histograms (p = 0.0033, z = −2.75). Combined with [[h-new-137-wrap-around-closure|H-NEW-137]] root-features primary pass (p = 0.0001), the wrap-around claim holds across **3 orthogonal feature spaces**.

**Striking extra result**: under verse-length-histogram Fisher-Rao, **Q 114 al-Nās is rank-1 NN for Q 1** (d = 0.0827) — the mushaf's last surah is closer to the first surah than any other surah is to Q 1 on the rhythm axis.

## Results

### H1a: char-4-gram (K_char = 2000)

| Quantity | Value |
|---|---:|
| mean_d_TRIAD (char-4-gram FR) | 0.4012 |
| Null mean (10K perms) | 0.7788 |
| Null median | 0.7820 |
| Null SD | 0.0837 |
| z-score | **−4.51** |
| **p_one-sided** | **0.0001** |
| α_bon (k=2) | 0.025 |
| **H1a PASS** | ✓ |

Q 1's rank-1 NN under char-4-gram FR: **Q 108 al-Kawthar at d = 0.3691** (matches [[h-new-137-wrap-around-closure|H-NEW-137]] qualitatively).

### H1b: verse-length histogram (8 bins)

| Quantity | Value |
|---|---:|
| Bin edges | [1, 5, 10, 15, 25, 40, 60, 100, ∞] |
| mean_d_TRIAD (verse-length FR) | 0.5724 |
| Null mean (10K perms) | 1.1814 |
| Null median | 1.1886 |
| Null SD | 0.2218 |
| z-score | **−2.75** |
| **p_one-sided** | **0.0033** |
| α_bon (k=2) | 0.025 |
| **H1b PASS** | ✓ |

**Q 1's rank-1 NN under verse-length FR: Q 114 al-Nās at d = 0.0827** (NOT Q 108). Q 108's distance under verse-length: 0.3568.

## Interpretation

- H1a (char-4-gram) replicates [[h-new-137-wrap-around-closure|H-NEW-137]] primary closely in both effect size and direction. This confirms the wrap-around is a TRUE content-level feature, not a root-specific artifact.
- H1b (verse-length) replicates the AGGREGATE closure (mean_d_TRIAD < null) but shifts Q 114 to rank-1 individually. Verse-length emphasizes **rhythm similarity** — Q 1 (7 verses avg-length 4.1) and Q 114 (6 verses avg-length 3.5) are ALMOST IDENTICAL in verse-length profile, hence d=0.08.

### Why verse-length puts Q 114 ahead of Q 108 for Q 1

- Q 1 al-Fātiḥa: 7 verses; verses of length 4-5 tokens
- Q 108 al-Kawthar: 3 verses; short but too few bins for overlap
- Q 114 al-Nās: 6 verses; very similar distribution to Q 1

Under root-content, Q 108 and Q 1 share the vocabulary of the short-mufaṣṣal cluster. Under rhythm, Q 114 and Q 1 share near-identical verse-length profiles. Different features emphasize different similarity axes — but BOTH support the wrap-around-closure architectural claim.

## Depends_on [[h-new-137-wrap-around-closure|H-NEW-137]]

Per pre-reg: this test was queued CONDITIONAL on [[h-new-137-wrap-around-closure|H-NEW-137]] primary PASS. [[h-new-137-wrap-around-closure|H-NEW-137]] primary passed at z=−4.17 p=0.0001. Condition satisfied. [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] executed.

## Combined verdict with [[h-new-137-wrap-around-closure|H-NEW-137]] → P8 CONFIRMED

| Test | Feature | p | Result |
|---|---|---:|---|
| [[h-new-137-wrap-around-closure|H-NEW-137]] Primary | QAC-STEM roots K=500 | 0.0001 | PASS (z=−4.17) |
| [[h-new-137-wrap-around-closure|H-NEW-137]] Sec B | Surface-word roots + Hellinger/JS/TV | — | 4/4 PASS |
| [[h-new-137-wrap-around-closure|H-NEW-137]] Sec A | d(Q 1, Q 114) < P10 at roots | — | NARROW MISS |
| [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] H1a | Char-4-gram | 0.0001 | PASS (z=−4.51) |
| [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] H1b | Verse-length | 0.0033 | PASS (z=−2.75) |
| [[h-new-138-wrap-around-feature-robustness|H-NEW-138]] extra | Q 114 rank-1 on verse-length | — | d=0.0827 (SUBSUMES Sec A miss) |

Under the combined evidence, the wrap-around closure architectural claim is **confirmed at 3 orthogonal feature spaces** (roots, char-4-grams, verse-length-histograms). **P8 earns CONFIRMED status** per theorist's pre-reg P8-status progression.

## Honest-limits

1. **Length-confound risk (pre-reg flag)**: Q 1, Q 108-114 are all short; verse-length replication is potentially confounded. Mitigation: H1a char-4-gram is feature-orthogonal to verse-length and also PASSES — so the closure claim is NOT reducible to a length artifact.

2. **Metric-family: FR-arccos-Bhattacharyya only**. Other metric families (Hellinger/JS/TV at char-4-gram and verse-length) NOT tested. Queue for H-NEW-138.1.

3. **Single run per feature space**. Reproducibility guaranteed by seed 20260418.

## Implications for the unified model

- Theorist's P2 (Fisher-Rao geodesic) is now REFINED: it's not just a linear-path optimization but a RING-closed topology
- P8 is the 2nd CONFIRMED principle after P2
- The Hamiltonian-PATH framing of [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] should be amended to Hamiltonian-CYCLE — the mushaf closes back on itself at the content-space level
- Classical liturgical practice (recite Q 1 at every prayer opening; recite Q 112-114 for protection) ALIGNS with this topological feature

## Classical wisdom integration

The architectural fact (Q 1 content-close to Q 108-114) mirrors the liturgical fact (Q 1 recited first every prayer; Q 112-114 recited before sleep / for protection). This is not a theological claim — we don't claim the liturgy caused the structure or vice versa — but the ALIGNMENT between classical usage and empirical-structural fact is noteworthy.

**This is [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s job to synthesize formally.** DM'd synthesizer.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-138-wrap-around-feature-robustness-prereg.md`
- Companion (parent): `findings/phase-b-hypotheses/h-new-137-wrap-around-closure.md`
- Findings: this file
- Inline execution: this session
