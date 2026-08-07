---
finding_id: H-NEW-2730
title: The scansion ordering does not survive a matched control — its prose leg is unit length, its poetry leg is real
author: Waiel Al-Shujaa
date: 2026-08-07
phase: C
parent: H-NEW-2690
method_parent: [H-NEW-2680, H-NEW-2720]
prereg: findings/phase-b-hypotheses/prereg-h-new-2730-scansion-genre-control.md
prereg_sha256: a5f742e15a8be6393b049ec2add61f237c36f165c884b54e0a17fb22c3578c25
run: findings/phase-b-hypotheses/runs/h-new-2730/20260807T040509Z/
seeds: 20260509 primary / 20260519 replication
status: >-
  ARTEFACT-OF-UNIT-LENGTH. The three-way ordering poetry < Qurʾān < prose does NOT
  survive. Its prose leg (H1b) is a unit-length artefact and is withdrawn; its poetry
  leg (H1a) survives every length control applied here. What H-NEW-2690 reported as an
  intermediate position is one real contrast plus one artefact.
verdict: >-
  Cut the Qurʾān's OWN verse stream to ḥadīth sentence lengths and its median d_min moves
  99.4 % of the way to ḥadīth's value (0.22222 → 0.23953 against Dārimī's native 0.23963),
  using no baseline text at all. Cut it to bayt lengths and it moves 7.5 % toward poetry.
  A matched partition of al-Dārimī lands at median d_min 0.22222 — the Qurʾān's own value
  to five decimals — and of al-Bukhārī at 0.21893, below it, with 199 of 200 offsets at or
  under the Qurʾān. In the single syllable-length bin where all three arms overlap, the
  Qurʾān and ḥadīth prose have identical medians (0.21739) while poetry sits at 0.14815.
  Only 49.2 % of Qurʾānic verses are more metrical than their own length-and-heaviness-
  matched random twin — a coin flip — against 88.3 % of poetry abyāt and 62-69 % of prose
  sentences.
---

# H-NEW-2730 — The genre control on H-NEW-2690's scansion ordering

**Pre-reg SHA-256 `a5f742e1…78c25`, runtime-verified. Nine frozen inputs SHA-verified. The
scanner is lifted verbatim from `scripts/h-new-2690.py` as two SHA-checked source regions;
the partition is lifted verbatim from `scripts/h-new-2680.py` as the same three fragments,
at the same digests, that H-NEW-2720 verified.**

---

## Headline

H-NEW-2690 was the one passing discriminating result of the 2026-08-07 session, and it named
its own missing control: *"designed-to-be-invariant is not the same as verified-invariant. A
matched-partition control on this statistic is REQUIRED."* This is that control.

**The ordering does not survive — but it does not fail symmetrically, and the asymmetry is
the finding.**

| registered arm | question | result | label |
|:--|:--|:--|:--|
| **D1** | Does prose stay above the Qurʾān under a matched partition? | Dārimī lands **at** the Qurʾān (0.22222 vs 0.22222); Bukhārī **below** it (0.21893), 199/200 offsets at or under | **ARTEFACT** |
| **D2** | Does poetry stay below the Qurʾān under a matched cut? | 0/200 draws reach the Qurʾān, p = 1×10⁻⁴ — but the locked gate below overrides | **UNINTERPRETABLE** |
| **D3** | Does the three-way **ordering** survive? | requires D1 ∧ D2 in both tuples | **ORDERING-DOES-NOT-SURVIVE** |
| **D4** | How much `d_min` variance is length alone? | pooled **R² = 0.287**; length predicts **5.1 %** of the Qurʾān–poetry gap and **206 %** of the Dārimī–Qurʾān gap | **PARTIALLY-LENGTH-DRIVEN** |
| **D5** | Does the ordering hold within matched length bins? | **1 of 10** bins has all three arms; in it Qurʾān = prose = **0.21739** exactly | **NON-OVERLAPPING-SUPPORT** |
| **D6** | Does it hold on excess over per-unit matched noise? | **reversed** — both prose corpora show *more* excess metricality than the Qurʾān | **EXCESS-FAILS** |
| **D7** | Does meter recovery survive partitioning? | `best_meter` collapses to 0.097 (chance 0.0625) | **CONTROL-FAILS** |
| **D8** | Where does the Qurʾān go when re-cut to another arm's unit lengths? | **99.4 %** of the way to prose; **7.5 %** toward poetry | **SELF-RECUT-CONFIRMS-LENGTH** |

