---
id: cross-finding-019
title: "Q 50 al-Qāf as composite-hub exemplar — the mushaf's mid-point multi-factor anomaly"
phase: B (synthesis; resolves R9 from cross-finding-018)
status: SYNTHESIS (resolves R9; descriptive composite-hub verdict with explicit post-hoc-feature-selection caveat)
date: 2026-04-17
author: synthesizer
parent_findings:
  - cross-finding-010 (Q 50 as upper-mid hub, degree 4 in cluster-network)
  - cross-finding-018 (4-principle reduced model; R9 Q 50 composite-hub)
  - H-NEW-146 (Q 50 Bonferroni-3 NULL; 3 near-misses at single-test α=0.05)
  - H-NEW-152 (Q 50 unique qrA v1↔v_last inclusio; descriptively-unique p=0.20 but 9× enriched)
  - H-NEW-153 (Q 50 body ق-frequency z=+4.20 — strongest single-surah ق signal)
  - H-NEW-154 (composite 5/5 score; COMPOSITE-CONFIRMED with post-hoc-feature-selection caveat; p_perm=0.0036)
classical_anchors:
  - al-Zarkashī al-Burhān fī ʿulūm al-Qurʾān (fawātiḥ + single-letter-muq discussion) — SECONDARY-TRIANGULATED
  - al-Suyūṭī al-Itqān (mufaṣṣal boundary at Q 49; al-Qāf as structural surah) — SECONDARY-TRIANGULATED
  - Classical short-name surahs (Q 36 Yā-Sīn "heart", Q 50 Qāf, Q 38 Ṣād, Q 68 Nūn) as ʿulūm-al-Qurʾān topic — SECONDARY-TRIANGULATED
bonferroni_family: n/a (synthesis; no new inferential test)
---

# [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]] — Q 50 al-Qāf as composite-hub exemplar


> ## ⛔ CORRECTION NOTICE — 2026-08-07
>
> **The arithmetic here is not retracted.** What fell is the inference drawn from the Fisher-Rao
> permutation null. Under the project's first genre control (`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md`),
> al-Bukhārī scores **z = −13.84** and pre-Islamic poetry **z = −15.13** against the Qurʾān's
> **z = −11.50** on an instrument-matched pipeline, and both baselines sit closer to their own TSP
> optima. Cutting this corpus's own verse stream into 114 blocks of the same size profile at offsets
> that ignore every surah seam gives z = −11.23 to −13.18. **Length-sorting alone reaches z = −8.66**
> (H-NEW-111's write-up mis-transcribed that anchor as 107.27; its own `csv/h-new-111.json` records
> 91.03 / 90.30). The mushaf's honest margin over pure length is **2.80 σ**, not 11.46 σ.
> The *relative* claim survives — mushaf 85.76 < Nöldeke 87.23 < Tanzil 89.53.
> Summary: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.


## Executive summary

Q 50 al-Qāf appears as an anomaly in **4+ independent findings**
across the 2026-04-17 session:

1. [[cross-finding-010-extended-network|cross-finding-010]]: degree 4 in the cluster-network (tied with
   Q 62, 112, 113, 114 at the 4-way top-hub tie post-dedup)
2. [[h-new-146-q50-qaf-hub|H-NEW-146]]: 3 Bonferroni-3 near-misses (position / content /
   structural) — no single axis explains its hub-ness
3. [[h-new-152-book-ref-inclusio|H-NEW-152]]: UNIQUE qrA (qurʾān) root occurrence in BOTH v1 and
   v_last — 1 of 114 (vs 0.11 expected; 9× enrichment; p=0.20
   fails Bonferroni-2 but descriptively striking)
4. [[h-new-153-muq-body-enrichment|H-NEW-153]]: body ق-frequency z=+4.20 — strongest single-surah
   ق signal (1.74× corpus baseline; "ق→Qāf is filled with ق"
   classical intuition vindicated)
5. [[h-new-154-q50-composite|H-NEW-154]]: UNIQUE 5/5 score on a 5-feature composite
   (position + book-reflexive + muqaṭṭāʿat + oath-opener +
   mufaṣṣal-boundary); p_perm=0.0036 with explicit post-hoc-
   feature-selection caveat

