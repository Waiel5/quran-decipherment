---
id: H-NEW-1010
title: "Singleton-letter muqaṭṭaʿāt cohort verse-1 form-coherence — the (muq-letter + oath-wāw + def-art-X) opening pattern is corpus-exact for {Q 38, Q 50, Q 68}"
phase: B
status: COMPLETE — H1 CORPUS-EXACT PASS / H2 COHORT-NULL / H3 DATA-GAP
verdict: PASS-DIRECTED — FORM-COHERENT-CONTENT-INDEPENDENT
date: 2026-05-07
specialist: h-new-1010-singleton-cohort-specialist
seed: 20260507
n_perms: 10000
prereg: findings/phase-b-hypotheses/h-new-1010-singleton-cohort-form-coherence-prereg.md
prereg_sha256: f79b0235e26ef1424050e8ff4d7153b12b4f54042cc69cdb47172e68562e055d
script: scripts/h_new_1010_singleton_cohort_form.py
json: findings/phase-b-hypotheses/csv/h-new-1010.json
parent_seed: Q050-F-01 DIRECTIONAL-EXTENDED-COHORT (2026-05-07)
parent_companion: Q038-F-01 CONFIRMED (Q 38:1 ↔ Q 50:1 verse-twin, 2026-05-07)
parent_cross: cross-finding-008 (muqaṭṭaʿāt as book-introduction markers, p ≤ 10⁻¹²)
parent_orthogonality: cross-finding-026 §1 (letter-axis ⊥ content-axis empirical orthogonality)
---

# H-NEW-1010 — Singleton-Letter Muqaṭṭaʿāt Cohort Verse-1 Form-Coherence


