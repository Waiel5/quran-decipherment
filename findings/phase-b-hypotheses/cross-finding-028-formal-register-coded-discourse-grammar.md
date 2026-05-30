---
finding_id: cross-finding-028-formal
status: FORMAL CODIFICATION (2026-05-30, Wave-Q) — unifies H-NEW-2250 + 2490 + 2500 + 2520 with a joint separability test (H-NEW-2530)
phase: C
date: 2026-05-30
verdict: The three Quranic registers are JOINTLY separable by their function-word + person-grammar signatures (LOO acc 76.9% vs 44% baseline, p=10⁻⁴; ANOVA F_sum p=10⁻⁴)
---

# Cross-finding-028 (FORMAL) — The register-coded discourse-grammar law: genre is encoded in the function-words and person-grammar, at the particle grain

## The principle, formally stated

> **Quranic discourse register (genre) is grammatically coded at the function-word and
> person-grammar grain. The three registers — narrative/qaṣaṣ, legal-Medinan, and
> eschatological-mufaṣṣal — each carry a distinct, mutually-distinguishing signature on
> (a) the verse-onset particle/formula axis and (b) the within-verse person-iltifāt axis.
> These signatures are not merely individually genre-correlated; they JOINTLY separate
> the registers: a per-surah feature vector built from the four marker-detectors predicts
> the register label at 76.9% (vs a 44% majority baseline) under leave-one-out
> cross-validation, far above a label-shuffle null (p = 10⁻⁴), and the between-register
> ANOVA on the same vector is equally significant (p = 10⁻⁴).**
>
> **Register signatures (the three columns of the law):**
> - **Narrative/qaṣaṣ** ⇒ *wa-idh / wa-lammā / wa-qālū* onsets + the **3↔1
>   divine-narrative-voice** iltifāt.
> - **Legal-Medinan** ⇒ the **2↔3 direct-community-address** iltifāt (keyed by
>   *yā ayyuhā alladhīna āmanū*).
> - **Eschatological/mufaṣṣal** ⇒ the *idhā* conditional-cascade + the *thumma*-led
>   doubling-for-emphasis intensifier.

This generalizes cross-finding-025 ("cohesion is pericope-scoped") and cross-finding-026
("cohesion is a law, chiasmus is a rarity") onto an orthogonal axis: where 025/026
concern *lexical cohesion*, 028 concerns *discourse register* — and shows register is
carried by a thin, specific grammatical layer (particles + person-deixis), not by content
vocabulary.

## The four empirical pillars + the unifying test

| Pillar | Finding | Register-feature it supplies | Ledger |
|---|---|---|---|
| qaṣaṣ-onset census | **H-NEW-2520** | *idh / lammā / qālū* onset densities (4–14× in s≤50) | §10.129 |
| eschatological cascade | **H-NEW-2250** | *idhā* conditional-cascade (2.6× in juzʾ-30, Q81:1-8 8-run) | §10.88 |
| doubling intensifier | **H-NEW-2490** | *thumma*-led adjacent doubling (6-member, ~17× juzʾ-ʿamma) | §10.130 |
| iltifāt type × genre | **H-NEW-2500** | person-shift TYPE (narrative 3↔1 +18.2; legal 2↔3 +13.1) | §10.131 |
| **unifying joint test** | **H-NEW-2530** | the 6-feature LOO-classifier + ANOVA separability test | §10.133+ |

H-NEW-2530 is the keystone. It **reuses the four pillars' own JSON outputs verbatim**
(no detector recomputed), assembles a per-surah 6-feature vector
{f_idh, f_lammā, f_qālū, f_idhā-cascade, f_doubling, f_iltifāt-type}, and tests whether
the vector separates the three registers above a surah-label-shuffle null (seed 20260509,
10000 perms, Bonferroni k=2, α_bon=0.025). **Both lenses pass at the floor p=10⁻⁴:**
- H1 leave-one-out nearest-centroid accuracy = **0.7692** (majority baseline 0.4396),
- H2 summed one-way ANOVA F = **80.54**,
- replicated at seed 20260511, cross-validated by Gaussian naïve-Bayes (71.4%), and
  robust to the 4-class extension (53.5%, still p=10⁻⁴).

