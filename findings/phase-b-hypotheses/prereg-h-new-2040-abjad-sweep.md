---
finding_id: h-new-2040-abjad-sweep
phase: B
status: PRE-REGISTERED (locked before computation)
date: 2026-05-29
rules_tuple: (no-tashkeel JSON for surah-name + verse-text; uthmani-consonantal JSON for muqaṭṭaʿāt openers; orthographic graphemes; mashriqi abjad default + maghribi cross-check; hamza-carrier policy per methodology.md §6: أ/إ/آ/ٱ→1, ؤ→6, ئ→10, ة skipped, ى skipped, bare ء skipped; basmala-counted-only-in-Q1; Hafs-Kufan)
null_model: row/value shuffle, 10000 permutations, seed 20260509
bonferroni_k: see family table below
classical_claim: ḥisāb al-jummal / ʿilm al-ḥarf tradition (Ibn ʿArabī al-Futūḥāt; al-Būnī Shams al-Maʿārif) and its modern echoes (basmala=786 talismanic tradition; Allāh=66; Muḥammad=92)
seed: 20260509
author: computational-tester
---

# H-NEW-2040 — Systematic abjad / ḥisāb al-jummal sweep + audit of famous gematria claims

## Purpose

A SYSTEMATIC audit of the ʿilm al-ḥarf (ḥisāb al-jummal) numerical tradition the project
exists to examine. Two classes of claim are tested:

- **CLASS A — famous deterministic claims** (basmala=786, Allāh=66, Muḥammad=92, and the
  muqaṭṭaʿāt abjad-sums). These are pure arithmetic; they either reproduce the cited integer
  or they do not. No null model is needed — the "test" is whether the locked abjad table
  reproduces the tradition's number. The interesting question is *which* rules-tuple the
  famous number assumes.
- **CLASS B — systematic correlation claims** (surah-name abjad vs surah position / verse-count;
  verse abjad-sum vs structural index). These ARE susceptible to garden-of-forking-paths and
  REQUIRE a permutation null + Bonferroni.

## Abjad table (locked, from methodology.md §6)

Mashriqi (default): ا=1 ب=2 ج=3 د=4 ه=5 و=6 ز=7 ح=8 ط=9 ي=10 ك=20 ل=30 م=40 ن=50 س=60 ع=70
ف=80 ص=90 ق=100 ر=200 ش=300 ت=400 ث=500 خ=600 ذ=700 ض=800 ظ=900 غ=1000.
Maghribi cross-check table also locked (ص=60 ض=90 س=300 ظ=800 غ=900 ش=1000), per methodology.md §6.
Hamza-carrier policy (locked): أ/إ/آ/ٱ → 1 (carrier alif), ؤ → 6, ئ → 10. ة, ى, bare ء contribute 0.

NOTE on tooling divergence: `analysis/tools/gematria.py` *silently skips* hamza carriers
(contributes 0), whereas methodology.md §6 assigns carriers their alif/waw/ya value. The
famous Class-A targets (basmala, Allāh, Muḥammad) contain NO hamza carriers, so the two
policies agree exactly for them. For surah-names (e.g. آل عمران, الأنعام) the two diverge;
this run implements the **methodology.md §6 carrier policy** as primary and reports the
gematria.py skip-policy as a sensitivity check.

## Hypotheses (DIRECTION LOCKED BEFORE OBSERVATION)

**H-A1 (basmala=786):** Under mashriqi, abjad(بسم الله الرحمن الرحيم) = 786 EXACTLY.
Direction: CONFIRM (deterministic). PREDICT 786.

**H-A2 (Allāh=66):** Under mashriqi, abjad(الله) = 66 EXACTLY (ا1+ل30+ل30+ه5=66).
Direction: CONFIRM. PREDICT 66.

**H-A3 (Muḥammad=92):** Under mashriqi, abjad(محمد) = 92 EXACTLY (م40+ح8+م40+د4=92).
Direction: CONFIRM. PREDICT 92.

