---
id: H-NEW-2070
title: Divine-name verse-final pairing arithmetic + co-occurrence graph (al-fawāṣil)
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 2
bonferroni_family: H-NEW-2070-verse-final-name-pairing (Cell A concentration + Cell B slot-independence)
alpha_bon: 0.025
direction_of_effect: The empirical distribution of verse-final divine-name PAIRS (the last two tokens of a verse, both base-normalizing to one of the 97 single-token al-Tirmidhī names) is MORE concentrated (higher top-5-pair share AND higher normalized Herfindahl–Hirschman index, HHI) than a null in which the name occupying slot-1 (penultimate) and slot-2 (final) are reassigned independently from their observed marginal frequencies. Observed concentration > null concentration.
origin: Classical balāgha al-fawāṣil — al-Bāqillānī (Iʿjāz al-Qurʾān) and al-Zarkashī (al-Burhān, nawʿ on al-fawāṣil) hold that verse-closings are semantically matched to verse content and that paired divine epithets (ghafūrun raḥīm, ʿazīzun ḥakīm, samīʿun ʿalīm) are not arbitrary but constrained collocations. The project has enumerated divine-name CO-OCCURRENCE anywhere-in-verse (H-NEW-140 / H-NEW-170) but has never enumerated the verse-FINAL bigram (the fawāṣila closer) as a distinct structure. This pre-reg locks the verse-final pairing graph and tests its non-randomness.
verdict_ceiling: PASS-DIRECTED (single planned concentration test family under Bonferroni-2; independent replication required for CONFIRMED promotion)
rules_tuple:
  orthography: no-tashkeel
  word_definition: orthographic-token (whitespace split); pure rasm/pause marks excluded
  letter_definition: graphemes
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  name_list_source: data/asma-al-husna.txt (al-Tirmidhī #3507 / al-Walīd b. Muslim chain — gharīb)
  pair_unit: verse-final ORDERED bigram = (base(token[-2]), base(token[-1]))
  base_normalization: strip leading definite article ال if present; strip a single trailing accusative/indefinite alif ا when token length > 3 (so العزيز, عزيز, عزيزا → عزيز; الحكيم, حكيم, حكيما → حكيم). No other normalization.
  divine_set: the 97 single-token al-Tirmidhī names, base-normalized by stripping ال (the 2 multi-token names مالك الملك and ذو الجلال والإكرام cannot occupy a single bigram slot and are excluded by construction).
  pair_admission: a verse is a "divine-pair-closing verse" iff BOTH base(token[-2]) AND base(token[-1]) are in the divine_set.
  concentration_statistic_1: top-5-pair share = (sum of the 5 most frequent ordered-pair counts) / (total divine-pair-closing verses).
  concentration_statistic_2: normalized HHI = sum over distinct pairs of (count/total)^2.
  null_model: slot-independence shuffle. Hold the observed MARGINAL frequency of each base-name in slot-1 (penultimate) and slot-2 (final) fixed; independently permute the slot-1 assignment and slot-2 assignment across the N divine-pair-closing verses, then re-pair. 10,000 perms, seed 20260509 (Cell A) / 20260511 (Cell B uses the same shuffle on a length/period-stratified resample — see below).
---

# H-NEW-2070 pre-registration — divine-name verse-final pairing (al-fawāṣil)

## Origin and classical anchor

A large number of Quranic verses close on a PAIR of divine epithets in the
fixed form *X-un Y-un* (nominative), *X-an Y-an* (accusative), or *al-X al-Y*
(definite): *ghafūrun raḥīm*, *ʿazīzun ḥakīm*, *samīʿun ʿalīm*, *ʿalīmun ḥakīm*,
*tawwābun raḥīm*, *ʿazīzun raḥīm*, *laṭīfun khabīr*, *wāḥidun qahhār*, …

Classical *balāgha* treats these closings under the rubric of **al-fawāṣil**
(verse-end cadences). al-Bāqillānī (*Iʿjāz al-Qurʾān*) and al-Zarkashī
(*al-Burhān fī ʿulūm al-Qurʾān*, the *nawʿ* on al-fawāṣil) argue the closers are
not interchangeable ornament but are **semantically governed collocations**
selected to seal the verse's content — al-Zarkashī's principle of
*murāʿāt al-fāṣila* (observance of the cadence). The empirical corollary, never
tested by this project, is that the verse-final name-PAIRINGS should be **highly
non-random**: a small number of ordered pairs should dominate, and the names
occupying the penultimate and final slots should NOT be independently
combinable.

The project's prior pairing work — H-NEW-140 (classical paired-names cluster,
PASS-DIRECTED) and H-NEW-170 (full 99-name co-occurrence network) — counted
co-occurrence **anywhere in a verse**. This pre-reg is orthogonal: it isolates
the **verse-final ordered bigram** (the fawāṣila closer specifically) and tests
its concentration against a slot-independence null.

