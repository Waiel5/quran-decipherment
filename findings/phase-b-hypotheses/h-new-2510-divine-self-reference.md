---
finding_id: H-NEW-2510
title: Divine-self-reference density corpus map + the tawḥīd-declaration verse class
date: 2026-05-30
phase: B+
seed: 20260509
n_perm: 10000
pre_reg_sha256: 68845be397a198ed5b95abe701c6b126159715ed07aa28c82b09ad16bfbdb53a
verdict: NULL (pre-committed direction REVERSED — published with full prominence per Protocol §1.3)
specialist: divine-self-reference-generator
generalizes: Q020-F-05 (§10.120)
---

# H-NEW-2510 — Divine-self-reference density corpus map


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

> **VERDICT: NULL — pre-registered direction REVERSED.** The corpus-top
> divine-self-reference-density verses are **NOT** the recognized
> tawḥīd-declaration class. They are short, first-person-clitic-dense verses,
> the majority of them **human-spoken** (believers, sinners, prophets), not
> divine self-disclosures. Published with full prominence (Protocol §1.3).

## 1. What was tested

This GENERALIZES **Q020-F-05** (§10.120: within Ṭā-Hā, Q 20:14
*innanī anā Allāhu lā ilāha illā anā…* is the rank-1 divine-self-reference verse,
density 0.5455, p_perm=0.0015). A GENERATOR scored **all 6,236 verses** for
divine first-person self-disclosure density, re-grounded in **QAC v0.4
morphology** (person/number features) instead of the noisy regex proxy used in
Q020-F-05.

- **Token set (QAC-grounded):** divine name *Allāh* (`POS:PN|LEM:{ll~ah`) + *ilāh*
  (`LEM:<ila`h`) + tawḥīd-*illā* (`LEM:<il~aA` adjacent to *ilāh*) + standalone
  1S/1P pronouns (*anā/naḥnu*) + clitic 1S/1P (*-nī/-ī/-nā*).
- **density = numerator / QAC-word-count.**
- **Metric-A (PRIMARY, speaker-agnostic)** — all tokens. **Metric-B (robustness,
  divine-gated)** — bare/clitic 1st-person counted only where the verse carries the
  divine name *Allāh* or the tawḥīd-formula.
- **Null:** per-verse word-shuffle preserving each verse's word-count, 10,000 perms,
  seed 20260509. Test statistics: max density, top-20 mean density.
- **Pre-registered direction (LOCKED):** density is non-uniform AND the corpus-top
  verses concentrate in the tawḥīd-declaration class
  {Q20:14, Q27:9, Q28:30, Q2:255, Q112:1, Q112:2}.

Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2510-divine-self-reference.md`
(SHA-256 `68845be3…db53a`, embedded + verified at runtime).
Output: `findings/phase-b-hypotheses/csv/h-new-2510.json`.
Script: `scripts/h-new-2510.py`.

## 2. Results

| Test | Pre-reg threshold | Observed | Pass? |
|:--|:--|:--|:--:|
| H1a max density > null | p_max ≤ 0.05 | obs 1.000, null-max-mean 1.0025, **p=0.988** | ✗ |
| H1b top-20 mean > null | p_top20 ≤ 0.05 | obs 0.7097, null 0.7086, **p=0.490** | ✗ |
| H2 anchor enrichment | ≥3 anchors in top-20, or mean-rank ≤ 624 | **1/6** in top-20; mean rank **852.8** | ✗ |

**H1 FAILS (concentration NULL).** The word-shuffle null reproduces the observed
max and top-20 densities almost exactly. Self-reference *placement* is **not** more
concentrated at the top than chance: density is dominated by verse-length (short
verses mechanically score high), a structure the length-preserving null reproduces.
(The top decile does carry 26.2% of all self-reference token mass vs 10% uniform —
a length artifact, not a placement signal.)

**H2 FAILS (anchor class NOT at top).** Only 1 of the 6 pre-named
tawḥīd-declaration anchors reaches the corpus top-20; the anchors' mean corpus-rank
is 852.8 (outside the top decile).

**Corpus top-10, Metric-A** — the verses that actually win on density:

| Rank | Verse | Density | Speaker (per tafsīr/context) | Composition |
|:-:|:--|:-:|:--|:--|
| 1 | Q20:41 | 1.000 | God→Mūsā (*wa-aṣṭanaʿtuka li-**nafsī***) | 2 clitic-1S, 0 anchors |
| 2 | Q69:20 | 0.800 | a believer at Resurrection | 4 clitic-1S |
| 3 | Q33:67 | 0.750 | the damned followers in Hell | 6 clitic-1P |
| 4 | Q36:25 | 0.750 | the believing man of the city | 3 clitic-1S |
| 5 | Q37:32 | 0.750 | the misleaders in Hell | 3 clitic-1P |
| 6 | Q89:24 | 0.750 | the regretful sinner | 3 clitic-1S |
| 7 | **Q20:14** | **0.7273** | **God (burning bush — tawḥīd-declaration)** | **Allāh+ilāh+illā+2 anā+3 clitic** |
| 8 | Q15:95 | 0.667 | God→Prophet | 2 clitic-1S |
| 9 | Q20:26 | 0.667 | Mūsā's prayer (human) | 1 pron + 1 clitic |
| 10 | Q26:108 | 0.667 | Nūḥ to his people (human) | Allāh + 1 clitic |

The genuine tawḥīd-declaration **Q20:14 is the highest-ranked self-disclosure verse
in the whole corpus, at rank 7/6236** — but it is *out-ranked* by six short verses
that are mostly human-spoken first-person speech. The direction is **reversed**.

**Anchor corpus-ranks (Metric-A):** Q20:14 → 7; Q112:2 → 90; Q27:9 → 233; Q112:1 →
609; Q28:30 → 1232; **Q2:255 (āyat al-kursī) → 2946.** Āyat al-kursī, classically
"the greatest verse," sinks to the corpus *median* on density precisely because it
is **long** (50 words): its dense self-disclosure head (*Allāh lā ilāha illā huwa
al-ḥayy al-qayyūm*) is diluted by 38 following words.

## 3. The disambiguation result (the real finding)

The locked pre-reg flagged the divine-vs-human first-person problem and shipped
**Metric-B (divine-gated)** as the robustness arm. Metric-B *does* lift Q20:14 to
rank-1 and Q112:2 to rank-17, but its top is then captured by the **prophets'
refrain** Q26:108/110/126/131/144/150/163/179 — *fa-ttaqū llāha wa-aṭīʿū**ni***
("fear Allāh and obey **me**"), spoken by Nūḥ/Hūd/Ṣāliḥ/Lūṭ/Shuʿayb — which the
divine-name gate **cannot** distinguish from divine speech (the name *Allāh*
appears, the *-ni* is the prophet's, not God's). Spearman ρ(A,B) = 0.41.

**This is the load-bearing negative result:** a density metric cannot recover the
tawḥīd-declaration class because (i) bare first-person is uttered by ~every speaker
in the Quran (humans, prophets, hypocrites, the damned), and (ii) the canonical
tawḥīd-declarations are **long** verses (āyat al-kursī = 50 words; Q112 = 4 verses)
whose self-disclosure is *spread*, not *packed*. Density rewards brevity, not
theological weight. The recognized tawḥīd class is identified by *content + length +
formula*, NOT by first-person-token density.

## 4. Relationship to the parent Q020-F-05

Q020-F-05 reported Q20:14 as **rank-1 within Ṭā-Hā**. Under the stricter QAC
Metric-A, Q20:14 is **rank-2 within Ṭā-Hā** (behind Q20:41 *wa-aṣṭanaʿtuka
li-nafsī*, a 2-word all-clitic verse, density 1.0). The within-surah finding is
therefore **rules-tuple-fragile**: the original regex numerator + denominator put
Q20:14 first; the morphology-grounded count promotes a 2-word clitic verse above it.
Q020-F-05's *qualitative* point (Q20:14 is an exceptionally self-disclosure-dense
verse) survives — it is still corpus-rank-7 of 6236 — but its *rank-1* claim does
not survive the corpus-wide, morphology-grounded re-grounding, in or out of surah.

