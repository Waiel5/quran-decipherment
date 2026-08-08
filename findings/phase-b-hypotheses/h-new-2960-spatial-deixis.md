---
title: "H-NEW-2960 — Spatial deixis: a full proximal/distal census of the 1,059 demonstratives, al-Ṭabarī on the deictic axis, and a NULL on whether that axis tracks the Hereafter"
author: Waiel Al-Shujaa
date: 2026-08-08
status: CENSUS ESTABLISHED (documentary) + NULL (inferential, underpowered) + ONE INSTRUMENT DISQUALIFIED
frontier_item: F-4 (HANDOFF/FRONTIER-MAP-2026-08-07.md:206)
prereg_path: findings/phase-b-hypotheses/prereg-h-new-2960-spatial-deixis.md
prereg_sha256: bb7934bd69f8a8d283b44b70fc7fd472fbd291496ab09f38d0fca0db92bc430e
script_path: findings/phase-b-hypotheses/scripts/h-new-2960.py
posthoc_script_path: findings/phase-b-hypotheses/scripts/h-new-2960-posthoc.py
run_dir: findings/phase-b-hypotheses/runs/h-new-2960/20260808T065650Z
posthoc_run_dir: findings/phase-b-hypotheses/runs/h-new-2960-posthoc/20260808T065928Z
git_commit_at_run: e1976028d2c82e35d7f63bc427da84f9872230f3
method_parents: [findings/UNIT-DRIFT-DEFECT.md, findings/PROXY-CLAIMS.md, findings/ABSENCE-CLAIMS.md]
model_finding: findings/phase-b-hypotheses/h-new-2950-sajdah-loci.md
---

# H-NEW-2960 — spatial deixis

## Verdict in one paragraph

**The census stands and is the deliverable.** The corpus carries **1,059 demonstratives, 330
proximal and 729 distal** — a 1 : 2.21 ratio — across 964 verses in 88 of 114 surahs, partitioned
by a morphological rule (the addressee-*kāf*) that agrees with an independently built lemma
partition on all 1,059 tokens with **zero disagreements**. The full inventory is at §1.
**On the inference, F-4 is NULL.** On the only face-valid instrument — the corpus's own antonym
pair *al-dunyā* / *al-ākhira* — distal demonstratives are enriched in Hereafter-framed verses in
the locked direction, **odds ratio 2.74**, but at **exact p = 0.0605** against a Bonferroni gate of
0.0167, and a second mechanical variant of the same instrument brackets it downward to p = 0.269.
**n = 49; this test is underpowered and a NULL is not evidence of absence.** Three results
qualify the null and each is worth more than it:

- **The confound the frontier map named cannot reach the primary test at all.** *Zero* of the 17
  muqaṭṭaʿāt-opening demonstratives — `dhālika l-kitāb` at Q 2:2 included — are in the eligible
  set, because Q 2:2 contains neither *al-dunyā* nor *al-ākhira*. The predicted dominator is
  absent by construction, and this was checked rather than assumed.
- **The formulae are not carrying the association.** Dropping the top ten demonstrative phrase
  types corpus-wide leaves the odds ratio at 3.00 against 2.74; dropping *ka-dhālika* **raises** it
  to 4.19. **CONFIRMED-BUT-FORMULAIC is not the right verdict here** — the honest verdict is
  simply NULL, and the formulaic reading is separately refuted.
- **The well-powered secondary instrument passed its gate and I am disqualifying it, on evidence
  from its own output.** A distributionally generated lexicon reached p = 0.0028 at N = 762 and
  survived length stratification at two bin widths — but its single strongest *this-world* term is
  **`qiyāma`, the Resurrection**, and it classifies Q 2:2 as Hereafter-framed. It is measuring the
  creedal/scriptural register, not eschatology. **A passing p-value from an instrument that
  inverts its own semantic axis is not a finding, and it is reported here as a methodological
  result rather than quietly dropped.**

---

## 1. The census — deliverable 1, documentary, no null model

