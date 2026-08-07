---
id: H-NEW-2670
title: Joint conjunction improbability — the muqaṭṭaʿāt-14 under ALL declared constraints simultaneously, and the property-selection artefact that voids it
date: 2026-08-07
phase: B
status: ARTEFACT-OF-CONSTRAINT-STACKING — locked rule returned NEAR-UNIQUE (W=7, q=0.018); a stricter post-observation control FAILS at q'=0.248
verdict: >-
  The exact joint count is **W = 7 of 40,116,600** (p = 1.745×10⁻⁷) — the attested
  muqaṭṭaʿāt-14 and six alternatives. The pre-registered control passes narrowly
  (q = 0.018). A stricter post-observation control, which lets each random 14-subset choose
  its own eleven axes from the same 33-axis attested menu, **FAILS at q' = 0.248**: one
  random subset in four becomes at least as unique as the muqaṭṭaʿāt, and 3.8 % reach
  W' ≤ 7 outright. Near-uniqueness here is manufactured by property selection, not found in
  the letters. The honest verdict is ARTEFACT. H-NEW-2550's CONFIRMED-BUT-MEANINGLESS stands
  untouched, and the one residue with content is that all six alternatives admit **و**.
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260519
n_exact: 40116600
n_distinct_profiles: 7887764
prereg_sha256: d6c5a48179585f665c5563f7357629ebb616bb00d075bf4fac2032034615fe7c
rules_tuple: (no-tashkeel graphemes, full-tashkeel for locus detection, 28-letter ḥurūf al-muʿjam, hamza folded into alif, basmala-as-v.1-of-Q1-only, Ḥafṣ-Kūfan, Mashriqī) + RT-2 tripartite-tajwīd taxonomy arm
parents: [H-NEW-2550, H-NEW-69, H-NEW-60, H-NEW-44.2, H-NEW-44.2.1, H-NEW-1810, H-NEW-1730, H-NEW-1740, H-NEW-165]
---

# H-NEW-2670 — Joint conjunction improbability

**Pre-registration locked and untouched at SHA-256 `d6c5a481…fe7c`, runtime-verified, with
four frozen input SHAs. Null computed EXACTLY over all 40,116,600 subsets — not sampled —
and independently re-derived by a stdlib-only engine. Seed 20260509, replication 20260519.**

## TL;DR

H-NEW-2550 tested the muqaṭṭaʿāt letters one axis at a time under Bonferroni k = 28.
Bonferroni controls a **union**; it cannot answer the **intersection** question. This test
answers it.

**Eleven properties were declared before counting, each one the muqaṭṭaʿāt demonstrably
have and each one motivated by a classical source or a prior pre-registered finding. Exactly
7 of the 40,116,600 possible 14-letter subsets satisfy all eleven. p_exact = 7/40,116,600 =
1.745 × 10⁻⁷.**

That number looks decisive. It is not, and the reason is the whole value of this finding:

- **The pre-registered control passes only narrowly.** Give a random 14-subset the same
  eleven property *kinds* at its own values, and 18 of 1,000 become at least as unique as the
  muqaṭṭaʿāt (replication 12/1,000). q = 0.018 against the locked α = 0.05.
- **A stricter control fails outright.** The eleven axes were not chosen at random — they are
  the survivors of sixteen prior tests run against this one letter-set. Give every subset the
  same privilege (choose your own best eleven axes from a 33-axis menu, every axis attested
  in a classical source or a prior locked finding) and **q' = 0.248**. One random 14-subset in
  four reaches the muqaṭṭaʿāt's level of uniqueness; **38 in 1,000 reach W' ≤ 7 outright**;
  two in 1,000 achieve W' = 1, perfect uniqueness. Replication: 0.265, 40, 2.
- **The gap between q = 0.018 and q' = 0.248 is the size of the property-selection effect**,
  and it is an order of magnitude. The eleven-fold conjunction does not measure the letters.
  It measures how many axes a researcher is allowed to pick.

**The one residue with real content:** the six non-attested survivors are all
one- or two-letter neighbours of the muqaṭṭaʿāt, and **every single one of them admits و**.
The entire discriminating power of the eleven-property conjunction, over and above what
H-NEW-69 and H-NEW-60 already published, reduces to the exclusion of a single letter — the
letter both of those findings independently flagged as anomalously excluded.

## 0. Prior art — what is NOT this finding's contribution

Stated in the pre-registration before the lock (§0.1), and repeated here so it cannot be
mistaken for new. Every **marginal** below was already published:

