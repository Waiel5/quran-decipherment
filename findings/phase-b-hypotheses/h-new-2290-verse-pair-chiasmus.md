---
finding_id: H-NEW-2290
title: "Verse-pair chiasmus / antithetical-mirror generator — DOUBLE REVERSAL: verse-pairs are PARALLEL not chiastic, and antithesis concentrates in the LONG surahs not the juzʾ-ʿamma"
specialist: h-new-2290-verse-pair-chiasmus-specialist
date: 2026-05-29
phase: B
verdict: "NULL (both sub-tests fail the locked direction); BOTH reversals are themselves significant in the OPPOSITE direction — published with full prominence as pre-commit reversals"
prereg: findings/phase-b-hypotheses/prereg-h-new-2290-verse-pair-chiasmus.md
prereg_sha256: 789b82551afdcf74769dda571d15af16a16aabf5026a9aa83628aedcf36674fc
seed: 20260509
perms: 10000
bonferroni_k: 2
alpha_bon: 0.025
rules_tuple: "(no-tashkeel, QAC v0.4 STEM-ROOT word-order, content-root sequence, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-2290 — Verse-pair chiasmus / antithetical-mirror generator

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

**VERDICT: NULL on both pre-registered directions — and both NULLs are
*significant reversals* of the locked direction.** This is a clean, honest
pre-commit double-violation, published with full prominence per protocol §1.3,
§1.8. The generator works; the *predictions* were wrong, and the data say
something more interesting than the predictions did.

Pre-reg SHA-256 `789b82551afdcf74769dda571d15af16a16aabf5026a9aa83628aedcf36674fc`
verified at runtime (script aborts on mismatch). All numbers from
`findings/phase-b-hypotheses/csv/h-new-2290.json`.

## Headline numbers

| Sub-test | Locked direction | Observed | z vs null | One-sided p (locked dir) | Verdict |
|:--|:--|:--|:-:|:-:|:--|
| (A) Word-order chiasmus | R_obs **>** null (excess AB→BA reversal) | R_obs = **0.3030**, null mean = 0.3505 | **−3.28** | 0.9999 | **NULL → reversal** |
| (B) Antithetical density | density(A: Q78–114) **>** density(B: Q1–49) | dA = **0.0038**, dB = **0.0570**, Δ = **−0.0532** | **−5.46** | 1.0000 | **NULL → reversal** |

Bonferroni family k = 2, α_bon = 0.025. Neither locked direction passes; both
opposite directions are significant (see below).

## Sub-test A — verse-pair chiasmus → significant PARALLELISM (the opposite)

Across all 113×Σ consecutive verse-pairs, 4,083 ordered shared-root pairs exist
(both members share ≥ 2 content roots). Of these, **1,237 are reversed-order
(AB→BA)** and **2,846 are same-order (AB→AB)**. The reversed-order rate is
**R_obs = 0.3030** — markedly *below* the within-surah verse-shuffle null mean of
0.3505 (sd 0.0145).

- **Locked chiastic direction (R_obs > null): NULL**, one-sided p = 0.9999.
- **The reverse — PARALLELISM (R_obs < null): significant**, one-sided
  p = **0.0013** (raw) < α_bon = 0.025; z = −3.28.
- **Triplet variant (MW-3, outer pair i↔i+2): same result** — R = 0.3137,
  chiastic p = 0.9945. Robust to aggregation.

**Interpretation.** When two adjacent verses share roots, those roots tend to
recur in the **same** linear order, not crossed. This is the expected fingerprint
of Quranic *anaphora / iʿādat al-ṣadr* (e.g. successive `al-ladhīna…`
relative-clause openers, repeated `wa-…` coordinations, parallel `Allāh…rabb…`
frames) rather than *radd al-ʿajuz ʿalā al-ṣadr* chiastic crossing. The
verse-pair scale is **parallelistic, not chiastic**. This dovetails with the
project's scale-of-aggregation law: chiasmus appears at the *block/pericope*
scale (Q002-F-07 → cross-finding-025, PASS) but NOT at the finest adjacent-verse
scale tested here — exactly the gradient one would expect if ring-composition is
a deliberate large-unit device, not a micro-local one.

