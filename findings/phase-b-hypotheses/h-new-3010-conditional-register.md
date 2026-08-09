---
id: H-NEW-3010
title: Realis vs irrealis conditionals are NOT established as register-coded — NULL
date: 2026-08-09
phase: B
author: Waiel Al-Shujaa
verdict: NULL — 0 of 12 pre-registered tests clear; the primary contrast loses 43 % of its
  magnitude to verse length alone
status: NULL (no pre-commit violation — all 12 directions ran as locked)
prereg: prereg-h-new-3010-conditional-register.md
prereg_sha256: 2b1718af47814c1eebc38178977074eba2631e45a7ff43e0ff0e98ad8c11fe93
script: scripts/h-new-3010.py
run: runs/h-new-3010/20260809T065744Z/
frontier_item: F-3 (HANDOFF/FRONTIER-MAP-2026-08-07.md lines 199-205)
parents: [cross-finding-028-formal, H-NEW-2530]
seed: 20260509
n_perm: 10000
---

# H-NEW-3010 — Realis (`in`) vs irrealis (`law` / `lawlā`) conditionals are NOT established as register-coded

> ## VERDICT: **NULL**
>
> **0 of 12 pre-registered tests clear.** The frontier map listed F-3's prior as
> *CONFIRMED*. It is not confirmed.
>
> All twelve tests carry the **locked** direction — so there is **no pre-commit
> violation** — but not one survives its worst length control at
> α_bon = 0.05/12 = 0.0041667. The primary contrast is
> **D = +0.158** (irrealis share 0.3736 in polemic ∪ eschatological against 0.2155 in
> legal), and **verse length alone reproduces 43 % of it with the register labels
> randomised.**
>
> **The single most important number in this finding:** under stratification on
> **log word count** the primary contrast sits at **p = 0.0006**; under stratification
> on **mean verse length** — measured here as the *strongest* nuisance channel for this
> grouping, Spearman **ρ = +0.5467** — the same contrast sits at **p = 0.0271–0.0439**.
> A ~70× swing, decided entirely by which length channel the control uses. Had this test
> locked one channel a priori instead of requiring all three, it would have published a
> PASS.

---

## 1. The hypothesis and where it came from

`HANDOFF/FRONTIER-MAP-2026-08-07.md` §F-3:

> **`in`** (open / realis condition) concentrates in **legal-Medinan**;
> **`law` / `lawlā`** (counterfactual / irrealis) concentrates in **polemic** and
> **eschatological warning**. This is the missing fourth column of cross-finding-028.

The grammatical case for it is genuine and is restated in the pre-registration §1.2:
`in` al-sharṭiyya presents its protasis as *possible*, which is the form a contingent
ruling takes; `law` is *ḥarf imtināʿ li-imtināʿ*, presupposing its protasis **false**,
which is the form of polemical reductio and of the `law tarā` warning. If register is
coded in the conditional apparatus at all, it must run this way. That is why the
direction was locked one-sided and why a reversal would have been a pre-commit
violation rather than a weaker result.

**No classical citation is made.** The frontier map points at the *sharṭ / jazāʾ*
apparatus in al-Zarkashī's *al-Burhān*, and the PDF is on disk at
`data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf` — but
`pdftotext` returns exit code 0 and **zero extractable characters**. The file is
image-only. No passage in it has been read, so no *nawʿ* is cited here or in the
pre-registration. The locked direction rests on the grammatical description of the
particles, not on a located classical passage.

---

## 2. THE VERDICT TABLE — all twelve tests

`p(max)` is the **maximum** over each test's 12 null configurations (2 statistics ×
3 length channels × 2 bin widths), per pre-registration §5.4: a claim is reported at
the strength of its **weakest** control.

α_bon = 0.05 / 12 = **0.0041667**.

