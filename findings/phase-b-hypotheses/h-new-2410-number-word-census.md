---
finding_id: H-NEW-2410
title: Explicit number-word census + counted-referent distribution
type: census + locked-test
author: Waiel Al-Shujaa
date: 2026-05-29
phase: B
seed: 20260509
n_perm: 10000
prereg_sha256: 1fdf55d1c8193dc299f87ceac66342482e44106f210689bd741329a7ebb3191f
verdict: CENSUS DELIVERED · Test A NULL (modal-but-not-beyond-base-rate) · Test B PRE-COMMIT VIOLATION (reversed → published NULL)
---

# H-NEW-2410 — Explicit number-word census + counted-referent distribution


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

> **This is a CENSUS, not numerology.** No miracle-claim is made. The
> iʿjāz ʿadadī / balanced-words programme is RETIRED on this project (ledger
> §10.79–§10.80; al-Khalifa §10.55/§10.60; H-META-1). The single-lexeme counts
> below are *facts*; the only inferential claims are the two pre-locked tests,
> both of which came back honestly negative. Any number that "looks special"
> (seven, nineteen, forty) is reported **CONFIRMED-BUT-MEANINGLESS** unless it
> beats its permutation null — and neither did.

Pre-reg SHA-256 `1fdf55d1c8193dc299f87ceac66342482e44106f210689bd741329a7ebb3191f`,
runtime-verified. Source morphology: `data/morphology/quranic-corpus-morphology-0.4.txt`
(QAC v0.4). Rules-tuple: `(QAC-lemma+root+POS, word-token, basmala-Q1-only, Hafs-Kufan, Mashriqi)`.

## 1. Methodological core: QAC has NO number POS — lemma disambiguation is everything

QAC v0.4 carries **no** cardinal/ordinal/number POS tag (verified: the only POS
values are N, V, P, PN, REL, … with N=25,136 and ADJ=1,961). Every number-word is
tagged `POS:N` (most) or `POS:ADJ` (a few), and must be identified by **root +
lemma**. Buckwalter roots are polysemous, so this census lives or dies on
homograph control — the same close-reading lesson as §10.80 (*kallā* homograph)
and §10.82 (hapax-at-form ≠ hapax-at-root). The locked exclusions:

| Buckwalter root | NUMBER sense (counted) | HOMOGRAPH sense (EXCLUDED) |
|:--|:--|:--|
| **`Esr` vs `E$r`** | ten = **`E$r`** (ʿ-sh-r): ʿashr/ʿashara | hardship = **`Esr`** (ʿ-s-r): ʿusr/ʿusra/al-ʿusrā (Q2:280, 9:117, 18:73, 65:7, 92:10, 94:5-6) — *not* a number |
| `vmn` | eight = thamāniya/thamānī; 1/8 = thumun | **thaman "price"** (Q2:41, 2:79, 3:77 …) — excluded |
| `Alf` | thousand = alf | **īlāf "covenant"** (Q106:1-2); **muʾallafa "reconciled"** (Q9:60); **allafa "He united"** (Q3:103) — excluded |
| `wHd` | one = wāḥid/wāḥida | **waḥīd "alone"** (Q74:11), **waḥda- "by itself"** — reported as isolation-sense, not cardinal |
| `vny` | two = ithnān; second = thānī | **al-mathānī "the oft-repeated"** (Q15:87, 39:23) — reported separately from distributive mathnā |
| `E$r` | ten / twenty | maʿshar "company", ʿashīra "kin", ʿishār "she-camels", ʿāsharū "consort" — excluded |
| `Awl` | first = **`>aw~al` only** | ūlū "possessors", āl "family", taʾwīl "interpretation" — excluded |

Had `Esr` been merged into "ten" (a natural-looking mistake), the count would have
been inflated by 8 hardship-tokens — the exact garden-of-forking-paths that
manufactures spurious "miracles." The census is built to forbid it.

## 2. THE CENSUS (descriptive-primary — facts, no verdict)

### 2a. Cardinals — totals by value (213 tokens)

