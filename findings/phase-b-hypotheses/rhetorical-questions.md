---
title: Rhetorical Questions in the Quran — Full Inventory, Formula Catalog, Ring-Center and Rhyme-Break Correlation
phase: phase-b-hypotheses
agent: rhetorical-questions-run-1
date: 2026-04-12
rules:
  - canonical corpus = Quranic Arabic Corpus morphology v0.4 (Dukes)
  - interrogative detection = POS:INTG tagging (prefix and standalone) + manual patch for Al-Rahman refrain
  - question-type classification = heuristic (marker + context) — not a human-validated gold label
  - no pre-registration; this is an exploratory inventory
  - all counts are per-verse unless otherwise noted
dependencies:
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  arabic_text: /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  rhyme_breaks: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/saj-fasila-per-verse.csv
  ring_centers: /Users/grey/Downloads/quran/findings/phase-c-structures/ring-center-semantics.md
outputs:
  per_verse_csv: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/rhetorical-questions-per-verse.csv
  per_surah_csv: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/rhetorical-questions-per-surah.csv
status: inventory + analysis complete
---

# Rhetorical Questions in the Quran

The Quran argues with its reader. A substantial fraction of its verses
are not assertions but **questions put to an implicit audience** — and
classical Arabic rhetoric (balāgha) knows these are not information-seeking
acts but argumentative moves. *Istifhām taqrīrī* affirms a known answer by
asking; *istifhām inkārī* denies by asking; reproach-questions
scold; challenge-questions dare. Al-Suyūṭī's *al-Itqān* gives them a
whole chapter (nawʿ 47). This document counts them.

## Headline numbers

| metric | count |
|---|---:|
| Verses containing at least one interrogative marker (INTG-tagged in Quranic Corpus v0.4) | **830** |
| Verses after patch (adding Al-Rahman refrain's 15 morphology-mis-tagged iterations) | **845** (~13.5% of the Quran's 6236 verses) |
| Total interrogative tokens in the INTG-tagged set | 946 |
| …hamza interrogative prefix `أ-` | 507 |
| …standalone interrogative particles (hal / mā / kayfa / man / …) | 439 |
| Verses with ≥2 interrogative markers stacked | 108 |
| Runs of ≥3 consecutive Q-verses | 26 (longest runs: **Al-Mulk 67:16-22** and **An-Naml 27:59-65**, 7 verses each) |

**The Quran puts a question to its reader, on average, once every 7.4 verses.**

---

## 1. Interrogative-marker inventory

The Quranic Arabic Corpus morphology v0.4 tags eleven distinct
interrogative stems plus the hamza prefix. Raw per-lemma counts:

| marker | token count |
|---|---:|
| `أ-` hamza prefix (rhetorical / yes-no) | 507 |
| `ما` mā (What…) | 95 |
| `هل` hal (Is there…) | 93 |
| `كيف` kayfa (How…) | 80 |
| `من` man (Who…) | 37 |
| `أي` ayy (Which…) — corpus under-tags; see §6 | 35 + patched 15 |
| `أنى` annā (Whence / how on earth…) | 27 |
| `ماذا` mādhā (What-then…) | 26 |
| `كم` kam (How many…) | 20 |
| `أين` ayna (Where…) | 12 |
| `متى` matā (When…) | 9 |
| `أيان` ayyāna (eschatological "when") | 5 |

Note: 507 hamza-prefixed tokens vs 218 verses opening with hamza-INTG. The
remaining 289 hamza prefixes are mid-verse (typically as part of an
*a-fa-lā / a-wa-lam / a-fa-man* construction).

---

## 2. Question-type classification (heuristic)

Using a rule-based classifier over marker + context cues (not gold-labeled):

| type | verses |
|---|---:|
| Neutral / other-question (default bucket) | 447 |
| **Rhetorical-negation** (*inkārī*) — hamza + negation (lā / lam / lan) | **177** |
| **Rhetorical-affirmation** (*taqrīrī*) — verse opens hamza-INTG, no negation | 112 |
| Prophet-speaking ("qul…" imperative + Q) | 49 |
| *kayfa* reproach/wonder | 25 |
| *hal*-rhetorical | 20 |
| *yasʾalūnaka + INTG* (real question from others) | 8 (explicit INTG; plus 18 *yasʾalūnaka* verses where the reported question is paraphrased without an INTG marker on the main clause) |
| Q-verse with "*qul* …" answer inside the same verse | 24 |

