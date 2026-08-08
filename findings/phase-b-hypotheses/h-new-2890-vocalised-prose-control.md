---
id: H-NEW-2890
title: "The vocalised-prose negative control — acquired from the repository's own shelves, and run"
phase: B
date: 2026-08-07
author: Waiel Al-Shujaa
frontier_item: F-16
parents: [H-NEW-2880, H-NEW-2870]
verdict: "CONTROL PASSES — vocalised Classical Arabic prose gains Δ = +0.030 to +0.033 at its own composed boundaries against this corpus's +0.1869. Cite with §7.1: under a worst-case-over-both-tuples reading the verdict would be PARTIAL, by a margin of 0.00010. Three of twelve D-P3 arms clear α in the damaging direction (§6.1)."
prereg: prereg-h-new-2890-prose-control.md
prereg_sha256: 8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec
run: runs/h-new-2890/20260807T145937Z/
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 36
alpha_bonferroni: 0.00138889
source_manifest: data/literature/hadith/VOCALISED-HADITH-SOURCE.md
---

# H-NEW-2890 — the prose control that both parents said could not be run

> ### ⚠ MAGNITUDE CORRECTED 2026-08-08 — the cross-corpus headline is inflated by unit length
>
> **H-NEW-2930** applied `findings/UNIT-DRIFT-DEFECT.md`'s screen to this family and it **TRIPS.**
> Δ tracks mean unit length across the nine prose books at **ρ = −0.65** (shorter units, larger Δ),
> and the Qurʾān's 13.21-word mean verse is **3.7× shorter than the shortest prose book**.
> Extrapolating the nine-book trend to that unit length predicts Δ = 0.05154 against the observed
> 0.18690 — **a residual of 3.63×, not the 5.3× reported here.**
>
> **Do not quote "5.3× the prose mean."** The defensible figure is ~3.6× after the unit-length
> trend, and that figure is itself an extrapolation 0.86 prose-ranges beyond the data.
>
> **Unaffected:** H-NEW-2880's within-corpus null, which permutes this corpus against itself with
> class count, sizes and concentration exactly fixed — no cross-corpus unit length enters it.
> z = +15.03 stands.

> ### Publication record — this finding was published incomplete and was completed afterwards
>
> **Commit `cf34b5b73` published this file while its run was still executing.** At that moment
> §6.1 and §7 were unfilled placeholders, there was no `run:` frontmatter field, and no run
> directory existed. It was then described to the project owner as a completed, publishable
> result. Both were errors.
>
> **They are now corrected. §6.1 and §7 are filled from
> `runs/h-new-2890/20260807T145937Z/result.json` and from nothing else** — not from the partial
> arms visible at commit time, and not from the 200-draw smoke run whose figures were briefly
> quoted into H-NEW-2880 §5.2 and have since been replaced with the measured values.
>
> **The cause, recorded because it generalises:** a partial finding was written to its final
> path intending to be completed later, and any lane's `git add -A` can capture such a file at
> any instant — the hazard `UNIT-DRIFT-DEFECT.md` §7 already documents for run directories.
> **The rule that follows: never write a partial finding to its final path. Draft outside the
> findings tree, or write the file only once the run directory exists.**
>
> Nothing in the finding's substance changed between the incomplete commit and this completion:
> Arm A, Arm B, D-P1 and the collapse decomposition were final at commit time and are unaltered.
> What was genuinely missing — D-P3 and the verdict — is now present, **and D-P3 returns three
> failures in twelve arms, which is reported in §6.1 rather than smoothed over.**

**One-line summary.** H-NEW-2870 and H-NEW-2880 both reported the vocalised-prose negative
control as **NOT COMPUTABLE**. **Both were wrong, and the error was mine as well as theirs.** A
repository-wide ḥarakāt census found 50,884 fully vocalised ḥadīth already committed, at
ḥarakāt densities of 0.7702–0.8829 against this corpus's own 0.7801. The control was then run
on H-NEW-2880's instrument, unmodified. **Vocalised Classical Arabic prose gains Δ = +0.030 to
+0.033 at its own composed boundaries against this corpus's +0.1869 — about one sixth — and its
excess over its own exactly-matched null is z = +1.26 to +3.16 against this corpus's +15.03.**