Instrument: QAC v0.4, `data/morphology/quranic-corpus-morphology-0.4.txt`, SHA-256
`a1d12923…5d8c46`. **A segment enters the inventory iff its `FEATURES` field contains the literal
substring `POS:DEM`.** Nothing is matched on Arabic script or on Buckwalter substrings of the
surface form — the brief's rule is honoured by matching the annotation, not the text.

**`POS:DEM` = 1,059 tokens. The frontier map's figure is confirmed exactly.**

### 1.1 The partition rule, stated as a function

> **DEIXIS(t) = DISTAL if the `FORM` of the `POS:DEM` segment ends in the addressee-kāf enclitic,
> PROXIMAL otherwise.**
> Regex: `(?:ka|ki|kumo|kumu|kumaA|kum|kun~a)$`

This is the classical criterion: the *kāf al-khiṭāb* on `dhāli-**ka**`, `til-**ka**`,
`ulāʾi-**ka**` is what turns the bare deictic base into a pointer away from the speaker; its
absence leaves the proximal with the *hāʾ al-tanbīh*, `hā-dhā`, `hā-dhihi`, `hā-ʾulāʾi`.
**No surah, verse, lemma or form is hard-coded anywhere in this design** — the rule is a function,
which is what `PROXY-CLAIMS.md` §3 Screen A asks for and what a set literal is not.

**Independent check.** Partitioning instead by QAC lemma — proximal {`ha`*aA`, `*aA`, `ha`*a`n`,
`ha`tayon`, `hunaA`, `ha`ka*aA`}, distal {`*a`lik`, `>uwla`^}ik`, `>uwlaA^'`, `tilokum`,
`*a`nik`} — reproduces the same partition on all 1,059 tokens, **0 disagreements**. Two
separately constructed partitions agreeing exactly is the check `UNIT-DRIFT-DEFECT.md` §8 asks
for; it is reported because it was run, not because it was needed.

### 1.2 Full inventory — 330 proximal

| FORM (Buckwalter) | lemma | gloss | n |
|:--|:--|:--|--:|
| `ha`*aA` | `ha`*aA` | *hādhā* — this (m.sg.) | 188 |
| `ha`^&ulaA^'i` | `ha`*aA` | *hāʾulāʾi* — these (pl.) | 45 |
| `ha`*aA^` | `ha`*aA` | *hādhā* (long-alif orthography) | 37 |
| `ha`*ihi` | `ha`*aA` | *hādhihi* — this (f.sg.) | 24 |
| `ha`*ihi.` | `ha`*aA` | *hādhihi* | 16 |
| `ha`*ihi.^` | `ha`*aA` | *hādhihi* | 7 |
| `*aA` | `*aA` | *dhā* — bare proximal base | 5 |
| `hunaA` | `hunaA` | *hunā* — here | 3 |
| `hunaA^` | `hunaA` | *hunā* | 1 |
| `ha`*aAni` / `ha`*a`ni` | `ha`*a`n` | *hādhāni* — these two (m.) | 2 |
| `ha`ka*aA` | `ha`ka*aA` | *hākadhā* — thus | 1 |
| `ha`tayoni` | `ha`tayon` | *hātayni* — these two (f.) | 1 |
| | | **total** | **330** |

Lemma totals: `ha`*aA` **317**, `*aA` 5, `hunaA` 4, `ha`*a`n` 2, `ha`ka*aA` 1, `ha`tayon` 1.

**All five `*aA` tokens are the rhetorical `man dhā lladhī`** — Q 2:245, 2:255, 3:160, 33:17,
57:11. They are proximal in form and interrogative-emphatic in function; counted, and flagged so
no reader mistakes them for ordinary pointing.

### 1.3 Full inventory — 729 distal

| FORM (Buckwalter) | lemma | gloss | n |
|:--|:--|:--|--:|
| `*a`lika` | `*a`lik` | *dhālika* — that (m.sg.) | 426 |
| `>uw@la`^}ika` | `>uwla`^}ik` | *ulāʾika* — those (pl.) | 204 |
| `tiloka` | `*a`lik` | *tilka* — that (f.sg.) | 40 |
| `*a`likumo` | `*a`lik` | *dhālikum* — that (addressee m.pl.) | 28 |
| `*a`likumu` | `*a`lik` | *dhālikumu* | 11 |
| `*a`likum` | `*a`lik` | *dhālikum* | 8 |
| `*a`liki` | `*a`lik` | *dhāliki* (addressee f.sg.) | 3 |
| `>uw@la`^}ikumo` | `>uwlaA^'` | *ulāʾikum* | 2 |
| `*a`likumaA`, `*a`likun~a`, `*~a`lika`, `t~iloka`, `*a`nika`, `tilokumaA`, `tilokumu` | — | dual / f.pl. / assimilated / *dhānika* / *tilkumā* | 1 each |
| | | **total** | **729** |