**Synthesis verdict**: Q 50 is a **genuine composite-hub
exemplar**, not a single-dominant-mechanism hub. No individual
axis explains its hub status at Bonferroni-significance; the
JOINT co-occurrence of multiple classical-balāgha features is
the mushaf's unique-at-Q-50 structural intersection.

This resolves R9 of [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] in the direction
"multi-factor weak composite is real but not reducible to a
single mechanism." Q 50 is a structural exemplar, not a
theoretical anchor; it does NOT warrant a separate principle
addition to the 4-principle model.

## What Q 50 is (descriptive anchors)

### Basic facts

- **Mushaf position 50** (mid-mushaf; 50 of 114)
- **Nöldeke rank 77** (pure Late-Meccan core; rank 72-85 = B6 sub-bin per [[cross-finding-017-b6-b7-staircase|cross-finding-017]])
- **Length 45 verses** (short-medium; not a length extreme)
- **Single-letter muqaṭṭāʿat ق** (cardinality 1; cluster: one of 8 singletons)
- **Opens with an oath**: "ق وَٱلْقُرْآنِ ٱلْمَجِيدِ" (ق + "By the
  glorious Qurʾān")
- **Closes with a Qurʾān-reference**: "فَذَكِّرْ بِٱلْقُرْآنِ"
  (remind by the Qurʾān)
- **Classical-balāgha status**: al-Zarkashī al-Burhān discusses
  Q 50 as a structural mufaṣṣal-boundary surah; multiple
  classical tafsir note its Qurʾān-reflexive framing

### Classical anchor: al-Zarkashī al-Burhān [SECONDARY-TRIANGULATED]

al-Zarkashī (d. 794H / 1392 CE), in al-Burhān fī ʿulūm al-Qurʾān
nawʿ on fawātiḥ al-suwar, discusses the single-letter muqaṭṭāʿat
openings (ص, ق, ن) as a distinct sub-class within the broader
muqaṭṭāʿat taxonomy. al-Zarkashī's view: the single-letter muq
are structurally distinct from the multi-letter clusters (الم,
الر, حم), and Q 50's opening ق is linked to the Qurʾān-
reflexive content of the surah (the classical reading of ق as
abbreviation / pointer to qurʾān).

Modern classical balāgha further notes Q 50 as a **mufaṣṣal-
boundary surah** (classical mufaṣṣal division begins at Q 49 or
Q 50 depending on reading; al-Suyūṭī al-Itqān discusses both).

**Status**: SECONDARY-TRIANGULATED (cited in McAuliffe EQ entry
on "fawātiḥ" and in multiple modern ʿulūm al-Qurʾān surveys).
No verbatim quotation downstream until VERIFIED per MW-6.

## The 4+ findings, integrated

### Finding 1: cluster-network degree 4

Per [[cross-finding-010-extended-network|cross-finding-010]] (post-dedup reading): Q 50 belongs to 4
of the 20 pre-committed cluster-systems, placing it among the
top-hub tie with Q 62, Q 112, Q 113, Q 114. Q 50's memberships
(post-dedup):
- C1 muqaṭṭāʿat (by membership; singleton ق)
- C12 oath-opener surahs (21-member class; Q 50 is one of the
  21 per [[h-new-85-oath-openers|H-NEW-85]] OATH_PARTICLE)
- C17 muqaṭṭāʿat singletons (7-member class; Q 50 is one of 7)
- C19 book-reference muqaṭṭāʿat subset ([[h-new-53-muqattaat-book-reference|H-NEW-53]]; Q 50 among
  the 24/29 with v1-3 book-ref)

Q 50's hub status is **structurally positioned** at the
intersection of these four cluster-systems. This is the
descriptive hub.

### Finding 2: [[h-new-146-q50-qaf-hub|H-NEW-146]] three near-misses

Pre-registered test of 3 mechanisms at Bonferroni-3 α_bon=0.0167:

| Cell | Hypothesis | p | Result |
|:-:|:---|---:|:-:|
| A | Q 50 rank 1 in Q 40-60 for cluster-degree | 0.095 | near-miss |
| B | Q 50 rank 10 of 114 for qrA density | 0.088 | near-miss |
| C | Q 50 FR-distance to other single-letter-muq 14% shorter | 0.031 | near-miss |

**All 3 direction-correct but underpowered at the pre-committed
Bonferroni**. MW-5 pipeline valid (Q 44 non-hub fails all 3 at
all thresholds). The single-mechanism hypothesis is FALSE
(Bonferroni-3 NULL); multi-mechanism hypothesis is
directionally consistent.

### Finding 3: [[h-new-152-book-ref-inclusio|H-NEW-152]] unique qrA v1↔v_last inclusio

Q 50 is the ONLY surah in the Quran with root qrA (qurʾān /
recite) in BOTH v1 and v_last:
- v1: "ق وَٱلْقُرْآنِ ٱلْمَجِيدِ" (qurʾān)
- v45: "فَذَكِّرْ بِٱلْقُرْآنِ" (qurʾān)

Observed: 1/114. Expected under independence: 0.11. 9×
enrichment on the ratio. p=0.20 fails Bonferroni-2 because the
single-observation statistic doesn't clear formal significance,
but the descriptive uniqueness is striking — the surah begins
and ends with Qurʾān-self-reference.

Under the classical reading (al-Zarkashī): Q 50's single-letter
ق opening is an abbreviation for qurʾān; the v1↔v_last
inclusio is the typographic-structural completion of that
self-reference.

### Finding 4: [[h-new-153-muq-body-enrichment|H-NEW-153]] body ق-frequency z=+4.20

ق root-frequency within Q 50's body is 1.74× corpus baseline,
z=+4.20 — the strongest single-surah ق signal in the 114.
Classical "ق→Qāf is filled with ق" intuition VINDICATED at
p<0.001.

Note heterogeneity: Q 42 (also ق-containing at the 5-letter
composite حمعسق) is DEPLETED in ق (body ratio 0.76, z=-2.14).
The classical claim applies UNIFORMLY to Q 50 only; it does
NOT hold for Q 42.

**Implication**: Q 50's body-ق enrichment is a SURAH-SPECIFIC
structural feature, not a generalized muqaṭṭāʿat-letter-
enrichment pattern. It is PARTICULAR to Q 50.

### Finding 5: [[h-new-154-q50-composite|H-NEW-154]] composite 5/5 score

Q 50 is the UNIQUE surah scoring 5/5 on a 5-feature composite:

| Feature | Description | Q 50 satisfies? |
|:-:|:---|:-:|
| F1 | Position centrality (Q 40-60) | ✓ (position 50) |
| F2 | Book-reflexive opening (qrA/ktb in v1-3) | ✓ (qurʾān v1) |
| F3 | Muqaṭṭāʿat-opened | ✓ (ق) |
| F4 | Oath-opener | ✓ (ق وَٱلْقُرْآنِ) |
| F5 | Mufaṣṣal-start position (Q 49-60) | ✓ (classical boundary) |

Score 5/5. Under shuffled-feature null: p_perm = 0.0036.

**Post-hoc-feature-selection caveat (per [[h-new-154-q50-composite|H-NEW-154]] pre-reg
disclosure)**: the 5 features were chosen knowing Q 50's
properties. Honest reading: the composite shows Q 50 is the
unique COINCIDENCE of 5 classical-balāgha features, not that
Q 50 was DESIGNED to satisfy all 5. The shuffled-feature null
is mathematically valid; the causal interpretation is limited
to "Q 50 is where 5 classical clusters happen to intersect,"
not "Q 50 was engineered to satisfy the 5."

**Inflated-independence on the composite**: F1 (Q 40-60) and F5
(Q 49-60) overlap substantially; F2 catches 24+ surahs (high
base-rate). Effective-independent-features ~3-4 of 5, not 5.

### Near-analogs (score 4/5)

Q 43, Q 44 (both ḥā-mīm): miss F5 (mufaṣṣal-start).
Q 52 al-Ṭūr: misses F3 (not muqaṭṭāʿat-opened).

**Q 52 is the closest non-muq analog of Q 50**: oath-opener
(وَٱلطُّور), mid-mushaf (position 52), mufaṣṣal-start (Q 52 is
inside al-mufaṣṣal), book-ref (ktb reference in opening verses).
It satisfies F1+F2+F4+F5 but fails F3 (no muqaṭṭāʿat).

Q 52 is also ONE OF THE ±58 MIRROR PAIR NEIGHBORS: Q 49→50 =
-58 chrono-reversal; Q 56→57 = +58 chrono-reversal. Q 50 sits
between them as the mid-mushaf pivot.

## The composite-hub mechanism (synthesis)

### What we CAN say

Q 50 is empirically the UNIQUE surah satisfying the 5-way
intersection: ق-singleton muqaṭṭāʿat AND oath-opener AND
Qurʾān-reflexive opening AND mid-mushaf AND mufaṣṣal-boundary.
No other surah combines all five. This is a DESCRIPTIVE
structural fact.

Q 50's hub status at cluster-network degree 4 is a CONSEQUENCE
of this intersection — it belongs to 4 pre-committed cluster-
systems BECAUSE it has features F1-F5.

Q 50's body-ق enrichment (z=+4.20) is a SURAH-SPECIFIC
structural amplification of the muqaṭṭāʿat marker: not only
does Q 50 open with ق, its body has 1.74× the corpus ق
frequency. This is a local typographic-structural phenomenon.

The v1↔v_last qrA inclusio (1-of-114 unique) is a
typographically-realized Qurʾān-reflexive frame.

### What we CANNOT say

1. **Causal design**: we cannot establish that Q 50 was
   COMPOSED with the 5-way intersection in mind. The features
   may be co-occurring for independent reasons.
2. **Single dominant mechanism**: [[h-new-146-q50-qaf-hub|H-NEW-146]]'s Bonferroni-3 NULL
   rules out any single-axis explanation. Q 50's hub-ness is
   multi-factorial.
3. **Generalization to other hubs**: Q 50's 5/5 score is unique
   in the corpus. No other surah achieves this intersection.
   The composite mechanism does NOT predict which OTHER surahs
   should be hubs (only 4-way-tie hubs Q 62, 112, 113, 114 have
   been separately analyzed).

## Q 50 in the 4-principle model (from [[cross-finding-018-four-principle-reduced-model|cross-finding-018]])

- **M1 (structured Hamiltonian cycle + length-extremity hubs)**:
  Q 50 is a mid-ring structural hinge ([[h-new-130-fisher-rao-residuals|H-NEW-130]] top-15 list
  position 17 / adjacent-to-top-15). NOT a length extreme (45
  verses is medium). The length-extremity absorption of former
  M4 does NOT place Q 50 as a front/back hub; Q 50's hub status
  is STRUCTURAL (mufaṣṣal-boundary) not length-extremity.
  **Q 50 is an exception to the length-extremity-hubs claim**:
  it's a mid-mushaf hub that is NOT length-extreme. This is a
  residual feature of M1.
- **M2 (Late-Meccan scripture-announcement, muqaṭṭāʿat-marked)**:
  Q 50 is pure Late-Meccan (B6 sub-bin per [[cross-finding-017-b6-b7-staircase|cross-finding-017]]);
  muqaṭṭāʿat-opened (ق); Qurʾān-reflexive v1↔v_last. Q 50 is a
  FULL exemplar of M2 at B6 — the purest pure-Late-Meccan
  scripture-announcement surah.
- **M3 (prosodic distinctiveness)**: Q 50's verse-length
  distribution is typical of pure-Late-Meccan surahs; not a
  distinctiveness outlier.
- **M5 (length-stratification + vocabulary concentration)**:
  Q 50 at the classical mufaṣṣal boundary (Q 49 or Q 50
  depending on reading); its ق body-enrichment is a
  vocabulary-concentration signature (specific-root-signature
  per M5).

**Integration**: Q 50 is an exemplar of M2 (fullest pure-LM
scripture-announcement surah) AND a structural-hinge per M1
(mid-ring position, mufaṣṣal-boundary) AND a vocabulary-
concentration signature per M5 (ق body-enrichment). Three of
the four principles converge at Q 50. **This is why Q 50 is a
composite hub**: multiple principles' emphasis points happen
to coincide at mushaf position 50.

## Q 50 as exception to M1's length-extremity framing

The former M4 absorption into M1 ([[cross-finding-018-four-principle-reduced-model|cross-finding-018]]) re-framed
the 4-region hub architecture as "length-extremity hubs."
Front hubs (Q 2, 3) are length-long; back-terminal hubs (Q 112-
114) are length-short; mid hub (Q 50) is NOT length-extreme.

**Q 50 is the one hub that does NOT fit the length-extremity
framing**. The other 3 hub regions (front, back-upper, back-
terminal) are all length-extremes; Q 50 at mushaf position 50
with 45 verses is mid-length.

**Honest framing**: M1's length-extremity-hubs sub-claim is
ACCURATE for 3 of 4 hub regions. Q 50 is a genuine exception
— a mid-mushaf mid-length hub whose hub-ness comes from the
mufaṣṣal-boundary + single-letter-muq + oath-opener + Qurʾān-
reflexive intersection, NOT from length extremity.

This is a **refinement** of [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] M1's sub-claim 4:
length-extremity hubs apply to the 3 peripheral regions
(front/back-upper/back-terminal); the mid-region hub (Q 50) is
a COMPOSITE-STRUCTURAL hub with its own mechanism.

## Honest limits

1. **Post-hoc-feature-selection caveat** on [[h-new-154-q50-composite|H-NEW-154]] preserved:
   the 5/5 composite score is mathematically valid under the
   shuffled null (p=0.0036) but the features were chosen
   knowing Q 50. Causal interpretation limited.
2. **Effective-independent-axes on the composite**: F1 ⊂ F5
   (overlapping position windows); F2 high-base-rate; effective
   ~3-4 of 5 features.
3. **Single-observation statistics**: [[h-new-152-book-ref-inclusio|H-NEW-152]]'s qrA v1↔v_last
   uniqueness (1 of 114) fails Bonferroni-2 because single-
   observation significance is hard to establish. Descriptively
   striking but formally underpowered.
4. **No predictive model**: the synthesis does NOT predict
   which OTHER surahs should be composite-hubs. Q 50 is a unique
   empirical exemplar; the mechanism does not generalize in a
   tested way.
5. **Classical anchor SECONDARY-TRIANGULATED only**: al-Zarkashī
   al-Burhān's discussion of single-letter muq + mufaṣṣal-
   boundary is cited via secondary sources; no verbatim from
   PENDING.
6. **Q 42 heterogeneity**: the other ق-containing surah (Q 42
   al-Shūrā, with 5-letter حمعسق) is DEPLETED in ق (z=-2.14).
   The classical "ق→Qāf" claim holds for Q 50 only; it does
   NOT hold for Q 42. This is a honestly-disclosed caveat on
   the body-ق enrichment pattern.

## Integration with [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] R9 resolution

R9 in [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] was: "Q 50 Qāf as composite-hub
exemplar — this is NEW this session; [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]] deep-
dive forthcoming."

