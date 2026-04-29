---
id: H-NEW-50
title: Bismillah 113+1=114 — quantitative test of the classical "complete-114" coincidence
status: PRE-REGISTERED 2026-04-15
spec_locked_at: 2026-04-15 (BEFORE running null model; the 114-count itself is well-known classical and was ratified in CC-015 of classical-quantitative-claims-audit.md — disclosed)
bonferroni_family: 2026-04-15-Wave-Bismillah-Numerology
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: (hafs-kufan; basmala-as-prepended-line per Tanzil simple-clean convention; substring match of literal "بسم الله الرحمن الرحيم" with normalized whitespace; no-tashkeel)
primary_data: 6266 verse lines (Tanzil simple-clean) + 114 surahs + Q 27:30 internal basmala
seed: 20260415
n_perm: 100000
---

# [[h-new-50-bismillah-114|H-NEW-50]] — Bismillah 113+1=114 Pattern

## Question

Classical claim (al-Shāfiʿī via al-Zarkashī, *Burhān* 1/213, already audited as CC-015):
"The basmala is recited 114 times in the muṣḥaf — 113 surah openings (all surahs except al-Tawba) + 1 internal occurrence at Q 27:30 (Solomon's letter to Bilqīs)."

The verification of the count is mechanical (and was confirmed in `classical-quantitative-claims-audit.md`).
The QUESTION pursued by [[h-new-50-bismillah-114|H-NEW-50]] is the **statistical significance** of the structural coincidence.

Specifically: under what null model does the conjunction
- (i) exactly 1 of the 114 surahs lacks an opening basmala, AND
- (ii) exactly 1 internal basmala occurs in the entire 6236-internal-verse corpus, AND
- (iii) the count therefore equals 114 (= number of surahs),

constitute a non-trivial coincidence rather than a forced/ trivial pattern?

## Garden-of-forking-paths disclosure

Pre-existing knowledge that motivated the spec:
- [[h-new-50-bismillah-114|H-NEW-50]] specialist KNOWS, before running, that:
  - Q 9 al-Tawba opens without basmala (the only surah).
  - Q 27:30 contains the unique internal basmala.
  - Both facts are ratified in CC-015 and are among the most well-known classical numerical observations.
  - The total = 114 = surah count is a famous "completion" pattern in classical recitation literature.

Honest protection: lock the 4-cell test family BEFORE running the null. Cells are NOT designed to retroactively reach significance; in fact two of them are designed to potentially DEMOTE the pattern.

## The 4 pre-registered test cells

### Cell 1 — Verification (mechanical)

Test statistic: number of basmala lines in Tanzil simple-clean text.
Pre-committed expected count: 113 line-starts + 1 internal = 114.
Direction: exact match.
Pass = exact 113 + 1 = 114. Fail = anything else.
This is a sanity / replication cell, not a probability test.

### Cell 2 — "Coincidence" of count = 114 = surah count under random-deletion null

Null model: assume each of the 114 surahs has a basmala opening with deletion probability p, AND assume internal basmalas occur uniformly at random across the 6236 non-opening verse positions with rate λ such that **E[total basmalas] = 114** (matching the observed total).

Under this null, what is the joint probability that:
- exactly 1 deletion occurs (among 114 surah openers), AND
- exactly 1 internal occurs (among 6236 non-opening verses).

Test statistic: Pr(deletions = 1 AND internals = 1 | total = 114).
Direction: two-sided (we ask if the observed split is the modal outcome; if not, by how many sigma).

This is the **central significance test**. We compute analytically (Poisson / binomial decomposition) AND verify with 10⁵ Monte Carlo draws (seed 20260415).

### Cell 3 — False-positive sweep for OTHER 4-word phrases with 114 occurrences

Test statistic: count, across all 4-word phrases (defined by the most-frequent 4-grams in the corpus AND a manually curated set of liturgically-significant 4-grams, see "MW-5 positive control" below), of phrases that occur exactly 114 times in the same 113-line-starts + 1-internal pattern.

Direction: one-sided. Lower count => more distinctive the basmala pattern.
Pre-committed expectation: ZERO other 4-word phrases match this exact structural pattern.

If even ONE other phrase matches: the basmala pattern is non-unique and weaker as numerical evidence.
If ZERO match: the basmala pattern is structurally unique among 4-word phrases of comparable frequency.

### Cell 4 — Q 27:30 verse-position salience