| test | locked sign | D_pooled | D_verse | tokens (A/B) | p(min) | **p(max)** | clears |
|:--|:-:|--:|--:|--:|--:|--:|:-:|
| **H1 \| M1 \| T1** *(primary)* | + | **+0.15816** | +0.22057 | 91 / 362 | 0.0004 | **0.0439** | **no** |
| H1 \| M1 \| T2 | + | +0.16030 | +0.24350 | 88 / 349 | 0.0001 | 0.0314 | no |
| H1 \| M2 \| T1 | + | +0.10705 | +0.08350 | 65 / 309 | 0.0587 | 0.3305 | no |
| H1 \| M2 \| T2 | + | +0.10786 | +0.09083 | 63 / 298 | 0.0755 | 0.3005 | no |
| H2 \| M1 \| T1 | − | −0.10799 | −0.11220 | 362 / 439 | 0.0042 | **0.0246** | no |
| H2 \| M1 \| T2 | − | −0.09305 | −0.11192 | 349 / 414 | 0.0047 | 0.0671 | no |
| H2 \| M2 \| T1 | − | −0.12049 | −0.11958 | 309 / 492 | 0.0009 | 0.0253 | no |
| H2 \| M2 \| T2 | − | −0.10602 | −0.12334 | 298 / 465 | 0.0023 | 0.0361 | no |
| H3 \| M1 \| T1 | + | +0.11165 | +0.14759 | 91 / 710 | 0.0021 | 0.1095 | no |
| H3 \| M1 \| T2 | + | +0.12412 | +0.16658 | 88 / 675 | 0.0009 | 0.0793 | no |
| H3 \| M2 \| T1 | + | +0.03595 | +0.02771 | 65 / 736 | 0.1769 | 0.4804 | no |
| H3 \| M2 \| T2 | + | +0.04714 | +0.04003 | 63 / 700 | 0.1846 | 0.3834 | no |

- **H1** = share(polemic ∪ eschatological) − share(legal)
- **H2** = share(legal) − share(everything else)
- **H3** = share(polemic ∪ eschatological) − share(everything else)
- **M1** = legal-precedence containment mapping · **M2** = first-token dominance mapping
- **T1** = {`law`, `lawlā`} vs {`in`, `in`-compounds} · **T2** = bare {`law`} vs {`in`}

Every test passed the 20-token power guard; none was `NOT-POWERED`. No permuted
statistic was ever undefined (`none_statistic_log` is empty).

**Verdict by the pre-registered ladder (§6):** the primary cell has the correct sign, so
no pre-commit violation; `n_clear = 0`, so not PASS, not DIRECTIONAL, not
WEAK-DIRECTIONAL. **NULL.**

### 2.1 "12 of 12 signs correct" is close to ONE fact, not twelve

The standing rule *check every control for tautology* applies to my own consistency
claim. The twelve tests are heavily dependent:

- **T2 is a 95.3 % subset of T1** (763 of 801 tokens). It differs by 35 `lawlā` and
  3 `in`-compound tokens. It is not an independent reading of the data.
- **H1, H2 and H3 are algebraically linked.** If legal sits below the corpus and
  polemic ∪ eschatological sits above it, all three follow from the same two group
  shares.
- **M1 and M2 overlap on 93 of 114 surahs.**

The honest count is **at most two effectively independent facts**, not twelve. The
uniform sign is worth stating and is worth nothing more than that.

---

## 3. THE MANDATED LENGTH DIAGNOSTIC — reported unconditionally

Pre-registration §4.2 required this to be computed and published *before* the primary
test and *regardless of what it showed*. It shows a substantial confound.

### 3.1 Do the register labels correlate with length? **Yes — strongly, on one channel.**

Spearman ρ between the binary group indicator and each length channel, n = 114:

| mapping · group | log word count | verse count | **mean verse length** |
|:--|--:|--:|--:|
| M1 · LEGAL | +0.2720 | +0.0719 | **+0.5467** |
| M1 · IRR | −0.3014 | −0.1018 | **−0.4129** |
| M2 · LEGAL | +0.2671 | +0.0889 | **+0.5128** |
| M2 · IRR | −0.2793 | −0.1621 | −0.2928 |

Group length profiles (medians, from QAC):

| mapping | group | n surahs | median words | median verses | **median words/verse** |
|:--|:--|--:|--:|--:|--:|
| M1 | LEGAL | 17 | 539 | 38 | **19.36** |
| M1 | IRR | 36 | 176 | 38 | **4.58** |
| M1 | OTHER | 61 | 574 | 43 | 9.89 |
| M2 | LEGAL | 13 | 1233 | 64 | **20.75** |
| M2 | IRR | 25 | 169 | 31 | **4.60** |
| M2 | OTHER | 76 | 409 | 44 | 9.11 |

