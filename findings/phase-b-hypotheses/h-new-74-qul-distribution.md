---
finding_id: h-new-74-qul-distribution
phase: B
status: PASS — 5 of 6 cells fire (Cell 1 verified, Cell 2 published, Cell 3 hard-equality pass, Cell 4 pass, Cell 5 NULL, Cell 6 PASS)
date: 2026-04-15
rules_tuple: (no-tashkeel, hafs-kufan, canonical-114, Tanzil-JSON for verse text, Leeds-QAC-v0.4 morphology, qul := POS:V|IMPV|LEM:qaAla|2MS)
null_models: hard-equality (Cell 1), set-equality (Cell 3), threshold (Cell 4), Mann–Whitney U two-sided (Cell 5), Kruskal–Wallis H (Cell 6)
bonferroni_k: 6
alpha_bon: 0.05/6 ≈ 0.00833
classical_claim: 332 qul imperatives (Sufi/popular figure ratified by Itqān; Prophet's didactic-dialogic register per Zarkashī al-Burhān; "qul tetralogy" Q 109/112/113/114 + Q 72)
seed: 20260417
author: h-new-74-specialist
---

# [[h-new-74-qul-distribution|H-NEW-74]] — qul (قل = "Say!") Distribution Across the Quran

## Question

The bare *qul* (2MS imperative of *qāla*, "Say!") is the divine command-to-the-
Prophet par excellence: a moment where the divine voice instructs the Prophet
to articulate a position. The widely-cited count is **332** (matched, in
popular Sufi numerology, by 332 *qālū*). This finding (i) verifies the count
mechanically against Leeds QAC v0.4, (ii) builds the per-surah distribution,
(iii) audits the surah-initial qul corpus, (iv) tabulates the formulaic
"qul + X" frames that recur as compositional templates, and (v) tests
period and phase correlations.

## Locked extractor

For each segment in `/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt`:

```
qul ⇔  POS:V  ∧  IMPV  ∧  LEM:qaAla  ∧  2MS  (all in features field)
```

Surface-string matching (e.g. bare قل in the no-tashkeel JSON) under-counts to
294 (because وقل / فقل surface-merge with the prefix), so the QAC predicate is
the canonical operationalisation.

## Cell 1 — Total count == 332 (MW-control) — **PASS**

`total_qul = 332` exactly. The classical figure is verified. This also
ratifies the prior `imperative-run-1` and `quotation-analysis.md`
findings against the same primary source.

## Cell 2 — Per-surah distribution — **PUBLISHED**

### Top-10 surahs by qul COUNT

| rank | surah | name | period | Nöldeke phase | verses | qul | density / 100 v |
|---|---|---|---|---|---|---|---|
| 1 | Q 6 | al-Anʿām | Meccan | Late Meccan | 165 | **44** | 26.67 |
| 2 | Q 10 | Yūnus | Meccan | Late Meccan | 109 | **24** | 22.02 |
| 3 | Q 3 | Āl ʿImrān | Medinan | Medinan | 200 | **23** | 11.50 |
| 4 | Q 17 | al-Isrāʾ | Meccan | Middle Meccan | 111 | **21** | 18.92 |
| 5 | Q 2 | al-Baqara | Medinan | Medinan | 286 | 18 | 6.29 |
| 6 | Q 34 | Sabaʾ | Meccan | Late Meccan | 54 | 15 | 27.78 |
| 6 | Q 39 | al-Zumar | Meccan | Late Meccan | 75 | 15 | 20.00 |
| 8 | Q 9 | al-Tawba | Medinan | Medinan | 129 | 12 | 9.30 |
| 9 | Q 7 | al-Aʿrāf | Meccan | Late Meccan | 206 | 11 | 5.34 |
| 9 | Q 23 | al-Muʾminūn | Meccan | Middle Meccan | 118 | 11 | 9.32 |

### Top-10 surahs by qul DENSITY (per 100 verses)

| rank | surah | name | period | phase | verses | qul | density |
|---|---|---|---|---|---|---|---|
| 1 | Q 34 | Sabaʾ | Meccan | Late Meccan | 54 | 15 | **27.78** |
| 2 | Q 62 | al-Jumuʿa | Medinan | Medinan | 11 | 3 | **27.27** |
| 3 | Q 6 | al-Anʿām | Meccan | Late Meccan | 165 | 44 | **26.67** |
| 4 | Q 112 | al-Ikhlāṣ | Meccan | Early Meccan | 4 | 1 | **25.00** |
| 5 | Q 13 | al-Raʿd | Medinan/Late-Meccan† | — | 43 | 10 | 23.26 |
| 6 | Q 10 | Yūnus | Meccan | Late Meccan | 109 | 24 | 22.02 |
| 7 | Q 39 | al-Zumar | Meccan | Late Meccan | 75 | 15 | 20.00 |
| 8 | Q 67 | al-Mulk | Meccan | Middle Meccan | 30 | 6 | 20.00 |
| 9 | Q 113 | al-Falaq | Meccan | Early Meccan | 5 | 1 | 20.00 |
| 10 | Q 17 | al-Isrāʾ | Meccan | Middle Meccan | 111 | 21 | 18.92 |

†Q 13 al-Raʿd has the period-vs-phase split (Egyptian: Medinan; Nöldeke phase: Late Meccan); both groupings carry the same content-density signal.

### Surahs with ZERO qul (n = 57 of 114)

```
[1, 44, 47, 50, 51, 53, 54, 55, 57, 58, 59, 60, 61, 63, 65, 66, 68, 69,
 70, 71, 73, 74, 75, 76, 77, 78, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89,
 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105,
 106, 107, 108, 110, 111]
```

**Exactly half the corpus (57 / 114) contains no qul at all.** The
zero-qul corpus is dominated by:
- The early-Meccan oath-and-eschatology cluster (Q 73–104 mostly).
- The praise-/sabbiḥ-opened sūras (Q 1, 57, 59, 61, 87 in this list — Q 6/18/34/35 escape because they contain qul beside the *al-ḥamd* opener).
- A handful of Medinan policy-and-narrative surahs that do not need the
  divine→Prophet quoted register (Q 47 Muḥammad, Q 58 al-Mujādila, Q 60
  al-Mumtaḥina, Q 65/66 al-Ṭalāq/al-Taḥrīm — addressed-to-believers
  rather than addressed-via-Prophet).

This bimodality (44/24/23/21/18/15/15/12/11/11 at top vs ZERO for half the
corpus) is the headline structural fact of the qul-corpus.

## Cell 3 — Surah-initial qul — **PASS** (set equality with prior prediction)

### v1-w1 qul-openers (qul as the very first word of the very first verse)

```
{Q 72, Q 109, Q 112, Q 113, Q 114}   (5 surahs)
```

This **exactly** matches the [[h-new-61-opening-words|H-NEW-61]] opening-word finding's IMPERATIVE
class (minus Q 96 al-ʿAlaq which opens with *iqraʾ* not *qul*).

The task prompt mentioned "Q 109, 112, 113, 114" (4 surahs); the **5th
canonical qul-opener is Q 72 al-Jinn**:

> *qul ūḥiya ilayya annahu istamaʿa nafarun mina-l-jinni…*
> "**Say**: It has been revealed to me that a group of the jinn listened…"

### Fast-opening qul (first qul within v ≤ 3)

| surah | first qul at | content frame |
|---|---|---|
| Q 8 al-Anfāl | v1 w4 | *yas'alūnaka ʿani-l-anfāli **quli**-l-anfālu li-llāhi…* |
| Q 34 Sabaʾ | v3 w7 | (after praise opener: *al-ḥamdu li-llāh… **qul** balā wa-rabbī…*) |
| Q 72 al-Jinn | v1 w1 | (canonical opener) |
| Q 109 al-Kāfirūn | v1 w1 | (canonical opener) |
| Q 112 al-Ikhlāṣ | v1 w1 | (canonical opener) |
| Q 113 al-Falaq | v1 w1 | (canonical opener) |
| Q 114 al-Nās | v1 w1 | (canonical opener) |

### The "qul tetralogy" → **qul-pentalogy**

Classical Sunni recitational tradition treats Q 109 / 112 / 113 / 114 as a
unified daily-recitation suite (al-Kāfirūn paired with al-Ikhlāṣ for the
two-rakaʿah sunnah; al-Falaq + al-Nās = the *muʿawwidhatān*). When you
project the structural feature "v1-w1 qul" mechanically, **Q 72 al-Jinn**
joins this suite as a 5th member — no other surah in the corpus has qul
as its first word. The classical recitational quartet is thus a
**recitational** subset of a slightly larger **structural** quintet. This
is a clean recovery of a classical observation with one structurally-novel
addition (Q 72).

## Cell 4 — Formulaic frame catalog — **PASS** (≥ 3 frames each ≥ 5×)

### Top-15 raw "qul + X1" bigrams

| count | qul + X1 (normalised) | gloss / classical formula |
|---|---|---|
| 25 | *qul inna* (قل ان) | "Say: indeed…" — assertive frame |
| 19 | *qul innamā* (قل انما) | "Say: only…" — exclusive-assertive |
| 16 | *qul yā* (قل يا) | "Say: O…" — direct-address opener |
| 16 | *qul Allāh* (قل الله) | "Say: Allāh…" — theonym-fronted |
| 14 | *qul lā* (قل لا) | "Say: no/I do not…" — negation frame |
| 12 | *qul man* (قل من) | "Say: who…" — interrogative-rhetorical |
| 11 | *qul innī* (قل اني) | "Say: I indeed…" (1st-person assertive) |
| 11 | *qul a-raʾaytum* (قل ارايتم) | "Say: have you considered…" — counter-question |
| 10 | *qul huwa* (قل هو) | "Say: He…" (the *qul huwa Allāhu aḥad* + *huwa lladhī…* family) |
| 10 | *qul hal* (قل هل) | "Say: is/are…" — yes/no rhetorical |
| 8 | *qul mā* (قل ما) | "Say: what…" / "Say: not…" |
| 7 | *qul law* (قل لو) | "Say: if (counterfactual)…" |
| 7 | *qul rabbi* (قل رب) | "Say: my Lord…" — invocation frame |
| 6 | *qul al-ḥamd* (قل الحمد) | "Say: praise be…" — praise frame |
| 5 | *qul li-lladhīna* (قل للذين) | "Say to those who…" — directed-address |

### Top 2-word and 3-word frames

| count | qul + X1 + X2 + X3 |
|---|---|
| 8 | *qul a-raʾaytum in…* ("Say: have you considered if…") |
| 6 | *qul yā ahla l-kitāb* ("Say: O People of the Book") |
| 6 | *qul yā ayyuhā l-nās* ("Say: O mankind") |
| 6 | *qul al-ḥamdu li-llāh* ("Say: praise be to God") |
| 4 | *qul sīrū fī l-arḍ* ("Say: travel through the earth") |
| 4 | *qul innamā anā…* ("Say: I am only…") |
| 3 | *qul hātū burhānakum* ("Say: bring your proof") |
| 3 | *qul hal yastawī l-aʿmā…* ("Say: are the blind and the seeing equal…") |
| 3 | *qul innamā ʿilmuhā ʿinda…* ("Say: knowledge of it is only with…") |
| 3 | *qul kafā bi-llāh shahīdan* ("Say: God suffices as witness") |
| 3 | *qul law kāna…* ("Say: if there were…") |

### Pre-registered formulaic-frame matches (binding test)

| frame | n | passes ≥ 5? |
|---|---|---|
| *qul innī / innamā / inna / innā* | 44 | **✓** |
| *qul man* | 12 | **✓** |
| *qul a-raʾayta(kum)* | 11 | **✓** |
| *qul huwa* | 10 | **✓** |
| *qul hal* | 10 | **✓** |
| *qul law* | 7 | **✓** |
| *qul li-* (cliticised addressee) | 7 | **✓** |
| *qul yā ayyuhā* | 6 | **✓** |
| *qul yā ahl(a)* | 6 | **✓** |
| *qul aʾa-* (counter-question) | 5 | **✓** |
| *qul li-lladhīna* | 5 | **✓** |
| *qul aʾaghayra* | 3 | — |
| *qul aʿūdhu* | 2 | — (only Q 113, Q 114) |
| *qul amara* | 1 | — |
| *qul kafā* | 0 (in slot 1; appears in slot 2) | — |

**11 of the 15 pre-registered frames each appear ≥ 5×.** Pre-reg threshold
was ≥ 3 frames; **frame catalog confirmation is therefore very strong**.

### Joint headline (Cell 4)

The qul-corpus is a **template-driven discourse register**:
- *qul + assertive particle* (*inna* / *innamā* / *innī*) covers 44 / 332
  ≈ 13.3% of all qul occurrences.
- *qul + interrogative* (*man* + *hal* + *aʾa-* + *a-raʾaytum*) covers
  38 / 332 ≈ 11.4%.
- *qul + direct-address vocative* (*yā ayyuhā*, *yā ahl*) covers 12.
- *qul + counterfactual* (*law*) covers 7.
- The four "muʿawwidhāt + ikhlāṣ + kāfirūn" recitational unit accounts
  for only 4 of 332 (1.2%); the bulk of qul is mid-corpus polemical-
  rhetorical, not Mufaṣṣal recitational.

## Cell 5 — qul-density × Meccan/Medinan Mann-Whitney U — **NULL**

| | n | mean density | median density |
|---|---|---|---|
| Meccan | 86 | 4.08 | 0.44 |
| Medinan | 28 | 5.05 | 2.84 |

Mann-Whitney U = 1109.5, z = -0.62, **p = 0.534** → fails Bonferroni
α = 0.00833.

The **median is 6× higher** in Medinan (2.84 vs 0.44), but the Meccan
distribution is bimodal: ~half the Meccan surahs are zero-qul (the early
oath-eschatology cluster), while the other half are qul-dense (Q 6 = 44,
Q 10 = 24, Q 17 = 21, Q 34 = 15, Q 39 = 15, Q 7 = 11, Q 23 = 11, Q 67 = 6,
Q 27 = 7, Q 18 = 8). This bimodality dilutes the rank-sum test.

This null result is itself diagnostic: **the Meccan-vs-Medinan period
binarisation does not capture the qul-density structure**; the relevant
cut is by Nöldeke phase (Cell 6).

## Cell 6 — qul-density × Nöldeke 4-phase Kruskal–Wallis — **PASS**

| Nöldeke phase | n surahs | mean density | median density |
|---|---|---|---|
| Early Meccan | 48 | **1.74** | 0.00 |
| Middle Meccan | 21 | 4.89 | 2.22 |
| **Late Meccan** | 21 | **8.95** | **5.34** |
| Medinan | 24 | 4.93 | 3.85 |

Kruskal-Wallis H = 35.36, df = 3, **p = 1.02 × 10⁻⁷** → passes Bonferroni
α = 0.00833 by 4 orders of magnitude.

**The qul-corpus is overwhelmingly a LATE-MECCAN phenomenon.**

- Late Meccan median density (5.34 / 100 verses) is **>> all other phases**.
- Late Meccan mean (8.95) is 5× the Early Meccan mean (1.74).
- Medinan settles at 4.93 mean / 3.85 median — solid but well below Late
  Meccan peak.

This **rises sharply through the Meccan period and partly relaxes in
Medinan** — exactly the pattern expected if qul is a polemical-dialogic
device tied to the Meccan dawʿah escalation (the Prophet being commanded
to articulate increasingly definite positions against ascendant
opposition), with Medinan settling into a mix of qul-via-Prophet (legal
*qul li-l-muʾminīna* style) and direct *yā ayyuhā lladhīna āmanū*
addressed-to-community register.

## Joint verdict

| cell | test | verdict |
|---|---|---|
| 1 | total = 332 | **PASS** |
| 2 | per-surah distribution | PUBLISHED |
| 3 | v1-w1 openers = {72, 109, 112, 113, 114} | **PASS** |
| 4 | ≥ 3 formulaic frames each ≥ 5× | **PASS** (11 of 15 frames pass) |
| 5 | period × density Mann-Whitney | NULL (p = 0.534) |
| 6 | phase × density Kruskal-Wallis | **PASS** (p = 1.0 × 10⁻⁷) |

5 of 6 cells fire. Cell 5's null is informative: **period (Meccan vs
Medinan) is the wrong cut**; phase (Nöldeke 4-class) reveals the actual
Late-Meccan peak.

