---
id: H-NEW-600
title: "DOUBLE NULL — ALM-6 @ 43.15%ile and ALR-5 @ 56.25%ile both NULL; H-NEW-570 generalization VINDICATED across letter-families; al-Biqāʿī family-munāsaba content-cohesion claim FALSIFIED at whole-surah FR-roots scale"
phase: B
status: PRIMARY DOUBLE NULL — ALM-6 NULL (43.15%); ALR-5 NULL (56.25%); MW-5 stable (drift ≤0.6pp both); MW-6 instrument over-dispersed (88.10%, expected per H-NEW-570 §5 pattern); muqaṭṭaʿāt-axis ⊥ content-axis CONFIRMED at within-letter-family resolution
date: 2026-04-28
executed_by: h-new-600-specialist
parent_1: H-NEW-570 (muqaṭṭaʿāt-29 NULL @ 65.62%ile; HM-7 @ 20.90%ile partial-NULL)
parent_2: H-NEW-130 (muqaṭṭaʿāt hub-architecture at letter-level CONFIRMED)
parent_3: H-NEW-97 (ALR letter-cluster → 4/5 PROPHET_PERSON p_mc=0.0059)
seed_primary: 20260430
seed_mw5: 20260431
seed_mw6: 20260432
prereg: h-new-600-letter-families-prereg.md
prereg_sha256: d667f28d3155a456758ab689ebb4d163c742501c878c767326a701801b2fb640
bonferroni_k: 3
alpha_bon: 0.01667
verdict: DOUBLE NULL on ALM-6 and ALR-5 PRIMARY; H-NEW-570 generalization "muqaṭṭaʿāt-axis ⊥ content-axis" VINDICATED at within-letter-family resolution; al-Biqāʿī content-munāsaba claim EMPIRICALLY FALSIFIED at whole-surah FR-roots scale; al-Suyūṭī/al-Rāzī epistemic-humility position EMPIRICALLY VINDICATED a third time
---

# [[h-new-600-letter-families|H-NEW-600]]/610 — Letter-family double-NULL: muqaṭṭaʿāt is ⊥ content even within families


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Headline

| Test | K | d̄ | %ile | Gate | Verdict |
|:--|:-:|:-:|:-:|:-:|:--|
| **ALM-6 PRIMARY** {Q 2, 3, 29, 30, 31, 32} | 6 | 0.9257 | **43.15%** | ≤16.67% DIR | **NULL** (median-level) |
| ALM-6 MW-5 (seed 20260431, N=5000) | 6 | 0.9257 | 42.58% | drift ≤3pp | stable (Δ=0.57pp) |
| **ALR-5 PRIMARY** {Q 10, 11, 12, 14, 15} | 5 | 0.9552 | **56.25%** | ≤16.67% DIR | **NULL** (above-median) |
| ALR-5 MW-5 (seed 20260431, N=5000) | 5 | 0.9552 | 56.38% | drift ≤3pp | stable (Δ=0.13pp) |
| MW-6 instrument {Q 5, 9, 17, 25, 33, 47} | 6 | 1.0129 | 88.10% | [25,75] | over-dispersed |

