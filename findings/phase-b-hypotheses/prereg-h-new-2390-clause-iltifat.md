---
id: H-NEW-2390
title: Clause-scale / within-verse iltifāt detector — PRE-REGISTRATION
date: 2026-05-29
phase: B
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
---

# PRE-REGISTRATION — H-NEW-2390 — Clause-scale (within-verse) iltifāt detector

**This file is locked BEFORE any computation. Its SHA-256 is embedded in
`scripts/h-new-2390.py` and verified at runtime (fail-fast on mismatch), per
Protocol §1.2.**

---

## 0. Motivation and relation to the coarse detector (H-NEW-2200)

H-NEW-2200 built the first corpus-wide iltifāt census, but at the **verse-boundary**
scale: it collapsed each verse to a single *dominant* (modal) grammatical person and
number, then flagged changes ACROSS verse boundaries (v, v+1). That detector found:

- pre-registered direction Meccan > Medinan density **REVERSED** (Medinan 0.546 vs
  Meccan 0.532, Δ=−0.014, p=0.66) → published NULL;
- the only real signal was **surah-length** (r≈+0.30), a length confound, region-NULL.

H-NEW-2200 explicitly flagged its own resolution ceiling (§7, §8, cross-finding-025):
> "classically-foregrounded iltifāt lives at the WITHIN-VERSE / CLAUSE scale, finer
> than that detector."

The flagship balāgha examples are themselves **within-verse**:
- **Q 1:5** *iyyāka naʿbudu wa-iyyāka nastaʿīnu* — 2nd-person address (`iyyāka` 2MS)
  → 1st-person verb (`naʿbudu` 1P) → 2nd (`iyyāka`) → 1st (`nastaʿīnu`): a 2↔1
  alternation **inside one verse** (verified in QAC at `(1:5:*)`).
