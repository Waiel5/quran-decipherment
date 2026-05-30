---
id: H-NEW-2500
title: Iltifāt TYPE × GENRE cross-tabulation — clause-scale person/number shifts are register-coded
date: 2026-05-30
phase: B
author: Waiel Al-Shujaa
verdict: CONFIRMED (H1 association + H2 both locked dominant-type directions)
parent: H-NEW-2390
prereg_sha256: ced7003da523afc2ebb83e08027422c07a4e9137ccd4dfd6463c455b8b625d4c
seed: 20260509
seed_replication: 20260510
n_perm: 10000
---

# H-NEW-2500 — Iltifāt TYPE × GENRE cross-tabulation

**Verdict: CONFIRMED.** Iltifāt TYPE is non-randomly associated with GENRE
(χ² = 1253.9, NMI = 0.0224, Cramér's V = 0.132; label-permutation p = 0.0001 for both
χ² and NMI, Bonferroni-2 α = 0.025; replicates at seed 20260510). Both pre-locked
dominant-type directions held: **narrative is the home of the 3↔1 divine-narrative
voice** (standardized residual +18.2) and **legal-Medinan is the home of the 2↔3
direct-address shift** (+13.1, top-of-row) — no pre-commit violation. Pre-reg SHA-256
`ced7003da523afc2ebb83e08027422c07a4e9137ccd4dfd6463c455b8b625d4c`, runtime-verified.
The H-NEW-2390 detector is **reused, not recomputed** (census marginals reproduced by
assertion: person-shifts 12,379, number-shifts 11,584).

---

## 0. What this adds to H-NEW-2390

H-NEW-2390 (§10.104) showed clause-scale iltifāt *density* is region-distinguishing
(Meccan > Medinan). It counted loci agnostic of type. H-NEW-2500 reuses the exact same
16,998-locus catalogue (`csv/h-new-2390.json`) and asks the richer question: **which
KIND of person/number shift goes with which KIND of passage?** The answer is a clean,
strongly significant type×genre map dominated by a narrative↔legal person-grammar
dissociation.

## 1. The genre proxy (deterministic, surah-scale, pre-locked)

Each of the 114 surahs receives exactly one genre by a locked hierarchical decision
procedure over region + length-band + marker-lexicon (full spec in
`prereg-h-new-2500-iltifat-genre-crosstab.md` §1):

| Genre | n | Decision rule (first match wins) | Classical anchor |
|:--|:-:|:--|:--|
| `legal_medinan` | 20 | Medinan AND (`yā ayyuhā alladhīna āmanū` + `kutiba ʿalaykum`) ≥ 1 | al-Suyūṭī *Itqān* nawʿ 1 (validated H-NEW-2270: 0/20 Meccan) |
| `narrative` | 31 | qāla-density ≥ 1.0 / 100 words | qaṣaṣ register (H-NEW-2260 prophet-cycles) |
| `eschatological_mufassal` | 40 | s ≥ 78 OR eschat-density ≥ 1.5 / 100 words | al-Zarkashī mufaṣṣal tiers; `idhā`-cascade H-NEW-2250 |
| `liturgical_didactic` | 23 | residual (Meccan `qul`-discourse + hymnic) | — (explicit residual) |

The 20 `legal_medinan` surahs are exactly the 20 carrying ≥1 *yā ayyuhā alladhīna
āmanū* — i.e. the proxy reproduces al-Suyūṭī's Medinan-legislative diagnostic exactly.

## 2. The contingency table (counts)

Unit = iltifāt type-tag (a `both`-locus contributes one person-tag + one number-tag;
Σ = 23,963 tags over 16,998 loci). Reused verbatim from `h-new-2390.json`.

| genre \ type | P_3↔1 | P_2↔3 | P_1↔2 | N_S↔P | N_dual | **row** |
|:--|--:|--:|--:|--:|--:|--:|
| narrative | 2274 | 2038 | 1219 | 4352 | 204 | **10087** |
| legal_medinan | 643 | 2887 | 577 | 4162 | 119 | **8388** |
| eschatological_mufassal | 192 | 444 | 129 | 692 | 19 | **1476** |
| liturgical_didactic | 585 | 1102 | 289 | 2003 | 33 | **4012** |
| **col** | **3694** | **6471** | **2214** | **11209** | **375** | **23963** |

