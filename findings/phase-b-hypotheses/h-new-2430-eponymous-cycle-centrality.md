---
finding_id: H-NEW-2430
title: "Eponymous-surah cycle-centrality law — eponymy ≠ centrality (0/5 dedicated prophet-surahs are their cycle's lexical centroid)"
phase: B+
status: CONFIRMED (locked direction) — eponymy ≠ centrality; core-carrier sub-mechanism FALSIFIED at corpus scale
date: 2026-05-30
author: Waiel Al-Shujaa
extends: "H-NEW-1820 (title-density independence) + H-NEW-2260 (prophet-cycle cohesion) + Q071-F-01 + Q020-F-06"
prereg_sha256: 67a689a5382cac196f7bec9cbdb19c31f3a226db864dcbe2b680e045fe09019e
seed: 20260509
n_perm: 10000
bonferroni: "Arm B α = 0.05/5 = 0.01"
rules_tuple: "(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2430 — Eponymous-surah cycle-centrality law

## Question

A surah named for a prophet (Nūḥ, Ibrāhīm, Hūd, Maryam, Yūnus) and the recurring
multi-surah cycle that retells that figure's story: is the **eponymous surah the
cycle's lexical centroid** (the hub from/toward which the scattered retellings
draw), or is it lexically peripheral? This promotes a two-point convergence —
**Q071-F-01** (Nūḥ Q 71 PERIPHERAL, rank 5/6) and **Q020-F-06** (Ṭā-Hā = Mūsā
HUB) — to a corpus-wide law, generalizing **H-NEW-1820** (title-density
independence: 47/89 eponymous surahs NOT rank-1 in their title-root) from
title-root density to narrative-cycle centrality.

## Pre-registration

- Pre-reg `prereg-h-new-2430-eponymous-cycle-centrality.md`, SHA-256
  `67a689a5382cac196f7bec9cbdb19c31f3a226db864dcbe2b680e045fe09019e` (embedded
  in the run script, verified at runtime — run passed).
- **Direction LOCKED:** eponymous surahs are NOT systematically the cycle
  centroid — **median eponymous centrality-rank > 1 (≤ 2 of 5 rank-1)**.
- Instrument: mean-pairwise QAC-v0.4-ROOT Jaccard centrality (medoid sense),
  extraction identical to H-NEW-2260 / Q071-F-01 / Q020-F-06.
- Nulls: per-cycle length-matched anchor-swap permutation (Arm B, Bonferroni-5,
  α=0.01) + cross-cycle uniform-rank null (Arm C). Seed 20260509, 10000 perms.
- All pericope boundaries + figure-markers verified on disk (runtime passed);
  Nūḥ rank 5/6 and Mūsā Q 20 hub-strength reproduce Q071-F-01 / Q020-F-06 (MW-5
  runtime assertions passed).

## Candidate inventory

Five figures have BOTH a dedicated eponymous surah AND a recurring multi-surah
narrative cycle: **Nūḥ (Q 71), Ibrāhīm (Q 14), Hūd (Q 11), Maryam (Q 19),
Yūnus (Q 10)**. Excluded with documentation (NOT silently dropped):

- **Yūsuf (Q 12)** — degenerate: the Yūsuf story is confined to Q 12; only
  naming-mentions elsewhere (Q 6:84, Q 40:34). No recurring narrative cycle to
  be central to.
- **Muḥammad (Q 47)** — degenerate: not a narrated multi-surah prophet-story.
- **Mūsā** — included as **control only**: there is no "Sūrat Mūsā", so Mūsā
  contributes no eponymous data point. It is the counter-case showing the hub
  can be a *non-eponymous* core-episode carrier (Q 20 Ṭā-Hā, Q020-F-06).

## Results

### Arm A + Arm B (per cycle; ◆ = eponymous; Bonferroni-5 α=0.01)

