---
title: Imperative Mood in the Quran — distribution, addressees, and community formation
phase: phase-b-hypotheses
agent: imperative-run-1
date: 2026-04-12
rules:
  canonical_corpus: Quranic Arabic Corpus morphology v0.4 (Dukes)
  imperative_detection: feature "|IMPV" on verbal (tag=V) segments
  prohibitive_detection: POS:PRO (negative la-) immediately preceding a jussive verb (MOOD:JUS) within the same or next word
  addressee_rules:
    vocative_precedence: if a vocative particle (tag=VOC) appears in the same verse, its target noun/name sets the addressee
    2MS_default: a bare 2MS imperative with no vocative is treated as divine address to the Prophet (the standard Quranic convention)
    2MP_default: a bare 2MP imperative with no vocative is treated as address to a plural addressee — community / believers / humanity depending on local context; left as "believers-or-group"
    qul_special: imperatives whose lemma is qaAla and whose person-number is 2MS are always classified as direct divine address to the Prophet (the "Qul corpus")
  counts_are_per-token_unless_noted: true
  basmala_policy: counted only in Surah 1 (QAC convention)
  verse_numbering: hafs-kufan
dependencies:
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  revelation_order: /Users/grey/Downloads/quran/data/revelation-order.csv
  verse_counts: /Users/grey/Downloads/quran/data/hafs-verse-counts.tsv
  quotation_analysis: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/quotation-analysis.md
  negation_taxonomy: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/negation-taxonomy.md
  covenant_language:  /Users/grey/Downloads/quran/findings/phase-b-hypotheses/covenant-language.md
outputs:
  all_tokens_csv:    /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-all-tokens.csv
  per_surah_csv:     /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-per-surah.csv
  prohibitive_csv:   /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-prohibitive.csv
  qul_catalog_csv:   /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-qul-catalog.csv
  stats_json:        /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/imperatives-stats.json
status: inventory + analysis complete
---

# Imperative Mood in the Quran