- **Q 10:22** the ship-storm — within ONE verse: 3MS (*huwa*) → 2MP (*kuntum*)
  → 3FP (the ships *jarayna*) → 3MP (*bihim*/*fariḥū*) → 3FS (*jāʾathā*) → 3MP
  (*ẓannū*) → 2MS/1P (*anjaytanā*… *la-nakūnanna*): a storm of mid-verse shifts
  (verified in QAC at `(10:22:*)`). The boundary detector sees only ONE dominant
  value per verse and misses every one of these.

**H-NEW-2390 builds the finer detector H-NEW-2200 called for.** It scans the ordered
sequence of finite-verb / pronoun person-number STATES inside each verse and flags
every **within-verse** shift. The pre-registered question: *does the clause scale
recover the genre/region signal the coarse boundary scale missed?*

---

## 1. Detector definition (MW-1, instrument-prior — LOCKED)

### 1.1 Token → state extraction (identical feature basis to H-NEW-2200)

For every QAC v0.4 segment, emit a **person-number state** `(person ∈ {1,2,3},
number ∈ {S,D,P})` iff the segment is:

- a finite verb token `POS:V` (this INCLUDES imperatives `IMPV`, which carry an
  explicit 2nd-person feature in QAC, e.g. `2MS`/`2MP`), taking the verb's own
  subject person-number (the FIRST person-number-gender field on the V segment); OR
- a pronoun: independent `POS:PRON`, or any suffix/object clitic carrying a
  `PRON:<png>` field.

Person-number-gender codes map to bare number via: `MS,FS,S→S`; `MD,FD,D→D`;
`MP,FP,P→P`. Regex (locked, copied verbatim from H-NEW-2200 for instrument
continuity): `^(?:PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$`.

Segments with no person feature (nouns, particles, prepositions, the divine name
as `PN`, relatives, demonstratives without a png token, etc.) emit NO state and are
simply skipped — they do not break a run and do not count as a shift.

### 1.2 The within-verse state SEQUENCE

For each verse (s,v), order all emitted states by (word_index, segment_index)
ascending → an ordered list `seq = [state_1, state_2, …, state_m]`. This is the
clause-scale grammatical-person trajectory of the verse. (A verse with m<2 states
cannot contain a within-verse shift and contributes 0.)

### 1.3 A within-verse iltifāt SHIFT (the locus — LOCKED)

A **within-verse shift** occurs at position i (1≤i<m) iff `state_i` and `state_{i+1}`
differ in PERSON or in NUMBER. We record, per shift:
- `kind ∈ {person, number, both}`;
- the directed person category (e.g. `2nd->1st`) and/or number category (e.g.
  `S->P`), using the SAME taxonomy as H-NEW-2200 so the two censuses are directly
  comparable;
- coordinates (surah, verse, position i, word indices).

Per-verse shift count = number of adjacent differing-state pairs. This is the
clause-scale analogue of the H-NEW-2200 boundary locus, but measured at every
adjacency INSIDE the verse rather than at the single (v,v+1) seam.

### 1.4 Two density normalisations (both LOCKED, reported)

- **Per-verse density** `D_verse = (# verses with ≥1 within-verse shift) / (# verses
  with ≥2 states)` — the fraction of *eligible* verses that carry at least one
  within-verse iltifāt. (Verses with <2 states are excluded from the denominator
  because they are structurally incapable of a within-verse shift — this is the
  honest eligible-denominator, locked here to forestall garden-of-forking-paths.)
- **Per-adjacency density** `D_adj = (# within-verse shifts) / (# within-verse
  adjacencies)`, where adjacencies = Σ over eligible verses of (m−1). This is the
  clause-scale twin of H-NEW-2200's per-boundary density and is the **primary**
  statistic for the region test (so the comparison to 2200 is apples-to-apples:
  shifts per adjacency, just intra- vs inter-verse).

Rules-tuple: `(no-tashkeel, QAC-v0.4-segment, finite-V[incl IMPV] + PRON
person-number, ordered within-verse sequence, adjacent-pair shift, Hafs-Kūfan,
Mashriqī)`.

---

## 2. Pre-registered hypotheses and LOCKED directions

The pre-flight thesis (locked): **at the clause scale, iltifāt density DOES
distinguish genre** — the signal the verse-boundary scale could not see. Two
direction-locked cells, Bonferroni k=2, α_bon = 0.025. Permutation null = surah-label
shuffle (the surah is the exchangeable unit; shifts and adjacencies move together with
their surah), seed 20260509, 10000 perms. p = (#perm Δ_perm ≥ Δ_obs + 1)/(n_perm+1),
one-sided in the locked direction.

### H1 (PRIMARY, region) — LOCKED DIRECTION: Meccan > Medinan
`D_adj(Meccan) > D_adj(Medinan)`, and Δ > 95th-pct of the surah-label-shuffle null.
- **Rationale (classical prior):** al-Zarkashī (*al-Burhān*, iltifāt nawʿ) and Abdel
  Haleem (1992 BSOAS) describe iltifāt as the dynamic "daring of Arabic" of the
  vivid, dramatic, oath/eschatological Meccan style. H-NEW-2200 REVERSED this at the
  boundary scale; the locked claim is that the **clause** scale recovers it.
- This is the DIRECT re-test of the exact direction 2200 reversed. A reversal here
  too ⇒ published NULL with pre-commit-violation flag (Protocol §1.8), and the
  conclusion "iltifāt density is region-independent at BOTH scales" gains prominence.

### H2 (SECONDARY, register) — LOCKED DIRECTION: short-mufaṣṣal-enriched
`D_adj(short-mufaṣṣal, s≥78) > D_adj(rest, s<78)`, Δ > 95th-pct of the
surah-label-shuffle null over the same partition.
- **Rationale:** the oath/eschatological register (qasam + *idhā* eschatology +
  rapid narrative tableaux) classically carries the densest rhetorical turns and
  was independently shown enriched in the short mufaṣṣal by H-NEW-2210 (qasam 3.44×)
  and H-NEW-2250 (*idhā* head 2.6×). The s≥78 boundary matches those findings for
  cross-comparability. Locked direction: short-mufaṣṣal DENSER.
- This is the register-register framing the pre-flight offered as the alternative
  lock. We commit to BOTH (region AND register) under Bonferroni-2.

### Comparison to H-NEW-2200 (DESCRIPTIVE, no new p-value)
Report side-by-side: clause-scale per-adjacency density vs 2200 boundary per-boundary
density, for Meccan/Medinan and for the length bands. Pre-registered descriptive
question: does the clause scale show a region effect (either direction, significant)
that the boundary scale did not? This is the headline interpretive comparison; it
makes no claim beyond the two locked p-values above (MW-7 discipline on anything
post-hoc).

---

## 3. Success / failure criteria (LOCKED)

- **CONFIRMED (clause scale recovers the signal):** H1 passes in the locked direction
  (Meccan > Medinan) at p < 0.025 (Bonferroni-2). The finer detector recovers a
  region signal the coarse detector missed → prominence to the scale-of-aggregation
  result.
- **PARTIAL:** H2 passes (register enrichment) but H1 does not, OR H1 passes but H2
  does not. Report both honestly.
- **NULL (pre-commit honored):** neither locked cell passes in its locked direction.
  If a cell's Δ comes out with the WRONG sign, it is flagged a pre-commit violation
  and published as NULL with full prominence — and the project conclusion strengthens
  to "iltifāt density is region/register-independent at BOTH the boundary AND the
  clause scale; the device is real but its DENSITY does not track genre."

Either outcome is a first-class finding. Equal NULL prominence (Protocol §1.3).

---

## 4. Validation (MW-6) and replication (MW-5)

- **MW-6 ground-truth recall** vs Abdel Haleem (1992) catalog
  (`data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`): the detector
  MUST fire within the verse on the flagship loci **Q 1:5, Q 10:22, Q 27:60, Q 36:22,
  Q 108:2** (verified individually). Report per-category recall (a verse counts as a
  hit if it carries ≥1 within-verse shift of the matching kind). Expectation: the
  clause detector should recover MORE of Abdel Haleem's within-verse references than
  the boundary detector's 56.7%/61.3%, because it now sees inside the verse — but the
  recall figure is descriptive, not a locked test.
- **MW-5 replication:** re-run H1 with a second seed (20260510) and with a
  **verb-only** state stream (drop pronoun-only states) — direction must hold for the
  finding to be called CONFIRMED rather than DIRECTIONAL.
- **MW-3 alternative model:** also report the per-VERSE density normalisation
  (D_verse) alongside D_adj for H1; the region direction should agree across both
  normalisations.

---

## 5. Classical anchoring (cited, not vague)

- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, the *nawʿ* on al-iltifāt (definition
  "change of speech from one mode to another… freshness and variety").
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, parallel iltifāt chapter (the disputed
  1st→2nd at Q 36:22).
- M. Abdel Haleem, "Grammatical Shift for Rhetorical Purposes: Iltifāt and Related
  Features in the Qurʾān", *BSOAS* 55(3):407–432 (1992) — ground-truth catalog at
  `data/literature/balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md` and
  `data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`.
- Ibn al-Athīr, *al-Mathal al-Sāʾir* — *shajāʿat al-ʿarabiyya*.

---

## 6. Output files

- pre-reg (this file): `findings/phase-b-hypotheses/prereg-h-new-2390-clause-iltifat.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2390.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2390.json`
- finding: `findings/phase-b-hypotheses/h-new-2390-clause-iltifat.md`

*Pre-registration locked 2026-05-29 by Waiel Al-Shujaa, before any computation.
Bismillāhi al-Raḥmāni al-Raḥīm.*
