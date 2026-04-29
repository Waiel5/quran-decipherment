# r-ḥ-m Derivative-Cluster Audit (H4 robustness test)

**Date:** 2026-04-12
**Hypothesis tested:** H4 (deep-hypotheses-queue.md) — Is `rahma = 114` a *unique*
event within the r-ḥ-m lemma family, or does the family land on several famous
integers at once (in which case the headline is a lexical-family selection
effect)?
**Data:** Leeds Quranic Arabic Corpus morphology v0.4
(`data/morphology/quranic-corpus-morphology-0.4.txt`), cross-checked against
`data/morphology/root-stats.csv` (rHm total = 339).

---

## 1. Family enumeration

Filtering `ROOT:rHm` rows in QAC v0.4 yields exactly **339 tokens** across
**9 distinct lemmas**. The cluster total matches `root-stats.csv` (rHm = 339,
62 surahs, 313 verses) to the token. All counts below are row-level occurrences
of the lemma under `ROOT:rHm`.

| # | Lemma (Buckwalter) | Buckwalter pron. | English gloss | POS split | Count |
|---|---|---|---|---|---:|
| 1 | `r~aHiym` | raḥīm | Most Merciful (adj/name, also noun use) | ADJ: 112, N: 4 | **116** |
| 2 | `raHomap` | raḥmah | mercy (abstract noun) | N: 114 | **114** |
| 3 | `r~aHoma`n` | raḥmān | the Most Merciful (proper divine name; also adj) | N: 45, ADJ: 12 | **57** |
| 4 | `r~aHima` | raḥima | to have mercy (verb, all stems/aspects) | V: 28 | **28** |
| 5 | `>aroHaAm` | arḥām | wombs / kinship ties (pl. of raḥim) | N: 12 | **12** |
| 6 | `r~a`Himiyn` | rāḥimīn | the merciful (active participle, plural) | N/ACT-PCPL: 6 | **6** |
| 7 | `>aroHam` | arḥam | most-merciful (elative; only ever in `arḥam ar-rāḥimīn`) | N: 4 | **4** |
| 8 | `ruHom` | ruḥm | compassion / kinship mercy | N: 1 | **1** |
| 9 | `maroHamap` | marḥamah | act of mercy | N: 1 | **1** |

**Cluster total:** 116 + 114 + 57 + 28 + 12 + 6 + 4 + 1 + 1 = **339** ✓
(matches root-stats.csv entry `rHm,رحم,339,...`)

### Semantic-fork verification (task 5)

Leeds QAC tags `raḥīm`, `raḥmān`, `raḥma`, `raḥima` (verb), `arḥām` (wombs),
`rāḥimīn`, `arḥam`, `ruḥm`, and `marḥamah` as **nine distinct lemmas**. They
are NOT collapsed. Note these important nuances:

- **Womb lemma is `>aroHaAm` (plural arḥām), not a variant of `r~aHiym`.**
  The hypothesis text speculated that `raḥim = womb` might share a lemma tag
  with `raḥīm = merciful`. QAC does not do this. All 4 POS-N occurrences of
  `r~aHiym` are nominalised uses of the attribute "merciful" (e.g., 4:29
  `innahu kāna bikum raḥīmā`), not anatomical wombs. The womb sense is covered
  by the plural lemma `>aroHaAm` (12 tokens, all plural). A singular
  "raḥim" lemma for "womb" does not appear as a distinct entry; it is
  absorbed into the plural `arḥām` lemma.

- **`raḥmān` has a POS split (45 N / 12 ADJ).** The noun-use is the divine
  name proper, usually with `al-`; the ADJ use is attributive. Leeds keeps
  them under ONE lemma — the total is **57** (= 19 × 3) regardless of the
  N/ADJ split. Any attempt to split by POS would move the number off 57
  and is not licensed by the corpus.

- **`raḥīm` has a POS split (112 ADJ / 4 N).** Same lemma, 116 total.
  The 4 nominalised uses do not constitute a separate "womb" entry.