**Two things must travel with that.** Prose's excess over its own null is small but **not
uniformly absent: three of twelve D-P3 arms clear α**, all of them Ṣaḥīḥ Muslim under tuple P1
(§6.1). And the verdict's margin is thin under one alternative reading of the locked threshold
(§7.1). Neither changes the Δ comparison, which is what the verdict gates on.

---

## 1. RESULT 1 — the acquisition, and a defect in my own finding

**No download was required.** The corpus has been in `data/literature/hadith/ahmedbaset-json/`
since 2026-04-28.

H-NEW-2880 §5.2 wrote: *"A census of all 36 baseline corpora on disk found no vocalised prose at
all."* The sentence is true and the inference drawn from it was not. **The census enumerated
`data/baseline-corpora/` only.** Everything measured in that section stands — those files really
do carry zero ḥarakāt — but the conclusion "the delta is not computable" should have read "not
computable *from the baseline corpora*".

**And the narrow census is not the worst of it.** The H-NEW-2900 sweep established that
**H-NEW-2730 — the finding H-NEW-2870's own frontmatter names as `method_parent_2` — had
already run "an exhaustive sweep of `data/`", found this corpus, and measured Ṣaḥīḥ al-Bukhārī
at diacritic ratio 0.770 and Sunan al-Dārimī at 0.866**, using both as its prose control. The
independent measurements here are 0.7702 and 0.8659: **agreement to three decimals, which is
the proof that nothing on disk changed and only the claim did.** `STATE-OF-THE-PROJECT` §5.4a
says the same thing in the document every pre-flight mandates.

> **The transferable lesson, and it is cheap: an absence claim is only as wide as the search
> that produced it. State the search, not just the absence — and grep your cited parents before
> asserting one.** Generalised, with the repository-wide inventory, in
> `findings/ABSENCE-CLAIMS.md`.

A correction notice has been added to H-NEW-2880 §5.2. Source, provenance, licence position and
SHA-256 for every file: `data/literature/hadith/VOCALISED-HADITH-SOURCE.md`.

**Licence.** The upstream snapshot on disk carries **no licence file**, and none is asserted
here. The underlying works are classical and long in the public domain; the *compilation* is
third-party. It is treated as research-use-only and is not redistributed.

---

## 2. RESULT 2 — the vocalisation screen. Threshold inherited, and it selects nothing.

The admissibility threshold — **unit-final vocalisation ≥ 0.90** — is taken **verbatim** from
H-NEW-2870 §6.4, where it was pre-declared to select three muʿallaqāt from seven. It is
inherited rather than set here, which matters because a threshold of 0.95 would have excluded
al-Bukhārī. **All nine books clear it, so the threshold performs no selection**, and all nine
are reported.

| text | units | chapters | ḥarakāt/char | **unit-final vocalised** | mean unit length | Qurʾān 3-gram | 5-gram |
|:--|--:|--:|--:|--:|--:|--:|--:|
| **al-Bukhārī** | 7,277 | 97 | **0.7702** | **0.9426** | 73.2 | 22.5 % | 4.0 % |
| **Muslim** | 7,459 | 57 | 0.7965 | 0.9405 | 64.6 | 17.8 % | 3.1 % |
| Abū Dāwūd | 5,276 | 43 | 0.7962 | 0.9505 | 63.1 | 17.0 % | 3.1 % |
| al-Tirmidhī | 4,053 | 49 | 0.7954 | **0.9887** | 91.1 | 24.6 % | 6.2 % |
| al-Nasāʾī | 5,768 | 52 | 0.7883 | 0.9511 | 59.0 | 19.1 % | 2.1 % |
| Ibn Mājah | 4,345 | 38 | 0.7911 | 0.9484 | 58.5 | 16.3 % | 2.0 % |
| Mālik | 1,860 | 61 | 0.8201 | 0.9457 | 63.0 | 17.7 % | 2.1 % |
| Aḥmad (partial) | 1,374 | 8 | 0.8829 | 0.9512 | 73.6 | 19.1 % | 2.9 % |
| al-Dārimī | 3,406 | 24 | 0.8659 | 0.9445 | 49.2 | 16.0 % | 3.1 % |
| ***Qurʾān*** | *6,236* | *114* | ***0.7801*** | ***0.9843*** | *12.4* | — | — |

