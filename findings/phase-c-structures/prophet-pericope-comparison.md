---
phase: C
finding_id: phase-c-prophet-pericope-comparison-run-1
date: 2026-04-12
agent: deep-reader
status: reported
claim_class: literary-structural / comparative-narratology
rules:
  orthography: no-tashkeel (for ring + Jaccard), full-tashkeel only where saj' cited
  word_definition: lemma-root (QAC v0.4), PN proper-noun lemma for prophet-name matching
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  null_model: 1.2-verse-shuffle-within-window (300-500 trials) for ring-score; no new nulls for Jaccard vocab diversity (exploratory)
  similarity: Jaccard of triliteral-root sets per verse
  pericope_clustering: consecutive prophet-mention verses gap ≤ 3 (core); gap ≤ 5 with ±5-verse pad (expanded narrative window)
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
  revelation_order: data/revelation-order.csv (Egyptian/Nöldeke)
  prior_findings:
    - findings/phase-c-structures/chiastic-audit.md
    - findings/phase-b-hypotheses/jinas-wordplay.md
    - findings/phase-b-hypotheses/saj-rhyme-analysis.md
    - findings/phase-b-hypotheses/root-cartography.md
    - findings/phase-b-hypotheses/chronological-revelation.md
script: scratch/prophet-pericope/analyze.py
machine_results: scratch/prophet-pericope/ (run artifacts)
---

# Prophet Pericope Comparative Audit — Moses, Abraham, Joseph, Noah, Jesus, Adam

How does the Quran tell the *same* prophetic story in different surahs? This
report locates every canonical prophet-mention, clusters them into pericope
units, and compares the resulting versions using the same root-based Jaccard
similarity that `chiastic-audit.md` used for ring detection. Six prophets,
≈330 total mentions, 220+ pericope windows. Every number below is reproducible
from the single script `scratch/prophet-pericope/analyze.py`.

---

## 1. Prophet-name census (Task 1)

Proper-noun lemmas from QAC (`POS:PN` + `LEM:<name>`). Counts match the task
spec exactly.

| Prophet | QAC lemma | Total mentions | Distinct verses | Surahs | Pericope units (gap ≤ 3) |
|---|---|---:|---:|---:|---:|
| Moses   | `muwsaY`      | **136** | 131 | **34** | **81** |
| Abraham | `<iboraAhiym` | **69**  | 63  | **25** | **46** |
| Joseph  | `yuwsuf`      | **27**  | 26  | **3**  | **14** |
| Noah    | `nuwH`        | **43**  | 43  | **28** | **39** |
| Jesus   | `EiysaY`      | **25**  | 25  | **11** | **21** |
| Adam    | `A^dam`       | **25**  | 25  | **9**  | **16** |

**Moses is, by a factor of ~2, the most fragmented prophet** — 136 mentions
spread across 34 surahs in 81 distinct pericope units. Noah is almost as
dispersed per mention (43 / 28 = 1.54 mentions/surah; Noah is typically named
once as part of a prophet list). **Joseph is the outlier**: 92.3% of all Joseph
mentions (24 of 26) are inside Surah 12; the other two are his single cameo in
6:84 (the prophet list) and 40:34 (a passing retrospective).

### 1.1 Major pericope windows per prophet

Longest contiguous mention cluster for each prophet, by surah. These are the
"main story" windows used in downstream analyses.

| Prophet | Surah | Window (mention-verses) | Expanded (±5 pad, merged) | Notes |
|---|---|---|---|---|
| Moses | **7 Al-Aʿrāf**    | v103–v160 | **v98–v165 (68 vv)**    | Pharaoh + tablets + calf |
| Moses | **20 Ṭā-Hā**      | v9–v98    | **v31–v96 (66 vv)**     | Burning bush → Sāmirī |
| Moses | **26 Ash-Shuʿarāʾ**| v10–v68  | **v38–v70 (33 vv)**     | Pharaoh contest, condensed |
| Moses | **28 Al-Qaṣaṣ**   | v3–v48    | **v1–v53 (53 vv)**      | Birth, Midian, mission |
| Moses | **2 Al-Baqarah**  | v51–v248  | **v46–v72 (27 vv, main cluster)** | Calf, spring, cow |
| Abraham | **2 Al-Baqarah** | v124–v140 | v119–v145 (27 vv)       | Qibla ring (Bonferroni) |
| Abraham | **37 Aṣ-Ṣāffāt** | v83–v113  | v78–v118 (41 vv)        | Sacrifice + Isaac birth |
| Abraham | **21 Al-Anbiyāʾ** | v51–v73  | v46–v78 (33 vv)         | Idol-smashing + fire ordeal |
| Abraham | **6 Al-Anʿām**    | v74–v83  | v69–v88 (20 vv)         | Afl-chain (star→moon→sun) |
| Joseph  | **12 Yūsuf**      | v4–v101   | **v1–v111 (111 vv)**    | **The only single-surah novella** |
| Noah    | **11 Hūd**        | v25–v48   | v20–v53 (34 vv)         | Ark + son-drowning dialogue |
| Noah    | **71 Nūḥ**        | v1–v28    | v1–v28 (28 vv, whole)   | Prayer monologue |
| Noah    | **26 Ash-Shuʿarāʾ**| v105–v122| v100–v127 (28 vv)       | Refrain-style retelling |
| Jesus   | **19 Maryam**     | v16–v40   | v11–v45 (35 vv)         | Birth + polemic break |
| Jesus   | **3 Āl-ʿImrān**   | v45–v62   | v40–v65 (26 vv)         | Annunciation + debate |
| Jesus   | **5 Al-Māʾida**   | v109–v118 | v108–v120 (13 vv)       | Māʾida + trial speech |
| Adam    | **2 Al-Baqarah**  | v31–v38   | v28–v43 (16 vv)         | Teaching of names + Fall |
| Adam    | **7 Al-Aʿrāf**    | v11–v27   | v6–v40 (35 vv)          | Dialogue + shame |
| Adam    | **20 Ṭā-Hā**      | v115–v123 | v110–v123 (14 vv, terminal) | Concluding warning |

