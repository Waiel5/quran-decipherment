---
surah: 57
surah_name_ar: الحديد
file_type: empirical-profile
date_last_updated: 2026-05-09
phase: B+
verdict: COMPLETE — empirical metrics integrated from H-NEW-58c, H-NEW-720, H-NEW-750, H-NEW-840, H-NEW-1080, H-NEW-143.1
---

# Q 57 al-Ḥadīd — Empirical Profile


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

## Headline

Q 57 sits at the **mushaf's structurally hardest seam (Q 56→Q 57, rank-1 root-bridge + 8th most-expensive TSP-cost)** and is the **first member of the H-NEW-1080 short-Medinan FR-cohesive block (Q 57-66)**. Its iʿjāz al-fawāṣil signature is moderate (rank 42/114), and its UAS rank is mid-corpus (~50/114). Architecturally, Q 57's significance lies NOT in surah-internal outlier metrics but in its position as a **mushaf-structural inflection point** — the entry-point to the Medinan-legal short-block + the rank-1 cross-boundary root-bridge.

## 1. UAS composite (H-NEW-840)

Source: `findings/phase-b-hypotheses/csv/h-new-840.json` (`all_uas[surah=57]`).

| Metric | Value | Rank |
|:--|:-:|:-:|
| **UAS** | **−0.200** | mid-corpus (~50/114) |
| abs_outlier (Δ-pp) | 0.32 | low |
| max_neighbor_TSP_cost | 0.227 | **rank 8/113** (Q 56→Q 57) |
| abs_iʿjāz_signature | 0.753 | rank 42/114 |

Q 57's UAS is a mild negative — its absolute architectural significance is mid-corpus. But the *driver* of its non-trivial UAS is the **max_neighbor_TSP_cost of 0.227**, indicating Q 57's neighbor-most-expensive transition (Q 56→Q 57) is among the corpus's hardest. This places Q 57 in a structurally distinct class: **architectural-position-significant**, not surah-content-outlier.

## 2. iʿjāz signature (H-NEW-750)

Source: `findings/phase-b-hypotheses/csv/h-new-750.json` (`per_surah[surah=57]`).

| Metric | Value | Rank |
|:--|:--|:--|
| n_verses | 29 | — |
| **rhyme_entropy_nats** (Shannon) | **1.386** | high (corpus mean ≈ 1.7; z=+1.12) |
| top_final_letter | ر (rāʾ) | — |
| top_final_letter_frac | 37.9% | non-monorhyme |
| mean_content_distance | 0.960 | z=+0.36 |
| local_cohesion | 0.986 | z=−0.72 |
| z_rhyme_entropy | +1.12 | high |
| **sig_A** | **+0.753** | **rank 42/114** — moderate iʿjāz al-fawāṣil |
| sig_B | +0.391 | rank 46/114 |

Q 57 is **NOT a sig_A outlier** (rank 42 is mid-pack). Its rhyme entropy is above corpus mean — Q 57 is closer to the iʿjāz-al-fawāṣil archetype than to the refrain/monorhyme archetype.

This contrasts sharply with **Q 55 al-Raḥmān** (sig_A = −3.173, rank 114/114, corpus-MINIMUM) two surahs prior. **The transition Q 55-monorhyme-refrain → Q 56-eschatology → Q 57-rhyme-balanced-Medinan-legal is itself a register-mode transition over 3 surahs**.

## 3. Final-letter distribution and rhyme structure

Computed from `quran-text/quran-no-tashkeel.json` after diacritic normalization:

| Final letter | Count | Fraction |
|:--|:-:|:-:|
| ر (rāʾ) | 11 | 37.9% |
| م (mīm) | 10 | 34.5% |
| ن (nūn) | 5 | 17.2% |
| ب (bāʾ) | 1 | 3.4% |
| د (dāl) | 1 | 3.4% |
| ز (zāy) | 1 | 3.4% |

The **rāʾ + mīm dyad accounts for 72.4% of fāṣila**. This is consistent with the divine-attribute *al-ʿAzīz al-Ḥakīm / al-Ḥakīm al-Ḥamīd / al-Baṣīr / al-Qadīr* pattern — Q 57's fāṣila are dominated by the active-participial divine-name endings.

## 4. Position in mushaf — universal hinge Q 56→Q 57

Source: `findings/phase-b-hypotheses/csv/h-new-720.json` (per_adjacency).

| Adjacency | δ (Fisher-Rao distance) | rank in 113 transitions |
|:--|:-:|:-:|
| Q 56 → Q 57 | **0.227** | **rank 8** (most-expensive end) |
| Q 57 → Q 58 | 0.021 | top-12% cheapest |