**al-Bukhārī's ḥarakāt density is essentially this corpus's own.** Admissible: **9 / 9**.

**Primary text: al-Bukhārī; replication: Muslim** — inherited from H-NEW-2870 §3/§6.5 and
H-NEW-2880 §5.2, where al-Bukhārī was already the declared negative control, so the text under
test was fixed by the parents rather than chosen on anything measured here.

**Qurʾānic quotation is stripped three ways and the conclusion is required under all three:**
**S5** (drop reports sharing a Qurʾānic 5-gram — primary), **S3** (trigram, the repository's own
`strip_quran_quotes.py` convention), **S0** (no stripping — retained deliberately because it is
the setting *least* favourable to H-NEW-2880: it leaves Qurʾānic material inside the control).

---

## 3. RESULT 3 — the class-collapse magnitude for prose, before any delta

| al-Bukhārī [S5] | classes K | K_eff | chance floor Σpᵢ² | A |
|:--|--:|--:|--:|--:|
| **C** citation | **785** | 159.70 | 0.02752 | 0.0715 |
| **P1** pausal minimal | **327** | 57.57 | 0.06241 | 0.1012 |
| P2 pausal full | 325 | 50.92 | 0.07949 | 0.1156 |

> **Collapse C → P1: 2.401×. The chance floor rises 0.0275 → 0.0624, so the collapse alone buys
> +0.0349 of adjacent-unit agreement for free.**
>
> **The observed prose gain is +0.0297 — LESS than the +0.0349 the arithmetic already
> guarantees.** The compositional remainder is **−0.0052**: negative.

**That is the sharpest number in this finding.** For comparison, the same decomposition on the
Qurʾān: collapse 3.422×, free gain +0.0619, observed Δ +0.1869, **compositional remainder
+0.1250**. In vocalised prose, pausal reduction buys *nothing beyond the arithmetic*. In this
corpus it buys **+0.125 on top of it**.

Muslim behaves the same way: K 838 → 347 (2.415×), free gain +0.0351, observed Δ +0.0325.

---

## 4. RESULT 4 — Arm B, composed boundaries. PRIMARY.

Unit = one ḥadīth (where the compiler chose to stop, and where a reciter performs *waqf*);
block = one chapter; adjacent within-chapter pairs. **Locked comparison target, fixed in the
pre-registration before any prose number existed: this corpus's own Δ(P1) = +0.1869.**

| text | setting | readable pairs | A(C) | A(P1) | **Δ(P1)** | Δ(P2) | Δ(P1) as share of +0.1869 |
|:--|:--|--:|--:|--:|--:|--:|--:|
| al-Bukhārī | **S5** | 6,306 | 0.0715 | 0.1012 | **+0.0297** | +0.0441 | **15.9 %** |
| al-Bukhārī | S3 | 5,063 | 0.0733 | 0.1051 | +0.0318 | +0.0460 | 17.0 % |
| al-Bukhārī | S0 | 6,579 | 0.0719 | 0.1035 | +0.0316 | +0.0468 | 16.9 % |
| Muslim | **S5** | 6,833 | 0.1109 | 0.1434 | **+0.0325** | +0.0454 | **17.4 %** |
| Muslim | S3 | 5,805 | 0.1082 | 0.1406 | +0.0324 | +0.0451 | 17.3 % |
| Muslim | S0 | 7,054 | 0.1100 | 0.1425 | +0.0325 | +0.0452 | 17.4 % |
| ***Qurʾān*** | — | *6,122* | *0.3484* | *0.5353* | ***+0.1869*** | *+0.1880* | *100 %* |

**The locked thresholds were: ≥ +0.09343 (half) = "prose gains comparably, H-NEW-2880 damaged";
≥ +0.04672 (quarter) = partial damage. The worst case over all six settings is +0.0325 —
below both.** The result is stable across the stripping rule to within 0.003, including under
S0, where no Qurʾānic material is removed at all.

Note also the *levels*, not just the deltas: prose barely rhymes in either convention
(A(P1) = 0.10–0.14) where this corpus reaches 0.5353.

---

## 5. RESULT 5 — Arm A, length-matched cuts

