---
id: H-NEW-65
title: Fātiḥa-as-DNA — does Sūrat al-Fātiḥa microcosmically encode the Quran's structural features across 6 axes?
phase: B
status: REFUTED-WEAK (1 of 6 axes Bonferroni-significant; threshold ≥ 2)
agent: h-new-65-specialist
spec_locked_at: 2026-04-15
ran_at: 2026-04-15
bonferroni_family: 2026-04-15-Wave-H-NEW-65-Fatiha-DNA
bonferroni_k: 6
alpha_bon: 0.00833
rules_tuple: (no-tashkeel; word-segment substring + first-letter-of-token; hafs-kufan; 6236 verses; basmala-counted-only-in-surah-1; mashriqi)
seed: 20260416
overall_verdict: REFUTED-WEAK
n_axes_pass: 1
---

# [[h-new-65-fatiha-as-dna|H-NEW-65]] — Fātiḥa-as-DNA: 6-axis microcosm test

## TL;DR

Pre-registered 6-axis test of the classical "Fātiḥa is a microcosm of the Quran" claim. **Verdict: REFUTED-WEAK** — exactly **1 of 6 axes** (semantic theme coverage) crosses the Bonferroni threshold; pre-committed PASS criterion required ≥ 2.

Fātiḥa scores **typically or worse-than-typically** on lexical commonness, rhyme commonness, structural representativeness, gzip cross-compression, and pharyngeal/glottal letter coverage. It does cover all 5 pre-locked theme classes (praise, mercy, judgment, guidance, supplication) — but that is only one axis out of six.

Combined with H-NEW-59 cell-3 (Fātiḥa-as-divine-name-encoder REFUTED at α=0.05, p=0.150), the broader empirical picture **does not support the strong "microcosm" reading** of Fātiḥa as a statistically distinctive encoder of corpus features. Classical exegetical "Mother of the Book" framing should be understood as theological-literary, not statistical.

## Per-axis results (sliding 7-verse-window null, n=6230 windows)

| # | Axis                                  | Direction | Fātiḥa value | Null median | Null q99 | p (1-sided) | α_bon=0.00833 |
|---|---------------------------------------|-----------|--------------|-------------|----------|-------------|----------------|
| 1 | Lexical mean log-token-freq           | UPPER     | 3.0234       | 3.190       | 4.064    | 0.65746     | FAIL           |
| 2 | Semantic theme coverage (5 themes)    | UPPER     | **5 / 5**    | 1           | 4        | **0.00144** | **PASS ***     |
| 3 | Phonetic rhyme LL                     | UPPER     | −9.480       | −9.870      | −4.839   | 0.49149     | FAIL           |
| 4 | Structural KS (vs corpus word-count)  | LOWER     | 0.6787       | 0.4699      | 0.8215   | 0.84703     | FAIL           |
| 5 | Compression gzip-gain (n=1000 null)   | UPPER     | 0.000500     | 0.0007      | 0.0028   | 0.74000     | FAIL           |
| 6 | Pharyngeal/glottal first-letter cov.  | UPPER     | 2 / 4        | 3           | 4        | 0.95024     | FAIL           |

**Axes Bonferroni-significant: 1 / 6 → REFUTED-WEAK** (PASS required ≥ 2; 0 = REFUTED-STRONG).

## Discussion of each axis

### Axis 1 — LEXICAL (FAIL, p=0.657)
Fātiḥa's distinct word-types (every type, not just frequent ones) have a **mean log-token-frequency of 3.023**, which is **below** the null median of 3.190 — Fātiḥa actually uses words that are slightly **less common** on average than a typical 7-verse window. Fātiḥa is at the 34th percentile, nowhere near the 99.17th percentile required. Words like ـ"الصراط"ـ (verse 6, 7) and proper-name-like constructs limit common-vocabulary density.

### Axis 2 — SEMANTIC (PASS, p=0.00144)  ⋆
Fātiḥa hits **all 5 theme classes** in just 7 verses: praise (الحمد), mercy (الرحمن/الرحيم), judgment (الدين), guidance (اهدنا/الصراط/المستقيم), supplication (نعبد/نستعين matched via "نعب"). Only 9 of 6230 sliding windows (0.144%) reach 5/5. This **does** clear Bonferroni — Fātiḥa's thematic *integrating* function is statistically real. This is the one axis on which the Umm-al-Kitāb metaphor has empirical traction.

### Axis 3 — PHONETIC (FAIL, p=0.491)
Fātiḥa's verse-final letters are م,ن,م,ن,ن,م,ن — entirely nasal, which is plausibly the dominant Quranic rhyme class. The log-likelihood of −9.48 is slightly above the null median of −9.87 (53rd percentile). It is *typical*, not extreme. Many 7-verse windows in the corpus rhyme more uniformly on the most common letter (max LL ≈ −4.84, achieved by windows that are 7×same-letter rhymes). Fātiḥa's nasal mix is representative but unremarkable.

