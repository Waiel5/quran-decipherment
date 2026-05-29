---
finding_id: H-NEW-2230
title: "QAC-lemma re-run of the numerical-symmetry series (homograph-disambiguated)"
type: pre-registration
genre: numerical-word-balance (Nawfal / Jarrār / al-Kuḥayl) + kallā distribution
date: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260529
phase: B
status: PRE-REGISTERED (direction-locked before recomputation)
closes: "MASTER-FINDINGS-LEDGER §10.80.3 open follow-up"
---

# H-NEW-2230 — Pre-Registration: QAC-Lemma Re-Run of the Numerical-Symmetry Series

## 0. Why this exists (the kallā lesson)

The H-NEW-2160 *kallā* audit (MASTER-FINDINGS-LEDGER §10.80) proved that **raw
substring counting LIES**: the consonantal skeleton `كلا` is a homograph spanning
two unrelated lemmas — the rebuke particle *kallā* (POS:AVR, LEM `kal~aA`) and the
quantifier *kullan* "each" (POS:N, LEM `kul~`). A raw substring count returned 38
across both halves of the muṣḥaf, *apparently* falsifying al-Dānī's claim of 33
rebuke-*kallā* all in the second half. The QAC lemma + part-of-speech annotation
(Dukes 2011) is the disambiguated gold-standard.

The §10.80.3 open follow-up explicitly asked: re-run the famous balance claims at
QAC-lemma level (homograph-disambiguated) and resolve the exact rebuke-*kallā* count.
This file is that re-run, pre-registered.

H-NEW-2000 already used QAC-lemma as its rule R3, so several of these counts are
re-confirmations; the **novelty** here is (a) doing every balance claim under
explicitly-stated lemma rules-tuples with the homograph caveat foregrounded, (b)
adding the within-lemma morphological disambiguation for `A^xir` (the Hereafter-noun
tā-marbūṭa subset vs the adjectival ākhir), and (c) the exact per-token kallā
disambiguation against the QAC POS:AVR tag.

## 1. The two pre-committed rules-tuples

All claims are counted under **two explicitly-stated lemma rules**, both on
`data/morphology/quranic-corpus-morphology-0.4.txt` (QAC v0.4):

- **R-lemma-strict**: exact QAC `LEM` field equality, STEM tokens only. The
  linguistically-principled, homograph-disambiguated count. This is the gold-standard.
- **R-lemma-all-clitics**: the same lemma, but additionally aggregating every
  proclitic/inflected surface realisation that QAC files under that one lemma
  (R-lemma-strict already does this, since QAC lemma membership is clitic-invariant;
  R-lemma-all-clitics therefore = R-lemma-strict for any single lemma, and the rule
  only *differs* when a claim's semantic target is split across **multiple** QAC
  lemmas or requires a **within-lemma morphological subset**, e.g. the Hereafter-noun
  tā-marbūṭa subset of `A^xir`). Where the two rules diverge, both numbers are
  reported side by side. This makes the rule-fragility explicit rather than hidden.

For `A^xir` specifically, a third **within-lemma** disambiguation is reported:
- **R-lemma-fem-noun**: the subset of QAC lemma `A^xir` whose surface form carries
  the feminine tā-marbūṭa (`'aAxirap*`), i.e. the eschatological noun *al-ākhira*
  "the Hereafter", as opposed to the masculine adjective *ākhir* "last/latter".

Counting unit = QAC token. Reading = Hafs-Kūfan. Basmala = counted only in Q1
(QAC files the Q1:1 basmala; other surah-openers are not separate verses).

## 2. The seven claims (target values from the literature)

Target-value source: `data/literature/nawfal/funci-miracle-of-numbers-in-quran.md`
(Nawfal / Jarrār / al-Kuḥayl digest) and, for (7), al-Suyūṭī *al-Itqān* nawʿ 40
citing al-Dānī *al-Muktafā*.

1. **al-dunyā = al-ākhira** — claimed 115 = 115.
2. **al-ḥayāt = al-mawt** — claimed 145 = 145.
3. **al-malāʾika = al-shayāṭīn** — claimed 88 = 88.
4. **al-rajul = al-marʾa** — claimed 24 = 24.
5. **calendar: shahr / yawm / ayyām** — claimed 12 / 365 / 30.
6. **Iblīs = istiʿādha (seek-refuge)** — claimed 11 = 11.
7. **kallā rebuke-lemma** — claimed exactly 33 (al-Dānī), all in the second half.

## 3. Pre-committed lemma keys (QAC v0.4)

| Target | QAC LEM (R-lemma-strict) |
|:--|:--|
| dunyā | `d~unoyaA` |
| ākhira (Hereafter-noun) | `A^xir` ∩ tā-marbūṭa subset (R-lemma-fem-noun) |
| ākhira (whole lemma) | `A^xir` (includes adjectival ākhir) |
| ākhar "other" | `A^xar` (reported, NOT part of ākhira) |
| ḥayāt (noun) | `Hayaw\`p` |
| mawt (noun) | `mawot` |
| malak (angel) | `malak` |
| shayṭān (devil) | `$ayoTa\`n` |
| rajul (man, sing) | `rajul` |
| imraʾa (woman/wife) | `{mora>at` |
| shahr (month) | `$ahor` (split sing/dual/plural by FEATURES) |
| yawm (day) | `yawom` (split sing/dual/plural by FEATURES) |
| Iblīs | `<iboliys` |
| refuge root ʿ-w-dh | ROOT `Ew*` (verbs by lemma) |
| kallā rebuke | POS:AVR ∧ LEM `kal~aA` |
| kullan quantifier (homograph) | LEM `kul~` (the 5 first-half كلا tokens) |