**The legal register's verses are 4.2× longer than the irrealis-predicted register's.**
Note that *verse count* is nearly uncorrelated (ρ = +0.07) — the two groups have almost
the same median number of verses. The confound is entirely in **verse length**, not in
"long surahs" as the frontier map's confound note anticipated.

### 3.2 Is the outcome itself length-correlated? **Yes.**

Spearman ρ between the per-surah irrealis share and each channel, over the 55 surahs
carrying ≥ 3 conditional tokens:

| tuple | log word count | verse count | **mean verse length** |
|:--|--:|--:|--:|
| T1 | +0.0569 | +0.1384 | **−0.2714** |
| T2 | +0.0704 | +0.1511 | −0.2416 |

Both legs of the mediation are present and both point the same way: **long verses →
lower irrealis share** (ρ = −0.27) and **legal → long verses** (ρ = +0.55). Verse
length alone therefore predicts legal to be low-irrealis, which is the observed result.

### 3.3 How much does length alone reproduce? **43 %.**

*Post-hoc diagnostic, not pre-registered, changing no verdict. Script:
`scripts/h-new-3010-posthoc-null-means.py`; output:
`runs/h-new-3010/POSTHOC-20260809T070155Z-null-means/`.*

Under a permutation stratified on a channel that predicts the outcome, permuted groups
inherit the real group's length profile, so the **null mean shifts toward the observed
value by exactly the amount length explains.** For the primary cell
(observed D_pooled = +0.15816):

| stratification | null mean | null sd | **% of observed reproduced** | z |
|:--|--:|--:|--:|--:|
| UNSTRATIFIED (no length control) | −0.00517 | 0.0598 | −3.3 % | +2.73 |
| log word count, quintiles | −0.00361 | 0.0543 | −2.3 % | +2.98 |
| log word count, deciles | −0.00708 | 0.0573 | −4.5 % | +2.88 |
| verse count, quintiles | +0.01711 | 0.0572 | 10.8 % | +2.47 |
| verse count, deciles | +0.02915 | 0.0519 | 18.4 % | +2.48 |
| **mean verse length, quintiles** | **+0.05257** | 0.0565 | **33.2 %** | +1.87 |
| **mean verse length, deciles** | **+0.06800** | 0.0492 | **43.0 %** | +1.83 |

Randomise the register labels entirely, hold only mean verse length fixed, and you
recover **+0.068 of the observed +0.158**. The register labels are worth the remaining
**+0.090**, at z = +1.83.

---

## 4. WHICH CONTROL KILLS IT — and the methodological point this run demonstrates live

The full p-grid for the primary cell:

| null configuration | p |
|:--|--:|
| verse count · quintiles · D_verse | **0.0004** ← min |
| log word count · quintiles · D_pooled | 0.0006 |
| log word count · deciles · D_pooled | 0.0006 |
| log word count · deciles · D_verse | 0.0007 |
| log word count · quintiles · D_verse | 0.0010 |
| verse count · deciles · D_verse | 0.0011 |
| verse count · quintiles · D_pooled | 0.0020 |
| verse count · deciles · D_pooled | 0.0038 |
| mean verse length · quintiles · D_pooled | 0.0271 |
| mean verse length · deciles · D_pooled | 0.0295 |
| mean verse length · deciles · D_verse | 0.0382 |
| **mean verse length · quintiles · D_verse** | **0.0439** ← max, binding |

`UNIT-DRIFT-DEFECT.md` §5 states the rule this run happens to instantiate:

> **A control that does not use the strongest channel is not a control.**

That document's drift table bolds **log word count** as the primary channel — for
**mushaf position**. This is a different comparison, and its strongest channel is a
different variable. Measured here, **mean verse length beats log word count 0.5467 to
0.2720**, and log-word-count stratification reproduces essentially **none** of the
effect (−2.3 %) while mean-verse-length stratification reproduces **43 %**.

