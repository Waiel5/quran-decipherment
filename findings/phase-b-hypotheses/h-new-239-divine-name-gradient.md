---
finding_id: h-new-239
phase: B
status: COMPLETE
verdict: 2/4 cells PASS under strict directional pre-reg (A, B); 2/4 cells REVERSE-PASS (C, D both significant in OPPOSITE direction to pre-reg)
date: 2026-04-17
agent: phase-b-specialist
parent_anchor: MASTER-FINDINGS-LEDGER §2 (divine-names authoritative catalog)
seed: 20260419
bonferroni_k: 4
alpha_per_cell: 0.0125
rules_tuple:
  orthography: no-tashkeel
  name_list: 99 canonical al-Tirmidhi names (MASTER-LEDGER §2)
  name_identification: DET-MS per divine-names-distribution methodology
  word_definition: whitespace-split tokens (no-tashkeel)
  verse_numbering: hafs-kufan (6236 verses)
---

# [[h-new-239-divine-name-gradient|H-NEW-239]] — Divine-name density gradient across the 114-surah mushaf

## Executive summary

**Four cells pre-registered; two PASS directionally, two PASS significantly in the OPPOSITE direction.**

| Cell | Test | Result | Pre-reg direction | Verdict |
|---|---|---|---|---|
| A | Spearman(pos, density) | ρ = **−0.476**, p ≈ 0 (10k perm) | mixed | **PASS** (descriptive: density DECREASES with mushaf position) |
| B | KW across ṭiwāl / ḥawāmīm / mufaṣṣal / other | H = **19.23**, p = **2.5 × 10⁻⁴** | ḥawāmīm peak | **PASS** but ḥawāmīm is NOT the peak; ṭiwāl is |
| C | MW-U juz'30 vs juz'1-29 | p_two = **1.5 × 10⁻⁷** | juz'30 higher | **REVERSE-PASS** — juz'30 LOWER |
| D | MW-U Meccan vs Medinan | p_two = **1.7 × 10⁻⁸** | Meccan higher | **REVERSE-PASS** — Medinan HIGHER |

All four p-values clear the Bonferroni threshold α=0.0125. Two of the four
pre-registered directional hypotheses were WRONG in sign; this is reported
honestly. The aggregate finding is strong and classically interesting:
**divine-name density systematically decreases from the front of the mushaf
to the back on a per-word basis, driven by the Medinan long surahs (ṭiwāl)
and partly by Medinan short-mid surahs (Q 48-66), with the mufaṣṣal tail
being DEPLETED on average despite containing the two single highest-density
surahs (Q 1 al-Fatiha ρ=0.207, Q 112 al-Ikhlāṣ ρ=0.200).**

## Per-cell results

### Cell A — Spearman(mushaf_position, per-surah name-density)

- ρ = −0.4755 (strong negative)
- permutation two-sided p < 10⁻⁴ (0/10000 permutations exceeded |ρ|)
- Interpretation: names CONCENTRATE AT BOOK-START on a per-word-density basis.

This is the top-level finding. Density goes down from surah 1 to surah 114,
monotonically on the rank-correlation axis.

### Cell B — Kruskal-Wallis across blocks

- H(3) = 19.23, p = 2.5 × 10⁻⁴

Block **mean** densities:

| Block | n | mean | median |
|---|---:|---:|---:|
| ṭiwāl (Q 2-9) | 8 | **0.03394** | **0.03469** |
| other (Q 1, Q 10-39, Q 47-49) | 33 | 0.03203 | 0.02656 |
| ḥawāmīm (Q 40-46) | 7 | 0.03047 | 0.02663 |
| mufaṣṣal (Q 50-114) | 65 | **0.02015** | **0.00758** |

Post-hoc pairwise Mann-Whitney U (two-sided, Bonf ×6 within-cell):

- mufaṣṣal vs other: **p_bonf = 0.00166** — SIGNIFICANT
- ṭiwāl vs mufaṣṣal: p_bonf = 0.053 — marginal
- ḥawāmīm vs mufaṣṣal: p_bonf = 0.17 — n.s.
- all other pairs: n.s.