## 4. DIRECTION-LOCKED PREDICTION (locked BEFORE recomputation)

**Primary direction (LOCKED):** QAC-lemma disambiguation does **NOT** rescue the
antonym-balance symmetries. Numerology stays retired. Concretely:

> **≤ 1 of the 6 balance claims (1–6) confirms EXACTLY at R-lemma-strict.**

Rationale: H-NEW-2000 already showed 0/10 confirm under principled rules; the lemma
is the most principled rule and is expected to *retire*, not rescue, the symmetries.
The single-lexeme corpus facts (dunyā = 115, shahr-sing = 12, ayyām = 30, Iblīs = 11)
will re-confirm — but those are not *symmetries*, they are one-sided facts. The
*paired balances* (dunyā=ākhira at strict, ḥayāt=mawt, malāʾika=shayāṭīn as glossed,
rajul=marʾa, yawm=365, refuge=11) are predicted to FAIL or hold only as conflation
artifacts at R-lemma-strict.

**Specific per-claim direction locks:**
- (1) dunyā=ākhira: R-lemma-strict will NOT balance (ākhira whole-lemma `A^xir` ≫ 115
  because it includes adjectival ākhir). A within-lemma morphological subset
  (R-lemma-fem-noun) may recover 115=115 — if so, that is RULES-FRAGILE (rescued
  only by a within-lemma rule), reported honestly, not CONFIRMED-clean.
- (2) ḥayāt=mawt: FALSIFIED (no rule hits 145; nouns 76 vs 50 predicted).
- (3) malāʾika=shayāṭīn: whole-lemma may equal 88=88, but this is a conflation
  artifact (plural malāʾika ≠ plural shayāṭīn) → RULES-FRAGILE, not CONFIRMED.
- (4) rajul=marʾa: FALSIFIED (predicted 29 vs 26, neither = 24).
- (5) calendar: shahr-sing = 12 ✓ and ayyām+dual = 30 ✓ are facts; yawm-sing ≠ 365
  (predicted ~375) → RULES-FRAGILE (2 of 3).
- (6) Iblīs = 11 ✓ fact; refuge has no natural 11 → RULES-FRAGILE.

**Counting confirms: at most claim (5)'s two sub-facts and the one-sided lexeme facts;
no PAIRED antonym balance confirms cleanly at R-lemma-strict.** I therefore predict
**0 of 6 balance claims CONFIRMED-clean at lemma-strict** (the ≤1 bound gives one
unit of slack in case the malāʾika/shayāṭīn whole-lemma 88=88 is scored as a clean
confirm rather than a conflation artifact).

**kallā (claim 7) direction lock:** rebuke-lemma (POS:AVR, LEM `kal~aA`) = **33
EXACTLY**, all attestations in surahs ≥ 19 (the second half / mufaṣṭal), confirming
al-Dānī. The 5 first-half كلا substring tokens (Q 4:130, 6:84, 7:46, 11:111, 17:20)
are predicted to be the quantifier `kul~` (POS:N), NOT the rebuke.

## 5. Bidirectional honesty clause

If QAC-lemma disambiguation RESCUES **more** than predicted (i.e. ≥ 2 balance claims
confirm cleanly at R-lemma-strict), that is published with full prominence as
evidence of **bidirectional rules-tuple sensitivity** — disambiguation can rescue OR
retire (project memory `feedback_rules_tuple_bidirectional`). A pre-commit violation
of the locked direction is published as such, never massaged.

## 6. Verdict vocabulary (per claim)

- **CONFIRMED** — claimed balance/value holds EXACTLY at R-lemma-strict (the
  principled, homograph-disambiguated rule), with no selective subset.
- **RULES-FRAGILE** — holds only under a within-lemma morphological subset or a
  multi-lemma aggregation, or holds at one lemma rule while breaking at a neighbour.
- **FALSIFIED** — no defensible lemma rule recovers the claim.
- **CONFIRMED-BUT-MEANINGLESS** — a number lands exactly but it is a one-sided
  single-lexeme corpus fact, not the claimed symmetry/astronomical match.

## 7. Success / failure criteria

- The pre-reg SHA-256 is embedded in `scripts/h-new-2230.py` and verified at runtime;
  mismatch = fail-fast.
- The locked direction (≤1 of 6 balance claims CONFIRMED-clean at lemma-strict) is
  evaluated against the computed verdicts. Confirmation of the direction strengthens
  the numerology-retired conclusion; violation is published as a rescue.
- kallā = 33 (POS:AVR) is a hard binary: confirm or deny, with per-token
  disambiguation of all 38 substring tokens.

## 8. Files

- pre-reg: this file.
- script: `findings/phase-b-hypotheses/scripts/h-new-2230.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2230.json`
- finding: `findings/phase-b-hypotheses/h-new-2230-qac-lemma-numerical-rerun.md`
- data: `data/morphology/quranic-corpus-morphology-0.4.txt`,
  `quran-text/quran-no-tashkeel.json`

*Direction locked 2026-05-29 by Waiel Al-Shujaa, before recomputation.
Bismillāhi al-Raḥmāni al-Raḥīm.*
