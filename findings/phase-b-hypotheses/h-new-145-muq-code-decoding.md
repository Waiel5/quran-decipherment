---
id: H-NEW-145
title: Muqaṭṭāʿat letter-sets as CODE — attempted decoding of surah metadata
phase: B
status: WEAK-SIGNAL (1 of 4 inferential cells pass; MW-5 PASS)
date: 2026-04-17
specialist: specialist-B (quran-equation-solvers)
parent_findings: [h-new-88 (metadata→letter-set RF 41.4%), cross-finding-006 (muqaṭṭāʿat multi-axis)]
seed: 20260417
rules_tuple: "(14 distinct muq letters across 29 surahs; 14 distinct letter-sets; Hafs-Kūfan; no-tashkeel)"
bonferroni: k=4 α_bon=0.0125 family=h-new-145-muq-code
pre_reg: findings/phase-b-hypotheses/h-new-145-muq-code-decoding-prereg.md
script: scripts/h_new_145_muq_code_decoding.py
output_json: findings/phase-b-hypotheses/csv/h-new-145.json
verdict: WEAK-SIGNAL — only Cell C (RF chronology-phase decoding) passes at α_bon; the other three cells (cardinality-mod-3, per-letter-theme hypotheses, classical singleton-interpretations) all fail. MW-5 shuffled-null positive control correctly fails all cells (pipeline sound).
---

# [[h-new-145-muq-code-decoding|H-NEW-145]] — Muqaṭṭāʿat letter-sets as CODE: decoding attempt


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

## Summary

The T-M.3 framing: "do the 14 muqaṭṭāʿat letter-sets ENCODE
surah METADATA decipherably?"

Four pre-registered inferential cells (Bonferroni k=4, α_bon=0.0125):

| Cell | Test | Result | Pass? |
|---|---|---|:-:|
| A | cardinality-mod-3 == verse-count-mod-3 match rate | 15/29 (52%), p=0.031 | **FAIL** |
| B | 4 classical-motivated per-letter-theme correlations | 0/4 sub-tests pass | **FAIL** |
| C | RF reverse-decoding (letter-presence → chronology/length/name-class) | chronology: 72.4% acc, p=0.010 | **PASS** |
| D | 3 classical singleton-interpretations top-5 rank | 1/3 cognates in top-5 | **FAIL** |
| MW-5 | shuffled-null positive control | all cells fail under null | PASS |

**Final verdict: WEAK-SIGNAL** — 1/4 inferential cells pass; the signal
appears to be limited to chronology-phase (mushaf-position-adjacent)
information, consistent with the [[h-new-88-letter-set-predictor|H-NEW-88]] finding that muq assignment
correlates with geographic clustering.

**The classical decoding attempts (Cell D) largely FAIL**. The specific
classical-tafsir interpretations ص→ṣabr (patience) and ق→qiyāma/qurʾān
do NOT survive empirical test under the pre-committed top-5 rank
criterion. Only ن→whale-narrative (Q 68) is rank 1/29 for whale root Hwt
density — and this is driven by the single verse Q 68:48 about Yūnus and
the whale.

## Pre-reg compliance