Prose units are **5.9×** longer than verses, so Arm B cannot hold unit length fixed. Arm A does
— the parent's own construction, cutting the prose word stream to this corpus's per-surah
verse-length profile, 200 cuts — but arbitrary cuts destroy composed boundaries, so **the locked
comparison target here is this corpus's own pseudo-fāṣila re-cut Δ = +0.0284, not its true Δ.**
Arbitrary cuts against arbitrary cuts.

| text | setting | Δ(P1) mean | sd | max | vs the Qurʾān's own re-cut +0.0284 |
|:--|:--|--:|--:|--:|:--|
| al-Bukhārī | S5 | **+0.0120** | 0.0014 | +0.0168 | below |
| al-Bukhārī | S3 | +0.0116 | 0.0015 | +0.0155 | below |
| al-Bukhārī | S0 | +0.0120 | 0.0014 | +0.0155 | below |
| Muslim | S5 | +0.0128 | 0.0015 | +0.0176 | below |
| Muslim | S3 | +0.0128 | 0.0016 | +0.0185 | below |
| Muslim | S0 | +0.0128 | 0.0014 | +0.0168 | below |

**Prose is below this corpus's own re-cut baseline in all six settings, and its maximum over
200 cuts never reaches it.** Even at arbitrary cut points, Qurʾānic Arabic gains about
2.3× what ḥadīth Arabic gains — so the +0.0284 re-cut figure that H-NEW-2870/2880 treated as
"what Arabic word-final morphology gives you anywhere" is itself partly a property of this
corpus's vocabulary, not of Arabic at large.

---

## 6. RESULT 6 — the registered tests

α_bon = 0.00138889, k = 36, one-sided in the locked direction, replicated at seed 20260519.

**D-P1 — is this corpus's per-pair gain larger than prose's?** 10,000-permutation label
exchange, the same machinery the parents used for their poetry control.

| text | setting | tuple | Δ_Qurʾān − Δ_prose | p | replication | |
|:--|:--|:--|--:|--:|--:|:--|
| al-Bukhārī | S5 | P1 | **+0.1572** | **0.0001** | 0.0001 | PASS |
| al-Bukhārī | S5 | P2 | +0.1439 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S3 | P1 | +0.1551 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S3 | P2 | +0.1420 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S0 | P1 | +0.1553 | 0.0001 | 0.0001 | PASS |
| al-Bukhārī | S0 | P2 | +0.1412 | 0.0001 | 0.0001 | PASS |
| Muslim | S5 | P1 | +0.1544 | 0.0001 | 0.0001 | PASS |
| Muslim | S5 | P2 | +0.1426 | 0.0001 | 0.0001 | PASS |
| Muslim | S3 | P1 | +0.1545 | 0.0001 | 0.0001 | PASS |
| Muslim | S3 | P2 | +0.1429 | 0.0001 | 0.0001 | PASS |
| Muslim | S0 | P1 | +0.1544 | 0.0001 | 0.0001 | PASS |
| Muslim | S0 | P2 | +0.1428 | 0.0001 | 0.0001 | PASS |

**12 / 12 pass at α.** **D-P2** — prose's matched-cut Δ against this corpus's re-cut Δ — is
below target in **12 / 12** arms (§5).

### 6.1 D-P3 — prose against ITS OWN exactly-matched null

The decisive form of the question. H-NEW-2880's exact zero-variance-floor null is applied to
prose's own partition: every draw carries prose's own class-size multiset, hence prose's own
chance floor, to the last bit. **Floor deviation is 0.0 × 10⁰ in all twelve arms**, so the
instrument's exactness gate holds on prose exactly as it did on this corpus.

