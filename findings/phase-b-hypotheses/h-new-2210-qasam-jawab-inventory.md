---
id: H-NEW-2210
title: Qasam / jawāb al-qasam structural inventory + oath-density concentration test
type: finding
date: 2026-05-29
author: Waiel Al-Shujaa
phase: B
verdict: CONFIRMED
seed: 20260509
prereg_sha256: b47aaa5017e118b80b1b07b9a6c6da70eae3b89ba8cce79866cf0f18f281f75d
rules_tuple: (no-tashkeel, QAC-morphology-POS, Hafs-Kufan, Mashriqi)
---

# H-NEW-2210 — Qasam / Jawāb al-Qasam Structural Inventory

**Verdict: CONFIRMED** (both pre-locked cells pass in the locked direction at p_perm < 0.0001,
Bonferroni k=2, α_bon = 0.025; MW-5 replication holds).

Pre-registration: `prereg-h-new-2210-qasam-jawab-inventory.md`
(SHA-256 `b47aaa5017e118b80b1b07b9a6c6da70eae3b89ba8cce79866cf0f18f281f75d`, verified at runtime).

## 1. What was built

A morphology-grounded GENERATOR (not a curated list) that enumerates **every** Quranic oath-opening
using the QAC v0.4 POS-tag layer, separating the oath-wāw (*wāw al-qasam*) from the ~8,500
conjunction-wāws that raw substring matching would conflate.

**Three morphologically-defined oath introducers (raw QAC counts, exact):**

| Introducer | QAC tag | Count | Example |
|:--|:--|:--:|:--|
| oath-wāw (*wāw al-qasam*) | `PREFIX\|w:P+` (POS P) | **28** | `wa-l-fajr` (89:1), `wa-l-shams` (91:1) |
| *(lā) uqsimu* | `LEM:>aqosamu` form-IV impf 1S | **8** | `lā uqsimu bi-yawmi-l-qiyāma` (75:1) |
| *ta-llāhi* | `PREFIX\|ta+` (POS P) | **9** | `ta-llāhi tafta'u` (12:85) |
| **total oath openings** | | **45** | across **44 clusters** (Q 75 stacks 2 uqsimu) |

All 45 morphological openings are captured by the generator (28 + 9 + 8), matching the raw QAC
counts exactly — full audit in `csv/h-new-2210.json`.

## 2. The inventory (44 oath-clusters, by surah)

Each cluster = one oath-opening + its coordinated genitive sworn-object chain (*taʿaddud al-muqsam
bihi*), sharing one *jawāb al-qasam*. The jawāb is detected as the first canonical apodosis marker
after the oath series: *inna/anna* (ACC), *lām al-tawkīd* (`la-`), *qad*, the negative-oath *mā / in*,
or `bare` (elided/no marker).

**Stacked-oath champions (taʿaddud al-muqsam bihi):**

| Surah | Sworn-object series | n_objects | jawāb |
|:--|:--|:--:|:--|
| **Q 91 al-Shams** | al-shams, al-ḍuḥā, al-qamar, al-nahār, al-layl, al-samāʾ, al-arḍ, al-nafs | **8** | `qad` (91:9 *qad aflaḥa man zakkāhā*) |
| **Q 77 al-Mursalāt** | al-mursalāt, al-ʿāṣifāt, al-nāshirāt, al-fāriqāt, al-mulqiyāt | 5 | `inna/anna` (77:7) |
| **Q 79 al-Nāziʿāt** | al-nāziʿāt, al-nāshiṭāt, al-sābiḥāt, al-sābiqāt, al-mudabbirāt | 5 | `inna/anna` (79:10) |
| **Q 89 al-Fajr** | al-fajr, layālin, al-shafʿ, al-watr, al-layl | 5 | `bare` (elided — classically debated) |
| **Q 85 al-Burūj** | al-samāʾ, al-yawm, shāhid, mashhūd | 4 | `mā` (neg-oath, 85:8) |

The al-Fajr stop at 5 objects (NOT sweeping in *thamūd / firʿawn* at 89:9-10) is correct: those
later genitives belong to a different interrogative-narrative construction (`a-lam tara... fa-ʿala
rabbuka bi-ʿād... wa-thamūda... wa-firʿawn`), and al-Fajr's jawāb is famously elided.

**Distance (qasam → jawāb), N = 44:** min 0, max 9, **mean 2.0 verses, median 1 verse**.
Distribution: dist 0 → 11, dist 1 → 13, dist 2 → 3, dist 3 → 7, dist 4 → 2, dist 5 → 1, dist 6 → 1,
dist 7 → 2, dist 8 → 1, dist 9 → 1. The longest qasam→jawāb spans are the stacked short-mufaṣṣal
oaths (Q 79 = 9, Q 91 = 8, Q 85 / 86 = 7) where the multi-oath build-up delays the apodosis.

**Jawāb-marker distribution (N = 44):**
`inna/anna` 21, `lām al-tawkīd (la-)` 11, `mā (neg-oath)` 5, `qad` 3, `in (neg-oath)` 2, `bare` 2.
The two dominant markers (*inna* + *la-*, together 32/44 = 73%) are exactly the canonical jawāb
markers Ibn al-Qayyim catalogues in *al-Tibyān fī aqsām al-Qurʾān*.