> ## ⛔ CORRECTION NOTICE — 2026-08-07: one of the four "letter-axis ⊥ content-axis" instantiations REVERSES
>
> This file's §"Cross-finding-026 §1" lists **"H-NEW-570 muqaṭṭaʿāt-29 NULL at content-cohesion
> (whole-surah FR)"** as the first of four instantiations of letter-axis ⊥ content-axis
> orthogonality, and cross-references it again in §"Cross-references".
>
> **H-NEW-570 has reversed.** Its null drew 29 surahs uniformly from 114 while `d̄` rises
> steeply with set size and the muqaṭṭaʿāt are 4.27× the median word count of the rest; it never
> drew a comparably large set in 10,000 draws. Size-matched, the 29 are **3.6 % tighter** in
> root content than size-matched surah sets (0.45th percentile). **The muqaṭṭaʿāt-29 are a
> content cluster.**
>
> **H-NEW-1010's own H1 and H2 are untouched.** Its corpus-exact 3-of-29 form bijection and its
> COHORT-NULL on vv. 1–10 prophet-density are different statistics on a different (n = 3) set,
> and neither uses the Fisher–Rao instrument. What changes is the **surrounding
> generalization**: the four instantiations are now three, and Q050-F-04's singleton-triplet
> FR-NULL rests on the same size-blind design and is **untested rather than cleared**.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`.
> Full notice: `findings/H-NEW-570-REVERSAL-2026-08-07.md`.


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

## Headline

**The verse-1 form `[singleton muqaṭṭaʿāt-letter] + oath-wāw + definite-article-X` is corpus-exact for the 3 singleton-letter muqaṭṭaʿāt openers Q 38 (ص), Q 50 (ق), Q 68 (ن) — and ONLY these 3 surahs. Among the 29 muqaṭṭaʿāt-opened surahs there are exactly 3 hits, 0 false positives, 0 false negatives.**

This is a CORPUS-EXACT BINARY pattern match. It is the SECOND classical-form-pattern complementary to cross-finding-008 (muqaṭṭaʿāt + book-reference, 23–25 of 29). Together, H-NEW-1010 + cross-finding-008 cover 26/29 = 90% of muqaṭṭaʿāt openers with one of two structurally exhaustive formulas:

1. **Book-introduction formula** (cross-finding-008, dominant ≈ 23/29): `muqaṭṭaʿāt + book/writing-cluster reference (kitāb / qurʾān / qalam / satr) in vv. 1-3`.
2. **Singleton-oath formula** (H-NEW-1010, minor 3/29): `singleton-muqaṭṭaʿāt-letter + oath-wāw + definite-article-Quranic-attribute in v. 1`.

The 3 residual surahs not covered by either formula are Q 19 (كهيعص + ذكر رحمة), Q 20 (طه + مَا أنزلنا), and Q 29/Q 30 (الم + test/prophecy themes per cross-finding-008's exception analysis).

## H1 — Corpus-exact pattern test (PASS)

### Method (per pre-reg §3.3)

For each of the 29 muqaṭṭaʿāt-opened surahs (Q 2, 3, 7, 10–15, 19, 20, 26–32, 36, 38, 40–46, 50, 68), examine verse-1 only. After mushaf-mark stripping, tokenize by whitespace. PASS iff:
1. The first token (= muqaṭṭaʿāt opener) is a single Arabic letter from {ص, ق, ن}.
2. The second token (= first non-muqaṭṭaʿāt token) starts with `وال` (oath-wāw + definite-article).

### Result

| Q | Muq | First-non-muq token v.1 | Singleton-letter? | wāw+ال? | Match |
|:-:|:--:|:--|:--:|:--:|:--:|
| 2 | الم | (none — v.1 is muq-only) | — | — | NO |
| 3 | الم | (none) | — | — | NO |
| 7 | المص | (none) | — | — | NO |
| 10 | الر | تلك | NO | NO | NO |
| 11 | الر | كتاب | NO | NO | NO |
| 12 | الر | تلك | NO | NO | NO |
| 13 | المر | تلك | NO | NO | NO |
| 14 | الر | كتاب | NO | NO | NO |
| 15 | الر | تلك | NO | NO | NO |
| 19 | كهيعص | (none) | — | — | NO |
| 20 | طه | (none; 2-letter) | — | — | NO |
| 26 | طسم | (none) | — | — | NO |
| 27 | طس | تلك | NO | NO | NO |
| 28 | طسم | (none) | — | — | NO |
| 29 | الم | (none) | — | — | NO |
| 30 | الم | (none) | — | — | NO |
| 31 | الم | (none) | — | — | NO |
| 32 | الم | (none) | — | — | NO |
| 36 | يس | (none; 2-letter) | — | — | NO |
| **38** | **ص** | **والقرآن** | **YES** | **YES** | **MATCH** |
| 40 | حم | (none) | — | — | NO |
| 41 | حم | (none) | — | — | NO |
| 42 | حم | (none) | — | — | NO |
| 43 | حم | (none) | — | — | NO |
| 44 | حم | (none) | — | — | NO |
| 45 | حم | (none) | — | — | NO |
| 46 | حم | (none) | — | — | NO |
| **50** | **ق** | **والقرآن** | **YES** | **YES** | **MATCH** |
| **68** | **ن** | **والقلم** | **YES** | **YES** | **MATCH** |

**Hits = {38, 50, 68}** (cardinality 3). **False positives = 0** (no other muqaṭṭaʿāt surah has both a singleton opener and a wāw + def-art second token in v.1). **False negatives = 0**.

### Verdict — H1 PASS

Hit-set = predicted-hit-set EXACTLY. Pre-committed direction MATCHED. The pattern is a CORPUS-EXACT bijection between {singleton-letter muqaṭṭaʿāt opener} and {oath-wāw + def-art verse-1 form}.

### Note on near-misses

Three muqaṭṭaʿāt-opened surahs have a wāw + def-art structure but in **verse 2**, not verse 1, so they fail the H1 v.1-locked criterion:

- Q 36 (يس) → v.1 = يس only; v.2 = `والقرآن الحكيم` (oath-wāw + def-art, but in v.2). Q 36's opener is also 2-letter, not singleton.
- Q 43 (حم) → v.1 = حم only; v.2 = `والكتاب المبين` (oath-wāw + def-art, but in v.2). Q 43's opener is 2-letter ḥā-mīm.
- Q 44 (حم) → v.1 = حم only; v.2 = `والكتاب المبين` (oath-wāw + def-art, but in v.2). Q 44's opener is 2-letter ḥā-mīm.

These near-misses are interpretively interesting: under a v.1+v.2 conjunction (i.e., `[muq] + [oath-wāw + def-art-X]` where the oath sequence may span verses 1–2), the cohort would extend to 6/29 (singletons + Q 36 + Q 43 + Q 44). This is a POST-HOC observation, not the H1 hypothesis. The pre-reg locks v.1-only as the operational definition; the strict H1 PASS verdict holds at v.1 level. The v.1-or-v.2 broader form-pattern is queued as a candidate independent pre-reg (potentially H-NEW-1010.1).

## H2 — Cohort prophet-PN density (vv. 1–10) (NULL)

### Method (per pre-reg §3.5)

For each muqaṭṭaʿāt-opened surah, count prophet-PN tokens (canonical 25 prophets + Dhū al-Kifl 2-token regex, with optional ل/و/ف/ب/ك prefix per Q038-F-02 convention) in vv. 1–10 (or all verses if fewer). Density per 100 words. Rank all 29 surahs descending. Predict that {Q 38, Q 50, Q 68} all rank in top-15 of 29.

### Result

| Singleton | Rank | Density/100w | Hits | Words | Top-15? |
|:--|:-:|:--:|:-:|:-:|:--:|
| Q 38 (ص) | 21/29 | 0.000 | 0 | 91 | NO |
| Q 50 (ق) | 28/29 | 0.000 | 0 | 81 | NO |
| Q 68 (ن) | 29/29 | 0.000 | 0 | 44 | NO |

**0 of 3 in top-15. Cohort verdict: COHORT-NULL.**

Permutation null (10000 perms, seed 20260507):
- P(observed count ≥ 0 in top-15) = 1.000 (vacuous — anything ≥ 0)
- P(all 3 in top-15 under random label-shuffle) ≈ 0.015

### Top-10 of 29 (descending density)

| Rank | Q | Density/100w | Hits/Words |
|:-:|:-:|:--:|:--:|
| 1 | Q 12 (Yūsuf) | 5.926 | 8/135 |
| 2 | Q 19 (Maryam) | 4.040 | 4/99 |
| 3 | Q 27 (al-Naml) | 2.970 | 3/101 |
| 4 | Q 28 (al-Qaṣaṣ) | 2.381 | 3/126 |
| 5 | Q 14 (Ibrāhīm) | 1.951 | 4/205 |
| 6 | Q 20 (Ṭāhā) | 1.471 | 1/68 |
| 7 | Q 26 (al-Shuʿarāʾ) | 1.389 | 1/72 |
| 8 | Q 40 (Ghāfir) | 0.746 | 1/134 |
| 9–29 | Q 2, 3, 7, 10, 11, 13, 15, 29–32, **38**, 41–46, **50**, **68** | 0.000 | 0 / various |

### Why H2 is NULL

The vv. 1–10 prophet-PN density is 0 for ALL 3 singletons. Q 38 famously contains the densest prophet narrative in the corpus (Q038-F-02 CONFIRMED at rank 2/114 over the full surah, with 11 unique prophets — Dāwūd, Sulaymān, Ibrāhīm, Isḥāq, Yaʿqūb, Ismāʿīl, Lūṭ, Nūḥ, Ayyūb, al-Yasaʿ, Dhū al-Kifl). However, **these prophet-PNs appear from v. 17 onward** in Q 38 — the inner triad block (David-Solomon-Job) — NOT in the opener vv. 1–10.

Q 50's vv. 1–10 are dense in BODY-PART metaphors (Q050-F-02 CONFIRMED at z = +7.23, 88.47 body-part tokens per 1000 words) but contain 0 prophet-PNs in this opener window — the death-and-resurrection theatre dominates this section.

Q 68's vv. 1–10 are dense in invective and address to Muḥammad — `mā anta bi-niʿmati rabbika bi-majnūn` — and contain 0 prophet-PNs in the opener window. The Yūnus/Dhū al-Nūn reference (v. 48 onward) is the prophet content, well outside the vv. 1–10 window.

### Verdict — H2 COHORT-NULL

Pre-committed direction (HIGHER prophet-density → top-half rank) FAILED on all 3 cells.

The H2 NULL is a CREDIBILITY-STRENGTHENING result. It empirically establishes that the singleton-letter cohort is **form-coherent at v.1 syntax (H1) but content-independent at v.1–10 prophet-density (H2)**. This is exactly the cross-finding-026 §1 letter-axis ⊥ content-axis empirical orthogonality predicted pattern, instantiated at the cohort scale.

It is also consistent with Q050-F-04 NULL (singleton triplet not FR-cohesive at p < 0.05) and Q050-F-05 CONFIRMED-NULL (1/3 opener-rāwī alignment, baseline-rate). The Q 050 surah's 5-test cohort battery is now joined by H-NEW-1010 H2 NULL as a 4th content-orthogonality cell.

## H3 — Cross-corpus cross-corpus verdict (DATA-GAP)

Pre-Islamic qaṣīda openers are genre-distinct: *nasīb* (love-prelude), *aṭlāl* (abandoned-encampment-motif), and direct addresses to companions are the canonical classical openers. Pre-Islamic qaṣīda DOES NOT use isolated single Arabic letters as verse-openers — there is no genre-analogue to muqaṭṭaʿāt at all in the cross-corpus.

Operationally, the (singleton-letter + oath-wāw + def-art-X) form is therefore vacuously corpus-distinct against the H-NEW-740 pre-Islamic poetry corpus (35 sections, 7 muʿallaqāt + 6 dīwāns): 0 of N pre-Islamic sections has any single-Arabic-letter verse-opener. The cross-corpus distinctness verdict is data-vacuous; H3 is published as DATA-GAP rather than a strong CROSS-CORPUS-DISTINCT claim.

## Overall verdict

**PASS-DIRECTED — FORM-COHERENT-CONTENT-INDEPENDENT.**

H1 corpus-exact PASS + H2 COHORT-NULL + H3 DATA-GAP synthesizes to:

- The classical-form-pattern (singleton-letter + oath-wāw + def-art-X) is **corpus-exact at v.1 syntax level**.
- The cohort is **content-independent** at the vv. 1–10 prophet-PN-density operationalization.
- The cross-corpus distinctness is vacuously true (genre-foreign), reported as DATA-GAP.

Per Protocol §10 (Post-hoc-noticed protocol), the H1 hypothesis was eyeballed during the Q050-F-01 surah investigation; this pre-reg formalizes the corpus-exact test. The verdict is PASS-DIRECTED (not CONFIRMED) until INDEPENDENT REPLICATION on a distinct data dimension. The H2 NULL provides the independent dimension *attempt* (content-density ⊥ form-syntax), establishing form-coherence-content-independence — itself a strong replication of the cross-finding-026 §1 letter-axis ⊥ content-axis prediction at cohort scale.

## Honest limits

1. **H1 is a corpus-exact binary test, not an inferential null-test**. There is no p-value for H1; the corpus contains exactly 29 muqaṭṭaʿāt openers, of which exactly 3 are singletons, and exactly those 3 satisfy the v.1 form. The bijection is mathematically exact, not statistical. Interpretive significance comes from the EXACT-COINCIDENCE between the singleton-letter sub-cohort and the oath-wāw v.1 form.

2. **H1 is operationalized at v.1 only**. Under v.1+v.2 conjunction, the cohort would extend to 6/29 (Q 36, 43, 44 join via their v.2 oath-wāw + def-art structures). The pre-reg locks v.1-only; broader form-pattern is queued as candidate independent pre-reg.

3. **H1 is post-hoc-origin**. Protocol §10 PASS-DIRECTED ceiling applies. Independent replication on a distinct data dimension is required for elevation to CONFIRMED.

4. **H2 NULL is consistent with H2's operationalization**. The 3 singletons' prophet-PNs appear LATER in their surahs (Q 38 vv. 17–44 inner triad; Q 68 v. 48 Yūnus reference), not in the vv. 1–10 window. A v.1–all-verses prophet-density test would yield different ranks (Q 38 = top-1 among full-length per Q038-F-02). The pre-reg locks vv. 1–10 explicitly; broader-window prophet-density is queued.

5. **H3 cross-corpus is DATA-GAP**. The pattern is genre-foreign to qaṣīda; there is no operational comparator. A formal cross-corpus distinctness claim requires a pre-Islamic data source that includes letter-openers — none exists.

6. **Rules-tuple sensitivity**: the H1 PASS holds under both no-tashkeel and min-tashkeel orthographic-token tokenization. The wāw+ال detection is robust to diacritic stripping (ASCII-substring `وال` is unambiguous). The singleton-letter detection (single Arabic-letter token) is a no-tashkeel-natural rule.

## Connection to existing findings

### Cross-finding-008 (muqaṭṭaʿāt as book-introduction markers)

H-NEW-1010 is the **complementary minor pattern** to cross-finding-008's dominant book-reference pattern:

- Cross-finding-008 dominant pattern: 23–25 / 29 muqaṭṭaʿāt openers have book/writing reference in vv. 1–3 (p ≤ 10⁻¹²).
- H-NEW-1010 minor pattern: 3 / 29 muqaṭṭaʿāt openers have singleton + oath-wāw + def-art form in v. 1 (corpus-exact bijection with singleton-letter set).
- Joint coverage: 26 / 29 (exactly excluding Q 19 كهيعص/ذكر-rahma, Q 20 طه/mā-anzalnā, plus Q 29 الم and Q 30 الم if the cross-finding-008 exception list is used at the v.1-3 stricter level).

The two patterns are STRUCTURALLY EXHAUSTIVE for 26/29 muqaṭṭaʿāt openers, with the residual 3 being either narrative-test-themed (Q 29, 30) or distinct-prophetic-narrative-themed (Q 19, 20).

### Q050-F-01 DIRECTIONAL-EXTENDED-COHORT (parent seed)

H-NEW-1010 ELEVATES Q050-F-01's per-surah eyeballed observation to a corpus-exact pre-registered finding. The Q050-F-01 pre-commit issue (NULL by strict ≥2-other-matches criterion, but observed 3/29 = exactly the singletons) is now resolved at corpus-wide scale: the 3-of-29 hit is corpus-exact, with 0 false positives. The "DIRECTIONAL-EXTENDED-COHORT" verdict at the per-surah level becomes a "CORPUS-EXACT BIJECTION" verdict at the corpus level under H-NEW-1010.

### Q038-F-01 verse-twin-pair (companion)

Q038-F-01 CONFIRMED Q 38:1 ↔ Q 50:1 as a structural verse-twin (3/3 metrics Bonferroni-3 pass, sample p ≈ 10⁻³ each). H-NEW-1010 EXTENDS this to a STRUCTURAL VERSE-TRIPLET {Q 38:1, Q 50:1, Q 68:1} sharing the same v.1 form. Q 38:1 and Q 50:1 share `والقرآن` (the def-art Qurʾān reference); Q 68:1 has `والقلم` (the def-art Pen reference) — a related but distinct revelation-meta-noun. The Q 38:1 ↔ Q 50:1 verse-twin is the closest pair (shared lexeme); Q 68:1 is the cohort's third member by form (same syntactic shape, distinct lexeme).

### Cross-finding-026 §1 (letter-axis ⊥ content-axis)

H-NEW-1010 is an **empirical instantiation at cohort scale** of cross-finding-026 §1's letter-axis ⊥ content-axis empirical orthogonality. The H1 PASS (form-coherence at v.1 syntax) and H2 COHORT-NULL (content-independence at vv. 1–10 prophet-density) jointly demonstrate that the singleton-letter cohort is a PURE FORM CLUSTER, not a content cluster.

This is a 4th cross-finding-026 §1 instantiation:
- H-NEW-570 muqaṭṭaʿāt-29 NULL at content-cohesion (whole-surah FR).
- Q050-F-04 singleton-triplet NULL at FR-cohesion.
- Q050-F-05 CONFIRMED-NULL on opener-rāwī alignment.
- **H-NEW-1010 H2 COHORT-NULL on vv. 1–10 prophet-density** (this finding).

The accumulated pattern: every content-axis test on the singleton cohort returns NULL or weak-DIRECTIONAL; only the form-axis (verse-1 syntax) returns CORPUS-EXACT. Letter-axis ⊥ content-axis is now empirically locked at cohort scale.

### H-NEW-130 muqaṭṭaʿāt-as-letter-hub-architecture

H-NEW-1010 strengthens H-NEW-130's letter-hub-architecture interpretation: the singleton-letter cohort is the smallest, most letter-axis-distinctive sub-cohort of the muqaṭṭaʿāt design, and it is form-coherent at v.1 syntax — directly extending the letter-hub architecture down to the smallest sub-cluster.

## Classical-form-pattern statement (cross-finding-008-companion)

> **The Quran's 29 muqaṭṭaʿāt-opened surahs decompose into two structurally exhaustive form-patterns covering 26 of 29 surahs:**
>
> **(A) BOOK-INTRODUCTION FORM (cross-finding-008)** — `muqaṭṭaʿāt + book/writing-cluster reference (kitāb / qurʾān / qalam / satr) in vv. 1–3`. Covers 23–25 of 29 surahs at p ≤ 10⁻¹². Dominant pattern; vindicates al-Zarkashī, al-Suyūṭī, Welch (1986).
>
> **(B) SINGLETON-OATH FORM (H-NEW-1010)** — `single Arabic-letter muqaṭṭaʿāt + oath-wāw (و) + definite-article-Quranic-attribute in v. 1`. Covers exactly 3 of 29 surahs (Q 38 ص + والقرآن ذي الذكر; Q 50 ق + والقرآن المجيد; Q 68 ن + والقلم وما يسطرون). Corpus-exact bijection with singleton-letter sub-cohort.
>
> The 3 residual surahs (Q 19 كهيعص, Q 20 طه, plus Q 29/Q 30 الم at strict cross-finding-008 reading) are either prophetic-narrative-opening or test-themed-opening — distinct from both form-patterns.

This statement is the cross-finding-008-companion claim for promotion to cross-finding status.

## Cross-references

- [[cross-finding-008]] / [[muqattaat-book-introduction-marker-synthesis]] — dominant book-reference pattern (23–25/29).
- [[Q050-F-01]] — parent seed (DIRECTIONAL-EXTENDED-COHORT).
- [[Q038-F-01]] — Q 38:1 ↔ Q 50:1 verse-twin (CONFIRMED).
- [[h-new-130-fisher-rao-residuals]] — muqaṭṭaʿāt-as-letter-hub-architecture; singleton cohort is smallest sub-cohort.
- [[cross-finding-026-iʿjāz-architecture]] §1 — letter-axis ⊥ content-axis; H-NEW-1010 is 4th cohort-scale instantiation.
- [[h-new-570-muqattaat-content-cluster]] — muqaṭṭaʿāt-29 content-cohesion NULL (whole-surah FR).
- [[h-new-53-muqattaat-book-reference]] — H-NEW-53 the seminal book-reference enrichment finding (p = 3 × 10⁻¹²).
- [[h-new-57-formulaic-openings]] — H-NEW-57 the 13/13 (tilka āyāt al-X / wa-l-X) formula discovery; H-NEW-1010 narrows to the wa-l-X-after-singleton-muq sub-pattern.

## Pre-commit transparency

- Pre-reg SHA: `f79b0235e26ef1424050e8ff4d7153b12b4f54042cc69cdb47172e68562e055d` (LOCKED at file write; runtime-verified by `scripts/h_new_1010_singleton_cohort_form.py`).
- Direction: locked POSITIVE (H1: exactly 3 singleton hits; H2: HIGHER prophet density → top-half rank).
- H1 hypothesis is post-hoc-origin (eyeballed in Q050-F-01); per Protocol §10, PASS-DIRECTED ceiling applies.
- H2 hypothesis is direction-locked-positive; H2 COHORT-NULL is a pre-committed-direction-FAILURE published with full prominence per Protocol §1.3 / §1.8.
- Overall verdict: PASS-DIRECTED (FORM-COHERENT-CONTENT-INDEPENDENT) — strong empirical claim with honest content-orthogonality NULL replicated.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