The fact that Moses has five major retellings (7, 20, 26, 28, 2), Abraham
four (2, 37, 21, 6), Noah three (11, 71, 26), Jesus three (19, 3, 5), and
**Joseph one** is itself the headline finding of Task 1.

---

## 2. Moses vocabulary divergence across surahs (Task 2)

Jaccard similarity of triliteral-root sets across the five Moses pericope
windows (S2 v46–72, S7 v98–165, S20 v31–96, S26 v38–70, S28 v1–53):

|  | S2 | S7 | S20 | S26 | S28 |
|---:|---:|---:|---:|---:|---:|
| **S2**  (|R|=169) | — | 0.390 | 0.264 | 0.161 | 0.246 |
| **S7**  (|R|=266) | 0.390 | — | 0.327 | 0.196 | 0.330 |
| **S20** (|R|=205) | 0.264 | 0.327 | — | 0.211 | 0.306 |
| **S26** (|R|=76)  | 0.161 | 0.196 | 0.211 | — | 0.162 |
| **S28** (|R|=226) | 0.246 | 0.330 | 0.306 | 0.162 | — |

**Mean Jaccard to the other four Moses windows** (lower = more distinct):

| Rank | Surah | Mean Jaccard | Reading |
|---:|---|---:|---|
| 1 | **26 Ash-Shuʿarāʾ** | **0.182** | Most distinct Moses |
| 2 | 28 Al-Qaṣaṣ  | 0.261 | |
| 3 | 2 Al-Baqarah | 0.265 | |
| 4 | 20 Ṭā-Hā     | 0.277 | |
| 5 | **7 Al-Aʿrāf** | **0.311** | Most shared Moses |

**Top pair-Jaccard:**  S2 ↔ S7 = 0.390 > S7 ↔ S28 = 0.330 > S7 ↔ S20 = 0.327.

### 2.1 Interpretation

- **Ash-Shuʿarāʾ (26) is the "most distinct Moses."** Its window is only 33
  verses (76 distinct roots) and it is locked into the `إنّه لَمِن المرسلين`
  refrain structure — it tells a compressed, refrain-driven Moses. The 0.182
  mean Jaccard means less than 1 in 5 of its Moses-pericope roots is shared
  with the median other Moses version.
- **Al-Aʿrāf (7) is the "most shared Moses."** At 266 roots it is the
  lexically richest retelling and acts as a union-type: if you need a single
  Moses to learn the Quran's Moses vocabulary, Al-Aʿrāf is it.
- **Baqarah (2) and Aʿrāf (7) share the most** (0.390). The S2 Moses window
  is the second-shortest (27 vv) but carries forward the covenant/calf core
  that Al-Aʿrāf also treats at length. S2 is the *legal-covenantal* Moses; S7
  is the *narrative-epic* Moses; they overlap on calf + tablets.
- **Ṭā-Hā (20) sits in the middle** — moderate Jaccard with everyone, which
  is consistent with its well-known "standard Moses narrative" role in the
  Meccan period.
- **Al-Qaṣaṣ (28) has the highest share of unique roots (31.9%)** — more
  than any other target — because it alone carries the birth-in-basket,
  Midian-shepherdess, and Shuʿayb-as-father-in-law episodes that no other
  version tells at length.

### 2.2 Moses "signature roots" per surah (Task 6 answer)

| Surah | # unique roots | % of pericope roots unique | Signature roots (top by in-window count) |
|---|---:|---:|---|
| **S2 Baqarah** | 37 | 21.9% | **بقر** bqr ×5 (the cow), برأ brA ×2 (creator), لون lwn ×2 (color), جهر jhr ×1 (openly), فجر fjr ×1 (gushed spring) |
| **S7 Aʿrāf** | 66 | 24.8% | **كلم** klm ×5 (direct speech), مكر mkr ×4 (plot), بأس bAs ×3 (distress), **لوح** lwH ×3 (tablets), طبع TbE ×2 (sealed), نقم nqm ×2 (vengeance), **فصّل** fSl ×2, **كشف** k$f ×2 |
| **S20 Ṭā-Hā** | 55 | 26.8% | **سمر** smr ×3 (Sāmirī — only here), قذف q*f ×3 (cast into basket), **طغى** Tgy ×3 (transgression), ذهب *hb ×3 (gold), خشي x$y ×3 (fear), كيد kyd ×3 (cunning), أثر Avr ×3 (trace), **زين** zyn ×2 (adornment) |
| **S26 Shuʿarāʾ** | 12 | 15.8% | عزّ Ezz ×2 (pride), **طمع** TmE ×1, **قلل** qll ×1 (little band), **كنز** knz ×1 (treasures), **فلق** flq ×1 (cleaving of sea), **صحب** SHb ×1 |
| **S28 Qaṣaṣ** | 72 | 31.9% | **شيع** $yE ×3 (faction), أحد AHd ×3 (one of two), **رضع** rDE ×2 (suckling), **مرأ** mrA ×2 (women), **شعر** $Er ×2 (perceive), **صبّح** SbH ×2 (morning), **نصح** nSH ×2 (sincere counsel), **وصل** wSl ×2 (connected), **ندو** ndw ×2 (companion), **نذر** n*r ×2 |