| text | setting | tuple | E_obs | null E mean | sd | null max | #≥obs / 10,000 | **p** | **z** | replication | clears α? |
|:--|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|:--|
| al-Bukhārī | S5 | P1 | 0.0514 | 0.0467 | 0.0037 | 0.0563 | 1,028 | 0.10289 | **+1.26** | 0.10609 | no |
| al-Bukhārī | S5 | P2 | 0.0522 | 0.0445 | 0.0052 | 0.0586 | 1,250 | 0.12509 | +1.48 | 0.13059 | no |
| al-Bukhārī | S3 | P1 | 0.0534 | 0.0472 | 0.0040 | 0.0581 | 394 | 0.03950 | +1.55 | 0.04060 | no |
| al-Bukhārī | S3 | P2 | 0.0550 | 0.0455 | 0.0055 | 0.0625 | 568 | 0.05689 | +1.76 | 0.06049 | no |
| al-Bukhārī | S0 | P1 | 0.0530 | 0.0467 | 0.0043 | 0.0579 | 588 | 0.05889 | +1.44 | 0.06459 | no |
| al-Bukhārī | S0 | P2 | 0.0543 | 0.0452 | 0.0054 | 0.0601 | 611 | 0.06119 | +1.71 | 0.05779 | no |
| **Muslim** | **S5** | **P1** | 0.0945 | 0.0857 | 0.0030 | 0.0961 | **1** | **0.00020** | **+2.88** | 0.00030 | **YES** |
| Muslim | S5 | P2 | 0.0926 | 0.0852 | 0.0037 | 0.0969 | 179 | 0.01800 | +2.03 | 0.01680 | no |
| **Muslim** | **S3** | **P1** | 0.0912 | 0.0819 | 0.0029 | 0.0917 | **3** | **0.00040** | **+3.16** | 0.00030 | **YES** |
| Muslim | S3 | P2 | 0.0889 | 0.0808 | 0.0038 | 0.0920 | 114 | 0.01150 | +2.13 | 0.01130 | no |
| **Muslim** | **S0** | **P1** | 0.0932 | 0.0846 | 0.0030 | 0.0929 | **0** | **0.00010** | **+2.90** | 0.00020 | **YES** |
| Muslim | S0 | P2 | 0.0909 | 0.0837 | 0.0036 | 0.0949 | 190 | 0.01910 | +2.02 | 0.01830 | no |
| ***this corpus*** | — | *P1* | *0.3666* | *0.2266* | *0.0093* | *0.2635* | ***0*** | ***0.0001*** | ***+15.03*** | *0.0001* | *yes* |

> ### **THREE OF TWELVE D-P3 ARMS CLEAR α IN THE DAMAGING DIRECTION, AND THAT IS A REGISTERED
> ### INFERENCE FAILING.**
>
> All three are **Muslim under tuple P1**, at p = 0.00010–0.00040 and z = +2.88 to +3.16, and
> they replicate at the second seed. **Ṣaḥīḥ Muslim's pausal merges do carry a small but real
> excess over a regrouping of identical coarseness.** al-Bukhārī's six arms do not (p = 0.040
> to 0.125), and no P2 arm does.

**What mitigates it, and what does not.** The pre-registration anticipated this in writing —
§7 states that *"prose isnād chains repeat proper names locally, so some excess over a random
regrouping is expected in any Arabic prose"*, and that *"what would damage H-NEW-2880 is a
large prose **Δ**"*, with z declared **not** comparable across corpora of different size and
class structure. **An anticipated failure is still a failure**, and it is recorded here as one
rather than dissolved into the caveat that predicted it.

**What it does not do is touch the verdict**, which gates on Δ (§7). The magnitude gap is the
point: prose's standardised excess is **+2.9 to +3.2** where this corpus reaches **+15.03**,
and prose's excess sits on a Δ of +0.033 against +0.1869.

---

## 7. Verdict

The runner printed prereg §8's grid verbatim, then its computed decisions, then the verdict.
Run `runs/h-new-2890/20260807T145937Z/`.

| locked outcome | measured |
|:--|:--|
| no admissible text → CONTROL UNAVAILABLE | 9/9 books admissible |
| Δ_prose(Arm B) ≥ **+0.09343** under any setting → **2880 DAMAGED** | worst = +0.03249 — **not reached** |
| **+0.04672** ≤ Δ_prose < +0.09343 → PARTIAL, amend 2880 | worst = +0.03249 — **not reached** |
| Δ_prose < +0.04672 under all three **and** D-P1 passes | **+0.03249**, and D-P1 **12/12** at α |

> ## **VERDICT: CONTROL PASSES — H-NEW-2880's interpretation survives**
>
> Worst-case Δ_prose over both texts and all three stripping settings: **+0.03249**
> (Muslim, S5) — **17.4 %** of this corpus's +0.1869, and 30 % below the quarter-threshold
> that would have forced an amendment.

### 7.1 The disclosure that must travel with the verdict

