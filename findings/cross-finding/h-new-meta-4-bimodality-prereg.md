---
id: H-NEW-META-4-PREREG
title: H-NEW-META-4 — Rhythmic-vs-Semantic Bimodality Pre-Registration
date: 2026-04-15
status: PRE-REGISTERED — locked before classification & before any direction-of-effect lookup
locked_at: 2026-04-15 (timestamp recorded in journal/h-new-meta-4-run-1.md)
parent_finding: cross-finding-005 (Quranic Smoothness Triple)
parent_classical_anchor: al-Bāqillānī, Iʿjāz al-Qurʾān (~1000 CE) — "neither prose nor poetry"
secondary_classical_anchors:
  - al-Khaṭṭābī, Bayān Iʿjāz al-Qurʾān
  - Kermani, Gott ist schön (1999)
  - Neuwirth, Der Koran als Text der Spätantike (2010)
  - Abdul-Raof, Qur'an Translation (2001)
inventory_source: findings/cross-finding/effect-size-inventory.tsv (158 rows; locked snapshot)
seed: 20260415
bonferroni_k: 1
bonferroni_alpha_family: 0.05
bonferroni_alpha_per_test: 0.05
pre_registration_authority: h-new-meta-4-specialist (self-pre-reg with ledger-published rubric)
---

# H-NEW-META-4 — Pre-Registration

## Why pre-register

Cross-finding-005 ("Quranic Smoothness Triple") observed three Fresh-Wave-3 probes
([[h-new-34-1-under-dispersion|H-NEW-34.1]], [[h-new-42-reverse-direction-fragility|H-NEW-42]], [[h-new-43-verse-length-fft|H-NEW-43]]) all converging on the direction "Quran SMOOTHER
than matched-Arabic baselines on rhythmic-surface axes." Per al-Bāqillānī's classical
*Iʿjāz al-Qurʾān* doctrine ("neither prose nor poetry but a distinctive register"),
the predicted operationalization is:

  - SEMANTIC-STRUCTURAL probes: Quran > baseline (extreme structure on meaning axes)
  - RHYTHMIC-SURFACE probes:   Quran ≤ baseline (intermediate / smoother on rhythm axes)

This pre-reg locks (a) the rubric for classifying each effect-inventory row, (b) the
statistical test, (c) the PASS/NULL criterion, BEFORE any classification of the rows
and BEFORE the direction column is consulted.

## Pre-Registered Classification Rubric (RUBRIC-V1, locked)

The rubric assigns each row of `effect-size-inventory.tsv` (data rows only; comment
lines and the bismillah ANCHOR row excluded) one of four labels:

  - SEMANTIC-STRUCTURAL  — the axis measures meaning, theological-density, root/lemma
                            relations, content-word distributions, narrative or
                            thematic structure.
  - RHYTHMIC-SURFACE      — the axis measures verse-length, abjad-residue, rhyme,
                            phonetic-surface, surface-adjacency, letter-bigrams,
                            verse-final position, AR(1) on length, or any other
                            surface property that does NOT depend on word-meaning.
  - MIXED                 — measures BOTH semantic and rhythmic-surface jointly,
                            or measures something orthogonal to both (e.g., classifier
                            meta-tasks, scientific-foreknowledge claims).
  - N/A                   — anchor rows, catalog rows, or refuted-modern-numerology
                            apologetic claims that do not test a Quran-vs-baseline
                            structural axis.

