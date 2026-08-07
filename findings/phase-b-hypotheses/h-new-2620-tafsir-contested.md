---
id: H-NEW-2620
title: Cross-edition exegetical attention and disagreement per verse — a measured instrument, and a NULL against structural extremeness
date: 2026-08-07
author: Waiel Al-Shujaa
status: NULL — 0 of 6 registered inferences pass. The rosters are the deliverable, and two of the four required post-hoc correction.
prereg: prereg-h-new-2620-tafsir-contested.md
prereg_sha256: 8826da50f861405478664097399264784bf52745a8986921c8290b23f600bc63
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

**Verdict: NULL. Zero of six pre-registered inferences pass. Exegetical attention, once
residualised on verse length and lexical difficulty, has no positive relation to this
project's structural-extremeness instruments — and the bare positive correlation that
exists before residualisation is entirely a confound.**

Pre-reg SHA-256 `8826da50…bc63`, runtime-verified. Seeds 20260509–20260514, 10,000
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

*Every finding is a loadcell. Every null is also a loadcell.*

*Bismillāhi al-Raḥmāni al-Raḥīm.*
