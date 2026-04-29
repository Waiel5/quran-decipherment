---
finding_id: h-new-139-1
title: "H-NEW-139 frequency-weighted null replication (audit-037 flag)"
specialist: specialist-a
date_prereg: 2026-04-17
seed: 20260417
bonferroni_k: 1
bonferroni_family: h-new-139-1-freq-weighted
alpha_bon: 0.05
direction_primary: "POSITIVE — observed 21/29 match count is GREATER than frequency-weighted-null mean. One-sided upper-tail."
parent_finding: h-new-139 (PASS-DIRECTED under uniform null at z=+5.96)
audit_flag_source: audit-037 (adversarial: uniform null overstates effect because fāṣila distribution is non-uniform; ن alone carries 50% of fāṣilas)
pre_committed_expectation: "audit-037 expects z to drop from +5.96 to +3..+4 but still pass α=0.05 single-test"
---

# [[h-new-139-1-freq-weighted|H-NEW-139.1]] — Frequency-weighted null replication

## Motivation

audit-037 flagged a methodological concern with [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s uniform null: the Arabic-alphabet-uniform draw does NOT match the empirical fāṣila-letter distribution, which is heavily skewed toward ن, م, ر, ل, ا (together >85% of all fāṣilas). Random 3-subsets under the uniform null are much LESS likely to include these common letters than random 3-subsets drawn proportionally to fāṣila frequency.

Since the muqaṭṭāʿat letter-sets overlap heavily with the same ن, م, ر, ل set (specifically الم, الر, المر are dense in these common-fāṣila letters), a uniform null OVERSTATES the null expectation of non-match.

This follow-up re-runs [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s test under a frequency-weighted null to calibrate the effect-size.

## Hypothesis

**Primary (H1).** Observed match count (21/29) is GREATER than the frequency-weighted-null mean, under a one-sided upper-tail test with α_bon = 0.05 (single-test, Bonferroni-1).

Secondary descriptive: report the per-surah null match probability under the frequency-weighted draw.

## Pre-committed method

### Data (frozen from [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]])

- 29 muq-opened surahs with canonical openings.
- Per-surah TOP-3 most-frequent verse-final letters (excluding v1 which is the muq-opening verse).
- Global fāṣila-letter frequency distribution (over all 6,236 verses, each verse's final letter after stripping tashkeel/waqf).

### Frequency-weighted null

For each of 29 surahs s with opening-letter-set OPEN(s) of size k_s:
- Draw a random subset of size k_s from the set of all letters in the Arabic alphabet, WEIGHTED BY global fāṣila-letter frequency.
- Compute match(s) = 1 if the drawn subset ∩ TOP3(s) ≠ ∅.
- Sum across 29 surahs.

Null distribution: 10,000 permutations, seed 20260417 (+2 offset from parent [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s seed).

**Technical note on sampling without replacement with weights**: use weighted-reservoir sampling (standard) or equivalently, treat each letter draw as independent-with-renormalization. The latter is equivalent for distinguishable letters and is what I will use for simplicity.

### Frequency source

Global fāṣila-letter frequencies computed from ALL 6,236 verses, NOT filtered to muq-surahs. This is the right reference: the question is "are the MUQ openings matching the TOP-3 more than a random draw from the fāṣila-frequency distribution?" not "more than a draw from the 28-letter alphabet uniform".

## Pre-committed acceptance windows

- **PRIMARY PASS**: p_one_sided_upper < 0.05. Matches the pre-committed expectation that z drops but still passes.
- **PRIMARY NULL**: p ≥ 0.05 → the uniform-null-derived PASS of [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] was an artifact. Publish with equal prominence.
- **Expected outcome per audit-037**: z in [+3, +4] range, p < 0.01, still PASS.

## Garden of forking paths

- Letter-draw: weighted-independent with renormalization. Alternative: weighted-reservoir without replacement. These give slightly different distributions for small subsets. Pre-committing to independent-with-renormalization for reproducibility.
- Reference frequency: global 6,236-verse distribution. Alternative: muq-only corpus frequency. Pre-committing to global (the right reference for "draw from the natural fāṣila distribution").
- K_subset size: same as opening-letter-set size (k_s). This matches [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s parent methodology.

## Post-hoc-noticed disclosure

This replication was dispatched after audit-037's adversarial flag. I did not re-compute the fāṣila frequency or per-surah top-3 before writing this pre-reg; they are inherited from [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]'s script reproduction (which I ran to verify the 21/29 match count).

## Deliverables

1. Pre-reg (this file).
2. Script `scripts/h_new_139_1_freq_weighted_null.py`.
3. JSON `findings/phase-b-hypotheses/csv/h-new-139-1.json`.
4. Findings `findings/phase-b-hypotheses/h-new-139-1-freq-weighted.md`.
5. Journal `journal/h-new-139-1-run-1.md`.