| Already published | value | source |
|:--|--:|:--|
| 14-set ties the al-Zamakhsharī 5-genus imbalance minimum; subsets tying it | 1,024,500 (2.5538 %) | H-NEW-2550 §3 |
| No coincidence with any of 8 classical 14-cuts; max Jaccard | 0.400 | H-NEW-69 |
| 11 of 13 dotless letters are muqaṭṭaʿāt | p = 0.000919 | H-NEW-60 |
| All 4 pharyngeal/glottal letters are muqaṭṭaʿāt | p = 0.048889 | H-NEW-44.2.1 |
| 5 of 6 sonorants are muqaṭṭaʿāt | p = 0.082367 | H-NEW-69 (post-hoc there) |
| The 14 carry 74.41 % of corpus letter mass | T3 PASS | H-NEW-1810 |
| Overlap with the corpus top-14 by frequency | k = 10 | H-NEW-1810 (T2 strong FALSIFIED) |

This run **reproduces every one of them to the published digit** — P10's marginal is exactly
H-NEW-60's 0.000919 and P11's is exactly H-NEW-44.2.1's 0.049, computed here by exhaustive
enumeration rather than closed-form hypergeometric. That agreement is MW-6, not a result.

**This finding's only contributions are:** the joint survivor count and the seven sets that
achieve it; the shrinkage curve and its order-dependence; the pairwise independence matrix;
and the two controls. Nothing else.

## 1. The eleven declared properties and their exact marginals

Locked before any count (pre-reg §1). Membership sets given in full there.

| ID | property | source | survivors | p |
|:--|:--|:--|--:|--:|
| **P1** | mahmūsa (10) split at floor: = 5 | al-Zamakhsharī, *al-Kashshāf* ad Q 2:1 | 12,252,240 | 0.3054157 |
| **P2** | shadīda (8) split at floor: = 4 | same passage | 12,932,920 | 0.3223833 |
| **P3** | muṭbaqa (4) split at floor: = 2 | same passage | 16,224,936 | 0.4044444 |
| **P4** | mustaʿliya (7) at floor: ∈ {3,4} | same passage | 24,690,120 | 0.6154589 |
| **P5** | qalqala (5) at floor: ∈ {2,3} | same passage | 27,041,560 | 0.6740741 |
| **P6** | corpus mass share > 0.50 | H-NEW-1810 T3 (0.50 pre-locked there) | 20,058,300 | **0.5000000** |
| **P7** | ≥ 10 of the corpus top-14 | H-NEW-1810 T2-weak | 1,142,975 | 0.0284913 |
| **P8** | max Jaccard vs 8 classical 14-cuts ≤ 0.400 | H-NEW-69 | 12,326,826 | 0.3072749 |
| **P9** | ≥ 5 of 6 sonorants | H-NEW-69 post-hoc  **[MW-7]** | 3,304,290 | 0.0823672 |
| **P10** | ≥ 11 of 13 dotless | H-NEW-60  **[MW-7]** | 36,870 | 0.0009191 |
| **P11** | all 4 pharyngeal/glottal | H-NEW-44.2.1  **[MW-7]** | 1,961,256 | 0.0488889 |

**P6 is exactly a coin flip, and the exactness is not a coincidence.** 20,058,300 is precisely
C(28,14)/2. Corpus mass is an integer out of the odd total 329,131, so no 14-subset can carry
exactly half, and every subset's complement carries the rest: **exactly half of all 14-subsets
carry more than 50 % of the corpus letter-mass, by symmetry.** H-NEW-1810's T3 "PASS" —
74.41 % against a locked 0.50 threshold — is therefore a property that 20,058,300 subsets
share. This is reported because it deflates a prior PASS, which is the direction that needs
no protection.

## 2. THE JOINT COUNT — and the seven sets

| | value |
|:--|--:|
| subsets enumerated (exact, not sampled) | **40,116,600** |
| distinct property-coordinate profiles | 7,887,764 |
| **survivors of all 11 declared properties** | **7** |
| **p_exact (exact fraction)** | **7 / 40,116,600 = 1.74491 × 10⁻⁷** |
| survivors of P1…P8 only (MW-7-capped) | 10,677 (p = 2.66149 × 10⁻⁴) |
| survivors of the balance block P1…P5 | 1,024,500 — reproduces H-NEW-2550 §3 |
| naive Π P(i) under independence | 0.0107 subsets |
| **true / naive** | **652 ×** |

Treating the eleven properties as independent would have predicted **0.011** surviving
subsets and thereby overstated the improbability by a factor of **652**. §4 shows why.

**The seven survivors, written out.** Nothing in this project has previously named the
alternatives; they are the whole reason the joint count is interpretable at all.

