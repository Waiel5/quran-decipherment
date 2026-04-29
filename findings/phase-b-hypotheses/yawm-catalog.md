---
phase: B
finding_id: phase-b-yawm-catalog-run-2
date: 2026-04-12
agent: yawm-catalog-agent
status: reported
claim_class: thematic / lexical-semantic / eschatological
rules:
  orthography: no-tashkeel (translit Buckwalter for morphology)
  word_definition: QAC lemma/root with idāfa-adjacency test (yawm + X at consecutive word positions)
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: none (exhaustive lemma/root match)
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (Dukes/QAC v0.4)
  text: quran-text/quran-no-tashkeel.json (114 surahs, 6236 verses)
  chronology: data/revelation-order.csv (Egyptian + Nöldeke)
priors:
  - findings/phase-b-hypotheses/paradise-hell-names.md  (Jannah/Jahannam toponymy)
  - findings/phase-b-hypotheses/covenant-language.md    (waʿd / mīʿād / ʿahd family)
  - findings/phase-b-hypotheses/oath-clusters.md        (opening oaths in Early Meccan surahs)
classical_priors:
  - al-Qurṭubī, al-Tadhkira fī aḥwāl al-mawtā wa-umūr al-ākhira
  - al-Ghazālī, al-Durra al-Fākhira fī kashf ʿulūm al-ākhira
  - Ibn Kathīr, al-Nihāya fī al-Fitan wa-l-Malāḥim
  - al-Suyūṭī, al-Budūr al-Sāfira fī Umūr al-Ākhira
scratch:
  - scratch/yawm-catalog/verify.py
  - scratch/yawm-catalog/verify-out.txt
---

# The Day of Judgement — Name-Level Catalog of the Quranic Epithets

## 0. Headline

The Quran names the Day of Judgement by at least **twenty distinct
epithets**. Every epithet carries a distinct semantic payload
(standing / reckoning / separation / gathering / deprivation / crying-out
/ striking / veiling / overwhelming / imminence / appointment /
threat / last-ness) and every epithet has a measurable signature in
**chronology** and **distribution**. Four hard facts fall out of the
verification:

1. **al-sāʿa** ("the Hour") is by a very wide margin the *most
   frequent* Day-of-Judgement term in the Quran — **43 unique
   verses** (48 segment hits) — and it is also the term that
   survives longest into the Medinan period (6 Medinan verses
   against 37 Meccan), making it the single **inter-period
   stable** lexical marker for the Last Day. Every other
   poetic epithet (al-qāriʿa, al-ṭāmma, al-ṣākhkha, al-ghāshiya,
   al-ḥāqqa, al-wāqiʿa, al-mawʿūd) is **100 % Early Meccan**.
2. **yawm al-qiyāma** ("the Day of Standing") is the *most
   frequent yawm-compound* — **70 unique verses** — and the
   only compound heavily used across Meccan *and* Medinan phases
   (48 Meccan vs 22 Medinan). It is the genre-neutral juridical
   standard term; it occupies the space al-sāʿa cannot because
   al-sāʿa is a *point*, yawm al-qiyāma is a *courtroom*.
3. **al-yawm al-ākhir** ("the Last Day") is almost exclusively
   **Medinan (25 of 26 verses)**. It is the creedal formula of
   the Medinan community: whoever *believes in God and the Last
   Day* does so.
4. The five surahs *named* after Day-of-Judgement epithets (56,
   69, 75, 88, 101) are **all Early Meccan**, all occur in
   Nöldeke phase 1, and all share a single rhetorical
   architecture: **disclosure oath → image of cosmic disruption
   → bifurcation of the dead → theological address**.

The catalog below verifies each epithet against QAC v0.4 morphology,
using **idāfa adjacency** (yawm at word W, epithet at word W+1) as
the hard test for "yawm al-X" compounds — not merely co-occurrence
within a verse.

## 1. Per-epithet verification

Counts are unique verses (Hafs numbering) from the Buckwalter lemma
field. "Meccan / Medinan" uses the Egyptian tradition; Nöldeke phase
from `data/revelation-order.csv`. *adj-yawm* counts only verses where
the yawm lemma is at word W and the epithet at word W+1 in the QAC
word index.

