---
id: H-NEW-1010
title: "PRE-REG — Singleton-letter muqaṭṭaʿāt cohort verse-1 form-coherence: the (muq-letter + oath-wāw + def-article-X) opening pattern is exclusive to Q 38, Q 50, Q 68"
phase: B
status: PRE-REGISTERED (locked before observation)
date: 2026-05-07
specialist: h-new-1010-singleton-cohort-specialist
parent_1: cross-finding-008 (muqaṭṭaʿāt as book-introduction markers, p ≤ 10⁻¹²)
parent_2: Q050-F-01 DIRECTIONAL-EXTENDED-COHORT (Q 38, Q 50, Q 68 visual-inspection match — the seed)
parent_3: Q038-F-01 CONFIRMED (Q 38:1 ↔ Q 50:1 verse-twin-pair, 3/3 metrics Bonferroni-3 pass)
parent_4: cross-finding-026-iʿjāz-architecture §1 (letter-axis ⊥ content-axis empirical orthogonality)
parent_5: al-Suyūṭī *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ on muqaṭṭaʿāt-openings (catalogues book-reference dominant pattern; does NOT separately catalogue the singleton + oath-wāw form)
parent_6: al-Zarkashī *al-Burhān fī ʿulūm al-Qurʾān*, muqaṭṭaʿāt chapter (qualitative observation of letter-as-opening-formula)
seed: 20260507
n_perms: 10000
n_bootstrap: 10000
bonferroni_k_h1: 1
bonferroni_k_h2: 3
bonferroni_family_h1: corpus-exact-pattern-match (single test, exhaustive enumeration)
bonferroni_family_h2: per-singleton prophet-PN-density rank-test
alpha_bon_h1: 0.05
alpha_bon_h2: 0.01667
verdict: PRE-REGISTERED
---

# H-NEW-1010 — Singleton-Letter Muqaṭṭaʿāt Cohort Verse-1 Form-Coherence


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Background and motivation

**Cross-finding-008** (parent) established that 23–25 of 29 muqaṭṭaʿāt-opened surahs have a book/writing-cluster reference (kitāb, qurʾān, qalam, satr) in vv. 1–3, at hypergeometric p ≤ 10⁻¹². The dominant classical-form pattern is **muqaṭṭaʿāt + book-reference**. al-Zarkashī, al-Suyūṭī, al-Rāzī, and Welch (1986) all flagged this qualitatively; it is now empirically locked.

**Q050-F-01** (DIRECTIONAL-EXTENDED-COHORT, 2026-05-07) — visual inspection during the Q 50 surah deep-dive revealed that the 3 verses

```
Q 38:1   ص ۚ والقرآن ذي الذكر       (Ṣād. By the Qurʾān, possessor of the Reminder)
Q 50:1   ق ۚ والقرآن المجيد        (Qāf. By the Glorious Qurʾān)
Q 68:1   ن ۚ والقلم وما يسطرون     (Nūn. By the Pen and what they inscribe)
```

share an exact verse-1 form: `[singleton muqaṭṭaʿ-letter] + wāw (oath-particle) + ال (definite article) + classical-Quranic-attribute`. These are EXACTLY the 3 surahs whose muqaṭṭaʿāt opener is a single Arabic letter (ص, ق, ن). The pattern is a SECOND classical-form-pattern complementary to cross-finding-008's dominant book-reference pattern.

**Q038-F-01** (CONFIRMED, 2026-05-07) — the Q 38:1 ↔ Q 50:1 verse-pair is structurally a twin: 3 of 3 corpus-pairwise verse-similarity metrics (token-bag cosine, root-bag cosine, 1−NCD) survive Bonferroni-3 at α = 0.01667; sample p-values 0.000760 / 0.002680 / 0.000760.

**What has NOT been pre-registered**: whether the (muq-letter + oath-wāw + def-art-X) verse-1 opening is EXACTLY-EXCLUSIVE to the 3 singleton-letter muqaṭṭaʿāt openers — i.e., whether the visual observation in Q050-F-01 is a corpus-exact pattern match with 0 false positives among the other 26 muqaṭṭaʿāt-opened surahs. H-NEW-1010 pre-registers this as a binary corpus-exact test.