## The mechanism — register lives in two thin grammatical layers

The per-feature ANOVA decomposition (H-NEW-2530) shows the JOINT separation is carried by
two layers, transparently and honestly:

1. **The onset-particle layer** (f_qālū F=33.5, f_lammā F=12.1, f_idh F=10.5; all
   p≈10⁻⁴) — qaṣaṣ narrative announces itself by *how a verse begins*.
2. **The person-iltifāt layer** (f_iltifāt-type F=19.8, p=10⁻⁴) — legal-Medinan announces
   itself by the 2↔3 direct-address turn; narrative by the 3↔1 divine-voice turn.

The two **sparse intensifier features** (f_doubling F=3.5, p=0.025; f_idhā-cascade F=1.1,
p=0.37) are individually weak — the *idhā* cascade has only 5 host-surahs corpus-wide and
is NOT a univariate separator on its own — but they contribute register-specific spikes to
the multivariate fit (all 5 of the 6-member doubling census sit in the eschatological
register). **This is precisely why the JOINT test is the right unit:** the law is a
multivariate fact, not the sum of six univariate facts, and the sparse markers would be
underpowered alone.

## The cleanest case: *idh* ⊥ *idhā* (recall vs eschatology)

The sharpest single demonstration of register-coding at the particle grain is the
near-minimal-pair contrast surfaced by H-NEW-2520 vs H-NEW-2250:
- **إِذْ *idh*** (`LEM:<i*`, recall) — 110/118 verse-initial tokens in s≤50, the narrative
  covenant-recall register (Q2 Banū-Isrāʾīl, Q2:124-127 Ibrāhīm tetrad).
- **إِذَا *idhā*** (`LEM:<i*aA`, eschatological conditional) — concentrated in s≥78, the
  Day-of-Judgment cascade (Q81:1-8 corpus-extreme 8-run).

Two orthographically-adjacent particles, distinct lemmas, opposite mushaf-halves, opposite
registers. The corpus uses the *grammatical particle itself* as a register marker.

## Why this is a law, not four narrated marginals (the skeptical alternative, falsified)

Before H-NEW-2530, the §10.133 "register-coded discourse grammar" statement was read off
four SEPARATE findings. The honest skeptical alternative was: these are four independent
genre-correlated marginals that only *look* like a joint structure because they were
described together. H-NEW-2530 falsifies that alternative directly — a held-out classifier
trained on the four pillars' assembled outputs recovers the register at 1.75× the majority
baseline (p=10⁻⁴). The information is JOINT and multivariate. That is the empirical content
that promotes the verbal convergence to a formal cross-finding.

## Honest qualifications (the law's soft edges)

1. **Legal↔eschatological is the soft boundary.** LOO confusion: narrative recovered
   25/31, eschatological 37/40, but legal only 8/20 (12 legal surahs misclassified as
   eschatological). Legal and eschatological SHARE the 2↔3-dominant person-grammar and
   both LACK qaṣaṣ onsets; what splits them (cascade/doubling) is sparse. The clean
   separations are narrative-vs-rest and eschatological-vs-rest. The legal register's
   *own* defining marker (*yā ayyuhā alladhīna āmanū*) is the genre-proxy DEFINITION, not
   a feature in the vector, so legal-vs-narrative is perfect (0 errors) but
   legal-vs-eschatological blurs. The law holds (all three jointly separable at p=10⁻⁴)
   with this stated soft edge.
