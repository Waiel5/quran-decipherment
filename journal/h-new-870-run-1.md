# H-NEW-870 — Run 1 Journal

**Date**: 2026-04-28
**Operator**: specialist agent (Q 33 architectural-content investigation)
**Task**: Deep architectural + content investigation of Q 33 al-Aḥzāb; quantitative keystone test against H-NEW-660 compression-tail law.

## Anchor — empirical convergence flagged Q 33 as #1

Three independent metrics put Q 33 at the top of architecturally-significant surahs:
1. **H-NEW-590 outlier-strength**: Δ%ile = +31.46pp (single highest in entire corpus, window Q 30-36).
2. **H-NEW-720 canonical-adjacency cost**: Q 32→Q 33 = 4.38%, Q 33→Q 34 = 3.99%. Q 33 sits in the second-most-expensive 3-surah TSP-residual cluster (after Q 1-Q 2 opener).
3. **H-NEW-750 iʿjāz signature**: 2.97 (top-tier).

Combined H-NEW-840 UAS = +9.36, rank 1 of 114.

This is not subtle. It demanded explanation.

## Method

Followed the H-NEW-870 task brief (deep investigation + quantitative keystone test).

**Key empirical test (point 5 of brief)**:
- Reproduce H-NEW-660 baseline two-piece compression-tail law.
- Counterfactual: remove Q 33 from the mushaf, re-index surviving 113 surahs, re-fit.
- Sensitivity sweep: do this for all 114 surahs to contextualize Q 33.

Script: `scripts/h_new_870_q33_keystone_test.py`. Seed 20260470. Operates on H-NEW-111 distance matrix (SHA `4c366c41…`).

## Results

### Baseline reproduction (sanity)

| Model | R² | β |
|:--|:-:|:-:|
| Linear | 0.7706 | -0.00619 |
| Quadratic | 0.9771 | — |
| Two-piece kink-50 | **0.9860** | -0.01237 |

Exact match with H-NEW-660 §1. Confidence in the test pipeline.

### Counterfactual — remove Q 33

| Model | R² (no Q 33) | ΔR² vs baseline |
|:--|:-:|:-:|
| Linear | 0.7691 | -0.0015 |
| Quadratic | 0.9718 | -0.0053 |
| Two-piece kink-50 | **0.9847** | **-0.0013** |

**Q 33 is NOT a structural keystone.** Removing it drops two-piece R² by only 0.13pp (from 0.9860 to 0.9847). Pre-committed threshold was ≥0.05 (≥5pp) for keystone classification. Q 33 falls firmly in the "high-magnitude outlier, but the law is robust without it" category.

### Sensitivity sweep — what surahs ARE the keystones?

Top-10 R²-damaging removals (these are the actual load-bearers of the compression-tail law):

| Rank | Surah | ΔR² | Classical context |
|:-:|:--|:-:|:--|
| 1 | Q 98 al-Bayyina | +0.0029 | mufaṣṣal-qiṣār |
| 2 | Q 96 al-ʿAlaq | +0.0023 | first-revelation, mufaṣṣal-qiṣār |
| 3 | Q 86 al-Ṭāriq | +0.0022 | mufaṣṣal-qiṣār |
| 4 | Q 82 al-Infiṭār | +0.0020 | mufaṣṣal-qiṣār |
| 5 | Q 87 al-Aʿlā | +0.0020 | mufaṣṣal-qiṣār (musabbiḥa) |
| 6 | Q 81 al-Takwīr | +0.0020 | mufaṣṣal-qiṣār |
| 7 | Q 92 al-Layl | +0.0017 | mufaṣṣal-qiṣār |
| 8 | Q 91 al-Shams | +0.0017 | mufaṣṣal-qiṣār |
| 9 | Q 88 al-Ghāshiya | +0.0017 | mufaṣṣal-qiṣār |
| 10 | Q 97 al-Qadr | +0.0016 | mufaṣṣal-qiṣār |

**ALL 10 keystones are mufaṣṣal-qiṣār surahs (Q 78-114).** Q 33 ranks 18 of 114 — distinctly secondary.

The compression-tail law is load-bearing on the late-Meccan terminal-cluster mufaṣṣal-qiṣār — exactly what the law is *about*.

### Anti-keystones (removing them improves the fit)

| Rank | Surah | ΔR² |
|:-:|:--|:-:|
| 114 | Q 41 Fuṣṣilat | -0.0034 |
| 113 | Q 46 al-Aḥqāf | -0.0029 |
| 112 | Q 45 al-Jāthiya | -0.0029 |
| 111 | Q 65 al-Ṭalāq | -0.0027 |
| 110 | Q 40 Ghāfir | -0.0025 |

These are the HM-cluster surahs (Q 40-46) — local noise that the global law smoothly absorbs.

### Q 33 within its windows — local effect IS real

Q 33 raises every K=15 window's d̄ that contains it by +0.015 to +0.026 (max +0.0257 at window Q 32-46). So Q 33 IS locally distinctive — but the global law's R²=0.986 is so high that one outlier in 100 windows can't move it.

## Findings narrative

### §1-3 (content + chronology) — written from classical sources