**Q 56 → Q 57 is one of the 3 universal hinges** identified in cross-finding-013 (Q 14→15, Q 49→50, Q 56→57) — boundaries that appear in the top-15 most-expensive transitions across **all three feature spaces** (roots, char-4-grams, verse-length). At Q 56→Q 57:

- **Period change**: Meccan (Q 56 al-Wāqiʿah, Late-Meccan eschatology) → Medinan (Q 57 al-Ḥadīd, Late-Medinan legal-exhortation)
- **Phase change**: Early-Meccan-resemblance → Medinan
- **Function change**: eschatological-warning → community-legal-formation

But the boundary is **bridged at root-level** — per H-NEW-143.1, **Q 56→Q 57 is the rank-1 root-bridge in the corpus** (cos-overlap 0.408, top of all 113 boundaries), with shared QAC-stem roots **sbḥ** (glorify) and **smw** (heavens). The mechanism: Q 56:96 closes with imperative *fa-sabbiḥ bismi rabbika al-ʿaẓīm* ("so glorify by the name of your mighty Lord"), and Q 57:1 opens with perfect-tense *sabbaḥa li-llāhi mā fī al-samāwāti wa-l-arḍ* ("All that is in the heavens and earth has glorified Allah"). The same root cycles from imperative-singular to perfect-cosmic.

This is one of the strongest empirical validations of **al-Biqāʿī's *munāsaba* (inter-surah continuity) doctrine** in the entire corpus — the seam is structurally hard at the content-distribution level (Fisher-Rao distance high) but rhetorically bridged at the root-level (sbḥ-echo).

## 5. Within-musabbiḥāt cluster centrality

Per Q057-F-01 (this folder, `csv/Q057-F-01.json`):

**Q 57 is FR-LEAST-CENTRAL within the 5-musabbiḥāt cluster** {Q 57, 59, 61, 62, 64}.

| Member | Mean FR distance to other 4 members | Rank (ascending = central) |
|:--|:-:|:-:|
| Q 64 | 0.736 | **1** (most central) |
| Q 61 | 0.763 | 2 |
| Q 59 | 0.774 | 3 |
| Q 62 | 0.782 | 4 |
| **Q 57** | **0.797** | **5** (least central) |

Within the 7-cluster (adding Q 17 noun-form and Q 87 imperative-form), Q 57 ranks 5/7 in centrality — Q 64 al-Taghābun is empirically the most central musabbiḥa, NOT Q 57 al-Ḥadīd despite being the first-by-mushaf-position.

**Asymmetric tense-cluster bridge**: Q 57's mean distance to perfect-tense siblings (Q 59, Q 61) = 0.809, while its mean distance to imperfect-tense surahs (Q 62, Q 64) = 0.786. **Q 57 is FR-CLOSER to the imperfect tense than to its own perfect tense siblings** — a notable asymmetry that complicates the H-NEW-58c "perfect/imperfect binary partition" reading at the FR-content level (the binary holds at the **opening-prefix character level** but not at the **whole-surah Fisher-Rao distance level** for Q 57 specifically). See `06-novel-findings.md` §1 for honest analysis.

## 6. Position in compression-tail laws

Q 57 is at s=57, just past the s=50 mufaṣṣal-onset kink. Predicted vs actual:

| Law | Equation | Predicted at s=57 | Actual |
|:--|:--|:-:|:-:|
| Content compression | d̄_content(s) ≈ 0.96 − 0.012·max(0, s−50) | 0.876 | 0.960 (above predicted; consistent with the post-hinge content-rebound at the universal-hinge crossing) |
| Rhyme dispersion | d̄_rhyme(s) ≈ 0.36 + 0.0041·max(0, s−50) | 0.389 | rhyme_entropy 1.386 (uses different units; cf. corpus mean 1.71) |

Q 57 sits **just past the universal hinge** — its content distance is +0.084 above local prediction, consistent with a content-mode rebound at the post-hinge point.

## 7. Architectural type classification

**Mid-corpus content-density + universal-hinge-position + first-of-block:**

Q 57 belongs to the structural class identified as **"hinge-entry surahs"** — surahs that sit immediately after a universal-hinge boundary and serve as the entry-point to a downstream cohort. The other two universal-hinge-entry surahs are:

- **Q 15 al-Ḥijr** (after Q 14→15 hinge)
- **Q 50 Qāf** (after Q 49→50 hinge)
- **Q 57 al-Ḥadīd** (after Q 56→57 hinge) — **THIS surah**

