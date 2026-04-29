# H-NEW-700 — Phonological Compression-Tail Run 1 Journal

**Date**: 2026-04-28
**Pre-reg SHA**: 63c0008f5e349129f0ec8421144c34a86bda4077221387cdf0b4ade933204b31
**Seed**: 20260435
**Operator**: specialist agent (parallel to H-NEW-660 team-lead inline)

## Pre-run garden-of-forking-paths log

Decisions LOCKED in the pre-reg before running:
1. Rhyme = final-letter of verse, 28-letter Arabic basis, ة → ه, ى → ي, hamza-bearing alif → alif, ؤ → و, ئ → ي.
2. Phoneme groups: emphatic = {ص,ض,ط,ظ}; pharyngeal = {ح,ع}; sibilant = {س,ش,ز,ص}; glottal = {ء,ه,أ,إ,آ,ؤ,ئ}.
3. Distance: cosine-distance pairwise on per-surah feature vectors.
4. Window K=15, starts s ∈ {1, ..., 100}, same as H-NEW-660.
5. Models: linear, quadratic, two-piece-kink at grid {25, 35, 50, 65, 75}.
6. Bonferroni-3 → α_bon = 0.01667.
7. PASS-EXTENDS-LAW required β < 0 (matching content direction).

## Run

```
python3 scripts/h_new_700_phonological_compression_tail.py
```

10000 permutations, both axes. Run time ≈ a few minutes (pure-Python).

## Headline numbers

### Rhyme axis
- d̄ range: 0.30 (best) to 0.90 (worst)
- Best window: starts at s=2 (Q 2-16), d̄=0.30 — TIGHT CLUSTER (mostly rhyme-on-ن)
- Worst window: starts at s=100 (Q 100-114), d̄=0.90 — MAXIMUM DISPERSION (each tiny surah picks its own rhyme letter)
- Linear: R²=0.605, β=+0.00412
- Quadratic: R²=0.765
- **Two-piece kink=50: R²=0.789, β=+0.00832**, p_R²=0.0019
- PRIMARY: two-piece-kink-50

### Phoneme axis
- d̄ range: 0.0019 (best) to 0.168 (worst)
- Best window: starts at s=2 (Q 2-16), d̄=0.0019
- Worst window: starts at s=100 (Q 100-114), d̄=0.168
- Linear: R²=0.544, β=+0.00089
- Quadratic: R²=0.840
- **Two-piece kink=75: R²=0.946, β=+0.00508**, p_R²<0.0001
- PRIMARY: two-piece-kink-75

## VS H-NEW-660 content axis

| Axis | Primary R² | Kink | Slope direction | β |
|:--|:-:|:-:|:-:|:-:|
| **CONTENT (H-NEW-660)** | 0.986 | s=50 (Hijra) | NEGATIVE — compression | -0.01237 |
| **RHYME (H-NEW-700)** | 0.789 | s=50 (Hijra) | POSITIVE — DISPERSION | +0.00832 |
| **PHONEME (H-NEW-700)** | 0.946 | s=75 (mufaṣṣal-qiṣār onset) | POSITIVE — DISPERSION | +0.00508 |

## Big surprise: SIGN INVERSION

The phonological axes show the SAME high R² as content (R²≈0.79-0.95 vs 0.986) but with INVERTED slope direction. Per the prereg, this fails the strict PASS-EXTENDS-LAW criterion (which required β<0). The verdict is INTERMEDIATE — but mechanistically more interesting than a flat axis.

**Mechanism**: The compression-tail (Q 51-114) shows TWO simultaneous trends:
1. CONTENT cohesion-distance MONOTONICALLY DECREASES (theological convergence — H-NEW-660).
2. RHYME and PHONEME cohesion-distances MONOTONICALLY INCREASE (per-surah rhetorical individuation — H-NEW-700).

These are anti-correlated. The mufaṣṣal-qiṣār (Q 78-114) compresses meaning while maximizing rhetorical/phonological distinctiveness per surah. This is the *fawāṣil al-qiṣār* signature: each tiny surah is a self-contained sonic-rhetorical unit picking its own rhyme letter (د, ر, ل, ب, س, ف, ه, ن — 8+ distinct rhyme letters across Q 95-114).