**The locked threshold quantity is tuple P1** (prereg §7, *"Arm B, **P1**, rime R2, setting
S5"*), and §8 extends the worst case over the three stripping settings. A reader could instead
take the worst case over **both** tuples. The runner prints both and gates on P1 as registered:

| reading | worst case | vs quarter threshold +0.04672 | verdict it gives |
|:--|--:|:--|:--|
| **as locked — P1 only** | **+0.03249** (Muslim, S5) | 30 % below | **CONTROL PASSES** |
| worst over both tuples | **+0.04682** (al-Bukhārī, S0, P2) | **exceeds by 0.00010** | PARTIAL |

**Under the stricter reading the finding would return PARTIAL, by a margin of one ten-thousandth
of a unit of agreement — roughly six adjacent ḥadīth pairs out of 6,579.** The P1 gate was fixed
in the pre-registration before any prose number existed, and it is not being reinterpreted now;
but a verdict that turns on 0.00010 should not be reported as comfortable, and it is not.
**Anyone citing "CONTROL PASSES" should cite this row with it.**

Two further honest notes on the verdict: **three of twelve D-P3 arms fail** (§6.1), and the P2
tuple runs consistently ~0.014 above P1 in prose because tāʾ marbūṭa → *h* merges a large class
of feminine endings that ḥadīth prose uses heavily — which is why the tuple choice moves the
number at all.

---

## 8. Honest limits

1. **A ḥadīth is not a verse.** Arm B compares composed boundaries across two genres whose units
   differ 5.9× in length. That is the point of the comparison and it is not a matched design;
   Arm A holds length fixed and loses the composed boundaries. The two arms bracket, they do not
   jointly resolve.
2. **Prose is at least as formulaic at unit-final position as this corpus is** — the top-10
   unit-final word types cover 8.1 % of al-Bukhārī's reports and 12.9 % of Muslim's against
   7.6 % of this corpus's verses. That channel favours prose, so it does not explain prose's
   lower delta; measured before locking, and reported because it could have gone the other way.
3. **The honorific formulae are unvocalised in this edition** (`صلى الله عليه وسلم`), and
   unit-final sukūn is 5.7 % in al-Bukhārī against 1.6 % here. Those units have no recoverable
   citation form and are removed by the readability screen; the unrestricted arm is reported
   alongside and moves the delta by under 0.002.
4. **The licence position upstream is unstated** (§1), and Musnad Aḥmad is missing chapters
   8–30 in the source.
5. **Two genres, not all prose.** Ḥadīth is a specific register — isnād chains repeat proper
   names locally, which if anything should *raise* its rhyme agreement. Adab, khuṭab and
   epistolary prose remain untested because no vocalised edition of them is on disk.
6. **E's absolute level is not comparable across corpora.** The prose exact null takes its floor
   from all units and its agreement from readable pairs; the floor is constant across draws so
   the p-value is unaffected, but the E *level* should not be read against this corpus's E.
7. **The classical anchor, which this family recorded as missing, is on disk and is now cited.**
   H-NEW-2900 found the **Arabic** Itqān at
   `data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt`, carrying
   `النوع الثامن والعشرون: في معرفة الوقف والابتداء` in full at **PageV01P281**.
   **Anchor for the whole pausal family: al-Suyūṭī, *al-Itqān*, nawʿ 28, *fī maʿrifat al-waqf
   wa-l-ibtidāʾ*, V01 p. 281.** This is the *second* false absence corrected in this family, by
   the same mechanism as the first, and it is why `findings/ABSENCE-CLAIMS.md` exists.
8. **This control does not rescue what it does not touch.** H-NEW-2880 §10 stands: the
   deliberately wrong pausal tuple also clears its own exact null, so within the pausal family
   the discrimination remains quantitative rather than categorical.

---

## 9. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2890-prose-control.md`
  (SHA-256 `8d5a8af94a49b901e5109a658c22d7f4dce1edf70e9766a1b92b5646bb5a6aec`, runtime-verified)
- Runner: `findings/phase-b-hypotheses/scripts/h-new-2890.py`
- Source manifest: `data/literature/hadith/VOCALISED-HADITH-SOURCE.md`
- Parents: `h-new-2880-pausal-retest-matched-concentration.md` (instrument, SHA-pinned),
  `h-new-2870-pausal-rhyme.md`

*Bismillāhi al-Raḥmāni al-Raḥīm.*