Lemma totals: `*a`lik` **520**, `>uwla`^}ik` **204**, `>uwlaA^'` 2, `tilokum` 2, `*a`nik` 1.

### 1.4 Distribution and collocation

| quantity | value |
|:--|--:|
| demonstrative tokens | **1,059** |
| proximal : distal | **330 : 729** (1 : 2.21) |
| verses carrying ≥ 1 demonstrative | **964** |
| surahs carrying ≥ 1 demonstrative | **88 of 114** |
| tokens whose word carries a `ka+` prefix (*ka-dhālika*, "thus") | **126** |
| tokens in vv. 1–3 of the 29 `POS:INL` surahs | **17** |

The **29 muqaṭṭaʿāt surahs are derived in code** from `POS:INL` — {2, 3, 7, 10, 11, 12, 13, 14, 15,
19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}, every locus at
verse 1 except Q 42, which also has one at verse 2. **No stored list of 29 surahs is read
anywhere in this work.**

**The ten most frequent demonstrative phrase types**, ranked corpus-wide (DEM form + next word's
first stem):

| n | phrase | n | phrase |
|--:|:--|--:|:--|
| 58 | *ulāʾika humu* | 20 | *dhālika āyatan* |
| 30 | *dhālika anna* | 19 | *ulāʾika hum* |
| 28 | *ulāʾika lladhīna* | 19 | *dhālika najzī* |
| 24 | *dhālika āyātin* | 15 | *hādhā illā* |
| 21 | *ulāʾika aṣḥābu* | 13 | *dhālika huwa* |

**The distal's dominant use is the anaphoric human-group verdict formula** — `ulāʾika humu…`,
`ulāʾika lladhīna…`, `ulāʾika aṣḥābu…` account for 107 tokens by themselves. This is descriptive
and carries no p-value; it is what §6's drop-the-formulae check is testing against.

### 1.5 Two asymmetries in QAC's `DEM` category, declared rather than corrected

1. **The locative axis is one-sided.** `hunā` ("here", 4 tokens) is `POS:DEM`; **`hunālika`
   ("there") is `POS:T` (8 tokens) and `POS:LOC` (1) and is therefore not in the inventory at
   all.** The proximal count carries a locative the distal count does not. Four tokens in 1,059;
   disclosed and left alone, because correcting it would mean hand-adding a form and that is the
   defect this design refuses.
2. **`hākadhā`** contains a *kāf* that is not the addressee-*kāf*. The rule is anchored to the end
   of the form, so `ha`ka*aA` — ending in `*aA` — is correctly left proximal. This was checked
   before the rule was locked and is why it is a suffix match.

**This census has standing value independent of everything below it, and nothing below can
weaken it.**

---

## 2. The classical anchor — al-Ṭabarī states the axis, and states its neutralisation

`data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/2/2.json`, on
`dhālika l-kitāb` (Q 2:2). **Read in the Arabic.** al-Ṭabarī first reports the exegetes' gloss:

> قال عامّة المفسرين: تأويل قول الله تعالى ( ذلك الكتاب ) : هذا الكتاب

> "The generality of the exegetes said: the interpretation of *dhālika l-kitāb* is *hādhā
> l-kitāb*."

He gives it by isnād from **Mujāhid** (via Ibn Jurayj), **ʿIkrima** (via Khālid al-Ḥadhdhāʾ),
**al-Suddī**, and **Ibn ʿAbbās** (via Ibn Jurayj) — reports 247–250 in the printed numbering. He
then raises the objection in the exact terms of this hypothesis:

