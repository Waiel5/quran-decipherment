---
surah: 2
surah_name_ar: البقرة
surah_name_translit: al-Baqara
file_type: empirical-profile
date_last_updated: 2026-04-28
phase: B+
verdict: SCAFFOLD-COMPLETE — full empirical profile integrated from H-NEW-111, 590, 700, 720, 750, 840, 95
---

# Q 2 al-Baqara — Empirical Profile


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

This file integrates all corpus-wide empirical findings that touch Q 2. Numbers are computed from the canonical mushaf (Hafs-Kufan) and the named pre-registered findings; every claim cites a specific JSON artifact under `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/` or a derivation script.

---

## 1. Master architectural identity

| Axis | Q 2 value | Rank | Source | Interpretation |
|:--|:--|:--:|:--|:--|
| **UAS (composite)** | **7.396** | **3 / 114** | [[h-new-840-unified-architectural-score]] | Top-3 corpus-significant; bracketed by Q 33 (rank 1, UAS=9.36) and Q 1 (rank 2, UAS=8.87) |
| **\|outlier-strength Δ%ile\|** | 20.62 | 1 / 114 (anchor side) | [[h-new-590-outlier-spectrum]] | **CORPUS-STRONGEST cohesion-anchor** — only surah whose presence increases its 7-window cohesion by more than 20pp |
| **max-neighbor TSP cost** | 0.6216 | 1 / 113 | [[h-new-720-canonical-adjacency-cost]] | Q1→Q2 is the corpus's **single most expensive canonical adjacency** (7.50% of total TSP residual) |
| **\|iʿjāz signature sig_A\|** | 0.997 | 30 / 114 (low end) | [[h-new-750-per-surah-iʿjāz-signature]] | LOW iʿjāz al-fawāṣil: rank 85 of 114 (sig_A = −0.997) — Q 2 is structural-iʿjāz, not fāṣila-variety iʿjāz |
| **iʿjāz signature sig_B** | −0.037 | rank 60 / 114 | [[h-new-750]] | Near-mean — neither distinctively meaning-iʿjāz nor anti-iʿjāz |

**Architectural type**: Q 2 is the corpus's **structural-core** — high outlier-strength + maximal local-TSP cost + LOW *iʿjāz al-fawāṣil*. This is a fundamentally different architecture from Q 1 (which is high on all three axes including sig_A), or Q 33 (highest outlier + medium cost + high \|sig_A\|).

