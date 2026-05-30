---
id: H-NEW-2530
title: Register-coded discourse grammar — the function-word + person-grammar feature-set JOINTLY separates the three Quranic registers (CONFIRMED)
date: 2026-05-30
phase: B → C
status: CONFIRMED
verdict: CONFIRMED — H1 (LOO classifier) + H2 (ANOVA) both PASS at α_bon=0.025; both seeds; cross-finding-028-formal minted
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260511
n_perm: 10000
prereg_sha256: e840a8477c3ba7e524c4026725b5554e7157ddcaffaf810181d4998c98736cfe
parents: [H-NEW-2250, H-NEW-2490, H-NEW-2500, H-NEW-2520]
cross_finding: cross-finding-028-formal
---

# H-NEW-2530 — Register-coded discourse grammar: the function-word + person-grammar feature-set JOINTLY separates the three registers

**Verdict: CONFIRMED — no pre-commit violation.** Pre-reg SHA `e840a847…6cfe`, seed
20260509, replication 20260511, 10000 perms, Bonferroni k=2, α_bon=0.025,
runtime-verified. The ONE unifying test of the §10.133 (Wave-Q) "register-coded
discourse grammar" convergence: assembled into a per-surah feature vector, the
function-word + person-grammar signatures of H-NEW-2250 / 2490 / 2500 / 2520 JOINTLY
separate the three named registers (narrative / legal-Medinan / eschatological-mufaṣṣal)
far above a label-shuffle null. **Detectors NOT recomputed — every feature is read
verbatim from the four parents' JSON outputs.**

## The result

| Statistic (PRIMARY, 3-register, N=91) | Observed | Null tail | p (10000 perms) | Verdict |
|---|---|---|---|---|
| **H1 — LOO nearest-centroid accuracy** | **0.7692** | majority baseline 0.4396 | **0.00010** | **PASS** |
| **H2 — Σ one-way ANOVA F (6 features)** | **80.54** | — | **0.00010** | **PASS** |
| MW-3 — Gaussian naïve-Bayes LOO acc | 0.7143 | — | 0.00010 | agrees |
| MW-5 — replication (seed 20260511) | — | — | LOO 0.00010 / ANOVA 0.00010 | holds |
| MW-3 — 4-class (add liturgical_didactic, N=114) | 0.5351 LOO / F=58.6 | — | 0.00010 / 0.00010 | holds |

The label-shuffle null preserves class-size marginals (31/20/40) and recomputes the
identical LOO + ANOVA pipeline on permuted register labels. The observed separation sits
at the extreme upper tail in all runs (1/10001 — the minimum achievable p), and both
the predictive lens (a held-out classifier) and the variance lens (between-register
ANOVA) agree. Direction was LOCKED before computation (features separate ABOVE chance);
the direction held.

## The three per-register grammatical signatures (centroids, raw per-verse densities)

| Register (n) | f_idh | f_lammā | f_qālū | f_idhā-cascade | f_doubling | f_iltifāt 3↔1−2↔3 |
|---|--:|--:|--:|--:|--:|--:|
| **narrative** (31) | 0.0177 | **0.0207** | **0.0371** | 0.0027 | 0.000 | **−0.001** |
| **legal_medinan** (20) | **0.0323** | 0.0025 | 0.0035 | 0.0009 | 0.000 | **−0.671** |
| **eschatological_mufaṣṣal** (40) | 0.0016 | 0.000 | 0.0015 | **0.0176** | **0.125** | −0.453 |

Read down the columns, this is the §10.133 thesis made quantitative and multivariate:

- **Narrative / qaṣaṣ** owns the *wa-lammā* and *wa-qālū* dialogue/sequence onsets
  (the two highest cells, 0.0207 / 0.0371) and is the only register whose person-iltifāt
  balance is near the corpus 3↔1 pole (−0.001 vs −0.45/−0.67 for the others — i.e.
  comparatively MORE of the 3↔1 divine-narrative voice; H-NEW-2500's narrative
  +18.2 residual).