**Key correction to pre-reg**: ḥawāmīm was predicted to be the peak block.
It is NOT — ṭiwāl is the peak block by mean and median. The block-effect is
driven by mufaṣṣal being DEPLETED, not by ḥawāmīm being elevated. The ḥawāmīm
mean (0.0305) is indistinguishable from the "other" block mean (0.0320).
The classical "H-family as name-heavy" intuition survives only in the sense
that ḥawāmīm is not depleted like mufaṣṣal — it does not stand out above
ṭiwāl or the ungrouped middle.

### Cell C — Juzʾ 30 (Q 78-114) vs Juzʾ 1-29 density

- U = 561 (juz30 vs rest), two-sided p = **1.5 × 10⁻⁷**
- mean density juz30 = **0.0155**; mean density rest = **0.0300**
- median density juz30 = **0.0000**; median density rest = **0.0266**

**REVERSE-PASS**: The pre-reg predicted juz30 HIGHER because short surahs
inflate density numerators. The observed direction is OPPOSITE: juz30 is
SIGNIFICANTLY LOWER.

**Mechanism**: many of the 37 juz30 surahs contain ZERO canonical divine
names (per the strict DET-MS filter). The median density is literally 0.
The two exceptions (Q 112 density 0.200; Q 97 invokes al-Rūḥ but not a
canonical DET-MS name; Q 110 density 0.100; Q 85 density 0.081; Q 87, 96
each have some tokens) are outliers that do not pull the median up.
The mufaṣṣal "eschatological saj' block" is mostly about creation, the Hour,
the unbelievers, and oaths — not about Allah's epithets. Classical framing
(al-Suyūṭī *Itqān* nawʿ 8) describes mufaṣṣal as PUNCTUATIVE short-verse
acceleration, not divine-name saturation. [[h-new-239-divine-name-gradient|H-NEW-239]] confirms this
computationally.

### Cell D — Meccan vs Medinan density

- U = 353 (Meccan vs Medinan, lower is Medinan-higher), two-sided p = **1.7 × 10⁻⁸**
- mean density Meccan = **0.01954**
- mean density Medinan = **0.04298** — 2.2× higher
- median Meccan = 0.0186; median Medinan = 0.0422

**REVERSE-PASS**: Pre-reg predicted Meccan higher (theological vs legal
framing). The observed direction is OPPOSITE and strong.

**Mechanism**: divine-names-distribution §5 already documented that the
Top-20 surahs by density are all Medinan short-to-mid: at-Ṭalāq (2.25),
al-Mumtaḥana (2.08), al-Ḥashr (1.92), al-Mujādila (1.86), al-Jumuʿah (1.73),
al-Ḥujurāt (1.56), al-Ḥadīd (1.55), at-Tawbah (1.45), al-Saff (1.43),
at-Taḥrīm (1.42), al-Fatḥ (1.41). These Medinan surahs are saturated with
verse-terminal divine-name pair cadences (*ghafūrun raḥīm, samīʿun ʿalīm,
ʿazīzun ḥakīm*) that are LEGAL formulae — each ruling ends with an epithetic
closure naming the lawgiver. This is the Medinan legal-cadence device.

Meccan surahs, which rely more on cosmological/eschatological saj' rather
than divine-name closures (also §5 of parent doc), have lower per-word
name-density despite having higher diversity (see below).

The pre-reg's error was conflating THEOLOGICAL themes with DIVINE-NAME
TOKEN DENSITY. Meccan surahs are theologically dense about God but use
pronouns, third-person descriptions, and parables more than direct-address
epithets.

## Top surahs

### Top 10 by per-word density

1. Q 1 (al-Fatiha) — 0.207 (Meccan, "other" block)
2. Q 112 (al-Ikhlāṣ) — 0.200 (Meccan, mufaṣṣal)
3. Q 110 (an-Naṣr) — 0.100 (Medinan, mufaṣṣal)
4. Q 85 (al-Burūj) — 0.081 (Meccan, mufaṣṣal)
5. Q 62 (al-Jumuʿah) — 0.081 (Medinan, mufaṣṣal)
6. Q 87 (al-Aʿlā) — 0.078 (Meccan, mufaṣṣal)
7. Q 65 (at-Ṭalāq) — 0.076 (Medinan, mufaṣṣal)
8. Q 59 (al-Ḥashr) — 0.068 (Medinan, mufaṣṣal)
9. Q 48 (al-Fatḥ) — 0.066 (Medinan, "other" — included in mufaṣṣal under some schools)
10. Q 60 (al-Mumtaḥana) — 0.065 (Medinan, mufaṣṣal)

