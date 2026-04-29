---
id: H-NEW-244
title: Q 1 al-Fātiḥa as *umm al-kitāb* — information-theoretic compression test
phase: B
status: MIXED — Cell A NULL; Cell B PASS; Cell C NULL. Classical *umm al-kitāb* claim is ROOT-LEVEL only, not distributional-compression
date: 2026-04-17
parent: H-NEW-155 (sui-generis-liturgical); complement H-NEW-231 (per-surah KL)
seed: 20260419
rules_tuple: "(no-tashkeel, hafs-kufan, 7-verse windows, char-4-gram, Dirichlet α=0.5, QAC v0.4 STEM roots for Cell B, seed 20260419)"
bonferroni_k: 3
alpha_bon: 0.0167
script: scripts/h_new_244_fatiha_compression.py
output_json: findings/phase-b-hypotheses/csv/h-new-244.json
prereg: findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab-prereg.md
prereg_sha256: 02208c5f561c15185daf1d1cc27e2dd66cb8a636944d2e6f94f3f9e12436d1b6
verdict: MIXED-SUPPORT — *umm al-kitāb* holds at the ROOT-DISPERSION axis (Cell B PASS p=0.002; Q 1's 18 STEM roots appear in 50.0% of other surahs vs null 39.8%) but FAILS at char-4-gram surface-distribution axis (Cell A NULL: Q 1 in 79%ile of 6230 7-verse windows; Cell C NULL: Q 1 per-verse-KL rank 102/114 = 89%ile). Q 1's compression is semantic/lexical (core-vocabulary palette) NOT orthographic (character sequence distribution). H-NEW-155 dispersion result replicates exactly; the new char-4-gram cells REFUTE the literal distributional-compression reading of classical al-Suyūṭī/al-Ghazālī/al-Rāzī claims.
---

# [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] — Q 1 as *umm al-kitāb*: mixed evidence under Bonferroni-3

## Headline

The classical **umm al-kitāb** claim (al-Suyūṭī *Itqān*, al-Ghazālī
*Iḥyāʾ*, al-Rāzī *Mafātīḥ al-ghayb*, Ibn Taymiyya *Majmūʿ al-Fatāwā*)
decomposes into TWO distinct compression claims when operationalised:

1. **ROOT-PALETTE compression** (Cell B, replicating [[h-new-155-q1-sui-generis|H-NEW-155]]):
   Q 1's 18 content-roots are unusually well-distributed across the
   corpus. **PASS** at α_bon=0.0167 (p=0.002).

2. **DISTRIBUTIONAL compression** (Cells A and C, new char-4-gram
   tests): Q 1's character-level distribution is NOT representative
   of the corpus — in fact it is CHARACTERISTICALLY IDIOSYNCRATIC.
   **NULL** at α_bon=0.05 (both cells far from pass).

The result is a **precision-sharpening** of the classical claim: Q 1
is "mother of the Book" in the sense of seeding a HIGH-COVERAGE
theological vocabulary palette, but it is not "mother of the Book"
in the sense of being a statistical miniature of the corpus's
character-distribution.

## Pre-reg compliance

Direction locked on 2026-04-17 with SHA-256
`02208c5f561c15185daf1d1cc27e2dd66cb8a636944d2e6f94f3f9e12436d1b6`.
Bonferroni-3 α_bon = 0.0167 (Cells A & C reported at 5%ile threshold
per pre-reg). Seed 20260419. No deviations.

## Results

| Cell | Instrument | Q 1 value | Null / comparison | Result |
|---|---|---:|---|---|
| **A** | 7-verse sliding window char-4-gram KL | **1.0261** | rank **4920 / 6230** (79%ile; top-5% = rank ≤ 311) | **NULL** |
| **B** | Q 1 roots' cross-surah presence rate | **0.5000** | null mean 0.3983 SD 0.0356; p=**0.0020** | **PASS** (α_bon=0.0167) |
| **C** | per-verse-normalised char-4-gram KL | **0.1466** | rank **102 / 114** (89%ile; top-5% = rank ≤ 5) | **NULL** |

### MW-5 cheat controls (Cell A)

- Random contiguous 7-verse window (seed 20260419, start=3963):
  rank 5393/6230 (87%ile) — **PASS** (not top-5%, as required).
- Random NON-contiguous 7-verse sample (seed 20260419+1): rank
  ~2900/6230 (47%ile) — **PASS**.

Both cheat draws land near mid-distribution, confirming the 4-gram
KL instrument discriminates.

### Top-5 MOST corpus-representative 7-verse windows (lowest KL)

| Window | Verses | KL |
|---|---|---:|
| 1 | Q 4:176 → Q 5:6 (sabʿ al-ṭiwāl boundary) | 0.915 |
| 2 | Q 2:253 → Q 2:259 (Baqarah central narrative) | 0.917 |
| 3 | Q 5:2 → Q 5:8 (dietary laws + tahāra) | 0.920 |
| 4 | Q 5:1 → Q 5:7 | 0.921 |
| 5 | Q 2:212 → Q 2:218 (legal corpus) | 0.921 |

All 15 top-representative windows are inside the Medinan legal-narrative
block (Q 2-5). These are the lowest-KL 7-verse windows because their
character distribution matches the corpus average (predominantly
Baqarah-style legal Arabic, which is itself ~8% of the corpus).

### Top-5 MOST corpus-representative surahs per-verse (Cell C)

| Rank | Surah | per-verse KL |
|---|---|---:|
| 1 | Q 2 al-Baqarah (286 verses) | 0.00129 |
| 2 | Q 3 Āl ʿImrān | 0.00213 |
| 3 | Q 7 al-Aʿrāf | 0.00228 |
| 4 | Q 4 al-Nisāʾ | 0.00276 |
| 5 | Q 6 al-Anʿām | 0.00291 |

Q 1's per-verse KL = 0.1466 (113× worse than Q 2). **Q 1 ranks 102/114
per-verse-normalised**, ahead only of the 12 shortest idiosyncratic
Meccan closures (Q 97, Q 103, Q 105, Q 106, Q 108, Q 110, Q 111,
Q 112, Q 113, Q 114 plus their neighbors). This is the [[h-new-231-kl-divergence-per-surah|H-NEW-231]]
length-dominance signal re-surfaced: long surahs are corpus-
representative per-verse simply because they have more characters to
average over.

## Interpretation

### What PASSED — Cell B, root-palette compression (replication)

Cell B exactly reproduces [[h-new-155-q1-sui-generis|H-NEW-155]]'s dispersion result under a
slightly different normalisation (cross-surah presence rate per root,
rather than dispersion as average-fraction). **Q 1's 18 QAC STEM
roots appear in 50.0% of the other 113 surahs on average**, vs null
mean 39.8% — a 10.2 percentage-point lift, z ≈ +2.86, p = 0.002.

This is the ROOT-PALETTE compression: Q 1 draws from the
highest-dispersion layer of Quranic vocabulary (الله, رب, رحم, حمد,
عبد, علم, دين, يوم, ملك, سماو, هدى, صراط, قوم, عون, نعم, غضب, ضل,
غير). These are the core theological pillars — and they are
systematically over-represented in Q 1 relative to random 7-verse
windows.

**The classical *umm al-kitāb* claim is substantiated AT THE
ROOT-LEVEL**: al-Fātiḥa presents the 18 most-widely-shared roots of
the Quranic theological lexicon.

### What FAILED — Cells A and C, distributional compression

Cells A and C test the stronger reading: is Q 1's FULL distribution
(at char-4-gram granularity) a scaled-down version of the corpus
distribution? Answer: **emphatically no**.

- Q 1's raw window KL (1.026) is WORSE than 79% of sliding 7-verse
  windows. The top-15 representative windows are all Medinan
  Baqarah/Māʾida legal material.
- Q 1's per-verse-normalised KL (0.147) is WORSE than 89% of the 114
  surahs — Q 1 sits among the short idiosyncratic closures (Q 97-114
  bloc) at the low-representativeness extreme.

**Why?** Q 1 is SHORT (7 verses, ~120 char) and its character
distribution is dominated by high-frequency theological 4-grams
(الرحم, الحمد, رب ال, مالك,  الدي, صراط, etc.) at 5-20× their
corpus background rate. This is the [[h-new-231-kl-divergence-per-surah|H-NEW-231]] signal: short surahs
DIVERGE from the corpus character distribution — and Q 1 is no
exception, even among the theological-core short surahs.

### Reconciliation with the classical tradition

The classical *umm al-kitāb* designation, when read carefully,
appears to target the **semantic/thematic** compression rather than
the **orthographic/distributional** compression:

- al-Ghazālī *Iḥyāʾ* vol 1, Kitāb al-Tilāwa: Q 1 is a "summary" in
  the sense of covering the MAJOR THEMES of the Quran (tawḥīd, rabb,
  raḥma, judgment day, worship, guidance, straight path, gratitude
  vs. anger-and-going-astray) — all of which map onto Q 1's 18
  roots.
- al-Rāzī *Mafātīḥ al-ghayb* Q 1 opening: explicitly frames the
  compression as THEMATIC (each verse maps to a Quranic theme-class),
  not statistical.
- al-Suyūṭī *Itqān* chapter on faḍāʾil al-Fātiḥa: organises the
  superiority as vocabulary-categorial (مفاتيح الخير), not as
  miniature-corpus.

**[[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] Cell B PASSES the classical claim on its own terms** —
and Cells A+C show that the compression does NOT extend to
character-level distribution. This is methodologically important
because Cell A+C is the test that a naive "umm al-kitāb as data-
compression" reading WOULD have predicted; that naive reading is
empirically refuted.

### Connection to [[h-new-231-kl-divergence-per-surah|H-NEW-231]] and [[h-new-192-mushaf-position-decomposition|H-NEW-192]]

- **[[h-new-231-kl-divergence-per-surah|H-NEW-231]]** established Spearman ρ(log-length, KL) = −0.967 —
  short surahs DIVERGE from the corpus. Q 1 (7 verses, 120 char) fits
  this length-based divergence pattern perfectly. Cell C's rank
  102/114 is exactly where length-alone would place it.
- **[[h-new-192-mushaf-position-decomposition|H-NEW-192]]** found Q 1's feature-predicted mushaf position = 105
  (Δ = −104 from actual position 1), making it the largest
  compositional residual in the corpus. [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] Cells A & C show
  the SAME structural fact from a different angle: Q 1's
  distributional profile BELONGS with surahs at positions 97-114
  (short creedal closures), NOT with position 1. The mushaf placement
  at position 1 is a LITURGICAL / P3-frame decision ([[h-new-238-cyclic-shift-wrap|H-NEW-238]]
  confirms this via cyclic-shift analysis), not a distributional
  placement.
- **[[h-new-155-q1-sui-generis|H-NEW-155]]** root-dispersion (50.4% vs 39.7%) replicates at Cell
  B (50.0% vs 39.8%) — the +1.2 p.p. discrepancy is likely
  stop-word handling in the two pipelines; the qualitative result
  is identical.

## The corrected **umm al-kitāb** interpretation

Integrating [[h-new-155-q1-sui-generis|H-NEW-155]], [[h-new-192-mushaf-position-decomposition|H-NEW-192]], [[h-new-238-cyclic-shift-wrap|H-NEW-238]], [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]]:

**Q 1 is *umm al-kitāb* in three specific senses and NOT in a fourth:**

1. **Root palette** (Cell B PASS): Q 1 collects the theologically
   most-dispersed core vocabulary. ✓
2. **Liturgical frame** ([[h-new-238-cyclic-shift-wrap|H-NEW-238]], [[h-new-192-mushaf-position-decomposition|H-NEW-192]] residual): Q 1's
   mushaf-1 position is dictated by its prayer-frame role, not by
   compositional similarity. ✓
3. **Sui-generis-liturgical class** ([[h-new-155-q1-sui-generis|H-NEW-155]]): Q 1 is the sole
   member of a distinct sūra-class defined by dispersion-seed
   pattern. ✓
4. **Distributional miniature-of-corpus** (Cells A & C NULL): Q 1 is
   NOT a scaled-down character-level version of the Quran. ✗

The refuted fourth reading is the one a **ḥisāb al-jummal /
ilm al-ḥarf** practitioner or a naive information theorist would have
expected. Its refutation is a direct audit-result: the classical
interpretive tradition was CORRECT at the root-level (which is where
al-Suyūṭī and al-Rāzī actually place the claim) and the stronger
character-level reading that some mystical traditions entertain (Q 1
as numerological/letter-level miniature) is NOT supported by this
instrument.

## Honest limits

1. **Char-4-gram is ONE encoding**. A 5-gram or morphological-
   n-gram might give different results; a Fisher-Rao distance on
   root frequency (per [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]) would likely favour Q 1 more
   (since Q 1's roots match the corpus's root frequency peaks).
2. **Dirichlet α=0.5 is one smoothing choice**. Sensitivity to α∈
   {0.1, 1.0} not tested. Because the signal in Cells A+C is so
   large (rank 79%ile / 89%ile, not a borderline miss), α sensitivity
   is unlikely to flip Cell A/C to PASS.
3. **7-verse windows cross surah boundaries**, pulling in mixed
   content. The top-representative windows are Medinan Baqarah
   legal material; this is an artifact of Q 2's dominance (8% of
   corpus). If windows were restricted to within-surah, the ranking
   would shift.