Test statistic: is verse-30 of Q 27 a numerically distinguished position?
Sub-statistics (each independent):
  (a) Is Q 27 the median (or mean) muqaṭṭaʿāt-opened surah index?
      Median of {2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,44,45,46,50,68}
      → record exact median; check if it equals 27.
  (b) Does verse-number 30 = (surah-29 → Q 27 verse-30 = surah+verse residue-class?) admit a lookup (e.g., 27+30=57, surah-57 al-Ḥadīd, or 27×30=810, etc.)
  (c) Does Q 27 have exactly 30 muqaṭṭaʿāt? (sanity: Q 27 starts with طس = 2 letters, so NO.)
  (d) Does the internal-basmala verse number (30) match any obvious modulus of the count 114 (e.g., 114 / 30 = 3.8, 114 mod 30 = 24, 30 = number of ajzāʾ in the muṣḥaf)?

Direction: one-sided exploratory. We pre-commit that **(a) median = 27 → significant**, **(d) 30 = ajzāʾ → suggestive but not conclusive without cross-corpus baseline**.

## Null model details

For cell 2, the null is:
- 114 surah-opening positions, each independently has basmala absence with probability p
- Internal basmalas ~ Poisson(λ) over 6236 verses
- Constraint: E[absences] + E[internals] = 114 - 114 + 1 = 1 absence, plus 1 internal, but generically: total Bismillah lines T = (114 − absences) + internals
- Under "the answer is exactly 114" constraint, decomposition splits into Pr(deletions = k) × Pr(internals = k) summed over k (since each deletion subtracts 1 and each internal adds 1, T = 114 ⟺ deletions = internals)

Honest framing: under any reasonable prior for p and λ, Pr(deletions = 1 AND internals = 1 | T = 114) is the central question. We compute the unconditional joint and the conditional.

## MW-5 positive control

Construct two reference 4-word phrases of comparable frequency in the corpus and verify Cell 3:

Plant 1: "the basmala without final word" → "بسم الله الرحمن" (3-word). EXCLUDE — different length.

Plant 2: A frequent 4-word phrase, e.g., "قل أعوذ برب" (3 words; the opening of Q 113 and Q 114). EXCLUDE — different length.

Plant 3 (real positive control): pick the most frequent **4-word phrase** in the no-tashkeel corpus that is NOT "بسم الله الرحمن الرحيم". Common candidates: "إن الله على كل" (continuation: "شيء قدير"), "الله لا إله إلا" (continuation: "هو"), "يا أيها الذين آمنوا" (4 words exactly).

For the most-frequent of these, count occurrences and locate them. If any 4-word phrase has exactly 113 line-starts + 1 internal pattern, Cell 3 PASSES the false-positive sweep — meaning the basmala pattern is NOT unique. If none, Cell 3 confirms uniqueness.

## Pre-committed verdict table

| Cell 1 (verify) | Cell 2 (coincidence) | Cell 3 (false-pos) | Cell 4 (Q 27:30) | Composite verdict |
|---|---|---|---|---|
| FAIL | * | * | * | ANOMALY-IN-DATA — investigate text |
| PASS | p > 0.05 | n_other > 1 | no salience | TRIVIAL — count is forced/non-distinctive |
| PASS | p > 0.05 | n_other = 0 | salience | EXPLORATORY-WEAK |
| PASS | p < 0.0125 | n_other = 0 | any | STRONG-PASS — the 113+1=114 pattern is statistically distinctive |
| PASS | p < 0.0125 | n_other > 0 | any | DEMOTED — significant but non-unique |
| PASS | p > 0.05 | n_other = 0 | strong salience | CLASSICAL-COINCIDENCE-CONFIRMED-BUT-NOT-STATISTICALLY-RARE |

## Mechanism interpretation

**If pass on cells 2 + 3:** the 113+1=114 pattern is a non-trivial structural coincidence in the canonical mushaf layout. It does NOT prove design (since the basmala may have been added editorially), but it raises the conditional probability that the canonical surah count was settled with this pattern in mind.

**If null:** the pattern is a forced consequence of (a) basmala being a near-universal opener and (b) the existence of the unique Solomonic letter quotation. The "completion to 114" is then a post-hoc observation rather than a design feature.

**Honest framing:** the mechanical fact (113+1=114) is undisputed. The QUESTION is whether the conjunction is more surprising than chance — and chance here must be carefully defined, since the basmala's status as the universal opener is itself a constraint.

## Integrity

- The 114 total is post-hoc-known; cells are pre-committed to evaluate the SIGNIFICANCE not the count.
- Bonferroni k=4 declared before null design.
- Publish all 4 cells regardless of direction.
- Seed 20260415 fixed for Monte Carlo cell 2.
- Cross-check with full-tashkeel and Tanzil min variants in supplementary cell.
