---
id: H-NEW-2390
title: Clause-scale (within-verse) iltifāt detector — recovers the Meccan>Medinan signal the verse-boundary detector missed
date: 2026-05-29
phase: B
verdict: CONFIRMED-PRIMARY (H1 region recovered at clause scale, p=0.0097 Bonf-2, replicates) + H2 register pre-commit-REVERSED (NULL) + normalisation-sensitive
author: Waiel Al-Shujaa
prereg_sha256: ea2d6fda596c17dbe82ff152c111895b0d273acc5f6a68dd591466cabc1db304
seed: 20260509
n_perm: 10000
---

# H-NEW-2390 — Clause-scale (within-verse) iltifāt detector


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the compression-tail is GENRE-SHARED and largely a unit-SIZE effect
>
> **The arithmetic reproduces exactly** — the QAC rebuild returns R² = 0.9860, β = −0.01237.
> What did not survive is the reading of the gradient as content architecture.
>
> 1. **A matched partition of ordinary Arabic prose reproduces it.** al-Jāḥiẓ's 200 cuts
>    average R² = **0.9686** and reach **0.9913**; al-Bukhārī's average 0.9577 and reach
>    0.9903. This corpus's 0.9887 sits at the **99th percentile** — high, and still inside the
>    band, with 1–5 of 200 arbitrary cuts exceeding it.
> 2. **Unit size alone explains 91.5 %.** Regressing the 100-window d̄ series on
>    **log(window mean word-count) and nothing else** — no position information whatever —
>    gives **R² = 0.9147** (r = +0.956). Adding size to the published kink model lifts it only
>    from 0.9887 to 0.9918.
> 3. **Equalise the sizes and it nearly vanishes.** Re-cutting this corpus's *own* verse
>    stream into 114 equal-verse blocks drops R² from **0.9887 to 0.3388** and flattens the
>    slope **nine-fold** (−0.01343 → −0.00151). Short surahs have sparse vectors that
>    Dirichlet smoothing pulls toward the prior, so d̄ falls because the surahs are short.
>
> The **rhyme** dispersion-tail sits at the **51st percentile** of ḥadīth and the 50.5th of
> adab prose — the middle of the distribution. The **phoneme** tail is at the 76.5th / 73rd
> and is edged by poetry. The **verse-length** tail is **REVERSED**, at the 31.5th / 32.5th
> percentile, and its words-per-verse arm is **degenerate by construction**.
>
> **What survives, at its true strength:** holding the size profile identical, this corpus's
> post-kink content-compression **slope** is steeper than **200/200** ḥadīth and **198/200**
> adab-prose partitions — a real residual content effect and the only axis in the whole sweep
> where this corpus leads. It is **genre-shared-but-larger**: a difference of degree on one
> axis of one law, not a discrimination.
>
> **Honest limit, for this law specifically:** arbitrary cuts *preserve* local continuity and
> make a contiguity-sensitive gradient *easier* for a baseline, so the baseline reproduction
> is the weaker of the three arguments. (2) and (3) involve no baseline at all.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Bottom line.** H-NEW-2200 mapped iltifāt at the **verse-boundary** scale and found the
Meccan>Medinan density direction **REVERSED** (p=0.66, region-NULL); it flagged that the
classically-foregrounded device lives at a *finer* scale. This finding builds that finer
detector: it scans the **ordered within-verse sequence** of finite-verb / pronoun
person-number states and flags every **clause-scale** shift. The result is a clean
**scale-of-aggregation reversal**: at the within-verse scale the pre-registered direction
**Meccan > Medinan HOLDS** (per-adjacency density 0.4602 vs 0.4227, Δ=+0.0375, p=0.0097,
passing Bonferroni-2; replicates at seed 20260510 p=0.0100 and under a verb-only stream
Δ=+0.048). **The finer detector recovers a region signal the coarse detector could not see.**
Two honest caveats carry equal prominence: (1) the **register** cell H2 (short-mufaṣṣal denser)
**REVERSED its locked sign** (short mufaṣṣal is *sparser*, p=1.0) — a pre-commit violation
published as NULL; the clause-scale hotspots are the *long narrative Meccan* surahs (Q20, Q11,
Q19, Q26), not the staccato short oath-surahs; and (2) the result is **normalisation-sensitive** —
under a per-verse (rather than per-adjacency) normalisation the region direction *reverses*
(Medinan saturates because its verses are long). The primary statistic was pre-locked as
per-adjacency, so H1 stands, but the sensitivity is reported in full.

