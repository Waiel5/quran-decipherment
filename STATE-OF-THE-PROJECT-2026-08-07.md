---
title: State of the project — 2026-08-07
author: Waiel Al-Shujaa
date: 2026-08-07
status: CANONICAL ORIENTATION DOCUMENT — read this before anything else in the repository
---

# State of the project — 2026-08-07

**Read this first. Nothing else in this repository is a safe starting point.**

On 2026-08-07 this project ran its first genre controls. Two audits — H-NEW-2680 and
H-NEW-2720 — put thirteen standing laws through a matched Arabic control, and **almost none
of them survived**. Three of the four "pillar laws" fell. The iʿjāz anti-twin fell and
reversed. The compression-tail family fell. The absence of a document like this one is why
those laws kept propagating into new work for months after they should have been questioned.

**This project is much smaller than it claimed to be yesterday.** What follows is an honest
statement of what stands, what fell, what was established as a negative — which is the
project's most defensible output — and what would actually be needed to settle the rest.

Every number below is cited to a file. Nothing here is asserted from memory.

> ### Updated later on 2026-08-07 — two audits changed §1 and §2
>
> This document was written mid-day. Two further audits landed the same evening and **both
> changed what §1 may claim**, so §1 has been restated at post-audit strength. What the
> document said before is preserved in the two rows added to §2 and in the sources cited
> there; nothing has been quietly softened or hardened.
>
> - **H-NEW-2760** audited Pillar 1 against a null that matches its nuisance parameter.
>   **The law survives — the first standing claim in this project to do so — and its
>   published `p = 3.17 × 10⁻¹²` is retired.** §1.1 rewritten.
> - **H-NEW-2730** genre-controlled the scansion ordering of H-NEW-2690. **The three-way
>   ordering falls; one of its two legs survives.** New §1.5, and the row in §2.
>
> The lesson of the day is now stated twice over: **a law that has never met a control is a
> description, and a p-value computed against the wrong null is a number, not a strength.**

> ### Updated again, late on 2026-08-07 — four further audits, and one of them cuts both ways
>
> Four more findings landed after the two above. They are recorded here at their own strength,
> and the most important thing in them is **not** a new law — it is that the same defect that
> demoted a dozen overclaims also **concealed a real one**.
>
> - **H-NEW-2820** audited the two most-cited flagged claims in the repository. They moved in
>   **opposite** directions. H-NEW-126 Cell A collapsed into its denominator. **H-NEW-570's
>   published NULL reversed** — the muqaṭṭaʿāt *are* a content cluster. New §1.6 and two §2 rows.
> - **H-NEW-2840** asked what that cluster is made of. **It is one cluster and the letters do not
>   carve it.** §1.6.
> - **H-NEW-2850** measured whether derivational form tracks subject agency. `NULL` under its
>   locked gate on both classifiers, with a large association that survives the confound that was
>   supposed to kill it. New §1.7.
> - **H-NEW-2810** re-derived the nine hard-coded literals circulating in this repository. **Seven
>   confirm exactly.** H-NEW-192's two are reachable but its published model is not. New §2 row.
>
> The lesson is now stated a third time, in the direction nobody was watching: **a null that
> cannot draw the thing it compares against is not a comparison, and it hides a result as
> readily as it manufactures one.**

---

## 0. The control-first rule — read this before reporting any group result

**Two claims were reported with enthusiasm on 2026-08-07 before their obvious control had been
run. Both died.** They were reported hours apart, by the same discipline that had spent the
whole day dismantling other people's uncontrolled claims. The rule that follows is written at
the top of this document because that is where it would have been read in time.

> **Before reporting any striking group result, check whether the group is contiguous,
> size-homogeneous, or period-homogeneous — and run that control first, not second.**

**The worked example is the ḥawāmīm, and it is worked here because it is the one that got
furthest.** H-NEW-2820 found the ḥawāmīm-7 at the **0.05th percentile** of a size-matched null —
10.7 % tighter in root content than size-matched surah sets, in every arm including the
parameter-free one. That was reported as the cleanest result in the finding. **The ḥawāmīm are
surahs 40–46: seven consecutive chapters of similar length.** The control that fact demands —
compare them to other consecutive runs — was not run until H-NEW-2840, several hours later. It
returns: the ḥawāmīm sit at the **47.71st percentile** of all 109 consecutive six-blocks in the
mushaf taken raw, and matched partitions of al-Bukhārī and al-Jāḥiẓ cut at the same seven slots
reproduce their tightness **47.5 % and 52.0 %** of the time. The result is not refuted, and it is
not a discrimination either.

**The second case is the scansion ordering.** H-NEW-2690 reported that this corpus sits between
poetry and prose in metricality and read it as al-Bāqillānī's *neither* nathr *nor* shiʿr,
operationalised. The control that fact demands — hold unit length fixed — was not run until
H-NEW-2730. Re-cutting this corpus's **own verses** to ḥadīth sentence lengths moves the
statistic **99.4 %** of the way to ḥadīth's value, using no baseline text at all (§1.5).

**Three homogeneities, and the check for each is one line of code:**

| if the group is… | the control | the case |
|:--|:--|:--|
| **contiguous** in the mushaf | compare against consecutive runs of the same length — and match them on size and period | ḥawāmīm 40–46, ALM's blocks, ṭawāsīn 26–28 |
| **size-homogeneous** | match the null on the size channel with the highest size-only R², ranked on the data | H-NEW-126's core-5, H-NEW-570's 29, the whole compression-tail family |
| **period-homogeneous** | cross-stratify on Meccan/Medinan | the muqaṭṭaʿāt are 10.3 % Medinan against 29.4 % for the rest; it is worth a third of H-NEW-570's matched effect and all of H-NEW-2840's vocabulary result |

**And the cheapest diagnostic of all, which precedes every p-value: does the null model ever
draw a comparison set like the observed one on the nuisance channel?** For H-NEW-570 the answer
was **0 of 10,000**. One line of code, no new statistic, and it settled the claim before any
p-value was computed.