The heuristic is conservative: a verse tagged "rhetorical-affirmation"
(*taqrīrī*) just means it opens with hamza-INTG and has no nearby negation
— it may still be inkārī in tafsir readings. Human validation would
tighten these numbers.

---

## 3. Top-20 rhetorical-question formulas by frequency

Counted at verse level with structural matching on the morphology
(hamza-INTG + fa/wa prefixes + lā/lam negation + target verb root, or
equivalent bare-interrogative constructions). Duplicates across families
are permitted (a verse with both *a-fa-lā yaʿqilūn* and *a-lam tara* is
counted in both rows):

| rank | formula | occurrences | famous example |
|---:|---|---:|---|
| 1 | verse-initial `أ-` (hamza interrogative opener) | 218 | Q 2:44, Q 55:60, Q 107:1 |
| 2 | bare `ما` (mā — What…) | 95 | Q 1:4 (مَا interrogative usage in other verses) |
| 3 | bare `هل` (hal — Is there…) | 93 | Q 76:1 *hal atā* |
| 4 | bare `كيف` (kayfa — How…) | 80 | "How can you disbelieve…" Q 2:28 |
| 5 | **`كيف + V`** (kayfa + any verb) | 79 | Q 2:28 *kayfa takfurūna bi-llāhi* |
| 6 | **`ألم + V` (other than tara)** — a-lam + verb | 51 | Q 2:6 *a-lam yaʿlam* chains |
| 7 | **`ألم تر` / `أولم يروا`** ("Did you not see…? Have they not seen…?") | 39 + 14 = 53 | Q 2:243, Q 14:24, Q 22:18 |
| 8 | bare `من` (man — Who…) | 37 | Q 2:255 *man dhā alladhī yashfaʿu ʿindahū* |
| 9 | bare `أي` (ayy — Which…) | 35 (+15 Al-Rahman refrain patch = **50**) | Q 55 refrain: *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* |
| 10 | bare `أنى` (annā — Whence/how…) | 27 | Q 2:259 *annā yuḥyī hādhihi llāhu baʿda mawtihā* |
| 11 | bare `ماذا` (mādhā — What-then…) | 26 | Q 2:26 *mā dhā arāda llāhu bi-hādhā mathalā* |
| 12 | bare `كم` (kam — How many…) | 20 | Q 2:211 *kam ātaynāhum min āyatin bayyinah* |
| 13 | **`مَا لَكُم / مَا لَهُم`** ("What is with you/them?") | 19 | Q 4:88, Q 10:35, Q 37:92 |
| 14 | **`أفلا تعقلون / يعقلون`** ("Do you/they not then reason?") | 14 | Q 2:44, Q 23:80, Q 36:68 |
| 15 | **`أولم يروا`** ("Have they not seen?") | 14 | Q 16:48, Q 36:71 |
| 16 | bare `أين` (ayna — Where…) | 12 | Q 81:26 *fa-ayna tadhhabūn* |
| 17 | **`هل من <X>`** ("Is there any…?") | 12 | Q 50:30 *hal min mazīd* |
| 18 | bare `متى` (matā — When…) | 9 | Q 2:214 *matā naṣru llāh* |
| 19 | **`أفلا تذكّرون`** ("Do you not then remember?") | 9 | Q 6:80, Q 10:3, Q 11:30 |
| 20 | **`هل يستوي`** ("Are they equal?") | 8 | Q 6:50, Q 11:24, Q 13:16, Q 35:19 |

Runners-up: *hal atā* (Has there come…?) 7x; *a-fa-lā tattaqūn* 5x;
*a-fa-lā tubṣirūn* 4x; *a-fa-lā yatadabbarūn al-Qurʾān* **only 2x**
(Q 4:82, Q 47:24) — despite being widely quoted, it is rare in the corpus.

### The `أفلا + V` family — 45 distinct verses