| Value | Count | Value | Count | Value | Count |
|:-:|:-:|:-:|:-:|:-:|:-:|
| 1 | 61 | 7 | **26** | 50 | 2 |
| 2 | 20 | 8 | 5 | 60 | 1 |
| 3 | 22 | 9 | 7 | 70 | 1 |
| 4 | 14 | 10 | 14 | 80 | 1 |
| 5 | 3 | 20 | 1 | 100 | 10 |
| 6 | 7 | 40 | 4 | 1000 | 14 |

- **One (61)** and **seven (26)** are the two most frequent cardinals. One = wāḥid
  is mostly theological (*ilāh wāḥid* "one God") — see §2d. Seven leads the
  multi-unit cardinals.
- The tens (20/30/40/50/60/70/80) are sparse and largely narrative (forty = Mūsā's
  40 nights / 40 years wandering, Q2:51, 5:26, 7:142, 46:15; seventy = Q69:32 the
  70-cubit chain; eighty = Q24:4 the 80 lashes for *qadhf*).
- Note: **30 (thalāthīn) is attested 0× as a standalone tens-form** in the
  whitelist scan — Mūsā's "thirty nights" Q7:142 uses `thalāthīn` which QAC stores
  under the base lemma; the script's tens-by-form rule captured only the
  arbaʿīn/sabʿūn cases, so thirty is folded under the value-3 cardinal head-count.
  Documented as a known counting-rule edge (see §6 limits).

### 2b. Ordinals (93 tokens — but awwal dominates and is mostly non-sequential)

| Ordinal | Count | Ordinal | Count |
|:--|:-:|:--|:-:|
| 1st (awwal) | **82** | 5th (khāmisa) | 2 |
| 2nd (thānī) | 2 | 6th (sādis) | 2 |
| 3rd (thālith) | 2 | 8th (thāmin) | 1 |
| 4th (rābiʿ) | 2 | | |