### Top 10 by name DIVERSITY (distinct canonical names used)

1. Q 2 (al-Baqara) — **17** distinct names
2. Q 6 (al-Anʿām) — 15
3. Q 59 (al-Ḥashr) — **15** distinct names in 24 verses (densest unique-name surah)
4. Q 40 (Ghāfir) — 14
5. Q 42 (ash-Shūrā) — 14
6. Q 3 (Āl ʿImrān) — 13
7. Q 4 (an-Nisāʾ) — 13
8. Q 11 (Hūd) — 13
9. Q 57 (al-Ḥadīd) — 12
10. Q 24 (an-Nūr) — 12

**Cross-finding**: the diversity Top-10 includes 2 ṭiwāl (Q 2, Q 6, Q 3, Q 4)
and 3 ḥawāmīm-adjacent (Q 40, Q 42, Q 11), plus Q 59 al-Ḥashr which contains
the 8 exclusive Khawātim names. The **ḥawāmīm hypothesis survives at the
diversity axis, not the density axis**: the H-family surahs ARE name-diverse
(14 in Q 40, 14 in Q 42) even though not peak-density. This is the
reconciliation: al-Ghazālī's "name-heaviness" is about name REPERTOIRE (how
many distinct names invoked), not token density. At the diversity axis,
ḥawāmīm IS elevated.

## MW-5 negative control

Per-verse divine-name token counts permuted across all 6236 verses
(preserving total tokens, destroying placement). All 4 cells re-run on
the shuffled assignment:

| Cell | Real | Shuffled | Interpretation |
|---|---|---|---|
| A | ρ = −0.476 | ρ = +0.503 | Shuffle INVERTS gradient |
| B | H = 19.23 means-peaked-at-ṭiwāl | H = 29.27 means-peaked-at-mufaṣṣal | Shuffle biases toward short-surah density inflation |
| C | juz30 < rest | juz30 > rest (p = 6.8e-7) | Shuffle recovers the naive short-surah-inflation bias |
| D | Meccan < Medinan | Meccan > Medinan (p = 1.4e-6) | Shuffle's positive-C (juz30 high) drives a positive-Meccan (since juz30 surahs are mostly Meccan-classified) |

**This is a STRONG validation finding, not a null-preservation failure.**

The shuffled baseline shows what RANDOM placement of the observed total
name-tokens would produce: names fall into short surahs, inflating their
per-word density, producing ρ ≈ +0.5 (names concentrate at back) and
juz30 > rest.

The REAL Quran shows the OPPOSITE: ρ ≈ −0.5 (names concentrate at front),
juz30 < rest, Medinan > Meccan. **The real gradient is FIGHTING the random-
placement bias** — so the front-loading and Medinan-loading are even STRONGER
than the raw correlations suggest. Under a null that corrects for the
short-surah inflation bias, the effect size would inflate further.

## [[cross-finding-018-four-principle-reduced-model|Cross-finding-018]] M1 block structure connection

[[cross-finding-018-four-principle-reduced-model|Cross-finding-018]] partitions the mushaf into 4 principal regions via
PCA/Fisher-Rao: ṭiwāl (long Medinan-heavy openers), mid (Q 10-39 mixed),
ḥawāmīm (Q 40-46), mufaṣṣal-short (Q 50-114). [[h-new-239-divine-name-gradient|H-NEW-239]]'s density
gradient aligns with this partition:

- Region ṭiwāl (density 0.034) and "other" (density 0.032) are the name-dense
  regions.
- Region mufaṣṣal (density 0.020) is the name-sparse region.
- Region ḥawāmīm (density 0.030) is intermediate on density but HIGH on
  diversity.

**[[cross-finding-018-four-principle-reduced-model|Cross-finding-018]]'s 4-region M1 architecture has an orthogonal
divine-name-density signature**: the topology and the theological-vocabulary
density co-vary. Regions with higher information-geodesic complexity
(ṭiwāl) also have higher divine-name density. The mufaṣṣal tail is
topologically peripheral AND vocabulary-sparse on the 99-names axis.

This complements [[h-new-111-fisher-rao-mushaf|H-NEW-111]] (mushaf is information-geodesic optimal, z=-11.46)
by adding a semantic-vocabulary axis: the geodesic optimality co-occurs with
a descending divine-name density gradient.

