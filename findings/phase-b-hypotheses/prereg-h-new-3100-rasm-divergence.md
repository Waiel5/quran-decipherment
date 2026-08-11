---
id: H-NEW-3100
title: The dagger-alef convention is a deciding parameter for the rasm divergence census — PRE-REGISTRATION
date: 2026-08-09
phase: B
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
seed: 20260509
n_perm: 10000
frontier_item: F-9 (rasm / imla)
parents: [H-NEW-2740, AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE, cross-finding-029, cross-finding-030]
supersedes: nothing
replicates: nothing
---

# PRE-REGISTRATION — H-NEW-3100 — Is the F-9 divergence census decided by the dagger-alef convention?

**Locked BEFORE any conditioned statistic, any null and any cross-tabulation. SHA-256
embedded as `EXPECTED_PREREG_SHA` in `scripts/h-new-3100.py`, runtime-verified with
`SystemExit` on mismatch.**

---

## 0. Why this is not the test that was dispatched, and not a re-derivation

The dispatch asked whether rasm divergence clusters by register or position. **That
question was answered on 2026-08-07 by `h-new-2740-rasm-divergence.md`, NULL on all five
registered inferences.** A first draft of this pre-registration duplicated its I2 and
I3a. It is not being run. In particular the draft's H1 was the *unconditioned*
verse-final enrichment, which H-NEW-2740 §Headline identifies explicitly as "real
arithmetic and a worthless inference": 1.93x at p = 1e-4 unconditioned, p = 0.10 once
conditioned on lexical identity.

**What is open is one level down.** H-NEW-2740 locked a single orthographic convention
and never varied it. This lane arrived at the opposite convention by a different route —
the four normaliser assertions in the dispatch brief force it — and the two disagree by
a factor of two on the size of the divergence set. Under `cross-finding-029`, a
parameter that moves a census by 2x and was never recorded as a choice is the deciding
parameter, and establishing that is not a re-derivation of anything.

---

## 1. The two conventions

The Uthmani text writes 9,838 U+0670 SUPERSCRIPT ALEF (dagger alef); the simple text
writes 3,330. It marks a long /a:/ that the rasm does not write with a full alef.

| | convention | dagger alef | consequence |
|:--|:--|:--|:--|
| **A** | `bare()` in `scripts/arabic_normaliser.py` | a LETTER: U+0670 -> U+0627 | the omitted alef is restored, so hadhf al-alif is not a divergence |
| **B** | `bare_mark()`, H-NEW-2740's `skeleton()` convention | a MARK: U+0670 deleted | hadhf al-alif is a divergence |

**Neither is wrong.** A is what the dispatch's assertion
`bare("ya'ayyuha") == bare("ya") + bare("'ayyuha")` forces, because the joined form
carries its alef as a dagger; A is therefore the only convention under which the
vocative-merge question of Deliverable 2 is answerable. B is the classical analysis:
al-Suyuti's first qa'ida is *al-hadhf*, and hadhf al-alif is the case it opens with.

**Both are implemented and both are run on every quantity below.** No headline is
reported under one convention alone.

### 1.1 Pre-lock observation, disclosed

The census sizes were computed before this lock: **A = 4,951 divergent 1:1 pairs
(6.05%), B = 10,065 (12.29%), A a strict subset of B, 5,114 tokens and 1,479 distinct
skeleton-pairs visible only under B.** That is the observation that motivated rewriting
this file, so concealing it would be worthless. **No conditioned statistic, no
positional rate, no register rate and no null was computed.** §4 is what is locked.

---

## 2. Data and inputs

- `data/alt-text/quran-uthmani-txt.txt`, `data/alt-text/quran-simple-txt.txt` — 6,236
  verse lines each after dropping blank and `#` lines.
- `quran-text/quran-no-tashkeel.json` — (surah, ayah) references in canonical order only.
- `findings/phase-b-hypotheses/csv/h-new-2500.json` — the **stored**
  `genre_proxy.surah_genre` labels. The matcher is NOT re-run: per
  `AUDIT-REGISTER-PROXY-ORTHOGRAPHY-DEPENDENCE` it returns zero on both files this lane
  reads, so re-running it would silently empty the legal class.
- `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` — al-Itqan,
  al-naw' al-sadis wa-l-sab'un, for the qa'ida mapping in §5.

All five SHA-256 hashed into the run manifest.

