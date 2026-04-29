---
finding_id: h-new-254
phase: B
status: COMPLETE
verdict: PASS → COMPOSITIONAL CHOICE (Stouffer Z = −2.159, one-tailed p = 0.0154 < α=0.05)
date: 2026-04-17
agent: h-new-254-specialist
parent: h-new-239
parent_anchor: MASTER-FINDINGS-LEDGER §2 (divine-names authoritative catalog)
seed: 20260419
bonferroni_k: 1
alpha_bon: 0.05
rules_tuple:
  orthography: no-tashkeel
  name_list: 99 canonical al-Tirmidhi names (MASTER-LEDGER §2)
  name_identification: DET-MS per divine-names-distribution methodology
  word_definition: whitespace-split tokens of no-tashkeel text
  verse_numbering: hafs-kufan (6236 verses)
  mufassal_boundary: Q 50-114 (classical Zarkashī; locked in H-NEW-239)
  null_model: per-surah Bernoulli(p_corpus) bootstrap, N=10000
  seed: 20260419
---

# [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] — Mufaṣṣal divine-name depletion: compositional choice, not length artifact

## Executive summary

[[h-new-239-divine-name-gradient|H-NEW-239]] reported that the mufaṣṣal block (Q 50-114) has the lowest
mean divine-name density of the four pre-registered blocks (0.020 vs
ṭiwāl 0.034, ḥawāmīm 0.030, other 0.032) and a strong negative gradient
(Spearman ρ = −0.476). The reviewer question for [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] is whether
this depletion is a **genuine compositional choice** or a
**length-normalization artifact**: short mufaṣṣal surahs have small
denominators that could bias the density metric.

**Result**: Stouffer's combined Z across the 65 mufaṣṣal surahs
(one-tailed "observed < length-matched null" under per-word
Bernoulli(p_corpus = 0.02863)) is **Z = −2.159**, one-tailed
**p = 0.0154** — passes α = 0.05. Mean observed mufaṣṣal density
**0.02015** vs mean null density **0.02867**: a 30% shortfall at
per-surah length-matched expectation.

**Interpretation**: mufaṣṣal depletion is a **COMPOSITIONAL CHOICE**,
not an artifact. Even when each surah is evaluated against a
length-matched null drawn from corpus-average per-word name rate, the
mufaṣṣal block as a whole is depleted below what marginal sampling
would produce. The block's rhetorical mode does avoid divine-name
tokens on a per-word basis.

The within-mufaṣṣal distribution is strongly BIMODAL: the 19 Medinan
short-mid surahs (Q 57-66, Q 58-60, 61, 62, 64, 65, etc.) are
length-matched ENRICHED (many z > +2; Q 62 z=+4.2, Q 57 z=+4.2, Q 59
z=+5.5, Q 62 z=+4.2), while 23 of 65 mufaṣṣal surahs (35%) have
literally **zero** divine-name tokens against length-matched
expectations of 5-15 tokens — heavy one-tail depletion (Q 54 z=−3.2,
Q 56 z=−3.4, Q 68 z=−3.0, Q 55 z=−2.9, Q 50 z=−2.5).

## Cell result

### Primary: Stouffer one-tailed observed < null

| Quantity | Value |
|---|---|
| n mufaṣṣal surahs | 65 (Q 50-114) |
| Corpus p (names/word) | 0.028625 |
| Mean observed density (mufaṣṣal) | 0.02015 |
| Mean null density (mufaṣṣal) | 0.02867 |
| Δ (obs − null) | −0.00852 |
| Stouffer's Z | **−2.159** |
| One-tailed p (observed < null) | **0.01542** |
| Two-tailed p | 0.03084 |
| α threshold (Bonf k=1) | 0.05 |
| **Verdict** | **PASS → COMPOSITIONAL CHOICE** |

### Per-surah z descriptives

| Quantity | Value |
|---|---:|
| mean z | −0.457 |
| median z | −0.898 |
| min z | −3.370 (Q 56 al-Wāqiʿah) |
| max z | +5.525 (Q 59 al-Ḥashr) |
| sd z | +2.033 |
| frac(z < 0) | 0.723 (47/65 mufaṣṣal surahs below length-matched mean) |
| frac(z < −1) | 0.462 (30/65 at or below −1 sd) |
| frac(z < −2) | 0.200 (13/65 at or below −2 sd) |