## Hypotheses (primary, pre-registered)

**H1 (concentration)**: the top-5 ordered verse-final divine-name pairs account
for a SHARE of all divine-pair-closing verses that EXCEEDS the 97.5th percentile
of the slot-independence null.

**H2 (HHI)**: the normalized Herfindahl–Hirschman index of the verse-final
ordered-pair distribution EXCEEDS the 97.5th percentile of the slot-independence
null.

Both statistics measure pairing concentration; both directions are LOCKED to
"observed > null" (more concentrated than chance). A single test family of two
correlated concentration measures → Bonferroni k = 2, α_cell = 0.025.

## Null model (locked) — slot-independence shuffle

The biologically meaningful null is: *given that the same set of divine names
appears at verse-ends with their observed position-frequencies, are the
penultimate↔final pairings themselves structured, or merely the product of two
independent marginal draws?*

1. Collect the N divine-pair-closing verses → two parallel arrays:
   `slot1[]` (base of penultimate token) and `slot2[]` (base of final token).
2. Observed pairs = zip(slot1, slot2). Compute top-5 share and HHI.
3. For each of 10,000 permutations: independently shuffle `slot1[]` and
   `slot2[]` (random.Random(seed).shuffle), re-zip, recompute top-5 share and HHI.
   This preserves each name's slot-1 and slot-2 marginal frequency EXACTLY while
   destroying any penultimate↔final dependence.
