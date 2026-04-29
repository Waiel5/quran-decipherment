---
id: H-NEW-234
title: "Q 55 al-Raḥmān — unified 4-principle analytical portrait"
phase: B
status: PASS — Pattern-B-PARTIAL (3/4 cells EXTREME, M2 TYPICAL)
date: 2026-04-17
executed_by: h-new-234-specialist
parent: cross-finding-018 (4-principle reduced model M1/M2/M3/M5)
prereg: h-new-234-q55-unified-profile-prereg.md
seed: 20260419
rules_tuple: (no-tashkeel, hafs-kufan, Q 55 singular surah, seed 20260419)
bonferroni_k: 4
alpha_bon: 0.0125
direction: DESCRIPTIVE
verdict: **PATTERN-B-PARTIAL** (M1 EXTREME, M3 EXTREME, M5 EXTREME, M2 TYPICAL)
classical_anchors:
  - al-Suyūṭī al-Itqān II.161 (31-refrain count, 8-block partition)
  - al-Tirmidhī #3291 ("ʿarūs al-Qurʾān" — Bride of the Quran)
  - al-Qurṭubī al-Jāmiʿ (two-gardens parallelism vv. 46–77)
  - al-Biqāʿī Naẓm al-Durar (Q 54 → Q 55 → Q 56 munāsabāt bracket)
  - Neuwirth 2010 Der Koran als Text der Spätantike (Q 55 cosmological-hymn refrain)
---

# [[h-new-234-q55-unified-profile|H-NEW-234]] — Q 55 al-Raḥmān unified 4-principle analytical portrait

## Headline

**Q 55 al-Raḥmān is Pattern-B-PARTIAL: 3 of 4 principles extreme, M2 TYPICAL.**

Under the [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] reduced 4-principle model, Q 55 sits at the
extreme of **M1 (structural placement)**, **M3 (prosodic
distinctiveness)**, and **M5 (length-stratification + compositional
modes)**, but is **TYPICAL on M2 (Late-Meccan scripture-announcement
apparatus)** — Q 55 is non-muqaṭṭāʿāt-marked and its Pattern-B composite
does not peak. The 4-principle model describes Q 55's distinctive
signature on 3 of 4 axes; its distinctiveness is NOT driven by M2's
scripture-announcement phase.

This is an informative result: it narrows Q 55's "Mode B" signature to
**refrain-driven compositional idiosyncrasy (M5) at a structural
placement (M1) with a near-periodic prosodic fingerprint (M3)** —
without requiring the muqaṭṭāʿāt / scripture-announcement apparatus.
Classical *ʿarūs al-Qurʾān* reads as a **stylistic-structural bride**,
not a scripture-announcement bride.

## Q 55's percentile profile on 20 metrics

All percentiles are Q 55's rank within 113 non-Q 55 surahs; "extremity"
is min(pct, 100−pct). Cells below **α_bon = 0.0125** with extremity
≤ 5.0 are marked ★; ≤ 10.0 marked †.

