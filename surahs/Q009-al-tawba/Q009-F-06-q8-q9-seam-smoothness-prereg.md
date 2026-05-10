---
finding_id: Q009-F-06
prereg_date: 2026-05-09
prereg_type: corpus-percentile rank-test
status: PRE-REGISTERED
---

# Q009-F-06 — Q 8 → Q 9 mushaf seam smoothness (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: Despite the basmala-omission and the Companions' historical uncertainty about whether Q 8 and Q 9 were a single surah, the Q 8 → Q 9 canonical-adjacency cost (FR-TSP residual, H-NEW-720) is in the **corpus-SMOOTH set** — defined as **top 30% smoothest seams** (rank-smooth ≤ 34 of 113, where rank-smooth = 1 is the smoothest seam in the mushaf).

This is the empirical correlate of al-Biqāʿī's (*Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*) thematic-couplet reading of Q 8 al-Anfāl and Q 9 al-Tawba: both Medinan war-context surahs (Badr/Ḥunayn ↔ Tabūk-expedition + treaty-revocation), forming a *tanāsub* pair.

**Direction**: rank-smooth ≤ 34. LOCKED before observing the H-NEW-720 delta_raw.

## 2. Null hypothesis

**H0**: Q 8 → Q 9 rank-smooth is uniformly distributed in {1..113}; probability of rank ≤ 34 = 34/113 ≈ 30.1%.

## 3. Rules-tuple

- source: `findings/phase-b-hypotheses/csv/h-new-720.json` `per_adjacency` array.
- field: `delta_raw` (penalty for forcing the canonical adjacency in TSP)
- ranking: ascending — rank 1 = smallest delta_raw = smoothest seam.
- Q 8 → Q 9 corresponds to the entry with `s=8` (pair=[8,9]).

## 4. Pre-committed thresholds

| Outcome | rank-smooth | Verdict |
|:--|:--|:--|
| Q 8-Q 9 rank-smooth ≤ 34 (top 30% smoothest) | 1-34 | **VINDICATED** — al-Biqāʿī thematic-couplet supported |
| Q 8-Q 9 rank-smooth in 35-80 | 35-80 | **NULL** |
| Q 8-Q 9 rank-smooth ≥ 81 | 81-113 | **FALSIFIED** — seam is structurally NOT smooth |

## 5. Bonferroni correction

Family k = 8 pre-registered Q 9 audits (F-01 through F-07). α_corrected = 0.05/8 = 0.00625.

## 6. Method

```python
data = json.load(open('h-new-720.json'))
pa = data['per_adjacency']
sorted_smooth = sorted(pa, key=lambda e: e['delta_raw'])
q8_q9 = next(e for e in pa if e['s']==8)
rank = sorted_smooth.index(q8_q9) + 1
# Compare against threshold 34
```

## 7. Replication

- Compare to Q 9 → Q 10 (s=9), which by Q009-F-03 ranks #4 most-expensive (rank-smooth ≈ 110/113). Asymmetric seam behavior is a sub-finding.
- Cross-reference against H-NEW-720's `top10_expensive` and `bottom10_cheap` lists.

## 8. Honest note

A pre-commit violation here (e.g., rank-smooth in mid or expensive region) would mean al-Biqāʿī's thematic-couplet reading is NOT supported at the FR-roots-distance level, complementing the prior FALSIFICATION of Ibn ʿAbbās's stronger "one surah" claim in [[Q008-F-01]] / [[h-new-890-numerical-reaudit]]. This is a finer-grained test: we are NOT asking whether Q 8 and Q 9 are duplicates; we are asking whether the SEAM between them is locally cheap.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
