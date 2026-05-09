---
surah: 39
test_id: Q039-F-02
title: Q 39 — خلص (xlS) root concentration vs corpus baseline
file_type: pre-registration
date_locked: 2026-05-09
seed: 20260509
n_perm: 10000
bonferroni_k: 4
bonferroni_family: Q039-novel-tests
alpha_bon: 0.0125
direction: q39_xls_density_above_corpus
---

# Q039-F-02 — Pre-registration: Q 39 خلص (sincere-devotion) root concentration

## 1. Hypothesis (locked before observation)

Q 39 al-Zumar contains four discrete attestations of the *xlS* root in the doctrinally-load-bearing phrase *mukhliṣīna lahu al-dīn* / *al-dīn al-khāliṣ*: at v.2 (*fa-ʿbud Allāh mukhliṣan lahu al-dīn*), v.3 (*alā li-llāhi al-dīn al-khāliṣ*), v.11 (*qul innī umirtu an aʿbuda Allāh mukhliṣan lahu al-dīn*), v.14 (*quli Allāh aʿbudu mukhliṣan lahu dīnī*). The phrase is the surah's tawḥīd-signature.

cross-finding-012 frames Late-Meccan surahs as employing intensified *qul* + scripture-announcement + tawḥīd-imperative apparatus. Q 39 is the corpus-densest concentrator of the *xlS* root in this specific *mukhliṣ-lahu-al-dīn* lexical frame.

**H1 (direction-locked):** Q 39's per-1000-word density of *xlS* root tokens is HIGHER than the corpus baseline (excluding Q 39) at α_bon = 0.0125 (one-tailed upper-tail under hypergeometric / permutation null).

**H2 (direction-locked, secondary):** The *xlS* root attestations corpus-wide are concentrated in Late-Meccan tawḥīd-cluster surahs (cross-finding-012 Pattern-B); operationalized: ≥ 60% of corpus *xlS* tokens fall in surahs with Nöldeke rank ≥ 65 (Late-Middle Meccan and later).

**Pre-commit violation conditions:**
- H1 reverse: Q 39's xlS density BELOW corpus median → reverse-direction; publish NULL.

**H0:** Q 39's xlS-density is corpus-typical; no Late-Meccan concentration.

## 2. Operational definitions

- Source: `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4).
- Token rule: count distinct entries with `ROOT:xlS` in the FEATURES field; surface form is e.g. *muxoliS*, *xaAliS*, *xal~aSa*, *xulasai*.
- Word denominator: orthographic-token count from no-tashkeel JSON (consistent with project rules-tuple).
- Corpus xlS count: sum across all 114 surahs.
- Q 39 xlS count: 4 (verified pre-reg by direct QAC-trace of v.2, v.3, v.11, v.14).
- Density = (xlS_count / total_words_in_surah) × 1000.

### Test 1 (H1) — Q 39 vs corpus
- Compute Q 39 density and rest-of-corpus density.
- Permutation null: 10,000 shuffles of xlS-token-positions across all 6,236 verses; recompute Q 39's density at each shuffle.
- One-tailed upper-tail p-value.

### Test 2 (H2) — Late-Meccan concentration of corpus xlS
- For each xlS occurrence, identify host surah and look up Nöldeke rank.
- Compute fraction of xlS tokens with host-Nöldeke ≥ 65.
- Compare to chance fraction = (verse-count in surahs with Nöldeke ≥ 65) / 6236.
- Hypergeometric one-tailed.

## 3. Empirical anchors (verified pre-reg)

From QAC trace of Q 39:
- v.2: muxoliSFA (mukhliṣan)
- v.3: xaAliSu (al-khāliṣ)
- v.11: muxoliSFA (mukhliṣan)
- v.14: muxoliSFA (mukhliṣan)

Q 39 has 1177 orthographic tokens (verified from no-tashkeel JSON). Q 39 xlS density = 4/1177 × 1000 = 3.398/1000.

The corpus-wide xlS count and its Nöldeke-distribution are NOT inspected pre-reg; the H1 + H2 directions are locked from doctrinal expectation (Late-Meccan tawḥīd-imperative concentration per cross-finding-012).

## 4. Success / Failure

- **CONFIRMED-DIRECTED**: H1 perm-p ≤ 0.0125 AND H2 hypergeometric p ≤ 0.0125.
- **PASS-DIRECTED**: H1 OR H2 passes; not both.
- **NULL**: Both fail.
- **PRE-COMMIT VIOLATION**: H1 reverse → NULL with `EXPLORATORY-REVERSE`.

## 5. Honest limits

- xlS-root has additional senses (e.g., *khalāṣ* = deliverance, *khalaṣa* = to be pure). Quran-attestations of xlS in non-mukhliṣ senses exist (e.g., *khalaṣū najiyyan* Q 12:80). The H1 test is on root-density, not on the lemma *mukhliṣ* specifically.
- N=4 within Q 39 is small; effect size at the surah level is modest by absolute count even if perm-p is low. Density rank position is a more robust ranking.
- xlS root corpus count is a published fact; the empirical anchor (4 in Q 39, total ~30-something corpus-wide) is approximately known from the QAC concordance, not pre-inspected for this test specifically.

## 6. Bonferroni & rules-tuple

- Family `Q039-novel-tests`, k=4, α_bon = 0.0125.
- Rules-tuple: (no-tashkeel, orthographic-token, graphemes, QAC v0.4 root annotation, basmala-counted-only-in-Q1, Hafs-Kufan).
- Seed 20260509.