> فإن قال قائل: وكيف يجوزُ أن يكون " ذلك " بمعنى " هذا "؟ و " هذا " لا شكّ إشارة إلى حاضر
> مُعايَن, و " ذلك " إشارة إلى غائب غير حاضر ولا مُعايَن؟

> "If someone asks: how can *dhālika* carry the sense of *hādhā*, when **hādhā is without doubt a
> pointing to what is present and directly seen, and dhālika a pointing to what is absent, not
> present and not seen**?"

**That sentence is the classical statement of the very axis F-4 proposes to test, and it is on
disk in Arabic.** al-Ṭabarī's answer is the part that matters for this finding: he holds that
what has *just been completed* — here, the الم that immediately precedes — is grammatically absent
but functionally present to the addressee, so the distal is licensed where a proximal is meant.

> **The tradition therefore supplies both halves at once: the deictic axis is real, and it is
> defeasible.** A classical grammarian would predict exactly what §4 measures — a directionally
> correct but leaky association — rather than a clean partition. This is the strongest reason not
> to read the null below as a refutation of the axis.

### 2.1 A source caution that this search turned up, and it is worth more than a citation

The obvious place to look for Ibn ʿAbbās on this verse is
`spa5k-tafsir-api/ar-tafseer-tanwir-al-miqbas/`. **That folder is not Ibn ʿAbbās.** It holds Ibn
ʿĀshūr's *al-Taḥrīr wa'l-Tanwīr* (d. 1393 AH), the slug having collided on the word *Tanwīr*; its
Q 2:2 entry quotes al-Zamakhsharī five times, al-Raḍī al-Astarābādhī three times and al-Sakkākī
three times, and **Ibn ʿAbbās died in 68 AH.** Recorded with its verification at
`data/literature/classical-tafsir/MISLABELLED-TANWIR-FOLDER.md`.

**This finding does not depend on that folder.** §2's Ibn ʿAbbās attribution comes from
al-Ṭabarī's own isnād — al-Qāsim b. al-Ḥasan ← al-Ḥusayn b. Dāwūd ← Ḥajjāj ← Ibn Jurayj ← Ibn
ʿAbbās, report 250 — read verbatim in the Arabic and independently confirmed by a
diacritic-insensitive recount of every transmitter named. The genuine *Tanwīr al-Miqbās* on disk
(`en-tafsir-ibn-abbas/`, English only) renders Q 2:2 as *"this is the Book that Muhammad is
reciting to you"* — **silently taking the distal as a proximal, with no deictic discussion at
all**, which is the same reading al-Ṭabarī reports and argues past.

---

## 3. The test — deliverable 2, and the thing I could not write as a function

Pre-registered at `prereg-h-new-2960-spatial-deixis.md`, SHA-256 `bb7934bd…c430e`, embedded as a
literal in the script and verified at runtime before the run directory was created.

### 3.1 The referent problem, stated plainly

**I cannot write a function that classifies the *referent* of a demonstrative, and the finding
does not pretend to.** A demonstrative's referent is a discourse entity; recovering it needs
either a dependency parse with coreference or human judgement. The judgement route is the exact
defect `PROXY-CLAIMS.md` catalogues and was refused. The parse route is not on disk, and the
absence is stated with its search per `ABSENCE-CLAIMS.md` §4:

> `ls -la data/syntax/` returns exactly one file, `data/syntax/UD-QURAN-SOURCE.md` (1,754 bytes),
> whose own front-matter reads `status: external reproducibility input; binary not committed`.
> No treebank, CoNLL-U file or dependency table is present. **Positive control:** the same command
> in `data/morphology/` returns the QAC file this work does use. Scope: `data/syntax/` only.

**What was written as a function is the verse's topical FRAME, and substituting frame for referent
is itself an untested empirical claim.** It is declared in the pre-registration and repeated here:
every verdict below is about **frame**, not **referent**. **F-4 as written is therefore not
decided by this run** — a weakened version of it is, and saying so is not a hedge but the actual
scope of the result.

### 3.2 The instrument that has face validity — C1, the closed antonym pair