**A design that had locked one channel a priori — following the bolded row of the
project's own drift table — would have returned p = 0.0006 and published a PASS.** The
pre-registration's §5.1 decision to require *every* channel rather than the
measured-strongest one is what produced the NULL. That decision was made because
`UNIT-DRIFT-DEFECT.md` §3 records its own table naming the wrong primary channel for
months; the same failure mode was live here and the design caught it.

---

## 5. WHAT THE DATA ACTUALLY SHOWS — the two clauses are not equally supported

The frontier-map hypothesis has two clauses, and the decomposition into H2 and H3
separates them. **They behave very differently.**

Corpus baseline, tuple T1: **220 irrealis / 801 conditional tokens = 0.2747**
(`law` 185, `lawlā` 35, `in` 578, `in`-compounds 3).

| M1 group | n irrealis | n realis | n total | irrealis share | vs corpus |
|:--|--:|--:|--:|--:|--:|
| LEGAL | 78 | 284 | 362 | **0.2155** | **−0.059** |
| polemic ∪ eschatological | 34 | 57 | 91 | **0.3736** | +0.099 |
| OTHER | 108 | 240 | 348 | 0.3103 | +0.036 |

**The signal is legal being LOW, not polemic/eschatological being HIGH.** The
irrealis-predicted group sits only **+0.063** above the unlabelled remainder (0.3736 vs
0.3103), while legal sits **−0.095** below it. And the p-values follow: H2's binding
control is 0.0246 while H3's is 0.1095, and H3 collapses to 0.4804 under the second
mapping.

So the honest summary of the surviving structure is:

> **Clause (i) — `in` concentrates in legal — is the part with support** (nearest miss:
> max p = 0.0246 against α_bon = 0.0042; it clears a raw single-test 0.05 but that is
> not the pre-registered gate and is not offered as one).
> **Clause (ii) — `law`/`lawlā` concentrates in polemic and eschatological — has
> essentially none** (max p = 0.079 to 0.480 across cells).

That asymmetry is partly a power fact and must be reported as one: the
irrealis-predicted register carries **91 of the corpus's 801 conditional tokens
(11.4 %)** while the legal register carries **362 (45.2 %)**.

### 5.1 Descriptive supplements (no inference)

**Secondary surah-unweighted arm** (declared in prereg §9.3, not in the decision rule;
surahs with ≥ 3 conditional tokens):

| mapping | group | n surahs | mean share | median share |
|:--|:--|--:|--:|--:|
| M1 | LEGAL | 15 | 0.1857 | 0.2121 |
| M1 | IRR | **7** | 0.3609 | 0.3846 |
| M1 | OTHER | 33 | 0.3380 | 0.3333 |
| M2 | LEGAL | 12 | 0.1529 | 0.1925 |
| M2 | IRR | **5** | 0.3079 | 0.3750 |
| M2 | OTHER | 38 | 0.3445 | 0.3333 |

It agrees directionally and it exposes the thinness: the irrealis-predicted arm has
**7 surahs** with ≥ 3 conditionals under M1 and **5** under M2, and OTHER (0.338) is
statistically indistinguishable from IRR (0.361) by eye.

**Meccan / Medinan (descriptive only, and length-confounded in exactly the same way):**
Meccan 132/407 = **0.3243**; Medinan 88/394 = **0.2234**.

**Narrative (descriptive only; no direction was locked for it, prereg §9.15):** 27
surahs, 67/230 = **0.2913** — indistinguishable from the corpus baseline of 0.2747.

**Conditional density per 1,000 words — labelled UNIT-DRIFT-EXPOSED and forbidden as a
primary statistic by prereg §4.1**, reported only because it is the descriptive fact a
reader will otherwise reconstruct wrongly: M1 LEGAL **14.23**, M1 IRR **7.86**, M1
OTHER 8.61, corpus 10.34. The legal register conditionalises about **1.8× more often
per word** than the eschatological one. This number is a rate with a word count in the
denominator and is exactly the kind of statistic this test was designed to avoid; it is
here as description, not as evidence.

---

## 6. HONEST LIMITS