---

## 1. What was tested and how it differs from H-NEW-2200

*Iltifāt* (الالتفات) — al-Zarkashī's "change of speech from one mode to another, for freshness
and variety" (*al-Burhān fī ʿulūm al-Qurʾān*, iltifāt *nawʿ*); Ibn al-Athīr's *shajāʿat
al-ʿarabiyya* (*al-Mathal al-Sāʾir*); al-Suyūṭī's parallel chapter in *al-Itqān*. Ground truth =
Abdel Haleem (1992 BSOAS 55(3):407–432;
`data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md`).

| | H-NEW-2200 (coarse) | **H-NEW-2390 (this, fine)** |
|:--|:--|:--|
| Unit | one **dominant** (modal) person+number per verse | **ordered sequence** of every state in the verse |
| Locus | change across verse **boundary** (v, v+1) | change between **adjacent states INSIDE** a verse |
| Sees Q 1:5 *iyyāka naʿbudu* 2↔1 alternation? | **No** (collapsed to one value) | **Yes** (3 within-verse shifts) |
| Sees Q 10:22 ship-storm mid-verse storm? | **No** | **Yes** (9 within-verse shifts) |
| Total loci | 3,278 boundaries | **16,998 within-verse shifts** in 4,515 verses |
| Region direction-locked test | NULL/REVERSED, p=0.66 | **HOLDS Meccan>Medinan, p=0.0097** |

**Detector (MW-1, locked).** Each QAC v0.4 segment that is a finite verb `POS:V` (incl.
imperatives `IMPV`, which carry an explicit 2nd-person feature) or a pronoun (independent
`POS:PRON` or suffix `PRON:<png>`) emits a person-number state `(p∈{1,2,3}, n∈{S,D,P})` via the
regex `^(?:PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$` (verbatim from H-NEW-2200 for instrument
continuity; `M*/F*→S/D/P`). States are ordered by (word, segment) index. A **within-verse shift**
is any adjacent pair differing in person OR number. Verses with <2 states are structurally
ineligible and excluded from the denominator.

Rules-tuple: `(no-tashkeel, QAC-v0.4-segment, finite-V[incl IMPV] + PRON person-number,
ordered within-verse sequence, adjacent-pair shift, Hafs-Kūfan, Mashriqī)`.

---

## 2. The clause-scale census (descriptive deliverable — COMPLETE)

| Quantity | Value |
|:--|--:|
| Eligible verses (≥2 states) | 5,463 |
| Within-verse adjacencies | 38,157 |
| **Total within-verse iltifāt shifts** | **16,998** |
| Verses carrying ≥1 within-verse shift | 4,515 |
| — person-shift instances | 12,379 |
| — number-shift instances | 11,584 |
| — both at one shift | 6,965 |

### Person-shift category census (within-verse, exhaustive)

| Category | Count | Classical type (Abdel Haleem) |
|:--|--:|:--|
| 3rd → 2nd (*ghayba → ḥuḍūr*) | 3,248 | Type 3 |
| 2nd → 3rd (*ḥuḍūr → ghayba*) | 3,223 | Type 4 |
| 1st → 3rd | 1,877 | Type 2 |
| 3rd → 1st | 1,817 | Type 1 |
| 1st → 2nd | 1,189 | Type 5 (classically "1 disputed verse") |
| 2nd → 1st | 1,025 | Type 6 (classically "does not occur") |

### Number-shift category census

| Category | Count |
|:--|--:|
| S → P | 5,856 |
| P → S | 5,353 |
| S→D / D→S / D→P / P→D | 375 combined |

> **Same interpretive caveat as H-NEW-2200.** This is a *grammatical-person* generator: a
> 3rd→2nd shift includes human-referent shifts (a disbeliever addressed), not only divine
> turns. It is a **superset generator** of canonical iltifāt, not a theologically-curated
> catalog. The near-symmetry of the directional counts (3↔2 ≈ 3248/3223; 1↔3 ≈ 1877/1817)
> reflects that most shifts are reversible alternations in running discourse. The classical
> tradition's "2nd→1st does not occur" claim refers to a *specific rhetorical turn*; at the raw
> grammatical-adjacency grain it of course occurs (1,025×) — the device the tradition names is
> a curated subset, exactly as al-Zarkashī's *li-iqtiḍāʾ al-ḥāl* ("when the situation
> necessitates") principle implies.

