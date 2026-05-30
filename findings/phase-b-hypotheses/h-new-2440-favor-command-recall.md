---
finding: H-NEW-2440
title: Favor→Command lexical-recall census — the device is real but its signature is LOCAL CO-LOCATION, not directional ordering
type: pre-registered census + null test
date: 2026-05-30
author: Waiel Al-Shujaa
seed: 20260509
seed_repl: 20260601
nperm: 10000
prereg_sha256: f4595836546c879f4c9c74628e0bbf4e2776b67c34a3745710978f6219421015
verdict: CONFIRMED (locked H1) + REFINED (mechanism = co-location, not direction)
rules_tuple: (no-tashkeel, QAC-root+POS/aspect/mood, segment-level, basmala-not-counted, Hafs-Kūfan, Mashriqi)
---

# H-NEW-2440 — Favor→Command Lexical-Recall Census

## Seed

Q093-F-01 Arm B (§10.116): in al-Ḍuḥā the root **ytm** "orphan" uniquely bridges the
favor-block (v6 *a-lam yajidka yatīman fa-āwā* — "did He not find you an orphan and
shelter [you]") and the command-block (v9 *fa-ammā l-yatīma fa-lā taqhar* — "so as for the
orphan, do not oppress"). Ibn Kathīr maps v6↔9 / v7↔10 / v8↔11, yet **only the orphan
pair is lexically realised**. This file asks whether that bridge is one instance of a
general, above-chance corpus device.

## Method (locked, SHA `f459583654…421015`, runtime-verified)

A GENERATOR over QAC v0.4 flags every verse as a **favor verse** (contains a past-tense
divine-favor verb: `PERF`, non-`PASS`, divine person 1S/1P/3MS/3MP, root ∈ a locked
28-root *taʿdīd al-niʿam* lexicon — wjd, Aty, nEm, hdy, jEl, xlq, rzq, nzl, …) and/or a
**command verse** (an imperative `IMPV`, or the prohibitive *lā al-nāhiya* = `POS:PRO` +
`IMPF MOOD:JUS` 2nd-person, e.g. *lā taqhar*). A **recall pair** is a content root R that
appears in an earlier favor verse V_f and re-appears in a later command verse V_c within
the same surah, with 0 < (V_c − V_f) ≤ W. **Primary statistic = corpus total recall-pair
tuples (R,V_f,V_c), W=8.** **Null = within-surah verse-order shuffle** (each verse keeps its
exact contents; only the order is scrambled), 10,000 perms, seed 20260509. Direction
**LOCKED**: observed > null.

## Result — the locked test PASSES, no pre-commit violation

| quantity | value |
|---|---:|
| favor verses (corpus) | **884** |
| command verses (corpus) | **1,400** |
| recall-pair tuples, W=8 | **1,584** |
| distinct (surah, root) recall-events | **645** |
| null mean (shuffle) | 1,343.9 (sd 45.2) |
| **z** | **+5.316** |
| **p (one-sided, locked)** | **0.00010** |
| direction_ok | **True** (observed > null) |
| replication (seed 20260601) | null mean 1,344.8, p = 0.00010 ✓ |
| **validity check: al-Ḍuḥā ytm v6→v9 present** | **TRUE** ✓ |

The locked one-sided hypothesis — *favor roots re-surface in later commands within a
surah more than a verse-order shuffle* — is **CONFIRMED at z=+5.3, replicated**, and the
operationalisation captures its own seed exactly (al-Ḍuḥā *ytm* v6→v9, favor-verb *Awy*
"sheltered" → prohibition *qhr* "oppress").

### MW-3 window robustness — the effect is LOCAL
| window W | observed | null mean | z | p |
|---|---:|---:|---:|---:|
| **4 (tight pericope)** | 872 | 691.3 | **+5.52** | 0.0001 |
| **8 (primary)** | 1,584 | 1,343.9 | **+5.32** | 0.0001 |
| **∞ (whole-surah)** | 12,807 | 12,259.9 | +1.23 | 0.108 |

The signal is **strongest at the tightest pericope window and collapses to non-significance
when the window is the whole surah** — exactly the profile of a *pericope-internal* device
(favor and command roots co-occur at short range), not a long-range one. This corroborates
the project's recurring law that **cohesion is densest at the finest scale**
([[h-new-2420-within-surah-nazm|H-NEW-2420]], cross-finding-025/026).

## The honest refinement — MW-6 reverse control: co-location, NOT direction

The instrument-control computes the **reverse** statistic (a favor root recalled in a
command verse that comes *before* it — command→favor):

| | observed | z vs own shuffle-null |
|---|---:|---:|
| forward (favor→command) | 1,584 | **+5.32** |
| reverse (command→favor) | 1,582 | **+5.24** |
| forward − reverse | **+2** | ≈ 0σ |

**The reverse direction beats the shuffle just as strongly as the forward direction.**
What the canonical order does is **co-locate favor verses and command verses sharing a
root within short windows far more than chance** — but it does **not** privilege
favor-*before*-command over command-*before*-favor. The directional arrow that the
al-Ḍuḥā showcase suggests is, corpus-wide, **symmetric**: the device is *local lexical
co-location of grace-talk and command-talk*, not an ordered favor→command recall.

This is a methodological refinement, **not a pre-commit violation**: the locked direction
was "observed > null" and that held (z=+5.3). The reverse control — a separate, non-verdict
diagnostic — shows the *mechanism* is co-location. The al-Ḍuḥā v6→v9 arrow is real and
beautifully directional in that surah, but it is a **hand-readable instance of a
symmetric co-location regularity**, the same lesson as the Q83 sijjīn/ʿilliyyīn and Q92
giver/miser showcases (a vivid single-surah case sitting on a corpus-wide regularity whose
*generic* form is less pointed than the showcase).

## The roster (H2)

- **1,584 recall tuples / 645 distinct (surah, root) events** across the corpus.
- **Gap distribution** (favor→command verse distance) decays monotonically:
  gap 1 = 262, gap 2 = 215, gap 3 = 188 … gap 8 = 167 — most recalls are within 1–3 verses,
  confirming the short-range / pericope character.
- **Top recalled roots:** Alh (459, the divine name — see caveat), then Elm "knowledge/teaching"
  (82), Amn "faith" (69), **rbb "Lord" (65)**, **Aty "give" (54)**, ArD "earth" (38),
  qwm "people/stand" (36).
- **Most-commanded verbs in recall verses:** qwl "say" (290), **wqy "guard/fear (God)" (82)**,
  *kr "remember" (68), Aty "give" (65), Ebd "worship" (30) — the recall device feeds the
  core imperatives *qul, ittaqū, udhkurū, ātū, uʿbudū*.
- **Top surahs:** Q2 al-Baqara (346), Q6 al-Anʿām (139), Q5 al-Māʾida (127), Q4 al-Nisāʾ
  (112), Q7 al-Aʿrāf (101) — the long Medinan/legal surahs where *niʿma*-recollection
  precedes legislation (the Banī-Isrāʾīl *udhkurū niʿmatī … wa-awfū* register).

### Showcase pairs (the al-Ḍuḥā family)
- **Q93 al-Ḍuḥā — ytm v6→v9** (favor *āwā* → prohibition *lā taqhar*): the seed. ✓
- **Q96 al-ʿAlaq — qrA v1→v3 and rbb v1→v3** (favor frame *iqraʾ bi-smi rabbika lladhī
  khalaqa* → command *iqraʾ*): the recitation-imperative recalls the recitation-frame and
  the Lord-who-created. The *first revelation*'s opening is itself a favor(create)→command(recite)
  recall.
- The long-surah bulk is the Medinan *udhkurū niʿmata Llāh … (then) command* formula.

### Caveat on the divine name
The root **Alh** (Allāh) supplies **29.0%** of all tuples (459/1,584). Per the locked pre-reg
it is a content PN, NOT a stop-root, so it is counted — but flagged: it recurs in nearly
every favor *and* command verse, so it inflates co-location trivially. **Excluding Alh**, the
device still yields **1,125 tuples / 606 distinct (surah,root) events**, with the same
top-content roots (Elm, Amn, rbb, Aty) — the substantive recall structure is robust to
dropping the divine name.

## Classical anchoring

The device is the empirical face of the *taʿdīd al-niʿam → takālīf* (enumeration of favors
then obligations) homiletic structure that the mufassirūn read throughout the Medinan
*khiṭāb*: al-Rāzī and al-Zamakhsharī on Q2:40–47 (*yā banī Isrāʾīla dhkurū niʿmatiya …
wa-awfū bi-ʿahdī*) read the command (*awfū*) as answering the recalled favor (*niʿma*); Ibn
Kathīr's v6↔9/v7↔10/v8↔11 al-Ḍuḥā mapping is the showcase. The corpus test confirms the
**co-location** is real and above chance, while refining the *directional* reading: the
Quran clusters grace-talk and command-talk in the same pericope, but does not impose a
strict grace-then-command word order at the root level.

## Verdict

**CONFIRMED (locked H1) + REFINED.** Favor roots and command roots co-occur within short
within-surah windows far more than a verse-shuffle null (z=+5.3, p=1×10⁻⁴, replicated,
W-local, validity-check ✓, robust to dropping the divine name). The locked direction held —
**no pre-commit violation.** The MW-6 reverse control refines the *mechanism*: the
regularity is **local lexical co-location of favor and command verses**, **symmetric in
order** (forward 1,584 ≈ reverse 1,582), not the directional favor→command arrow the
al-Ḍuḥā seed suggests. al-Ḍuḥā *ytm* and al-ʿAlaq *qrA/rbb* are genuine, vivid
single-surah instances of this symmetric co-location law.

## Honest limits

- **Direction not established.** The headline "favor→command recall" arrow is a
  surah-readable feature, not a corpus-directional one; the test demonstrates co-location,
  and (deliberately) reports the reverse control rather than hiding it.
- **Lexicon-bounded.** The 28-root favor lexicon is principled but finite; a different
  benefaction-verb set could shift counts (it would not flip the co-location sign — the
  effect is large).
- **Divine-name inflation** (29%) is reported and shown non-load-bearing.
- **Co-location ≠ rhetorical intent.** That favor and command roots cluster does not prove
  each command was *composed to* recall a specific favor; the seed shows it happens, the
  corpus shows it happens more than chance, the direction-symmetry shows the generic case
  is weaker than the showcase.

## Files
- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2440-favor-command-recall.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2440.py`
- data: `findings/phase-b-hypotheses/csv/h-new-2440.json`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