**Instrument gate:** `python3 scripts/arabic_normaliser.py` must exit 0 before any
counting. Its assertion results are copied into the manifest.

---

## 3. ARM 1 — DESCRIPTIVE census under both conventions

No inference. Reported, not tested:

1. 1:1 aligned pairs; divergent count and rate under A and under B; |B \ A|; |A \ B|.
2. Distinct skeleton-pairs under each.
3. **Lexical determinism, both conventions.** Over orthographic types of the SIMPLE
   token: never-divergent / always-divergent / alternating, and the share of divergent
   tokens belonging to lexically invariant types. **This is H-NEW-2740's load-bearing
   95.74%.** Whether it survives the convention flip is reported.
4. Merge-site classification (Deliverable 2), reproduced in the manifest.

## 4. ARM 2 — the single registered INFERENCE

> **Is the verse-final enrichment of rasm divergence, conditioned on lexical identity,
> convention-stable?**

- **Population:** all 1:1 aligned pairs. **Strata:** the bare simple token (the lexeme
  proxy — orthographically neutral between the two conventions by construction, since it
  is taken from the simple text, which contains no dagger-alef ambiguity of the kind at
  issue).
- **Statistic:** `RR = P(DIVERGENT | verse-final) / P(DIVERGENT | non-final)`.
- **Null (within-lexeme permutation):** within each stratum, permute the DIVERGENT
  labels across that stratum's tokens. Strata whose tokens are all-divergent or
  all-non-divergent are invariant under this permutation and contribute nothing; the
  count of **informative tokens** (tokens in alternating strata) is reported, and it is
  the honest N of this test. Seed 20260509, 10,000 draws.
- **p:** one-sided upper-tail, `(1 + #{RR_null >= RR_obs}) / (1 + n_perm)`.
- **Run separately under convention A and convention B.**

**Family: K = 2** (one test per convention). Project novelty rule: corrected gate 0.005,
**raw per-test gate = 0.005 / 2 = 0.0025**. Equivalently `min(1, 2p) < 0.005`.

### 4.1 Length channels

The unit here is the token, not the surah, so surah-length is not the nuisance; **verse
length is**, because a long verse has more non-final tokens per final one. Three
channels, all three computed, none privileged:

- `C1` = verse token count
- `C2` = log verse token count
- `C3` = surah mean verse length, attached to each token

For each channel the null is re-run with strata refined by channel quintile crossed with
lexeme. **HEADLINE = the WORST (largest) of the three channel p-values, per convention.**
The **dominant** channel — largest |Spearman rho| against the per-token divergence
indicator — is named in the report. `rho(control, treatment)` is reported beside every p
per `cross-finding-030` mechanism 3.

### 4.2 Ties

All statistics are on discrete counts; ties are counted **in** the rejection region
(`>=`), the conservative direction. **The tie fraction — the share of null draws exactly
equal to the observed statistic — is measured and reported for every test.** Any test
with tie fraction > 50% is re-run by exact enumeration where the support permits, and
reported as DEGENERATE and excluded from the family where it does not.

### 4.3 Decision rule — transcribed into `verdict()` line by line

| condition | verdict |
|:--|:--|
| both conventions: headline p < 0.0025 and RR > 1 | **CONVENTION-STABLE PASS** |
| both conventions: headline p >= 0.0025 | **CONVENTION-STABLE NULL** |
| exactly one convention clears | **CONVENTION-DECIDED** — name the convention, report both p and the ratio; this is a `cross-finding-029` deciding-parameter result |
| either convention: p < 0.0025 and RR < 1 | **REVERSE** under that convention |

### 4.4 NULL branch — mandatory if ARM 2 returns NULL

1. **MDE** at 80% power: inject a synthetic verse-final excess of increasing size into
   the observed data, 1,000 injections per size, report the smallest RR clearing 0.0025
   in >= 80%.
2. **Power** against the project reference band low end, **RR = 1.27**
   (`cross-finding-029` anchor 3).
3. **`S*` vs `S_max`** — observed divergent-final count against the maximum attainable
   given the strata marginals. Computed, never asserted.

## 5. ARM 3 — the divergence typology, HAND-CURATED and frozen here

### 5.1 Scope

Over the convention-B divergent set (the superset). Merge sites excluded — they are
Deliverable 2's subject and al-Suyuti's fifth qa'ida, not a spelling divergence.

### 5.2 The types — executable predicates, first fire wins