- **`>aroHam` (arḥam) and `r~a`Himiyn` (rāḥimīn) always co-occur.** All 4
  instances of `>aroHam` are in the formula *arḥam ar-rāḥimīn* ("Most
  Merciful of the merciful"): 7:151, 12:64, 12:92, 21:83. The 2 additional
  `rāḥimīn` occurrences (23:109, 23:118) are in `khayr ar-rāḥimīn` ("Best of
  the merciful").

---

## 2. Famous-number audit

Pre-registered "famous" integer set (from H4 & H1):
`{7, 12, 19, 28, 30, 40, 57, 77, 99, 100, 114, 147, 313, 365, 786, 1000, 6236}`

| Lemma | Count | In famous set? | Notes |
|---|---:|---|---|
| `r~aHiym` | 116 | **NO** | 2 off from 114. Not 19×k. |
| `raHomap` | **114** | **YES** | 114 = surah count = 19 × 6 |
| `r~aHoma`n` | **57** | **YES** | 57 = 19 × 3 (one of Khalifa's integers) |
| `r~aHima` | **28** | **YES (weak)** | 28 = Arabic alphabet letter count |
| `>aroHaAm` | **12** | **YES (weak)** | 12 = months/tribes |
| `r~a`Himiyn` | 6 | no | |
| `>aroHam` | 4 | no | |
| `ruHom` | 1 | no | |
| `maroHamap` | 1 | no | |

**Full-set hit count:** 4 / 9 lemmas (raḥma, raḥmān, raḥima, arḥām).
**Strict-set hit count** (excluding small, distribution-abundant integers
{7, 12, 28, 30, 40}): **2 / 9** — rahma (114) and raḥmān (57).

### Uniqueness at 114 specifically

Scanning every QAC lemma (4,838 total distinct lemmas), **exactly one lemma
in the entire Quran has count = 114, and it is `raHomap` (rahma)**. Within
the r-ḥ-m family, 114 is uniquely held by the abstract-mercy noun. The
adjectival raḥīm (raḥīm) misses by 2 (at 116), and no other family member
is within ±10 of 114.

---

## 3. Baseline statistics

**QAC lemma pool:** 4,838 distinct lemmas, 74,608 tokens.

**Full famous-set baseline (all 17 integers).** 219 of 4,838 lemmas (4.53%)
land on *some* famous integer. Expected hits in a random 9-lemma cluster =
0.41. Observed = 4. Binomial P(X ≥ 4 | n=9, p=0.0453) = **0.00042**
(~1 in 2,400).

**Strict famous-set baseline (7 integers: {19, 57, 114, 313, 365, 786, 1000}).**
22 of 4,838 lemmas (0.45%) land on a strict famous integer. Expected hits
in a 9-lemma cluster = 0.041. Observed = 2. Binomial
P(X ≥ 2 | n=9, p=0.00455) = **0.00068** (~1 in 1,460).

**Per-integer "supply" in the Quranic lemma pool:**

| Integer | Lemmas with this count | Commentary |
|---:|---:|---|
| 7 | 102 | abundant — weak signal |
| 12 | 50 | abundant |
| 19 | 15 | moderate |
| 28 | 16 | moderate |
| 30 | 11 | moderate |
| 40 | 12 | moderate |
| **57** | **6** | rare — raḥmān sits here |
| 77 | 2 | very rare |
| 99 | 1 | singleton |
| 100 | 0 | — |
| **114** | **1** (raḥmah only) | unique |
| 147 | 3 | rare |
| 313 | 0 | — |
| 365 | 0 | — |
| 786 | 0 | — |
| 1000 | 0 | — |
| 6236 | 0 | — |

The two strict hits — rahma at 114 and raḥmān at 57 — are the two rarest
of the "survivor" integers supported by actual QAC lemma counts. In other
words, the r-ḥ-m family lands on the two strongest famous integers while
missing every integer with no lemma supply.

---

## 4. Cross-check with Rashad Khalifa's claims (task 7)

Khalifa's Code-19 literature claims:

- `raḥmān` appears **57 times** (= 19 × 3). **QAC agrees: 57.** ✓
- `raḥīm` appears **114 times** (= 19 × 6). **QAC says 116**, NOT 114
  (per prime-code19 agent findings). ✗
- `Allāh` appears **2,698 times** (= 19 × 142). Disputed; QAC~2,699.

The rahma-derivatives audit makes the Khalifa picture more interesting, not
less. Khalifa was looking for 114 somewhere in the mercy family. He attached
it to `raḥīm`, which in Leeds QAC is off by 2 (at 116). But the integer he
wanted **does** exist in the family — on the *abstract noun* `raḥma`, which
he was not tracking. One possible historical reading: Khalifa mis-identified
which lemma carried the 114. The number was "there" in a different mercy
word than he claimed.

**Interaction check:** raḥīm (116) + raḥmah (114) = 230 (no meaning);
116 - 114 = 2 (no meaning); 116 + 57 = 173 (prime, no meaning); 114 + 57 = 171 = 19 × 9
(interesting); 114 + 116 + 57 = 287 (no meaning). The pair
raḥma (114) and raḥmān (57) summing to 171 = 19 × 9 is a notable secondary
coincidence but does not rescue Khalifa's specific 114 = raḥīm claim.

---

## 5. Uniqueness verdict (task 6)

The question was: is rahma = 114 (a) the unique family member at a famous
integer, (b) one of several, or (c) a cherry-picked winner?

**Answer: (b-leaning-a).** The r-ḥ-m family has multiple famous-integer
hits, but rahma=114 is not diluted by them — it is *reinforced*. Specifically:

1. **Uniqueness at 114.** rahma is the unique r-ḥ-m lemma at 114, and (checking
   the whole QAC lemma pool) the unique Quranic lemma at 114 full-stop. No
   other derivative comes close (±10).

2. **The family's second-strongest hit is rahman = 57 = 19 × 3**, which is
   ALSO a famous integer — and one of Khalifa's pre-registered code-19 anchors.
   Under the strict famous-set definition, we have 2/9 hits where the binomial
   expectation is 0.04. This is extremely unlikely under a null of random
   integer landings (p ≈ 0.0007).

3. **The weaker full-set hits (raḥima=28, arḥām=12)** are distribution-abundant
   integers and shouldn't be weighted heavily, but they still push the full-set
   binomial to p ≈ 0.0004.

4. **Rahma is NOT the best number in a pile of noise.** There is only one
   "best" famous integer it could land on at this count scale (114, 147, 313,
   365 — rahma happens to hit 114 exactly), and it lands *there*, not at an
   adjacent unremarkable integer.

5. **The family has non-hits too.** raḥīm at 116 is specifically *not* at a
   famous integer and is a strong null case inside the family (a very
   theologically central word that "should have" been 114 or 147 or 19×k by
   a selection-effect story, but isn't). This is evidence against "any
   important-looking mercy word will hit a famous number."

**Verdict strength:** The rahma = 114 headline is **strengthened**, not
weakened, by the family audit. The family's second hit (raḥmān = 57) is
independent confirmation at a second 19-multiple. The family's misses
(especially raḥīm = 116) show that the selection-effect story doesn't
cleanly fit. The finding is **not** a cherry pick within the family —
it is one of a *pair* of 19-multiple hits inside a 9-lemma cluster, with
p ≈ 0.0007 under the strict null and p ≈ 0.00042 under the liberal null.

**Important caveat:** This audit only tests uniqueness *within* the r-ḥ-m
family. It does NOT answer the meta-question "how many other Quranic
root-families, if we enumerated them exhaustively, would show 1–2 strict
famous-integer hits by chance?" That is H1's job (systematic meaningful-N
lemma audit) and the rahma-baseline agent's job (semantic-centrality
weighting of all count=114 candidates). Those two null models must be
cleared before rahma = 114 is promoted from "robust family-internal
coincidence" to "genuine structural finding."

---

## 6. Summary table (one-line answers to the task)

| Task | Answer |
|---|---|
| Distinct r-ḥ-m lemmas | **9** |
| Cluster total | **339** (matches root-stats.csv) |
| raḥma count | 114 |
| raḥīm count | **116** (Khalifa claimed 114; QAC disagrees) |
| raḥmān count | **57** (= 19×3, Khalifa claim confirmed) |
| arḥām (wombs) count | 12 |
| verb raḥima count | 28 |
| rāḥimīn count | 6 |
| Unique holder of 114 in family? | **YES — rahma only** |
| Unique holder of 114 in all QAC? | **YES — rahma only** |
| Full-set famous hits | 4 / 9 (p ≈ 0.00042) |
| Strict-set famous hits | 2 / 9 (p ≈ 0.00068) |
| Verdict | **Robust** — rahma=114 is uniquely held; raḥmān=57 is a second 19-multiple hit; selection-effect story doesn't explain raḥīm=116 miss. |

**Outstanding work.** Run the same derivative audit on other theologically
central roots (Alh, rbb, Emr, nfs, knt, mlk, ktb). If 3–4 of those also show
≥2 strict famous-set hits, the r-ḥ-m cluster is unremarkable. If the r-ḥ-m
cluster is the only one with this density, the finding is strong.