The rubric is operationalized as a deterministic keyword-list applied case-insensitively
to (`test_name` + " " + `parent_finding_id` + " " + `classical_anchor`). The
keyword-precedence ladder is:

  Step 1: STRONG SEMANTIC keywords (immediate label SEMANTIC-STRUCTURAL):
    - "lemma" / "root" / "lexem" / "vocab" / "vocabular" / "word-pair"
    - "naẓm" / "nazm" / "munasaba" / "munāsaba" / "mutashabih" / "iltifat"
    - "covenant" / "divine name" / "khawātim" / "khawatim" / "hashr"
    - "ism al-azam" / "ism al-aʿẓam" / "ism al-aʿzam"
    - "prophet" / "pericope" / "ʿīsā" / "isa" / "mūsā" / "musa" / "muhammad" / "muḥammad"
    - "kitāb" / "kitab" / "qurʾān" / "quran"-as-shift-token (only in shift-test names)
    - "chiastic" / "ring" / "ring-composition" / "biqāʿī" / "biqai" / "cuypers" / "farrin"
    - "hapax" (semantic distinctiveness of word-types) when paired with semantic context
    - "incipit-class" / "twin-opener" / "opening" (formulaic semantic openers)
    - "claim" / "classifier" / "feature" / "signature" (when meta-classifier on claims)
    - "muqattaʿat" / "muqattaat" — letters-as-symbols, classified SEMANTIC-STRUCTURAL
    - "narrative" / "dialog" / "turn-taking" / "munāẓara"
    - "Mecca" / "Medin" / "chronolog" / "Nöldeke" / "noldeke"
    - "kawthar" / "ar-rahman" / "kahf" / "yusuf" / "yūsuf" / "māʾida" / "maida"
    - "embryo" / "iron" / "big bang" / "fingerprint" / "mountain" / "expanding" / "sun"
      / "two seas" / "deep-sea" / "atom" / "milk" / "pharaoh" — but these are tagged N/A
      via the apologetic-override below.
    - "shahada" / "muḥammad-named" / "qul" / "negation"
    - "midpoint" / "self-reference" / "compression" (self-reference is meaning-laden)
    - "iʿjāz al-ījāz" / "ijaz al-ijaz"
    - "pronoun" (pronoun-chain semantics)
    - "elision-eschatology"

  Step 2: STRONG RHYTHMIC-SURFACE keywords (immediate label RHYTHMIC-SURFACE):
    - "verse-length" / "verse length" / "length-ratio" / "Hurst"
    - "AR(1)" / "Ljung-Box" / "ρ(1)" / "rho(1)" / "autocorrelation" / "autocorr"
    - "Markov" (when applied to letters/bigrams/n-grams, NOT to lemma)
    - "letter-bigram" / "bigram spectrum" / "spectral gap" / "λ₂" / "lambda_2"
    - "abjad" / "ḥisāb al-jummal" / "hisab al-jummal" / "hisab-al-jummal"
    - "rhyme" / "saj" / "saj'" / "fāṣila" / "fasila" / "rawi"
    - "verse-final" / "verse final" / "verse-ending"
    - "rhymed" (poetic rhyme)
    - "RQA" / "recurrence-quantification" / "determinism" / "laminarity" (rhythmic)
    - "acrostic" (letter-sequence)
    - "letter-multiset" / "letter ordering" / "letter-div" / "letter-sequence"
    - "prime-mod" / "mod-7" / "mod-11" / "mod-19" / "div-19" / "Code-19" / "code 19"
    - "Zipf" / "zipf"
    - "fragility" / "ablation" / "perturbation" (surface-perturbation tests)
    - "phonetic" / "palindrome" (when LETTER-level; root-palindrome → semantic)
    - "TDA" / "persistent homology" / "topological" / "manifold" / "bottleneck"
      (when on token/orthographic embeddings, not on semantic embeddings)
    - "iqa" / "īqāʿ" / "rhythm" / "meter"
    - "smoothness" / "smoother" / "white-noise"
    - "syntactic" — syntactic-mood-switch is RHYTHMIC-SURFACE (verse-boundary surface)
    - "boundary" (verse-boundary, surah-boundary surface markers)
    - "twin-opener Lock" — surface-character-match → RHYTHMIC-SURFACE
      (twin-opener as rhetorical category w/ semantic content → SEMANTIC-STRUCTURAL;
      conflict resolved by rule: PRIMARY label = RHYTHMIC-SURFACE if the test_name
      mentions L≥30 char-match or otherwise foregrounds SURFACE-character-match)

  Step 3: APOLOGETIC-OVERRIDE (immediate label N/A):
    - any row in HONEST-LIMITS-§1.x or HONEST-LIMITS-§II.x (refuted modern numerology
      or scientific-foreknowledge) → N/A. Rationale: these are apologetic claims that
      do not test a structural axis vs matched baseline; they are philological or
      numerical-coincidence claims. Excluding them prevents the bimodality test from
      being polluted by claims unrelated to literary-compositional structure.
    - bismillah-anchor (locked anchor row) → N/A.
    - any row whose verdict is "ANCHOR" or "CONFIRMED-catalog" or "REFUTED-catalog"
      where no quantitative baseline-comparison was run → N/A. (NOTE: this rule does
      NOT consult the direction-of-effect column; it consults only the verdict
      meta-flag for whether a baseline-test was performed.)

  Step 4: MIXED label:
    - meta-classifier rows that aggregate over many sub-claims of mixed type
      (e.g., H-META-1 confirmable-claim signature classifier) → MIXED.
      EXCEPTION: if the test is an aggregate over a SINGLE class (e.g., all
      semantic claims), label by that class.
    - any row not captured by Step 1 or Step 2 → MIXED.

  Step 5: TIE-BREAKER — if both a Step-1 and a Step-2 keyword fire on the same row,
    apply the following deterministic tie-break:
      a. If the test_name contains BOTH "root" AND "verse-length", classify by
         which appears FIRST in the test_name string.
      b. If "rhyme" / "abjad" / "AR(1)" / "Markov" appears AT ALL, the row is
         RHYTHMIC-SURFACE (rhythmic dominates when both fire).
      c. Otherwise, default to SEMANTIC-STRUCTURAL.

## Direction-of-effect coding (also locked here)

