---
id: H-NEW-2550
title: The muqaṭṭaʿāt-14 as an articulatory-feature-space optimizer — al-Zamakhsharī's "half of each genus" against the exact C(28,14) null
date: 2026-08-07
phase: B
status: CONFIRMED-BUT-MEANINGLESS (primary) — RULES-TUPLE-FRAGILE
verdict: >-
  RULES-TUPLE-FRAGILE / CONFIRMED-BUT-MEANINGLESS. al-Zamakhsharī's claim is
  descriptively EXACT — the 14 sit at the GLOBAL MINIMUM of feature-imbalance over all
  40,116,600 fourteen-letter subsets — and statistically ORDINARY: 1,024,500 subsets
  (2.554%) tie that minimum, p_exact = 0.02554 vs α_bon = 0.0025. Under the later
  tripartite tajwīd taxonomy the claim collapses to exactly the null median (p = 0.5567).
  One of 20 cells clears α_bon: against a corpus-frequency-weighted null (p = 0.00183),
  which locates a real and narrow fact — the balance is achieved BY including the four
  low-frequency letters ح س ص ط that frequency-driven selection omits.
author: Waiel Al-Shujaa
seed: 20260509
seed_replication: 20260511
n_mc: 10000000
n_exact: 40116600
bonferroni_k: 20
alpha_bon: 0.0025
prereg_sha256: 3faabc4df31f794db38b6c9495b296501f23fd917c902f0275c9744c38b7d0ed
rules_tuple: (no-tashkeel graphemes, full-tashkeel for locus detection, 28-letter ḥurūf al-muʿjam, basmala-as-v.1-of-Q1-only, Hafs-Kūfan, Mashriqī) + 4 declared variants
parents: [H-NEW-69, H-NEW-1730, H-NEW-1740, H-NEW-1810, H-NEW-600]
---

# H-NEW-2550 — Are the 14 muqaṭṭaʿāt letters an articulatory-feature-space optimizer?

**Pre-reg SHA-256 `3faabc4d…d0ed`, runtime-verified. Seed 20260509, replication 20260511.
Primary null computed EXACTLY over all 40,116,600 subsets — not sampled. Bonferroni
k = 20, α_bon = 0.0025.**

## Prior art — H-NEW-69, and why this test is not a repeat of it

**Disclosed 2026-08-07, after the run.** `h-new-69-half-alphabet-split.md` (+ `-prereg`,
registered 2026-04-15, seed 20260415, Bonferroni k=8) asked a different question of the same
14 letters: *does the muqaṭṭaʿāt set **coincide with** any classical 14-of-28 grouping* —
shamsiyya/qamariyya and seven others? **Its verdict was NULL: 0/8 groupings significant at
α_bon = 0.00625, and 0/8 even at an unprotected α = 0.05.**

This test asks whether the set **balances each phonetic genus near exact-half** — an
optimization question, not a matching question. The two are logically independent: a set can
split every genus evenly without coinciding with any single named classical grouping, which is
exactly what is observed.

**H-NEW-69's NULL should have been treated as lowering the prior here**, and it was not
consulted before this run — a prior-art disclosure failure recorded rather than quietly fixed.
It does not change any locked direction, threshold, or number below; the pre-registration SHA
`3faabc4d…d0ed` stands unamended and the result is unaltered. But the two findings now read
together as one coherent picture: **the 14 match no classical grouping (H-NEW-69) yet sit at
the global minimum of genus-imbalance (this file) — while 2.55% of all subsets do too.**

---

## TL;DR

al-Zamakhsharī (*al-Kashshāf* ad Q 2:1) and al-Suyūṭī (*al-Itqān*, fawātiḥ nawʿ) report
that the 14 muqaṭṭaʿāt letters are not merely half the alphabet but take **half of every
phonetic genus** — half the voiceless, half the stops, half the emphatics, half the
raised, half the qalqala letters. Both enumerate the memberships. Every number they give
is **exactly right**, and this is the first computation of what that is worth.