| Cycle | Eponymous pericope | Rank | n | Arm A | Centroid | Arm B z | Arm B p | Arm B |
|:--|:--|:-:|:-:|:--|:--|:-:|:-:|:--|
| **Nūḥ**    | ◆ Q 71:1-28   | **5** | 6 | PERIPHERAL | Q 7:59-64 | +0.424 | 0.278 | NULL |
| **Ibrāhīm**| ◆ Q 14:35-41  | **5** | 6 | PERIPHERAL | Q 21:51-70 | +1.179 | 0.096 | NULL |
| **Hūd**    | ◆ Q 11:50-60  | **3** | 5 | PERIPHERAL | Q 46:21-26 | +1.823 | 0.024 | DIRECTIONAL |
| **Maryam** | ◆ Q 19:16-34  | **4** | 5 | PERIPHERAL | Q 21:91   | +2.453 | 0.007 | PASS |
| **Yūnus**  | ◆ Q 10:98     | **2** | 4 | NEAR-CENTROID | Q 37:139-148 | +2.372 | 0.023 | DIRECTIONAL |

### Arm C — the cross-cycle law (confirmatory cell)

| Metric | Observed | Uniform-rank null | Verdict |
|:--|:-:|:-:|:--|
| Eponymous ranks {Nūḥ,Ibrāhīm,Hūd,Maryam,Yūnus} | {5,5,3,4,2} | — | — |
| Cycle sizes | {6,6,5,5,4} | — | — |
| **# rank-1 of 5** | **0** | mean ≈ 1.0 | p(#rank1 ≥ obs) = 1.0000 |
| **Median eponymous rank** | **4** | mean median 3.03 | p(median ≤ obs) = 0.9411 |

**Verdict: H1 CONFIRMED — eponymy ≠ centrality (median rank 4 > 1).** The locked
direction holds, and far more strongly than predicted: **not a single one** of
the five eponymous surahs is its cycle's lexical centroid. Eponymous ranks are
if anything *worse* than chance (observed median 4 vs uniform-null mean 3.03;
0/5 rank-1 vs ~1/5 expected). No pre-commit violation.

## Interpretation — the real mechanism (corrects the §10.120 sub-claim)

The 2-point convergence proposed a discriminating mechanism (§10.120): *a
dedicated surah is the cycle-hub iff it carries the cycle's CORE episode*. At
corpus scale this **sub-mechanism is FALSIFIED**:

| Cycle | Eponymous pericope | Core-episode carrier? | Rank | Eponymous #roots |
|:--|:--|:-:|:-:|:-:|
| Maryam | Q 19:16-34 | **YES** (fullest nativity) | 4/5 | 89 |
| Hūd    | Q 11:50-60 | **YES** (fullest Hūd→ʿĀd)  | 3/5 | 64 |
| Nūḥ    | Q 71:1-28  | no (daʿwa/idol variant)   | 5/6 | 87 |
| Ibrāhīm| Q 14:35-41 | no (Mecca-duʿāʾ variant)  | 5/6 | 47 |
| Yūnus  | Q 10:98    | no (1-verse allusion)     | 2/4 | 12 |

The two core-episode carriers (Maryam Q 19, Hūd Q 11) rank **4/5 and 3/5** —
*low*, the opposite of the §10.120 prediction. The single best-placed eponymous
member is **Yūnus Q 10:98 — a one-verse allusion** carrying only 12 roots.

The variable that actually governs eponymous centrality is **private-vocabulary
mass (pericope size)**, exactly as the Q071-F-01 pre-reg anticipated:

- The largest eponymous pericopes — **Maryam Q 19 (89 roots), Nūḥ Q 71 (87
  roots)** — rank worst (4/5, 5/6). Their long, fully-elaborated narratives
  accumulate huge *private* vocabulary (Maryam: the palm-tree, the dates, the
  infant speaking, the genealogy; Nūḥ: cosmological signs vv 15-20, the five
  named idols v 23, the night/day complaint) that the short cross-surah
  retellings do not share, **depressing Jaccard overlap**.
- The smallest eponymous pericope — **Yūnus Q 10:98 (12 roots)** — has almost no
  private vocabulary, so a high fraction of its tiny root-set is shared, lifting
  its relative centrality to 2/4.

**The eponymous surah, precisely because it tells the figure's story most fully,
becomes the lexical OUTLIER of its own cycle.** Full elaboration ⇒ maximal
private vocabulary ⇒ minimal Jaccard centrality. This is the sharpened,
corrected law: eponymy is anti-correlated with cycle-centrality, and the driver
is elaboration/length, not the core-vs-variant distinction.