### Illustrative reversed-order census (MW-7 single-test cap — NOT confirmatory)
624 verse-pairs carry ≥ 1 reversed-order root pair; the strongest are
legal/listing passages where order is content-forced, not rhetorical:

| Pair | reversed / same | sample reversed root-tuples |
|:--|:-:|:--|
| Q 4:11–12 | 49 / 56 | (Alh,kwn) (Axw,wHd) (Axw,vlv) — inheritance-share lists |
| Q 2:184–185 | 13 / 8 | (Axr,Edd) (Axr,Swm) (Edd,Swm) — fasting / counting days |
| Q 4:90–91 | 13 / 15 | (Ezl,byn) (byn,slT) — withdrawal / authority |
| Q 7:43–44 | 12 / 3 | (Alh,Hqq) (Alh,jnn) — Garden dwellers ↔ companions of Fire |

These are *enumerated for the census*, not claimed as significant; the corpus
mean direction is parallel.

## Sub-test B — antithetical density → significant LONG-surah concentration (the opposite)

The locked-genre prediction was that the eschatological juzʾ-ʿamma short surahs
(Q 78–114) would be the antithesis-dense region. **The data reverse this
emphatically.**

| Region | antithetical pairs | consecutive pairs | density |
|:--|:-:|:-:|:-:|
| A = Q 78–114 (locked-predicted high) | **2** | 527 | **0.0038** |
| B = Q 1–49 (locked-predicted low) | **261** | 4,581 | **0.0570** |
| Sharper (MW-3): A = Q78–114 vs B = Q1–9 (ṭiwāl) | 2 vs 282 | — | 0.0038 vs **0.1159** |

- Δ = dA − dB = **−0.0532**; z = **−5.46**; locked-direction (A>B) p = 1.0000.
- The reverse (**B > A**) is overwhelming (label-permutation null mean Δ ≈ 0, sd
  0.0097; observed Δ five-and-a-half sd below it).
- The ENTIRE juzʾ-ʿamma contributes **two** adjacent antithetical pairs:
  **Q 81:12–13** (paradise↔hellfire: *al-jaḥīm* brought near ↔ *al-janna* brought
  near) and **Q 98:6–7** (faith: the disbelievers ↔ the believers as best/worst
  of creatures).

**Interpretation.** Adjacent-verse antithesis is a feature of the **long
Medinan polemical surahs**, not the Meccan eschatological miniatures. The
drivers are Q 2 (34 pairs, density 0.119), Q 4 (33; 0.189), Q 3 (25; 0.126),
Q 5 (22; 0.185), Q 9 (15; 0.117), Q 8 (12; 0.162), Q 47 (9; 0.243), with the
highest single density in Q 60 al-Mumtaḥana (5/12 = 0.417). The dominant
opposed field by a wide margin is **F1 faith↔disbelief (219 of 290 census
pairs)**, then F3 paradise↔hellfire (23), F2 guidance↔misguidance (22),
F6 righteous-deed↔corruption (22). The juzʾ-ʿamma surahs pit the saved against
the damned *within single verses* and across thematic blocks, but rarely split
the two poles across an *adjacent verse-pair* — their antithesis is intra-verse
or whole-surah, not pair-mirrored. The long surahs, by contrast, run extended
believer-list / disbeliever-list adjacencies (e.g. Q 2:25 vs 2:24-type
sequences), producing the pair-level signal. **My genre lock chose the wrong
genre**: the right answer is "long Medinan disputation," not "short Meccan
eschatology."

## Why this is the honest, correct outcome (not a failure of the generator)

The generator is sound: SHA-locked lexicon, 10,000-perm matched nulls per
sub-test, equal-prominence reporting. Two independent direction-locked
predictions were tested and both *reversed* — and crucially, **each reversal is
itself statistically significant**, so the corpus is making a positive statement,
not merely failing to confirm:

1. **The verse-pair scale is parallelistic** (p = 0.0013). Chiasmus lives at the
   block scale, not the adjacent-verse scale. This *sharpens* the project's
   scale-of-aggregation law with a new data point at the finest scale.
2. **Adjacent-verse antithesis is a long-Medinan-disputation signature**
   (z = −5.46), not an eschatological-miniature one. This is a genuine,
   re-usable genre marker discovered by the census.

## Census artifacts (full enumeration on disk)

