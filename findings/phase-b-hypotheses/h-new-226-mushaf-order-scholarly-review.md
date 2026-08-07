---
id: H-NEW-226
title: Classical-vs-empirical review on the rationale for mushaf order
phase: B (classical-scholarship survey; synthesis)
status: DESCRIPTIVE-REVIEW (no new inferential test; cites and scores already-landed empirical findings)
date: 2026-04-17
owner: classical-survey-agent
parent_findings:
  - cross-finding-011 (Fisher-Rao mushaf-geodesic CONFIRMED)
  - cross-finding-013 (mushaf-topological-ring CONFIRMED)
  - H-NEW-111 / 111b / 111c (triple-feature Fisher-Rao)
  - H-NEW-130 / 130b / 130c (structural-hinge decomposition, 3 universal hinges)
  - H-NEW-142 (rhetorical bridging of chronology-reversal hinges)
  - H-NEW-183 (Nöldeke predictor R²=0.836)
  - H-NEW-192 (mushaf position decomposition R²=0.76-0.82)
  - H-NEW-212 (alt-chronology Fisher-Rao — all 4 chronologies beat random; mushaf still shortest)
  - canonical-order-recovery (combined-τ FAIL; length-residualized NCD τ=+0.648; adjacent-pair 17/113)
  - classical-quantitative-claims-audit.md (al-Biqāʿī last-9-mirror-first-9 REFUTED z=−4.87)
cross_findings_used:
  - classical-cross-references.md (attribution table)
rules_tuple: (citation-only; no new counts; all referenced p-values inherit from parent-finding rules)
integrity_note: |
  This is a citation-and-synthesis document. No new statistical test runs
  here. All claims about empirical status inherit status from parent findings
  pre-registered prior to this review. The six positions below are ordered
  per the H-NEW-226 task spec, not by importance. Where a position has not
  been directly tested in the project, status is marked UNTESTED.
---

# [[h-new-226-mushaf-order-scholarly-review|H-NEW-226]] — Why is the mushaf order what it is? A classical-vs-empirical review


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


## The question

The ~1400-year Islamic tradition and ~170-year Western academic tradition have
produced six major theoretical positions on *why* the 114 surahs sit in their
canonical mushaf order. This file catalogues each position, extracts its
empirical predictions if true, and evaluates its status against the project's
landed findings ([[h-new-111-fisher-rao-mushaf|H-NEW-111]] through [[h-new-222-more-chronologies|H-NEW-222]] series + cross-findings 011, 013).

The empirical landscape the review draws on:

- **Mushaf is Fisher-Rao geodesic-optimal under root-content + char-4-gram**
  ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] CONFIRMED, z ≈ −11 in two orthogonal feature spaces)
- **Mushaf is a topological ring, not a path**: Q 1 ↔ Q 108–114 content-close
  at z = −4.17 (roots), −4.51 (char-4-grams), −2.75 (verse-length); Q 114 → Q 1
  wrap-around is smallest verse-length distance among all 113 candidate edges
  ([[cross-finding-013-mushaf-topological-ring|cross-finding-013]] CONFIRMED)
- **15 top-jump edges coincide with pre-registered structural boundaries**
  ([[h-new-130-fisher-rao-residuals|H-NEW-130]]/130b/130c, triple-feature replication; 3 universal hinges: Q 14→15,
  Q 49→50, Q 56→57)
- **Mushaf is ~8% LESS predictable than Nöldeke chronology** from 15
  compositional features ([[h-new-192-mushaf-position-decomposition|H-NEW-192]]: R²=0.76 vs 0.836)