This [[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]] **RESOLVES R9** in the following sense:

- Q 50's hub status is a COMPOSITE-STRUCTURAL intersection of
  5 classical-balāgha features, none individually at Bonferroni-
  significance, JOINTLY unique at Bonferroni-1 (with post-hoc-
  feature-selection caveat).
- Q 50 is an EXEMPLAR, not a NEW PRINCIPLE. It does NOT
  require adding a 5th principle to [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]'s 4-
  principle model.
- Q 50 refines M1's length-extremity-hubs sub-claim (3-of-4
  hub regions are length-extreme; Q 50 is the mid-region
  exception).
- Q 50 fully exemplifies M2 at the B6 sub-bin level.
- Q 50's body-ق enrichment (z=+4.20) is a vocabulary-
  concentration signature per M5.

**The R9 residual is now ANNOTATED as exemplar-not-principle**.
Q 50 remains a distinctive feature of the mushaf architecture;
this synthesis documents WHY without elevating it to a generative
mechanism.

## Integration with ±58 mirror pair (R10 of [[cross-finding-018-four-principle-reduced-model|cross-finding-018]])

Q 50 sits BETWEEN the ±58 mirror pair:
- Q 49→50 boundary: Δ Nöldeke = −58 (rank 5 by signed
  chronology-reversal)