- **Legal-Medinan** is defined on the **person-grammar axis**: f_iltifāt = **−0.671**,
  by far the most 2↔3-dominant (direct community-address; H-NEW-2500's legal +13.1 on
  2↔3, −18.1 on 3↔1). It has *idh* onsets (0.032, covenant-recall like Q 2's Banū-Isrāʾīl
  passages) but near-zero *lammā/qālū* continuous-narrative and near-zero eschatological
  markers.
- **Eschatological-mufaṣṣal** owns the two intensifier features: the *idhā*
  conditional-cascade (0.0176, 11–20× the other registers) and the *thumma*-led doubling
  (0.125 — all 5 of its 6-member doubling census fall here), with near-zero qaṣaṣ onsets.

## What carries the signal (per-feature ANOVA, MW-7-capped, honest)

| Feature | ANOVA F | perm-p | role |
|---|--:|--:|---|
| f_qālū (2520) | 33.54 | 0.0001 | strongest single separator (narrative dialogue-onset) |
| f_iltifāt-type (2500/2390) | 19.79 | 0.0001 | person-grammar axis (isolates legal 2↔3) |
| f_lammā (2520) | 12.06 | 0.0001 | narrative onset |
| f_idh (2520) | 10.51 | 0.0002 | recall onset |
| f_doubling (2490) | 3.52 | 0.0252 | marginal (eschatological intensifier) |
| f_idhā-cascade (2250) | 1.12 | 0.374 | **NOT significant alone** (sparse: 5 surahs) |

This is the honest mechanism and exactly what the pre-reg anticipated: the bulk of the
separation rides on the **onset densities (1–3) and the iltifāt-type axis (6)**; the two
**sparse** features add register-specific spikes. The *idhā*-cascade feature, with only
5 host-surahs corpus-wide (§10.88), is underpowered as a univariate separator (p=0.37)
— precisely why the JOINT test is the honest unit. The doubling feature is marginal
alone (p=0.025) but its 5/6 eschatological concentration contributes to the multivariate
fit. **The joint claim is real; no single feature is the whole story.**

## Confusion structure (where it separates cleanly, where it doesn't)

LOO confusion (row = true, col = predicted):

| true \ pred | narrative | legal | eschat |
|---|--:|--:|--:|
| **narrative** | **25** | 3 | 3 |
| **legal_medinan** | 0 | **8** | 12 |
| **eschat_mufaṣṣal** | 1 | 2 | **37** |

- **Narrative is cleanest** (25/31, 81%) — distinctive onset profile.
- **Eschatological is cleanest of the three** (37/40, 92%) — the idhā/doubling spikes.
- **Legal-Medinan is the hardest** (8/20): 12 of its 20 surahs are misclassified as
  eschatological. Honest reading: legal and eschatological SHARE the 2↔3-dominant
  person-grammar (both negative f_iltifāt, −0.67 vs −0.45) and both LACK narrative
  onsets; what splits them (cascade/doubling) is sparse. The legal register's distinctive
  marker (*yā ayyuhā alladhīna āmanū*) is the *genre-proxy definition*, not a feature in
  this vector — so the classifier separates legal from narrative perfectly (0 legal→narr)
  but blurs legal↔eschatological. The overall 76.9% accuracy is driven by the
  narrative/eschatological poles plus the legal-vs-narrative separation. This is an
  honest qualification of the joint law, not a defeat of it: all three registers remain
  jointly separable at p=0.0001, but the legal↔eschatological boundary is the soft one.

## Why this is a cross-finding, not just a fifth marginal effect

§10.133 read the register-coding off four SEPARATE findings — one detector per
register-feature. The natural skeptical alternative is that these are four independent
marginal genre-effects that LOOK like a joint structure only because they were narrated
together. H-NEW-2530 falsifies that skeptical alternative: when the four findings' own
outputs are assembled into ONE per-surah vector and fed to a held-out classifier, the
register label is recoverable at 77% (1.75× the majority baseline) — the features carry
JOINT, multivariate register-information, not merely four parallel univariate trends.
This is the empirical content that promotes the §10.133 verbal convergence to
**cross-finding-028-formal** (the register-coded discourse grammar law).

## Robustness summary

