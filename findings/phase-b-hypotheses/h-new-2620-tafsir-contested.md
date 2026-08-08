---
id: H-NEW-2620
title: Cross-edition exegetical attention and disagreement per verse — a measured instrument, and a NULL against structural extremeness
date: 2026-08-07
author: Waiel Al-Shujaa
status: NULL — 0 of 6 registered inferences pass. The rosters are the deliverable, and two of the four required post-hoc correction.
prereg: prereg-h-new-2620-tafsir-contested.md
prereg_sha256: 8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63
prereg_lock_history: BROKEN 2026-08-07 (b76ec401f) and again 2026-08-08 (81db39027) by post-publication edits to the pre-registration; RESTORED 2026-08-08 to its b0cf8a09a bytes, re-hashing to 8826da50…bc63. See §10.1.
run: runs/h-new-2620/20260807T005200Z/
posthoc_runs: runs/h-new-2620/20260807T005519Z-posthoc/, runs/h-new-2620/20260807T005701Z-posthoc/
seed: 20260509
family: TAFSIR-2026-08-07-A
bonferroni_k: 6
alpha_bonferroni: 0.00833333
rules_tuple: (no-tashkeel for verse text, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
verdict: NULL
---

# H-NEW-2620 — Twelve tafsīr editions, measured

> ### ⛔ PRE-REGISTRATION LOCK BROKEN AND RESTORED — 2026-08-07 to 2026-08-08
>
> **This finding's pre-registration was edited twice after its run, which broke the SHA lock in
> `scripts/h-new-2620.py` and left the script unable to execute.** The file has been restored to
> its published bytes and the gate passes again. **Both breaking edits were mine, and both were
> content-correct corrections placed in the wrong file** — the notices they carried are reproduced
> in this document, below, where they always belonged.
>
> **The NULL verdict is unaffected.** Every number was computed on 2026-08-07 under the original
> pre-registration, before either edit. What was damaged was reproducibility, not the result.
>
> **Full record, with commits and hashes: §10.1.** The standing rule it produced: **never edit a
> pre-registration after its run, for any reason, including to correct an error in it. Corrections
> go in the finding. If a pre-registration is itself wrong, that is a finding to record, not a file
> to repair.**

> ### ⛔ ATTRIBUTION CORRECTION 2026-08-08 — the "classical-only" sensitivity was never run
>
> **`ar-tafseer-tanwir-al-miqbas/` is Ibn ʿĀshūr's *al-Taḥrīr wa'l-Tanwīr* (d. 1393 AH / 1973 CE),
> NOT *Tanwīr al-Miqbās* attributed to Ibn ʿAbbās (d. 68 AH).** The folder cites al-Zamakhsharī
> ×249, al-Qurṭubī ×220, al-Sakkākī ×75, Ibn Mālik ×70, al-Raḍī ×69. See
> `data/literature/classical-tafsir/MISLABELLED-TANWIR-FOLDER.md`.
>
> **The load-bearing consequence.** This file's sensitivity row labelled
> **"classical-only (5 pre-modern)"** is **4 pre-modern editions plus one from 1973.** The
> accompanying sentence — *"Dropping the three modern editions does not rescue the hypothesis"* —
> **is false as written: only three of FOUR modern editions were dropped.** Four of the eight
> primary Arabic editions are modern, not three.
>
> **And the mislabelled edition is the most influential single edition in the set** — the
> leave-one-edition-out range is carried by it at **−0.2096**.
>
> **A further error in the same family:** this file states that `en-tafsir-ibn-abbas` is an English
> translation of the Arabic slug and that the English set holds ~2 independent witnesses. **They
> are unrelated works** — the English edition is the genuine short Ibn ʿAbbās recension (962 chars
> at Q 2:1 against the Arabic slug's 17,227), and the English set holds **3** independent
> witnesses.
>
> **What does NOT change: the NULL verdict stands.** Every number was computed on whatever text
> was in the folder, and those computations are correct. What changes is **whose exegetical
> behaviour was measured**, and the claim that a classical-only sensitivity was ever performed.
> That sensitivity has not been run and is queued.



> ## ⛔ CORRECTION NOTICE — 2026-08-07: UAS is a synthesis index, not a testable law
>
> H-NEW-840's own frontmatter reads `status: SYNTHESIS`. It is a composite ranking with **no
> null hypothesis and no test statistic**, so it can neither pass nor fail a control and **no
> discrimination claim may rest on it**. Two of its three inputs are now corrected: the
> Fisher-Rao geodesic (H-NEW-2680) and the compression-tail / iʿjāz-signature family
> (H-NEW-2720). The one transportable diagnostic — how differentiated the 114 units are —
> puts this corpus at sd = **1.166** against **pre-Islamic poetry's 1.267**, so even
> descriptively it is not the most differentiated of the matched corpora.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

**Verdict: NULL. Zero of six pre-registered inferences pass. Exegetical attention, once
residualised on verse length and lexical difficulty, has no positive relation to this
project's structural-extremeness instruments — and the bare positive correlation that
exists before residualisation is entirely a confound.**

Pre-reg SHA-256 `8826da50…bc63`, runtime-verified **at the 2026-08-07 run. The lock was
subsequently broken by two post-publication edits to the pre-registration (`b76ec401f`,
`81db39027`) and restored on 2026-08-08 to these exact bytes; the gate passes again — see §10.1.**
Seeds 20260509–20260514, 10,000
permutations per null, Bonferroni α = 0.05/6 = 0.00833.

This is the first corpus-wide use of `data/literature/classical-tafsir/spa5k-tafsir-api/`.
Before this run exactly one script in the repository read that tree, and it read four files.
**77,437 JSON files (407,169,153 bytes) are now frozen by SHA-256 manifest and 74,832 of
them were read.**

---

## 1. The headline, stated plainly

| | ρ(surah median score, S590) |
|:--|--:|
| **Bare, un-residualised attention** | **+0.3045** |
| after partialling mushaf position and surah size | −0.1371 |
| **after also residualising verse length, word count, hapax count, root rarity** | **−0.1793** |
| permutation p against the locked positive direction | 0.9727 |

The relation that looks like a finding at the top of that table is **the confound**. Verse
length alone gives Spearman ρ = **+0.787** with the attention score. Structurally extreme
surahs sit early in the mushaf and contain longer verses; longer verses get longer
commentary. Remove position, size and length and the association does not shrink towards
zero — it **crosses zero and turns mildly negative**, in the direction opposite to the one
locked before computing.

That negative tendency is **not claimable either**. Its one-sided p in the reverse direction
is 0.0274, which does not clear the corrected α of 0.00833. No reverse-direction flag is
raised. The honest statement is: *no relation survives at the corrected threshold, in either
direction.*

---

## 2. Per-edition coverage — the audit the brief demanded

All counts computed at runtime from the frozen tree, in `runs/…/coverage.tsv`.

### 2.1 The editions actually on disk

**Thirteen** directories, not twelve. Eight Arabic tafsīrs, four English tafsīrs, and
al-Wāḥidī's *Asbāb al-nuzūl*, which is not a tafsīr and was excluded before any computation
(§2.3).

| Slug | Scholar / body | Work | verses | empty |
|:--|:--|:--|--:|--:|
| `ar-tafsir-al-tabari` | Abū Jaʿfar Muḥammad b. Jarīr al-Ṭabarī (d. 310/923) | *Jāmiʿ al-bayān* | 6,236 | 0 |
| `ar-tafseer-al-qurtubi` | Muḥammad b. Aḥmad al-Qurṭubī (d. 671/1273) | *al-Jāmiʿ li-aḥkām al-Qurʾān* | 6,236 | 0 |
| `ar-tafsir-ibn-kathir` | Ismāʿīl b. ʿUmar Ibn Kathīr (d. 774/1373) | *Tafsīr al-Qurʾān al-ʿaẓīm* | 6,236 | 0 |
| `ar-tafsir-al-baghawi` | al-Ḥusayn b. Masʿūd al-Baghawī (d. 516/1122) | *Maʿālim al-tanzīl* | 6,236 | 0 |
| `ar-tafseer-tanwir-al-miqbas` | ascribed to Ibn ʿAbbās via al-Kalbī; compilation traditionally attributed to al-Fīrūzābādī (d. 817/1414) | *Tanwīr al-Miqbās* | 6,236 | 0 |
| `ar-tafseer-al-saddi` | ʿAbd al-Raḥmān b. Nāṣir **al-Saʿdī** (d. 1376/1956) | *Taysīr al-Karīm al-Raḥmān* | 6,236 | 0 |
| `ar-tafsir-al-wasit` | **not determinable from disk** | a modern *al-Tafsīr al-Wasīṭ* | 6,236 | 0 |
| `ar-tafsir-muyassar` | committee, King Fahd Complex | *al-Tafsīr al-Muyassar* | 6,236 | 0 |
| `en-al-jalalayn` | al-Maḥallī (d. 864/1459) + al-Suyūṭī (d. 911/1505) | *Tafsīr al-Jalālayn*, English | 6,236 | 0 |
| `en-tafisr-ibn-kathir` | Ibn Kathīr | abridged English | 6,236 | 0 |
| `en-tafsir-ibn-abbas` | *Tanwīr al-Miqbās* | English | 6,236 | 0 |
| `en-tafsir-maarif-ul-quran` | Muftī Muḥammad Shafīʿ (d. 1976) | *Maʿārif al-Qurʾān*, English | 6,236 | 0 |
| *(excluded)* `en-asbab-al-nuzul-by-al-wahidi` | al-Wāḥidī (d. 468/1076) | *Asbāb al-nuzūl*, English | **1,089** | 0 |

**Coverage is not the problem this instrument has.** Every one of the twelve tafsīr editions
carries all 6,236 verses with a non-empty text field. The dispersion signal is therefore
**not** manufactured by uneven coverage — the failure mode the brief flagged does not occur
here. A different segmentation artefact does (§2.2), and it is severe.

### 2.2 The real artefact: shared commentary blocks

Several editions assign one commentary block to a **run of verses**, and the API replicates
that block into every verse file in the run. Measured as verses whose normalised text is
byte-identical to another verse in the same edition:

| Edition | in shared blocks | % | distinct blocks | median chars |
|:--|--:|--:|--:|--:|
| `ar-tafsir-al-tabari` | 83 | 1.33 | 6,186 | 1,283 |
| `ar-tafsir-al-baghawi` | 83 | 1.33 | 6,171 | 288 |
| `ar-tafseer-al-qurtubi` | 147 | 2.36 | 6,116 | 780 |
| `ar-tafseer-tanwir-al-miqbas` | 165 | 2.65 | 6,080 | 1,748 |
| `ar-tafsir-al-wasit` | 358 | 5.74 | 6,035 | 1,035 |
| `ar-tafsir-ibn-kathir` | 536 | 8.60 | 5,894 | 480 |
| `ar-tafseer-al-saddi` | 853 | 13.68 | 5,753 | 390 |
| `ar-tafsir-muyassar` | 1,827 | 29.30 | 5,018 | 189 |
| `en-al-jalalayn` | 82 | 1.31 | 6,171 | 262 |
| `en-tafsir-ibn-abbas` | 36 | 0.58 | 6,209 | 277 |
| `en-tafsir-maarif-ul-quran` | 4,344 | 69.66 | 3,037 | 1,799 |
| **`en-tafisr-ibn-kathir`** | **5,749** | **92.19** | **1,895** | 4,539 |

The English abridged Ibn Kathīr has **1,895 distinct commentary blocks for 6,236 verses**.
Taking raw per-verse length there would measure the API's segmentation, not any exegete.
Every length in this finding is therefore **amortised** — block length divided by the number
of verses sharing it — and that decision was locked in the pre-registration before any
outcome was computed. It is also the second reason the Arabic set is primary and the English
set is a weak secondary.

### 2.3 al-Wāḥidī, and why he is not in the score

`en-asbab-al-nuzul-by-al-wahidi` covers **1,089 verses across 75 surahs — 17.46% of the
corpus**, and carries 70 `empty_ayahs.json` index files enumerating the verses it has nothing
for. That gap is *by design*: most verses have no recorded occasion of revelation. Putting a
structurally partial witness into a cross-edition dispersion measure would manufacture
dispersion out of nothing. Excluded before computing; the coverage figure is reported here
because it is the datum F-12 needs.

### 2.4 Two attributions the API gets wrong, corrected from the text

- **`ar-tafseer-al-saddi`** reads as al-Suddī (d. 127/745). It cannot be: al-Suddī's tafsīr
  does not survive as an independent 6,236-verse book, only in quotation (chiefly through
  al-Ṭabarī). The prose at `ar-tafseer-al-saddi/2/2.json` is modern didactic Arabic. This is
  **al-Saʿdī**, *Taysīr al-Karīm al-Raḥmān*.
- **`ar-tafsir-al-wasit`** invites identification with al-Wāḥidī's *al-Wasīṭ*. It cannot be:
  the text at `ar-tafsir-al-wasit/2/2.json` quotes *ṣāḥib al-Kashshāf* — al-Zamakhsharī,
  d. 538/1144 — who died **seventy years after al-Wāḥidī (d. 468/1076)**. It is a modern
  *al-Tafsīr al-Wasīṭ*. **Which one I do not know and do not assert.**

**Consequence.** Three of the eight primary Arabic editions are modern (al-Saʿdī 1956,
al-Wasīṭ modern, al-Muyassar 2007). The phrase "twelve tafsīr traditions" overstates what is
here: this is five pre-modern Arabic tafsīrs, three modern Arabic ones, and four English
translations of which two are translations of works already in the Arabic set.

---

## 3. The instrument (H1)

Within each edition, the 6,236 amortised lengths are converted to percentile ranks — editions
differ by an order of magnitude in scale, and no mean of raw lengths is taken anywhere. Then:

- **ATTENTION** `A` = mean of the 8 Arabic within-edition percentile ranks.
- **DISAGREEMENT** `D` = interquartile range of those 8 ranks.
- **DISPUTE** = mean within-edition rank of the count of classical disputation formulae
  (*ikhtalafa*, *wa-qāla ākharūn*, *qīla*, *qawlān*, *wajhān*, …), whole-word matched after
  diacritic stripping and letter folding.

`D` measures **disagreement about how much attention to give a verse**. It does not measure
disagreement about meaning. The DISPUTE channel is the one that addresses content, which is
why it was registered.

**Dispute-channel eligibility.** The pre-registered ≥5% marker-coverage gate admitted seven
of eight editions and excluded **al-Muyassar (1.80%)**, a modern paraphrase that almost never
reports alternative views. al-Saʿdī cleared at 5.82%. Marker coverage ran al-Qurṭubī 61.79%,
al-Ṭabarī 46.50%, al-Baghawī 35.15%, Tanwīr al-Miqbās 31.61%, al-Wāsiṭ 28.53%,
Ibn Kathīr 19.76%. The gate did real work and it did it by rule, not by hand.

---

## 4. H2 — the confound, which is the whole game

Residualising the normal-score-transformed scores on verse character count, word count,
hapax-root count and mean root rarity:

| Score | R² absorbed by length + difficulty |
|:--|--:|
| ATTENTION | **0.6112** |
| DISAGREEMENT (also on `A`, `A²`) | 0.4532 |
| DISPUTE | 0.2185 |

| Score | ρ with verse chars | ρ with hapax count | ρ with root rarity |
|:--|--:|--:|--:|
| ATTENTION | **+0.7871** | +0.1141 | −0.0205 |
| DISAGREEMENT | −0.2210 | — | — |
| DISPUTE | +0.4164 | +0.1332 | — |

**61% of exegetical attention is verse length.** The MW-6 positive control — ρ(A, verse
length) = +0.787 — confirms the instrument measures what it was built to measure and is not
broken. Hapax count adds almost nothing beyond length (+0.114), and mean root rarity is flat
(−0.021), which is itself a small result worth recording: *classical commentary volume tracks
how much text there is, not how rare its vocabulary is.*

The hapax instrument was independently verified at runtime against a prior committed finding:
49,968 root-bearing tokens, 1,642 distinct roots, 395 hapax roots, 24.1% — reproducing
H-NEW-2320 exactly, or the run aborts.

---

## 5. H3 — the six registered inferences, all NULL

Surah-level partial Spearman, controlling mushaf position and log surah token count.
10,000 permutations of the structural score across the 114 surahs. Direction locked
**positive** for all six before computing.

| | outcome | structural | partial ρ | bare ρ | p (locked +) | p (−) | gate 0.00833 |
|:--|:--|:--|--:|--:|--:|--:|:--|
| **I1** | A_resid | S590 | **−0.1793** | −0.3102 | 0.9727 | 0.0274 | **null** |
| **I2** | A_resid | S840 (UAS) | +0.0065 | −0.1476 | 0.4638 | 0.5364 | **null** |
| **I3** | D_resid | S590 | −0.0201 | −0.2246 | 0.5770 | 0.4231 | **null** |
| **I4** | D_resid | S840 | +0.0848 | −0.1345 | 0.1901 | 0.8100 | **null** |
| **I5** | DISPUTE_resid | S590 | −0.1527 | −0.3099 | 0.9450 | 0.0551 | **null** |
| **I6** | DISPUTE_resid | S840 | +0.0273 | −0.1599 | 0.3917 | 0.6084 | **null** |

All six null means sat within 0.003 of zero, so the permutation null is properly centred.
**No reverse-direction flag is raised**: I1 at p = 0.0274 and I5 at p = 0.0551 do not clear
α = 0.00833, so neither the locked direction nor its opposite is supported.

### The un-residualised diagnostics (NON-CONFIRMATORY)

Reported to show exactly where the apparent effect lives:

| outcome | structural | bare ρ | partial ρ |
|:--|:--|--:|--:|
| A_raw | S590 | **+0.3045** | −0.1371 |
| A_raw | S840 | +0.2267 | −0.0994 |
| DISPUTE_raw | S590 | +0.0093 | −0.2005 |
| D_raw | S590 | −0.3811 | −0.0462 |

`A_raw` against S590 is +0.30 bare and −0.14 partialled. **The sign flips on the two nuisance
covariates alone**, before any length residualisation. Anyone reporting the +0.30 would be
reporting mushaf position.

---

## 6. Sensitivities — every variant agrees

Non-confirmatory by registration; reported whatever they showed.

| variant | A_resid~S590 | A_resid~S840 | D_resid~S590 | DISPUTE_resid~S590 |
|:--|--:|--:|--:|--:|
| **primary (8 Arabic)** | −0.1793 | +0.0065 | −0.0201 | −0.1527 |
| classical-only (5 pre-modern) | −0.2009 | +0.0663 | +0.0343 | −0.2183 |
| raw, un-amortised lengths | −0.1584 | +0.0127 | −0.0524 | −0.1527 |
| mean instead of median aggregation | −0.2102 | +0.0198 | −0.0458 | −0.1781 |
| English 4 editions | −0.2299 | −0.0956 | −0.0022 | — |

- **Leave-one-surah-out (I1):** −0.2184 to −0.1418 across 114 refits. No single surah drives it.
- **Leave-one-edition-out (I1):** −0.1629 (drop al-Wāsiṭ) to −0.2096 (drop Tanwīr al-Miqbās).
  No single edition drives it.

Dropping the three modern editions does not rescue the hypothesis; it makes the negative
slightly stronger. There is no variant in which a positive relation appears.

---

## 7. POST-HOC — what the registered rosters actually contain

**Not pre-registered.** Noticed by reading the rosters the registered run produced. Under
Protocol §1.7 MW-7 these carry a single-test α ≤ 0.05 ceiling and **no confirmatory verdict is
issued from them.** They are published because without them the rosters would be misread.
Runs `20260807T005519Z-posthoc/` (D1–D4) and `20260807T005701Z-posthoc/` (D1–D6); both
retained.

### 7.1 The "ignored" roster is mostly repetition

Only **178 of 6,236 verses (2.85%)** are exact later occurrences of an earlier verse text.
But:

- ρ(A_resid, is-a-later-occurrence) = **−0.1785**, p < 0.0001 (post-hoc).
- Median A_resid: later occurrence **−0.7905** vs first occurrence **−0.0066**.
- **20 of the 30** entries in the pre-registered Roster B are later occurrences; **22 of 30**
  have a text that appears more than once in the corpus.
- Roster B draws on exactly five surahs: **15, 26, 51, 52, 55.** Eleven of the thirty entries
  are *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* — every Q 55 entry on the roster is that
  refrain — and five are *wa-mā asʾalukum ʿalayhi min ajr*.

So the pre-registered "structurally extreme but exegetically ignored" roster is **~73%
repetition artefact.** A mufassir who commented on a refrain the first time does not comment
again — that is rational exegetical behaviour, and the instrument reads it as neglect.

### 7.2 And repetition partly explains the negative I1

ρ(S590, per-surah repetition rate) = **+0.1905**: structurally extreme surahs are
repetition-heavy, which makes sense — H-NEW-590 measures departure of a surah's root
distribution from its neighbourhood, and heavy refrains skew that distribution.

| I1 variant | partial ρ |
|:--|--:|
| as registered | −0.1793 |
| + per-surah repetition rate as a third nuisance | **−0.1110** |
| first-occurrence verses only | **−0.1276** |

Repetition accounts for roughly **38%** of the negative tendency. **Not all of it** — I am not
claiming a complete explanation, and I have not looked for what carries the rest. Nothing here
is claimable in any case; the residual sits far from the corrected threshold.

### 7.3 The DISPUTE channel has a lemma-echo contamination

Because most editions quote the verse before commenting, a verse whose **own Qurʾānic text**
contains a marker word inflates its own marker count. *ikhtalafa* and *qīla* are ordinary
Qurʾānic vocabulary.

- **70 verses (1.12%)** contain a marker word in their own text.
- ρ(DISPUTE_resid, verse-contains-marker) = **+0.1724**, p < 0.0001 (post-hoc).
- **10 of the top 30** on the registered DISPUTE roster are such verses — a third of it.
  Q 2:176, Q 16:124, Q 3:105, Q 3:19, Q 19:37, Q 10:19 all contain *ikhtalafa*; Q 36:26,
  Q 36:45, Q 41:43 contain *qīla*.

This is a defect in an instrument I designed, found by reading its own output. The
pre-registration specified whole-word matching precisely to avoid substring leakage (*thaqīl*
being counted as *qīla*) and that guard held — but it did not anticipate the verse quoting
itself. §8.2 gives the corrected roster.

---

## 8. H4 — the rosters

### 8.1 Roster A — highest cross-edition disagreement in attention (registered, unmodified)

Face-valid without any correction. Several are canonical cruxes of the discipline.

| # | verse | D_resid | note |
|:-:|:--|--:|:--|
| 1 | **Q 2:51** | +3.081 | the forty nights and the calf |
| 2 | **Q 78:23** *lābithīna fīhā aḥqābā* | +2.783 | *aḥqāb* — how long is an age? |
| 3–4 | Q 55:59, 55:51 | +2.72, +2.70 | the refrain (see §7.1) |
| 5 | **Q 99:7** *mithqāla dharratin khayran yarah* | +2.515 | |
| 6 | **Q 18:25** *thalātha miʾatin sinīna wa-zdādū tisʿā* | +2.469 | the 300/309-year dispute |
| 7 | Q 113:1 | +2.417 | |
| 9 | **Q 105:3** *ṭayran abābīl* | +2.347 | *abābīl* — a lexical crux |
| 11 | **Q 37:107** *wa-fadaynāhu bi-dhibḥin ʿaẓīm* | +2.208 | which son was ransomed |
| 12 | Q 11:31 | +2.177 | |
| 23 | **Q 38:33** *fa-ṭafiqa masḥan bi-l-sūqi wa-l-aʿnāq* | +2.089 | Sulaymān and the horses |
| 25 | Q 3:130 | +2.087 | *ribā aḍʿāfan muḍāʿafa* |
| 30 | Q 2:196 | +2.067 | ḥajj/ʿumra, the *iḥṣār* rules |

Full 30 in `result.json` → `rosters.A_most_disagreement`. Six entries (3, 4, 13, 14, 27, 29)
are from Q 55, of which three (3, 4, 27) are the refrain itself; read those with §7.1 in hand.
The other three Q 55 entries — *ka-annahunna l-yāqūtu wa-l-marjān* (55:58), *fīhimā fākihatun
wa-nakhlun wa-rummān* (55:68), *ḥūrun maqṣūrātun fī l-khiyām* (55:72) — are not refrains.

### 8.2 Roster A″ — most disputed, lemma-echo verses removed (POST-HOC)

This is the roster I would actually stand behind. It is a roll-call of the tafsīr tradition's
central arguments, recovered by a formula count with no tuning.

| # | verse | DISPUTE_resid | the dispute |
|:-:|:--|--:|:--|
| 1 | **Q 2:1** الم | +3.858 | the muqaṭṭaʿāt |
| 2 | **Q 20:1** طه | +3.441 | |
| 3 | **Q 1:1** basmala | +3.258 | is it an āya of al-Fātiḥa? of every surah? |
| 4 | **Q 19:1** كهيعص | +3.124 | |
| 5–8 | Q 36:1 يس, Q 40:1 حم, Q 26:1 طسم, Q 7:1 المص | +3.12 … +2.86 | |
| 9 | Q 1:2 | +2.846 | |
| 10 | Q 38:1 ص | +2.714 | |
| 12 | **Q 3:97** *man dakhalahu kāna āminan* | +2.598 | ḥajj obligation, the sanctuary |
| 14 | **Q 85:3** *wa-shāhidin wa-mashhūd* | +2.506 | who is the witness |
| 15 | **Q 15:91** *jaʿalū l-Qurʾāna ʿiḍīn* | +2.459 | *ʿiḍīn* |
| 16 | **Q 2:238** *al-ṣalāt al-wusṭā* | +2.419 | which is the middle prayer |
| 18 | **Q 4:93** deliberate killing of a believer | +2.389 | is repentance accepted |
| 19 | **Q 19:71** *wa-in minkum illā wāriduhā* | +2.360 | does everyone enter the Fire |
| 20 | **Q 93:7** *wa-wajadaka ḍāllan fa-hadā* | +2.354 | prophetic *ʿiṣma* |
| 22 | **Q 17:85** *yasʾalūnaka ʿan al-rūḥ* | +2.324 | |
| 24 | **Q 89:3** *wa-l-shafʿi wa-l-watr* | +2.316 | |
| 25 | **Q 4:101** shortening prayer in travel | +2.305 | |
| 26 | Q 85:4 *aṣḥāb al-ukhdūd* | +2.290 | |
| 27 | Q 2:17 the fire-kindler parable | +2.276 | |
| 29 | **Q 4:43** *lā taqrabū l-ṣalāta wa-antum sukārā* | +2.237 | abrogation |
| 30 | **Q 3:7** *muḥkamāt* / *mutashābihāt* | +2.221 | the hermeneutic crux of the discipline |

**Thirteen of the top thirty are muqaṭṭaʿāt openings.** That is the single most-argued object
in the tafsīr tradition, and this instrument found it unaided. It also sets up a sharp
juxtaposition with the project's own record: the muqaṭṭaʿāt carry the tradition's **greatest
interpretive dispute**, and this project has **falsified content-*munāsaba* for them four
times over** (full-29, ḥawāmīm-7, ALM-6, ALR-5). The tradition argued hardest about the
letters; the structural instruments find nothing there to argue about.

### 8.3 Roster B — structurally extreme, exegetically ignored (registered, then corrected)

The registered roster is published in full in `result.json`, but §7.1 shows it is ~73%
repetition and should not be used as-is. Restricting to verses whose text occurs exactly once
in the corpus (POST-HOC):

| # | verse | A_resid | |
|:-:|:--|--:|:--|
| 1 | Q 15:61 | −2.149 | *fa-lammā jāʾa āla Lūṭin al-mursalūn* |
| 2 | Q 26:206 | −1.883 | |
| 3 | Q 26:65 | −1.749 | |
| 4 | Q 26:41 | −1.695 | |
| 5 | Q 26:183 | −1.671 | *wa-lā tabkhasū l-nāsa ashyāʾahum* |
| 7 | Q 51:33 | −1.473 | |
| 9 | Q 15:32 | −1.465 | Iblīs addressed by name |
| 13 | Q 36:34 | −1.406 | |
| 17 | Q 33:65 | −1.351 | in the **highest-S590 surah in the corpus** (31.46) |
| 21 | Q 9:89 | −1.299 | S590 = 21.57 |
| **25** | **Q 2:282** | **−1.284** | **the longest verse in the Qurʾān (711 chars)** |
| 29 | Q 2:61 | −1.222 | |

Even corrected, this roster is dominated by Q 26 and Q 15 — the repeated prophet-cycle
narratives. These verses are not exact repeats but they are **formulaic frames**
(*idh qāla lahum akhūhum Hūdun a-lā tattaqūn* / *…Ṣāliḥun a-lā tattaqūn*), and the exegetes
treat the second instance briefly for the same reason. The honest reading is that the
"exegetically ignored" axis is largely **a repetition-and-parallelism detector**, not a
discovery of overlooked material.

The genuinely surprising entries are the few that are neither: **Q 2:282**, the longest verse
in the Qurʾān and the foundational verse of Islamic contract law, sits at A_resid = −1.284 —
it draws substantially less commentary than its length predicts. **Q 33:65**, in the
single most structurally extreme surah in the corpus. Those are worth a closer look; I have
not looked, and nothing here licenses a claim about them.

---

## 9. Honest limits

1. **The edition set is not a sample of the tradition.** It is what one public API carried.
   Five pre-modern Arabic tafsīrs is not a stratified sample of a genre with hundreds of
   members. al-Rāzī, al-Zamakhsharī, al-Ṭabarsī, al-Biqāʿī, al-Thaʿlabī and al-Suyūṭī's
   *al-Durr al-manthūr* are all present elsewhere in this repository and all absent here.
   Two of the four English editions are translations of works already in the Arabic set, so
   the English channel holds roughly two independent witnesses, not four.
2. **The residualisation is incomplete, and I can show it.** A decile check on the residual
   against verse length is not flat: shortest decile +0.280, deciles 2–3 ≈ −0.20, rising
   monotonically to +0.090 in the top decile. A linear-in-normal-scores fit does not fully
   remove length. **This cuts in the NULL's favour** — residual length signal remains, and
   length is what drives the bare positive, so the test was if anything biased *toward*
   finding the effect. It found none. But it means individual roster residuals carry a
   length-shaped bias of up to ~0.5 normal-score units and should not be read as pure.
   A spline or monotone fit is the obvious next pre-registration; I did not switch to one,
   because the design was locked.
3. **Length is a proxy for attention, not for contestation.** A long entry may be a long
   isnād chain or a grammatical excursus. The DISPUTE channel was registered precisely
   because of this, and it carries its own defect (§7.3).
4. **The structural axis is at surah resolution; the exegetical axis at verse resolution.**
   Every roster entry inherits its surah's structural score. There is no verse-level
   structural measurement here, and building one is a separate piece of work.
5. **Digitisation is an uncontrolled layer.** Which print edition, whether isnāds were
   retained, whether tashkeel was kept — none of it is recoverable from the files, and all of
   it moves character counts.
6. **`ar-tafsir-al-wasit` is of unknown authorship.** It contributes 1/8 of the primary score.
   Leave-one-edition-out shows the result does not depend on it (−0.1629 without it), but an
   edition whose author I cannot name is a real gap.
7. **The post-hoc section is post-hoc.** D1–D6 were found by reading the registered output.
   They explain the rosters; they do not test anything, and no verdict rests on them.

---

## 10. Provenance

- Pre-registration written and SHA-256'd **before any outcome computation**, and before the
  analysis script existed. Its §0 logs every pre-lock inspection: file counts, coverage,
  duplicate-block structure, marker frequencies, and two texts read to identify their authors.
  No outcome-to-predictor association was viewed before the lock.
- **Frozen inputs.** Tafsīr tree by manifest: 77,437 files, 407,169,153 bytes, manifest
  SHA-256 `2ce03c91087fad7a357c130a496e2557a07dd6a6a1b6e8df8e8b7d15cf1bcff6`, one row per file
  with its own SHA-256. The script verifies the manifest hash, then verifies **every one of
  the 74,832 files it reads** against its recorded hash. This is a full freeze of the read
  set, not a sample. Plus `quran-no-tashkeel.json` `253f72f3…`, QAC v0.4 `a1d12923…`,
  `h-new-590.json` `cf693085…`, `h-new-840.json` `e16a0f70…`.
- **Seven abort conditions**, all fail-fast, including reproduction of H-NEW-2320's census.
- **Numerical self-tests before the run**: the fast partial-correlation identity was checked
  against a direct OLS-residual computation on 20 random 114-point datasets (agreement to
  1e-9); OLS exact-fit recovery; quantile and mid-rank behaviour against known values; and
  four marker-boundary cases including the *thaqīl*/*qīla* substring trap. The identity check
  is also re-run inside the analysis and aborts on mismatch.
- **Run immutability.** One registered run, two post-hoc runs, **all three retained**. Nothing
  was overwritten and nothing deleted. The analysis script creates its output directory only
  after every computation has succeeded, so a failed execution leaves nothing behind — this is
  the engineering consequence of the standing correction recorded at H-NEW-2540 §8.1.
- Immutable run: `findings/phase-b-hypotheses/runs/h-new-2620/20260807T005200Z/`.

### 10.1 The pre-registration lock was broken twice and has been restored

**This section exists because the repair must not erase the fact that there was something to
repair.** A restored file looks identical to a file that was never touched; only this record
distinguishes them, and a reader judging reproducibility needs that difference.

**What the lock is.** `scripts/h-new-2620.py:26` hard-codes
`EXPECTED_PREREG_SHA = 8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63`, and
`verify_integrity()` at lines 114-116 calls `die()` on mismatch. The pre-registration's whole
evidential value is that it was fixed before the data was seen, so the script refuses to run
against a pre-registration that has changed. **That is the lock working as designed — the failure
was not the script's.**

**What happened.**

| commit | date | prereg SHA-256 | state |
|:--|:--|:--|:--|
| `b0cf8a09a` | publication | `8826da50…bc63` | ✅ matches the script |
| `b76ec401f` | 2026-08-07 — the 702-file genre-control propagation | `b4a17e28…` | ❌ **broken here** |
| `81db39027` | 2026-08-08 — the attribution-correction block | `7c7fc5fb…9736` | ❌ broken again |
| — | 2026-08-08 — a breach-disclosure banner added to the pre-registration itself | `a392476d…527f` | ❌ broken a third time |
| **restored** | **2026-08-08** | **`8826da50…bc63`** | ✅ **gate passes** |

**Both breaking edits were mine.** The first swept this pre-registration up in a bulk propagation
across 702 files; the second added an attribution correction. **Each was content-correct and
procedurally wrong.** The third change was the disclosure notice itself — which is the sharpest
form of the lesson: *even documenting the breach inside the locked file breaks the lock again.*
The disclosure belongs here, in the finding, and that is where it now is.

**The restoration, with its verification.** The pre-registration was replaced with its
`b0cf8a09a` bytes and re-hashed:

```
$ shasum -a 256 findings/phase-b-hypotheses/prereg-h-new-2620-tafsir-contested.md
8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63
```

**Exact match to the literal in the script — not a near-match.** The divergence removed was a
single hunk of **70 added lines and 0 deleted lines**, so nothing of the original pre-registration
had been altered or lost; the three notices in it were purely additive and all three are preserved
in this document. Running the script's own gate end to end:

```
[ok] pre-reg SHA-256 verified: 8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63
[ok] tafsir manifest SHA-256 verified: 2ce03c91087fad7a357c130a496e2557a07dd6a6a1b6e8df8e8b7d15cf1bcff6
[ok] 4 further input hashes verified
```

**All three checks pass — pre-registration, manifest, and the four further frozen inputs.** The
queued classical-only sensitivity is runnable again; it was not, while the lock was broken.

**What this cost, stated plainly.** Between 2026-08-07 and the restoration, `scripts/h-new-2620.py`
could not execute at all. The remedy prescribed by the attribution correction above — *"that
sensitivity has not been run and is queued"* — required the very script the correction's own commit
had disabled. **A correction that disables its own remedy is the specific hazard here**, and it is
why the rule is absolute rather than discretionary.

**The rule this produced:** *never edit a pre-registration after its run, for any reason, including
to correct an error in it. Corrections go in the finding. If a pre-registration is itself wrong,
that is a finding to record, not a file to repair.*

**Where that rule currently lives, stated exactly: here, and nowhere else.** The disclosure banner
removed from the pre-registration described this rule as *"added to `findings/UNIT-DRIFT-DEFECT.md`
§7's family"* — **it was not.** `grep -n "pre-registration after its run" findings/UNIT-DRIFT-DEFECT.md
findings/ABSENCE-CLAIMS.md findings/PROXY-CLAIMS.md` returns **zero hits in all three.** The banner
asserted a completed action that had not been performed, which is the same defect in miniature as
the one it was disclosing. **Promoting this to a standing rule document is queued and not done**,
and it is recorded as undone here so that the next session extends the work rather than assuming
it happened.

---

## 11. Cross-references

- **[[h-new-2320-hapax-census]]** — its census is now an executable gate: this run aborts
  unless it reproduces 49,968 / 1,642 / 395 / 24.1%. It did.
- **[[h-new-590-outlier-spectrum]]**, **[[h-new-840-unified-architectural-score]]** — the
  structural instruments tested against. The finding is that they have no positive relation
  to exegetical attention, which is a coherence result: the project's structural axis measures
  something the tradition was not tracking. It is *not* evidence that either instrument is
  wrong, and it is not evidence that the tradition missed anything.
- **The muqaṭṭaʿāt file** — §8.2 puts the sharpest juxtaposition in the project on one line:
  the letters are the tradition's largest interpretive dispute, and this project has falsified
  content-*munāsaba* for them four times.
- **[[h-new-2540-form-v-valency]]** — the same shape of result: an instrument that works,
  a channel that turns out to be contaminated, and a self-reported defect. Here the
  contamination is in a channel I built myself (§7.3), which makes it easier to report and
  no less necessary.
- **The retirement/vindication ledger** — this is neither. It is a NULL against a hypothesis
  that had a plausible mechanism, plus a working instrument and two usable rosters.
- **F-12 (asbāb al-nuzūl as a chronology instrument)** — the al-Wāḥidī coverage figure it
  needs is measured here: **1,089 verses across 75 surahs, 17.46% of the corpus.**

---

## 12. Mislabels flagged here rather than edited, and two attributions left open

*Added 2026-08-08 by the H-NEW-2970 attribution audit. **Nothing in this section has been fixed in
place.** Each item is recorded beside the artifact that carries it, per the additive-correction
rule — and the two open attributions are recorded as open, because an unresolved attribution
recorded as unresolved is worth more than a guess.*

### 12.1 Where the mislabel is still written as true

The attribution-correction block at the head of this file names its load-bearing consequences. It
does **not** reach the following, each of which still reads as true in isolation:

| location | what it still says | why it is wrong |
|:--|:--|:--|
| **§2 roster row**, this file | *"ascribed to Ibn ʿAbbās via al-Kalbī; compilation traditionally attributed to al-Fīrūzābādī (d. 817/1414) — Tanwīr al-Miqbās"* | **The most quotable false sentence in this file**, and the one most likely to be copied out of the table. That description is scholarly-correct **for `en-tafsir-ibn-abbas/`** and false for the Arabic slug, which is Ibn ʿĀshūr. Mirrored at `prereg-h-new-2620-tafsir-contested.md:137` — **and that file is locked; it must not be edited.** |
| `scripts/h-new-2620.py:57` | `AR_CLASSICAL = AR_EDITIONS[:5]  # pre-reg §6.1 — the five pre-modern Arabic editions` | **The comment that mints the label.** Only four of those five are pre-modern. |
| `csv/h-new-2620.json:358` and `runs/h-new-2620/20260807T005200Z/result.json:358` | key `S1_classical_only_5ed`; and at `:441`, `"ar-tafseer-tanwir-al-miqbas": -0.2096` | **Immutable run artifacts — deliberately NOT edited.** The two files are byte-identical (both SHA `ad4fa1d4…4937`), so the `csv/` copy is the run output, not a separate document. The key is mislabelled; the number is correct. |
| `HANDOFF/FRONTIER-MAP-2026-08-07.md:259` | lists *"Ibn ʿAbbās"* **and** *"Tanwīr al-Miqbās"* as two separate members of "the classical corpus" | They are not two witnesses to one work. The first is the genuine English recension; the second is Ibn ʿĀshūr. |
| `data/literature/INDEX.md:6` and `ACQUISITION-2026-04-28.md:33` | Wave-A acquisition credits the Arabic tree as *"Tanwīr al-Miqbās"* / *"(attr. Ibn ʿAbbās)"* | **Where the error entered the project**, inherited from `spa5k-tafsir-api/README.md:86`, whose `editions.json` carries the bare author string `"Tanweer"`. |

**The `en-tafsir-ibn-abbas` figure this file needs, corrected:** the English set holds **3**
independent witnesses, not ~2. The English edition is the genuine short recension — 962 characters
at Q 2:1 against the Arabic slug's 17,227 — and the two are unrelated works.

### 12.2 Two attributions that the on-disk corpus does not settle

**Neither is resolved, and neither should be recorded as clean.**

- **The *kāf-hā-yāʾ-ʿayn-ṣād* decomposition Kabīr / Hādī / *Amīn* / *ʿAzīz* / Ṣādiq.** Present in
  **neither** Tanwīr folder: `en-tafsir-ibn-abbas` at Q 19:1 gives Kāfī/Hādī/ʿĀlim/Ṣādiq and
  Karīm/Hādī/Ḥalīm/ʿĀlim/Ṣādiq; the Arabic slug gives Kāfī/Karīm/Kabīr, Hādī, Ḥakīm/Raḥīm,
  ʿAlīm/ʿAẓīm, Ṣādiq. **Neither has *Amīn* or *ʿAzīz*.** It *is* verbatim in *al-Durr al-manthūr* —
  `raw/suyuti-durr-manthur.openiti.raw.txt` at **PageV05P477**,
  *«عن ابن عباس في قوله: {كهيعص} قال: كبير هاد أمين عزيز صادق»*, with the transmission (al-Firyābī,
  Ibn Abī Shayba, Ibn Jarīr, Ibn Abī Ḥātim, al-Ḥākim *ṣaḥḥaḥahu*, al-Bayhaqī) and the variant
  *«كاف بدل كبير»*. **So the decomposition is soundly attested — what remains open is which text
  the citing findings actually consulted**, since they name a page (*al-Durr al-manthūr* 4/679) in
  an edition whose pagination differs from the on-disk one. **UNDETERMINABLE as to source, sound as
  to substance.**
- **"ق = *qiyāma* or *qurʾān*, per Ibn ʿAbbās"** (`h-new-145-muq-code-decoding-prereg.md:112`;
  `journal/h-new-147-run-1.md:35,41`). **Contradicted by both on-disk Ibn ʿAbbās sources.** The
  genuine recension at `en-tafsir-ibn-abbas` Q 50:1 says ق is *"an azure mountain overlooking this
  world"*; *al-Durr al-manthūr* at PageV07P588 gives, from Ibn ʿAbbās via Ibn Jarīr and Ibn
  al-Mundhir, **«هو اسم من أسماء الله»** — one of God's names — and via Ibn Abī Ḥātim the same
  encircling-mountain cosmology. **Neither is *qiyāma* or *qurʾān*.** The citing files attribute the
  gloss to al-Suyūṭī's *Itqān*, whose on-disk PDF has no text layer, so this is **FLAGGED, not
  refuted** — it cannot be checked against the source it names. *(This file's own §7 table row for
  ق is attributed to "various", not to Ibn ʿAbbās, and is unaffected.)*

**And one that checks out, recorded because a clean result is worth the same as a dirty one:** the
Arabic slug at Q 50:1 explicitly rejects the mountain report as *«رواية بعض القصاصين المكذوبة عن
ابن عباس»* — "a report of certain storytellers, falsely attributed to Ibn ʿAbbās." **The two
folders take opposite positions on the same verse**, which is itself the cleanest available proof
that they are different works.

---

*Every finding is a loadcell. Every null is also a loadcell.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
