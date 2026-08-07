---
finding_id: H-NEW-2260
title: "Prophet-cycle pericope parallelism/cohesion — Nūḥ / Mūsā / Ibrāhīm"
phase: B+
status: 2/3 PASS-DIRECTED (Nūḥ, Mūsā) + 1/3 NULL (Ibrāhīm) — partial cross-finding-025 support
date: 2026-05-29
author: Waiel Al-Shujaa
extends: cross-finding-025-formal (scale-of-aggregation pericope-flip law)
prereg_sha256: 0845e412aa91ac3668c1ada6b9969de6341ee9fcd658fdbaad9e76eac435ec25
seed: 20260509
n_perm: 10000
bonferroni: "α = 0.05/3 = 0.016667"
rules_tuple: "(no-tashkeel, QAC v0.4 ROOT, verse-union pericope, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2260 — Prophet-cycle pericope parallelism/cohesion (Nūḥ / Mūsā / Ibrāhīm)


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


## Question

The same prophet-narrative recurs across many surahs (classical *takrār
al-qaṣaṣ*; al-Suyūṭī, *al-Itqān*, nawʿ 63 *fī qaṣaṣ al-Qurʾān*; al-Zarkashī,
*al-Burhān*, on *takrār al-qiṣaṣ*). Do same-prophet **pericopes** share
root-vocabulary above what equally-sized random pericopes drawn from the corpus
share? This is a direct pericope-scale test extending
`cross-finding-025-formal` (the scale-of-aggregation pericope-flip law) to the
recurring-prophet-narrative marker class.

## Pre-registration

- Pre-reg: `prereg-h-new-2260-prophet-cycle-pericope.md`, SHA-256
  `0845e412aa91ac3668c1ada6b9969de6341ee9fcd658fdbaad9e76eac435ec25` (embedded
  in the run script, verified at runtime — run passed).
- **Direction LOCKED (all 3 cycles): TIGHTER — J_mean(cycle) > null_mean (z > 0).**
- Instrument: mean pairwise root-Jaccard over QAC v0.4 ROOT-sets per pericope
  (extraction identical to H-NEW-1380 / H-NEW-1500 / H-NEW-1760).
- Null: 10000-perm length-matched random-pericope null, seed 20260509.
- Bonferroni across k=3 cycles: **α_corrected = 0.016667.**
- All pericope boundaries verified to exist and to narrate the named prophet in
  `quran-text/quran-no-tashkeel.json` (runtime `verify_boundaries()` passed).

## Results

| Cycle | Pericopes (pairs) | J_obs | null mean | null p95 | z | p_perm | Bonferroni (α=0.0167) | Verdict |
|:--|:-:|:-:|:-:|:-:|:-:|:-:|:--|:--|
| **Nūḥ**    | 6 (15) | 0.1805 | 0.1137 | 0.1596 | **+2.51** | **0.0087** | PASS | **PASS-DIRECTED** |
| **Mūsā**   | 4 (6)  | 0.2168 | 0.1056 | 0.1636 | **+3.34** | **0.0017** | PASS | **PASS-DIRECTED** |
| **Ibrāhīm**| 5 (10) | 0.1793 | 0.1371 | 0.1933 | +1.28 | 0.1073 | FAIL | **NULL-AT-PERICOPE-SCALE** |

Direction matched (z > 0) for all three cycles — no pre-commit violation.
**Synthesis: 2/3 cycles PASS-DIRECTED.**

### Locked pericope inventory (verified on disk)

- **Nūḥ**: Q 7:59-64 (L=6), Q 11:25-49 (25), Q 23:23-30 (8), Q 26:105-122 (18),
  Q 54:9-17 (9), Q 71:1-28 (28).
- **Mūsā** (burning-bush / Pharaoh-commissioning): Q 20:9-36 (28), Q 27:7-14 (8),
  Q 28:29-35 (7), Q 79:15-26 (12).
- **Ibrāhīm**: Q 6:74-83 (10), Q 19:41-50 (10), Q 21:51-70 (20), Q 26:69-104 (36),
  Q 37:83-113 (31).

## Interpretation — what drives each verdict

**Nūḥ PASSES** on concrete flood-narrative roots that recur across retellings:
`flk` (فلك, ark), `grq` (غرق, drowning), `njw` (نجو, deliverance),
`qwm` / `mlA` (the people / the chiefs who reject), `k*b` (denial). The
top pair is Q 7:59-64 × Q 26:105-122 (J=0.308). The ark-and-flood lexicon is a
stable narrative core re-used in nearly every retelling.