### Axis 4 — STRUCTURAL (FAIL, p=0.847)
Fātiḥa's verse word-counts (4,4,2,3,4,3,9) yield a KS distance of 0.679 from the corpus-wide word-count CDF — that's at the 85th percentile of KS distances among sliding windows, i.e., Fātiḥa is *more dissimilar than average* from the corpus-wide word-count distribution. The 9-word verse 7 plus the very short verses 3–4 push Fātiḥa toward the high-KS tail. Refutes the "structural representativeness" reading.

### Axis 5 — COMPRESSION (FAIL, p=0.740)
Prepending Fātiḥa to the rest of the corpus produces a compression-gain ratio of just 0.0500% — slightly **below** the null median of 0.07% (27th percentile). Fātiḥa is not an unusually good gzip-dictionary for the rest of the Quran; common 7-verse windows of formulaic content (e.g., narrative repetition) compress the rest better.

### Axis 6 — LETTER COVERAGE (FAIL, p=0.950)
Of the four pharyngeal/glottal letters {ا, ه, ع, ح}, Fātiḥa as first-letter-of-token covers only **2** (ا and ع). It is missing both ه and ح at the token-initial position (under the no-tashkeel rules-tuple, alif-hamza variants أ/إ are not equated with bare ا). This places Fātiḥa at the **24th percentile** — *worse than typical* on this axis. The [[h-new-44-2-poa-closure|H-NEW-44.2]].1 muqaṭṭaʿāt-class saturation pattern does **not** extend to Fātiḥa.

## MW-5 sanity controls

| Control | Value | Expected |
|---------|-------|----------|
| Q 59:22 window axis-1 (lexical) | 3.138 | Not extreme — H-NEW-59 cell 3 already showed 59:22-24 is divine-name-extreme but not lexically extreme. ✓ |
| Q 59:22 window axis-2 (semantic) | 2 | Below median; the Khawātim are divine-name dense, not theme-class diverse. Consistent. |
| Q 26:1 window axis-4 (KS) | 0.465 | Near median (0.470); the muqaṭṭaʿāt window is not structurally extreme by word-count KS. |

The MW-5 controls behave as expected for the chosen test statistics. (The pre-reg flagged that the MW-5 anchor verses are not necessarily extreme on *these specific* test statistics — MW-5 is named for being divine-name-dense and rhetorically distinctive, properties not directly captured by axes 1, 4 here.)

## Combined picture: H-NEW-59 + [[h-new-65-fatiha-as-dna|H-NEW-65]]

H-NEW-59 cell 3 already ran a **narrower** Fātiḥa-as-DNA test (asking whether Fātiḥa over-encodes the 99 divine names). It returned p=0.150 → REFUTED at α=0.05.

[[h-new-65-fatiha-as-dna|H-NEW-65]] broadens the question across 6 independent axes and finds 1/6 Bonferroni-significant → REFUTED-WEAK. Per M-9 (convergence-does-not-multiply), these are the project's first two systematic Fātiḥa-microcosm tests; effective independent N ≈ 2.

The convergent picture: **the strong "Fātiḥa as statistical microcosm" claim is empirically refuted.** The classical *Umm al-Kitāb* designation is best understood as:

1. **Liturgical primacy** (recited in every prayer; the exegetical kernel of supplication).
2. **Thematic comprehensiveness** (axis 2 PASS — Fātiḥa really does name all 5 major thematic axes in 7 verses, which is statistically rare).
3. **NOT** lexical compression, structural representativeness, or letter-class saturation.

## Honesty controls satisfied

- ✓ All 6 axes' raw values + null distribution summaries published in `csv/h-new-65.json` regardless of verdict.
- ✓ Pre-committed PASS criterion (≥ 2 of 6 Bonferroni-significant) followed; not revised post-hoc.
- ✓ Pre-committed direction per axis (UPPER for 1,2,3,5,6; LOWER for 4) followed.
- ✓ Seed 20260416 reproducible (sliding-window null is deterministic anyway; only axis 5's 1000-sample subset is RNG-dependent).
- ✓ MW-5 controls reported transparently (pre-reg noted they are non-blocking for these test statistics).

## Files produced

- Script: `/Users/grey/Downloads/quran/scripts/h_new_65_fatiha_as_dna.py`
- Raw JSON: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-65.json`
- This findings file: `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-65-fatiha-as-dna.md`
- Journal: `/Users/grey/Downloads/quran/journal/h-new-65-run-1.md`

## Cross-references

- H-NEW-59 cell 3 (Fātiḥa as divine-name encoder, REFUTED at α=0.05, p=0.150).
- [[h-new-44-2-poa-closure|H-NEW-44.2]].1 (pharyngeal/glottal saturation in muqaṭṭaʿāt; [[h-new-65-fatiha-as-dna|H-NEW-65]] axis 6 shows Fātiḥa does NOT inherit this property).
- M-9 (convergence-does-not-multiply): Fātiḥa-microcosm effective N ≈ 2 (this + H-NEW-59).
- MASTER-LEDGER entry: Fātiḥa thematic-coverage real (axis 2); strong microcosm REFUTED-WEAK.