**Overall: ARTEFACT-OF-UNIT-LENGTH.** Not profile-fragile, not rules-tuple-fragile. Every
cell reproduces at seed 20260519 and under both word-length profiles (§9).

**Stated plainly.** H-NEW-2690's H1b — *prose is less metrical than the Qurʾān* — is
withdrawn: it measures the fact that a ḥadīth sentence is three and a half times longer than
a Qurʾānic verse. H-NEW-2690's H1a — *the Qurʾān is less metrical than the muʿallaqāt* —
survives every length control applied here and is **not** withdrawn. What does not survive
is the thing that made the finding interesting: **"between poetry and prose" is not a
measured intermediate position.** It is one real contrast, on the poetry side, plus one
artefact, on the prose side.

---

## 1. The instrument reproduces H-NEW-2690 exactly — the control that had to pass first

Before any control value was computed, the lifted scanner was run on the parent's own arms.
**Five published values reproduce**, in both pausal tuples:

| quantity | H-NEW-2690 published | reproduced here |
|:--|--:|--:|
| Qurʾān median `d_min`, P_forceheavy (n) | 0.2222 (6211) | **0.22222** (6211) |
| Qurʾān median `d_min`, P_pausal (n) | 0.2188 (6209) | **0.21875** (6209) |
| poetry median `d_min` (prereg §4 benchmark) | 0.1429 | **0.14286** |
| Qurʾān matched-noise floor | 0.2394 | **0.23913** |
| poetry matched-noise floor | 0.2222 | **0.22222** |

**Nothing in this finding says any H-NEW-2690 computation is wrong.** The arithmetic is
exact. What is challenged is what the numbers mean.

Three further gates passed fail-fast before any arm ran:

- **`dmin_fast` identity gate.** The fast routine used for the bulk arms agrees with the
  lifted `metricality()` on `d_min` to 1×10⁻¹² **and** on the argmin meter on **1,500 of
  1,500** units drawn from all four corpora.
- **Tokeniser equivalence gate.** `normalise_words()` deletes every diacritic, so it cannot
  be used verbatim on a scansion test — it would delete the signal. The vocalisation-
  preserving tokeniser used instead is proved **token-for-token identical** to it after
  diacritic stripping, on every baseline corpus. The word stream cut here is provably the
  stream H-NEW-2680 and H-NEW-2720 cut.
- **Cyclic-partition equivalence gate.** The cyclic cut used for the undersized poetry stream
  returns **exactly** what `build_pseudo_corpus()` returns on any stream long enough to
  complete one pass; asserted at runtime on both prose corpora.

---

## 2. What could not be controlled, stated before the results

**Scansion requires vocalisation, and the corpora H-NEW-2720 used have none.**
`bukhari-noquran.txt`, `jahiz-hayawan.txt` and all eight `diwan-*.txt` files carry a
diacritic ratio of **0.000**. An exhaustive sweep of `data/` returns only the Qurʾān, the
ḥadīth collections, Ibn Kathīr's tafsīr (whose Arabic is ḥadīth quotation, and which quotes
the Qurʾān throughout) and three vocalised muʿallaqāt.

**al-Jāḥiẓ therefore cannot be tested on this statistic by any means.** The prose control is
ḥadīth-only, and two ḥadīth collections are not "Arabic prose in general". That is a real
narrowing and it is carried in §10.

**al-Bukhārī, however, is recoverable.** The ahmedbaset JSON edition of the same Ṣaḥīḥ is
vocalised at ratio 0.770, so the matched al-Bukhārī partition H-NEW-2720 could not have run
on this statistic **is** run here.

| arm | source | voc. | words | partition |
|:--|:--|--:|--:|:--|
| Qurʾān | `quran-full-tashkeel.json`, 6,236 verses | 0.918 | — | native |
| prose A | Sunan al-Dārimī, 3,406 ḥadīth — **the parent's own prose arm** | 0.866 | 167,564 | 200 offsets |
| prose B | Ṣaḥīḥ al-Bukhārī, 7,277 ḥadīth | 0.770 | 532,918 | 200 offsets |
| poetry | 3 vocalised muʿallaqāt, 240 abyāt | 0.72–0.84 | 2,302 | **2.8 % of requirement** |