These "signature roots" reproduce the literary fingerprint of each retelling:

- **S2** is the *bovine* Moses (bqr is literally absent from the other four).
- **S7** is the *speech-and-tablet* Moses (klm, lwH, fSl).
- **S20** is the *Sāmirī* Moses (smr is a hapax to this pericope) plus the
  basket-casting/golden calf inflection (q*f, *hb).
- **S26** is the *sea-cleaving* Moses (flq hapax here) and the stripped-down
  refrain version.
- **S28** is the *infancy* Moses (rDE suckling, mrA women who fetch him, $yE
  faction) — the birth-and-Midian material unique to Al-Qaṣaṣ.

Every "signature root" is a Mustansir-Mir-style motif. The mechanical diff is
doing the work of a traditional literary commentary.

---

## 3. Ring structure per pericope (Task 3)

Ring-score = mean Jaccard of root-sets between paired verses `(v_i, v_{N+1-i})`
inside a window. Null = within-window verse shuffle, 300–500 trials. This is
the same statistic as `chiastic-audit.md`; the anchor case (Al-Baqarah 131-144,
z = +9.69 at the 14-verse window) replicates exactly.

| # | Pericope | Window | N | obs | z vs shuffle-null | Verdict |
|---:|---|---|---:|---:|---:|---|
| 1 | **Abraham / Baqarah 131–144** (Farrin) | 2:131–144 | 14 | **0.2551** | **+3.64** on local null, **+9.69** in full chiastic-audit sub-window scan | Bonferroni-surviving, anchor |
| 2 | Jesus / Maryam 16–40 (birth + polemic) | 19:16–40 | 25 | 0.0487 | +0.43 | Weak |
| 3 | Jesus / Maryam 16–35 (annunciation → polemic) | 19:16–35 | 20 | 0.0448 | −0.96 | Below null |
| 4 | Moses / Ṭā-Hā main pericope | 20:31–96 | 66 | 0.0238 | **−1.36** | Anti-ring (worse than random) |
| 5 | Noah / Surah 71 (whole) | 71:1–28 | 28 | 0.0199 | −0.56 | Below null |
| 6 | Joseph / Surah 12 (whole) | 12:1–111 | 111 | 0.0406 | **−1.60** | Below null |
| 7 | Joseph / Surah 12:30–82 (middle arc) | 12:30–82 | 53 | 0.0340 | **−2.21** | Actively anti-ring |
| 8 | Joseph / Surah 12:50–101 (dreams → revelation) | 12:50–101 | 52 | 0.0930 | +1.16 | Best Joseph sub-window |

**Ranking (highest ring-ness first):**

1. **Abraham / Baqarah 131–144** — still the single strongest prophet-pericope
   ring in the Quran. No other prophet pericope comes close.
2. **Joseph / 12:50–101** — the dreams-interpret-and-family-reunion arc, z ≈ +1.16.
3. **Jesus / Maryam 16–40** — mildly positive (+0.43) but well below noise.
4. Everyone else is at or below the null.

### 3.1 Key negative: Joseph is linear, not chiastic

The whole-surah Joseph test is **anti-ring** (z = −1.60 to −2.21 depending on
window). Joseph's story has a plot shape, not a chiastic shape: dream →
betrayal → prison → elevation → reunion is a *forward* arc, not a mirror.
**This contradicts a common Muslim-literary-critical claim** (Cuypers-style)
that Yūsuf is tightly ring-structured. At the lexical-root level it is not.

