---
deliverable_id: cross-finding-prose-baselines
type: consolidated standing deliverable (not a new hypothesis test)
phase: cross-cutting
status: LIVE — updated each time a finding adds a new Quran-vs-prose contrast
author: computational-tester
created: 2026-04-14
seed: 20260413 (universal)
source_tasks: #85 (skeptical-auditor cross-finding proposal)
---

# Quran vs matched-Arabic-prose baselines — consolidated contrast table

## Purpose

Every Quran-specific claim in this project has to survive against at least
one matched-Arabic baseline; otherwise it is a claim about Arabic, not
about the Quran. This file consolidates the comparative Quran-vs-prose
contrasts scattered across Phase-B/C findings into a single auditable
table. Each row records: which scale (letter / word / verse / surah), which
statistic, which baseline(s), the numerical contrast, and the verdict.

The table is a **standing deliverable** — whenever a new finding completes
a Quran-vs-prose baseline contrast, its row is added here by the
integrator. Existing rows are not edited (except to record forthcoming
superseding results with a cross-ref).

## Baselines used across the project

| Baseline              | Source                                    | Typical N tokens  | Role                                   |
|-----------------------|-------------------------------------------|-------------------|----------------------------------------|
| **Bukhari-noquran**   | Ṣaḥīḥ al-Bukhārī matn, Quran-quotes stripped | ~77 k             | ḥadīth prose (formal, report-style)    |
| **Jāḥiẓ Ḥayawān**     | *Kitāb al-Ḥayawān* vol. 1                 | ~77 k / ~48 k segments | secular Abbasid prose (discursive)    |
| **Sīra Ibn Hishām**   | Sīrat al-Nabawiyya                        | ~19 k             | Islamic historical prose               |
| **Muʿallaqāt**        | 7 pre-Islamic monorhyme qaṣīda            | ~2.5 k hapax / ~770 units | rhymed classical Arabic poetry         |
| **Mutanabbī**         | Dīwān (later use in H-META-2 Markov comparator) | varies         | later Abbasid poetry (rhymed)          |

Bukhari and Jāḥiẓ together cover two distinct prose registers. Muʿallaqāt
is the rhymed-baseline control used to separate "rhyme-register effects"
from "Quran-specific effects." Sīra is used in pooled-prose controls
(H-NEW-29) and the TDA manifold baseline (H-TDA).

## Consolidated contrast table

Rows sorted by **scale** (letter → word → verse → surah → whole-corpus),
then by |z|.

