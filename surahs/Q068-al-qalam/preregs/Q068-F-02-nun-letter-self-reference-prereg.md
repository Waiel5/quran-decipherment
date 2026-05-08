---
finding_id: Q068-F-02
title: "Q 68 al-Qalam — letter ن self-reference frequency in surah body relative to corpus baseline"
date_pre_registered: 2026-05-07
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 1
bonferroni_family: "Q068-F-02 (single test)"
alpha_raw: 0.05
alpha_bon: 0.05
direction: "POSITIVE — Q 68 expected to have HIGHER ن-letter frequency than corpus baseline"
---

# Q068-F-02 — NŪN-LETTER SELF-REFERENCE

## Hypothesis

**The classical claim**: the muqaṭṭaʿ-letter ن at Q 68:1 is the surah's "self-name" (in the same way ق opens Q 50 and ص opens Q 38). If the muqaṭṭaʿ-letter is functionally a *self-reference*, then the letter should appear in the surah body at a rate distinguishable from corpus baseline.

This test is a NUMERICAL-LETTER-DENSITY test: does Q 68's per-letter occurrence rate of ن exceed the corpus per-letter occurrence rate?

## Locked operationalization

For the no-tashkeel orthographic-token Quran:
- **Q 68 ن-rate** = (# ن letters in Q 68 body) / (# all Arabic-letters in Q 68 body)
- **Corpus baseline ن-rate** = (# ن letters in entire corpus excluding Q 68) / (# all Arabic-letters in corpus excluding Q 68)
- Letter inventory: Arabic alphabet, **with hamza-on-alif normalized to alif** (أ → ا, إ → ا, آ → ا) so the ن-count is not biased by alif-orthographic variants.
- Q 68 body = ALL 52 verses (i.e., we include v.1 even though ن is the muqaṭṭaʿ — this is the inclusive operationalization).

## Rules-tuple (LOCKED)

`(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

## Null distribution

**Permutation null**:
- Compute observed Q 68 ن-rate.
- For each of 10,000 permutations: randomly sample, *without replacement*, a contiguous segment of Q 68's letter-count from the rest of the corpus. Compute that sample's ن-rate.
- Empirical p = (# permutations with rate ≥ Q 68 observed) / 10000.

**Parametric backup**: binomial test using corpus baseline rate p_corpus and Q 68's letter total as n; p_value = binomial right-tail of Q 68's observed ن-count given expected k = n × p_corpus.

## Direction (LOCKED)

POSITIVE: Q 68's ن-rate > corpus-baseline ن-rate at p_perm < 0.05 (one-sided).

A REVERSED direction (Q 68 has *less* ن than corpus average) is a pre-commit violation, published as NULL with full prominence per Protocol §1.3.

## Success / failure criteria

| Verdict | Criterion |
|:--|:--|
| **VINDICATED** | p_perm < 0.05 AND Q 68 ن-rate > corpus-rate |
| **DIRECTIONAL** | 0.05 ≤ p_perm < 0.10 AND Q 68 ن-rate > corpus-rate |
| **NULL** | p_perm ≥ 0.10 OR rates equal |
| **DIRECTION_REVERSED** | Q 68 ن-rate < corpus-rate (pre-commit violation) |

## Cross-singleton sibling test (REPLICATION)

For replication context (NOT for Bonferroni — these are independent surah-specific tests pre-registered separately by the Q050 and Q038 specialists):
- Q 50 (ق opener): ق-rate in Q 50 body vs corpus
- Q 38 (ص opener): ص-rate in Q 38 body vs corpus

If all 3 singleton-letter surahs pass on their own letter, that is a coordinated joint-architecture finding (cross-finding ext). If only some pass, the rules-tuple is fragile across singletons. The Q068-F-02 verdict is, however, INDEPENDENT of Q050-F-* and Q038-F-* outcomes.

## Output files

- Pre-reg: this file.
- Script: `scripts/Q068_F_02_nun_letter_self_reference.py`.
- JSON: `csv/Q068-F-02.json`.
- Findings: in `06-novel-findings.md`.
