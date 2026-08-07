---
id: H-NEW-2550
title: The muqaṭṭaʿāt-14 as an articulatory-feature-space optimizer — al-Zamakhsharī's "half of each genus" against the exact C(28,14) null
date: 2026-08-07
phase: B
status: CONFIRMED-BUT-MEANINGLESS (primary) — TAXONOMY-SPECIFIC — 0 of 28 cells clear α_bon
verdict: >-
  CONFIRMED-BUT-MEANINGLESS and TAXONOMY-SPECIFIC. Under al-Zamakhsharī's own five genera
  the 14 sit at the GLOBAL MINIMUM of feature-imbalance over all 40,116,600 fourteen-letter
  subsets — and 1,024,500 subsets (2.554%) tie that minimum; p_exact = 0.025538 vs
  α_bon = 0.00178571. Under all five other classically-sourced taxonomies tested the claim
  is at or worse than chance (percentiles 3.6 / 17.9 / 26.1 / 51.1 / 55.7 / 78.8). ZERO of
  28 cells clear the corrected threshold. Confirms and extends H-NEW-69's NULL, which found
  the univariate form of this result first.
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260511
n_mc: 10000000
n_exact: 40116600
bonferroni_k: 28
alpha_bon: 0.00178571
prereg_sha256_lock: 3faabc4df31f794db38b6c9495b296501f23fd917c902f0275c9744c38b7d0ed
prereg_sha256_amended: 3b7bc7216c6c3eec00b6014dd2ffce978675f3a8cd7e0bfab1b814ccff288fdc
rules_tuple: (no-tashkeel graphemes, full-tashkeel for locus detection, 28-letter ḥurūf al-muʿjam, basmala-as-v.1-of-Q1-only, Hafs-Kūfan, Mashriqī) + 6 declared variants
parents: [H-NEW-69, H-NEW-44.2, H-NEW-1810, H-NEW-165, H-NEW-1740, H-NEW-600, H-NEW-60]
---

# H-NEW-2550 — Are the 14 muqaṭṭaʿāt letters an articulatory-feature-space optimizer?

**Binding pre-observation lock SHA-256 `3faabc4d…d0ed`; post-observation AMENDMENT A1
(prior-art disclosure + two added sensitivity arms + tightened correction)
`3b7bc721…8fdc`. Both runtime-verified. Seed 20260509, replication 20260511. Primary null
computed EXACTLY over all 40,116,600 subsets — not sampled. Bonferroni k = 28,
α_bon = 0.00178571.**

## TL;DR

al-Zamakhsharī (*al-Kashshāf* ad Q 2:1) and al-Suyūṭī (*al-Itqān*, fawātiḥ nawʿ) report
that the 14 muqaṭṭaʿāt letters take **half of every phonetic genus** — half the voiceless,
half the stops, half the emphatics, half the raised, half the qalqala letters — and both
enumerate the memberships. Every number they give is exactly right. This is the first
computation of what that is worth.

**Under al-Zamakhsharī's own taxonomy the 14 sit at the global minimum of imbalance — no
14-subset of the 28 can be more balanced — and 1,024,500 of the 40,116,600 possible
subsets (2.554 %) tie that same minimum.** One 14-letter subset in 39 is exactly as
"perfectly balanced" as the muqaṭṭaʿāt. `p_exact = 0.025538` against `α_bon = 0.00178571`.
**Zero of 28 pre-registered cells clear the corrected threshold.**

Two results carry the finding past a bare null:

- **The property is specific to the taxonomy al-Zamakhsharī used.** Against five other
  classically-sourced taxonomies — a hamza-split inventory, the later tripartite tajwīd
  manner-split, al-Suyūṭī's own 17- and 16-makhraj tables, and this project's
  independently-locked H-NEW-165 codebook — the muqaṭṭaʿāt-14 lands at percentile
  3.6 / 55.7 / 17.9 / 26.1 / 51.1, and at **78.8** once al-Khalīl's places of articulation
  are added. On the taxonomy every modern reciter learns, the claim is a coin flip.