In the dual-iʿjāz typology of H-NEW-840:
- **structural-iʿjāz** (al-Bāqillānī): Q 33, 1, 2, 9, 24 — high UAS via content + rhyme balance.
- **theological-iʿjāz** (al-Khaṭṭābī): Q 112, 114 — low UAS, high *thuluth* status.
- **refrain-iʿjāz**: Q 55 — high UAS via content + REFRAIN-density.
- **architectural-position-iʿjāz** (proposed for Q 57): mid-UAS via universal-hinge + first-of-block + rank-1-root-bridge entry.

This is a 4th provisional class. Cross-reference [[cross-finding-026-iʿjāz-architecture]] and [[cross-finding-013-mushaf-topological-ring]] for the project-level discussion.

## 8. Cross-references to all H-NEW findings touching Q 57

| Finding | Q 57 role |
|:--|:--|
| [[h-new-58c-musabbihat-tense-split]] | Q 57 in perfect-tense sub-cluster |
| [[h-new-103-musabbihat-4form]] | Q 57 in PERFECT verbal class (1 of 3) |
| [[h-new-111-fisher-rao-mushaf]] | source of Q 57 FR distances |
| [[h-new-130c-fisher-rao-residuals-verselen]] | Q 56→Q 57 universal hinge confirmed (3-way: roots+char4+verselen) |
| [[h-new-142-universal-hinges-chrono-rhetorical]] | Q 56→Q 57 cosmic-rhetorical-bridge anchor |
| [[h-new-143-1-root-bridge]] | **Q 56→Q 57 is RANK 1 of 113 root-bridges** (cos=0.408, sbḥ + smw) |
| [[h-new-720-canonical-adjacency-cost]] | Q 56→Q 57 = 0.227 (rank 8 expensive); Q 57→Q 58 = 0.021 (top-12% cheap) |
| [[h-new-750-per-surah-iʿjāz-signature]] | sig_A = +0.753 (rank 42/114) |
| [[h-new-840-unified-architectural-score]] | UAS = −0.200 (mid-corpus ~50/114) |
| [[h-new-1080-short-medinan-block]] | Q 57 is the 1st of the FR-cohesive Q 57-66 block |
| [[h-new-1120-divine-name-pair-distribution]] | 4-pair tetrad corpus-UNIQUE to Q 57:3 |
| [[cross-finding-013-mushaf-topological-ring]] | Q 56→Q 57 universal-hinge member |
| [[hadid-deep-dive]] | earlier deep-audit; iron-abjad numerology REFUTED |

## 9. Honest limits

- **Q 57 is NOT an outlier on UAS** — its architectural significance is positional (universal-hinge entry), not surah-internal.
- **Within-musabbiḥāt centrality is asymmetric**: Q 57 is FR-closer to imperfect-tense siblings than to its own perfect-tense siblings. The H-NEW-58c "binary tense split" holds at the OPENING-PREFIX-CHARACTER level (24-56 chars within tense, 0 across), not at the WHOLE-SURAH FR level.
- **The rank-1 root-bridge at Q 56→Q 57 is shared root-level (sbḥ + smw)**, but per H-NEW-143 the surface-WORD bridge test is NULL — the bridge is at root-stem, not at lemma. Disclose: H-NEW-143.1's "root-bridge" is a *post-hoc* re-operationalization after H-NEW-143's surface-bridge NULL. The Q 56→Q 57 rank-1 result holds under MW-7 single-test cap.
- **Iron-cosmology numerology is REFUTED** (cf. cross-finding-015 + `hadid-deep-dive.md`); we report the corpus-EXACT *anzala*-iron-singularity as a STRUCTURAL not NUMEROLOGICAL claim.
- **Tense-cluster reading is for OPENING-FORMULA only**; whole-surah content distinguishes Q 57 from its perfect-tense siblings on multiple axes.

## 10. Verdict

Q 57 is empirically a **mid-UAS surah with architectural-position significance**. Its three structural anchors (4-pair quartet at v 3, universal-hinge entry from Q 56, iron-descent at v 25) make it a **classical-anchor surah** with corpus-EXACT divine-name uniqueness at v 3 and rank-1 mushaf-root-bridge at its boundary. The classical *al-musabbiḥāt* honorific empirically tracks the *opening-formula* level (4-form typology per H-NEW-103) but **NOT the whole-surah Fisher-Rao centrality** for Q 57 specifically — the perfect-tense binary partition holds at v.1 character-prefix only.

**Q 57 is the 1st musabbiḥa by mushaf-position and the entry-point to the H-NEW-1080 short-Medinan block (Q 57-66).** Its iʿjāz architecture is NOT refrain-density (cf. Q 55) and NOT theological-singleton (cf. Q 112), but **structural-positional** — anchored at one of the mushaf's hardest seams.