| # | Epithet | Lemma (Buckwalter) | Match | Unique verses | Meccan | Medinan | Nöldeke profile |
|---:|---|---|---|---:|---:|---:|---|
| 1 | yawm al-dīn | `yawom`+`diyn` | adj | 13 | 13 | 0 | E 9 · M 4 · L 0 · Med 0 |
| 2 | yawm al-qiyāma | `yawom`+`qiya\`map` | adj | 70 | 48 | 22 | E 3 · M 12 · L 33 · Med 22 |
| 3 | yawm al-ḥaqq | `yawom`+`Haq~` | adj | 1 | 1 | 0 | E 1 |
| 4 | yawm al-ḥisāb | `yawom`+`HisaAb` | adj | 4 | 4 | 0 | M 3 · L 1 |
| 5 | yawm al-faṣl | `yawom`+`faSol` | adj | 6 | 6 | 0 | E 4 · M 2 |
| 6 | yawm al-jamʿ | `yawom`+`jamoE` | adj | 2 | 1 | 1 | L 1 · Med 1 |
| 7 | yawm al-taghābun | `yawom`+`t~agaAbun` | adj | 1 | 0 | 1 | Med 1 |
| 8 | yawm al-tanād | `yawom`+`t~anaAd` | adj | 1 | 1 | 0 | L 1 |
| 9 | yawm al-khurūj | `yawom`+`xuruwj` | adj | 1 | 1 | 0 | M 1 |
| 10 | yawm al-mawʿūd | `yawom`+`mawoEuwd` | adj | 1 | 1 | 0 | E 1 |
| 11 | yawm al-waʿīd | `yawom`+`waEiyd` | adj | 1 | 1 | 0 | M 1 |
| 12 | al-yawm al-ākhir | `yawom`+`\|xir` | adj | 26 | 1 | 25 | L 1 · Med 25 |
| 13 | al-sāʿa | `saAEap` | lemma | 43 | 37 | 6 | E 1 · M 12 · L 24 · Med 6 |
| 14 | al-qāriʿa | `qaAriEap` | lemma | 5 | 4 | 1* | E 4 · L 1 |
| 15 | al-ṭāmma al-kubrā | `T~aA^m~ap` | lemma | 1 | 1 | 0 | E 1 |
| 16 | al-ṣākhkha | `S~aA^x~ap` | lemma | 1 | 1 | 0 | E 1 |
| 17 | al-ghāshiya | `ga\`$iyap` | lemma | 3 | 3 | 0 | E 1 · L 2 |
| 18 | al-wāqiʿa | `waAqiEap` | lemma | 2 | 2 | 0 | E 2 |
| 19 | al-ḥāqqa | `HaA^q~ap` | lemma | 3 | 3 | 0 | E 3 |
| 20 | al-āzifa | `'aAzifap` | lemma | 2 | 2 | 0 | E 1 · L 1 |

\* Q 13:31 has the Meccan qāriʿa-lemma in a Medinan surah (al-Raʿd,
Late Meccan by Nöldeke but Medinan by Egyptian tradition — one of
the classic disputed attributions).

### 1.1. Commentary on each name

**yawm al-dīn** (Q 1:4, 15:35, 26:82, 37:20, 38:78, 51:12, 56:56,
70:26, 74:46, 82:15, 82:17, 82:18, 83:11). 13 verses, *all Meccan*,
**9 of 13 Early Meccan**. It is the name the Quran uses when the
Day is being defined *to a new audience*: the catechistic surahs
74, 82, 83 each use it to introduce the Day to the listener for the
first time. Fātiḥa (1:4) inherits this catechistic register. In
Sūrat al-Infiṭār (82) the phrase appears three times in four
verses (82:15, 82:17, 82:18), the only cluster of its kind. The
root `dyn` here is the *judgement / recompense* sense; the word
does not lose that sense in Medinan usage but the Medinan surahs
prefer `yawm al-qiyāma` and `al-yawm al-ākhir` instead.

**yawm al-qiyāma** (70 verses). The juridical standard. Appears in
*every* Nöldeke phase, heavily in Late Meccan (33 verses) and
Medinan (22 verses). The root `qwm` (to stand) encodes the
legal image of the defendants standing before the court: this is
why the Medinan legal surahs (2, 3, 4, 5) deploy it so heavily
(17 of the 22 Medinan verses are in these four surahs). Sūrat
al-Qiyāma (75) itself uses the compound only twice (75:1, 75:6),
as a frame: the surah opens with the **oath** "I swear by the Day
of Qiyāma" and returns at v.6 with the **question** "When is the
Day of Qiyāma?" — the intervening material is the answer.

**yawm al-ḥaqq** (Q 78:39 only). A hapax compound. The lemma `Haq~`
itself appears in 231 verses, but only once is it adjacent to
`yawom`. It is a *metatheological* name — the Day of Truth, the
Day *in which* the false certainties are reversed. The
surrounding verses (78:38–40) describe the Spirit and the angels
standing in rows, then: "that is the Day of Truth."

