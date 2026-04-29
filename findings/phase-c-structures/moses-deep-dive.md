---
phase: C
finding_id: phase-c-moses-deep-dive-run-1
date: 2026-04-12
agent: moses-deep-reader
status: reported
claim_class: literary-structural / comparative-narratology / lexical-cartography
rules:
  orthography: no-tashkeel (for Jaccard, ring, jinas); QAC PN lemma for proper-noun matching
  word_definition: lemma + triliteral root (Leeds QAC v0.4)
  letter_definition: not applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  null_model:
    - chiastic 1.2-verse-shuffle-within-window (500 trials per pericope, seed = surah*10000 + start_verse)
  similarity: Jaccard of triliteral-root sets per verse-window
  pericope_clustering: consecutive Moses-mention verses gap ≤ 5; per-surah "Moses span" = min..max Moses verse padded ±2
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  text: quran-text/quran-no-tashkeel.json
  translation: data/translations/en.sahih.txt
  revelation_order: data/revelation-order.csv (Egyptian + Nöldeke)
prior_findings:
  - findings/phase-b-hypotheses/word-pair-symmetry.md   # 136/136 anchor
  - findings/phase-b-hypotheses/root-cartography.md
  - findings/phase-c-structures/chiastic-audit.md
  - findings/phase-b-hypotheses/jinas-wordplay.md
  - findings/phase-b-hypotheses/chronological-revelation.md
  - findings/phase-c-structures/prophet-pericope-comparison.md  # general 6-prophet survey
scripts:
  - scratch/moses/moses_deep.py
  - scratch/moses/moses_structures.py
machine_results:
  - scratch/moses/moses_summary.json
  - scratch/moses/run1.log
  - scratch/moses/run2.log
---

# Moses (Mūsā, موسى) — A Deep Computational Reading

> **Lemma:** `muwsaY``  **POS:** PN  **Tokens:** 136  **Distinct verses:** 131  **Surahs:** 34
>
> Moses is, by lemma count, the most-named individual human in the Quran. The lemma
> `muwsaY`` (Mūsā) appears 136 times — more than Abraham (69), Noah (43), Joseph
> (27), Jesus (25), Adam (25), or even the post-Hijra entries of "Muhammad" (4).
> No other prophet's name approaches the same density. The narrative is told and
> re-told from the very earliest Meccan layer (one-line allusions in 87, 79, 53,
> 51) to the longest Medinan covenant text (Al-Baqara). This document maps every
> Moses occurrence, computes the comparative vocabulary across the principal
> Moses-bearing surahs, identifies the roots that are most distinctively
> Moses-coded, examines the Pharaoh sub-distribution, runs structural metrics on
> Surah 18's Khidr pericope, compares the five tellings of the staff miracle,
> compares Ṭā-Hā (the longest Meccan Moses biography) to Al-Qaṣaṣ (the longest
> Medinan one), and traces the chronological growth of the Moses material across
> the revelation order.

---

## 1. The 136-token Moses inventory