Sources: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md` §§2.2, 3.3;
`findings/phase-b-hypotheses/h-new-2840-muqattaat-cluster-structure.md` "THE CONTIGUITY CONTROL"
§§C1, and §7.3(b); `findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`; the
general rule and its screens, `findings/UNIT-DRIFT-DEFECT.md` §3 Screen B and §4.1.

---

## 1. What survives, with its actual strength

Five things. Each carries its caveat inline, because the caveat is part of the result. **Each
is stated at its post-audit strength, not the strength it was published at** — where those
differ, the difference is named.

### 1.1 The muqaṭṭaʿāt are book-introduction markers — **survives its nuisance parameter; its published p-value does not**

**This is the strongest thing in the project and the only claim here that has met a null
matching the variable that drives it.** H-NEW-2760 supplied that null. Read the two halves
separately, because they are separately true.

**(a) The law survives.** H-NEW-53's headline — 24 of 29 muqaṭṭaʿāt surahs reference *kitāb*
or *qurʾān* in their first three verses — **reproduces exactly at 24/29**, and it survives a
null that permutes the muqaṭṭaʿāt label *within opening-window-size quintiles*, so the
opening-token budget is identical by construction: observed **24 against a null mean of
9.304**, rate ratio **2.580**, z = +7.01, p = 1.0 × 10⁻⁴, observation eleven above the 95 %
band top. **Every matched null in the ladder still places the observation outside its own
95 % band. The effect never vanishes.**

**(b) `p = 3.17 × 10⁻¹²` is withdrawn as a description of that strength.** It is
arithmetically correct and inferentially void: it prices a hypergeometric that draws 29
surahs *uniformly from 114*, which requires the 29 to be exchangeable with the other 85. They
are not, and **this project established that itself** — `h-new-46` is a STRONG-PASS showing
muqaṭṭaʿāt surahs concentrate in long surahs. **The honest effect size is a rate ratio
between 1.27 and 2.58, not a twelve-order-of-magnitude tail.**

**The sharpest form of the law is new, positional, and length-free.** Conditioning on each
surah's own verse count and its own number of Book-bearing verses: **all 29 muqaṭṭaʿāt surahs
mention the Book somewhere** — so do 40 others — but they place the **first** mention at
**0.0996** of the surah against **0.3403** for the other 40 (Δ = −0.2407, p = 5.0 × 10⁻⁴).
The law is not *"muqaṭṭaʿāt surahs mention the Book"*; it is ***"muqaṭṭaʿāt surahs announce it
at the top."***

**Three qualifications travel with the verdict and are not separable from it.**
1. **H-NEW-2760's H2 failed its gate.** The nuisance channel it made primary — opening-window
   size, ρ = +0.1678 — is the *weaker* of the two available; whole-surah length is stronger at
   ρ = +0.4583. **Against that stronger channel the rate ratio falls to 1.694**, and under the
   locked rule's own RR < 2.0 clause applied to that stratification the verdict would read
   GENRE-SHARED-BUT-LARGER. Both numbers are the reader's entitlement.
2. **DISCRIMINATES was earned on the within-corpus nulls, not on the genre arm.** In
   H-NEW-2760's matched-partition control **0 of 3 baselines clear the gate, and the poetry arm
   is a published pre-commit violation** (locked positive, observed ρ = −0.0343).
3. **The cross-genre half remains partly definitional**, exactly as this document said before.
   The 2680 marker-class search recovers the muqaṭṭaʿāt themselves at **p_bonf = 4.7 × 10⁻¹³**
   and finds nothing in either baseline — but only **6** Bukhārī and **1** poetry pseudo-surah
   mention *kitāb* or *qurʾān* in their opening units at all. **"Only scripture talks about
   itself as a book" is a weaker claim than "only this corpus has an engineered marker system,"
   and no control run so far separates the two.** H-NEW-2720 sharpened the problem rather than
   resolving it: al-Jāḥiẓ's *Kitāb al-Ḥayawān* — adab prose, not scripture — yields **الكتاب**
   and **الكتب** among its strongest marker classes, because adab prose talks about books
   constantly.

Sources: `findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md`;
`findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` §7.

### 1.2 The post-kink content-compression **slope** — **genre-shared-but-larger**

Holding the unit-size profile identical by construction, this corpus's post-kink
content-compression slope β = **−0.01343** is steeper than **all 200** matched al-Bukhārī
partitions and **198 of 200** matched al-Jāḥiẓ partitions (196/200 on replication). Its
content-distance falls about a third faster than ḥadīth's under the same size profile.

**This is a difference of degree on one axis of one law, not a discrimination**, and it is
the *only* axis in the entire nine-law sweep where this corpus leads. It is emphatically not
the "R² = 0.986, 98.6 % of mushaf cohesion-variance in one parameter" headline the law is
cited for — that R² is genre-shared and 91.5 % explained by unit size (§2.3).

Source: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md` §2.1.

### 1.3 The muṭāwaʿa / causative direction — **real, and narrower than it was reported**

The team's morphology line is the healthiest thing in the project, because it corrected
itself repeatedly under adversarial audit. Its current state, accurately:

- **H-NEW-2540** (Form II→V, III→VI reduce overt dependency-object realization):
  `DUAL-FAMILY SUPPORT as an EQTB-internal association — NOT independent confirmation
  (parser contamination confirmed)`. The load-bearing evidence is the parser-free
  object-pronoun channel in its §2b, not the treebank association.
- **H-NEW-2600** (the muṭāwaʿa lattice): its `LATTICE-STRUCTURED` verdict was **RETRACTED on
  2026-08-07** for violating its own locked decision rule. The corrected verdict is **2 of 5
  registered arms pass** — P2 (I→VIII) and N2 (I→IV) at pA = pB = 1.0 × 10⁻⁴; **N1 (I→II)
  fails its dual-null gate at pA = 0.00060 against a 0.0005 threshold**, and exhaustive
  enumeration of all 2³⁷ sign-flips confirms the miss is not a seed artefact. P1 and P3 are
  unresolved.