### "I ↔ We" divine-majesty subtype (within-verse)

**11 within-verse loci** where the person stays 1st while number flips S↔P — the *majestic
plural* iltifāt occurring *inside a single verse*: Q 9:75, 14:35, 14:37, 14:40, 18:63, 18:102,
18:109, 19:21, 28:28, 50:27, 70:40. Two verified by hand: **Q 19:21** (Gabriel: "*it is easy
for **Me** (1S)… and that **We** (1P najʿala) may make him a sign*"), **Q 50:27** (the
disbeliever's *qarīn*: "*Our Lord (1P), **I** (1S) did not make him transgress*"). These are the
finest-grain empirical correlates of the classical divine-I/We alternation, now localized below
the verse.

---

## 3. Instrument validation — recall vs Abdel Haleem (MW-6)

| Catalog category | Ground-truth verses | Clause-detector hits | **Clause recall** | (H-NEW-2200 boundary recall) |
|:--|--:|--:|--:|--:|
| Person iltifāt (types 1–4 union) | 157 | 118 | **75.2%** | 56.7% |
| Number iltifāt | 31 | 24 | **77.4%** | 61.3% |

The clause detector recovers **+18.5 pp / +16.1 pp** more of Abdel Haleem's catalog than the
boundary detector — direct confirmation that it sees the within-verse shifts the boundary scale
was blind to. Flagship loci (must fire within-verse):

| Locus | states | within-verse shifts | note |
|:--|--:|--:|:--|
| **Q 1:5** *iyyāka naʿbudu wa-iyyāka nastaʿīnu* | 4 | **3** | 2↔1 alternation, exactly the famous turn |
| **Q 10:22** ship-storm | 27 | **9** | 3MS→2MP→3FP(ships)→3MP→3FS→3MP→2MS/1P storm |
| **Q 27:60** *amman khalaqa…* | 14 | **6** | |
| **Q 36:22** disputed 1↔2 | 7 | **4** | |
| **Q 108:2** *fa-ṣalli li-rabbika* | 3 | **0** | correctly NULL — see §6 |

The Q 108:2 zero is **not a miss**: its iltifāt (1P→3rd, *aʿṭaynāka* → *rabbika*) is a
**boundary** shift between v.1 and v.2, which H-NEW-2200 catches and this detector by design does
not. The two scales are **complementary**, not competing (§6).

---

## 4. Pre-registered tests — H1 CONFIRMED (region), H2 REVERSED (register)

Surah-label-shuffle permutation null (surah = exchangeable unit; shifts and adjacencies move with
their surah), 10,000 perms, one-sided in the locked direction, Bonferroni k=2, α_bon=0.025.

### H1 (PRIMARY, region) — locked Meccan > Medinan — **HOLDS, PASSES**

| | shifts | adjacencies | per-adjacency density |
|:--|--:|--:|--:|
| Meccan | 10,665 | 23,174 | **0.4602** |
| Medinan | 6,333 | 14,983 | 0.4227 |

**Δ = +0.0375 (Meccan denser), p = 0.0097 < 0.025 → PASS in locked direction.**
- **MW-5 replication seed 20260510:** p = 0.0100 (stable).
- **MW-5 verb-only stream** (drop pronoun-only states): Meccan 0.5480 vs Medinan 0.5000,
  Δ = +0.0480, direction HELD.
- **The clause scale recovers the exact region direction the boundary scale reversed.**

### H2 (SECONDARY, register) — locked short-mufaṣṣal (s≥78) > rest — **REVERSED → NULL**

| | shifts | adjacencies | per-adjacency density |
|:--|--:|--:|--:|
| short mufaṣṣal (s≥78) | 193 | 632 | **0.3054** |
| rest (s<78) | 16,805 | 37,525 | 0.4478 |

**Δ = −0.1425 (short mufaṣṣal SPARSER), p = 1.0000. Direction REVERSED → pre-commit violation,
published NULL with full prominence (Protocol §1.8).** The locked rationale — that the
oath/eschatological short-mufaṣṣal register (qasam-enriched per H-NEW-2210, *idhā*-enriched per
H-NEW-2250) would carry the densest within-verse turns — is **FALSIFIED**. The short surahs have
very few states per verse, so they offer few within-verse adjacencies. The clause-scale iltifāt
**hotspots are the long narrative Meccan surahs** (§5), not the short oath-surahs. The
rhetorical intensity of the short mufaṣṣal lives in its *cadence and oath-stacking* (H-NEW-2210/
2240/2250), not in within-verse person-churn.

---

## 5. Where the within-verse iltifāt actually concentrates

Densest surahs (clause scale, ≥20 within-verse adjacencies):

| Surah | type | D_adj | shifts/adjs |
|:--|:--|--:|:--|
| Q 82 al-Infiṭār | meccan | 0.600 | 12/20 |
| Q 38 Ṣād | meccan | 0.573 | 169/295 |
| **Q 20 Ṭā-Hā** | meccan | 0.549 | 400/729 |
| **Q 19 Maryam** | meccan | 0.539 | 233/432 |
| Q 15 al-Ḥijr | meccan | 0.536 | 165/308 |
| **Q 11 Hūd** | meccan | 0.531 | 535/1008 |
| Q 14 Ibrāhīm | meccan | 0.521 | 211/405 |
| Q 17 al-Isrāʾ | meccan | 0.510 | 400/785 |
| Q 43 al-Zukhruf | meccan | 0.501 | 224/447 |
| **Q 26 al-Shuʿarāʾ** | meccan | 0.500 | 301/602 |
| Q 34 Sabaʾ | meccan | 0.496 | 212/427 |
| Q 47 Muḥammad | medinan | 0.495 | 152/307 |

Eleven of the top twelve are **Meccan**, and the dense ones are the **prophet-narrative**
surahs (Ṭā-Hā, Maryam, Hūd, al-Shuʿarāʾ, al-Ḥijr, Ṣād) — precisely the register where Abdel
Haleem and al-Zarkashī locate iltifāt's dramatic vividness (multiple speakers, dialogue,
divine-voice turns within a single verse). This is *why* H1 holds at the clause scale and H2
(short-mufaṣṣal) reverses: the driver is **narrative dynamism**, which correlates with Meccan
register but lives in the *long* narrative surahs, not the short oath ones.