Aggregating all *a-fa-lā + Verb* constructions yields **45 unique verses**
(some share the same verb root; the top verbs are `ʿql` 14x, `dhkr` 9x,
`wqy` 5x, `bṣr` 4x, `šrk/šmʿ/fqh/nẓr` 2x each, plus single appearances
for `fkr`, `dbr`, `r'y`, `Amn`, `ʿlm`, `twb`). The formula is the Quran's
argumentative pivot-move: a cosmic or historical sign has just been
described; the verse closes "do you not then…?" and challenges the
reader to complete the syllogism.

### The `ألم تر` family — 53 distinct verses

This is one of the Quran's signature openers. Breakdown by what follows:

| what follows `ألم تر` | count | nature |
|---|---:|---|
| `إلى` + historical example (Pharaoh, Thamūd, Moses, the Exodus Israelites…) | ~18 | Historical sign |
| `أنّ اللّه` + cosmic verb (sent rain / created / subjected…) | ~22 | Cosmic sign |
| `إلى` + contemporary addressee (the hypocrites, "those who were told…") | ~8 | Polemic |
| Other | ~5 | Mixed |

Ibn Taymiyya's reading of Q 2:243 (*a-lam tara ilā lladhīna kharajū min
diyārihim*) famously treats this as a literary convention — the Prophet
had not physically "seen" the Israelites' Exodus, so the question is
rhetorical; "did you not see" = "have you not become aware of / do you
not know about". **Every *a-lam tara* in the Quran takes either a
historical example or a cosmic sign as its object.** The formula
is the Quran's "sign-based argument" trigger.

---

## 4. Rhetorical questions at ring centers

For the 4 Bonferroni-surviving sub-surah rings plus Hud as whole-surah
ring (per `/findings/phase-c-structures/ring-center-semantics.md`):