- **H-NEW-2650** (pronoun channel): `CHANNEL DEGRADED by the locked rule`, triggered by a
  single arm on an n = 1 denominator — but **all five locked signs held, no arm lost
  significance, and every correction enlarged the parent effects.**

**What genuinely stands here is the causative reverse-control.** The direction was locked in
advance — if the causative arms had come out positive the verdict was pre-committed to
`INSTRUMENT-CONFOUNDED` — and they reversed as locked. That is a real falsification control
that a real effect passed. What does **not** stand is the word "lattice."

Sources: `h-new-2540-form-v-valency.md`, `h-new-2600-mutawaa-lattice.md`,
`h-new-2650-pronoun-channel-validation.md`.

### 1.4 H-NEW-2710 — **TOPICALITY-EXPLAINED**

The replacement for the withdrawn Pillar 4. Surah titles are **not** independent of content
density (the original law was wrong), and they are **not** strongly dependent either (the
proposed inversion was also wrong). Against a null matched on **both frequency and
dispersion**, the residual rate ratio is **1.285** at rank-1 and the median rank is
statistically indistinguishable from null (2 vs 2.24, **p = 0.76**). The residual is
topicality: a root concentrates where its topic is discussed.

This is the model for how a claim should end — both the thesis and its antithesis falsified,
with the mundane explanation surviving and quantified.

Source: `findings/phase-b-hypotheses/h-new-2710-title-density-retest.md`.

### 1.5 The corpus is measurably less metrical than pre-Islamic poetry — **half of al-Bāqillānī, and only half**

H-NEW-2690 reported that on `d_min`, the length-invariant distance to the nearest classical
metrical template, this corpus sits **between** poetry and prose, and read that as an
operationalisation of al-Bāqillānī's *neither* nathr *nor* shiʿr. H-NEW-2730 genre-controlled
it. **The three-way ordering does not survive. One of its two legs does.**

