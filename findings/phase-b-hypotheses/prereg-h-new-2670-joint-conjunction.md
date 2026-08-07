---
id: H-NEW-2670
title: "PRE-REGISTRATION — Joint conjunction improbability: the muqaṭṭaʿāt-14 under ALL declared constraints simultaneously"
date: 2026-08-07
phase: B
status: LOCKED — written before any survivor count was computed
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260519
parents: [H-NEW-2550, H-NEW-69, H-NEW-60, H-NEW-44.2, H-NEW-44.2.1, H-NEW-1810, H-NEW-1730, H-NEW-1740, H-NEW-165]
---

# PRE-REGISTRATION — H-NEW-2670

**Nothing in this file may be altered after the first survivor count is computed. Its
SHA-256 is embedded in `findings/phase-b-hypotheses/scripts/h-new-2670.py` and verified at
runtime with `SystemExit` on mismatch, per INVESTIGATION-PROTOCOL §1.2.**

---

## 0. The methodological gap this test addresses

[[h-new-2550-muqattaat-phonetic-optimizer|H-NEW-2550]] tested the 14 muqaṭṭaʿāt letters on
several axes **one at a time** and applied Bonferroni with k = 28. Bonferroni controls the
family-wise error rate of a **union** — "did any of 28 tests hit by chance?" It is the
correct instrument for that question and the wrong instrument for a different one:

> **How many of the 40,116,600 possible 14-letter subsets of the 28-letter alphabet satisfy
> ALL the observed properties simultaneously?**

That is an **intersection** question. No prior finding in this project has computed it.
H-NEW-2550 established that 1,024,500 subsets (2.5538 %) tie the al-Zamakhsharī
feature-imbalance global minimum, and separately that a corpus-frequency-weighted cell sits
at p = 0.001828. **Nobody has computed how many subsets satisfy both, or all, at once.**

That number is the object of this test. It may be orders of magnitude smaller than any
single-axis p — or it may collapse to 1 purely because enough constraints were stacked.
**Distinguishing those two cases is the entire purpose of §6.** Constraint-stacking to
uniqueness is the standard mechanism by which numerology manufactures miracles; §6 is the
guard against this finding doing the same thing.

## 0.1 What is already known, and therefore is NOT this test's contribution

Stated before the lock so it cannot later be presented as new:

| Already published | Value | Source |
|:--|:--|:--|
| The 14-set ties the al-Zamakhsharī 5-genus imbalance global minimum | D = 1.0 | H-NEW-2550 §3 |
| Subsets tying that minimum | 1,024,500 = 2.5538 % | H-NEW-2550 §3 |
| The set does not coincide with any of 8 classical 14-cuts | max Jaccard 0.400 | H-NEW-69 |
| 11 of 13 dotless letters are muqaṭṭaʿāt | p = 0.000919 | H-NEW-60 |
| All 4 pharyngeal/glottal letters are muqaṭṭaʿāt | p = 0.049 | H-NEW-44.2.1 |
| 5 of 6 sonorants are muqaṭṭaʿāt | p = 0.0744 | H-NEW-69, post-hoc |
| The 14 carry 74.41 % of corpus letter mass | T3 PASS | H-NEW-1810 |
| The 14 overlap the corpus top-14 by frequency in 10 places | T2 strong FALSIFIED | H-NEW-1810 |

Every marginal above is prior art. **This test's only contributions are: the joint survivor
count, the shrinkage curve, the order-dependence of that curve, the pairwise independence
matrix, and the random-subset control.** Nothing else.

---

## 1. The declared property list — LOCKED

Each property must be (a) a property the attested 14-set demonstrably has, (b) computable
for any 14-subset of the 28-letter alphabet, (c) independently motivated by a classical
source or a prior pre-registered finding, and **not** reverse-engineered from the attested
set. Membership sets are given in full so no post-lock reinterpretation is possible.

The attested set is derived from the corpus at runtime (§7 MW-6a), never asserted. Its
expected value is **ا ح ر س ص ط ع ق ك ل م ن ه ي**.

### 1.1 Balance block — al-Zamakhsharī's five binary genera