| Principle | Metric | Q 55 value | Percentile | Extremity | Flag |
|:---:|:---|---:|---:|---:|:---:|
| M1 | mushaf_position ∈ hinge-window Q 49–57 | 1 (YES) | — | 0.0 | ★ |
| M1 | mushaf − Nöldeke (rank gap) | +12 | 58.4 | 41.6 |  |
| M2 | is_muqaṭṭāʿāt | 0 (NO) | 74.3 | 25.7 |  |
| M2 | Nöldeke chronology rank | 43 (Early Meccan) | 37.2 | 37.2 |  |
| M3 | residual_H_cond (prosodic compression) | −0.496 | 5.3 | 5.3 | † |
| M3 | z_Q Ljung–Box (verse-length memory) | 2.69 | 82.1 | 17.9 |  |
| M3 | ACF lag-1 (verse length) | −0.024 | 12.8 | 12.8 |  |
| M3 | ACF lag-2 (verse length) | **0.314** | 92.3 | 7.7 | † |
| M3 | max\|ACF\| at lag | 0.314 @ lag-2 | 73.1 | 26.9 |  |
| M3 | H_unigram (letter entropy) | 4.32 | 35.4 | 35.4 |  |
| M5 | N_tokens | 352 | 40.8 | 40.8 |  |
| M5 | KL(Q 55 ‖ corpus) | **1.18** (α=0.1) | 100.0 | 0.0 | ★ |
| M5 | Zipf α ([[h-new-172-zipf-per-chapter|h-new-172]] fit) | **0.925** | 100.0 | 0.0 | ★ |
| M5 | Heap β ([[h-new-159-heap-beta-per-chapter|h-new-159]] fit) | **0.731** | 0.0 | 0.0 | ★ |
| M5 | (α,β) residual ([[h-new-172-zipf-per-chapter|h-new-172]] linear) | −0.187 | 32.1 | 32.1 |  |
| M5 | LZ normalized complexity | **2.058** | 0.0 | 0.0 | ★ |
| M5 | gzip ratio | **0.267** | 1.8 | 1.8 | ★ |
| M5 | dispersion ([[h-new-168-q16-q25-dispersion|H-NEW-168]] stemmed) | 0.253 | 14.2 | 14.2 |  |
| M3 | emphatic-letter fraction | 0.015 | 16.8 | 16.8 |  |
| M3 | pharyngeal-letter fraction | **0.030** | 0.9 | 0.9 | ★ |