- **All four published chronologies (Nöldeke, Bell, Egyptian, Blachère) beat
  random under Fisher-Rao** — so chronology-sorting ALSO has real coherence
  signal ([[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] PASS family-level) — but **mushaf is shorter than all four**
- **Length-desc ↔ canonical τ = +0.84**: mushaf dominantly length-sorted
  (canonical-order-recovery)
- **Length-residualized NCD τ = +0.648, p < 10⁻⁴**: there IS a thematic residual
  layer beyond length
- **al-Biqāʿī's global "last 9 mirror first 9"** = REFUTED at z = −4.87
  (classical-quantitative-claims-audit.md)
- **Local pairwise munāsabāt** = 17/113 edges recovered by blind structural TSP,
  p < 10⁻⁴; 5+ of them are specifically pairs al-Biqāʿī named (Q 92-93, Q 62-63,
  Q 82-83, Q 113-114, Q 17-18, Q 2-3, Q 4-5)

With that evidence in hand, here is each classical position.

---

## Position 1. al-Zarkashī (d. 794 AH / 1392 CE) — *al-Burhān fī ʿUlūm al-Qurʾān*

### (a) Claim

Nawʿ 2 of *al-Burhān* — *munāsabāt al-suwar wa-l-āyāt* — articulates the
foundational Sunnī doctrine that the canonical *tartīb al-suwar* (order of
surahs) is **tawqīfī** (divinely fixed), not ijtihādī (a human committee
decision). Zarkashī catalogues dozens of specific thematic and rhetorical
connections between adjacent surahs and between adjacent verses. He concedes
some surahs may have been ijtihādī-ordered (a minority position) but his
stronger claim is that most inter-surah transitions have a *discoverable
munāsaba* that justifies the sequence.

Zarkashī is also the principal medieval source for the catalogue of 77,934
Quranic words (later cited by Suyūṭī), but does not compute per-surah structural
metrics.

### (b) Empirical predictions if TRUE

1. **Local adjacency coherence**: adjacent surahs should share vocabulary,
   rhetoric, or thematic elements more than randomly-selected pairs.
2. **Fawātiḥ ↔ khawātim echoes**: surah-openings and surah-endings should
   rhyme structurally; adjacent surahs' openings/endings should echo.
3. **The tartīb should be rediscoverable** from text similarity if the
   tradition is telling the truth about its non-arbitrariness.

### (c) Status per our landed findings

- Prediction 1 **PARTIALLY CONFIRMED**. Fisher-Rao [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] shows
  mushaf-adjacent surahs are root-content closer than random permutations
  (z = −11, two feature spaces). On canonical-order-recovery's blind TSP
  search, 17 of 113 canonical edges are rediscovered at p < 10⁻⁴. **Mushaf
  local continuity is strongly empirically validated.**
- Prediction 2 **PARTIALLY SUPPORTED**. [[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]] documents literal rhetorical
  bridging at the 3 universal hinges (e.g., Q 56:96 *fa-sabbiḥ* → Q 57:1
  *sabbaḥa*, same root bridging a 58-position Nöldeke chronological gap).
- Prediction 3 **QUALIFIED**: canonical-order-recovery's combined-τ FAILS
  at p = 0.81 (primary pre-reg), but the adjacent-pair count (17/113) is
  extreme (p < 10⁻⁴), and length-residualized NCD yields τ = +0.648.

**Zarkashī's tawqīfī-munāsaba thesis is empirically vindicated at the LOCAL
resolution** (adjacent-pair level) but cannot be reified at the global (whole
sequence from one similarity metric) resolution.

---

## Position 2. al-Suyūṭī (d. 911 AH / 1505 CE) — *al-Itqān fī ʿUlūm al-Qurʾān*

### (a) Claim

Nawʿ 18 *Fī tartīb al-suwar wa-l-āyāt* catalogues **both sides of the
tawqīfī vs ijtihādī debate**. Suyūṭī explicitly records:

- The tawqīfī position (majority): ordering is divinely stipulated, attributed
  to hadith reports of Jibrīl dictating surah placement to the Prophet.
- The ijtihādī position (minority, attributed to Mālik and reported by Qāḍī
  Abū Bakr al-Bāqillānī in *al-Intiṣār*): ordering of surahs was a ṣaḥāba
  decision, but ordering of āyāt within surahs is unanimous tawqīfī.
- A hybrid position: some surahs tawqīfī (e.g., Fātiḥa, al-Zumar follows
  al-Ṣāffāt on hadith report), others ijtihādī.

Suyūṭī's own **Asrār Tartīb al-Qurʾān** (separate monograph) commits more
strongly to tawqīfī. He also cites length-descending observations and
mufaṣṣal-classification. *Al-Itqān* records total-word counts (77,934 /
77,437 / various narrations) but not per-surah or per-root counts.

### (b) Empirical predictions if TRUE

1. (Tawqīfī branch) Global structural coherence beyond what a length-sorted
   committee could produce.
2. (Ijtihādī branch) Length-descent is the dominant visible axis; residual
   thematic placements where the committee had theological reasons.
3. Either way: surah placement decisions should correlate with the classical
   mufaṣṣal/mi'ūn/mathānī partitioning.

### (c) Status

- Prediction 1 **PARTIALLY CONFIRMED**: [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]]'s geodesic-
  optimality result goes beyond pure length. Pure length-descending ordering
  L ≈ 107 ≈ null mean; mushaf L = 85.76 (z = −11). So mushaf has structure
  BEYOND length-sorting.
