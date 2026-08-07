---
finding: H-NEW-2450
title: The ADJACENT near-verbatim reprise — corpus census + adjacency-excess / genre-concentration
date: 2026-05-30
phase: B+
seed: 20260509
nperm: 10000
prereg_sha256: 11f93da43357ff93bb6efdcdd26d716cb3ded2218e4896b897fb776cb69bf6bd
verdict: H1 PRE-COMMIT VIOLATION → NULL (reversed, full prominence) · H2 PASS · CENSUS delivered
extends: Q094-F-01 (§10.118), H-NEW-2310 (refrain), H-NEW-2350/2380 (cross-surah twins), H-NEW-2420 (within-surah naẓm)
---

# H-NEW-2450 — The "immediately echoed verse": the adjacent near-verbatim reprise rung


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

**The repetition scale-ladder finally has its finest rung.** The project has censused repeated material at every scale EXCEPT the immediately-adjacent one: H-NEW-2310 catalogued byte-exact refrains (any spacing), H-NEW-2350 the exact cross-surah verse-twins, H-NEW-2380 the near cross-surah twins (≤2 token edits, **non-adjacent**). Q094-F-01 then discovered that Q94:5-6 (*fa-inna maʿa al-ʿusri yusrā / inna maʿa al-ʿusri yusrā*) is the corpus-tightest **adjacent** couplet — a verse echoed at position i+1 with a single-fāʾ change — and noted it is INVISIBLE to the byte-exact refrain census. This finding builds the dedicated census of that (i, i+1) rung: the full edit-distance distribution over every adjacent verse-pair, the low-edit roster, the edit-1/2/3 families, and two pre-registered direction-locked tests.

This is **compositional repetition with variation in one canonical Hafs-Kūfan text** — not qirāʾāt, not naskh.

**Two-part honest verdict.** The **device is real and genre-concentrated** (H2 PASS, p=0.0097), but the pre-registered claim that the Quran *places* near-identical verses **adjacent** more than chance is **decisively REVERSED** (H1 pre-commit violation, p=1.0): when the Quran owns a family of near-identical verses it **DISPERSES** them, it does not stack them. The adjacent reprise (Q94:5-6) is a rare *figure*, not the corpus's default handling of look-alike verses.

Pre-reg SHA-256 `11f93da43357ff93bb6efdcdd26d716cb3ded2218e4896b897fb776cb69bf6bd`, seed 20260509, 10000 permutations, runtime-verified (fail-fast assert passed).

## Instrument

- **Text:** `quran-text/quran-no-tashkeel.json`. Rules-tuple `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`.
- **The H-NEW-2380 waqf lesson (LOCKED):** the no-tashkeel file carries 4,578 standalone Quranic waqf / pause / codex glyphs (U+06D6–U+06ED — pause marks, rub-el-ḥizb U+06DE, sajda U+06E9) as whitespace-separated tokens. These are recitation/codex annotations, NOT lexical words, and are stripped before tokenizing.
- **Adjacency:** same-surah (verse i, verse i+1) in canonical order — **6,122 within-surah pairs** (= 6,236 verses − 114 surahs). The 113 cross-surah junctions are EXCLUDED (the reprise is a within-surah device; the cross-surah rung is H-NEW-2350/2380).
- **Edit distance, TWO levels:** **char-edit** = Levenshtein over the verses' tokens joined with no separator (the Q094-F-01 Arm B convention; PRIMARY ranking metric — it discriminates a one-letter connective from a whole-word swap, which token-edit collapses to 1); **token-edit** = Levenshtein over the token sequences. Both reported per pair.
- **Substantive filter:** both verses ≥ 3 lexical tokens (Q094-F-01 `SUB=3`) — excludes muqaṭṭaʿāt and 1–2-word verses whose tiny distances are not "reprise." **5,821 substantive pairs.**
- **Test band (locked a priori):** `char-edit ≤ 3` (the closed low tail edit-1 ∪ edit-2 ∪ edit-3). **Reporting roster:** `char-edit ≤ 6` (descriptive bucket, NOT a test threshold).

## The census — the low tail is a near-empty desert with a sharp floor