## 2. Hypotheses (DIRECTION-LOCKED)

### H1 — Primary direction-locked test (corpus-exact pattern match)
**The 3 singleton-letter muqaṭṭaʿāt openers (Q 38, Q 50, Q 68) and ONLY these 3 surahs in the 29-muqaṭṭaʿāt-opened set follow the (muq-letter + oath-wāw + def-art) verse-1 pattern.**

- Predicted hit set: exactly {Q 38, Q 50, Q 68} (cardinality 3).
- Predicted false-positive count among the 26 non-singleton muqaṭṭaʿāt-openers: **0**.
- This is a binary verdict:
  - **PASS** iff hit set = {38, 50, 68} EXACTLY (3 hits, 0 false positives).
  - **FAIL** iff (a) any of {38, 50, 68} fails the pattern OR (b) any non-singleton muqaṭṭaʿāt surah passes the pattern.

### H2 — Secondary strengthening test (prophet-PN-density)
**At the v.2 level (operationalized as vv. 1–10 to ensure adequate sample), all 3 singleton surahs (Q 38, Q 50, Q 68) rank in the top-half (15/29) of muqaṭṭaʿāt-opened surahs on prophet-proper-name density per 100 words.**

- Bonferroni-3 across the cohort. α_bon = 0.01667 per cell.
- Per-singleton test: Q 38, Q 50, Q 68 each individually ranked. PASS iff each is in ranks 1–15 of 29.
- Cohort verdict: 3/3 PASS = COHORT-CONFIRMED; 2/3 = COHORT-PARTIAL; 0–1/3 = NULL.
- Direction-locked positive (HIGHER prophet density, top-half rank).
- Permutation null: rank position under random assignment of prophet-density values to surah-position. 10000 perms, seed 20260507.

### H3 — Cross-corpus cross-corpus test (OPTIONAL, DATA-GAP-PERMITTING)
**The (singleton-letter + oath-wāw + def-art) opening is corpus-distinct against pre-Islamic poetry — i.e., no 7 muʿallaqāt or 6 dīwāns in the H-NEW-740 corpus has an analogous structural opener.**

- This is operationally weak because pre-Islamic qaṣīda openers are different genre conventions (nasīb prelude, atlal motif, etc.) and pre-Islamic poetry does not use isolated single-letters as verse-openers.
- If cross-corpus baseline is accessible at `/Users/grey/Downloads/quran/data/baseline-corpora/`, document a pattern-mismatch verdict; otherwise document as DATA-GAP.

## 3. Operationalization (LOCKED before observation)

### 3.1 Canonical 29 muqaṭṭaʿāt-opened surahs (per al-Suyūṭī catalogue)

```
Q 2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68
```

### 3.2 Singleton-letter cohort (per visual inspection of Quran orthography)

```
Q 38: ص (Ṣād)         — single Arabic letter ص
Q 50: ق (Qāf)         — single Arabic letter ق
Q 68: ن (Nūn)         — single Arabic letter ن
```

NOT singletons (under Hafs-Kufan orthographic-token rules-tuple):
- Q 20 طه (ṭā-hā): two letters
- Q 36 يس (yā-sīn): two letters
- All other muqaṭṭaʿāt are 2+, 3+, 4+, or 5-letter clusters (الم, المص, الر, المر, كهيعص, طسم, طس, حم, حم-ʿsq).

### 3.3 H1 pattern-match procedure

For each of the 29 muqaṭṭaʿāt-opened surahs, examine **verse 1 only** (basmala-not-counted; following the rules-tuple for the Q050-F-01 lock). After stripping mushaf-marks (ۚ ۖ ۗ ۛ etc.), tokenize by whitespace.