Qurʾānic quotation was stripped from both prose streams by 7-gram match against the Qurʾān's
own word stream: **390 words (0.23 %)** from Dārimī and **1,470 (0.28 %)** from Bukhārī.
Contamination was negligible, and removing it runs *against* this finding's conclusion.

### 2.1 The nuisance parameter, measured before the directions were locked

| arm | median words/unit | median **syllables**/unit |
|:--|--:|--:|
| poetry (bayt) | 9.6 | **25** |
| **Qurʾān (verse)** | **10** | **28** |
| Bukhārī (sentence) | — | **55** |
| Dārimī (sentence) | 36 | **76** |

Word counts are whitespace tokens of the source text; the partition tokeniser (which drops
non-Arabic characters) gives a Dārimī sentence median of 29 words, the figure used in §3.

**The reported ordering is monotone in unit length.** A Dārimī sentence is **2.7×** the
Qurʾānic verse in syllables and a Bukhārī sentence **2.0×**. A three-way ordering is
ordinarily harder to fake than a
two-way extremity claim — that was H-NEW-2690's stated defence — but that argument fails
exactly when the nuisance parameter is itself monotone across the three arms. It is.

---

## 3. The result that decides it, and it uses no baseline text at all

**D8 — take the Qurʾān's own verse word stream, order preserved, and re-cut it into units
drawn from another arm's length profile.** No baseline text is scored; only the unit-length
profile is borrowed. This is the analogue of H-NEW-2720 §2.1c, which collapsed the
compression tail from R² = 0.9887 to 0.3388 by re-cutting the Qurʾān's own verses.

| re-cut of the Qurʾān's own stream | Qurʾān native | after re-cut (200 draws) | target arm's native | **distance moved** |
|:--|--:|--:|--:|--:|
| **to ḥadīth sentence lengths** (median 29 words) | 0.22222 | **0.23953** [0.23529, 0.24202] | Dārimī **0.23963** | **99.4 %** |
| **to bayt lengths** (median 9 words) | 0.22222 | **0.21624** [0.21053, 0.22222] | poetry **0.14286** | **7.5 %** |

Profile medians are in partition-tokeniser words (§2.1).

Under P_pausal: **92.9 %** and **8.1 %**.

**Cut the Qurʾān like ḥadīth and it becomes ḥadīth on this statistic — to within 0.0001.**
Cut it like poetry and it does not become poetry; it moves less than a tenth of the way.

This single arm answers the question the parent finding asked. The Qurʾān–prose gap is unit
length, essentially all of it. The Qurʾān–poetry gap is not.

**It is also the arm that escapes the "a partition is not a composed book" caveat entirely**
(§10.2), because there is no baseline partition in it.

---

## 4. D1 — the matched-partition control

Each prose stream cut into 6,236 units on the Qurʾān's verse word-length profile, at 200
seeded offsets, `d_min` scored on a seed-locked sub-sample of 500 units per offset.

| | native median | matched-partition mean | range over 200 offsets | Qurʾān | offsets **≤** Qurʾān |
|:--|--:|--:|--:|--:|--:|
| **al-Dārimī** | 0.23963 | **0.22222** | [0.21429, 0.23077] | 0.22222 | **155 / 200** |
| **al-Bukhārī** | 0.23529 | **0.21893** | [0.21053, 0.22727] | 0.22222 | **199 / 200** |

Because `d_min` is a ratio of small integers its medians are heavily quantised, so the count
of ties matters and is reported rather than absorbed:

| | offsets **below** Qurʾān | **exactly equal** | **above** |
|:--|--:|--:|--:|
| al-Dārimī | 43 | **112** | 45 |
| al-Bukhārī | **135** | 64 | **1** |

**A matched partition of al-Dārimī ties the Qurʾān exactly** — same median to five decimals,
with 112 of 200 offsets landing on the identical value. **A matched partition of al-Bukhārī
beats it**, with 199 of 200 offsets at or below.

The like-for-like comparison makes it sharper still. Bootstrapping the Qurʾān's own 6,211
values 200× at the same n = 500 gives a band of **[0.21429, 0.22997], mean 0.22207** —
against Dārimī's matched-partition band **[0.21429, 0.23077], mean 0.22222**. **The two
bands share their lower bound and their means differ in the fifth decimal.** The Qurʾān's own
sampling variability covers the matched prose partition.

Under P_pausal, Dārimī's per-corpus label softens to ATTENUATED (25/200 at or below) while
Bukhārī remains ARTEFACT (135/200). That tuple-dependence is real and is reported; the
overall D1 label is ARTEFACT in both tuples, in both seeds, and under both word profiles.