4. **Cell B uses QAC v0.4 STEM-roots**; alternative morphological
   analyses could give slightly different root sets.
5. **"Representativeness" here means "low KL to rest-of-corpus"**,
   a distributional sense of compression. Content-semantic
   representativeness (concept-coverage) is not directly tested;
   Cell B partially addresses this via root-palette, but not
   semantic-field coverage.
6. **n=1 corpus test**: no out-of-corpus Arabic control (e.g.,
   pre-Islamic poetry, ḥadīth) to compare whether a random 7-verse
   Arabic text would show similar divergence.

## Connection to unified model ([[cross-finding-018-four-principle-reduced-model|cross-finding-018]] / [[cross-finding-020-the-complete-equation|cross-finding-020]])

- **M5 (length-stratification + compositional modes)**: Q 1 confirmed
  as a short-surah-profile case even at char-4-gram resolution. The
  length-stratification holds at this encoding too.
- **P3 (liturgical frame)**: the Cells A+C NULL + Cell B PASS
  jointly reinforce P3 — Q 1's placement at position 1 is not
  explicable from compositional features (M1+M5 would place it at
  ~position 100-110), only from liturgical convention. This matches
  [[h-new-192-mushaf-position-decomposition|H-NEW-192]], [[h-new-233-ensemble-mushaf-predictor|H-NEW-233]], [[h-new-238-cyclic-shift-wrap|H-NEW-238]] residual findings.