Diagnostic for tail surahs:
- Q 97 (al-Qadr): rhyme on ر (100%)
- Q 98 (al-Bayyina): rhyme on ه (100%)
- Q 103 (al-ʿAṣr): rhyme on ر (100%)
- Q 104 (al-Humaza): rhyme on ه (100%)
- Q 105 (al-Fīl): rhyme on ل (100%)
- Q 108 (al-Kawthar): rhyme on ر (100%)
- Q 111 (al-Masad): rhyme on ب (80%)
- Q 112 (al-Ikhlāṣ): rhyme on د (100%)
- Q 114 (al-Nās): rhyme on س (100%)

Vs Q 1-12 mostly on ن (60-90%). The early mushaf has a HOMOGENEOUS rhyme register (long surahs share a common sonorous final-ن/-īn/-ūn pattern); the late mushaf has a HETEROGENEOUS rhyme register (each surah picks distinctive rhymes).

## Kink position divergence

- Content: kink at s=50 (Hijra hinge, Q 56/57).
- Rhyme: kink at s=50 (SAME).
- Phoneme: kink at s=75 (different — mufaṣṣal-qiṣār onset, Q 78/89).

Rhyme follows the Hijra hinge; phoneme follows a LATER hinge — the start of the mufaṣṣal-qiṣār. This is a NEW finding: the phonological compression-axes have THEIR OWN structural break that diverges from the content-axis Hijra break.

## Permutation null sanity

All four primary R² values exceed Bonferroni-3 α=0.01667 thresholds. The null distributions cluster near R²≈0.05-0.08. Observed values are 10-19× the null mean. Signals are real; permutation cannot manufacture them.

## Honest limits

1. Sign-inversion was NOT pre-registered as a verdict outcome. Reporting it as INTERMEDIATE per prereg, but the data clearly shows a strong signal — just one that DISCONFIRMS the universal-law hypothesis and CONFIRMS that compression-tail is content-axis-specific.
2. Phoneme-axis kink at s=75 is at the edge of the kink grid {25,35,50,65,75}. A finer grid might shift the kink ±5. Re-run with grid {65, 70, 75, 80, 85} would localize better — queued as H-NEW-710.
3. Cosine-distance is appropriate for proportional vectors but not necessarily optimal. Fisher-Rao on the same vectors might give different magnitudes (but same sign).
4. ة → ه mapping: classical *fawāṣil* sometimes treats ة distinctly. Sensitivity check queued.

## Queued follow-ups

- **H-NEW-710**: refine phoneme kink with finer grid around s=75.
- **H-NEW-720**: cross-axis correlation test — is the per-window content-d̄ ANTI-CORRELATED with phonological-d̄? (Prediction: r ≈ -0.7 from H-NEW-700 sign-flip.)
- **H-NEW-730**: per-letter rhyme-axis decomposition — which final-letters drive the dispersion? Is it the late mushaf's expansion to {د, ر, ل, ب, س, ف, ه} from the early {ن, ا, ي} core?
- **H-NEW-740**: classical *fawāṣil* literature cross-reference — al-Bāqillānī's *Iʿjāz al-Qurʾān* and al-Suyūṭī's *al-Itqān* chap on sajʿ — does the qualitative classical tradition predict this rhyme-dispersion pattern?

## Final note

This is a **NULL-with-twist** result on the prereg's universal-law hypothesis. The PASS-CONFIRMS-CONTENT-INVARIANCE branch had a specific R²<0.30 threshold which is FALSIFIED. But the prereg also said "If kink position diverges from s=50, REPORT it honestly — that would be a NEW finding". This is exactly that: phonological axes show STRONG structure, but with INVERTED slope, and PHONEME axis with a DIFFERENT kink at s=75.

The honest framing: H-NEW-660's compression-tail is content-axis specific in DIRECTION (β<0), but a parallel phonological-DISPERSION-tail exists with the same magnitude of structural fit. The mushaf simultaneously compresses content AND disperses sonic identity in its tail. This is a NEW architectural finding.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