**The permutation arm of D1 is not load-bearing and should not be read as one.** With arm
sizes of 3,000 against 6,211 and a heavily quantised statistic, the permutation null is not
centred at zero — an observed difference of exactly 0.00000 returns p = 0.942. The
mis-calibration makes SURVIVES *harder*, i.e. it runs toward this finding's conclusion, which
is why the offset band and not the p-value is quoted as the evidence.

---

## 5. D2 and D7 — the poetry arm, and why its verdict is withheld

The poetry stream is **2.8 %** of the 82,375 words the partition consumes, so the cut cycles
the locked profile: 200 seeded draws, median 169 units each.

| | value |
|:--|--:|
| poetry native median `d_min` | 0.14286 |
| matched-cut mean over 200 draws | **0.15037** [0.09091, 0.17857] |
| Qurʾān | 0.22222 |
| draws reaching the Qurʾān | **0 / 200** |
| permutation, Qurʾān − poetry | +0.05556, **p = 1×10⁻⁴** |

Taken alone this is a clean pass. **It is not reported as one**, because the pre-registered
gate fails:

**D7 — the muʿallaqāt positive control, re-run on the partitioned data.** `best_meter()`
recovers the known meter of a partitioned poetry unit **9.7 % of the time** (n = 37,483)
against **77.1 %** on whole abyāt and **6.25 %** chance. By the locked rule (prereg §7, §11)
that makes **D2 UNINTERPRETABLE — neither passed nor failed.**

### 5.1 Why the control fails, reported as a disclosed MW-7 diagnostic

This changes no verdict and is descriptive only, but it would be dishonest to report a gate
failure without the mechanism.

`best_meter()` compares a unit against a **doubled hemistich of fixed length** and normalises
by `max(len)`. It is **not length-invariant**, so on units that are not bayt-length it is
being used outside its calibration. `d_min`'s argmin **is** length-invariant — the template
is tiled to L at every phase. Both were computed:

| meter-recovery instrument | on whole abyāt | on partitioned units |
|:--|--:|--:|
| `best_meter()` — length-sensitive | **0.771** | **0.097** |
| `d_min` argmin — length-invariant | 0.608 | **0.641** |

**Metre survives the partition; the instrument does not.** The length-invariant identifier
recovers ṭawīl/wāfir on 64.1 % of arbitrarily cut poetry fragments — slightly *better* than
on whole abyāt — while the length-sensitive one collapses to near chance.

So the honest reading of the poetry arm is: **the pre-registered gate failed, so D2 carries no
verdict; but the failure is diagnosably an artefact of the gate's own instrument, and the
poetry contrast is corroborated independently by D4 (5.1 %), D5 (bin 4) and D8 (7.5 %), none
of which uses `best_meter` or a partition.** The direction lock is honoured — D2 is recorded
as UNINTERPRETABLE in the run and in the verdict table — and the corroboration is reported
beside it rather than in place of it.

---

## 6. D4 and D5 — length-invariance, measured rather than asserted

### 6.1 The variance explained by length alone

Regressing `d_min` on `log L` (L = syllable-string length) across all four native arms,
n = 11,476:

| | R² | r |
|:--|--:|--:|
| **pooled** | **0.2875** | **+0.536** |
| within Qurʾān | 0.3039 | +0.551 |
| within al-Dārimī | 0.2746 | +0.524 |
| within al-Bukhārī | 0.2678 | +0.518 |
| within poetry | 0.0518 | −0.228 |

Under P_pausal: pooled **0.3048**. **Length alone explains 28.7 % of `d_min` variance, and
about 30 % within the Qurʾān, al-Dārimī and al-Bukhārī separately.** `d_min` rises with unit
length at r ≈ +0.52 in every arm that spans a length range.

**This is the pre-registered answer to "is `d_min` length-invariant in practice": no, but
only partially.** 0.287 falls below the locked NOT-LENGTH-INVARIANT bar of 0.50, so D4's own
label is **PARTIALLY-LENGTH-DRIVEN**, and it must be said plainly that **the overall ARTEFACT
verdict fired on D1 alone, not on the D4 ∧ D8 clause.** The pooled R² is not oversold here.

The decomposition is where the force is:

| gap | observed | predicted by length alone | share |
|:--|--:|--:|--:|
| Qurʾān − poetry | +0.07937 | +0.00408 | **5.1 %** |
| Dārimī − Qurʾān | +0.01740 | +0.03592 | **206 %** |
| Bukhārī − Qurʾān | +0.01307 | +0.02429 | **186 %** |

The fitted length model **over-predicts** the prose–Qurʾān gap twofold — the arms' length
difference is more than sufficient to produce the whole observed gap — and predicts almost
none of the Qurʾān–poetry gap. The two legs of the "ordering" have opposite explanations.

### 6.2 The arms barely share a length range

Binning all 11,476 native units into deciles of pooled syllable length, a bin is *usable*
when it holds ≥ 30 units from each of poetry, Qurʾān and prose. **One bin of ten qualifies.**

| bin | L | poetry | Qurʾān | prose | medians |
|:-:|:--|--:|--:|--:|:--|
| 3 | [17, 23) | 19 | 768 | 330 | — |
| **4** | **[23, 29)** | **220** | **716** | **269** | poetry **0.14815** · Qurʾān **0.21739** · prose **0.21739** |
| 5 | [29, 37) | 1 | 840 | 297 | — |
| 8–10 | [62, 1259) | 0 | 736 | 2,725 | — |

Poetry occupies essentially a single length bin — a bayt is a fixed metrical object — while
the Qurʾān spans 4 to 1,259 syllables and prose is concentrated at the long end.

**In the one bin where all three arms coexist, the Qurʾān and ḥadīth prose have identical
medians — 0.21739 and 0.21739 — and poetry sits far below at 0.14815.** At matched length the
Qurʾān–prose distinction vanishes completely and the Qurʾān–poetry distinction remains at
full size. That is the same asymmetry D8 found, on an arm that uses no partition and no
re-cutting whatsoever.

The locked label is **NON-OVERLAPPING-SUPPORT**: with one usable bin the arms are declared not
length-comparable, and the raw three-way median comparison is uninterpretable without a
control. That is a statement about H-NEW-2690's design, and it was pre-registered as an
outcome before the bins were computed.

---

## 7. D6 — the noise floors alone reproduce the ordering

For every unit, 2690's own `matched_noise()` generates one random syllable string of
**identical length and identical heavy-fraction**. The parent computed this control for the
Qurʾān and poetry arms and never used it as an ordering test; the prose floor was never
computed at all.

| arm | median `d_min` | **matched-noise floor** | median excess | mean excess | **units beating their own twin** |
|:--|--:|--:|--:|--:|--:|
| poetry | 0.14286 | **0.22222** | −0.08333 | −0.08754 | **88.3 %** |
| **Qurʾān** | 0.22222 | **0.23913** | **0.00000** | −0.01821 | **49.2 %** |
| al-Bukhārī | 0.23529 | **0.25992** | −0.02381 | −0.02366 | 62.4 % |
| al-Dārimī | 0.23963 | **0.26549** | −0.02542 | −0.02494 | 68.6 % |

Two things follow, and both are damaging.

**(a) Random strings reproduce the ordering.** The noise floors run
poetry 0.22222 < Qurʾān 0.23913 < Bukhārī 0.25992 < Dārimī 0.26549 — **the same three-way
ordering as the observed data**, generated by strings that contain no Arabic, no metre and no
text, matched only on length and syllable weight. Whatever else `d_min` measures, the ordering
it produces is reachable without any of the properties the ordering was taken to be about.

**(b) On excess, the Qurʾān is last, not intermediate.** Controlling length and weight
per-unit, both prose corpora show **more** excess metricality than the Qurʾān. The locked
direction (prose > Qurʾān) **reverses** in both tuples: Dārimī diff = −0.02542, Bukhārī
−0.02381. D6a (Qurʾān > poetry) passes at p = 1×10⁻⁴ in both tuples; **D6b fails, reversed,
in all four arms.**

**Only 49.2 % of Qurʾānic verses are closer to a classical metre than their own
length-and-heaviness-matched random twin.** That is a coin flip. Against 88.3 % of poetry
abyāt and 62–69 % of ḥadīth sentences.

This bears directly on a sentence in the parent finding: *"Qurʾān median d_min 0.2222 vs its
own phoneme-shuffled noise floor 0.2394 — metrical structure above noise."* That inference
compares the **medians of two distributions**; because the noise strings are matched *per
unit*, the correct comparison is **paired**, and the paired median excess is exactly
**0.0000** with a 49.2 % win rate. The mean excess is −0.018, so a small effect survives in
the tail — but "metrical structure above noise" overstates what the paired statistic shows,
and the corpora it was contrasted with have more of it, not less.