| Finding / task | Scale    | Statistic                                  | Baseline(s)                | Observed contrast                                                     | Pre-reg verdict                          | Direction interpretation                                 |
|----------------|----------|--------------------------------------------|-----------------------------|-----------------------------------------------------------------------|------------------------------------------|----------------------------------------------------------|
| H-NEW-34 (#68) | letter (verse-final abjad mod m) | χ² z-score vs resample null           | Bukhari-noquran             | m=7 z = **−5.90**; m=11 z = **−11.36**; m=19 z = **−7.42**            | NULL-CONFIRMED (pre-reg) + REVERSE (exploratory) | Quran verse-final abjad residues MORE UNIFORM than Bukhari at all 3 moduli; reverse-direction to every ḥisāb-al-jummal clustering claim |
| H-NEW-34 (#68) | letter (verse-final abjad mod m) | χ² z-score vs resample null           | Jāḥiẓ Ḥayawān               | m=7 z = **−4.28**; m=11 z = **−6.75**; m=19 z = **−4.83**              | NULL-CONFIRMED + REVERSE (same as above)  | Same reverse under-dispersion; mechanism adjudication queued as [[h-new-34-1-under-dispersion|H-NEW-34.1]] Muʿallaqāt rhymed-baseline |
| [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] (#44) | letter (surah-boundary detection) | JS-divergence rolling-window F1 vs shuffle | (intra-Quran shuffle nulls; no prose baseline by design) | Real Quran hits = 41 / 113 (z = +4.39); within-surah shuffle = 53.24 (preserves 174.5 % of excess); length-matched iid = 25.10 (preserves 3.2 %) | CONFIRMED + novel side-finding | Letter ordering SUPPRESSES signal (-74.5 %); registered as H-NEW-24.1/.2/.3 candidate mechanisms |
| H-NEW-13 (#20) | letter (bigram transition-matrix spectrum) | spectral-gap vs matched-Arabic       | Bukhari-noquran             | (see phase-b letter-bigram file)                                      | NULL                                     | Letter-bigram spectrum NOT distinctively Quranic        |
| H-NEW-16 (#24) | word (cross-word phonetic palindromes) | count z vs bigram-Markov null        | (internal Markov null; prose baseline FLAGGED as open gap) | Observed 67 palindromes vs null-1 148 / null-2 129 → z = **−6.38 / −4.73** two-tailed | REVERSE-SIGNAL CONFIRMED | Quran actively SUPPRESSES phonetic palindromes at ~½ matched-Markov rate; needs Bukhari/Jāḥiẓ contrast to rule out general-Arabic artefact |
| counterfactual-fragility | word (root-substitution palindrome Δ) | two-sample z pooled                  | pooled Bukhari + Jāḥiẓ + Sīra | Quran vs pooled baseline **z = −4.86**                                | PASS (signal)                            | Quran is LESS fragile to root-substitution than pooled prose |
| H-NEW-29 (#54) | word (root inter-occurrence CV)    | Mann-Whitney U vs matched-length prose | Bukhari-noquran             | U = 1,476,700; **z = −9.636**                                        | (b) Comparative CONFIRMED (dual verdict) | Quran root-repetition MORE REGULAR (CV 1.287 vs 1.333) — al-Jāḥiẓ *takrār maqbūl* vindicated in comparative form |
| H-NEW-29 (#54) | word (root inter-occurrence CV)    | Mann-Whitney U                         | Jāḥiẓ Ḥayawān               | U = 1,844,751; **z = −7.948**                                         | (b) Comparative CONFIRMED                | Same direction; Jāḥiẓ is the name-giver of the doctrine |
| H-NEW-29 (#54) | word (root inter-occurrence CV)    | Mann-Whitney U                         | Bukhari ∪ Sīra pooled       | **z = −14.79**                                                        | (b) Comparative CONFIRMED                | Pooling tightens significance; consistent direction      |
| H-NEW-23 / T-004 (#72) | word (hapax-at-verse-final slot) | observed/expected enrichment + two-prop z-diff | Muʿallaqāt 7-ode pooled    | Quran per-hapax pooled z = **+10.61**; Muʿallaqāt pooled z = **+6.43**; two-proportion z-diff = **+6.67** (Quran > Muʿallaqāt, p = 2.55 × 10⁻¹¹) | DISCRIMINATIVE PASS                      | Slot-engineering effect IS present in pre-Islamic monorhyme poetry, but Quran's effect is ~4.23× stronger per hapax — Quran-specific residual above register baseline |
| H-NEW-25 (#45) | letter (consonant-trigram entropy) | entropy contrast vs al-Khalīl         | Bukhari-noquran, Jāḥiẓ, Muʿallaqāt | (in-flight; see task #45 status)                                 | IN-FLIGHT                                | placeholder                                              |
| H-NEW-35 (#69) | verse (length autocorrelation ρ(1)) | Fisher z-diff vs baselines            | Bukhari-noquran (ḥadīth-split) | Quran ρ(1) = 0.137, Bukhari ρ(1) = **−0.152** → Fisher z-diff = **+19.464** | PASS                                     | Quran rhythm sharply differs from Bukhari; Bukhari shows NEGATIVE ρ(1) — novel side-finding (isnad/matn alternation hypothesis) |
| H-NEW-35 (#69) | verse (length autocorrelation ρ(1)) | Fisher z-diff                          | Jāḥiẓ Ḥayawān (sentence-split) | Quran ρ(1) = 0.137, Jāḥiẓ ρ(1) = 0.146 → Fisher z-diff = **−0.666** | **FAIL** (indistinguishable)            | Quranic *īqāʿ* autocorrelation IS NOT distinctively Quranic — matches Jāḥiẓ prose; al-Sakkākī *īqāʿ* claim demoted to "description" not "distinguishing feature" |
| [[h-new-2-iltifat-catalog-rho|H-NEW-2]] × iltifāt (#55) | verse (pronoun-chain entropy × iltifāt density) | Spearman ρ(per-surah density, z) | (intra-Quran only)          | ρ(density, z_H) = +0.4266; ρ(density, z_MI) = −0.4061; ρ(density, z_shift) = +0.4490 | REVERSE-SIGN REFUTE (pre-reg sign wrong) | Surahs with more classically-flagged iltifāt have WEAKER [[h-new-2-iltifat-catalog-rho|H-NEW-2]] signature; main [[h-new-2-iltifat-catalog-rho|H-NEW-2]] finding unaffected |
| H-TDA (tda-manifold.md) | surah-ish (persistence diagram bottleneck) | within-baseline null → Quran distance percentile | Bukhari, Sīra, Jāḥiẓ, Muʿallaqāt | Median Quran-vs-baseline = 0.0390; within-baseline median = 0.0394; 99th pct = 0.0480 — Quran INSIDE baseline cloud | **NULL** (4/4 Quran-vs-baseline ≤ within-90%) | Quran's persistent-homology H1 signature is indistinguishable from matched-Arabic prose; TDA-bottleneck is NOT a Quran-specific signature |
| T1 LLM-judge (phase-c) | whole-corpus (semantic inauthenticity judgements) | rule-based classifier accuracy on proxy labels | (intra-Quran proxy; prose baseline pending) | Pilot: 100 % accuracy on 9/0 class-imbalanced subset → **PILOT_HONEST_NO_SIGNATURE** (p_perm = 1.00) | NULL (pilot); awaiting 120-claim corpus  | Pipeline integrity-checked; no signature detectable at pilot balance; awaiting classical-scholar labeled corpus |
| H-NEW-1 (#1, #39)   | letter (verse-ending Markov residual) | surprise z on (break vs conform) × residual | (intra-Quran only; H-META-2 adjudicates null choice) | Order-3 classical-rawī z = +5.53 all-verses / z = +8.78 Medinan | CONFIRMED pending retest | H-NEW-1 ledger note says "pending H-META-2 null adjudication" |
| H-META-2 (#43)       | (null-model on Mutanabbī + Jāḥiẓ) | NULL-A vs NULL-B Type-I + power        | Mutanabbī, Jāḥiẓ             | Null-A reject 0.693 (Mut) / 0.651 (Jāḥiẓ); Null-B reject 0.620 / 0.720 — both outside [0.005, 0.02]. Null-B flips SIGN on Jāḥiẓ planted-σ injection (+4.74, +4.83, +6.69 recovered for −0.5σ, −1σ, −2σ planted) | **BOTH_DISQUALIFIED** (pre-registered 4th branch) | Both Markov-surprise-family nulls fail calibration by 30–70× the nominal α rate; H-NEW-1 Markov-surprise-family retest BLOCKED pending H-NEW-META-3 third-null delivery (#118 in-flight) |

## Per-scale synthesis commentary

### Letter-level
Strongest Quran-vs-prose divergence appears at the **letter level**:
verse-final abjad residues are significantly MORE UNIFORM than Bukhari
and Jāḥiẓ at all three moduli (H-NEW-34 z = −4.28 to −11.36 across 6
tests). [[h-new-34-1-under-dispersion|H-NEW-34.1]] Muʿallaqāt rhymed-baseline (pre-registered 2026-04-14)
is the decisive adjudication of whether this is rhyme-mechanism or
Quran-specific novel finding. [[h-new-24-b1-b2-orthogonalization|H-NEW-24]] (letter-multiset surah-boundary
detection) is tokenization-free and found a **letter-order suppression**
(−74.5 % signal attributable to ordering alone) with no prose baseline by
design — cross-corpus generalization is the H-NEW-24.1/.2/.3 family.

### Word-level
Mixed direction:
- **Repetition-regularity** (H-NEW-29): Quran MORE regular than Bukhari
  (z = −9.64) and Jāḥiẓ (z = −7.95), with Sīra pooling pushing to
  z = −14.79. al-Jāḥiẓ's own *takrār maqbūl* doctrine is vindicated in
  the comparative form.
- **Phonetic-palindrome rate** (H-NEW-16): Quran has ROUGHLY HALF the
  palindromic-substring count of matched-Markov nulls (z = −6.38
  two-tailed). Prose baseline not yet run — this is the cleanest
  open gap for distinguishing Quran-specific suppression from Arabic-Semitic
  templatic-morphology artefact.
- **Hapax-slot engineering** (H-NEW-23/T-004): Quran ~4.23× stronger per
  hapax than the 7-Muʿallaqāt pool. The effect IS present in monorhyme
  poetry (not Quran-unique as claim), but the **residual above monorhyme
  register** is the Quran-specific part.
- **Counterfactual fragility**: Quran is LESS fragile to root-substitution
  than pooled Bukhari+Jāḥiẓ+Sīra (z = −4.86).

### Verse-level
Double-signal:
- **ρ(1) autocorrelation** (H-NEW-35): Quran's ρ(1) = 0.137 is sharply
  different from Bukhari's NEGATIVE ρ(1) = −0.152 (Fisher z-diff = +19.46)
  but statistically indistinguishable from Jāḥiẓ's ρ(1) = 0.146 (Fisher
  z-diff = −0.67). Bukhari is the outlier, not the Quran — a **caution
  flag** against treating any "Quran vs Bukhari only" z-score as
  Quran-distinctive without Jāḥiẓ cross-check.

### Surah-level / whole-corpus
H-TDA persistent-homology bottleneck: Quran is **inside** the cloud of
matched-Arabic baselines (median Quran-vs-baseline = 0.0390 < within-baseline
median 0.0394). TDA-H1 is NOT a Quran-distinctive signature.

### Open / in-flight prose baselines
- **H-NEW-25** (consonant-trigram entropy vs al-Khalīl *talāʾum al-ḥurūf*) — in-flight
- **H-NEW-37** (vowel-level Markov saj' test) — in-flight
- **H-META-2** — will decide NULL-A vs NULL-B for the Markov-surprise family
- **[[h-new-34-1-under-dispersion|H-NEW-34.1]]** Muʿallaqāt rhymed-baseline for verse-final abjad — pre-registered, dispatch pending

## Key methodological findings

### (1) Bukhari is often the outlier, not the Quran
In H-NEW-35 ρ(1), Bukhari's sign is negative, Quran and Jāḥiẓ are both
positive. Treating Quran-vs-Bukhari z as evidence of Quran-specificity
without a Jāḥiẓ cross-check mislocates the distinctiveness. The
Quran-vs-Bukhari z-diff of +19.46 is statistically about **Bukhari's
editorial-interleaving of ḥaddathanā isnād-matn units**, not about the
Quran. This is a general caution: any single-baseline contrast should be
checked against at least two prose registers before claiming
Quran-distinctiveness.

### (2) Jāḥiẓ is a stringent baseline; Bukhari is a weak baseline
Jāḥiẓ's discursive prose tracks Quranic rhythm much more closely than
ḥadīth report-style Bukhari. For a Quran-distinguishing claim to hold,
it needs to pass against Jāḥiẓ in particular. Findings where Quran vs
Bukhari is large but Quran vs Jāḥiẓ is small (H-NEW-35) are
"Bukhari-vs-Jāḥiẓ" findings, not "Quran-vs-Arabic" findings.

### (3) Direction-of-effect matters for reverse-signal routing
Several baseline contrasts reveal REVERSE signals (Quran MORE regular,
LESS diverse, LESS palindromic than baseline). These are genuine
quantitative findings but run opposite to much popular apologetic
tradition (which emphasizes Quran-uniqueness at the side of
"more ornate"/"more structured"). The reverse signals are:
- H-NEW-34: Quran MORE uniform abjad-residues
- H-NEW-29: Quran MORE regular root-repetition
- H-NEW-16: Quran LESS palindromic than Markov-matched
- counterfactual-fragility: Quran LESS fragile than prose

Each reverse signal has been filed honestly as a reverse-direction
finding, not as a spin-interpreted confirmation of original claim.
Anti-HARK discipline (4/4 PASS) on H-NEW-29, H-NEW-34, [[h-new-24-b1-b2-orthogonalization|H-NEW-24]]-B1/B2.

### (4) Rhymed baselines are the right control for verse-final effects
T-004 (Muʿallaqāt hapax-slot positive-control) and [[h-new-34-1-under-dispersion|H-NEW-34.1]] (pre-reg)
both use Muʿallaqāt because rhyme-register effects artificially inflate
"Quran specificity" against prose-only baselines. Any verse-final
observation should add a Muʿallaqāt contrast before claiming
Quran-distinctiveness.

## Cross-reference to H-NEW-SURVEY meta-hypothesis

The mirror-string suppression meta-pattern (H-NEW-SURVEY, task #74):
- Letter-level palindromes (H11 palindrome-full-sweep): suppressed
- Cross-word phonetic palindromes (H-NEW-16): suppressed (z = −6.38)
- Verse-final abjad residues (H-NEW-34): under-dispersed (suggestive)

If [[h-new-34-1-under-dispersion|H-NEW-34.1]] routes to [[h-new-34-1-under-dispersion|H-NEW-34.1]]-B (novel-finding), abjad-residue
flatness becomes a **third** scale in the cross-scale suppression
pattern (task #84 H-NEW-SURVEY-EXT registered).

## Update protocol

- Integrator appends a new row whenever a finding closes with a
  Quran-vs-prose contrast.
- Each row must include at least one z-score or effect-size estimate, the
  baseline name(s), and a verdict label.
- Rows never deleted; superseding results add "SUPERSEDED BY X at date"
  as a note column.
- Synthesis commentary §"Per-scale" updated when new scales or directions
  emerge.

## Status

- **Created** 2026-04-14 per task #85 (skeptical-auditor cross-finding
  proposal).
- **Meta-methodology appendix added** 2026-04-14 per team-lead quality item
  (§A–§D below).
- **Next update trigger**: completion of H-NEW-37 (#71, in-flight),
  H-NEW-25 (#45, in-flight), [[h-new-34-1-under-dispersion|H-NEW-34.1]] execution (#102, dispatched),
  H-NEW-META-3 pre-reg closure (#118, in-flight).
- **Broader-baseline coverage gaps** flagged in order of priority:
  1. H-NEW-16 phonetic-palindrome rate vs Bukhari/Jāḥiẓ (currently only
     intra-Markov null; would distinguish Quran-specific from
     Arabic-general suppression)
  2. H-TDA persistence → add Mutanabbī (later rhymed poetry) alongside
     Muʿallaqāt (pre-Islamic) for rhymed-period coverage
  3. Any newly-closed Markov-residual finding once H-NEW-META-3 delivers
     a third (non-disqualified) null spec

---

# Meta-methodology appendix (added 2026-04-14)

This appendix exists because team-lead flagged that the project has
accumulated enough prose-baseline contrasts to warrant standing
*meta-methodology* — not just a row-list of contrasts, but an explicit
decision framework for which baseline is appropriate for which claim-type,
and what we have empirically *learned* about baselines themselves.

The appendix is informed by two meta-findings:
- **H-META-1 confirmable-signature classifier** (MASTER §1 item #5,
  Tier-A): the project's finding-distribution has a detectable ex-ante
  signature — classical structural-formal claims confirm at 72%, numerical
  at 32%, scientific-foreknowledge at 0%. The baseline-appropriateness
  question has a *partially predictable* answer before the test is run.
- **H-META-2 null-model-comparator** (2026-04-13, BOTH_DISQUALIFIED):
  both of the two nulls used throughout the Markov-surprise family fail
  calibration on independent classical Arabic at 30–70× the nominal α
  rate. Markov-retrain nulls in particular recover **planted signal with
  the wrong sign** on Jāḥiẓ (Null-B: −σ planted, +4.74 to +6.69
  recovered across σ ∈ {0.5, 1.0, 2.0}) — a directional failure, not just
  a power failure.

## §A. Baseline-appropriateness decision matrix

Given a claim *C* and its observable scale, pick baseline(s) per the
following matrix. Each cell lists the *primary* baseline (bold) and the
*control* baseline (italic). Single-baseline claims are provisional until
a second baseline is added.

| Claim's observable scale | Claim asserts Quran ≠ classical Arabic on… | Primary baseline (must pass) | Control baseline (should pass) | Rationale |
|---|---|---|---|---|
| **letter** (abjad, bigram, multiset) | unprompted-orthography, n-gram distributions | **Bukhari** (register-wide prose) | *Jāḥiẓ* | Letter distributions are register-agnostic; both prose sources sample Arabic script at scale. |
| **letter at verse-final only** | rhyme-dependent letter statistics | **Muʿallaqāt** (rhymed positive-control) | *Bukhari + Jāḥiẓ* | Without a rhymed baseline the contrast cannot separate "Quran-specific" from "any rhymed classical Arabic." |
| **word** (root, lemma, hapax, collocation) | word-placement / slot engineering | **Muʿallaqāt** + **Bukhari** (both) | *Jāḥiẓ* | Word-slot effects need both a rhyme-register baseline (Muʿallaqāt) to rule out rhyme-artefact AND a prose baseline (Bukhari) to rule out register-wide templatic patterning. |
| **word** (repetition, CV, entropy) | repetition-regularity, *takrār maqbūl* claims | **Bukhari + Jāḥiẓ** pooled | *Sīra Ibn Hishām* | Pooled prose is the strong matched-Arabic baseline for claims about repetition control. Muʿallaqāt too small for within-surah repetition statistics. |
| **verse** (ρ(1) autocorrelation, length) | *īqāʿ* rhythm, length cadence | **Jāḥiẓ** (discursive prose, closer register) + **Bukhari** (contrast register) | *Muʿallaqāt* | Jāḥiẓ is the *tightest* prose baseline for rhythm; Bukhari is the *loose* baseline; disagreement between them is diagnostic (see §C below). |
| **verse-to-verse adjacency** (pointwise MI, echoes, phrase DAG) | Quran-specific inter-verse coherence | **Sīra + Bukhari + Jāḥiẓ** (all three) | *Muʿallaqāt* | Inter-unit coherence needs multiple prose baselines; poetry has structural adjacency by construction. |
| **surah-level** (persistence, clustering, ring) | surah-as-unit geometric signature | **Bukhari + Sīra + Jāḥiẓ + Muʿallaqāt** (all four — H-TDA protocol) | none remaining | Surah-level claims are coarse; exhausting matched corpora is the minimum evidential bar. H-TDA exemplifies this protocol. |
| **whole-corpus** (compression, semantic-manifold) | global structural signatures | **Bukhari + Sīra + Jāḥiẓ + Muʿallaqāt + Mutanabbī** (five-corpus) | none remaining | Only global contrasts can afford the full baseline suite; global claims require it. |
| **Markov-residual family** | verse-ending consonant surprisal | **BLOCKED** pending H-NEW-META-3 | — | Both previous nulls disqualified by H-META-2 on Mutanabbī + Jāḥiẓ. Do not add new Markov-residual rows until H-NEW-META-3 delivers a calibrated third null. |

**Pre-registration discipline.** The baseline for a claim must be
selected *before* the test is run. Retroactively promoting a weak
baseline to "distinguishing" after a strong baseline fails is the same
failure mode as HARKing on the null.

## §B. What H-META-1 tells us about which baselines CAN ever distinguish

H-META-1 (78.2% CV LR L1, feature collapse to 3 features dominated by
`school=modern` at w=−1.158) teaches that **the substance-type of the
claim predicts the verdict** at high accuracy before any text is seen:

- **structural-formal claims** (rhyme, inclusio, taṣdīr, munāsaba,
  pericope coherence, mutashābih pairing) → base rate 72% CONFIRMED.
  Any prose baseline that distinguishes these from matched Arabic is
  operating in the regime H-META-1 predicts will validate the claim.
- **numerical-gematric claims** (abjad-residue, clean factorization,
  word-count-divisibility) → base rate 32% CONFIRMED, and when they
  confirm they often confirm *reverse* (H-NEW-34 Quran MORE uniform, not
  less). Baselines for numerological claims must therefore be tuned for
  the REVERSE direction; a null that only detects "Quran more
  ornate/more structured" cannot catch them.
- **scientific-foreknowledge claims** → base rate 0% CONFIRMED (0/6).
  Baseline design is moot because no test at any scale has ever returned
  a confirmation; treat these as a PhD-thesis-weight skeptical prior,
  not as a baseline-design problem.

**Corollary.** Prose baselines do most of their epistemic work on the
**structural-formal** lane (where the base rate is already 72% — the
baseline's job is to carve the 72% into "Quran-specific 72%" vs
"register-wide-Arabic 72%"). On the **numerical-gematric** lane, the
baseline's job shifts: it's not "is this Quran-specific?" but "is this
*in the right direction* and *surviving a pigeonhole null*?" — a
different statistical framing (R-007 reverse-direction findings, §3c).

## §C. What H-META-2 tells us about single-baseline nulls

H-META-2 demonstrated empirically that the two Markov-surprise nulls
used throughout the project fail at 30–70× the nominal α rate on
independent corpora, and Null-B flips sign on synthetic planted
signal. Three lessons:

1. **Calibrate on independent data before adjudication.** Post-hoc
   adjudication between null specs on the same data is illegitimate
   (H-META-2 is a case study in why). MW-5 positive-control principle is
   the prospective version of the same rule: test your null on data
   where you know the answer.

2. **Markov-retrain nulls are dangerous for rhyme-register data.**
   Retraining a Markov model on permuted verse-endings destroys the
   model's prediction capacity for verse-endings, mechanically
   inflating residual magnitudes and (on short-rhyme-set Jāḥiẓ
   segments) flipping sign. The triggering incident was H-NEW-1
   audit-015; the generalization is: *a null whose construction
   destroys the very structure being measured is mathematically broken
   at the null-construction layer*, not at the data layer.

3. **Single-baseline contrasts are provisional.** Bukhari is frequently
   the outlier, not the Quran (H-NEW-35 ρ(1): Bukhari −0.152, Jāḥiẓ
   +0.146, Quran +0.137 — Quran tracks Jāḥiẓ, Bukhari is the weird
   one). Any "Quran vs Bukhari" z-score is therefore prima facie a
   "Bukhari vs Jāḥiẓ" finding until a second prose baseline confirms.
   See §D for the operationalization.

## §D. Bukhari-is-often-the-outlier diagnostic

A claim "Quran distinctive on statistic S" using only Bukhari as
baseline is provisionally acceptable only if the following diagnostic
passes:

- **(D-i)** Compute S on Bukhari, Jāḥiẓ, Muʿallaqāt (rhymed control
  where applicable), and Quran.
- **(D-ii)** Compute the spread of S across the three baselines.
  If the three baselines span a range that contains the Quranic value
  (i.e. Quran is INSIDE the baseline cloud, as in H-TDA), the claim
  fails Quran-distinctiveness regardless of Quran-vs-any-single-baseline
  z.
- **(D-iii)** If the three baselines cluster tightly and Quran lies
  outside the baseline cluster, the Quran-vs-any-single-baseline z is
  load-bearing.
- **(D-iv)** If Jāḥiẓ + Muʿallaqāt cluster tightly and Bukhari is
  the outlier among baselines, the correct framing is
  "Bukhari-distinctive relative to Quran/Jāḥiẓ/Muʿallaqāt" — the
  finding is about Bukhari's editorial-interleaving of isnād-matn
  segments, not about the Quran. This is the H-NEW-35 outcome.

**Empirical anchor.** H-NEW-35 is the canonical instance where this
diagnostic changed the framing: the Quran-vs-Bukhari Fisher z-diff of
+19.46 dissolves when Jāḥiẓ is added; it becomes a
Bukhari-is-an-outlier finding, not a Quran-distinctive finding. The
*īqāʿ* rhythm claim by al-Sakkākī is thereby demoted from "Quran
distinctive" to "classical Arabic prose has it, Quran inherits it."

## §E. Reverse-signal direction catalog

A distinguishing feature of this project's baseline work is that
*four* confirmed baseline contrasts return REVERSE direction (Quran
MORE regular / LESS diverse / LESS ornate than matched Arabic). The
reverse-signal catalog is epistemically important because it runs
opposite to most apologetic-tradition framings of Quran-uniqueness.

| Finding | Scale | Direction | Magnitude vs pooled prose | Status |
|---|---|---|---|---|
| H-NEW-34 | letter (verse-final abjad mod m) | Quran MORE uniform | z = −4.28 to −11.36 (6 tests, 2 baselines × 3 moduli) | PRIMARY NULL-CONFIRMED; reverse exploratory pending [[h-new-34-1-under-dispersion|H-NEW-34.1]] Muʿallaqāt |
| H-NEW-29 | word (root inter-occurrence CV) | Quran MORE regular | z = −9.64 (Bukhari) / −7.95 (Jāḥiẓ) / −14.79 (pooled) | Dual verdict (b) CONFIRMED |
| H-NEW-16 | word (cross-word phonetic palindromes) | Quran LESS palindromic | z = −6.38 two-tailed vs Markov null | Reverse-signal CONFIRMED; prose baseline still open |
| counterfactual-fragility | word (root-substitution Δ) | Quran LESS fragile | z = −4.86 vs pooled prose | PASS |

**Mirror-string suppression meta-pattern** (H-NEW-SURVEY, task #74)
unifies four reverse-direction findings under a single meta-hypothesis:
the Quran systematically *suppresses* surface-level repetition symmetries
(palindromes, clean factorizations, mod-m residue clustering, within-verse
echo density) — doing the *opposite* of what ḥisāb-al-jummal / numerology
predicts. The appendix's job is to ensure future contributors reading
this table **file new reverse-direction findings under H-NEW-SURVEY**
rather than spin-interpreting them as confirmations of the
"Quran-is-more-ornate" thesis.

## §F. Anti-HARK discipline enforced across the appendix

The appendix's rules close four HARKing escape hatches:

1. **No post-hoc baseline swaps.** The baseline matrix §A must be
   consulted before the test runs. A claim tested against Bukhari only,
   which then fails, cannot be "upgraded" to "Quran vs pooled" until
   that pooled version is pre-registered.
2. **No direction swaps.** A reverse-direction finding is a reverse
   finding, not an unexpected confirmation of the original direction.
   File under H-NEW-SURVEY meta-hypothesis.
3. **No single-baseline distinctiveness claims.** §D (D-i to D-iv) is
   the enforcement mechanism.
4. **No post-hoc null-spec adjudication.** H-META-2 established that
   adjudication must happen on INDEPENDENT data with pre-locked
   decision tables. H-NEW-META-3 (#118) is the next instance.

## §G. Relationship to MW-series methodology norms

- **MW-1** (length residualization at primary-test level) — operates on
  the primary test, orthogonal to baseline choice but complementary.
- **MW-2** (secondary-null residualization protocol) — triggered when an
  adversarial flag requires a secondary null; the appendix's §D
  diagnostic IS a standing MW-2-style secondary null for the
  Bukhari-as-outlier case.
- **MW-5** (positive-control for permutation nulls) — H-META-2 is the
  retrospective MW-5 catch for the Markov-surprise family.
- **MW-6** (nawʿ-verification tag) — orthogonal (citation discipline).
- **MW-7** (internal-error pre-publication gate) — the appendix's
  §F anti-HARK discipline is enforced at the MW-7 integrator-gate layer:
  no finding enters the ledger without passing §D and §F.

The appendix is thereby the baseline-choice analogue of the
MW-5/MW-6/MW-7 pipeline discipline.

---