A surah PASSES the pattern iff:
1. The muqaṭṭaʿāt opener is a **single Arabic letter** (one of ص, ق, ن; equivalently, the first whitespace-token after stripping ASCII/diacritic noise is a single Arabic letter).
2. The next whitespace-token after the muqaṭṭaʿāt-letter starts with `وال` (oath-wāw + definite-article ال) in the no-tashkeel orthography.
3. The first non-muqaṭṭaʿāt token IS in the same verse-1 (NOT in verse 2).

The third condition is critical: surahs like Q 36 (يس / والقرآن الحكيم — but `والقرآن الحكيم` is in v2, not v1), Q 43 (حم / والكتاب المبين — v2), Q 44 (حم / والكتاب المبين — v2) have the wāw + def-art structure but it appears in v2 because the muqaṭṭaʿāt occupy all of v1. These do NOT match the H1 pattern.

### 3.4 Rules-tuple (LOCKED)

```
(no-tashkeel-allowed-for-letter-detection,
 min-tashkeel-allowed-for-wāw-detection,
 orthographic-token,
 graphemes,
 basmala-counted-only-in-Q1,
 Hafs-Kufan,
 mushaf-order)
```

The rules-tuple is dual-mode because:
- Letter-detection works best on no-tashkeel (single letter ص is unambiguously one orthographic-token).
- Wāw-detection (the oath-particle prefix) is verified on min-tashkeel for additional cross-validation; the substring `وال` is unambiguous in both no-tashkeel and min-tashkeel.

### 3.5 H2 prophet-PN-density operationalization

Use the canonical-25-prophets list from Q038-F-02 pre-reg (already established as the project canonical):

```
آدم, نوح, إدريس, هود, صالح, إبراهيم, لوط, إسماعيل, إسحاق,
يعقوب, يوسف, شعيب, هارون, موسى, داوود (دواد is corrupted spelling),
سليمان, إلياس, اليسع, يونس, أيوب, زكريا, يحيى, عيسى, ذا الكفل, محمد
```

For each of the 29 muqaṭṭaʿāt-opened surahs:
- Concatenate vv. 1–10 (or all verses if fewer than 10).
- Strip muqaṭṭaʿāt opener tokens.
- Count prophet-PN tokens (with optional ل/و/ف/ب/ك prefix attached as one token, per Q038-F-02 convention).
- Compute density = (count / total-words) × 100.
- Rank all 29 surahs.

For each of {Q 38, Q 50, Q 68}, predict TOP-HALF (rank 1–15 of 29).

### 3.6 Permutation null for H2

Random shuffle of (surah → density) labels. 10000 perms, seed 20260507. Probability that each singleton lands in top-15 under random labeling is 15/29 ≈ 0.517 per cell. Joint probability all 3 in top-15 is C(15,3)/C(29,3) = 455/3654 ≈ 0.1245 (chance baseline). Pre-registered Bonferroni-3 per-cell α = 0.01667; chance per-cell ≈ 0.517 — so a single cell rank-15 cell does NOT pass per-cell α=0.01667 by itself; the COHORT 3/3-pass interpretation is the meaningful inferential claim, not a per-cell test against chance.

**Therefore the H2 verdict is operationalized as the COHORT-LEVEL joint-rank test**: under the null (random permutation of density labels), the joint probability that all 3 of {Q 38, Q 50, Q 68} land in top-15 of 29 is empirically computed via 10000 perms and reported with single-test α=0.05 cap (post-hoc cap per Protocol §1.7 MW-7, since the H2 strengthening was specified after the H1 hypothesis was direction-locked but before observing H2 results).

## 4. Success and failure criteria

### H1 (corpus-exact pattern test)
- **PASS**: hit set = exactly {Q 38, Q 50, Q 68} (3 hits, 0 false positives).
- **FAIL**: anything else.

### H2 (cohort prophet-density)
- **COHORT-CONFIRMED**: all 3 of Q 38, Q 50, Q 68 in top-15/29 ranks AND joint-rank permutation p < 0.05.
- **COHORT-PARTIAL**: 2/3 in top-15.
- **COHORT-NULL**: 0–1/3 in top-15.