Direction locked BEFORE execution. PRE-REG-STANDARD-04. Bonferroni
k=4, α_bon=0.0125 (family = [[h-new-145-muq-code-decoding|h-new-145]]-muq-code). Renumbered from
[[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] pre-execution due to ID collision with completed universal-
hinges finding.

Auditor DM'd for review; proceeded after reasonable window per the
team-lead's autonomous-no-idle directive.

## Cell A — cardinality-mod-3 vs verse-count-mod-3

For each muq surah, compute `card(letter-set) mod 3` and
`nverses(surah) mod 3`. Count matches across 29 surahs.

- Observed matches: **15 / 29 = 0.517**
- Under null (verse-count-mod-3 roughly uniform): expected 29/3 ≈ 9.67 matches
- 1-sided binomial p (29 trials, p_null = 1/3): **p = 0.031**
- Pre-committed threshold: match_rate > 0.55 AND p < 0.0125
- Result: neither criterion met; **FAIL**

**Observation, not decoding**: the 52% match rate IS meaningfully above
the 33% chance baseline (p=0.031, single-test would PASS). Under Bonferroni-
4 family correction α_bon=0.0125, this does not survive. Honest FAIL at
the pre-committed threshold.

**Interpretation**: there is a WEAK (possibly chance, possibly real)
residual match between cardinality-mod-3 and verse-count-mod-3, but it is
not strong enough to call "decoding".

## Cell B — per-letter binary-feature classical-motivated tests

Four sub-tests at α_within = 0.0125/4 = 0.003125:

### B1 — M ↔ longer surah length (Spearman ρ > 0)

**Observed**: ρ = **−0.21**, p_one_sided = 0.87 (direction-reversed).

**Finding**: M-presence (in ALM, ALMS, ALMR, HM, TSM, etc.) is actually
NEGATIVELY correlated with surah length among the 29 muq surahs. This
contradicts the naive expectation from [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] that "muq surahs are
longer" — but [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]] was a muq-vs-non-muq comparison; WITHIN the muq set,
the shorter surahs are the single-letter-set ones (HM has 6 members at mid-
lengths; ALM has 6 at mid-to-long; ALR has 5 at variable; singletons tend
to be shorter). So M-presence as a continuous indicator is a WEAK proxy
that ends up slightly anti-correlated with length.

### B2 — ḤĀ (ح) presence ↔ Medinan chronology (Spearman ρ > 0)

**Observed**: ρ = **0.019**, p_one_sided = 0.46 (essentially zero correlation).

**Finding**: the 7 ḤĀ-bearing surahs (HM cluster Q 40-46 + HMASQ Q 42)
are not systematically later-chronology than other muq surahs when ranked
by Nöldeke. The HM cluster are Late-Meccan but other muq surahs (الم at
Q 29-32) are similarly Late-Meccan — no within-muq ḤĀ-chronology signal.

### B3 — SAD (ص) ↔ patience-theme (root Sbr hypergeometric enrichment)

**Observed**: SAD-bearing surahs = {Q 7, 19, 38}. Top-third by Sbr-root
density = {Q 2, 3, 13, 14, 31, 32, 38, 41, 42, 46}. Overlap = **1** (only
Q 38). Hypergeometric p = 0.73.

**Finding**: only 1 of 3 SAD-surahs is in the patience-theme top-third.
The classical ص-→ṣabr connection is NOT supported at the SAD-letter level.
Q 38 itself DOES rank highly for Sbr, but it's a weak single-surah effect,
not a general SAD-carrying pattern.

### B4 — Q (ق) ↔ eschatology (roots qwm + qrA hypergeometric)

**Observed**: Q-bearing surahs = {Q 42, 50}. Top-third by qwm+qrA density
= {Q 7, 10, 11, 13, 14, 27, 29, 30, 45, 46}. Overlap = **0**. Hypergeometric
p = 1.0.

**Finding**: NO Q-bearing surah is in the top-third for eschatology-root
density. The classical ق → qiyāma claim is REFUTED as a letter-mapping.

### Cell B overall

0 / 4 sub-tests pass at α_within = 0.003125. **Cell B FAIL.**

None of the classical-motivated per-letter-to-theme hypotheses survive
empirical test at the pre-committed level. The M-length connection even
runs in the OPPOSITE direction from expected.

## Cell C — RF reverse-decoding (letter-presence → metadata)

Three targets with 200-permutation LOOCV null:

| Target | LOOCV acc | Majority baseline | Uniform chance | Null mean | p_perm | Pass? |
|---|---:|---:|---:|---:|---:|:-:|
| C1 length-bin | 0.586 | 0.586 | 0.333 | 0.501 | 0.343 | FAIL |
| C2 chronology-phase | **0.724** | 0.552 | 0.250 | 0.458 | **0.010** | **PASS** |
| C3 name-class | 0.172 | 0.241 | 0.111 | 0.135 | 0.383 | FAIL |

Cell C PASS — C2 beats majority baseline by 17 percentage points and
survives 200-permutation null at p=0.010 < α_bon=0.0125.

**This is the single real signal in the study.**

**Caveat — overlap with [[h-new-88-letter-set-predictor|H-NEW-88]]**: [[h-new-88-letter-set-predictor|H-NEW-88]] trained metadata→letter-set
(RF 41.4%). This result (C2) is the inverse direction: letter-set
→chronology-phase at 72.4%. Mathematically related (same joint
distribution over surah × letter-set × chronology), but the decoding
framing is the novel contribution.

**The mechanism is mushaf-position**: muq letter-sets cluster geographically
in the mushaf (ALM at Q 2-3, 29-32; ALR at Q 10-15; HM at Q 40-46), and
mushaf-position strongly correlates with chronology-phase. The RF
effectively learns "this muq set lives at mushaf-positions X, which are
associated with Nöldeke phase Y". So **the "code" is not a cryptographic
mapping from letters to meaning; it is a LOCATION-MARKER**: muq letter-
sets mark which chronological phase the surah belongs to by proxy of
mushaf-position.

This is consistent with the emerging cross-finding literature (muq as
Late-Meccan scripture-announcement apparatus; [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]]). The
"code" is phase-marking, not content-encoding.