**Type glossary:** `P_3↔1` ghayba↔mutakallim (divine narrative voice, Abdel Haleem
I.1+I.2); `P_2↔3` ḥuḍūr↔ghayba (honouring / reproaching / commanding, I.3+I.4);
`P_1↔2` mutakallim↔mukhāṭab (rare, incl. disputed Q 36:22, I.5+I.6); `N_S↔P` number
singular↔plural (contains the divine *I↔We* majestic plural); `N_dual` dual-iltifāt.

## 3. The signal — standardized Pearson residuals

| genre \ type | P_3↔1 | P_2↔3 | P_1↔2 | N_S↔P | N_dual |
|:--|--:|--:|--:|--:|--:|
| **narrative** | **+18.2** | −13.1 | +9.4 | −5.3 | +3.7 |
| **legal_medinan** | −18.1 | **+13.1** | −7.1 | +3.8 | −1.1 |
| eschatological_mufassal | −2.4 | +2.3 | −0.6 | +0.1 | −0.9 |
| liturgical_didactic | −1.4 | +0.6 | −4.2 | +2.9 | −3.8 |

The dominant structure is a **narrative ↔ legal-Medinan mirror on the PERSON axis**:

- **Narrative is the home of the 3↔1 divine-narrative voice (+18.2)** and actively
  *avoids* the 2↔3 direct-address shift (−13.1). It also carries the 1↔2 speaker↔addressee
  shift above chance (+9.4) — qaṣaṣ is dialogue-rich (prophet ↔ people ↔ divine narrator).
- **Legal-Medinan is the exact mirror (+13.1 on 2↔3, −18.1 on 3↔1).** The legislative
  register opens by addressing the believing community in the 2nd person
  (*yā ayyuhā alladhīna āmanū…*) then turns to the absent 3rd party / the ruling about
  Allāh — Abdel Haleem's "honouring, reproaching, commanding, requesting" direct-address
  function. It does NOT use the divine-narrative 3↔1 voice (that belongs to qaṣaṣ).