| # | the 14-letter set | difference from the muqaṭṭaʿāt | mass |
|:-:|:--|:--|--:|
| 1 | ا ت ح ر س ص ط ع ق ل م ن ه **و** | − ك ي  + ت **و** | 0.7505 |
| 2 | ا ت ح ر س ص ط ع ق ل م ه **و** ي | − ك ن  + ت **و** | 0.7459 |
| 3 | ا ث ح ر ص ط ع ق ك ل م ن ه **و** | − س ي  + ث **و** | 0.7293 |
| 4 | ا ح ر س ص ط ع ق ك ل م ن ه **و** | − ي  + **و** | 0.7433 |
| **5** | **ا ح ر س ص ط ع ق ك ل م ن ه ي** | **— the attested muqaṭṭaʿāt-14 —** | 0.7441 |
| 6 | ا ح ر س ص ط ع ق ك ل ن ه **و** ي | − م  + **و** | 0.7403 |
| 7 | ا ح ر ش ص ط ع ق ك ل م ن ه **و** | − س ي  + ش **و** | 0.7315 |

**All six alternatives contain و. Every one.** Two of them (#4, #6) differ from the attested
set by a single swap, and in both cases the swap is *into* و. The eleven-property conjunction
therefore does not isolate the muqaṭṭaʿāt from the alphabet; it isolates a **seven-member
neighbourhood** whose only systematic internal contrast is the presence or absence of wāw.

This is a direct convergence with two prior findings that flagged و independently and asked
for exactly this follow-up: H-NEW-69 ("**و appears to be systematically excluded** across
multiple muqaṭṭaʿāt-design axes despite being dotless, sonorant, and high-frequency. This
deserves its own follow-up pre-reg") and H-NEW-60 (و is one of only two dotless letters
excluded). H-NEW-2670 supplies the quantitative form of their observation: **conditional on
all eleven declared properties, excluding و is the whole of what remains.**

## 3. The shrinkage curve — MANDATORY, and violently order-dependent

The final count is order-invariant. The curve is not, and the spread is the point.

| ordering | survivors after each property |
|:--|:--|
| **O1 declared** P1→P11 | 12,252,240 → 3,917,760 → 1,524,600 → 1,155,216 → **1,024,500** → 512,250 → 16,127 → 10,677 → 4,532 → **21** → **7** |
| **O2 reverse** P11→P1 | 1,961,256 → 17,340 → 2,091 → 544 → 184 → 184 → 68 → 9 → 9 → **7** → **7** |
| **O3 most-restrictive-first** | 36,870 → 2,425 → 1,390 → 746 → 318 → 107 → 59 → 29 → **29** → 8 → **7** |
| **O4 least-restrictive-first** | 27,041,560 → 16,508,700 → 8,254,350 → 4,121,208 → 1,685,970 → 500,156 → 319,179 → 27,928 → 48 → 36 → **7** |
| **MW-7-capped** P1→P8 | … → **10,677** (stops here) |

**O5 — 500 uniformly random orderings, seed 20260509:**

| depth | min | median | max |
|--:|--:|--:|--:|
| 1 | 36,870 | 12,326,826 | 27,041,560 |
| 2 | 2,425 | 1,123,902 | 16,508,700 |
| 3 | 780 | 218,460 | 8,254,350 |
| 4 | 169 | 30,931 | 4,121,208 |
| 5 | 51 | 3,461 | 1,615,860 |
| 6 | 30 | 712 | 833,987 |
| 7 | 9 | 145 | 51,724 |
| **8** | **7** | 56 | 27,928 |
| 9 | 7 | 24 | 4,532 |
| 10 | 7 | 9 | 36 |
| 11 | 7 | 7 | 7 |

**What the curve shows, and it is not flattering.** Under a favourable ordering the count is
already at its floor of 7 after **eight** properties; the median random ordering is at 9 after
ten. Three properties do essentially all the work — P10 (dotless, p = 0.00092), P7 (top-14,
p = 0.0285) and P11 (pharyngeal, p = 0.0489) — and each of those three is a **published
prior finding in its own right**. O3 makes this explicit: the first two properties alone take
40.1 M down to 2,425, and the last five together take 107 down to 7. In O3, **P6 removes
nothing at all** (29 → 29). This is a curve that collapses because a few strong pre-existing
results are being re-used, not because eleven independent constraints happen to intersect.

## 4. Independence — the properties are NOT independent, and one dependency the locked rule missed

Measured over all 40,116,600 subsets. Locked reading rules (pre-reg §5): |φ| ≥ 0.5 or
lift ≥ 2.0 → NOT INDEPENDENT; P(i∧j) = min(P(i),P(j)) → NESTED.

**NOT INDEPENDENT by the locked rule — 4 of 55 pairs:**

| pair | P(i∧j) count | lift | φ | mechanism |
|:--|--:|--:|--:|:--|
| P10 × P11 | 17,340 | **9.620** | +0.059 | **PHARYNGEAL ⊂ DOTLESS** — all 4 of ا ه ع ح are dotless, so demanding ≥11 of 13 dotless nearly forces all 4 |
| P7 × P9 | 495,055 | **5.259** | +0.219 | **SONORANT ⊂ TOP14** — all 6 of ر ل م ن و ي are corpus rank 1–14, so demanding ≥10 of the top-14 pulls the sonorants in |
| P7 × P10 | 2,425 | 2.308 | +0.007 | shared high-frequency/dotless letters |
| P9 × P10 | 6,801 | 2.239 | +0.011 | 4 of 6 sonorants (ر ل م و) are dotless |

**A dependency the locked rule fails to flag, reported because it is real.** P1 × P8 has
lift 1.811 and φ = +0.358 — under the locked thresholds it is classed "approximately
independent". It is not. P8's Jaccard bound is algebraically equivalent to a set of interval
constraints, and because **H-NEW-69's G4 ≡ mahmūsa** and **G8 ≡ muṭbaqa** (both asserted
equal at runtime, MW-6i), the G3/G4 clause of P8 reduces exactly to

