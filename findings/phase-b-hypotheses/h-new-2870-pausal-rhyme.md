---
id: H-NEW-2870
title: "Is the fāṣila defined at PAUSAL phonology rather than citation form? — the class-collapse magnitude, the delta, and a null that decides between them"
phase: B
date: 2026-08-07
author: Waiel Al-Shujaa
frontier_item: F-16
verdict: "NULL by the locked grid — but the arm that produced it is shown post-hoc to be ill-posed. Read §3 and §9 together before citing this."
prereg: prereg-h-new-2870-pausal-rhyme.md
prereg_sha256: 119753ad7862d66dfead2ff6de1032adee0a824cd7544cd8bc4d6688587508d4
run: runs/h-new-2870/20260807T131820Z/
seed: 20260509
seed_replication: 20260519
n_perm: 10000
n_recut: 2000
bonferroni_k: 16
alpha_bonferroni: 0.003125
---

# H-NEW-2870 — the fāṣila at pausal phonology

**One-line summary.** Pausal reduction collapses the corpus's verse-final rime inventory
**3.42-fold** (397 classes → 116), and that collapse buys **+0.062 of adjacent-verse rhyme
agreement for free**; the observed rise is **+0.187**, so **one third of the effect is
arithmetic and two thirds is not** — and the two-thirds remainder sits outside the entire
support of a null that holds the class count fixed.

**But the locked verdict grid returns NULL**, because one of the two matched-collapse nulls
does not clear the tightened α. A post-hoc diagnostic (§9) shows that **100 % of the null
draws that beat the observed value are more concentrated than the real pausal partition** —
that null is measuring a coarser merge than waqf performs. The pre-registration anticipated
this failure mode and instructed that such a null be reported as uninterpretable rather than
used to gate. Both readings are set out in §10 and neither is hidden.

---

## 1. Gates — reported before any test statistic (prereg §9)

### 1.1 Gate A — orthography. **PASS.**

`quran-full-tashkeel.json` encodes **77.7 % of its tanwīn** (6,643 of 8,554 marks) with three
codepoints whose Unicode *names* do not describe their function:

| codepoint | Unicode name | function here | verified |
|:--|:--|:--|--:|
| U+0657 (ٗ) | ARABIC INVERTED DAMMA | **tanwīn fatḥ** | 1195 match / **0** mismatch |
| U+065E (ٞ) | ARABIC FATHA WITH TWO DOTS | **tanwīn ḍamm** | 580 / **0** |
| U+0656 (ٖ) | ARABIC SUBSCRIPT ALEF | **tanwīn kasr** | 759 / **0** |

Verified against Tanzil Uthmani v1.1 under 1:1 verse alignment: **2,534 tanwīn-bearing words
checked, zero mismatches** across all six marks. Tanwīn is exactly what pausal reduction
removes, so misreading these would have voided the test silently.

> ### ⚠ Defect found in the reused machinery — H-NEW-2690 / H-NEW-2730 should be told
>
> `scripts/h-new-2690.py`'s `normalize()` places U+0656, U+0657 and U+065E in its `DROP`
> set. **It therefore deletes 6,643 tanwīn — 77.7 % of the corpus's tanwīn — before
> syllabification.** Every syllable-weight computation in H-NEW-2690 and H-NEW-2730 runs on
> a text with most of its nunation removed. This does not touch their muʿallaqāt control
> gate (the poems are not encoded this way), and the direction of the effect on `d_min` is
> not established here — but it is a real defect in a validated instrument and it should be
> assessed by whoever owns those findings. H-NEW-2870 does not inherit it.

### 1.2 Is the citation form actually recoverable? **Yes, and this was checked before running.**

If the mushaf spelled its verse-ends pausally, the whole contrast would be circular. It does
not: verse-final words carry their full *waṣl* iʿrāb.

| verse-final word ends in | n | share |
|:--|--:|--:|
| short vowel (full case ending written) | 3,836 | 61.5 % |
| tanwīn | 1,069 | 17.1 % |
| bare — long vowel / indeclinable, no case vowel exists in waṣl either | 1,233 | 19.8 % |
| sukūn — genuinely pausal or jussive | 98 | **1.6 %** |