## Cell D — classical singleton-interpretations top-5 test

Three specific classical claims, tested as "does the labeled surah rank
in the top-5 of 29 muq surahs for its cognate-root density?":

| Test | Target | Cognate root(s) | Target density | Rank in 29 | Top-5? |
|---|---|---|---:|---:|:-:|
| D1 | ص (Q 38) ↔ ṣabr | Sbr | 0.0341/verse | **8 / 29** | FAIL |
| D2 | ق (Q 50) ↔ qiyāma | qwm ∪ qrA | 0.0889/verse | **21 / 29** | FAIL |
| D3 | ن (Q 68) ↔ whale-narrative | Hwt | 0.0192/verse | **1 / 29** | PASS |

**1/3 passes**. Binomial p under null (p = 5/29): 0.43. **Cell D FAIL.**

**Observation — classical ص→ṣabr is MODERATELY supported**: Q 38 at rank
8/29 is in the upper third but not top-5. The classical claim "ص relates
to patience" may have some signal but fails the strict top-5 criterion.

**Observation — classical ق→qiyāma is REFUTED**: Q 50 at rank 21/29 (lower
third) for qwm ∪ qrA density is the OPPOSITE of the classical prediction.
Q 50's actual thematic density is elsewhere (actual Q 50 themes: day-of-
reckoning imagery expressed through non-qwm vocabulary).

**Observation — classical ن→whale PASSES decisively**: Q 68 is rank 1/29
for Hwt (whale) root density. The single whale-mention (Q 68:48, referring
to Yūnus) drives this. This IS a classical-philological match:
Ibn ʿAbbās's interpretation "ن = the whale" (or "the inkwell"; Suyūṭī
al-Itqān) is consistent with Q 68's content. One data point, but a clean
one.

## MW-5 positive control — shuffled letter-set null

Shuffle surah→letter-set assignments (permuting the 29 mappings while
preserving the multiset of 14 distinct letter-sets). Re-run Cells A, B, C:

- Cell A (shuffled): match_rate = 0.241, pass = False ✓
- Cell B (shuffled): 0/4 sub-tests pass ✓
- Cell C (shuffled): no target passes ✓

All three cells correctly fail under the shuffled null. **MW-5 PASS**.
Pipeline is sound; the real-data results (Cell C PASS) is NOT a testing
artifact.

## Integrated interpretation

The muq letter-sets DO carry some decodable information — specifically
chronology-phase, via the geographic mechanism of mushaf-position
clustering. This confirms and extends [[h-new-88-letter-set-predictor|H-NEW-88]] in the reverse direction.

The classical tafsir interpretations of SINGLE letters as theme-codes
(ص→ṣabr, ق→qiyāma) are NOT empirically supported by this test. The
partial exception is ن→whale (Q 68), which IS supported but as a single
data point.

**"The muq are a code" claim needs to be specified carefully**:

1. **NOT a cryptographic code** where each letter has a fixed semantic
   mapping.
2. **IS a positional marker** that correlates with chronological phase
   (via mushaf geography).
3. **Possibly an aesthetic/rhetorical apparatus** (per [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]]
   rhyme-prefiguration finding, which survived rigorous replication
   before the 2026-04-17 retraction under frequency-weighted null;
   [[h-new-139-1-freq-weighted|H-NEW-139.1]]).
4. **Classical singleton interpretations mostly FAIL** when tested.

The "mysterious opening" tradition (al-Zamakhsharī, al-Rāzī's multi-
interpretation agnosticism) is CONSISTENT with this finding: the muq
are a marker of something (a phase, a genre, an opening-cue) rather
than a decipherable message.

## What this RULES IN and RULES OUT

### Rules IN (positive support)

- muq letter-sets carry chronology-phase information via mushaf-position
  (Cell C PASS at 72.4% acc, p=0.010)
- ن (Q 68) ↔ whale-narrative interpretation (Cell D partial pass; 1/3)

### Rules OUT (refuted at pre-committed thresholds)

