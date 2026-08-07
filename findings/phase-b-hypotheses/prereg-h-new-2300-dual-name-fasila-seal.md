---
finding_id: H-NEW-2300
title: Dual-name fāṣila seal-grammar — does verse CONTENT predict the sealing name-PAIR?
phase: B
date_preregistered: 2026-05-29
seed: 20260509
n_perm: 10000
status: PRE-REGISTERED (direction-locked before verdict)
extends: H-NEW-2070
---

# PRE-REGISTRATION — H-NEW-2300


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 0. Relationship to the prior (H-NEW-2070)

H-NEW-2070 (MASTER-FINDINGS-LEDGER §10.78, PASS-DIRECTED, p<0.0001) established
the **positional** *al-fawāṣil* grammar: which divine-name occupies the head
(penultimate) vs the seal (final) slot of a verse-final name-PAIR, and that the
pairings are non-random (321 verses, 54 ordered pairs, *raḥīm*/*ḥakīm* terminal
seals, *samīʿ* never seals, *ʿalīm* the lone pivot). It did NOT test whether the
SEMANTIC content of the verse body predicts WHICH pair is chosen.

H-NEW-2300 tests the **content↔seal matching** claim — the orthogonal, semantic
axis. This is the classical *murāʿāt al-naẓīr* / *tamkīn al-fāṣila* doctrine:
the closing name-pair is chosen to SUIT the verse meaning (power/judgment verses
seal with *al-ʿAzīz al-Ḥakīm*; sin/mercy verses with *al-Ghafūr al-Raḥīm*).

## 1. Classical claim under test

- **al-Zarkashī**, *al-Burhān fī ʿulūm al-Qurʾān*, nawʿ on *al-fawāṣil*
  (*murāʿāt al-fāṣila*): the fāṣila is chosen in concord with the verse's
  meaning, not merely for cadence.
- **al-Rāzī**, *Mafātīḥ al-ghayb* (*al-Tafsīr al-kabīr*): the recurrent
  *tamkīn al-fāṣila* observation — the verse body "settles" (*yumakkin*) the
  closing epithet so that the seal is felt as the necessary, expected name.
- **al-Suyūṭī**, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 59 (*fawātiḥ /
  khawātim / fawāṣil*; *asmāʾ mutazāwijah*).
- The doctrine is documented in the project's own prior ledger entry
  H-NEW-2070 §10.78.6 (which cites these same three works). H-NEW-2300 cites
  the doctrine at the level the project already attests; it does NOT assert new
  page-numbers it has not verified on disk.

## 2. Data and rules-tuple

- Text: `quran-text/quran-no-tashkeel.json` (verse-final pair detection — IDENTICAL
  detector to H-NEW-2070).
- Roots (verse content): `data/morphology/quranic-corpus-morphology-0.4.txt`
  (QAC v0.4, `ROOT:` field, Buckwalter).
- Names: `data/asma-al-husna.txt` (97 single-token al-Tirmidhī names; strip ال).
- Rules-tuple:
  `(no-tashkeel, orthographic-token for seal-detection + QAC-ROOT for content,
    verse-final ordered name-pair, base-normalized to 97 al-Tirmidhī single-token
    names, content = QAC stem-roots of verse body EXCLUDING the final 2 words
    [the seal], basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`.

## 3. Seal-pair CLASSES (locked)

Each of the 97 names that participates in a verse-final pair is mapped to a
thematic super-class by its Buckwalter root:

- **MERCY** (forgiveness / mercy / relenting / clemency): gfr, rHm, twb, wdd,
  Efw, rAf, brr, Hlm, $kr.
- **POWER** (might / dominion / decree / judgment / wisdom-as-governance): Ezz,
  Hkm, qhr, jbr, kbr, qdr, Elw, EZm, qwy, mtn.
- **KNOW** (knowledge / hearing / sight / witness / awareness): Elm, smE, bSr,
  xbr, $hd, HfZ, lTf, rqb.

A verse is **pure-class** iff BOTH its seal names belong to the SAME super-class
(e.g. *ghafūr+raḥīm* = MERCY; *ʿazīz+ḥakīm* = POWER; *samīʿ+ʿalīm* / *samīʿ+baṣīr*
= KNOW). Mixed-class pairs (e.g. *ʿalīm+ḥakīm* = KNOW+POWER) are EXCLUDED from the
primary test to avoid arbitrary tie-breaking; they are reported descriptively.
This is the sharpest, least-ambiguous operationalization of the classical claim.

## 4. Content FEATURE (locked)

Independent content-lexicon (verse-BODY roots; chosen on theme, NOT identical to
the seal-root map — the overlap on the seal's own roots is the leakage we control):

- **MERCY-content**: gfr, twb, *nb (sin), Avm (sin), jrm (crime), xTA (error),
  Efw, Hwb (sin), swA (evil), bgy (transgression), fsq (iniquity), Zlm
  (wrongdoing), Edw (enmity/transgression), rHm.
- **POWER-content**: Hkm, mlk (dominion), qdr, qhr, Ezz, jbr, Amr (command),
  qDy (decree), ktb (decree/writ), glb (overcome), qtl (fighting), Hrb (war).
- **KNOW-content**: Elm, smE, bSr, $hd, rAy (see), HfZ, xbr, ktm (concealment),
  bTn (hidden), srr (secret).

**Leakage control (locked, PRIMARY):** the verse body excludes the final two
words (the seal itself) AND the two seal-name roots are stripped from the body
before content-classification, so a verse cannot "match" merely by echoing its
own seal. A leakage-UNCONTROLLED sensitivity run (seal-roots kept) is reported
separately and is expected to be inflated.

For each pure-class verse, the body's **dominant content-class** = the content
super-class with the most root-hits; ties → no-call (verse excluded from the MI
contingency). Only verses with ≥1 content-lexicon root and an unambiguous
dominant class are "called."

## 5. Hypotheses, direction LOCKED, null

**Permutation null (both statistics):** hold the called-verse content-labels
fixed; PERMUTE the seal-class labels across called verses (destroys content↔seal
association, preserves both marginals). seed=20260509, 10,000 perms.

Bonferroni family k=2, α_cell = 0.025.

- **H1 (primary, MI):** mutual information I(dominant-content-class ; seal-class)
  over called verses is **GREATER** than the null (one-sided upper tail).
  Direction LOCKED above. PASS iff p_perm ≤ 0.025.
- **H2 (match-rate):** the fraction of called verses whose dominant-content-class
  EQUALS the seal-class is **GREATER** than the null. Direction LOCKED above.
  PASS iff p_perm ≤ 0.025.

**Pre-registered SECONDARY (directional, the sharpest classical sub-claim):**
- **H3 (MERCY-vs-rest):** among ALL pure-class verses, a 2×2 of
  {body-has-MERCY-content-root (leakage-stripped)} × {seal-class==MERCY}; the
  one-sided Fisher exact test (direction: mercy-content enriches mercy-seal) is
  significant. Reported with α=0.05 (single directional test; not in the
  Bonferroni-2 family).

## 6. Verdict rule (LOCKED)

- **EXTENDS H-NEW-2070 (PASS-DIRECTED-CONTENT):** H1 AND H2 pass (both p≤0.025)
  AND H3 significant — the seal is content-matched, not merely formulaic.
- **PARTIAL:** exactly one of {H1, H2} passes, or H1/H2 pass but H3 not
  significant.
- **NULL (reverse / formulaic):** observed MI and match-rate BOTH below the null
  median → seals are FORMULAIC / cadence-driven, NOT content-matched. This is a
  real, equally-prominent finding (would mean the *al-fawāṣil* pairing is a
  positional-phonological constraint only, refining H-NEW-2070's scope).

## 7. Garden-of-forking-paths log (design fixed BEFORE verdict-lock)

Design choices were fixed by exploratory inspection of the data STRUCTURE (class
sizes, leakage mechanics) NOT by the verdict:
1. 3 super-classes (MERCY/POWER/KNOW) rather than per-pair — chosen because
   per-pair cells are too sparse (54 pairs, median count low) for a stable MI.
2. Pure-class-only primary — chosen to avoid arbitrary tie-breaking on mixed
   pairs; mixed pairs reported descriptively.
3. Leakage-stripped body as PRIMARY; leakage-kept as sensitivity — the
   leakage-kept version trivially inflates and is NOT the claim being tested.
4. Tie → no-call — conservative; avoids inventing a content-class.
5. MERCY-vs-rest (H3) pre-registered as the cleanest directional sub-claim
   because MERCY content (sin/forgiveness vocabulary) is the most lexically
   distinct theme.

## 8. MW protections

- MW-1: statistics (MI, match-rate, Fisher) and direction fixed here.
- MW-2: 10,000-perm label-permutation null.
- MW-3: two statistics (MI + match-rate) + a third independent design
  (2×2 Fisher) + a leakage-sensitivity model variant.
- MW-6: leakage-stripped vs leakage-kept is the instrument-control contrast.
- MW-7: H3 is directional/pre-registered, not post-hoc.

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2300-dual-name-fasila-seal.md` (this file)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2300.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2300.json`
- Finding: `findings/phase-b-hypotheses/h-new-2300-dual-name-fasila-seal.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