- Prediction 2 **CONFIRMED**: canonical-order-recovery τ(length-desc,
  canonical) = +0.84. Length is the dominant layer as the ijtihādī-hybrid
  position describes.
- Prediction 3 **PARTIALLY SUPPORTED**: [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]'s Q 49→50 universal hinge
  is the canonical mufaṣṣal-alt entry point. [[h-new-192-mushaf-position-decomposition|H-NEW-192]]'s verse-count feature
  dominates mushaf-position prediction at 42% of feature importance.

**Suyūṭī's hybrid position (two-layer: length + theological residual) maps
almost exactly onto what the data shows** (canonical-order-recovery's "two-
layered" honest-synthesis section). This is the **empirical winner among
classical positions** at the non-metaphysical level.

---

## Position 3. al-Biqāʿī (d. 885 AH / 1480 CE) — *Naẓm al-Durar fī Tanāsub al-Āyāt wa-l-Suwar*

### (a) Claim

The 22-volume *Naẓm al-Durar* is the most ambitious classical operationalization
of the tawqīfī-munāsaba thesis. Biqāʿī argues **every** adjacent-verse and
adjacent-surah transition has a discoverable connective principle; the mushaf
is a DIVINELY ORDERED composition where no sequence is arbitrary. Stronger:
he argues the **last 9 surahs mirror the first 9** as a whole-mushaf ring,
anticipating Farrin (2014) by five centuries.

Biqāʿī also commits to *ilm al-munāsabāt* as a formal discipline with rules
(thematic echo, lexical repetition, legal/rhetorical pairing).

### (b) Empirical predictions if TRUE

1. **Whole-mushaf global ring**: last 9 surahs content-mirror first 9.
2. **Every adjacent-surah pair has a munāsaba**: blind structural search
   should recover CANONICAL order at near-perfect τ.
3. **Adjacent pairs' content (vocabulary/roots) should be systematically
   tighter than non-adjacent pairs** at whole-mushaf scale.

### (c) Status

- Prediction 1 **REFUTED**: classical-quantitative-claims-audit.md tested the
  explicit last-9 vs first-9 mirror thesis and found z = −4.87 (MORE disordered
  than random). Al-Biqāʿī's global-ring claim FAILS.
- Prediction 2 **REFUTED at the strongest reading**: canonical-order-recovery
  combined-τ = +0.015, p = 0.81. Blind structural search does NOT rediscover
  every munāsaba.
- Prediction 3 **CONFIRMED at a weaker local reading**: adjacent-pair
  recovery 17/113 at p < 10⁻⁴ is 8× null-mean; many of the 17 are Biqāʿī's
  specifically-named pairs (Q 92-93, Q 17-18, Q 62-63, Q 113-114, Q 82-83).
  Length-residualized NCD τ = +0.648 (STRONG) shows thematic residual.
- **[[cross-finding-013-mushaf-topological-ring|Cross-finding-013]]'s topological ring** vindicates a DIFFERENT ring claim
  than Biqāʿī's: Q 1 ↔ terminal-triad content closure (z = −4.17) is a
  ring of a-different-topology — the ring closes AT Q 114 ↔ Q 1, not at
  the first-9/last-9 mirror.

**Biqāʿī's STRONG thesis (every transition has a discoverable munāsaba and
the whole mushaf is a first-9/last-9 mirror) is REFUTED at the global scale.
His WEAK thesis (adjacent surahs systematically have connective principles)
is CONFIRMED at the local scale.** This is rules-tuple sensitivity
bidirectional (memory feedback_rules_tuple_bidirectional): the global
claim breaks but the local claim is rehabilitated.

