---
finding_id: h-new-35-length-autocorr
phase: B
status: MIXED — strong primary ρ(1) signal (z=+13.13 vs phase-shuffle null) but classical al-Sakkākī īqāʿ interpretation only partially supports novelty: Quran ρ(1)=0.137 is nearly identical to Jahiz prose ρ(1)=0.146, so the autocorrelation is NOT distinctively Quranic vs Arabic prose. Bukhari hadith-reports show NEGATIVE ρ(1)=−0.152 (novel side-finding)
date: 2026-04-13
rules_tuple: (no-tashkeel, hafs-kufan, character-length-cleaned-verse, weighted-per-surah)
classical_claim: al-Sakkākī Miftāḥ al-ʿUlūm pp. 527-540 on īqāʿ — Quranic verse-length sequences should exhibit rhythmic-memory autocorrelation decaying with lag
null_models:
  - phase-shuffle within each surah (1000 perms, preserves surah-length-distribution + per-surah multiset of verse-lengths, destroys ordering)
  - baseline comparison: Bukhari-noquran ḥaddathanā-split hadith-reports
  - baseline comparison: Jahiz-hayawan sentence-split
bonferroni_k: 3
seed: 20260414
author: computational-tester
---

# H-NEW-35 — Verse-length autocorrelation as rhythmic-memory signature

## Classical claim

al-Sakkākī *Miftāḥ al-ʿUlūm* pp. 527-540 discusses *īqāʿ* (rhythm) as a
foundational feature of Quranic prose, distinguishing the cadence of the
text from ordinary kalām. A natural quantitative operationalization: verse
length should display short-range positive autocorrelation — adjacent verses
should be more similar in length than distant verses — and this rhythmic-
memory should decay monotonically with lag.

## Pre-registered sub-tests (Bonferroni k=3, α_bon=0.0167)

- **(a)** Quran weighted ρ(1) z > +2.58 vs phase-shuffle null
- **(b)** Strict monotonic decay ρ(1) > ρ(2) > ρ(3) > ρ(4) > ρ(5)
- **(c)** Quran ρ(1) differs from BOTH Bukhari AND Jahiz via Fisher z-diff
  |Δ| > 2.58

## Operationalization

For each surah, extract the sequence of verse-lengths (character count of
Arabic letters in cleaned verse text). For each lag k ∈ {1..5}, compute
Pearson ρ(k) per surah (using surahs with n_verses > k). Take the
weighted mean ρ(k) across surahs with weight = (n_verses − k).

Null: for each perm, shuffle verse-lengths uniformly within each surah,
recompute weighted-mean ρ(k). Repeat 1000 times.

Baselines: extract sentence-length sequences from Bukhari-noquran (split on
ḥaddathanā / ʾakhbaranā report-markers, since Arabic hadith texts use no
punctuation) and Jahiz-hayawan (split on period/question-mark/newline).

## Results

### Quran weighted-mean autocorrelation

| lag k | ρ(k) |
|---|---|
| 1 | **0.1368** |
| 2 | 0.0960 |
| 3 | 0.0676 |
| 4 | 0.0185 |
| 5 | 0.0345 |

Note: ρ(4) < ρ(5) (slight uptick), breaking strict monotonic decay.
Loose decay ρ(1) > ρ(5) holds (0.137 > 0.034).

### Phase-shuffle null (1000 perms, within-surah)

| lag k | observed | null μ | null σ | z | p_emp |
|---|---|---|---|---|---|
| 1 | 0.1368 | −0.0023 | 0.0106 | **+13.127** | 0.0000 |
| 2 | 0.0960 | −0.0023 | 0.0118 | **+8.34** | 0.0000 |
| 3 | 0.0676 | −0.0022 | 0.0122 | **+5.74** | 0.0000 |
| 4 | 0.0185 | −0.0021 | 0.0130 | +1.59 | 0.0520 |
| 5 | 0.0345 | −0.0018 | 0.0133 | **+2.73** | 0.0030 |

Primary signal at lag 1 is overwhelming (z=+13.13, p_emp<0.001).

### Baseline comparison (full-corpus autocorrelation)

| corpus | n sentences | mean length | ρ(1) |
|---|---|---|---|
| Quran (verses) | 6,236 | — | **0.1368** (weighted) |
| Bukhari hadith-reports | 16,698 | 118.1 | **−0.1521** |
| Jahiz sentences | 48,936 | 29.1 | **0.1456** |

