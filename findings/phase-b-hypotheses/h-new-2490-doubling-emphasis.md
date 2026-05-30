---
finding: H-NEW-2490
title: The adjacent doubling-for-emphasis device (taʾkīd bi-l-tikrār) — corpus census
author: Waiel Al-Shujaa
date: 2026-05-30
phase: B
verdict: H1 VINDICATED (genre-concentrated, no pre-commit violation) · CENSUS delivered
prereg_sha256: 6a2c133f2322598483a1ed87a94d7e928b588e8dc15d582d7a89668f621e5f87
seed: 20260509
nperm: 10000
rules_tuple: (no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi); QAC v0.4 segment lens for connective/core separation
---

# H-NEW-2490 — The adjacent DOUBLING-FOR-EMPHASIS device (*taʾkīd bi-l-tikrār*)

**Verdict: H1 VINDICATED (genre-concentrated in juzʾ-ʿamma; direction locked, no
pre-commit violation) · full corpus census delivered.** Pre-reg SHA-256
`6a2c133f…5f87`, seed 20260509 (replication +10), 10000 perms, runtime-verified.

## 1. The device and its definition (locked)

The **doubling-for-emphasis** (*taʾkīd bi-l-tikrār*, emphatic reassertion by
repetition) is the tightest, most semantically-constrained rung of the project's
repetition scale-ladder:

```
H-NEW-2100/2140 (refrain saturation)
  → 2310 (metronomic refrain-spacing)   [byte-exact cross-verse refrain]
  → 2350 (exact cross-surah verse twin)
  → 2380 (near cross-surah verse twin)
  → Q094-F-01 (the corpus-tightest adjacent couplet)              §10.118
  → 2450 (adjacent near-verbatim reprise; ANY edit-mechanism)     §10.125
  → 2490 (THIS): the directional REASSERTION subset
```

A pair (verse i, verse i+1) — or two consecutive clauses within one verse — is a
**doubling** iff (locked predicate D, see prereg §1):

> the two **lexical cores are identical** (or differ by exactly **one** minimal
> in-place change: a root-shared inflection, or a `sawfa`↔`sa-` future-particle
> swap), and they differ by exactly **one leading emphatic connective**
> `∈ {thumma (ثم), fa (ف), wa (و)}`.

No new content token is introduced. A parallel template with a *different content
word* (e.g. Q99:7-8 *khayran*→*sharran*) is NOT a doubling — that is *muqābala*, a
distinct device. The discriminator is **lexical-core containment**: the second
member repeats the first verbatim, the only addition being the connective.