Only the last row is ambiguous. Mid-verse words carry sukūn at 17.5 % by comparison, so the
verse-final position is *more* fully vocalised than the body of the text, not less.

### 1.3 Gate B — instrument. **6/6 PASS.**

The pausal classes reproduce H-NEW-2240's independently-derived, hand-validated results:
Q18 al-Kahf 110/110 open `-ā`; Q112 4/4 `-ad`; Q108 3/3 `-ar`; Q114 6/6 `-ās`; Q1 all seven
in {`-īm`, `-īn`}; Q55 modal `-ān` (63 of 78). Rime-region readability of the corpus:
**99.62 %**.

---

## 2. RESULT 1 — the class-collapse magnitude. **Reported before the delta, and it is large.**

This is the number the whole test turns on. If pausal reduction cuts the inventory hard, any
rise in agreement is arithmetic before it is anything else.

| | classes **K** | effective classes **K_eff** | chance floor Σpᵢ² |
|:--|--:|--:|--:|
| **C** — citation (waṣl) | **397** | **37.03** | 0.1068 |
| **P1** — pausal, minimal | **116** | **10.87** | 0.1687 |
| P2 — pausal, full (ة → h) | 115 | 10.82 | 0.1688 |
| P3 — pausal, strict (−an → ∅, deliberately wrong) | 213 | 16.89 | 0.1415 |

> **Collapse factor C → P1: 3.42× on K, 3.41× on K_eff.**
> **The chance-collision floor rises 0.1068 → 0.1687, so collapse alone buys +0.0619 of
> adjacent-verse agreement for free.**

The map C → P1 is a **clean coarsening: 0 citation types split, 0 verses affected.** (Under
the pre-registered rime R1 the corresponding figure is 1,059 verses, 17.0 % — see §7.)

---

## 3. RESULT 2 — the nulls that hold the class count fixed

### 3.1 N1-a — verse-count-profile-matched (as pre-registered, §6.2)

| tuple | observed A | null mean | null sd | null **max** | #≥obs / 10,000 | p | z | profile TV |
|:--|--:|--:|--:|--:|--:|--:|--:|--:|
| P1 | 0.5353 | 0.4252 | 0.0200 | **0.5742** | 57 | 0.0058 | +5.49 | 0.328 |
| P2 | 0.5364 | 0.4256 | 0.0201 | 0.5742 | 54 | 0.0055 | +5.52 | 0.326 |

Replication at seed 20260519: p = 0.0050 both. **Does not clear α = 0.003125.**

Note the null **maximum exceeds the observed value**. Some random regroupings of the citation
endings, matched on class count, produce *more* rhyme agreement than the real waqf rules do.
§9 establishes what those draws actually are.

### 3.2 N1-b — cardinality-matched, on the excess over the chance floor (REPAIR-1)

Statistic **E = A − Σpᵢ²**, which subtracts the collapse arithmetic analytically.

| tuple | observed E | null E mean | null sd | null max | #≥obs / 10,000 | p | z |
|:--|--:|--:|--:|--:|--:|--:|--:|
| P1 | **0.3666** | 0.2060 | 0.0365 | 0.2989 | **0** | **0.0001** | +4.40 |
| P2 | 0.3677 | 0.2059 | 0.0365 | 0.2990 | **0** | **0.0001** | +4.43 |

Replication: p = 0.0001 both. **Outside the entire null support.**

---

## 4. RESULT 3 — the delta, and its decomposition

| convention | A | Δ vs C |
|:--|--:|--:|
| **C** citation | **0.3484** (2,133 / 6,122 pairs) | — |
| **P1** pausal minimal | **0.5353** (3,277) | **+0.1869** |
| **P2** pausal full | 0.5364 (3,284) | +0.1880 |
| P3 pausal strict (wrong rule) | 0.4360 (2,669) | +0.0876 |