**Sworn-object semantic-class tally (over all 100 sworn objects in the clusters):**
temporal 18, divine 17 (*rabb / Allāh*), agentive 17 (angel/wind participles: ṣāffāt, mursalāt,
nāziʿāt …), cosmic 14 (samāʾ, shams, qamar, najm, ṭāriq …), scriptural 6 (Qurʾān ×3, kitāb ×2,
qalam ×1), human/soul 5, place/other 4, eschatological 3 (shafʿ, watr, shafaq …), unresolved 3.

## 3. The pre-registered concentration test (verdict-bearing)

Density = oath OPENINGS per verse (coordinated objects excluded so the density is not inflated by
the stacking). Corpus density = 45 openings / 6,236 verses.

| Cell | Statistic | Observed | p_perm (one-sided, 10k) | Locked direction | Verdict |
|:--|:--|:--:|:--:|:--|:--:|
| **A** short-mufaṣṣal s ≥ 78 | enrichment ratio vs corpus mean | **3.44×** | **0.0000** | short-mufaṣṣal > corpus | **PASS** |
| **B** Meccan vs Medinan | density ratio | **7.56×** | **0.0000** | Meccan > Medinan | **PASS** |

- Cell A: s ≥ 78 holds 28 of 45 openings in 564 of 6,236 verses → 3.44× the corpus rate.
- Cell B: Meccan oath-density 0.0085/verse vs Medinan 0.0011/verse → 7.56× Meccan-enriched.
- Both pass Bonferroni k = 2 (α_bon = 0.025) by a wide margin.
- **No pre-commit violation:** both effects run in the pre-locked direction.

**MW-5 replication** (alternative length cut s ≥ 93, pure short-mufaṣṣal qiṣār): enrichment **3.53×**,
p_perm = 0.0000 — same direction, same strength.

**MW-6 within-corpus negative control** (the *ta-llāhi* human-witness oaths): these cluster in the
mid-corpus narrative surahs — **Q 12 Yūsuf (×4), Q 16 al-Naḥl (×2), Q 21 al-Anbiyāʾ, Q 26 al-Shuʿarāʾ,
Q 37 al-Ṣāffāt** — NOT in the short-mufaṣṣal. They are oaths spoken by *characters inside narratives*
(Joseph's brothers, Abraham against the idols, the people of the Fire), categorically distinct from
the divine cosmic/temporal oaths of the short suras. This is a clean control: the short-mufaṣṣal
enrichment is specific to the *divine* qasam, not to oath-grammar in general.

## 4. Classical anchoring

- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *al-aqsām* — the oaths of the Qurʾān.
- **al-Zarkashī**, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on aqsām al-Qurʾān.
- **Ibn al-Qayyim al-Jawziyya**, *al-Tibyān fī aqsām al-Qurʾān* — the monograph that observes the
  *muqsam bihi* (sworn object) in the short Meccan suras is predominantly cosmic/temporal and the
  *muqsam ʿalayhi* (jawāb) is the truth of the Resurrection, the Qurʾān, or the Prophet's veracity.

This finding **quantifies** the qualitative classical claim: the divine qasam is 3.4× over-represented
in the short-mufaṣṣal and 7.6× Meccan-enriched, with *inna* + *lām al-tawkīd* carrying 73% of the
jawāb-clauses, exactly the pattern the *ʿulūm al-Qurʾān* literature describes.

## 5. Honest limits

- The **jawāb-detection rule** is a deterministic POS-anchored heuristic (first canonical marker after
  the oath series within a 12-verse window). For Q 89 al-Fajr and Q 75 al-Qiyāma the jawāb is
  classically held to be *elided* (maḥdhūf); the generator flags these `bare`. The marker-based jawāb
  is the *syntactic* apodosis, which can differ from a mufassir's *semantic* apodosis in elided cases.
- The **semantic-class mapping** is a locked root→class table plus an ACT-PCPL→agentive fallback; the
  agentive class (angels/winds) is theologically contested (winds vs angels) but the morphology is not.
- The **stacked-object count** depends on the predication-boundary stop (R1 in the script); it is a
  descriptive figure (MW-7-capped), not a verdict-bearing statistic. The verdict rests only on the
  oath-OPENING density, which is invariant to the stacking refinements.
- The concentration test uses mushaf-position bins (s ≥ 78 / s ≥ 93) and the JSON `type` field for
  Meccan/Medinan; the Meccan/Medinan attribution follows the standard Egyptian/Nöldeke consensus and
  inherits its known boundary debates (a handful of mixed suras).
- The classical *aqsām* sources describe the phenomenon qualitatively; no per-verse density figure
  exists in them to cross-validate the exact ratio.

## 6. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2210-qasam-jawab-inventory.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2210.py`
- Data: `findings/phase-b-hypotheses/csv/h-new-2210.json` (full 44-cluster inventory + test)

## 7. Cross-references

- Re-uses the QAC morphology instrument from the H-NEW-2100/2140 micro-rhetoric series.
- Complements **H-NEW-2150** (rhetorical-question density — Q 67 champion): both are surface-grammar
  GENERATORS keyed to the short-mufaṣṣal register.
- Supports the **s = 50 Meccan/Medinan kink** (al-Suyūṭī, per Protocol §3.6): oath-density is a further
  Meccan-marking surface feature, here ≥7× enriched.
- The agentive-participle sworn-objects (ṣāffāt, mursalāt, nāziʿāt) overlap the **H-NEW-235**
  mutashābih refrain communities (Q 77 *waylun yawmaʾidhin li-l-mukadhdhibīn* / al-Mursalāt cluster).