The corpus lexicalises the opposition itself, in one matched pair: *al-ḥayāt al-**dunyā*** against
*al-**ākhira***. Using it names no third word.

> **frame(v) = ESCH** if *v* carries ≥1 segment with `LEM:A^xir` and none with `LEM:d~unoyaA`;
> **DUNYA** if the reverse; **UNCLASSIFIED** if both or neither.

Free parameters: none. **Lemma disambiguation is load-bearing here**: `ākhar` "another"
(`LEM:A^xar`, 70 tokens) shares the root ʾ-KH-R and is excluded by lemma, not by judgement. A
substring search on the root would have swept it in — which is the brief's warning, occurring on
this design's own instrument.

Coverage: 156 verses classified — 99 ESCH, 57 DUNYA — carrying **49 demonstratives in 42 verses**.

### 3.3 Statistic, null, and the clustering it has to respect

**S = the count of DISTAL tokens in ESCH-frame verses** — an integer cell of the 2×2. A raw count,
not a density; `UNIT-DRIFT-DEFECT.md` Screen A cannot reach it, which is why this target was
chosen.

A verse can carry several demonstratives (49 tokens sit in 42 verses), so tokens are **not
independent** and Fisher's exact test is anticonservative here. **The registered primary p is a
verse-clustered permutation**: permute ESCH/DUNYA labels across the eligible verses holding the
verse counts fixed, tokens travelling with their verse; 200,000 draws, seed 20260509, replication
20260519. Fisher is reported alongside as the unclustered comparison and is not the gate.

Because the primary's state space is small, the **exact** permutation p is also computed by a
dynamic programme over the multiset — no sampling error at all. **It was verified against
brute-force enumeration of all subsets before the run**, on the multiset {0,1,2,1,3,0,2} choosing
3: the DP and the exhaustive enumeration return 0.571429, 0.342857 and 0.142857 at thresholds
4, 5 and 6, identical to six decimals. The script's own `--self-check` verifies the Fisher
routine against a hand-computable 2×2 (17/70) and the deixis rule against four forms including
`hākadhā`.

Direction locked in advance: one-sided upper, **proximal → this-world, distal → Hereafter**.
Bonferroni over the three registered tests, α = 0.05/3 = **0.0166667**.

---

## 4. Results — the primary is NULL, and it is bracketed downward

### 4.1 C1, the registered primary

| | DUNYA-frame | ESCH-frame | row |
|:--|--:|--:|--:|
| **DISTAL** | 10 | **24** | 34 |
| **PROXIMAL** | 8 | 7 | 15 |
| column | 18 | 31 | **49** |

| quantity | value |
|:--|--:|
| odds ratio | **2.743** |
| observed S | 24 |
| null E[S] | 20.238 |
| **clustered permutation p (200k draws, seed 20260509)** | **0.06024** |
| **exact permutation p (closed form, no sampling)** | **0.060535** |
| replication, seed 20260519 | 0.05988 |
| Fisher one-sided (unclustered, not the gate) | 0.10116 |
| gate | α = 0.0166667 |
| **verdict** | **NULL** |

**Direction is as locked** — distal is 70.6 % Hereafter-framed against proximal's 46.7 % — and the
effect size is not small. It simply does not clear the gate at n = 49.

**Note that the clustered p (0.0605) is smaller than Fisher's (0.1012).** The clustering
correction moves the result *toward* significance rather than away, because the eligible tokens
are only mildly clustered (49 in 42 verses) while Fisher additionally conditions on a margin the
permutation lets float. The registered null is the one whose assumptions hold and it is the one
reported; the disagreement is recorded rather than resolved in the finding's favour.

### 4.2 The sensitivity that brackets it downward — and it matters

`LEM:A^xir` is a whole lemma, chosen precisely so no sub-selection judgement enters. It therefore
also carries `ākhirīn` ("later generations", 10 tokens) and `ākhir` ("end/last", 8), which are not
eschatological. **S1** restricts the marker to the feminine-singular form class `'aAxirap*` — a
second mechanical rule — which cleanly isolates *al-ākhira* but **discards `al-yawm al-ākhir`,
the Last Day (16 ADJ tokens), which is squarely eschatological.**

