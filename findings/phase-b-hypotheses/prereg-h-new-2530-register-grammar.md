---
id: H-NEW-2530
title: Register-coded discourse grammar — joint function-word + person-grammar separability of the three Quranic registers — PRE-REGISTRATION
date: 2026-05-30
phase: B → C
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
parents: [H-NEW-2250, H-NEW-2490, H-NEW-2500, H-NEW-2520]
cross_finding: cross-finding-028-formal (register-coded discourse grammar) — minted IFF this test PASSES
---

# PRE-REGISTRATION — H-NEW-2530 — Register-coded discourse grammar: do the function-word + person-grammar signatures JOINTLY separate the three registers?

**This file is locked BEFORE any computation of the per-surah feature matrix, the
classifier, the ANOVA, or the permutation null. Its SHA-256 is embedded in
`scripts/h-new-2530.py` and verified at runtime (fail-fast on mismatch), per
Protocol §1.2.** The feature definitions and the genre proxy (reused verbatim from
H-NEW-2500) were fixed, and the per-register *feature-availability* census (nonzero
counts — NOT the separation statistic) inspected to forestall structural zeros,
BEFORE this lock. The separation statistic itself (LOO classifier accuracy, ANOVA F)
and its permutation null are computed only AFTER the lock.

---

## 0. Motivation — the §10.133 convergence as ONE falsifiable claim

Wave-Q (§10.133, 2026-05-30) observed a convergence across four independently
pre-registered findings: the corpus appears to encode discourse **register (genre)**
in its choice of **function-words and person-grammar**, at the single-particle grain:

- **Narrative / qaṣaṣ:** opens on *wa-idh / wa-lammā / wa-qālū* (H-NEW-2520, 4–14×
  concentrated in s ≤ 50) and runs the **3↔1 divine-narrative-voice** iltifāt
  (H-NEW-2500, std-residual +18.2).
- **Legal-Medinan:** runs the **2↔3 direct-community-address** iltifāt (H-NEW-2500,
  +13.1), keyed by *yā ayyuhā alladhīna āmanū*.
- **Eschatological / mufaṣṣal:** runs the *idhā* conditional-cascade (H-NEW-2250) and
  the *thumma*-led doubling-for-emphasis intensifier (H-NEW-2490).

§10.133 asserted these registers are "mutually exclusive on the particle/person axis."
That assertion has so far been read off **separate** findings (one detector per
register-feature), never tested as a **joint** claim. H-NEW-2530 converts the verbal
convergence into ONE pre-registered, falsifiable test: **assembled into a per-surah
feature vector, do the function-word + person-grammar features JOINTLY separate the
three register labels above a label-shuffle null?** If yes → the convergence is a real,
multivariate, register-coding law (promote to cross-finding-028-formal). If no
(features do not separate registers above chance) → the convergence was an artefact of
reading four marginal effects as a joint structure, and is published as NULL with full
prominence (the registers would NOT be grammatically separable — itself a first-class
finding). Direction is LOCKED below.

This test **reuses the existing finding outputs verbatim**; no detector is recomputed.
All six features are read from `csv/h-new-2250.json`, `csv/h-new-2490.json`,
`csv/h-new-2390.json` (the H-NEW-2500 parent locus catalogue), and `csv/h-new-2520.json`.

## 1. The GENRE proxy (LOCKED — reused verbatim from H-NEW-2500)

Genre is the **surah-scale deterministic proxy of H-NEW-2500**, read directly from
`csv/h-new-2500.json` → `genre_proxy.surah_genre` (114 labels: narrative 31 /
legal_medinan 20 / eschatological_mufassal 40 / liturgical_didactic 23). This proxy is
NOT re-derived; its decision procedure, marker lexicons, and the resulting partition are
fixed by the H-NEW-2500 lock (SHA `ced7003d…5d4c`) and were inspected there before that
lock. The genre map is asserted at runtime to reproduce the 2500 n-per-genre marginals
(MW-6 fail-fast).

**PRIMARY test population = the THREE named registers** of the §10.133 convergence:
`narrative` (31), `legal_medinan` (20), `eschatological_mufassal` (40) — N = 91 surahs.
The residual `liturgical_didactic` (23) is **excluded from the primary test** because
it is not one of the three registers the convergence names (it is, by H-NEW-2500's own
decision-procedure, a residual catch-all that is "person-grammar-flat"; §10.131). It is
re-included in a 4-class **secondary/robustness** run (§5, MW-3) to confirm the primary
verdict is not an artefact of dropping it.

## 2. The per-surah FEATURE VECTOR (LOCKED — 6 features, all from existing outputs)

Each surah s (1..114) receives a 6-dimensional feature vector. All counts are read
from the pre-existing JSONs; NO detector is recomputed. `V(s)` = Hafs-Kūfan verse count
(from the source JSON / equivalently the 2520 per-surah `verses` field). Densities are
per-verse.