**Mūsā PASSES most strongly** (z=+3.34) and is driven by episode-specific
burning-bush roots: `byD` (بياض, the white hand), `ESw` (عصو, the staff),
`Twy` (طوى, the holy valley Ṭuwā), `Ans` (أنس, "I perceived a fire"),
`*hb` (ذهب, "go [to Pharaoh]"), `dbr` (دبر, turning away). The Q 27:7-14 ×
Q 28:29-35 pair reaches J=0.363 — the two retellings of the same fire-staff-hand
episode are almost word-for-word parallel at root level. This is the strongest
single-cycle result.

**Ibrāhīm NULLs at pericope scale** — an honest, substantive finding. Two
compounding reasons:

1. **Generic rather than episode-specific shared lexicon.** The recurring roots
   are monotheist-polemic generics — `Abw` (أب, father), `Alh` (إله, god),
   `Snm` (صنم, idol), `Ebd` (عبد, worship), `dwn` (دون, "besides [Allāh]") —
   not a narrative core unique to the Ibrāhīm story. These are the project's
   high-frequency creedal roots, so two pericopes can share them without sharing
   episode-content.

2. **Episode dispersion.** The Quran tells the Ibrāhīm story across genuinely
   *different episodes*: the star/moon/sun argument (Q 6), the plea to his
   father (Q 19), the idol-smashing + the cooled fire (Q 21), an eschatological
   extension (Q 26:88-104, the Day-of-Judgement scene that follows his duʿāʾ),
   and the near-sacrifice of the son (Q 37). These episodes do not share an
   ark-or-staff-like concrete vocabulary anchor.

3. The Ibrāhīm null-mean is itself elevated (0.137 vs ~0.11 for the other two)
   because the Ibrāhīm pericopes are the longest in the study (up to L=36), and
   longer windows have larger root-unions and higher baseline overlap. The
   length-matched null correctly absorbs this, and Ibrāhīm's J_obs (0.179) sits
   below the cycle's own 95th-percentile null (0.193).

This is exactly the kind of NULL cross-finding-025 §4 anticipates and treats as
a first-class result: **the Ibrāhīm cycle is told with substantially disjoint
episode-vocabulary across surahs**, in contrast to the lexically-conserved Nūḥ
and Mūsā cycles. Narrative variation is real and measurable here.

## Relation to cross-finding-025

H-NEW-1310 found the **Christ-narrative NULL at whole-surah scale**; H-NEW-1500
flipped it at pericope scale. H-NEW-2260 tests three further prophet cycles
**directly at pericope scale** with a length-matched random-pericope null.

- **Further cross-finding-025 evidence: YES (partial).** 2 of 3 recurring-prophet
  cycles (Nūḥ, Mūsā) cohere at pericope scale above the length-matched
  random-pericope baseline at Bonferroni-corrected significance. This extends
  the pericope-scale cohesion principle to a new marker class (recurring-prophet
  narrative), beyond the narrative / liturgical / discourse / opener classes
  already on the cross-finding-025 ledger.
- **Refinement to the law**: cohesion at pericope scale is **content-anchored,
  not automatic**. Cycles with a concrete shared narrative object (ark/flood for
  Nūḥ; fire/staff/white-hand for Mūsā) cohere; a cycle whose retellings span
  disjoint episodes with only generic creedal shared-lexicon (Ibrāhīm) does not.
  The pericope-flip law is necessary-conditioning (the marker is the content at
  pericope scale) but not sufficient — sufficiency requires a conserved
  episode-lexicon. This is a sharper statement than "thin markers flip."

## Honest limits

- **Pericope-boundary choice.** Boundaries are scholar-conventional verse blocks
  (e.g. Q 26 prophet-by-prophet segmentation). They were locked before
  computation and verified on disk, but a different defensible segmentation
  (e.g. including/excluding the closing refrain verses of the Q 26 series) could
  shift Ibrāhīm at the margin. The pre-reg locked one segmentation; alternatives
  would be MW-7-capped exploratory.
- **One instrument.** ROOT-Jaccard is the locked lens (for cross-finding-025
  comparability). A lemma-level or orthographic-token lens could rehabilitate or
  further demote a marginal cycle (rules-tuple sensitivity is bidirectional). Not
  run here; flagged as the natural follow-up.
- **Ibrāhīm is a NULL, not a falsification of cohesion in general** — z is still
  positive (+1.28); the cycle trends toward cohesion but does not clear the
  random-pericope baseline at corrected significance.
- **N is small per cycle** (4-6 pericopes). The permutation null is exact under
  the model, but cross-cycle generalization rests on 3 cycles; more cycles
  (Lūṭ, Ṣāliḥ/Thamūd, Hūd/ʿĀd, Yūsuf) would strengthen the marker-class claim.

## Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2260-prophet-cycle-pericope.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2260.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2260.json`
- This finding: `findings/phase-b-hypotheses/h-new-2260-prophet-cycle-pericope.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
