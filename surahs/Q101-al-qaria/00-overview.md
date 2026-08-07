---
surah: 101
surah_name_ar: القارعة
surah_name_translit: al-Qāriʿa
surah_name_english: The Calamity / The Striker
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD — full template built; 4 novel tests pre-registered + executed under Bonferroni-k=4
author: Waiel Al-Shujaa
---

# Q 101 al-Qāriʿa — Overview


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

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 101 | canonical |
| Arabic name | القارعة | canonical |
| Transliteration | al-Qāriʿa | canonical |
| English meaning | "The Calamity / The Striker / The Crashing One" — judgment-day name | classical (Ibn Kathīr) |
| Verse count | 11 | Hafs-Kūfan, `data/hafs-verse-counts.tsv` |
| Position in mushaf | 101 | canonical |
| Type | **Early Meccan** | `data/revelation-order.csv` Q101 row |
| Position in revelation order (Tanzil Egyptian Standard) | **30 / 114** | `data/revelation-order.csv` |
| Position in Nöldeke chronology | **24 / 114 (Early Meccan)** | `data/revelation-order.csv` `noldeke_phase = Early Meccan` |
| Word count (no-tashkeel) | **36** | computed from `quran-text/quran-no-tashkeel.json` |
| Letter count (no-tashkeel, all non-space chars) | **160** | same |
| Mean words/verse | **3.27** | computed |
| **Opening** | **القارعة ۚ ما القارعة ۚ وما أدراك ما القارعة** — "The Striker. What is the Striker? And what will make you know what the Striker is?" | self-naming triad with the *wa-mā adrāka mā* meta-question formula |
| Top rāwī (final-letter) | **ه (hāʾ)** at **81.8%** of 11 verses | computed from `h-new-750.json` (`top_final_letter_frac=0.8182`) |
| Sajda verse | none | classical |

## 2. ⭐ Corpus-distinctive structural property — central member of the *wa-mā adrāka mā* cluster

Q 101 is one of the 10 corpus-EXACT members of the *wa-mā adrāka mā* cluster, locked at law-strength under [[h-new-1190-wa-ma-adraka-cluster|H-NEW-1190]] (FR-cohesive at p = 0.00068, z = −4.65). The cluster is:

```
{Q 69, Q 74, Q 77, Q 82, Q 83, Q 86, Q 90, Q 97, Q 101, Q 104}
```

Every member opens an unknowable eschatological referent with the rhetorical question *wa-mā adrāka mā X* ("What will make you know what X is?"). Q 101 instantiates the formula **TWICE**: at v 3 (`wa-mā adrāka mā al-qāriʿa`) and at v 10 (`wa-mā adrāka mā hiyah`). Three cluster surahs use the formula twice (Q 82, Q 83, Q 101) — a corpus-EXACT 3-instance double-pattern within the 10-member cluster.

**Q101-F-01 (CONFIRMED)**: **Q 101 is RANK 1 of 10 in cluster centrality.** Its mean Fisher-Rao distance to the other 9 cluster members is `d̄ = 0.5232` — the lowest of any cluster member, meaning Q 101 sits at the *geometric center* of the *wa-mā adrāka mā* cluster on the H-NEW-111 root-distribution Fisher-Rao manifold. The full ranking (computed from `findings/phase-b-hypotheses/csv/h-new-111.json`):

| Rank | Surah | Mean intra-cluster FR |
|:-:|:-:|:-:|
| **1** | **Q 101** | **0.5232** |
| 2 | Q 104 | 0.5262 |
| 3 | Q 97 | 0.5562 |
| 4 | Q 86 | 0.5660 |
| 5 | Q 90 | 0.5842 |
| 6 | Q 82 | 0.5953 |
| 7 | Q 83 | 0.6487 |
| 8 | Q 77 | 0.7032 |
| 9 | Q 74 | 0.7377 |
| 10 | Q 69 | 0.7425 |

Q 101's tightness with Q 104 is so close (0.523 vs 0.526) that the two surahs effectively co-anchor the cluster's centroid. The pair (Q 101, Q 104) is the cluster's tightest pair: `d(Q 101, Q 104) = 0.3253` — well below the cluster mean.

**This is the gold-standard FR-cohesion empirical lock**: per cross-finding-025, the *wa-mā adrāka mā* cluster (with H-NEW-1200 short-Meccan eschatology) is the only confirmed FR-tight cluster on root-distribution. Q 101's centrality within it makes Q 101 a key empirical fixture — referenced as the canonical positive-control sub-sample for FR instrument-validity tests in subsequent pre-regs (e.g., H-NEW-1310 Christ-narrative cluster used Q {69, 97, 101} as PC; H-NEW-1330 used Q 101 as PC).

## 3. ⭐ The eschatological *al-qāriʿa* root concentration

The root **q-r-ʿ** (qāriʿa, the "Striker") occurs **EXACTLY 5 times in the corpus** (per `data/morphology/root-index.json` for `qrE`), and **3 of those 5 occurrences (60%) are in Q 101 alone** (vv. 1, 2, 3, comprising the title-triad). The other 2 occurrences are:

- Q 13:31 (al-Raʿd, prophet-narrative + warning)
- Q 69:4 (al-Ḥāqqa, eschatological — also a *wa-mā adrāka mā* cluster member)

This is a corpus-EXACT lexical cohesion: every occurrence of *q-r-ʿ* in the Qurʾān is in a surah dealing with eschatological warning, with the title-bearing surah Q 101 carrying 60% of the root's corpus distribution.

## 4. ⭐ Triple-naming of the Day of Judgment

Q 101 belongs to the small set of surahs that name the Day of Judgment itself:

- **al-Qāriʿa** (Q 101) — "the Striker / Crusher"
- **al-Ḥāqqa** (Q 69) — "the Reality"
- **al-Ṭāmma al-Kubrā** (Q 79:34) — "the Greatest Calamity"
- **al-Ṣākhkha** (Q 80:33) — "the Deafening Cry"
- **al-Wāqiʿa** (Q 56) — "the Inevitable"
- **yawm al-faṣl** (Q 77, Q 78) — "Day of Decision"

These are all in the short-Meccan-tail eschatology block (cross-finding-026 §13.5). Per Ibn Kathīr (`data/literature/classical-tafsir/spa5k-tafsir-api/en-tafisr-ibn-kathir/101.json`):

> "Al-Qāriʿa is one of the names of the Day of Judgment, like al-Ḥāqqa, al-Ṭāmma, al-Ṣākhkha and others."

Q 101's contribution is the **physical-impact metaphor** (*qāriʿa* = "the one that strikes / pounds"): the Day described as a violent percussive impact. This is reinforced by Q 101's Day-imagery: *kāl-farāshi al-mabthūth* ("scattered moths") and *kāl-ʿihni al-manfūsh* ("carded wool") — the cosmic-disruption signature of Early-Meccan eschatological imagery.

## 5. Length classification and registers

11 verses, 36 words — **mufaṣṣal-qiṣār-class** (terminal-tail short-Meccan zone). Per H-NEW-660 prediction: short surahs in the s ≥ 100 zone are in the deepest-cohesion segment of the mushaf (the post-kink-50 cohesion-tail).

Verse-length distribution: shortest verse Q 101:1 (1 word: *al-qāriʿa*); longest verse Q 101:4 (5 words: *yawm yakūn al-nāsu kāl-farāshi al-mabthūth*). Mean 3.27 w/v puts Q 101 firmly inside the corpus's terminal-tail "kerygmatic-burst" register.

## 6. Rhyme structure

Final-letter distribution across all 11 verses (per `h-new-750.json` `top_final_letter_frac=0.8182`):

| Final letter | % | Verses |
|:--:|:--:|:--|
| **ه (hāʾ)** | **81.8%** (9/11) — top rāwī | vv. 1, 2, 3, 6, 7, 8, 9, 10, 11 (after assimilation: *qāriʿa-h*, *mabthūth-...*, etc.) |
| ش (shīn) | 9.1% (1/11) | v. 5 (*manfūsh*) |
| (other / silent) | rest | |

The 81.8% top-rāwī fraction places Q 101 in the **monorhyme-tier** of the corpus. The رmā is the *rawī al-hāʾ* signature with the three-mode pattern: (1) *al-qāriʿa* in the title-triad with definite-article terminal hāʾ; (2) *rāḍiya* / *hāwiya* / *ḥāmiya* with feminine-ending *-iya* converging on hāʾ at pause; (3) *mabthūth* / *manfūsh* using verbal-passive feminine endings. This is a near-purely-monorhyme surah.

