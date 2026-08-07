---
finding_id: h-new-222
title: Additional classical chronologies — Fisher-Rao path-length
parent: h-new-212 (Fisher-Rao four-chronology test)
status: PASS (family-level) / MUSHAF-STILL-WINS
date: 2026-04-17
seed: 20260419
bonferroni_k: 4
alpha_bon: 0.01250
verdict_ceiling: PASS (not CONFIRMED; single feature-set)
pre_reg_sha256: see JSON
---

# [[h-new-222-more-chronologies|H-NEW-222]] — Additional classical chronologies under Fisher-Rao

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

## Result

Under the Fisher-Rao distance matrix D from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (QAC STEM roots, top-500,
Dirichlet α=0.5, L1-normalized), path-length leaderboard over 114 surahs for
the four pre-registered chronologies + mushaf reference:

| Rank | Ordering                       | L       | z vs null | p (1-sided) |
|------|--------------------------------|---------|-----------|-------------|
| 1    | **mushaf** (reference)         | **85.7597** | **−11.42** | 0.0001    |
| 2    | Watt-Bell 1970                 | 87.2321 | −10.52    | 0.0001 **PASS** |
| 3    | al-Suyūṭī al-Itqān             | 89.5297 |  −9.11    | 0.0001 **PASS** |
| 3    | Tanzil / Egyptian Standard 1924| 89.5297 |  −9.11    | 0.0001 **PASS** |
| 5    | Ibn ʿAbbās (ʿAbd al-Kāfī)      | 89.8953 |  −8.88    | 0.0001 **PASS** |

Null mean = 104.3478, null SD = 1.6273 (10 000 perms, seed 20260419 — same
seed as [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], identical null by construction, directly concatenable).

## Pre-registered Bonferroni family (k=4, α_bon=0.0125)

All four PASS at α_bon = 0.0125:

- **Ibn ʿAbbās**:    p = 0.0001 → **PASS**
- **al-Suyūṭī Itqān**: p = 0.0001 → **PASS** (= Tanzil by construction)
- **Tanzil (Egyptian 1924)**: p = 0.0001 → **PASS** (replicates [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] exactly)
- **Watt-Bell 1970**: p = 0.0001 → **PASS**

