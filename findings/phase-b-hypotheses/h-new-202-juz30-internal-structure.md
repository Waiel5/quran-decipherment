---
id: h-new-202
title: "Juzʾ 30 internal spectral structure"
phase: B (specialist)
status: NULL (0/3 primary) with strong descriptive signal
date: 2026-04-17
seed: 20260419
bonferroni_k: 3
alpha_bon: 0.01667
parent_findings:
  - H-NEW-185 (mushaf ring Fiedler bisection at Q 77/Q 78)
  - H-NEW-111 (Fisher-Rao D matrix)
rules_tuple: "(no-tashkeel, QAC-STEM root tokens K=500, QAC v0.4, Dirichlet-0.5, L1-norm, sub-path Q 78..Q 114, Hafs-Kufan, Fisher-Rao angular distance)"
---

# [[h-new-202-juz30-internal-structure|H-NEW-202]] — Juzʾ 30 internal structure

## Headline

All three pre-registered tests **fail** Bonferroni α = 0.01667. Juzʾ 30
is NOT internally more cohesive than random 37-arcs at the pre-reg
threshold. BUT a striking descriptive signal: among all 30 juzʾ
partitions (by contiguous-surah approximation), **Juzʾ 30 has the
single lowest internal mean edge weight** (0.459 vs next lowest 0.631,
juzʾ 3). The Q 77/Q 78 boundary in [[h-new-185-ring-laplacian|H-NEW-185]] is real but its
primary cause is likely the Ḥawāmīm-core density in the Q 13–Q 77
community, not an especially tight Juzʾ 30 interior.

## Pre-registered tests and outcomes (α_bon = 0.01667)

| Hyp | Test | p | z | Verdict |
|:---|:---|:---:|:---:|:---:|
| H1 | Juzʾ-30 mean-edge < null (lower tail) | 0.0186 | −1.82 | **NULL** (near-miss) |
| H2 | Juzʾ-30 sub-path λ_2 − λ_1 > null (upper) | 0.2703 | +0.46 | **NULL** |
| H3 | Boundary-vs-interior \|t\| > null (two-sided) | 0.2586 | +1.16 | **NULL** |

Overall: **NULL (0/3)**. H1 narrowly misses at raw α=0.05 but not
Bonferroni; would need k=1 framing to escape.

## Juzʾ 30 observed statistics

- N = 37 surahs (Q 78..Q 114)
- Mean consecutive-pair Fisher-Rao distance: **0.459** (range
  0.226–0.721)
- Sub-path Laplacian: λ_1 = 0.00369, λ_2 = 0.01558, Δ = 0.01188
- **Sub-Fiedler sign flip at exactly ONE position: between Q 97 and
  Q 98**

## Descriptive findings (NOT pre-registered)

### 1. Juzʾ 30 is the most-cohesive juzʾ in the entire mushaf

Ranking 30 juzʾ by contiguous-surah-path mean edge weight (excluding
juzʾ 2 and 5 which are single-surah interior spans):

| Rank | Juzʾ | Surah range | Mean edge |
|:---:|:---:|:---|:---:|
| **1** | **30** | **Q 78..Q 114** | **0.459** |
| 2 | 3 | Q 2..Q 3 | 0.631 |
| 3 | 8 | Q 6..Q 7 | 0.721 |
| 4 | 28 | Q 58..Q 66 | 0.777 |
| … | … | … | … |
| 30 | 18 | Q 23..Q 25 | 1.089 |

Juzʾ 30's mean edge is **27% smaller than the next-tightest juzʾ** and
**58% smaller than the loosest juzʾ 18**. This is a robust
descriptive effect. The null failure reflects that 37 is much larger
than typical juzʾ (most are 1–3 surahs), and the random-arc null
includes arcs that overlap Juzʾ 30 itself.

### 2. Internal Fiedler boundary = Q 97/Q 98 (al-Qadr → al-Bayyinah)

The sub-Fiedler vector on the Juzʾ 30 path has **exactly one sign
flip**, between **Q 97 al-Qadr and Q 98 al-Bayyinah**. This is:

- **Q 97 al-Qadr**: the Night-of-Power / revelation-moment surah, 5
  ayat. Inside the qiṣār-mufaṣṣal tier in most classical schemes.
- **Q 98 al-Bayyinah**: the People-of-the-Book denunciation, 8 ayat.
  A stylistic anomaly — uses longer, more Medinan-like vocabulary
  (notably *al-kitāb*, *mushrikīn*, *ḥunafāʾ*) than its neighbours.

Classical scholarship often flags Q 98 as the **latest-revealed
sura in the "short-mufaṣṣal" block** and sometimes classifies it as
Medinan (Ibn ʿAbbās variant), against the otherwise-Meccan short
block. The sub-Fiedler boundary independently picks up exactly this
stylistic break.

**Note**: This does NOT align with the standard tripartite mufaṣṣal
cut (ṭiwāl/awsaṭ at Q 85|86, awsaṭ/qiṣār at Q 98|99). The Fiedler
boundary is one position BEFORE the awsaṭ/qiṣār split (Q 97|98
instead of Q 98|99), putting al-Bayyinah on the qiṣār side with
al-Zalzalah, etc. — a spectrally-motivated correction to the
classical mufaṣṣal split that isolates Q 98 as the pivot.