4. p_perm = (# perms with null statistic ≥ observed) / 10,000, for each statistic.

This null is the correct control: it cannot be "passed" merely because a few
names are frequent at verse-ends (that frequency is held fixed in both slots).
A PASS means the specific PAIRINGS are constrained beyond their marginals.

## Cell A and Cell B

- **Cell A (whole-corpus)**: the full set of N divine-pair-closing verses, seed 20260509.
- **Cell B (period-robustness)**: the same slot-independence shuffle restricted to
  the Medinan-revealed divine-pair-closing verses (the fawāṣila-pair density is
  Medinan-skewed per H-NEW-140), seed 20260511. This controls for the worry that
  whole-corpus concentration is a chronology artifact (one revelation-stratum
  dominating). Period from `data/revelation-order.csv`.

**Decision rule**: PASS-DIRECTED if H1 AND H2 both reject at p ≤ 0.025 in Cell A,
AND Cell B (Medinan-only) also shows observed > null-median on both statistics
(directional concordance; Cell B is robustness, not an independent α gate).
Acceptance window table below.

## Acceptance windows

| Cell A H1 | Cell A H2 | Cell B concordant | Verdict |
|:-:|:-:|:-:|:--|
| ✓ | ✓ | ✓ | PASS-DIRECTED |
| ✓ | ✓ | ✗ | PASS-DIRECTED (period-fragile; noted) |
| ✓ | ✗ (or ✗✓) | any | PARTIAL (one statistic only) |
| ✗ | ✗ | any | NULL |
| reverse direction (obs < null) | — | — | NULL (anti-concentration; published with p) |

## Descriptive outputs (NOT part of the α-budget)

1. **Top-15 verse-final ordered name-pairs** by frequency (Arabic base forms +
   transliteration + count + example surah:verse).
2. **Full verse-final pairing graph**: nodes = base divine names appearing at a
   verse-end slot; directed edges = ordered pairs with weight = count. Node
   in-degree / out-degree; identification of "hub" names (highest weighted
   degree).
3. **The famous *al-ʿazīz al-ḥakīm* count**: number of verses closing on this
   pair, broken down by morphological form (al-X al-Y / X-un Y-un / X-an Y-an).
4. **Corpus-EXACT / corpus-extreme pairs**: any ordered pair attested exactly
   once (corpus-singleton fawāṣila), and the single most frequent pair (corpus-max).
5. **Cross-reference to H-NEW-140** (anywhere-in-verse co-occurrence): how the
   verse-final ranking compares to the whole-verse ranking.

## Rules-tuple discipline

| Axis | Locked value |
|:--|:--|
| Tashkeel | no-tashkeel (`quran-text/quran-no-tashkeel.json`) |
| Token level | whitespace-split orthographic tokens; pure rasm/pause marks dropped |
| Pair unit | ordered verse-final bigram, base-normalized |
| Base rule | strip `ال`; strip one trailing `ا` when len>3 |
| Divine set | 97 single-token al-Tirmidhī names (base-normalized) |
| Basmala | counted only in Q 1 |
| Reading tradition | Hafs-Kufan |
| Script | Mashriqi |

**Known limitation (referent ambiguity)**: the base-normalized substring rule does
not disambiguate divine vs non-divine referent. In verse-FINAL position this is
near-negligible (verse-enders are overwhelmingly divine epithets), but e.g.
`العزيز` could in principle close a verse referring to the Egyptian governor.
Manual spot-check of the top pairs is reported descriptively; no verse-final
top-pair instance is a non-divine referent in the observed data (verified at
spot-check). This does not affect the null comparison, which is internal to the
verse-final-pair set.

**Garden-of-forking-paths disclosure**:
- The divine set is locked to the 97 single-token al-Tirmidhī names. Adding
  attested non-list fawāṣila epithets (نصير، بشير، نذير، خلاق، علام) was
  CONSIDERED and REJECTED to keep the set tied strictly to the canonical list.
  Their exclusion is documented; it removes a handful of pairs (e.g. غفور+شكور
  remains; نعم+نصير-class endings are dropped).
- Concentration statistics locked to top-5-share and HHI. top-10-share, Gini,
  entropy were considered; not locked (would expand the family).
- The null is slot-independence (marginal-preserving). A uniform-pair null and a
  degree-preserving graph null were considered; slot-independence is the locked
  primary because it is the strongest (hardest to pass) and the most directly
  interpretable for the al-fawāṣil claim.
- Ordered (not unordered) pairs are locked: *X-un Y-un* word order is itself a
  fawāṣila datum (ghafūr precedes raḥīm; ʿazīz precedes ḥakīm). Unordered
  collapse was considered and reported only descriptively.

## MW-1..MW-7 compliance

- **MW-1 (instrument-prior)**: detection rule, base-normalization, divine set,
  both statistics, and the slot-independence null are all locked above.
- **MW-2 (corpus-prior)**: 10,000 permutations per cell.
- **MW-3 (alternative-models)**: two statistics (share + HHI) and two cells
  (whole-corpus + Medinan robustness).
- **MW-4 (over-fitting)**: no fitted parameter; pair set and statistics fixed.
- **MW-5 (replication)**: PASS-DIRECTED is the ceiling; independent replication
  (e.g. min-tashkeel rule, or QAC-morphology divine-tagging) required for CONFIRMED.
- **MW-6 (instrument-control)**: the slot-independence null controls for marginal
  name-frequency at verse-ends (the obvious confound).
- **MW-7 (post-hoc cap)**: two planned statistics; no post-hoc dimensions. Verdict
  capped at PASS-DIRECTED.

## Anti-flip

The reverse direction (observed concentration BELOW the null median = pairings
LESS structured than independent marginals) is NOT a reportable PASS and is
published as NULL with the observed p.

## Honest expectation

Strong PASS expected on H1/H2: the raw scan (pre-lock inspection of the top
bigrams, recorded here as motivation only) shows ghafūr+raḥīm, ʿazīz+ḥakīm,
samīʿ+ʿalīm, ʿalīm+ḥakīm dominating. The non-trivial scientific content is
whether this survives the slot-INDEPENDENCE null — i.e. whether the concentration
is more than a reflection of a few names (raḥīm, ḥakīm, ʿalīm) being frequent at
verse-ends in general. If H1/H2 PASS, the al-fawāṣil pairing constraint is
empirically vindicated as a real collocational structure, not a marginal artifact.

## Pre-commit attestation

Locked by SHA256. The run script reads this file, recomputes its SHA256, and
fail-fasts on mismatch before any computation. SHA embedded in the script as
EXPECTED_SHA after this file is finalized.