**It is worth almost nothing, and the exact amount is now known.** Under the classical
28-letter inventory and al-Zamakhsharī's own five binary genera, the attested 14 sit at
the **global minimum** of total imbalance — no 14-subset of the 28 can be more balanced.
And **1,024,500 of the 40,116,600 possible 14-subsets (2.554 %) tie that same minimum**.
One 14-letter subset in 39 is exactly as "perfectly balanced" as the muqaṭṭaʿāt.
`p_exact = 0.025538`, against the pre-registered `α_bon = 0.0025`. The claim is
**descriptively exact and statistically ordinary**.

Two further results carry the finding beyond a bare null:

- **The claim is an artefact of al-Zamakhsharī's own taxonomy.** Under the *later*
  tripartite tajwīd manner-split (shadīd / bayniyya / rikhw) that every modern reciter
  learns, the 14 take **all five** bayniyya letters (ر ع ل م ن — 100 %, not 50 %) and the
  statistic lands on **exactly the null median**, `p = 0.5567`. "Half of each genus" is
  true in the 12th-century binary taxonomy and false in the one that replaced it.
- **One cell of twenty clears α_bon, and it is interpretable.** Against a
  *corpus-frequency-weighted* null the 14 are significantly more balanced
  (`p = 0.001828`, replication `0.001794`). The mechanism is exact and singular: the
  balance is achieved **because** the set includes the four low-frequency letters
  **ح س ص ط** — precisely H-NEW-1810's four "displacements". Swap them for the four
  high-frequency letters they displaced (ب ت ف و) and imbalance goes from **1.0 to 7.0**.

## 1. The classical claim — three attestations located on disk, one negative result

### 1.1 al-Zamakhsharī — the strong form, with membership lists

**al-Zamakhsharī, *al-Kashshāf ʿan ḥaqāʾiq al-tanzīl*, ad Q 2:1**, edition pagination
**PageV01P028–029**;
`data/literature/classical-tafsir/raw/zamakhshari-kashshaf.openiti.raw.txt` (byte ≈ 36 088),
duplicated at `…/zamakhshari-kashshaf-ar-openiti-Q002.txt` (byte ≈ 10 627):

> … وجدتها **نصف أسامى حروف المعجم أربعة عشر سواء** … **في تسع وعشرين سورة** على عدد
> حروف المعجم. ثم إذا نظرت في هذه الأربعة عشر وجدتها **مشتملة على أنصاف أجناس الحروف** …
> **من المهموسة نصفها**: الصاد، والكاف، والهاء، والسين، والحاء … **ومن الشديدة نصفها**:
> الألف، والكاف، والطاء، والقاف … **ومن المطبقة نصفها**: الصاد، والطاء … **ومن المستعلية
> نصفها**: القاف، والصاد، والطاء … **ومن حروف القلقلة نصفها**: القاف، والطاء.

### 1.2 al-Suyūṭī — independent strong-form attestation, extended to makhārij