> P8 ⟹ |S ∩ mahmūsa| ∈ {5, 6},  |S ∩ shamsiyyah| ∈ {6,7,8},  |S ∩ modern-voiced| ∈ {7,8}

and P1 sets |S ∩ mahmūsa| = 5. **P1 therefore absorbs one of P8's three binding clauses
outright**, and P8's clauses on G7 (ṣafīr) and G8 (iṭbāq) are non-binding for every 14-subset
— the maximum attainable Jaccard on a 3- or 4-letter class is below 0.400. So P8 is not one
property but three, one of which is redundant with P1 and two of which are vacuous. The
locked |φ| ≥ 0.5 / lift ≥ 2.0 rule was too coarse to see this. **The rule is reported as
locked and its failure is reported alongside it**; no threshold was adjusted after
observation.

The pre-registered "effective property count" therefore reads **11** by the locked rule and
is honestly **lower** — the true joint count exceeds the independence product by 652×, which
is the quantitative statement of the same fact.

## 5. THE CONTROL — the decisive section

### 5.1 The pre-registered control PASSES, narrowly

Pre-reg §6: 1,000 random 14-subsets; each described on the **same eleven property kinds** at
its own values; count how many subsets share its profile.

| variant | seed | q = #(W_r ≤ W_obs)/1000 | random W_r: min / median / max | #(W_r = 1) | #(W_r ≤ 10) |
|:--|--:|--:|:--|--:|--:|
| Control-1 direction-locked | 20260509 | **0.005** | 4 / 4,694 / 227,090 | 0 | 6 |
| Control-1 direction-locked | 20260519 | 0.003 | 2 / 4,877 / 195,423 | 0 | 6 |
| **Control-2 self-directed (PRIMARY)** | 20260509 | **0.018** | 2 / 710 / 57,966 | 0 | 27 |
| **Control-2 self-directed** | 20260519 | 0.012 | **1** / 622 / 46,455 | **1** | 25 |

`W_obs = 7` under the identical rule. **CONTROL-PASSED** at the locked α = 0.05 — but by a
factor of under 3, and the replication already produced **one random 14-subset with
W_r = 1 — strictly more unique than the attested set's 7.**

One genuinely favourable result: a random 14-subset satisfies on average only **3.34 of the
11 declared properties** (max observed 8; **not one of the 2,000 draws reached 9, 10 or 11**).
The declared conjunction is not trivially satisfiable.

### 5.2 The property-selection control FAILS — decisively

**This control is post-observation, MW-7-capped, and demote-only. It was written after the
primary run, the pre-registration was not modified, and its SHA gate was re-verified
unchanged before it ran.**

The pre-registered control has a blind spot it cannot see past: **it holds the eleven axes
fixed, and those axes were not chosen at random.** They are the survivors of a long series of
prior tests aimed at this one letter-set — H-NEW-44, 44.2, 44.2.1, 45, 46, 51, 53, 55, 56,
57, 60, 69, 165, 600, 1810, 2550. Holding them fixed hands the muqaṭṭaʿāt an advantage no
random subset receives.