| instrument | N | odds ratio | exact p |
|:--|--:|--:|--:|
| **C1** — whole lemma, **over-inclusive** | 49 | **2.743** | **0.0605** |
| **S1** — feminine-singular form class, **over-exclusive** | 36 | 1.600 | 0.2690 |

> **Neither is the right marker set; they bracket it from opposite sides, and both are NULL.**
> Per `UNIT-DRIFT-DEFECT.md` §6 rule 6 both are reported and the stricter is taken. **A reader
> should take S1's p = 0.269 as the honest strength of the primary claim, not C1's 0.0605** — a
> meaningful part of C1's already-insufficient association is carried by tokens that are not
> about the Hereafter at all.

---

## 5. The named confound cannot reach the primary — and this was checked, not assumed

The frontier map's stated confound is that *`dhālika l-kitāb` at Q 2:2 and the muqaṭṭaʿāt-opening
formulae will dominate the distal count*, and the pre-registration locked the decision to model
them rather than delete them (prereg §3). Modelling them produced a cleaner answer than deletion
could have:

| check | result |
|:--|--:|
| demonstratives in vv. 1–3 of the 29 `POS:INL` surahs | **17** (8 *tilka*, 4 *dhālika*, 3 *hādhā*, 1 *dhālikumu*, 1 *ulāʾika*) |
| **of those, in the C1-eligible set** | **0** |
| frame of **Q 2:2** under C1 | **UNCLASSIFIED** |
| effect of arm D1 (drop all 17) on the primary | **none — N stays 49, p unchanged at 0.06024** |

> **Q 2:2 contains neither *al-dunyā* nor *al-ākhira*, so `dhālika l-kitāb` is not in the test
> and cannot be driving it.** The predicted dominator is absent from the eligible set by
> construction. **Had this been assumed rather than measured, the natural move would have been to
> exclude the openings and report a "cleaned" result — which would have been a deletion that
> changed nothing, described as a control.**

---

## 6. The drop-the-formulae check — the association does *not* die

This is the check the brief named as decisive, and its answer is the opposite of the frontier
map's prior (*"the effect may be entirely carried by ~20 formulaic phrases"*). Phrase types are
ranked **corpus-wide**, never within the test set, so the ranking cannot be tuned.

**C1, the primary instrument:**

| arm | N | odds ratio | exact p |
|:--|--:|--:|--:|
| full inventory | 49 | 2.743 | 0.0605 |
| drop muqaṭṭaʿāt openings (D1) | 49 | 2.743 | 0.0605 |
| **drop `ka+`-prefixed *ka-dhālika* (D2)** | 43 | **4.190** | **0.0359** |
| drop top-1 / top-2 phrase types | 48 | 2.629 | 0.0798 |
| drop top-3 / **top-5** phrase types | 44 | 2.540 | **0.0926** |
| drop top-10 phrase types | 40 | **3.000** | 0.0983 |

> **The odds ratio is flat to rising across every deletion — 2.74 → 2.54 → 3.00 — and removing the
> manner connective *ka-dhālika* raises it to 4.19.** The p-values drift upward only because N is
> falling; the association itself is not concentrated in the frequent phrases.

**CONFIRMED-BUT-FORMULAIC is therefore not the correct verdict here, and it would have been the
wrong one to reach for.** The honest verdict is NULL — and the formulaic reading is separately
refuted rather than left standing as an unexamined alternative. On the secondary instrument the
same deletions *strengthen* the result monotonically (C3: p = 0.00275 full → 0.000315 at top-5
dropped), which points the same way.

---

## 7. The secondary instrument passed its gate, and I am disqualifying it

**Because C1 classifies only 49 tokens, the pre-registration also generated a lexicon** — rather
than curating one — by Monroe–Colaresi–Quinn log-odds over the C1 seed verses, restricted to
{N, PN, ADJ, V} lemmas with `POS:DEM` and `POS:PRON` excluded by construction, at two declared
values of k (prereg §4.2).

**Both secondaries cleared the Bonferroni gate**, on ~15× the data:

