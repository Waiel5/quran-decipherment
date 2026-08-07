---
id: H-NEW-1310
title: Christ-narrative 3-surah cluster Fisher-Rao cohesion {Q 3, Q 5, Q 19}
date_locked: 2026-05-09
date_run: 2026-05-09
verdict: NULL (both cells; PC passed)
seed: 20260509
n_perm: 10000
prereg_sha: d131ca234513a5bd7f825707c0778a5dedfe6f04cea6dab6e0cba7f013b17996
prereg_path: findings/phase-b-hypotheses/h-new-1310-christ-narrative-cluster-prereg.md
script_path: findings/phase-b-hypotheses/scripts/h_new_1310_christ_narrative.py
output_json: findings/phase-b-hypotheses/csv/h-new-1310.json
---

# H-NEW-1310 — Christ-narrative 3-surah cluster Fisher-Rao cohesion {Q 3, Q 5, Q 19}


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

## Verdict: NULL

The pre-registered direction "the 3-surah Christ-narrative cluster {Q 3, Q 5, Q 19} forms a tight FR cohesion group" is **rejected on both cells** with a passing instrument-control:

| Cell | Result | p | Pass (α=0.025) |
|:--|--:|--:|:-:|
| A — uniform 3-of-113 null | obs 0.948 vs null mean 0.927 | 0.481 | NO |
| B — length-matched (±20% of 418v) | obs 0.948 vs null p5 0.887 | 0.187 | NO |
| MW-5 PC — H-NEW-1190 sub-sample {69, 97, 101} | obs 0.608 vs null p5 0.632 | 0.041 | **YES** |

The H-NEW-1190 *wa-mā adrāka mā* sub-sample passed instrument-control at p_pc = 0.041, confirming the FR matrix can detect known cohesion. **The NULL is therefore substantive, not instrument-broken.**

## Pairwise structure (descriptive only — not the test)

| Pair | FR distance |
|:--|--:|
| Q 3 ↔ Q 5 (both long Medinan, both shariʿa-heavy) | **0.698** |
| Q 3 ↔ Q 19 | 1.031 |
| Q 5 ↔ Q 19 | 1.116 |

Q 3 and Q 5 are tightly close at 0.698 — likely length + chronology + jurisprudence-register driven, not Christ-narrative-driven. Q 19 al-Maryam is **far from both**: its signature dominated by the Maryam/Zakariyyāʾ/Yaḥyā/Ibrāhīm/Mūsā/Ismāʿīl/Idrīs/Nūḥ prophet-cycle catalog (vv 41-58), not Christ-narrative specifically.

## Interpretation

The Christ-narrative content distribution across the corpus is too **thinly-spread** to drive root-distribution clustering. The relevant Christ-narrative passages occupy:

- Q 3 vv 33-63 (≈30 verses out of 200) — Annunciation, birth, Jesus's miracles, disciples
- Q 5 vv 17, 46-50, 72-78, 109-120 (≈25 verses out of 120) — Gospel, table-spread, Jesus's disavowal
- Q 19 vv 16-37 (22 verses out of 98) — Mary/Jesus episode (then wider prophet-cycle continues to v 58)

In each surah Christ-narrative is one block among multiple, not the dominant root-driver. The dominant root-distribution drivers per surah are:

- Q 3: kitāb / tawḥīd / hijra-era jurisprudence + Battle-of-Uḥud retrospective vv 121-179
- Q 5: ḥalāl/ḥarām code (food, hunting, oaths) + āyat al-ikmāl 5:3 + multi-religious-community framework
- Q 19: prophet-cycle catalog (Maryam → Ibrāhīm → Mūsā → Ismāʿīl → Idrīs → Nūḥ) — explicitly multi-prophet-narrative

Christ-narrative is a **shared content thread** but not a **shared root-signature**.

## Why this NULL is informative

This NULL refines the project's understanding of "thematic cluster" vs "structural cluster":

- **Confirmed structural clusters** (per existing findings): muqaṭṭāʿat (cross-finding-008, p ≤ 10⁻¹²), short-Meccan-tail eschatology (H-NEW-1200, p=0.00030), *wa-mā adrāka mā* (H-NEW-1190, p=0.00068), Khawātim al-Ḥashr (H-NEW-95), short-Medinan block (H-NEW-1080, p=0.049).
- **NULL "thematic" clusters** (per this finding + H-NEW-1301): IMPV-qrā 4-surah cluster, Christ-narrative 3-surah cluster.