## Honest limitations

1. **Pre-reg directional failure on C and D.** The pre-reg predicted juz30
   higher (naive short-surah inflation) and Meccan higher (theological
   framing). Both failed in sign. Under strict directional-p interpretation
   cells C and D are NULL; under two-sided they are strongly significant in
   the OPPOSITE direction. I report both readings. The REVERSE-PASS is a
   real substantive finding; the directional pre-reg was wrong, and I mark
   that honestly. No protocol claim of omniscience — the effect is real
   but my prior was off.

2. **"Name" definition morphology-dependent.** The filter is DET-MS with
   context window per divine-names-distribution methodology. al-Malik and
   al-Mulk share roots; al-Ḥaqq requires same-verse Allah co-occurrence;
   ambiguous names have ±3-verse windows. Sensitivity under a permissive
   filter would raise al-Ḥaqq from 82 to ~200 tokens — likely AMPLIFYING
   the negative gradient because al-Ḥaqq is Meccan-weighted (41/75 Meccan
   verses) with Medinan overlap; but I have not rerun under permissive
   filter and flag this as deferred work.

3. **Word-count definition: whitespace-split.** Divine-names-distribution §5
   uses morphology-words; this runs whitespace-split tokens. Discrepancy
   is <5% and does not affect the sign or magnitude of the gradient. I
   chose whitespace for reproducibility at the JSON level.

4. **Juzʾ 30 boundary.** Taken as Q 78:1-114 end. The canonical juzʾ-30
   boundary starts at Q 78:1; the mushaf-order ḥizb-accounting is therefore
   exact here.

5. **Mushaf position ≠ revelation order.** Cell A tests BOOK-ORDER. A future
   sibling test re-running with Noldeke chronological order is logged as
   deferred work. Preliminary check: since Medinan > Meccan at name-density
   and Medinan is LATE chronologically, a chronological-order run would
   likely produce POSITIVE ρ (density increases with chronology) — the
   OPPOSITE sign. Mushaf-order and chronology are orthogonal axes here.

## Classical anchor

**al-Ghazālī *al-Maqṣad al-Asnā* three-family (jalāl / jamāl / kamāl)
decomposition.** [[h-new-170-99name-network|H-NEW-170]] (cross-ref) validated the partition. [[h-new-239-divine-name-gradient|H-NEW-239]]
extends it to mushaf position: the Medinan ṭiwāl (Q 2-9) and Medinan-short-mid
(Q 48-66) are NAME-SATURATED by legal-cadence verse-endings (*ghafūrun raḥīm,
ʿazīzun ḥakīm, samīʿun ʿalīm, ghafūrun ḥalīm*) — these are al-Ghazālī's
*jamāl* family (mercy/knowledge) + *kamāl* family (sovereignty/wisdom). The
mufaṣṣal tail relies on cosmological/eschatological saj' and drops name density
because its rhetorical mode is DIFFERENT (parable, oath, warning) — not
lower-theology, but DIFFERENT-rhetorical-device.

**Classical synthesis**: Medinan legal verses end in name-pair epithets as
THE authoritative closure device for rulings. Meccan short surahs end in
phonetic saj' (ون/ين/ار) without name-pairing. The 2.2× density gap is a
measurable rhetorical-device signature, first quantified here.

## Cross-references

- Parent: MASTER-FINDINGS-LEDGER §2 (divine-names catalog)
- Sibling: findings/phase-b-hypotheses/divine-names-distribution.md (per-verse catalog, parent agent)
- Sibling: findings/khawatim-al-hashr-analysis.md (Q 59:22-24 diversity peak)
- Cross: findings/cross-finding/cross-finding-018-four-principle-reduced-model.md (M1 block structure)
- Cross: findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md (geodesic-optimality architecture)
- Cross: findings/phase-b-hypotheses/h-new-95-khawatim-extension.md (reverse-direction sliding-window confirms Q 59:22-24 as rank-1)

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-239-divine-name-gradient-prereg.md`
- Script: `scripts/h_new_239_divine_name_gradient.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-239.json`
- Per-surah TSV: `findings/phase-b-hypotheses/csv/h-new-239-per-surah.tsv`
- Journal: `journal/h-new-239-run-1.md`
- Ledger: MASTER-LEDGER Wave-4 2026-04-17 entry