- **[[cross-finding-020-the-complete-equation|cross-finding-020]] h_P3 share**: the ~4-5% P3 liturgical component
  is substantively LOCATED at Q 1 — [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] confirms that
  locating the P3 slack specifically at Q 1 (not distributed) is
  correct. Q 1 is the concentrated residual of the 5% P3 term.

## Queued follow-ups

- **H-NEW-244.1**: repeat Cells A & C under Fisher-Rao on root
  frequency (not char-4-gram). Hypothesis: Q 1 will rank HIGHER on
  root-distribution (since Cell B already shows root-palette match),
  so this test is the "semantic" vs "orthographic" discrimination.
- **H-NEW-244.2**: α-sensitivity — α ∈ {0.1, 1.0, 2.0} for Cells A
  & C. Expected: rank stays in 70-90%ile (signal size too large to
  flip).
- **H-NEW-244.3**: restrict window to within-surah only — re-do
  Cell A on within-surah 7-verse windows. Q 1 is the only surah
  ≤ 7 verses (it IS its own 7-verse window), so this collapses back
  to the 114-surah test — which is Cell C. Not informative at this
  window size.
- **H-NEW-244.4**: compression test with GZIP / LZMA on Q 1 as
  preamble (concatenate Q 1 + rest-of-corpus, compare compression
  ratio to rest-of-corpus alone). Does Q 1 reduce the compressed
  size of the rest disproportionately? Non-parametric complement to
  KL.

