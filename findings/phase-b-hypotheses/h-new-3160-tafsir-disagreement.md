---
id: H-NEW-3160
title: Per-verse cross-edition exegetical divergence against the per-verse structural profile — NULL, and the length rule decides it
date: 2026-08-09
author: Waiel Al-Shujaa
status: NULL — 0 of 3 registered inferences pass. The headline channel misses its pre-registered floor by 0.67% of the floor.
prereg: prereg-h-new-3160-tafsir-disagreement.md
prereg_sha256: 6ebab8006998accd93e269937eb2a4bf1ca81325b33a3f69f90d49981722c746
run: runs/h-new-3160/20260809T102637Z/
scripts: scripts/h-new-3160.py (locked, ABORTED by design), scripts/h-new-3160-c8disq.py (disclosed variant)
seed: 20260509
family: TAFSIR-2026-08-09-A
bonferroni_k: 3
alpha_bonferroni: 0.01666667
parent: H-NEW-2620 (surah-level, NULL 0/6); H-NEW-2990 (the per-verse instrument)
rules_tuple: (no-tashkeel for verse text, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
verdict: NULL
---

# H-NEW-3160 — the tradition's disagreement, measured per verse

**Verdict: NULL. Zero of three registered inferences pass.** Per-verse cross-edition exegetical
divergence is related to the verse's own structural profile in the **direction locked before the
run**, at a **size indistinguishable from the floor locked before the run**, and the **choice of
length rule moves the estimate by a factor of 3.96**.

n = 6,095 verses. Pre-reg SHA-256 `6ebab800…c746`, runtime-verified. Seed 20260509, 10,000
within-decile permutations per channel, Bonferroni α = 0.05/3 = 0.0166667. **74,832 tafsīr files
read and individually SHA-256 hashed**; manifest `d020f929…0ae1`.

---

## 1. The headline, stated plainly

| | ΔR² over the length block | gate |
|:--|--:|:--|
| **C1 DISPUTE-rank** — H-NEW-2620's own channel, inherited unmodified | **0.03933** | **passes all four** |
| **C2 DISPUTE-density** — the same markers per 1,000 characters | **0.00993** | **fails the 0.01 floor** |

**Same corpus, same verses, same marker list, same structural block. The only difference is
whether you rank the amortised marker count or divide it by length. The estimate moves 3.96×,
and the verdict moves with it.**

The pre-registration headlined this inference by the **worse** of its two length rules — the
brief's warning 3, locked in §5 before any number existed. **That rule converted a PASS into a
NULL.** The dominant channel is named, as required: **C1**.

**C2 misses by 0.00006698 — 0.670% of the floor.** This is not a decisive absence and is not
reported as one. The honest statement is that **the length-honest DISPUTE channel lands
essentially exactly on a threshold chosen before the data was seen.**

---

## 2. What the p-values were worth: nothing, exactly as registered

**All four channels returned p = 9.999 × 10⁻⁵ — the permutation floor, 1/10,001.** Every channel
is maximally significant. Not one of them passes.

Pre-registration §4 said this in advance: *"At n = 6,236 a correlation of ρ = 0.05 gives
p < 0.0001 … a significant result is therefore close to guaranteed and means nothing on its own."*
The design made the effect size binding and the p-value decorative, and that is precisely how it
played out. **A lane that had gated on p alone would have reported four passes out of four.**

---

## 3. The direction lock was right, and it did not save the hypothesis

All four channels ran **positive**, as locked from H-NEW-2620 §4's published anchors
(ρ(DISPUTE_raw, hapax) = +0.1332, ρ(ATTENTION_raw, hapax) = +0.1141):

| channel | signed partial of `frac_hapax_root_tokens` given the nuisance block |
|:--|--:|
| C1 DISPUTE-rank | **+0.1181** |
| C2 DISPUTE-density | +0.0368 |
| C3 DIVERGENCE-L | +0.0748 |
| C4 DIVERGENCE-V | +0.1003 |

**No reverse-direction flag is raised** (§6.3); reverse p ranged 0.985 to 1.000. So the mechanism
in §1 of the pre-registration — *lexically extraordinary verses draw more reported dispute* — is
**correct in sign and too small to clear the bar**. That is a different result from "no relation",
and it is the one the data supports.

The counter-anchor recorded before the run (2620's ρ(ATTENTION, root rarity) = −0.0205, flat) did
not fire against the hapax channels.

---

## 4. The gate table

| | outcome | ΔR² | p | abs floor 0.01 | length-rule floor | direction | **verdict** |
|:--|:--|--:|--:|:--|--:|:--|:--|
| **I1** | DISPUTE (**worse of C1/C2 → C2**) | **0.00993** | 9.999e-5 | ✗ **by 6.7e-5** | ✓ 0.00070 | ✓ +0.0368 | **NULL** |
| **I2** | DIVERGENCE-L (C3) | 0.00852 | 9.999e-5 | ✗ | ✓ 0.00581 | ✓ +0.0748 | **NULL** |
| **I3** | DIVERGENCE-V (C4) | 0.06600 | 9.999e-5 | ✓ | ✓ 0.01399 | ✓ +0.1003 | **DISQUALIFIED** (§6) |
| *(non-inferential)* | C1 DISPUTE-rank | 0.03933 | 9.999e-5 | ✓ | ✓ 0.00866 | ✓ +0.1181 | *passes, not headlined* |

**Survivors: 0 of 3 → NULL.** Conjunction reported as §6.2 requires: the three channels are three
proxies for one construct, and none survived.

**The computed floor did real work.** ΔR²_lengthrule — the variance commanded by the arbitrary
choice among three near-identical length channels — ran **0.00866** for C1, **0.00581** for C3 and
**0.01399** for C4. For C4 the choice of length rule alone commands **more variance than the
absolute floor**. This is `cross-finding-029`'s deciding parameter, computed rather than asserted.

---

## 5. Why C1 and C2 disagree — the mechanism, named

**POST-HOC diagnostic**, non-confirmatory, no verdict rests on it. Spearman ρ of each channel
against length:

| channel | vs verse words | vs verse letters | **vs mean commentary length** |
|:--|--:|--:|--:|
| **C1 DISPUTE-rank** | **+0.4085** | +0.4168 | **+0.7465** |
| **C2 DISPUTE-density** | **+0.0772** | +0.0812 | **+0.2696** |
| C3 DIVERGENCE-L | −0.2180 | −0.2240 | −0.0247 |
| C4 DIVERGENCE-V | **−0.5064** | −0.4808 | −0.0497 |

**The rank channel carries 5.3× the verse-length correlation of the density channel** (0.4085
against 0.0772). Ranking an amortised *count* ranks length: a longer commentary contains more
words and therefore more marker words, whatever the exegete thinks.

**And the comparison that matters for the parent finding.** H-NEW-2620 registered ATTENTION and
DISPUTE as separate channels addressing separate constructs — *"the DISPUTE channel is the one
that addresses content, which is why it was registered"*. Rebuilding its ATTENTION channel
exactly (mean of the 8 within-edition percentile ranks of amortised commentary length) and
correlating it with the two DISPUTE encodings:

| | ρ with H-NEW-2620's ATTENTION | shared rank variance |
|:--|--:|--:|
| **C1 DISPUTE-rank** (2620's own encoding) | **+0.7155** | **51.2%** |
| **C2 DISPUTE-density** | +0.2621 | 6.9% |

**H-NEW-2620's DISPUTE channel shares 51.2% of its rank variance with its own ATTENTION
channel** — the two it registered as measuring different things. Under the density encoding that
falls to **6.9%**. This does not overturn 2620's NULL — nothing here does, and its NULL is
reinforced — but its two channels were substantially less independent than the design supposed.
**Reported because it is a defect in an instrument I chose to inherit unmodified**, and because
the same rank-of-a-count construction is what carries the 3.96× in §1.

---

## 6. C4 was disqualified, and the pre-registration that disqualified it contradicts itself

**This section records an error of mine in the locked document.**

Prereg abort condition 8 requires the permutation null mean of ΔR² to sit within 3 permutation-SDs
of the analytic expectation. Measured **null inflation** (stratified null mean ÷ analytic
expectation):

| channel | null mean | analytic | **inflation** |
|:--|--:|--:|--:|
| C1 | 0.000904 | 0.000591 | 1.5× |
| C2 | 0.001100 | 0.000764 | 1.4× |
| C3 | 0.002081 | 0.000701 | 3.0× |
| **C4** | **0.015031** | 0.000686 | **21.9×** |

**C4's null is inflated 21.9-fold**, and §5's diagnostic says why: Jaccard distance is
mechanically a length statistic (ρ = **−0.5064** with verse length — a terse gloss and a long
excursus share few words even in perfect agreement). **This is exactly the pathology
pre-registration §10 predicted for C4 before the run.** The condition worked.

**But the pre-registration is internally inconsistent.** §4 specifies a stratified null that
*deliberately preserves length-mediated association*; §8's condition 8 then demands that null be
centred where an **iid** null would be. Those cannot both hold whenever the structural block
carries stratum-level signal. **I wrote both clauses and did not notice.**

**What I did, and why it cannot have helped the hypothesis.** The locked script
`scripts/h-new-3160.py` was run first and **aborted, exactly as written** — console log preserved
at `runs/…/locked-run-abort.log`, no run directory created. Taken literally it discards three
valid channels for one bad one. A disclosed variant, `scripts/h-new-3160-c8disq.py`, marks the
failing channel **DISQUALIFIED** and continues. This is a **tightening**:

- **k stays 3 and α stays 0.05/3.** Reducing k would *raise* α — forbidden.
- **A DISQUALIFIED channel can never PASS**, so the verdict ceiling drops from SUPPORTED to
  PARTIAL. The design can no longer return its most favourable outcome.
- **It is non-load-bearing.** I1 and I2 already returned NULL, so survivors = 0 and the verdict is
  NULL whatever C4 does. **Nothing about this deviation can convert a NULL into a finding.**

**The pre-registration was not edited**, per the standing rule from H-NEW-2620 §10.1: *never edit
a pre-registration after its run, for any reason, including to correct an error in it.* The two
scripts differ in three hunks, all documented in the variant's docstring.

---

## 7. Sensitivities — and the two that cut against the verdict

Non-confirmatory by registration. Reported whatever they showed.

| variant | C1 | **C2** | C3 | C4 |
|:--|--:|--:|--:|--:|
| **primary** | 0.03933 | **0.00993** | 0.00852 | 0.06600 |
| **§7.1 classical-only (4 verified pre-modern)** | 0.04466 | **0.00768** | **0.00165** | **0.01366** |
| modern-only (4) | 0.01096 | 0.00966 | 0.00239 | 0.04666 |
| drop lemma-echo verses | 0.04182 | **0.01069** | 0.00878 | 0.06543 |
| first-occurrence verses only | 0.04098 | **0.01084** | 0.00870 | 0.07042 |
| full clean 21-column block | 0.05876 | **0.01649** | 0.03989 | 0.17434 |
| English 4 editions | — | — | 0.00116 | 0.00887 |

**Three of these put C2 above the floor** (0.01069, 0.01084, 0.01649). **They are
non-confirmatory and do not change the verdict** — but reporting the verdict without them would
misrepresent how close this is. The locked design returned NULL; three declared variants of it
would not have.

**§7.1 is the sensitivity H-NEW-2620 claimed and never ran.** That finding's row labelled
*"classical-only (5 pre-modern)"* contained **four pre-modern editions plus Ibn ʿĀshūr (d. 1393
AH / 1973 CE)**. Run correctly here on the four verified pre-modern Arabic editions — al-Ṭabarī
(310), al-Baghawī (516), al-Qurṭubī (671), Ibn Kathīr (774):

- **C2 falls** 0.00993 → 0.00768
- **C3 collapses 5.2×** 0.00852 → 0.00165
- **C4 collapses 4.8×** 0.06600 → 0.01366
- **C1 rises** 0.03933 → 0.04466

**On the genuinely pre-modern tradition, three of four channels get weaker, and the one that gets
stronger is the length-confounded one.** Prereg §10 named this test: *"if the classical-only
sensitivity reverses against the primary, then whatever is being measured is a property of
20th-century Arabic exegetical prose."* It does not reverse — signs hold — but it **attenuates
sharply**, and the attenuation runs the wrong way for the hypothesis.

**Caveat, stated because it limits that reading:** the classical and modern arms use 4 editions
against the primary's 8, and the modern arm's DISPUTE uses only 3 (al-Muyassar fails the coverage
gate). Fewer editions means a noisier IQR and fewer Jaccard pairs, so part of the C3/C4 collapse
is edition count, not chronology. **The comparison that is matched on count is classical-4 vs
modern-4**, and there C1 runs 0.04466 against 0.01096 while C4 runs 0.01366 against 0.04666 — the
two families disagree in *opposite directions on different channels*, which is not a coherent
chronological story and is reported as such rather than resolved.

**Leave-one-edition-out (C2): 0.00642 (drop al-Ṭabarī) to 0.01685 (drop al-Qurṭubī).** Dropping
al-Qurṭubī — the highest marker coverage in the set at 61.79% — **nearly doubles** the density
channel, because his enormous marker count is spread over an enormous commentary. Dropping
al-Muyassar changes C1 and C2 **not at all** (0.03933 / 0.00993 unchanged), which is the correct
behaviour since the coverage gate already excluded it — an internal consistency check that passed.

---

## 8. The roster, and the contamination that pre-registration removed

Top of the DISPUTE roster, residualised on the full nuisance block:

| # | verse | resid | the dispute |
|--:|:--|--:|:--|
| 1 | **Q 19:71** *wa-in minkum illā wāriduhā* | +2.847 | does everyone enter the Fire |
| 2 | **Q 15:91** *jaʿalū l-Qurʾāna ʿiḍīn* | +2.733 | *ʿiḍīn* — a lexical crux |
| 3 | **Q 38:1** ص | +2.670 | the muqaṭṭaʿāt |
| 4 | **Q 1:1** basmala | +2.630 | is it an āya of al-Fātiḥa? |
| 5 | **Q 85:4** *aṣḥāb al-ukhdūd* | +2.366 | |
| 6 | **Q 2:238** *al-ṣalāt al-wusṭā* | +2.359 | which is the middle prayer |
| 7 | **Q 4:93** deliberate killing of a believer | +2.353 | is repentance accepted |
| 8 | **Q 3:97** *man dakhalahu kāna āminan* | +2.353 | ḥajj obligation |
| 9 | **Q 68:13** *ʿutullin baʿda dhālika zanīm* | +2.339 | *zanīm* |
| 10 | **Q 17:85** *yasʾalūnaka ʿan al-rūḥ* | +2.338 | |
| 11 | **Q 89:3** *wa-l-shafʿi wa-l-watr* | +2.338 | |
| 12 | **Q 58:3** *ẓihār* | +2.315 | |
| 13 | **Q 2:197** *al-ḥajju ashhurun maʿlūmāt* | +2.309 | |
| 14 | **Q 50:1** ق | +2.303 | |
| 15 | **Q 5:33** the *ḥirāba* punishment | +2.286 | |

**Zero of the top 40 are lemma-echo verses. H-NEW-2620's top 30 contained ten.** That
contamination — verses whose own Qurʾānic text contains *ikhtalafa* or *qīla*, inflating their own
marker count — was a post-hoc discovery there and a **pre-registered covariate** here, and the
roster is clean of it by construction rather than by correction. Two of the top 40 are repeat
verses, against 2620's 22 of 30.

**The instrument replicates 2620's independent discoveries without being tuned to them:** Q 19:71,
Q 15:91, Q 1:1, Q 85:4, Q 2:238, Q 4:93, Q 3:97, Q 17:85 and Q 89:3 all appear on both rosters,
built by different residualisation at a different resolution. Q 68:13 (*zanīm*), Q 58:3 (*ẓihār*),
Q 2:197 and Q 5:33 (*ḥirāba*) are new here.

**Only 3 of the top 40 are muqaṭṭaʿāt openings**, against 2620's *thirteen of thirty*. That is the
lemma-echo and length corrections working: 2620's muqaṭṭaʿāt cluster was partly an artefact of
scoring one-word verses on a length-confounded rank.

---

## 9. MDE, power, and the untestable branch

Computed per prereg §6.4, including the branch H-NEW-3030 §3.5 requires.

| channel | ΔR²\* (clears α) | ΔR²\* (clears all four gates) | attainable ceiling | |
|:--|--:|--:|--:|:--|
| C1 | 0.00232 | 0.01000 | 0.05876 | testable |
| **C2 (I1)** | **0.00306** | **0.01000** | **0.01649** | **testable** |
| C3 (I2) | 0.00468 | 0.01000 | 0.03989 | testable |
| C4 (I3) | 0.02071 | 0.02071 | 0.17434 | testable |

**The untestable branch was computed and did not fire.** ΔR²\* ≤ ceiling on every channel, so the
design *could* have rejected. This is a NULL that **did not detect**, not one that **could not
have detected**.

**But the margin on the headline inference is thin and must be stated as such.** For I1 the
testable window is **[0.01000, 0.01649]** — the binding gate sits at 61% of the maximum the full
21-column clean block can reach. **The design can only reject effects in a narrow band**, and the
observed 0.00993 sits just below its floor. A reader should treat I1 as *at the threshold*, not as
*absent*.

**Register labels are not used in this design**, so the effective-n / phase-degenerate-strata
requirement does not apply. Recorded rather than silently omitted.

**Tie fractions, measured before the lock as mandated:** C1 and C2 **17.32%** (verses with zero
markers in all seven eligible editions), C3 0.10%, C4 0.02%. **All below 50%, so the exact-test
trigger did not fire** — exact permutation was used throughout regardless, and **no parametric
p-value is verdict-bearing anywhere in this design.**

---

## 10. The instrument audit

### 10.1 Coverage — the failure mode the brief feared does not exist here

All **twelve tafsīr editions**: 114 surah directories, **228 top-level entries**, 6,236 verse
files, **6,236 non-empty**. **Per-verse coverage across the twelve is a single point mass at 12 —
100.00% of verses have a comment in all twelve; zero verses in only one; zero in none.**
Cross-edition dispersion in this tree cannot be manufactured by uneven coverage.

`en-asbab-al-nuzul-by-al-wahidi` is confirmed truncated — **152 top-level entries against 228**,
1,089 verses, and **39 surahs with no verse directory: 78-114 continuous, plus 72 and 77** (the
brief's figure was 37; the correct count is 39). **It is not a tafsīr, is not used here**, and is
F-12's instrument.

### 10.2 Attribution — and the death-date test's own failure mode

The census already existed (H-NEW-2970, `findings/PROXY-CLAIMS.md`). I re-ran it rather than trust
it, and reproduced every load-bearing result. The decisive one is stronger than the record:
**`ar-tafseer-tanwir-al-miqbas` signs its own colophon** — Q 2:271 «وقال الشيخ **ابن عاشور جدي**»
(*"Shaykh Ibn ʿĀshūr, my grandfather"*), and at Q 114:6, the book's last verse, «يقول **محمد
الطاهر ابن عاشور**: قد وفيت بما نويت». Ibn ʿAbbās (d. 68 AH) cannot sign a book as Muḥammad
al-Ṭāhir Ibn ʿĀshūr (d. 1393 AH / 1973 CE).

**Three of my own probes produced confident false positives at scale**, caught only by reading
contexts:

- al-Qurṭubī (d. 671) appeared to cite **"ابن كثير" ×292** — impossible. Every hit is a *qirāʾa*
  citation («قراءة ابن كثير», «وقرأ نافع وابن كثير وأبو عمرو»): **ʿAbdallāh ibn Kathīr al-Makkī,
  one of the seven canonical readers (d. 120 AH)**, a different man. al-Qurṭubī is clean.
- al-Baghawī and Ibn Kathīr appeared to cite **"محمد عبده"** — both hits are the shahāda formula
  «ومحمدٌ **عبدُه** ورسولُه» at Q 85:22 in both. Ordinary Arabic, not a name. Both clean.
- al-Ṭabarī's single "رشيد رضا" hit is **Aḥmad Shākir's modern editorial apparatus**, a footnote.

**Standing caution: a raw hit count is not evidence; a read context is.** A name that is also an
ordinary Arabic phrase, or shared with an earlier man in another discipline, produces a false
accusation at **×292**, not ×1. The published census got all three right; a less careful
application of the same test would have condemned al-Qurṭubī.

### 10.3 "Twelve tafsīr traditions" is not what this corpus holds

| stratum | editions | n |
|:--|:--|--:|
| pre-modern Arabic | al-Ṭabarī (310), al-Baghawī (516), al-Qurṭubī (671), Ibn Kathīr (774) | **4** |
| modern Arabic | al-Saʿdī (1376/1956), **Ibn ʿĀshūr (1393/1973)**, al-Wasīṭ (20th c.), al-Muyassar (2007 committee) | **4** |
| English | al-Jalālayn (864/911), Ibn Kathīr abridged (**duplicate of the Arabic**), Tanwīr al-Miqbās (ascribed 68), Maʿārif al-Qurʾān (1396/1976) | **4** |

**At most 11 distinct works; half the Arabic set is 20th-century.** No claim here uses the phrase
"twelve traditions".

### 10.4 Three exact replications of H-NEW-2620

Computed at runtime as abort conditions, not quoted:

- **All eight marker-coverage figures to 0.01 pp** — al-Qurṭubī 61.79, al-Ṭabarī 46.50,
  al-Baghawī 35.15, Tanwīr 31.61, al-Wāsiṭ 28.53, Ibn Kathīr 19.76, al-Saʿdī 5.82,
  al-Muyassar 1.80. Eligible set: the same seven.
- **Lemma-echo verses: 70.** 2620 §7.3 reported 70.
- **Repeat verses: 178.** 2620 §7.1 reported 178.

Distinct-block counts also reproduce (`en-tafisr-ibn-kathir` 1,895 blocks for 6,236 verses;
`en-tafsir-maarif-ul-quran` 3,037).

---

## 11. Honest limits

1. **The proxies do not measure disagreement about meaning.** DISPUTE measures *reported*
   disagreement — how often an edition says *"they differed"* — which is one step removed and is
   also a measure of genre convention and isnād-stacking style. DIVERGENCE-L measures disagreement
   about *how much attention to give*, which H-NEW-2620 §3 already said is not disagreement about
   meaning. **No analysis choice removes this**, and the §2 declaration table stands.
2. **The edition set is not a sample of the tradition.** Four pre-modern Arabic tafsīrs is not a
   stratified sample of a genre with hundreds of members. al-Rāzī, al-Zamakhsharī, al-Ṭabarsī,
   al-Biqāʿī, al-Thaʿlabī and al-Suyūṭī's *al-Durr al-manthūr* are all elsewhere in this
   repository and all absent from this tree.
3. **`ar-tafsir-al-wasit` is of unknown authorship**, bounded only to the later 20th century. It
   carries 1/8 of the divergence channels.
4. **Digitisation is an uncontrolled layer** — print edition, isnād retention, tashkeel policy are
   not recoverable from the files and all move character counts. The al-Ṭabarī tree carries
   Shākir's modern apparatus inside the same text field as al-Ṭabarī's prose.
5. **The structural block is five columns chosen by one mechanism.** The full 21-column clean
   block roughly doubles every ΔR² (§7), so the 5-column choice is conservative — but it is a
   choice, and a different mechanism would pick different columns.
6. **141 verses (2.26%) were dropped** for undefined structural columns, chiefly
   `root_simpson_repeat`, which is empty when a verse has fewer than two root tokens. Short verses
   are therefore under-represented, and short verses are where the muqaṭṭaʿāt live.
7. **§5 and the null-inflation table are POST-HOC.** They explain the verdict; they do not test
   anything, and no verdict rests on them.

---

## 12. What I got wrong

**Four errors, three of mine in this lane.**

1. **My first marker implementation omitted 2620's leading-و/ف stripping**, so it missed «وقيل»
   and «فقيل». Coverage came out uniformly low and **al-Saʿdī fell to 4.27%, below the 5%
   eligibility gate — it would have silently dropped an edition from the primary.** Caught
   pre-lock by comparing against 2620's published figures; recorded in prereg §0.2 before the run.
2. **The pre-registration predicted n = 6,214. The realised n is 6,095.** I read `n_defined =
   6214` off the rarity columns and missed that `root_simpson_repeat` is defined for only 6,095.
   The prereg's *rule* (drop rows with any undefined column, report the count) is what bound, so
   the analysis is unaffected — but the stated expectation was wrong.
3. **The pre-registration says "31-clean-column block". The usable set is 21.** H-NEW-2990's
   "31 of 33 clean" counts identity and length columns as clean; excluding those leaves 21. My
   §6.4 ceiling therefore uses 21 columns, not 31.
4. **Abort condition 8 contradicts §4 of my own pre-registration** (§6 above). The locked script
   aborted on it, and I ran a disclosed tightening variant rather than edit the locked file.

**And one thing the brief got slightly wrong, reported because it was checkable:** the asbāb
folder is missing **39** surahs, not 37 — 78-114 plus 72 and 77.

---

## 13. Cross-references

- **[[h-new-2620-tafsir-contested]]** — the parent. Its surah-level NULL is **reinforced**, not
  overturned: at verse level, with a length-honest rule, the effect is still below a floor set in
  advance. Its §9 limit 4 asked for this test by name. **Its DISPUTE channel is shown here to
  carry ρ = +0.7465 with commentary length** (§5), which is a defect in an instrument I inherited
  deliberately and unmodified.
- **[[h-new-2990-verse-profile]]** — the instrument that made this possible. First use of the
  per-verse profile against anything other than ḥadīth reception. Its column-declaration
  discipline is what let the structural block be chosen without a length audit of my own.
- **[[cross-finding-029-the-deciding-parameter]]** — a sixth anchor. The quantity that fixed this
  verdict is **the length rule**, not the hypothesis: 3.96× between two encodings of one marker
  count, and a floor crossed by 0.67%.
- **[[h-new-3000-reception-residual-rosters]]** — the same shape of honesty problem, opposite
  channel: there a parametric p ran 57× too liberal on a tied outcome. Here the ties were measured
  first (17.32%) and no parametric p was ever verdict-bearing.
- **[[findings/PROXY-CLAIMS]]** — §10.2 adds a failure mode of the death-date test itself.
- **F-12 (asbāb al-nuzūl)** — the coverage datum it needs is re-measured here: **1,089 verses, 75
  surah directories, 39 surahs entirely absent.**

---

*Every finding is a loadcell. Every null is also a loadcell.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