| char-edit | substantive adjacent pairs |
|:-:|:-:|
| **0 (exact)** | **0** |
| 1 | **1** |
| 2 | 4 |
| 3 | 1 |
| 4 | 3 |
| 5 | 6 |
| 6 | 18 |
| 7 | 26 |
| … | bulk centred ≈ 13–16, long right tail to 506 |

**There are ZERO exact-verbatim adjacencies in the entire corpus** (confirming Q094-F-01 Arm B at census scale) and exactly **one** char-edit-1 pair. The distribution then climbs through a thin band (edit 2–6: 4, 1, 3, 6, 18) before joining the bulk. The reprise is a genuinely rare device — at char-edit ≤ 3 there are just **6 pairs corpus-wide**. Token-edit confirms it: only 4 pairs at token-edit 1, 40 at token-edit 2.

### The edit-1 singleton, edit-2 family, edit-3 family (with aligned edits)

| c | t | pair | text i → text j | differing token(s) |
|:-:|:-:|:--|:--|:--|
| **1** | 1 | **Q94:5-6** | فإن مع العسر يسرا → إن مع العسر يسرا | `فإن → إن` (drop leading fāʾ) |
| 2 | 1 | Q75:34-35 | أولى لك فأولى → ثم أولى لك فأولى | prepend `ثم` |
| 2 | 1 | Q102:3-4 | كلا سوف تعلمون → ثم كلا سوف تعلمون | prepend `ثم` |
| 2 | 2 | Q74:19-20 | فقتل كيف قدر → ثم قتل كيف قدر | prepend `ثم` + `فقتل → قتل` |
| 2 | 2 | Q82:17-18 | وما أدراك ما يوم الدين → ثم ما أدراك ما يوم الدين | prepend `ثم` + `وما → ما` |
| 3 | 2 | Q99:7-8 | فمن يعمل مثقال ذرة خيرا يره → ومن يعمل مثقال ذرة شرا يره | `فمن → ومن` + `خيرا → شرا` |

These six are **exactly the Arm-B family Q094-F-01 predicted** ({Q94:5-6} edit-1 + {Q74:19-20, Q75:34-35, Q82:17-18, Q102:3-4} edit-2), now machine-confirmed as the complete ≤3 set plus Q99:7-8 at edit-3. Note the dominant mechanism in the ≤2 band: **the *thumma* / *fa* / *wa* connective re-anchoring** — the same verse re-spoken with an intensifying particle (*thumma* "then again," Q75/Q102/Q74/Q82), or the leading fāʾ dropped (Q94:5→6). Q99:7-8 is the single antithetical reprise: the same weighing-of-deeds template with `khayran → sharran` (good ↔ evil).

## The differing-token taxonomy (the ≤6 roster, 33 pairs) — links the H-NEW-2380 mechanisms

Across the 33 roster pairs the edits fall into the same small structured set H-NEW-2380 found cross-surah, here operating **within a single surah**:

| mechanism | edit-count | exemplars |
|:--|:-:|:--|
| **parallel-template noun/verb swap** | 30 | Q81 cosmic-collapse cascade (`النجوم انكدرت`→`الجبال سيرت`→`العشار عطلت`→…); Q53:43-44 `أضحك وأبكى`→`أمات وأحيا`; Q99:7-8 `خيرا`→`شرا` |
| **rhyme-driven final-word swap (fāṣila re-tuning)** | 26 | Q91:2-3 `تلاها`→`جلاها`; Q91:5-6 `بناها`→`طحاها`; Q93:7-8 `فهدى`→`فأغنى`; Q37:165-166 `الصافون`→`المسبحون` |
| **connective/particle prepend or drop** | 5 | `ثم` prepends (Q75, Q102, Q74, Q82) |
| **connective/particle swap** | 4 | Q94:5-6 `فإن`→`إن` |
| **pronoun/inflection shift** | 4 | Q82:17-18 `وما`→`ما` |