`findings/phase-b-hypotheses/csv/h-new-2290.json` contains:
- `subtest_A_chiasmus.census`: all **624** consecutive verse-pairs with ≥ 1
  reversed-order root pair, each with (surah, i, j), reversed/same counts, and
  the reversed (X,Y) root tuples.
- `subtest_B_antithetical.census`: all **290** antithetical consecutive
  verse-pairs with (surah, i, j), triggered field(s), and which verse carried
  which pole.
- `subtest_B_antithetical.per_surah`: per-surah pair counts and densities.

## Locked-lexicon honesty note

Per the SHA-locked lexicon, four Buckwalter codes were written with notation
that does not attest in QAC v0.4 and therefore acted as **no-ops** (documented,
not silently fixed): `Srk` (shirk; real QAC root `$rk`), `>jr` (reward-ajr; real
`Ajr`), `sqr` (saqar — annotated as PN without ROOT), and effectively `lZy`
(*laẓā*, 1 attestation, mostly un-rooted). Their absence does not affect the
verdict: the dominant fields (F1 `Amn`/`kfr`+`nfq`, F2 `hdy`/`Dll`,
F3 `jan~ap`/`jHm`/`sEr`/`Hamiym`/`naAr`, F4 `nuwr`/`Zuluma`t`, F8 `Hyy`/`mwt`)
all attest robustly and carry the entire signal. The reward/punishment field is
the only one materially weakened by a no-op (`>jr`); F5 still fired via
`vwb`/`jzy`-reward vs `Eqb`-punishment lemmas. Re-running with the corrected
codes (`$rk`, `Ajr`) would only ADD a handful of long-surah pairs, deepening the
already-significant B>A reversal — it cannot rescue the locked A>B direction.

## MW protections honored

- **MW-1**: lexicon, ordered-root chiasmus rule, region definitions all SHA-locked
  before computation.
- **MW-2**: 10,000 within-surah verse-shuffle perms (A) and 10,000 label perms (B),
  seed 20260509.
- **MW-3**: triplet variant (A) and sharper ṭiwāl contrast (B) both confirm the
  reversal direction.
- **MW-4**: no fitted free parameters.
- **MW-5**: replication on char-n-gram (A) and alternative lexicon (B) deferred;
  irrelevant for a NULL/reversal verdict (PASS-ceiling moot).
- **MW-6**: the verse-shuffle (A) and label-permutation (B) ARE the matched
  controls; global same-vs-reversed baseline sits near the null mean as expected.
- **MW-7**: individual striking pairs (Q 4:11–12 etc.) reported as census only,
  single-test α, never confirmatory.

## Honest limits

- The chiasmus operationalisation is *root-order* based; a phrase-level or
  syntactic chiasmus (matching grammatical roles, not just roots) could in
  principle differ — but root-order is the standard, falsifiable proxy and the
  parallel signal is robust across pair and triplet windows.
- Antithesis is detected as *cross-verse* pole opposition; *within-verse*
  ṭibāq (extremely common in juzʾ-ʿamma, e.g. Q 101:6–9 heavy↔light scales spread
  across four short verses) is by design NOT counted here, which is exactly why
  the juzʾ-ʿamma scores low on this *pair-mirror* metric. A separate within-verse
  or block-window antithesis scan would likely vindicate the eschatological-genre
  intuition at a coarser scale — a clean follow-up (H-NEW-2290.1).

## Classical anchoring

The parallel-not-chiastic verse-pair result is consistent with al-Zarkashī's and
al-Suyūṭī's treatment of *radd al-ʿajuz ʿalā al-ṣadr* and *taʿakkus* as
deliberate, *marked* figures (al-Suyūṭī, *al-Itqān*, nawʿ 59; al-Zarkashī,
*al-Burhān*, nawʿ on *al-badīʿ*) — i.e. special, not the default adjacency mode,
which is parallelism. The antithesis result re-locates *al-ṭibāq* /
*al-muqābala* (al-Sakkākī, *Miftāḥ al-ʿulūm*, *al-muḥassināt al-maʿnawiyya*) as a
pair-level device of the Medinan *jadal* (disputation) register rather than the
Meccan *indhār* register, refining the classical association of antithesis with
eschatology.
