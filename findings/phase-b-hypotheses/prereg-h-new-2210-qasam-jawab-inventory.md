---
id: H-NEW-2210
title: Qasam / jawāb al-qasam structural inventory + oath-density concentration test
type: pre-registration
date: 2026-05-29
author: Waiel Al-Shujaa
phase: B
status: LOCKED-BEFORE-COMPUTE
seed: 20260509
---

# H-NEW-2210 — Qasam / Jawāb al-Qasam Structural Inventory (PRE-REGISTRATION)

## 0. One-line statement

Build an exhaustive morphology-grounded GENERATOR cataloguing every Quranic **oath-opening** (qasam) — the
oath-wāw (*wāw al-qasam*) + sworn-object, plus the rarer *(lā) uqsimu* form and the *ta-llāhi* form — identify
the **jawāb al-qasam** (response/apodosis) for each, and enumerate corpus-wide the qasam→jawāb verse-distance,
the number of stacked oaths before each jawāb, and the sworn-object semantic class
(cosmic / temporal / scriptural / divine / human-witness).

Then run a **direction-locked** confirmatory test of the classical observation (al-Suyūṭī *al-Itqān* nawʿ
al-aqsām; al-Zarkashī *al-Burhān*; Ibn al-Qayyim *al-Tibyān fī aqsām al-Qurʾān*) that oath-clusters
**concentrate in the early-Meccan short-mufaṣṣal**.

## 1. Data sources (all on disk)