- **The mechanism of the failure is a known result.** The one axis on which the muqaṭṭaʿāt
  *are* genuinely non-random — **sonority** (H-NEW-69: 5 of 6 Arabic sonorants are
  muqaṭṭaʿāt; H-NEW-60: dotless preference at p = 0.0009) — is not one of al-Zamakhsharī's
  five genera. Add a sonorant feature and the balance breaks (6 of 7, deviation 2.5, the
  single largest term in T-F).

## 0. Prior art — H-NEW-69 got the univariate form of this result first

**This section is the honest core of the finding and is placed before the results.**

| Finding | Question | Verdict |
|:--|:--|:--|
| **[[h-new-69-half-alphabet-split\|H-NEW-69]]** (2026-04-15) | Does the muq-14 **COINCIDE** with a classical 14-of-28 grouping? | **NULL** — 0/8 at α_bon = 0.00625; 0/8 even unprotected |
| **[[h-new-44-2-poa-closure\|H-NEW-44.2]]** (2026-04-16) | How do the muq-14 distribute over al-Khalīl's **8 POA classes**? | **NULL** — χ² = 12.67, df 7, perm p = 0.065 |
| H-NEW-44.2.1 | All 4 pharyngeal/glottal letters muqaṭṭaʿāt? | PASS-DIRECTED, p = 0.049 |
| [[h-new-60-muqattaat-dotless-preference\|H-NEW-60]] | Dotless preference | STRONG-PASS, 11/13, p = 0.0009 |
| [[h-new-165-phonological-predictor\|H-NEW-165]] / 165.2 | Locked tajwīd codebook; OQ-1 letter-set predictor | PASS-PRIMARY / ROBUST |

**How this test differs from H-NEW-69.** H-NEW-69 asked a **matching** question — *is the
muq-14 the same set as some classical grouping G?* (per-grouping hypergeometric on the
overlap k). H-NEW-2550 asks an **optimization** question — *does the muq-14 split every
genus near exact-half simultaneously?* (joint summed deviation D, exact enumeration over
the whole subset space).

**But the two are closer than that framing suggests, and the finding must say so.**
"Matches G" means k ≈ |G| or k ≈ 0 — **maximal** D. "Splits G at half" means k ≈ |G|/2 —
**minimal** D. Perfect balance and perfect matching are opposite ends of one axis.
H-NEW-69's headline is literally *"k = 9 vs E = 9.0 for majhūra, k = 5 vs E = 5.0 for
mahmūsa … a striking NULL — the muqaṭṭaʿāt selection is voicing-NEUTRAL"*, and it adds that
the observed split *"IS the expected ratio under random selection given the asymmetric
class sizes — not a meaningful pattern."* **That is this finding's thesis, stated
qualitatively and one genus at a time, four months earlier.**

H-NEW-2550's additive contribution is therefore narrower than it first appears, and is
exactly: **(i)** the joint statistic across all five genera at once rather than
genus-by-genus; **(ii)** the exact enumeration establishing that the joint value is the
**global optimum**; **(iii)** the exact **mass at that optimum** (2.554 %) — the number
per-grouping hypergeometrics cannot produce, and the number that converts "not significant"
into "one subset in 39"; **(iv)** the taxonomy-dependence result (§4); **(v)** the
frequency-conditioned null (§5). **It does not claim as new that the muqaṭṭaʿāt split the
classical genera at chance level. H-NEW-69 found that first.**