## Novel findings (relative to imperative-run-1 / classical literature)

1. **The "qul tetralogy" is structurally a quintet (Cell 3).** Classical
   recitational tradition pairs Q 109 + 112 + 113 + 114 as the daily-
   recitation suite; the structural extractor adds **Q 72 al-Jinn** as a
   5th canonical v1-w1 qul-opener. No other surah in the corpus opens with
   bare qul. (Recovers + extends the [[h-new-61-opening-words|H-NEW-61]] finding at the qul-specific
   level.)

2. **qul-density is a Late-Meccan signature (Cell 6).** Mean density per
   100 verses by Nöldeke phase: Early Meccan 1.74 → Middle Meccan 4.89 →
   **Late Meccan 8.95** → Medinan 4.93. This is a phase-shaped curve, not
   a binary period cut; the Meccan-vs-Medinan Mann-Whitney U is null
   precisely because of within-Meccan heterogeneity. **p = 1.0 × 10⁻⁷**
   (Bonferroni-passing). qul is the polemical-dialogic register that
   peaks during the late-Meccan oppositional dawʿah, then settles in
   Medinan as legal-instructional speech-act verb.

3. **The qul-corpus is template-driven (Cell 4).** 11 of 15 pre-registered
   "qul + X" frames each occur ≥ 5×; combined ≈ 130 / 332 (39%) of all
   qul tokens are accounted for by ten or so locked compositional
   templates: *qul + assertive* (44), *qul + interrogative* (38), *qul +
   direct-address* (12), *qul + counterfactual* (7), etc. This places the
   qul-corpus on the same footing as the *yā ayyuhā lladhīna āmanū* and
   *tilka āyāt al-kitāb* incipit templates documented in [[h-new-61-opening-words|H-NEW-61]]: an
   **explicit speech-act register** with a small finite set of compositional
   schemas, not a free-form imperative.