## 5. Honest limits

- The word-shuffle null is conservative-correct: it preserves the corpus word-bag
  and each verse's length, isolating *placement*. It shows placement adds nothing
  beyond length. A different null (e.g., free-length) would trivially "confirm"
  concentration by exploiting length — which is why it was not pre-registered.
- Speaker attribution in the top-table is by standard tafsīr/context (al-Ṭabarī,
  Ibn Kathīr) and is descriptive, not part of any pass/fail gate. The point holds
  regardless of exact attribution: the top is not the tawḥīd-declaration class.
- This is NOT a claim that divine self-disclosure is unimportant — only that
  *token-density* is the wrong instrument for surfacing it. A length-aware or
  formula-anchored instrument (count of tawḥīd-formulae per surah; presence of the
  *lā ilāha illā* construction) is the correct future tool; H-NEW-2510 establishes
  the density instrument is reversed for this target.

## 6. Cross-references

- Parent: Q020-F-05 (§10.120), `surahs/Q020-ta-ha/csv/Q020-F-05.json`.
- Theological-iʿjāz axis (al-Khaṭṭābī, *iʿjāz al-maʿnā*): Q 112 is the corpus
  FR-centroid and *thuluth al-Qurʾān* (al-Bukhārī #5013–5015) yet ranks 609/2 on
  this density metric — re-confirms that **theological weight ⊥ token-density**,
  consistent with the dual-iʿjāz typology (Protocol §3.4).
- Divine-name distribution: H-NEW-620 (divine-name density), H-NEW-239
  (divine-name gradient) — those are *name*-only and length-normalized differently.
- Method pillar reinforced: **brevity confounds density metrics** — the same
  length-confound that the compression-tail laws (Protocol §3.1) handle by
  length-controlled nulls.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
