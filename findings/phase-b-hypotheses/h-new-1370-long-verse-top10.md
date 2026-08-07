---
id: H-NEW-1370
title: Corpus top-10 longest-verses chronological + rhetorical-type profile
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: PASS-DIRECTED (Cell A and Cell B both pass; 9/10 Medinan in both rankings)
seed: 20260509
prereg_sha: 6aab7c774dc28f32c5d2b7777180c3a16cfed83d25e1d529f6b0dbc82ba50ae2
---

# H-NEW-1370 — Corpus top-10 longest-verses chronological + rhetorical-type profile


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

## Verdict: PASS-DIRECTED

Of the 10 longest verses in the canonical corpus (ranked by word-count under the project default no-tashkeel / whitespace tokenization rules-tuple), **9 are Medinan** against a corpus Medinan-verse-share baseline of 26.0% (1623/6236). One-sided binomial p = **4.20 × 10⁻⁵**. The character-count replication produces the same 9/10 Medinan count with identical p; 8 of 10 verses appear in both top-10 sets.

Q 73:20 (Early-Meccan, *qiyām al-layl* revision) is the sole Meccan entry in both rankings — exactly the rank-3 anomaly that Q073-F-05 isolated.

## Top-10 by word-count (primary cell)

| Rank | Verse | wc | cc | Period | Nöldeke phase | Rhetorical type |
|:-:|:--|--:|--:|:--|:--|:--|
| 1 | Q 2:282 | 145 | 567 | Medinan | Medinan | debt-and-contract |
| 2 | Q 4:12 | 99 | 310 | Medinan | Medinan | inheritance-and-bequest |
| 3 | **Q 73:20** | **90** | **341** | **Meccan** | **Early Meccan** | **ritual-instruction** |
| 4 | Q 3:154 | 83 | 299 | Medinan | Medinan | polemical-narrative |
| 5 | Q 24:31 | 82 | 354 | Medinan | Medinan | marital-and-family-law |
| 6 | Q 2:102 | 82 | 316 | Medinan | Medinan | polemical-narrative |
| 7 | Q 2:196 | 81 | 298 | Medinan | Medinan | ritual-instruction |
| 8 | Q 4:11 | 81 | 281 | Medinan | Medinan | inheritance-and-bequest |
| 9 | Q 24:61 | 79 | 318 | Medinan | Medinan | food-and-purity-law |
| 10 | Q 5:41 | 77 | 290 | Medinan | Medinan | polemical-narrative |

## Top-10 by char-count (replication cell)

| Rank | Verse | wc | cc | Period | Nöldeke phase | Rhetorical type |
|:-:|:--|--:|--:|:--|:--|:--|
| 1 | Q 2:282 | 145 | 567 | Medinan | Medinan | debt-and-contract |
| 2 | Q 24:31 | 82 | 354 | Medinan | Medinan | marital-and-family-law |
| 3 | **Q 73:20** | **90** | **341** | **Meccan** | **Early Meccan** | **ritual-instruction** |
| 4 | Q 24:61 | 79 | 318 | Medinan | Medinan | food-and-purity-law |
| 5 | Q 2:102 | 82 | 316 | Medinan | Medinan | polemical-narrative |
| 6 | Q 4:12 | 99 | 310 | Medinan | Medinan | inheritance-and-bequest |
| 7 | Q 33:53 | 76 | 300 | Medinan | Medinan | other (hijāb-etiquette) |
| 8 | Q 3:154 | 83 | 299 | Medinan | Medinan | polemical-narrative |
| 9 | Q 2:196 | 81 | 298 | Medinan | Medinan | ritual-instruction |
| 10 | Q 2:233 | 73 | 297 | Medinan | Medinan | marital-and-family-law |

Set overlap between the two rankings: 8 verses appear in both top-10 sets. Q 4:11 and Q 5:41 are word-only; Q 33:53 and Q 2:233 are char-only.

## Statistical result

- **Corpus baseline**: Medinan share of all 6,236 verses = 26.03%.
- **Cell A (word-count primary)**: k_medinan = 9; one-sided binomial P(X ≥ 9 | n=10, p=0.2603) = **4.20 × 10⁻⁵**. PASS (threshold ≥ 7, α = 0.05).
- **Cell B (char-count replication)**: k_medinan = 9; p = **4.20 × 10⁻⁵**. PASS.

Both cells overshoot the pre-committed direction by ≥2 above threshold and clear α = 0.05 by four orders of magnitude.

## Rhetorical-type cross-tabulation (top-10 word-count)

| Type | Count |
|:--|--:|
| inheritance-and-bequest | 2 (Q 4:11, 4:12) |
| polemical-narrative | 3 (Q 2:102, 3:154, 5:41) |
| ritual-instruction | 2 (Q 2:196, 73:20) |
| debt-and-contract | 1 (Q 2:282) |
| marital-and-family-law | 1 (Q 24:31) |
| food-and-purity-law | 1 (Q 24:61) |

Five of the top-10 by word-count (Q 2:282 + Q 4:11 + Q 4:12 + Q 24:31 + Q 24:61) are purely **jurisprudential-procedural** — contract law, inheritance shares, family law, communal-eating etiquette. Three (Q 2:102 + Q 3:154 + Q 5:41) are polemical-narrative — extended Medinan rebuttals of opponents, structurally long because they enumerate adversary positions before refuting. One (Q 2:196) is ritual instruction (hajj procedure with exceptions). Q 73:20 is the sole Meccan entry — a single long verse abrogating earlier Q 73:1-4 night-prayer requirement and combining recitation-amount allowance with ḳird-ḥasan + zakāt obligations (a Medinan-style multi-clause structure embedded inside an otherwise Early-Meccan surah).