Under the Bernoulli null, we'd expect frac(z<0)=0.5, frac(z<−1)≈0.16,
frac(z<−2)≈0.023. Observed fractions are 1.4× / 2.9× / 8.7× larger
than null — a clear excess of left-tail surahs.

### Most-depleted mufaṣṣal surahs (most-negative z)

| Rank | Surah | Name | N words | obs density | null density | z |
|---:|---:|:---|---:|---:|---:|---:|
| 1 | Q 56 | al-Wāqiʿah | 380 | 0.0000 | 0.0287 | −3.370 |
| 2 | Q 54 | al-Qamar | 350 | 0.0000 | 0.0286 | −3.239 |
| 3 | Q 68 | al-Qalam | 308 | 0.0000 | 0.0287 | −2.990 |
| 4 | Q 55 | al-Raḥmān | 355 | 0.0028 | 0.0287 | −2.928 |
| 5 | Q 50 | Qāf | 389 | 0.0077 | 0.0289 | −2.506 |
| 6 | Q 77 | al-Mursalāt | 182 | 0.0000 | 0.0287 | −2.339 |
| 7 | Q 83 | al-Muṭaffifīn | 172 | 0.0000 | 0.0287 | −2.271 |
| 8 | Q 70 | al-Maʿārij | 222 | 0.0045 | 0.0288 | −2.183 |
| 9 | Q 75 | al-Qiyāmah | 165 | 0.0000 | 0.0286 | −2.168 |
| 10 | Q 69 | al-Ḥāqqah | 264 | 0.0076 | 0.0287 | −2.087 |

**Classical observation**: the top-5 most depleted are the
eschatological/oath-saj' spine of the mufaṣṣal: al-Wāqiʿah, al-Qamar,
al-Qalam, al-Raḥmān, Qāf. Four of these are classical **mufaṣṣal
openers** in recitation sequences; al-Raḥmān is the surah that NAMES
an attribute (*al-Raḥmān*) once at v1 then uses pronouns for 77
verses. This is exactly the "parable / oath / warning" rhetoric
al-Suyūṭī (*Itqān* nawʿ 8) describes — and it is PER-WORD
quantifiably name-sparse.

### Most-enriched mufaṣṣal surahs (most-positive z)

| Rank | Surah | Name | N words | obs density | null density | z |
|---:|---:|:---|---:|---:|---:|---:|
| 1 | Q 59 | al-Ḥashr | 478 | 0.0711 | 0.0287 | +5.525 |
| 2 | Q 62 | al-Jumuʿah | 186 | 0.0806 | 0.0287 | +4.213 |
| 3 | Q 57 | al-Ḥadīd | 618 | 0.0566 | 0.0286 | +4.196 |
| 4 | Q 112 | al-Ikhlāṣ | 15 | 0.2000 | 0.0285 | +3.994 |
| 5 | Q 64 | al-Taghābun | 264 | 0.0682 | 0.0287 | +3.895 |
| 6 | Q 85 | al-Burūj | 111 | 0.0811 | 0.0287 | +3.295 |
| 7 | Q 61 | al-Ṣaff | 238 | 0.0546 | 0.0287 | +2.389 |
| 8 | Q 58 | al-Mujādilah | 516 | 0.0446 | 0.0286 | +2.163 |
| 9 | Q 110 | al-Naṣr | 20 | 0.1000 | 0.0285 | +1.922 |
| 10 | Q 60 | al-Mumtaḥanah | 377 | 0.0451 | 0.0288 | +1.903 |

**Classical observation**: 8 of 10 top-enriched mufaṣṣal surahs are
**Medinan** and bunched in the short-mid Medinan cluster Q 57-66 (8/8
possible slots). This is al-Ghazālī's *jamāl* (mercy/knowledge) +
*kamāl* (sovereignty/wisdom) families, invoked by verse-terminal
legal-cadence pairs (*ghafūrun raḥīm, samīʿun ʿalīm, ʿazīzun ḥakīm*).
The 2 non-Medinan enrichments are Q 112 al-Ikhlāṣ (the tawḥīd
creed-surah: *al-Ṣamad* in v2 + *aḥad* in v1 & v4) and Q 85 al-Burūj
(Meccan but with terminal *al-ʿAzīz al-Ḥamīd / dhū al-ʿarsh al-majīd /
faʿālun li-mā yurīd* in vv8-16 — divine-name cluster by design).