| instrument | N | odds ratio | permutation p | replication | length-stratified, quintiles / deciles |
|:--|--:|--:|--:|--:|--:|
| C2, k = 25 | 702 | 1.612 | 0.01239 | 0.01204 | 0.01927 / 0.01307 |
| **C3, k = 50** | 762 | **1.771** | **0.00275** | 0.00288 | **0.00548 / 0.00328** |

Verse length is not the driver: stratifying the permutation within length bins barely moves
either, at either of the two bin widths `UNIT-DRIFT-DEFECT.md` §6.1 requires — even though the
distal share does climb monotonically with verse length (0.622 in the shortest quintile to 0.741
in the longest). **C2 is the one arm that moves across the gate**: 0.01239 unstratified → 0.01927
at quintiles, which would fail α = 0.0167, → 0.01307 at deciles, which would pass. §6.1's rule is
that the finer bin is the honest one, and it agrees with the unstratified value; the disagreement
is recorded rather than resolved in the finding's favour. C3 clears at every setting.

**And none of that matters, because the instrument is measuring the wrong thing.** From its own
output (post-hoc run
`findings/phase-b-hypotheses/runs/h-new-2960-posthoc/20260808T065928Z/result.json`, probe P2 —
**not pre-registered, and it can only weaken**):

| side | top five generated terms |
|:--|:--|
| "Hereafter" | *āmana* (believed), *Allāh*, *kitāb*, *yawm*, *rasūl* |
| "this-world" | **`qiyāma` — the Resurrection**, *baʿḍ*, *ḥayāt*, *nafs*, *ittakhadha* |

> **The single strongest this-world term in the generated lexicon is the Resurrection.** At both
> k = 25 and k = 50, `qiyāma` ranks **first** on the DUNYA side — because *yawm al-qiyāma* occurs
> in the recurrent contrastive formula alongside *al-ḥayāt al-dunyā*, and a distributional
> generator learns its seed's collocates, not its semantic field. Meanwhile *janna*, *nār*,
> *sāʿa* and *baʿatha* are **absent from the lexicon entirely**, and the "Hereafter" side is the
> creedal-and-scripture register — *believe*, *God*, *book*, *day*, *messenger* — which is where
> *al-ākhira* actually lives, inside `yuʾminūna bi-l-ākhira`.

**The demonstration lands on the exact verse the frontier map named.** C3 classifies **Q 2:2 —
`dhālika l-kitābu lā rayba fīhi`, a verse about scripture — as Hereafter-framed**, because
*kitāb* is its third-strongest ESCH term. And 14 of the 17 muqaṭṭaʿāt-opening demonstratives *are*
in the C3-eligible set, against 0 in C1's.

> **C2 and C3 measure creedal/scriptural register against worldly-life register. That is a real
> axis and the association with deixis is real; it is not the eschatological axis F-4 proposes,
> and it cannot be reported as evidence for it.**

Per the locked verdict logic (prereg §7), a secondary that passes while the primary fails is a
**descriptive observation requiring its own prospective pre-registration** and cannot rescue,
upgrade or create a verdict. That rule is applied here without exception — and in this case the
observation does not even survive its own face-validity check.

**The generator was still the right call.** `PROXY-CLAIMS.md` §4 asks for generators over curated
lists; the generator failed *visibly*, from its own ranked output, in a way a hand-built
eschatological word list would have concealed behind my own agreement with it. **A curated list
would have passed and been wrong.**

---

## 8. Honest limits

1. **n = 49 on the primary, and it governs everything.** The permutation floor is 5.0 × 10⁻⁶, so
   p-resolution is not the constraint; power is. **A NULL here is not evidence that the deictic
   axis is unrelated to eschatological reference** — it is evidence that any relation is not
   large enough for 49 tokens under a verse-clustered null to reveal. This sentence was written
   into the pre-registration before any cell existed and is repeated unchanged.
2. **Frame is not referent.** §3.1. The substitution is an untested claim, and F-4 as written is
   not settled by this run.
3. **The marker set is bracketed, not solved.** §4.2. C1 over-includes, S1 over-excludes, and the
   right instrument is somewhere between them. A verse-level tagging of *al-yawm al-ākhir* as
   distinct from *ākhirīn* would need a form-and-context rule this design did not attempt.
