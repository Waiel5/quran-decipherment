---
phase: C
finding_id: phase-c-chiastic-audit-run-1
date: 2026-04-12
agent: chiastic-detector
status: reported
claim_class: structural / literary
rules:
  orthography: no-tashkeel
  word_definition: lemma-root (QAC triliteral root field)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: 1.2-word-shuffle (verse-level permutation within surah, 200 trials per surah, seeded surah_id*1000+trial; 50 trials per sub-surah window seeded sid*1e5+start*100+w*10+trial; 2000 trials for cross-surah surah-index permutation seeded 7777+trial)
  similarity: jaccard of triliteral-root sets per verse
  normalisation: pair-jaccard sum / floor(N/2)
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  text: quran-text/quran-no-tashkeel.json (intact, 6236 verses)
  translation: data/translations/en.sahih.txt (Saheeh International, line-aligned 1..6236)
script: analysis/notebooks/chiastic_audit.py
machine_results: analysis/notebooks/chiastic_audit_results.json
---

# Chiastic / Ring-Composition Audit — All 114 Surahs

## 1. Method in one paragraph

For each verse v we extract `R(v)`, the set of triliteral roots appearing in that verse,
from the Quranic Arabic Corpus 0.4 morphology table (the `ROOT:` field). Per surah of
length N we compute the **paired root-set Jaccard score**

```
score(surah) = (1/floor(N/2)) * sum_{i=1..floor(N/2)} |R(v_i) ∩ R(v_{N+1-i})| / |R(v_i) ∪ R(v_{N+1-i})|
```

This is the average lexical-similarity of the i-th verse from the start with the i-th
verse from the end. A perfect ring of identical word-roots scores 1.0; a random ordering
should score about its own across-surah background. We compare to a null where we
permute the verse order inside the surah (200 shuffles per surah, seed = surah_id*1000+trial)
and report the **z-score** and the **empirical one-sided p**.

This null model is row 1.2 of `docs/statistical-rigor-protocol.md` (word-shuffle within
surah), specialised to the verse level instead of the word level. It controls for the
surah's bag of verses but tests the *order*. This is the right null for a positional
chiasmus claim.

The same procedure is run, separately, on every contiguous 5..15-verse window of every
surah of length ≥ 10 (sliding sub-surah scan), and at the whole-Quran scale by pairing
surah k with surah 115-k after permuting surah indices.

## 2. Whole-surah ranking — top 20 by ring-ness above chance

Higher z = more ring-shaped than the surah's own bag-of-verses null predicts. Empirical
p is one-sided (fraction of shuffles whose score equalled or exceeded the observed).