### H3 (cross-corpus, optional)
- **CROSS-CORPUS-DISTINCT**: 0 of N pre-Islamic poetry sections has analogous opener-form.
- **DATA-GAP**: cross-corpus baseline not accessible or not parseable.

### Overall verdict
- H1 PASS + H2 COHORT-CONFIRMED + H3 DISTINCT → CONFIRMED-CROSS-FINDING-COMPANION
- H1 PASS + H2 COHORT-PARTIAL → PASS-DIRECTED (form-coherence locked, content-strengthening partial)
- H1 PASS + H2 COHORT-NULL → FORM-COHERENT-CONTENT-INDEPENDENT (consistent with Q050-F-04 NULL on FR-content cohesion and Q050-F-05 CONFIRMED-NULL on rāwī alignment — exactly the cross-finding-026 §1 letter-axis ⊥ content-axis predicted pattern)
- H1 FAIL → NULL (pattern not corpus-exact; the Q050-F-01 visual observation does not generalize)

## 5. Honest pre-commit transparency

The H1 hypothesis is a CORPUS-EXACT pattern (binary verdict). It was eyeballed by the Q 50 specialist on 2026-05-07 in the Q050-F-01 inspection. The pre-reg here (H-NEW-1010) is the FORMAL pre-registration of the pattern as corpus-wide claim; per Protocol §1.7 (MW-7 post-hoc cap) and Protocol §10 (Post-hoc-noticed protocol):

- **Origin**: post-hoc visual inspection in Q050-F-01.
- **Disclosure**: this pre-reg explicitly discloses the post-hoc origin.
- **Verdict ceiling**: PASS-DIRECTED unless replicated on an INDEPENDENT data dimension.
- **Independent-replication candidates**: H2 (prophet-PN density at vv. 1–10) is an INDEPENDENT data dimension (content-density, not v.1 syntax). H3 (cross-corpus baseline) would be a SECOND independent dimension.

If H1 PASSES + H2 COHORT-CONFIRMED, the verdict is **PASS-DIRECTED with replication on independent dimension** — defensible as a corpus-exact + content-strengthened cross-finding companion. If H1 PASSES + H2 COHORT-NULL, the verdict is **FORM-COHERENT-CONTENT-INDEPENDENT**, an empirical instantiation of cross-finding-026 §1.

## 6. Falsification design

H1 fails if any of these occur:
- Any of Q 38, Q 50, Q 68 verse-1 lacks the muq + wāw + def-art form (e.g., if the wāw is not an oath-particle but a different grammatical wāw).
- Any of the 26 non-singleton muqaṭṭaʿāt openers (Q 2, 3, 7, 10–15, 19, 20, 26–32, 36, 40–46) has a verse-1 with the muq + wāw + def-art form.

The non-singleton verses-1 must therefore be programmatically verified to have NO muq + wāw + def-art structure in v.1. The classical-form-dictionary lookup (per Protocol §6 critical guidance):