1. **`f_idh`** — *wa-idh / idh* narrative-recall onset density.
   `= per_surah.idh[s] / V(s)` from `csv/h-new-2520.json` (0 if absent). (2520)
2. **`f_lamma`** — *fa-lammā / wa-lammā* narrative onset density.
   `= per_surah.lamma[s] / V(s)` from `csv/h-new-2520.json` (0 if absent). (2520)
3. **`f_qalu`** — *wa-qālū / qālū* dialogue-onset density.
   `= per_surah.qalu[s] / V(s)` from `csv/h-new-2520.json` (0 if absent). (2520)
4. **`f_idha_cascade`** — *idhā* eschatological conditional-cascade density.
   `= (Σ length of idhā maximal runs in surah s) / V(s)`, summed over `runs.idha` in
   `csv/h-new-2250.json` (0 if the surah hosts no idhā ≥3-run). (2250)
5. **`f_doubling`** — *thumma*-led adjacent doubling-for-emphasis PRESENCE (binary).
   `= 1` iff surah s appears in `verse_grain_roster` of `csv/h-new-2490.json`, else `0`.
   (2490)
6. **`f_iltifat_type`** — dominant person-iltifāt TYPE axis, **signed 3↔1 vs 2↔3
   balance**.
   Using the H-NEW-2500 type-tagging rule (`scripts/h-new-2500.py` `type_tags`, applied
   to `all_loci` in `csv/h-new-2390.json`): per surah count `n31` = #`P_3<->1` tags and
   `n23` = #`P_2<->3` tags. Feature `= (n31 − n23) / (n31 + n23)` if `n31+n23 > 0`, else
   `0.0`. Range [−1, +1]: **+1 = pure 3↔1 (narrative divine-voice)**, **−1 = pure 2↔3
   (legal direct-address)**, **0 = balanced or no person-iltifāt**. (2500/2390)

**Standardization (LOCKED):** before classification each feature column is z-scored
across the test population (mean 0, sd 1; a column with sd 0 is left at 0 to avoid
division-by-zero). The same z-transform is recomputed inside each permutation on the
permuted-label population's *features* (the features never change; only labels are
permuted — so z-scoring is invariant under permutation and applied once to the fixed
feature matrix). The binary `f_doubling` is z-scored like the rest.

**Honest limit (pre-stated):** features 4 (cascade) and 5 (doubling) are SPARSE by
construction — only ~5 surahs host an idhā cascade and exactly 6 host a doubling
(corpus census, §10.88 / §10.130). They are near-zero for most surahs. The bulk of the
multivariate signal therefore rides on the onset densities (1–3) and the iltifāt-type
axis (6); the sparse features add register-specific spikes (e.g. eschatological
doublings). This is a property of the corpus (the markers are genuinely rare), not a
defect of the test — and it is exactly why a JOINT test is the honest unit: any single
sparse feature would be underpowered alone.

## 3. Pre-registered hypothesis and LOCKED direction

**Pre-flight thesis (LOCKED): the 6-feature function-word + person-grammar vector
SEPARATES the three registers — i.e. it predicts the register label JOINTLY above a
label-shuffle null.** Direction is one-sided and LOCKED: the observed separation
statistic EXCEEDS the upper tail of the permutation null (more separable than chance,
never less).

### H1 (PRIMARY — leave-one-out classifier accuracy) — LOCKED DIRECTION: above null
A **leave-one-out (LOO) nearest-centroid classifier** is trained on the z-scored
6-feature matrix over the N = 91 three-register surahs. For each held-out surah, class
centroids are computed from the other 90 surahs (mean feature vector per register), and
the surah is assigned to the register whose centroid is nearest in Euclidean distance;
ties broken toward the larger class then by register-name order (deterministic).
`ACC_obs` = fraction correctly classified.

**LOCKED:** `ACC_obs` exceeds the 1−α_bon upper tail of the label-shuffle null. The
null shuffles the 91 register labels among the 91 surahs (preserving the
class-size marginals 31/20/40) and recomputes LOO accuracy identically. seed 20260509,
10000 perms, `p = (#{ACC_perm ≥ ACC_obs} + 1)/(n_perm + 1)`. PASS iff `p < α_bon`.

### H2 (PRIMARY — summed one-way ANOVA F across features) — LOCKED DIRECTION: above null
Independent of the classifier, the **between-register separability** of the feature set
is measured by `F_sum = Σ_{j=1..6} F_j`, where `F_j` is the one-way ANOVA F-ratio
(between-group / within-group mean-square) of feature j across the three registers.
**LOCKED:** `F_sum_obs` exceeds the 1−α_bon upper tail of the same label-shuffle null
(same seed, same 10000 perms, same permuted-label sets). PASS iff `p < α_bon`.

H1 (predictive) and H2 (associational/variance) are two complementary lenses on the
SAME locked direction (features separate registers above chance). Reporting both is the
MW-3 alternative-statistic protection — a defensible result must hold on both.

