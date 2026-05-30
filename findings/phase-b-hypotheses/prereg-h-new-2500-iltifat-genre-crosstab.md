---
id: H-NEW-2500
title: Iltifāt TYPE × GENRE cross-tabulation — PRE-REGISTRATION
date: 2026-05-30
phase: B
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
parent: H-NEW-2390
---

# PRE-REGISTRATION — H-NEW-2500 — Iltifāt TYPE × GENRE cross-tabulation

**This file is locked BEFORE any computation of the cross-tabulation, the
association statistics, or the permutation null. Its SHA-256 is embedded in
`scripts/h-new-2500.py` and verified at runtime (fail-fast on mismatch), per
Protocol §1.2.** The genre proxy below was designed and its 4 cell-populations
inspected (to forestall structural zeros) BEFORE this lock; the iltifāt-TYPE ×
GENRE contingency itself and its association test are computed only AFTER the lock.

---

## 0. Motivation and relation to H-NEW-2390

H-NEW-2390 (§10.104) established that **clause-scale (within-verse) iltifāt density
is region-distinguishing** (Meccan > Medinan, Δ=+0.0375, p=0.0097) — recovering the
genre signal the verse-boundary detector (H-NEW-2200) washed out. That finding
counted iltifāt loci *agnostic of type*: it asked only "how dense are person/number
shifts?" It did not ask **which KIND of shift goes with which KIND of passage.**

H-NEW-2500 builds the richer map. We REUSE the exact locus catalogue from
`findings/phase-b-hypotheses/csv/h-new-2390.json` (16,998 within-verse shifts in 4,515
verses; each locus carries `surah`, `verse`, `person_from/to`, `number_from/to`,
`person_shift`, `number_shift`, `kind`) — **the detector is NOT recomputed.** We
cross-tabulate the iltifāt TYPE of each locus against the GENRE of its surah, and test
whether type is non-randomly associated with genre.

Classical anchor for the question: al-Zarkashī (*al-Burhān fī ʿulūm al-Qurʾān*, the
*nawʿ* on al-iltifāt) and Abdel Haleem (1992 *BSOAS* 55(3):407–432) both note that the
*functions* of iltifāt are register-bound — honoring/reproaching/threatening (a
*direct-address* function) vs the divine narrative voice turning toward itself (a
*majesty/narration* function). Abdel Haleem's own type-counts (3rd→1st >140 "divine
narrative voice"; 3rd→2nd ~60 "honouring, reproaching, threatening, requesting") are
*functionally* genre-coded; H-NEW-2500 tests whether that functional coding leaves a
*distributional* trace at corpus scale.

---

## 1. The GENRE proxy (LOCKED — deterministic, surah-scale)

Genre is assigned **per surah** (the reproducible, pre-registerable unit; the locus
catalogue and the per-surah region/length metadata both key on the surah, and
pericope boundaries are not a pre-registerable object without subjective segmentation —
a garden-of-forking-paths hazard). Each of the 114 surahs receives **exactly one** of
four genre labels by the following **hierarchical, deterministic decision procedure**,
evaluated top-to-bottom (first match wins). All inputs are textual proxies:

- region `type ∈ {meccan, medinan}` from `quran-text/quran-no-tashkeel.json`;
- surah index `s` (1..114) as the mushaf-length-band proxy (s ≥ 78 = short mufaṣṣal,
  the juzʾ-30 cut used by H-NEW-2210 / H-NEW-2250);
- marker-lexicon counts (substring, no-tashkeel orthography retaining hamza/madda),
  word-count `w` from whitespace tokenization.

Marker lexicons (LOCKED):
- **LEGAL** = {`يا أيها الذين آمنوا` (yā ayyuhā alladhīna āmanū, "O you who believe"),
  `كتب عليكم` (kutiba ʿalaykum, "it is prescribed upon you")}. The covenant-community
  legislative address; al-Suyūṭī *Itqān* nawʿ 1 records the *yā ayyuhā alladhīna āmanū*
  ⇒ Medinan rule (empirically validated 0/20 Meccan in H-NEW-2270).
- **ESCHAT** = {`يوم القيامة` (yawm al-qiyāma), `الساعة` (al-sāʿa), `يومئذ` (yawmaʾidhin),
  `جهنم` (jahannam), `إذا ` (idhā, "when…" eschatological conditional head, the
  juzʾ-30 cascade marker of H-NEW-2250)}.
- **NARRATIVE** = qaṣaṣ speech-frame `قال` (qāla, "he said"), the dominant marker of
  the prophetic-narrative register (H-NEW-2260 prophet-cycles).

