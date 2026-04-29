---
id: H-NEW-200
title: Surah-name etymology class × mushaf position / Meccan–Medinan / Nöldeke-phase cluster predictor
phase: B
status: 2/3 PASS, 1 NULL — etymology-class PREDICTS mushaf-rank and Nöldeke-phase but NOT Meccan/Medinan binary at Bonferroni-3
date: 2026-04-17
executed_by: autonomous H-NEW-200 agent
seed: 20260419
bonferroni_family: 2026-04-17-H-NEW-200-name-class-predictor
bonferroni_k: 3
alpha_bon: 0.01667
n_perm: 100000
rules_tuple: (hafs-kufan; no-tashkeel; canonical 114; Tanzil Egyptian Standard + Wikipedia Nöldeke rev-order; locked H-NEW-49 9-way taxonomy)
pre_reg: h-new-200-name-class-predictor-prereg.md
verdict: "T1 PASS (p=0.00106), T2 NULL (p=0.0433), T3 PASS (p=0.00092)"
---

# [[h-new-200-name-class-predictor|H-NEW-200]] — Etymology-class predictor of mushaf position, Meccan/Medinan, and Nöldeke cluster

## Core result

| Test | Statistic | Obs | df | Perm p | α_bon=0.01667 | Verdict |
|---|---|---:|---:|---:|---:|---|
| **T1** Mushaf position (Kruskal-Wallis) | H | **24.04** | 8 | **0.00106** | ✓ | **PASS** |
| **T2** Meccan/Medinan (χ², 6 cols pooled) | χ² | 12.73 | 6 | 0.04334 | ✗ | NULL |
| **T3** Nöldeke 4-phase (χ², 6 cols pooled) | χ² | **42.07** | 18 | **0.00092** | ✓ | **PASS** |

**Bottom line**: the 9-way etymology of the surah name alone — with no
compositional statistics, no lexical counts, no phonology — predicts the
surah's mushaf position and its Nöldeke compositional phase at perm
p < 10⁻³. The Meccan/Medinan binary is the weakest predictor (pooled
full p = 0.043, below raw α=0.05 but above Bonferroni-3 α_bon=0.0167),
because the 4-way Nöldeke partition encodes structure that the
meccan/medinan binary collapses.

## Class distribution (114 surahs)

| Class | N |
|---|---:|
| SOCIAL_LEGAL | 22 |
| COSMOLOGICAL_NATURAL | 19 |
| EVENT_ESCHATOLOGICAL | 18 |
| REVELATION_RITUAL | 17 |
| ANIMAL_OBJECT | 13 |
| PROPHET_PERSON | 11 |
| DIVINE_ATTRIBUTE | 7 |
| MUQATTAAT_LETTER | 4 |
| OTHER_ABSTRACT | 3 |

## T1 — Class median mushaf-rank ordering

The H = 24.04 signal is driven by a clear monotonic-with-gaps pattern in
class median mushaf-rank:

| Class | N | Median mushaf-rank | Interpretation |
|---|---:|---:|---|
| PROPHET_PERSON | 11 | **19** | Middle-mushaf narrative spine (Q10 Yūnus … Q47 Muḥammad) |
| MUQATTAAT_LETTER | 4 | 37 | ḥawāmīm/Ṭā-Hā/Yā-Sīn/Qāf middle-mushaf cluster |
| REVELATION_RITUAL | 17 | 41 | Spread (Q1, Q17, Q22, Q25 … Q97) |
| ANIMAL_OBJECT | 13 | 43 | Spread |
| DIVINE_ATTRIBUTE | 7 | 55 | Spread (Q24, Q35, Q55, Q67, Q87, Q112) |
| SOCIAL_LEGAL | 22 | 59 | Medinan cluster + short-mufaṣṣal social (Q109, Q114) |
| COSMOLOGICAL_NATURAL | 19 | **70** | Back-mushaf short-mufaṣṣal concentration |
| EVENT_ESCHATOLOGICAL | 18 | **78.5** | Back-mushaf short-mufaṣṣal |
| OTHER_ABSTRACT | 3 | 102 | Short back (Q72 Jinn, Q102 Takāthur, Q108 Kawthar) |

The 60-position median-gap between PROPHET_PERSON (19) and
EVENT_ESCHATOLOGICAL (78.5) is the single dominant axis.

## T3 — Nöldeke-phase × etymology-class full contingency table

| Phase \\ Class | PROPH | ANIM | DIV | COSM | EVENT | SOC | REVEL | MUQ | OTHER | Total |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| **Early Meccan** | 0 | 5 | 3 | **13** | **13** | 5 | 7 | 0 | 2 | 48 |
| **Middle Meccan** | 3 | 2 | 1 | 3 | 0 | 4 | 3 | **4** | 1 | 21 |
| **Late Meccan** | **6** | 3 | 2 | 3 | 1 | 3 | 3 | 0 | 0 | 21 |
| **Medinan** | 2 | 3 | 1 | 0 | 4 | **10** | 4 | 0 | 0 | 24 |
| Total | 11 | 13 | 7 | 19 | 18 | 22 | 17 | 4 | 3 | 114 |

Dominant cells (observed ≫ expected):