Source: **al-Zamakhsharī, *al-Kashshāf*, ad Q 2:1, PageV01P028–029**, who enumerates the
memberships; corroborated by **al-Suyūṭī, *al-Itqān*, fawātiḥ nawʿ, PageV03P031**. Feature
table taken verbatim from H-NEW-2550 §3 (tuple T-A), which fail-fast-verified it against
al-Zamakhsharī's nine stated counts.

The classical claim is "**half of each genus**". For odd-sized genera exact half is not an
integer, so the faithful operationalisation is **deviation at the arithmetic floor**:
`| |S ∩ f| − |f|/2 | ≤ 0.5`. This is the form under which D_obs = 1.0 is the global minimum.

| ID | Genus | members | \|f\| | condition on \|S ∩ f\| | attested |
|:--|:--|:--|--:|:--|--:|
| **P1** | mahmūsa (voiceless) | ت ث ح خ س ش ص ف ك ه | 10 | = 5 | 5 |
| **P2** | shadīda (stops) | ا ب ت ج د ط ق ك | 8 | = 4 | 4 |
| **P3** | muṭbaqa (emphatic) | ص ض ط ظ | 4 | = 2 | 2 |
| **P4** | mustaʿliya (raised) | خ ص ض ط ظ غ ق | 7 | ∈ {3, 4} | 3 |
| **P5** | qalqala | ب ج د ط ق | 5 | ∈ {2, 3} | 2 |

P1 ∧ P2 ∧ P3 ∧ P4 ∧ P5 is exactly the event `D ≤ 1.0`, whose count H-NEW-2550 published as
1,024,500. Reproducing that number is MW-6h.

### 1.2 Frequency block

| ID | Property | condition | attested | source |
|:--|:--|:--|--:|:--|
| **P6** | corpus letter-mass share exceeds the uniform baseline | Σ freq(S) / 329,131 > **0.50** | 0.7441 | H-NEW-1810 **T3**, threshold 0.50 pre-locked there **before** observation |
| **P7** | overlap with the corpus top-14 by frequency | \|S ∩ TOP14\| ≥ **10** | 10 | H-NEW-1810 **T2-weak**; al-Suyūṭī *al-Itqān* nawʿ 6 |

`TOP14 = ا ل ن م ي و ه ت ر ب ك ع ف ق` (H-NEW-1810 rank 1–14; reproduced at runtime, MW-6d).

P6's threshold is a **theoretical constant** (the 50 % uniform baseline), not a value read
off the attested set; it was locked in H-NEW-1810's pre-registration before that finding's
observation. P7's threshold **is** the attested value, used as the standard
"at-least-as-extreme" event; this is disclosed and is why P7 also appears in the
self-directed control of §6.

### 1.3 Non-coincidence block

| ID | Property | condition | attested | source |
|:--|:--|:--|--:|:--|
| **P8** | the set does not coincide with any classical 14-cut | max over G1…G8 of Jaccard(S, G) ≤ **0.400** | 0.400 | H-NEW-69 (NULL on all 8) |

Groupings verbatim from `findings/phase-b-hypotheses/csv/h-new-69.json`
(SHA-256 `86d4796bc6dc2cc807565048f9ee7a1944f52bd5cc434e847481351d6bd56fb3`):

| G | name | source | members |
|:--|:--|:--|:--|
| G1 | shamsiyyah | al-Zamakhsharī *Mufaṣṣal* §82 | ت ث د ذ ر ز س ش ص ض ط ظ ل ن |
| G2 | qamariyyah | complement of G1 | ا ب ج ح خ ع غ ف ق ك م ه و ي |
| G3 | majhūra | Sībawayh *al-Kitāb* IV ch. 565 | ا ب ج د ذ ر ز ض ط ظ ع غ ق ل م ن و ي |
| G4 | mahmūsa | Sībawayh *al-Kitāb* IV ch. 565 | ت ث ح خ س ش ص ف ك ه |
| G5 | modern-voiced | Watson 2002 | ا ب ج د ذ ر ز ض ظ ع غ ل م ن و ي |
| G6 | modern-voiceless | Watson 2002 | ت ث ح خ س ش ص ط ف ق ك ه |
| G7 | ṣafīr | Sībawayh / al-Khalīl | ز س ص |
| G8 | iṭbāq | Sībawayh / al-Mubarrad | ص ض ط ظ |

Jaccard(S, G) = |S ∩ G| / |S ∪ G| = k / (14 + |G| − k), monotone increasing in k.
**Declared in advance: G8 ≡ P3's muṭbaqa set. P8 and P3 are therefore not independent by
construction, and §5 must report it.**