---

## 8. What falls and what survives

**Falls.**
- **H1b — "prose is less metrical than the Qurʾān" — withdrawn.** A matched partition of
  al-Dārimī ties the Qurʾān exactly and one of al-Bukhārī beats it; the Qurʾān's own verses
  re-cut to ḥadīth sentence lengths reach ḥadīth's value at 99.4 %; at matched syllable length
  the two medians are identical; and on per-unit noise-controlled excess the direction
  reverses. Four independent lines, two of which use no baseline text.
- **The three-way ordering, and with it "the Qurʾān sits BETWEEN poetry and prose".** There is
  no measured intermediate position. There is one contrast and one artefact.
- **"`d_min` is length-invariant by construction."** It is length-invariant in its *units* and
  not in its *distribution*: length alone explains 28.7 % of its variance and about 30 %
  within each long-range arm, because `d_min` is a minimum over ~200 tiled templates and the
  minimum-of-many falls as L falls.
- **The parent's length-invariance check.** Its three bins spanned 8 syllables (20/24/28) on
  240 poetry abyāt, inside poetry's single length bin; the arms it compares span 4 to 1,259.

**Survives.**
- **Every H-NEW-2690 computation.** Five published values reproduce exactly (§1).
- **H1a — the Qurʾān is less metrical than the muʿallaqāt.** Length explains 5.1 % of that
  gap; it survives the per-unit noise control at p = 1×10⁻⁴ in both tuples; it holds at full
  size in the one matched-length bin (0.21739 vs 0.14815); and re-cutting the Qurʾān to bayt
  lengths moves it only 7.5 % of the way. **This is a real, length-controlled contrast and it
  is not withdrawn.** It is a two-way claim against one genre, on 240 abyāt covering two of
  sixteen meters — not the discriminating three-way result the parent reported.
- **The positive control's substance.** The partition does not destroy metre: the
  length-invariant identifier recovers the known meter on 64.1 % of partitioned poetry
  fragments (§5.1). It is `best_meter()` that fails outside its calibration.
- **al-Bāqillānī's claim is untouched.** "Neither *nathr* nor *shiʿr*" was never a claim about
  medians of normalised edit distances. What is withdrawn is its stated empirical
  operationalisation on this axis, not the classical thesis.

---

## 9. Replication, sensitivity, and the two rules-tuple axes

| cell | pausal | profile | seed | D1 Dārimī | D1 Bukhārī | D2 | D7 |
|:--|:--|:--|--:|:--|:--|:--|:--|
| **PRIMARY** | P_forceheavy | W_2680 | 20260509 | ARTEFACT (155/200) | ARTEFACT (199/200) | UNINTERPRETABLE | 0.097 |
| TUPLE_SENS | P_pausal | W_2680 | 20260509 | ATTENUATED (25/200) | ARTEFACT (135/200) | UNINTERPRETABLE | 0.090 |
| PROFILE_SENS | P_forceheavy | **W_lex** | 20260509 | ARTEFACT (53/60) | ARTEFACT (**60/60**) | UNINTERPRETABLE | 0.101 |
| REPLICATION | P_forceheavy | W_2680 | **20260519** | ARTEFACT (49/60) | ARTEFACT (58/60) | UNINTERPRETABLE | 0.092 |
| REPLICATION | P_pausal | W_2680 | **20260519** | ATTENUATED (7/60) | ARTEFACT (42/60) | UNINTERPRETABLE | 0.087 |

**Overall D1 = ARTEFACT in all five cells; D2 = UNINTERPRETABLE in all five; D7 fails in all
five.** Neither `profile_fragile` nor `rules_tuple_fragile` is triggered.

**The word-length profile axis mattered and was declared in advance.** H-NEW-2680 and
H-NEW-2720 take `QVERSE_WLEN` from `quran-no-tashkeel.json` (**82,375** words); H-NEW-2690
scanned `quran-full-tashkeel.json` (**77,429**). The 4,946-word difference is real — the
no-tashkeel file writes waqf marks as separate tokens, so Q2:2 is 9 tokens there and 7 here.
W_2680 is primary because the instruction was to reuse the parent method verbatim; W_lex is
the linguistically correct one. **Both give the same verdict**, and under W_lex the result is
stronger (Bukhārī 60/60).

