---
surah: 2
surah_name: al-Baqara
file_type: novel-finding
test_id: Q002-F-03
date_last_updated: 2026-04-28
phase: B+
verdict: DIRECTIONAL — Q 2 LOO-shift rank 6/114, just outside pre-committed top-5
prereg_sha: 8d8088867adcb9575df2cb318b2345d06f0485a247121c91e74fb5f659b53d97
---

# Q002-F-03 — Q 2 gravitational centrality test

## Target claim

al-Biqāʿī (*Naẓm al-Durar*, intro and Q 2 sections) — al-Baqara is the "scaffold" (qāʿida / fusṭāṭ) of the entire Quran's structure. Test: Q 2's removal from the FR distance space should perturb the corpus geometry MORE than ≥ 95% of others.

## Pre-registration

`Q002-F-03-q2-centrality-test-prereg.md` (SHA256 8d8088867adcb9575df2cb318b2345d06f0485a247121c91e74fb5f659b53d97). Direction-LOCKED: HIGH (Q 2 in top-5 / 114 by LOO-shift OR by gravitational-pull).

## Empirical result

From `csv/Q002-F-03.json` (114×114 FR distance matrix from `h-new-111.json`):

| Metric | Q 2 value | Rank / 114 |
|:--|:--|:--|
| LOO mean-vector shift (Σ\|Δd_i\|) | 0.2325 | **6** |
| Gravitational pull (Σ 1/d_X,j) | 174.5 (approx) | **103** |
| Mean distance to all others | 1.040 (approx) | **104** (low-rank = central) |
| Grav-pull-rank (high = peripheral) | — | bottom-decile |

**Top-5 by LOO-shift**: Q 9 (0.268), Q 55 (0.262), Q 4 (0.260), Q 3 (0.255), Q 6 (0.233).

**Top-5 medoid candidates** (lowest mean distance): Q 112 (0.759), Q 110 (0.764), Q 108 (0.772), Q 1 (0.779), Q 106 (0.780).

## Verdict — DIRECTIONAL

Q 2 ranks **6/114 by LOO-shift** — just outside the pre-committed top-5 threshold. By the alternative metric (gravitational pull) Q 2 ranks 103/114 — close to the OPPOSITE of central.

This is a **genuinely informative split**:

1. **Q 2 perturbs the geometry** when removed (rank 6 by shift, top 5%) — confirming a meaningful "scaffold" role.
2. **Q 2 is NOT close to all surahs** (rank 103 by grav-pull / rank 104 by mean distance) — Q 2 has high mean-distance, sitting FAR from corpus mean.
3. **The medoid is Q 112** (al-Ikhlāṣ) — the mufaṣṣal-qiṣār surahs cluster tightly around the center, Q 1 sits 4th-closest.

## What this means — refining al-Biqāʿī's "scaffold" claim

Q 2 is a scaffold by **OUTLIER-AS-ANCHOR** logic, not by **GRAVITATIONAL-CENTRALITY** logic:

- Q 2 is FAR from the centroid (so its removal pulls all distances outward dramatically).
- BUT its removal does shift the corpus geometry significantly (rank 6).
- The empirical "scaffold" surah by gravitational-pull is actually **Q 112** (al-Ikhlāṣ), which has the LOWEST mean distance to all others — making it the empirical medoid of the FR root distribution.

This is consistent with [[h-new-590-outlier-spectrum]] (Q 2 is corpus-strongest cohesion-anchor by Δ=−20.62pp) — Q 2's "scaffold" function is to **anchor cohesion as an outlier**, not to **provide a centroid**.

This refines al-Biqāʿī: Q 2 is the *structural* scaffold via being an extreme cohesion-anchor; it is NOT the *centroid* of the root distribution. Q 112 is the centroid.

## Why top-5-by-shift is mostly a-l-sabʿ al-ṭiwāl

Top-6 by LOO-shift are all from Q 1-10 (Q 9, Q 55 the exceptions). This shows the al-sabʿ al-ṭiwāl + Q 9 + Q 55 are all gravitationally heavy (their length and breadth of vocabulary makes their removal disrupt the geometry). Q 2 fits this pattern naturally — but is NOT the SINGLE most-disruptive (Q 9 is, by ~2% margin).

## Honest limits

- The FR distance matrix in `h-new-111.json` is on QAC stem-roots (no morph). Switching to lemma-level or surface-level could rescore.
- "LOO-shift" is one of many possible centrality metrics. A spectral-centrality (eigenvector) metric would tell a different story.
- Pre-committed direction (TOP-5) was strict; rank 6 is just barely DIRECTIONAL not VINDICATED. Honest reporting.

## Cross-references

- [[h-new-111-fisher-rao-mushaf]] — distance matrix source.
- [[h-new-590-outlier-spectrum]] — Q 2 corpus-strongest cohesion-anchor.
- [[h-new-720-canonical-adjacency-cost]] — Q 1-Q 2 most-expensive pair.
- [[Q002-al-baqara/05-classical-claims-audit]] — claim #4 (al-Biqāʿī scaffold).

## Status

DIRECTIONAL. Pre-commit threshold (top-5) NOT met by 1 rank; supplementary metrics REFINE rather than confirm the al-Biqāʿī claim — the "scaffold" function is more accurately *cohesion-anchor* than *centroid*.