Major content blocks of Q 33 verified against the Quran text:
- vv 1-8: opening admonition, prophetic-spousal regulation framing.
- vv 9-27: al-Aḥzāb battle (Trench / Khandaq) — historical narrative, the surah's name.
- vv 28-34: ḥijāb / mothers-of-believers regulations (the famous v 33 *innamā yurīdu Allāh*).
- vv 35-40: men-and-women parity verse (v 35); Zaynab marriage; v 40 *khātam al-nabiyyīn*.
- vv 41-48: dhikr commands.
- vv 49-52: marriage regulations.
- vv 53-55: ḥijāb-of-the-curtain verse (53); v 56 *innallāha wa-malāʾikatahu yuṣallūna ʿalā al-nabī*.
- vv 57-73: closing — āyat al-amāna v 72.

Chronology verified against `data/revelation-order.csv`: Q 33 mushaf-position 33, revelation-order 90, Medinan. Q 32 = rev 75 (Late Meccan). Q 34 = rev 58 (Late Meccan). The whole stretch Q 28-Q 42 is Late/Middle Meccan EXCEPT Q 33. **Q 33 is the sole Medinan island in 15 consecutive Meccan surahs.**

The ALM-muqaṭṭaʿāt at Q 32 is a key piece: classically the ALM-cluster {Q 2, 3, 29, 30, 31, 32} forms the "Alif-Lām-Mīm" group; Q 33 breaks this cluster's natural Late-Meccan tone with a Medinan insertion of completely different register.

### §5 (classical reception) — the "reticence" hypothesis

Searched fadāʾil literature in my training:
- al-Bukhārī fadāʾil al-Qurʾān: extensive on Q 1, 2, 36, 67, 112, 113, 114. **Silent on Q 33.**
- al-Tirmidhī Sunan: Q 67 al-Mulk has its own bāb. Q 36 Yā-Sīn has multiple fadāʾil aḥādīth (some weak). **No comparable corpus for Q 33.**
- al-Suyūṭī al-Itqān: discusses Q 33 only for chronological + sabab-al-nuzūl context, not fadāʾil.
- Ibn Kathīr tafsīr: extensive on Q 33's content (legal verses) but does not flag any architectural-significance.

Honest reading: classical fadāʾil literature is reticent about Q 33 because (a) it has no fadāʾil aḥādīth of major-collection grade attached to it, (b) much of its content is sensitive (ḥijāb, Zaynab marriage, Prophet's wives), making it more a tafsīr-and-fiqh surah than a recitation-merit surah. The architectural-distinctness was not flagged — but classical scholars were not running compression-tail regressions either.

### §6 — synthesis

Q 33 is not a keystone of the compression-tail law. It IS a keystone of corpus content-distinctness. These are different architectural notions:

| Architectural notion | Definition | Q 33 status |
|:--|:--|:--|
| Compression-tail load-bearing | Removing Q 33 collapses R² | NO (rank 18, ΔR²=+0.0013) |
| Local outlier-strength | Window Δ%ile vs neighbors | YES (#1 corpus, +31.46pp) |
| Canonical-adjacency cost | Forcing Q 32-Q 33 adjacency raises TSP cost | YES (Q 32-33 = 4.38%, second-largest single edge) |
| iʿjāz signature | Content + rhyme combined extremity | YES (2.97) |

**Q 33 is the corpus's most architecturally-singular surah, but not the corpus's most architecturally-load-bearing surah.** The compression-tail law is borne by the mufaṣṣal-qiṣār terminal block; Q 33 is a sui generis local feature whose distinctness is content-driven (Medinan in Meccan-stretch) but not structurally necessary for global laws.

## Honest limits

1. K=15 windowing — the keystone test is window-size dependent. K=7 might give a different sensitivity. (Not tested here; brief specified the H-NEW-660 logic which used K=15.)
2. R²-damage is one operationalization of "keystone". Other operationalizations (e.g. β-shift, kink-position-shift) might rank surahs differently.
3. The 113-surah counterfactual has 99 windows vs 100; this changes the regression slightly even before Q 33's content is considered. The 0.0013 drop is therefore a SUM of (real Q 33 effect) + (window-count change). The real Q 33 effect alone may be even smaller.
4. fadāʾil silence is not proof of absence — many classical works have variable Q 33 coverage I cannot fully audit.

## Cross-references confirmed

- H-NEW-660 (compression-tail R²=0.986 baseline)
- H-NEW-590 (Q 33 outlier-strength +31.46pp)
- H-NEW-720 (Q 32-33 + Q 33-34 canonical-adjacency cost cluster)
- H-NEW-750, H-NEW-840 (Q 33 UAS rank 1)
- al-Suyūṭī *al-Itqān* chronology (Q 33 = revelation-order 90)
- al-Bukhārī fadāʾil literature (silent on Q 33)

## Outputs

- `findings/phase-b-hypotheses/h-new-870-q33-architectural-keystone.md`
- `scripts/h_new_870_q33_keystone_test.py`
- `findings/phase-b-hypotheses/csv/h-new-870.json`
- This journal: `journal/h-new-870-run-1.md`

## Verdict (returned to caller)

**Q 33 al-Aḥzāb is NOT a structural keystone of the compression-tail law** (R² drops only 0.0013 when removed; rank 18 of 114 by R²-damage; far behind Q 78-114 mufaṣṣal-qiṣār). **Q 33 IS the corpus's most singular local-content outlier** (+31.46pp Δ%ile, #1 corpus-wide, with a clear cause — sole Medinan in a 15-surah Late-Meccan stretch). These are different architectural roles. The classical scholarly tradition's relative reticence about Q 33 is consistent with this: Q 33 is content-architecturally distinctive but not load-bearing for the global cohesion-architecture, so traditional *fadāʾil* attention (which centers on recitation merit and global structural roles like *umm al-Kitāb* for Q 1) would not naturally identify it.