4. **QAC's `DEM` category is not the whole deictic system.** `hunālika` sits outside it (§1.5),
   and `thamma` ("there", 4 `POS:LOC` tokens) is outside it too. A census of the full deictic
   field would need `POS:LOC` and `POS:T` folded in, which changes the object being counted.
5. **The permutation sampler was changed before the first real run**, from a per-draw shuffle to a
   batched one, for speed. **No result existed at that moment**; the pre-registration names a
   seed but no RNG, and the exact closed-form p in §4.1 — which involves no sampling at all —
   agrees with the sampled value to 3 × 10⁻⁴. Recorded because the change is invisible in the
   output and would otherwise be undiscoverable.
6. **One classical source is used; the parallel Arabic search of al-Qurṭubī and al-Zamakhsharī
   ran alongside and §9 records its outcome.** al-Ṭabarī's passage in §2 was read directly in the
   Arabic JSON and is quoted verbatim from it.
7. **The secondary's association is real and unexplained.** Disqualifying it as an eschatology
   instrument does not explain why distal demonstratives are enriched in the creedal/scriptural
   register at OR ≈ 1.8, p = 0.0028, surviving length stratification. That is a live observation
   and it needs its own prospective test.

---

## 9. What this settles, and what it queues

**Settled:**
- The demonstrative census: **1,059 = 330 proximal + 729 distal**, full inventory at §§1.2–1.3,
  partition rule agreeing with an independent lemma partition on **0 disagreements**.
- **F-4 is NULL** on the face-valid instrument, at OR = 2.74, exact p = 0.0605, bracketed
  downward to p = 0.269, against α = 0.0167.
- **The named confound is absent from the primary test set** — 0 of 17 opening formulae, Q 2:2
  unclassified.
- **The effect is not formulaic.** Dropping the top ten phrase types leaves OR at 3.00.
  CONFIRMED-BUT-FORMULAIC is refuted, not merely unclaimed.
- **A distributionally generated lexicon is not a semantic classifier**, demonstrated by its own
  ranking of `qiyāma` as the strongest *this-world* term. This is a transferable methodological
  result and applies to any future seed-and-expand instrument in this repository.
- **al-Ṭabarī states the proximal/distal axis explicitly, in the Arabic, at Q 2:2**, and states
  its defeasibility in the same passage.

**Queued (each needs its own prospective pre-registration):**
- **H-NEW-2961** — the creedal-register association at OR ≈ 1.8, tested as its own hypothesis
  rather than as a failed proxy for eschatology.
- **H-NEW-2962** — the deictic field widened to `POS:LOC` and `POS:T` so `hunālika` and `thamma`
  are inside the object rather than outside it.
- **H-NEW-2963** — referent extraction for adnominal demonstratives once a dependency parse is on
  disk, replacing frame with government.

---

## Sources

- `data/morphology/quranic-corpus-morphology-0.4.txt` — QAC v0.4 (Kais Dukes, GPL; text lineage
  Tanzil Uthmani 1.0.2), SHA-256 `a1d12923…5d8c46`.
- `data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/2/2.json` — §2, verbatim.
- `findings/phase-b-hypotheses/prereg-h-new-2960-spatial-deixis.md` — SHA-256 `bb7934bd…c430e`.
- Run: `findings/phase-b-hypotheses/runs/h-new-2960/20260808T065650Z/{result,manifest}.json`.
- Post-hoc: `findings/phase-b-hypotheses/runs/h-new-2960-posthoc/20260808T065928Z/{result,manifest}.json`.
- Method: `findings/UNIT-DRIFT-DEFECT.md`, `findings/PROXY-CLAIMS.md`,
  `findings/ABSENCE-CLAIMS.md`, `STATE-OF-THE-PROJECT-2026-08-07.md` §0.
- Model finding: `findings/phase-b-hypotheses/h-new-2950-sajdah-loci.md`.
- Frontier: `HANDOFF/FRONTIER-MAP-2026-08-07.md:206` (F-4).