The two dominant mechanisms — **parallel-template slot-swap** and **rhyme-driven fāṣila re-tuning** — ARE the within-surah face of the cross-surah iʿjāz al-fawāṣil that H-NEW-2380 documented: the proposition/template is conserved across the adjacent pair, and the change is either the swapped content slot of a parallel frame or the re-tuned cadence-word. This is the within-verse-pair correlate of the content⊥rhyme −0.86 anti-twin lock ([[h-new-730-content-rhyme-anticorrelation]]). The roster is **32/33 Meccan, 22/33 in juzʾ-ʿamma** (Q78–114) — the lone Medinan member is Q99:7-8 (al-Zalzala).

## H1 — ADJACENCY-EXCESS: **REVERSED → NULL (pre-commit violation, full prominence)**

**Locked direction:** the true canonical verse-order places near-identical verses ADJACENT more than chance → `N_low` (substantive adjacent pairs with char-edit ≤ 3) is GREATER than under a within-surah shuffle.

| null model | observed N_low | null mean | p (one-sided, locked "obs > null") |
|:--|:-:|:-:|:-:|
| **within-surah shuffle (PRIMARY)** | 6 | **17.27** | **1.0000** (replication seed: 1.0000) |
| global verse-shuffle (robustness) | 6 | 0.29 | 0.0001 |

**The primary direction is REVERSED and the reversal is total.** A random re-ordering of each surah's own verses produces ~17 low-edit adjacencies on average; the actual canonical order produces only 6. The Quran places near-identical verses adjacent **far LESS** than chance — it DISPERSES them. This is a pre-commit violation; per protocol it is published as NULL with full prominence and NOT massaged.

The two nulls disagree in sign **by design**, and the pre-reg anticipated exactly this: the global shuffle mixes the corpus's long Medinan verses with the short Meccan ones, so any low-edit adjacency becomes astronomically rare (null mean 0.29) and the observed 6 looks "excessive" — but that is a verse-LENGTH artefact, not a placement signal. The within-surah shuffle (locked PRIMARY) controls each surah's own length/genre profile and is the honest test; it governs the verdict.

### Why it reversed — the dispersion diagnostic (the deep result)

Decomposing the null mean per surah reveals the mechanism. It is dominated by surahs that **own large families of near-identical verses but place ZERO of them adjacent**:

| surah | verses | unordered verse-pairs within char-edit 3 | **adjacent** (canonical) | shuffle-mean adjacent |
|:--|:-:|:-:|:-:|:-:|
| **Q55 al-Raḥmān** | 78 | **465** | **0** | **12.09** |
| Q77 al-Mursalāt | 50 | 45 | 0 | 1.82 |
| Q26 al-Shuʿarāʾ | 227 | 99 | 0 | 0.84 |
| Q37 al-Ṣāffāt | 182 | 34 | 0 | 0.35 |
| Q54 al-Qamar | 55 | 9 | 0 | 0.33 |

**Q55 al-Raḥmān alone supplies 12 of the ~17.3 null mean.** Its 31 *fa-bi-ayyi ālāʾ rabbikumā tukadhdhibān* refrains (plus other near-identical verses) form 465 near-identical unordered verse-pairs — and NONE are adjacent in the canonical order. Shuffle the surah and ~12 of them collide into adjacency. This is the **ordering-by-dispersion principle** and it converges, hard, with two prior findings:

- **H-NEW-2310 (§10.93):** Q55's refrain is metronomically spaced (gaps ≈ 2), V_obs=0.116 vs null 3.18, p=0.0001 — refrains are *interleaved by design*.
- **H-NEW-2420 (§10.108):** Q55 is the standout naẓm-reversal (z = −5.32) — its refrains are so dispersed that the canonical order is *anti-adjacent*, and shuffling raises the adjacent shared-root similarity.

H-NEW-2450 now shows this is not a Q55 quirk but the corpus's general policy for near-identical verses: **the Quran spaces its look-alikes.** The adjacent reprise is the marked, rare exception (6 pairs) precisely because the default is dispersion.

## H2 — GENRE-CONCENTRATION: **PASS** (Bonferroni α = 0.025)

**Locked direction:** the adjacent-reprise device concentrates in the short-mufaṣṣal / eschatological juzʾ-ʿamma (mushaf id 78–114).