**Rule of thumb emerging**: a content-theme drives FR cohesion only when the theme is the surah's DOMINANT root-driver, not when it's one block among many. Q 19's Christ-narrative is one of 6+ prophet-blocks; Q 3's is one of 5+ Medinan-jurisprudence-blocks. By contrast, Q 55 al-Raḥmān's *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* refrain dominates root-distribution corpus-EXACT (H-NEW-1250); the *wa-mā adrāka mā* meta-question dominates the 10 short-Meccan surahs that use it (H-NEW-1190). Domination, not mention, drives FR clustering.

## Connection to existing findings

- Q 3 ↔ Q 5 pairwise = 0.698 ranks among long-Medinan close-pairs. **Not a NEW finding**: this echoes the long-Medinan jurisprudential cluster already in cross-finding-009 and the H-NEW-89 hub structure.
- Q 19's distance from Q 3 and Q 5 (≥1.03) places it firmly in the prophet-cycle/short-Meccan signature, consistent with H-NEW-86 surah-name-as-key-root and the كهيعص singleton-cluster anchors.
- Cross-finding-013 ring-topology / M3: the 3 surahs are mushaf positions 3, 5, 19. Q 3-Q 5 are both M3-near (Q 4 al-Nisāʾ also long-Medinan); Q 19 sits 14 mushaf-positions away. The mushaf does not pull Christ-narrative surahs together either — consistent with M3 being a length+chronology architecture, not a thematic-bridge architecture.

## Honest limits

- **NULL by pre-reg with instrument-control passing**: this is the strongest form of NULL. Christ-narrative {3, 5, 19} is genuinely NOT FR-cohesive on root-distribution.
- **Only one feature space tested**: H-NEW-700 rhyme/phoneme, H-NEW-590 outlier-strength, char-4-gram, verse-length all untested. Christ-narrative might cluster on a non-root axis. Future H-NEW-1311 could replicate under H-NEW-700 rhyme.
- **Cluster identity locked from handoff text**: Q 4 (4:157-158 denial-of-crucifixion) and Q 43 (43:57-65 Jesus discussion) are NOT in the cluster. A 5-surah maximal Christ-content cluster {3, 4, 5, 19, 43} is a separate hypothesis requiring its own pre-reg.
- **"Christ-narrative" as a category is a Christian-tradition import**: in the Quran's own framing, the relevant category is *ʿīsā ibn maryam* + the *injīl* + the *ḥawāriyyūn*. The thematic granularity of "Christ-narrative" may not be the right Quran-internal category. A Quran-internal "Maryam-Zakariyyāʾ-Yaḥyā prophet-cycle" cluster would be {Q 3, Q 19, Q 21, Q 66:12} — different membership, different test.

## Follow-up moves (NOT yet locked)

- **H-NEW-1311** (queued): Replicate {3, 5, 19} cohesion on H-NEW-700 rhyme/phoneme features. Use H-NEW-1190 sub-sample for PC.
- **H-NEW-1312** (queued): Test Quran-internal *Mūsā* prophet-narrative cluster {Q 7, 20, 26, 28} for FR cohesion (Mūsā is the most-mentioned prophet in the Quran; ~136 mentions; corpus-EXACT-extreme prophet-block).
- **H-NEW-1313** (queued): Test the Maryam-Zakariyyāʾ-Yaḥyā prophet-cycle {Q 3 vv 33-44, Q 19 vv 1-15, Q 21 vv 89-90, Q 66:12} at the verse-twin level (H-NEW-66 instrument), where the cluster has coherent verse-block structure.

## Classical citations

- al-Ṭabarī, *Tafsīr*, on Q 3:33-63 (Annunciation + birth narrative parallel to Q 19:16-37); cross-references the two surahs as "two iterations of the Mary-Jesus narrative."
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on intra-Qurʾānic narrative-iteration (verify nawʿ-number against on-disk PDF).
- al-Biqāʿī, *Naẓm al-Durar*, on Q 3 — argues the Christ-narrative block is structurally subordinated to the Uḥud-retrospective frame, not the surah's primary axis. **Empirically supported by this NULL**.

## Verdict summary

| Quantity | Value |
|:--|--:|
| Cluster {Q 3, Q 5, Q 19} obs intra mean | 0.948 |
| Cell A uniform null p | 0.481 |
| Cell B length-matched p | 0.187 |
| MW-5 PC p (H-NEW-1190 sub-sample {69, 97, 101}) | 0.041 ✓ |
| **Verdict** | **NULL** |

The Christ-narrative thematic cluster is NOT a Fisher-Rao structural cluster on root-distribution. The Q 3 ↔ Q 5 sub-pair (FR=0.698) is real but driven by long-Medinan jurisprudence, not Christ-narrative.