Each predicate is a rewrite; the type fires if applying it to the Uthmani skeleton
yields the simple skeleton.

| # | type | predicate | al-Suyuti qa'ida |
|:--|:--|:--|:--|
| T1 | `HADHF_ALIF` | insert U+0627 | al-hadhf |
| T2 | `HADHF_YA` | insert U+064A | al-hadhf |
| T3 | `HADHF_WAW` | insert U+0648 | al-hadhf |
| T4 | `HADHF_LAM` | insert U+0644 | al-hadhf |
| T5 | `ZIYADA_ALIF` | delete U+0627 | al-ziyada |
| T6 | `ZIYADA_WAW` | delete U+0648 | al-ziyada |
| T7 | `ZIYADA_YA` | delete U+064A | al-ziyada |
| T8 | `BADAL_YA_ALIF` | U+0649/U+064A <-> U+0627 | al-badal |
| T9 | `BADAL_WAW_ALIF` | U+0648 <-> U+0627 | al-badal |
| T10 | `HAMZ` | fold all hamza carriers to U+0621 on both sides | al-hamz |
| T11 | `BADAL_OTHER` | single non-alef/waw/ya/hamza consonant substitution | al-badal |
| T12 | `MIXED` | two or more of T1-T11 required together | — |

**Number of types defined: 12**, plus `UNASSIGNED`. Declared before counting per
`findings/PROXY-CLAIMS.md`.

### 5.3 Hand-assigned quantity — reporting obligations

Reported: **unambiguous fraction** (exactly one predicate fires), **ambiguous fraction**
(two or more, i.e. T12), **unassigned fraction** (none).

### 5.4 Validation against a computed alternative — locked

The parameter-free alternative is the `difflib` edit signature of the skeleton pair.
Reported, not verdict-entering:

1. **Adjusted Rand Index** between the hand partition and the signature partition.
2. **Purity** of each signature under the modal hand type.

No threshold is set; setting one after seeing the signature list would be circular.

### 5.5 Relation to H-NEW-2740's typology

H-NEW-2740 published a 14-class typology over convention B. **This lane's T1-T12 is not
independent of it** — it was written after reading that table, and the class names are
taken from it. **No agreement statistic between the two typologies is claimed as
evidence**, because they are not independent constructions. What ARM 3 adds is the
A-vs-B split per class: which classes vanish entirely under convention A.

## 6. Classical anchor — VERIFIED, contrary to the dispatch brief

The dispatch stated no orthography anchor is on disk and instructed that it be reported
UNVERIFIED. **That is incorrect and the correction is recorded here.**

- al-Dani, `al-Muqni' fi rasm masahif al-amsar` — **NOT on disk.** Searched: `find` over
  the repository for `*muqni*`, `*tabyin*`, `*hija*`, `*rasm*`; and grep for `al-muqni`,
  `mukhtasar al-tabyin`, `hija' al-tanzil`. No hit.
- Abu Dawud Sulayman b. Najah, `Mukhtasar al-tabyin` — **NOT on disk**, same search.
- `findings/classical-sources/dani-23-site-supplement.tsv` — a **verse-counting** work.
  **NOT an orthography source and not cited as one.**
- **al-Suyuti, `al-Itqan fi 'ulum al-Qur'an`, al-naw' al-sadis wa-l-sab'un, `fi marsum
  al-khatt wa-adab kitabatihi` — ON DISK and VERIFIED BY THIS LANE at
  `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`.** Line 23216 opens
  the naw'; line 23255 carries
  `قلت، وسنحصر أمر الرسم في الحذف والزيادة والهمز والبدل والفصل، وما فيه قراءتان`;
  the qawa'id open at 23257 (al-hadhf), 23336 (al-ziyada), 23397, 23418 (al-wasl
  wa-l-fasl), 23453 (ma fihi qira'atan). Checked line by line by this lane, not taken
  from H-NEW-2740; H-NEW-2740's erratum (23255, not its prereg's 23252) is confirmed
  correct — 23252 is a different sentence.

The qa'ida column in §5.2 is therefore anchored, not asserted. **What remains UNVERIFIED
is any claim about which specific words al-Dani lists**, since al-Muqni' is absent.

## 7. Immutability

`runs/h-new-3100/<UTC>/` via `os.makedirs(exist_ok=False)`; artefacts via `open(..., 'x')`.
No run directory is ever deleted or overwritten. Seed 20260509, 10,000 permutations.
