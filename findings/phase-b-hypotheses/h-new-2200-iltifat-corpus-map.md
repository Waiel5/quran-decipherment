---
id: H-NEW-2200
title: Iltifāt (grammatical-person shift) corpus map — exhaustive generator + Meccan/Medinan density direction-lock
date: 2026-05-29
phase: B
verdict: NULL (pre-commit direction reversed) + length-confounded position effect + descriptive census COMPLETE
author: Waiel Al-Shujaa
prereg_sha256: a324e9b8348b099dba85600cceafb8bd1a910c455bde56e96c99353e22cb95f9
seed: 20260509
n_perm: 10000
---

# H-NEW-2200 — Iltifāt corpus map

**Bottom line.** The first objective, corpus-wide morphological census of *iltifāt*
(grammatical-person / number shift) at verse boundaries. The descriptive GENERATOR is
COMPLETE: **3,278 iltifāt loci** across the 6,122 intra-surah verse boundaries, fully
enumerated with coordinates and category. The pre-registered direction-locked density
test — *Meccan density > Medinan density* — **REVERSED its locked sign** (Medinan slightly
denser, Δ = −0.0144, p = 0.66) and is therefore published as **NULL with a pre-commit-violation
flag** per Protocol §1.8. A secondary, length-confounded position effect (s≤50 block denser
than s>50, p = 0.0001) is the real signal, and it is **not** a chronology effect: it is a
**surah-length / discourse-length** effect.

---

## 1. What was tested

*Iltifāt* (الالتفات) is the central balāgha device of abrupt grammatical shift in person,
number, or addressee. Defined by al-Zarkashī (*al-Burhān fī ʿulūm al-Qurʾān*, the *nawʿ* on
iltifāt) as "the change of speech from one mode to another, for the sake of freshness and
variety for the listener"; called by Ibn al-Athīr (*al-Mathal al-Sāʾir*) *shajāʿat
al-ʿarabiyya* ("the daring of Arabic"). al-Suyūṭī gives a parallel chapter in *al-Itqān*.
The modern ground-truth catalog is Abdel Haleem (BSOAS 55(3):407-432, 1992; transcribed at
`data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`).

The device has never been enumerated corpus-wide by an objective detector. This finding
builds a GENERATOR over QAC v0.4 person/number features.

**Detector (pre-registered, MW-1).** For each verse, derive a `dominant_person ∈ {1,2,3}`
and `dominant_number ∈ {S,D,P}` as the *modal* grammatical value over all finite verbs
(`POS:V`) and all pronouns (independent `POS:PRON` + suffix/object `PRON:*` clitics); ties
broken toward the later-occurring value (the value the verse "leaves the reader on"). An
intra-surah boundary (v, v+1) is an **iltifāt locus** iff dominant_person OR dominant_number
changes across it, both endpoints defined. Cross-surah boundaries excluded. Basmala counted
only as Q 1:1.

Rules-tuple: `(no-tashkeel, QAC-v0.4-segment, finite-V + PRON person-number, dominant=modal/tie→later, intra-surah-boundary, Hafs-Kūfan)`.

---

## 2. The census (descriptive deliverable — COMPLETE)

| Quantity | Value |
|:--|--:|
| Intra-surah verse boundaries | 6,122 |
| **Total iltifāt loci** | **3,278** (53.5% of all boundaries) |
| — person-shift loci | 2,297 |
| — number-shift loci | 1,919 |
| — both at one boundary | 938 |

### Person-shift category census (exhaustive)

| Category | Count | Classical type (Abdel Haleem) |
|:--|--:|:--|
| 3rd → 2nd (*ghayba → ḥuḍūr*) | 658 | Type 3 |
| 2nd → 3rd (*ḥuḍūr → ghayba*) | 655 | Type 4 |
| 3rd → 1st | 358 | Type 1 (classically the most common) |
| 1st → 3rd | 357 | Type 2 |
| 1st → 2nd | 139 | Type 5 (classically "1 disputed verse") |
| 2nd → 1st | 130 | Type 6 (classically "does not occur") |

### Number-shift category census

| Category | Count |
|:--|--:|
| SG → PL | 922 |
| PL → SG | 918 |
| SG ↔ DU / DU ↔ PL (all) | ~80 combined |

### Absent ↔ Present (*ghayba ↔ ḥuḍūr*) overlay