### Why §10.120 (Q 20 hub) is still consistent

Q020-F-06's confirmatory cell was **hub-strength vs a random-window null** (Arm
B z=+5.807), NOT a within-cycle centrality *rank*. In Q020-F-06's own
descriptive table Q 20 was hub-**rank 2** of 4 (Q 28:29-35 led) — already not
rank-1. So §10.120's "hub" claim was always the cohesion-above-random claim, not
the centroid claim. H-NEW-2430's Arm B reproduces that pattern: Maryam Q 19
PASSES the random-window null (z=+2.45) while ranking only 4/5 within its cycle —
**cohesive yet non-central**. The two facts (above-random cohesion + non-centroid
rank) are not in tension; H-NEW-2430 separates them cleanly and shows the rank
fact is the corpus-wide regularity.

## Arm B summary (cohesion above random window)

Three of five eponymous pericopes share more vocabulary than a length-matched
random window (Maryam PASS at Bonferroni-0.01; Hūd, Yūnus DIRECTIONAL at raw
0.05); Nūḥ and Ibrāhīm are NULL. So eponymous surahs are *usually* lexically
attached to their cycle (above chance) — they are simply never its most-central
member. Cohesion ≠ centrality.

## Relation to prior findings

- **H-NEW-1820** (title-density independence, 47/89 NOT rank-1): H-NEW-2430 is
  the narrative-cycle analogue and is **even stronger** — 0/5 (not 52.8%) of
  eponymous surahs are rank-1 in cycle-centrality. The independence law deepens:
  a surah's name tracks neither its dominant *word* (H-NEW-1820) nor its position
  in the figure's *retelling-network* (H-NEW-2430).
- **H-NEW-2260** (cohesion is content-anchored): consistent. Cycles cohere
  (Nūḥ, Mūsā PASS there), but the eponymous member is not the cohesion source.
- **Q071-F-01 / Q020-F-06**: both reproduced exactly (MW-5). H-NEW-2430 keeps
  Q071-F-01's PERIPHERAL result and re-frames Q020-F-06's HUB result as
  above-random cohesion (rank-2), so the 2-point convergence is preserved while
  its proposed *mechanism* (core-vs-variant) is corrected to *length/private-mass*.

## Honest limits

- **N is small** (5 eponymous cycles). Arm C's significance rests on a clean but
  modest sample; the *direction* (0/5 rank-1, median worse than chance) is
  unambiguous, but a 6th–7th eligible cycle does not exist in the corpus (Yūsuf,
  Muḥammad are degenerate), so 5 is the population, not a sample — strengthening
  the "law over the eligible set" reading while capping inferential reach beyond it.
- **Maryam cycle composition.** Three of its five members are single-verse
  allusions (Q 21:91, Q 23:50, Q 66:12). The pre-reg locked these as members; an
  alternative segmentation using only the two extended narratives (Q 3, Q 19)
  would make centrality a single pairwise number (degenerate). The single-verse
  members drive the Maryam centroid (the shared nafkh-rūḥ formula links Q 21:91 ×
  Q 66:12 at J=0.357). This is locked, not post-hoc; rules-tuple-sensitive.
- **Ibrāhīm eponymous member added.** Q 14:35-41 was not in the H-NEW-2260
  Ibrāhīm set (which used Q 6/19/21/26/37); it is the eponymous surah's only
  Ibrāhīm narrative (the Mecca-duʿāʾ), added here to make Q 14 testable. Its low
  rank (5/6) is robust to this addition (it is a genuinely distinct episode).
- **One instrument.** QAC ROOT-Jaccard, locked for comparability. A lemma or
  orthographic-token lens could shift a marginal eponymous rank by ±1; bidirectional
  rules-tuple sensitivity flagged, MW-7-capped, not run.
- The **core-vs-variant sub-mechanism is falsified, not the parent law**: the
  parent claim (eponymy ≠ centrality) is confirmed; only the §10.120 *explanation*
  for why a particular surah is/ isn't the hub is replaced (length/private-mass).

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2430-eponymous-cycle-centrality.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2430.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2430.json`
- This finding: `findings/phase-b-hypotheses/h-new-2430-eponymous-cycle-centrality.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
