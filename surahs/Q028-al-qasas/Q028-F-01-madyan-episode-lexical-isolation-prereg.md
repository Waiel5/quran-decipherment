---
finding_id: Q028-F-01
title: Q 28:22-28 Moses-Madyan-water episode lexical isolation (hapax-payload + token-uniqueness)
date_locked: 2026-05-07
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q028-novel-findings
alpha_bon: 0.01
direction: ONE-SIDED-UPPER
status: PRE-REGISTERED
specialist: Q028-al-qasas-specialist
verdict: TBD
---

# Q028-F-01 — Madyan-episode lexical isolation pre-reg

## 1. Hypothesis

The Q 28:22-28 Moses-Madyan-water-marriage episode is the corpus' only extended treatment of Moses' Madyan exodus and is a self-contained narrative block. We pre-register that under the default rules-tuple `(no-tashkeel, orthographic-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`:

**H1 (locked, one-sided upper-tail):** The orthographic-hapax density of Q 28:22-28 (= number of corpus-orthographic-hapax tokens in vv. 22-28 / total tokens in vv. 22-28) **exceeds** the median orthographic-hapax density of every other contiguous 7-verse window in Q 28 (88 − 7 + 1 = 82 candidate windows).

**H2 (locked, one-sided upper-tail):** Q 28:22-28 contains **≥ 3** orthographic-tokens that are **corpus-wide hapax legomena** (≤ 1 attestation outside the window).

**H3 (locked):** The token *مدين* (Madyan) and forms `وَمَدْيَنَ` / `مدين` concentrate ≥ 50 % in Q 28 vs. corpus.

## 2. Direction-locking

H1 direction: 7-verse window 22-28 hapax-density > median(82 windows). Lower-tail or null = NULL with full prominence.
H2 direction: count ≥ 3. Lower = NULL.
H3 direction: Q 28 share ≥ 0.50. Lower = NULL.

## 3. Method

- Source: `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.
- Tokenizer: split on whitespace after stripping Quranic-pause markers `[ۖۗۚۛۜ۞۩ۘ]`.
- Hapax = orthographic-exact-token with ≤ 1 attestation in the entire corpus, including the verse of interest. Strict orthographic, no lemma/root collapsing.
- Permutation null for H1: random sample 10 000 contiguous 7-verse windows in Q 28 (population = 82, exhaustive enumeration; report observed-rank).
- For H3: orthographic substring-match of `مدين` with prefixes `و`, `ل`, `ب`, `ف`, then per-surah counts; pre-committed Q 28 ≥ 50 % of corpus-total.

## 4. Test family + Bonferroni

Family: Q028-novel-findings, k = 5 (this surah's pre-registered novel tests F-01 … F-05).
α_Bonferroni = 0.05 / 5 = **0.01** per test (in cases where H is probabilistic — H1).
H2 is a deterministic count threshold (≥ 3); H3 is a deterministic share + permutation.

## 5. Pre-committed acceptance / failure

- **H1 PASS**: observed window-rank ≤ 4 of 82 (top 5 %) AND p_perm < 0.01.
- **H2 PASS**: ≥ 3 corpus-hapax tokens in vv. 22-28.
- **H3 PASS**: Q 28 ≥ 50 % of `مدين`-token attestations.
- **Aggregate VINDICATED**: ≥ 2 of 3 sub-claims pass.
- **Aggregate NULL**: 0 sub-claims pass.

## 6. MW protections

- MW-1: window-length matched (7 verses) — no length confound.
- MW-2: 10 000 perms (exhaustive 82-window enumeration).
- MW-3: alternative-window-length sensitivity = report 5-verse and 9-verse window ranks (secondary, no acceptance threshold).
- MW-5: positive control = randomly-shuffled-Q28 verses (hapax density should not concentrate).
- MW-6: token-orthographic vs lemma-rule-tuple comparison (sensitivity report).
- MW-7: not invoked (test is pre-registered, not post-hoc).

## 7. Garden-of-forking-paths

- Window choice fixed at vv. 22-28 BEFORE observation (matches narrative-block boundary identified in tafsir tradition: ولما توجه تلقاء مدين … قال ذلك بيني وبينك). Justification: this is the universally-recognized Madyan-episode boundary in al-Ṭabarī, Ibn Kathīr, al-Rāzī, al-Qurṭubī, al-Biqāʿī. See `03-tafsir-survey.md`.
- Hapax definition fixed at orthographic-exact-token, ≤ 1 corpus attestation, BEFORE observation.
- 50 % threshold for H3 chosen as a clean structural threshold (majority share); pre-committed.

## 8. Output

- `surahs/Q028-al-qasas/csv/Q028-F-01.json`
- `surahs/Q028-al-qasas/06-novel-findings.md` § F-01

## 9. Pre-reg SHA

To be SHA-256-hashed at file-lock time and embedded in the runner script.