---

## 6. The scale-of-aggregation result (the headline)

| Scale | Meccan dens. | Medinan dens. | Δ | p | direction |
|:--|--:|--:|--:|--:|:--|
| **Verse boundary (H-NEW-2200)** | 0.5317 | 0.5461 | −0.0144 | 0.66 | **REVERSED → NULL** |
| **Within-verse / clause (H-NEW-2390)** | 0.4602 | 0.4227 | +0.0375 | **0.0097** | **HOLDS → PASS** |

This is a textbook **cross-finding-025 scale-of-aggregation flip**: the *same* pre-registered
direction (Meccan>Medinan iltifāt density) is NULL at the surah-boundary aggregation and
significant at the within-verse aggregation. The classical balāgha tradition foregrounds iltifāt
as a *within-clause* device; measuring it at the *boundary* container washed the genre signal out
(it became length-driven). Dropping to the clause scale recovers the genre signal — vindicating
H-NEW-2200's own diagnosis (§7-8) that "iltifāt lives at the within-verse/clause scale, finer than
that detector." The two detectors are **complementary**: Q 108:2 is a boundary iltifāt only
(caught by 2200, not 2390); Q 1:5 and Q 10:22 are within-verse iltifāt (caught by 2390, invisible
to 2200). A full iltifāt map needs both scales.

---

## 7. Honest limits (equal prominence)

1. **H2 register pre-commit violation.** The locked short-mufaṣṣal>rest direction REVERSED hard
   (p=1.0). This is a genuine NULL, published with full prominence — the dramatic register is
   *narrative-Meccan*, not *short-oath-Meccan*, at the within-verse grain. The Bonferroni-2
   family is thus 1 PASS / 1 REVERSED.
2. **Normalisation sensitivity (reported, not hidden).** H1 holds under the **pre-locked
   per-adjacency** statistic (Δ=+0.0375) and under verb-only (Δ=+0.048), but the **per-verse**
   normalisation REVERSES (Meccan 0.816 < Medinan 0.853, Δ=−0.037). Mechanism: Medinan verses are
   long enough that ~85% carry at least one shift (saturation of the per-verse indicator), while
   Meccan verses shift more *per opportunity*. The primary statistic was pre-registered as
   per-adjacency precisely to be the apples-to-apples twin of 2200's per-boundary density, so H1
   stands — but the conclusion is "Meccan verses iltifāt-churn more *frequently per state-pair*,"
   NOT "more Meccan verses contain iltifāt." A reader who prefers the per-verse framing should
   treat the region effect as DIRECTIONALLY AMBIGUOUS.