2. **Genre proxy is the coarse surah-scale H-NEW-2500 surrogate** (each surah's *dominant*
   register; Q2 is both legislative and narrative). A pericope-scale re-test
   (cross-finding-025's lesson) is the natural sharpening.
3. **f_iltifāt-type and the legal label are correlated by the underlying register** (not
   circular — the proxy uses *yā ayyuhā* substrings, not iltifāt counts — but the
   correlation IS the claim: register is coded in the grammar).
4. **Person/number iltifāt only** (Abdel Haleem types III–VI out of the H-NEW-2390
   detector's scope).

## Classical connection

Vindicates the classical recognition that mode-of-address is register-bound:
- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — the *nawʿ* on al-iltifāt (grammatical
  shift for rhetorical renewal) + the *nawʿ* on al-makkī wa-l-madanī (register basis). The
  thesis that *how* the text addresses (person, particle) tracks *what kind* of passage it
  is, is al-Zarkashī's; cross-finding-028 is its multivariate quantitative confirmation.
- **M. Abdel Haleem, "Grammatical Shift for Rhetorical Purposes," *BSOAS* 55(3):407–432
  (1992)** — the functional type-coding (3rd→1st = divine-narrative-voice; 3rd→2nd =
  honouring/reproaching/commanding) that the iltifāt-type feature operationalizes. The
  47%/0% empirical residual structure of H-NEW-2500 and the 76.9% joint separability of
  H-NEW-2530 are the distributional face of Abdel Haleem's functional reading.
- al-Suyūṭī, *al-Itqān*, nawʿ 1 (*yā ayyuhā alladhīna āmanū* ⇒ Medinan; the legal marker)
  + the qaṣaṣ-genre nawʿ.

## Relation to the other formal laws

- **cross-finding-025/026 (cohesion axis):** cohesion is content-anchored and
  pericope-scoped (025), a law for cross-pericope cohesion but not within-pericope
  chiasmus (026). cross-finding-028 is the orthogonal **register axis** — genre coded in
  particles + person-deixis. Together: the corpus's *content cohesion* and its *discourse
  register* are carried by different linguistic layers.
- **cross-finding-027 (naming axis):** a surah's name marks theme, not the lexical peak.
  028 adds: a surah's register is marked by its grammar, not its content vocabulary.
  Recurring project signature — **the organizing variable lives in a specific thin layer
  (titles / particles / person-deixis), not where naive frequency-intuition expects.**

## The Wave-Q meta-pattern (continued from cross-finding-026)

cross-finding-026 logged a provisional meta-statement: "Quranic structure is cohesive and
positional but not symmetric below block scale, and not iconic at surah scale." Wave-Q
adds a fourth clause, now promoted: **and register-coded at the function-word grain.** The
project's structural map is converging on: cohesive (025/026) + curatorial-named (027) +
register-grammatical (028), with mirror-symmetry and numerology consistently retired.

## Open follow-ups

1. **Pericope-scale re-test** (cross-finding-025's standing prescription): does the
   register-separability sharpen when the unit is a pericope-window rather than a whole
   surah? Predict the legal↔eschatological soft boundary cleans up.
2. **Resolve the legal↔eschatological blur** with a legal-specific *feature* (e.g.
   *kutiba ʿalaykum* / *yā ayyuhā* onset density) added to the vector — but only as a NEW
   pre-registered test, not a post-hoc tune.
3. **Cross-corpus baseline:** does pre-Islamic poetry / Bukhari hadith show the same
   particle-grain register-coding, or is the *idh ⊥ idhā* register-dichotomy
   Quran-specific?
4. Extend the person-iltifāt feature to Abdel Haleem types III–VI when a detector exists.

## Files

- This codification.
- Keystone: `h-new-2530-register-grammar.md`, `prereg-h-new-2530-register-grammar.md`,
  `scripts/h-new-2530.py`, `csv/h-new-2530.json`.
- Pillars: `h-new-2520-pericope-onset.md` (§10.129), `h-new-2250-particle-cascade.md`
  (§10.88), `h-new-2490-doubling-emphasis.md` (§10.130),
  `h-new-2500-iltifat-genre-crosstab.md` (§10.131).
- Parent laws: `cross-finding-025-formal-scale-of-aggregation-law.md`,
  `cross-finding-026-formal-cohesion-vs-chiasmus-bifurcation.md`.

---

*Cross-finding-028 codified 2026-05-30 (Wave-Q) by Waiel Al-Shujaa. Register is coded in
the grammar; the convergence is a law; the joint test decides. Bismillāhi al-Raḥmāni
al-Raḥīm.*