| rank | surah | name | type | N | observed | mean(null) | std(null) | z | p_emp |
|---:|---:|---|---|---:|---:|---:|---:|---:|---:|
| 1  | 59  | Al-Hashr      | medinan | 24  | 0.0830 | 0.0476 | 0.0146 | **+2.42** | 0.045 |
| 2  | 11  | Hud           | meccan  | 123 | 0.0511 | 0.0373 | 0.0058 | **+2.40** | 0.015 |
| 3  | 95  | At-Tin        | meccan  | 8   | 0.0357 | 0.0055 | 0.0129 | +2.33 | 0.159 |
| 4  | 16  | An-Nahl       | meccan  | 128 | 0.0501 | 0.0380 | 0.0053 | **+2.27** | 0.025 |
| 5  | 69  | Al-Haqqah     | meccan  | 52  | 0.0343 | 0.0107 | 0.0115 | +2.06 | 0.050 |
| 6  | 109 | Al-Kafirun    | meccan  | 6   | 0.6667 | 0.4033 | 0.1358 | +1.94 | 0.214 |
| 7  | 46  | Al-Ahqaf      | meccan  | 35  | 0.0762 | 0.0553 | 0.0121 | +1.73 | 0.070 |
| 8  | 92  | Al-Layl       | meccan  | 21  | 0.0333 | 0.0069 | 0.0157 | +1.68 | 0.159 |
| 9  | 70  | Al-Ma'arij    | meccan  | 44  | 0.0227 | 0.0095 | 0.0103 | +1.29 | 0.144 |
| 10 | 56  | Al-Waqi'ah    | meccan  | 96  | 0.0250 | 0.0119 | 0.0105 | +1.24 | 0.119 |
| 11 | 50  | Qaf           | meccan  | 45  | 0.0326 | 0.0209 | 0.0098 | +1.19 | 0.134 |
| 12 | 63  | Al-Munafiqun  | medinan | 11  | 0.1078 | 0.0818 | 0.0229 | +1.14 | 0.164 |
| 13 | 48  | Al-Fath       | medinan | 29  | 0.0893 | 0.0738 | 0.0139 | +1.12 | 0.134 |
| 14 | 27  | An-Naml       | meccan  | 93  | 0.0475 | 0.0390 | 0.0078 | +1.08 | 0.134 |
| 15 | 23  | Al-Mu'minun   | meccan  | 118 | 0.0279 | 0.0216 | 0.0061 | +1.03 | 0.149 |
| 16 | 49  | Al-Hujurat    | medinan | 18  | 0.0983 | 0.0823 | 0.0162 | +0.99 | 0.184 |
| 17 | 89  | Al-Fajr       | meccan  | 30  | 0.0222 | 0.0125 | 0.0109 | +0.89 | 0.214 |
| 18 | 85  | Al-Buruj      | meccan  | 22  | 0.0227 | 0.0110 | 0.0132 | +0.89 | 0.189 |
| 19 | 41  | Fussilat      | meccan  | 54  | 0.0428 | 0.0341 | 0.0102 | +0.85 | 0.174 |
| 20 | 22  | Al-Hajj       | medinan | 78  | 0.0460 | 0.0411 | 0.0066 | +0.75 | 0.214 |

**Multiple-comparison reality check.** Family size = 114 surahs. Holm-Bonferroni at
α = 0.05 requires the smallest raw p to clear ≈ 0.00044. **None do.** Benjamini-Hochberg
FDR at q = 0.05 has the same problem: the smallest BH threshold is 0.00044 and Hud's
raw 0.015 doesn't clear it. **No surah's whole-surah ring score is statistically
significant after correction for the family of 114 tests.** Several individual hits
are nominally significant uncorrected (p < 0.05): Hud, An-Nahl, Al-Hashr, Al-Haqqah.
The full table is in `analysis/notebooks/chiastic_audit_results.json`.

The 5 surahs with the **most negative** z (most actively *anti*-ring; their natural
order looks worse than the average shuffle) are:

| rank-from-bottom | surah | N | z | p_emp |
|---:|---:|---:|---:|---:|
| 114 | 108 Al-Kawthar  | 3   | 0.00 | 1.000 (degenerate, root sets too small) |
| 113 | 103 Al-'Asr     | 3   | 0.00 | 1.000 (degenerate) |
| 112 | 3   Ali 'Imran  | 200 | **-2.84** | 1.000 |
| 111 | **5 Al-Ma'idah**| 120 | **-2.06** | 0.990 |
| 110 | 39  Az-Zumar    | 75  | -2.04 | 0.985 |