Bonferroni **k = 2** over {H1 LOO-accuracy, H2 ANOVA-F}, **α_bon = 0.025**.

### Per-register signature (descriptive, MW-7-capped)
Report each register's mean feature profile (the centroid), the LOO confusion matrix,
and per-feature F_j + permutation-p. Any pattern beyond H1/H2 is exploratory, MW-7-capped
at single-test α = 0.05.

## 4. Success / failure criteria (LOCKED)

- **CONFIRMED → mint cross-finding-028-formal:** H1 PASSES (LOO accuracy p < 0.025) AND
  H2 PASSES (ANOVA F_sum p < 0.025). The function-word + person-grammar feature-set
  JOINTLY separates the three registers above the label-shuffle null. The §10.133
  convergence is a real multivariate law; promote.
- **PARTIAL → do NOT mint cross-finding-028:** exactly one of H1 / H2 passes. Record the
  H-NEW-2530 finding with the partial verdict; the joint claim is suggestive but not
  locked. (Both lenses must agree for a cross-finding-grade promotion.)
- **NULL (pre-commit honored / equal prominence) → do NOT mint cross-finding-028:**
  neither H1 nor H2 rejects the label-shuffle null → the registers are NOT grammatically
  separable on the function-word/person-grammar axis; the §10.133 convergence was four
  marginal effects misread as a joint structure. Published as NULL with full prominence
  (Protocol §1.3). A REVERSAL (observed separation BELOW the null lower tail — the
  features ANTI-separate registers) is a pre-commit violation, published with full
  prominence as REVERSED.

## 5. Robustness / replication (MW-3, MW-5, MW-6)

- **MW-5 replication:** re-run H1 + H2 with a second seed **20260511**; both directions
  must hold.
- **MW-3 alternative model A (4-class):** re-run H1 + H2 on the FULL 4-class partition
  (add the 23 `liturgical_didactic` surahs, N = 114). The primary 3-register verdict
  must not be an artefact of excluding the residual class; report whether the 4-class
  separation also clears α_bon.
- **MW-3 alternative model B (classifier):** report a second classifier — **Gaussian
  naïve-Bayes** (per-feature per-class Gaussian, diagonal covariance, with a small
  variance-floor 1e-9) LOO accuracy and its permutation-p; the H1 direction should agree.
- **MW-6 instrument-control:** assert at runtime that (a) the 2500 surah_genre map
  reproduces n-per-genre 31/20/40/23; (b) the reused 2390 `all_loci` reproduces the 2500
  person-tag marginals (Σ P_3↔1 = 3694, Σ P_2↔3 = 6471 across all 114 surahs — recomputed
  and asserted from the locus catalogue); (c) the 2490 verse-grain doubling roster has
  exactly 6 surah-members and the 2250 idhā runs cover exactly the cascade surah-set.
  Fail-fast on any mismatch.

## 6. Rules-tuple

`(no-tashkeel, orthographic/QAC-v0.4 features via the four parent detectors,
per-surah feature vector, surah-scale 3-register genre proxy [reused H-NEW-2500],
Hafs-Kūfan, Mashriqī)`. Verse counts V(s) from `quran-text/quran-no-tashkeel.json`
(cross-checked against the 2520 per-surah `verses` field). Densities per-verse.

## 7. Classical anchoring (cited, not vague)

- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — the *nawʿ* on al-iltifāt (grammatical
  shift for rhetorical renewal) and the *nawʿ* on al-makkī wa-l-madanī (the register/genre
  basis); al-Zarkashī's recognition that mode-of-address is genre-bound is the classical
  root of the register-coding thesis tested here.
- **M. Abdel Haleem, "Grammatical Shift for Rhetorical Purposes: Iltifāt and Related
  Features in the Qurʾān", *BSOAS* 55(3):407–432 (1992)** — the type-by-function coding
  (3rd→1st divine-narrative-voice; 3rd→2nd honouring/reproaching/commanding) that
  feature 6 operationalizes; catalogue at
  `data/literature/balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md`.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (*yā ayyuhā alladhīna āmanū* ⇒
  Medinan, the legal_medinan marker) and the qaṣaṣ-genre nawʿ (the narrative register).

## 8. Output files

- pre-reg (this file): `findings/phase-b-hypotheses/prereg-h-new-2530-register-grammar.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2530.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2530.json`
- finding: `findings/phase-b-hypotheses/h-new-2530-register-grammar.md`
- cross-finding (IFF CONFIRMED): `findings/phase-b-hypotheses/cross-finding-028-formal-register-coded-discourse-grammar.md`

*Pre-registration locked 2026-05-30 by Waiel Al-Shujaa, before any computation of the
feature matrix, the classifier, the ANOVA, or the permutation null. Bismillāhi
al-Raḥmāni al-Raḥīm.*