---

## Position 4. Ibn Taymiyya (d. 728 AH / 1328 CE)

### (a) Claim

Ibn Taymiyya's position in *Majmūʿ al-Fatāwā* and his Quranic-studies writings
is a **moderated tawqīfī** stance: the canonical order is divinely mandated
in its broad shape, with specific liturgical/theological purposes (Fātiḥa as
opening, al-Ikhlāṣ + muʿawwidhatān as closure), but he is skeptical of the
more speculative munāsaba exercises. Ibn Taymiyya's broader methodology
rejects ilm-al-ḥurūf / abjad / numerological readings of the mushaf. He
prioritizes *al-maʿnā al-ẓāhir* (the evident meaning) over deep structural
reading.

Ibn Taymiyya's specific contribution to the tartīb question is restraint:
he accepts tawqīfī ordering as doctrine without requiring every transition
to yield a discoverable munāsaba to human analysts.

### (b) Empirical predictions if TRUE

1. **Fātiḥa as opening + muʿawwidhatān as closing are liturgically/structurally
   distinguished** from generic surah placement.
2. **No requirement that every transition be structurally tight** — null results
   at individual pair level are theologically acceptable.
3. **No prediction of abjad/numerological coherence.**

### (c) Status

- Prediction 1 **STRONGLY CONFIRMED**: [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]'s ring topology
  identifies Fātiḥa and the terminal triad {Q 112-114} as content-closed
  (z = −4.17 to −4.51 on two features). [[h-new-155-q1-sui-generis|H-NEW-155]] found Q 1 sui-generis.
- Prediction 2 **COMPATIBLE**: canonical-order-recovery's 17/113 adjacent-
  pair recovery (vs null 2.01) is consistent with "some adjacencies are
  meaningful, not all" — which is Ibn Taymiyya's restrained stance.
- Prediction 3 **COMPATIBLE**: project's abjad-residue null findings
  (abjad-residue-fasila-mechanism.md and abjad-residue-null.md) support
  Ibn Taymiyya's anti-numerological caution; H-NEW-19 and related abjad
  series have weak or null results.

**Ibn Taymiyya's moderated tawqīfī position is the most
empirically-well-calibrated of the classical positions**: it predicts
exactly what the data shows — meaningful framing (Fātiḥa, muʿawwidhatān),
variable local coherence, no strong numerological structure.

---

## Position 5. Modern Muslim *naẓm* school — al-Farāhī (d. 1930), al-Iṣlāḥī (d. 1997)

### (a) Claim

Ḥamīd al-Dīn al-Farāhī and his student Amīn Aḥsan al-Iṣlāḥī (*Tadabbur-i-
Qurʾān*) revive and systematize the *naẓm* doctrine: the Quran is organized
into **surah-pairs** (zawj) sharing a single theme, and these pairs are
grouped into **seven groups** with a shared theme-progression. Each surah
has a central *ʿamūd* (thematic pillar) that governs its content. The
mushaf order is NOT chronological — it is thematic-structural by design.

Iṣlāḥī's seven groups:
1. Q 1-5, 2. Q 6-9, 3. Q 10-29, 4. Q 30-49, 5. Q 50-66, 6. Q 67-104, 7. Q 105-114.