- Q 56→57 boundary: Δ Nöldeke = +58 (rank 6; also rank-1 root-
  bridge at cos=0.408 with shared roots sbH+smw)

Q 50 is at mushaf position 50; Q 57 is at position 57. The
mirror pair brackets positions 49-57 (a 9-surah window) with
Q 50 at the entry point. This is a descriptive architectural
observation; no causal claim.

## Classical tradition alignment

Q 50's structural distinctiveness is recognized in classical
ʿulūm al-Qurʾān:
- al-Zarkashī al-Burhān notes single-letter muq (ق) as
  structurally distinct
- Classical tafsir link ق to qurʾān (though al-Rāzī's abbreviation-
  theory is REFUTED per [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]])
- al-Suyūṭī al-Itqān discusses Q 50 as mufaṣṣal-boundary
- The v1↔v_last Qurʾān-inclusio is noted in classical i'jāz
  literature (see McAuliffe EQ on "inclusio in the Qurʾān")

These classical observations are CONSISTENT with the empirical
structural facts. Per [[cross-finding-015-classical-scholarship-validation-pattern|cross-finding-015]]'s balāgha-survives
pattern: the qualitative observations about Q 50 as a
structurally-distinct mid-mushaf surah receive quantitative
confirmation at the composite-score level.

**No theological claim**. The empirical-structural alignment
with classical framings does not establish iʿjāz or design
intent; it establishes that classical observers correctly
identified a structurally-unique surah at position 50.