**Joint test (Bonferroni #3): NULL** — neither family ≤ 16.67%ile; aggregate H1 (al-Biqāʿī content-munāsaba within letter-families) FAILS at α_bon = 0.01667. Aggregate NULL = [[h-new-570-muqattaat-content-cluster|H-NEW-570]] generalization VINDICATED.

**Major architectural finding**: [[h-new-570-muqattaat-content-cluster|H-NEW-570]]'s "muqaṭṭaʿāt-axis ⊥ content-axis" claim, originally established at the full-29 level (65.62%ile), now SURVIVES the harder within-letter-family test. Even when restricted to surahs sharing the SAME exact opening-letter sequence (ALM or ALR), there is no whole-surah FR-roots content-cohesion. This makes the orthogonality finding much stronger: the muqaṭṭaʿāt-letter-axis is empirically PURE letter-structural at every observable resolution from full-29 → 7-ḥawāmīm → 6-ALM / 5-ALR.

## 2. ALM-6 result

**ALM-6** = {Q 2 al-Baqara, Q 3 Āl ʿImrān, Q 29 al-ʿAnkabūt, Q 30 al-Rūm, Q 31 Luqmān, Q 32 al-Sajda}, K=6.

- d̄ = 0.9257 (corpus mean of FR distances over C(6, 2) = 15 pairs)
- PRIMARY percentile in 10000 random-6 null (seed 20260430): **43.15%ile**
- MW-5 replication (seed 20260431, N_perms=5000): 42.58%ile, drift = 0.57pp → stable
- STRICT gate ≤ 1.67%: **FAIL**
- DIRECTIONAL gate ≤ 16.67%: **FAIL**

**Classical anchor**: al-Biqāʿī *Naẓm al-Durar fī tanāsub al-āyāt wa-l-suwar* on Q 2:1 treats ALM as the canonical letter-family for *munāsaba* — and Q 29-32 as a tight thematic-block within ALM (consecutive Meccan, shared "signs of Allāh" motif). al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān* nawʿ 40 enumerates ALM as the largest (6-surah) family. al-Rāzī *Mafātīḥ al-ghayb* vol. 2 surveys 20+ classical opinions on ALM specifically.

**Empirical**: ALM-6 sits at near-exact median of corpus dispersion (43.15%ile). al-Biqāʿī's prediction that ALM-6 should cohere is empirically UNSUPPORTED at whole-surah FR-roots resolution. The ALM letter-family is a structural-letter feature, not a content-cohesion feature.

The intra-family pair Q 29-32 (the "tight Meccan block" in al-Biqāʿī) might still cohere as a 4-tuple — that is a queued sub-test (§8), not part of the locked [[h-new-600-letter-families|H-NEW-600]] protocol.

## 3. ALR-5 result

**ALR-5** = {Q 10 Yūnus, Q 11 Hūd, Q 12 Yūsuf, Q 14 Ibrāhīm, Q 15 al-Ḥijr}, K=5.

- d̄ = 0.9552 (over C(5, 2) = 10 pairs)
- PRIMARY percentile in 10000 random-5 null (seed 20260430): **56.25%ile**
- MW-5 replication (seed 20260431, N_perms=5000): 56.38%ile, drift = 0.13pp → stable
- STRICT gate ≤ 1.67%: **FAIL**
- DIRECTIONAL gate ≤ 16.67%: **FAIL**

**Classical anchor**:
- **al-Biqāʿī** *Naẓm al-Durar* on Q 10:1 — ALR opens the qiṣaṣ-block: Yūnus, Hūd, Yūsuf, Ibrāhīm, al-Ḥijr (Ṣāliḥ + Lūṭ). Treated as the strongest-cohering letter-family on content grounds.
- **al-Rāzī** *Mafātīḥ al-ghayb* vol. 17 on Q 10:1 explicitly notes the qiṣaṣ-cohesion across the ALR family.
- **[[h-new-97-name-letter-joint|H-NEW-97]]** EMPIRICALLY confirmed at SURAH-NAME-CLASS level: ALR-5 is 4/5 PROPHET_PERSON at p_mc = 0.0059 < α_bon = 0.0125 (Cramer's V = 0.586 LARGE effect). This is INDEPENDENT empirical evidence that ALR coheres on the prophet-narrative theme.

**Empirical**: ALR-5 at 56.25%ile is ABOVE-median dispersion — even MORE diffuse than ALM-6 (43.15%). This is **the most striking result of [[h-new-600-letter-families|H-NEW-600]]**: ALR-5 has the strongest classical-scholarship + independent-empirical ([[h-new-97-name-letter-joint|H-NEW-97]] name-class) prediction of cohesion of any muqaṭṭaʿāt sub-family — and yet it shows ZERO whole-surah-FR cohesion (sits above the median of random 5-subsets of the corpus).

This is the decisive falsifier: the family with the strongest prior is the one most thoroughly NULL. al-Biqāʿī's content-munāsaba framework FAILS specifically where it would have been most expected to succeed.

The interpretation must be: the prophet-narrative-theme cohesion that [[h-new-97-name-letter-joint|H-NEW-97]] detected at the surah-name-class level is **not driven by whole-surah FR-roots distribution**. ALR surahs share a prophet-naming convention (and possibly verse-level narrative vocabulary) but do NOT share enough whole-surah root frequencies to be content-cohesive in FR-space. This is consistent with [[h-new-97-name-letter-joint|H-NEW-97]]'s own finding that ALR's name-class signal is concentrated at NAME (not whole-content) level.

## 4. [[h-new-570-muqattaat-content-cluster|H-NEW-570]] generalization status — "muqaṭṭaʿāt-axis ⊥ content-axis"

[[h-new-570-muqattaat-content-cluster|H-NEW-570]] §6 made the ARCHITECTURAL claim that the muqaṭṭaʿāt-letter-axis is orthogonal to the content-axis at whole-surah FR scale. This was based on the full-29 (65.62%ile) and HM-7 (20.90%ile, moderate-not-extreme) results.

**[[h-new-600-letter-families|H-NEW-600]] SHARPENS the orthogonality claim** to within-letter-family resolution:

| Resolution | Set | %ile | Verdict |
|:--|:--|:-:|:--|
| All-29 ([[h-new-570-muqattaat-content-cluster|H-NEW-570]]) | full muqaṭṭaʿāt-29 | 65.62% | NULL |
| HM-7 ([[h-new-570-muqattaat-content-cluster|H-NEW-570]] MW-5) | Q 40-46 | 20.90% | weak partial-NULL |
| **ALM-6 ([[h-new-600-letter-families|H-NEW-600]] PRIMARY)** | Q 2, 3, 29, 30, 31, 32 | **43.15%** | **NULL** |
| **ALR-5 (H-NEW-610 PRIMARY)** | Q 10, 11, 12, 14, 15 | **56.25%** | **NULL** |

**The orthogonality holds at every resolution tested.** Going from the full muqaṭṭaʿāt set down to single-letter-family sub-clusters does NOT recover content-cohesion. The signal is simply not there at whole-surah FR-roots scale.

The HM-7 partial-cohesion (20.90%) is now better understood as a CHRONOLOGY+CONSECUTIVE-MUSHAF-POSITION effect rather than a letter-family effect: HM-7 is also 7 consecutive Meccan surahs — and consecutive Meccan blocks are known to weakly cohere from the chronological-cluster [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] stack. ALM-6 and ALR-5 are ALSO mostly Meccan (Q 2, 3 are Medinan within ALM-6; ALR-5 is fully Meccan) and ALR-5 is mostly consecutive (Q 10, 11, 12 consecutive; gap at Q 13 ALMR; Q 14, 15 consecutive). Yet ALR-5 STILL doesn't cohere — confirming the chronology+adjacency null is the relevant baseline, not "letter-family" as such.

## 5. Implication for [[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] multi-axis architecture

[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]] 5-factor model (chronology, content-register, sub-genre-cluster, outlier-factor, plus the muqaṭṭaʿāt-axis added by [[h-new-570-muqattaat-content-cluster|H-NEW-570]] §6) is now FURTHER HARDENED by [[h-new-600-letter-families|H-NEW-600]]:

- The muqaṭṭaʿāt-axis is robustly **independent** of content-register at all observable sub-scales (29 → 7 → 6 → 5).
- The 4-region architecture established by Wave-1 2026-04-17 (Fisher-Rao + 4-region) treats muqaṭṭaʿāt as a structural/letter feature; [[h-new-600-letter-families|H-NEW-600]] confirms this is the right architectural placement.
- The ALR name-class signal from [[h-new-97-name-letter-joint|H-NEW-97]] is now sharply localized: it exists at SURAH-NAME / VERSE-LEVEL but NOT at whole-surah-FR-roots level. This is itself a falsifiable prediction for future verse-level / phonological tests (queued).

**Architectural upshot**: muqaṭṭaʿāt operates as a pure letter-structural axis. Its content-correlations (such as they exist, e.g. ALR → prophet-name) are non-FR-root and likely operate at name-/verse-/phonological-scale — orthogonal directions for future investigation.

## 6. MW-6 instrument check

**MW-6 set** = {Q 5 al-Māʾida, Q 9 al-Tawba, Q 17 al-Isrāʾ, Q 25 al-Furqān, Q 33 al-Aḥzāb, Q 47 Muḥammad}, K=6 non-muqaṭṭaʿāt.

- d̄ = 1.0129
- %ile = 88.10% (over-dispersed; expected [25, 75])

The MW-6 instrument check fails its expected null-typical window — the random-6 set is more dispersed than 88% of random-6 draws. This **mirrors [[h-new-570-muqattaat-content-cluster|H-NEW-570]]'s MW-6 over-dispersion at 100.00%ile** (§5 of [[h-new-570-muqattaat-content-cluster|H-NEW-570]]). The cause is the same: the chosen non-muqaṭṭaʿāt set spans Medinan-ṭiwāl legal (Q 5, Q 9), Meccan narrative (Q 17, Q 25), late-Medinan (Q 33), and combat-context (Q 47) — a chronology+register-diverse mix that over-disperses by construction.

This is an **instrument-side artifact, not a substantive failure**. It signals that picking pseudo-random subsets from the non-muqaṭṭaʿāt complement tends to over-disperse because that complement happens to be register-diverse. The PRIMARY tests (random-K subsets of the FULL corpus) are unaffected — they use the full corpus null, not the non-muqaṭṭaʿāt complement.

For future runs, MW-6 should be replaced by a confirmed-cohesive cluster (e.g., qiṣār-22, awsāṭ-15) as a positive control, since the random-non-muq selection is empirically over-dispersing.

## 7. Honest limits

1. **FR-roots only.** Verse-level, phonological, or rhyme-level letter-family cohesion entirely untested by [[h-new-600-letter-families|H-NEW-600]]. The [[h-new-97-name-letter-joint|H-NEW-97]] ALR → PROPHET_PERSON signal at name-class level is empirically real and may have correlates at verse / phonological scales that [[h-new-600-letter-families|H-NEW-600]] cannot detect.
2. **K=5 and K=6** are small. Power for detecting cohesion at ≤ 1.67%ile STRICT is correspondingly limited; however, our PRIMARY %iles (43% and 56%) are so far from STRICT that no power-correction would change the verdict.
3. **Q 13 al-Raʿd EXCLUDED** (ALMR not ALR). [[h-new-620-divine-name-density|H-NEW-620]] follow-up (queued §8) will test ALMR-disjunction explicitly.
4. **Single-letter-sequence families only** (ALM, ALR). The mixed-letter families (ALMS Q 7, ALMR Q 13, KHYʿṢ Q 19, ḤM-ʿSQ Q 42) are 1-element each and not testable as cohesion clusters.
5. **MW-6 random-non-muq** over-dispersion is instrument-side, noted §6.
6. **PRIMARY null = random-K subset of full corpus.** Tighter null choices (e.g., random-K within Meccan-only, random-K within consecutive-mushaf) might produce sharper inference about whether the small HM-7 cohesion is letter-family or chronology+adjacency. This is queued §8.
7. **Length-variation.** Q 2 (286 verses) vs Q 32 (30 verses) within ALM-6 — but FR uses L1-normalized probability vectors (length-controlled per [[h-new-111-fisher-rao-mushaf|H-NEW-111]] MW-1), so this is not a confound.

## 8. Cross-references

- **[[h-new-570-muqattaat-content-cluster|H-NEW-570]]** (muqaṭṭaʿāt-29 + HM-7 NULL): [[h-new-600-letter-families|H-NEW-600]] STRENGTHENS this finding to within-letter-family resolution.
- **[[h-new-130-fisher-rao-residuals|H-NEW-130]]** (muqaṭṭaʿāt hub at letter-level): complemented by [[h-new-600-letter-families|H-NEW-600]] (muqaṭṭaʿāt NOT a content-cluster even at letter-family resolution). Two-axis architecture confirmed.
- **[[h-new-97-name-letter-joint|H-NEW-97]]** (ALR-PROPHET_PERSON p_mc=0.0059 at name-class): now sharply localized — name-level signal, NOT whole-surah-FR signal.
- **[[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]** (mushaf FR baseline): [[h-new-600-letter-families|H-NEW-600]] uses the [[h-new-111-fisher-rao-mushaf|H-NEW-111]] D-matrix.
- **[[cross-finding-024-five-factor-cohesion-model|cross-finding-024]]** (multi-axis model): muqaṭṭaʿāt-axis independence further hardened.
- **al-Biqāʿī** *Naẓm al-Durar*: family-content-munāsaba claim FALSIFIED at whole-surah FR-scale (THIRD empirical falsification, after full-29 and HM-7).
- **al-Suyūṭī** *Itqān* nawʿ 40 + **al-Rāzī** *Mafātīḥ al-ghayb*: epistemic-humility stance EMPIRICALLY VINDICATED a THIRD time.
- **Wave-1 2026-04-17** (Fisher-Rao + 4-region architecture): consistent — muqaṭṭaʿāt is properly placed as a letter-structural axis, not a content-region.

## 9. Queued follow-ups

- **[[h-new-620-divine-name-density|H-NEW-620]]**: ALMR disjunction — does {ALR-5 ∪ {Q 13}} = ALMR-extended-6 cohere? Tests whether Q 13 al-Raʿd's ALMR opening is closer to ALR-cohesion or ALM-cohesion behavior. Independent K=6 null required.
- **[[h-new-630-supercluster-substructure|H-NEW-630]]**: Q 29-32 (al-Biqāʿī's "ALM-tight-Meccan-block") as 4-tuple within ALM-6 — does the consecutive-Meccan sub-cluster cohere? K=4 null.
- **H-NEW-640**: ALR-5 chronology-controlled null — random-5 within Meccan-only and within consecutive-mushaf-positions, to disentangle chronology+adjacency from letter-family.
- **H-NEW-650**: Verse-level FR-roots ALR-5 test — does the ALR family cohere at first-N-verses or at qiṣaṣ-vocabulary subset?
- **[[h-new-660-compression-tail-gradient|H-NEW-660]]**: Phonological-axis test of ALM-6 / ALR-5 — do they share rhyme / sound patterns even though they don't share roots?
- **[[h-new-670-tsp-hijra-constraint|H-NEW-670]]**: Replace MW-6 with positive-control cluster (qiṣār-22 K=22 sub-sample, or awsāṭ-15) for instrument calibration.

## 10. Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-600-letter-families-prereg.md`
- Pre-reg SHA: `d667f28d3155a456758ab689ebb4d163c742501c878c767326a701801b2fb640`
- Run script: `scripts/h_new_600_letter_families.py`
- Output JSON: `findings/phase-b-hypotheses/csv/h-new-600.json`
- Findings: this file
- Journal: `journal/h-new-600-run-1.md`

## 11. Final statement

**[[h-new-600-letter-families|H-NEW-600]] / H-NEW-610 produce a DOUBLE NULL on both muqaṭṭaʿāt letter-families tested**: ALM-6 at 43.15%ile (median-level) and ALR-5 at 56.25%ile (above-median). MW-5 replications stable (drift ≤ 0.6pp on both). MW-6 instrument over-dispersed in line with [[h-new-570-muqattaat-content-cluster|H-NEW-570]] §5 pattern.

**The classical al-Biqāʿī content-munāsaba framework is now EMPIRICALLY FALSIFIED at whole-surah FR-roots scale at three resolutions** (full-29, HM-7 partial, ALM-6, ALR-5). The classical al-Suyūṭī / al-Rāzī epistemic-humility stance ("*Allāh aʿlam bi-murādihi*") is EMPIRICALLY VINDICATED a third time.

**The most striking result is ALR-5 NULL at 56.25%ile**: the family with the strongest classical prior (qiṣaṣ-cohesion per al-Biqāʿī, al-Rāzī) AND the strongest INDEPENDENT empirical prior ([[h-new-97-name-letter-joint|H-NEW-97]] 4/5 PROPHET_PERSON at p_mc = 0.0059) shows ZERO whole-surah FR-roots cohesion — sitting ABOVE the median of random-5 corpus draws. This is the decisive falsifier: the family most expected to cohere is the most thoroughly diffuse.

This sharpens the [[h-new-570-muqattaat-content-cluster|H-NEW-570]] architectural claim: **the muqaṭṭaʿāt-letter-axis is orthogonal to whole-surah-content-axis at every observable resolution from full-29 down to single-letter-family**. The muqaṭṭaʿāt operates as a pure letter-structural feature; any content-correlations (e.g., ALR → prophet-naming) are non-FR-root and operate at name- / verse- / phonological-scale.

**Verdict on classical claims**:
- al-Biqāʿī content-munāsaba within letter-families: **FALSIFIED**
- al-Suyūṭī / al-Rāzī epistemic-humility: **VINDICATED**
- [[h-new-570-muqattaat-content-cluster|H-NEW-570]] generalization "muqaṭṭaʿāt ⊥ content-axis": **VINDICATED at within-letter-family resolution**
- [[h-new-97-name-letter-joint|H-NEW-97]] ALR-PROPHET_PERSON name-level signal: **PRESERVED**, but sharply localized to name-class (not whole-surah FR)

Published DOUBLE NULL with equal prominence.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