- **Eschatological-mufaṣṣal** is mildly 2↔3-leaning (+2.3) — the staccato address of the
  Day-of-Judgment sermon — but its residuals are small: the short-mufaṣṣal's intensity
  lives in oath/cadence/cascade (H-NEW-2210/2240/2250), not person-churn (consistent with
  H-NEW-2390's H2 reversal, where short-mufaṣṣal was the SPARSEST iltifāt register).
- **Liturgical-didactic** carries no marked person-type; its only above-chance lean is
  the bare singular↔plural number shift (+2.9) and a deficit of 1↔2 and dual (−4.2, −3.8).

**Dominant (largest-residual) type per genre:** narrative → **P_3↔1**;
legal_medinan → **P_2↔3**; eschatological_mufassal → **P_2↔3**;
liturgical_didactic → **N_S↔P**.

## 4. The divine *I↔We* majesty-plural sub-count

The theologically marked *iltifāt al-ʿadad* (person stays 1st, number switches S↔P —
the majestic-plural "I/We" turn, e.g. Q 75:1-4) is rare within the verse (11 loci total,
matching the H-NEW-2390 census). **9 of 11 fall in the `narrative` genre**, 1 in
legal_medinan, 1 in liturgical_didactic, **0 in eschatological_mufassal.** The divine
majestic-plural shift is therefore a feature of the *divine-narration* register, not the
sermon register — converging with the +18.2 narrative `P_3↔1` residual: the long
narrative Meccan surahs (Q 14, Q 18 carry these loci per the 2390 catalogue) are where
the divine voice modulates person AND number around itself. This is the concrete answer
to the pre-flight prompt's example ("divine sg↔pl majesty-shifts concentrate in a
specific register") — they concentrate in **narrative**, the genre of the divine
narrative voice.

## 5. Statistics + robustness

| Test | χ² | NMI | Cramér's V | p(χ²) | p(NMI) |
|:--|--:|--:|--:|--:|--:|
| **Full 5×4 (H1)** | 1253.9 | 0.0224 | 0.132 | **0.0001** | **0.0001** |
| Replication seed 20260510 | — | — | — | 0.0001 | 0.0001 |
| **Person-only 3×4 (MW-3)** | 1134.1 | 0.0470 | **0.214** | 0.0001 | 0.0001 |

- **H1 PASS** at Bonferroni-2 (α = 0.025) on both association statistics; the smallest
  attainable permutation p (1/10001) — observed χ² exceeds every one of 10,000 label-shuffle
  nulls.
- **MW-3 person-only** (drop the two number classes): the association is *concentrated*
  on the person axis — Cramér's V rises from 0.132 to **0.214** when the number classes
  (which are genre-flatter) are removed. The genre signal is fundamentally a
  **person-grammar** signal.
- **MW-5 replication** holds at the second seed.
- **MW-6 sanity:** the reused catalogue reproduces the H-NEW-2390 census marginals
  exactly (asserted in-script).

## 6. H2 verdict (locked dominant-type directions)

| Locked prediction | Observed residual | Verdict |
|:--|--:|:--|
| legal_medinan × P_2↔3 POSITIVE and row-max | +13.07 (row-max = P_2↔3) | **PASS** |
| narrative × P_3↔1 POSITIVE | +18.23 | **PASS** |

Both locked directions held. **H2 PASS, no pre-commit violation.**

## 7. Interpretation — the grammar of genre

The map operationalizes, at corpus scale, the *functional* coding that al-Zarkashī
(*al-Burhān*, nawʿ al-iltifāt) and Abdel Haleem (1992 BSOAS) describe qualitatively:

1. **Qaṣaṣ (narrative) grammar = the divine narrative voice.** The 3rd↔1st turn
   (recounting "He/they… then We…") is the signature of the story-telling register; the
   majestic-plural I↔We modulation lives here too. Narrative *shuns* the 2↔3
   address-turn.
2. **Legislative (legal-Medinan) grammar = direct community address.** The 2nd↔3rd turn
   (addressing the believers, then the ruling/absent referent) is the signature of the
   covenant register. It *shuns* the divine-narrative 3↔1 voice.

These two are near-perfect mirror images (|residual| ≈ 18 / 13 in opposite signs),
which is why the person-only sub-table carries the strongest association (V = 0.214).
The eschatological-mufaṣṣal and liturgical-didactic registers are person-grammar-flat —
their rhetorical intensity is carried by *other* devices (oath, cadence, cascade,
refrain), not person-churn, consistent with the H-NEW-2390 H2 reversal and with
H-NEW-2210/2240/2250.

## 8. cross-finding-025 integration

This is a new data point for the scale-of-aggregation programme, but a **type-resolved**
one. H-NEW-2390 showed iltifāt *density* distinguishes region at the clause scale;
H-NEW-2500 shows the *type composition* distinguishes genre at the clause scale — and
the discriminating axis is PERSON, not number. The genre signal is not "more vs less
iltifāt" but "WHICH iltifāt": narrative does the 3↔1 divine-voice turn, legislation does
the 2↔3 address turn. This refines cross-finding-025 from a density law to a
**type-composition law** at the clause grain.

## 9. Honest limits

- **Genre proxy is coarse.** It is a deterministic surrogate for an exegetical genre
  judgment; surahs are internally heterogeneous (Q 2 al-Baqara is both legislative and
  narrative — the proxy assigns it `legal_medinan` by the locked priority because its
  legislative marker fires). The proxy captures the *dominant* register, not pericope-level
  genre. A pericope-scale follow-up (segmenting each surah and re-tagging) is queued as
  **H-NEW-2500.1** but requires a pre-registerable segmentation to avoid garden-of-forking-paths.
- **`liturgical_didactic` is a residual cell**, reported as such; its near-null residuals
  are consistent with it being a heterogeneous catch-all.
- **Type taxonomy covers only person/number iltifāt** (Abdel Haleem types I + II). Tense/mood,
  addressee, case, and noun-for-pronoun iltifāt (types III–VI) are not in the H-NEW-2390
  detector and are out of scope.
- **Tag-multiplicity:** `both`-loci contribute two tags; the label-permutation null is
  invariant to this (it preserves the exact tag structure and shuffles only genre labels),
  so the inference is unbiased, but the raw χ² magnitude should be read as a permutation
  statistic, not a parametric one.
- The effect sizes (V = 0.13 full / 0.21 person-only) are *small-to-moderate* — the
  association is highly significant and directionally crisp, but iltifāt type is one
  register signal among several, not a deterministic genre classifier.

## 10. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2500-iltifat-genre-crosstab.md`
  (SHA `ced7003da523afc2ebb83e08027422c07a4e9137ccd4dfd6463c455b8b625d4c`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2500.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2500.json`
- cross-tab deliverable: `findings/phase-b-hypotheses/h-new-2500-iltifat-genre-crosstab.md` (this file)
- parent locus catalogue (reused): `findings/phase-b-hypotheses/csv/h-new-2390.json`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