Decision procedure (LOCKED priority):
1. **`legal_medinan`** — `type == medinan` AND (count(`يا أيها الذين آمنوا`) +
   count(`كتب عليكم`)) ≥ 1. (The Medinan legislative-covenant register.)
2. **`narrative`** — qāla-density = 100·count(`قال`)/w ≥ 1.0 per 100 words. (Prophetic
   qaṣaṣ register.)
3. **`eschatological_mufassal`** — s ≥ 78 OR ESCHAT-density = 100·Σcount(ESCHAT)/w
   ≥ 1.5 per 100 words. (The short-mufaṣṣal / Day-of-Judgment register.)
4. **`liturgical_didactic`** — residual. (Meccan disputational/`qul`-discourse +
   hymnic/devotional surahs that are not dominantly qaṣaṣ, not short-eschatological,
   and not Medinan-legislative — e.g. the `qul`-heavy Q 6, Q 10, Q 67, Q 72 and the
   hymnic Q 55, Q 56.)

This procedure was designed and the resulting partition inspected for cell balance and
absence of structural zeros (n = 31 narrative / 20 legal / 40 eschatological-mufaṣṣal /
23 liturgical-didactic) BEFORE this lock. The procedure is fixed; no threshold may be
re-tuned after the cross-tab is seen (Protocol §1.2). The full surah→genre map is
emitted in the JSON.

**Honest limit (pre-stated):** the genre proxy is a coarse, deterministic surrogate for
a real exegetical genre judgment; surahs are internally heterogeneous (Q 2 al-Baqara is
both legislative and narrative). The proxy captures each surah's *dominant* register by
its strongest distinctive marker, in the locked priority order. The `liturgical_didactic`
cell is an explicit residual, reported as such.

## 2. The iltifāt TYPE taxonomy (LOCKED)

Each within-verse locus in `h-new-2390.json` is tagged with one or more **type-classes**
from a fixed 5-class taxonomy (a locus of `kind == both` carries one person-tag AND one
number-tag; person-only or number-only loci carry a single tag):

- **`P_3<->1`** — person shift 3rd ↔ 1st (ghayba ↔ mutakallim): the divine narrative
  voice turning toward / away from itself (Abdel Haleem types I.1 + I.2, the most
  numerous; "divine narrative voice").