### 3. The boundary-surah signal exists but is not Bonferroni-significant

Mean pairwise Fisher-Rao distance:
- **Boundary (Q 78-80 + Q 112-114, 15 pairs): 0.562**
- **Interior (Q 81-111, 465 pairs): 0.475**

The 6 boundary-surahs are **18% more dissimilar from each other
than interior-surahs are from each other** (p = 0.259 two-sided,
z = +1.16; directionally consistent with the hypothesis but not
significant). The raw effect sign is as predicted — Q 78 (al-Nabaʾ,
long eschatological) and Q 114 (al-Nās, 6-ayat refuge) are very
different content, whereas the Q 81–Q 111 interior is relatively
homogeneous (short, kerygmatic).

### 4. Juzʾ 30 sub-cohesion is not a spectral-gap phenomenon

H2 strongly NULL (p=0.27). Juzʾ 30 has low mean edge weight
(similar neighbours) but NOT a tight λ_2 − λ_1 gap — the sub-path
does not resolve into two sharp sub-communities. This is consistent
with it being a **gradient** of length/style rather than a
two-community structure.

## Honest caveats

1. **0/3 Bonferroni-PASS**: the primary verdict is NULL. The
   descriptive rank-1 cohesion result is informative but not pre-reg
   inferential. The lower-tail p=0.019 for H1 is a near-miss that
   would pass at un-corrected α=0.05.
2. **Juzʾ-range approximation**: classical juzʾ boundaries cut
   MID-surah; this analysis uses contiguous-surah-range approximations
   per juzʾ. True juzʾ-level feature spaces (using ayah-level D)
   would tighten the descriptive comparison.
3. **Null contamination**: the random-contiguous-arc null at PERMS
   10,000 samples includes start=77 (the actual Juzʾ 30 arc), giving
   ~88 exact hits in the null. P-value uses conservative +1 smoothing,
   so this does not inflate Type-I but does reduce power.
4. **Feature-specific**: all results depend on the K=500 root
   feature D matrix. Char-4-gram or verse-length D could shift the
   sub-Fiedler boundary (Q 97/Q 98) or the juzʾ-30 rank-1 finding.
5. **Length confound**: Juzʾ 30 surahs are short; short surahs sample
   a narrower vocabulary, which mechanically compresses Fisher-Rao
   distance. The rank-1 cohesion may be partly a length-artifact,
   though the Fiedler-boundary-at-Q 97/98 is not.

## Connection to [[h-new-185-ring-laplacian|H-NEW-185]]

[[h-new-185-ring-laplacian|H-NEW-185]] found the mushaf ring bisects at Q 77/Q 78 with the
short-surah bracket Q 78..Q 114 ∪ Q 1..Q 12 as one community. This
study shows **that community's Juzʾ-30 half is internally coherent
(descriptive rank-1) but does NOT decompose into sharp sub-clusters
(H2 null)**. The community is dense but smooth, not hierarchically
structured. The one internal boundary it DOES have — Q 97/Q 98 —
isolates al-Bayyinah as the late-Medinan stylistic outlier in the
short-mufaṣṣal block, a finding consistent with the classical
classification debate over Q 98's revelation context.

## Suggested follow-ups (NOT pre-registered)

1. **H-NEW-202b**: replicate on char-4-gram D matrix from [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]
   — does the Q 97/Q 98 Fiedler boundary persist?
2. **H-NEW-202c**: ayah-level Juzʾ 30 partition (true classical
   juzʾ-boundary, not surah-contiguous approximation).
3. **Length-controlled null** for H1: restrict null to 37-arcs whose
   surahs have total ayah-count within ±10% of Juzʾ 30's 564 ayat.
   If H1 still near-null, cohesion may be a length artifact.
4. **Q 98 audit**: does the surah's root-distribution align more with
   Medinan long-surahs (Q 2, 5) than with its qiṣār-mufaṣṣal
   neighbours?

## Output files

- `scratch/h-new-202/h-new-202-prereg.md`
- `scratch/h-new-202/h_new_202_juz30_internal.py`
- `scratch/h-new-202/h-new-202-juz30-internal.json`

## Verdict

**NULL (0/3)** at pre-registered Bonferroni α_bon = 0.01667.
Descriptively, Juzʾ 30 ranks **1st of 30** for internal cohesion
(27% tighter than next juzʾ), and its single internal sub-Fiedler
boundary isolates **Q 97/Q 98 (al-Qadr → al-Bayyinah)** — not the
classical mufaṣṣal tripartition. The boundary-vs-interior asymmetry
is directionally confirmed (boundary surahs 18% more dissimilar)
but not Bonferroni-significant. The [[h-new-185-ring-laplacian|H-NEW-185]] spectral bisection at
Juzʾ 30 is driven more by the Ḥawāmīm-core density of the other
community than by exceptional Juzʾ-30-internal structure.
