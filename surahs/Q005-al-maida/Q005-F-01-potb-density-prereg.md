---
finding_id: Q005-F-01
prereg_date: 2026-05-07
prereg_type: per-surah lemma-density rank test
status: PRE-REGISTERED
seed: 20260507
n_perm: 10000
bonferroni_k: 5
bonferroni_family: Q005 deep-dive (5 novel tests F-01..F-05)
alpha_bon: 0.01
rules_tuple: "(no-tashkeel, QAC-LEMMA tokens, QAC v0.4, basmala-counted-only-in-surah-1, Hafs-Kufan, Mashriqi)"
---

# Q005-F-01 — People-of-the-Book vocabulary density (pre-registration)

## 1. Background

al-Rāzī (*Mafātīḥ al-ghayb*, intro to Q 5 sūrat al-māʾida, "khitāb al-yahūd wa-l-naṣārā") asserts Q 5 is the densest *People-of-the-Book* address in the corpus. al-Biqāʿī (*Naẓm al-durar* on Q 5) and al-Suyūṭī (*al-Itqān*, nawʿ 1 on chronology) both attach Q 5 to this register because of its late-Medinan timing (rev #112 Egyptian Standard, Nöldeke #114 LAST). The empirical question: among the 5 corpus-largest Medinan-legal surahs (Q 2, 3, 4, 5, 9), is Q 5's PoTB-vocabulary density per 100 words *in the top 2*?

## 2. Lemma family (FROZEN)

QAC v0.4 lemmas (rules-tuple-default):

| Concept | Lemma (QAC Buckwalter) |
|:--|:--|
| al-yahūd / yahūdī | `yahuwdiy~` |
| al-naṣārā | `naSoraAniy~` |
| al-tawrāh | `t~aworaY`p` |
| al-injīl | `<injiyl` |
| Banī Isrāʾīl | `<isoraA}iyl` |
| al-masīḥ | `{lomasiyH` (lemma form `masiyH`) |
| ʿĪsā | `EiysaY` |
| Mūsā | `muwsaY``` |
| al-ḥawāriyyūn | `HawaAriy~uwn` |

(zabūr is excluded because the QAC lemma `zabuwr` does not occur in Q 5 and corpus total is 3 — too sparse for density rank-stability. ahl al-kitāb is excluded because `>ahol` `+` `kita`b` is a compound construction the QAC lemma index does not flag as a single unit; including it would double-count single tokens. We restrict to single-lemma-token POTB markers.)

## 3. Hypothesis (DIRECTION-LOCKED)

**H1 (primary)**: Q 5 PoTB-density (PoTB-tokens / 100 words) ranks in the **top 2** among the 5 Medinan-legal surahs {Q 2, Q 3, Q 4, Q 5, Q 9}.

**H1' (secondary)**: Q 5 PoTB-density ranks in the **top 5** corpus-wide (all 114 surahs).

## 4. Null

**H0**: Q 5 PoTB-density is no more than the median of the 5-surah Medinan-legal cluster.

## 5. Method

1. For each surah s ∈ [1, 114]:
   - Count total PoTB-lemma tokens from the family above.
   - Word-count via `quran-no-tashkeel.json` whitespace tokenization (rules-tuple-default).
   - Compute density(s) = 100 × tokens(s) / words(s).
2. Rank densities; record Q 5's rank within {Q2, Q3, Q4, Q5, Q9} and corpus-wide.
3. Permutation null: shuffle the 9 lemma counts across all 114 surah-positions (preserving each surah's words), recompute density-rank for the position originally hosting Q 5, repeat 10000× under seed 20260507.

## 6. Pre-committed thresholds

| Outcome | Verdict |
|:--|:--|
| Q 5 ranks 1 or 2 among {Q2,Q3,Q4,Q5,Q9} AND p_perm < α_bon = 0.01 | VINDICATED al-Rāzī PoTB-density claim |
| Q 5 ranks 1 or 2 but p_perm ≥ α_bon | DIRECTIONAL |
| Q 5 ranks ≥ 3 within the 5-surah cluster | NULL |

If primary fails: secondary H1' is reported but **only descriptively** (no promotion above DIRECTIONAL).

## 7. SHA self-verification

The SHA256 of this pre-reg file (computed AFTER finalizing) is embedded in `scripts/Q005_F_01_potb_density.py` and verified at run-time before any computation.

## 8. Garden-of-forking-paths log

- Lemma family was frozen BEFORE running ANY count except the prior eyeball check that confirmed `naSoraAniy~` and `<injiyl` exist as QAC v0.4 lemmas in Q 5. No counts have been observed at the per-surah density level prior to lock.
- The choice of {Q 2, 3, 4, 5, 9} as the 5-surah Medinan-legal comparison set is fixed BEFORE running — these are the al-sabʿ al-ṭiwāl Medinan-classified members + Q 9 (per al-Suyūṭī chronology).
- ahl al-kitāb is excluded by deliberate methodological choice to avoid double-counting single tokens; this is documented as a rules-tuple choice, not a post-hoc adjustment.
- zabūr is excluded for sparseness; documented above.

## 9. Pre-commit locked.