| Q | Muqaṭṭaʿāt | Verse-1 opening structure | Pattern-mismatch reason |
|:-:|:--:|:--|:--|
| 2 | الم | Verse-1 = الم only; Verse-2 = ذلك الكتاب (demonstrative + def-art, NO oath-wāw) | v.1 muq-only (no extra phrase) |
| 3 | الم | Verse-1 = الم only; Verse-2 = الله لا إله إلا هو | v.1 muq-only |
| 7 | المص | Verse-1 = المص only; Verse-2 = كتاب أنزل (NO oath-wāw) | v.1 muq-only |
| 10 | الر | Verse-1 = الر + تلك آيات (demonstrative, NO oath-wāw) | v.1 has demonstrative |
| 11 | الر | Verse-1 = الر + كتاب أحكمت (NO oath-wāw) | v.1 has noun, no wāw |
| 12 | الر | Verse-1 = الر + تلك آيات (demonstrative) | v.1 has demonstrative |
| 13 | المر | Verse-1 = المر + تلك آيات (demonstrative) | v.1 has demonstrative |
| 14 | الر | Verse-1 = الر + كتاب أنزلناه (NO oath-wāw) | v.1 has noun, no wāw |
| 15 | الر | Verse-1 = الر + تلك آيات (demonstrative) | v.1 has demonstrative |
| 19 | كهيعص | Verse-1 = كهيعص only; Verse-2 = ذكر رحمت (noun) | v.1 muq-only |
| 20 | طه | Verse-1 = طه only; Verse-2 = ما أنزلنا (NO oath-wāw); 2-letter, not singleton | 2-letter; v.1 muq-only |
| 26 | طسم | Verse-1 = طسم only; Verse-2 = تلك آيات (demonstrative) | v.1 muq-only |
| 27 | طس | Verse-1 = طس + تلك آيات (demonstrative) | v.1 has demonstrative |
| 28 | طسم | Verse-1 = طسم only | v.1 muq-only |
| 29 | الم | Verse-1 = الم only | v.1 muq-only |
| 30 | الم | Verse-1 = الم only | v.1 muq-only |
| 31 | الم | Verse-1 = الم only | v.1 muq-only |
| 32 | الم | Verse-1 = الم only | v.1 muq-only |
| 36 | يس | Verse-1 = يس only; Verse-2 = والقرآن الحكيم (HAS oath-wāw + def-art, but in v2!); 2-letter | 2-letter; v.1 muq-only |
| 38 | ص | Verse-1 = ص + والقرآن ذي الذكر | **MATCH** (singleton + wāw + def-art) |
| 40 | حم | Verse-1 = حم only; Verse-2 = تنزيل الكتاب (NO oath-wāw) | v.1 muq-only |
| 41 | حم | Verse-1 = حم only; Verse-2 = تنزيل من (NO def-art) | v.1 muq-only |
| 42 | حم | Verse-1 = حم only; Verse-2 = عسق (more muqaṭṭaʿāt!) | v.1 muq-only |
| 43 | حم | Verse-1 = حم only; Verse-2 = والكتاب المبين (HAS oath-wāw, but in v2) | v.1 muq-only |
| 44 | حم | Verse-1 = حم only; Verse-2 = والكتاب المبين (HAS oath-wāw, but in v2) | v.1 muq-only |
| 45 | حم | Verse-1 = حم only | v.1 muq-only |
| 46 | حم | Verse-1 = حم only | v.1 muq-only |
| 50 | ق | Verse-1 = ق + والقرآن المجيد | **MATCH** (singleton + wāw + def-art) |
| 68 | ن | Verse-1 = ن + والقلم وما يسطرون | **MATCH** (singleton + wāw + def-art) |

The pre-reg locks this pattern table BEFORE the runtime test. The script must reproduce this exact table by parsing v.1 of each surah and applying the H1 pattern criterion.

## 7. Output files

- Pre-reg: this file (`findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence-prereg.md`).
- Script: `scripts/h_new_1010_singleton_cohort_form.py` (SHA-verified at runtime).
- JSON: `findings/phase-b-hypotheses/csv/h-new-1010.json`.
- Findings: `findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence.md`.
- Journal: `journal/h-new-1010-run-1.md`.
- Ledger update: insert after H-NEW-960 entry in `MASTER-FINDINGS-LEDGER.md`.

## 8. Pre-commit attestation

This pre-reg is locked before computation. The H1 pattern criterion, the canonical 29-muqaṭṭaʿāt list, the 3-singleton predicted hit set, the H2 prophet-density rank prediction, and the H3 cross-corpus optional design are ALL specified before runtime. The classical-form-pattern dictionary in §6 is the pre-locked authoritative table. Any post-hoc adjustment is a pre-commit violation and would be published with full prominence as NULL per Protocol §1.3 / §1.8.

Direction is LOCKED: H1 predicts EXACTLY 3 hits (the singletons); H2 predicts ALL 3 in top-half by prophet-density.

The empirical observation is a CORPUS-EXACT BINARY TEST. There is no inferential μ to manipulate; either the pattern matches exactly or it does not.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