(Note: H-NEW-750's `rhyme_entropy_nats = 0.6002` is one of the lower in the corpus, reflecting this near-monorhyme.)

## 7. Q 100 → Q 101 → Q 102 → Q 103 mushaf neighbourhood

**Q 100 → Q 101 seam cost** (H-NEW-720): `delta_raw = 0.0286`, rank 29 / 113 (cheap). `fraction_residual = 0.0035` — well below the 1% threshold for "very smooth seam".
**Q 101 → Q 102 seam cost** (H-NEW-720): `delta_raw = 0.0287`, rank 30 / 113 (cheap). `fraction_residual = 0.0035`.
**Q 102 → Q 103 seam cost** (H-NEW-720): `delta_raw = 0.0480`, rank 44 / 113 (middle).

Q 101 is doubly-cheap-bordered: both its left edge (Q 100→101) and right edge (Q 101→102) are sub-1% residual seams. Q 101 sits at a low-friction junction in the mushaf reading-order TSP. (Note: not in the H-NEW-1240 13-clamped-zero-seamless set — those are negative-delta only, but Q 101's seams are inside the cheapest 30% nonetheless.)

The full Q 100-104 seam profile:

```
Q 100 → Q 101:  delta=0.0286 [rank 29, frac=0.35%]    cheap
Q 101 → Q 102:  delta=0.0287 [rank 30, frac=0.35%]    cheap  
Q 102 → Q 103:  delta=0.0480 [rank 44, frac=0.58%]    middle
Q 103 → Q 104:  delta=0.1157 [rank 88, frac=1.40%]    expensive
```

Q 103 → Q 104 is the local-maximum within the Q 100-104 sequence — the Q 103/Q 104 seam pays a structural cost transitioning from al-ʿAṣr (compressed-doctrinal) into al-Humaza (eschatological-condemnation). **The Q 101 ↔ Q 102 ↔ Q 103 trio sits in a coherence-bowl bordered by the Q 99/100 transition on the left and Q 103/104 on the right.**

See `01-empirical-profile.md` §3 for the full Fisher-Rao neighborhood.

## 8. The H-NEW-1190 cluster's classical lineage

Per al-Suyūṭī's *al-Itqān fī ʿulūm al-Qurʾān* (`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, nawʿ on rhetorical questions), the *wa-mā adrāka mā X* construction is identified as the standard interrogative-emphatic formula introducing the **sublime-unknowable** (*tafkhīm li-l-mafhūm*) in late-Meccan eschatological surahs. Al-Suyūṭī notes:

> "وما أدراك" فقد أخبر به ... وما يدريك" تركه ...
> Wherever Allāh says *wa-mā adrāka*, He has informed [the listener of the referent]; wherever He says *wa-mā yudrīka*, He has left it [unexplained].

Q 101 is the textbook example of the *informed* variant: the *al-qāriʿa* is named (v. 1), questioned (v. 2), wa-mā-adrāka-questioned (v. 3), then explained (vv. 4-11). Al-Suyūṭī cites Q 101:10 (*wa-mā adrāka mā hiyah*) as a corpus exemplar of *ḥadhf al-mubtadaʾ* (subject ellipsis in interrogative-answer constructions) — the second occurrence of the formula in the same surah is grammatically distinct from the first, supporting al-Rāghib al-Iṣfahānī's variant analysis cited by al-Suyūṭī inline.

## 9. Hadith corpus

See `04-hadith-corpus.md` for the full citation set across the 9-book canon. Key references:

- **Bukhārī ḥadīth on Day-of-Judgment names** (Bukhārī Kitāb al-Riqāq) — the Day is referred to by ~50 names; Q 101's *al-qāriʿa* is among the canonical list.
- **Tirmidhī (Kitāb al-Janna)**: Q 101's "scales-of-deeds" verse (vv. 6-9) is a primary scriptural reference for the doctrine of *mīzān* (the eschatological Balance) — paired in classical sermons with Q 7:8-9 and Q 23:102-103.

## 10. Connection to META cross-findings

- **cross-finding-025 (marker-thickness vs FR-cohesion)**: Q 101 is a core data point — sub-sampled as PC for downstream FR-cluster tests (H-NEW-1310, H-NEW-1330) given its membership in the only confirmed FR-tight short-mufaṣṣal cluster.
- **cross-finding-026 (mushaf architectural decomposition)**: Q 101 is in the *terminal-tail short-Meccan eschatology zone* (Q 78-104), directly upstream of the post-Q-104 transition into al-Fīl/Quraysh/al-Māʿūn (Q 105-107).
- **cross-finding-013 (mushaf as topological ring)**: Q 101's tight FR-distance to Q 108 al-Kawthar (`d = 0.296`, rank 1 of 113 nearest neighbours of Q 101) is part of the wrap-around closure architecture between front and back of the mushaf.

## 11. Source files

- `findings/phase-b-hypotheses/csv/h-new-111.json` (Fisher-Rao 114×114)
- `findings/phase-b-hypotheses/csv/h-new-720.json` (TSP-cost decomposition)
- `findings/phase-b-hypotheses/csv/h-new-750.json` (iʿjāz signatures)
- `findings/phase-b-hypotheses/csv/h-new-590.json` (outlier-strength spectrum)
- `findings/phase-b-hypotheses/csv/h-new-840.json` (UAS)
- `data/morphology/root-index.json` (root distribution)
- `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4 morphology)
- `quran-text/quran-no-tashkeel.json` (no-tashkeel canonical text)
- `data/revelation-order.csv` (Tanzil + Nöldeke)
- `data/literature/classical-tafsir/spa5k-tafsir-api/en-tafisr-ibn-kathir/101.json` (Ibn Kathīr)
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (al-Suyūṭī Itqān)
- `findings/phase-b-hypotheses/cross-finding-025-marker-thickness-vs-fr-cohesion-threshold.md` (FR-cohesion meta-rule)

Rules tuple: `(no-tashkeel, QAC-stem-roots K=500, Fisher-Rao angular distance, basmala-counted-only-in-Q1, mushaf order, Hafs-Kūfan, Mashriqī)`. All numerical values in this file are computed from disk and traceable to the cited paths.