This places Q 2 as **the al-Bāqillānī test-case-of-second-kind**: a top-3 architectural surah whose distinctness comes from content-distribution (al-Bāqillānī's *taʿālluq al-maʿānī*), not from rhyme-density (*iʿjāz al-fawāṣil*).

---

## 2. Outlier-strength decomposition (H-NEW-590)

From `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-590.json`:

```
Q 2 record: {
  "X": 2,
  "window": [1, 2, 3, 4, 5, 6, 7],
  "window_minus_X": [1, 3, 4, 5, 6, 7],
  "d_W": 0.9154,           // mean pairwise FR distance, full window
  "d_W_minus_X": 0.9550,   // mean pairwise FR distance, window minus Q 2
  "pct_W": 37.9,           // percentile of d_W against random 7-windows
  "pct_W_minus_X": 58.52,  // percentile of d_W_minus_X
  "delta_pct": -20.62,     // Q 2 REDUCES the percentile by 20.62pp
  "classification": "COHESION_ANCHOR"
}
```

**What this says**: When you remove Q 2 from its 7-window (Q 1-7), the window's mean pairwise FR distance JUMPS from 0.9154 to 0.9550. The window goes from the 37.9th percentile (relatively cohesive) to the 58.5th percentile (above-mean dispersion). Q 2 is acting as a **content-gravity-well**: it pulls neighbors into closer thematic proximity by means of its enormous, content-rich vocabulary.

The outlier-spectrum produced no other surah with Δ < −20pp on the cohesion-anchor side; Q 51 is at −16.17, Q 3 at −15.28, Q 23 at −10.91. Q 2's effect is **27% larger** than the next-strongest anchor (Q 51).

### Anchor-side ranking (most-negative Δ first)

| Rank | Surah | Δ%ile | Class |
|:--:|:--:|:--:|:--|
| 1 | **Q 2** | **−20.62** | COHESION_ANCHOR |
| 2 | Q 51 | −16.17 | COHESION_ANCHOR |
| 3 | Q 3 | −15.28 | COHESION_ANCHOR |
| 4 | Q 23 | −10.91 | COHESION_ANCHOR |
| 5 | Q 52 | −10.82 | COHESION_ANCHOR |
| 6 | Q 45 | −10.68 | COHESION_ANCHOR |

Notable: of the corpus's six COHESION_ANCHOR surahs (Δ ≤ −10), three are al-sabʿ al-ṭiwāl (Q 2, Q 3) or close mufaṣṣal (Q 23, Q 51, Q 52, Q 45) — supporting the hypothesis that the long-Medinan/Qāf-cluster surahs share a content-dense anchoring role.

---

## 3. Canonical-adjacency cost decomposition (H-NEW-720)

From `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-720.json`:

| Adjacency | L_constrained | δ (extra cost) | fraction-of-residual | Rank |
|:--|:--:|:--:|:--:|:--:|
| **Q 1 → Q 2** | 78.088 | **0.622** | **7.50%** | **1 (most expensive of 113)** |
| Q 2 → Q 3 | 77.483 | 0.0165 | 0.20% | 91 (very cheap) |

**Architectural reading**: The mushaf pays its single largest TSP-tax for joining Q 1 (al-Fātiḥa) to Q 2 (al-Baqara), but the very next adjacency Q 2 → Q 3 (āl-ʿImrān) is essentially **free** (in fact 91 of 113 adjacencies are more expensive). This asymmetry is striking — it tells us:

1. **Q 1 and Q 2 are not natural neighbors in content-distribution space.** Q 1 is the densely-packed prayer-creed (29 words); Q 2 is the colossal Medinan legislative-narrative-creed compendium (6,630 words). Their immediate adjacency is a **structural choice**, not a content-cohesion artefact.
2. **Q 2 and Q 3 are natural twins** ("the two flowers" / *al-Zahrāwān* — see hadith corpus). The cheapness of this adjacency reflects classical recognition: al-Bukhārī ḥadīth #4811 has the Prophet ﷺ pairing them as "the two lights" / "two clouds" / "two flocks of birds." Empirical TSP-cost vindicates the classical pairing intuition.

The Q1-Q2 expensive adjacency joins the project's "tartīb tawqīfī" evidence-set: the mushaf pays expensive transitions to enforce specific commitments (Q 1 first; Q 33 hub; Hijra hinge at Q 56-57). Q1-Q2 is the FOREMOST such commitment.

### Cumulative TSP statistics for context

- L_mushaf = 85.760
- L_2opt_unconstrained = 77.467
- residual = 8.293 length-units (10.7% of mushaf)
- Σ Δ_113 = 9.827 (ratio_to_residual 1.185× — super-additive 16% over independent constraint sum)
- Q 1-Q 2 alone accounts for 7.50% of the 8.293 residual.

---

## 4. iʿjāz-signature decomposition (H-NEW-750)

From `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-750.json`:

```
Q 2 per_surah: {
  "n_verses": 286,
  "rhyme_entropy_nats": 1.011,        // Shannon entropy of fāṣila-letter distribution
  "top_final_letter": "ن" (nūn),
  "top_final_letter_frac": 0.6748,    // 67.48% of fāṣila are -ūn/-īn/-ān
  "mean_content_distance": 1.069,
  "local_cohesion": 1.170,
  "z_rhyme_entropy": +0.437,           // 0.44σ above corpus mean (mid-range)
  "z_mean_content_distance": +1.434,   // 1.43σ above corpus mean (FAR from corpus center)
  "z_local_cohesion": -0.474,          // 0.47σ below corpus mean
  "sig_A": -0.997,    // = z_rhyme_entropy − z_mean_content_distance − z_local_cohesion (rank 85)
  "sig_B": -0.037,    // distance-from-iʿjāz-axis (rank 60)
  "rank_A": 85, "rank_B": 60
}
```

### What this says

- **Q 2 is FAR from corpus-centre in content-distance (z = +1.43)** — its root-distribution is highly distinctive against the rest of the corpus (it has more legal/civic/communal vocabulary than any other single surah).
- **Q 2 has only mid-range rhyme-entropy (z = +0.44)** — fāṣila-variety is moderately above mean, but two-thirds of its 286 verses end in nūn (-ūn/-īn/-ān). This is the *exact opposite* of the *iʿjāz al-fawāṣil* peak surahs (e.g. Q 86 al-Ṭāriq sig_A = +3.02).
- **The combination produces sig_A = −0.997**, ranking 85th of 114 (i.e., in the low-iʿjāz-al-fawāṣil tail). Q 2's structural significance does NOT come from rhyme-variety.

### iʿjāz top-10 vs Q 2

The structural-iʿjāz top-10 (by sig_A) is dominated by mufaṣṣal-qiṣār: Q 86, 84, 89, 96, 82, 106, 113, 81, 100, 70. Q 2 is nowhere near this group. **Q 2's high UAS therefore comes from \|outlier\|+\|TSP-cost\|, not from iʿjāz-signature.**

This is an empirically novel typology distinction:
- Q 1 is high on all three: outlier (+27.09), TSP-cost (0.622), sig_A (+1.27).
- Q 2 is high only on outlier (−20.62) and TSP-cost (0.622). sig_A (−1.00) DRAGS it down.
- Q 33 is high on outlier (+31.46) and sig_A (−2.97), only mid on TSP-cost (0.363).

These three top-UAS surahs are **architecturally non-redundant**: each occupies a different sub-region of the 3-axis space.

---

## 5. Phonological window-profile (H-NEW-700)

The corpus-wide rhyme-dispersion law is `d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50)` (R²=0.789). The phoneme-dispersion law is `d̄_phoneme(s) ≈ 0.001 + 0.00089·max(0, s−75)` (R²=0.946).

For the 15-window starting at s=2 (covering Q 2-Q 16):

- **Rhyme d̄ = 0.2997 — the corpus minimum** (rank 1 of 100 windows). Source: `h-new-700.json → rhyme.best_window`.
- **Phoneme d̄ = 0.00190 — the corpus minimum** (rank 1 of 100 windows). Source: `h-new-700.json → phoneme.best_window`.

**Interpretation**: The 15-window beginning at Q 2 has the **most uniform rhyme distribution AND the most uniform phoneme distribution** of any 15-window in the corpus. This is consistent with two facts:
1. The 7 long surahs (Q 2-7, 9 or 10) are predominantly nūn-rhymed Medinan legal/narrative prose.
2. Their phoneme distributions track each other very closely.

**Empirical implication**: The phonological compression-tail law's "maximum dispersion" zone is clearly NOT Q 2-onward; it is Q 75-onward (the kink). Q 2 lives in the "low-dispersion plateau" of both laws.

### Q 2's phoneme vector (4-dim)

`[0.0171, 0.0429, 0.0336, 0.1086]` — the four canonical phoneme-densities (emphatic / pharyngeal / sibilant / glottal) for Q 2. Notable: Q 2 has the **highest glottal density (10.86%)** of the four-surah opening cluster (Q 1 has 0.056). This tracks Q 2's heavy use of *Allāh* (282 tokens) and *Allāh*-bound divine attributes.

---

## 6. Fisher-Rao distance-matrix neighborhood (H-NEW-111)

`h-new-111.json` provides the 114×114 Fisher-Rao distance matrix on QAC stem-roots. Q 2's row reveals its corpus-position:

- **Q 2's mean FR-distance to other 113 surahs = 1.069** (z = +1.43 above corpus mean ≈ 0.95).
- Q 2's nearest neighbors in FR space are NOT the canonical neighbors (Q 1, Q 3) — the canonical adjacencies are EXPENSIVE (Q1-Q2 = 0.622, the corpus max).
- Q 2's nearest FR neighbors are other long-Medinan: Q 5 (al-Māʾida), Q 4 (al-Nisāʾ), Q 9 (al-Tawba), Q 24 (al-Nūr) — exactly the al-sabʿ al-ṭiwāl + Medinan-legal cluster. (Specific distances available in h-new-111.json; cross-reference cross-finding-010 for hub-architecture.)

The cross-finding-010 4-region architecture identifies Q 2 as a **HUB-HEMISPHERE-ANCHOR** in the southern-content-anchor region, not a satellite. Q 2's role is to anchor the long-Medinan content-region (Q 2-9 + scattered Medinan) against the mufaṣṣal compression-tail (Q 78-114).

---

## 7. Structural metrics computed directly from text

(Computed 2026-04-28 from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`.)

| Metric | Q 2 | Corpus | Q 2 / corpus |
|:--|--:|--:|--:|
| Verses | 286 | 6,236 | n/a |
| Words (no-tashkeel, whitespace-tokenized) | 6,630 | 82,375 | 8.05% of corpus |
| Letters (no-tashkeel, no spaces) | 26,739 | 335,287 | 7.97% of corpus |
| Words / verse | **23.18** | 13.21 | 1.756× |
| Letters / verse | 93.49 | 53.77 | 1.739× |
| Letters / word | 4.033 | 4.070 | 0.991× |

**Q 2 verses are 75% longer than the corpus mean** (by either word- or letter-count). This places Q 2 at rank 5 of 114 in words/verse, after Q 60 (29.00), Q 65 (26.08), Q 5 (25.39), Q 58 (23.45). All 5 top-words/verse surahs are Medinan. Confirms compression-tail Law-4 (verse-length compression-tail R²=0.81 from H-NEW-770).

The classical numerology coincidence of `6,630 / 286 = 23.182` words/verse has no special arithmetic property (not divisible by 19, not prime, no factor-of-114 structure), but is in fact the signature of Medinan-legal verbosity.

### "Allah" token density

- Q 2: 282 *Allāh*-form tokens (matches *الله/لله/بالله/والله/فالله/ولله/تالله*) / 6,630 words = **4.253%**.
- Corpus: 2,689 / 82,375 = 3.264%.
- Q 2 / corpus density ratio: **1.303×** — Q 2 is 30% more *Allāh*-dense than corpus mean.

### Prophet/forefather frequencies in Q 2

(Q 2 holds 8% of the corpus by word, so the "expected" share for any name is ~8%.)

| Name (Hafs orthography) | Q 2 count | Corpus count | Q 2 share | Over/under-represented |
|:--|--:|--:|--:|:--|
| إبراهيم (Ibrahim) | 15 | 69 | **21.7%** | 2.7× expected |
| إسماعيل (Ismail) | 5 | 12 | **41.7%** | 5.2× expected |
| إسحاق (Ishaq) | 3 | 17 | 17.6% | 2.2× expected |
| يعقوب (Yaqub) | 4 | 16 | 25.0% | 3.1× expected |
| موسى (Musa) | 13 | 136 | 9.6% | 1.2× expected |
| عيسى (Isa) | 3 | 25 | 12.0% | 1.5× expected |
| سليمان (Sulayman) | 2 | 17 | 11.8% | 1.5× expected |
| داوود (Dawud) | 1 | 16 | 6.2% | 0.8× expected |
| يوسف (Yusuf) | 0 | 27 | 0.0% | 0× — entirely absent |
| نوح (Nuh) | 0 | 50 | 0.0% | 0× — entirely absent |
| آدم (Adam) | 5 | 25 | 20.0% | 2.5× expected |
| إسرائيل (Israel, free or in *banū Isrāʾīl*) | 6 | 43 | 14.0% | 1.7× expected |

**Pattern**: Q 2 is over-represented in **Adam** and **the Abrahamic chain** (Ibrahim, Ismail, Ishaq, Yaqub) by 2.5×–5.2×. It is at-or-near expected for Musa/Isa, and entirely absent for Yusuf/Nuh. This empirically grounds the classical observation that Q 2 is the Quran's foundational treatment of the **Adam–Ibrahim chain as the genealogical core of the Abrahamic settlement**, with Joseph and Noah handled in their own dedicated surahs (Q 12, Q 71). The cow-narrative (verses 67-71) supplies the surah's name; but Adam (verses 30-39) and Ibrahim (verses 124-141) supply the surah's foundational mytho-historical anchors.

---

## 8. Special-verse computations

### Q 2:255 — āyat al-kursī

(Computed from `/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, verse cleansed of pause-marks ۚۖۗ.)

- Words (no-tashkeel, whitespace-tokenized): **50** (some popular sources say 57 or 58; the 50 figure uses no-tashkeel words after pause-mark removal — confirms classical count is sensitive to whether sentence-divider sukūn-marks are word-internal).
- Letters (no-tashkeel, no spaces): **189** (popular: 182 — same tashkeel/orthography sensitivity).
- *Allāh*-form tokens: 1 (only the opening *Allāhu*; remaining divine references are pronominal/attributive).
- Number of distinct attributive divine names referenced: ~6 (al-Ḥayy, al-Qayyūm, al-ʿAlī, al-ʿAẓīm, ʿālim, etc.) — this is the Quran's densest *attributive* divine-naming verse outside Q 59:22-24.

The 114chambers ring-composition decomposition (claim-id `ayat-al-kursi-chiasmus`) of Q 2:255 into 9 sections with humanity at the centre is on the project's audit list (see [[Q002-F-04-ring-structure-prereg]]); the 57-word claim's source is unreliable (popular blog).

### Q 2:284-286 — khawātim al-Baqara

| Verse | Words | Letters | Allāh-form count |
|:--|--:|--:|--:|
| Q 2:284 | 31 | 106 | 1 (الله occurs once explicitly) |
| Q 2:285 | 30 | 121 | 1 |
| Q 2:286 | 55 | 202 | 1 |
| **Total** | **116** | **429** | **5** (incl. لله and بالله forms) |

- *Allāh*-token density across Q 2:284-286 = 5/116 = **4.31%**, matching Q 2's surah-mean (4.25%) — i.e., the khawātim are NOT divine-name-density anomalous.
- **Khawātim 9-name (asmāʾ al-ḥusnā subset Q 59:22-24) test** (H-NEW-95): Q 2:284-286 contains **zero** of the 9 specific khawātim names (al-Quddūs, al-Salām, al-Muʾmin, al-Muhaymin, al-Jabbār, al-Mutakabbir, al-Khāliq, al-Bāriʾ, al-Muṣawwir). Q 59 al-Ḥashr is rank 1 with 9 tokens; Q 2 is **rank 9** (tied with multiple zero-token surahs).

**Implication for *khawātim al-Baqara* claim**: The classical hadith assigns these 3 verses extraordinary virtue (al-Bukhārī #4802, "kafatāhu" — "they suffice him"). But the project's H-NEW-95 measurement of *9-name divine-name density* identifies **Q 59:22-24 as rank 1**, NOT Q 2:284-286. Q 2:284-286's virtue (per al-Bukhārī) is rooted in *content* (creed of universal-prophet acceptance + abrogation of "interior thought" punishment) NOT in 99-name density. This is an **iʿjāz al-maʿnā** profile, not an *iʿjāz al-fawāṣil* one.

Q 2:285-286 also includes the only canonical Quranic "supplication-with-amen-response" (per Ibn Kathīr citing Mu'ādh's practice of saying "Āmīn" after "fa-anṣurnā ʿalā al-qawmi al-kāfirīn") — making it a structural pair to al-Fātiḥa's terminal duʿāʾ.

### Q 2:282 — āyat al-dayn (verse of debt)

Q 2:282 is **the longest single verse in the Quran by word and letter count** (popularly cited; verified at 130 words / ~525 letters in our no-tashkeel computation; this verse is testable via the [[Q002-F-05-q2-282-longest-verse-prereg]] specialist test).

### Q 2:143 — āyat al-wasaṭ (verse of the middle)

Q 2:143 contains the foundational "*ummatan wasaṭan*" claim:
- 286 verses ÷ 2 = 143 — exact midpoint by verse-index.
- This positional coincidence is the centerpiece of Farrin (2010) and the linguisticmiracle.wordpress.com argument (claim-id `baqarah-middle-ayah-143`). The TYPE of "middle-ness" claimed is positional (verse 143 of 286 is the midpoint), but Farrin's broader argument is *thematic* (verses 142-152 form section E, the chiastic centerpoint of his nine-section ring).
- Whether this midpoint is **statistically anomalous** vs the "verses about social/communal-balance themes randomly placed" null is a target for the [[Q002-F-04-ring-structure-prereg]] test.

---

## 9. Cluster membership

| Cluster | Members | Q 2 status |
|:--|:--|:--|
| al-sabʿ al-ṭiwāl (Seven Long) | Q 2, 3, 4, 5, 6, 7, +(9 or 10 — disputed) | Member; the longest member |
| Muqaṭṭaʿāt-cluster (29 surahs) | All ALM/ALR/ḤM/etc. opening surahs | Member; opens with ALM (the most common 3-letter prefix) |
| ALM-6 (specific letter-family) | Q 2, 3, 29, 30, 31, 32 | Member; the prototype |
| Madanī (Medinan) | 28 surahs by classical reckoning | Member; the FIRST sustained Medinan revelation (chronological position 87, mushaf position 2) |
| al-Zahrāwān (the two flowers) | Q 2 + Q 3 | Member; classical pair (Sahih Muslim #1766, Bukhari ḥadīth) |
| Long-Medinan content-anchor cluster | Q 2, 3, 4, 5, 8, 9, 24, 33, 47-49, 57-66 | Hub of this cluster |

---

## 10. Cross-references to H-NEW findings touching Q 2

- [[h-new-590-outlier-spectrum]] — Q 2 rank 1 anchor, Δ=−20.62.
- [[h-new-720-canonical-adjacency-cost]] — Q1-Q2 rank 1 expensive (7.50% of TSP residual); Q2-Q3 rank 91 cheap.
- [[h-new-840-unified-architectural-score]] — Q 2 UAS rank 3 of 114.
- [[h-new-750-per-surah-iʿjāz-signature]] — Q 2 sig_A rank 85 (low iʿjāz al-fawāṣil), sig_B rank 60 (mid).
- [[h-new-700-phonological-compression-tail]] — Q 2-onward 15-window has the corpus-MIN rhyme & phoneme dispersion.
- [[h-new-95-khawatim-divine-names]] — Q 2:284-286 contains 0 of the 9 al-Ḥashr khawātim names; rank 9 of 114 by density (tied).
- [[h-new-111-fisher-rao-distance]] — Q 2 mean-FR-distance = 1.069 (z=+1.43).
- [[h-new-580-five-factor-regression]] — Q 2's high cohesion-anchor status partially derives from {block-adjacency: high; register: Medinan-legal; chrono: late-revealed but mushaf-early; formula: muqaṭṭaʿāt; outlier: anchor — all "tight" factors}.
- [[h-new-770-verse-length-compression-tail]] — Q 2 is rank-5 in words/verse (23.18, vs corpus 13.21); confirms verse-length compression-tail Law-4.
- [[h-new-770]] — Q 2:282 is the longest single verse in the corpus.
- [[h-new-860-hadith-architectural-alignment]] — Q 2 has both high hadith-fadāʾil rank AND high UAS rank 3. The CONVERGENCE of meaning-iʿjāz and structure-iʿjāz at Q 2 is the corpus's strongest such convergence (cf. Q 33 has high UAS but mid hadith; Q 112 has high hadith but bottom UAS).

---

## 11. Honest limits

1. **Outlier-strength replication failure**: H-NEW-590's pre-registered Q 55 replication failed (pre-reg required Q 55 ≥ 20pp, observed +14.26). The framework still passes rank-stability checks but the strict replication is NULL. This affects confidence in Q 2's −20.62 figure: the value is reproducible across rules-tuple variations (no-tashkeel/min-tashkeel, with/without basmala) but the OOS-replication threshold was not met. Rules-tuple sensitivity is moderate.

2. **TSP-cost is heuristic**: H-NEW-720 is best-of-10-restart 2-opt; absolute optimum may be slightly lower. The Q1-Q2 RANK as #1 most-expensive is robust (Δ-margin to Q32-Q33 is 0.622 vs 0.363, ratio 1.71×).

3. **Word-count discrepancy with classical sources**: Ibn Kathīr (citing classical counts) gives Q 2 = 287 verses, 6,221 words, 25,500 letters (line 49 of `/Users/grey/Downloads/quran/data/literature/classical-tafsir/raw/ibn-kathir-en-Q002.txt`). Wikipedia gives 6,116 words / 25,900 letters. Our no-tashkeel computation gives 286 verses / 6,630 words / 26,739 letters. Discrepancies derive from (a) verse-count tradition (Hafs-Kufan = 286; some traditions add the basmala = 287), (b) word-tokenization rules (proclitics counted as separate or not), (c) whether shadda counts a letter once or twice. **All numerical claims in this profile use the no-tashkeel, whitespace-tokenized, Hafs-Kufan, no-basmala-counted convention.**

4. **iʿjāz signature interpretation** (sig_A = −0.997): the negative value reflects HIGH content-distance + LOW rhyme-entropy(z); a literal reading is "Q 2 is far from corpus content-mean BUT with normal-ish rhyme-entropy, so the *contrast-axis* (al-Bāqillānī's structural inimitability via fāṣila + content) is anti-aligned." This does NOT mean Q 2 has no rhetorical brilliance — it means Q 2's rhetorical brilliance is NOT in fāṣila-variety. al-Sakkākī's *iqāʿ*-dispersion law (H-NEW-700) confirms: Q 2 is in the LOW-iqāʿ-dispersion plateau.

5. **Q 2:255 word/letter counts diverge from popular sources**: Our computation gives 50 words / 189 letters; popular Arab-blog sources say 57/182; the 114chambers source claims 57 words = 3×19 (a Code-19 echo). The Code-19 framework has been falsified across the project (see [[h-new-127]] series). The popular 57 is presumably counting in min-tashkeel orthography (where shadda doubling adds tokens) or counting compound proclitic+root words separately. Our 50/189 comes from no-tashkeel + whitespace.

---

*Computation script: ad-hoc Python integrating h-new-590/700/720/750/840/95.json, quran-no-tashkeel.json. All values reproducible 2026-04-28; rules-tuple `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)` unless noted.*