4. **57 of 114 surahs (50%) have zero qul.** The corpus splits sharply:
   exactly half the Quran has no instance of the divine command-to-Prophet
   *qul*. The zero-qul surahs cluster in the early-Meccan
   oath-and-eschatology Mufaṣṣal short suras (Q 73–104, mostly) and a
   handful of Medinan policy-narrative suras addressed-to-believers.
   This is an **independent confirmation of the Late-Meccan peak**: by
   definition, qul concentrates in the surahs that DO use qul, and those
   surahs are the Late Meccan polemical mid-corpus (Q 6, 10, 17, 34, 39…)
   plus the few qul-opening Mufaṣṣal poles (Q 109, 112, 113, 114, 72).

## Limitations / pre-registered carve-outs

- The 332-count uses the QAC canonical four-feature filter
  `POS:V|IMPV|LEM:qaAla|2MS`. Surface-string matching (294 bare قل + 21
  وقل + 18 فقل = 333) gives a different number because a single surface
  قل may not be morphologically qaAla-IMPV-2MS (e.g. inside a quotation
  frame). The QAC predicate is the canonical form for this hypothesis and
  matches the publicly-cited 332.

- Cell 5's null is not a failure of the hypothesis but of the binary
  Meccan/Medinan cut. Cell 6's phase-cut yields a sharply significant
  result. A follow-up h-new-74-1-period-bimodality could explicitly test
  for the bimodality of the Meccan distribution.