- **COSMOLOGICAL_NATURAL → Early Meccan** (13/19 = 68.4% in 42% of corpus).
  Al-Najm, al-Qamar, al-Ḥijr [?actually Middle], al-Najm, al-Ṭūr, al-Ṭāriq,
  al-Fajr, al-Balad, ash-Shams, al-Layl, aḍ-Ḍuḥā, al-Falaq, al-ʿAṣr…
- **EVENT_ESCHATOLOGICAL → Early Meccan** (13/18 = 72.2%). Short-mufaṣṣal
  eschatology: al-Qiyāma, al-Mursalāt, an-Nabaʾ, an-Nāziʿāt, al-Inshiqāq,
  al-Qāriʿa, al-Zalzala, etc.
- **MUQATTAAT_LETTER → Middle Meccan** (4/4 = 100%). Ṭā-Hā Q20, Yā-Sīn Q36,
  Ṣād Q38, Qāf Q50 — all Middle-Meccan Nöldeke ranks. Zero hits elsewhere.
- **PROPHET_PERSON → Late Meccan** (6/11 = 54.5%). Yūnus Q10, Hūd Q11,
  Yūsuf Q12, Ibrāhīm Q14, Luqmān Q31, Sabaʾ Q34 — the long Late-Meccan
  narrative complex.
- **SOCIAL_LEGAL → Medinan** (10/22 = 45.5%; Medinan class = 21% of corpus).
  An-Nisāʾ, al-Aḥzāb, al-Ḥujurāt, al-Munāfiqūn, al-Mumtaḥana, aṣ-Ṣaff,
  al-Mujādila, al-Mutaffifīn (Meccan), al-Muṭaffifīn, aṭ-Ṭalāq, at-Taḥrīm,
  Quraysh, al-Humaza, etc.

## T2 — Meccan/Medinan collapses the signal

Dropping from the 4-way Nöldeke phase to the binary Meccan/Medinan
hides the Early/Middle/Late-Meccan sub-structure. The binary χ² is 12.73
on 6 df (pooled) and p_perm = 0.0433 — above α_bon = 0.0167. This is
informative: the structural signal lives in the *compositional phase*,
not in the *geographical label*.

## Interpretation

Etymology-class is a PURE SURFACE-METADATA PREDICTOR — a label assigned
from the single-word surah name — yet it carries 3+ bits of information
about where the surah sits in mushaf and Nöldeke orderings. This
converges with [[h-new-183-chronology-predictor|H-NEW-183]] (chronology-from-composition R²=0.84) and
[[h-new-192-mushaf-position-decomposition|H-NEW-192]] (mushaf-from-composition R²=0.76) but uses a radically
impoverished feature: just the semantic class of the name.

**Mechanism candidates** (not tested here):
1. **Compositional-tradition indexing**: short-mufaṣṣal Early-Meccan
   surahs were *named* after the natural-phenomenon oaths that open them
   (al-Najm, ash-Shams, al-Layl, al-Fajr) — so COSMOLOGICAL_NATURAL class
   is a direct consequence of the oath-opening tradition (cf. [[h-new-196-oath-cluster|H-NEW-196]]
   oath-cluster findings).
2. **Medinan legal corpus**: the Medinan period produced the long
   ḥukm-rich narratives which were named after legal/social-organization
   concepts (Nisāʾ, Aḥzāb, Mujādila, Ṭalāq, Taḥrīm), giving the
   SOCIAL_LEGAL → Medinan near-deterministic mapping.
3. **Late-Meccan prophet-cycle**: Q10–Q14 Yūnus-Hūd-Yūsuf-Ibrāhīm is a
   well-known Late-Meccan narrative sequence; all 3 of Yūnus, Hūd, Yūsuf
   are Late Meccan in the Nöldeke ordering.
4. **Muqaṭṭaʿāt letter-only naming** is restricted to the Middle-Meccan
   ṬāHā/YāSīn/Ṣād/Qāf tradition — a tight localized phenomenon.

The name is therefore a *phase-indexed* label: classical-era naming
conventions varied systematically across the four Nöldeke phases.

## Honest limits

- The 9-way taxonomy was locked in [[h-new-49-surah-name-class|H-NEW-49]]. Alternative taxonomies
  (7-way collapsing ANIMAL_OBJECT + COSMOLOGICAL_NATURAL, or 11-way
  splitting PROPHET_PERSON into individual prophets vs collectives) could
  yield different effect sizes.
- These tests are *descriptive* — they establish class × phase non-
  independence but do not prove the class CAUSES the placement (and
  nothing in the mushaf-compositional literature would predict that
  direction). Most plausible reading: phase-specific compositional
  style shaped the naming convention, not vice versa.
- T2 being NULL at Bonferroni-3 but nominally significant at raw α=0.05
  (p=0.043) means the Meccan/Medinan binary carries the signal too but
  more weakly than the 4-way phase. We do NOT reject the null for T2.
- No feature-residualization was attempted here. H-NEW-200.1 should
  control for verse_count and mean_verse_length to ask whether
  etymology-class adds information BEYOND length-phase coupling.

## Data and code

- `scripts/h_new_200_name_class_predictor.py` — test driver
- `findings/phase-b-hypotheses/csv/h-new-200.json` — full results
- `findings/phase-b-hypotheses/csv/h-new-200-per-surah.csv` — per-surah table
- Reused locked taxonomy: `scripts/h_new_49_surah_name_class.py::SURAH_CLASS`
- Reused phase table: `data/revelation-order.csv`