The one genuinely tuple-dependent cell is **Dārimī under P_pausal**, which softens from
ARTEFACT to ATTENUATED. Reported, not smoothed. Bukhārī is ARTEFACT in every cell, and D8, D5
and D6 reach the same conclusion in both tuples without a partition at all.

---

## 10. Honest limits — read these before citing anything above

1. **al-Jāḥiẓ is untestable on this statistic.** There is no vocalised adab prose on disk.
   The prose control is **ḥadīth-only**: two collections, one genre. This is narrower than the
   control H-NEW-2720 ran on other laws, and nothing here establishes what non-ḥadīth Arabic
   prose does under scansion.
2. **A partition is not a composed book, and for this statistic the caveat cuts against the
   conclusion.** `d_min` is **contiguity-sensitive**: arbitrary cuts of a continuous stream
   preserve local continuity and destroy no boundary `d_min` reads, so they make the law
   *easier* for a baseline. By `STATE-OF-THE-PROJECT-2026-08-07.md` §4.7 that makes **D1's
   failure weaker evidence than the 199/200 count alone suggests.** This is stated as a limit,
   not used as an escape hatch — and it is the reason the finding leads with **D8, D5 and
   D6**, none of which scores a baseline partition. The conclusion does not rest on D1.
3. **The poetry arm is scaled, not matched** (2.8 % of requirement), its 200 draws re-cut the
   same 2,302 words and are far from independent, and **its verdict is formally withheld**
   under the locked D7 gate.
4. **Two of sixteen meters have vocalised ground truth.** Inherited whole from H-NEW-2690: the
   scanner is unvalidated on the other fourteen.
5. **The prose corpora are less completely vocalised** than the Qurʾān (0.866 and 0.770 vs
   0.918). Incomplete vocalisation inflates `d_min`, biasing the prose arms *upward* — i.e.
   **toward H1b passing**. The bias runs against this finding's conclusion, which is the
   conservative direction.
6. **`dmin_fast` is a rewrite.** Its identity gate is exact on 1,500 units across four corpora
   but is not a proof.
7. **D4's own label is PARTIALLY-LENGTH-DRIVEN, not NOT-LENGTH-INVARIANT.** The pooled
   R² = 0.287 is below the locked 0.50 bar. The overall ARTEFACT verdict fired on D1, and the
   D4 ∧ D8 route to the same verdict did **not** fire. Anyone quoting "d_min is not
   length-invariant" should quote 0.287 and the decomposition, not the label.
8. **D8 borrows its unit-length profiles from the baselines** (Dārimī sentences, muʿallaqāt
   abyāt), though no baseline text is scored. It is baseline-free in the sense that matters
   for §10.2, not in every sense.
9. **D5 rests on a single usable bin.** One bin is enough to show the arms are not
   length-comparable — which is its pre-registered purpose — but it is not a length-stratified
   replication, and its Qurʾān = prose equality is one number on 716 and 269 units.
10. **The D1 permutation p-values are mis-calibrated** by unequal arm sizes and a quantised
    statistic (§4), conservatively against SURVIVES. The offset band is the evidence.
11. **H1a's survival is bounded by what it was tested against.** Nothing here shows the
    Qurʾān's position is unusual among *elevated or religious* Arabic prose, or among Arabic
    poetry beyond three muʿallaqāt in two meters.

---

## 11. Garden of forking paths

- **Every direction, threshold and verdict rule was locked at SHA `a5f742e1…` before any
  partitioned, stratified, self-recut or noise-controlled value existed.** The pre-registration
  states the expected outcome explicitly — *"I expect H-NEW-2690's ordering to fall, and I am
  running this test in order to kill it"* — and §1.1's direction lock is justified by
  unit-length facts measured before locking and recorded in prereg §9.
- **Known at lock time**, and recorded there: corpus vocalisation ratios and word counts, the
  three arms' unit word-length profiles, the Qurʾān's verse syllable-length distribution, the
  three H-NEW-2680 fragment SHAs, and a speed calibration of `dmin_fast` against
  `metricality()` on 1,000 Qurʾānic units. **No arm median, no baseline value and no partition
  existed before the lock.**
- **The result went the way the pre-registration predicted on the prose leg and against it on
  the poetry leg.** D2's locked prediction was that partitioned poetry stays below the Qurʾān;
  it does (0/200 draws), and the arm's verdict is nonetheless withheld because the locked D7
  gate failed. Enforcing a gate that suppresses a passing arm is the pre-registration doing its
  job.