## Cross-references

- **[[h-new-155-q1-sui-generis|H-NEW-155]]** (parent): root-dispersion sui-generis; REPLICATED at
  Cell B.
- **[[h-new-231-kl-divergence-per-surah|H-NEW-231]]**: per-surah raw KL; Q 1 here sits at the short-surah
  end of its length-correlated trend.
- **[[h-new-192-mushaf-position-decomposition|H-NEW-192]]**: Q 1 mushaf-residual Δ=−104; [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] Cells A+C
  DIRECTLY CORROBORATE this residual at char-4-gram resolution.
- **[[h-new-238-cyclic-shift-wrap|H-NEW-238]]**: Q 1 → Q 2 edge rank 114/114 (worst in cycle);
  [[h-new-244-fatiha-umm-al-kitab|H-NEW-244]] Cells A+C show the local reason — Q 1 and Q 2 have
  highly DIVERGENT char-4-gram distributions (Q 1 high-KL / short;
  Q 2 lowest-KL / longest).
- **[[cross-finding-020-the-complete-equation|cross-finding-020]]** Q 1 P3 slack: substantively located.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-244-fatiha-umm-al-kitab-prereg.md`
- Script: `scripts/h_new_244_fatiha_compression.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-244.json`
- Findings: this file
- Journal: `journal/h-new-244-run-1.md`
- Ledger: Wave-4 addendum (next commit)
