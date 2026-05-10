---
finding_id: H-NEW-1570
title: "Chronology-paired surahs inverse-rank lexical-key principle (corpus-wide formalization)"
date_pre_registered: 2026-05-10
status: PRE-REGISTERED
seed: 20260509
n_perm: 10000
bonferroni_k: 5
bonferroni_family: "H-NEW-1570 (5 chronology-adjacent surah pairs)"
alpha_raw: 0.05
alpha_bon: 0.01
direction: "POSITIVE — title-eponymous-root of LATER surah is denser in EARLIER chronology-pair-partner (inverse-rank within shared lexical-key)"
parent_finding: Q068-F-06 (Q 96 rank-1, Q 68 rank-2 by qlm density)
---

# H-NEW-1570 — CHRONOLOGY-PAIRED SURAHS INVERSE-RANK LEXICAL-KEY PRINCIPLE

## Hypothesis (LOCKED before observation)

Q068-F-06 discovered that the title-eponymous root of Q 68 (al-Qalam, revelation #2) — `qlm` —
is **densest** not in Q 68 itself but in Q 96 (al-ʿAlaq, revelation #1), the chronology-adjacent
earlier-revealed surah. The pair (Q 96, Q 68) thus holds the *qlm* key in **inverse rank order**:
the EARLIER-revealed surah at rank-1, the TITLE-BEARING LATER-revealed surah at rank-2.

This pre-reg formalizes the question: is this an idiosyncratic 1-off, or a corpus-wide
phenomenon? We test five chronology-adjacent pairs from classical Suyūṭī/Nöldeke chronology
(`/Users/grey/Downloads/quran/data/revelation-order.csv`) where the LATER-revealed surah is
title-eponymous (its name derives from a distinctive root).

## The five chronology-adjacent pairs (LOCKED)

| pair | early surah (rev #n) | later surah (rev #n+1) | shared lexical key (later surah's title root) |
|:-:|:--|:--|:--|
| 1 | Q 96 al-ʿAlaq (rev #1) | Q 68 al-Qalam (rev #2) | `qlm` |
| 2 | Q 73 al-Muzzammil (rev #3) | Q 74 al-Muddaththir (rev #4) | `dvr` |
| 3 | Q 1 al-Fātiḥa (rev #5) | Q 111 al-Masad (rev #6) | `msd` |
| 4 | Q 81 al-Takwīr (rev #7) | Q 87 al-Aʿlā (rev #8) | `Elw` |
| 5 | Q 93 al-Ḍuḥā (rev #11) | Q 94 al-Sharḥ (rev #12) | `$rH` |

Chronology source: `data/revelation-order.csv` (Tanzil Egyptian Standard + Nöldeke). The five
pairs are pre-committed and will be reverified at runtime against the CSV.

## Operationalization (LOCKED)

For each pair (early, later) and the later-surah title-root R:
1. Extract QAC v0.4 ROOT tokens from `data/morphology/quranic-corpus-morphology-0.4.txt`.
2. For each of the 114 surahs s, compute density_R(s) = (count of ROOT:R in s) / (total QAC root-tokens in s) × 1000.
3. Rank all 114 surahs by density_R(s) descending. Ties broken by raw count, then by surah number ascending.
4. Record rank_early = rank of the early surah; rank_later = rank of the later surah.
5. Pair satisfies the **inverse-rank pattern** iff:
   - rank_early = 1 AND rank_later = 2 AND (rank_early + rank_later) ≤ 5 (trivially satisfied when 1+2=3), AND
   - density_early > density_later strictly (the inverse-rank inequality).

The strict criterion "rank_early=1, rank_later=2" is the exact replication of the Q 96 ↔ Q 68 pattern.

## Rules-tuple (LOCKED)

`(no-tashkeel, QAC v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Null distribution (LOCKED)

For each pair, the **structural background** is: across all 114 surahs, what is the
probability that for a randomly chosen pair of distinct surahs (a, b), a holds rank-1 and
b holds rank-2 in the density ranking of an arbitrary single root?

We compute the corpus-wide null via permutation:
- For each of N=10,000 permutations (seed 20260509):
  - For each pair, randomly select two distinct surahs from {1,..,114} as the "early" and "later" candidates.
  - Test whether the random pair satisfies the inverse-rank pattern for the SAME locked root R.
- Tally the proportion of permutations where ≥ k_obs of 5 pairs satisfy the inverse-rank pattern.

This is a conservative null because the observed pairs are chronology-locked, so the
permutation breaks chronology while preserving root choice.

A secondary null (single-pair-marginal): for a single pair with locked root R, P(random pair
satisfies pattern) = (114 surahs eligible to be rank-1) × (113 eligible rank-2) / (114×113)
= 1/(114×113) per ordered position, but the rank-1+rank-2 slots are deterministic in the data,
so the marginal P = 2/(114×113) per ordered pair sampling. We will report the exact corpus-marginal
via direct permutation.

## Direction (LOCKED before observation)

POSITIVE: ≥ 3 of 5 pairs satisfy the strict inverse-rank pattern (rank_early=1, rank_later=2).

A result of 0 or 1 satisfying pairs = NULL.
A result of 2 satisfying pairs = DIRECTIONAL (insufficient for verdict-PASS).
A reversed direction (no pairs even close — e.g., all later surahs are rank-1 instead of rank-2
when the root appears in both) would be PRE-COMMIT-VIOLATION.

## Success / failure criteria

| Verdict | Criterion |
|:--|:--|
| **PASS-DIRECTED** | ≥ 3 of 5 pairs satisfy strict inverse-rank AND permutation p < α_bon=0.01 |
| **DIRECTIONAL** | 2 of 5 pairs satisfy inverse-rank, OR ≥ 3 pass but p > α_bon |
| **NULL** | 0 or 1 pairs satisfy the inverse-rank pattern |
| **PRE-COMMIT-VIOLATION** | All 5 pairs have rank_later = 1 (title-bearer outranks early-pair-partner consistently — opposite of the principle) |

## Pre-committed structural observations

The locked roots have very different corpus-population properties:

- `qlm` (pair 1): 4 attestations corpus-wide (Q 3, 31, 68, 96) — small-N, BOTH pair-members attest. **Inverse-rank in principle possible AND known from Q068-F-06.**
- `dvr` (pair 2): **singleton** — only attestation at 74:1:2:2. Q 73 has zero `dvr`. **Inverse-rank STRUCTURALLY IMPOSSIBLE — Q 73 has density 0.**
- `msd` (pair 3): **singleton** — only attestation at 111:5:5:1. Q 1 has zero `msd`. **Inverse-rank STRUCTURALLY IMPOSSIBLE — Q 1 has density 0.**
- `Elw` (pair 4): rich root (high attestations across corpus). Need to compute whether Q 81 has any `Elw` tokens. Provisional inspection: Q 87:1 is the only `Elw` attestation in either surah; Q 81 may have zero. **Inverse-rank likely structurally limited.**
- `$rH` (pair 5): 5 attestations (Q 6, 16, 20, 39, 94). Q 93 has zero `$rH`. **Inverse-rank STRUCTURALLY IMPOSSIBLE — Q 93 has density 0.**

This pre-reg ACKNOWLEDGES BEFORE OBSERVATION that 3 of 5 pairs (2, 3, 5) cannot satisfy the
inverse-rank pattern by the locked operationalization, and pair 4 is likely also constrained.
The honest a-priori expectation is that **only pair 1 satisfies** — i.e., a NULL verdict.

This pre-reg is therefore registered as **a falsification attempt** of the corpus-wide
generalization of Q068-F-06. If the result is NULL with 1/5, Q068-F-06 remains an isolated
finding (not a general principle). If by surprise ≥ 3 satisfy, the principle is corpus-wide.

## Methodological-Walls coverage

- **MW-1 (instrument-prior)**: Density metric, QAC v0.4 ROOT, ranking algorithm pre-specified.
- **MW-2 (corpus-prior)**: 10,000-perm null with seed 20260509.
- **MW-3 (alternative-models)**: Strict rank-1+rank-2 criterion (primary). Loose "rank_early < rank_later AND both in top-5" criterion (secondary, reported but not gating).
- **MW-4 (over-fitting)**: No parameters fit; direct enumeration.
- **MW-5 (replication)**: Pair 1 = Q068-F-06 replication. Pairs 2–5 are out-of-sample tests.
- **MW-6 (instrument-control)**: Singleton-root pairs (2, 3, 5) are structural controls.
- **MW-7 (post-hoc cap)**: Bonferroni k=5; α_bon=0.01.

## Output files (LOCKED paths)

- Pre-reg: this file (`findings/phase-b-hypotheses/prereg-h-new-1570-chronology-pair-inverse-rank.md`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-1570.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-1570.json`
- Findings: `findings/phase-b-hypotheses/h-new-1570-chronology-pair-inverse-rank.md`

## Equal NULL prominence statement

If the verdict is NULL, the result will be published with equal prominence as a PASS. A NULL
here means **Q068-F-06 is an isolated structural coincidence, not a corpus-wide principle**,
and that conclusion is just as scientifically valuable as a positive finding.
