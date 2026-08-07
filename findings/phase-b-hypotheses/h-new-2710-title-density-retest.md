---
id: H-NEW-2710
title: Title-density re-tested — the apparent eponymy effect is almost entirely topicality and root rarity
date: 2026-08-07
author: Waiel Al-Shujaa
status: TOPICALITY-EXPLAINED — Null A passes overwhelmingly, Null B fails the registered gate on all three statistics; residual rate ratio 1.285 at rank-1, median rank indistinguishable (p = 0.76)
prereg: prereg-h-new-2710-title-density-retest.md
prereg_sha256: c9d91fe656383016139271759c65ca7b306e3bc7fd0ee9054bd8f7beed100fc2
run: runs/h-new-2710/20260807T014219Z/
replaces: H-NEW-1820 (Pillar 4, withdrawn 2026-08-07)
prior_art: H-NEW-2680 D4
seed: 20260509
seed_replication: 20260519
family: TITLE-2026-08-07-A
---

# H-NEW-2710 — Title-density, with an actual null

**Verdict: `TOPICALITY-EXPLAINED`. Neither the withdrawn law nor the withdrawal notice
was right. Under a null that matches control roots on frequency *and* dispersion, the
eponymy effect shrinks to a rate ratio of 1.285 at rank-1 and vanishes entirely on median
rank (2 vs 2.24, p = 0.76). Nothing clears the registered gate. And the entire remaining
effect is carried by rare title roots: 27 of 29 bottom-tertile roots are rank-1, against
7 of 31 top-tertile.**

Pre-reg SHA-256 `c9d91fe6…100fc2`, runtime-verified. 10,000 draws per null, two nulls of
different kinds, replications at +10. Family of **6** registered inferences; Bonferroni
α = 0.008333, project novelty rule stricter, so the **raw decision gate is 0.000833**.

---

## 1. Results

Metric: **per-word density**, the single stated primary (pre-reg §3.2). Observed
statistics over the 89 eponymous surahs: **42 rank-1, median rank 2, MRR 0.5892.**

| statistic | observed | **Null B** (topicality + rarity matched) | | | **Null A** (pairing permutation) | | |
|:--|--:|--:|--:|:-:|--:|--:|:-:|
| | | null mean | p | gate | null mean | p | gate |
| S1 rank-1 count | **42** | **32.68** | 0.0019 | ✗ | 0.94 | 1.0e-4 | ✓ |
| S2 median rank | **2** | **2.24** | 0.761 | ✗ | 12.19 | 1.0e-4 | ✓ |
| S3 MRR *(primary)* | **0.5892** | **0.5155** | 0.0011 | ✗ | 0.1725 | 1.0e-4 | ✓ |

All three locked directions matched. **All three FAIL under Null B and PASS under Null
A.** Replications agree (Null B 0.0024 / 0.764 / 0.0014; Null A all 1.0e-4).

Effect sizes under Null B, as pre-reg §5.1 requires the finding to lead with:

- **S1 rate ratio = 1.285**, z = +2.97, null 95% band [26, 39] against observed 42.
- **S3 rate ratio = 1.143**, z = +3.08.
- **S2: no effect at all** — median rank 2 observed against a null median of 2.24.

Under Null A the same numbers are RR 44.8 and 3.42, z = +42.7 and +39.5. **The gap
between the two nulls is the whole story.**

---

## 2. The enrichment shrinks monotonically as the null gets better matched

This is the finding's core, and it explains why two competent readings of the same data
disagreed.

| null model | expected rank-1 | observed | rate ratio |
|:--|--:|--:|--:|
| uniform over 114 surahs *(never run; the intuition behind "astronomical")* | ~0.8 | 42 | ~54 |
| **Null A** — permute the 89 pairings, no topicality | 0.94 | 42 | **44.8** |
| **H-NEW-2680 D4** — control roots attested in the surah, matched on **frequency only** | 25.66 | 43 | **1.68** |
| **Null B (this test)** — matched on **frequency AND dispersion** | **32.68** | 42 | **1.285** |

Each row conditions on more of the corpus's real structure, and the effect falls by an
order of magnitude at each step. **Adding dispersion matching to D4's frequency matching
absorbs most of what was left.** The withdrawal notice's phrase *"strongly ENRICHED"*
rests on the frequency-only row; it was directionally right and quantitatively wrong.

---

## 3. Where the effect actually lives: rare roots

Split by title-root corpus frequency tertile (per-word density, T1):

| tertile | n | rank-1 | median rank | MRR |
|:--|--:|--:|--:|--:|
| **low frequency** | 29 | **27 (93%)** | **1** | **0.966** |
| mid frequency | 29 | 8 (28%) | 3 | 0.467 |
| **high frequency** | 31 | **7 (23%)** | **6** | 0.351 |

**27 of the 42 rank-1 surahs have title roots in the bottom frequency tertile.** A root
attested a handful of times, concentrated where its topic is discussed, ranks its own
surah first almost automatically — *raʿd* (thunder, Q 13), *naḥl* (bees, Q 16), *naml*
(ants, Q 27). That is arithmetic about rare words, not a fact about naming.