- `data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4) — **primary instrument**. The oath-wāw is
  POS-tagged `PREFIX|w:P+` (preposition-wāw = *wāw al-qasam*), distinct from `w:CONJ` (conjunction-wāw),
  `w:REM` (resumption), `w:CIRC` (circumstantial), `w:SUP`, `w:COM`. The *uqsimu* verb is `LEM:>aqosamu|ROOT:qsm`
  form IV imperfect 1S. The *ta-llāhi* oath particle is `PREFIX|ta+` (POS P). **This is the load-bearing
  separation the substring-method cannot do** — raw `wa-` substring conflates ~8500 conjunction-wāws with the
  28 oath-wāws.
- `quran-text/quran-no-tashkeel.json` — verse text + Meccan/Medinan `type` + verse counts.
- `quran-text/quran-min-tashkeel.json` — cross-check of the oath-particle wāw vs vocative-wāw.
- `data/hafs-verse-counts.tsv` — verse counts per surah.
- `data/revelation-order.csv` — Nöldeke chronology / period for the Meccan>Medinan comparison.

## 2. Definitions (rules-tuple)

Default tuple: `(no-tashkeel, orthographic-token, QAC-morphology-POS, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`.

- **Qasam (oath-opening)** = any token QAC-tagged `PREFIX|w:P+` (oath-wāw) OR a *(lā) uqsimu* verb
  (`LEM:>aqosamu` form-IV 1S) OR a `PREFIX|ta+` oath particle. These three are the morphologically-defined
  oath-introducers. The **sworn-object** is the immediately governed genitive noun phrase.
- **Stacked oaths** = a maximal run of consecutive oath-introducers (each governing its own object) that share
  a single jawāb. Counted per opening-cluster.
- **Jawāb al-qasam (apodosis)** = the response clause. Detection rule (locked): the first clause after the
  final sworn-object of the cluster that opens with one of the canonical jawāb markers —
  `inna`/`anna` (ACC particle `<in~`/`>an~`), the *lām al-tawkīd* `la-` (EMPH prefix `l:EMPH`),
  `qad`, the negative-oath `in` / `mā`, or a bare verbal/nominal predicate when no marker is present
  (flagged `bare`). The jawāb verse is the verse-id where the marker first appears.
- **qasam→jawāb verse-distance** = (jawāb verse-id) − (first oath verse-id) within the surah, in verses.
- **Semantic class of sworn-object** (assigned from QAC root + lemma, locked mapping):
  - `cosmic` (roots: smw sky, njm star, qmr moon, $ms sun, smw heaven, ...),
  - `temporal` (fjr dawn, ESr time/afternoon, DHw forenoon, lyl night, ywm day),
  - `scriptural` (qrA Qurʾān, ktb Book, qlm pen),
  - `divine` (Alh Allāh, rbb Rabb),
  - `agentive/eschatological` (Sff ranks, rsl sent-ones, nzE pluckers, Edw chargers, ...),
  - `place/other` (bld town, tyn fig, $rq/grb easts/wests, balad).

## 3. Hypothesis + LOCKED DIRECTION (pre-committed before any compute)

**H-2210-MAIN.** Oath-introducers concentrate in the early-Meccan short-mufaṣṣal.

Two pre-locked one-sided sub-tests (Bonferroni family k = 2, α_bon = 0.025):

- **CELL A — length-bin direction (LOCKED):** oath-introducer **density per verse** in the
  **short-mufaṣṣal block (mushaf surahs s ≥ 78)** is **GREATER** than the corpus per-verse mean.
  Locked direction: short-mufaṣṣal > corpus mean. Statistic: ρ_A = (oaths in s≥78)/(verses in s≥78) ÷
  (total oaths)/(total verses) — observed enrichment ratio.
- **CELL B — Meccan>Medinan direction (LOCKED):** oath-introducer density per verse is **GREATER** in
  Meccan surahs than in Medinan surahs. Locked direction: Meccan > Medinan.

**Reversed direction → published NULL with full prominence** (pre-commit violation flag). If
short-mufaṣṣal density ≤ corpus mean, or Medinan ≥ Meccan, that cell is NULL.

## 4. Null model

- **Permutation null (MW-2):** randomly relabel which surahs are "short-mufaṣṣal" (Cell A) / "Meccan"
  (Cell B) by permuting the surah→bin assignment 10,000 times, holding the per-surah oath counts and
  verse counts fixed (i.e., shuffle the bin labels across the 114 surahs). For each permutation recompute
  the enrichment ratio / Meccan-vs-Medinan density ratio. seed = **20260509**.
- p_perm (one-sided, locked direction) = fraction of permutations with statistic ≥ observed.
- Report raw + Bonferroni-corrected (k=2, α_bon = 0.025).

## 5. Verdict rule

- **CONFIRMED**: both cells one-sided p_perm < 0.025 in the LOCKED direction, and replication (MW-5) holds.
- **DIRECTIONAL**: one cell passes, the other does not, both in pre-locked direction (no reversal).
- **NULL**: neither cell passes.
- **Pre-commit VIOLATION → NULL-with-prominence**: any cell's effect runs OPPOSITE the locked direction.
- **CONFIRMED-BUT-MEANINGLESS**: passes but is the independence/structurally-forced expectation.

## 6. MW protections

- MW-1 (instrument): oath defined by QAC POS-tag `w:P+`/`ta+`/`uqsimu` BEFORE compute (this file).
- MW-2: 10,000-perm null.
- MW-3 (alt-models): two binning schemes — (a) s≥78 short-mufaṣṣal cut; (b) Meccan/Medinan. Plus a
  robustness cut at s≥93 (pure short-mufaṣṣal qiṣār) reported descriptively.
- MW-5 (replication): re-run Cell A with an alternative length-cut (s≥93) and confirm same direction.
- MW-6 (control): the `ta-llāhi` human-witness oaths (in Yūsuf, Anbiyāʾ, Naḥl, Shuʿarāʾ narratives) should
  NOT concentrate in the short-mufaṣṣal — they are a within-corpus negative control. Report their distribution.
- MW-7: the inventory itself is descriptive (no p-value); only the concentration test carries the verdict.

## 7. Outputs

- `findings/phase-b-hypotheses/scripts/h-new-2210.py` (embeds this file's SHA-256, verifies at runtime)
- `findings/phase-b-hypotheses/csv/h-new-2210.json` (full inventory + test results)
- `findings/phase-b-hypotheses/h-new-2210-qasam-jawab-inventory.md` (findings)

## 8. Classical anchor

- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on *al-aqsām* (the oaths of the Qurʾān).
- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on aqsām al-Qurʾān.
- Ibn al-Qayyim al-Jawziyya, *al-Tibyān fī aqsām al-Qurʾān* (al-Tibyān fī aymān al-Qurʾān) — the
  monograph-length treatment; observes that the *muqsam bihi* (sworn object) in the short Meccan suras
  is predominantly cosmic/temporal, and the *muqsam ʿalayhi* (jawāb) is the truth of the Resurrection,
  the Qurʾān, or the Prophet's veracity.

Honest note: the classical sources qualitatively describe oath-clustering in the muqaṣṣar Meccan suras;
they do NOT give per-verse densities. This test quantifies the qualitative claim. NULL is a real possible
outcome and will be published with equal prominence.