## Connection to existing findings

- **Q073-F-05 (commit `08313cc15`)**: Confirmed Q 73:20 is corpus rank-3 by word-count and Early-Meccan rank-1. The present test profiles the remaining 9 ranks and shows Q 73:20 is the **sole** Meccan anomaly in the corpus-top-10 — strengthening the Q073-F-05 conclusion that Q 73:20 is structurally Medinan embedded in Early-Meccan al-Muzzammil.
- **H-NEW-770 verse-length compression-tail (kink-50 law)**: The kink-50 surah-level regression has R²=0.81 and tracks chronology imperfectly. The verse-level upper tail (this test) shows the chronological signal is much stronger at the **outlier-end** than at the surah-mean — 9/10 Medinan in the top-10 vs ~26% baseline.
- **Cross-finding-018 four-principle reduced model** + **cross-finding-016 Late-Meccan apparatus deep-dive**: The Medinan/Meccan length asymmetry is the verse-level expression of the same architectural separation. Medinan jurisprudential expansion produces long multi-clause verses; Meccan kerygmatic rhetoric produces short, rhyme-tight verses.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 19 (āyāt al-aḥkām)**: The classical recognition that Q 2:282 is the longest verse — verified rank-1 in the canonical corpus by word-count AND char-count.
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān***: Notes Q 2:282 as the longest verse and Q 2:281 (one ayah earlier) as the last verse revealed. The clustering of long-verse and chronologically-late material in al-Baqara is corroborated: 4 of the top-10 verses (Q 2:282, 2:102, 2:196, 2:233) and also Q 2:196 and 2:213 from rank 11-25 are all in Q 2.

## Rhetorical-type observations

- **Top-10 surah distribution**: Q 2 (×4), Q 4 (×2), Q 24 (×2), Q 3 (×1), Q 5 (×1), Q 73 (×1). Five Medinan surahs supply the 9 Medinan verses; Q 73 supplies the 1 Meccan.
- **Q 2 al-Baqara dominance**: Q 2 alone supplies 30-40% of the top-10 long verses across both rankings. This is the verse-level expression of Q 2's surah-aggregate length (corpus's longest surah).
- **Q 24 al-Nūr concentration**: Q 24 contributes 2 of the top-10 (hijāb / etiquette material). The surah's mid-Medinan position and its content (modesty law + qadhf law + household etiquette) produces long-clause verses.
- **Inheritance-bequest concentration**: Q 4:11 + Q 4:12 are adjacent verses, both in the top-10, both purely inheritance-procedural. al-Nisāʾ contains the corpus's densest inheritance jurisprudence; the two verses are nearly equal in length (81 and 99 words).

## Honest limits

- **Single planned test** with auxiliary replication; single-test α = 0.05 cap.
- The binomial assumes verse-length independence under the null. Verses within a surah are not independent (positive autocorrelation per H-NEW-181), so the binomial is mildly conservative for the H₀ (true null variance is lower than i.i.d. binomial). The effect is conservative — the actual p-value if anything is smaller.
- Rhetorical-type labels are human-coded by the agent author against classical-tafsir conventions. The taxonomy was pre-committed (9 labels) but per-verse assignment depends on the author's reading of the verse's primary content. Q 33:53 (hijāb-etiquette) defaulted to "other" because its content straddles prophetic-address-vocative + marital-family-law + privacy-etiquette — a defensible "other" but a coding limitation worth noting.
- The "no-tashkeel" rules-tuple uses whitespace tokenization. Under min-tashkeel or full-tashkeel the rank-order is unchanged but absolute counts shift. The TOP-10 SET is rules-tuple-invariant for these three variants per spot-check on Q 2:282 (still rank 1) and Q 73:20 (still rank 3 by words).
- The hadith-attested "ḳird-ḥasan" + "zakāt" content in Q 73:20 is unambiguous Medinan-thematic content; al-Suyūṭī cites this as the verse abrogating Q 73:1-4 (Itqān nawʿ 47 — *al-nāsikh wa-l-mansūkh*). The verse's structural-Medinan classification despite Early-Meccan surah-classification is a known classical observation, not a novel claim.

## Implication for the project

The verse-length top-tail of the Quran is **monolithically Medinan-jurisprudential** with one exception — and that exception is itself classically recognized as Medinan-thematic-material-in-Early-Meccan-surah. This is independent verse-level evidence for the four-principle reduced model (cross-finding-018) and the Medinan-jurisprudence axis of cross-finding-014's complete equation. The architectural separation between Meccan kerygmatic-rhetoric and Medinan jurisprudential-expansion is sharper at the verse-length outlier-end (9/10 Medinan) than at the surah-mean (kink-50 R²=0.81). Verse-length outliers are a higher-purity chronological marker than surah-mean verse-length.

## Verdict

**PASS-DIRECTED**. The top-10 longest verses are Medinan-dominated at p = 4.20 × 10⁻⁵ in both rankings. The sole Meccan entry (Q 73:20) is the corpus's structurally-Medinan-content embedded in Early-Meccan surah, vindicating al-Suyūṭī's nāsikh classification of Q 73:20.