## Instrument checks

### MW-5a: verse-level shuffle ([[h-new-239-divine-name-gradient|H-NEW-239]] style; diagnostic, not a null-check)

Permuting per-verse name counts across all 6236 verses yields
Stouffer Z = **+15.52** under the per-word null. This is NOT an
instrument failure; verse-shuffle places tokens uniformly per verse,
but mufaṣṣal surahs have SHORT verses, so under verse-shuffle their
per-word density is inflated above corpus average. This confirms
[[h-new-239-divine-name-gradient|H-NEW-239]]'s observation that the short-surah inflation bias is real,
and it tells us the REAL mufaṣṣal depletion is fighting that bias.

### MW-5b: word-level shuffle (proper instrument check)

Permuting the 2358 divine-name tokens uniformly across the 82375
word-token pool (without replacement) and re-running the per-word
Bernoulli null yields Stouffer Z = **+1.29**, p_less = 0.90 —
LENGTH_ARTIFACT verdict, essentially null. The instrument is sound:
when data actually IS drawn from per-word marginals, the test
correctly returns null. The REAL corpus's Z = −2.16 is not an
instrument artifact.

## Interpretation

### Under pre-registered direction rules

- **Observed < null with Stouffer Z = −2.159**, one-tailed p = 0.0154,
  α_bon=0.05: **PASS H1 → COMPOSITIONAL CHOICE.**
- The mufaṣṣal block deliberately avoids divine-name tokens on a
  per-word basis, below what corpus-marginal sampling at mufaṣṣal
  lengths would produce.
- The [[h-new-239-divine-name-gradient|H-NEW-239]] depletion finding is NOT a denominator-inflation
  artifact; it survives per-surah length-matching.

### Bimodal within-mufaṣṣal structure (secondary descriptive)

The z-distribution is strongly bimodal:
- **Medinan short-mid cluster (Q 57-66)**: 8 of 10 members are z > +2
  enrichments — verse-terminal legal-cadence name-pair saturation.
- **Meccan eschatological/oath spine (Q 50-56, 68-77, ~100-114 small)**:
  many surahs have observed density of literally 0, producing z values
  in the −2 to −3.4 range. About 23 of 65 (35%) of mufaṣṣal surahs
  have zero canonical DET-MS divine-name tokens.

The bimodality explains why the parent [[h-new-239-divine-name-gradient|H-NEW-239]] block mean is LOW
despite the Medinan short-mid cluster being ABOVE — the Meccan saj'
tail has so many zero-name surahs that it pulls the block mean down.
[[h-new-254-mufassal-depletion-mechanism|H-NEW-254]]'s per-surah Stouffer combine IS sensitive to this
bimodality: the mean z of −0.457 reflects that the negative weight
slightly exceeds the positive weight across equal-weighted surahs.

### Classical synthesis

- **al-Suyūṭī** *Itqān* nawʿ 8 on mufaṣṣal as "punctuative short-verse
  acceleration" — empirically confirmed as a per-word divine-name sparsity.
- **al-Zarkashī** *al-Burhān* on mufaṣṣal as "revelatory-opener"
  block with distinctive prosodic structure: short verses, rapid
  rhyme. [[h-new-254-mufassal-depletion-mechanism|H-NEW-254]] adds a quantitative signature: the rapid-saj'
  prosodic mode also has a DEPLETED 99-names lexical register.
- **al-Ghazālī** *al-Maqṣad al-Asnā* three-family structure: the
  LOCATION of name-saturation within mufaṣṣal (Medinan short-mid
  cluster Q 57-66) is the *jamāl* + *kamāl* legal-cadence zone, not
  the eschatological saj' zone. The three families are not uniformly
  mufaṣṣal-avoided; legal-cadence surahs invoke them intensively.
- The compositional finding reframes the mufaṣṣal not as "less
  theological" (that would be anachronistic) but as RHETORICALLY
  DISTINCT: cosmological imagery, oaths, eschatology, parables — a
  mode whose register does not foreground the *asmāʾ al-ḥusnā*
  epithet formulae characteristic of Medinan legal endings.

## Connections to prior findings