The Leeds QAC v0.4 yields exactly **136 tokens** of `LEM:muwsaY`` with `POS:PN`,
distributed across **131 distinct verses** in **34 surahs**. The token total
matches the anchor in `word-pair-symmetry.md` line-for-line. Five verses contain
the name twice (e.g. 7:142 has both "Moses" and "Moses said"), accounting for
the 136 vs 131 gap.

### 1.1 Per-surah Moses density

| Mushaf | Surah | Tokens | Distinct verses | Period | Rev. pos |
|---:|---|---:|---:|---|---:|
| 7  | Al-Aʿrāf       | **21** | 19 | Late Meccan   | 39 |
| 28 | Al-Qaṣaṣ       | **18** | 17 | Late Meccan   | 49 |
| 20 | Ṭā-Hā          | **17** | 17 | Middle Meccan | 45 |
| 2  | Al-Baqarah     | **13** | 13 | Medinan       | 87 |
| 10 | Yūnus          |  8 |  8 | Late Meccan   | 51 |
| 26 | Ash-Shuʿarāʾ   |  8 |  8 | Middle Meccan | 47 |
| 40 | Ghāfir         |  5 |  5 | Late Meccan   | 60 |
| 4  | An-Nisāʾ       |  3 |  2 | Medinan       | 92 |
| 5  | Al-Māʾidah     |  3 |  3 | Medinan       | 112 |
| 6  | Al-Anʿām       |  3 |  3 | Late Meccan   | 55 |
| 11 | Hūd            |  3 |  3 | Late Meccan   | 52 |
| 14 | Ibrāhīm        |  3 |  3 | Late Meccan   | 72 |
| 17 | Al-Isrāʾ       |  3 |  2 | Middle Meccan | 50 |
| 27 | An-Naml        |  3 |  3 | Middle Meccan | 48 |
| 18 | Al-Kahf        |  2 |  2 | Middle Meccan | 69 |
| 23 | Al-Muʾminūn    |  2 |  2 | Middle Meccan | 74 |
| 33 | Al-Aḥzāb       |  2 |  2 | Medinan       | 90 |
| 37 | Aṣ-Ṣāffāt      |  2 |  2 | Middle Meccan | 56 |
| 46 | Al-Aḥqāf       |  2 |  2 | Late Meccan   | 66 |
| (15 surahs with 1 token each) |  | 15 |  |  |  |
| **Total** |  | **136** | **131** |  |  |

The first eight surahs account for **93/136 = 68%** of all Moses tokens. The
distribution is heavy-tailed but not concentrated: Moses spreads across 34 of
114 surahs, more than any other named figure.

### 1.2 The 62 pericope units (gap ≤ 5 clustering)

Clustering Moses-mention verses by adjacency (gap ≤ 5) within a surah yields
**62 pericope units**. The largest single contiguous Moses unit in the Quran
is **7:115-160 (17 mention-verses across 46 verses)**: the magicians' contest,
the calf, and the post-Sinai disciplinary cycle. Other major units:

| Surah | Range | Mentions | Topic |
|---:|---|---:|---|
| 28 | 3-20  | 7 | Birth and youth (unique to S28) |
| 28 | 29-48 | 9 | Burning bush, Pharaoh, Moses-Aaron mission |
| 20 | 57-70 | 5 | Magicians' contest |
| 20 | 83-91 | 4 | Calf episode |
| 10 | 75-88 | 8 | Pharaoh confrontation |
| 26 | 43-52 | 4 | Magicians' submission |
| 2  | 51-61 | 6 | Sinai-and-disobedience cycle |
| 40 | 23-27 | 3 | Pharaoh-and-Haman + believer's speech setup |

Compare with the 47 single-mention "telegraphic" pericopes scattered across
sūras 3, 4, 5, 6, 11, 14, 17, 19, 21, 22, 23, 25, 29, 32, 33, 41, 42, 43, 51,
53, 61, 79, 87 — most of these are list-of-prophets or appeal-to-Mosaic-scripture
formulae rather than narrative.

---

## 2. The Moses = ittabaʿa = 136 word-pair re-examined

`word-pair-symmetry.md` flagged Mūsā / ittabaʿa (`{t~abaEa`, "to follow") as
both having lemma count 136, with the framing "the children of Israel followed
(or didn't) Moses." The match is empirically verified — both lemmas hit
exactly 136 tokens. The deeper question is whether the symmetry has thematic
substance or is bookkeeping.

### 2.1 Co-occurrence audit

| Co-occurrence test | ittabaʿa tokens (of 136) | % |
|---|---:|---:|
| Same verse as Moses | **2** | 1.5% |
| Within ±5 verses of any Moses verse | 27 | 19.9% |
| Within ±10 verses of any Moses verse | 39 | 28.7% |
| In a surah that contains any Moses verse | 98 | 72.1% |

The two co-occurring verses are **7:142** and **18:66**:

- **7:142** — "Moses said to his brother Aaron: 'Take my place among my people,
  do right by them, **and do not follow** (*lā tattabiʿ*) the way of the
  corrupters.'" The only direct Moses-says-ittabaʿa is a *prohibition*. (The
  context is the 40 nights on Sinai during which the calf will be made.)
- **18:66** — "Moses said to him [Khidr]: 'May I follow you (*hal attabiʿuka*)
  on the condition that you teach me from what you have been taught of sound
  judgement?'" The only "Moses follows" verse in the corpus is Moses asking
  to follow Khidr — a striking inversion of the normal Israelite-following-Moses
  pattern, and the literary heart of the Khidr unit (§7).

### 2.2 Verdict

The 136/136 match is real but **the thematic claim ("Moses ↔ to follow") is
weak at the verse level**. Only ~2% of ittabaʿa tokens co-locate with Moses;
~20% are even close. ittabaʿa is a ubiquitous verb of religious adherence — it
appears in dozens of contexts (following the Messenger, following revelation,
following one's whim, following Satan, following the path, following the
ancestors, following truth). It is not Moses-special.

What is striking, however, is the **symbolic** alignment of the two verses
where Moses *does* meet ittabaʿa: both are **inversions** of the expected
follower pattern. In 7:142 Moses commands his brother *not to follow*; in
18:66 Moses himself *asks to follow*. Both are role-reversal moments. If the
136/136 count is a coincidence, the *placement* of the two co-occurrences in
the most rhetorically-loaded inversion verses is itself a (probably accidental)
literary echo.

This is consistent with the §5 honest-verdict in `word-pair-symmetry.md`: the
Quranic count distribution is heavy-tailed, matches at this rate are expected
by pigeonhole (the McKay denominator), and `muwsaY/{t~abaEa` is "real
(verified counts) and semantically suggestive" but "not statistically miraculous."
This dive doesn't change that.

---

## 3. Comparative vocabulary across the top-5 Moses surahs

For each of the five highest-Moses-density surahs (7, 20, 26, 28, 2) I extracted
the *Moses span* — the contiguous range from the first to the last Moses verse
in that surah, padded ±2 verses for context — and computed the set of triliteral
roots appearing in that span.

| Surah | Span | N verses | \|roots in span\| | \|roots in Moses-only verses\| |
|---:|---|---:|---:|---:|
| 7  | v101-v162 | 62  | 253 | 138 |
| 20 | v7-v93    | 87  | 232 | 67  |
| 26 | v8-v67    | 60  | 125 | 27  |
| 28 | v1-v78    | 78  | 282 | 127 |
| 2  | v49-v250  | 202 | 499 | 109 |

Two cuts: a **wide** Jaccard (over the entire span, including non-Moses framing
material) and a **narrow** Jaccard (only the verses that literally name Moses).

### 3.1 Jaccard matrix (wide span)

|         | S7    | S20   | S26   | S28   | S2    |
|---|---:|---:|---:|---:|---:|
| **S7**  | 1.000 | 0.314 | 0.286 | 0.344 | 0.365 |
| **S20** | 0.314 | 1.000 | 0.266 | 0.339 | 0.276 |
| **S26** | 0.286 | 0.266 | 1.000 | 0.245 | 0.184 |
| **S28** | 0.344 | 0.339 | 0.245 | 1.000 | 0.356 |
| **S2**  | 0.365 | 0.276 | 0.184 | 0.356 | 1.000 |

**Mean Jaccard to other Moses spans (lower = more distinct):**

| Surah | Mean J | Rank |
|---:|---:|---:|
| 26 (Shuʿarāʾ)  | **0.245** | most distinct |
| 20 (Ṭā-Hā)     | 0.299 | |
| 2  (Baqarah)   | 0.295 | |
| 28 (Qaṣaṣ)     | 0.321 | |
| 7  (Aʿrāf)     | **0.327** | most central |

### 3.2 Most-similar pair

**S2 ↔ S7 = 0.365 (highest)** — the two longest Moses-rich corridors share the
most vocabulary. This is despite one being late-Meccan narrative (S7) and the
other being Medinan covenant (S2). The shared vocabulary is dominated by
Israelite-history terms (covenant, calf, repentance, springs-from-rock,
Sabbath, the cow narrative). The Medinan re-telling in Al-Baqara is selective
but draws on the same root inventory.

**S2 ↔ S26 = 0.184 (lowest)** — Shuʿarāʾ is the outlier. Its Moses material
(vv 10-67) is embedded in a refrain-driven prophet sequence (Noah, Hud, Salih,
Lot, Shuʿayb) where each prophet's section closes with the same formulaic
refrain "indeed your Lord is the Mighty, the Merciful." The Moses section is
dominated by the magicians-of-Pharaoh contest and is *short on covenant
language* — no calf, no Sinai legislation, no springs, no quail.

### 3.3 Narrow Jaccard (Moses-only verses)

The pattern sharpens when restricted to verses literally containing the name:
S26's mean Jaccard collapses to 0.116 (lowest), confirming that **Shuʿarāʾ's
Moses-naming verses use vocabulary the other surahs don't share** — a
formula-driven retelling rather than a content-driven one.

### 3.4 Why S26 is the outlier

Surah 26 (Ash-Shuʿarāʾ) is the only top-Moses surah where Moses is one prophet
among many, slotted into a numerically-balanced sequence. The others are
Moses-driven: Ṭā-Hā opens with Moses (vv 9-98) and only later turns to Adam
(vv 116-127); Al-Qaṣaṣ literally announces "We recite to you from the news of
Moses and Pharaoh" (28:3); Al-Aʿrāf gives Moses the longest single-prophet
treatment in its prophet cycle (vv 103-162, 60 verses); Al-Baqara has Moses
as the central prophet of the Israelite covenant material. Shuʿarāʾ alone
treats Moses as an item on a list. The vocabulary divergence is the
mathematical signature of that narrative-status difference.

---

## 4. Moses signature vocabulary

For every triliteral root with ≥5 occurrences in the Quran, I computed
**fraction_in_Moses_span** = (occurrences inside any Moses span) / total. The
top 33 roots scoring ≥0.50 form Moses's lexical fingerprint.

### 4.1 100% Moses-coded roots

| Root | Count | Gloss | Notes |
|---|---:|---|---|
| `ESw`  | 12 | "staff" (ʿaṣā) | All 12 are Moses's staff. The single most exclusively Moses-coded root in the Quran. |
| `$Tr`  | 5  | "shore / coast / direction" (in 2:144 the qibla, but the Moses uses are about the river) | |
| `sbT`  | 5  | "tribes" (asbāṭ — the 12 tribes of Israel) | All 5 are the Moses 12-tribes set. |
| `jwz`  | 5  | "to cross over / pass through" | All 5 are Moses crossing the sea / passing the Red Sea. |

### 4.2 70-90% Moses-coded

| Root | Moses / Total | Gloss |
|---|---:|---|
| `srH` | 6/7   = 0.857 | "let go / send away" — Moses says "let my people go" |
| `bqr` | 7/9   = 0.778 | "cow" — the cow narrative S2:67-73 |

### 4.3 60-70% Moses-coded

| Root | Moses / Total | Gloss |
|---|---:|---|
| `Swm` | 9/14  = 0.643 | "to fast" / Moses's Sinai retreat (linked to 40 days) |
| `Twr` | 7/11  = 0.636 | "Mount Sinai" (al-Ṭūr) |
| `ymm` | 7/11  = 0.636 | "the sea" (yamm — Pharaoh drowns, Moses crosses) |
| `sHr` | 39/63 = 0.619 | "magic / sorcery" — the Pharaoh-magicians contest dominates |
| `hwd` | 12/21 = 0.571 | "the Jews / to be Jewish" |

### 4.4 50-60% Moses-coded

| Root | Moses / Total | Gloss |
|---|---:|---|
| `dmr` | 6/10 = 0.600 | "to destroy" |
| `$bh` | 7/12 = 0.583 | "to resemble / similitude" (Christ-confusion polemic + Moses) |
| `*bH` | 5/9  = 0.556 | "to slaughter" (Pharaoh slaughtering newborns; the cow) |
| `$kk` | 8/15 = 0.533 | "doubt" |
| `Tlq` | 12/23 = 0.522 | "to set free / divorce" — Moses pleading for release of his people |
| `Hjj` | 17/33 = 0.515 | "argument / pilgrimage" — Moses's "clear argument" against Pharaoh |
| `byD` | 6/12 = 0.500 | "white" — the white-shining hand miracle |
| `tmm` | 11/22 = 0.500 | "to complete / perfect" — "We perfected for Moses 40 nights" |
| `lwH` | 3/6  = 0.500 | "tablet / Tablets" — the Sinai tablets |

### 4.5 Pharaoh's name itself

**`firoEawon`** (Pharaoh, PN): **74 tokens / 67 distinct verses** in **27 surahs**.
Co-distribution with Moses:

| Surah | Pharaoh verses | Moses verses |
|---:|---:|---:|
| 7  | 9 | 19 |
| 40 | 8 | 5  |
| 28 | 7 | 17 |
| 26 | 6 | 8  |
| 10 | 5 | 8  |
| 20 | 5 | 17 |
| (other 21 surahs) | 27 | 51 |

**15 verses contain both Moses and Pharaoh** — the canonical confrontation moments
(7:103-104, 10:75-79, 11:97, 23:46, 26:11, 27:12, 28:3, 28:8-9, 28:32, 28:38,
40:24-26, 43:46). Pharaoh appears without Moses in 52 verses, mostly in
shortened "people of Pharaoh" formulae (e.g. 8:52, 8:54, 3:11) and in late
apocalyptic single-line allusions (S69, S73, S79, S85, S89). Moses appears
without Pharaoh in 116 verses — most often when the narrative has moved past
the Exodus into Sinai or the wilderness.

Pharaoh has no triliteral root in QAC; he is exclusively a proper noun, like
Mūsā. So the entire "Pharaoh signature" is name-only — there is no oblique or
metaphorical Pharaoh material.

### 4.6 Reading the signature

The signature is unmistakably narrative-locked: staff, sea, tribes, cow, white
hand, tablets, magic. These are *story-objects* that have no other home in the
Quran. The Moses pericopes are the only place these roots are needed at any
density, and the QAC root index reflects that. The Quran's lexicon literally
swells around the Moses material.

Compare this to e.g. the Abraham signature (the root `Hnf` "ḥanīf, primordially
monotheist" is Abraham-coded, but Abraham's lexicon is otherwise generic
theological language) or the Joseph signature (`sjn` "prison" 12/12, `qmS`
"shirt" 6/6 — narrowly thematic). Moses sits between: he has *more* exclusive
roots than any other prophet because he has more story.

---

## 5. The Moses-Khidr pericope (18:60-82)

Sūrat al-Kahf 18:60-82 is the only Quranic appearance of the figure later
called al-Khiḍr (the Quran calls him only "a servant of Our servants whom We
had given mercy and taught knowledge of Our own"). The pericope is structurally
unusual: it has no Pharaoh, no staff, no tribes, no Sinai, no plagues. It is
a self-contained wisdom tale embedded in a surah that is otherwise about the
Cave-dwellers, Two-Gardens, and Dhū al-Qarnayn.

### 5.1 Form

The pericope has 23 verses. Three-act structure:

| Section | Verses | Content |
|---|---|---|
| **Prologue** | 60-65 | Moses sets out, the fish escapes at the junction-of-the-two-seas, they meet "the servant" |
| **Episode 1 — Boat** | 66-72 | Moses asks to follow; the servant scuttles a boat; Moses objects |
| **Episode 2 — Boy** | 73-75 | The servant kills a boy; Moses objects |
| **Episode 3 — Wall** | 76-77 | The servant rebuilds a wall in a town that refused them food; Moses objects |
| **Epilogue** | 78-82 | The interpretation: boat = saved from a king's seizure; boy = would have grieved his believing parents; wall = protecting two orphans' inheritance |

### 5.2 Ring score

Pairwise root-set Jaccard (v60↔v82, v61↔v81, …) over the 23 verses:

- **Observed score: 0.1549**
- **Null mean (500 verse shuffles): 0.0808 ± 0.0316**
- **z = +2.28** (uncorrected)

This is a *real* signal under the chiastic-audit.md null. Not Bonferroni-surviving
on its own, but consistent with the surah's other ring (Dhū al-Qarnayn 18:83-91,
listed in chiastic-audit.md §3 as one of the four Bonferroni-surviving sub-surah
rings at z = +5.19). **Surah 18 has at least two genuine ring units.** The
Khidr pericope has been read as concentric in the literary tradition (each
"so they set out" inaugurates a parallel episode); the metric agrees.

### 5.3 Why Khidr matters

The pericope is the only place in the Quran where Moses is the *student*, not
the *teacher*. It is also the only place where the verb ittabaʿa lands in a
verse that names Moses (18:66 — "may I follow you"). And the explicit reason
the servant gives for parting from Moses (18:78) is that "you cannot bear with
patience what you do not encompass in knowledge." This is the inverse of the
Sinai pattern: Moses, the bearer of the Tablets and the law, is told that
there is a knowledge he does not have. The cohesion of this short pericope —
both narratively and metrically — is the highest of any Moses unit in the
Quran short of the magicians' submission.

---

## 6. The five tellings of the staff miracle

Moses's staff turns into a serpent five times in the Quran: 7:107, 20:20,
26:32, 27:10, 28:31. The QAC morphology lets us compare them token-for-token.

### 6.1 The two minimal versions (7:107 and 26:32) are word-for-word identical

Both are six tokens with identical lemmas:

| Position | Token | Lemma | Root |
|---:|---|---|---|
| 1 | fa-                | (conjunction) | — |
| 2 | alqā               | `>aloqaY^`    | `lqy` |
| 3 | ʿaṣā               | `EaSaA2`      | `ESw` |
| 4 | -hu                | (pronoun)     | — |
| 5 | fa-idhā hiya       | (deictic)     | — |
| 6 | thuʿbānun mubīn    | `vuEobaAn` + `m~ubiyn` | `vEb` + `byn` |

Both verses translate to "And he threw his staff, and behold, it was a
manifest serpent." The only difference between 7:107 and 26:32 in QAC is the
location reference and the surrounding context — the staff sentence itself
is verbatim.

The full Jaccard matrix:

|             | 7:107-108 | 20:17-22 | 26:32-33 | 27:10-12 | 28:31-32 |
|---|---:|---:|---:|---:|---:|
| **7:107-108** | 1.000 | 0.143 | **1.000** | 0.125 | 0.129 |
| **20:17-22**  | 0.143 | 1.000 | 0.143    | 0.209 | 0.244 |
| **26:32-33**  | 1.000 | 0.143 | 1.000    | 0.125 | 0.129 |
| **27:10-12**  | 0.125 | 0.209 | 0.125    | 1.000 | **0.486** |
| **28:31-32**  | 0.129 | 0.244 | 0.129    | 0.486 | 1.000 |

### 6.2 Two clusters

- **The brief cluster (7:107 + 26:32)**: identical 6-word formula, embedded
  in the magicians-of-Pharaoh contest. The narrator uses the same line twice,
  in two different surahs, in two different periods of revelation.
- **The Sinai-call cluster (27:10 + 28:31)**: J = 0.486 — share *thuʿbān*
  (serpent) is replaced with *jānn* (light snake / jinn-snake) and Moses
  *flees* from the staff. The 27 and 28 versions are the burning-bush call,
  not the magicians' contest. Moses is alone with God, not facing Pharaoh.
  Shared roots include `wly` "to turn one's back", `Eqb` "to retreat",
  `ymn` "right hand", `byD` "white" (the white hand miracle is paired with
  the staff in these versions only).
- **The Ṭā-Hā version (20:17-22)**: longest of the five, the only one with
  the full dialogue ("What is in your right hand, O Moses?" / "It is my staff;
  I lean on it; I bring down leaves for my sheep…"). Has 13 unique roots no
  other version uses. Moses *lists what the staff is for* before God
  transforms it — a moment of literary suspense unique to Surah 20.

### 6.3 Roots common to ALL FIVE versions

Only four:

| Root | Gloss |
|---|---|
| `lqy` | to throw |
| `ESw` | staff |
| `ydy` | hand |
| `byD` | white |

The hand-and-white show that **the white-hand miracle is part of the staff
formula in all five tellings**, even when only mentioned in passing.

### 6.4 Editorial reading

The minimal 6-word identical version (7:107 ≡ 26:32) is the *signature line*
— the narrator's stock formula for the public miracle in front of Pharaoh's
court. The expansive Sinai-call versions (27, 28) are the private dialogue
between Moses and God. The Ṭā-Hā version (20:17-22) is the most expanded
literary treatment, with the only dialogue about *what the staff was for*
before its transformation. **Three different rhetorical registers for the
same event** — and the Quranic narrator deploys them according to the surah's
genre needs.

---

## 7. Ṭā-Hā vs Al-Qaṣaṣ

These are the two surahs where Moses *is the surah*. Comparison:

| Metric | S20 (Ṭā-Hā) | S28 (Al-Qaṣaṣ) |
|---|---:|---:|
| Period | Middle Meccan | Late Meccan |
| Revelation pos | 45 | 49 |
| N verses | 135 | 88 |
| Moses verse range | 9-98 | 3-46 |
| Moses tokens | 17 | 18 |
| Moses span N | 90 | 44 |
| Span / surah | 67% | 50% |
| Root tokens (whole surah) | 837 | 882 |
| Tokens / verse (whole surah) | 6.2 | 10.0 |
| Jinas density (whole surah) | 0.790 | 0.838 |
| Jinas density (Moses span) | 0.733 | 0.717 |
| Whole-surah ring z | -0.17 | -0.76 |
| Moses-span ring z | -1.57 | **+1.71** |

### 7.1 Reading

**Ṭā-Hā** is *episodic*. Moses encounters God at the burning bush (20:9-24),
goes to Pharaoh (20:43-79), the magicians submit (20:65-73), and then the
calf episode unfolds (20:83-98). Each unit is locally cohesive but the surah
*as a whole* and the *Moses corridor as a whole* score below the ring null —
no reverse-paired symmetry. Ṭā-Hā's structure is forward-moving narrative.

**Al-Qaṣaṣ** is *cyclical*. The surah opens with Moses's birth (28:7-13),
cycles through his Midian exile-and-marriage (28:22-28), brings him back to
Egypt (28:29ff), and closes the Moses arc with the destruction of Korah
(28:76-82, who reuses the Pharaoh-pattern as a wealthy-Israelite-tyrant
counterpoint). The Moses span scores **z = +1.71** — mild but real ring
tendency. The opening verses about Pharaoh's oppression and the closing verses
about Korah's destruction serve as outer brackets; the Midian exile and
return are an inner symmetry.

### 7.2 The Tuwa pun in Ṭā-Hā

Surah 20 has the famously sound-mimetic toponym ṭuwā (طوى, "rolled / sacred
valley") in 20:12, and the same root reappears as the cosmic "rolled-up
heavens" in 21:104 and elsewhere. This is the kind of jinas the
`jinas-wordplay.md` density metric catches (Ṭā-Hā jinas density = 0.79, in
the upper third of the corpus). Surah 20's opening also has the unique
`Tāhā` muqaṭṭaʿāt itself, which has been read as Aramaic for "O man!" or as
an attention-syllable; in either case it sets a register of intimate
direct address before the Moses biography begins.

---

## 8. Pharaoh's structural distribution

### 8.1 Where Pharaoh lives

Pharaoh's 67 distinct-verse occurrences cluster in 8 main surahs (S7, S40, S28,
S26, S10, S20, S2 + S17), with 19 single-verse trailing references in late
Meccan apocalyptic surahs (S69:9, S73:16, S79:17, S85:18, S89:10) and one
Medinan list (S66:11). Two structural patterns:

1. **The biographical Pharaoh** (S7, S20, S26, S28, S40) — Pharaoh has speaking
   parts. He confronts Moses, summons magicians, exalts himself, drowns.
2. **The exemplary Pharaoh** (S2, S3, S8, S69, S73, S79, S85, S89) — Pharaoh
   is invoked as a *type* of denial, often in a single line: "the way of the
   people of Pharaoh and those before them — they denied the signs of their
   Lord, so We destroyed them" (3:11). No staff, no plagues, no dialogue.

The *biographical* Pharaoh is concentrated in Late and Middle Meccan surahs
(S7, S20, S26, S28, S40 = rev pos 39, 45, 47, 49, 60). The *exemplary*
Pharaoh dominates the early Meccan apocalyptic and the Medinan polemical. This
is consistent with the chronological-revelation finding that the early Quran
addresses by direct typological reference and the middle Quran develops the
sustained narrative.

### 8.2 Within Moses pericopes

In the magicians' contest pericopes — 7:103-126, 10:75-82, 20:56-79,
26:30-51 — Pharaoh's name density rises to 0.05-0.08 of root tokens. In the
Moses-Khidr pericope (18:60-82) it is 0.0 (Pharaoh is absent). In the calf
episode (7:148-157, 20:83-98, 2:51-54) it is 0.0 again — the calf is a
post-Pharaoh problem; once Israel is delivered, Pharaoh disappears from the
text. The narrator's discipline about Pharaoh's *absence* is striking: he
appears only when the Egyptian setting is active.

### 8.3 Pharaoh-as-inverse-prophet

In 28:38 Pharaoh utters "I have not known of any deity for you other than me"
— a verbatim parody of *lā ilāha illā Allāh*. In 79:24 he says "I am your
Lord most high" (*ana rabbukum al-aʿlā*). The Pharaoh of the Quran is
constructed as a *negative theological double* of God — the only character
in the corpus who claims the divine attributes for himself. This typological
function is *why* he gets so much narrative space: he is the most theologically
loaded antagonist the text has.

---

## 9. Chronological growth of the Moses material

Egyptian-edition revelation order locates the earliest Moses mentions in
Early-Meccan apocalyptic surahs as bare allusions:

| Rev pos | Surah | Verses | Tokens / verse | Content |
|---:|---:|---|---:|---|
| 8  | 87 | v17-21       | 1.2 | "the scriptures of Abraham and Moses" |
| 23 | 53 | v34-38       | 2.8 | "or has he not been informed of what was in the scriptures of Moses?" |
| 39 | 7  | v101-162 (62) | 10.5 | full magicians+calf+Sinai cycle |
| 42 | 25 | v33-37       | 7.0 | "We gave Moses the Book and made his brother Aaron with him a minister" |
| 44 | 19 | v49-53       | 6.2 | telegraphic "remember Moses, indeed he was sincere" |
| 45 | 20 | v7-93 (87)    | 5.8 | full Ṭā-Hā biography |
| 47 | 26 | v8-67 (60)    | 4.1 | refrain-driven Shuʿarāʾ retelling |
| 49 | 28 | v1-78 (78)    | 10.1 | full Qaṣaṣ biography (only one with birth-narrative) |
| 51 | 10 | v73-90 (18)   | 9.2 | Yūnus retelling (Pharaoh focus) |
| 52 | 11 | v15-112 (98)  | 9.4 | Hūd prophet-cycle Moses (one of seven) |
| 60 | 40 | v21-55 (35)   | 9.7 | Ghāfir believer-of-Pharaoh's-house speech |
| 67 | 51 | v36-40        | 4.4 | telegraphic "and in Moses [is a sign]" |
| 69 | 18 | v58-68        | 7.5 | Khidr pericope |
| 87 | 2  | v49-250 (202) | 13.7 | Medinan covenant-and-Israelite-disobedience corpus |
| 89 | 3  | v82-86        | 9.8 | Medinan covenant-list inclusion |
| 90 | 33 | v5-71         | 12.1 | Medinan oblique reference |
| 92 | 4  | v151-166      | 11.5 | Medinan polemical reference |
| 112| 5  | v18-26        | 12.1 | last-revealed Moses material — the entry-into-the-land refusal |

### 9.1 Reading

Three phases:

1. **Early Meccan allusion (rev pos 8-30)**: Moses appears as a *reference*,
   1-2 verses, 1-3 root tokens per verse. The audience is presumed to know
   the story — the text only needs to point.
2. **Mid-to-late Meccan biography (rev pos 39-72)**: the four big retellings
   land — S7, S20, S26, S28 — each in a different rhetorical register
   (cycle, episodic, refrain, cyclic). Plus shorter retellings (S10, S11,
   S40). Average tokens per verse climbs to 4-10.
3. **Medinan covenant (rev pos 87+)**: S2, S3, S4, S5 — Moses now a *legal
   precedent*. The Israelites' disobedience to Moses (the cow narrative,
   the calf, the entry-refusal) becomes typology for the new umma's risk
   of disobedience to Muḥammad. Average tokens per verse climb above 12.

This is precisely the pattern `chronological-revelation.md` identifies for
the corpus as a whole (verse length doubles from 18.5 to 79.9 letters across
Nöldeke's four phases) — applied here specifically to Moses, the same trend
holds. Moses-bearing verses follow the corpus-wide growth curve almost
perfectly. The Moses material is *not* an exception to the diachronic
expansion: it is a cleaner instance of it.

The last Moses material chronologically is **5:18-26** (rev pos 112), where
the Children of Israel refuse to enter the holy land and wander 40 years.
This is the bleakest and most polemical Moses passage in the Quran. By the
time the corpus closes, Moses is no longer presented as a model of triumphant
prophecy — he is presented as a model of the prophet who is *failed by his
people*, a typology with obvious application to the Medinan community's
own internal divisions.

---

## 10. Prior-art note (WebSearch)

| Scholar | Work | Relevance |
|---|---|---|
| **Gabriel Said Reynolds** | *The Qurʾān and Its Biblical Subtext* (Routledge 2010); *The Qurʾān and the Bible: Text and Commentary* | Reads the Quran's prophet narratives — including Moses — as alluding to a presumed audience knowledge of Jewish/Christian scripture. Argues that the medieval *tafsīr* tradition partially obscured these intertexts. The minimal-formula 7:107 ≡ 26:32 (this report §6) is consistent with Reynolds's "the Qurʾān relies on prior knowledge" framing — the brief versions presume the audience supplies the rest. |
| **Angelika Neuwirth** | "Form and Structure" in *Cambridge Companion to the Qurʾān*; *Der Koran als Text der Spätantike* | Treats the Meccan surahs (esp. middle Meccan, including S20 Ṭā-Hā) as carefully composed liturgical units with ring-like and bipartite structures. Reads Ṭā-Hā as a Moses-narrative balanced by an Adam-narrative, with the longer Moses telling introducing a theme that the shorter Adam telling reprises. This report's metric (Ṭā-Hā ring z = -0.17 whole-surah, +1.71 for the parallel Qaṣaṣ Moses span) does not falsify Neuwirth's bipartite reading but suggests that Ṭā-Hā's coherence is *thematic* (Moses then Adam) rather than *root-lexical* (the two halves don't share enough roots to register as a chiasmus). |
| **Reuven Firestone** | *Journeys in Holy Lands* (1990 — focused on Abraham), articles on prophet-legend transmission | Comparative-narratology approach to the development of prophet legends from Bible → para-biblical → Quran → tafsir. The Moses-Khidr pericope is often discussed as an Islamic adaptation of the Alexander-Romance tradition; Firestone's methodology of legend-strata analysis is the model. This report offers no new comparative claim, but the §5 ring-score for 18:60-82 (z = +2.28) confirms that the pericope is a self-contained literary unit, consistent with Firestone-style readings of it as an inserted wisdom-tale. |

None of the three scholars, to my knowledge, has published the specific
quantitative findings of this report (the 12/12 staff signature, the 7:107
≡ 26:32 verbatim identity, the 0.486 cluster between 27:10 and 28:31, the
+2.28 ring score for the Khidr pericope, the 136/136 word-pair flagged in
`word-pair-symmetry.md`, or the chronological tokens/verse ramp on Moses
specifically). These are computational confirmations of literary intuitions
already present in the field.

---

## 11. Verdict

Moses is the most-developed character in the Quran by every measure: total
mentions (136), distinct verses (131), surahs occupied (34), pericope units
(62), exclusive vocabulary (≥33 roots ≥50% Moses-coded, with `ESw` at 100%),
and chronological span (early Meccan single-line allusion through last-revealed
Medinan covenant material). The retellings are not redundant: each major
surah deploys a distinct rhetorical register (S7 long cycle; S20 burning-bush
episodic; S26 refrain-driven; S28 cyclic with birth-narrative; S2 covenant-
legal; S40 dissident-courtier framing; S18 wisdom-tale inversion). The Moses
material is the Quran's primary site for refining its own prophetology —
across the chronological span, the same character is used to establish, then
defend, then critique the relationship between a prophet and his people.

The 136/136 Mūsā = ittabaʿa coincidence is real but slack at the verse level
(only 2 same-verse co-occurrences). Both same-verse occurrences, however,
are *role-reversal* moments — in 7:142 Moses commands his brother *not* to
follow corruptors; in 18:66 Moses himself asks to follow a teacher who knows
more than he does. This is probably accidental but it is unusually elegant.

The most structurally coherent Moses pericope is the Khidr unit (z = +2.28),
not any of the canonical biographies. The most lexically distinctive Moses
telling is in Shuʿarāʾ (mean Jaccard 0.245), not the Ṭā-Hā/Qaṣaṣ pair. The
most chronologically late Moses material is Sūrat al-Māʾidah's entry-refusal
text — the bleakest, most pessimistic Moses passage in the Quran — and its
late position is editorially significant: by the end of the revelation,
Moses is the type of the prophet whose people fail him.

---

## Sources (web prior-art search)

- [Reynolds, *The Qurʾān and Its Biblical Subtext* (Routledge 2010)](https://www.routledge.com/The-Quran-and-its-Biblical-Subtext/Reynolds/p/book/9780415524247)
- [Reynolds, *The Qurʾān and the Bible: Text and Commentary* (Yale 2018) — open PDF](https://almuslih.org/wp-content/uploads/2024/10/Reynolds-G-The-Quran-and-the-Bible-Text-and-Commentary.pdf)
- [Reynolds review in *Journal of Qurʾanic Studies*](https://www.euppublishing.com/doi/full/10.3366/jqs.2012.0040)
- [Wikipedia, "Tā Hā" — covers Neuwirth's bipartite reading](https://en.wikipedia.org/wiki/Ta-Ha)
- [Imam Ghazali Institute, tafsir of S18:60-82 Moses-Khidr](https://www.imamghazali.org/blog/tafsir-surah-al-kahf-verses-60-82-musa-khidr)
- [Firestone, *Journeys in Holy Lands*](https://www.barnesandnoble.com/w/journeys-in-holy-lands-reuven-firestone/1123688479)

---

## Reproducibility

Every number in this report comes from one of two scripts:
- `scratch/moses/moses_deep.py` — main inventory, 136/136 audit, signature
  vocabulary, top-5 Jaccard matrix, staff-miracle analysis, Pharaoh
  distribution, chronological trace
- `scratch/moses/moses_structures.py` — ring scores and jinas density per
  pericope

Both scripts read only `data/morphology/quranic-corpus-morphology-0.4.txt`,
`data/translations/en.sahih.txt-2.txt`, and `data/revelation-order.csv`. Run
logs are at `scratch/moses/run1.log` and `run2.log`. Raw JSON output is at
`scratch/moses/moses_summary.json`.