**al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, fawātiḥ al-suwar nawʿ, PageV03P031**;
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` (byte ≈ 717 265):

> … فذكر منها **أربعة عشر حرفا وهي نصف جميع الحروف وذكر من كل جنس نصفه**: فمن **حرف
> الحلق** الحاء والعين والهاء، ومن **التي فوقها** القاف والكاف، ومن **الحرفين الشفهيين**
> الميم، ومن **المهموسة** السين والحاء والكاف والصاد والهاء …

al-Suyūṭī writes **الهمزة** where al-Zamakhsharī writes **الألف** — both treat the
muqaṭṭaʿāt alif as the glottal stop. That fork is tested as tuple T-B. His munfatiḥa list
has 11 members against al-Zamakhsharī's 12 (اللام absent); ل is munfatiḥ in every
classical table, so this is recorded as a transmission omission, disclosed and not
silently corrected.

### 1.3 al-Rāzī — **weak form only** (a negative result, reported as such)

**al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 2:1**, *furūʿ ʿalā al-qawl bi-annahā asmāʾ al-suwar*,
point *al-thānī*, ≈ PageV02P257;
`data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt` (byte ≈ 628 493):

> الثاني: أن الله تعالى أورد في هذه الفواتح **نصف أسامي حروف المعجم: أربعة عشر سواء** …
> **في تسع وعشرين سورة**.

**In the copy held by this project al-Rāzī reports only the weak form** — 14 letters =
half the alphabet, in 29 surahs — and **no per-ṣifa breakdown by al-Rāzī was located**.
Diacritic-insensitive searches of the full 29.7 MB raw for المهموسة / المطبقة /
المستعلية / أجناس الحروف / أنصاف أجناس return his ḍād-vs-ẓāʾ tajwīd discussion
(≈ byte 124 517) and unrelated hits, not the fawātiḥ ṣifāt passage. **The strong form is
attributed to al-Zamakhsharī and al-Suyūṭī only.** Any attribution of the per-category
claim to al-Rāzī is, on this project's evidence, unsupported.

## 2. The 14 letters — derived from the corpus, not asserted

A detector that never names the letters it seeks: the first whitespace token of verse 1
and verse 2 of every surah in `quran-text/quran-full-tashkeel.json` is a muqaṭṭaʿāt token
**iff it carries no ordinary vocalisation** (no U+064B–U+0652, no U+0670). Across all
**228 scanned tokens** it returns **30 loci in exactly 29 surahs** (Q 42 twice: 42:1 حم,
42:2 عسق), **zero false positives**, and a union of **exactly 14 graphemes**:

> **ا ح ر س ص ط ع ق ك ل م ن ه ي**

identical to al-Zamakhsharī's enumerated fourteen and to the 29-surah catalogue of
[[h-new-1740-khalifa-muqattaat-complete-audit|H-NEW-1740]] §1. All asserted fail-fast.

## 3. PRIMARY RESULT — T-A × H1 × N1 (the claim as stated, exact null)

`D(S) = Σ_f | |S ∩ f| − |f|/2 |` over al-Zamakhsharī's five binary genera.

| Genus | \|f\| | in the 14 | classical half | deviation |
|:--|--:|--:|--:|--:|
| mahmūsa (voiceless) | 10 | **5** | 5.0 | **0.0** |
| shadīda (stops) | 8 | **4** | 4.0 | **0.0** |
| muṭbaqa (emphatic) | 4 | **2** | 2.0 | **0.0** |
| mustaʿliya (raised) | 7 | **3** | 3.5 | **0.5** |
| qalqala | 5 | **2** | 2.5 | **0.5** |
| | | | **D_obs** | **1.0** |

The two non-zero deviations are **unavoidable**: 3.5 and 2.5 are not integers, so 0.5 is
the floor. **D_obs = 1.0 is the global minimum of D over the whole subset space** — the
exact enumeration confirms `null_min = 1.0`. al-Zamakhsharī's description is not merely
accurate; the set he describes is *optimal* for his own statistic.

**And that optimum is common:**

| Exact null over all C(28,14) = 40,116,600 subsets | value |
|:--|--:|
| D_obs | **1.0** |
| null minimum | **1.0** (obs is the global minimum) |
| **subsets tying the minimum** | **1,024,500** |
| **fraction tying the minimum** | **2.5538 %** |
| **p_exact (one-sided low, tie-inclusive)** | **0.025538** |
| percentile of D_obs | 2.554 |
| null mean / SD / median | 4.4299 / 1.7781 / 4.0 |
| z of D_obs | −1.93 |
| α_bon (k = 20) | 0.0025 |
| **verdict** | **CONFIRMED-BUT-MEANINGLESS** |

Independent stdlib-only uniform Monte Carlo (200,000 draws) returns 0.02582 against the
exact 0.025538 — agreement within 0.8 SE, on all five tuples.

**One 14-subset in 39 is exactly as balanced as the muqaṭṭaʿāt.** "Half of each genus" is
the *expected value* of a random 14-subset (`E[|S∩f|] = |f|·14/28 = |f|/2` by symmetry),
so the null is centred on the claim and tightly concentrated. This is a combinatorial
inevitability wearing the clothes of a design signature. **The pre-registered
most-likely outcome (pre-reg §0) is the outcome.**

## 4. The rules-tuple collapse — the claim depends on al-Zamakhsharī's own taxonomy

al-Zamakhsharī uses the **binary** shadīd/rikhw split (his rikhwa list contains ل م ر ع ن).
Later tajwīd interposes a five-member **bayniyya / mutawassiṭa** class between them. Under
that taxonomy (tuple **T-C**):

| Genus | \|f\| | in the 14 | half | deviation |
|:--|--:|--:|--:|--:|
| **bayniyya** | 5 | **5** | 2.5 | **2.5** |
| **rikhw** | 15 | **5** | 7.5 | **2.5** |
| mahmūsa / shadīd / muṭbaqa / mustaʿliya / qalqala | — | — | — | 0 / 0 / 0 / 0.5 / 0.5 |
| | | | **D_obs** | **6.0** |

The 14 take **100 % of the bayniyya letters** (ر ع ل م ن), not half. `D_obs = 6.0` is
**exactly the null median**; `p_exact = 0.5567`, percentile 55.7. **Verdict: NULL.**

This is the sharpest result in the finding. The celebrated "half of every genus" is not a
property of the letters; it is a property of the letters *as classified by the taxonomy
al-Zamakhsharī happened to use*. Change to the taxonomy that superseded his — the one
every modern reciter is taught — and the claim becomes a coin flip. This is textbook
bidirectional rules-tuple sensitivity, in the demoting direction.

## 5. The one cell that clears α_bon — and exactly what it means

| | p (seed 20260509) | p (replication 20260511) |
|:--|--:|--:|
| **T-A × H1 × N2 (corpus-frequency-weighted null)** | **0.001828** | **0.001794** |

Both below α_bon = 0.0025. Under the pre-registered rule this cell is
**OPTIMIZER-CONFIRMED**. Its content is narrow and fully explicable:

| 14-letter set | D |
|:--|--:|
| **the attested muqaṭṭaʿāt-14** (ا ح ر س ص ط ع ق ك ل م ن ه ي) | **1.0** |
| **top-14 by corpus frequency** (ا ل ن م ي و ه ت ر ب ك ع ف ق) | **7.0** |
| muqaṭṭaʿāt-14 with ح س ص ط swapped for ب ت ف و | **7.0** |

A frequency-driven selection takes **zero** emphatics (all four of ص ض ط ظ rank 22–28 by
corpus frequency, H-NEW-1810) and only one mustaʿlī, for deviations of 2.0 and 2.5. The
muqaṭṭaʿāt set does not, and **the entire difference is carried by four letters**:
**ح س ص ط** — which are *exactly* the four "displacements" H-NEW-1810 identified as
muqaṭṭaʿāt letters falling outside the corpus top-14.

So this cell says: **the selection of the 14 was not driven by corpus frequency**, and the
four letters that break the frequency ranking are the four that make the phonetic balance
exact. That is a genuine mechanistic synthesis, and it gives H-NEW-1810's unexplained
anomaly a rationale for the first time.

**What it does not say.** N2 is a deliberately *biased* null — a model of "selection by
frequency alone". Beating it establishes that frequency alone was not the rule; it does
not establish phonetic optimisation. The unbiased question — *is this balance rare among
14-subsets?* — is answered by N1, and the answer is no: 2.554 % of subsets match it.
A result significant only against a biased null and not against the unbiased one is
**weak evidence for design and strong evidence about mechanism**, and is reported as such.

## 6. Full 20-cell result table (Bonferroni k = 20, α_bon = 0.0025)

| Tuple | N | feats | D_obs | H1 × N1 exact p | H1 × N2 p | D_freq | H2 × N1 exact p | H2 × N2 p |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| **T-A** primary (5 binary ṣifāt) | 28 | 5 | **1.000** | **0.025538** | **0.001828** ✔ | 0.6818 | 0.09275 | 0.02798 |
| **T-B** hamza ≠ alif | 29 | 5 | 1.897 | 0.036109 | 0.004775 | 0.6524 | 0.18959 | 0.08497 |
| **T-C** tripartite manner | 28 | 7 | 6.000 | 0.556716 | 0.090009 | 1.1928 | 0.33469 | 0.02446 |
| **T-D** + 17-makhraj (alif→jawf) | 28 | 21 | 11.000 | 0.178982 | 0.017696 | 7.8594 | 0.57352 | 0.23465 |
| **T-E** + 16-makhraj (alif→ḥalq) | 28 | 20 | 11.000 | 0.260996 | 0.026461 | 7.3594 | 0.65649 | 0.27170 |

✔ = the single cell clearing α_bon. Exact enumeration totals verified as
C(28,14) = 40,116,600 and C(29,14) = 77,558,760.

**No cell is REVERSED.** Across the exactly-computed H1 × N1 cells the smallest upper-tail
p is 0.617 (T-C); on H2 × N1 the highest percentile reached is 65.6 % (T-E). Nothing sits
anywhere near the upper tail, so the locked direction was never violated. **No pre-commit
violation occurred.**

**al-Suyūṭī's makhraj extension (T-D / T-E) is directionally right but not significant**
(p = 0.179 / 0.261): the 14 are somewhat better distributed across the articulation points
than a random subset, but well inside the bulk of the null.

**H2 (frequency-weighted balance) fails everywhere.** On the mass axis the set is
systematically *over*-half — mahmūsa 57.6 %, shadīda 69.9 %, muṭbaqa 56.8 %, mustaʿliya
62.4 % of each genus's corpus mass — consistent with the 74.4 % total mass share this run
reproduces from H-NEW-1810 (T3 = 0.7441). The 14 are a **type-balanced but
mass-unbalanced** half of the alphabet. The one under-half genus is qalqala (28.5 %),
because the set takes the two low-frequency qalqala letters (ق ط) and none of the three
common ones (ب ج د).

## 7. What this finding licenses, and what it forbids

**Licensed.** (i) al-Zamakhsharī and al-Suyūṭī counted correctly — every one of their nine
stated intersection counts is exact, and the set is genuinely optimal for the statistic
they implicitly defined. (ii) The muqaṭṭaʿāt selection was **not** governed by corpus
letter frequency, and the four letters that prove it (ح س ص ط) are the four that make the
phonetic balance exact. (iii) The observation is taxonomy-relative and does not survive
the taxonomy that replaced al-Zamakhsharī's.

**Forbidden.** Any claim that the muqaṭṭaʿāt letters were "selected to span articulatory
space" as a demonstrable design signature. The exact enumeration settles this: over a
million alternative 14-subsets are equally balanced. A property shared by 2.554 % of the
alternatives is not a signature, and after the pre-registered correction it does not reach
significance. **This closes the last quantitative candidate H-NEW-1810 left open** for a
non-arbitrary selection rule over the 14 (its four candidates were phonetic balance,
theological association, abjad constraint, and a pre-Islamic alphabetic substrate; the
first is now tested and does not carry).

The project's standing pillar is untouched and unrevisited: the muqaṭṭaʿāt are
**book-introduction markers**, and the **letter-axis is orthogonal to the content-axis**
(al-Biqāʿī's content-*munāsaba* reading FALSIFIED in 4 replications;
[[h-new-600-letter-families|H-NEW-600]], Protocol §3.7). H-NEW-2550 tested the phonetic
axis, which was untested, and finds no design signature there either.

## 8. Honest limits

1. **The observed statistic was known before the lock, and this was disclosed in
   advance** (pre-reg §0, §9). al-Zamakhsharī *enumerates* the memberships, so reading
   the passage in order to cite it reveals D_obs. What was genuinely unobserved — and is
   the entire empirical content — is the null distribution, its minimum, its
   minimum-mass, and every p-value. Those were computed only after the SHA-gated lock.
   The same disclosure covers T-C, where assembling the feature table made the 5/5
   bayniyya intersection visible pre-lock.
2. **Four feature assignments rest on mnemonics not verified in this repository**:
   ب, ج, د ∈ qalqala and the bayniyya set {ر ع ل م ن}, from Ibn al-Jazarī's قطب جد and
   لن عمر. ق and ط ∈ qalqala *are* on disk via al-Zamakhsharī. ب ∈ shadīda and
   ف ∈ mahmūsa are **derived by closure** from al-Zamakhsharī's own stated halves, not
   assumed. The bayniyya dependency matters: T-C's collapse verdict rests on a
   mnemonic-sourced five-member class. It is the standard class in every tajwīd
   tradition, but it is not verified in a file here.
3. **The pre-reg's decision rules leave one combination unlabelled** — not significant,
   does not reproduce al-Zamakhsharī's enumeration, yet D_obs below the null median
   (T-B, T-D, T-E). These are reported with the conservative label
   "NULL (non-significant; direction-consistent)". No cell was upgraded by this gap.
4. **A modern distinctive-feature (IPA) encoding is not tested.** The claim under test is
   a classical claim about classical genera; scoring it on a modern inventory tests a
   different proposition. Recorded in the pre-reg as discarded-with-reason and flagged as
   a legitimate separate test.
5. **N2's p-value is not a design test.** It compares against a frequency-biased null and
   therefore answers "was the selection frequency-driven?", not "is the balance rare?".
   §5 states this rather than trading on the ambiguity.
6. **Normalisation sensitivity is inherited from H-NEW-1810**: counting ة separately from
   ت, or ى from ي, could move 1–2 letters. Held identical to H-NEW-1810 so the frequency
   vector is directly comparable.
7. **`D` weights every genus equally.** A genus-importance weighting could be defended
   (e.g. iṭbāq is more perceptually salient than qalqala), but any such weighting is a
   free parameter the classical sources do not supply, and introducing one would be the
   forking freedom this protocol exists to forbid.
8. **numpy is used**, a disclosed deviation from Protocol §7.1 (stdlib-only). The
   justification is that the pre-registered null is an *exact* enumeration of 40.1 M
   subsets, which stdlib cannot do; a stdlib-only Monte-Carlo guard is run against every
   exact p and agrees on all five tuples.

## 9. MW-1 … MW-7 compliance

- **MW-1** instrument-prior: statistic, feature table, five tuples, both nulls, thresholds
  and all four verdict labels fixed in the pre-reg before any null was computed.
- **MW-2** corpus-prior: N1 is **exact over the entire subset space** — stronger than any
  permutation count; N2 uses 10⁷ draws, 1000× the §7.1 minimum.
- **MW-3** alternative models: 5 taxonomies × 2 statistics × 2 nulls = 20 cells, all
  reported, none dropped.
- **MW-4** over-fitting: no fitted parameters; `D` has no free constants.
- **MW-5** replication: N2 re-run at seed 20260511 — p = 0.001794 vs 0.001828, and every
  other cell reproduces to 3 significant figures. N1 is exact and needs none.
- **MW-6** instrument-control, all fail-fast at runtime: 30 loci / 29 surahs / 0 false
  positives; derived 14-set == al-Zamakhsharī's fourteen; surah list == H-NEW-1740 §1;
  letter frequencies reproduce **all 28** H-NEW-1810 counts, total 329,131 and standalone
  hamza 1,578 exactly; feature table reproduces al-Zamakhsharī's **nine** stated
  intersection counts (5/9/4/10/2/12/3/11/2); category sizes 10/8/4/7/5/5; makhraj groups
  sum to 28 with no overlap; enumeration totals == C(28,14) and C(29,14). The exact
  engine was additionally validated against full brute force on 5 randomised small cases
  (all quantities identical) before the real run.
- **MW-7** post-hoc cap: §5's swap contrast (D 1.0 → 7.0) and the top-14-by-frequency
  contrast are **descriptive, exploratory and MW-7-capped**; no p-value is claimed for
  them and they add no cell to the family.

## 10. Garden of forking paths

- **Choices made after seeing the data:** none. The only post-lock code change was to make
  the `verdict()` function implement the pre-registered decision *text* literally — the
  first draft returned CONFIRMED-BUT-MEANINGLESS for a tuple sitting exactly *at* the null
  median, which the pre-reg assigns to NULL. This tightened T-C from
  CONFIRMED-BUT-MEANINGLESS to NULL and upgraded no cell. Disclosed here rather than
  silently applied.
- **Pre-reg erratum, corrected before any observation:** the first written draft of the
  pre-reg (SHA `4ec738f2…2c7c`) had C(29,14) as 67,863,915 instead of 77,558,760 — an
  arithmetic slip in an MW-6 assertion constant only. Corrected before any null was
  computed; both SHAs are recorded in pre-reg §14; the binding hash is `3faabc4d…d0ed`.
- **Alternative tuples considered and discarded, with reasons:** lām-alif (لا) as a 29th
  letter — discarded on principle, it is an orthographic ligature with no ṣifa or makhraj,
  so including it would require inventing feature values; modern IPA encoding — tests a
  different proposition; ة/ى split — held to H-NEW-1810's normalisation.
- **Sibling hypotheses:** H2 was pre-registered rather than reported selectively; its
  absolute-mass form is a re-derivation of H-NEW-1810 T3 and is reported descriptively
  only.
- **Why this test:** H-NEW-1810 §Interpretation named "phonetic-articulation balance" as
  candidate #1 for the muqaṭṭaʿāt selection rule after falsifying the frequency reading,
  and left it untested. This is that test.

## 11. Cross-references

- [[h-new-1810-letter-frequency|H-NEW-1810]] — **parent**. Falsified the strong al-Suyūṭī
  frequency claim (10/14, not 14/14) and named the four displacements ح س ص ط. H-NEW-2550
  supplies their mechanism: those four are exactly what makes the phonetic balance exact,
  and it closes 1 of the 4 candidate selection rules that finding left open.
- [[h-new-1740-khalifa-muqattaat-complete-audit|H-NEW-1740]] — the 29-surah catalogue used
  as an MW-6 cross-check; al-Khalifa's div-by-19 thesis NULL at 1/29.
- [[h-new-1730-muqattaat-letter-count-audit|H-NEW-1730]] — sample-of-4 parent of 1740.
- [[h-new-600-letter-families|H-NEW-600]] — muqaṭṭaʿāt letter-family content-cohesion
  NULL. **Convergent**: neither the content axis nor the phonetic axis carries a
  muqaṭṭaʿāt design signature.
- **Challenging prior:** the single α_bon-clearing cell (§5) is the one result that pushes
  *against* a flat null reading, and it is reported with its own deflation rather than
  buried.
- al-Zamakhsharī, *al-Kashshāf*, ad Q 2:1, PageV01P028–029; al-Suyūṭī, *al-Itqān*,
  fawātiḥ nawʿ PageV03P031 and makhārij nawʿ 38 PageV01P346–348 (the 17-makhraj table and
  the 16-makhraj variant, both used as tuples); al-Rāzī, *Mafātīḥ al-ghayb*, ad Q 2:1
  ≈ PageV02P257 (weak form only); Ibn al-Jazarī, *al-Nashr*, as quoted by al-Suyūṭī
  PageV01P348–349 (the pairwise ṣifāt comparison grounding most of the feature table).

## 12. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2550-muqattaat-phonetic-optimizer.md`
- script: `findings/phase-b-hypotheses/scripts/h-new-2550.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-2550.json`
- this finding: `findings/phase-b-hypotheses/h-new-2550-muqattaat-phonetic-optimizer.md`

---

*H-NEW-2550 completed 2026-08-07 by Waiel Al-Shujaa. The classical scholars counted
correctly; the counting was worth less than it looked. A null computed exactly over
40,116,600 alternatives is worth more than a confirmation computed loosely over one.
Bismillāhi al-Raḥmāni al-Raḥīm.*