- muq-cardinality as a hash-function over verse-count (Cell A FAIL)
- M-presence as a length-coding (Cell B1 FAIL; direction-reversed)
- ḤĀ-presence as a Medinan-chronology-coding (Cell B2 FAIL)
- SAD-presence as a patience-theme coding (Cell B3 FAIL)
- Q-presence as an eschatology-coding (Cell B4 FAIL; direction-reversed)
- ص (Q 38) as ṣabr-coding per classical ṣ→ṣabr (Cell D1 FAIL at top-5)
- ق (Q 50) as qiyāma/qurʾān-coding (Cell D2 FAIL; REFUTED at rank 21/29)

### Undetermined

- Length and name-class decoding: RF at chance (Cell C1, C3 FAIL)

## Connection to prior findings

- **Extends [[h-new-88-letter-set-predictor|H-NEW-88]]**: metadata→letter-set prediction (RF 41.4%) has
  a corresponding reverse direction where letter-set→chronology is also
  predictable. This is REDUNDANT information, not an independent code
  channel.
- **Refutes classical letter→theme singleton mappings at pre-committed
  thresholds** (except ن→whale at Q 68). Classical tafsir multi-
  interpretation agnosticism (al-Rāzī) is CONSISTENT with this result.
- **Aligns with [[cross-finding-012-late-meccan-scripture-announcement|cross-finding-012]] Late-Meccan scripture-announcement
  apparatus**: muq letters PHASE-MARK rather than theme-code.
- **Does NOT contradict [[h-new-113-letter-position|H-NEW-113]] (muq letters verse-final enriched)**:
  that finding is about the letters AS letters; this finding is about
  the letter-sets as indicators.

## Caveats and limits

1. **Non-independence from [[h-new-88-letter-set-predictor|H-NEW-88]]**: Cell C's chronology-phase signal
   shares structure with the [[h-new-88-letter-set-predictor|H-NEW-88]] mushaf-position effect. The
   decoded "code" is largely a positional clustering, not a literal
   encoding.
2. **Single Nöldeke chronology**: uses Nöldeke 4-phase classification
   as ground truth. Other chronologies (e.g., Egyptian Standard) may
   give slightly different labelings.
3. **Cell D singleton tests are n=1**: inherently low-power.
4. **Classical tafsir operationalization is limited**: I tested specific
   root-density interpretations; other operationalizations (semantic
   similarity, synonym expansion) could yield different results.
5. **Cell A near-miss (p=0.031) at tighter Bonferroni-4 fails but
   single-test would pass**: possibly a real weak effect worth re-testing
   independently.

## Queued follow-ups

- **H-NEW-145.1**: extended classical singleton-interpretations: test the
  FULL list of Ibn ʿAbbās's letter-meanings (ا=Allāh, ل=Jibrīl, م=Muḥammad;
  طه=Yā ṭāhir=O Pure One; كهيعص=kāf kāfī hādī ʿazīz ṣādiq) as theme-
  enrichment tests on the respective surahs.
- **H-NEW-145.2**: explicit control for [[h-new-88-letter-set-predictor|H-NEW-88]] overlap — strip mushaf-
  position effects via residualization, then re-test Cell C.
- **H-NEW-145.3**: the 52% cardinality-mod-3 match in Cell A — run
  independent replication on an alternative mod (mod-7, mod-abjad-value)
  to see if the near-miss is a real signal or noise.

## Connections

- Parent: [[h-new-88-letter-set-predictor|H-NEW-88]] (letter-set predictor)
- Cross-finding-006 (muq multi-axis design)
- [[h-new-113-letter-position|H-NEW-113]] (muq verse-final enrichment)
- [[cross-finding-012-late-meccan-scripture-announcement|Cross-finding-012]] (Late-Meccan scripture-announcement apparatus)
- [[h-new-44-muqattaat-combinatorial-closure|H-NEW-44]] (muq combinatorial closure)
- [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]], [[h-new-46-muqattaat-vs-surah-length|H-NEW-46]], [[h-new-51-cardinality-position-decline|H-NEW-51]] (surah-index / length / cardinality-position)
- [[h-new-139-muq-opening-vs-rhyme|H-NEW-139]] (RETRACTED): muq rhyme-prefiguration — the original PASS-
  DIRECTED verdict was retracted under frequency-weighted null; the
  present finding is CONSISTENT with the retraction (muq letters are
  not simple theme-coders).