### Fisher z-diff (Quran ρ(1) vs baselines)

| comparison | z-diff | |Δ| > 2.58? |
|---|---|---|
| Quran vs Bukhari | **+19.464** | PASS |
| Quran vs Jahiz | **−0.666** | **FAIL** (Quran ≈ Jahiz) |

## Verdict breakdown

| sub-test | result | interpretation |
|---|---|---|
| (a) ρ(1) z > +2.58 vs phase-shuffle | **PASS (z=+13.127)** | Strong rhythmic-memory signal |
| (b) strict monotonic decay ρ(1..5) | **FAIL** | lag 4→5 inverts (0.019 → 0.034) |
| (b) loose decay ρ(1) > ρ(5) | PASS | 0.137 > 0.034 |
| (c) differs from BOTH baselines | **FAIL** | Quran ρ(1) ≈ Jahiz ρ(1) |

**Joint strict verdict: FAIL**

**Joint loose verdict: FAIL** (sub-c still fails)

## Interpretation

The Quran does exhibit pronounced positive verse-length autocorrelation at
short lag, and this autocorrelation is astronomically unlikely under a
within-surah phase-shuffle null (z=+13 is a ~10⁻³⁹-level effect). Verse
length is NOT rhythmically independent — adjacent verses cluster in length.

However, the novelty-vs-prose claim fails in two respects:

**1. Strict monotonic decay breaks at lag 4→5**. The autocorrelation does
decay from lag 1 to lag 4 (0.137 → 0.019), but then slightly rebounds
at lag 5 (0.034). This small non-monotonicity may reflect period-5
structural patterns (e.g., quintet-like rhyme groupings in some surahs,
or the structural spacing of formulaic phrases) but is NOT consistent
with al-Sakkākī's idealized monotonic-memory decay.

**2. Quran ρ(1) matches Jahiz almost exactly** (0.137 vs 0.146, Fisher
z-diff −0.67). Sentence-length autocorrelation appears to be a general
feature of Arabic prose, not uniquely Quranic. The pre-registered sub-(c)
differentiation fails because Quran ρ(1) is statistically
indistinguishable from Jahiz's *Kitāb al-Ḥayawān*.

The classical al-Sakkākī īqāʿ thesis is therefore **partially confirmed
within-Quran** (there IS rhythmic memory) but **not supported as
distinctively Quranic** — Jahiz's prose shows the same short-range
length autocorrelation. If classical balāgha literature holds that
īqāʿ is distinctively Quranic, this measurement-level evidence does
not support that stronger claim.

## Unexpected novel side-finding: Bukhari NEGATIVE ρ(1)

The Bukhari-noquran ḥaddathanā-split sequence shows ρ(1) = **−0.1521** —
a moderate NEGATIVE autocorrelation of hadith-report lengths. This means
successive hadith reports tend to ALTERNATE long and short, rather than
cluster. Proposed mechanism:

- Hadith-report structure is typically [isnad — chain of transmitters]
  + [matn — the text of the prophetic saying].
- Isnad lengths are highly variable (some reports have 3-link chains,
  others 7+ links).
- Editorial ordering in the Ṣaḥīḥ Bukhari chapters tends to juxtapose
  a report with a long isnad against a short summary-report (ikhtiṣār)
  or a cross-reference, producing systematic alternation.
- Aggregated over 16,698 ḥaddathanā-segments, this alternating pattern
  yields a robust negative lag-1 correlation.

This is not the hypothesis being tested in H-NEW-35, but it is a
genuinely novel and publishable observation about hadith-editorial
style — Bukhari's length-alternation is the opposite of prose's
length-clustering. **Worth a follow-up test H-NEW-35A** to characterize
the mechanism in isnad/matn decomposition.

## Per-surah ρ(1) heterogeneity (descriptive)

Not formally tested, but the weighted mean hides substantial per-surah
variance. Quick scan of first/last verse lengths suggests:

- **Meccan short surahs** (Q 78-114): small surahs amplify per-surah ρ(1)
  because the formulaic rhyme constraint locks verse length to tight
  windows (e.g., Q 113 al-Falaq has 5 verses all of similar length).
- **Medinan long surahs** (Q 2, Q 4, Q 5): have more variable verse
  lengths and likely smaller per-surah ρ(1).