**1. The irrealis arm is half a single surah.** Under M1, the polemic ∪ eschatological
group is 36 surahs but only **12 of them carry any conditional particle at all**, and
**Q 6 al-Anʿām alone supplies 45 of the arm's 91 tokens (49.5 %) and 18 of its 34
irrealis tokens (52.9 %)**. Under M2 the arm is dominated even more starkly by
**Q 9 al-Tawba at 58.5 %** — and Q 9 is one of the most heavily legal surahs in the
corpus, which M2's first-token rule assigns to the *polemic* group because its Sinai
label is `polemical-legal`. **The M1/M2 gap is, to a first approximation, the question
of where Q 6 and Q 9 land.** No test resting on that is robust, and the NULL should be
read at least as much as an underpowered instrument as a refuted hypothesis.

A jackknife over the 53 contrast surahs (post-hoc, descriptive, no inference) gives
D_pooled ranging **+0.132 … +0.171**, all 53 the same sign; dropping Q 6 moves it to
+0.132. The **direction** is stable; the **significance** never was.

**2. Register labels are surah-scale.** cross-finding-025's standing prescription is to
re-test at the scale where structure operates, and register plainly operates at pericope
scale — Q 2 is legislative *and* narrative *and* polemical within one surah. No
pericope-scale register labelling exists on disk, and building one here would have been
a hand-assigned proxy of exactly the class `findings/PROXY-CLAIMS.md` exists to prevent.
**This is the single largest limitation of the design and it was recorded in the
pre-registration before the run (§9.1), not after seeing the NULL.**

**3. The coarse mapping is a researcher choice and it matters enormously.** M1 and M2
are both mechanical and both defensible, and they differ on 21 surahs; H1 moves from
p(max) = 0.0439 to 0.3305 and H3 from 0.1095 to 0.4804 between them. Any future work
here must treat the mapping as a first-class rules-tuple, not a preprocessing step.

**4. No classical anchor was located.** The al-Zarkashī PDF is image-only (§1). The
grammatical premise is standard and uncontroversial, but this finding has **no
verified classical citation**, and none should be added to it without reading a
machine-readable text.

**5. One implementation detail was not covered by the pre-registration.** If a permuted
or observed statistic were undefined (a group with zero tokens in a cell), the draw is
counted **into** the tail, which can only inflate p — a tightening, resolved
conservatively. **It never fired:** `none_statistic_log` is empty for all 144
permutation p-values.

**6. The tuple axis is weak.** T2 is a 95.3 % subset of T1 (§2.1). Only the mapping axis
is a genuine rules-tuple test. The protocol's "≥ 2 rules-tuples" requirement is met on
both axes, but only one of them carries information.

**7. This says nothing about cross-finding-028's classifier.** Whether the conditional
axis would improve H-NEW-2530's register separability was **not** tested and cannot be
inferred from these numbers. That requires re-running that pipeline with a new feature,
under its own pre-registration.

---

## 7. WHAT THIS MEANS FOR THE SURROUNDING WORK

**F-3's prior was wrong.** `HANDOFF/FRONTIER-MAP-2026-08-07.md` records the prior for
F-3 as *"CONFIRMED. Cheap, and it directly extends a law that was minted 2026-05-30."*
It was cheap. It did not confirm. The frontier map's confound note named "verse length
and surah length — the legal register lives in long surahs"; the measurement says the
surah-length half is nearly absent (ρ = +0.07 on verse count) and **the verse-length
half is the whole confound** (ρ = +0.55).

**cross-finding-028 does not gain a fourth column.** Its claim — that register is coded
at the function-word grain — is not damaged by this result, but it is now **bounded**:
here is a function-word axis, chosen on strong grammatical grounds, that does **not**
carry register once verse length is held fixed. cross-finding-028's own open follow-up
2 proposed resolving the legal↔eschatological blur with an added legal-specific feature.
**The conditional-modality axis is not that feature.**

**A NULL that bounds a law is worth as much as a column that extends it.** The
distinction being tested — realis vs irrealis modality — is one of the sharpest
semantic contrasts available in the Arabic particle inventory, and it is *not* how this
corpus separates its legal register from its polemical one. That is a fact about the
text, not merely about this test.

---

## 8. THE INSTRUMENT — why QAC lemma was mandatory

Recorded because it is reusable and because it would silently wreck any repeat of this
test done by substring search:

