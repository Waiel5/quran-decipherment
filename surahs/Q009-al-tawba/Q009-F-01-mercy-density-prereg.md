---
finding_id: Q009-F-01
prereg_date: 2026-04-28
prereg_type: rules-tuple-stable corpus-percentile audit
status: PRE-REGISTERED
---

# Q009-F-01 — Mercy-vocabulary density audit (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: Q 9 al-Tawba's per-1000-token mercy-vocabulary density (root r-ḥ-m, "rHm" in QAC Buckwalter) is **at or below the lower-quartile** of the 114-surah distribution (rank ≤ 28 of 114, i.e. percentile ≤ 25).

This is the empirical correlate of the classical (al-Bayhaqī, Ibn al-ʿArabī, ʿAlī b. Abī Ṭālib via al-Suyūṭī's *al-Itqān* nawʿ 7) "war-context-incompatible-with-mercy → no basmala" claim.

**Direction**: rank-from-bottom (low density). LOCKED before observing.

## 2. Null hypothesis

**H0**: Q 9 mercy-density rank is uniformly distributed in {1..114}; the probability of rank ≤ 28 is exactly 28/114 ≈ 24.6%.

## 3. Rules-tuple

- corpus: `quran-text/quran-no-tashkeel.json` (Hafs, no-tashkeel)
- tokens: orthographic word split on whitespace
- root index: `data/morphology/root-index.json` (QAC v0.4)
- root-of-interest: `rHm` (Arabic ر-ح-م, Buckwalter rHm)
- density: 1000 × (Q9-occurrences) / (Q9-token-count)
- ranking: descending — "rank 1" = highest density. We test for LOW rank-from-top → HIGH rank-from-bottom.
- Report Q9 rank-from-top out of 114 (1=most-mercy-dense; 114=least-mercy-dense).

## 4. Pre-committed thresholds

| Outcome | Q9 rank | Verdict |
|:--|:--|:--|
| Q9 rank ≥ 87 (bottom-quartile, low density) | rank 87-114 | **VINDICATED** classical claim |
| Q9 rank in 29-86 (middle) | | **NULL** |
| Q9 rank ≤ 28 (top-quartile, HIGH density) | | **DIRECTIONAL VIOLATION** — falsifies the no-basmala-because-no-mercy classical claim |

## 5. Bonferroni correction

Family k = 5 pre-registered Q9 audits (F-01 through F-05). α_corrected = 0.05/5 = 0.01.

## 6. Method

```python
# pseudocode
qd = json.load('quran-no-tashkeel.json')
ri = json.load('root-index.json')
for s in 1..114:
    wc[s] = len(' '.join(verses).split())
    rhm_count[s] = count of attestations in ri['rHm'] with surah==s
    density[s] = 1000 * rhm_count[s] / wc[s]
sorted_desc = sorted(density.items(), key=lambda x: -x[1])
q9_rank = position of surah 9 in sorted_desc (1-indexed)
```

## 7. Replication

- Cross-validate density with regex-search on `quran-min-tashkeel.json` for surface forms (الرحمن, الرحيم, رحمة, etc.).
- Cross-validate with QAC stem-tokens from `data/morphology/quranic-corpus-morphology-0.4.txt` filtered to ROOT=rHm and `surah=9`.

## 8. Pre-commit

This pre-reg is finalized. SHA256 will be embedded in the run script; the run script will halt if the pre-reg has been modified after run-time.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