3. **Superset generator.** 16,998 raw grammatical-adjacency shifts ≫ the ~320–370
   theologically-curated classical loci; the census counts human-referent alternations too (§2
   caveat). Recall (75%/77%) is the validation metric; precision against Abdel Haleem is not
   scoreable (his catalog is explicitly non-exhaustive).
4. **Clause ≠ syntactic clause.** "Within-verse adjacency" is a sequence of person-bearing
   *tokens*, not a parsed clause boundary; a shift between two tokens in the same clause and a
   shift across a clause boundary are counted identically. A QAC-syntax-aware refinement
   (clause-node boundaries) is queued as H-NEW-2390.1.
5. **MW-7.** The §5 "narrative-Meccan hotspot" reading and the per-verse/per-adjacency mechanism
   were noticed during analysis; they are reported descriptively, carrying no significance claim
   beyond the two pre-locked p-values.

---

## 8. Verdict

| Component | Verdict |
|:--|:--|
| Within-verse census (16,998 shifts, all categories) | **COMPLETE** (first within-verse iltifāt map) |
| H1 region Meccan > Medinan (per-adjacency, primary) | **CONFIRMED** (Δ=+0.0375, p=0.0097, Bonf-2; seed2 + verb-only replicate) |
| H2 register short-mufaṣṣal > rest | **NULL** (pre-commit direction reversed, p=1.0) |
| H1 under per-verse normalisation | REVERSED — finding is normalisation-sensitive (§7.2) |
| Detector validation | recall **75.2% person / 77.4% number** vs Abdel Haleem (+18/+16 pp over boundary) |
| Scale-of-aggregation vs H-NEW-2200 | **FLIP** — region-NULL at boundary, region-PASS at clause |

**Headline:** the within-verse iltifāt detector **recovers the Meccan>Medinan genre signal that
the verse-boundary detector reversed/nulled** — a clean scale-of-aggregation flip vindicating the
classical placement of iltifāt at the clause grain. The recovery is real on the pre-locked
per-adjacency statistic (replicated), driven by the **long narrative Meccan surahs**; it is
normalisation-sensitive and does NOT extend to the short-mufaṣṣal register (locked H2 reversed,
NULL). The clause and boundary detectors are complementary scales of one device.

---

## 9. Cross-references

- **H-NEW-2200** (`h-new-2200-iltifat-corpus-map.md`) — the coarse boundary detector this finding
  was built to refine; it explicitly called for a within-verse detector and predicted the region
  signal would live below the verse. **This finding confirms that prediction.**
- **cross-finding-025-formal (scale-of-aggregation)** — direct new data point: the SAME locked
  direction flips from NULL (boundary) to PASS (clause). Iltifāt joins the project's family of
  effects that are scale-dependent.
- **Abdel Haleem 1992** + **al-Zarkashī *al-Burhān*** (iltifāt nawʿ) + **al-Suyūṭī *al-Itqān***
  (Q 36:22 disputed 1→2) + **Ibn al-Athīr *al-Mathal al-Sāʾir*** (*shajāʿat al-ʿarabiyya*) —
  classical anchoring; the within-verse hotspots (§5) are exactly the narrative surahs the
  tradition cites.
- **H-NEW-2210 (qasam)**, **H-NEW-2250 (*idhā* cascade)**, **H-NEW-2240 (fāṣila)** — the
  short-mufaṣṣal register IS rhetorically dense, but in oath/cadence/cascade structure, NOT in
  within-verse person-churn (explains the H2 reversal). The registers carry *different* rhetorical
  intensities.
- **H-NEW-660 compression-tail / s=50 kink** — length gradient; here the length confound is
  *controlled out* by the per-adjacency normalisation, isolating a genuine register effect that
  survives length (unlike 2200's boundary density, which was length-driven).

## 10. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2390-clause-iltifat.md` (SHA-256 `ea2d6fda596c17dbe82ff152c111895b0d273acc5f6a68dd591466cabc1db304`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2390.py` (runtime SHA-verified)
- JSON (full within-verse locus map + per-surah + I↔We list + flagship + 2200 comparison): `findings/phase-b-hypotheses/csv/h-new-2390.json`
- finding: this file

*H-NEW-2390 logged 2026-05-29 by Waiel Al-Shujaa. The finer detector recovered the signal the
coarse one missed; the register sub-hypothesis honestly reversed. Bismillāhi al-Raḥmāni al-Raḥīm.*