| lemma | COND | other tags on the same lemma |
|:--|--:|:--|
| `<in` (*in*) | **578** | **NEG 114**, CERT 5 |
| `law` | **185** | SUB 16 |
| `lawolaA^` (*lawlā*) | **35** | **EXH 40** |

**`in` is a negative particle 114 times** — substring counting inflates the realis arm
by ~20 %. **`lawlā` is exhortative (*taḥḍīḍ*, "why not…?") more often than conditional**
— 40 EXH against 35 COND — and the *taḥḍīḍ* use carries no counterfactual presupposition
at all. Nothing else on disk separates these.

Excluded by locked rule as *asmāʾ al-sharṭ* and the temporal conditional (they carry no
realis/irrealis marking): `man` 184, `maA` 23, `{l~a*iY` 22, `>am~aA` 11, `>ayon` 3,
`Hayov2` 2, `mahomaA` 1, `<i*aA` 1, `>aY~` 1. Total POS:COND = **1,049**; the tested
realis/irrealis apparatus is **801** of them.

---

## 9. WHAT WOULD MOVE THIS

In descending order of expected value, each requiring its own pre-registration:

1. **Pericope-scale register labels.** The stated largest limitation. Requires a
   labelling that is not hand-assigned — e.g. derived from an existing pericope
   segmentation plus a mechanical rule over marker phrases.
2. **A verse-length-matched sub-corpus test.** The per-quintile breakdown (below) shows
   the contrast is not uniform across verse lengths; a design powered *within* the
   17–21-word band would be the sharpest form of the question.
3. **Cross-corpus baseline.** Does al-Bukhārī's legal material also run low on `law`?
   If ordinary Arabic legal prose does the same thing, the whole axis is genre-generic
   and the question is settled the other way. Given 2026-08-07, this control should
   arguably come first.

The primary cell inside fixed host-verse-length quintiles (T1, M1) — the reason the
verse-length-matched statistic behaves unstably:

| host-verse words | IRR irr/tot | share | LEGAL irr/tot | share | diff |
|:--|--:|--:|--:|--:|--:|
| ≤ 11 | 10/30 | 0.3333 | 4/18 | 0.2222 | +0.111 |
| 12–16 | 5/19 | 0.2632 | 21/69 | 0.3043 | **−0.041** |
| 17–21 | 10/21 | 0.4762 | 8/59 | 0.1356 | +0.341 |
| 22–30 | 4/14 | 0.2857 | 22/100 | 0.2200 | +0.066 |
| > 30 | **5/7** | 0.7143 | 23/116 | 0.1983 | **+0.516** |

The sign **reverses** in the 12–16 band, and the largest gap sits in the band where the
irrealis arm holds **7 tokens**. `D_verse` = +0.2206 is larger than `D_pooled` = +0.1582
precisely because it up-weights that sparse band — which is why it is also the binding
control.

---

## 10. FILES

- Pre-registration: `prereg-h-new-3010-conditional-register.md`
  (SHA-256 `2b1718af47814c1eebc38178977074eba2631e45a7ff43e0ff0e98ad8c11fe93`, embedded
  in the script and verified at runtime)
- Script: `scripts/h-new-3010.py`
- Run (immutable, write-once): `runs/h-new-3010/20260809T065744Z/` —
  `manifest.json`, `results.json`, `verdict.txt`
- Post-hoc diagnostic: `scripts/h-new-3010-posthoc-null-means.py` →
  `runs/h-new-3010/POSTHOC-20260809T070155Z-null-means/`
- Data: `data/morphology/quranic-corpus-morphology-0.4.txt`,
  `findings/classical-sources/neuwirth-sinai-genre-labels.tsv`,
  `data/hafs-verse-counts.tsv` (verse counts verified equal for all 114 surahs),
  `data/revelation-order.csv` (descriptive cross-tab only)

---

*H-NEW-3010 run 2026-08-09 by Waiel Al-Shujaa. The direction was right in all twelve
tests and it was not enough; forty-three per cent of the contrast belonged to verse
length, and the register labels were left holding the rest at z = +1.83. Published NULL
at the same prominence a PASS would have received. Bismillāhi al-Raḥmāni al-Raḥīm.*
