---
id: H-NEW-67
title: al-sabʿ al-ṭiwāl + Fātiḥa-as-Mathānī — top-7-longest enrichment STRONG-PASS; cluster-cohesion marginal
phase: B
status: STRONG-PASS on top-7-longest enrichment (p=0.0001); MARGINAL on shared-prefix cohesion (p=0.030-0.053)
date: 2026-04-16
agent: integrator (specialist hit rate-limit before script)
test: closed-form / 10K random 7-surah subsets
verdict: STRONG-PASS-DIRECTED on length axis
---

# [[h-new-67-sab-tiwal-mathani|H-NEW-67]] — al-sabʿ al-ṭiwāl Cluster Test (RESULT)

## Headline

The classical "al-sabʿ al-ṭiwāl" (7 long surahs per al-Suyūṭī Itqān) — Q 2, 3, 4, 5, 6, 7, plus either Q 9 or Q 10 — is statistically distinguished by being **5 of 7 in the top-7 longest surahs** of the Quran (p = 1.0×10⁻⁴ via 10K-permutation null).

The remaining 2 top-7-longest surahs are Q 26 al-Shuʿarāʾ (227 verses) and Q 37 al-Ṣāffāt (182 verses) — both classically NOT counted as al-sabʿ al-ṭiwāl. The classical 7 are NOT the strict 7-longest (which would include Q 26, Q 37) — they are the 7 longest among the FRONT of the muṣḥaf.

## Detailed results

### Q 2-9 (no Yūnus) reading [2, 3, 4, 5, 6, 7, 9]
- Verse counts: 286, 200, 176, 120, 165, 206, 129 (sum 1,282; mean 183.1)
- Top-7-longest enrichment: 5/7 (p = 0.0001)
- Cluster cohesion (mean pairwise prefix 1.24): p = 0.053 (marginal, fails α=0.05)
- 3/7 are muqaṭṭāʿat-opened (Q 2, 3, 7)

### Q 2-7 + Yūnus reading [2, 3, 4, 5, 6, 7, 10]
- Verse counts: 286, 200, 176, 120, 165, 206, 109 (sum 1,262; mean 180.3)
- Top-7-longest enrichment: 5/7 (p = 0.0001)
- Cluster cohesion (mean pairwise prefix 1.62): p = 0.030 (PASS at α=0.05 unprotected; not Bonferroni)
- 4/7 are muqaṭṭāʿat-opened (Q 2, 3, 7, 10)

The al-sabʿ al-ṭiwāl as "the 7 longest in the muṣḥaf-front" is robustly confirmed; pairwise structural cohesion is marginal.

## Fātiḥa-as-7-mathānī observation

Q 1 al-Fātiḥa has 7 verses with character-lengths [22, 21, 13, 14, 22, 21, 52]:

```
v1: 22 chars / 4 words — Bismillah
v2: 21 chars / 4 words — al-Ḥamd
v3: 13 chars / 2 words — al-Raḥmān al-Raḥīm
v4: 14 chars / 3 words — Mālik yawm al-Dīn (center)
v5: 22 chars / 4 words — Iyyāka naʿbud
v6: 21 chars / 3 words — Ihdinā al-ṣirāṭ
v7: 52 chars / 9 words — ṣirāṭ alladhīna anʿamta...
```

Notable structural observations:
- **v2 and v6 have EXACTLY equal char-length (21)** — equidistant from center v4
- v3 (13) and v5 (22) are not symmetric in length
- v7 (52 chars) is a dramatic capstone — more than 2× any other verse
- v4 "Mālik yawm al-Dīn" (Master of Judgment Day) is the shortest substantive verse (14 chars / 3 words) — the textual CENTER

This is partial symmetric structure: v2≡v6 (length-mirror), v4 as central, v7 as capstone. Not a perfect palindrome but exhibits center-symmetry signals.

The classical "Fātiḥa is microcosm of Quran" claim cannot be tested via shared-prefix here (Fātiḥa is 7 verses, not 7 surahs). Per H-NEW-59 the divine-name encoding hypothesis is NULL. Per [[h-new-65-fatiha-as-dna|H-NEW-65]] (queued) — multi-axis test.

## What this confirms / refutes

### CONFIRMS
- al-sabʿ al-ṭiwāl as "the 7 longest (in the front of the muṣḥaf)" at p = 0.0001
- Either Q 9 or Q 10 reading both PASS the top-7-longest enrichment criterion
- The Fātiḥa shows partial center-symmetry (v2 ≡ v6 lengths)

### REFUTES
- al-sabʿ al-ṭiwāl as a sharp shared-prefix cluster (only marginally significant)
- The al-sabʿ al-ṭiwāl are NOT all 7 of the absolute-top-7 longest (Q 26, 37 are excluded by classical definition)

### FRAMING
- The classical reading is essentially LENGTH-BASED (the 7 longest at the FRONT), not COHESION-BASED. This explains why pairwise prefix is only marginally significant: the surahs share the property "long" but don't share opener formulas (only 3-4 of 7 are muqaṭṭāʿat).
- Q 9 vs Q 10 ambiguity: classically, Q 9 al-Tawba is sometimes treated as continuation of Q 8 al-Anfāl (no Bismillah break), in which case Q 8+9 jointly = 1 surah and Yūnus Q 10 fills the 7th slot. Both readings give equivalent top-7-longest enrichment.

## Cross-finding context

- The al-sabʿ al-ṭiwāl include Q 2, 3, 7 (muqaṭṭāʿat-opened, also in cross-finding-008)
- Q 9 al-Tawba is the unique no-Bismillah surah (cross-references [[h-new-50-bismillah-114|H-NEW-50]] quantification)
- Length is the dominant axis: [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] + [[h-new-46-1-chronology-disentangle|H-NEW-46.1]] already established that muqaṭṭāʿat surahs are dramatically longer; al-sabʿ al-ṭiwāl confirms the classical reading is length-based

## Honest caveats

- 7-surah list pre-locked but TWO competing classical readings tested (Q 2-9 vs Q 2-7+10); both pass top-7-longest. Not post-hoc selected.
- Cluster cohesion via shared-prefix is the SAME instrument used in [[h-new-58b-shared-prefix-pairs|H-NEW-58b]]/c; consistent methodology.
- The Fātiḥa center-symmetry observation (v2≡v6 lengths) is post-hoc-noticed; cannot be elevated without independent confirmation.

## Verdict

**STRONG-PASS-DIRECTED on top-7-longest enrichment (p = 0.0001).**
Cluster-cohesion: MARGINAL (p = 0.03–0.05).
Fātiḥa structural symmetry: OBSERVED-FACT (post-hoc).

Recommendation: the classical al-sabʿ al-ṭiwāl is empirically CONFIRMED as a length-based cluster, not a cohesion-based cluster. The Fātiḥa-7-as-mathānī interpretation requires the [[h-new-65-fatiha-as-dna|H-NEW-65]] multi-axis test for full assessment.