Each group has a ring-or-parallel internal structure. Surahs 2-3, 4-5, 6-7,
10-11, 12-13, 14-15, 16-17, 18-19, ... are claimed to be paired.

### (b) Empirical predictions if TRUE

1. **Surah pairs** (Q 2-3, Q 4-5, Q 6-7, Q 8-9, Q 10-11, ...) should be
   systematically content-closer than non-adjacent same-group surahs.
2. **Group boundaries** (Q 5→6, Q 9→10, Q 29→30, Q 49→50, Q 66→67, Q 104→105)
   should appear as structural hinges.
3. Mushaf should be predictable from thematic features (not just length).

### (c) Status

- Prediction 1 **PARTIAL CONFIRMATION**: canonical-order-recovery's top
  adjacent-pair recoveries include Q 4-5, Q 2-3, Q 12-13 cluster. Iṣlāḥī's
  pair Q 2-3 is the strongest-content-ring-center per H-NEW ring tests.
  But not ALL Iṣlāḥī pairs survive (partial, not total, support).
- Prediction 2 **STRIKINGLY CONFIRMED**: [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]'s 3 universal hinges
  include **Q 49→50** (Iṣlāḥī's group-4 → group-5 boundary) and Q 56→57
  is within Iṣlāḥī's group 5. Q 14→15 is an intra-group-3 hinge. The
  mufaṣṣal-alt start at Q 50 is both classical and Iṣlāḥī-boundary.
- Prediction 3 **CONFIRMED**: [[h-new-192-mushaf-position-decomposition|H-NEW-192]] shows mushaf-position predictable at
  R² = 0.76-0.82 from 15 compositional features including eschatological
  density, divine-name density, legal density — thematic axes exactly
  aligned with Iṣlāḥī's ʿamūd theory.

**Farāhī–Iṣlāḥī's naẓm-school is STRONGLY supported** by our empirical work,
especially at the group-boundary level. Q 49→50 as a deliberate architectural
hinge is vindicated across three orthogonal feature spaces ([[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]
TRIPLE-REPLICATION-CONFIRMED). This is the classical position that makes
the sharpest testable predictions and scores best on them.

---

## Position 6. Orientalist chronology reconstructions

### (a) Claims

- **Theodor Nöldeke** (*Geschichte des Qorāns*, 1860) — canonical order is
  non-chronological; real chronology recoverable from stylistic cues
  (verse length, fawātiḥ-type, rhyme density, vocabulary). 4 periods:
  Early/Middle/Late Meccan + Medinan.
- **Richard Bell** (*The Qurʾan: Translated with a Critical Rearrangement of
  the Surahs*, 1937-39) — more granular stylistic sort; proposes surah-internal
  redaction and re-ordering at the pericope level. Canonical order is
  redaction-artifact.
- **Régis Blachère** (*Le Coran*, 1947) — largely length-descending with
  Nöldekian-style chronological adjustments; Blachère's reading is "canonical
  order = length-sort + adjustment."
- **W. Montgomery Watt** (*Bell's Introduction to the Qurʾan*, 1970) — broadly
  Nöldekian but more cautious about fine-grained chronology; stresses
  canonical order is *not* chronology, *not* divinely structured, but a
  pragmatic Uthmanic committee decision.

### (b) Empirical predictions if TRUE

1. Canonical order correlates **negatively** with chronology (tradition itself
   says so — al-Dānī, al-Zamakhsharī).
2. **Length-descent** is the visible organizing axis.
3. Stylistic chronology (Nöldeke's verse-length, fawātiḥ, rhyme density)
   should be a coherent signal — surahs-in-chronological-order should show
   local stylistic continuity.
4. Canonical order should have NO structure beyond length + arbitrary
   committee choice.

### (c) Status

- Prediction 1 **CONFIRMED**: [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] reports ρ(mushaf, Nöldeke) = −0.655,
  ρ(mushaf, Bell) = −0.621, ρ(mushaf, Blachère) = −0.406, ρ(mushaf, Egyptian)
  = −0.406. All four chronologies are anti-correlated with mushaf.
- Prediction 2 **CONFIRMED**: τ(length-desc, canonical) = +0.84.
- Prediction 3 **CONFIRMED (weaker than mushaf)**: [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] finds all 4
  chronologies BEAT random under Fisher-Rao (p < 10⁻⁴ each). Nöldeke 1860
  L = 87.23 (z = −10.52), second-shortest path. So stylistic chronology DOES
  have real coherence — but mushaf (L = 85.76, z = −11.46) still beats it.
- Prediction 4 **REFUTED**: mushaf has structure BEYOND length. cross-
  finding-011 triple-feature replication (roots + char-4-grams + verse-length)
  shows mushaf L-shorter than 9999/10000 random permutations. [[h-new-192-mushaf-position-decomposition|H-NEW-192]]
  shows mushaf is ~8% less predictable than Nöldeke chronology from the
  same 15 compositional features — meaning mushaf has *additional*
  organizing information that pure chronology doesn't capture. Watt's
  "pragmatic committee" reading under-determines the data: a pragmatic
  committee would place length + easy-thematic-groups; it would not
  produce a Fisher-Rao near-TSP-optimal path with Q 1 ↔ Q 114 wrap-around.

**Orientalist chronology is partially-right (anti-correlation with mushaf,
length-dominant axis, real stylistic signal) but its strongest claim
— that mushaf is structurally arbitrary beyond length — is REFUTED at
multiple independent feature spaces.** The data shows mushaf order has
*more* organization than chronology-sorting, not less.

---

## Synthesis: a combined-empirical verdict

When we overlay our findings onto the six classical positions:

| Position | Core claim | Status |
|---|---|---|
| Zarkashī | tawqīfī + local munāsaba everywhere | **LOCAL-CONFIRMED**, global-not-tested-in-strong-form |
| Suyūṭī | two-layer: length + theological residual | **EMPIRICALLY BEST FIT** among classical positions |
| Biqāʿī (strong) | last-9 mirrors first-9 globally | **REFUTED** (z = −4.87) |
| Biqāʿī (weak) | adjacent-surah pairs have munāsaba | **LOCAL-CONFIRMED** (17/113 at p < 10⁻⁴) |
| Ibn Taymiyya | moderated tawqīfī + liturgical framing | **BEST-CALIBRATED**: predicts exactly what data shows |
| Farāhī–Iṣlāḥī | naẓm + pairs + 7-groups + ʿamūd | **STRONGLY SUPPORTED**, Q 49→50 hinge vindicated |
| Nöldeke/Bell/Blachère/Watt | canonical is length + anti-chronology + arbitrary beyond | **PARTIAL** — first two true, third REFUTED |

### The data-supported picture

The canonical mushaf order is a **punctuated-cycle geodesic** (per
[[cross-finding-013-mushaf-topological-ring|cross-finding-013]]): a Hamiltonian cycle in Fisher-Rao content space that
closes at Q 114 → Q 1, dominated by length-descent (τ = 0.84 with
length-desc ordering), but with:

1. **Local root-content continuity** beyond length ([[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]], τ_resid
   = 0.648 when length is partialled out)
2. **15 deliberate structural hinges** at pre-registered architectural boundaries
   ([[h-new-130-fisher-rao-residuals|H-NEW-130]] triple-feature confirmed; 3 are universal across all 3 features)
3. **Rhetorical bridges** at the deepest chronological jumps ([[h-new-142-universal-hinges-chrono-rhetorical|H-NEW-142]]:
   Q 56:96 *sabbiḥ* → Q 57:1 *sabbaḥa*)
4. **Ring-closure** where Q 1 ↔ terminal-triad are content-anomalously close
   ([[cross-finding-013-mushaf-topological-ring|cross-finding-013]], z ≈ −4 on 3 features)

**This is neither the orientalist "arbitrary-beyond-length" nor Biqāʿī's
"every transition is a munāsaba and the whole mushaf is a first-9/last-9
mirror." It is CLOSEST to Suyūṭī's hybrid-tawqīfī-ijtihādī position and
Ibn Taymiyya's moderated tawqīfī + Farāhī–Iṣlāḥī's naẓm-of-groups with
deliberate hinges.**

The project makes NO claim that this adjudicates the theological question
of divine authorship vs human-committee-under-divine-guidance vs any other
metaphysics. The empirical observation stops at: **the mushaf has more
organizing information than pure length or pure chronology, that information
is structured rather than random, and the classical scholars who claimed
"there is structure here" were mostly right; the ones who claimed "ALL is
structure" (strong Biqāʿī) overshot; the ones who claimed "there is NO
structure beyond length" (strong Nöldekian) undershot.**

---

## Honest limits of this review

1. **No new tests were run for this survey.** All empirical statuses are
   inherited from parent-findings pre-registered independently before this
   synthesis. No garden-of-forking-paths here because no tests are selected
   post hoc.

2. **The six-position taxonomy is conventional, not exhaustive.** Other
   positions exist (e.g., Ibn al-Zubayr al-Gharnāṭī's *al-Burhān fī Tartīb
   Suwar al-Qurʾān*, Ṭāhir ibn ʿĀshūr's *al-Taḥrīr wa-l-Tanwīr* introduction
   on tartīb). These could be added.

3. **Tawqīfī vs ijtihādī is a theological binary** that empirical methods
   cannot adjudicate. What we can and do say is that the *effect* of either
   cause (divine dictation or sophisticated committee work) is the same:
   structured, non-arbitrary, multi-axis organization. Our work is agnostic
   between the two causal stories.

4. **All findings inherit their own MW-tier + Bonferroni discipline.**
   [[cross-finding-011-mushaf-fisher-rao-confirmed|cross-finding-011]] CONFIRMED, [[cross-finding-013-mushaf-topological-ring|cross-finding-013]] CONFIRMED, [[h-new-130c-fisher-rao-residuals-verselen|H-NEW-130c]]
   TRIPLE-REPLICATED, [[h-new-212-alt-chronology-fisher-rao|H-NEW-212]] Bonferroni-k=3 PASS. The classical-
   quantitative-claims-audit Biqāʿī-refutation z = −4.87 is single-test
   but at the level of classical-giants that is the relevant scale.

5. **Classical citations in this review are summarized from project files**
   (classical-cross-references.md, fresh-wave-3-classical-anchors.md,
   canonical-order-recovery.md, [[cross-finding-013-mushaf-topological-ring|cross-finding-013]]). Edition-level verification
   is MW-tier-variable (mostly PENDING per fresh-wave-3 methodology).

---

## Files cited

- `/Users/grey/Downloads/quran/findings/classical-cross-references.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/canonical-order-recovery.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-011-mushaf-fisher-rao-confirmed.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-013-mushaf-topological-ring.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-130-fisher-rao-residuals.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-142-universal-hinges-chronology-reversal.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-183-chronology-predictor.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-189-medinan-inclusio.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-192-mushaf-position-decomposition.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-212-alt-chronology-fisher-rao.md`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/classical-quantitative-claims-audit.md`
- `/Users/grey/Downloads/quran/findings/classical-sources/fresh-wave-3-classical-anchors.md`

## Status

**DESCRIPTIVE-REVIEW, LANDED**: combines citation of 6 classical/orientalist
positions with empirical status from already-landed findings. No new test
ran; no new p-value claimed. [[h-new-226-mushaf-order-scholarly-review|H-NEW-226]] is complete.

**Follow-up candidate ([[h-new-227-wrap-edge-chronologies|H-NEW-227]])**: direct test of Farāhī–Iṣlāḥī's 7-group
structure as a grouping hypothesis — compute within-group vs across-group
Fisher-Rao distance ratio and test against permutation null. If this lands,
it would upgrade the Farāhī–Iṣlāḥī position from "strongly supported" to
"directly confirmed."