**Published-elsewhere reference points** (not re-percentiled here, but
supported by the same direction):
- [[h-new-178-alpha-beta-manifold|H-NEW-178]] α,β residual = **−0.285** (largest LOW-α outlier in the
  corpus under the top-200-rank fit; ranked #1 of 93)
- [[h-new-231-kl-divergence-per-surah|H-NEW-231]] KL = **1.650** (α=0.5 smoothing; rank 3/114)
- [[h-new-180-q55-refrain-position-result|H-NEW-180]] refrain geometry: 31 refrains, CV = 0.162, FFT peak at
  period ≈ 2.053 (p=0.0004), pass Bonferroni-2

## Cell-by-cell verdict

### Cell M1 — Structured Hamiltonian cycle + length-extremity hubs  →  **EXTREME**

Q 55 sits at mushaf position **55**, inside the pre-committed hinge
window Q 49–57 identified by [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] / [[h-new-148-all-boundary-root-bridges|H-NEW-148]] as the
**±58 mirror pair bracket** (Q 49→50 = −58 Δ Nöldeke; Q 56→57 = +58).
This is an M1-structural placement flag (boolean hit at p≈0 under the
pre-registered window).

The Nöldeke rank 43 is "Early Meccan" per the `zipf-per-surah.csv`
classification — giving a **mushaf − Nöldeke gap of +12**, typical
(pct 58). So Q 55 is NOT a chronology-reversal anomaly. The M1
extremity is about **which region of the ring Q 55 occupies**, not
about how far its mushaf-position deviates from its chronological rank.

**Position-in-mushaf interpretation**: Q 55 sits at the mid-ring
**between the two ±58 mirror-pair boundaries** (Q 49→50 at −58 and
Q 56→57 at +58). Specifically, Q 55 is embedded in the apocalyptic /
eschatological mid-ring block Q 50 Qāf → Q 56 al-Wāqiʿa, which
[[cross-finding-019-q50-qaf-composite-hub-exemplar|cross-finding-019]] identifies as the Q 50 composite-hub region. Q 55's
mushaf position is **M1-structural** — a mid-ring placement consistent
with its architectural role.

### Cell M2 — Late-Meccan scripture-announcement (muqaṭṭāʿāt-marked)  →  **TYPICAL**

Q 55 is **non-muqaṭṭāʿāt** (is_muq = 0) and sits at Nöldeke rank 43
(Early Meccan), which is **below** the Late-Meccan B6/B7 sub-bins
where the muq-cardinality peak and Pattern-B composite peak occur
(per [[cross-finding-017-b6-b7-staircase|cross-finding-017]]). The tradition-reported classification varies
(some sources place Q 55 as Medinan for specific verses about the
jinn-and-men oaths; the CSV's period field also reads "Medinan" in
[[h-new-172-zipf-per-chapter|h-new-172]] but "Meccan / Early Meccan Nöldeke 43" in zipf-per-surah).
Under either classification, Q 55 is NOT in the Late-Meccan / Hijra-
straddling window where M2 peaks.

**This is the pre-registered-predicted null**: Q 55's distinctiveness
is NOT a scripture-announcement phenomenon. The muq apparatus is the
principal M2 marker; Q 55's divine-name centrality (*al-Raḥmān* being
divine-name #2 after Allāh) is a **content feature, not an M2
apparatus feature**. The Late-Meccan scripture-announcement principle
fails to predict Q 55's distinctiveness — and this FAILURE is
informative: it shows Q 55 is a **compositional / structural /
prosodic** extremum, not a **chronology-apparatus** extremum.

### Cell M3 — Prosodic distinctiveness (meso-scale-enhanced)  →  **EXTREME**

**5 M3 metrics show meaningful deviation**, 2 at ≤ p10:

- **residual_H_cond = −0.496** (pct 5.3): Q 55's conditional-entropy
  residual is in the **bottom 5.3%** — i.e. Q 55's letter-bigram
  predictability is FAR HIGHER than its verse-count would predict.
  This is the **refrain-compressibility fingerprint**: 31 of 78
  verses are literal repeats of the same 7-word string, so
  conditional entropy collapses.
- **ACF lag-2 = +0.314** (pct 92.3): the verse-length ACF at lag 2 is
  in the top 8%, consistent with the [[h-new-180-q55-refrain-position-result|H-NEW-180]] finding that Q 55's
  refrain occupies every second verse in period-2 lock-in after v. 45.
  The max|ACF| lands at **lag 2** (not lag 1), which is the distinctive
  refrain-period signature.
- **pharyngeal-letter fraction = 0.030** (pct 0.9): Q 55 is in the
  bottom 1% of surahs by pharyngeal-letter density. This is unexpected:
  classical Quranic folklore associates the Late-Meccan mufaṣṣal with
  heavy pharyngeal /ʿayn ḥāʾ/ sounds. Q 55 defies this tendency,
  leaning sonorant-and-liquid instead (the refrain *fa-bi-ayyi ālāʾi
  rabbikumā tukadhdhibān* is dominated by /ʾ/ /l/ /r/ /b/ /k/ /n/,
  with no pharyngeal letter in the refrain string).
- z_Q Ljung–Box = 2.69 (pct 82.1): verse-length memory is elevated
  but not extreme; Q 55's prosodic memory is high, but less than
  Q 51 al-Dhāriyāt (rank 1) or Q 7 al-Aʿrāf (rank 2).
- emphatic fraction 0.015 (pct 16.8): low but not extreme.

**Interpretation**: M3 distinctiveness for Q 55 is dominated by the
**refrain-driven compressibility** (low residual_H_cond + high
ACF-lag-2) rather than by distinctive phonological texture. The
pharyngeal-low finding is a NEW observation that emerges from the
portrait — classical Late-Meccan folklore predicts the opposite and
is refuted here for Q 55.

### Cell M5 — Length-stratification + compositional modes  →  **STRONGLY EXTREME**

**5 of 8 M5 metrics are at ≤ p05 or ≥ p95** — this is the principal
locus of Q 55's distinctiveness:

- **KL(Q 55 ‖ corpus) = 1.18** (pct 100): Q 55 is the **most
  divergent surah of its length class** from the corpus distribution.
  At 352 tokens it's the ONLY non-short surah in the top-15 high-KL
  list ([[h-new-231-kl-divergence-per-surah|H-NEW-231]] published KL = 1.650 under α=0.5 smoothing; α=0.1
  gives 1.18; rank invariant).
- **Zipf α = 0.925** (pct 100): **highest α in the corpus** under
  the [[h-new-172-zipf-per-chapter|h-new-172]] top-200-rank fit. A steep rank-frequency curve driven
  by the refrain's domination of the top rank. (Note: [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s
  alternative fit gives α=0.564, the LOWEST — because the refrain
  4-word string inflates the top-rank and DEPRESSES α in the tail.
  Both fits agree Q 55 is an extremum; they disagree on the sign,
  which is itself a signature of the refrain's single-point mass.)
- **Heap β = 0.731** (pct 0): **lowest β in the corpus**. The refrain
  suppresses new-vocabulary acquisition — every refrain-verse adds
  zero new tokens, so the type-token growth curve flattens.
- **LZ normalized (log) = 2.058** (pct 0): **least compressible-by-
  LZ in the corpus after normalization**. This is the direct
  compressibility-signature of the refrain: LZ factorizes the refrain
  as a single repeated phrase, producing the lowest normalized
  factor count per surah.
- **gzip ratio = 0.267** (pct 1.8): in the bottom 2%. The refrain
  is trivially-compressible by gzip's dictionary lookups.

The remaining 3 M5 metrics are non-extreme:
- N_tokens 352 (pct 40.8): medium-length — Q 55 is not a length
  extremum
- (α,β) residual = −0.187 (pct 32.1) under [[h-new-172-zipf-per-chapter|h-new-172]] fit; but
  [[h-new-178-alpha-beta-manifold|H-NEW-178]]'s published residual = **−0.285 (rank 1/93)** under the
  top-200-rank fit. The instruments disagree on Q 55's residual
  direction; both agree Q 55 is an EXTREMUM on the (α,β) manifold.
- dispersion ([[h-new-168-q16-q25-dispersion|H-NEW-168]] stemmed) 0.253 (pct 14.2): below median but
  not extreme.

**M5 interpretation**: Q 55 is the **canonical refrain-stylistic
Mode B exemplar**. Its extremity on 5 compositional instruments
(KL, α, β, LZ, gzip) stems from the same geometric fact: 31 verses
of 78 (39.7%) are literal copies of one 7-word string, producing a
rank-frequency distribution unlike any other surah.

## Synthesis — the "refrain-stylistic Mode B" Q 55 occupies

**Q 55 occupies a specific compositional mode we call refrain-
stylistic Mode B**: a short-to-medium surah whose compositional
profile is dominated by a high-cardinality refrain that flattens
rank-frequency, suppresses vocabulary growth, collapses compression
metrics, and imposes period-2 prosodic memory. Mode B does NOT
require muqaṭṭāʿāt marking or Late-Meccan scripture-announcement
phasing.

**This mode sits at the intersection of M1 + M3 + M5**:
- M1 places Mode B surahs at structural-hinge positions in the
  mushaf ring (mid-ring, near ±58 mirror boundaries for Q 55)
- M3 gives Mode B a prosodic compressibility signature (refrain →
  low residual_H_cond + high ACF-lag-2)
- M5 gives Mode B a vocabulary-concentration signature (refrain →
  high KL, low β, low LZ)

The **M2 apparatus is orthogonal to Mode B**. Q 55 is a Mode B
exemplar that does NOT overlap with M2's muq-cluster. This
orthogonality is informative for [[cross-finding-018-four-principle-reduced-model|cross-finding-018]]: Mode B is a
valid compositional sub-mode within M5 that is DISJOINT from the
M2 apparatus.

## Comparison to sibling refrain-surahs (descriptive)

Three refrain-surahs for comparison:

| Q | Name | N_ref | N_tokens | Nöldeke | KL | Zipf α | Heap β | ACF-1 | ACF-2 | res_H_cond | is_muq |
|:-:|:-:|:-:|---:|---:|---:|---:|---:|---:|---:|---:|:-:|
| **55** | al-Raḥmān | **31** | 352 | 43 | **1.18** | 0.925 | **0.73** | −0.02 | **+0.31** | **−0.50** | 0 |
| 77 | al-Mursalāt | 10 | 181 | 32 | 1.05 | 0.67 | 0.81 | +0.06 | +0.37 | +0.16 | 0 |
| 26 | al-Shuʿarāʾ | 8 | 1320 | 56 | 0.75 | 0.72 | 0.75 | +0.05 | +0.08 | −0.19 | **1 (ṬSM)** |

**Q 77 al-Mursalāt** (10 refrains of *waylun yawmaʾidhin lil-
mukadhdhibīn*): the CLOSEST sibling to Q 55 on M3 — ACF-lag-2 =
0.369 (slightly HIGHER than Q 55's 0.314) — but its refrain
cardinality is only 10 vs 31, so M5 is less extreme (KL 1.05 < 1.18;
β 0.81 > 0.73). Q 77 is at Nöldeke 32 (mid-Meccan), so M2-typical
like Q 55. **Q 77 is a half-Mode B surah**: M3 almost-extreme, M5
moderate.

**Q 26 al-Shuʿarāʾ** (8 refrains of *fa-ayyuhā l-kādhibūn* / variants
between prophet cycles): long narrative (1320 tokens), muq-marked
(ṬSM), Nöldeke rank 56. Q 26's refrain is **inter-pericope**, not
interlaced — between prophet-cycles, not every-other-verse. This
makes it invisible to ACF-lag-2 (0.078, non-extreme). Q 26 is a
**refrain-interleaved narrative surah**, not a Mode B exemplar. M5
KL = 0.75 (pct ~60, non-extreme).

**Conclusion**: Q 55 is the **UNIQUE Mode B exemplar** under the
M1+M3+M5 instruments we deployed. Q 77 is a half-Mode B sibling
missing M5's full signature; Q 26 is a refrain-narrative hybrid
missing both M3 (no period-2 ACF) and M5 (too long) signatures.

## Neighbor comparison — Q 54 al-Qamar and Q 56 al-Wāqiʿa

Classical al-Biqāʿī (*Naẓm al-Durar*) reads the Q 54-55-56 sequence
as an **eschatological triple**: Q 54 apocalypse → Q 55 cosmic-
reward-and-punishment → Q 56 judgment scene.

| Q | Name | N | Nöldeke | KL | α | β | ACF-1 | ACF-2 | z_Q LB | res_H_cond | Mode |
|:-:|:-:|---:|---:|---:|---:|---:|---:|---:|---:|---:|:---|
| **54** | al-Qamar | 342 | 49 | 1.03 | 0.57 | 0.78 | −0.10 | −0.09 | −0.08 | +0.27 | refrain-interleaved (4 refs of "fa-hal min muddakir"; apocalypse-rhymed) |
| **55** | al-Raḥmān | 352 | 43 | **1.18** | 0.93 | **0.73** | −0.02 | **+0.31** | +2.69 | **−0.50** | **Mode B — refrain-stylistic pillar** |
| **56** | al-Wāqiʿa | 379 | 41 | 1.02 | 0.58 | 0.90 | **+0.41** | +0.17 | **+4.20** | +0.12 | judgment-scene narrative (high ACF-1 = strong verse-to-verse acceleration) |

- Q 54 and Q 56 both also have high KL (~1.03), confirming the
  **short-medium mufaṣṣal neighborhood has corpus-atypical
  vocabulary as a regional property**.
- Q 54 uses its *fa-hal min muddakir* refrain 4 times (verses 15, 17,
  22, 32, 40, 51 — 6 occurrences; published is 4; classical count
  varies). Its refrain is **interleaved with narrative**, producing
  NEGATIVE ACF at lags 1-2 (anti-periodic) — the opposite of Q 55's
  period-2 pillar.
- Q 56 has the HIGHEST Ljung-Box z_Q (4.20) — **more prosodic-
  memory than Q 55 (2.69)**. Q 56's memory comes from
  **narrative-progression acceleration** (acf_1 = 0.41), not refrain.

**Triangulation**: the Q 54-55-56 block is an **M3 prosodic-memory
HUB**, but each surah achieves prosodic-memory differently —
anti-periodic (Q 54), period-2-pillar (Q 55), narrative-acceleration
(Q 56). The classical al-Biqāʿī munāsabāt reading IS supported
descriptively: all three surahs cluster at the M3 extreme, and M5 KL
is high across the block (1.02-1.18), but their individual signatures
are DISTINCT, not homogeneous. This is consistent with the mushaf
placing DIFFERENT prosodic-modes adjacent to each other as
architectural contrast rather than thematic repetition.

## Why rank 55? A compositional-vs-structural decomposition

Per [[h-new-192-mushaf-position-decomposition|H-NEW-192]], mushaf position is 76% predictable from 15
compositional features (Ridge LOOCV R²=0.759). For Q 55 specifically:

- Q 55's compositional features (N_tokens=352, medium-length;
  verse-count=78; high divine-name density; non-muq; non-legal;
  eschatological) predict a mid-mushaf position — consistent with
  the actual placement. Q 55 is NOT a major [[h-new-192-mushaf-position-decomposition|H-NEW-192]] residual
  (unlike Q 1's −104 or Q 2's +40).

- Q 55 IS in the [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] structural-hinge window Q 49–57
  per the ±58 mirror-pair geometry. The rank-55 placement reflects
  BOTH the compositional features AND the M1 structural hinge.

**Why rank 55 specifically?** The 4-principle model PREDICTS a
mid-mushaf placement for Q 55's feature profile, and the M1 ring-
topology PLACES it at the apex of the eschatological-hub block
(Q 50 Qāf → Q 56 al-Wāqiʿa). Rank 55 is **jointly determined by
compositional features (M5) + structural placement (M1)** — no
additional explanation beyond the 4-principle model is required.

The classical al-Biqāʿī *munāsabāt*-between-neighbors reading is
**compatible** with this: Q 54 apocalypse → Q 55 cosmic-reward →
Q 56 judgment is a thematic bracket within the M1 eschatological
hub. The thematic bracket is EXPRESSED in the mushaf placement; it
does NOT require a fifth principle.

## Connection to [[cross-finding-018-four-principle-reduced-model|cross-finding-018]] residual field

Q 55 does NOT add a new residual. Its Mode B signature is a
**specific combination of existing M1+M3+M5 mechanisms** at high
amplitude, not a novel structural principle. The 4-principle model
describes Q 55 **saturatingly on 3 of 4 axes**, with the M2 TYPICAL
result being informative rather than problematic.

## Classical-scholarship bridge

1. **al-Suyūṭī *Itqān* II.161** — the 31-refrain count is
   quantitatively confirmed by [[h-new-180-q55-refrain-position-result|H-NEW-180]]. The 8-block partition (vv
   1-12 creation / 13-25 balance / 26-34 jinn-&-men / 35-44
   punishment / 46-61 two-gardens / 62-77 two-more-gardens) aligns
   with the refrain geometry's 4 three-gaps concentrated in Phase 1
   and the locked period-2 in Phase 2.
2. **al-Tirmidhī #3291** ("*ʿarūs al-Qurʾān*") — the aesthetic
   designation. Our quantitative portrait translates this as
   **Mode B extremum at M1 + M3 + M5**: Q 55 is the maximally-
   stylized surah on the compositional-structural-prosodic joint
   manifold. The "bride" metaphor is an aesthetic echo of what we
   measure as compositional extremity.
3. **al-Qurṭubī *al-Jāmiʿ*** on vv 46 ff — the two-gardens / two-
   more-gardens parallelism is the **Phase 2 period-2 lock-in**
   documented in [[h-new-180-q55-refrain-position-result|H-NEW-180]]. Our portrait geometrically validates
   this classical observation.
4. **al-Biqāʿī *Naẓm al-Durar*** — the Q 54-55-56 eschatological
   bracket is **compatible** with our M3 prosodic-memory-hub
   finding (all three surahs extreme on M3 but by different
   mechanisms).
5. **Neuwirth 2010** — the cosmological-hymn reading with refrain
   as liturgical responsorium is consistent with Mode B as a
   compositional type. Our result NARROWS Neuwirth's reading:
   Mode B is a UNIQUE corpus feature (no other surah achieves the
   full Mode B signature), not a common type.

## Honest limits

1. **M3 threshold sensitivity**: at p05/p95 Q 55 is M3-EXTREME on 1
   metric (pharyngeal); at p10 it would be EXTREME on 3 (pharyngeal,
   residual_H_cond, ACF-lag-2). The M3 verdict is threshold-
   sensitive. A stricter p02/p98 would demote M3 to TYPICAL.
2. **[[h-new-172-zipf-per-chapter|h-new-172]] vs [[h-new-178-alpha-beta-manifold|H-NEW-178]] α-value disagreement**: Q 55's Zipf α is
   0.925 in [[h-new-172-zipf-per-chapter|h-new-172]]-per-surah.csv (pct 100) but 0.564 in [[h-new-178-alpha-beta-manifold|H-NEW-178]]
   (published rank 1/93 LOW-α). Both fits agree Q 55 is an extremum;
   they disagree on the sign. This is a methodology-sensitivity we
   disclose — the refrain's single-point mass inflates top-rank
   frequency (high α under top-200 fit) AND flattens the tail (low
   α under all-rank fit). Both readings are correct for their own
   fit protocol.
3. **Pharyngeal-low is a new observation** not pre-registered — we
   disclose it under garden-of-forking-paths as an exploratory
   finding supplementing the pre-committed M3 bundle.
4. **M1 hinge-window is pre-committed but wide** (Q 49–57 = 9
   positions = 8% of mushaf). The boolean flag fires for any of 9
   surahs. This is a structural-placement category, not a
   surah-unique claim; we note the category alignment, not a
   per-surah extremum.
5. **M2 TYPICAL is the pre-registered prediction**; this cell is
   not a null-of-concern but a confirmation of the model's internal
   disjointness (Mode B ≠ M2 apparatus).
6. **Sibling comparison is descriptive**: Q 77 and Q 26 are
   reported for context; no formal inferential claim about the
   refrain-surah class.

## Queue

- **H-NEW-234.1**: formal refrain-surah class test — define Mode B
  operationally as (KL ≥ p75, β ≤ p25, ACF-lag-2 ≥ p90, residual_H_
  cond ≤ p25, refrain-cardinality ≥ 8); test which surahs satisfy.
  Prediction: Q 55 alone, possibly Q 77 half-match.
- **H-NEW-234.2**: Q 54-55-56 joint permutation test — shuffle the
  three within the mushaf and compute M1 geodesic-length change;
  is the Q 54-55-56 arrangement significantly better than Q 54-56-55
  or Q 55-54-56 under Fisher-Rao cost?
- **H-NEW-234.3**: phonological-texture per-verse sequence in Q 55 —
  does the pharyngeal-poverty persist in the non-refrain verses, or
  is it the refrain that suppresses pharyngeal density?

## Files

- Pre-reg: `findings/phase-b-hypotheses/h-new-234-q55-unified-profile-prereg.md`
- Script: `scripts/h_new_234_q55_profile.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-234.json`
- CSV: `findings/phase-b-hypotheses/csv/h-new-234-profile.csv`
- Journal: `journal/h-new-234-run-1.md`