So give every subset the same privilege. A **menu of 33 axes** (34 listed, deduplicated by
complement — a tail or balance event on a class is the identical event on its complement),
every axis attested in a classical source or a prior locked finding of this project:
al-Zamakhsharī's five ṣifāt, bayniyya, shamsiyyah, Watson voicing, ṣafīr, al-Khalīl's eight
places of articulation, H-NEW-60's four iʿjām classes, H-NEW-69's phonotactic classes,
H-NEW-1810's frequency strata, H-NEW-165's codebook, al-Suyūṭī's makhārij. Each reference set
picks the **eleven** axes on which it is most exceptional, and on each may claim whichever
attested property-kind serves it better — **TAIL** (enrichment/depletion, the kind H-NEW-60,
H-NEW-69 and H-NEW-44.2.1 use) or **BALANCE** (at-least-as-close-to-half, the kind
al-Zamakhsharī and H-NEW-2550 use). Same budget, same menu, same rule, for everyone.

| | seed 20260509 | seed 20260519 |
|:--|--:|--:|
| **q′ = #(W′_r ≤ W′_obs)/1000** | **0.248** | **0.265** |
| random W′: min / median / max | 1 / 235 / 18,869 | 1 / 216 / 42,862 |
| **# random subsets reaching W′ = 1** | **2** | **2** |
| **# random subsets reaching W′ ≤ 7** | **38** | **40** |

`W′_obs = 65` for the muqaṭṭaʿāt under the same free-choice rule.

**SUPPLEMENTARY-CONTROL-FAILED.** One random 14-subset in four becomes at least as unique as
the muqaṭṭaʿāt. Thirty-eight in a thousand reach **W′ ≤ 7 outright** — matching or beating
the declared conjunction's own count using axes they chose for themselves. Two in a thousand
are **perfectly unique**, which the attested set never is.

**What the muqaṭṭaʿāt actually pick when free to choose** is itself worth recording — and it
is not al-Zamakhsharī's balance:

| rank | axis | \|f\| | k | kind | p |
|--:|:--|--:|--:|:--|--:|
| 1 | dotless | 13 | 11 | tail | 0.000919 |
| 2 | one-dot | 10 | 1 | tail | 0.002212 |
| 3 | **bayniyya** | 5 | **5** | tail | 0.020370 |
| 4 | freq top-14 | 14 | 10 | tail | 0.028491 |
| 5 | freq top-7 | 7 | 6 | tail | 0.038406 |
| 6 | pharyngeal/glottal | 4 | 4 | tail | 0.048889 |
| 7 | sonorant | 6 | 5 | tail | 0.082367 |
| 8 | interdental | 3 | 0 | tail | 0.111111 |
| 9 | coronal sonorant | 3 | 3 | tail | 0.111111 |
| 10 | fricatives | 14 | 5 | tail | 0.128400 |
| 11 | freq bottom-7 | 7 | 2 | tail | 0.192271 |

**Not one of al-Zamakhsharī's five genera makes the cut** — every balance claim is beaten by
some enrichment claim. And the third-best axis the set can claim is **bayniyya at 5 of 5**,
the very intersection H-NEW-2550 §4 identified as the one that *destroys* al-Zamakhsharī's
balance under the tripartite taxonomy. Left to choose its own description, the muqaṭṭaʿāt-14
describes itself as an orthographic and sonority object, not a ṣifāt-balance object —
converging exactly on H-NEW-60 and H-NEW-69.

### 5.3 What the gap between the two controls measures

q = 0.018 → q′ = 0.248 is a **fourteen-fold** difference, produced by nothing but allowing
each subset to choose its own axes. That gap *is* the property-selection effect, measured.
The eleven-property conjunction is not measuring a feature of the letters; it is largely
measuring how many attested axes a researcher may select from after seeing the target.

One honest asymmetry in the free-choice rule, disclosed: it picks axes greedily by *marginal*
rarity, which is not the same as minimising the *joint* count. That is why W′_obs = 65
exceeds W = 7 — the declared list, assembled over years from findings that each looked at
this set, beats the set's own greedy self-description. **The same greedy rule is applied to
every random subset, so the q′ comparison is like-for-like**; and the fact that a
retrospectively assembled list outperforms greedy self-selection is itself further evidence
of the selection effect, not a defence against it.

## 6. Both taxonomies, as required