**H-A4 (muqaṭṭaʿāt sums):** Compute abjad-sum of all 14 unique muqaṭṭaʿāt letter-strings.
This is exploratory-descriptive; PREDICT no muqaṭṭaʿ sum equals a "clean" target
(its surah position, its surah verse-count, 19, 114, 786) beyond what chance over a
small set would give. Direction: NULL of meaningful coincidence (report any hits as
post-hoc, MW-7 capped at α=0.05 single-test, no correction credit).

**H-B1 (surah-name abjad ⟂ position):** Pearson r between surah-name abjad-sum and surah
position (1..114) is indistinguishable from 0 under a 10000-perm shuffle null.
Direction: NULL (no design). PREDICT |r| not significant at Bonferroni α.

**H-B2 (surah-name abjad ⟂ verse-count):** same, against Hafs verse-count.
Direction: NULL. PREDICT not significant.

**H-B3 (surah-name abjad == position, exact-match count):** number of surahs whose
name-abjad exactly equals their position. NULL: expected exact-matches under shuffle.
Direction: NULL. PREDICT observed ≈ chance.

**H-B4 (surah-name abjad == verse-count, exact-match count):** same vs verse-count.
Direction: NULL. PREDICT observed ≈ chance.

**H-B5 (verse abjad == structural index, exploratory scan):** count verses whose full
abjad-sum equals (a) their within-surah verse number, (b) surah*1000+verse, (c) a global
running verse index 1..6236. These targets are astronomically larger or smaller than typical
verse abjad-sums for most cases; treated as descriptive scan. NULL: shuffle verse→index
assignment. Direction: NULL. PREDICT observed exact-matches ≈ chance.

## Null model

- Class B: `random.Random(20260509)`; 10000 permutations.
  - H-B1/H-B2: shuffle the surah-name-abjad vector, recompute Pearson r, two-sided perm-p.
  - H-B3/H-B4: shuffle name-abjad vector against fixed targets, count exact matches, perm-p
    on observed-match-count being ≥ observed.
  - H-B5: shuffle the verse→target assignment within each target family, perm-p on match count.

## Bonferroni family

Class-B inferential family k = 6 (H-B1, H-B2, H-B3, H-B4, and H-B5 has 3 sub-targets but
they are reported as one exploratory family; conservatively count the 3 sub-targets →
k = 2 + 2 + 3 = 7). α_corrected = 0.05 / 7 ≈ 0.00714. Class A is deterministic (no α).

## Success / failure criteria

- **Class A SUCCESS:** the three famous integers (786, 66, 92) reproduce EXACTLY under
  mashriqi with the locked table. FAILURE: any mismatch (would itself be a publishable
  finding about the tradition's table-dependence).
- **Class B "NULL CONFIRMED" (the pre-registered expectation):** no Class-B test reaches
  Bonferroni α; exact-match counts are within the perm-null central mass.
- **Class B pre-commit VIOLATION:** if any Class-B correlation is significant at Bonferroni
  α in the direction of "designed structure", it is published with full prominence as a
  REVERSED-DIRECTION result (the tradition would be partially vindicated), NOT massaged.

## MW protections

- MW-1: abjad table + Pearson r + exact-match-count metrics fixed here, pre-observation.
- MW-2: 10000-perm null.
- MW-3: mashriqi AND maghribi tables (≥2 model variants) for Class A and the surah-name sweep.
- MW-6: instrument-control — also correlate name-abjad vs a *random* permutation of positions
  (should be null by construction; sanity check the null machinery).
- MW-7: any post-hoc "interesting" muqaṭṭaʿ coincidence capped at single-test α=0.05, no
  Bonferroni credit, flagged exploratory.

## Anti-cherry-picking note

The surah-name sweep tests the WHOLE 114-name vector, not a hand-picked subset. The verse
scan tests ALL 6236 verses against fixed structural targets. No subset selection.