- **Two disclosed additions made after the smoke run, neither of which changes a verdict:**
  the `d_min`-argmin meter-recovery diagnostic in §5.1 (MW-7, explains a gate failure), and
  the distributional reporting of D6's excess — mean and win-rate beside the median. Both are
  descriptive, carry no new p-value and add no cell.
- **One aggregation choice goes beyond the locked text.** Prereg §7 specifies only that D1's
  overall label is SURVIVES iff both prose corpora survive; the runner additionally labels the
  overall ARTEFACT when *either* corpus is ARTEFACT. That choice favours this finding's
  expectation, so **the per-corpus labels are reported as the primary object** in §4 and §9
  and either aggregation can be applied by a reader. Under the stricter reading — overall
  ARTEFACT only if *both* corpora are ARTEFACT — PRIMARY, PROFILE_SENS and
  REPLICATION_forceheavy still return ARTEFACT, and the two P_pausal cells return ATTENUATED.
  **The overall verdict is unchanged in the primary cell under either rule.**
- **The verdict logic was diffed against prereg §7 clause by clause before the run**, per
  `STATE-OF-THE-PROJECT-2026-08-07.md` §4.4.
- **Run directories are never deleted.** The calibration smoke run is retained beside the
  primary run.

---

## 12. What should change in the project record

Per project convention these are flagged, not applied — a correction to another finding's file
is not mine to make.

- **`h-new-2690-quantitative-scansion.md` needs a correction notice.** Its `status` reads
  *"H1a and H1b PASS in both rules-tuples (poetry < Qurʾān < prose)"*. **H1b does not survive a
  matched control and should be withdrawn**; H1a stands and should be restated as a two-way
  claim against pre-Islamic poetry. Its §2 sentence *"This operationalizes al-Bāqillānī's
  claim that the text is neither nathr nor shiʿr — as a measured intermediate position"*
  should be withdrawn: there is no measured intermediate position. Its §4 limit 1 — which
  required exactly this control and predicted it might not survive — was correct, and should
  be marked as discharged.
- **The "metrical structure above noise" reading in its §2** should carry the paired statistic:
  median excess 0.0000, 49.2 % of verses beating their own matched twin, against 88.3 % of
  poetry and 62–69 % of ḥadīth prose.
- **`STATE-OF-THE-PROJECT-2026-08-07.md` §1 should gain a fifth surviving item and lose a
  claim.** The Qurʾān–poetry metricality contrast is a genuine, length-controlled negative
  result about the *prose* comparison plus a real contrast against poetry; the discriminating
  three-way ordering it was carried as is withdrawn.
- **`h-new-48-poetic-meter.md`** — H-NEW-2690 superseded its scope; nothing here changes that,
  but the "between" predicate it and H-NEW-2690 share is now measured and does not hold.
- **A methodological lesson for §4 of the state document.** *A statistic that is
  length-invariant in its units may not be length-invariant in its distribution.* `d_min`
  normalises by L and tiles to L, yet is a minimum over ~200 templates, and a minimum-of-many
  falls as L falls. **Normalisation is not invariance; only a measurement is.**

---

## 13. Files

- Pre-registration: `findings/phase-b-hypotheses/prereg-h-new-2730-scansion-genre-control.md`
  (SHA-256 `a5f742e15a8be6393b049ec2add61f237c36f165c884b54e0a17fb22c3578c25`)
- Script: `findings/phase-b-hypotheses/scripts/h-new-2730.py` — pre-reg SHA-gated; lifts the
  2690 scanner as two SHA-checked source regions and the 2680 partition as three SHA-checked
  fragments; three fail-fast equivalence gates
- JSON: `findings/phase-b-hypotheses/csv/h-new-2730.json`
- Runs (immutable, never deleted): `findings/phase-b-hypotheses/runs/h-new-2730/20260807T040509Z/`
  (primary, 1,074 s) and `runs/h-new-2730-SMOKE/20260807T034657Z/` (calibration), each with a
  `manifest.json` recording every frozen input SHA in repo-relative form

---

*Run 2026-08-07 by Waiel Al-Shujaa. A statistic that normalises by a nuisance parameter has
not thereby controlled for it. Bismillāhi al-Raḥmāni al-Raḥīm.*
