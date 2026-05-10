---
finding_id: Q009-F-07
prereg_date: 2026-05-09
prereg_type: corpus-percentile rank-test
status: PRE-REGISTERED
---

# Q009-F-07 — Q 9 long-Medinan jurisprudential signature (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: Q 9 al-Tawba's verse-mean-length (words per verse) is in the **top-10 of the corpus** (rank ≤ 10 of 114) by words/verse.

This is the empirical correlate of the classical observation (al-Suyūṭī *al-Itqān* nawʿ 4 on *ṭiwāl/mufaṣṣal* classification; al-Zarkashī *al-Burhān* *al-nawʿ al-thālith*) that Medinan surahs containing extensive jurisprudential prose (sharīʿa rulings, *aḥkām*, treaty-revocation, *hudna*-language, *jizya*-rulings, hypocrite-discourse) have markedly longer mean verse-length than Meccan eschatological/short-verse surahs. Q 9's content profile — Tabūk-expedition critique, treaty-language, *aḥkām al-jihād*, *fadāʾiḥ al-munāfiqīn* — predicts long jurisprudential prose verses.

**Direction**: rank ≤ 10 by mean-words-per-verse. LOCKED before observation.

## 2. Null hypothesis

**H0**: Q 9 rank by words/verse is uniformly distributed in {1..114}; probability of rank ≤ 10 = 10/114 ≈ 8.77%.

## 3. Rules-tuple

- corpus: `quran-text/quran-no-tashkeel.json` (Hafs-Kufan, no-tashkeel, orthographic-words).
- per-surah words-per-verse = (total whitespace-separated tokens across all verses of the surah) / (verse count).
- Q 9 verse count: 129 (Hafs).
- ranking: descending — rank 1 = highest mean words/verse.

## 4. Pre-committed thresholds

| Outcome | Q 9 rank | Verdict |
|:--|:--|:--|
| Q 9 rank ≤ 10 (top-10 longest verse-mean) | 1-10 | **VINDICATED** |
| Q 9 rank in 11-30 | 11-30 | **NULL/DIRECTIONAL** |
| Q 9 rank > 30 | 31-114 | **FALSIFIED** — Q 9 does NOT have the long-Medinan jurisprudential verse-length signature |

## 5. Bonferroni correction

Family k = 8 pre-registered Q 9 audits (F-01 through F-07). α_corrected = 0.05/8 = 0.00625.

## 6. Method

```python
quran = json.load(open('quran-no-tashkeel.json'))
wpv = []
for s in quran:
    total = sum(len(v['text'].split()) for v in s['verses'])
    nv = len(s['verses'])
    wpv.append((s['id'], total / nv))
sorted_desc = sorted(wpv, key=lambda x: -x[1])
q9_rank = next(i+1 for i,e in enumerate(sorted_desc) if e[0]==9)
```

## 7. Replication

- Cross-validate on `quran-min-tashkeel.json` and `quran-full-tashkeel.json` for rules-tuple stability.
- Cross-reference top-10 against revelation-order to confirm Medinan dominance.

## 8. Honest note

This is a coarse first-moment test on verse-length. It does NOT distinguish jurisprudential prose from narrative-extended prose; both contribute to long verses. The verdict-direction reflects ONLY whether Q 9's verse-length is unusually high; the further claim that it is *jurisprudentially-driven* is interpretive and rests on the content analysis in `02-content-analysis.md`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