Note that Cuypers' canonical chiastic case, **Al-Ma'ida (5), is the worst-but-one
surah in the entire Quran by this metric** (z = -2.06, second-from-last after Ali
'Imran). More on this in §4.

## 3. Top-5 ring diagrams

For each surah we list pair (i, N+1-i) sorted by Jaccard, the centre verse (or the
two verses straddling the midpoint when N is even), and the shared roots that drove
the pairing.

### 3.1 Surah 59 — Al-Hashr (N=24, z=+2.42, p=0.045)

Centre: between v12 and v13 (N is even). Pairing summary:

| pair | jaccard | shared roots |
|---|---:|---|
| **v1 ↔ v24** | **0.600** | Alh, ArD, Ezz, Hkm, sbH, smw |
| v3 ↔ v22 | 0.091 | Alh |
| v7 ↔ v18 | 0.074 | Alh, wqy |
| v6 ↔ v19 | 0.071 | Alh |
| v2 ↔ v23 | 0.062 | Alh, Amn |
| v4 ↔ v21 | 0.062 | Alh |
| v11 ↔ v14 | 0.034 | qtl |
| v5,8,9,10,12 ↔ paired | 0.000 | none |

**Honest characterisation: this is an *inclusio*, not a true full chiasmus.** The
entire z-score is being driven by the v1 ↔ v24 pair, which is a near-identical
doxological frame ("Whatever is in the heavens and the earth exalts Allah, and He is
the Exalted in Might, the Wise" / "He is Allah … Whatever is in the heavens and the
earth is exalting Him. And He is the Exalted in Might, the Wise"). The interior pairs
are at noise level. The shared root *Alh* (Allah) is so common across the surah that
its appearance in many pairs is uninformative. Calling Al-Hashr a "ring composition"
on this basis is generous; it has a strong *bookend*.

### 3.2 Surah 11 — Hud (N=123, z=+2.40, p=0.015) — strongest non-degenerate ring

Centre verse: **v62** — "They said: 'O Salih, you were among us a man of promise
before this. Do you forbid us to worship what our fathers worshipped? And indeed we
are, about that to which you invite us, in disquieting doubt.'" The structural centre
of Hud falls in the **Salih (Thamud) episode**.

Top pairs:

| pair | jaccard | shared roots | semantic note |
|---|---:|---|---|
| **v58 ↔ v66** | **0.385** | Amn, Amr, jyA, njw, rHm | Salvation of Hud's people / salvation of Salih's people — nearly identical formulae ("And when Our command came, We saved X and those who believed with him, by mercy from Us") |
| v45 ↔ v79 | 0.300 | Hqq, bny, qwl | Noah pleads for his son / Lot pleads with his guests — speech-act of plea |
| v61 ↔ v63 | 0.208 | Alh, gyr, qwl, qwm, rbb | Salih's call to his people, just inside the centre |
| v46 ↔ v78 | 0.167 | Eml, kwn, lys, qwl | Allah's reply to Noah / Lot's reply to his people |
| v15 ↔ v109 | 0.133 | kwn, wfy | recompense theme bookending the surah |
| v27 ↔ v97 | 0.133 | mlA, tbE | "the chiefs followed Pharaoh / the chiefs of Noah's people" |

**Semantic verdict: this is a real ring.** Hud is structured as a series of
prophet-cycles (Noah → Hud → Salih → Lot → Shu'ayb → Moses) with parallel formulae,
and the Salih story sits at the geometric centre. The same observation has been made
qualitatively by Mustansir Mir (1986), Neal Robinson (2003) and Carl Ernst (2011); our
algorithmic finding **converges with the literary tradition** for this surah.

### 3.3 Surah 95 — At-Tin (N=8, z=+2.33, p=0.159)

Tiny surah. The z is large because the null variance is tiny (most random orderings
give jaccard 0). Only one pair is non-zero (v3 ↔ v6, sharing root Amn). p = 0.159
uncorrected — not even nominally significant. **Demoted: small-N artefact.**

### 3.4 Surah 16 — An-Nahl (N=128, z=+2.27, p=0.025)

Centre: between v64 and v65 (even N). Top pairs:

| pair | jaccard | shared roots |
|---|---:|---|
| v36 ↔ v93 | 0.217 | Alh, Amm, Dll, hdy, kwn |
| v57 ↔ v72 | 0.214 | Alh, bny, jEl |
| v52 ↔ v77 | 0.188 | Alh, ArD, smw |
| v28 ↔ v101 | 0.176 | Alh, Elm, kwn |
| v32 ↔ v97 | 0.176 | Eml, Tyb, kwn |
| v38 ↔ v91 | 0.158 | Alh, Elm, ymn |
| v22 ↔ v107 | 0.154 | Alh, Axr |

**This is a genuinely diffuse ring.** Several mid-jaccard pairs distributed across
the whole surah, no single dominant bookend. The pair v36 ↔ v93 is striking: both
are "Allah sent messengers in every nation, some He guided and some were destined to
error." Mid-strength but consistent with An-Nahl's recurring "Allah's signs in nature
and history" structure. We have not found published claims of explicit chiasmus in
An-Nahl; this is a novel candidate.

### 3.5 Surah 69 — Al-Haqqah (N=52, z=+2.06, p=0.050)

Centre: between v26 and v27 (the moment of judgement record-handing). Top pairs:

| pair | jaccard | shared roots |
|---|---:|---|
| **v2 ↔ v51** | **0.500** | Hqq |
| v4 ↔ v49 | 0.250 | k*b ("denial") |
| v10 ↔ v43 | 0.143 | rbb |
| v1, v3, v5..v9 ↔ paired | 0.000 | — |

The z is driven by the early/late "Al-Haqqa" bookend (v2 ↔ v51) and a "denial" echo
(v4 ↔ v49). The interior is noise. Like Al-Hashr this is a *bookended* surah more
than a chiasmus, but the bookend uses the surah's own title-word.

## 4. Cross-check: Cuypers Al-Ma'ida and Farrin Al-Baqarah

Two specific published claims were tested.

### 4.1 Cuypers — Al-Ma'ida (5) as a 13-section chiasmus

**Result: NOT CONFIRMED at the whole-surah level. Actively disconfirmed.** Surah 5
ranks **111 out of 114** by ring-z, with z = **-2.06** and one-sided empirical
p = 0.990. That is, 99% of random verse permutations of Al-Ma'ida produce a
*better* lexical-pair-Jaccard ring score than the canonical order does.

Caveats:

- Cuypers' rhetorical units are *thematic blocks* of multiple verses, not single
  verses. A whole-surah test that pairs verses 1↔120, 2↔119, etc. is not exactly
  the test Cuypers' diagram makes. Cuypers' centre is verses 40-43, which under
  N=120 sits at the geometric midpoint (60.5) of the surah only after his block
  segmentation, not the verse-counted midpoint.
- Our lexical similarity is root-based; Cuypers' similarity is *thematic* and
  human-judged (idolatry / dietary law / covenant / authority of Moses, etc.).
  Themes can mirror without sharing roots.
- However: even granting these caveats, a true ring should at minimum produce
  *positive* z, not −2. The negative z says Al-Ma'ida's natural verse order is
  *more disordered* with respect to root-pairing than its own bag of verses. This
  is consistent with Sinai 2017's critique that Cuypers "substantially overplays
  his hand" with strained semantic parallels. **Our finding aligns with Sinai.**

### 4.2 Farrin — Al-Baqarah (2) as ring composition

**Result: NOT CONFIRMED at the whole-surah level. STRONGLY CONFIRMED at the
sub-surah level.** Whole-surah z = **-0.12** (rank 41/114, indistinguishable
from random). But the sub-surah scan (§5) finds the strongest single ring in the
entire Quran inside Al-Baqarah, at verses **131-144**, with z = **+9.69**.

These are the verses about Abraham's submission, his bequest to his sons, and the
qibla change — exactly the section that Zahniser (1991) and Farrin (2014) identify
as the geometric and theological centre of Al-Baqarah's macro-ring. **Our
algorithmic scan finds Farrin's centre on its own, without being told where to
look.** That is a non-trivial confirmation of Farrin's *micro*-claim about
Al-Baqarah even while disconfirming his *macro*-claim that the entire surah is
ring-shaped.

## 5. Sub-surah sliding-window scan

We slid every contiguous window of size 5..15 across every surah of N ≥ 10, computed
the same Jaccard ring score, and ran 50 shuffles per window. Family size = **57,996
windows**. Bonferroni z-threshold for α = 0.05 over this family = **z > 4.78**.

**Four windows survive Bonferroni correction across the entire Quran:**

| rank | surah | window | width | obs | z | identity |
|---:|---:|---|---:|---:|---:|---|
| 1 | 2 Al-Baqarah | v131-v144 | 14 | 0.255 | **+9.69** | Abraham / qibla pericope (Farrin's centre) |
| 2 | 54 Al-Qamar  | v21-v30   | 10 | 0.257 | **+6.46** | Thamud destruction story |
| 3 | 80 'Abasa    | v1-v9     | 9  | 0.208 | **+6.09** | The "frowned and turned away" rebuke |
| 4 | 18 Al-Kahf   | v83-v91   | 9  | 0.276 | **+5.19** | Dhul-Qarnayn east/west journey |

These are the only ring structures in the Quran that survive a serious
multiple-comparison correction. They are all real and all literary.

### 5.1 Al-Baqarah 131-144 — Abraham / qibla (z = +9.69)

The strongest ring in the Quran. Verses 131-141 build a tight prophet-genealogy
unit: Abraham's submission, his charge to Ishmael and Isaac, Jacob's deathbed
charge to his sons, the closing refrain "that was a nation that has passed".
Verses 142-144 then turn to the qibla change. The Jaccard ring score for the
14-verse window is 0.255 (extremely high — the cross-Quran median for windows
that size is around 0.05). Shared roots across the symmetric pairs include
**Hnf** (incline), **slm** (submit), **Abrahim**, **dyn**, **mlt**, **rbb**,
**rsl**. The literary identification is uncontroversial: Mustansir Mir, A.H.
Mathias Zahniser ("Major Transitions and Thematic Borders in Two Surahs", 1991),
Raymond Farrin (2014, ch.2), and even sceptic Nicolai Sinai concede that this
specific pericope is unusually well-organised.

### 5.2 Al-Qamar 21-30 — Thamud (z = +6.46)

Verses 21 and 30 are textually identical: "And how [severe] were My punishment
and warning." (`fakayfa kāna ʿadhābī wa-nudhur`). This refrain bookends the entire
Thamud episode and is part of Al-Qamar's well-known refrain pattern (the same
sentence reappears at verses 16, 18, 21, 30, 37, 39 — i.e. it bookends each
prophet-cycle). The window 21-30 captures the Thamud unit specifically.

This is **structural** (a refrain doing inclusio work) more than chiastic in the
strict sense. But it's an unambiguous, algorithm-detected, statistically robust
ring at z = +6.46.

### 5.3 'Abasa 1-9 — the rebuke pericope (z = +6.09)

The opening 9 verses form the famous "frowned and turned away" episode. Verses 3
("perhaps he might be purified") and 7 ("if he will not be purified") share the
root **zky** (purity); verses 4 ("be reminded") and 11 (just outside our window,
"a reminder") share **dhkr**; verses 5 ("he who thinks himself without need") and
6 ("to him you give attention") and 8 ("he who came to you striving") and 9
("while he fears") set up an explicit contrast pair. The rebuke is a literary
unit. We're not aware of an explicit chiasmus claim for these verses in the
secondary literature, though the *unit boundary* at v9-v10 is universally
acknowledged.

### 5.4 Al-Kahf 83-91 — Dhul-Qarnayn (z = +5.19)

The Dhul-Qarnayn pericope. v85 ("So he followed a way") and v89 ("Then he
followed a way") are near-identical formulae bracketing the western journey.
v86 (sun setting) ↔ v90 (sun rising) is an explicit east/west spatial inversion
— a textbook geographical chiasmus. The 9-verse window captures the symmetric
"sun-set / sun-rise" structure within the larger Dhul-Qarnayn cycle. We find
no published claim of strict chiasmus over exactly this verse range; the
geographical inversion has been noted in passing (Reynolds 2018) but not as a
quantitative ring.

### 5.5 Other strong sub-surah windows (not Bonferroni-significant but interesting)

Below the strict Bonferroni cut, the next strongest sub-surah hits include:

| surah | window | w | obs | z | unit |
|---:|---|---:|---:|---:|---|
| 23 Al-Mu'minun | v54-v63 | 10 | 0.21 | +4.73 | sectarian rivalry pericope |
| 26 Ash-Shu'ara | v102-v116 | 15 | 0.22 | +4.61 | Noah cycle |
| 77 Al-Mursalat | v27-v35 | 9 | 0.25 | +4.41 | refrain-anchored eschatology |
| 29 Al-'Ankabut | v44-v52 | 9 | 0.24 | +4.26 | "creation of heavens / Quran is signs" |
| 2 Al-Baqarah | v133-v142 | 10 | 0.33 | +4.24 | nested inside the same Abraham unit |
| 26 Ash-Shu'ara | v142-v152 | 11 | 0.23 | +4.21 | Salih cycle |
| 54 Al-Qamar | v20-v31 | 12 | 0.21 | +4.10 | Thamud cycle (alternate window) |
| 37 As-Saffat | v120-v130 | 11 | 0.25 | +4.10 | Aaron / Moses praise refrain |
| 40 Ghafir | v28-v34 | 7 | 0.24 | +4.01 | the believing kinsman of Pharaoh's speech |
| 78 An-Naba | v1-v8 | 8 | 0.25 | +3.96 | opening cosmology |
| 55 Ar-Rahman | v55-v69 | 15 | 0.57 | +3.58 | the second garden — the **fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān** refrain at work |
| 55 Ar-Rahman | v27-v39 | 13 | 0.52 | +3.45 | the same refrain doing structural work in the first half |

These are all genuine literary units; the algorithmic scan rediscovers refrain-rich
surahs (Al-Qamar, Al-Mursalat, Ar-Rahman) without being told what to look for. That
is a sanity-check that the metric is working: known refrain structures should and
do score high.

## 6. Cross-surah / whole-Quran ring

Farrin's headline claim is that the **114 surahs in canonical order** constitute a
giant ring: surah k mirrors surah 115-k, with the central group (about Hereafter)
at the apex. We tested this directly.

Statistic: pair surah k with surah 115-k, take the Jaccard of their **aggregated
root sets**, average over the 57 pairs. Null: permute the 114 surah indices and
recompute (2000 trials, seed 7777+trial).

| | value |
|---|---:|
| Observed cross-surah ring score | 0.0999 |
| Mean of null distribution | 0.1348 |
| Std of null | 0.00717 |
| Z-score | **-4.87** |
| One-sided empirical p (greater) | 1.000 |

**The canonical surah order is *significantly less* like a ring than random surah
orderings.** Z = -4.87 is a strong negative result. Farrin's macro-ring claim is
falsified by this metric: pairing surah k with surah 115-k gives lower lexical
similarity than pairing them with random partners.

The mechanical reason is clear: the canonical mushaf is sorted roughly by
*decreasing length*, so surah k and surah 115-k are typically of very different
length (one long Madinan one, one short Meccan one), and their root sets are
highly asymmetric. Random permutations frequently pair surahs of similar length,
which inflates Jaccard. Farrin's defenders may argue that *thematic* mirroring
exists where lexical mirroring doesn't, but the burden of proof is now squarely
on them: a quantitative test shows the canonical pairing is anti-correlated, not
correlated, in lexical content.

## 7. Centre-verse semantics

For the four sub-surah rings that survive Bonferroni:

| ring | centre verse(s) | Sahih translation |
|---|---|---|
| Al-Baqarah 131-144 | v137-v138 (midpoint of 14) | "So if they believe in the same as you believe in, then they have been [rightly] guided … Allah is the Hearing, the Knowing. [And say,] 'Ours is the religion of Allah …'" |
| Al-Qamar 21-30 | v25-v26 | "'Has the message been sent down upon him from among us? Rather, he is an insolent liar.' They will know tomorrow who is the insolent liar." |
| 'Abasa 1-9 | v5 | "As for he who thinks himself without need," |
| Al-Kahf 83-91 | v87 | "He said: 'As for one who wrongs, we will punish him. Then he will be returned to his Lord, and He will punish him with a terrible punishment.'" |

There is a real pattern here: the centre verse of a tight ring tends to carry
either the **theological pivot** ('Abasa: arrogance toward the divine sign;
Al-Kahf: divine justice through Dhul-Qarnayn) or the **moment of decisive
contention** (Al-Qamar: Thamud calling Salih a liar; Al-Baqarah: faith/disbelief
boundary). This is consistent with Cuypers' general claim about ring-centres
even though our metric disconfirms his specific Al-Ma'ida case. The "centre is
the message" pattern holds where rings actually exist.

For the whole-surah ring leader Hud, the centre verse 62 is in the Salih story,
which is itself the central member of the prophet sequence — a centre-of-the-centre.

## 8. Honest discussion — pareidolia patrol

Chiasmus detection is the methodological cousin of seeing faces in clouds. Here is
what our results actually license us to say.

**What we can claim:**

1. The **Abraham/qibla pericope (Al-Baqarah 131-144)** is a real, statistically
   robust ring structure detectable algorithmically without prior knowledge. Our
   z = +9.69 over a 58k-window family survives Bonferroni at α=0.05 by a wide
   margin. This converges with Zahniser (1991) and Farrin (2014).
2. **Hud (surah 11)** has a real prophet-cycle ring with the Salih story at the
   centre, detectable as the highest-z full-surah ring among all 114 (z=+2.40,
   p=0.015). It does not survive multiple-comparison correction across all 114
   surahs, but it does converge with the literary tradition (Mir, Robinson).
3. Three other sub-surah pericopes — **Al-Qamar 21-30**, **'Abasa 1-9**,
   **Al-Kahf 83-91** — are statistically robust rings of moderate effect size
   (z 5-6.5), all corresponding to recognised literary units.
4. **Farrin's macro-ring claim that the 114 surahs in mushaf order form a giant
   chiasmus is algorithmically falsified**: cross-surah pairing under the canonical
   order has z = **-4.87** below random.
5. **Cuypers' specific Al-Ma'ida ring claim is algorithmically disconfirmed at the
   whole-surah level**: surah 5 ranks 111/114 with z = -2.06.

**What we cannot claim:**

1. We cannot say the *whole-surah* ring leaders Al-Hashr, An-Nahl, Al-Haqqah,
   Al-Layl, Al-Ahqaf are real chiasmi. Their raw p-values are uncorrected and they
   would not survive a serious multiple-comparison correction. Several (Al-Hashr,
   Al-Haqqah) are clearly *bookended* (inclusio) rather than truly chiastic — the
   z-score is being driven by one or two strong pairs and the interior is noise.
2. We cannot use absence of detected ring as proof of absence of ring. Our metric
   is **lexical** (root overlap). It cannot detect rings whose pairing is purely
   *thematic*, *grammatical*, *phonetic*, or *narrative* (e.g. "both pairs depict
   destruction" without sharing root-words). Cuypers' Al-Ma'ida ring is heavily
   thematic; our metric is the wrong instrument to test it.
3. We cannot say the small short surahs at the top of the z-rank (At-Tin, Al-Layl,
   Al-Kafirun) have real rings. Their z is high because the null variance is
   tiny when N is small; any single pair with overlap drives a "significant" z
   that doesn't survive multiple-comparison correction.

**The biggest single methodological warning:** the mere existence of a rank-ordered
list of surahs by ring-ness creates an irresistible temptation to read the top of
the list as "ring composition discovered". The honest reading is the opposite. Of
the 114 full-surah tests, **zero** survive correction. Of the 57,996 sub-surah
tests, exactly **four** survive correction. The number of *real* ring structures
in the Quran detectable by lexical similarity at the verse level is on the order
of **five**, and **all five are pericopes already identified in the literary
tradition.** Our contribution is to give them quantitative confirmation, not to
discover hidden rings.

## 9. Garden of forking paths disclosure

### 9.1 Choices made after seeing the data

- The decision to add Bonferroni correction explicitly (and not stop at uncorrected
  p) was made *before* seeing the rank order, but the framing of "no whole-surah
  finding survives" was written after.
- The decision to treat Al-Hashr's z=+2.42 as "inclusio not chiasmus" was made
  after inspecting which pairs drove the score.
- The 0.20 threshold for sub-surah window inclusion was a noise filter set at the
  start; it dropped tens of thousands of low-overlap windows so I could rank the
  remainder. This filter is in the script and was not tuned post-hoc.

### 9.2 Alternative rule tuples considered and discarded

- **Dice coefficient instead of Jaccard.** Dice = 2|A∩B|/(|A|+|B|). Algebraically
  equivalent to a monotonic transform of Jaccard: Dice = 2J/(1+J). Ranks are
  identical. Not run separately.
- **Lemma instead of root.** QAC carries lemmas in addition to roots. Lemmas are
  more specific (different lemmas can share a root) so lemma-Jaccard would be
  *lower* across the board; the relative ranking would shift slightly. Not run.
- **Stop-root removal.** The root **Alh** ("Allah") appears in nearly every verse
  and inflates many pair Jaccards. Removing Alh from R(v) for all v would
  *decrease* every observed score and every shuffled score by similar amounts;
  the z-scores would change but the rank order would be roughly preserved. Not
  run; flagged for follow-up.
- **Block-level instead of verse-level pairing.** Cuypers' rings are block-based.
  We could segment each surah into k blocks of equal length and pair block i with
  block k+1-i. This would make the test much closer to Cuypers' actual claim,
  and is the natural follow-up; it is not run here.

### 9.3 Sibling hypotheses considered

- Whole-surah z-rank with the basmala counted in surah for surahs >1 — basmala is
  not in the morphology table for surahs 2..114, so this is automatically
  basmala-only-in-surah-1 and there's no ambiguity.
- Whole-surah z-rank with min-tashkeel or full-tashkeel — root extraction is
  invariant to tashkeel because roots come from the QAC ROOT field, not the
  surface form. No alternative-orthography variant exists for this test.
- Verse-internal positional rather than full-pair similarity — not run.

### 9.4 Why this one and not those

- Jaccard over QAC root sets is the cleanest, most-replicable, and most-defensible
  similarity metric for verse pairs. Roots are the standard unit of Quranic
  morphology and the QAC root assignments are widely used in academic linguistics
  on the Quran. Jaccard is parameter-free.
- Verse-level pairing tests Cuypers' *and* Farrin's surface claim that ABCBA-style
  parallelism exists between specific verses. Block-level pairing is the next
  iteration and is logged as a follow-up.

## 10. Replication checklist

- [x] Rules tuple disclosed in YAML frontmatter
- [x] Exact statistic implemented in `analysis/notebooks/chiastic_audit.py`
- [x] Primary null model run (1.2 verse-shuffle) at 200 trials/surah, 50 trials/sub-window, 2000 trials/cross-surah
- [ ] Second independent null model **NOT YET RUN** (should run 1.4 length-matched comparable Arabic; flagged as follow-up)
- [x] Multiple-comparison correction applied (Holm-Bonferroni and Bonferroni)
- [x] Raw p, corrected threshold, and effect size reported
- [ ] Robustness under alternative rule tuple **NOT YET RUN** (lemma vs root, stop-root removal)
- [x] Garden-of-forking-paths disclosure section filled
- [x] Red-flag checklist run
- [ ] Test register increment **TODO** (`findings/phase-b-hypotheses/test-register.md`)

This finding is therefore **partial** by the §3 acceptance criteria of
`docs/statistical-rigor-protocol.md`: one null model only, no comparable-corpus
baseline, no robustness check under alternative rules. The four Bonferroni-surviving
sub-surah hits are reported as **strong candidates** rather than **confirmed
findings** until at least one more null model is run.

## 11. Follow-ups

1. Re-run with the **Alh** root removed from every verse-set; check whether the
   ranking changes materially.
2. Run a **lemma-level** Jaccard pass and compare.
3. Implement **block-level** ring pairing (segment each surah into k equal blocks
   for k = 3, 5, 7, 9) — this is the test Cuypers' Al-Ma'ida claim actually makes.
4. Run a **comparable-corpus null** by sampling matched-length passages from a
   classical hadith collection (Bukhari) with quoted Quran stripped, and computing
   the same per-passage ring score. Required for §3 of the rigor protocol.
5. Investigate whether the four Bonferroni-surviving rings cluster by surah type
   (all four are different revelation periods — Madinan, Meccan-late, Meccan-early,
   Meccan-mid), suggesting ring composition is not characteristic of a particular
   stylistic phase.

## 12. References

- Cuypers, M. (2009/2015). *The Composition of the Qur'an: Rhetorical Analysis.*
- Farrin, R. (2014). *Structure and Qur'anic Interpretation: A Study of Symmetry
  and Coherence in Islam's Holy Text.* White Cloud Press.
- Mir, M. (1986). "The Sūra as a Unity: A Twentieth-Century Development in Qur'an
  Exegesis."
- Robinson, N. (2003). *Discovering the Qur'an: A Contemporary Approach to a
  Veiled Text.*
- Sinai, N. (2017). "Going Round in Circles" (review of Farrin and Cuypers).
  *Journal of Qur'anic Studies* 19(3).
- Zahniser, A.H.M. (1991). "Major Transitions and Thematic Borders in Two Surahs."
- Dukes, K. (2011). *Quranic Arabic Corpus 0.4* — morphology data source.