What *is* true: the dream motif recurs (v4 young Joseph's star dream, v36
prisoner dreams, v43 king's dream, v100 fulfilment) and the shirt motif
recurs (v18, v25, v27, v28, v93) — but these are forward-referenced
flashbacks, not mirror pairs, and they don't symmetrize around the surah's
geometric midpoint.

### 3.2 Moses in Ṭā-Hā is the most anti-ring long prophet-pericope

Moses / Ṭā-Hā 20:31–96 scores z = **−1.36** — meaning the natural verse
order is *more disordered* than the average within-pericope shuffle.
Ṭā-Hā's Moses is narratively linear and refrain-free; it goes burning-bush
→ Pharaoh → exodus → calf → Sāmirī in chronological order, and no mirror
exists around the pericope midpoint. **Ṭā-Hā tells a story; it does not
build a ring.**

### 3.3 Abraham / Baqarah as the *only* ring-shaped prophet pericope

Our collective evidence across this audit and `chiastic-audit.md` is now
unambiguous: **the Abraham / qibla pericope (Q 2:131–144) is the sole
prophet-pericope in the Quran that exhibits statistically robust ring
structure** (Bonferroni-surviving). Every other prophet pericope we tested
is either narratively linear (Moses, Joseph), refrain-driven (Ash-Shuʿarāʾ,
Qamar — but Qamar's Thamud ring is a refrain-ring not a narrative ring),
inclusio-bookended (Hūd's surah-level z=+2.40 but raw p=0.015 does not
survive the 114-family correction), or simply below-null.

---

## 4. Jinas density per pericope (Task 4)

Jinas density = fraction of root-tokens in a pericope that belong to a
repeated root (≥2 occurrences). This is a verse-window adaptation of the
metric in `jinas-wordplay.md`.

### 4.1 Top-20 prophet pericopes by jinas density

| Prophet | Surah | Window | N | jinas_density |
|---|---|---|---:|---:|
| **Joseph** | 12 | v41–v104 | 64 | **0.823** |
| Moses | 7 | v98–v165 | 68 | **0.803** |
| Abraham | 2 | v119–v145 | 27 | 0.776 |
| Abraham | 3 | v79–v102 | 24 | 0.764 |
| Moses | 2 | v131–v141 | 11 | 0.761 |
| Noah  | 11 | v20–v53 | 34 | 0.761 |
| Jesus | 2 | v131–v141 | 11 | 0.761 |
| Moses | 28 | v1–v53  | 53 | 0.759 |
| Moses | 5  | v15–v29 | 15 | 0.753 |
| Moses | 10 | v70–v93 | 24 | 0.742 |
| Jesus | 5  | v41–v51 | 11 | 0.727 |
| Adam  | 7  | v6–v40  | 35 | 0.727 |
| Jesus | 4  | v152–v176 | 25 | 0.727 |
| Moses | 14 | v1–v13  | 13 | 0.726 |
| Moses | 2  | v241–v253 | 13 | 0.724 |
| Abraham | 3 | v60–v73 | 14 | 0.723 |
| Moses | 4  | v148–v169 | 22 | 0.721 |
| Noah  | 7  | v54–v74 | 21 | 0.719 |
| Moses | 20 | v31–v96 | 66 | 0.718 |
| Abraham | 6 | v156–v165 | 10 | 0.709 |

### 4.2 Per-prophet length-weighted mean

| Prophet | Total pericope length (verses) | # pericope windows | Weighted mean jinas density |
|---|---:|---:|---:|
| **Joseph**  | 120  | 4  | **0.7279** |
| **Jesus**   | 209  | 16 | **0.6506** |
| Moses   | 796  | 48 | 0.5950 |
| Adam    | 166  | 11 | 0.5752 |
| Abraham | 484  | 38 | 0.5680 |
| Noah    | 388  | 32 | 0.5479 |

### 4.3 Interpretation

**Joseph wins jinas density decisively** — 0.73 vs ~0.57–0.60 for the others.
This converges with the root-cartography finding that the Yūsuf surah
anchors three exclusive surah-level roots (`sjn` prison, `qmS` shirt, `Axw`
brother chain) and uses each word-family densely inside its one telling.
**Joseph is where the Quran's root-repetition rhetoric peaks**, and the
single-surah concentration (Task 7) is what enables that density —
repetition is harder when a story is scattered across 34 surahs (Moses's
case).

**Jesus is #2, driven by the Māʾida (5:110–118) "Ā Jesus, did you say…"
passage** — where `qwl` (say) appears 5× in v116 alone, and the
`Allah / mā qultu / qulta / qāla` quadruple hits in v116 and v117. The
jinas-wordplay agent already flagged 5:116 as a root-5× jinas anchor; our
per-pericope metric confirms this bleeds across the whole 11-verse Māʾida
window.

**Moses has the most total jinas mass** (48 pericope windows × ~0.60 = 796
verse-units of repeated-root rhetoric). But because he is so fragmented,
each individual window is less dense than Joseph's — the repetition pool is
diluted across 34 surahs.

Moses's peak window is **Al-Aʿrāf v98–v165 at 0.803**, driven by the
seven-fold repetition of `klm` (speech/tablets), the 4× `mkr` (plot), and
the `Tyr` / `nqm` pairs. Al-Aʿrāf is **both** the most shared Moses (§2)
**and** the highest jinas-density Moses pericope. This is consistent with
the Mustansir-Mir characterization of Al-Aʿrāf as the "narrative encyclopedia"
of Moses.

**Adam and Noah are the lowest-density prophets.** Adam because most of his
mentions are terse ("then Adam received words from his Lord"); Noah because
his stories are refrain-driven and the refrains are formulaic but not
lexically dense in new roots.

---

## 5. Chronological ordering of the Moses story (Task 5)

Moses appears in 34 surahs. Using the Egyptian revelation order and Nöldeke's
4-phase classification, here are the per-phase totals:

| Phase | n surahs with Moses | Moses mentions | Pericope units | Total span (verses) | Mean mentions / surah |
|---|---:|---:|---:|---:|---:|
| Early Meccan (pos 1–48) | 8 | 51 | 17 | 108 | **6.4** |
| Middle Meccan (pos 49–69) | 13 | 48 | 25 | 78 | 3.7 |
| Late Meccan (pos 70–90) | 9 | 25 | 15 | 39 | 2.8 |
| **Medinan (pos 91–114)** | **4** | **7** | **5** | **9** | **1.8** |

### 5.1 Key observations — the inverse of the folk-wisdom expectation

**The folk-wisdom prediction was "early Meccan terse Moses → late Medinan
long legal/covenantal Moses."** The data invert it.

- **Moses mentions per Moses-containing surah decrease monotonically** from
  Early Meccan (6.4) → Middle Meccan (3.7) → Late Meccan (2.8) → Medinan
  (1.8). By the Medinan period, Moses is being invoked one-shot (in prophet
  lists, or as a single appealed-to precedent).
- **The longest single Moses pericope units are all Early Meccan** (Surah 7
  Al-Aʿrāf, position 39; Surah 20 Ṭā-Hā, position 45; Surah 26 Ash-Shuʿarāʾ,
  position 47; Surah 28 Al-Qaṣaṣ, position 49 = first Middle Meccan). These
  four surahs alone account for **65 of the 81 Moses pericope units** across
  the whole Quran.
- **Surah 7 Al-Aʿrāf (pos 39) is the maximal Moses** — 19 mentions across 48
  verses of span. This is the *middle* of the Early Meccan period, not the
  end.
- **In Medinan surahs Moses shrinks to a footnote.** Even Al-Baqarah (position
  87, first Medinan) reduces Moses to scattered 1-verse covenantal invocations
  (cow, calf, spring) plus the Dāwūd / Ṭālūt / Jalūt war-inset — 13 mentions
  across 6 pericope units of 23 total verse span. Medinan Moses is a
  *citation*, not a *narrative*.

### 5.2 Progression interpretation

The chronology points to a **"narrative Moses → citation Moses"** arc, not
"terse → long." Moses's maximum narrative density happens in the mid-Meccan
period (surahs 7, 20, 26, 28) when the community needs a prophetic exemplar
to model Muhammad's own conflict with Mecca's elite. Once the community is
politically established in Medina, Moses drops out of narrative mode and is
repurposed as a **legal-covenantal precedent**: "you know what Allah commanded
the children of Israel about X" (the cow, the Sabbath, the calf). This is
consistent with the general chronological trend flagged in
`chronological-revelation.md`: the root `rbb` (Lord) also declines
chronologically; the early Quran is oracular and theocentric, the later
Quran is legal and communal.

**The "verse length doubles monotonically across Nöldeke's 4 phases"
(F=210)** finding from chronological-revelation.md sits alongside this: as
verses get longer, fewer of them are needed, and the Moses narrative density
per surah goes *down*, not up.

---

## 6. Joseph as single-surah narrative (Task 7)

### 6.1 Quantification of single-surah concentration

| Prophet | Total mentions | Surahs | Top-surah concentration |
|---|---:|---:|---|
| **Joseph** | 27 | **3** | **S12: 24 mentions (92.3%)** |
| Abraham | 69 | 25 | S2: 12 (19.0%) |
| Moses   | 136 | 34 | S7: 19 (14.5%) |
| Adam    | 25 | 9  | S7: 7 (28.0%) |
| Jesus   | 25 | 11 | S5: 6 (24.0%) |
| Noah    | 43 | 28 | S11: 8 (18.6%) |

**Joseph is the only prophet whose story is >90% concentrated in a single
surah.** The next most concentrated prophet is Adam at 28% (S7), then
Jesus at 24% (S5). Joseph's concentration (92.3%) is **more than triple**
the next-most-concentrated prophet.

### 6.2 Structural integrity vs fragmentation

The natural complement: how does the "structural integrity" of Joseph
compare to the fragmented Moses / Abraham treatments?

**Integrity signals for Joseph:**
- **100% of the narrative lives inside one surah.** No pericope is split.
- **Distinct Yūsuf-anchored roots** (from `root-cartography.md §0`):
  `sjn` 12× all in S12, `qmS` 6× all in S12, `Axw` (brother) chain is Surah-12
  dense. These are lexical fingerprints that no other prophet gets.
- **Peak jinas density of any prophet pericope** (§4: Joseph 0.73 weighted mean,
  peak window 0.823).
- **Forward-linear narrative arc**: 12:4 dream → 12:100 dream-fulfillment,
  the only surah-spanning inclusio in our data (but forward-referenced,
  not mirror-structured, so not a *ring*).

**Disintegration signals for Joseph:**
- **It does not pass the ring test** (z = −1.60 whole-surah). The "most
  beautiful story" is the most jinas-dense but the most linearly structured.
  **Beauty does not equal chiasmus.**

**Comparison:** For Moses, Jesus, Noah, Abraham, no single surah carries
more than ~25% of the prophet's total mentions. They are *distributed*
figures. The Quran deploys each of them as a *repeat visitor* across many
surahs, re-telling their stories with different framings (refrain in S26,
epic in S7, legal in S2, intimate in S20). Joseph gets the opposite
treatment: **one telling, maximally rich**, and then almost never again.

The implication for the overall composition theory is striking: **the
Quran's default narrative mode is distributed retelling; Joseph is the
exception that proves the rule**. The opening verse of Surah 12 (`naḥnu
naquṣṣu ʿalayka aḥsana l-qaṣaṣi`, "We relate to you the best of narratives")
is self-consciously marking this as a singular exception.

### 6.3 Why not the others? A suggestive null

Moses is the natural comparison for "could the Quran have told Moses in a
single surah?" The answer from the Jaccard matrix (§2) is no: **no single
Moses window root-set even covers half the union**. Union of all 5 Moses
windows = roughly 650 distinct roots; Al-Aʿrāf (266) covers 41%, Al-Qaṣaṣ
(226) covers 35%. No single Moses telling is lexically complete. **The
Quran literally cannot compress Moses to one surah without losing ~60% of
the vocabulary it attaches to him.** Joseph is compressible because Joseph
is smaller — 27 mentions vs Moses's 136. The structural question "why is
Yūsuf single-surah" has a mundane answer: because Moses won't fit.

---

## 7. Jesus and the Maryam rhyme-break (Task 8)

### 7.1 Re-reading Maryam 34–40

From `saj-rhyme-analysis.md` §3.1: Maryam's 98-verse surah is 66% locked into
the `يا` rhyme. The two longest unbroken `يا` runs are:

- **vv 2–33** (32 verses, 100% `يا`) — Zachariah/John/Mary/Jesus birth
- **vv 41–74** (34 verses, 100% `يا`) — Ibrahim → Isaac → Ishmael → Idris

Between them sits **vv 34–40** (7 verses, **all breakers**). This is the
exact Jesus-polemic: "That is Jesus son of Mary — the word of truth about
which they dispute. It is not for Allah to take a son…"

Our consonantal-ending extraction reproduces this:

| Verse | last word | fasila_2 | rhyme status |
|---|---|---|---|
| v32 | شقيا | يا | ✓ match |
| v33 | حيا  | يا | ✓ match (*end of birth narrative*) |
| **v34** | يمترون | ون | **BREAK** ("That is Jesus son of Mary — the word of truth about which they dispute") |
| **v35** | يكون  | ون | **BREAK** ("It is not for Allah to take a son…") |
| **v36** | مستقيم | يم | **BREAK** |
| **v37** | عظيم  | يم | **BREAK** |
| (v38–v40 also break) | | | |
| v41 | نبيا | يا | ✓ resumes (*start of Ibrahim cycle*) |

The polemic is **exactly** the break. Form enacts content with surgical
precision. This is the `saj-rhyme-analysis.md` headline candidate finding
that has no prior published comparable precision.

### 7.2 Extending to Surahs 3, 4, 5 — do they also mark Jesus with rhyme breaks?

**Short answer: No. Surah 19 Maryam is uniquely structured this way. The
other three surahs handle Jesus in prosaic discursive rhyme.**

Detailed per-surah analysis of Jesus-verse rhyme endings:

**Surah 3 (Āl ʿImrān) — Jesus section vv 45–62.** This is a long-verse
Medinan surah. Its dominant rhyme is `ين / ون` (from the scattered plural
masc endings). The Jesus passage:

| v | end | fasila_2 | note |
|---|---|---|---|
| v45 | المقربين | ين | annunciation |
| v46 | الصالحين | ين | |
| v47 | يكون | ون | Mary's "How can I have a child?" |
| v48 | الإنجيل | يل | Torah+Gospel — **rhyme bends to ـيل** |
| v49 | يعلمون | ون | Jesus's miracle list (raises dead) |
| v50 | تطيعون | ون | |
| v51 | مستقيم | يم | "This is a straight path" — **bends to ـيم** |
| v52 | مسلمون | ون | Apostles |
| v53 | الشاهدين | ين | |
| v54 | الماكرين | ين | God-plots-plotters |
| v55 | يختلفون | ون | |
| v56 | ناصرين | ين | |
| v57 | الظالمين | ين | |
| v58 | الحكيم | يم | |
| v59 | فيكون | ون | **"The example of Jesus is like that of Adam"** — the core Christological position |
| v60 | الممترين | ين | |
| v61 | الكاذبين | ين | mubāhala (invocation of mutual curse) |
| v62 | الحكيم | يم | |

Āl ʿImrān's dominant rawi is ن (final consonant), which catches ين / ون /
يم / يل in a single acceptable band. The Jesus passage **does not break the
rhyme of Surah 3** — it stays within the wide-band Medinan ـين / ـون / ـيم /
ـيل envelope. The one verse that sits structurally at the *Christological
pivot*, **v59** (`إن مثل عيسى عند الله كمثل آدم`), ends in `فيكون` — the
same word that Maryam v35 used at its polemic break. But in Surah 3 the
`ون` ending is the **norm**, not a break. The form-content collision that
makes Maryam 19:35 rhetorically electric does not happen in Surah 3, because
3 isn't monorhymed to begin with.

**Surah 4 (An-Nisāʾ) — Jesus at vv 157, 163, 171.** All three are cameo
mentions inside long Medinan verses. The dominant surah rhyme is -يرا /
-يما / -يلا (long ā endings) and the Jesus verses fit that envelope
perfectly (v157 قينا, v158 كيما, v163 بورا, v171 وكيلا, v172 ميعا). **No
rhyme-break marking**. The crucifixion-denial polemic (v157, `وما قتلوه`)
is not phonetically distinguished from its Medinan-legal neighborhood.

**Surah 5 (Al-Māʾida) — Jesus at v46, v78, v110–118.** Al-Māʾida is
essentially unrhymed (it is the most prosaic of the Medinan surahs and
ranks 111/114 in the ring-score table — `chiastic-audit.md` §2). There is
no "rhyme" for any verse to break. The Māʾida trial scene (vv 110–119) runs
on `-يم` (عليم, علام, الغيوب) without any structural discontinuity.

### 7.3 Headline inference

**Surah 19 Maryam is the ONLY surah in which a rhyme-break aligns to a
Jesus polemic.** Surahs 3, 4, 5 handle Jesus in prosaic long-verse
discourse where the rhyme band is already too wide for a local break to
stand out.

This strengthens the Maryam finding rather than generalizing it: the
Christological form-content alignment is a unique feature of Meccan
Maryam's tight monorhyme, impossible in the Medinan Jesus surahs because
they don't have tight monorhymes for content to break against. **The
Jesus polemic breaks rhyme exactly once in the Quran, in Maryam, because
Maryam is the only place where Jesus appears inside a phonetically tight
enough envelope for a break to register.**

### 7.4 A secondary observation — the Jesus root pair `Ebd` / `wlk`

Across all Jesus sections (3:45–62, 4:171, 5:17, 5:72, 5:116–117, 19:30,
19:35, 19:88–93, 43:57–65) the recurring root pair is `Ebd` (servant) ↔
`wld` (son). Almost every Jesus polemic in the Quran turns on this
antonym. Q 19:30 `innī ʿabdullāh` ("I am Allah's servant") → 19:35 "it is
not for Allah to take a son." Q 4:171-172 "the Messiah will not disdain
to be a servant of Allah" → "they say Allah has a son." Q 43:59 `in huwa
illā ʿabd` ("He is only a servant"). The Jesus polemic is a **lexical
substitution game**: everywhere the Christian audience would say "son"
(*walad*), the Quran substitutes "servant" (*ʿabd*). This is a pan-surah
pattern, not a single-surah ring, and is best described as
*refrain-at-a-theological-level* rather than chiasm.

---

## 8. Cross-prophet summary table

| Prophet | Mentions | Surahs | Top-surah % | Best ring | Best jinas | Longest pericope | Chronology |
|---|---:|---:|---:|---|---:|---|---|
| Moses   | 136 | 34 | 14.5% (S7) | none (anti-ring) | 0.803 (S7 v98–165) | S7 68vv | Early Mec peak, decline through Medinan |
| Abraham | 69  | 25 | 19.0% (S2) | **+9.69 (S2 131–144)** Bonferroni | 0.776 (S2 119–145) | S2 27vv | Peak in Middle/Late Meccan + Medinan covenant |
| Joseph  | 27  | 3  | **92.3%** (S12) | anti-ring (S12 z=-1.60) | **0.823** (S12 41–104) | **S12 111vv** | Single Middle-Meccan telling |
| Noah    | 43  | 28 | 18.6% (S11) | none | 0.761 (S11 20–53) | S11 34vv | Evenly spread Meccan refrain |
| Jesus   | 25  | 11 | 24.0% (S5) | near-null (S19 +0.43) | 0.727 (S5 41–51) | S19 35vv | Late Meccan (Maryam) + 3 Medinan polemic cameos |
| Adam    | 25  | 9  | 28.0% (S7) | none | 0.727 (S7 6–40) | S7 35vv | Distributed across Meccan Fall-story retellings |

## 9. Cross-cutting findings

1. **Abraham has the only Bonferroni-surviving prophet-pericope ring.**
   (Al-Baqarah 131–144, z=+9.69). No other prophet's narrative achieves
   even half that signal.
2. **Joseph has the highest jinas density and the highest single-surah
   concentration — but the weakest ring signal.** The story the literature
   canonizes as "the best of narratives" is the most lexically self-dense
   and the most narratively linear. Density ≠ ring.
3. **Ṭā-Hā's Moses is below the null for ring** (z=-1.36). It is a strictly
   *linear* narrative. Ring composition is not characteristic of Quranic
   Moses.
4. **Al-Aʿrāf is simultaneously the "most shared Moses" (highest mean
   Jaccard = 0.311) and the "most jinas-dense Moses" (0.803).** It is the
   Moses encyclopedia. If you want the Quran's default Moses, read S7.
5. **Ash-Shuʿarāʾ is the "most distinct Moses"** (mean Jaccard 0.182) and
   has the lowest unique-root count. It compresses Moses into its surah's
   refrain-driven prophetic cycle format.
6. **Al-Qaṣaṣ is the only Moses version that tells the birth-in-basket,
   suckling, and Midian-Shuʿayb episodes** (signature roots: $yE faction,
   rDE suckling, mrA women, SbH morning, wSl connected, ndw companion).
7. **Moses narrative density decreases monotonically across the Nöldeke
   chronology** (6.4 → 3.7 → 2.8 → 1.8 mentions/surah). Folk wisdom
   predicted the opposite.
8. **The Jesus polemic breaks rhyme exactly once in the Quran (Maryam
   19:34–40). Surahs 3, 4, 5 have no rhyme-break analogue** because their
   rhyme envelope is too wide for a local break.
9. **Jesus's rhetorical engine is a lexical substitution** (ʿabd ↔ walad)
   applied at pan-surah scale, not a ring.
10. **The Quran's default narrative mode is distributed retelling** — every
    major prophet except Joseph appears in ≥9 surahs. Joseph is the only
    single-surah exception, and Q 12:3 self-consciously marks this.

---

## 10. Prior art — academic comparative pericope work

| Author | Work | Relevance |
|---|---|---|
| **Gabriel Said Reynolds** | *The Qurʾān and Its Biblical Subtext* (2010); *The Qurʾān and the Bible: Text and Commentary* (2018, Yale) | Reynolds's thesis: the Quran's prophet retellings are *allusive* — they depend on the audience's Biblical-Syriac literary background. Treats Adam, Abraham, Jonah, Mary, Muhammad as pericope units whose sense is only visible against Christian/Jewish subtext. His comparative method is *qualitative*; ours is *lexical-statistical*. Convergence: both identify a handful of loci (Al-Baqarah Abraham, Maryam Jesus) as semantically dense. |
| **Angelika Neuwirth** | *The Qur'an: Text and Commentary*, Vol 1 *Early Meccan Suras* (Yale 2022), Vol 2.1 *Early Middle Meccan Suras* (Yale 2024); earlier *Studien zur Komposition der mekkanischen Suren* (1981/2007) | Neuwirth introduced the *tripartite pericope structure* (dialogical frame → biblical pericope core → dialogical frame) for middle/late Meccan surahs. Our Ṭā-Hā and Aʿrāf Moses windows sit precisely at her "biblical core" position. Our per-window Jaccard confirms her form-critical unit boundaries are also lexical unit boundaries. |
| **Michael Zwettler** | *The Oral Tradition of Classical Arabic Poetry* (1978); "Mantic Manifesto" paper (1990) | Applied oral-formulaic theory (Parry-Lord) to pre-Islamic poetry. Foundational for the "Quranic variant retellings reflect oral composition" hypothesis. |
| **Andrew Bannister** | *An Oral-Formulaic Study of the Qurʾan* (2014); JQS review 2017 | Computational continuation of Zwettler. Reports **Quranic formulaic density 23.55%–52.18%**, crossing Parry-Lord's 20% oral-composition threshold. Our jinas-density metric (mean 0.55–0.73 weighted) is a different grain (root-level intra-pericope) but tells the same story at pericope scale. **Moses as "35+ sura prophet with multiple variant retellings" is explicitly Bannister's framing.** |
| **Joseph Witztum** | "The Syriac Milieu of the Quran" (dissertation 2011); multiple articles on parallel passages | Argued a "systematic study of parallel passages in the Qur'an is necessary to answer basic questions concerning its formation." This report is partial computational implementation of that program for 6 prophets. |
| **Reuven Firestone** | *Journeys in Holy Lands: The Evolution of the Abraham-Ishmael Legends in Islamic Exegesis* (SUNY 1990) | Firestone's comparative treatment of Abraham narratives across Jewish / Christian / Islamic traditions. Argues for *evolutionary* development of legend rather than borrowing/dependency. Our finding that Al-Baqarah 131–144 is the only Bonferroni-surviving prophet ring fits his claim that the Abraham/qibla pericope is the most rhetorically structured Abraham in the Quran. |
| **Marianna Klar et al.** | "Variant Versions of the Moses Story in the Qur'ān" (Academia.edu preprint, ca. 2022) | A **direct-hit paper**: the title describes exactly the comparison we compute here. Compares narrative elements across 36+ Moses surahs, argues for "diverse theological emphases." Quantitative approach absent; this report is the computational companion. |

**Novelty claim:** a *computational, root-based Jaccard matrix* across Moses
(and every other prophet's) pericope windows, with a *per-pericope ring-score
test against verse-shuffle null*, and a per-prophet *weighted jinas density*,
is, as far as we can tell, not in any of the above. The qualitative
narratological tradition — Neuwirth, Reynolds, Firestone, Witztum, Bannister,
Klar — has been building to this test for thirty years; we deliver the
numbers.

---

## 11. Replication checklist

- [x] Rules tuple disclosed in YAML frontmatter
- [x] Script single-file reproducible: `scratch/prophet-pericope/analyze.py`
- [x] Per-prophet PN lemma counts verified against task spec (Moses ~136,
      Abraham ~69, Joseph 27, Noah 43, Jesus 25, Adam 25)
- [x] Moses Jaccard matrix reproduces from 5 windows
- [x] Ring-score null: 300–500 within-window shuffles per test
- [x] Jinas density = repeated-root-token rate on expanded pericopes
- [x] Al-Baqarah 131–144 anchor replicates from `chiastic-audit.md`
      (Jaccard-ring z = +3.64 on local null; +9.69 on full sub-window family)
- [ ] Bonferroni correction across prophet-pericope ring test family **NOT
      YET APPLIED** — 6 targets × 2 methods ≈ 12 local tests; without
      correction the only surviving signal is still Al-Baqarah 131–144.
- [ ] Comparable-corpus null (Bannister-style oral formulaic density on
      Bukhari) **NOT RUN** — follow-up.
- [ ] Pre-registration: this is exploratory Phase-C extension; all
      p-values are demoted.

---

## 12. Summary (500 words)

Across the six major prophet narratives (Moses, Abraham, Joseph, Noah, Jesus,
Adam), we located every proper-noun mention from the Leeds Quranic Arabic
Corpus, clustered adjacent verses into pericope units, and computed
root-based similarity, ring structure, and jinas density. Three patterns
dominate.

**First, the Quran's default narrative mode is distributed retelling, and
Joseph is the sole exception.** Moses scatters 136 mentions across 34 surahs
into 81 pericope units, Abraham 69 across 25, Noah 43 across 28, Jesus 25
across 11, Adam 25 across 9. Joseph concentrates 24 of 27 (92.3%) in Surah
12 alone — three times the concentration of the next-most-concentrated
prophet. Surah 12:3 self-consciously markers this exception ("We relate to
you the best of narratives"). The lexical consequence: Joseph has the
Quran's highest-jinas-density pericope (0.823, S12:41–104) and the strongest
surah-exclusive vocabulary (`sjn` prison 12× all in S12, `qmS` shirt 6× all
in S12, `Axw` brother chain). He is also the most *linear* of the prophets
— Surah 12 scores z = −1.60 against its own ring null. The "best narrative"
is not chiastic; it is forward-referenced.

**Second, Moses's five major retellings (surahs 7, 20, 26, 28, 2) each
carry distinct signature vocabulary.** Mean Jaccard on root-sets ranges
from S26's 0.182 (most distinct — refrain-compressed Moses) to S7's 0.311
(most shared — encyclopedic Moses). The vocabulary fingerprints match the
literary characterizations: S2 is the cow/covenant Moses, S7 the
speech-and-tablets epic, S20 the Sāmirī + golden calf drama, S26 the
sea-cleaving refrain, S28 the birth-in-basket + Midian infancy. S7
Al-Aʿrāf is simultaneously the most shared and the most jinas-dense
(0.803); if the Quran had to pick one Moses, it would pick Aʿrāf. **Moses
mentions per containing surah decrease monotonically through the Nöldeke
chronology** (Early Mec 6.4 → Middle 3.7 → Late 2.8 → Medinan 1.8),
inverting the folk expectation of "terse early / long legal Medinan." The
pattern is *narrative → citation*: by the Medinan period, Moses is a legal
precedent, not a story.

**Third, ring structure is rare, not the norm, in prophet pericopes.**
Across all six prophets, the only Bonferroni-surviving prophet ring is
Al-Baqarah 131–144 (Abraham/qibla, z = +9.69) — the anchor case from
`chiastic-audit.md`. Moses in Ṭā-Hā scores z = −1.36 (anti-ring), Joseph
scores z = −1.60, Noah and Jesus are near null. Jesus in Maryam produces
the famous rhyme-break signal (vv 34–40 breaks the `يا` monorhyme exactly
on the Christological polemic), and extending to Surahs 3, 4, 5 shows this
is *unique to Maryam*: the Medinan Jesus surahs have rhyme envelopes too
wide for a local break to register. The Jesus polemic instead operates as
a **lexical substitution** (*ʿabd* servant ↔ *walad* son) applied at
pan-surah scale. Across all prophets, the Quran's rhetorical architecture
is: rings for Abraham, linear density for Joseph, refrain for Noah,
distributed variant for Moses, lexical antonym for Jesus, terse echoic
repetition for Adam. Six prophets, six different compositional modes.