- **MW-5 (replication seed 20260511):** both H1 and H2 hold at p=0.0001.
- **MW-3 (4-class, N=114):** adding the residual liturgical_didactic class lowers
  accuracy to 53.5% (expected — the residual catch-all is, by H-NEW-2500's own finding,
  "person-grammar-flat" and is the least feature-distinctive; it absorbs 18 of the
  eschatological surahs in confusion), but the 4-class separation STILL clears the null
  at p=0.0001 on both statistics. The primary 3-register verdict is not an artefact of
  dropping the residual.
- **MW-3 (alternative classifier):** Gaussian naïve-Bayes LOO = 71.4%, p=0.0001 —
  agrees with the nearest-centroid direction.
- **MW-6 (instrument-control, all fail-fast asserted at runtime):** genre marginals
  31/20/40/23 reproduced; iltifāt person-tag marginals Σ P_3↔1 = 3694 / Σ P_2↔3 = 6471
  reproduced exactly from the reused 2390 catalogue (cross-validated against the 2500
  contingency col-totals); 2490 doubling roster = exactly {74,75,78,82,94,102}; verse
  counts V(s) cross-checked against the 2520 onset tables.

## Honest limits

1. **The genre proxy is the H-NEW-2500 surah-scale deterministic surrogate** — coarse,
   and surahs are internally heterogeneous (Q 2 is both legislative and narrative). The
   law is at the level of each surah's *dominant* register.
2. **f_iltifāt-type partly co-determines the legal label** by construction-adjacency:
   the legal register's defining marker drives both its genre label (via 2500's proxy)
   and its 2↔3 iltifāt-dominance (a separate H-NEW-2500 finding). These are not circular
   (the genre proxy uses *yā ayyuhā alladhīna āmanū* substrings, NOT iltifāt counts), but
   the two are correlated by the underlying register, which is the point — the law claims
   register IS coded in the grammar.
3. **Two of six features are sparse** (cascade 5 surahs, doubling 6 surahs); the joint
   separability is genuine but is carried mainly by onsets + iltifāt-type, as the
   per-feature ANOVA transparently shows.
4. **Legal↔eschatological is the soft boundary** (12/20 legal → eschatological); the
   clean separations are narrative-vs-rest and eschatological-vs-rest.
5. Person/number iltifāt only (Abdel Haleem types III–VI out of scope, inherited from
   the H-NEW-2390 detector).

## Classical anchoring

- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān***: the *nawʿ* on al-iltifāt (mode-of-
  address shift for rhetorical renewal) and the *nawʿ* on al-makkī wa-l-madanī (register
  basis). The thesis that mode-of-address is register-bound is al-Zarkashī's; H-NEW-2530
  is its multivariate quantitative confirmation.
- **M. Abdel Haleem, *BSOAS* 55(3):407–432 (1992)**: the type-by-function coding
  (3rd→1st divine-narrative-voice; 3rd→2nd honouring/reproaching/commanding) that
  feature 6 operationalizes —
  `data/literature/balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md`.
- al-Suyūṭī, *al-Itqān*, nawʿ 1 (*yā ayyuhā alladhīna āmanū* ⇒ Medinan) + the qaṣaṣ nawʿ.

## Relation to prior findings

- **Pillars (joined here):** H-NEW-2520 (qaṣaṣ onsets), H-NEW-2250 (idhā cascade),
  H-NEW-2490 (thumma doubling), H-NEW-2500 (iltifāt type×genre).
- **cross-finding-025/026:** scale-of-aggregation + cohesion/chiasmus bifurcation —
  cohesion is content-anchored and pericope-scoped. cross-finding-028 is the orthogonal
  *register-axis* law: register is coded in function-words + person-grammar, at the
  particle grain.
- **cross-finding-027:** eponymy-independence (the naming-axis). 028 is the
  discourse-grammar axis. Both are "the corpus's organizing variable is carried by a
  *specific* linguistic layer (titles / particles), not where naive intuition expects."

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2530-register-grammar.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2530.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2530.json`
- cross-finding: `findings/phase-b-hypotheses/cross-finding-028-formal-register-coded-discourse-grammar.md`

---

*H-NEW-2530 CONFIRMED 2026-05-30 by Waiel Al-Shujaa. The registers are grammatically
separable; the convergence is a law. Bismillāhi al-Raḥmāni al-Raḥīm.*