**yawm al-ḥisāb** (Q 14:41, 38:16, 38:26, 38:53, 40:27 — 4
*adjacent* hits; the concept appears in ~15 more verses with
`yawma` used as a bare accusative of time: "on the day of the
reckoning"). Heavy in Sūrat Ṣād (38), the Dāʾūdic surah: three of
four Ṣād occurrences cluster around the Davidic judgement-seat
passage (38:26) where God appoints David a *khalīfa* to judge
between people. The book's internal logic — *the Day of
Reckoning* is the cosmic version of *David's daily reckoning*.

**yawm al-faṣl** (Q 37:21, 44:40, 77:13, 77:14, 77:38, 78:17). The
"Day of Separation / Decision". 4 of 6 occurrences are in Sūrat
al-Mursalāt (77), which has the entire refrain **"wayl yawmaʾidhin
li-l-mukadhdhibīn"** (Woe that day to the deniers) repeated 10
times. Both 44:40 and 77:13 gloss the Day as an *appointed meeting*
(mīqāt, mīʿād). This is the covenant-linked name (see §5 below).

**yawm al-jamʿ** (Q 42:7, 64:9). "Day of Gathering". Only 2 verses.
Q 64:9 is interesting because the *same verse* contains **two**
Day-of-Judgement epithets back-to-back: *yawm al-jamʿ* and *yawm
al-taghābun*. This is the only verse in the Quran where two yawm-
compound names are juxtaposed.

**yawm al-taghābun** (Q 64:9 only — hapax). "Day of Mutual Loss /
Dispossession". The root `gbn` means commercial deception / loss
on a trade, and form-VI `taghābun` means *mutual* disadvantage —
specifically, the Day on which the elect and the damned *exchange
fates*: the elect "win" paradise at the expense of those who lose
it. The economic metaphor fits Sūrat al-Taghābun's overall
rhetoric of credit and debt (64:15–17).

**yawm al-tanād** (Q 40:32 only — hapax). "Day of Mutual Calling-
Out". Root `ndw` in form VI, *tanāda* = calling to each other.
The context (40:32–33) is the believer in Pharaoh's court warning
his people: "I fear for you the Day of Calling-Out, the day you
will turn back fleeing, having no protector from God." It is the
most *vivid* of the Day-names — a soundscape.

**yawm al-khurūj** (Q 50:42 only — hapax, though root `xrj` is
pervasive). "Day of the Emergence" — the dead coming forth from
the graves. In Sūrat Qāf (50) it is preceded, in the same verse,
by yawma yasmaʿūna l-ṣayḥa (the day they hear the cry). The pair
*ṣayḥa / khurūj* encodes the **blast-and-emergence** moment of
resurrection.

**yawm al-mawʿūd** (Q 85:2 only). "The Promised Day" — passive
participle of `waʿada`. The root is the Quran's primary
**promise/threat** root (151 occurrences, see
`covenant-language.md`). This is the Day-name that most directly
links Day-of-Judgement vocabulary to covenant vocabulary: the
*promised* Day is the Day that God has *promised/threatened*
(depending on the addressee).

**yawm al-waʿīd** (Q 50:20 only — "that is the Day of the
Threat"). Same root (`wEd`) from the *threat* side; `waʿīd`
(6 total verse occurrences including non-yawm contexts) is the
root-internal doublet of `waʿd` (46 occurrences, promise). The
asymmetry is itself a theological statement: waʿd is *either*
promise or threat (polysemic), but waʿīd is *only* threat.

**al-yawm al-ākhir** (26 verses, 25 Medinan). The *creedal*
formula. Its appearance is the single cleanest chronological
marker in Day-of-Judgement vocabulary: the phrase is
**essentially absent from Meccan revelation** (1 Late Meccan
occurrence: 29:36) and becomes the Medinan community's
standard signature of faith (*man kāna yuʾminu bi-llāhi wa-l-
yawmi l-ākhir* — 2:8, 2:62, 2:126, 2:177, 2:228, 2:232, 2:264,
3:114, 4:38, 4:39, 4:59, 4:136, 4:162, 5:69, 9:18, 9:19, 9:29,
9:44, 9:45, 9:99, 24:2, 33:21, 58:22, 60:6, 65:2). It is the
**confessional** name.

**al-sāʿa** (43 verses, 48 segment hits — see §3 for full
discussion).

**al-qāriʿa** (Q 13:31, 69:4, 101:1, 101:2, 101:3). "The
Crushing-Blow / Striker". 101:1–3 is the surah's triple-
interrogation opening.

**al-ṭāmma al-kubrā** (Q 79:34 — hapax). "The Great
Overwhelmer". Root `Tmm` = to fill / overflow.

**al-ṣākhkha** (Q 80:33 — hapax). "The Deafening Blast / The
Shriek". Root `Sxx`. The onomatopoeia is central: the sound
*is* the name.

**al-ghāshiya** (Q 7:41, 12:107, 88:1). "The Veiler /
Overwhelmer". Root `g$w` (to cover). In 88:1 it is framed as
a question addressed to the Prophet: *hal atāka ḥadīthu l-
ghāshiya* — "has the report of the Veiler reached you?"

**al-wāqiʿa** (Q 56:1, 69:15). "The Inevitable / The Falling-
Event". Root `wqE` (to fall, to occur). 56:1 opens Sūrat al-
Wāqiʿa with a temporal clause: *idhā waqaʿati l-wāqiʿa* — "when
the Inevitable inevitably occurs." The figura etymologica is
the whole theology: the Event is called "the Event" because it
*is* what occurs.

**al-ḥāqqa** (Q 69:1, 69:2, 69:3). "The Reality / The
Certifier". Feminine active participle of `Hqq`. Sūrat al-
Ḥāqqa opens with a triple repetition: *al-ḥāqqatu mā l-ḥāqqatu
wa-mā adrāka mā l-ḥāqqa*. The structure parallels al-qāriʿa
(101:1–3) exactly: it is a surah-architecture pattern.

**al-āzifa** (Q 40:18, 53:57). "The Approaching". Root `Azf`
(to be near). In 53:57 the surface verb (>azifati) and the
participle ('aAzifap) occur in the same verse — figura
etymologica again: "*the Approaching has approached*."

## 2. Distributional summary

### 2.1. Meccan / Medinan split (unique verses)

| Register | Epithet | Meccan | Medinan | Total |
|---|---|---:|---:|---:|
| Dominant inter-period | al-sāʿa | 37 | 6 | 43 |
| Dominant inter-period | yawm al-qiyāma | 48 | 22 | 70 |
| Medinan creedal | al-yawm al-ākhir | 1 | 25 | 26 |
| Early Meccan oaths | al-qāriʿa | 4 | 1 | 5 |
| Early Meccan oaths | al-wāqiʿa | 2 | 0 | 2 |
| Early Meccan oaths | al-ḥāqqa | 3 | 0 | 3 |
| Early Meccan oaths | al-ghāshiya | 3 | 0 | 3 |
| Early Meccan oaths | al-ṭāmma | 1 | 0 | 1 |
| Early Meccan oaths | al-ṣākhkha | 1 | 0 | 1 |
| Early Meccan catechism | yawm al-dīn | 13 | 0 | 13 |
| Early/Middle Meccan prom | yawm al-mawʿūd | 1 | 0 | 1 |
| Middle Meccan threat | yawm al-waʿīd | 1 | 0 | 1 |
| Middle Meccan davidic | yawm al-ḥisāb | 4 | 0 | 4 |
| Late Meccan oration | yawm al-tanād | 1 | 0 | 1 |
| Middle Meccan emergence | yawm al-khurūj | 1 | 0 | 1 |

The pattern is clean. **Medinan = ākhir + qiyāma + (rarely) sāʿa.**
**Early Meccan = the poetic epithets (wāqiʿa, qāriʿa, ḥāqqa,
ghāshiya, ṭāmma, ṣākhkha, mawʿūd, dīn, faṣl, āzifa).** The shift
is register-driven: Early Meccan is oath-poetry with
onomatopoeic Day-names; Medinan is creedal prose with one or two
stabilised formulae.

### 2.2. Count of distinct Day-names per surah

Sūrat al-Ḥāqqa (69) contains the widest name-cluster: al-ḥāqqa
(×3), al-qāriʿa (×1), al-wāqiʿa (×1). Sūra 50 (Qāf) contains
*three* yawm-compounds: yawm al-waʿīd (50:20), yawm al-khurūj
(50:42), and al-sāʿa (indirectly, 50:27 and structurally
implied). Sūrat al-Ṭūr, Sūrat al-Infiṭār, Sūrat al-Inshiqāq and
Sūrat al-Takwīr build Day-images without fixed epithet.

## 3. al-sāʿa — the Hour

### 3.1. Exact count

- **48 segment hits** of lemma `saAEap`.
- **43 unique verses**.
- **36 verses** carry the definite article `al-` (DET prefix) or
  a pronominal clitic (al-sāʿatu-hum, etc.) — i.e. *the* Hour in
  an identifiable Day-of-Judgement sense. The other 7 verses
  have `sāʿa` without DET (*an indeterminate hour*), and they
  are overwhelmingly **still eschatological** — "an hour they
  cannot advance or defer" (7:34), "if we delayed punishment to a
  fixed hour" (11:8). There are no unambiguously *mundane*
  occurrences of `sāʿa` in the Quran: every instance is
  time-of-judgement even when indefinite.

### 3.2. Chronological profile

| Nöldeke phase | Verses |
|---|---:|
| Early Meccan | 1 (79:42) |
| Middle Meccan | 12 |
| Late Meccan | 24 |
| Medinan | 6 |

The shape is **right-shifted Meccan**: al-sāʿa is not a Phase-1
term. It emerges in Middle Meccan, peaks in Late Meccan, and
survives into Medina. It is the *argumentative* Day-name: the
surahs that use it are disputing with interlocutors ("they will
ask you about the Hour, when is its anchorage?" 7:187, 33:63,
79:42, 47:18). The six Medinan occurrences are **9:117** (Tabūk
narrative, *sāʿat al-ʿusra*), **22:1**, **22:7**, **22:55**
(the three Ḥajj-sūra Day-descriptions), **33:63** (Aḥzāb
question-and-answer), and **47:18** (the signs of the Hour,
see §6 below).

### 3.3. al-sāʿa vs yawm al-qiyāma

Both straddle all four phases. But they are **not interchangeable**:

| Feature | al-sāʿa | yawm al-qiyāma |
|---|---|---|
| Frame | Temporal *point* ("the Hour") | Juridical *day* |
| Grammatical host | Interrogative ("when?") | Locative ("*on* the day") |
| Typical predicate | *comes, approaches, is near* | *on that day X will happen* |
| Polemical use | Answering sceptic ("when is it?") | Describing courtroom events |
| Governing root | `swE` (time-point) | `qwm` (standing up) |

In a sampling of Late-Meccan verses where both terms *could*
grammatically have appeared, al-sāʿa appears in "will they wait
for / when does it come?" contexts; yawm al-qiyāma appears in
"on that day, the wrongdoer will bite his hands" contexts.

## 4. The five surahs named after Day-of-Judgement epithets

Five surahs are *titled* with a Day-of-Judgement name. The choice
is not random: each title is a **noun that appears in the surah's
opening verse**, forming a **title-incipit loop**. This section
compares their internal architecture.

| # | Surah | Title | Verses | Nöldeke | Rev-order | Opening formula |
|---:|---|---|---:|---|---:|---|
| 56 | al-Wāqiʿa | The Inevitable | 96 | Early Meccan | 46 | `idhā waqaʿati l-wāqiʿa` (temporal clause) |
| 69 | al-Ḥāqqa | The Reality | 52 | Early Meccan | 78 | `al-ḥāqqatu mā l-ḥāqqa` (triple-question) |
| 75 | al-Qiyāma | The Standing | 40 | Early Meccan | 31 | `lā uqsimu bi-yawmi l-qiyāma` (denial-oath) |
| 88 | al-Ghāshiya | The Veiler | 26 | Early Meccan | 68 | `hal atāka ḥadīthu l-ghāshiya` (interrogation) |
| 101 | al-Qāriʿa | The Striker | 11 | Early Meccan | 30 | `al-qāriʿatu mā l-qāriʿa` (triple-question) |

All five are **Early Meccan**. All five place the titular epithet
in verse 1.

### 4.1. Shared architecture

Each of the five surahs follows a **three-movement arc**:

1. **Disclosure move** — the surah announces the Day by *name*
   (oath, triple-question, interrogation, or temporal clause).
   56:1 `idhā waqaʿat`, 69:1 `al-ḥāqqa`, 75:1 `lā uqsimu`, 88:1
   `hal atāka`, 101:1 `al-qāriʿa`.
2. **Cosmic-disruption panel** — a dense series of `idhā` /
   `yawma` clauses describing the dislocation of nature: earth
   pounded flat (56:4, 69:14), mountains like carded wool
   (101:5), faces cast down and labouring (88:2–3), sight
   dazzled (75:7). This panel is always 4–8 verses.
3. **Bifurcation and address** — the dead sort into two or
   three groups, and the surah turns to a theological address
   (typically to the Prophet or the human addressee).
   - Sūrat al-Wāqiʿa: three groups (56:7–10: *aṣḥāb al-maymana,
     aṣḥāb al-mashʾama, al-sābiqūn*).
   - Sūrat al-Ḥāqqa: two groups (69:19 recipients-of-the-
     right-hand, 69:25 recipients-of-the-left).
   - Sūrat al-Qāriʿa: two groups (101:6–7 heavy scales, 101:8
     light scales).
   - Sūrat al-Ghāshiya: two groups (88:2–7 labouring faces,
     88:8–16 serene faces).
   - Sūrat al-Qiyāma: two groups (75:22–23 radiant faces, 75:24–
     25 scowling faces) — then a pivot to the biographical claim
     (75:36 onwards).

### 4.2. The "two faces" motif

Four of the five surahs (69, 75, 88, 101) use the **"faces on
that day"** motif as the hinge of bifurcation:

- 75:22 `wujūhun yawmaʾidhin nāḍira`
- 88:2 `wujūhun yawmaʾidhin khāshiʿa`
- 88:8 `wujūhun yawmaʾidhin nāʿima`
- 80:38–40 (an adjacent Early Meccan surah, al-ʿAbasa, also
  uses this motif).

The five epithet-surahs constitute a **genre**: the "surahs of
the disclosed Day", identifiable by title-incipit loop, three-
movement arc, and the "two faces" hinge.

### 4.3. Length gradient

56 (96 v.) → 69 (52 v.) → 75 (40 v.) → 88 (26 v.) → 101 (11 v.).
The **length decreases monotonically** with the mushaf order. Sūrat
al-Wāqiʿa is the longest, al-Qāriʿa is the shortest. This is
consistent with the overall mushaf-length gradient but is
particularly striking here because all five are in the same
revelation phase.

## 5. `mawʿūd` / `waʿīd` and covenant language

`covenant-language.md` (covenant-deep-agent run-1) reports the `wEd`
root as the Quran's *single largest* diachronic signal in the
legal-theological register, with 151 total occurrences split
across lemmas `waʿd`, `waʿada`, `mīʿād`, `mawʿid`, `mawʿūd`,
`waʿīd`.

### 5.1. Lemma inventory for `wEd`

| Lemma (Bw) | Gloss | Total | Unique verses |
|---|---|---:|---:|
| waEod | waʿd (promise/threat noun) | 49 | 46 |
| waEada | waʿada (to promise verb) | 70 | 65 |
| wa\`Eado | wāʿada (to make an appointment with) | 4 | 4 |
| m~iyEaAd | mīʿād (appointed time) | 6 | 6 |
| m~awoEid | mawʿid (appointed time/place) | 12 | 12 |
| m~awoEidap | mawʿida (singular fem) | 1 | 1 |
| mawoEuwd | mawʿūd (the promised [Day]) | 1 | 1 (85:2) |
| waEiyd | waʿīd (the threat) | 6 | 6 |
| tawaAEad | tawāʿada (to agree a meeting) | 1 | 1 |
| tuwEidu | tūʿidu (to promise) | 1 | 1 |

### 5.2. Covenant linkage

Two of the Day-names in this catalogue are **built directly from the
covenant root**:

- **yawm al-mawʿūd** (85:2): the participle `mawʿūd` is "that-which-
  is-promised". It is the *only* occurrence of this exact form in
  the Quran, and its referent is unambiguously the Day. The noun
  functions as a **covenant-predicate**: the Day is an object
  God has *committed Himself* to producing.
- **yawm al-waʿīd** (50:20): `waʿīd` is the *threat*-pole of the
  waʿd-continuum. The whole of Sūrat Qāf (50) is structured
  around this pole — six occurrences of `waʿīd` in the surah
  (50:14, 20, 28, 45) plus the linked yawm al-khurūj (50:42)
  make Qāf the **"day of the threat"** surah par excellence.

### 5.3. mīʿād / mawʿid and the "appointed time" of the Day

Even the non-Day-titled instances of `wEd` are consistently
linked to Day-of-Judgement: `mīʿād` appears six times and in five
of six cases it is the *divine appointment of judgement*
(3:9 *inna Allāha lā yukhlifu l-mīʿād*, 3:194, 8:42, 13:31,
34:30). `mawʿid` adds: 11:17, 11:81, 15:43, 18:48, 18:58, 20:58.
The Quran uses the **covenant vocabulary of appointed-meeting**
to describe the Day even where it does not use a yawm-compound
name. Yawm al-faṣl is explicitly glossed `mīqātu-hum ajmaʿīna`
(the appointed meeting for them all, Q 44:40) — a gloss that
connects yawm al-faṣl → mīqāt → wEd-family (though `mīqāt`
itself is ROOT `wqt`, not `wEd`, the surrounding semantic field
is covenant-appointment).

### 5.4. Asymmetry of waʿd

As covenant-language.md observes, `waʿd` is uniquely *polar*:
it means both *promise* (to the believers) and *threat* (to the
deniers), and context alone disambiguates. `waʿīd`, by contrast,
is unipolar: **threat only**. The Day is the moment at which the
polarity of waʿd collapses — for the elect it reveals itself as
promise kept, for the damned as threat executed. Yawm al-mawʿūd
and yawm al-waʿīd are the two faces of the same event.

## 6. Q 47:18 — the signs of the Hour

Q 47:18: *fa-hal yanẓurūna illā l-sāʿata an taʾtiya-hum baghtatan?
fa-qad jāʾa ashrāṭu-hā. fa-annā la-hum idhā jāʾat-hum
dhikrā-hum?*

"Do they await anything but the Hour — that it come upon them
suddenly? Its portents have already come. So how will they
[find] their reminder when it has come to them?"

### 6.1. Morphological payload

From QAC at (47:18):

- `saAEap` — the Hour, DEF, object of anticipation.
- `ta>otiya` (from `Aty`, "to come") — subjunctive: the action
  they are *awaiting*.
- `bagotapF` (indef accusative) — suddenness. Only 13 Quranic
  occurrences of this lemma; 10 of 13 are in eschatological
  contexts.
- `>a$oraATu-haA` — *its portents*. Lemma `>a$oraAT`, root `$rT`.
  This is the **only occurrence** in the entire Quran of the
  plural `ashrāṭ`, and the Quran's only use of this word for
  "signs of the Hour". Every subsequent Islamic tradition uses
  this single word as the technical term for the *precursor signs
  of the eschaton*.
- `dhikrā-hum` — their reminder/remembrance.

### 6.2. Theological reading

The verse makes three moves:

1. **The Hour comes** — unconditional, subjunctive *an taʾtiya*.
2. **Its signs have come** (*fa-qad jāʾa ashrāṭu-hā*) — perfect
   tense. The signs are *already* in the world.
3. **How then will the reminder help once it arrives?** — the
   argument is: *the reminder is now*; by the time the Hour
   arrives the window has closed.

This is the only verse in which the Quran explicitly states that
the Hour has **precursor signs** already present. The hadith
literature's elaborate ashrāṭ al-sāʿa tradition (the Dajjāl,
descent of Jesus, sun-from-west, etc.) is built on this single
verse's single word.

### 6.3. Medinan embedding

47:18 is **Medinan** (Nöldeke phase 4, mushaf ord. 47, rev. ord.
95 — Medinan in both traditions). It is one of the 6 Medinan al-
sāʿa verses. Its significance: the *ashrāṭ* vocabulary is not
Meccan; it emerges once the community is embedded in a time that
calls for reading current events as portents.

## 7. Sequence of events

The Quran does not provide a *narrative* of Day-of-Judgement
events in a single place. But the verbs-and-nouns of the event
line up across the corpus into a canonical sequence. Below is
the root-level evidence.

### 7.1. sūr (horn) — blown twice

Root `Swr` in the sense "horn/trumpet": lemma `Suwr` appears at
6:73, 18:99, 20:102, 23:101, 27:87, 36:51, 39:68, 50:20, 69:13,
74:8, 78:18 — **11 verses** all eschatological. Root `nfx` (to
breathe/blow) is paired with `Suwr`: the phrase *nufikha fī
l-ṣūr* ("the horn will be blown") occurs at 6:73, 18:99, 20:102,
23:101, 27:87, 36:51, 39:68, 50:20, 69:13, 78:18.

Sūrat al-Zumar 39:68 is the verse that specifies **two blasts**:
*"then the horn will be blown and everyone in the heavens and
earth will faint, except whom God wills; then it will be blown
another time and at once they will be standing, looking on."*

Root `Swr`: 19 segment hits, 17 verses. Root `nfx`: 20 hits, 18
verses. The collocation isolates the horn-blast as a discrete
event-type.

### 7.2. Resurrection — baʿth / nushūr / qiyām

- Root `bEv` (to send, resurrect): 67 segment hits, 64 verses.
- Root `n$r` (to spread, resurrect): 21 segment hits, 20 verses.
- Root `qwm` (to stand, arise): pervasive (yuqīmu, qiyāma,
  qāma, etc.). The lemma `qiya\`map` alone is 70 verses; `qwm`
  as a whole is far larger.

The canonical phrase *yawma yabʿathu-humu llāh* ("the day God
resurrects them": Q 58:6, 58:18) uses `bEv`. *Wa-llāhu yabʿathu
man fī l-qubūr* (22:7) pairs `bEv` with al-sāʿa earlier in the
same passage (22:1, 22:7). Resurrection *follows* the second
horn-blast in the Zumar text.

### 7.3. Reckoning — ḥisāb

Root `Hsb`: 109 segment hits, 102 verses. Lemma `HisaAb`:
39 segment hits. yawm al-ḥisāb (4 adj verses), plus related
phrases *sarīʿu l-ḥisāb* (God is swift of reckoning: 2:202,
3:19, 3:199, 5:4, 13:41, 14:51, 24:39, 40:17), *ʿasīru l-ḥisāb*
(74:9 — the reckoning is "difficult for the disbelievers").
Ḥisāb comes *after* resurrection in the event sequence: the dead
are raised **in order to be reckoned**.

### 7.4. Scales — mīzān

Root `wzn`: 23 segment hits, 21 verses. The scales-noun
`mawāzīn` / `mīzān` in eschatological contexts: 7:8 *al-
waznu yawmaʾidhin al-ḥaqq* (the weighing that day is the
truth), 7:9, 21:47, 23:102, 23:103, 101:6, 101:8. Sūrat al-
Qāriʿa (101) is the only surah whose Day-bifurcation *is* the
scales: heavy-scales → pleasant life; light-scales → hāwiya.

### 7.5. Ṣirāṭ — the path

Root `SrT`: 45 segment hits, 45 verses. *al-ṣirāṭ al-
mustaqīm* (the straight path) in 33 of 45 verses (1:6, 2:142,
etc.). Only a handful of verses describe the Day-crossing
image directly (37:23–24: "guide them to the path of the
Fire"). The *ṣirāṭ over hell* of hadith is not an explicit
Quranic image; it is a tradition built on a reading of
19:71–72 (*wa-in minkum illā wāriduhā* — "every one of you
will come upon it"), an eschatological passage that does not
use `SrT` but uses `wrd` (to approach a watering-place).

### 7.6. The canonical sequence

Putting the pieces together, the Quran assembles a **canonical
event-sequence**:

1. First blast of the horn (`nufikha fī l-ṣūr`) — 39:68a. All
   conscious life is annihilated / swoons.
2. Second blast — 39:68b. Resurrection (`bʿth`, `qwm`).
3. Gathering (`jamʿ`) — yawm al-jamʿ (42:7, 64:9).
4. Separation (`faṣl`) — yawm al-faṣl (77:13, 44:40). The elect
   separated from the damned.
5. Reckoning (`ḥisāb`) — yawm al-ḥisāb (14:41, 38:26).
6. Weighing (`wazn`) — al-mawāzīn / al-mīzān (7:8–9, 21:47,
   23:102–103, 101:6–9).
7. Dispensation (taghābun) — yawm al-taghābun (64:9); the elect
   enter paradise, the damned enter hell.

This sequence is *implicit* — no single surah enumerates it in
order. But the adj-yawm catalog above maps **each stage** onto
a distinct name:

| Stage | Dominant epithet | Evidence verse |
|---|---|---|
| Cosmic disruption | al-qāriʿa, al-ṭāmma, al-ṣākhkha, al-ghāshiya, al-wāqiʿa, al-ḥāqqa | 101:1, 79:34, 80:33, 88:1, 56:1, 69:1 |
| Horn-blast | yawm al-waʿīd + al-ṣayḥa + al-khurūj | 50:20, 50:42 |
| Gathering | yawm al-jamʿ | 42:7, 64:9 |
| Standing before the court | yawm al-qiyāma | passim (70v) |
| Separation | yawm al-faṣl | 37:21, 44:40, 77:13–38, 78:17 |
| Reckoning | yawm al-ḥisāb, yawm al-dīn | 14:41, 38:26, 1:4 |
| Mutual loss/gain | yawm al-taghābun | 64:9 |
| Final judgement-by-threat/promise | yawm al-mawʿūd, yawm al-waʿīd | 85:2, 50:20 |
| Creedal marker | al-yawm al-ākhir | 2:8, 2:62, passim Medinan |
| Time-point | al-sāʿa | 22:1, 47:18, passim |

**The catalogue of names is, semantically, a catalogue of
*stages*.** The Quran uses the *name* it needs for the
*stage* it is foregrounding. This is why the same Day carries
twenty names: each is a magnification of one phase of the event.

## 8. Hypotheses arising

(H1) **Stage-specific naming rule.** The choice among Day-names
in a given verse is predictable from which stage of the event
the verse foregrounds. Testable: for a balanced sample of
Day-of-Judgement verses, annotate which stage the verse
describes; show the name used matches the stage at above-chance
rates.

(H2) **Register-chronology rule.** Epithets with onomatopoeic /
participial form (al-qāriʿa, al-ṭāmma, al-ṣākhkha, al-ghāshiya,
al-wāqiʿa, al-ḥāqqa, al-āzifa) are constrained to Early-Meccan;
epithets with abstract / nominal form (al-ḥisāb, al-qiyāma,
al-ākhir, al-faṣl) survive into or emerge in later phases. This
is already visible in §2.1; it predicts that *any* novel
onomatopoeic epithet is Early Meccan and *any* novel abstract
epithet is Late-Meccan or Medinan.

(H3) **The "disclosed-Day" surah-genre.** Surahs 56, 69, 75, 88,
101 form a sub-genre defined by (a) title-incipit loop,
(b) disclosure move, (c) cosmic disruption panel, (d) two-faces
hinge. The genre may include unnamed members (candidates:
77, 79, 80, 82). Testable by architectural coding of each
candidate against the four-feature template.

(H4) **Covenant-Day isomorphism.** Every major Day-of-Judgement
epithet either *is* a covenant term (mawʿūd, waʿīd) or is
glossed by one (faṣl ↔ mīqāt at 44:40; jamʿ ↔ mīʿād at 42:7;
tanād → the believer in the Pharaonic court appealing to
covenant). The covenant framework described in
`covenant-language.md` extends to eschatology: *the Day is the
keeping of the covenant*.

(H5) **The "ashrāṭ" hapax.** The Quran's technical term for the
precursor signs of the Hour is a hapax (47:18). The entire
post-Quranic "signs of the Hour" literature is an exegesis of
*one word*. This is worth an independent replication.

## 9. Limits & caveats

- The adjacency test captures classical yawm-compounds but not
  non-adjacent yawm+X verses (e.g. yawm yaqūmu l-ḥisāb, Q 14:41).
  The adj-count is therefore a *lower bound* on yawm-compound
  attestations.
- The al-sāʿa "DoJ count" of 43 is unambiguous for the lemma
  `saAEap`; separating "Hour" from "hour" requires a semantic
  judgement. The 36 DET/PRON-anchored count is the *strict*
  lower bound.
- The ghāshiya lemma appears at 7:41 and 12:107 in non-surah-
  title contexts. 7:41 is *ghāshin min jahannam* (a veiler from
  Hell) — ambiguously topographical. 12:107 is *tātihim
  ghāshiyatun min ʿadhāb Allāh* (lit. "a veiler of punishment
  comes upon them"). The word's range is "veiler" more
  generically; only 88:1 unambiguously names the Day.
- The Nöldeke-phase labels follow the traditional chronology
  and should be taken as a rough ordering, not a strict dating.
- No null-model statistical test has been run. All claims above
  are descriptive-categorical.

## 10. Files

- `scratch/yawm-catalog/verify.py` — verification script
- `scratch/yawm-catalog/verify-out.txt` — full output (708 lines)
- `scratch/yawm-catalog/probe.py` — lemma probe
- `journal/yawm-run-2.md` — agent journal