Conversely, a surah named after a common root is usually *not* its density peak: 24 of 31
top-tertile eponyms are not rank-1. This is exactly the set of cases the project had been
collecting one at a time as striking individual findings (Q 19 *maryam*, Q 68 *qlm*,
Q 40 *gfr*, Q 47 *qtl*, Q 55 *raḥmān*). **They are not individually striking. They are
what a common title root does.**

The strict-matching subset — the 63 pairs that matched controls at ±×2 on both axes,
which necessarily excludes the extreme-rare roots — gives **20/63 rank-1, median rank 3,
MRR 0.473**, well below the full set. Same conclusion from the other direction.

---

## 4. The three claims, kept apart — the plain-words conclusion

H-NEW-1820 conflated these. Pre-reg §6 fixed the language before the run.

**(a) "Eponymous surahs are usually not rank-1 in their own title root."**
**TRUE, and it reproduces exactly: 47 of 89 are not rank-1.** This descriptive fact never
depended on a null and is unaffected by anything here.

**(b) "Eponymy is independent of density rank."**
**NOT REFUTED at the registered gate — but "independent" is still the wrong word.** A
residual association survives topicality-and-rarity matching (RR 1.285, z = +2.97,
p = 0.0019) and would clear a conventional α = 0.05. It does not clear this project's
Bonferroni + novelty gate of 0.000833, so this test does not license calling it
established. The honest statement is: **almost all of the apparent association is
topicality and root rarity; a small residual remains, suggestive and unconfirmed.**

**(c) "Eponymy strongly predicts density rank."**
**REFUTED.** 1.285× is not "strongly." The withdrawal notice's inversion was an
overcorrection, and pre-reg §6 explicitly forbade me from adopting it without evidence.

**Consequence for Pillar 4.** The law as written — *"title-eponymy and lexical-density-
rank-1 are empirically independent at p ≈ 50:50"* — should **not** be reinstated. The
"p ≈ 50:50" was never a probability of anything; the correct reference is 32.68/89 = 37%
under a matched null, not 50%. But the law's *practical* content survives in a corrected
form:

> **Replacement statement.** A surah's being named after a root raises its chance of
> being that root's density peak by roughly **1.3×** over a comparably frequent and
> comparably dispersed root drawn from the same surah — an effect that does not clear the
> project's novelty gate. The bulk of the raw 42/89 rank-1 rate is explained by title
> roots being rare: 93% of bottom-tertile eponyms are rank-1 against 23% of top-tertile.
> **Any future "surah X is rank-1 in its title root" observation should be checked against
> that root's corpus frequency before being treated as notable.**

That last sentence is the methodological content worth keeping, and it is stronger than
what the original law offered.

---

## 5. Metric fragility — the error that started this, quantified

H-NEW-1820's invalid "correction" substituted a raw-count/per-verse result into a
per-word-density law. Here is what that substitution is worth:

| metric | rank-1 count | median rank | MRR |
|:--|--:|--:|--:|
| **T1 per-word density** *(primary, the law's own instrument)* | **42** | **2** | **0.589** |
| T2 raw count | 34 | 3 | 0.512 |
| T3 per-verse | 40 | 2 | 0.574 |

**The headline count moves by 8 surahs — from 42 to 34 — purely by changing the
denominator.** Under raw count, 55 of 89 are not rank-1, not 47. Cross-metric
substitution is not a rounding issue; it changes the number the law is named after. Only
T1 is gated here; T2 and T3 are reported and are never mixed into a claim.

---

## 6. Audit of H-NEW-1820 — a third uncaught error

87 of 89 published ranks reproduce exactly under the stated tie convention
(`rank = 1 + #{strictly greater}`). Two do not:

| surah | root | published | recomputed | assessment |
|:--|:--|--:|--:|:--|
| **Q 112 al-Ikhlāṣ** | *xlS* | **112** | **18** | **ERROR.** Q 112 has zero *xlS* tokens; 17 surahs have *xlS* density > 0. Q 1 (also zero-count) was correctly ranked 26 by the same rule, so the file is internally inconsistent. |
| Q 77 al-Mursalāt | *rsl* | 20 | 19 | off-by-one, tie handling |

This is a **third** defect in that file, after the reverted 48/89 and the 42+48=90
arithmetic break. Its direction is worth noting: correcting Q 112 from 112 to 18 makes
the eponymous surahs look **better**, and pulls the mean rank from 7.11 to 5.05. **It was
not caught, and it flatters the data — the same failure mode the file's own correction
notice identifies.** All ranks used here are recomputed; the JSON is used only as the
eponymous-set source.

The two zero-attestation eponyms (Q 1 *ftH*, Q 112 *xlS*) are reported separately per
pre-reg §7.1; excluding them leaves 42 rank-1, median 2, MRR 0.602 over 87 — no material
change.

---

## 7. Honest limits

1. **The titles are a transmitted convention, not revealed text.** If transmitters named
   surahs after words salient in them, any residual enrichment is a fact about **naming
   practice**, not composition. **No null in this design separates the two**, and the
   §4 replacement statement must be read as being about received titles.
2. **Null A is trivially significant by construction** and is reported only because it is
   the naive reading of "independence." No claim here rests on it. Its z = +42.7 measures
   the strength of topicality, not of eponymy.
3. **The residual is not nothing.** p = 0.0019 and 0.0011 fail a 0.000833 gate but would
   pass α = 0.05. Calling this "independence confirmed" would overstate it in the other
   direction. A better-powered or better-matched follow-up could resolve it.
4. **The direction lock was not blind** (pre-reg §1.2). The observed rank vector is
   published in `h-new-1820.json` and I had read it, as the brief required; D4's
   approximate null expectation was also known. **What this pre-registration protects is
   the null specification, the statistic set, the tie convention, the metric hierarchy,
   the matching bands and the decision rule — not the direction.**
5. **The eponymous set's selection rule is not fully reproducible.** 12 personal names +
   4 muqaṭṭaʿāt = 16 of 25 exclusions; the remaining 9 are attributed to "could not be
   uniquely mapped" and are not itemised in H-NEW-1820. The set is reused verbatim for
   comparability, not endorsed. Excluded: 5, 10, 11, 12, 14, 19, 20, 21, 23, 29, 30, 31,
   34, 36, 38, 47, 50, 71, 72, 78, 80, 88, 93, 106, 114.
6. **Titles map to roots one-to-one by assumption**, including compound titles
   (*Āl ʿImrān* → *Eml*), which I did not audit item by item.
7. **Null B draws controls from a surah's own roots**, so pools are small for short
   surahs (min 3, median 16). Widening tiers: 63 at ×2, 12 at ×4, 6 at ×8, 8
   unrestricted. The strict-×2 subset is reported in §3.
8. **QAC root assignment is an annotation**, and roots are not senses.
9. **No cross-corpus control** — no other corpus has an equivalent eponymous-title system.

---

## 8. Provenance

- Pre-registration written and SHA-256'd before any null distribution existed, with
  **§1.2 declaring the prior knowledge explicitly** rather than claiming a blind lock.
- Inputs SHA-verified at runtime: `h-new-1820.json` `1a6282e4…`, QAC v0.4 `a1d12923…`,
  `quran-no-tashkeel.json` `253f72f3…`.
- **Verdict-logic diff performed before publication, as required.** Pre-reg §5: *"A
  statistic PASSES iff its observed direction matches the lock AND both of its raw
  p-values are < 0.000833."* Script: `PASS = dir_ok and null_a.passes_gate and
  null_b.passes_gate`, with `passes_gate = p < RAW_GATE` and `RAW_GATE = CORRECTED_GATE /
  TESTS_IN_FAMILY = 0.005 / 6`. Locked directions §4.4 (S1 >, S2 <, S3 >) map to
  `LOCKED_GREATER = {S1: True, S2: False, S3: True}`. **Match, line for line.**
- Manifest paths are repository-relative, so the run record is committable as written.
- Immutable run: `findings/phase-b-hypotheses/runs/h-new-2710/20260807T014219Z/`.
  **No run directory was deleted**, including the empty
  `runs/h-new-2680/20260807T011917Z/`, which belongs to another test and was not touched.
- One 200-permutation smoke run for correctness, written outside `findings/` and
  self-declaring `SMOKE_RUN: true`, retained at `smoke-2710/20260807T014206Z/`.

---

## 9. Cross-references

- **[[h-new-1820-title-density-independence-formal]]** — the withdrawn Pillar 4. §4 gives
  the replacement statement; §6 records a third error in it. Its descriptive 47/89 is
  confirmed and may continue to be cited **as a description**.
- **[[cross-finding-027-formal-eponymy-independence-law]]** — carries the same withdrawal
  and needs the same replacement wording.
- **[[h-new-2680]] D4** — the prior art that triggered the withdrawal, and the row in §2
  that this test refines. **Its full-power run completed while this test was being written**
  (`runs/h-new-2680/20260807T011917Z/`, 2,000 draws): observed 43, null mean **25.657**,
  sd 3.157, p = 5.0e-4 — a rate ratio of **1.68**, confirming and slightly lowering the
  20-draw smoke's 1.75. §2's table uses the full-power numbers. **Its number is not wrong;
  its null matched on frequency only, and adding dispersion matching takes the residual from
  1.68 to 1.285.** D4's own pre-registration calls it descriptive with no locked direction
  and no gate, so it does not by itself retire or reinstate anything.
- **The six individual "not rank-1" findings** (H-NEW-1700, Q068-F-06, Q040-F-03,
  Q047-F-05, H-NEW-1720) — §3 reclassifies these. All five concern **common** title roots,
  where non-rank-1 is the ordinary outcome (23% rank-1 in the top tertile). They are
  instances of a frequency effect, not individual surprises.
- **The retirement/vindication ledger** — this is a **replacement, not a retirement**. The
  law's headline ("independence") was never supported; its practical content survives in
  the corrected, frequency-aware form of §4.