**Instrument corroboration.** Two prior independent pre-registrations reproduce four of
this test's five category memberships: H-NEW-69's G3 majhūra (|G| = 18, k = 9), G4 mahmūsa
(|G| = 10, k = 5) and G8 iṭbāq (|G| = 4, k = 2) are identical to §3's table; H-NEW-165's
locked codebook gives ḥurūf al-tafkhīm = {خ ص ض ط ظ غ ق} (= §3's mustaʿliya) and
qalqala = {ق ط ب ج د} (= §3's qalqala), both asserted equal at runtime. The fifth genus,
shadīda, is enumerated by al-Zamakhsharī himself. The feature table was therefore **not a
free researcher choice** — it is pinned by a fail-fast against al-Zamakhsharī's nine stated
counts *and* corroborated by two prior locks.

## 1. The classical claim — three attestations on disk, one negative result

**al-Zamakhsharī, *al-Kashshāf*, ad Q 2:1**, PageV01P028–029;
`data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt` (byte ≈ 36 088):

> … وجدتها **نصف أسامى حروف المعجم أربعة عشر سواء** … **في تسع وعشرين سورة** … ثم إذا نظرت
> في هذه الأربعة عشر وجدتها **مشتملة على أنصاف أجناس الحروف** … **من المهموسة نصفها**:
> الصاد، والكاف، والهاء، والسين، والحاء … **ومن الشديدة نصفها**: الألف، والكاف، والطاء،
> والقاف … **ومن المطبقة نصفها**: الصاد، والطاء … **ومن المستعلية نصفها**: القاف، والصاد،
> والطاء … **ومن حروف القلقلة نصفها**: القاف، والطاء.

**al-Suyūṭī, *al-Itqān*, fawātiḥ al-suwar nawʿ, PageV03P031**;
`…/raw/suyuti-itqan.openiti.raw.txt` (byte ≈ 717 265) — independent attestation, and the
warrant for the makhraj tuples:

> … فذكر منها **أربعة عشر حرفا وهي نصف جميع الحروف وذكر من كل جنس نصفه**: فمن **حرف
> الحلق** الحاء والعين والهاء، ومن **التي فوقها** القاف والكاف، ومن **الحرفين الشفهيين**
> الميم، ومن **المهموسة** السين والحاء والكاف والصاد والهاء …

al-Suyūṭī writes **الهمزة** where al-Zamakhsharī writes **الألف** (both read the muqaṭṭaʿāt
alif as the glottal stop — tuple T-B tests that fork); his munfatiḥa list has 11 members
against al-Zamakhsharī's 12, ل absent, recorded as a transmission omission and not silently
corrected.

**al-Rāzī gives only the WEAK form** — a negative result, reported as such.
*Mafātīḥ al-ghayb* ad Q 2:1, ≈ PageV02P257 (`…/raw/razi-mafatih-al-ghayb.openiti.raw.txt`
byte ≈ 628 493): *"نصف أسامي حروف المعجم: أربعة عشر سواء … في تسع وعشرين سورة"* — 14 = half
the alphabet, in 29 surahs, **no per-ṣifa breakdown**. Diacritic-insensitive searches of the
full 29.7 MB raw for المهموسة / المطبقة / المستعلية / أجناس الحروف return his ḍād-vs-ẓāʾ
tajwīd discussion (≈ byte 124 517) and unrelated hits, not the fawātiḥ passage. **The strong
form is attributable to al-Zamakhsharī and al-Suyūṭī only.**

## 2. The 14 letters — derived from the corpus

A detector that never names the letters it seeks: the first whitespace token of verses 1 and
2 of every surah in `quran-text/quran-full-tashkeel.json` is a muqaṭṭaʿāt token **iff it
carries no ordinary vocalisation** (no U+064B–U+0652, no U+0670). Across **228 scanned
tokens**: **30 loci in exactly 29 surahs** (Q 42 twice), **zero false positives**, union of
**exactly 14** graphemes — **ا ح ر س ص ط ع ق ك ل م ن ه ي** — identical to al-Zamakhsharī's
fourteen and to H-NEW-1740 §1's catalogue. All fail-fast asserted.

## 3. PRIMARY RESULT — T-A × H1 × N1 (the claim as stated, exact null)

`D(S) = Σ_f | |S ∩ f| − |f|/2 |` over al-Zamakhsharī's five binary genera.

| Genus | \|f\| | in the 14 | half | deviation |
|:--|--:|--:|--:|--:|
| mahmūsa (voiceless) | 10 | **5** | 5.0 | **0.0** |
| shadīda (stops) | 8 | **4** | 4.0 | **0.0** |
| muṭbaqa (emphatic) | 4 | **2** | 2.0 | **0.0** |
| mustaʿliya (raised) | 7 | **3** | 3.5 | **0.5** |
| qalqala | 5 | **2** | 2.5 | **0.5** |
| | | | **D_obs** | **1.0** |

The two non-zero deviations are **unavoidable** — 3.5 and 2.5 are not integers, so 0.5 is
the floor. **D_obs = 1.0 is the global minimum over the whole subset space**
(`null_min = 1.0`). al-Zamakhsharī's description is not merely accurate; the set is
*optimal* for his own statistic.

**And that optimum is common:**

| Exact null over all C(28,14) = 40,116,600 subsets | value |
|:--|--:|
| D_obs | **1.0** |
| null minimum | **1.0** (obs **is** the global minimum) |
| **subsets tying the minimum** | **1,024,500** |
| **fraction tying the minimum** | **2.5538 %** |
| **p_exact (one-sided low, tie-inclusive)** | **0.025538** |
| null mean / SD / median | 4.4299 / 1.7781 / 4.0 |
| z of D_obs | −1.93 |
| α_bon (k = 28) | 0.00178571 |
| **verdict** | **CONFIRMED-BUT-MEANINGLESS** |

Stdlib-only uniform Monte Carlo (200,000 draws) returns 0.02582 vs the exact 0.025538 —
within 0.8 SE, on every tuple.

**One 14-subset in 39 is exactly as balanced as the muqaṭṭaʿāt.** "Half of each genus" is
the *expected value* of a random 14-subset (`E[|S∩f|] = |f|·14/28 = |f|/2` by symmetry), so
the null is centred on the claim and tightly concentrated. This is a combinatorial
inevitability wearing the clothes of a design signature — **the pre-registered most-likely
outcome (pre-reg §0) is the outcome**, and H-NEW-69's NULL had already lowered the prior in
exactly this direction.

## 4. THE DECISIVE RESULT — the property is specific to al-Zamakhsharī's taxonomy

| Tuple | taxonomy | source | D_obs | null min | **percentile** | p_exact |
|:--|:--|:--|--:|--:|--:|--:|
| **T-A** | al-Zamakhsharī's 5 genera | *al-Kashshāf* Q 2:1 | **1.000** | 1.000 | **2.55** | 0.025538 |
| T-B | + hamza ≠ alif (29 letters) | al-Suyūṭī's الهمزة; Sībawayh | 1.897 | 1.172 | 3.61 | 0.036109 |
| T-D | + al-Suyūṭī 17-makhraj | *al-Itqān* nawʿ 38, P347–348 | 11.000 | 8.000 | 17.90 | 0.178982 |
| T-E | + al-Suyūṭī 16-makhraj | *al-Itqān* nawʿ 38, P346 | 11.000 | 7.000 | 26.10 | 0.260996 |
| **T-F** | H-NEW-165 codebook ṣifāt | Ibn Jinnī / Watson / Holes | 6.000 | 3.000 | **51.05** | 0.510526 |
| **T-C** | tripartite manner (later tajwīd) | shadīd / bayniyya / rikhw | 6.000 | 2.000 | **55.67** | 0.556716 |
| **T-G** | H-NEW-165 ṣifāt + al-Khalīl 8-POA | + H-NEW-44.2 | 14.000 | 5.000 | **78.77** | 0.787691 |

**Only the taxonomy al-Zamakhsharī himself used puts the muqaṭṭaʿāt-14 near the optimum.**
Every other classically-sourced classification places it at or above chance. Two are worth
naming:

**T-C — the later tripartite manner split.** al-Zamakhsharī uses the **binary** shadīd/rikhw
division (his rikhwa list contains ل م ر ع ن). Later tajwīd interposes a five-member
**bayniyya** class. Under it the 14 take **all five** bayniyya letters (ر ع ل م ن — 100 %,
not 50 %, deviation 2.5) and only 5 of 15 rikhw (deviation 2.5). `D_obs = 6.0` is **exactly
the null median**, `p = 0.5567`.

**T-F / T-G — this project's own locked codebook.** Against H-NEW-165's independently
pre-registered tajwīd codebook the claim is at the median (51.1) and, once al-Khalīl's 8
places of articulation are added, **worse than chance** (78.8). The per-feature breakdown
names the culprit:

| T-F feature | \|f\| | in the 14 | half | deviation |
|:--|--:|--:|--:|--:|
| **sonorant** | 7 | **6** | 3.5 | **2.5** |
| idhlāq | 6 | 4 | 3.0 | 1.0 |
| mahmūs / stops / tafkhīm / pharyngealized / qalqala | — | — | — | 0.5 each |

**The muqaṭṭaʿāt are sonorant-enriched, and sonority is not one of al-Zamakhsharī's five
genera.** H-NEW-69 flagged this post-hoc (5 of 6 Arabic sonorants are muqaṭṭaʿāt, only و
excluded; hypergeometric p = 0.074) and H-NEW-60 found the convergent dotless preference at
p = 0.0009. H-NEW-2550 supplies the consequence: **the axis on which the set is genuinely
non-random is precisely the axis al-Zamakhsharī's taxonomy does not measure**, and adding it
destroys the balance. The "perfect half of every genus" holds on five hand-picked axes and
fails on the sixth — the one where a real signal lives.

## 5. The frequency-conditioned null — a real mechanism that misses the threshold

| | p (seed 20260509) | p (replication 20260511) | α_bon |
|:--|--:|--:|--:|
| T-A × H1 × N2 (corpus-frequency-weighted null) | **0.001828** | **0.001794** | 0.00178571 |

**This cell does NOT clear**, missing by 2.4 % (p/α = 1.024). Under the pre-reg's original
k = 20 it cleared; under the corrected k = 28 (§9) it does not. It is reported because the
**mechanism** is real and interpretable regardless of the threshold:

| 14-letter set | D |
|:--|--:|
| **the attested muqaṭṭaʿāt-14** | **1.0** |
| **top-14 by corpus frequency** (ا ل ن م ي و ه ت ر ب ك ع ف ق) | **7.0** |
| muqaṭṭaʿāt-14 with ح س ص ط swapped for ب ت ف و | **7.0** |

A frequency-driven selection takes **zero** emphatics (all of ص ض ط ظ rank 22–28 by corpus
frequency) and one mustaʿlī. The muqaṭṭaʿāt set does not, and **the whole difference is four
letters — ح س ص ط**, exactly H-NEW-1810's four "displacements". So: **the selection of the 14
was not driven by corpus frequency, and the four letters that break the frequency ranking
are the four that make al-Zamakhsharī's balance exact.** That gives H-NEW-1810's unexplained
anomaly a mechanism.

What it is not: N2 is a deliberately *biased* null modelling "selection by frequency alone".
Beating it would establish that frequency alone was not the rule, not that phonetic
optimisation was. The unbiased question is N1's, and N1 says 2.554 % of subsets match. The
cell misses the corrected threshold anyway; nothing here rests on it.

## 6. Full 28-cell table (Bonferroni k = 28, α_bon = 0.00178571)

| Tuple | N | feats | D_obs | H1 × N1 | H1 × N2 | D_freq | H2 × N1 | H2 × N2 |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| **T-A** primary | 28 | 5 | 1.000 | 0.025538 | 0.001828 | 0.6818 | 0.09275 | 0.02798 |
| T-B hamza ≠ alif | 29 | 5 | 1.897 | 0.036109 | 0.004775 | 0.6524 | 0.18959 | 0.08497 |
| T-C tripartite manner | 28 | 7 | 6.000 | 0.556716 | 0.090009 | 1.1928 | 0.33469 | 0.02446 |
| T-D + 17-makhraj | 28 | 21 | 11.000 | 0.178982 | 0.017696 | 7.8594 | 0.57352 | 0.23465 |
| T-E + 16-makhraj | 28 | 20 | 11.000 | 0.260996 | 0.026461 | 7.3594 | 0.65649 | 0.27170 |
| T-F 165-codebook ṣifāt † | 28 | 7 | 6.000 | 0.510526 | 0.026742 | 1.6881 | 0.90072 | 0.30402 |
| T-G 165 + 8-POA † | 28 | 15 | 14.000 | 0.787691 | 0.119362 | 4.6990 | 0.97174 | 0.59312 |

† post-observation arms (AMENDMENT A1), MW-7-capped in addition to the family α.

**ZERO of 28 cells clear α_bon.** **No cell is REVERSED** — the smallest H1 × N1 upper-tail p
is 0.617 (T-C) and the highest H2 × N1 percentile is 97.2 (T-G, still short of the tail); the
locked direction was never violated, so there is **no pre-commit violation**.

**T-D / T-E are a REPLICATION, not a discovery.** H-NEW-44.2 already tested the muq-14
against al-Khalīl's 8 POA classes and returned NULL (χ² perm p = 0.065). T-D/T-E ask the same
substantive question with a finer partition (al-Suyūṭī's 17/16 makhārij) and a different
statistic, and return the same answer (p = 0.179 / 0.261). This is **convergent replication
of H-NEW-44.2 under a new instrument**, and is not claimed as novel.

**H2 (frequency-weighted balance) fails everywhere.** On the mass axis the set is
systematically *over*-half — mahmūsa 57.6 %, shadīda 69.9 %, muṭbaqa 56.8 %, mustaʿliya
62.4 % of each genus's corpus mass — consistent with the 74.4 % total mass share this run
reproduces from H-NEW-1810 (T3 = 0.7441). The 14 are a **type-balanced but mass-unbalanced**
half. The one under-half genus is qalqala (28.5 %): the set takes the two low-frequency
qalqala letters (ق ط) and none of the three common ones (ب ج د).

## 7. What this licenses, and what it forbids

**Licensed.** (i) al-Zamakhsharī and al-Suyūṭī counted correctly — all nine stated
intersection counts are exact and the set is optimal for the statistic they implicitly
defined. (ii) The property is **taxonomy-specific**: it survives only under al-Zamakhsharī's
own five genera and fails under five other classically-sourced classifications, including
this project's own locked codebook. (iii) The muqaṭṭaʿāt selection was not governed by corpus
letter frequency, and the four letters proving it (ح س ص ط) are the four that make the
balance exact. (iv) The axis where the set *is* non-random is sonority/orthography
(H-NEW-69, H-NEW-60), not the ṣifāt al-Zamakhsharī enumerated.

**Forbidden.** Any claim that the muqaṭṭaʿāt letters were "selected to span articulatory
space" as a demonstrable design signature. The exact enumeration settles it: over a million
alternative 14-subsets are equally balanced, and no cell clears correction. **This closes the
phonetic-balance candidate that H-NEW-1810 left open** — its four candidates were phonetic
balance, theological association, abjad constraint, and a pre-Islamic alphabetic substrate;
the first is now tested and does not carry.

The project's standing pillar is untouched: the muqaṭṭaʿāt are **book-introduction markers**,
and the **letter-axis is orthogonal to the content-axis** (al-Biqāʿī's content-*munāsaba*
FALSIFIED 4×; [[h-new-600-letter-families|H-NEW-600]], Protocol §3.7).

## 8. Honest limits

1. **The observed statistic was known before the lock, and this was disclosed in advance**
   (pre-reg §0, §9): al-Zamakhsharī *enumerates* the memberships, so citing the passage
   reveals D_obs. What was unobserved — and is the entire empirical content — is the null
   distribution, its minimum, its minimum-mass and every p-value. The same disclosure covers
   T-C, where the 5/5 bayniyya intersection became visible while building the table.
2. **H-NEW-69 anticipated the conclusion at the univariate level** (§0). The original brief
   and the original pre-reg both missed it; the finding's additive contribution is the five
   items listed in §0 and no more.
3. **Four feature assignments rest on mnemonics not verified in this repository**: ب, ج,
   د ∈ qalqala and bayniyya {ر ع ل م ن} (Ibn al-Jazarī's قطب جد and لن عمر). ق and ط ∈ qalqala
   *are* on disk via al-Zamakhsharī; ب ∈ shadīda and ف ∈ mahmūsa are **derived by closure**
   from al-Zamakhsharī's stated halves. **T-C's collapse verdict depends on the
   mnemonic-sourced bayniyya class** — the standard class in every tajwīd tradition, but not
   verified in a file here. Acquiring a tajwīd primary source would close this.
4. **T-F/T-G are post-observation** (AMENDMENT A1) and MW-7-capped: they may corroborate or
   contradict but cannot by themselves establish a verdict. They contradict, which is the
   direction that needs no protection.
5. **H-NEW-165's codebook could not be used as the primary tuple**, for two reasons that are
   facts about it: its per-letter table covers only the 14 muqaṭṭaʿāt letters (D needs |f|
   over all 28, so completing it would be the unlogged degree of freedom the reuse
   instruction exists to prevent), and its voicing is modern-adjusted, placing **ق in
   mahmūs** where al-Zamakhsharī explicitly lists القاف among the majhūra taken by the 14.
   Its 28-letter-defined features *are* used, as T-F/T-G. Primacy was also locked before
   observation and cannot be reassigned after it.
6. **`D` weights every genus equally.** A salience weighting is defensible but the classical
   sources supply no weights, and inventing one is the forking freedom the protocol forbids.
7. **A modern IPA/distinctive-feature encoding is untested** — a different proposition from
   the classical claim; recorded as discarded-with-reason and flagged as a separate test.
8. **numpy is used**, a disclosed deviation from Protocol §7.1, justified by the exact
   40.1 M-subset enumeration; a stdlib-only guard agrees with every exact p.

## 9. Amendment, corrections, and garden of forking paths

- **AMENDMENT A1 (post-observation).** Adds prior-art disclosure (§0), adds tuples T-F/T-G,
  and **tightens** the family from k = 20 to k = 28. It changes no locked direction, no null
  model, no verdict definition, and not the primary tuple. Pre-reg §A1.5 requires T-A…T-E to
  reproduce bit-identically; this is **asserted at runtime** and passed.
- **Bonferroni arithmetic correction — consequential, disclosed.** A first draft of A1 wrote
  k = 24 (α_bon = 0.00208333). That was a slip: 7 × 2 × 2 = 28, α_bon = 0.00178571. The
  correction runs in the conservative direction and **removes this finding's only positive
  cell**: T-A × H1 × N2 (p = 0.001828) cleared at k = 24 and does not at k = 28. Applied
  because it is right, and recorded here precisely because it costs the finding its sole
  positive result. (Tightening self-verifies; only loosening would need ratification.)
- **Pre-reg erratum, corrected before any observation.** The first draft (SHA
  `4ec738f2…2c7c`) had C(29,14) = 67,863,915 instead of 77,558,760 — an arithmetic slip in an
  MW-6 constant. Corrected before any null was computed; binding lock is `3faabc4d…d0ed`.
- **Post-lock code change:** `verdict()` was corrected to implement the pre-registered
  decision *text* literally — the first draft returned CONFIRMED-BUT-MEANINGLESS for a tuple
  sitting exactly *at* the null median, which the pre-reg assigns to NULL. This demoted T-C
  and promoted nothing.
- **Choices made after seeing the data:** none beyond the amendment above, all of which
  tighten or disclose.
- **Alternative tuples considered and discarded:** lām-alif (لا) as a 29th letter — an
  orthographic ligature with no ṣifa or makhraj, so including it would require inventing
  feature values; modern IPA encoding — different proposition; ة/ى split — held to
  H-NEW-1810's normalisation for comparability.
- **Why this test:** H-NEW-1810 §Interpretation named "phonetic-articulation balance" as
  candidate #1 for the selection rule after falsifying the frequency reading, and left it
  untested.

## 10. MW-1 … MW-7 compliance

- **MW-1** instrument-prior: statistic, feature table, five tuples, both nulls, thresholds and
  all four verdict labels fixed before any null was computed; T-F/T-G added by disclosed
  amendment and MW-7-capped.
- **MW-2** corpus-prior: N1 is **exact over the entire subset space**; N2 uses 10⁷ draws.
- **MW-3** alternative models: 7 taxonomies × 2 statistics × 2 nulls = 28 cells, all reported,
  none dropped.
- **MW-4** over-fitting: no fitted parameters; `D` has no free constants.
- **MW-5** replication: N2 at seed 20260511 reproduces every cell to 3 s.f.; N1 is exact.
- **MW-6** instrument-control, all fail-fast at runtime: 30 loci / 29 surahs / 0 false
  positives; derived 14-set == al-Zamakhsharī's fourteen; surah list == H-NEW-1740 §1; letter
  frequencies reproduce all 28 H-NEW-1810 counts + total 329,131 + hamza 1,578; feature table
  reproduces al-Zamakhsharī's nine stated counts; category sizes 10/8/4/7/5/5; makhraj groups
  sum to 28 without overlap; enumeration totals == C(28,14) and C(29,14); **A1 arms**:
  H-NEW-165 tafkhīm == mustaʿliya and qalqala == qalqala asserted equal, the ق-voicing
  divergence asserted *present* so the §8.5 disclosure cannot silently become false,
  H-NEW-44.2's 8-POA asserted a partition of 28; **A1.5** T-A…T-E asserted bit-identical to
  the locked run. The exact engine was validated against full brute force on 5 randomised
  small cases before the first run.
- **MW-7** post-hoc cap: §5's swap contrast and the top-14-by-frequency contrast are
  descriptive and claim no p-value; T-F/T-G are MW-7-capped.

## 11. Cross-references

- [[h-new-69-half-alphabet-split|H-NEW-69]] — **primary parent**. Asked the *matching*
  question and returned NULL on 8 classical 14-cuts; found the univariate form of this result
  first (§0). H-NEW-2550 supplies the joint statistic, the exact null, the minimum-mass, the
  taxonomy-dependence and the frequency mechanism.
- [[h-new-44-2-poa-closure|H-NEW-44.2]] — **replicated** by T-D/T-E under a finer makhraj
  partition and a different statistic. Also the source of T-G's 8-POA partition.
- [[h-new-165-phonological-predictor|H-NEW-165]] + H-NEW-165.2 — source of the T-F/T-G
  codebook and independent corroboration of two category memberships. Its axis is **OQ-1**
  (which letter-set a surah gets), orthogonal to this test's question (whether the 14-letter
  inventory is balanced); no result of it is restated.
- [[h-new-1810-letter-frequency|H-NEW-1810]] — falsified the frequency reading and named the
  four displacements ح س ص ط; §5 supplies their mechanism and §7 closes its candidate #1.
- [[h-new-60-muqattaat-dotless-preference|H-NEW-60]] — dotless preference p = 0.0009;
  converges with §4's sonority finding on where the real signal lives.
- [[h-new-1740-khalifa-muqattaat-complete-audit|H-NEW-1740]] / H-NEW-1730 — the 29-surah
  catalogue used as an MW-6 cross-check.
- [[h-new-600-letter-families|H-NEW-600]] — content-cohesion NULL. **Convergent**: neither the
  content axis nor the phonetic-balance axis carries a muqaṭṭaʿāt design signature.
- al-Zamakhsharī, *al-Kashshāf* ad Q 2:1 PageV01P028–029; al-Suyūṭī, *al-Itqān* fawātiḥ nawʿ
  PageV03P031 + makhārij nawʿ 38 PageV01P346–348; al-Rāzī, *Mafātīḥ al-ghayb* ad Q 2:1
  ≈ PageV02P257 (weak form only); Ibn al-Jazarī, *al-Nashr*, quoted by al-Suyūṭī P348–349.

## 12. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2550-muqattaat-phonetic-optimizer.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2550.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2550.json`
- this finding: `findings/phase-b-hypotheses/h-new-2550-muqattaat-phonetic-optimizer.md`

---

*H-NEW-2550 completed 2026-08-07 by Waiel Al-Shujaa. The classical scholars counted
correctly; the counting was worth less than it looked, and it was worth that much only in the
taxonomy they chose. A null computed exactly over 40,116,600 alternatives is worth more than a
confirmation computed loosely over one. Bismillāhi al-Raḥmāni al-Raḥīm.*