| Direction | Count |
|:--|--:|
| ghayba → ḥuḍūr (3rd → 2nd) | 658 |
| ḥuḍūr → ghayba (2nd → 3rd) | 655 |
| ghayba → ḥuḍūr (3rd → 1st) | 358 |
| ḥuḍūr → ghayba (1st → 3rd) | 357 |

### "I ↔ We" divine-majesty subtype

**29 loci** where the dominant person stays 1st across the boundary while grammatical number
flips singular↔plural — the *majestic plural* iltifāt (e.g. Q 12:55→56, Q 15:89→90, Q 25:48→49).
These are the empirical correlates of the classical "divine I/We" alternation. Full list in JSON.

> **Important interpretive caveat.** This is a *dominant-grammatical-person* detector. A 3rd→2nd
> boundary count includes shifts where the 3rd person is a human referent (disbelievers, peoples),
> not God. The detector is therefore a **superset generator** of canonical iltifāt, not a
> theologically-curated catalog. The high symmetry of the directional counts (3rd↔2nd ≈ 658/655;
> 3rd↔1st ≈ 358/357) reflects that most shifts are *reversible boundary alternations* in a running
> discourse, not the one-directional rhetorical turns the balāgha tradition foregrounds.

---

## 3. Instrument validation — recall vs Abdel Haleem ground truth (MW-6)

| Catalog category | Ground-truth verses | Detector hits | Recall |
|:--|--:|--:|--:|
| Person iltifāt (types 1–4 union) | 157 | 89 | **56.7%** |
| Number iltifāt | 31 | 19 | **61.3%** |

The detector fires on the canonical flagship loci — Q 1:5 (*iyyāka naʿbudu*, 3rd→2nd),
Q 27:60 (*amman khalaqa*), Q 10:22 (Yūnus multi-step shift), Q 36:22 (the disputed 1st↔2nd),
Q 108:2 (al-Kawthar) — confirming the instrument measures iltifāt. The ~40-43% misses are
**expected and structural**: (a) Abdel Haleem catalogs many *within-verse* and *intra-clause*
shifts a verse-boundary detector cannot see; (b) his references point to the verse where a
shift *lands*, while a boundary detector localizes to the (v, v+1) pair; (c) a *dominant*-person
detector misses shifts that do not move the modal person of the verse. This is a recall
ceiling for a clause-blind boundary detector, not a defect. Precision cannot be scored against
Abdel Haleem (his catalog is explicitly non-exhaustive).

---

## 4. The pre-registered direction-locked test — NULL (pre-commit violation)

**H1 (locked):** density(Meccan) > density(Medinan), Δ > 0 and Δ > 95th-percentile of a
10,000-perm label-shuffle null (α = 0.05, k = 1, seed 20260509).

| Region | Loci | Boundaries | Density |
|:--|--:|--:|--:|
| Meccan | 2,407 | 4,527 | 0.5317 |
| Medinan | 871 | 1,595 | **0.5461** |

**Δ = −0.0144 (Medinan denser), p = 0.6614. Direction REVERSED. → NULL with pre-commit-violation flag.**

The locked rationale — Meccan short oath/eschatological sūras would churn person faster — is
FALSIFIED at the dominant-grammatical-person scale. Per Protocol §1.8 the result is not
massaged: it is published as NULL with full prominence. **Verb-only replication confirms the
NULL**: dropping pronouns gives Meccan 0.3439 vs Medinan 0.3486, Δ = −0.0047 (still reversed).
Iltifāt density at the dominant-person grain is **register-independent** between Meccan and Medinan.

---

## 5. The real signal — a length-confounded position effect

The secondary (pre-registered, MW-3) mushaf-position split is strongly significant — but in
the *opposite* framing to the naive expectation:

| Block | Density | Δ | p |
|:--|--:|--:|--:|
| s ≤ 50 (early mushaf) | 0.5805 | +0.1844 | **0.0001** |
| s > 50 (late mushaf) | 0.3961 | | |

The early block is denser. Decomposing by surah length reveals the mechanism:

| Surah length band | n surahs | mean per-surah density |
|:--|--:|--:|
| 1–10 verses | 19 | 0.311 |
| 11–30 verses | 32 | 0.467 |
| 31–75 verses | 33 | 0.461 |
| 76+ verses | 30 | **0.585** |