**What survives — the *not-poetry* half.** The corpus is less metrical than the muʿallaqāt,
and that contrast is not a length artefact: unit length explains **5.1 %** of the gap; it
holds at full size in the one syllable-length bin where the arms overlap (**0.21739** against
poetry's **0.14815**); it survives a per-unit noise control matched on length *and* syllable
weight at p = 1 × 10⁻⁴ in both rules-tuples; and re-cutting this corpus's own verses to
bayt lengths moves it only **7.5 %** of the way toward poetry.

**What falls — the *not-prose* half.** Cutting this corpus's **own verses** to ḥadīth sentence
lengths moves its `d_min` **99.4 %** of the way to ḥadīth's value (0.22222 → 0.23953 against
al-Dārimī's native 0.23963), **using no baseline text at all**. A matched partition of
al-Dārimī lands at **0.22222** — this corpus's own median to five decimals — and one of
al-Bukhārī at **0.21893**, with **199 of 200** offsets at or below it. At matched syllable
length the two medians are **identical**. And only **49.2 %** of this corpus's verses are more
metrical than their own length-and-heaviness-matched random twin — a coin flip — against
**88.3 %** of poetry abyāt and **62–69 %** of ḥadīth sentences.

**So: one real contrast plus one artefact, not a measured intermediate position.** The
classical thesis is untouched — "neither *nathr* nor *shiʿr*" was never a claim about medians
of normalised edit distances — but its stated empirical operationalisation is half withdrawn.

**Caveats.** There is **no vocalised adab prose on disk**, so al-Jāḥiẓ cannot be tested on this
statistic at all and the prose control is ḥadīth-only. The poetry side rests on 240 abyāt
covering **two of sixteen** meters. Nothing here shows the position is unusual among elevated
or religious Arabic prose.

Source: `findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`.

### 1.6 The muqaṭṭaʿāt surahs are one content cluster — **and the letters explain nothing about it**

**This entry exists because a published NULL turned out to be wrong in the direction nobody
audits.** It has two halves and they must be read together, because a reader who takes only the
first will overclaim and a reader who takes only the second will miss a real result.

**(a) The cluster is real, and it was hidden by the same defect that demoted everything in §2.**
`h-new-570` reported that the muqaṭṭaʿāt are **not** a content cluster — 65.62nd percentile,
"orthogonal to content" — and thirty external files inherited that as evidence of absence.
H-NEW-2820 reproduced its arithmetic exactly (`d̄ = 0.938813123152709` against a published
`0.9388131231527093`) and then asked the cheap question: **does its null ever draw a set as
large as the muqaṭṭaʿāt? Not once in 10,000 draws.** Size-matched, the 29 fall from the 65.62nd
percentile to the **0.45th**, crossing the claim's own 10 % bar; cross-stratified on period as
well they sit at **5.44**. H-NEW-2840 rebuilt the matrix in a separately written harness and
reproduces this at **5.48** period-matched and **0.43** size-only. The effect is small and the
percentile is not: the 29 are **3.6 % tighter** in root content than size-matched surah sets.
The ḥawāmīm-7 are **10.7 % tighter**, at the **0.05th** percentile.

**It is not adjacency, and that is the strongest single thing here.** Twenty-four of the 29 sit
in a mushaf run of length ≥ 2. Delete **every** pair within ten mushaf positions of each other —
123 of the 406 pairs — and recompute the null under the identical restriction: the remaining 283
pairs leave the result at the **5.25th** percentile against **5.07** unrestricted. **The
clustering is carried by the surahs that are nowhere near each other.** Nor do the baselines
reproduce it: only **6.5–10 %** of arbitrary matched partitions of al-Bukhārī or al-Jāḥiẓ reach
the Qurʾān's value, in two instruments that agree.

**(b) The letters do not carve the cluster. Every arm that asked them to, failed.**

- **The set is *less* internally sub-structured than matched sets**, not more — max silhouette
  **0.0829** against a null mean of 0.1103, at the **9.31st percentile**. The registered direction
  was the opposite one.
- **What structure exists is size, and it cuts across the letter classes.** At k = 4 the two large
  clusters differ by a factor of **1.7** in median word count (1159 against 694) and split the
  ḥawāmīm, ALM and ALR down the middle. The dendrogram is a size gradient wearing no letters.
- **"The opening string predicts content position" fails at the corrected bar** — Δ = −0.03378 at
  **p = 0.0325** (free permutation) and 0.0348 (size-restricted) against **α_bon = 0.00417** over
  the registered family of twelve. **And the whole of it is one class**: dropping the ḥawāmīm
  takes p from 0.0325 to **0.156**, while dropping any other class leaves it where it was or
  improves it.
- **The fact that needs no null at all:** of the 19 surahs belonging to a multi-member letter
  class, **only 4 have their nearest neighbour inside their own class** — two pairs, Q 2 ↔ Q 3 and
  Q 41 ↔ Q 46. **Fifteen of nineteen sit closest to a surah that opens with a different string.**
- **No root distinguishes the 29 from the other 85 once size and period are held fixed** —
  **0** roots survive BH at q = 0.05, against **19** under the size-blind null. And the size-blind
  list is a **Meccan-versus-Medinan register list**: *say*, *sign*, *follow* enriched; *oath*,
  *riḍwān*, *mawlā*, *jihād*, *food* depleted. The muqaṭṭaʿāt are 10.3 % Medinan against 29.4 %
  for the rest. Its fourth-strongest depletion, `Alw` الو, has **31 of its 37 corpus tokens in
  Q 55 al-Raḥmān alone** — a surah that is not one of the 29.
- **These 29 surahs group as long Meccan surahs, not as letter-sharers.** That sentence is the
  finding.

**Two classes must be named individually, because they are the two a reader will ask about.**

- **The ḥawāmīm are the one arm that clears α_bon** — ḤM-6 at **p = 0.00090**, the 0.08th matched
  percentile — **and then lose the genre control**: they are the contiguous run Q 40–46, they sit
  at the **47.71st percentile** of all 109 consecutive six-blocks taken raw, and matched
  partitions of al-Bukhārī and al-Jāḥiẓ cut at the same slots reproduce them **47.5 % / 52.0 %**
  of the time. Adding Q 42 destroys the within-corpus result too (p = 0.199). See §0.
- **ALM is the opposite shape and is the one open question worth a purpose-built test.** It is
  the non-contiguous family — {Q 2, 3} and {Q 29–32}, two blocks twenty-six surahs apart — so
  adjacency cannot explain it. It sits at the **2.81st** matched percentile (z = −1.950,
  p = 0.0282), beats size-and-period-matched consecutive blocks at **z = −7.77, p = 1 × 10⁻⁴**,
  and is reproduced by only **10.5 % / 13.0 %** of arbitrary baseline offsets — the best genre
  margin of any class. Strip its own internal adjacency and score only its **8 cross-region
  pairs**: still directional at **p = 0.046**. **It never clears α_bon = 0.00417 and it survives
  every control put to it.** Neither ALM nor the ḥawāmīm is established; they fail in opposite
  ways, and ALM is the one a next test should be built for.
- And **al-Biqāʿī's Q 29–32 "tight Meccan block" is adjacency and nothing else** — 66.42nd
  percentile of matched consecutive blocks, 33.67th under the period-matched null. **ALR**, the
  family with the strongest classical prior, moves the *wrong* way under matching: from the 56th
  size-blind percentile to the **79.31st**, more dispersed than matched sets.

**Three qualifications travel with this entry and are not separable from it.**

1. **The matched null is more than half this group.** A "matched random 29-set" is on average
   **16.32 of the muqaṭṭaʿāt themselves** (56.3 % overlap), because the 29 dominate the upper size
   range. Every matched NULL above — the vocabulary result above all — is correspondingly **weak
   evidence of absence**, and every matched pass is conservative.
2. **Conditioning on size may remove mechanism, not only confound.** `h-new-46` is a STRONG-PASS
   that muqaṭṭaʿāt concentrate in long surahs; a size-matched comparison group of 29
   non-muqaṭṭaʿāt **cannot be built from the other 85 at all** (bin 3 of 5 needs 14 donors and
   contains 9). The correct reading is narrow: *given surah sets of the same size profile*, the
   muqaṭṭaʿāt set is measurably tighter in root content.
3. **This is not a vindication of al-Biqāʿī and not a refutation of al-Suyūṭī.** It removes an
   empirical falsification; it decodes nothing. What is withdrawn is the assertion that the
   statistic *empirically vindicated* epistemic humility — the statistic was measuring the size
   of the surahs. And **this is not an independent confirmation of Pillar 1**: same 29 surahs,
   same corpus, same selection. Removing the entire revelation-and-recitation vocabulary — Book,
   recite, send down, sign, remind, inspire, criterion, 1,587 tokens — moves the matched
   percentile only from 5.48 to **6.94**, which refutes double-counting but does not make two
   properties of one group into two results.

Sources: `findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md` §§1, 2.2, 3.2, 3.3, 4.2,
7.2, 8; `findings/phase-b-hypotheses/h-new-2840-muqattaat-cluster-structure.md`
§§"THE CONTIGUITY CONTROL", "ALM", 2, 3, 3.1, 3.2, 4, 5, 7.1, 7.3, 8, 11;
`findings/H-NEW-570-REVERSAL-2026-08-07.md`.

### 1.7 Form and agency — **`NULL` under the locked gate, and the failure is power, not the effect**

H-NEW-2850 asked whether derivational verb form tracks the agency class of the grammatical
subject, and whether any such correlation survives being conditioned on transitivity — since form
is already known to track object realization (§1.3). **The verdict is `NULL` on both classifiers
and it is not being overridden.** But a `NULL` that fails on one specific clause is not the same
as an absence, and the difference is stated here rather than left to the finding.

**What failed.** The pre-registration required, for any arm to count, that **both** the exact
root-level sign test **and** the token-level permutation null clear a raw p of 0.0005. **Null B
clears it on four of five `C-WIDE` arms and two of five `C-STRICT` arms. The root-level sign test
clears it on none** — its best value anywhere is **5.40 × 10⁻³**. Under the locked conjunction no
arm passes. The stricter of two disagreeing nulls is the root-level one, and it fails.

**What did not fail, stated at the same prominence.**

- **The association is large.** Divine-subject rate **0.5089** for Form II against **0.1176** for
  Form V; the two causatives sit at 0.44–0.52, the base form at 0.24–0.25, the four *muṭāwiʿ*
  forms at 0.00–0.23. **The person-free classifier reproduces the ordering** — `C-STRICT`, which
  never sees a person feature, puts Form II at **0.5214** against Form V at **0.0694** — so this
  is not the corpus's person deixis wearing an agency label.
- **All five locked `C-WIDE` signs hold, including both causative reverse-controls**, so the
  pre-committed `INSTRUMENT-CONFOUNDED` escape hatch was available and the data did not take it.
  **48 of 50 signed sensitivity cells** hold their locked direction; the two that do not are both
  `C-STRICT` cells at 3 and 4 roots.
- **It survives the confound that was supposed to kill it.** Conditioning on overt object
  realization (Cochran–Mantel–Haenszel, strata = root × object-clitic) leaves every well-powered
  arm pointing the same way **inside both strata**, at odds ratios of **6.21, 3.22, 0.292 and
  0.217** — on opposite sides of 1 exactly as the doctrine predicts.

**So the honest reading is that the evidence is token-weighted rather than lexically general.**
Ten roots of fourteen point the predicted way on II→V, against eighteen of nineteen in the parent
object-realization result. This project's registered bar for a confirmatory claim is lexical
generality, and it should stay that way.

**The queued redesign, and why the current one cannot answer the question.** Eligibility requires
**≥2 classified tokens of each form, of the same root** — so a root only becomes evidence when the
corpus supplies both members of the pair *and* the classifier can see the subject of both. It
usually cannot: the primary classifier covers **15.94 %** of active verbs, **8,479 third-person
verbs carry no explicit subject** and are invisible to it, and the arm testing III→VI has **zero
eligible roots** while I→II has three. The showcase root ط ه ر is the case in miniature — it has
nine Form II tokens, the classifier sees **three**, and the six it cannot see are exactly the
divine-agent ones, including the showcase verse itself. **A next test must therefore stop making
the within-root form-pair the unit of evidence** — it must not require both forms *and* both
subject types to co-occur inside one root. Two routes are open and neither needs new annotation:
score each form against the corpus-wide subject-class base rate so a root contributes on one form
alone, or resolve the subjectless third-person verbs by coreference and re-run the existing
design on the coverage that unlocks. *(Queued, not registered — this is the implication of the
finding's own §5 and §9.3 diagnosis, not a result in it.)*

**One self-reported bias travels with the entry.** Of the 2,903 explicit-subject classifications,
**79 (2.72 %)** take a subject whose word carries a clause-linking prefix, and **43 of the 811
divine calls (5.30 %)** are of that kind. It is form-correlated — Form X 14.29 %, Form IV 3.97 %,
Form I 2.55 %, Form II 0.71 % — and **it runs in the direction that favours the hypothesis**,
since Form IV is the causative in the strongest arm. The absolute numbers are small (15 Form IV
tokens corpus-wide) and the correction was not registered and not applied.

Source: `findings/phase-b-hypotheses/h-new-2850-agency-grammar.md` §§2.2, 3, 3.1, 4, 5, 7, 8, 9;
eligibility rule at `findings/phase-b-hypotheses/prereg-h-new-2850-agency-grammar.md` §7.1,
decision rule §9.

---

## 2. What fell on 2026-08-07, and why

One line each: the claim, the control, the number.

| what fell | the claim | the control | the number |
|:--|:--|:--|:--|
| **Pillar 2 — the geodesic** | mushaf order is information-geodesic-optimal, z = −11.46 | 114-unit length-matched partitions of the baselines | al-Bukhārī **z = −13.84**, poetry **−15.13**, this corpus **−11.50** — both baselines *more* extreme |
| **Pillar 2, again** | the surah seams carry the effect | re-cut this corpus's own verses at offsets ignoring every seam | z = −11.23, −13.18, −12.92, −12.33, −12.62 — four of five *more* extreme than the real division |
| **Pillar 2, length control** | "MW-1 length control is working" | actually compute it | sorting surahs by **length alone**, using no vocabulary, reaches **z = −8.66**; the mushaf's true margin over pure length is **2.80 σ**, not 11.46 |
| **Pillar 3 — scale-of-aggregation flips** | thin-marker cohesion flips at pericope scale, a corpus-wide law | same test, five best-shot marker classes per baseline | poetry **5/5**, al-Bukhārī **4/5**, al-Jāḥiẓ **5/5**; poetry's largest flip z = +22.4 against this corpus's +24.7 |
| **Pillar 4 — title-density independence** | titles are independent of content density | frequency-and-dispersion-matched null | withdrawn and replaced by H-NEW-2710; the "47/89 → 48/89 correction" that preceded it was itself an **invalid cross-metric substitution** |
| **The iʿjāz anti-twin** | r(content × rhyme) = −0.86, "cross-corpus distinct vs poetry at p < 10⁻¹⁰" | matched partition instead of equal 30-bayt blocks | poetry **r = −0.872** vs this corpus's **−0.870**; al-Jāḥiẓ **−0.931**; **this corpus at the 3rd percentile** of adab prose |
| **The anti-twin, mechanism** | it is an architectural property | control for unit size | r(d̄_content, log size) = **+0.956**, r(d̄_rhyme, log size) = **−0.838**; partial r = **−0.432**; equal-cut r = **−0.338** |
| **The compression tail** | d̄_content law at **R² = 0.986**, one parameter | matched prose partitions; log-size regression; equal-size re-cut | al-Jāḥiẓ reaches **0.991**; **log-size alone gives 0.9147**; this corpus's own verses cut equal collapse to **0.3388** |
| **The rhyme dispersion-tail** | R² = 0.789, an architectural law | matched prose partitions | **51st percentile** of al-Bukhārī — the middle of the distribution |
| **The phoneme dispersion-tail** | R² = 0.946 | matched prose partitions | 76th percentile; edged by poetry (0.9332 vs 0.9329) |
| **The verse-length tail** | R² ≈ 0.81 | matched prose partitions | **31st percentile** — 137 of 200 baseline cuts more extreme; its words/verse arm is **degenerate by construction** |
| **Anti-chiasmus** | this corpus is anti-chiastic | all four matched corpora | poetry −0.120, this corpus −0.136, al-Bukhārī −0.146, **al-Jāḥiẓ −0.209** |
| **Register separability** | thin grammar separates the three registers at 1.75× lift | same pipeline, surrogate 3-way labels | **poetry 1.842** against this corpus's 1.658 (capped: surrogate labels) |
| **UAS** | a unified architectural significance ranking | it has no null hypothesis | its own frontmatter reads `status: SYNTHESIS`; the dispersion diagnostic puts poetry (1.267) above this corpus (1.166) |
| **The four p-values** | multiply to ~10⁻¹² | check what each null randomises | they are **not commensurable**; only one multiplication is licensed (L1 × L2), and its L2 factor does not mean what it appears to |
| **Pillar 1's p-value** *(evening)* | 24/29 book-reference at **p = 3.17 × 10⁻¹²** | a null that permutes the label **within opening-window-size quintiles** | the **law survives** (§1.1) but the p-value is **withdrawn**: it prices an exchangeable null this corpus does not satisfy. Rate ratio **2.580** against the registered channel, **1.694** against the stronger one |
| **The scansion ordering** *(evening)* | poetry < this corpus < prose on `d_min`, "measurably more metrical than prose" | re-cut **this corpus's own verses** to ḥadīth sentence lengths; matched partitions of two ḥadīth corpora | the prose leg moves **99.4 %** of the way to ḥadīth; a matched al-Dārimī partition **ties** it at 0.22222; al-Bukhārī's **beats** it at 199/200 offsets. **H1b withdrawn; H1a survives** (§1.5) |
| **H-NEW-126's isolate core** *(late)* | the five surahs {Q 16, 21, 22, 23, 25} share root vocabulary at **2.64×** chance, p = 0.0009 — **32 external citing files**; the test that would settle it was queued as "H-NEW-126.1" and never run | permute group membership within quantile bins of the group's own dominant channel, ranked on the data (log root-set size, ρ = +0.9398) | **1.002×, p = 0.459** — the null mean rises from 0.129 to **0.341**, which *is* the observed value. **79 % of the published enrichment is the mechanical Jaccard ceiling** `min\|R\|/max\|R\|`, which uses no vocabulary overlap at all. Cutting al-Bukhārī or al-Jāḥiẓ at the same five slots reproduces it at **z = +3.19 / +3.55** against this corpus's +3.79, and after matching the baselines are the *more* extreme ones |
| **H-NEW-570's published NULL** *(late)* — **and it fell in the other direction** | the muqaṭṭaʿāt are **not** a content cluster: 65.62nd percentile, "orthogonal to content", al-Suyūṭī "EMPIRICALLY VINDICATED", al-Biqāʿī "UNSUPPORTED" — **30 external citing files** | ask the one-line question first: does the null ever draw a set as large as the observed one? | **0 of 10,000.** The null it was scored against contained **no comparison set of comparable size at all**. Size-matched, the 29 move to the **0.45th** percentile (5.44 cross-stratified on period) and the ḥawāmīm-7 to the **0.05th**. **A flagged NULL reversed into a positive result** — the four quoted conclusions are withdrawn as empirical results, and the cluster is §1.6 |
| **H-NEW-600's DOUBLE NULL** *(late)* | ALM-6 and ALR-5 are both NULL; ALR is *"the decisive falsifier… the family with the strongest prior is the one most thoroughly NULL"* | the size-and-period-matched null H-NEW-600 §9 queued as "the cheap next step" and never ran | **the two halves move in opposite directions.** ALM 43.15 → **2.81** (toward cohesion, p = 0.0282, still short of α_bon); ALR 56.25 → **79.31**, *more* dispersed than matched sets — **the ALR sentence survives matching and hardens.** H-NEW-600's honest-limit 7, *"length-controlled per H-NEW-111 MW-1, so this is not a confound"*, is **asserted, never computed, and false**: `d̄` correlates with mean log word count at **ρ = +0.8998**. Its queued H-NEW-620 and H-NEW-630 both return NULL under matching (49.17th, 33.67th) |
| **H-NEW-192's model** *(late)* | mushaf position decomposes at Ridge **R² = 0.759** and RF **0.817**, *"verse-count dominates (~42 % of importance)"* — `verdict: STRONG PASS`, asserted in 15 markdown files, and hard-coded as H-NEW-233's literal decision thresholds | exhaustive evaluation of **all 20,349** admissible 15-feature sets, with the published importance vector as a second, independent constraint | the R² are **reachable and therefore not evidential**: 15 sets hit 0.759 where a normal approximation predicts **≈ 198** by chance, and 30 of 100 reach 0.817. **No candidate reproduces the importance vector** — **0 of 100** match rank order and the best misses by **16×** its bar. The best simultaneous candidate **inverts the published top feature**: verse_count 0.416 → **0.133** while type_token_ratio 0.095 → **0.635**, a deviation of **27×** the bar. **`REACHABLE-BUT-NOT-IDENTIFIED`** — the published number is recoverable by coincidence; the published model is not recoverable at all |

Full evidence: `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` and
`findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`. Per-file correction status:
`findings/PILLAR-CORRECTION-INVENTORY-2026-08-07.md` and
`findings/GENRE-CONTROL-INVENTORY-2026-08-07.md`. The two evening rows:
`findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md` and
`findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`.

**The four late rows, and §§1.6–1.7:**
`findings/phase-b-hypotheses/h-new-2820-group-claims-matched.md`,
`findings/phase-b-hypotheses/h-new-2840-muqattaat-cluster-structure.md`,
`findings/phase-b-hypotheses/h-new-2810-unverifiable-rederivation.md`,
`findings/phase-b-hypotheses/h-new-2850-agency-grammar.md`, and
`findings/H-NEW-570-REVERSAL-2026-08-07.md`. The mechanism common to all of them, with its three
detection screens and the grouping form of Screen B, is `findings/UNIT-DRIFT-DEFECT.md`.

**One result in that batch belongs here as a credit rather than a correction, and it is recorded
because naming the clean cases is part of the rule.** H-NEW-2810 scanned every script in the
repository for a numeric literal bound to a *different* finding's name — a generator, not a
remembered list — and found nine, four of which nobody had previously identified. **Seven confirm
exactly against their own artifacts**, several to ten decimal places. The strongest is
H-NEW-1710's Mūsā total of **136**, the only one re-derived from the corpus rather than from an
artifact: counting Leeds QAC tokens with `LEM:muwsaY\`` returns 136, agreeing three separate ways.
**Only H-NEW-192's two fail both checks.** A CONFIRM here is a transcription check and not a
validation — H-NEW-233's two constants reproduce perfectly and still do not survive a size-matched
null — but the constants circulating in this repository are, with one exception, exactly right.

**Nothing was deleted.** Every original claim remains in place with a notice beside it. The
record of what was believed and when is itself evidence, and erasing it would be a second
dishonesty on top of the first.

---

## 3. The established negatives — the project's most defensible output

**This is the part of the project that held.** Negative results are not consolation prizes
here; they are the strongest thing on the shelf, because each one is an exhaustive,
pre-registered, correctly-nulled retirement of a claim that circulates widely.

- **H-NEW-2660 — HUNT-NULL.** An exhaustive generator over five pre-declared types of exact
  structural coincidence scanned **124,148** zero-tolerance candidates across three
  rules-tuples, found **1,581** exact coincidences, and **zero survive** the whole-space
  Bonferroni threshold α = 4.027 × 10⁻⁷. In the decoupled strata the corpus produces exact
  coincidences at **0.69× to 1.38×** the exactly-computed chance rate, and 432 of 657 cells
  fall *below* their exact expectation. Every per-hit denominator is a closed form in exact
  rational arithmetic, not a sample.
- **H-NEW-2670 — ARTEFACT-OF-CONSTRAINT-STACKING.** The joint-conjunction method
  *manufactures* uniqueness. Its locked rule returned 7 of 40,116,600 letter-subsets at
  p = 1.7 × 10⁻⁷ and its control passed narrowly at q = 0.018 — but a stricter control
  letting each random subset pick its own axes from the same attested menu **failed at
  q′ = 0.248**: roughly **one random 14-letter subset in four** can be made to look as unique
  as the muqaṭṭaʿāt. This is the engine behind letter-numerology, demonstrated.
- **H-NEW-2550.** al-Zamakhsharī's "half of every phonetic genus" is **exactly right** — the
  14 sit at the global minimum of genus-imbalance over all 40,116,600 subsets — and
  **statistically ordinary**: 1,024,500 subsets (2.554 %) tie that minimum.
- **The numerological retirements**, each pre-registered with a proper null: abjad ↔ structure
  (H-NEW-2040), Code-19 divisibility (H-NEW-1530, H-NEW-1600), antonym word-balance
  (H-NEW-2000, H-NEW-2010, H-NEW-2020, H-NEW-2230), surah-position arithmetic (H-NEW-2090),
  the number-word census (H-NEW-2410). Across the exhaustive generators the corpus produces
  *fewer* meaningful coincidences than chance predicts, not more.
- **And now the genre controls themselves** (H-NEW-2680, H-NEW-2720, and in the evening
  H-NEW-2730), which belong in this list: showing that fourteen of the project's own laws do
  not discriminate is a harder and more useful result than any of them was. **H-NEW-2730 adds
  the cleanest demonstration of the day**, because it needs no baseline text: re-cut this
  corpus's own verses to another genre's unit lengths and the statistic walks 99.4 % of the way
  to that genre's value.

---

## 4. Methodological lessons — stated so they are not re-learned the hard way

1. **A control that does not match the nuisance parameter is not a control.** H-NEW-740 is
   the case study, and it is worth studying: a genuine cross-corpus control, properly
   pre-registered, that compared **equal 30-bayt poetry blocks** to this corpus's **unequal
   surahs** and therefore measured the unit-size profile rather than the genre. Its own
   honest-limits section named block size as the risk and reasoned it *"biases AGAINST
   detecting strong content×rhyme structure, again favoring the iʿjāz inference"* — **the
   sign was backwards**, because the driver is size *dispersion*, not size *level*.
   Direction-of-bias reasoning is not a substitute for matching.
2. **Audit your strongest claim first, not last.** The compression-tail R² = 0.986 was the
   most-cited number in the repository and among the least examined. It stood from
   2026-04-28 to 2026-08-07 without a control. The oldest, most-quoted, most-load-bearing
   number is the one most likely to have escaped scrutiny, precisely because everything was
   built on top of it.
3. **A correction that crosses metrics is a new error.** The "47/89 → 48/89" fix applied to
   Pillar 4 substituted a value from a different metric; it was published, propagated, and
   then had to be withdrawn along with the law.
4. **A runner's verdict rule must literally match the pre-registration's.** H-NEW-2600's
   `LATTICE-STRUCTURED` verdict came from code that implemented a *looser* rule than the
   locked text ("causative signs merely pointed negative and any positive arm passed"). The
   pre-registration was correct; the implementation was not. **Diff the verdict logic against
   the pre-registration's decision section before declaring anything.**
5. **Never assert a robustness property — compute it.** "MW-1 length control is working"
   (H-NEW-111) and "block size biases against us" (H-NEW-740) were both asserted and both
   false. H-NEW-2560's independence claim was likewise asserted, never tested, and false.
6. **Check every control for tautology before trusting it.** H-NEW-770's words-per-verse arm
   is identical across all four corpora *by construction* under the matched partition. It was
   caught in pre-registration; it would have looked like a striking confirmation otherwise.
7. **A partition is not a composed book — and that cuts both ways.** Baseline pseudo-surahs
   are arbitrary cuts of a continuous stream. For **contiguity-sensitive** statistics
   arbitrary cuts *preserve* local continuity and make a law *easier* for a baseline, so a
   baseline pass is weak evidence against the law. For **boundary-sensitive** statistics
   arbitrary cuts *destroy* real boundaries, so a baseline pass is strong evidence. State
   which regime each verdict is in; never use the caveat as a blanket excuse.
8. **Normalisation is not invariance.** `d_min` divides by unit length and tiles its templates
   to unit length, and was described as "length-invariant by construction" — yet length alone
   explains **28.7 %** of its variance, because it is a minimum over ~200 templates and a
   minimum-of-many falls as the string shortens. A statistic can be invariant in its *units*
   and not in its *distribution*. **Only a measurement settles which.** This is §4.5 again,
   in a form that survived a whole finding because the normalisation looked like a proof.
   (H-NEW-2730.)
9. **A p-value is a property of a null, not of a claim.** Pillar 1's `p = 3.17 × 10⁻¹²` was
   the largest number in the repository and it priced a hypergeometric drawing 29 surahs
   uniformly from 114. The claim it described is **real and survived**; the number was still
   void, and this project's own `h-new-46` had already shown why. **When quoting a p-value,
   quote the null it came from in the same breath.** (H-NEW-2760.)
10. **Rank the nuisance channels on the data before locking one as primary.** H-NEW-2760
    pre-registered opening-window size as its primary nuisance and deferred whole-surah length
    as "correlated but not identical". On the data the deferred channel was more than twice as
    strong (ρ = +0.4583 against +0.1678), and the registered rate ratio of 2.580 falls to 1.694
    against it. The pre-registration is what made this visible and it is why both numbers are
    published — but a cheap descriptive measurement of each candidate channel, *before*
    locking, would have ranked them correctly.

---

## 5. What would actually settle the open questions

Naming the instruments that do not exist yet is more useful than another test with the ones
that do.

1. **A matched Classical-Arabic dependency treebank.** The morphology line (§1.3) is limited
   by having a treebank for this corpus and none for any comparison corpus. Every valency and
   syntax result is therefore uncontrolled in exactly the way §4.1 warns about. Without a
   matched treebank, "muṭāwaʿa reduces object realization" cannot be shown to be a property of
   *this* text rather than of Arabic. This is the single highest-value missing instrument.
2. **A genuinely composed control corpus, not a partitioned one.** Every genre control run so
   far cuts a continuous stream into artificial units. What is needed is a corpus of texts
   that were *authored as bounded units of comparable size distribution* — a curated
   collection of short treatises, letters, or sermons — so that unit boundaries mean something
   on both sides of the comparison. Until then every "does not discriminate" verdict carries
   the §4.7 caveat and every "discriminates" verdict is suspect for the mirror reason.
3. **Form-blind human reannotation.** Several results depend on annotations produced by a
   parser whose features correlate with the very forms under test (H-NEW-2540's parser
   contamination is the confirmed case). A sample reannotated by readers who cannot see the
   morphological form would bound that contamination. Nothing computational substitutes for it.
4. **More than three matched genres.** Poetry, ḥadīth and adab prose are the only matched
   Arabic corpora on disk. Three genres cannot establish what Arabic in general does, and
   every percentile in §2 is a percentile within a very small reference class.
4a. **A *vocalised* comparison corpus, which is a separate and narrower gap.** Any test that
   reads syllable weight — scansion, prosody, metre, tajwīd — needs diacritics, and on disk
   only this corpus, the ḥadīth collections and **three** of the seven muʿallaqāt have them.
   `bukhari-noquran.txt`, `jahiz-hayawan.txt` and **all eight dīwāns** sit at a diacritic ratio
   of **0.000**. H-NEW-2730's prose control is therefore ḥadīth-only and al-Jāḥiẓ is untestable
   on that axis by any means. A vocalised adab-prose text and a vocalised dīwān would each
   open a class of questions that is currently closed.
5. **Qirāʾāt data and a rasm/imlāʾ divergence set**, neither of which is on disk, for the
   orthographic questions the project has never been able to touch.

---

## 6. How to read the rest of the repository

- **Correction notices are additive.** A file carrying a ⛔ notice still contains its original
  claim, verbatim. Read both.
- **Two documents are canonical for what fell**:
  `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` (the four pillar laws) and
  `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md` (the nine laws of the genre sweep).
  **The two evening audits are canonical for what changed after those were written**:
  `h-new-2760-muqattaat-book-reference-nuisance.md` (Pillar 1 survives; its p-value does not)
  and `h-new-2730-scansion-genre-control.md` (the scansion ordering, half withdrawn). Where
  this document and a finding disagree, the finding wins — it has the run directory.
- **`MASTER-FINDINGS-LEDGER.md` is not a safe index on its own.** It is 1.2 MB, has
  duplicated section numbers, and asserts corrected laws in dozens of places. Use it with the
  correction notices, never alone.
- **The pre-registrations are the project's real asset.** Where a finding and its
  pre-registration disagree, the pre-registration wins — that is what it is for, and
  H-NEW-2600 is the case where enforcing that rule retracted a published verdict.
- **The poem is art and it stays.** `poem/al-nuniyya.html` and its English mirror keep their
  verse untouched; only the scientific certifications beside individual lines have been
  withdrawn where the underlying result fell.

---

*Written 2026-08-07 by Waiel Al-Shujaa, on the day fourteen laws met their first controls,
and updated the same evening when the first of them survived one. A law that has never met a
control is a description. Most of this project's laws were descriptions. One is not: the
muqaṭṭaʿāt announce the Book at the top, at a rate ratio between 1.27 and 2.58 — smaller than
it was published as, and real. The negatives were real, the discipline was real, and the
discipline is what found the error. Bismillāhi al-Raḥmāni al-Raḥīm.*