- Per-surah low-edit rate (char-edit ≤ 3 ÷ substantive pairs): **juzʾ-ʿamma 0.01617 vs rest 0.00078, Δ = +0.01539**, label-permutation **p = 0.0097 < 0.025 → PASS.**
- The juzʾ-ʿamma rate is **~21× the rest of the corpus.** The roster bears this out: 22/33 roster pairs are in Q78–114, 32/33 are Meccan, and the densest carriers (Q81, Q82, Q74, Q91, Q93, Q88) are short Meccan eschatological surahs whose **wa-idhā / oath-cascade parallel templates** generate the near-adjacent look-alikes.

So even though the corpus DISPERSES large refrain families (H1), the short Meccan eschatological surahs — built from tight parallel cadences over very few verses — are where adjacent reprises actually surface. The device is genre-bound to the juzʾ-ʿamma register that H-NEW-2210 (qasam), H-NEW-2240 (fāṣila homogeneity), H-NEW-2250 (idhā-cascade) and H-NEW-2410 (Meccan number-density) have all independently flagged.

## Integration

- **Confirms Q094-F-01 (§10.118)** at census scale: 0 exact adjacencies corpus-wide; Q94:5-6 is the unique char-edit-1 adjacent couplet; the edit-2 family is exactly {Q74:19-20, Q75:34-35, Q82:17-18, Q102:3-4}.
- **Completes the repetition scale-ladder.** The rungs now read: byte-exact refrain (2310) → exact cross-surah twin same-period (2350) → near cross-surah twin same-period (2380) → **adjacent near-verbatim reprise (2450, this finding)** → tightest adjacent couplet exemplar (Q094-F-01). The within-surah-adjacent rung was the one the earlier censuses explicitly did not cover.
- **Reinforces ordering-by-dispersion** as a corpus law: H-NEW-2310 (Q55 metronomic) + H-NEW-2420 (Q55 anti-adjacent z=−5.32) + H-NEW-2450 (within-surah shuffle produces 17 vs observed 6). When the Quran has near-identical verses, it SPACES them. The same finding that vindicates the dispersion law records its own H1 as a NULL — the discipline working.
- **Within-surah iʿjāz al-fawāṣil:** the two dominant roster mechanisms (parallel-template slot-swap + rhyme-driven fāṣila re-tuning) are the within-surah-adjacent face of the cross-surah edit-mechanisms in H-NEW-2380, both expressions of content⊥rhyme (r=−0.86).
- **Classical anchor:** al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 60 (*tikrār al-āyāt*) treats verse-repetition as deliberate; the dispersion result refines it — the *taqsīm/taqrīr* spacing al-Zarkashī (*al-Burhān*) describes is realised by SEPARATING reprises, with the immediately-adjacent reprise reserved as a marked intensifier (the Q94 *yusrayn*, the *thumma* re-assertions of Q75/Q102, the antithetical Q99 weighing).

## Honest limits

- **H1 is a pre-commit violation, reported as NULL with full prominence.** The locked "adjacent-excess" direction is wrong: the corpus is adjacent-DEPLETED for low-edit pairs (p=1.0). The interesting science is in the *reversal* (dispersion), not the locked claim.
- The within-surah vs global null sign-disagreement is a verse-LENGTH confound; the pre-reg locked the within-surah shuffle as primary precisely to neutralise it, so the verdict is unambiguous, but a reader who (wrongly) preferred the global null would see "excess." Disclosed prominently.
- The `≤6` roster band is descriptive; all inference used the a-priori `≤3` band (MW-7).
- The mechanism labels are a descriptive heuristic; the token alignments in the JSON are exact and machine-verified.
- H2's Δ is small in absolute terms (1.5pp) though significant; it rests on a thin tail (6 ≤3-edit pairs total), so it is a directional genre signal, robustly positive but power-limited.

## Files
- `prereg-h-new-2450-adjacent-reprise.md` (SHA-256 self-locked, embedded, runtime-verified)
- `scripts/h-new-2450.py`
- `csv/h-new-2450.json` (full census: histograms, 33-pair roster with edit alignments, edit-1/2/3 families, mechanism tally, H1/H2 statistics, per-surah dispersion diagnostic)
- `h-new-2450-adjacent-reprise.md` (this file)

*Bismillāhi al-Raḥmāni al-Raḥīm.*