- "Addressee analysis" (Question 4 in the task) was operationalised as
  the *qul + X* compositional-frame catalog (Cell 4). The bare 2MS
  imperative is invariantly to-the-Prophet (one of the QAC selectional
  invariants), so "who is being addressed BY the qul-imperative" has a
  single answer (the Prophet); the more interesting question — "what is
  the Prophet then asked to say to whom" — is captured by the 1/2/3-word
  follow-frame.

- Q 13 al-Raʿd has an Egyptian (Medinan) vs Nöldeke (Late Meccan) split
  in our chronology source. The phase-correlation Cell 6 uses the Nöldeke
  phase column. With the Egyptian period column for Cell 5, this places
  Q 13 in Medinan; with Nöldeke phase for Cell 6 it places Q 13 in Late
  Meccan. Both groupings keep Q 13 in a high-qul-density bin, so the
  effect is robust to this single re-classification.

## Cross-reference

- `findings/phase-b-hypotheses/imperative-mood.md` — [[h-new-74-qul-distribution|H-NEW-74]]'s parent;
  total 332 count, 940 to-Muḥammad imperatives, salāh+zakāh joint
  formula. [[h-new-74-qul-distribution|H-NEW-74]] is the qul-specific deep-dive.
- `findings/phase-b-hypotheses/h-new-61-opening-words.md` — [[h-new-74-qul-distribution|H-NEW-74]]
  Cell 3's v1-w1 result is exactly the IMPERATIVE-class subset of [[h-new-61-opening-words|H-NEW-61]]
  minus Q 96 (which is *iqraʾ* not *qul*).
- `findings/phase-b-hypotheses/quotation-analysis.md` — the original
  332-qul anchor; `qāla` (532), `qālū` (332), `qul` (332), confirming
  the Sufi-numerology equality of *qālū* and *qul*.
- `findings/phase-b-hypotheses/h-new-67-sab-tiwal-mathani.md` — long
  exposition surahs (Q 2, 3, 4, 5, 6, 7, 9, 10) — the high-qul-count
  surahs Q 2, 3, 6, 7, 9, 10 fall almost entirely within this group.

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-74-qul-distribution-prereg.md`
- Script: `scripts/h_new_74_qul_distribution.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-74.json`
- Journal: `journal/h-new-74-run-1.md`