> ### The decomposition, which is the honest answer to "is it arithmetic?"
>
> | component | value | share of Δ |
> |:--|--:|--:|
> | **arithmetic** — the chance-collision gain from concentration (Σpᵢ² rise) | **+0.0619** | **33.1 %** |
> | **compositional** — the excess that concentration does not explain | **+0.1250** | **66.9 %** |
>
> **A third of the delta is the merge doing arithmetic. Two thirds is not, and that two
> thirds is unreachable by 10,000 random merges of matched coarseness.**

**P3 matters.** Dropping tanwīn fatḥ *without* its compensatory alif — not what waqf does in
any reading — more than halves the effect (+0.0876 against +0.1869) and inflates the class
count to 213. The single rule *−an → ā* carries roughly half the finding. The rules-tuple is
load-bearing, exactly as this project has repeatedly found.

---

## 5. RESULT 4 — pseudo-fāṣila re-cut. Within-corpus, no baseline text.

Re-cut each surah's own word stream into the same number of units whose lengths are a random
permutation of that surah's own verse lengths — identical text, vocabulary, orthography,
vocalisation and length profile; only the boundaries are not composed.

| tuple | observed Δ | re-cut mean | sd | re-cut max | #≥obs / 2,000 | p | z |
|:--|--:|--:|--:|--:|--:|--:|--:|
| P1 | **+0.1869** | +0.0284 | 0.0022 | +0.0354 | **0** | **0.0005** | **+70.7** |
| P2 | +0.1880 | +0.0297 | 0.0023 | +0.0379 | **0** | 0.0005 | +69.1 |

Replication identical. 12.84 % of re-cut boundaries coincidentally land on a true verse end.

**Arabic word-final morphology gives Δ ≈ +0.028 anywhere you cut. The fāṣila positions give
+0.187 — about 6.6× that, and 70 standard deviations above it.** The pausal gain is a
property of *where the boundaries are*, not of Arabic word endings in general. This control
uses no baseline text and is immune to every genre-matching objection raised on 2026-08-07.

---

## 6. RESULT 5 & 6 — the three control texts

### 6.1 Positive control — pre-Islamic poetry. **Behaves exactly as locked.**

Three muʿallaqāt with line-final vocalisation ≥ 0.9 (threshold fixed before any rhyme
statistic; the other four sit at 0.000–0.494 and are excluded by it). Primary arm is
readable-only pairs (REPAIR-2).

| poem | n | readable | A(C) | A(P1) | Δ |
|:--|--:|--:|--:|--:|--:|
| Imruʾ al-Qays | 78 | 0.949 | 0.4507 | 0.4930 | +0.0423 |
| Zuhayr | 62 | 1.000 | 0.5082 | 0.5082 | **0.0000** |
| ʿAmr b. Kulthūm | 103 | 1.000 | **0.9804** | **1.0000** | +0.0196 |
| **pooled (n = 234 pairs)** | | | **0.6966** | 0.7179 | **+0.0214** |
| *Qurʾān, for comparison* | | | *0.3484* | *0.5353* | *+0.1869* |

- **D4a passes decisively: poetry rhymes twice as well at citation form as the Qurʾān does**
  (0.6966 vs 0.3484). Poetry does not need pausal reduction to rhyme, because it is
  monorhymed by construction.
- **D4b: Δ_Qurʾān − Δ_poetry = +0.1655, p = 0.0001** (replication 0.0001).
- The ceiling caveat pre-registered in §6.4 is real for ʿAmr b. Kulthūm (A(C) = 0.98, nowhere
  to rise) but not for the pooled arm at 0.70, which had ample headroom and did not use it.

### 6.2 Negative control — prose. **The delta is BLOCKED, and this was declared in advance.**

`bukhari-noquran.txt` carries **0 harakāt** over 2,056,880 Arabic characters; `jahiz-hayawan.txt`
**0** over 1,422,374. **The citation form cannot be recovered from a text that never wrote its
final short vowels, so Δ is not computable for either prose baseline.** Automatic vocalisation
would substitute a model's output for data and was not used.