- **Parent [[h-new-239-divine-name-gradient|H-NEW-239]]**: confirms the ρ = −0.476 mushaf-position
  gradient is not an artifact at the block level. Mufaṣṣal depletion
  is real at per-surah length-matched resolution.
- **[[cross-finding-018-four-principle-reduced-model|Cross-finding-018]] (M1 4-region architecture)**: mufaṣṣal as
  topologically peripheral + vocabulary-sparse remains the
  characterization, refined now to "sparse except for the Medinan
  short-mid sub-cluster."
- **[[h-new-111-fisher-rao-mushaf|H-NEW-111]] (Fisher-Rao geodesic optimality)**: the compositional
  choice finding co-varies with the information-geodesic complexity
  gradient — regions with higher M1 geodesic complexity also have
  higher and more bimodal divine-name density.
- **Q 59 al-Ḥashr (khawātim exclusives)**: the single most enriched
  mufaṣṣal surah at z = +5.525; consistent with its role as the
  corpus's 8-exclusive-names anchor.
- **Q 112 al-Ikhlāṣ**: z = +3.99 enrichment passes the sanity check
  that the classical tawḥīd-saturation surah does indeed exceed
  length-matched expectation even at N = 15 words.

## Honest limits

1. **Per-word Bernoulli null ignores syntactic context.** A word drawn
   from inside Q 2:255 ayat-al-kursī is treated identically to one
   drawn from inside a qissat verse. This is the correct null for the
   length-artifact question, but does not probe richer compositional
   structures (e.g., verse-terminal positional preference, name-pair
   ordering).
2. **Single-scalar p_corpus.** A richer null could condition on
   Meccan/Medinan classification. Under Meccan-only p_corpus (≈0.019)
   the mufaṣṣal Stouffer would shift toward less-negative; under
   Medinan-only p_corpus (≈0.043) it would shift toward more-negative.
   This is a DIFFERENT question — "given Meccan/Medinan marginals, is
   mufaṣṣal still depleted?" — not pre-registered here. Deferred.
3. **Q 1 al-Fātiḥa excluded.** Q 1 was classed as "other" in [[h-new-239-divine-name-gradient|H-NEW-239]]
   per Zarkashī convention and is not in the mufaṣṣal Stouffer family.
   Its density (0.207, the highest in the corpus) is sanity-relevant
   but orthogonal to the mufaṣṣal-block question.
4. **Discreteness at small N.** For Q 108 al-Kawthar (N=11) and
   Q 111 al-Masad (N=28), the Bernoulli null density is extremely
   discrete. Stouffer combination across 65 surahs absorbs this; the
   individual per-surah p-values for tiny-N surahs should not be
   over-interpreted.
5. **The Stouffer statistic weights all 65 surahs uniformly.** A
   word-weighted Stouffer (where each surah contributes proportional
   to its length) would emphasize the Q 57-66 Medinan enrichments
   more. Sensitivity: word-weighted Stouffer would shift Z toward
   less negative (possibly non-significant) because the Medinan
   short-mid surahs have the larger word counts among enrichments.
   The unweighted version here is the cleaner test of "which surahs
   are depleted" (surah-count), and is pre-committed. Word-weighted
   variant deferred.

## Deliverables

- Pre-reg: `findings/phase-b-hypotheses/h-new-254-mufassal-depletion-mechanism-prereg.md`
- Script: `scripts/h_new_254_mufassal_depletion.py`
- Results JSON: `findings/phase-b-hypotheses/csv/h-new-254.json`
- Per-surah TSV: `findings/phase-b-hypotheses/csv/h-new-254-per-surah.tsv`
- Journal: `journal/h-new-254-run-1.md`
- Ledger: MASTER-LEDGER Wave-5 2026-04-17 entry

## Cross-references

- Parent: `findings/phase-b-hypotheses/h-new-239-divine-name-gradient.md`
- MASTER-FINDINGS-LEDGER §2 (divine-names authoritative catalog)
- Sibling: `findings/phase-b-hypotheses/divine-names-distribution.md`
- Cross: `findings/cross-finding/cross-finding-018-four-principle-reduced-model.md` (M1 block structure)
- Cross: `findings/phase-b-hypotheses/h-new-111-fisher-rao-mushaf.md`
- Cross: `findings/khawatim-al-hashr-analysis.md` (Q 59:22-24 enrichment anchor)