**RT-2, the later tripartite tajwīd taxonomy (H-NEW-2550 tuple T-C).** Pre-registered
prediction, made before the run and confirmed: the attested set takes **5 of 5 bayniyya** and
**5 of 15 rikhw**, both far from the floor. **Two of RT-2's seven genus-balance properties
are properties the attested set does not have**, so criterion (a) excludes them and the RT-2
conjunction is built from the five genera the taxonomies share. This is reported rather than
silently dropped.

**Aggregate-balance arms** (the H-NEW-2550 statistic `D ≤ D_obs` replacing P1…P5):

| arm | taxonomy | D_obs | balance alone | + P6…P11 | + P6,P7,P8 |
|:--|:--|--:|--:|--:|--:|
| RT-1b | al-Zamakhsharī 5 genera (T-A) | 1.0 | 1,024,500 (2.5538 %) | **7** | 10,677 |
| RT-2b | tripartite tajwīd (T-C) | 6.0 | 22,333,544 (55.6716 %) | **20** | 108,775 |

Both reproduce H-NEW-2550 §3–§4 to seven decimal places (MW-6h). **The joint count is
taxonomy-dependent: 7 under the taxonomy al-Zamakhsharī used, 20 under the one every modern
reciter learns — a factor of 2.9.** H-NEW-2550's taxonomy-specificity result survives the
move from single-axis to joint testing.

## 7. Verdict

**The locked rule (pre-reg §7) returns JOINT-CONJUNCTION-NEAR-UNIQUE**: W = 7 (in the
2 ≤ W ≤ 100 band) with CONTROL-PASSED at q = 0.018. That is what the pre-registration's own
machinery produced and it is recorded as such.

**The honest verdict is ARTEFACT-OF-CONSTRAINT-STACKING**, on the test's own pre-registered
decision language: *"Small survivor count but random subsets achieve similar → artefact of
constraint-stacking."* W = 7 is small; under the stricter control random subsets do achieve
similar, at q′ = 0.248 with 3.8 % reaching W′ ≤ 7. The pre-registered control was too weak to
see it because it fixed the axes; the stricter one was written afterwards, can only demote,
and does.

A demotion by a stricter post-observation guard is legitimate where a promotion would not be.
The pre-registration was not edited, its SHA gate was re-verified unchanged before the
supplementary run, and the locked verdict is published beside the demotion rather than
replaced by it.

**This retires the joint-conjunction approach for the muqaṭṭaʿāt.** The intersection question
was worth asking and is now answered: with a menu of attested axes this size, near-uniqueness
is available to roughly a quarter of all 14-subsets, so it cannot be evidence of design.

## 8. What this licenses, and what it forbids

**Licensed.**
1. The exact joint count is 7 of 40,116,600, verified by two independent engines. The seven
   sets are named in §2 and can be checked by hand.
2. The eleven declared properties are strongly **positively dependent**: the true joint count
   exceeds the independence product by 652×, with named structural mechanisms
   (SONORANT ⊂ TOP14; PHARYNGEAL ⊂ DOTLESS; P8's G3/G4 clause absorbed by P1; P8's G7/G8
   clauses vacuous). **Any future finding that multiplies muqaṭṭaʿāt property-probabilities
   together is wrong by about three orders of magnitude.**
3. H-NEW-1810's T3 threshold property (mass > 0.50) is satisfied by **exactly half** of all
   14-subsets, by an exact symmetry argument. It carries no information.
4. Conditional on all eleven properties, **the exclusion of و is the entire remaining
   content** — the substantive follow-up H-NEW-69 asked for, now quantified.

**Forbidden.**
- Any reading of p = 1.745 × 10⁻⁷ as a design signature, an improbability, or evidence of
  intentional selection. §5.2 settles it: a quarter of random 14-subsets reach comparable
  uniqueness on axes of the same kinds, and 3.8 % reach this exact count.
- Any claim that the eleven properties are independent, or any Bonferroni/product arithmetic
  that assumes they are.
- Any upgrade of H-NEW-2550. Its verdict — **CONFIRMED-BUT-MEANINGLESS, taxonomy-specific,
  zero of 28 cells clearing α_bon** — stands exactly as published; the intersection test does
  not rescue it, and §6 reproduces its numbers rather than revising them.

The project's standing pillar is untouched: the muqaṭṭaʿāt are **book-introduction markers**
and the **letter-axis is orthogonal to the content-axis** (al-Biqāʿī's content-*munāsaba*
FALSIFIED 4×; Protocol §3.7).

## 9. Honest limits

1. **The pre-registered control was too weak, and I did not see that until after the run.**
   Fixing the property *kinds* cannot detect a selection effect operating on the *choice* of
   kinds. The supplementary control repairs this, but it is post-observation and therefore
   MW-7-capped: it is admitted only because it demotes.