For each non-N/A row, the direction is coded from the existing
`observed_z_or_p` and `verdict` columns AFTER classification is locked:

  - "Quran > baseline" (Q-HIGH): the Quran shows MORE of the measured property than
    the baseline (z is positive AND interpreted as Quran > baseline given the
    test_name's polarity). For tests where MORE structure = Quran > baseline
    (e.g., al-Razi adjacent z=+30.76, RQA determinism z=+15.09), positive z = Q-HIGH.
    For tests where LESS dispersion = MORE structure (e.g., abjad residue under-
    dispersion z=-11.36 means Quran more uniform than expected), the test_name's
    direction-convention is documented row-by-row in the script.
  - "Quran < baseline" (Q-LOW): the Quran shows LESS of the measured property.
  - "NULL/EQUAL" (Q-EQ): the test is statistically null at α=0.05 (|z|<1.96 OR
    p>0.05) AND the verdict is NULL/REFUTED-with-no-direction. Ties go to Q-EQ.

For the bimodality test, Q-EQ rows are EXCLUDED from the 2×2 contingency table
(documented in the script). Including them as a third bin is reported as a
robustness check, not the primary test.

## Statistical test

Primary test: 2×2 contingency table χ² (Yates-corrected for cell counts < 5,
otherwise Pearson).

  | Class                | Q-HIGH | Q-LOW |
  |----------------------|--------|-------|
  | SEMANTIC-STRUCTURAL  |   a    |   b   |
  | RHYTHMIC-SURFACE     |   c    |   d   |

H0: independence between class and direction.
H1: class predicts direction (specifically: SEMANTIC-STRUCTURAL → Q-HIGH,
RHYTHMIC-SURFACE → Q-LOW).

Bonferroni-1 (single test pre-registered).

## PASS criterion (al-Bāqillānī doctrine confirmed)

ALL of the following must hold:

  1. Among SEMANTIC-STRUCTURAL probes (excluding Q-EQ): a / (a + b) ≥ 0.70
     (≥ 70% of semantic probes show Quran > baseline).
  2. Among RHYTHMIC-SURFACE probes (excluding Q-EQ): c / (c + d) ≤ 0.50
     (≤ 50% of rhythmic probes show Quran > baseline).
  3. χ² test p < 0.05 (Bonferroni-1).

## NULL criterion

ANY of (1)/(2)/(3) fails → NULL. Specifically:

  - If semantic probes are NOT predominantly Q-HIGH (a/(a+b) < 0.70), OR
  - If rhythmic probes ARE predominantly Q-HIGH (c/(c+d) > 0.50), OR
  - If χ² p ≥ 0.05,
  then the al-Bāqillānī bimodality is NOT confirmed by this meta-test, and
  cross-finding-005 remains EXPLORATORY (not promoted to CONFIRMED).

## MW-5 positive control

The Khawātim al-Ḥashr divine-name density finding (MASTER-§1-#9 / khawatim-al-hashr)
MUST be classified SEMANTIC-STRUCTURAL by the rubric (it is anchored on "divine name"
and "khawātim" — both Step-1 keywords). If the rubric's auto-classification disagrees,
the rubric is broken and a re-pre-reg is required.

The MW-5 control also requires that this row's direction be Q-HIGH (Quran > baseline),
which is independently true (49=7² Bonferroni-survives, 8 exclusive divine names).

## Disclosure obligation

The findings file MUST disclose the rubric's classification of all 158 rows
(or all included rows after N/A exclusion), so future audits can re-classify and
re-test under alternative rubrics.

## Garden-of-forking-paths log

The rubric was constructed BEFORE any classification was performed. The rubric
keywords were drawn from:
  (a) the cross-finding-005 narrative (which lists the smoothness-triple's shared
      surface-rhythmic property),
  (b) standard Arabic literary-critical vocabulary (naẓm, munāsaba, ʿiyāqāʿ, fāṣila,
      saj', muqattaʿāt) sourced from al-Suyūṭī's *Itqān* and al-Zarkashī's *Burhān*,
  (c) the test_name vocabulary visible in inventory column-1 BEFORE looking at any
      results column.

No keyword was added or removed AFTER any classification was attempted.

The single ambiguous-class rule (twin-opener Lock — surface vs semantic) was
locked at this pre-reg stage with a deterministic L≥30 character-match criterion;
the rationale (L≥30 indicates SURFACE character-match dominating semantic) is
documented above and not re-litigated post-hoc.

## What is NOT pre-registered (and why)

  - The exact COUNT of N/A vs MIXED rows. The rubric is fully deterministic, so
    these counts are mechanical outputs.
  - The χ² value or p-value. These are mechanical outputs.
  - The verdict (PASS or NULL). This is determined by the locked criterion.

## Files

  - Script: `scripts/h_new_meta_4_bimodality.py`
  - JSON output: `findings/cross-finding/csv/h-new-meta-4.json`
  - Findings: `findings/cross-finding/h-new-meta-4-bimodality.md`
  - Journal: `journal/h-new-meta-4-run-1.md`

## Pre-registration commitment

I, h-new-meta-4-specialist, commit to publishing the result PASS or NULL identically,
without selective reporting. This pre-reg is locked at file-write-time
(2026-04-15) BEFORE the script is executed and BEFORE the rubric has been
applied to any specific row. The rubric is published verbatim above and any
deviation in the script will be flagged as an integrity violation.