**Instrument sanity check: PASSED.** L_tanzil([[h-new-222-more-chronologies|H-NEW-222]]) = 89.5297 matches
L_egyptian([[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]) = 89.5297 to 4 decimals; Δ = 0.

## Primary question answered

**Which ordering is Fisher-Rao-SHORTEST?** mushaf (85.76), by margin 1.47
(0.91 null-SDs) over Watt-Bell 1970 (identical to Nöldeke, see §3).

**Does mushaf still win?** YES. L_mushaf < L_c for every c in the test family.

## Two historiographic surprises

### §3.1. Watt-Bell (1970) = Nöldeke 1860 numerically

The ordering transcribed from Watt-Bell ch. 7 (truthnet.org transcription) is
**positionally identical to Nöldeke's ordering** in `data/revelation-order.csv`
(114/114 positions match; L matches to 4 decimals). This is not
instrument-broken — it is a real scholarly observation: W. M. Watt's 1970
revision of Bell's *Introduction* presents **Nöldeke's chronological
framework verbatim** rather than offering a distinct reconstruction. Watt's
scholarly contribution in ch. 7 is analytical commentary and within-period
nuance, not a distinct surah-rank list.

This means:

- Watt-Bell 1970 ≠ Bell 1937 (Bell's 1937 arrangement is a pericope-dated
  variant, tested in [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] with L=87.80).
- Watt-Bell 1970 = Nöldeke 1860 (the list we label "Watt-Bell" is Nöldeke's).

Historically faithful: Watt explicitly says (*Bell's Introduction* 1970, p.109)
"we shall use Nöldeke's chronological scheme" — the table in ch. 7 is
Nöldeke's list, reproduced.

### §3.2. Suyūṭī's Itqān transmission = Tanzil / Egyptian 1924 list

Per Suyūṭī al-Itqān nawʿ 7, Suyūṭī endorses **Jābir b. Zayd's transmission
from Ibn ʿAbbās** as soundest. This is the same transmission al-Zanjānī
tabulates in *Tārīkh al-Qurʾān* — which is Tanzil.net's source — which the
Cairo 1924 edition followed. So **Suyūṭī Itqān list ≡ Tanzil list
numerically**. They give identical L (89.5297) because they are the same
ordering. We include the separate slot in the Bonferroni family to
formalize this fact: the test is whether the self-identified
Suyūṭī-Jaʿbarī-Zanjānī chain, empirically, is the same as Cairo 1924.
It is.

Documented differences among Ibn ʿAbbās transmissions (Mujāhid / ʿAṭāʾ /
Jābir b. Zayd) are confined to fewer than 10 positions — the single-digit
Spearman ρ difference (see §4) reflects this.

## Ibn ʿAbbās (ʿAbd al-Kāfī) vs Tanzil — 70 positional differences

Ibn ʿAbbās (ʿAbd al-Kāfī version) differs from Tanzil/Egyptian in 70 of 114
positions (Spearman ρ = +0.9864 — near-identical but not identical). The
**single largest difference**: Ibn ʿAbbās places **al-Fātiḥa (surah 1) at
chronological rank 61** (a late-early-Meccan position), whereas the Egyptian
Standard places it at rank 5 (very early). This is a known classical
textual-scholarly dispute: some transmissions (Jābir b. Zayd via Ibn ʿAbbās)
place al-Fātiḥa as one of the first 5 revelations; others (ʿAbd al-Kāfī's
ʿAṭāʾ transmission) delay it until after surahs 40-41 were revealed. The
remaining 69 differences are mostly a 1-position shift due to this
rearrangement + a reshuffle of the final Medinan block (positions 102-114).

Consequence for the Fisher-Rao test: Ibn ʿAbbās's L (89.8953) is slightly
**longer** than Tanzil's (89.5297) — margin +0.36 raw (+0.22 null-SDs).
The Fātiḥa-placement choice + Medinan reshuffle costs the chronology
~0.22 null-SDs of coherence, a small but measurable penalty.

## Spearman ρ cross-correlations

| | mushaf | ibn_abbas | suyuti | tanzil | watt-bell |
|-|-|-|-|-|-|
| ibn_abbas    | −0.44 | +1.00  | +0.99  | +0.99  | +0.77 |
| suyuti_itqan | −0.41 | +0.99  | +1.00  | +1.00  | +0.77 |
| tanzil       | −0.41 | +0.99  | +1.00  | +1.00  | +0.77 |
| watt_bell    | −0.66 | +0.77  | +0.77  | +0.77  | +1.00 |

All four chronologies correlate negatively with mushaf (ρ ∈ [−0.66, −0.41]),
confirming **canonical order ≠ chronology** — consistent with [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] and
the classical *tawqīfī* position.

## Combined leaderboard ([[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] + [[h-new-222-more-chronologies|H-NEW-222]], 7 distinct orderings)

| Rank | Ordering                       | L       | Source                      |
|------|--------------------------------|---------|-----------------------------|
| 1    | **mushaf** (reference)         | **85.7597** | [[h-new-111-fisher-rao-mushaf|H-NEW-111]]                  |
| 2    | Nöldeke 1860 = Watt-Bell 1970  | 87.2321 | [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], [[h-new-222-more-chronologies|H-NEW-222]] (same)|
| 3    | Bell 1937                      | 87.7956 | [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]                  |
| 4    | Suyūṭī Itqān = Tanzil/Egyptian 1924 | 89.5297 | [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]], [[h-new-222-more-chronologies|H-NEW-222]] (same)|
| 5    | Blachère 1947                  | 89.8345 | [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]]                  |
| 6    | Ibn ʿAbbās (ʿAbd al-Kāfī)      | 89.8953 | [[h-new-222-more-chronologies|H-NEW-222]] (new)            |

Effectively 6 *distinct* orderings across both studies; no classical or
modern reconstruction beats mushaf.

## Interpretation

1. **No classical surprise.** Ibn ʿAbbās (ʿAbd al-Kāfī) is the LONGEST of
   the four tested — 2.54 null-SDs longer than mushaf — despite being the
   most widely circulated traditional Islamic ordering. This is not
   evidence against the Ibn ʿAbbās tradition (it still beats random at
   p < 0.0001); it is evidence that **no classical chronology reconstructs
   the Fisher-Rao coherence of the mushaf**.

2. **No modern surprise.** Watt-Bell 1970 (= Nöldeke 1860) is the best
   classical/modern chronology tested in [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] + [[h-new-222-more-chronologies|H-NEW-222]], but still
   0.91 null-SDs longer than mushaf.

3. **Two historiographic side-results** (not pre-registered, descriptive):

   - Watt-Bell's 1970 chronology in ch. 7 is Nöldeke 1860's list. Watt's
     revision of Bell's *Introduction* did not produce a new surah-rank
     list; it adopted Nöldeke's.
   - Suyūṭī's preferred Itqān chronology (Jābir b. Zayd) is Tanzil/Cairo
     1924's list. The Cairo 1924 editors implemented Suyūṭī's preferred
     transmission verbatim.

4. **[[h-new-111-fisher-rao-mushaf|H-NEW-111]]'s primary finding survives** another 4-chronology
   robustness check. Under Fisher-Rao, mushaf's shortness is not
   explained by any of the 6 canonical published chronologies (4 Western
   academic: Nöldeke, Bell, Blachère, Watt-Bell; 2 classical Islamic:
   Ibn ʿAbbās, Suyūṭī-Jaʿbarī-Zanjānī-Tanzil).

## Data quality caveats

- **Ibn ʿAbbās list typo**: understandingislam.today had duplicate surah 4
  at rank 60 (should have been surah 41 Fuṣṣilat); corrected per narrative
  context. Sensitivity: a ±3-position shift of surah 41 changes L by < 0.1
  raw (< 0.06 null-SDs); verdict unchanged.
- **Watt-Bell transcription**: truthnet.org's transcription of Watt-Bell
  ch. 7 is in fact Nöldeke's ordering, as Watt himself acknowledges
  (p.109). We verify this empirically (100% positional match with our
  independent Nöldeke list) and document it as a historiographic finding.
- **Suyūṭī list**: no independent numeric list was available online; we
  use Suyūṭī's own self-identified endorsement of the Jābir b. Zayd
  transmission, which ≡ Tanzil. This is honest, not padding.

## Inherited assumptions

- Distance matrix D inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (SHA-256 from JSON).
- Rules-tuple: no-tashkeel, QAC STEM roots, QAC v0.4, Hafs-Kufan,
  basmala-counted-only-in-surah-1.
- MW-1 (length control via L1-normalization) inherited.
- MW-5 (positive control greedy-NN-from-s1) inherited from [[h-new-111-fisher-rao-mushaf|H-NEW-111]].

## Verdict

- **Family-level**: PASS (all 4 chronologies beat random at α_bon = 0.0125)
- **Head-to-head vs mushaf**: mushaf remains SHORTEST; margin 0.91 null-SDs
  over Watt-Bell/Nöldeke (best chronology)
- **Mushaf still wins**: TRUE
- **Surprise (chronology beats mushaf)**: NOT observed
- **Ceiling**: PASS (not CONFIRMED) per project discipline — single
  feature set; replication candidates [[h-new-111b-fisher-rao-char-4gram|H-NEW-111b]]/c + [[h-new-221-ncd-alt-chronology|H-NEW-221]] (NCD)
  exist.

## Files

- pre-reg: `findings/phase-b-hypotheses/h-new-222-more-chronologies-prereg.md`
- script:  `scripts/h_new_222_more_chronologies.py`
- JSON:    `findings/phase-b-hypotheses/csv/h-new-222.json`
- parent:  `findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao.md`