2. **The free-choice rule is greedy by marginal rarity, not optimal by joint count** (§5.3).
   Both the attested set and every random subset are handicapped identically, but neither is
   guaranteed its best possible eleven. A joint-optimal selection rule would lower every W′
   and is not computed here.
3. **The menu is a judgement call.** Thirty-three axes were included because each is attested
   in a source on disk or a prior locked finding; a larger menu would raise q′ and a smaller
   one would lower it. The menu is listed in full in the supplementary JSON so the choice is
   auditable. It was fixed before the supplementary control was run and no axis was added or
   removed after seeing q′.
4. **Three of the eleven declared properties (P9, P10, P11) were post-hoc-noticed or
   single-test-directed in their parent findings** and are MW-7-capped here. The
   MW-7-capped 8-property curve stops at W₈ = 10,677 — three orders of magnitude short of 7.
   **Essentially all of the collapse from 10,677 to 7 is carried by the capped block.**
5. **The locked independence rule (|φ| ≥ 0.5 or lift ≥ 2.0) is too coarse** and missed the
   P1 × P8 structural dependency (§4). It is reported as locked; the miss is reported beside it.
6. **1,000 control draws per seed** (2,000 with replication) bound q′ to about ±0.014 at the
   observed level. That precision is far more than the verdict needs — q′ = 0.248 is not near
   0.05 — but a larger control would tighten the tail statistics (#(W′ = 1) = 2 per 1,000).
7. **P4/P5 use the arithmetic-floor form** of "half of each genus"; the control uses strict
   equality. Both are reported. The floor form is the faithful reading of the classical claim,
   since 3.5 and 2.5 are not attainable counts.
8. **numpy is used**, a disclosed deviation from Protocol §7.1, for the exact 40.1 M-subset
   enumeration. A stdlib-only bitmask enumeration independently re-derives both
   W = 7 and the balance-block 1,024,500.

## 10. Amendment, and the garden of forking paths

- **The pre-registration was never edited.** Its SHA-256 `d6c5a481…fe7c` was verified at the
  start of the primary run and re-verified, unchanged, at the start of the supplementary
  control. There is no amended-hash chain in this finding.
- **The supplementary control (§5.2) is the one post-observation addition.** It adds a
  strictly stricter guard, is MW-7-capped, and by construction can only demote — it changes no
  locked property, no threshold, no direction, and no null model. It is the reason the
  headline verdict is ARTEFACT rather than the locked NEAR-UNIQUE.
- **Decisions made before any count** are logged in pre-reg §9 and were followed exactly:
  floor-form balance; P6's threshold at H-NEW-1810's pre-locked 0.50; P7/P9/P10/P11 as
  at-least-as-extreme events; the Jaccard maximum taken over all eight of H-NEW-69's
  groupings despite three being complements and one being identical to muṭbaqa; 1,000 control
  draws.
- **The RT-2 failure was pre-declared**, in the pre-registration, before the run: the
  attested set was predicted to fail both extra tripartite balance properties, and does. A
  runtime assertion would have fired had it not.
- **Properties rejected before the lock** are listed in pre-reg §1.5, including the tempting
  and inadmissible *"contains exactly ح س ص ط outside the frequency top-14"* — the property
  that would have named its own members.
- **Choices made after seeing the data:** the supplementary control, and nothing else.

## 11. MW-1 … MW-7 compliance

- **MW-1** instrument-prior: all eleven properties, both taxonomies, every threshold, all
  five orderings, both control variants and every verdict label fixed in the pre-registration
  before the first count.
- **MW-2** corpus-prior: the null is **exact over the entire subset space** — 40,116,600
  subsets, no sampling.
- **MW-3** alternative models: 2 taxonomies × 2 balance forms (per-genus, aggregate) × 2
  property sets (full, MW-7-capped) × 2 control variants + the supplementary control; all
  reported, none dropped.
- **MW-4** over-fitting: no fitted parameters; every threshold is a classical enumeration, a
  constant locked in a prior pre-registration, or a declared at-least-as-extreme event.
- **MW-5** replication: both controls re-run at seed 20260519 (q 0.018 → 0.012;
  q′ 0.248 → 0.265); the exact enumeration is deterministic.
- **MW-6** instrument-control, all fail-fast at runtime and all passed: 30 loci / 29 surahs /
  0 false positives with the 14 letters **derived from the corpus, never asserted**; derived
  14 == al-Zamakhsharī's fourteen; surah list == H-NEW-1740 §1; al-Zamakhsharī's nine stated
  counts reproduced; all 28 H-NEW-1810 frequencies + total 329,131 + hamza 1,578 + the TOP14
  list reproduced; H-NEW-69's eight overlaps (6, 8, 9, 5, 7, 7, 2, 2) and max Jaccard 0.400
  reproduced; H-NEW-60's 11-of-13 and H-NEW-44.2.1's 4-of-4 reproduced; enumeration total ==
  C(28,14); **P1∧…∧P5 == 1,024,500 exactly, reproducing H-NEW-2550 §3 through a different
  engine**; both aggregate arms reproducing H-NEW-2550 §4 to 7 d.p.; G8 == muṭbaqa and
  G4 == mahmūsa asserted **equal** so the redundancy disclosure cannot silently become false;
  every declared property asserted TRUE of the attested set (guarding W = 0); and a
  stdlib-only enumeration independently returning 7 and 1,024,500.
- **MW-7** post-hoc cap: P9, P10, P11 capped, with the 8-property curve reported separately;
  the entire supplementary control capped and demote-only.

## 12. Cross-references

- [[h-new-2550-muqattaat-phonetic-optimizer|H-NEW-2550]] — **the finding this corrects
  methodologically.** Its single-axis numbers are reproduced exactly here (1,024,500 / 2.5538 %
  under T-A; 55.6716 % under T-C) and its verdict is unchanged. What is corrected is the
  instrument: Bonferroni answered a union question, this answers the intersection question,
  and the answer is that the intersection is an artefact of axis choice.
- [[h-new-69-half-alphabet-split|H-NEW-69]] — source of P8 and P9 and of the eight groupings.
  Its و-exclusion note is the one substantive residue this test leaves standing (§2), and its
  G4 ≡ mahmūsa identity is the mechanism behind §4's missed dependency.
- [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] — source of P10, the single most
  restrictive property (p = 0.000919, reproduced exactly). It carries most of the shrinkage.
- [[h-new-44-2-poa-closure|H-NEW-44.2]] / H-NEW-44.2.1 — source of P11 (p = 0.048889,
  reproduced exactly) and of the POA menu axes.
- [[h-new-1810-letter-frequency|H-NEW-1810]] — source of P6 and P7. **§1 deflates its T3:**
  the mass > 0.50 property holds of exactly half of all 14-subsets.
- [[h-new-1730-muqattaat-letter-count-audit|H-NEW-1730]] / [[h-new-1740-khalifa-muqattaat-complete-audit|H-NEW-1740]]
  — the 29-surah catalogue used as an MW-6 cross-check, and the project's prior worked example
  of a selection effect (2 of 4 verifies collapsing to 1 of 29 at full scope). H-NEW-2670 is
  the same lesson on a different axis: **the survivors of a search look designed until you
  count what was searched.**
- [[h-new-165-phonological-predictor|H-NEW-165]] — supplies four menu axes.
- [[h-new-600-letter-families|H-NEW-600]] — content-cohesion NULL. Convergent: neither the
  content axis, nor the phonetic-balance axis, nor the joint conjunction of eleven axes
  carries a muqaṭṭaʿāt design signature.
- al-Zamakhsharī, *al-Kashshāf* ad Q 2:1, PageV01P028–029; al-Suyūṭī, *al-Itqān*, fawātiḥ nawʿ
  PageV03P031 and makhārij nawʿ 38 PageV01P346–348; al-Zamakhsharī, *al-Mufaṣṣal* §82;
  Sībawayh, *al-Kitāb* IV ch. 565; Watson 2002.

## 13. Files

- pre-reg (locked, unedited): `findings/phase-b-hypotheses/prereg-h-new-2670-joint-conjunction.md`
- primary script: `findings/phase-b-hypotheses/scripts/h-new-2670.py`
- supplementary control script: `findings/phase-b-hypotheses/scripts/h-new-2670-supplementary-control.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2670.json`,
  `findings/phase-b-hypotheses/csv/h-new-2670-supplementary-control.json`
- immutable run dirs (never deleted): `runs/h-new-2670/20260807T011646Z/`,
  `runs/h-new-2670/20260807T012414Z-supplementary-control/`
- this finding: `findings/phase-b-hypotheses/h-new-2670-joint-conjunction.md`

---

*H-NEW-2670 completed 2026-08-07 by Waiel Al-Shujaa. Seven sets in forty million is a small
number, and it means nothing, because a quarter of all fourteen-letter subsets can be made
just as rare by choosing which questions to ask them. The test was built to catch exactly
that, and it caught it. What survives is one letter: **و**. Bismillāhi al-Raḥmāni al-Raḥīm.*