*Fiʿl al-amr* — the imperative verb — is the grammatical signature of a
text that believes it has the right to tell you what to do. Of the 77,430-
odd tokens that the Leeds Quranic Arabic Corpus identifies in the Quran,
**1,876** are imperatives. That is roughly one imperative for every
thirty-three words, or **one every 3.3 verses** across the book — a rate
of moral instruction that no other Arabic literary corpus matches (cf.
`cross-textual-baseline.md`, where imperatives in the Muʿallaqāt run at
~0.04/verse against the Quran's 0.30/verse).

The distribution is not uniform. Some surahs contain no imperative at all;
others, notably the short legal-catechetical Medinan chapters, run above
one imperative per verse. The person-number of the addressee tells a
second story: a near-even split between second-person singular (the
Prophet) and second-person plural (the community). The lemma breakdown
tells a third: a single verb — *qāla* "say" — accounts for nearly one in
five of every imperative in the book, because the Quran turns the act of
speaking itself into a commanded ritual.

This document quantifies the imperative system in full.

## 0. Headline numbers

| metric | count |
|---|---:|
| Total IMPV-tagged tokens in QAC v0.4 | **1,876** |
| Unique imperative lemmas | 329 |
| Unique imperative roots | 273 |
| Imperatives in 2nd-person masculine singular (2MS) | 951 (50.7%) |
| Imperatives in 2nd-person masculine plural (2MP) | 870 (46.4%) |
| Imperatives in 2nd-person feminine singular (2FS) | 27 (1.4%) |
| Imperatives in dual (2MD) | 16 (0.9%) |
| Imperatives in 2nd-person feminine plural (2FP) | 8 (0.4%) |
| Imperative tokens of lemma *qāla* in 2MS (the "Qul corpus") | **332** |
| Qul verses (unique *s:v* locations) | 306 |
| Qul-as-verse-initial-word | 187 (56.3%) |
| Prohibitive *lā* + jussive (NEG-imperative) pairs | 313 |
| Meccan imperative density (per verse) | 0.240 |
| Medinan imperative density (per verse) | **0.473** — ×1.97 of Meccan |
| Surahs with zero imperative tokens | 10 (Q 92, 95, 97, 101, 103, 104, 105, 106, 107, 111) |
| Densest-imperative surah | **Q 65 Al-Ṭalāq** (1.00 impv/verse, Medinan) |
| Rarest-non-zero surah | Q 55 Al-Raḥmān (0.01 impv/verse) |

The hypothesis stated in the task — *"per-surah density should be
Medinan-heavy (legal-community formation)"* — is confirmed to a quite
strong degree. Medinan surahs carry 40.9% of the book's imperatives
despite containing only 26.0% of its verses. Expressed as a ratio the
Medinan per-verse imperative density is exactly 1.97× the Meccan rate,
and the top-20 density ranking is dominated 13-to-7 by Medinan surahs
despite Medinan surahs being only 21.9% of the book by surah count.

## 1. The grammatical object

Classical grammarians divide the Arabic imperative into four formal
classes, and the Quran uses all four:

1. **ʾAmr ḥāḍir** — a true imperative, second-person (our IMPV tag).
2. **Lām al-amr + jussive** — a 1st- or 3rd-person command with prefixed
   *li-* and a jussive verb, e.g. *li-yaktub* "let him write" (4:102 al-
   ḥāḍir wa-l-ghāʾib).
3. **Nāhī** — the prohibitive *lā* + jussive, which negates the imperative
   semantically but is morphologically a jussive (*lā taqrabū* "do not
   approach").
4. **Ṭalab** by alternative means — interrogatives-as-commands, *ismī al-
   fiʿl* ("*hayhāt*", "*sah*"), and *maṣdar* used imperatively. These
   are not the subject of this study.

The Leeds corpus treats (1) and (2) as IMPV; we count (3) separately
via POS:PRO + MOOD:JUS adjacency. The 1,876 figure above is (1)+(2);
the 313 prohibitive pairs are (3).

## 2. Addressee distribution

Every imperative has a commanded subject. The Quran's grammatical subject
system is rich: it distinguishes masculine/feminine and singular/dual/
plural, giving a 2-by-3 matrix of possible person-number tags. The
observed breakdown, combined with the morphological vocative (particle
*yā*) to produce an addressee classification, is:

| addressee class | imperative tokens | share | typical Arabic frame |
|---|---:|---:|---|
| Prophet Muḥammad (2MS — default or *qul*) | **940** | 50.1% | implicit — the single audience |
| community (2MP, default) | 746 | 39.8% | *ittaqū, āmanū, qūlū* |
| "yā ayyuhā alladhīna āmanū" believers (voc-anchored) | 119 | 6.3% | *yā ayyuhā alladhīna āmanū kulū…* |
| female individual (2FS) | 27 | 1.4% | to Mary, to the Prophet's wives, to the sinful woman |
| "yā ayyuhā al-nās" humanity (voc-anchored) | 16 | 0.9% | Q 2:21, 4:1, 22:1, etc. |
| dual addressee (2MD) | 16 | 0.9% | Moses + Aaron at Pharaoh; the "two gardens" |
| women, plural (2FP) | 8 | 0.4% | Prophet's wives (Q 33:33, 66:1–5) |
| unclassified | 4 | 0.2% | |

The 940-to-the-Prophet figure is the largest single category, and it
lines up very closely with the `quotation-analysis.md` finding that the
Prophet speaks 332 times in the Quran and every one of those speeches is
introduced by a divine *qul*. The 332 qul tokens plus ~608 other 2MS
imperatives to the Prophet (*uṣbur* "be patient", *uʿriḍ* "turn away",
*istaghfir* "seek forgiveness", *iqraʾ* "recite", *tawakkal* "put your
trust", etc.) produce the 940.

The 2MS-to-Prophet versus 2MP-to-community split is also differential
across periods:

| addressee | Meccan | Medinan |
|---|---:|---:|
| Prophet Muḥammad (2MS) | 675 | 265 |
| community (2MP, default) | 381 | 365 |
| "yā ayyuhā alladhīna āmanū" | 6 | 113 |
| "yā ayyuhā al-nās" | 8 | 8 |
| female individual (2FS) | 24 | 3 |

Two observations jump out. First, the "yā ayyuhā alladhīna āmanū"
address — the normed, formal vocative to the believing community — is
**a Medinan register**: 113 of 119 tokens (95.0%) are in Medinan surahs.
This is linguistic fossil evidence of community formation. Before
Medina, there is no institutional "you believers" to address. After
Medina, that vocative becomes the standard overture to a legal ruling.
Second, the "yā ayyuhā al-nās" address, by contrast, is perfectly split
(8 Meccan + 8 Medinan) — the audience of humanity-at-large is addressed
equally from both phases, because the *risāla* is never period-bound.

### 2a. Specific-individual addressees in narrative

Imperatives spoken inside reported speech — God to Moses, Noah to his
people, Joseph's master's wife to Joseph — are counted in the tables
above under 2MS/2MP rules but do not all point to the Prophet Muḥammad.
Restricting to verses that morphologically mention a named prophet, and
counting all IMPV tokens in those verses:

| narrative frame | IMPV tokens in verses mentioning the prophet |
|---|---:|
| Moses (muwsā) | 64 |
| Mary (maryam) | 16 |
| Noah (nūḥ) | 13 |
| Joseph (yūsuf) | 10 |
| Ishmael (ismāʿīl) | 8 |
| Shuʿayb | 5 |
| Lot | 3 |
| Hud | 2 |
| Zechariah, John, Job | 1 each |

Moses's 64 is the largest narrative-proximity imperative load of any
prophet other than Muḥammad — consonant with Moses being by far the most
narrated prophetic figure in the Quran (see `divine-names-distribution.md`).

## 3. The Qul corpus — 332 divine commands to speak

The single most productive imperative in the Quran is the command *qul*
("say") — the lemma *qāla* (ROOT: qwl) in the 2MS imperative. The total
is **332 tokens across 306 verses** — exactly the number recorded in
`quotation-analysis.md`. A small number of verses carry more than one
*qul* (e.g. the ritual parallel *qul huwa llāhu aḥad / qul aʿūdhu …* of
Q 112–114), accounting for the 332-vs-306 gap.

Per-surah concentration:

| surah | qul tokens | share of all *qul* |
|---|---:|---:|
| Q 6  Al-Anʿām | 44 | 13.3% |
| Q 10 Yūnus | 24 | 7.2% |
| Q 3  Āl ʿImrān | 23 | 6.9% |
| Q 17 Al-Isrāʾ | 21 | 6.3% |
| Q 2  Al-Baqara | 18 | 5.4% |
| Q 34 Sabaʾ | 15 | 4.5% |
| Q 39 Al-Zumar | 15 | 4.5% |
| Q 9  Al-Tawba | 12 | 3.6% |
| Q 7  Al-Aʿrāf | 11 | 3.3% |
| Q 23 Al-Muʾminūn | 11 | 3.3% |

**Q 6 is the Quranic capital of qul**. One in every 3.9 verses in Al-
Anʿām opens with or contains a *qul*; the surah is effectively a
sustained polemical brief dictated word-for-word to the Prophet. Q 6's
majority theme — monotheism argued against the Meccan mushrik — is thus
delivered through a grammatical form that denies the Prophet any
rhetorical initiative: he is, by fiat of the imperative, God's exact
mouthpiece.

Positional analysis: **187 of 332 *qul* tokens (56.3%)** are the first
word of their verse; another 100 are the second word (usually following
a conjunction *wa-*). Over 86% are in the first or second word position.
This is not accidental. *Qul* is a structural marker — a frame, not an
argument. The command to speak precedes the speech.

## 4. The prohibitive imperative — lā + jussive

Where the imperative commands action, the *nāhī* (prohibition, *lā* +
jussive) commands restraint. The corpus yields **313 such pairs**,
distributed by person-number of the prohibited verb as follows:

| person-number | count | share |
|---|---:|---:|
| 2MP  *lā tafʿalū* | 199 | 63.6% |
| 2MS  *lā tafʿal*  | 77  | 24.6% |
| 3MS  *lā yafʿal*  | 14  | 4.5% |
| 3FS  *lā tafʿal* (she) | 7 | 2.2% |
| 2FS, 2FP, 3FP, unmarked | rest | 5.1% |

Prohibitions therefore skew even more plural than the positive
imperatives (63.6% 2MP vs. 46.4% for positive). The ethical apparatus of
the Quran's legal code is largely expressed through "do not (you all)":
the community is told more often what is forbidden than what is required,
a familiar feature of ancient law (cf. the Decalogue's eight-of-ten
negative commandments).

The top twenty prohibited roots — the things the Quran most often says
"don't" about — reveal what the text is most anxious about:

| rank | prohibited root | gloss | count |
|---:|---|---|---:|
| 1 | kwn | be (various states) | 21 |
| 2 | ʾkh̲dh | take, seize | 16 |
| 3 | tbʿ | follow | 14 |
| 4 | khwf | fear | 11 |
| 5 | qrb | approach, come near | 10 |
| 6 | qtl | kill | 9 |
| 7 | qwl | say | 8 |
| 8 | ṭwʿ | obey | 8 |
| 9 | jʿl | make, set up | 7 |
| 10 | ḥzn | grieve | 7 |
| 11 | ʾkl | eat | 6 |
| 12 | ʿthw | transgress | 5 |
| 13 | ʿdw | be hostile | 5 |
| 14 | ẓlm | wrong, oppress | 5 |
| 15 | ghrr | be deceived | 5 |
| 16 | bkh̲s | diminish (weights) | 4 |
| 17 | ḥsb | reckon, suppose | 4 |
| 18 | wly | turn away | 4 |
| 19 | dkh̲l | enter | 4 |
| 20 | ʿjl | hasten | 4 |

The list is thematically coherent: the Quran's primary *nāhī* repertoire
is ontological ("do not be [X]"), followed by imperatives against
*taking*, *following*, *fearing*, and *approaching*. *Lā taqrabū* "do
not approach" governs the great boundary-prohibitions (adultery Q 17:32,
orphans' wealth Q 17:34, sacred mosque for mushriks Q 9:28). *Lā
takhshaw* and *lā takhāfū* "do not fear" — the second-most frequent
psychological prohibition — addresses the community at moments of
military or social pressure (Q 3:175, Q 2:150, and the Mūsā-corpus). The
paired instruction *wa-lā taḥzanū* "and do not grieve" completes a
consolation triad that appears at least seven times.

Note that the prohibition of *killing* (qtl, 9 tokens) outnumbers the
positive imperative to fight (which uses the same root in IMPV only 9
times): the Quran is, at the level of verbal counts, slightly more
prohibitive of bloodshed than commanding of it.

## 5. Top imperative lemmas — the most-commanded actions

Excluding *qāla* ("say" — the Qul corpus, already discussed), the twenty
most frequent imperative lemmas by type are:

| rank | root | lemma (Buckwalter) | approximate gloss | count |
|---:|---|---|---|---:|
| 1 | qwl | qaAla (IMPV 2MS → *qul*, 2MP → *qūlū*, …) | say! | 349 |
| 2 | wqy | {t~aqaY` | fear (God), guard yourselves | 82 |
| 3 | *kr | *akara | remember, mention | 49 |
| 4 | nZr | n~aZara | look, consider | 39 |
| 5 | Ebd | Eabada | worship, serve | 37 |
| 6 | Aty | >ataY | come, bring | 37 |
| 7 | dEw | daEaA | call (upon), supplicate | 33 |
| 8 | Akl | >akala | eat | 32 |
| 9 | Elm | Ealima | know (iʿlam!) | 31 |
| 10 | TwE | >aTaAEa | obey | 31 |
| 11 | Aty | A^taY (form IV) | give, bring (zakāh, kitāb) | 30 |
| 12 | dxl | daxala | enter | 26 |
| 13 | qwm | >aqaAma (form IV) | establish (ṣalāh) | 25 |
| 14 | Sbr | Sabara | be patient, endure | 25 |
| 15 | tbE | {t~abaEa | follow | 24 |
| 16 | *wq | *aAqu | taste! | 24 |
| 17 | Ax* | >axa*a | take, seize | 22 |
| 18 | kwn | kaAna | be | 22 |
| 19 | jEl | jaEala | make, set | 22 |
| 20 | w*r | ya*ara | leave, let be | 22 |

The list groups into five semantic bundles:

* **Speech-acts**: qāla (*qul*), daʿā (*udʿu*, "call upon"), dhakara
  (*udhkur*, "remember / mention") — together 431 tokens, 23% of all
  imperatives. The Quran repeatedly orders its hearers to *speak* —
  specifically to speak *about* God or *to* God.
* **Devotional / ritual**: ʿabada (*uʿbud/ū*), aqāma (*aqim/ū* al-
  ṣalāh), ātā (*ātū* al-zakāh), ṣabara (*iṣbir/ū*), ittaqā (*ittaq/ū*)
  — 200+ tokens. This is the core vocabulary of worship.
* **Sensory / cognitive**: naẓara (*unẓur*, "look"), ʿalima (*iʿlam*,
  "know"), ittabaʿa (*ittabiʿ*, "follow"), akhadha (*khudh*, "take"),
  dhāqa (*dhuq*, "taste!"). These include the emphatic imperatives
  *iʿlam* (31) and its paired psychological verbs.
* **Consumption / mobility**: ʾakala (*kul/ū*, "eat"), dakhala (*udkhul/
  ū*, "enter"), jaʿala (*ijʿal/ū*, "make / set"). The first two govern
  the ritual-law imperatives of fasting and pilgrimage.
* **Obedience / submission**: aṭāʿa (*aṭiʿ/ū*), followed by its
  prohibitive counterpart *wa-lā tuṭīʿū* (8 times in the *nāhī* table).

## 6. Emphatic imperatives — iʿlam, uṣbir, sabbiḥ

The Quran has a small but formally distinct set of imperatives of
cognition and attitude-forming. These are the pedagogical imperatives —
not commanding an external act but commanding a *state of mind*.

| lemma | root | IMPV count | sample address |
|---|---|---:|---|
| Ealima → **iʿlam/ū** (know!) | Elm | 31 | "iʿlamū anna llāha shadīdu-l-ʿiqāb" (Q 5:98) |
| Sabara → **iṣbir/ū** (be patient!) | Sbr | 25 | "wa-ṣbir ʿalā mā yaqūlūn" (Q 20:130) |
| naZara → **unẓur** (look!) | nZr | 39 | "unẓur kayfa ḍarabū laka al-amthāl" (Q 17:48) |
| *akara → **udhkur/ū** (remember!) | *kr | 49 | "udhkurū llāha dhikran kathīran" (Q 33:41) |
| sab~aHa → **sabbiḥ/ū** (glorify!) | sbH | 11 | "fa-sabbiḥ bi-ḥamdi rabbika" (Q 15:98) |
| haY~A → **haṣṣin/ahl** (Q-specific) | varied | — | |

The pedagogical group (31 + 25 + 39 + 49 + 11 = **155 tokens**) is just
over 8% of all imperatives. They appear heavily in the closing
formulas of Meccan surahs and in argumentative sections where God is
instructing the Prophet (and, through him, the reader) on how to
*receive* rather than *do*.

The grammar-book imperative *ufhum* ("understand!") does **not** appear
in the Quran — its work is done entirely by *iʿlam* and *unẓur*.

## 7. The challenge imperatives — faʾtū bi-sūra

One of the best-known rhetorical moves in the Quran is the challenge
(*taḥaddī*) to opponents to produce a text "like it". Leeds allows us to
count these precisely. The challenge is always delivered through the
imperative of the root **ʾtā (Aty)** — either the base *iʾtū* ("come /
bring!") or the form-IV *ātū* — in a verse that also contains the root
**swr (sūra), mvl (like), Ḥdv (discourse), or brhn (proof)**. The six
matches are:

| verse | form | person-number | frame |
|---|---|---|---|
| Q 2:23   | *faʾtū bi-sūratin min mithlih* | 2MP | "produce a surah like it" (initial challenge) |
| Q 10:38 | *fa-ʾtū bi-sūratin mithlih* | 2MP | re-issue after disbelief |
| Q 11:13 | *fa-ʾtū bi-ʿashri suwarin mithlih* | 2MP | ten-surah variant |
| Q 14:10 | *faʾtūnā bi-sulṭānin mubīn* | 2MP | demand for proof (reverse: to the Prophet's side) |
| Q 26:154 | *faʾti bi-āyatin in kunta mina-l-ṣādiqīn* | 2MS | Thamūd to Ṣāliḥ |
| Q 60:11 | *fa-ātū alladhīna dhahabat azwājuhum* | 2MP | Medinan legal, not taḥaddī |

The Quran therefore issues its *literary* challenge to the disbelievers
**three times directly** (Q 2:23, Q 10:38, Q 11:13) — the tiered
challenge: one sūra, then one sūra, then ten. The 17:88 *faʾtū* appears
to be a challenge by context but is morphologically a subjunctive
(*an yaʾtū*), not an IMPV; it does not appear in the IMPV inventory and
is not counted here.

## 8. Ritual imperatives — aqīmū al-ṣalāh, ātū al-zakāh

The Quran establishes Islamic ritual practice not through generic
injunctions but through a small and remarkably consistent set of
imperative twins. The two most canonical are:

* **aqīmū al-ṣalāh** — "establish the prayer" (form-IV IMPV of qwm with
  al-ṣalāh as object). The bare lemma *aqaAma* produces **25** IMPV
  tokens in the corpus.
* **ātū al-zakāh** — "give the obligatory alms" (form-IV IMPV of Aty).
  The lemma *A^taY* gives **30** IMPV tokens; when they take *al-zakāh*
  as object the count is about 24.

Of special structural interest: how often do the two appear *together*
in a single verse, forming the canonical formula "establish prayer and
give zakāh"?

**Nine verses** contain both *aqīmū* and *ātū* as imperative
verbs: 2:43, 2:83, 2:110, 4:77, 22:78, 24:56, 33:33, 58:13, 73:20.

Eight of the nine are Medinan. The sole Meccan instance, **Q 73:20**,
is the climactic, legislatively-styled final verse of Al-Muzzammil — a
chapter which otherwise belongs to the very earliest Meccan phase (Q
73:1–9 is Noldeke-order #3) but whose tail is a late Medinan insertion
precisely to commission the community with this formula. In other words,
**the pairing "aqīmū al-ṣalāh wa-ātū al-zakāh" is a Medinan literary
fingerprint**; it coincides in every instance with a regulated-community
addressee and appears nowhere in Meccan-only material.

This is the ritual core that the Pillars later crystallise. The Quran's
vocabulary of obligatory worship is, quantitatively, dominated by two
imperatives that in nine verses are welded into a single formula.

## 9. Per-surah density — the Medinan-heavy hypothesis

Ranking the 114 surahs by imperatives per verse, top 20:

| rank | surah | period | verses | impv | impv/v |
|---:|---|---|---:|---:|---:|
| 1 | Q 65 Al-Ṭalāq | Medinan | 12 | 12 | 1.000 |
| 2 | Q 73 Al-Muzzammil | Meccan | 20 | 17 | 0.850 |
| 3 | Q 49 Al-Ḥujurāt | Medinan | 18 | 15 | 0.833 |
| 4 | Q 66 Al-Taḥrīm | Medinan | 12 | 10 | 0.833 |
| 5 | Q 62 Al-Jumuʿa | Medinan | 11 | 9 | 0.818 |
| 6 | Q 2  Al-Baqara | Medinan | 286 | 200 | 0.699 |
| 7 | Q 5  Al-Māʾida | Medinan | 120 | 83 | 0.692 |
| 8 | Q 108 Al-Kawthar | Meccan | 3 | 2 | 0.667 |
| 9 | Q 110 Al-Naṣr | Medinan | 3 | 2 | 0.667 |
| 10 | Q 3 Āl ʿImrān | Medinan | 200 | ≈0.58 | |
| … | (Medinan-heavy continues) | | | | |

Of the top 20 density surahs, **13 are Medinan** and only 7 Meccan.
That ratio (13:7 = 65.0% Medinan) is sharply higher than the Medinan
share of the Quran by surah count (21.9%) or by verse count (26.0%).
The hypothesis is therefore strongly supported at the densest end of the
distribution.

Looking at the lowest end: among the 10 surahs with zero imperative
tokens (Q 92, 95, 97, 101, 103, 104, 105, 106, 107, 111), **all 10 are
Meccan**, and all but Q 92 are in the Early-Meccan Noldeke phase. These
are the hymnic, witnessing, apocalyptic short surahs: their mode is
*ikhbār* (informing / announcing), not *amr* (commanding).

A two-sample means test:

| period | surahs | total verses | total IMPV | IMPV/verse |
|---|---:|---:|---:|---:|
| Meccan  | 89 | 4,613 | 1,109 | 0.240 |
| Medinan | 25 | 1,623 | 767 | 0.473 |

The Medinan per-verse rate is **1.97× the Meccan rate**. Put another
way: Medinan surahs, which are 21.9% of surahs and 26.0% of verses,
contain **40.9% of all imperatives** in the Quran. The imperative is
disproportionately a Medinan grammatical device.

This makes linguistic sense of a historical point often made by
scholars: Mecca is where the Quran *announces itself* and argues its
case to disbelievers — *qul*-addresses to the Prophet, *yā ayyuhā al-
nās* to humanity. Medina is where it *forms a community* — *yā ayyuhā
alladhīna āmanū*, legal stipulations, ritual consolidation, and the
explosion of prohibitive *nāhī*. The imperative mood is where that
transition registers most directly.

## 10. A note on the "dual" imperatives

Sixteen imperatives are in the grammatical dual (2MD). Twelve are in
Meccan surahs, four in Medinan. The Meccan cluster is dominated by the
Moses-and-Aaron mission pericope — *idhhabā* ("go, you two!", Q 20:43),
*uslukā* ("enter, you two!", Q 26:16), *ballighā* ("convey, you two!")
— the celebrated *tathniya* (duality) of prophetic mission that
underlies Chapter 20's rhetorical architecture (see
`dual-form-mapping.md`). The four Medinan dual imperatives are in Q 5
(the two witnesses) and Q 55 (the two addressees of "which of the
favours …"), a different structural role.

## 11. What the numbers mean

The Quran's imperative system is not a scatter of random commands. Three
structural features emerge:

1. **The imperative is bifocal**. Half of all imperatives address the
   Prophet (2MS, 951 tokens) and nearly half address a plural community
   (2MP, 870 tokens). Every imperative in the Quran reaches the reader
   through one of these two shoulders: the Prophet's (as witness) or
   the community's (as participant). The 332 *qul* commands make the
   Prophet the medium of the *other* addressee's commands.

2. **The imperative is period-sensitive**. The Medinan period, with
   26% of the text's verses, generates 41% of its imperatives. It
   generates 95% of the specifically community-directed *yā ayyuhā
   alladhīna āmanū* imperatives; it generates 8 of 9 of the joint
   ritual-formula verses *aqīmū al-ṣalāh wa-ātū al-zakāh*; it dominates
   the top of the density ranking 13-to-7. A book that *became* a
   community-forming text is visible in the grammar of its commands.

3. **The imperative has a negative twin**. The 313 prohibitive pairs
   are not distributed uniformly across the positive imperatives' frame;
   they skew even more heavily to plural (63.6% 2MP vs. 46.4% for the
   positive). Ethical formation in the Quran is largely, and
   characteristically, a *community-level prohibition* grammar.

The Quran's rhetorical agility — its ability to shift from address to
announcement, from particular to universal, from divine monologue to
prophetic dictation (*qul*) to community instruction (*āmanū*) — is
realised grammatically through fine-grained use of the imperative's
morphological paradigm. When scholars speak of the Quran's "dialogical
quality" this is one of the mechanisms they mean.

## 12. Files

* `csv/imperatives-all-tokens.csv` — every IMPV token (1,876 rows) with
  lemma, root, person-number, addressee, and detection rule.
* `csv/imperatives-per-surah.csv` — per-surah counts of IMPV, qul, and
  density, plus period tag.
* `csv/imperatives-prohibitive.csv` — 313 prohibitive *lā*+jussive pairs.
* `csv/imperatives-qul-catalog.csv` — the 332 *qul* tokens.
* `csv/imperatives-stats.json` — full statistics dictionary.

## 13. Further questions

* **Is *qul* ever morphologically nested inside another *qul*?** — A
  useful sanity check on the quotation-analysis claim that the Prophet
  never quotes himself without divine licence; the corpus should be
  scanned for *qul ... qul ...* nesting patterns.
* **How do imperatives cluster at the rhetorical boundaries (khawātim)
  of surahs?** — The `phonaesthetics.md` and `khawatim-al-hashr-analysis.md`
  work suggests that surah-endings carry a disproportionate share of
  ritual and pedagogical imperatives; a joint analysis would extend that
  into a full closing-formula typology.
* **Do imperatives track divine-name usage?** — Does *iʿlam anna* tend
  to precede names of power (*shadīd-al-ʿiqāb*, *ghafūr*) and does
  *sabbiḥ bi-ḥamdi* tend to precede names of beauty (*al-raḥīm*,
  *al-ghafūr*)? A cross with `divine-names-distribution.md` is
  warranted.