**Instrument** (MW-1): `quran-text/quran-no-tashkeel.json` (waqf/codex glyphs
U+06D6–U+06ED stripped); QAC v0.4 morphology
(`data/morphology/quranic-corpus-morphology-0.4.txt`) is the lens that separates the
leading connective morpheme from the lexical core and supplies ROOT for the
inflection test. Two logged instrument decisions (garden-of-forking-paths, made
during the run, both faithful to the locked grapheme definition):
1. the QAC pausal superscript marker `^` is stripped from forms (it is a codex
   notation, not a lexical difference — e.g. Q75:35 `>awolaY`^` = Q75:34 `>awolaY`);
2. a leading `fa`/`wa` grapheme prefix counts as the connective under **any** QAC
   syntactic subtype (CONJ / CAUS / REM / RSLT / SUP), because the rhetorical
   doubling is carried by the *particle*, not its fine syntactic tag (e.g. Q74:19
   carries an `f:CAUS` fa). The total count did NOT change under this broadening
   (still 6) — the gate is the core-match, not the connective subtype.

## 2. The full verse-grain census (H2)

**6 adjacent verse-pairs corpus-wide satisfy D. ALL 6 are Meccan; 4 are in
juzʾ-ʿamma.** (Source: `csv/h-new-2490.json`.)

| pair | surah | region | connective | core change | text i ‖ text i+1 |
|:--|:--|:--|:--|:--|:--|
| **Q74:19-20** | al-Muddaththir | Meccan | fa/thumma | identical | فقتل كيف قدر ‖ ثم قتل كيف قدر |
| **Q75:34-35** | al-Qiyāma | Meccan | thumma | identical | أولى لك فأولى ‖ ثم أولى لك فأولى |
| **Q78:4-5** | al-Nabaʾ | Meccan (ʿamma) | thumma | identical | كلا سيعلمون ‖ ثم كلا سيعلمون |
| **Q82:17-18** | al-Infiṭār | Meccan (ʿamma) | thumma/wa | identical | وما أدراك ما يوم الدين ‖ ثم ما أدراك ما يوم الدين |
| **Q94:5-6** | al-Sharḥ | Meccan (ʿamma) | fa | identical | فإن مع العسر يسرا ‖ إن مع العسر يسرا |
| **Q102:3-4** | al-Takāthur | Meccan (ʿamma) | thumma | identical | كلا سوف تعلمون ‖ ثم كلا سوف تعلمون |

**The seed family `{Q75:34-35, Q78:4-5, Q102:3-4}` is recovered exactly** (validity
check passed — fail-fast was armed). **Three new members are found beyond the seed:**

- **Q74:19-20** — *fa-qutila kayfa qaddara* / *thumma qutila kayfa qaddara* ("so may
  he be killed, how he plotted! / then may he be killed…") — the al-Walīd b.
  al-Mughīra damnation-doubling, the chronologically EARLIEST member (al-Muddaththir
  is among the first revelations). It contrasts an `fa` (causal/result) with `thumma`
  — a doubling that *escalates* the connective.
- **Q82:17-18** — *wa-mā adrāka mā yawm al-dīn* / *thumma mā adrāka mā yawm al-dīn*
  ("and what will make you realise what the Day of Judgement is! / then…") — the
  *mā adrāka* rhetorical-question doubling, contrasting `wa` with `thumma`.
- **Q94:5-6** — *fa-inna maʿa al-ʿusri yusrā* / *inna maʿa al-ʿusri yusrā* (the
  *yusrayn* consolation couplet, the Q094-F-01 §10.118 corpus-tightest adjacent
  pair) — the SOLE non-`thumma`-leading member of the family (an `fa` on the FIRST
  member rather than `thumma` on the second), and the only **consolation**-register
  member among five **threat/warning**-register members.

### Connective distribution (the brief's headline)

| connective(s) | count | members |
|:--|:--:|:--|
| `thumma` (pure) | 3 | Q75, Q78, Q102 |
| `fa`/`thumma` (both members carry a connective, escalating) | 1 | Q74 |
| `thumma`/`wa` | 1 | Q82 |
| `fa` (pure) | 1 | Q94 |

**`thumma` is the dominant connective of the device: it appears in 5 of the 6
doublings** (the three pure seeds + Q74 + Q82). `fa` appears in 2 (Q74, Q94); `wa`
in 1 (Q82). There are **0 bare (connective-less) verbatim adjacencies** — consistent
with H-NEW-2450 §10.125 ("0 exact-verbatim adjacencies corpus-wide"): the canonical
text never doubles a verse with *zero* marker; the doubling is ALWAYS connective-led.
**Every doubling has an identical lexical core (0 content change)** — these are pure
reassertions, not paraphrases.

### Within-verse clause-grain census (descriptive, MW-7 capped)

**1 within-verse clause-doubling:** **Q112:3** *lam yalid wa-lam yūlad* ("He begets
not, nor is He begotten") — clause `lam yalid` doubled by `wa-lam yūlad`, same
negator *lam*, same root y-l-d, active→passive inflection, `wa` connective. This is
the tawḥīd-creed's active/passive negation doubling — the within-verse face of the
device, in al-Ikhlāṣ. (The seed Q75:34 *awlā* / *fa-awlā* is a genuine within-verse
fa-doubling but is correctly excluded by the ≥2-core-word substantive gate, since
*awlā* alone is one word; it surfaces only at verse grain as part of Q75:34-35.)

## 3. H1 — genre-concentration (CONFIRMATORY)

Statistic: per-surah doubling-rate = (#doublings)/(#substantive adjacent pairs);
Δ = mean_rate(juzʾ-ʿamma 78–114) − mean_rate(rest 1–77).

| quantity | value |
|:--|:--|
| mean doubling-rate, juzʾ-ʿamma | 0.00992 |
| mean doubling-rate, rest (1–77) | 0.00058 |
| **Δ observed** | **+0.00934** |
| label-permutation null mean | 0.00003 |
| **p (one-sided)** | **0.0166** |
| replication (seed +10) p | 0.0165 |
| α (k=1 confirmatory) | 0.05 |

**H1 PASS — direction held, no pre-commit violation.** The doubling-for-emphasis
device is **genre-concentrated in juzʾ-ʿamma**: the short-Meccan eschatological /
warning register carries it at ~17× the rate of the rest of the corpus, and the
concentration is significant against a 10000-perm label-permutation null
(p=0.0166, replicated 0.0165). All 6 doublings are Meccan; 4 of 6 sit in juzʾ-ʿamma
itself (Q78, Q82, Q94, Q102), the other 2 (Q74, Q75) in the adjacent short-Meccan
warning surahs.

### MW-3 — Meccan vs Medinan (secondary axis, non-confirmatory)

mean_rate(Meccan)=0.00478, mean_rate(Medinan)=**0.00000**, Δ=+0.00478, p=0.173.
**The device is corpus-EXCLUSIVE to Meccan surahs** (0 Medinan doublings) — the
direction is correct and the absolute exclusion is total, but with only 6 events
the coarse Meccan/Medinan label-permutation does not reach significance; the finer
juzʾ-ʿamma cut (H1) does. This is the expected geometry: the device is bound to the
short, percussive, oath-and-threat Meccan register, not merely "Meccan."

## 4. MW-6 — the H-NEW-2450 subset cross-check (instrument validation)

H-NEW-2450's low-edit roster (char-edit ≤ 3) holds exactly 6 adjacent pairs:
{Q74:19-20, Q75:34-35, Q78:4-5, Q82:17-18, Q94:5-6, Q99:7-8}. Predicate D:

- **accepts 5** as doublings (Q74, Q75, Q78, Q82, Q94 — all 5 reassertions);
- **rejects exactly 1**: **Q99:7-8** *fa-man yaʿmal mithqāla dharratin **khayran** yarah*
  / *wa-man yaʿmal mithqāla dharratin **sharran** yarah* — the zalzala "atom's-weight
  of good/evil" pair. This is a *muqābala* (antithetical parallel template):
  *khayr* "good" (root خ-ي-ر) ↔ *sharr* "evil" (root ش-ر-ر) is a **different-root
  content substitution**, not a reassertion. D correctly excludes it.

This is the clean validation that D is a genuine **strict-subset selector**: it
isolates the *reassertions* (taʾkīd) and discards the *contrast templates*
(muqābala) and rhyme-retunings that H-NEW-2450 (by design) pooled together. The
doubling census is a proper, semantically-meaningful refinement of 2450, not a
re-run of it.

## 5. Classical grounding

- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60 (al-badīʿ)** lists
  **al-Takrār (Repetition)** among the rhetorical devices
  (`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`,
  extracted text ≈line 3560: ">l-Takr~r (Repetition)"; the discussion ≈line 11094
  holds that prose free of repetition is generally superior *except where the
  repetition serves a rhetorical purpose* — precisely the emphatic *taʾkīd*
  function the canonical text deploys here). The census operationalises al-Suyūṭī's
  *takrār* at its sharpest sub-type (connective-led adjacent verbatim reassertion).
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** treats *al-taʾkīd* (confirmation/
  emphasis) and *al-tikrār*; *taʾkīd lafẓī* (verbal emphatic reassertion) by a
  connective such as `thumma` / `fa` is its canonical means
  (`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`).
- **The finding refines both**: the device is not corpus-uniform "repetition for
  eloquence"; it is a SHARP, genre-bound intensifier — `thumma`-dominant,
  Meccan-exclusive, juzʾ-ʿamma-concentrated, threat-register (5/6), with the single
  consolation-register exception (Q94) being also the corpus-tightest couplet.

## 6. Convergences with prior project findings

- **Q102-F-01 B-H1 (§10.114)** seeded the 3-member *thumma*-threat family; this
  census recovers it and finds 3 more members, confirming the seed was a true family
  fragment, not a singleton.
- **H-NEW-2450 (§10.125)** — the doublings are a strict subset of 2450's low-edit
  roster (MW-6); 2450's *ordering-by-dispersion* law (the corpus SPACES look-alikes)
  is the macro-rule, and the doubling device is exactly the *marked, reserved
  exception* — the rare adjacent verbatim reprise used deliberately as an
  intensifier. The two findings are complementary: dispersion is the default,
  connective-led doubling is the licensed exception.
- **Q094-F-01 (§10.118)** — Q94:5-6 is both the corpus-tightest adjacent couplet AND
  the sole consolation-register doubling; this finding places it inside the larger
  family and shows it is the lone `fa`-only, non-threat member.
- **Genre-concentration register** — H1's PASS joins the juzʾ-ʿamma /
  short-Meccan-eschatology concentration cluster (H-NEW-2210/2240/2250/2410/2450-H2):
  the percussive warning register is the corpus's locus of marked repetition devices.

## 7. Honest limits

- N=6 verse-grain events is small; H1 reaches p=0.0166 because the rest-of-corpus
  rate is near-zero, not because of large counts. The Meccan/Medinan coarse cut does
  not reach significance (MW-3, p=0.173) though its direction and absolute exclusion
  (0 Medinan) are clean.
- The ≤1-minimal-change rule is the one consequential design choice; it was locked
  in the pre-reg and, in the event, all 6 verse-grain doublings turned out to have
  **0** core change (pure identical cores), so the rule's slack was never load-bearing
  for the headline census.
- The clause-grain census (within-verse) has researcher degrees of freedom in clause
  segmentation and is reported as descriptive only (MW-7 cap); its single hit (Q112:3)
  is robust by inspection.
- Two instrument decisions (caret-stripping, fa/wa-prefix-subtype broadening) were
  made during the run and logged in §1; both are faithful to the locked grapheme
  definition and neither changed the count of 6.

## 8. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2490-doubling-emphasis.md`
- Script: `findings/phase-b-hypotheses/scripts/h-new-2490.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2490.json`
- Findings: `findings/phase-b-hypotheses/h-new-2490-doubling-emphasis.md` (this file)