### 1.4 Orthographic and articulatory block

| ID | Property | condition | attested | source |
|:--|:--|:--|--:|:--|
| **P9** | sonorant enrichment | \|S ∩ {ر ل م ن و ي}\| ≥ **5** | 5 | H-NEW-69 §"striking observation" (**post-hoc there**); H-NEW-2550 §4 T-F (largest deviation term) |
| **P10** | dotless preference | \|S ∩ DOTLESS\| ≥ **11** | 11 | H-NEW-60 (STRONG-PASS-DIRECTED, p = 0.000919) |
| **P11** | pharyngeal/glottal exhaustivity | \|S ∩ {ا ه ع ح}\| = **4** | 4 | H-NEW-44.2.1 (PASS-DIRECTED, p = 0.049) |

`DOTLESS = ا ح د ر س ص ط ع ك ل م ه و` (13 letters, H-NEW-60 per-letter table).

**MW-7 disclosure.** P9 was noticed post-hoc in H-NEW-69 and explicitly excluded from its
Bonferroni family. P10 was noticed post-hoc in H-NEW-60 (its §"Honest caveats" 1). P11 is
PASS-DIRECTED at single-test α only. All three are carried here **MW-7-capped**: the
shrinkage curve is reported with and without the {P9, P10, P11} block (§4.4), and no verdict
may rest on the capped block alone.

### 1.5 Properties considered and REJECTED before the lock

Recorded so the property list cannot be quietly expanded later:

- *"Contains exactly the letters ح س ص ط outside the frequency top-14"* — **rejected**:
  reverse-engineered from the attested set; names its members.
- *"Contains ≥ 2 emphatics"* — **rejected**: identical to P3 by construction on the attested
  value; adds no information.
- *"Contains the 5 letters of one of the attested muqaṭṭaʿāt strings"* — **rejected**:
  reverse-engineered.