Per-boundary density rises monotonically with surah length (Pearson r(n_verses, density) = +0.30).
The s≤50 block is denser **because the long sūras (al-sabʿ al-ṭiwāl + early mufaṣṣal) sit there**,
not because of an early-revelation rhetorical register. This also explains the reversed primary
test: Medinan sūras are systematically longer, so their *boundary-weighted* density edges out the
short late-Meccan sūras. **The driver of dominant-person iltifāt density is discourse length, not
chronological register.**

> The short Meccan mufaṣṣal sūras are NOT the iltifāt hotspots a naive reading of al-Suyūṭī's
> Meccan-intensity typology would predict — at the dominant-grammatical-person grain. Their
> rhetorical turns are real but operate *within* verses (the clause grain Abdel Haleem catches),
> below this detector's resolution.

**Densest sūras (≥5 boundaries):** Q 66 (0.91), Q 109 (0.80), Q 67 (0.79), Q 61 (0.77),
Q 17 (0.75), Q 14 (0.75), Q 72 (0.74), Q 73 (0.74), Q 15 (0.74), Q 65 (0.73) — a mix of both
registers, confirming register-independence.

---

## 6. Verdict

| Component | Verdict |
|:--|:--|
| Descriptive census (3,278 loci, all categories) | **COMPLETE** (first corpus-wide iltifāt map) |
| H1 Meccan > Medinan density | **NULL** (pre-commit direction reversed, p = 0.66) |
| Verb-only replication of H1 | **NULL** (direction still reversed) |
| Secondary s≤50 vs s>50 | significant (p = 0.0001) but **length-confounded**, not chronology |
| Detector validation | recall 56.7% person / 61.3% number vs Abdel Haleem (clause-blind ceiling) |

**Headline:** dominant-grammatical-person iltifāt density is governed by **discourse length**,
and is **independent of Meccan/Medinan register** — a clean NULL on the pre-registered direction.

---

## 7. Honest limits

- **Dominant-person resolution.** This detector sees only shifts that move the *modal* person of
  a verse across a boundary. It is clause-blind and within-verse-blind; Abdel Haleem's catalog
  operates at a finer grain. Recall ~57-61% is the structural ceiling, not a tuning failure.
- **Superset, not curated catalog.** Loci include human-referent 3rd-person alternations, so the
  3,278 figure is a *generator* count, larger than the theologically-foregrounded ~320-370 of the
  classical tradition. The category census is honest about this (§2 caveat).
- **The NULL is real, not an artifact.** It replicates under a verb-only tally and is explained by
  a length confound, not by detector noise.
- **MW-7.** The length-confound interpretation of the secondary split was noticed during analysis;
  it is reported descriptively (single-test, no novel claim of significance beyond the
  pre-registered position split itself).

---

## 8. Cross-references

- **Abdel Haleem 1992** (`data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`,
  `data/literature/balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md`) — ground truth;
  al-Zarkashī *al-Burhān* + al-Suyūṭī *al-Itqān* iltifāt chapters underneath.
- **H-NEW-660 compression-tail** + **s=50 kink (al-Suyūṭī makkī/madanī)** — the length/position
  gradient that drives the iltifāt-density position effect is the same s-axis as the compression-tail.
- **H-NEW-2140 (verse-initial anaphora runs)**, **H-NEW-2150 (istifhām density)** — sibling
  close-reading discourse-structure generators; same Wave-L family.
- **cross-finding-025-formal (scale-of-aggregation)** — the iltifāt phenomenon classically
  foregrounded by balāgha lives at the *within-verse / clause* scale; the dominant-person
  *boundary* scale measured here NULLs the register hypothesis, consistent with the project law
  that rhetorical structure is finer-grained than the surah container.

## 9. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2200-iltifat-corpus-map.md` (SHA-256 `a324e9b8348b099dba85600cceafb8bd1a910c455bde56e96c99353e22cb95f9`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2200.py` (runtime SHA-verified)
- JSON (full locus map + per-surah density + I↔We list): `findings/phase-b-hypotheses/csv/h-new-2200.json`
- finding: this file

*H-NEW-2200 logged 2026-05-29 by Waiel Al-Shujaa. The census is complete; the register hypothesis is null. Bismillāhi al-Raḥmāni al-Raḥīm.*