This is a **gap in the evidence, not a result**, and it is the single biggest limitation of
this finding. What *is* computable — a **level** comparison on the skeleton instrument
(H-NEW-2240's `classify`), on units length-matched to the Qurʾān's verse profile, 200 cuts:

| text | A(skeleton) | note |
|:--|--:|:--|
| poetry | 0.8917 | monorhyme |
| **Qurʾān** | **0.5521** | |
| al-Bukhārī | 0.0849 (max 0.0944 over 200 cuts) | Qurʾān at percentile **1.000** |
| al-Jāḥiẓ | 0.0754 (max 0.0869) | Qurʾān at percentile **1.000** |

The Qurʾān's verse-end agreement exceeds **400 of 400** matched prose cuts, by roughly 6×.
That is a level statement about rhyme density — essentially a cross-corpus restatement of
H-NEW-2240 — and it is **not** a control on the delta. It is not described as one.

---

## 7. The rules-tuple on the rime definition — and why the pre-registered one is defective

Under the rime as pre-registered (**R1**, §4.3), the last consonant of a tanwīn word is the
tanwīn *nūn*, so it is read as the rāwī:

| pair | R1 citation rime | do they rhyme? |
|:--|:--|:--|
| `ʿaẓīmun` / `mubīnun` | both **`uن`** → scored as rhyming | **no** — rāwī م vs ن |
| `ḥasanan` / `waladan` | both **`aن`** → scored as rhyming | **no** — rāwī ن vs د |

The defect is **asymmetric across the two conventions**: for a tanwīn word R1 reads the rime
of the *tanwīn* syllable under C and of the *stem-final* syllable under P — which is exactly
the like-for-like depth §4.3 was written to guarantee. **R2** (tanwīn-transparent) strips the
tanwīn to expose the stem and appends the tanwīn vowel as majrā. R2 ≡ R1 under all pausal
tuples. Both were run on everything (REPAIR-3).

| | R1 (pre-registered) | R2 (repair) |
|:--|--:|--:|
| K(C) | 157 | **397** |
| collapse factor C→P1 | 1.35× | **3.42×** |
| map violation (verses in split citation types) | **1,059 (17.0 %)** | **0 (0.0 %)** |
| A(C) | 0.4696 | **0.3484** |
| **Δ(P1)** | **+0.0657** | **+0.1869** |
| arithmetic share of Δ | 46.0 % | 33.1 % |
| surahs with Δ < 0 | **8** | **0** |

**R1 inflates A(C) and therefore understates Δ by roughly 3×.** Its eight negative-Δ surahs
are an artefact: Q58 al-Mujādila at −0.333 is a tanwīn-dense legal surah whose endings R1
merges into `-un`/`-in`/`-an` at citation and then correctly separates in pause. Under R2 that
surah has Δ = 0.000. R1's 17 % map-violation rate is itself a **prereg §12 failure condition**.

**R2 is the sound instrument and R1 is reported because it was pre-registered.** They bracket
the answer; the true Δ is not below R1's +0.066 and is best estimated at R2's +0.187.

---

## 8. RESULT 7 — per-surah, and the exceptions

Under R2, across 114 surahs: **Δ > 0 in 94, Δ = 0 in 20, Δ < 0 in none.** Mean Δ = **+0.215**.

**Perfect pausal monorhyme (A(P1) = 1.000) — 11 surahs:** Q18, Q48, Q65, Q72, Q76, Q87, Q91,
Q92, Q108, Q112, Q114.
**Perfect *citation* monorhyme — only 4:** Q87 al-Aʿlā, Q91 al-Shams, Q92 al-Layl, Q114 al-Nās.
Seven surahs are perfectly monorhymed **only in pause**.

### Where pausal reduction rescues the rhyme outright

| surah | n | A(C) | A(P1) | Δ | classes C → P1 |
|:--|--:|--:|--:|--:|:--|
| **Q18 al-Kahf** | 110 | **0.110** | **1.000** | **+0.890** | **53 → 1** |
| Q65 al-Ṭalāq | 12 | 0.000 | 1.000 | +1.000 | 9 → 1 |
| Q108 al-Kawthar | 3 | 0.000 | 1.000 | +1.000 | 3 → 1 |
| Q112 al-Ikhlāṣ | 4 | 0.000 | 1.000 | +1.000 | 3 → 1 |
| Q48 al-Fatḥ | 29 | 0.179 | 1.000 | +0.821 | 9 → 1 |
| Q33 al-Aḥzāb | 73 | 0.167 | 0.972 | +0.806 | 17 → 2 |
| Q4 al-Nisāʾ | 176 | 0.194 | 0.943 | +0.749 | 28 → 5 |
| Q17 al-Isrāʾ | 111 | 0.273 | 0.991 | +0.718 | 20 → 2 |
| Q76 al-Insān | 31 | 0.300 | 1.000 | +0.700 | 5 → 1 |
| Q25 al-Furqān | 77 | 0.342 | 0.974 | +0.632 | 11 → 2 |
| Q72 al-Jinn | 28 | 0.481 | 1.000 | +0.519 | 7 → 1 |

**Q18 al-Kahf is the case worth stating in words.** Read with full iʿrāb its 110 verse-ends
fall into **53 different rime classes and only 11 % of adjacent pairs rhyme**. Read in pause
they fall into **one class and every adjacent pair rhymes.** H-NEW-2240 recorded the 110/110
figure; what was not known is that the same surah is *almost unrhymed* at citation form. That
single contrast is the clearest evidence in this finding for the hypothesis, and it is
descriptive — it needs no p-value.

Note also that the rescued set is **not** the short mufaṣṣal. Q4 (176 verses), Q17, Q33 and
Q25 are long Medinan and long Meccan surahs. This is not a short-surah artefact.

### Where pausal reduction does nothing — the informative exceptions

Twenty surahs have Δ exactly 0. They split into two kinds:

- **Nothing to gain (4):** Q87, Q91, Q92, Q114 already rhyme perfectly at citation form.
- **Pausal reduction does not help, and the rhyme stays weak (9):** Q103 al-ʿAṣr (A = 0.000,
  3 classes for 3 verses), Q106 Quraysh (0.000), Q49 al-Ḥujurāt (**0.059**, 18 verses,
  4 classes → 4), Q102 al-Takāthur (0.143), Q109 al-Kāfirūn (0.200), Q101 al-Qāriʿa (0.200),
  Q97 al-Qadr (0.250), Q59 al-Ḥashr (0.391), Q58 al-Mujādila (0.238).
- **Moderate and unmoved (7):** Q30, Q32, Q47, Q63, Q93, Q94, Q99.

**Weakest even in pause:** Q103 (0.000), Q106 (0.000), Q49 (0.059), Q60 al-Mumtaḥana (0.083),
Q102 (0.143), Q1 al-Fātiḥa (0.167), Q22 al-Ḥajj (0.169, 32 → 14 classes).

Q49 al-Ḥujurāt is the sharpest exception in the corpus: eighteen verses, four rime classes
under both conventions, and **one adjacent pair in seventeen rhymes**. Whatever organises
al-Ḥujurāt's verse divisions, on this instrument it is not rhyme, and pausal phonology does
not change that. Q1 al-Fātiḥa's low value is a different thing — it alternates `-īm`/`-īn`,
which the coarse ridf-class of H-NEW-2240 unifies and this finer class does not.

---

## 9. POST-HOC — which null to believe

Declared post-hoc; gates nothing. Script `scripts/h-new-2870-posthoc.py`, 10,000 draws.

N1-a's null draws that beat the observed value: **what are they?**

| | R1 | R2 |
|:--|--:|--:|
| draws reaching or beating observed A(P1) | 11 / 10,000 | 57 / 10,000 |
| **their own chance floor Σpᵢ², mean** | **0.2372** | **0.2879** |
| all other draws' chance floor, mean | 0.1534 | 0.2066 |
| **the real pausal partition's chance floor** | **0.1687** | **0.1687** |
| **share of winning draws MORE concentrated than the real partition** | **11/11 = 100 %** | **57/57 = 100 %** |
| corr(A_null, floor_null) over all draws | +0.7063 | +0.6805 |

**Every single draw that beats the observed value is more concentrated than the partition
waqf actually produces** — by 1.7× in mean Σpᵢ² under R2. N1-a's upper tail is not "a random
merge as coarse as waqf"; it is a random merge **substantially coarser**, and it wins by
buying more chance collisions than waqf buys. Its measured verse-profile fidelity is
TV = 0.33, and A_null tracks floor_null at r = +0.68.

The pre-registration named this: §6.2 requires the profile fidelity be reported and §12 makes
"N1 ill-posed → report the null as uninterpretable rather than reporting a p-value from it" an
explicit failure condition. **That condition is met.** N1-b — matched exactly on cardinality
and comparing the excess over each draw's own floor — is the null that is not confounded by
concentration, and it returns 0 / 10,000.

---

## 10. Verdict — stated at every setting, because the setting decides it

The runner's verdict logic was diffed against prereg §8 and printed before declaration. **Its
mechanical output is `NULL — the gain is arithmetic` under both rime definitions.** That is
the locked result and it is reported as the headline.

It is not the whole story, and the following grid is given in full so nothing turns on a
choice made after seeing the data:

| α and D2 definition | R1 | R2 |
|:--|:--|:--|
| **exactly as pre-registered** — k = 6, α = 0.008333, D2 = N1-a alone | **PASS** (p = 0.0012) | **PASS** (p = 0.0058) |
| tightened k = 16, α = 0.003125, D2 = N1-a alone | PASS (0.0012) | NULL (0.0058) |
| tightened k = 16, D2 = N1-b alone (N1-a set aside per §12) | NULL (0.0071) | **PASS (0.0001)** |
| **tightened k = 16, D2 = N1-a ∧ N1-b — what the runner used** | **NULL** | **NULL** |

**Read plainly: the finding fails only in cells that pair a sound instrument with an unsound
null, or an unsound instrument with a sound null.** On the pre-registration taken literally it
passes. On the best instrument (R2, zero map violation) with the best null (N1-b, exactly
matched) it passes at p = 0.0001, z = +4.40, 0 / 10,000. It returns NULL under the conjunction
because that conjunction requires the ill-posed N1-a as well.

**My reading, labelled as judgement and not as a verdict:** the hypothesis is **supported** —
the fāṣila is materially better defined at pausal phonology than at citation form, by a
compositional margin of +0.125 after the +0.062 of collapse arithmetic is removed — and the
NULL is an artefact of a null the pre-registration itself flagged as possibly ill-posed. **I
am not overturning the locked verdict on post-hoc grounds.** The locked verdict stands as
NULL; anyone citing this must cite §9 and this grid with it.

The three things that do **not** depend on any of this:

1. **The collapse magnitude: 3.42×, and +0.0619 of the +0.1869 (33.1 %) is arithmetic.**
2. **The re-cut control: +0.187 against +0.028, z = +70.7, 0 / 2,000.** No α choice touches it.
3. **Q18 al-Kahf: 53 rime classes and 11 % adjacent agreement at citation form; 1 class and
   100 % in pause.** A description, not an inference.

---

## 11. Deviations from pre-registration — all declared, all tightenings

Found by a `--smoke` run that writes nothing, **before** the real run. Every repair **adds**
tests; none replaces a pre-registered quantity, and all pre-registered quantities are reported.

| | what | why | effect on strictness |
|:--|:--|:--|:--|
| **REPAIR-1** | N1-a reported with its measured fidelity; N1-b added; D2 = both | N1-a cannot match the verse-count profile — 116 target blocks from ~157/397 citation types means most blocks take one type, so achievable profiles are pinned by the type-size multiset (TV = 0.33–0.65) | **tightens** |
| **REPAIR-2** | rime-region readability criterion; poetry reported unrestricted **and** readable-only | the muʿallaqāt carry harakāt on 72–84 % of characters, so `fa-ḥawmali` parses as a 3-consonant coda and fails to rhyme with `manzili`, which it does rhyme with. Criterion is measured on the **input**, never on a result | **tightens** |
| **REPAIR-3** | rime definition R2 added; every test run under both R1 and R2 | §7 — R1 reads the tanwīn nūn as the rāwī | **tightens** |
| **Bonferroni** | k = 6 → **k = 16**, α 0.008333 → **0.003125** | the above multiply the primary family to {D2a, D2b, D3, D4b} × {P1, P2} × {R1, R2} | **tightens; self-verifies** |

Also declared: the phonemiser skips ALEF **and** ALEF MAQSŪRA after tanwīn fatḥ. The parent
skips ALEF only — but the parent never reached that branch, because it had dropped the mark
(§1.1). This is a mechanical consequence of the tanwīn fix, not an independent choice.

**The tightening is what produced the NULL.** Under the pre-registered k = 6 the finding
passes. That is stated here rather than buried, because a correction that changes a verdict
must be visible.

---

## 12. Classical anchor — **NONE CITED, and this is a gap**

The brief named `suyuti-al-itqan-fi-ulum-al-quran-english.pdf` nawʿ 27 (waqf). **It is not in
that file.** Checked before locking:

- The Itqān PDF is Muneer Fareed's translation of, in its own introduction, *"some twenty
  chapters of excerpts."* Full-text extraction gives 18,853 lines; searching the waqf
  technical vocabulary (*waqf tāmm*, *kāfin*, *ḥasan*, *ibtidāʾ*) returns **no section on
  pauses**. The nawʿ is absent from this translation.
- `zarkashi-al-burhan-fi-ulum-al-quran.pdf` (1,568 pp.), which does contain al-Zarkashī's nawʿ
  on *al-waqf wa-l-ibtidāʾ*, is a **scanned image with no text layer** — `pdftotext` returns
  0 characters.
- No citable primary waqf source (Ibn al-Jazarī *al-Nashr*, al-Dānī) is on disk.

**No page citation is given and none was invented.** The waqf rules are used as the standard
recitational convention; the claim is carried by the measurement. **Acquisition need:** a
text-layer *al-Burhān* or *al-Nashr* vol. 1. This is the same gap F-16 already recorded
("Classical anchor. Classical `waqf` phonology; Ibn al-Jazarī *al-Nashr*. **Not on disk.**").

---

## 13. Honest limits

1. **The prose delta is not computable** (§6.2). The negative control for the *delta* does not
   exist on disk. Every prose number here is a level comparison on a different instrument.
   Until a vocalised prose corpus is acquired, the claim "prose would gain little" is
   **untested**, not supported.
2. **The locked verdict is NULL** and §10 explains why; the reading in §10 is judgement.
3. **The "citation form" is the Ḥafṣ mushaf's written iʿrāb**, which is itself a recitational
   tradition, not a neutral pre-recitational baseline. The contrast is waṣl-vs-waqf *within*
   one reading, not text-vs-performance.
4. **F-16's own warning stands**: this is close to a definitional restatement, and it is worth
   having as a **magnitude** (3.42× collapse, 33 % arithmetic, +0.125 compositional) and a
   **localisation** (§8), not as a discovery that the Qurʾān rhymes in pause.
5. **The poetry arm is 234 pairs from 3 poems.** It behaves as locked, but it is small, and
   four of the seven muʿallaqāt were excluded for vocalisation.
6. The pairwise-adjacency statistic ignores rhyme structure beyond immediate neighbours; a
   surah alternating ABAB would score 0 and is not distinguished here from an unrhymed one.

---

## 14. Files

- Pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2870-pausal-rhyme.md`
  (SHA-256 `119753ad7862d66dfead2ff6de1032adee0a824cd7544cd8bc4d6688587508d4`, verified at runtime)
- Runner: `findings/phase-b-hypotheses/scripts/h-new-2870.py`
- Post-hoc: `findings/phase-b-hypotheses/scripts/h-new-2870-posthoc.py`
- Run: `runs/h-new-2870/20260807T131820Z/` (`result.json`, `console.log`, `MANIFEST.txt`)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2870.json`, `csv/h-new-2870-posthoc.json`
- Prior rhyme work, cited not duplicated: `h-new-2240-fasila-assonance-taxonomy.md`,
  `h-new-2080-rhyme-scan.md`; method parents `h-new-2690-quantitative-scansion.md`,
  `h-new-2730-scansion-genre-control.md`.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