## Verdict

**SYNTHESIS (descriptive composite-hub verdict)**. Q 50 al-
Qāf is empirically the UNIQUE surah at the 5-way intersection
of (position 40-60) + (book-reflexive opening) + (muqaṭṭāʿat-
opened) + (oath-opener) + (mufaṣṣal-start). This composite-
uniqueness is mathematically valid at p=0.0036 under shuffled-
feature null; causally limited by the post-hoc-feature-
selection caveat. Q 50 is an EXEMPLAR-NOT-PRINCIPLE in the 4-
principle model; it refines M1's length-extremity-hubs sub-
claim (Q 50 is the mid-mushaf exception), fully exemplifies M2
at B6, and exhibits vocabulary-concentration per M5.

R9 of [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] is RESOLVED in the direction "composite-
hub exemplar, not principle addition." The mushaf's mid-point
structural hub is a genuine multi-factor anomaly consistent
with 14 centuries of classical Quranic scholarship's
identification of Q 50 as distinctive.

## Files

- [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] (parent model): `findings/phase-b-hypotheses/cross-finding-018-four-principle-reduced-model.md`
- [[h-new-146-q50-qaf-hub|H-NEW-146]] (three near-misses): `findings/phase-b-hypotheses/h-new-146-q50-qaf-hub.md`
- [[h-new-152-book-ref-inclusio|H-NEW-152]] (qrA inclusio): `findings/phase-b-hypotheses/h-new-152-book-ref-inclusio.md`
- [[h-new-153-muq-body-enrichment|H-NEW-153]] (body ق enrichment): `findings/phase-b-hypotheses/h-new-153-muq-body-enrichment.md`
- [[h-new-154-q50-composite|H-NEW-154]] (composite 5/5): `findings/phase-b-hypotheses/h-new-154-q50-composite.md`
- [[cross-finding-010-extended-network|cross-finding-010]] (cluster-network): `findings/phase-b-hypotheses/cross-finding-010-extended-network.md`

## Final statement

Q 50 al-Qāf is the mushaf's mid-point composite-hub exemplar:
a structurally-unique surah at the intersection of 5 classical-
balāgha features (mid-mushaf position, Qurʾān-reflexive
opening, single-letter muqaṭṭāʿat, oath-opener, mufaṣṣal-
boundary), with body-specific ق-frequency enrichment (z=+4.20),
unique qrA v1↔v_last inclusio (1-of-114), and cluster-network
hub-degree 4. No single mechanism explains its hub status;
the JOINT co-occurrence is its distinctiveness. Q 50 does not
warrant a 5th principle in [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]'s 4-principle
model; it is an EXEMPLAR within M1 + M2 + M5's combined
architecture. R9 of [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] is RESOLVED as composite-
exemplar not principle-addition.