**HONEST FLAG**: the 82 *awwal* tokens are overwhelmingly the **adjectival
"first/foremost/former"** sense, NOT a sequential count — e.g. *awwal kāfir bihi*
"the first to disbelieve in it" (Q2:41), *awwal al-muslimīn* "the first of those
who submit" (Q6:163), *al-awwalūn / al-ūlā* "the ancients / former peoples"
(Q56:49, 20:51). The genuine *sequential* ordinals (2nd-8th) total only **11**,
and they cluster in two famous enumerations: **Q18:22** (the Sleepers debate —
"...the fourth of them their dog... the sixth of them... the eighth of them their
dog") and **Q58:7** (the secret-counsel verse — "no three but He is their fourth,
nor five but He is their sixth"). These two pericopes carry the ordinal sequence
of the entire Quran.

### 2c. Fractions (21 tokens — the inheritance apparatus)

| Fraction | Count | Fraction | Count |
|:--|:-:|:--|:-:|
| 1/2 (niṣf) | 7 | 1/5 (khumus) | 1 |
| 1/3 (thuluth) | 6 | 1/8 (thumun) | 1 |
| 1/6 (sudus) | 3 | 1/10 (miʿshār) | 1 |
| 1/4 (rubuʿ) | 2 | | |

Fractions are the *farāʾiḍ* (inheritance-share) lexicon: niṣf/thuluth/rubuʿ/
sudus/thumun cluster in **Q4:11-12 + Q4:176** (the inheritance verses). khumus =
the one-fifth war-spoil share (Q8:41); miʿshār = "a tenth" (Q34:45).

### 2d. Counted-referent distribution (the "what is being counted" map)

The immediate syntactic head (next content word) of each cardinal:

| Cardinal | Top counted noun(s) (root → count) |
|:--|:--|
| **7** | **smw heaven 5** · snbl ear-of-grain 3 · bqr cow 2 · ʿijāf lean(-cows) 2 · shadīd severe 2 |
| **6** | **ywm day 7** (the six days of creation, exclusively) |
| **1000** | **snw year 5** (alf sana "a thousand years") · malak angel 3 |
| **3** | ywm day 4 · layl night 2 · shahr month 2 |
| **4** | shahīd witness 4 · shahr month 3 (the 4 sacred months / 4 witnesses) |
| **2** | ʿashar (→twelve) 5 · ilāh/dhikr/ahl 2 each |
| **100** | ʿām year 2 · alf →(100k) 2 |
| **10** | ʿayn spring 2 (the 12 springs context) |

**Global most-counted referents** (across all cardinals): `ywm` day **13** ·
`snw` year 7 · `shahr` month 7 · `Alh` Allāh 6 · `smw` heaven 5. Time-units
(day/year/month/night) dominate what the Quran counts; "seven heavens" is the
single most fixed *number+noun* bond but is out-ranked in aggregate by counted
*time*.

### 2e. Excluded-but-documented (integrity ledger)

- **zawj "pair/spouse" (root zwj): 81 tokens** — a collective noun, deliberately
  NOT counted as a cardinal (it does not denote a quantity, it denotes a kind).
- **isolation-sense `wHd`: 7 tokens** (waḥīd/waḥda-) — "alone", not "one".
- **al-mathānī (oft-repeated): 2 tokens** (Q15:87, 39:23) — descriptor, not a count.
- **distributive mathnā** (Q4:3, 35:1) — "two-by-two", reported separately.

## 3. THE TWO LOCKED INFERENTIAL TESTS — both honest negatives

### Test A — "seven collocates with heavens beyond base-rate": NULL

| Quantity | Value |
|:--|:--|
| sabʿ attestations with determinable head | 25 |
| modal head-noun | **smw (heaven) = 5** — argmax ✓ |
| 2nd–4th | sunbula (ear) 3 · baqara/ʿijāf 2 each |
| null p95 of max-collocate | 5 |
| permutation p (smw ≥ obs under all-cardinal head-bag) | **0.0825** |
| **Direction (smw is the mode)** | **CONFIRMED** |
| **Beyond base-rate** | **FAILED** (p > 0.025) |

The pre-registered direction holds — *sabʿ samāwāt* "seven heavens" **is** the
single most frequent number+noun bond, and it is sabʿ's modal head (Q2:29, 41:12,
65:12, 67:3, 71:15). **But it does not beat the base-rate null**: a count of 5
top-collocate hits is reached by chance in 8.25% of permutations that simply draw
from the corpus-wide head-noun frequencies. Verdict: **CONFIRMED-as-modal-BUT-
NOT-beyond-base-rate.** Seven's bond to "heavens" is real and is the Quran's
tightest numeral collocation, yet it is statistically consistent with samāʾ
simply being a frequent count-target — exactly the CONFIRMED-BUT-MEANINGLESS
discipline the pre-reg demanded. (The small N=25 of sabʿ-heads limits power; this
is a power-limited null, not a strong refutation of the collocation's salience.)

### Test B — "number-density is higher in Medinan/legal surahs": PRE-COMMIT VIOLATION → NULL

| Quantity | Value |
|:--|:--|
| mean density Meccan (per 1000 words) | **4.556** |
| mean density Medinan (per 1000 words) | **2.500** |
| Δ (Medinan − Meccan), locked direction > 0 | **−2.056** |
| permutation p (locked direction) | 0.962 |
| variant: per-1000-root-token Δ | **−3.106** (also reversed) |
| **Verdict** | **DIRECTION REVERSED — pre-commit violation, published NULL** |

The locked prediction (Medinan inheritance-fractions + ʿidda + witness-counts
make numbers denser in Medina) is **flatly reversed**: number-word density is
**~1.8× higher in Meccan surahs**, and the reversal is robust across both
normalizations (per-word and per-root-token). Per Protocol §1.8 this is published
as NULL with full prominence — no massaging, no silent pre-reg edit.

**Why it reverses (diagnostic, not a new claim):** the densest number-surahs are
all short Meccan ones — Q97 al-Qadr (33.3/1000: *alf shahr* "a thousand months"),
Q93 al-Ḍuḥā, Q69 al-Ḥāqqa (six tokens incl. the 70-cubit chain), Q73 al-Muzzammil
(*niṣf al-layl*), Q56 al-Wāqiʿa. Meccan eschatology/cosmology counts heavily
(seven heavens, six days, thousand years, the *tisʿata ʿashar* 19 angels of
Q74:30, forty nights), while the Medinan legal fraction-cluster is concentrated in
just a few long surahs (Q4, Q2, Q8) and is diluted per-1000-words. **Numbers are
NOT a Medinan-legal signature.** This exactly parallels the H-NEW-2200 iltifāt
NULL (§10.86): a register feature presumed Medinan/legal turns out
register-independent and length/genre-mediated.

## 4. What the census actually shows (honest synthesis)

1. **The Quran counts time, then cosmos.** The most-counted referents are
   day/year/month/night (aggregate 31 cardinal heads), then heaven (5). The
   famous *sabʿ samāwāt* is the tightest single bond but not the densest theme.
2. **Seven is the lead multi-unit cardinal (26×)** and its modal noun is heaven —
   a real, classically-noted collocation (the *sabʿ samāwāt ṭibāqan* formula) —
   but it is **statistically within base-rate** (p=0.08). Reported as
   CONFIRMED-BUT-MEANINGLESS per pre-reg.
3. **Sequential ordinals barely exist (11 tokens)** outside Q18:22 (Sleepers) and
   Q58:7 (secret-counsel); "first" (awwal, 82×) is an adjective of priority, not a
   counter.
4. **Fractions ARE the legal apparatus** — but they are too few (21) and too
   surah-concentrated to lift Medinan density; numbers overall are a **Meccan**
   density signal, reversing the intuitive legal-Medinan prior.
5. **No symmetry, no miracle claimed or found.** This is a clean factual map of
   what number-words exist and what they modify.

## 5. Classical anchoring

- The "seven heavens in layers" (*sabʿ samāwāt ṭibāqan*) is a fixed Quranic
  formula noted across tafsīr (Q67:3, 71:15); the census confirms it is the
  empirical modal numeral collocation, while declining to inflate it into a
  statistical "sign" (al-Khaṭṭābī's caution against forcing ʿadad into iʿjāz).
- The inheritance fractions map onto the classical *ʿilm al-farāʾiḍ* — niṣf/
  thuluth/rubuʿ/sudus/thumun are exactly the Qurʾānic *furūḍ muqaddara*, all in
  Q4:11-12, 176 + Q8:41 khumus, as the census head-distribution shows.
- The reversal away from a "Medinan-legal number density" is consistent with the
  project's standing result that genre/length, not Meccan/Medinan label, drives
  most surface-feature densities (H-NEW-2200 iltifāt; H-NEW-770 verse-length).

## 6. Honest limits

- **Head-noun heuristic**: "immediate next content word (N/PN/ADJ)" approximates
  but does not equal the true syntactic *mawṣūf/maʿdūd*; idāfa and adjective
  insertion can displace the true counted noun (the script also scans w+2 to
  mitigate). A full dependency parse would refine ~10% of heads.
- **"Thirty" edge**: thalāthīn (Q7:142) folds under the value-3 head-count rather
  than a standalone tens-cell (the tens-by-form rule covered only arbaʿīn/sabʿūn);
  this is a known counting-rule boundary, declared, not hidden.
- **Test A is power-limited** (N=25 sabʿ-heads); the NULL is "not beyond
  base-rate," not "no collocation." A larger numeral-collocation family would be
  needed to test salience with power.
- **awwal polysemy**: included in the ordinal class for completeness but flagged;
  excluding it would leave 11 sequential ordinals.
- QAC v0.4 only; a re-run on a dependency-annotated corpus could sharpen heads.

## 7. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2410-number-word-census.md`
  (SHA `1fdf55d1c8193dc299f87ceac66342482e44106f210689bd741329a7ebb3191f`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2410.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2410.json`
- finding: this file

## 8. Cross-references

- §10.79/§10.80 (H-NEW-2000/2010/2020) — balanced-words RETIRED; this census is
  the *non-numerological* complement: it maps number-words without any symmetry claim.
- §10.82 (H-NEW-2320 hapax) / §10.80 (kallā) — same homograph/counting-rule lesson
  (Esr-hardship vs E$r-ten; awwal-adjective vs ordinal).
- §10.86 (H-NEW-2200 iltifāt) — parallel register-independence NULL (Test B
  reversal echoes the iltifāt length-not-region result).
- H-META-1 — modern-numerology 0% confirmation; this census makes 0 such claims.

*H-NEW-2410 logged 2026-05-29 by Waiel Al-Shujaa. The number-words are real; no
symmetry is claimed; both locked tests came back honest. Census, not numerology.
Bismillāhi al-Raḥmāni al-Raḥīm.*