A per-surah ρ(1) histogram and correlation with surah length/period
would be an instructive follow-up but not part of this pre-reg.

## Garden of forking paths (disclosed)

- **Length metric**: Arabic-letter count (not word count, not grapheme
  cluster count). Word-count autocorrelation would likely give similar
  qualitative results but quantitatively different.
- **Lag range 1-5**: pre-registered. Larger lags (6-10) not tested;
  strict decay pattern might continue or not.
- **Weighted mean with w = (n − k)** is the variance-optimal weighting
  for lag-k autocorrelation, but an unweighted (per-surah equal-weight)
  mean would down-weight long surahs and up-weight short ones.
- **Null model**: within-surah phase shuffle preserves surah-level
  verse-length distributions (correct control). An across-surah shuffle
  would be wrong here because it would destroy surah-length pattern.
- **Bukhari split method**: ḥaddathanā / ʾakhbaranā / وحدثنا / وأخبرنا
  are the four high-frequency report-markers. Other markers
  (e.g., *ʿan*, *sami'tu*) were not used — these split reports at
  intra-isnad boundaries which would be too fine-grained.
- **Jahiz split method**: period/question-mark/newline/double-space.
  Jahiz's *Kitāb al-Ḥayawān* has modern-edition punctuation, so this
  works. For un-punctuated classical texts this method would fail.
- **Fisher z approximation** assumes r is sampled from a sufficiently
  large n. N_Quran_pairs ≈ 6,122 (hafs-kufan minus lag=1 terms per
  surah); N_Bukhari=16,697; N_Jahiz=48,935. Large enough for Fisher z.

## Limits

1. **Cannot disentangle ρ(1) from rhyme-scheme driven length constraints**.
   Quranic rhyme groups tend to lock verse-final syllables, which
   correlates strongly with verse length. A rhyme-controlled autocorr
   is not computed here.
2. **Surah-level heterogeneity** not reported. Per-surah ρ(1) values
   could be used to test period-specific īqāʿ claims (early-Meccan
   vs Medinan).
3. **Only one baseline each**. A broader corpus set (Muʿallaqāt, Ibn
   Isḥāq Sīra, Ibn Qutayba Adab al-Kātib) would test the "general
   Arabic prose" claim more robustly.
4. **No test against Quranic prose after phase-shifting by surah**
   (which would separate within-surah rhythm from cross-surah structure).
5. **Bukhari negative ρ(1) mechanism is hypothesized, not proven**.
   A direct isnad-length / matn-length decomposition is needed to
   confirm the alternating-isnad-matn-length story.

## Followup hypotheses

- **H-NEW-35A** (proposed): decompose Bukhari's negative ρ(1) into isnad
  vs matn length autocorrelations; predict isnad and matn length each
  have positive autocorr but their sum has negative autocorr due to
  editorial interleaving.
- **H-NEW-35B** (proposed): partial correlation of ρ(1) controlling for
  rhyme-class; if Quran ρ(1) vanishes after rhyme-controlling, the
  al-Sakkākī īqāʿ is really a rhyme-epiphenomenon.
- **H-NEW-35C** (proposed): per-surah ρ(1) vs revelation period
  (Meccan early/middle/late, Medinan); if early-Meccan ρ(1) is sharply
  higher, this is consistent with formulaic-rhythm theories of early
  Quranic composition.

## Verdict

**MIXED** — pre-registered joint test FAILS, but the primary effect
(sub-a ρ(1) z=+13) is so large that the finding cannot be discarded.
The honest summary is: Quranic verse-length autocorrelation is real and
strong, but it is not distinctively Quranic (Jahiz matches closely),
and the detailed lag-decay structure is not strictly monotonic. The
al-Sakkākī īqāʿ reading is partially vindicated as a description of
Quranic rhythm but does NOT support the stronger claim that īqāʿ
distinguishes Quranic prose from secular Arabic prose.

The most interesting novel finding in this test is the
**hadith-editorial length alternation** in Bukhari — a negative
autocorrelation that is itself an interpretable feature of the
Ṣaḥīḥ's compositional method.

## Files

- Script: `scripts/h_new_35_length_autocorr.py`
- Output: `findings/phase-b-hypotheses/csv/h-new-35.json`
- Seed: 20260414
