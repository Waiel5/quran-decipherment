---
finding_id: H-NEW-2410
title: Explicit number-word census + counted-referent distribution (CENSUS, not numerology)
type: pre-registration
author: Waiel Al-Shujaa
date_locked: 2026-05-29
seed: 20260509
n_perm: 10000
phase: B
status: LOCKED-BEFORE-COMPUTATION
---

# H-NEW-2410 — Pre-registration: Explicit number-word census + referent distribution

## 0. What this is and is NOT

**This is a CENSUS.** A clean, descriptive-primary inventory of every explicit
cardinal/ordinal/fractional **number-WORD** in the Quran corpus, identified by
QAC v0.4 lemma + root + POS, together with — where determinable from the
immediate syntactic head — the **counted noun** (e.g. *sabʿ samāwāt* "seven
heavens", *sabʿ sanābil* "seven ears of grain", *arbaʿīn layla* "forty nights").

**This is NOT numerology.** No miracle-claim is made or implied. The
iʿjāz ʿadadī / "balanced-words" programme is RETIRED on this project
(MASTER-FINDINGS-LEDGER §10.79–§10.80, §10.55/§10.60 al-Khalifa, H-META-1):
the standing finding is that *single-lexeme corpus counts are real, claimed
symmetries are not*. This census **deliberately makes no symmetry claim**. Any
number that appears "special" (e.g. seven, nineteen) is reported as
**CONFIRMED-BUT-MEANINGLESS** unless it beats a proper permutation null on the
single pre-locked distributional test below. The census frequency table is the
deliverable; the one locked test is the only inferential claim.

This descriptive/inferential split is the same discipline used by H-NEW-2010/2020
(generators) + H-NEW-2000 (per-claim audit): the counts are facts; only the
pre-locked test carries a verdict.

## 1. Rules-tuple (default project tuple, with explicit deviations)

`(no-tashkeel-equivalent via QAC, QAC-lemma+root+POS token, words, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

- **Text/morphology source**: `data/morphology/quranic-corpus-morphology-0.4.txt`
  (QAC v0.4). QAC has NO dedicated cardinal/ordinal POS in v0.4 — number-words
  are tagged `POS:N` (most) or `POS:ADJ` (a few) and must be identified by
  **lemma + root**. This is the central methodological hazard and is handled in §2.
- **Counting unit**: an *attestation* = one QAC word-token whose stem segment
  carries a number-lemma. Segment-level prefixes/suffixes (wa-, bi-, -hā) do not
  create extra attestations.
- **Region map** (for the Medinan/Meccan test): `s["type"]` in
  `quran-text/quran-no-tashkeel.json` ("meccan"/"medinan").

## 2. The number-lemma whitelist (LOCKED) and the homograph exclusions

QAC Buckwalter roots are polysemous; classical close-reading discipline
(§10.80 *kallā* homograph lesson; §10.82 hapax-at-form≠hapax-at-root lesson)
requires lemma-level disambiguation. The following whitelist is **LOCKED**.
A token counts as a number-word **iff** its (root, lemma) pair is in this table.

### 2a. CARDINALS

| Value | Root (BW) | Lemma(s) (BW) | Gloss |
|:--|:--|:--|:--|
| 1 | wHd | `wa`Hid`, `wa`Hidap` | wāḥid / wāḥida |
| 2 | vny | `{vonayon`, `{vonatayon` | ithnān / ithnatān |
| 2 (distributive) | vny | `mavonaY`` | mathnā ("two by two") |
| 3 | vlv | `vala`v`, `vala`vap`, `v~aAlivap` | thalāth / thalātha |
| 4 | rbE | `>arobaE`, `>arobaEap`, `ruba`E` | arbaʿ / arbaʿa / rubāʿ |
| 5 | xms | `xamosap`, `xamos` | khamsa |
| 6 | stt | `sit~ap` | sitta |
| 7 | sbE | `saboE`, `saboEap` | sabʿ / sabʿa |
| 8 | vmn | `vama`niyap`, `vama`niY` | thamāniya / thamānī |
| 9 | tsE | `tisoE`, `tisoEap` | tisʿ / tisʿa |
| 10 | E$r | `Ea$or`, `Ea$orap`, `Ea$ar` | ʿashr / ʿashara / ʿashar |
| 100 | mAy | `miA}ap` | miʾa (incl. dual miʾatayn) |
| 1000 | Alf | `>alof` | alf (incl. dual alfayn, pl. ulūf/ālāf) |
| 20 | E$r | `Ei$oruwn` | ʿishrūn |
| 30/40/50/80/70/60 | rbE,xms,vmn,sbE,stt | `>arobaE`(40 via -īn), `xamosiyn`(50), `vama`niyn`(80), `saboE`(70 via -ūn), `sit~iyn`(60) | tens via sound-plural suffix |

Note: QAC stores 40 and 70 under the base cardinal lemma (`>arobaE`,`saboE`)
with the dual/plural suffix in the FORM (`>arobaEiyna`,`saboEuwna`); the script
detects the tens by FORM suffix `-iyn`/`-uwn` on these number-lemmas and reports
them in a dedicated "tens" sub-table. 30 (`vala`viyn`) is searched the same way.

### 2b. ORDINALS

| Ordinal | Root | Lemma | Gloss |
|:--|:--|:--|:--|
| 1st | Awl | `>aw~al` ONLY | awwal (NOT `>uwliY` ūlū "possessors", NOT `'aAl` āl "family", NOT `ta>owiyl`) |
| 2nd | vny | `vaAniY` | thānī |
| 3rd | vlv | `vaAliv` | thālith |
| 4th | rbE | `raAbiE` | rābiʿ |
| 5th | xms | `xa`misap` | khāmisa |
| 6th | sds | `saAdis` | sādis |
| 8th | vmn | `vaAmin` | thāmin |

### 2c. FRACTIONS

| Fraction | Root | Lemma | Gloss |
|:--|:--|:--|:--|
| 1/2 | nSf | `niSof` | niṣf |
| 1/3 | vlv | `v~uluv` | thuluth |
| 1/4 | rbE | `r~ubuE` | rubuʿ |
| 1/5 | xms | `xumus` | khumus |
| 1/6 | sds | `s~udus` | sudus |
| 1/8 | vmn | `v~umun` | thumun |
| 1/10 | E$r | `miEo$aAr` | miʿshār ("a tenth") |

### 2d. EXPLICIT HOMOGRAPH EXCLUSIONS (the close-reading guardrails)

The following share a Buckwalter root with a number but are **NOT** number-words
and are EXCLUDED by lemma. Documenting them is the integrity core of this census.

| Excluded lemma | Root | Why excluded |
|:--|:--|:--|
| `Eusor`,`Eusorap`,`EusoraY`` | **Esr** (ʿ-s-r) | = ʿusr / ʿusra / al-ʿusrā "hardship, difficulty" (Q2:280, 9:117, 18:73, 65:7, 92:10, 94:5-6). The Arabic root is ʿ-s-r (difficulty), spelled `Esr`; the NUMBER ten is ʿ-sh-r, spelled `E$r`. Distinct roots, must not be merged. |
| `Easiyr`,`Easir` | Esr | = ʿasīr "difficult" (Q25:26, 54:8, 74:9). |
| `vaman` | vmn | = thaman "price" (Q2:41, 2:79, …) — NOT thumun/thamāniya. |
| `<ila`f` | Alf | = īlāf "covenant/security" (Q106:1-2) — NOT alf "thousand". |
| `mu&al~afap`, `>al~afa` | Alf | = "those reconciled" (Q9:60), "He united" (Q3:103) — NOT thousand. |
| `waHiyd`, `waHod` | wHd | = waḥīd "alone" (Q74:11) / waḥda- "by himself" (isolation sense). Reported in a separate "isolation-sense" line; NOT counted as cardinal "one". |
| `zawoj`, `zuw~ijato` | zwj | = zawj "pair/spouse/kind" — a collective noun, not a counting cardinal; reported separately, NOT in the cardinal table. |
| `m~avaAniY` | vny | = al-mathānī "the oft-repeated (verses/pairs)" (Q15:87, 39:23) — descriptor, reported separately from the distributive mathnā. |
| `maEo$ar` | E$r | = maʿshar "company/assembly". |
| `Ea$iyrat`,`Ea$iyr`,`Ei$aAr` | E$r | = ʿashīra "kin", ʿashīr "associate", ʿishār "pregnant she-camels". |
| `EaA$iru` | E$r | = ʿāshirū "consort with" (verb, Q4:19). |
| `mavonaY`` at non-distributive sites | — | retained as distributive cardinal where it heads a count (Q4:3 mathnā wa-thulātha wa-rubāʿ); reported in a flagged sub-line. |

## 3. Output of the census (descriptive-primary, no verdict)

1. Full frequency table: every number-lemma, value, count, list of surahs.
2. Cardinal totals by value (1,2,3,…,10,20,…,100,1000).
3. The counted-noun (immediate syntactic head = next content word) distribution
   for each cardinal, and the global "most-counted referents" ranking.
4. Ordinal and fraction sub-tables.
5. Per-surah number-word density (number-tokens / total word-tokens).

## 4. THE ONE LOCKED INFERENTIAL TEST

**Two pre-locked claims, direction LOCKED. Bonferroni k=2, α_corrected = 0.025.**

### Test A — collocation (DIRECTION LOCKED)
> **Claim A**: Among all cardinal *sabʿ* (7) attestations whose immediate
> syntactic head (next content word) is determinable, the single most frequent
> counted noun is **samāwāt / samāʾ** (root `smw`, "heaven(s)"), and it is the
> MODE of the head-noun distribution.

- Direction: `smw` is the argmax of the sabʿ-head-noun frequency table.
- Null: under 10000 random reassignments of sabʿ's observed head-nouns drawn
  (with replacement preserving the empirical head-noun multiset of ALL cardinals)
  to the sabʿ slots, how often does `smw` (or any single noun) reach the observed
  sabʿ-smw count? **PASS** iff observed sabʿ-smw count > 95th percentile of the
  null max-collocate count AND `smw` is the empirical argmax. This controls for
  "samāʾ is just a frequent head-noun overall."
- This is descriptive-confirmatory: it tests whether seven's bond to "heavens"
  exceeds what corpus-wide head-noun base-rates predict.

### Test B — register density (DIRECTION LOCKED)
> **Claim B**: Number-word density (number-tokens per 1000 word-tokens) is
> **higher in Medinan surahs than Meccan surahs**, driven by legal apparatus
> (inheritance fractions niṣf/thuluth/…, ʿidda waiting-periods, witness counts).

- Direction: mean_density(Medinan) > mean_density(Meccan).
- Null: 10000 label-permutations of the Meccan/Medinan tag across the 114 surahs;
  p = fraction of permutations with Δ ≥ observed Δ (one-sided, locked direction).
- **PASS** iff observed Δ > 0 AND permutation p < 0.025 (Bonferroni).
- **Reversed direction** (Meccan > Medinan, significant) = PRE-COMMIT VIOLATION,
  published as NULL with full prominence per Protocol §1.8.

### Failure handling
- If A fails: report sabʿ's true modal collocate honestly; "seven heavens" is
  then CONFIRMED-as-frequent-BUT-NOT-beyond-base-rate.
- If B fails or reverses: numbers are register-independent (parallels the
  H-NEW-2200 iltifāt NULL — apparatus-density is a length artifact, not a
  Medinan signature). Publish as NULL.

## 5. MW protections
- MW-1: metric (head-noun = next stem-bearing content word; density = tokens/1000)
  fixed here, pre-computation.
- MW-2: 10000-perm permutation nulls.
- MW-3: Test B reported under both raw word-count density and root-bearing-token
  density (2 model variants) — direction must hold in primary (per-1000-word).
- MW-6: Test A null uses the empirical head-noun multiset of ALL cardinals as the
  control bag (instrument-control against "frequent-noun" artifact).
- MW-7: only TWO tests; both pre-locked; no post-hoc number is promoted.

## 6. Success/Failure summary
- **Census**: always delivered (descriptive); no verdict attached.
- **Test A PASS** = seven-heavens collocation beats base-rate.
- **Test B PASS** = Medinan number-density excess, locked direction.
- Overall verdict is the conjunction reported honestly, each test independently.

*Locked 2026-05-29 by Waiel Al-Shujaa. Census, not numerology. Bismillāh.*