- **`P_2<->3`** — person shift 2nd ↔ 3rd (ḥuḍūr ↔ ghayba): direct address ↔ absent
  reference (Abdel Haleem types I.3 + I.4; "honouring, reproaching, threatening,
  requesting").
- **`P_1<->2`** — person shift 1st ↔ 2nd (mutakallim ↔ mukhāṭab): speaker ↔ addressee
  (Abdel Haleem types I.5 + I.6, rare; includes the disputed Q 36:22).
- **`N_S<->P`** — number shift singular ↔ plural. This class contains the **divine
  sg↔pl majesty-shift** (*iltifāt al-ʿadad*; the classical "I/We" majestic plural,
  e.g. Q 75:1-4) as its theologically marked sub-case (person stays 1st, number S↔P);
  reported additionally as a sub-count.
- **`N_dual`** — number shift involving the dual (S↔D, D↔P, D↔S, P↔D): the marginal
  dual-iltifāt class.

(Tense/mood, addressee, case-marker, and noun-for-pronoun iltifāt — Abdel Haleem types
III/IV/V/VI — are NOT in the H-NEW-2390 person/number detector and are out of scope
here, stated as a coverage limit.)

The contingency unit is the **type-tag** (Σ = 23,963 tags over 16,998 loci, since
`both`-loci contribute two tags). The permutation null (below) permutes only the
surah→genre label assignment and preserves the exact tag structure, so the tag-multiplicity
does not bias the null — the same statistic is computed identically on observed and
permuted labels.

## 3. Pre-registered hypothesis and LOCKED direction

**Pre-flight thesis (LOCKED): iltifāt TYPE is NON-randomly associated with GENRE.** The
type×genre contingency table departs from independence beyond what a surah→genre
label-permutation null produces.

### H1 (PRIMARY — association) — LOCKED DIRECTION: positive association
The χ² statistic of the 5(type) × 4(genre) contingency table, and the normalised
mutual information NMI(type; genre), each EXCEED the 95th percentile of the
surah-label-permutation null. (One-sided, locked: more association than chance, never
less.) Bonferroni k = 2 over {χ², NMI}, α_bon = 0.025. p = (#{stat_perm ≥ stat_obs} + 1)
/ (n_perm + 1), seed 20260509, 10000 perms. The exchangeable unit is the **surah** (its
genre label is shuffled; all of a surah's loci move with it, preserving the
within-surah type-clustering that would otherwise inflate association).

### H2 (SECONDARY — locked dominant-type prediction) — DIRECTION-LOCKED PER GENRE
A specific, falsifiable register prediction locked BEFORE computing the standardized
residuals, derived from Abdel Haleem's functional coding + the visual structure of
classical examples:

- **legal_medinan → over-represented in `P_2<->3`** (ḥuḍūr↔ghayba direct-address):
  the legislative-covenant register addresses the believing community directly
  ("O you who believe…") then refers to the absent third party / Allāh's ruling —
  the "honouring/reproaching/commanding" direct-address function. **LOCKED:** the
  legal_medinan × `P_2<->3` standardized Pearson residual is POSITIVE and is the
  largest positive residual in the `legal_medinan` row.
- **narrative → over-represented in `P_3<->1`** (ghayba↔mutakallim divine-narrative
  voice): qaṣaṣ is the home of Abdel Haleem's most-numerous type, "the divine
  narrative voice turning toward itself." **LOCKED:** the narrative × `P_3<->1`
  standardized Pearson residual is POSITIVE.

These two cell-direction locks are the H2 prediction. PASS = both hold (each residual
positive, with the legal `P_2<->3` residual top-of-row). A REVERSAL of either locked
direction is a pre-commit violation, published as NULL with full prominence.

### Descriptive (no new p-value, MW-7-capped)
Report the dominant type per genre (largest standardized residual), the full residual
matrix, the per-type-per-genre row/column profiles, and the divine sg↔pl majesty
sub-count by genre. Any pattern beyond H1/H2 is exploratory and MW-7-capped.

## 4. Success / failure criteria (LOCKED)

- **CONFIRMED (type×genre map is real and directionally as predicted):** H1 passes
  (χ² AND NMI each > 95th pct of null at α_bon = 0.025) AND H2 passes (both locked cell
  directions hold).
- **PARTIAL:** H1 passes but H2 (one or both locked cell directions) fails / reverses;
  OR H1 fails but the descriptive structure is clear. Report honestly.
- **NULL (pre-commit honored / REVERSED → full prominence):** H1 fails to reject (the
  table is independence-consistent under the label null) → iltifāt type is genre-blind;
  OR an H2 locked direction reverses → published as pre-commit violation with full
  prominence. Either is a first-class finding (Protocol §1.3, equal NULL prominence).

## 5. Robustness / replication (MW-3, MW-5, MW-6)

- **MW-5 replication:** re-run H1 with second seed 20260510; direction must hold.
- **MW-3 alternative model:** also report **Cramér's V** (effect-size normalisation of
  χ²) and the **person-only** contingency (drop the two number classes; 3 person-types
  × 4 genres) — the association direction should agree.
- **MW-6 instrument-control / sanity:** confirm the reused locus catalogue reproduces
  the H-NEW-2390 census marginals (Σ person-shifts = 12,379; Σ number-shifts = 11,584;
  S↔P = 11,209 type-tags) by assertion — a fail-fast that the JSON was read correctly.

## 6. Rules-tuple

`(no-tashkeel, QAC-v0.4-segment via H-NEW-2390 loci, finite-V[incl IMPV] + PRON
person-number, within-verse type-tag, surah-scale genre proxy [region + s≥78 length-band
+ marker-lexicon], Hafs-Kūfan, Mashriqī)`. Genre marker counts use the no-tashkeel
substring instrument on `quran-text/quran-no-tashkeel.json`.

## 7. Classical anchoring (cited, not vague)

- al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*, the *nawʿ* on al-iltifāt (the change of
  speech from one mode to another, for freshness and to renew the listener's interest);
  and nawʿ on al-makkī wa-l-madanī (the register/genre proxy basis).
- M. Abdel Haleem, "Grammatical Shift for Rhetorical Purposes: Iltifāt and Related
  Features in the Qurʾān", *BSOAS* 55(3):407–432 (1992) — the type-by-function coding
  (3rd→1st divine-narrative-voice; 3rd→2nd honouring/reproaching/commanding) that H2
  operationalizes; catalogue at
  `data/literature/balagha/1992-abdel-haleem-grammatical-shift-iltifat-bsoas.md`.
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 1 (*yā ayyuhā alladhīna āmanū* ⇒
  Medinan) — the legal_medinan genre-marker anchor (validated in H-NEW-2270).

## 8. Output files

- pre-reg (this file): `findings/phase-b-hypotheses/prereg-h-new-2500-iltifat-genre-crosstab.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2500.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2500.json`
- finding: `findings/phase-b-hypotheses/h-new-2500-iltifat-genre-crosstab.md`

*Pre-registration locked 2026-05-30 by Waiel Al-Shujaa, before any computation of the
cross-tabulation or its association test. Bismillāhi al-Raḥmāni al-Raḥīm.*