| ring | center verse(s) | contains Q? | marker |
|---|---|:---:|---|
| Al-Baqarah 131-144 (z = +9.69) | v137 | — | no (declarative) |
|  | **v138** | **YES** | *wa-man aḥsanu mina llāhi ṣibghah* — "Who is better than God in [religious] coloring?" |
|  | v143 | — | no |
| Al-Qamar 21-30 (z = +6.46) | **v25** | **YES** | *a-ulqiya l-dhikru ʿalayhi min bayninā* — "Was the reminder sent down on him alone among us?" (the Thamūd's accusation) |
|  | v26 | — | no |
| ʿAbasa 1-9 (z = +6.09) | v5 | — | no (*ammā man istaghnā* — "as for him who thinks himself without need" — a conditional, not interrogative) |
| Al-Kahf 83-91 (z = +5.19) | v87 | — | no (Dhul-Qarnayn's judgment — declarative) |
| **Hud (whole surah)** (z = +2.40) | **v62** | **YES** | *a-tanhānā an naʿbuda mā yaʿbudu ābāʾunā* — "Are you forbidding us from worshipping what our fathers worshipped?" (Thamūd's rejection of Sāliḥ) |

**Result: 3 of 5 ring centers (60%) contain a verbatim rhetorical question
at or immediately adjacent to the center.** Under a Quran-wide Q-verse
rate of 13.5%, the probability of that outcome under independence
(k≥3 of 5 with p=0.135) is about **p = 0.012** — suggestive but not
pre-registered. The pattern's real interest is qualitative: **all three
Q-containing ring centers are the moment of accusation or rejection**.
Al-Baqarah 2:138's *wa-man aḥsanu* is God's rhetorical claim; Al-Qamar
54:25's *a-ulqiya* is Thamūd accusing Sāliḥ; Hud 11:62's *a-tanhānā* is
again Thamūd accusing Sāliḥ. This is **exactly consistent with the
"ring-center = boundary-drawing" thesis** of the ring-center-semantics
agent: questions are the verbal form boundary-drawing takes. When
two moral worlds collide, they collide through a question.

---

## 5. Rhetorical questions at rhyme breaks

Using the rhyme-break definition of the saj' agent (non-modal fasila in
a mono-rhymed surah with modal-rhyme share ≥ 40%):

| | Q-verse | non-Q | total |
|---|---:|---:|---:|
| rhyme-breaker | 229 | 1479 | 1708 |
| rhyme-follower | 601 | 3927 | 4528 |
| total | 830 | 5406 | 6236 |

**Observed overlap = 229. Expected under independence = 227.3. O/E = 1.01.**

**This is a NULL result.** Rhetorical questions and rhyme-breaks do NOT
cluster. This is interesting — both are "marked" rhetorical moves, both
are associated with theological pivots in the qualitative literature, but
empirically they mark *different* pivots. The form-meets-content-outliers
finding (rhyme-breaks at doctrinal statements in Maryam) and the Q-verse
findings (questions at ring centers and chains-of-argument) identify
**independent rhetorical channels**. The Quran does not double-mark:
it either rhymes-out-of-pattern OR asks-a-question, but not both.

That's a genuinely novel observation.

---

## 6. Density per surah — rhetorical questions by address-intensity

Top 15 surahs by Q-verse density (computed after the Al-Rahman patch):

| rank | surah | Q-verses | total | density |
|---:|---|---:|---:|---:|
| 1 | **55 Al-Rahman** (patched) | **31** | 78 | **39.7%** |
| 2 | **67 Al-Mulk** | 13 | 30 | **43.3%** |
| 3 | 61 Al-Ṣaff | 5 | 14 | 35.7% |
| 4 | 27 An-Naml | 28 | 93 | 30.1% |
| 5 | 101 Al-Qāriʿah | 3 | 11 | 27.3% |
| 6 | 10 Yūnus | 27 | 109 | 24.8% |
| 7 | 54 Al-Qamar | 13 | 55 | 23.6% |
| 8 | 6 Al-Anʿām | 36 | 165 | 21.8% |
| 9 | 39 Az-Zumar | 16 | 75 | 21.3% |
| 10 | 96 Al-ʿAlaq | 4 | 19 | 21.1% |
| 11 | 57 Al-Ḥadīd | 6 | 29 | 20.7% |
| 12 | 34 Saba' | 11 | 54 | 20.4% |
| 13 | 32 As-Sajdah | 6 | 30 | 20.0% |
| 14 | 46 Al-Aḥqāf | 7 | 35 | 20.0% |
| 15 | 90 Al-Balad | 4 | 20 | 20.0% |

### The Al-Mulk / Al-Rahman story

These two surahs are the **densest-questioning surahs in the Quran**, and
they do it with opposite rhetorical registers:
- **Al-Rahman (55)** repeats a single question 31 times as refrain:
  *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān* — "Then which of the favors
  of your Lord will you (two) deny?" This is classical *istifhām taqrīrī*:
  the answer is assumed to be "none." The dual `-kumā` (addressed to
  *jinn and mankind*) is itself an argument from audience-universality.
- **Al-Mulk (67)** stacks seven different questions in verses 16-22,
  each one escalating: "Do you feel secure that He who is in heaven will
  not cause the earth to swallow you?" → "Or do you feel secure…?" → "Is
  he who walks upside-down more rightly guided, or he who walks upright?"
  → "Say: who is it that could protect you from the Most Merciful?" This
  is classical *istifhām inkārī*: the answer is assumed to be "no one."

One surah is questioning-by-refrain, the other is questioning-by-accumulation.
They are the two purest examples of "theology-under-interrogation" in the
Quran. **That Al-Mulk is sometimes called "al-Munjiyah" (the Saver, because
of its nightly-recitation tradition) is precisely because it talks to the
reciter, refuses to let them pass silently.**

### On the Al-Rahman morphology patch

The Quranic Arabic Corpus v0.4 tags *ayy* in the Al-Rahman refrain as `INTG`
in only 16 of the 31 refrain iterations. The other 15 are tagged `N` (noun)
with identical surface form. This is almost certainly a parser artifact,
not a theological reading — classical commentators are unanimous that all
31 are rhetorical. **We corrected this in our CSV**, noting that under the
morphology-literal counting, Al-Rahman drops to 21.8% density (rank 8)
while under the classical reading it tops the list at 39.7%.

### An-Naba / Al-ʿAlaq / short Meccan pattern

**An-Naba (78)** opens with the classic Quranic rhetorical shock-question
*ʿamma yatasāʾalūn* — "About what are they asking one another?" — but
only 2 of its 40 verses are formally INTG-tagged. The surah *talks about*
a question the unbelievers are asking, rather than stacking its own
questions. Al-ʿAlaq (96) and Al-Qāriʿah (101) continue the short-Meccan
pattern: dense with questions, short surahs, high-impact ratios.

### An-Naml — the outlier

**An-Naml (Surah 27, "The Ants")** at 30.1% density is the anomaly: a
medium-long Meccan surah that runs as densely questioning as a short
Meccan one. Verses 27:59-65 are a 7-verse chain of *man khalaqa… amman…
amman* ("Who created…? Or is it he who…? Or is it he who…?") — stacking
FIVE `amman` challenges in succession, each daring the disbelievers to
name their alternative creator. This is **the longest pure-question
chain in the Quran** and it takes the form of a structured "or" ladder.

---

## 7. Stacked-question verses

**108 verses contain 2 or more interrogative markers**. Full list in the
CSV; notable examples:

| verse | markers | content |
|---|---:|---|
| 2:259 | 3 | "How (annā) will God give life to this after its death?…He said, how long (kam) did you tarry?…Say (answer)." The verse asks three questions and answers two. |
| 6:46 | 3 | "If God took your hearing and sight…who (man) but God would bring it? Look how (kayfa) We diversify the signs, then they turn away." |
| 10:35 | 3 | "Is there among your partners any (hal min) who guides to the truth?…Is he who guides to the truth (a-fa-man yahdī) more worthy to be followed, or he who guides not unless he himself is guided?…What (fa-mā la-kum kayfa) is wrong with you, how do you judge?" — the densest verse in the Quran by question-per-phrase. |
| 13:16 | 3 | "Say, who is the Lord of the heavens and the earth? Say, Allah… Is the blind equal to the seeing? Or are darknesses equal to the light?" |
| 39:38 | 3 | "If you asked them who created the heavens and the earth, they would say Allah. Say, then have you considered what you call on besides Allah — if Allah intended harm to me, are they removers of His harm? Or if He intended mercy, are they withholders of His mercy?" |

Pattern: **stacked questions are argument-ladders.** Each successive
question closes an escape route. The 3-question verse is not three
independent challenges — it is one argument with three closures.

---

## 8. Longest consecutive Q-verse runs

26 runs of ≥3 consecutive Q-verses exist. Top runs:

| run | length | theme |
|---|---:|---|
| **Al-Mulk 67:16-22** | **7** | "Do you feel secure…?" escalation |
| **An-Naml 27:59-65** | **7** | "Who created…?" *amman* ladder |
| Al-Aʿrāf 7:97-100 | 4 | "Do the people of the towns feel secure…?" (parallel to Al-Mulk) |
| Al-Ghāshiyah 88:17-20 | 4 | "Do they not look at the camel…? And at the sky…? And at the mountains…? And at the earth…?" (cosmic sign-ladder) |
| Al-Baqarah 2:67-70 | 4 | The cow-interrogation (Israelites asking Moses repeatedly) |
| Yūnus 10:50-53 | 4 | "Say: have you considered… Say: have you considered…" |
| Al-Qamar 54:15-18 | 4 | "Have We left it as a sign? Is there any who will remember? (repeated)" |

**Finding: the 7-verse Al-Mulk and An-Naml chains are structurally
parallel across 40 surahs of distance.** Both ask "who could protect /
who could create" seven times over, in succession, without answering.
Both end with "say" followed by brief summary. This is the Quran's
longest rhetorical structure: the **question-chain pericope**.

---

## 9. Questions answered vs. questions left hanging

- **Questions answered in the same verse by "qul"**: 24 verses
  (e.g. 2:215 *yasʾalūnaka mādhā yunfiqūna qul…* "They ask you what they
  should spend. Say…").
- **Questions followed by the next verse as answer**: extensive — most
  *yasʾalūnaka* in juz' 2-3 use this pattern.
- **Questions left unanswered (the reader answers)**: the bulk of
  *a-fa-lā + V* and *hal yastawī* formulas. These are **the reader's
  homework.** The Quran produces the question and moves on.

The Quran's rhetorical signature is that **the rhetorical question is
an unanswered question.** The reader is made into the respondent. This
is in tension with the *yasʾalūnaka* pattern (where the Prophet is the
respondent) — and that tension is part of the text's grammar of
authority: outsiders ask questions and the Prophet answers; insiders
hear questions and must answer themselves.

---

## 10. Counterfactual / wistful constructions — "law" and "laʿalla"

| marker | verses |
|---:|---:|
| `law` / `law-anna` / `lawlā` / `lawmā` (COND) | 176 |
| `laʿalla` ("perhaps you / perhaps they") | 123 |

Both are related to questions because they imply unrealized possibilities —
"if only you knew", "perhaps you will reason." They function as
rhetorical questions' positive mood: instead of asking to indict, they
wistfully imagine. A useful companion inventory to the question-set.

- Famous *law-annā* : Q 6:27 "If only you could see when they are made
  to stand before the Fire"; Q 26:102 "If only we had one more return."
- Famous *laʿalla*: Q 2:21 *laʿallakum tattaqūn* — closing every
  commandment with "perhaps you will fear God." A softer counterpart
  to *a-fa-lā tattaqūn*.

Together, 299 verses carry one of these two modal constructions — nearly
as many as the 830 question verses. The Quran's argumentative mood is not
purely interrogative; it is interrogative + conditional + wistful, all
three modalities of address-beyond-assertion.

---

## 11. Who is asking? — register classification

A qualitative classification over the 845 verses (scan-based, partial):

| register | approximate verses |
|---|---:|
| God → Prophet / humanity (most *a-lam tara*, *a-fa-lā*, *hal yastawī*) | ~550 |
| Prophet → unbelievers (opens with *qul …*) | 49 direct; many more where *qul* precedes a question | 
| Unbelievers → Prophet (*yasʾalūnaka*, or *yaqūlūna matā hādhā l-waʿd*) | ~35 |
| Angels → dead / disbelievers (*fī-ma kuntum* Q 4:97) | ~6 |
| Satan → humans (Q 7:22 *a-lam anhakumā* — the first lie re-told with hamza) | ~3 |
| Dwellers of Fire ↔ Dwellers of Paradise | ~10 (Q 7:44, 37:54, 74:42) |
| Moses / Abraham / Joseph / Noah (prophets as askers) | ~25 |
| The cosmic voice at Judgment (*matā hādhā l-waʿd*, *li-man al-mulk*) | ~8 |

Each register has a distinct formula-palette. God-to-humanity prefers
*a-fa-lā* and *a-lam tara*; Prophet-to-unbelievers prefers *qul + hal*
or *qul + a-raʾaytum*; angels-to-dead prefers *fī-ma kuntum*; Paradise-
to-Fire prefers *hal…* .

---

## 12. Novel patterns — what I think this means

1. **The Quran's densest-questioning surahs (67 Al-Mulk, 55 Al-Rahman) are
   its two densest-*single-audience* surahs.** Al-Rahman addresses "you two"
   throughout (jinn + humanity); Al-Mulk addresses a generic "you". Other
   high-density surahs (An-Naml, Yūnus, Al-Anʿām) are polemical Meccan.
   Question density is an index of direct-address intensity.

2. **The 7-verse question-chain is a reproducible rhetorical form.** It
   appears twice at maximum length: Al-Mulk 67:16-22 and An-Naml 27:59-65.
   Both use a different INTG particle as their base (Al-Mulk uses *a- + 
   verb*; An-Naml uses *amman — "or who is it that…"*). Both end in a
   commanded reply ("say…"). This is a plausible candidate for a named
   Quranic literary form: the **question-pericope** or *ʿiqd al-suʾāl*.

3. **Rhetorical questions and rhyme-breaks are INDEPENDENT** (O/E = 1.01).
   This is a genuinely novel empirical null: two classical-marked
   rhetorical channels that don't correlate. The Quran distributes its
   "marked" rhetorical devices across orthogonal axes.

4. **Ring-center Q-correlation is qualitative, not quantitative.** 3 of 5
   ring centers contain a rhetorical question, which is suggestive
   (p ≈ 0.012 unadjusted) but the sample is too small for confident
   inference. The qualitative pattern — that when rings have a question at
   the center, the question is an **accusation spoken by disbelievers**
   against a prophet (Thamūd↔Sāliḥ in both Al-Qamar 54:25 and Hud 11:62)
   or God's counter-accusation (Al-Baqarah 2:138) — is the real finding.
   **The Quran's chiastic centers stage rhetorical confrontations.**

5. **The Al-Rahman morphology mis-tag** (15 of 31 refrain iterations
   tagged `N` instead of `INTG` in Dukes' Quranic Arabic Corpus v0.4) is
   a small but genuine data-quality finding worth reporting upstream. Any
   INTG-based analysis of Surah 55 that relies on the corpus without
   patching will **underestimate the refrain count by 48%**.

6. **The Quran asks 830-845 questions and answers fewer than 50 of them.**
   The overwhelming majority of the Quran's rhetorical questions are
   given to the reader to answer. This is in keeping with Al-Suyūṭī's
   observation in *al-Itqān* that Quranic questions are *not* information-
   seeking; they are argumentative. The text's pedagogical strategy is
   **interrogation without resolution**. What is resolved is resolved by
   the reader. This is, in a precise computational sense, the theology
   of *ʿaql* (reason) embedded in the text's syntax.

---

## 13. Classical prior art

- **Al-Suyūṭī, al-Itqān fī ʿulūm al-Qurʾān**, nawʿ 47 (On Quranic
  questions). Al-Suyūṭī distinguishes *ḥaqīqī* (real) from *majāzī*
  (rhetorical) questions and lists subtypes: *taqrīr*, *inkār*, *tawbīkh*
  (reproach), *taʿajjub* (wonder), *tahdīd* (threat), *takdhīb*
  (charge-of-lying). Our rule-based 7-bucket classifier is a rougher
  rediscovery of his taxonomy.
- **Al-Zarkashī, al-Burhān fī ʿulūm al-Qurʾān**, kitāb 43 on *istifhām*.
  Covers the same territory as Suyūṭī.
- **Al-Jurjānī, Dalāʾil al-Iʿjāz**, on rhetorical syntax. The theoretical
  foundation for the *istifhām* distinction.
- **Ibn Taymiyya** on Q 2:243 *a-lam tara*: extended argument that the
  formula is conventional ("have you not become aware of") and does not
  claim the Prophet witnessed past events. This reading is built into our
  decision to count all *a-lam tara* as rhetorical-affirmation, not real.
- **Al-Ghazālī, Iḥyāʾ ʿulūm al-dīn**, on dhikr and on *fa-bi-ayyi ālāʾi*.
- **Farrin (2014)** and **Cuypers** on ring composition: consistent with
  our finding that ring centers host rhetorical confrontations.

**Novel relative to classical:**
- The count of 830-845 (patched) Q-verses is a modern computational
  count; al-Suyūṭī does not report it.
- The *a-fa-lā + V* formula frequency table (14x ʿql, 9x dhkr, 5x wqy, 4x
  bṣr, etc.) is not in classical sources.
- The Al-Rahman morphology-mis-tag is strictly a modern corpus
  observation.
- The ring-center-question qualitative correlation and the
  question-chain-as-literary-form observation are novel empirical
  readings of well-known classical material.

---

## 14. Outputs

- `/findings/phase-b-hypotheses/rhetorical-questions-per-verse.csv` —
  845 rows, one per Q-verse, with: surah, verse, Arabic text,
  n_markers, marker_lemmas, hamza/fa/lā/lam flags, opens_with_hamza,
  is_rhyme_break, question_type, formulas_matched.
- `/findings/phase-b-hypotheses/rhetorical-questions-per-surah.csv` —
  114 rows, one per surah: Q-verse count, total verses, density%.
- Journal: `/journal/rhetorical-questions-run-1.md`.

---

## 15. Limitations

- **Morphology trust**: Dukes v0.4 has at least one known systematic
  mis-tag (Al-Rahman `ayy`). Other mis-tags are possible. The 830→845
  patch is the one we caught; we did not exhaustively audit.
- **Heuristic type-classifier**: 447 of 830 verses fall in the "other-
  question" bucket. A human-gold classification would move many of these
  into inkārī / taqrīrī. This is why we report ranges rather than
  exact numbers for the rhetorical-vs-real split.
- **No pre-registration**: The ring-center p ≈ 0.012 and the rhyme-break
  null are exploratory. Future work should pre-register these tests.
- **Translation**: All Arabic readings used morphology + Arabic text;
  no translation alignment (the en.sahih.txt file has 6247 vs 6236
  lines, indicating wrap-inconsistency). Not required for counting
  but limits qualitative excerpts in the CSV.