- *"Abjad-value sum falls in a given range"* — **rejected**: no pre-existing pre-registered
  finding fixes the range; would be a free parameter (H-NEW-1810 candidate #3 is untested).
- *"H-NEW-165 codebook ṣifāt balance"* — **rejected as a declared property**: the attested
  set does **not** have it (H-NEW-2550 T-F puts it at percentile 51.05). Criterion (a) fails.
- *"Divisibility of muqaṭṭaʿāt letter counts by 19"* — **rejected**: H-NEW-1740 falsified it
  (1/29, chance-level); the attested set does not have the property in any general form.

### 1.6 Property count

**11 declared properties.** This number is locked. No property may be added after the first
count is computed; if one is, this file's SHA changes and the run voids itself.

---

## 2. Rules-tuples — ≥ 2, both run, both reported

**RT-1 (primary).** `(no-tashkeel graphemes for frequency, full-tashkeel for locus detection,
28-letter ḥurūf al-muʿjam, hamza folded into alif, basmala-as-v.1-of-Q1-only, Ḥafṣ-Kūfan,
Mashriqī)` with the **al-Zamakhsharī five-genus taxonomy** (H-NEW-2550 tuple T-A) supplying
the balance block P1–P5. Identical to H-NEW-2550's primary tuple.

**RT-2 (mandatory second taxonomy).** Identical rules-tuple, but the balance block is
replaced by the **later tripartite tajwīd manner taxonomy** (H-NEW-2550 tuple T-C):
shadīd (8) / bayniyya {ر ع ل م ن} (5) / rikhw (15), plus mahmūsa, muṭbaqa, mustaʿliya,
qalqala — **seven** genera. H-NEW-2550 §4 showed this taxonomy collapses the single-axis
result to the null median (percentile 55.67).

**Pre-declared consequence, stated before running.** Under RT-2 the attested set takes
**5 of 5** bayniyya letters and **5 of 15** rikhw letters. Both deviate from the floor.
Therefore under RT-2 the two extra genus-balance properties are **properties the attested
set does not have**, and criterion (a) excludes them from the conjunction. The RT-2 arm
must report this explicitly rather than silently dropping them: **2 of RT-2's 7 balance
properties FAIL on the attested set**, and the RT-2 conjunction is consequently built from
the 5 genera the two taxonomies share.

**RT-1b / RT-2b (aggregate form, reported alongside).** Because the per-genus form makes RT-2
degenerate, both taxonomies are also run with the balance block collapsed to the single
H-NEW-2550 statistic `D_taxonomy(S) ≤ D_taxonomy(attested)` — the event whose exact
probability H-NEW-2550 published (2.5538 % under T-A; 55.6716 % under T-C). This yields a
genuinely different joint count under the two taxonomies and is the honest way to satisfy
the two-taxonomy requirement. Direction (low D) is locked, as in H-NEW-2550.

---

## 3. Null model and enumeration

**Uniform over all C(28,14) = 40,116,600 fourteen-letter subsets, enumerated EXACTLY.** No
sampling. H-NEW-2550 proved this tractable. Enumeration is by meet-in-the-middle over the
two 14-letter halves of the alphabet; the total must equal C(28,14) exactly (MW-6g).

**The exact joint p** = (subsets satisfying all declared properties) / 40,116,600, reported
as an exact integer fraction, never as an estimate.

The frequency-weighted null (H-NEW-2550's N2) is **not** used here: it is a deliberately
biased null for a different question, and H-NEW-2550's own §5 states nothing rests on it.

---

## 4. Mandatory reporting — the shrinkage curve

### 4.1 The curve
Survivors after property 1; after 1+2; after 1+2+3; … through all 11. Reported as absolute
counts and as fractions of 40,116,600.

### 4.2 Order-dependence — MANDATORY
The curve is reported under, at minimum:
- **O1** the declared order P1 → P11;
- **O2** the exact reverse;
- **O3** most-restrictive-first (by marginal count — a data-dependent order, disclosed as such);
- **O4** least-restrictive-first;
- **O5** 500 uniformly random orderings, seed 20260509 — reporting min / median / max
  survivor count at each depth 1…11.

The **final** survivor count is order-invariant by definition (intersection is commutative);
the curve is not, and O5's envelope is what shows a reader whether the collapse is driven by
one property or by piling constraints on.

### 4.3 Marginals
Every property's standalone survivor count and fraction, reported in the same table.

### 4.4 MW-7-capped variant
The full curve is re-reported over the 8 properties {P1…P8} only, excluding the post-hoc /
directed block {P9, P10, P11}.

---

## 5. Independence between properties — MANDATORY

Over all 40,116,600 subsets, for every pair (i, j):
- P(i), P(j), P(i ∧ j);
- **lift** = P(i ∧ j) / (P(i)·P(j)) — lift = 1 means independent;
- **φ** (Matthews / mean-square-contingency coefficient).

Pre-declared reading rules, locked before observation:
- |φ| ≥ 0.5 or lift ≥ 2.0 → **NOT INDEPENDENT**; multiplying the two marginals is invalid
  and the finding must say so at the point of use.
- P(i ∧ j) = min(P(i), P(j)) → **NESTED** (one property implies the other); the pair carries
  the information of one property, not two.
- Otherwise → treat as approximately independent, with the measured lift reported anyway.

**Already known and declared in advance (§1.3): G8 ≡ muṭbaqa, so P8 and P3 share a class.**
Any further redundancy discovered is reported as a finding, not corrected away.

An **effective property count** is reported: the number of properties remaining after
collapsing every NESTED pair. The naive product Π P(i) is reported **only** alongside the
true joint P, with the discrepancy between them stated numerically — the gap between them is
the measure of how far the properties are from independent.

---

## 6. THE CRITICAL CONTROL — uniqueness by construction

**This is the single most important section of this pre-registration.** If a randomly drawn
14-subset can be made comparably unique by its *own* property profile, then near-uniqueness
is an artefact of the method, the joint p is meaningless, and the whole approach is retired.

### 6.1 Construction
Draw **1,000 uniformly random 14-subsets**, seed **20260509** (replication: a second
independent 1,000 at seed **20260519**). For a reference set X — either the attested
muqaṭṭaʿāt-14 or a random R — the eleven **same-kind** events are:

| kind | event E_i(X) |
|:--|:--|
| K1–K5 (balance) | { S : \|S ∩ f_i\| = \|X ∩ f_i\| }, f_i the five al-Zamakhsharī genera |
| K6 (mass) | { S : mass(S) > 0.50 } — **fixed** threshold; if mass(X) ≤ 0.50, X lacks this property and it is dropped from X's profile |
| K7 (top-14 overlap) | { S : \|S ∩ TOP14\| ≥ \|X ∩ TOP14\| } |
| K8 (non-coincidence) | { S : maxJaccard(S) ≤ maxJaccard(X) } |
| K9 (sonorant) | { S : \|S ∩ SONORANT\| ≥ \|X ∩ SONORANT\| } |
| K10 (dotless) | { S : \|S ∩ DOTLESS\| ≥ \|X ∩ DOTLESS\| } |
| K11 (pharyngeal) | { S : \|S ∩ PHARYNGEAL\| ≥ \|X ∩ PHARYNGEAL\| } |

K6's threshold is fixed for every X because it is a theoretical constant (§1.2), not a value
read off a set. The **identical** rule is applied to the attested set to produce W_obs, so the
comparison is like-for-like. W_obs under this rule is **not** the same number as the declared
conjunction of §1 (K1–K5 use equality where P4/P5 use the floor interval); both are reported.

### 6.2 Two control variants, both run
- **Control-1 (direction-locked)**: directions exactly as in the table above.
- **Control-2 (self-directed) — PRIMARY**: for K7 and K9–K11, the inequality points **away
  from the null median** on the side where X actually falls. This does not penalise a random
  R for sitting below the median on an axis where the attested set sits above it, and is the
  fairer and stronger guard. K1–K5 (equality) and K6 (fixed) are unchanged.

### 6.3 Reported quantities
For each of the 1,000 draws: the survivor count W_r under its own profile; the number of
declared §1 properties it happens to satisfy; and the full distribution of W_r
(min / quartiles / median / max, and the count of draws achieving W_r = 1).

### 6.4 Decision rule — LOCKED
Let `q = #{ r : W_r ≤ W_obs } / 1000` under **Control-2**.

- **CONTROL-PASSED** iff **q < 0.05**.
- **CONTROL-FAILED** iff **q ≥ 0.05** — i.e. at least 1 random 14-subset in 20 achieves at
  least as much uniqueness from its own profile as the muqaṭṭaʿāt do from theirs.

---

## 7. Verdict rule — LOCKED BEFORE OBSERVATION

Let **W** = survivors of the declared 11-property conjunction of §1 under RT-1.

| W | control | **VERDICT** |
|:--|:--|:--|
| W = 1 | CONTROL-PASSED | **JOINT-CONJUNCTION-REMARKABLE** — report at full strength with all caveats |
| 2 ≤ W ≤ 100 | CONTROL-PASSED | **JOINT-CONJUNCTION-NEAR-UNIQUE** — report, weaker than above |
| W ≤ 100 | CONTROL-FAILED | **ARTEFACT-OF-CONSTRAINT-STACKING** — the honest verdict; retires the approach and is a more valuable result than a positive one |
| W > 100 | either | **CONJUNCTION-ADDS-NOTHING** — H-NEW-2550's CONFIRMED-BUT-MEANINGLESS stands; control reported regardless |
| W = 0 | either | **PRE-COMMIT VIOLATION** — impossible unless a property is misdefined; run voids, published as such |

W = 0 is impossible if every declared property genuinely holds of the attested set; a zero is
therefore a self-check on §1 and is treated as an error condition, not a result.

**No verdict may be upgraded by the RT-1b/RT-2b aggregate arms, by RT-2, or by the
MW-7-capped variant. They may only corroborate or contradict.**

---

## 8. MW-1 … MW-7 compliance

- **MW-1** instrument-prior: all 11 properties, both taxonomies, all thresholds, all
  orderings, both control variants and every verdict label are fixed in this file before the
  first survivor count.
- **MW-2** corpus-prior: the null is **exact over the entire subset space**; no sampling.
- **MW-3** alternative models: 2 taxonomies × (per-genus and aggregate balance forms) ×
  (full and MW-7-capped property sets), all reported, none dropped.
- **MW-4** over-fitting: no fitted parameters. Every threshold is either a classical
  enumeration, a constant locked in a prior pre-registration, or the attested value used as a
  standard at-least-as-extreme event (disclosed per property in §1).
- **MW-5** replication: the control is re-drawn at seed 20260519; the exact enumeration is
  deterministic and needs none.
- **MW-6** instrument-control, all fail-fast at runtime with `assert`:
  - **a** 30 muqaṭṭaʿāt loci in exactly 29 surahs, 0 false positives, union exactly 14
    letters, surah list identical to H-NEW-1740 §1, derived from the corpus and never asserted;
  - **b** derived 14 == al-Zamakhsharī's enumerated fourteen;
  - **c** feature table reproduces al-Zamakhsharī's nine stated counts (mahmūsa 5, majhūra 9,
    shadīda 4, rikhwa 10, muṭbaqa 2, munfatiḥa 12, mustaʿliya 3, munkhafiḍa 11, qalqala 2);
  - **d** letter frequencies reproduce all 28 H-NEW-1810 counts, total 329,131, hamza 1,578,
    and the TOP14 list;
  - **e** H-NEW-69's eight groupings reproduce its published overlaps k = 6, 8, 9, 5, 7, 7,
    2, 2 and its max Jaccard 0.400;
  - **f** H-NEW-60's 11-of-13 dotless and H-NEW-44.2.1's 4-of-4 pharyngeal reproduce;
  - **g** the enumeration total == C(28,14) == 40,116,600 exactly;
  - **h** the P1∧…∧P5 count == **1,024,500** and its fraction == 0.025538…, reproducing
    H-NEW-2550 §3 independently through a different engine;
  - **i** G8 iṭbāq == muṭbaqa asserted **equal**, so the §1.3 redundancy disclosure cannot
    silently become false;
  - **j** every declared property asserted TRUE of the attested set (guards W = 0).
- **MW-7** post-hoc cap: {P9, P10, P11} are MW-7-capped; §4.4's 8-property curve is the
  uncapped result.

---

## 9. Integrity, files, and the garden of forking paths

**Frozen inputs, SHA-256:**

| file | SHA-256 |
|:--|:--|
| `quran-text/quran-full-tashkeel.json` | `382a7341300602ec8b366316d4bbe2a44955c2bf984d395bdd82dae6110b6715` |
| `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |
| `findings/phase-b-hypotheses/csv/h-new-69.json` | `86d4796bc6dc2cc807565048f9ee7a1944f52bd5cc434e847481351d6bd56fb3` |
| `findings/phase-b-hypotheses/scripts/h-new-2550.py` | `87aeabfff8c25d4563e77db1f9b5f59d202f824fb33a08e1606f2febe3c7264a` |

**Files:**
- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2670-joint-conjunction.md` (this file)
- script: `findings/phase-b-hypotheses/scripts/h-new-2670.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2670.json`
- immutable run dir: `runs/h-new-2670/<UTC timestamp>/` — **never deleted, including
  superseded or uncommitted runs**
- finding: `findings/phase-b-hypotheses/h-new-2670-joint-conjunction.md`

**Dependency disclosure.** numpy is used, a declared deviation from Protocol §7.1, for the
same reason H-NEW-2550 declared it: the null is an exact enumeration of 40,116,600 subsets.
A stdlib-only guard re-derives the joint survivor count independently.

**Garden of forking paths — decisions made BEFORE any count, recorded here:**
1. The balance block is operationalised at the **arithmetic floor**, not at strict equality,
   because "half of each genus" cannot mean equality for odd-sized genera. The strict-equality
   variant is what §6's control uses, and both are reported.
2. P6's threshold is 0.50 because H-NEW-1810 locked it there; no other value was considered.
3. P7, P9, P10, P11 use the attested value as an at-least-as-extreme cut. This is disclosed
   per property and is precisely why the control of §6 exists.
4. G2, G4, G6 are complements of G1, G3, G5 and G8 equals muṭbaqa; the Jaccard maximum in P8
   is taken over all eight regardless, as H-NEW-69 did.
5. 1,000 control draws, not 10,000, so the control's own survivor counts remain exactly
   computable over the full 40.1 M space within the run budget. The replication seed doubles
   this to 2,000 effective draws.
6. No property will be added, removed, or re-thresholded after the first count. If the joint
   count comes out at 1, that is reported **with** the control result attached in the same
   sentence, never alone.

**A small number is not the goal of this test.** If §6 shows the method makes anything
unique, that is the finding, and it will be stated plainly and prominently.

---

*Locked 2026-08-07 by Waiel Al-Shujaa, before any survivor count.
Bismillāhi al-Raḥmāni al-Raḥīm.*
