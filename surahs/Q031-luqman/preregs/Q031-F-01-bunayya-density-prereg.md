---
test: Q031-F-01
title: Q 31 Luqmān-pericope yā-bunayya density vs other yā-bunayya surahs
test_type: corpus-share + per-verse-density double-test
direction_locked: positive (Q 31 corpus-MAX on per-verse density of yā-bunayya within the 5-surah cohort)
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: Q031-luqman-specialist
alpha_bon: 0.025
acceptance_window:
  primary: per-verse density Q 31 ≥ next-densest surah AND p_perm < α_bon
  secondary: corpus-share Q 31 ≥ corpus median of yā-bunayya-bearing surahs
date_locked: 2026-05-09
---

# Q031-F-01 — Pre-registration

## 1. Rationale

Q 31 contains 3 *yā bunayya* (singular father-to-son vocative) tokens at vv.13, 16, 17 within an 8-verse pericope. The corpus has 9 such tokens (after filtering out *yā banī isrāʾīl* and *yā banī ādam* plural-vocatives), distributed across 5 surahs. The pre-registered question: is Q 31's per-verse density of *yā bunayya* the corpus-MAX among the 5 yā-bunayya-bearing surahs?

Cohort:
- Q 2: 1 occurrence in 286 verses (density = 0.0035)
- Q 11: 1 occurrence in 123 verses (density = 0.0081)
- Q 12: 3 occurrences in 111 verses (density = 0.0270)
- Q 31: 3 occurrences in 34 verses (density = 0.0882) — pre-registered prediction MAX
- Q 37: 1 occurrence in 182 verses (density = 0.0055)

Q 12 (Yūsuf) is the natural comparator: also 3 occurrences. Q 31's density advantage is hypothesis-driven by the eponymous didactic-pericope concentration.

## 2. Hypothesis

**H1**: Q 31's per-verse density of yā-bunayya is the maximum among the 5 cohort-surahs.
**H2**: Q 31's corpus-share of yā-bunayya is greater than the per-cohort-median (3/9 = 33.3% vs cohort-median 1/9 = 11.1%).
**H3**: A randomized-distribution null on the 9 yā-bunayya tokens (uniformly redistributed across the 5 cohort-surahs by surah-length-weighted probability) yields Q 31 density ≥ observed density at perm-p < α_bon.

## 3. Method

- Corpus: `quran-text/quran-no-tashkeel.json` (114 surahs, 6,236 verses, locked).
- Tokenization: regex `(?<!\S)يا\s*بني(?!\S)` filtered to exclude *banī isrāʾīl* (next-token contains *إسرائيل*) and *banī ādam* (next-token contains *آدم*).
- Per-surah density: density(s) = count(s) / verse_count(s).
- Permutation null: redistribute the 9 corpus-wide tokens across the 5 cohort-surahs proportional to surah-length (verse-count) — i.e. each surah's expected-count under uniform-density-null = (verse_count(s) / total_cohort_verse_count) × 9.
  - For Q 31: expected = (34 / 736) × 9 = 0.42.
  - Observed: 3.
  - Compute permutation distribution of Q 31 density under 10,000 random redistributions; one-tailed p = P(perm_density ≥ observed_density).

- Bonferroni: k=2 tests (H1 + H3). H2 is descriptive.

## 4. Pre-committed acceptance window

- PASS: per-verse density Q 31 = MAX in cohort AND perm-p < α_bon = 0.025.
- DIRECTIONAL: per-verse density Q 31 = MAX but perm-p ≥ α_bon.
- NULL: per-verse density Q 31 NOT MAX in cohort.
- PRE-COMMIT VIOLATION: Q 31 density < cohort-median (impossible given observed 3/34).

## 5. Garden-of-forking-paths log

- The yā-bunayya construction was identified as a Q 31 distinctive feature in `00-overview.md` §4 BEFORE the pre-reg lock (during empirical-anchor extraction). This is a **post-hoc-noticed** finding per HANDOFF/04-DISCIPLINE.md. Single-test α=0.05 cap applies; verdict ceiling is **PASS-DIRECTED** until INDEPENDENT REPLICATION on a distinct data dimension.
- The filter on plural-vocatives (*banī isrāʾīl*, *banī ādam*) was decided BEFORE looking at the per-surah breakdown; this is the "yā bunayya" target-construction definition, not a post-hoc data exclusion.
- The 5-surah cohort is the closed set of surahs with at least 1 yā-bunayya token; this is data-defined, not data-snooped.

## 6. Honest limits

- The per-verse density advantage is partly a length-effect: Q 31's 34 verses vs Q 12's 111 verses inflates the density. The permutation null controls for this by surah-length-weighting (a longer surah has higher expected count under uniform-density redistribution).
- The eponymous-didactic frame (Q 31's name is Luqmān + the pericope is a didactic discourse) selects-for the vocative-density. This is NOT an independent statistical signal; it is the structural-thematic fingerprint of the surah.
- INDEPENDENT REPLICATION would require a different operationalization: e.g. measuring the density of any didactic-pericope construction (not just yā-bunayya) in Q 31 vs other didactic-pericope-containing surahs.

## 7. Direction lock

LOCKED positive (Q 31 = corpus-MAX on per-verse density within the 5-surah cohort).

## 8. SHA-locking

This pre-reg file's SHA256 will be computed at write-time and verified at run-time. Computed at file-creation-completion.

## 9. Cross-references

- [[surahs/Q031-luqman/00-overview]] §4 — the 5-surah cohort identification.
- [[surahs/Q012-yusuf]] — the co-equal corpus-cohort surah (3/9 yā-bunayya occurrences spread across 111 verses).
- [[surahs/Q037-al-saffat/06-novel-findings]] — Q037-F-01 salām-ʿalā-prophet 4-in-Q37 pre-registration template (this pre-reg follows the same structure).
