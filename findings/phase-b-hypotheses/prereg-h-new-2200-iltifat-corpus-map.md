---
id: H-NEW-2200
title: Iltifāt (grammatical-person shift) corpus map — exhaustive generator + Meccan/Medinan density direction-lock
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
bonferroni_k: 1
bonferroni_family: H-NEW-2200-iltifat-density (single pre-registered direction-locked density test)
alpha_bon: 0.05
direction_of_effect: >
  MECCAN surahs exhibit HIGHER iltifāt density per verse than MEDINAN surahs.
  Density(region) = (# of verse-boundary iltifāt loci detected within that region's surahs)
  / (# of intra-surah verse boundaries in that region). Direction LOCKED:
  density(Meccan) > density(Medinan). Observed difference Δ = density(Meccan) − density(Medinan)
  must be POSITIVE and exceed the 95th percentile of the label-shuffle null. If Δ ≤ 0
  (Medinan denser or equal) the result is published as NULL with a pre-commit-violation flag.
origin: >
  Iltifāt (الالتفات, "the turning-aside") is the central balāgha device of abrupt grammatical-person
  / number shift. al-Zarkashī (al-Burhān fī ʿulūm al-Qurʾān, the nawʿ on iltifāt, ~50 examples)
  and al-Suyūṭī (al-Itqān, parallel chapter, ~35 examples) catalogued it qualitatively; Ibn al-Athīr
  (al-Mathal al-Sāʾir) called it shajāʿat al-ʿarabiyya ("the daring of Arabic"). Abdel Haleem
  (BSOAS 55(3):407-432, 1992; transcribed at data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md)
  produced the modern verse-by-verse ground-truth catalog. The device has NEVER been enumerated
  corpus-wide by an objective morphological detector. This pre-reg builds a GENERATOR over QAC v0.4
  person/number features and direction-locks ONE density hypothesis.
verdict_ceiling: DIRECTIONAL (single planned density test; CONFIRMED requires independent replication / robustness across detector variants documented herein)
rules_tuple:
  text_source: quran-text/quran-no-tashkeel.json (verse inventory, 114 surahs / 6236 verses, Hafs-Kūfan)
  morphology_source: data/morphology/quranic-corpus-morphology-0.4.txt (QAC v0.4)
  token_unit: QAC morphological segment (LOCATION = surah:verse:word:segment)
  feature_extraction: person-number-gender tag drawn from any FEATURES field matching the regex
    ^(PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$ ; person ∈ {1,2,3}; number ∈ {S,D,P}
    (D=dual normalized; bare S/D/P with no gender allowed).
  counted_pos: finite VERBS (POS:V — IMPF/PERF/IMPV) AND PRONOUNS (POS:PRON independent, plus
    SUFFIX|PRON:* object/possessive clitics, plus PREFIX subject-pronoun verbal affixes carried
    inside the V segment's own feature). Participles, nouns, particles excluded from the person tally.
  per_verse_profile: the MULTISET of (person, number) over all counted segments in the verse.
  dominant_person(verse): the modal grammatical PERSON (1/2/3) by raw count of counted segments;
    ties broken toward the LATER-occurring person within the verse (a shift resolves to the value
    the verse leaves the reader on). Verses with zero counted segments have dominant_person = NONE
    and are skipped as shift endpoints (the previous defined value carries forward for adjacency).
  dominant_number(verse): the modal grammatical NUMBER (S/D/P) by raw count; same tie-break.
  basmala_policy: basmala counted only as verse 1 of surah 1 (QAC numbering); not a separate verse elsewhere.
  divine_voice_overlay: a SECONDARY annotation (does NOT gate the primary detector). A 1st-person
    segment is divine-voice by default in the Quran (the speaker "I/We" is God or God-quoted); a
    1sg↔1pl shift between adjacent divine-voice verses is flagged as the "I↔We" majesty-iltifāt subtype.
  shift_locus_definition: an intra-surah verse boundary (v, v+1) is an ILTIFĀT LOCUS iff
    dominant_person(v) ≠ dominant_person(v+1) (PERSON shift) OR dominant_number(v) ≠ dominant_number(v+1)
    (NUMBER shift), with both endpoints having a defined dominant value. Cross-surah boundaries excluded.
  density_definition: per region, loci / intra-surah-boundaries.
  region_definition_primary: Meccan vs Medinan per the 'type' field of quran-text/quran-no-tashkeel.json
    (86 Meccan / 28 Medinan surahs).
  null_model: 10,000 random reassignments of the {meccan,medinan} label to the 114 surahs holding the
    marginal 86/28 split fixed (label shuffle), recomputing Δ each time; seed=20260509.
benchmark: recall against Abdel Haleem 1992 person-iltifāt union (catalog file above) is REPORTED as a
  precision/recall diagnostic, NOT as a pass/fail gate (Abdel Haleem's list is acknowledged incomplete;
  precision cannot be judged against it).
---

# H-NEW-2200 pre-registration — iltifāt corpus map + Meccan/Medinan density direction-lock

## 1. The device

Iltifāt is the abrupt shift of grammatical person, number, or addressee mid-discourse.
al-Zarkashī's definition (al-Burhān): *"the change of speech from one mode to another, for
the sake of freshness and variety for the listener."* The Quran uses it far more than any
other Arabic prose (Abdel Haleem: a sampling of ḥadīth found "not a single instance").

Six classical PERSON sub-types (Abdel Haleem Table):
1. 3rd→1st (>140, most common — the divine narrative voice turning toward itself)
2. 1st→3rd (~100)
3. 3rd→2nd (~60)
4. 2nd→3rd (<30)
5. 1st→2nd (1, disputed: Q 36:22 only)
6. 2nd→1st (0, does not occur)

Plus NUMBER shifts (~53 catalogued) and ADDRESSEE shifts (~24).

## 2. The generator (primary deliverable)

For every verse I compute a person-number profile from QAC v0.4: the multiset of
(person, number) tags carried by finite verbs and pronouns. From the profile I derive
dominant_person ∈ {1,2,3} and dominant_number ∈ {S,D,P}. At every intra-surah verse
boundary I test for a change in either. Each detected change is an ILTIFĀT LOCUS,
recorded with full coordinates (surah:verse → verse+1), the from→to person tuple, the
from→to number tuple, and a divine-voice overlay flag for 1↔1 majesty shifts.

Categories enumerated exhaustively:
- divine 1S↔1P ("I"↔"We") — the majesty-iltifāt subtype
- 3rd→1st and 1st→3rd
- 3rd→2nd and 2nd→3rd
- 1st→2nd and 2nd→1st
- 2nd SG↔PL (and all SG↔PL/DU number shifts)
- absent→present (ghayba↔ḥuḍūr), operationalized as the 3↔{1,2} person change

This is a CENSUS: every locus is published with coordinates regardless of the density test outcome.

## 3. Pre-registered direction-locked hypothesis

**H1 (density direction-lock):** Meccan surahs show HIGHER per-boundary iltifāt density
than Medinan surahs. Δ = density(Meccan) − density(Medinan) > 0 AND Δ exceeds the 95th
percentile of the 10,000-perm label-shuffle null (α = 0.05, k = 1).

**Rationale for the locked direction (committed before computation):** The Meccan corpus
is dominated by short, oath-laden, eschatological, polemical sūras with rapid rhetorical
turns and frequent direct address of the Prophet / disbelievers / mankind; the Medinan
corpus is dominated by longer legislative-discursive passages with sustained third-person
narration and stable addressee. al-Suyūṭī's Meccan/Medinan stylistic typology (Itqān,
nawʿ on makkī wa-madanī) associates the Meccan register with rhetorical intensity. The
prior project finding that the s=50 compression kink separates a high-d̄ early block from
a low-d̄ tail is consistent with greater per-verse rhetorical churn in the (largely Meccan)
short sūras. I therefore lock density(Meccan) > density(Medinan).

**Failure condition:** if Δ ≤ 0, or Δ > 0 but does not clear the 95th percentile, H1 is
NOT confirmed. A reversed sign (Medinan denser) is published as NULL with a pre-commit
violation flag and equal prominence.

## 4. Null model

Label shuffle: hold the 86/28 Meccan/Medinan marginal fixed; randomly reassign the labels
to the 114 surahs 10,000 times (seed 20260509); recompute Δ each permutation. p = fraction
of permutations with Δ_perm ≥ Δ_obs (one-sided, direction-locked). Surah-level shuffle (not
verse-level) is the correct exchangeable unit because the region label is a surah property.

## 5. Robustness / MW protections committed in advance

- **MW-1 (instrument-prior):** detector defined above before any run.
- **MW-2 (corpus-prior):** 10,000-perm permutation null.
- **MW-3 (alternative-models):** secondary region split s≤50 vs s>50 (mushaf position) reported
  alongside the primary Meccan/Medinan split; and a person-ONLY detector vs person-OR-number detector.
- **MW-5 (replication):** density recomputed under a verb-only person tally (drop pronouns) as a
  detector-robustness replication; direction must hold for the headline to stand as DIRECTIONAL.
- **MW-6 (instrument-control):** recall benchmark against Abdel Haleem ground truth confirms the
  detector fires on the canonically-recognized loci (sanity that the instrument measures iltifāt).
- **MW-7 (post-hoc cap):** any pattern noticed only after the run is capped at single-test α and flagged.

## 6. Verdict ceiling

DIRECTIONAL on a single planned test. Promotion to CONFIRMED requires the direction to survive
the verb-only replication AND the s≤50/s>50 secondary split (both pre-registered here). The census
itself (the locus map) is a descriptive deliverable, not subject to the density verdict.

*Locked 2026-05-29 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
