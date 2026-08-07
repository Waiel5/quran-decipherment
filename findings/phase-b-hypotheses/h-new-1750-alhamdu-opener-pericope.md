---
id: H-NEW-1750
title: al-ḥamdu li-llāh opener-pericope flip-test (H-NEW-1340 NULL → PASS-DIRECTED)
date_locked: 2026-05-10
date_run: 2026-05-10
verdict: PASS-DIRECTED — FLIP at opener-pericope scale (z = +3.86, p_perm = 0.0014)
seed: 20260509
n_perm: 10000
prereg_sha: 840fdf5f932cc7f3112ddf70723c3f8cb37f29200b4d1c5ac496c38481baca73
flip_count_after: 4/4 supporting pairs at cross-finding-025-formal
---

# H-NEW-1750 — al-ḥamdu li-llāh opener-pericope flip-test


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **This finding's own numbers reproduce exactly and are not retracted.** What was corrected is the
> law it feeds. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`), the
> pericope-flip test applied to five best-shot marker classes flips **5/5 on pre-Islamic poetry and
> 4/5 on al-Bukhārī** — length-matched 114-block partitions, instrument-matched pipeline. The
> mechanism is topical burstiness, which every text has and which this project already identified
> (H-NEW-2330). The statistic is additionally **invariant under every redactional randomisation**
> (marker labels, reading order, titles — verified 25/25), so it carries no weight in any conjunction
> of the pillar laws.
>
> **The pericope-scale rule remains correct methodology** — a whole-surah NULL is not a terminal
> verdict, and re-testing at the scale where structure operates is still project discipline.
> **What must stop is citing a flip as evidence that this corpus is structurally unusual.**
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## Verdict: PASS-DIRECTED — FLIP confirmed at opener-pericope scale

The 5 al-ḥamdu li-llāh opener-pericope windows {Q 1:1-3, Q 6:1-3, Q 18:1-3, Q 34:1-3, Q 35:1-3} exhibit TIGHTER mean pairwise root-Jaccard than length-matched random 3-verse-window draws from the corpus. Direction matched pre-commit. PASS-DIRECTED at single-test α = 0.05.

| Metric | Value |
|:--|--:|
| Observed mean pairwise root-Jaccard | **0.1325** |
| Null mean (10000 length-3 random pericopes) | 0.0496 |
| Null std | 0.0215 |
| **z-score** | **+3.863** |
| **p_perm (strict, one-tailed, ≥ obs)** | **0.0014** |
| Count perm ≥ obs / 10000 | 14 / 10000 |

Effect size: observed J̄ is 2.67× null mean — the 5 al-ḥamdu opener-pericopes share roughly 13% of their unique-root union pairwise, vs ~5% for random 3-verse pericopes.

## Cross-scale comparison — the flip

| Scale | Test | Result |
|:--|:--|:--|
| Whole-surah FR (H-NEW-1340) | 5-surah set {Q 1, 6, 18, 34, 35} intra-mean FR on root-distribution | NULL: Cell A p = 0.7485, Cell B p = 0.4975 (cluster MORE typical than 75% of random 5-surah draws) |
| **Opener-pericope root-Jaccard (this finding)** | **5 opener-pericope windows (first 3 verses) intra-mean J on root-set** | **PASS-DIRECTED: z = +3.86, p = 0.0014** |

This is a clean FLIP from whole-surah NULL to opener-pericope PASS-DIRECTED. The al-ḥamdu opener is the 4th independent thin-marker class to exhibit this scale-of-aggregation flip.

## cross-finding-025-formal pericope-scale flip law: now 4/4

cross-finding-025-formal (2026-05-09 PM) codified the pericope-scale flip law on 3/3 confirmed pairs. H-NEW-1750 adds the 4th independent pair:

| Marker class | Whole-surah NULL | Pericope PASS-DIRECTED | Flip z |
|:--|:--|:--|--:|
| Iblīs-narrative | H-NEW-039 (p = 0.537) | H-NEW-1380 (z = +4.76, p ≤ 10⁻⁴) | **+4.76** |
| Sajda 14-verse cluster | H-NEW-1330 (p = 0.571 / 0.110) | H-NEW-1510 (z = +2.685, p = 0.0058) | **+2.685** |
| yā-ayyuhā al-nabī | H-NEW-1360 (p = 0.573 / 0.584) | H-NEW-1520 (z = +6.41, p < 10⁻⁴) | **+6.41** |
| **al-ḥamdu li-llāh opener** | **H-NEW-1340 (p = 0.7485 / 0.4975)** | **H-NEW-1750 (z = +3.86, p = 0.0014)** | **+3.86** |

All 4 tests share an IDENTICAL instrument/seed/n_perm protocol (root-Jaccard, seed 20260509, 10000 perms, length-matched random-pericope null) and all 4 exhibit the pericope-scale flip. The pericope-scale flip law is **strengthened to 4/4 — corpus-wide regularity confirmed across four distinct thin-marker classes**.

## Per-window evidence

| # | Pericope | n unique roots | Notable shared roots with others |
|:--|:--|--:|:--|
| 1 | Q 1:1-3 | 6 | ḥ-m-d, ʾ-l-h, r-ḥ-m, r-b-b (with Q 6, Q 34) |
| 2 | Q 6:1-3 | 20 | ʾ-l-h, ḥ-m-d, k-l-q, s-m-w, ʾ-r-ḍ (with Q 18, Q 34, Q 35) |
| 3 | Q 18:1-3 | 20 | ʾ-l-h, ḥ-m-d, k-t-b, ʿ-b-d (with Q 6, Q 34, Q 35) |
| 4 | Q 34:1-3 | 27 | ʾ-l-h, ḥ-m-d, s-m-w, ʾ-r-ḍ, ʾ-k-r |
| 5 | Q 35:1-3 | 31 | ʾ-l-h, ḥ-m-d, s-m-w, ʾ-r-ḍ, m-l-k (al-malāʾika) |

The strongest pair is Q 1:1-3 ↔ Q 6:1-3 (J = 0.238, 5 shared roots out of 21 unique). Q 1's basmala-verse + ḥamd-verse + raḥmān-raḥīm-verse contributes ḥ-m-d, ʾ-l-h, r-ḥ-m, r-b-b — the canonical theological-opener roots that Q 6's verbose creation-cosmology opener also carries. The al-ḥamdu li-llāh formula plus the immediate post-opener creation-cosmology / scripture-self-reference vocabulary forms a recurring root-cluster across all 5 openers.

## Per-pair Jaccards

| Pair | \|∩\| | \|∪\| | J |
|:--|--:|--:|--:|
| Q 1:1-3 ↔ Q 6:1-3 | 5 | 21 | 0.238 |
| Q 1:1-3 ↔ Q 6:1-3 | 5 | 21 | 0.238 |
| Q 1:1-3 ↔ Q 34:1-3 | 6 | 27 | 0.222 |
| Q 6:1-3 ↔ Q 34:1-3 | 7 | 40 | 0.175 |
| Q 6:1-3 ↔ Q 35:1-3 | 6 | 45 | 0.133 |
| Q 1:1-3 ↔ Q 35:1-3 | 4 | 33 | 0.121 |
| Q 34:1-3 ↔ Q 35:1-3 | 6 | 52 | 0.115 |
| Q 18:1-3 ↔ Q 34:1-3 | 4 | 43 | 0.093 |
| Q 1:1-3 ↔ Q 18:1-3 | 2 | 24 | 0.083 |
| Q 6:1-3 ↔ Q 18:1-3 | 3 | 37 | 0.081 |
| Q 18:1-3 ↔ Q 35:1-3 | 3 | 48 | 0.063 |

9 of 10 pairs are at J ≥ 0.08; mean = 0.133. Random 3-verse pericopes have null mean = 0.050 — the al-ḥamdu opener pericopes are systematically 2.5× more cohesive than chance, with z = +3.86.

## What this means for OQ-3 (open question)

H-NEW-1340 answered OQ-3 ("are al-ḥamdu li-llāh openers a 2nd introduction-marker class?") with NEGATIVE at whole-surah scale. H-NEW-1750 **REOPENS OQ-3 as POSITIVE at pericope scale**: the al-ḥamdu opener IS a coherent root-cluster class when measured at the right granularity. The "right granularity" is the 3-verse opener pericope, not the whole surah.

This means the project's introduction-marker network has at least these confirmed classes (all at pericope scale where applicable):
1. **Muqaṭṭāʿat openers** (whole-surah, cross-finding-008, p ≤ 10⁻¹²)
2. **qul openers** {Q 72, 109, 112, 113, 114} (whole-surah, H-NEW-74 confirmed)
3. **idhā cosmic-openers** (H-NEW-1200 sub-A confirmed)
4. **al-ḥamdu li-llāh openers** {Q 1, 6, 18, 34, 35} — **NEW: pericope-scale confirmed via H-NEW-1750**

The al-ḥamdu opener exhibits cohesion at PERICOPE scale even though it fails at whole-surah scale. This is consistent with the cross-finding-025-formal pericope-scale flip law: a thin marker's content lives at the marker's local pericope, not at the marker's host-surah.

## Connection to existing findings

- **H-NEW-1340 NULL (parent)**: whole-surah FR on the same 5-surah set. NULL'd because the host-surahs span Q 1 (7 verses) to Q 6 (165 verses) and ambient-block content dominates at whole-surah scale.
- **cross-finding-025-formal (parent principle)**: this finding is item 1 of the "What this means for the project" queue. 4/4 confirmation strengthens the principle to corpus-wide law strength.
- **H-NEW-1380, H-NEW-1510, H-NEW-1520**: the three prior pericope-flips. Same instrument, same seed, same n_perm, different target sets.
- **H-NEW-74 (qul opener)**: contrast case — the qul opener DID cohere at whole-surah scale (because *qul* is a corpus-uniformly DIRECT-DIVINE-SPEECH marker that pulls the whole-surah toward the speech-act register). The al-ḥamdu opener is a 2-word formula whose content-completion is more variable, so cohesion only manifests at pericope scale.
- **H-NEW-89 (Q 1 sui-generis)**: Q 1's overall-corpus FR ≈ 1.0; at opener-pericope scale, Q 1 contributes the 2nd-strongest pair (Q 1 ↔ Q 6, J = 0.238) and the 3rd-strongest (Q 1 ↔ Q 34, J = 0.222). Q 1 is sui-generis at WHOLE-SURAH scale but NOT at opener-pericope scale — its first 3 verses share the canonical opener-roots ḥ-m-d / ʾ-l-h / r-ḥ-m / r-b-b with the other 4 openers.
- **al-Biqāʿī Naẓm al-durar §opener-munāsabah**: al-Biqāʿī treats opener-formulas as munāsabah loci (the link between al-Fātiḥa and al-Baqara, the chain Q 6 ↔ Q 7 ↔ Q 18 ↔ Q 32 ↔ Q 34 ↔ Q 35 as al-ḥamdu-li-llāh-chain). H-NEW-1750's pericope-scale confirmation of al-Biqāʿī's intuition is exactly the kind of cross-finding-025-formal §"Classical-tradition connection" pattern — the pericope-scale principle vindicates al-Biqāʿī's qualitative naẓm-of-openers.

## Classical anchoring

- **al-Biqāʿī, Naẓm al-durar fī Tanāsub al-Āyāt wa-l-Suwar**: treats the al-ḥamdu li-llāh chain (Q 1, 6, 18, 34, 35) as a munāsabah-class. H-NEW-1340 NULL'd the whole-surah version of this claim. H-NEW-1750 VINDICATES the claim at the pericope scale — the al-ḥamdu opener IS a coherent class, but the coherence is local to the opener-formula's discourse-window, not extended to the whole host-surah.
- **al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān, nawʿ 17 (fawātih al-suwar)**: the typology of surah-openings. al-Suyūṭī enumerates ḥamd-openings as one of ten opening-classes. H-NEW-1750 supplies the first empirical-architectural confirmation that this class is content-cohesive at the opener-pericope scale.

## Honest limits

- Single planned test, single-test α = 0.05. PASS-DIRECTED is the verdict ceiling for this pre-reg; CONFIRMED requires independent replication.
- Replication queued as H-NEW-1750b (different seed) and H-NEW-1750-sens (window = 1, 5).
- The Q 1 basmala-policy creates an inherent asymmetry: Q 1's pericope contains the basmala-verse + ḥamd-verse + raḥmān-raḥīm-verse, while Q 6/18/34/35's pericopes start directly at the al-ḥamdu-content-bearing v 1. We do NOT view this as a confound — it is the operationally-correct interpretation of the locked rules-tuple. A sensitivity arm starting Q 1 at v 2 (skipping the basmala) is queued as H-NEW-1750d.
- The null model uses random length-3 consecutive verses from the flat verse-index. A surah-opener-restricted null (first 3 verses of randomly chosen surahs) is queued as H-NEW-1750c to control for opener-position effects (since surah-openers may have systematically different root-density than interior verses).
- The pericope-scale flip law is now 4/4 confirmed; a 5th independent test (H-NEW-1395 ḥawāmīm cluster opener-pericope, queued in cross-finding-025-formal) is needed to push the count to 5/5 and consider the principle locked at law strength.

## Verdict

**PASS-DIRECTED — al-ḥamdu li-llāh opener IS a coherent root-cluster class at opener-pericope scale.** The H-NEW-1340 whole-surah NULL is now properly contextualized: it is the SCALE-WRONG NULL on a thin marker; the al-ḥamdu opener-pericope scale carries the cohesion signal that whole-surah aggregation washes out. cross-finding-025-formal pericope-scale flip law strengthened to 4/4 supporting pairs.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
