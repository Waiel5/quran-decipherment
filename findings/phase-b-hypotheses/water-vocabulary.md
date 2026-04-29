---
title: Water vocabulary in the Quran — a lexical and theological map
phase: B
agent: water-vocabulary-run-1
date: 2026-04-12
rules:
  orthography: not-applicable (root- and lemma-level counts)
  word_definition: root (Leeds QAC v0.4) + lemma split where one root carries multiple senses
  letter_definition: not-applicable
  basmala_policy: counted-only-in-surah-1
  verse_numbering: hafs-kufan
  abjad_table: not-applicable
  null_model: descriptive (no hypothesis test; comparisons are against prior phase-B tables)
source_corpus:
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - data/morphology/root-index.json
  - quran-text/quran-no-tashkeel.json
  - data/translations/en.sahih.txt
companion_files:
  - findings/phase-b-hypotheses/paired-opposites-network.md
  - findings/phase-b-hypotheses/sacred-geography.md
  - findings/phase-b-hypotheses/paradise-hell-names.md
---

# Water vocabulary in the Quran

## 0. Why a water map

Water in the Quran is not a single word but a **lexical network** of at least
nine roots distributed across 6236 verses. The paired-opposites file shows
that sea/land (baḥr/barr) co-occurs 11 times (enrichment 8.6×) — but the
full water cosmos is bigger than one pair. Water in the Quran is:

- the **substrate of life** (Q 21:30 — "We made every living thing from water"),
- the **instrument of judgment** (Noah's flood, Pharaoh's drowning in *yamm*),
- the **proof of resurrection** (revival of dead land → revival of the dead),
- the **currency of paradise** (four rivers — water, milk, wine, honey, Q 47:15),
- the **semantic shape of mercy** (ghayth = rain = raḥma, Q 42:28),
- and the **ritual solvent of purity** (wuḍūʾ, ghusl, and its dry substitute,
  *tayammum*, from the same root as *yamm*, "the sea").

This file enumerates every water-lexeme occurrence, then reads the eight
theological loci named in the task brief.

## 1. Full inventory — roots, lemmas, counts

All counts are surface lemma occurrences under the Leeds QAC v0.4 root
assignment. Where one root carries more than one sense, lemmas are split.

| Root (Buckwalter / approx. Arabic) | Total | Lemmas (count) | Gloss |
|---|---:|---|---|
| bḥr (bHr) | 42 | *baḥr* 41, *baḥīra* 1 (Q 5:103) | sea; the *baḥīra* is a pre-Islamic dedicated she-camel — semantic extension of "split/cut" (*baḥara*) |
| nhr (nhr) | 113 | *nahār* "daytime" 57, *nahar* "river" 54, *tanhar* "to repel" 2 | one root, three senses — river, daytime, repulsion |
| mwh (mwh) | 63 | *māʾ* 63 | water — always the simple noun |
| ghyth (gyv) | 4 | *ghayth* 3, *yughāthu* 1 (Q 12:49) | rain-as-rescue; root ḡ-y-ṯ = "succour" |
| mṭr (mTr) | 15 | *maṭar* 7, *umṭirat* "was rained upon" 7, *mumṭir* 1 | rain, almost always punitive |
| rwḥ (rwH) | 57 | *rīḥ* "wind" 29, *rūḥ* "spirit" 21, *rawḥ* "breath/ease" 3, *rayḥān* 2, *turīḥu* 1, *rawāḥ* 1 | the wind/spirit/breath complex — not water but the air that moves clouds |
| ʿyn (Eyn) | 65 | *ʿayn* 57 (spring and eye), *maʿīn* "flowing spring" 4, *ʿīn* "wide-eyed houris" 4 | spring / eye / fountain — polysemy is inherent in Arabic |
| biʾr (bAr) | 1 | *biʾr* 1 (Q 22:45 — "well abandoned") | the well, a hapax in this exact lexeme |
| kvr (kvr → kawthar) | 167 | *akṯar* 80, *kaṯīr* 63, *kaṯīra* 11, *istakṯara* 3, *kaṯura* 2, *kaṯra* 2, *akṯaru* 2, *takāṯur* 2, *kaṯṯara* 1, *kawṯar* 1 (Q 108:1) | root = "abundance"; *kawṯar* is a superlative hapax |
| ymm (ymm) | 11 | *yamm* "sea (Moses-cycle)" 8, *tayammam* "seek/aim for" 3 | the Egyptian sea AND the dry ablution verb share one root |
| jnb (jnb) | 33 | *ijtanaba* "avoid" 9, *jānib* "side/bank" 9, *janb* "flank" 8, *junub* "state of major impurity" 4, others 3 | "side" — includes the *bank* of a valley and the *state* that requires ghusl |
| sḥl (sHl) | 1 | *sāḥil* 1 (Q 20:39 — Moses' basket cast ashore) | shore — hapax |
| brr (brr) | 32 | *barr* "dry land" 22, *birr* "righteousness" 8, *tabarrū* 2 | "land" as antonym of sea; NOT the same as *bariyya* "created beings" (root br') |

Additional water-adjacent lexemes (outside the seed list) that should be
tracked together:

| Root | Total | Lemmas | Comment |
|---|---:|---|---|
| mwj (mwj) | 7 | *mawj* "wave" | Noah (Q 11:42–43); the "darknesses of wave upon wave" (Q 24:40) |
| mlḥ (mlH) | 2 | *milḥ* "salt" | only in the two-seas verses (25:53, 35:12) |
| ujj (Ajj) | 3 | *ujāj* "bitter/briny" | only paired with *milḥ* in the two-seas verses + scalding hell-water |
| frt (frt) | 3 | *furāt* "sweet (of water)" | 25:53, 35:12, 77:27 |
| fjr (fjr) | 24 | *infajarat* "gushed forth" | Q 2:60, and metaphorically Q 17:90–91 |
| ʿḏb (E\*b) | ~14 | *ʿaḏb* "sweet" | sweet water is morphologically twinned with *ʿaḏāb* "torment" (same root) |
| sqy (sqy) | 25 | *saqā* "to give drink" | the whole "give-drink" verb cycle, incl. the paradise drinks |
| mzj (mzj) | 3 | *mizāj* "mixture" | Q 76:5, 76:17, 83:27 — the paradise blended drinks |
| snm (snm) | 1 | *tasnīm* "lofty fountain" | Q 83:27, a hapax paradise spring |
| qṭr (qTr) | 5 | *qaṭr* "drop/liquid metal" | two of the five are the molten-copper flood of Dhū al-Qarnayn (Q 18:96) |
| syl (syl) | 4 | *sayl* "torrent", *sāla* "flowed" | Q 13:17, 34:12 (Sabaʾ flood) |
| gsq (gsq) | 4 | *ghassāq* "pus/dark-liquid" | Q 38:57, 78:25 — hell's anti-water |
| ḥmm (Hmm) | 21 | *ḥamīm* "scalding water" | the standard hell-drink (Q 47:15 pair, 56:42, etc.) |

### Distributional note

The top surahs by water-lexeme density are al-Baqara (2), Hūd (11),
al-Kahf (18), al-Raʿd (13), and al-Shuʿarāʾ (26) — all long, narrative-rich
surahs where Moses / Noah / the Garden-simile appears. Surah 55 (al-Raḥmān)
is comparatively short but carries the two-seas and the pearl-and-coral
verses. Surah 108 (al-Kawṯar) contains a single water-word (kawṯar) and is
the shortest surah in the Quran — a water-bearing pinpoint.

## 2. Q 21:30 — "We made every living thing from water"

> *wa-jaʿalnā min al-māʾi kulla shayʾin ḥayy*
> "and We made from water every living thing."

Morphologically the verse is a chain of three cosmological claims:

1. *kānatā ratqan* — sky and earth were "sewn together" (one lump).
2. *fa-fataqnāhumā* — "and We unstitched them."
3. *jaʿalnā min al-māʾ kulla shayʾin ḥayy* — "and from water We made every
   living thing."

The syntactic partitive *min* is causal-material here: water is the **min-argument
of ḥayāt**. This is the only place in the Quran where *māʾ* and *kull shayʾin
ḥayy* occur in the same clause. In the paired-opposites file the *heaven/earth*
pair has enrichment 9× and 224 same-verse hits; Q 21:30 is **the verse where
that pair is unstitched** — and water is what the stitch is replaced by. The
verse is a lexical hinge: *samāwāt* / *arḍ* (pair) → *māʾ* (substrate) → *ḥayy*
(effect). The rhetorical muqābala of heaven-vs-earth is resolved into a
monadic substrate, *māʾ*.

This also aligns Q 21:30 with Q 24:45 (*wa-Llāhu khalaqa kulla dābbatin min
māʾ*, "God created every crawling thing from water") — the only other verse
that asserts a water-origin for all life. Together these two verses carry
the Quran's aquatic materialism.

## 3. The two seas (al-baḥrāni) — Q 25:53, 35:12, 55:19–20

Three verses use the dual *al-baḥrāni*. The lexical skeleton is identical:

- Q 25:53: *hādhā ʿaḏbun furātun wa-hādhā milḥun ujāj* — "this one is sweet
  and fresh, this one is salt and briny."
- Q 35:12: same dichotomy, adding that from **each** the human extracts
  tender flesh and ornaments.
- Q 55:19–20: *maraja al-baḥrayni yaltaqiyān / baynahumā barzakhun lā yabghiyān*
  — "He let loose the two seas to meet; between them is a barrier they do not
  transgress."

Three technical observations:

1. The verb *maraja* (Q 25:53, 55:19) is a hapax-collocation root — used
   only with the two seas. It means "to let loose/mix" but the result is
   paradoxically **non-mixing**. The *barzakh* (a Persian loan) makes the
   paradox explicit.
2. The two-seas pair is the only place where *milḥ* (salt, root mlḥ) and
   *ujāj* (briny, root Ajj) and *furāt* (sweet, root frt) appear. These are
   three dedicated lexemes reserved for this cosmological contrast.
3. Q 35:12 then declares *mā yastawī al-baḥrāni* — "the two seas are not
   equal" — and the very next clause is **wa-mā yastawī** pivoting to the
   blind/seeing, living/dead pairs (Q 35:19–22). The two-seas image is an
   oceanographic muqābala that opens a chain of metaphysical muqābalas.

The pearl/coral pair (*luʾluʾ wa-marjān*) in Q 55:22 is the product that
emerges *min-humā* — from both seas. Classical tafsīr (al-Rāzī, al-Qurṭubī)
disputes whether this means both salt and fresh, or whether it is a
compressed way of saying "from one of the two" (the salt one, since pearls
come only from the sea). The ambiguity is itself a muqābala — the verse
refuses to separate the two sources.

## 4. Paradise rivers — Q 47:15 and the four-river formula

Q 47:15 is the **anhār-itemisation verse**: the only place in the Quran
where the paradise rivers are enumerated by substance.

> *fīhā anhārun min māʾin ghayri āsin*
> *wa-anhārun min labanin lam yataghayyar ṭaʿmuh*
> *wa-anhārun min khamrin laḏḏatin li-l-shāribīn*
> *wa-anhārun min ʿasalin muṣaffā*

Four substances, each with a defect-cancellation clause:

| Substance | Cancelled defect |
|---|---|
| water (*māʾ*) | not stagnant (*ghayr āsin*) |
| milk (*laban*) | taste does not change |
| wine (*khamr*) | delicious, not headache-inducing (contrast Q 37:47, Q 56:19) |
| honey (*ʿasal*) | strained (*muṣaffā*), no beeswax |

Each river is presented **as the perfected form of its worldly counterpart**.
This is the Quran's standard paradisal rhetoric: the noun is kept, the
defect is negated. The same technique operates elsewhere — *khamr* that
"does not cause headache" (Q 56:19), *zaqqūm* fruit that reverses Eden's
fruit.

The generic formula *tajrī min taḥtihā al-anhār* ("beneath which rivers
flow") appears **35 times** with taḥtihā and 4 times with taḥtihim — total
39 occurrences of the paradise-rivers-flowing formula. Q 47:15 is the
itemised version of that formula. The *anhār* count in paradise verses is
much higher than in geographic verses: of the 54 occurrences of *nahar*
"river", roughly 40 are eschatological (paradise), 14 are geographic
(Pharaoh's Nile, the river in Q 2:249 = Saul/Ṭālūt, etc.). The Quran's
primary river is an eschatological river.

Note also the **anti-paradise** in the very next clause of Q 47:15: those
in hell are given *māʾ ḥamīm* ("scalding water") that severs their
intestines. Water is the axial substance of both destinies.

## 5. Moses parts the sea — Q 26:63, Q 20:77 — and the lexical split

Moses' parting of the sea is told with **two different words**:

- Q 26:63: *iḍrib bi-ʿaṣāka al-baḥr* — "strike the **sea** (*baḥr*) with
  your staff" (then *fa-nfalaqa* "and it split").
- Q 20:77: *fa-ḍrib lahum ṭarīqan fī al-baḥri yabasan* — "strike for them
  a dry path in the **sea** (*baḥr*)."

The Moses-cycle also uses *yamm* (Egyptian loan from Hebrew/Aramaic *yām*
"sea"):

- Q 20:39: Moses-infant cast into *al-yamm*; *al-yamm* casts him onto the
  *sāḥil* (the one and only *sāḥil* in the Quran).
- Q 20:78, 28:40, 51:40, 7:136: Pharaoh and his hosts drowned in *al-yamm*.
- Q 20:97: the calf of Sāmirī is incinerated and its ash scattered *fī al-yamm*.
- Q 28:7: Moses-infant cast into *al-yamm* (parallel to 20:39).

**Distributional signal**: *yamm* is used **only** in the Moses narrative
(and the fleeting 2:267/4:43/5:6 *tayammamū*). *Baḥr* is the universal word;
*yamm* is the Moses-specific geography — plausibly a register choice to
echo the Egyptian/Hebrew source of the story. When the text narrates **the
parting** (a miracle of divine command), it uses *baḥr* (Q 26:63, 20:77).
When it narrates **the drowning** (a judgment executed without Moses' verbal
strike), it uses *yamm* (Q 20:78, 28:40, 51:40, 7:136). *Baḥr* is the word
of the prophet's staff; *yamm* is the word of God's hand.

The *sāḥil* (Q 20:39) is a hapax: the edge where Moses' basket lands. It is
the geographic mirror of *jānib* — both mean "side/bank" but *sāḥil* is
marine, *jānib* is riverine/mountain. Moses is the prophet whose biography
plays across both banks.

## 6. Q 108 — al-Kawṯar

Sura 108 is three verses long and contains the water-word *kawṯar* (Q 108:1).
The root kvr means "abundance": it yields *akṯar* 80×, *kaṯīr* 63× — the
ambient root is simply "many". The superlative form *kawṯar* (on the pattern
*faʿwal*, a formal hapax in the Quran) occurs only here.

Classical tafsīr (al-Bukhārī, Ṣaḥīḥ, K. al-Raqāʾiq, #6578; al-Ṭabarī, ad loc.)
preserves the Prophetic hadith identifying *al-kawṯar* as a river in
paradise, "whiter than milk, sweeter than honey," whose banks are of hollow
pearl. This places *al-kawṯar* on the paradise-rivers map (§4): it is the
**named** paradise river, while Q 47:15's four rivers are anonymous.

Structurally, Q 108 is a pivot between:

- lexical **abundance** (kawṯar, from a 167-count root),
- the lexically **cut-off** enemy (*al-abtar*, a hapax root *btr*),

i.e. the surah is itself a muqābala: kawṯar ↔ abtar, abundance ↔ amputation.
The **naḥr** (*wa-nḥar*, Q 108:2 — "and sacrifice") shares three consonants
with nhr (river) but is a distinct root (n-ḥ-r vs n-h-r). The auditory
near-pun is likely deliberate: in a surah about the abundance-river,
the command is to *naḥr* — a phonic shadow of *nahr*.

## 7. Rain as revival — *ghayth*, *maṭar*, *māʾ min al-samāʾ*

The Quran has **two rain-words with opposite valences**:

- **ghayth** (root ḡyṯ "succour") — always positive. 4 occurrences:
  Q 12:49, 31:34, 42:28, 57:20. Of these, 3 of 4 are explicit
  **mercy/knowledge/revelation** metaphors.
- **maṭar** (root m-ṭ-r) — 14 of 15 occurrences are **punitive** (rain
  of stones on Sodom, rain of punishment). Only Q 4:102 (rain as a reason
  to put down weapons) is neutral.

Q 42:28 makes the identification explicit:

> *wa-huwa lladhī yunazzilu al-ghayṯa min baʿdi mā qanaṭū wa-yanshuru raḥmatah*
> "He is the one who sends down the *ghayṯ* after they have despaired and
> spreads His **mercy**."

The verse grammatically co-locates *ghayṯ* and *raḥma*. This is one node of a
denser pattern. Q 16:65, 22:5, 30:50, 43:11, 50:9 all instantiate the
**revival-by-rain** schema:

> *anzala min al-samāʾi māʾan fa-aḥyā bihi al-arḍa baʿda mawtihā*
> "He sent down water from the sky and gave life by it to the earth after
> its death."

The schema is then **explicitly analogised to resurrection**:

> *kaḏālika tukhrajūn* — "thus you (too) will be brought forth" (Q 43:11).
> *inna ḏālika la-muḥyī al-mawtā* — "indeed that (same power) is the reviver
> of the dead" (Q 30:50).

Revival-by-rain is therefore not a stock pastoral trope but a **forensic
exhibit**: the annual hydrological cycle is presented as a repeated
premonitory event, a built-in proof-text for resurrection. Q 31:34 lists
knowledge of "when the *ghayṯ* falls" among the five exclusive prerogatives
of God — along with knowledge of the Hour and of the womb. Rain, resurrection,
and gestation share one knowledge-register.

Q 57:20 then inverts the metaphor: the **worldly life itself** is like
*ghayṯ* whose vegetation delights the farmer — then dries, yellows, and
becomes dust. So *ghayṯ* marks both (a) the theology of mercy-revival and
(b) the aesthetics of transience. One word, two opposite rhetorical uses.

## 8. The four purifying uses — *wuḍūʾ*, *ghusl*, *tayammum*, and the paradox of water's absence

The ritual-purity verses are Q 5:6 and Q 4:43 — structurally parallel.
They name **three water-modes** and one non-water substitute:

| Mode | Verb / noun | Trigger | Referent |
|---|---|---|---|
| wuḍūʾ (minor ablution) | *f-gh-s-l* ("wash") faces, arms, feet; *m-s-ḥ* wipe head | rising to prayer (Q 5:6) | standard case |
| ghusl (major ablution) | *f-ṭ-h-r* "purify yourselves"; *ightasalū* (Q 4:43) | *janāba* — post-sexual state or post-ejaculation | the "junub" state, from root **jnb** |
| istijmār / istinjāʾ | not named by verb; implied by "comes from place of easement" | post-defecation | extra-Qurʾānic fiqh detail |
| tayammum (dry substitute) | *tayammamū ṣaʿīdan ṭayyiban* "aim for clean dust" | ill, travelling, or **no water found** | root **ymm** — same as yamm "sea" |

The semantic joke of the Quran's purity law is that the dry substitute for
water is called **tayammum**, from the same root (y-m-m) as **yamm** ("sea").
When the sea is unavailable, you "sea-it" symbolically with dust. The text
grammar encodes the mercy that *purity is intention-shaped*, not
substance-bound.

A second encoded detail: the state requiring ghusl is *janāba*, *junub*
(Q 4:43, 5:6), from root **jnb** — the same root that gives *jānib* ("side,
bank"). The ritually impure person is etymologically "set-apart-to-one-side".
Water restores them to the centre. The verb *ijtanibū* "avoid" (9 occurrences,
e.g. Q 5:90 "avoid intoxicants and gambling") is the same verb: avoidance
is side-stepping, and the impure is the self side-stepped.

So the cluster **water / bank / avoidance / impurity** is etymologically
one word-family in the Quran — impurity is being pushed to the bank of the
river of prayer, and water is the return to midstream.

## 9. Network summary

The water lexicon resolves into a three-tier system:

**Tier 1 — the substrate.** *māʾ* (63 occurrences). Undifferentiated. This
is the word of Q 21:30 and Q 24:45; the word of the womb; the word of the
paradise-river Q 47:15.

**Tier 2 — bodies and qualifications.** *baḥr* (sea, 41) + *yamm* (Moses-sea,
8) + *nahar* (river, 54) + *ʿayn* (spring, 57) + *biʾr* (well, 1) + *sāḥil*
(shore, 1) + *jānib* (bank, 9). Each lexeme marks a geographic facet.
The *yamm* / *baḥr* split is register-sensitive (Egyptian / universal).
*biʾr* and *sāḥil* are hapax pinpoints.

**Tier 3 — states and transitions.** *ghayth* (rescuing rain, 4) + *maṭar*
(punishing rain, 15) + *rīḥ* (wind, 29) + *mawj* (wave, 7) + *sayl* (flood,
4). These are the verbs of water — water in motion, water as event.

The semantic duals lock into eleven muqābalas:

| Pair | Texts |
|---|---|
| fresh / salt (*ʿaḏb*-*furāt* / *milḥ*-*ujāj*) | 25:53, 35:12 |
| sea / sea (yamm / baḥr) | 20:39 vs 20:77 |
| rain-mercy / rain-punishment (ghayth / maṭar) | 42:28 vs 26:173 |
| water-of-paradise / ḥamīm-of-hell | 47:15 |
| rivers-of-life / ghassāq | 47:15 / 38:57 |
| water-found / water-absent (wuḍūʾ / tayammum) | 5:6 |
| pure / impure (ṭahāra / janāba) | 5:6 |
| wave-hides / light-reveals | 24:40 |
| sweet / sunken (*ʿadhb maʿīn* / *māʾ ghawr*) | 67:30 |
| sea-split (infalaqa) / sea-sealed (baḥr masjūr) | 26:63 / 52:6 |
| sea/land (baḥr/barr) | paired-opposites (§1) |

This is considerably denser than any non-water semantic field except
light-vs-darkness. Water is the Quran's most *internally-muqābala-saturated*
lexical network — a cosmos organised by salt/sweet, rescue/punishment,
found/absent, life/death.

## 10. Open questions (for later phases)

1. **Kawṯar abjad.** Does the gematria of *al-kawṯar* (ك و ث ر = 20+6+500+200
   = 726, or with alif-lam 757) stand in any numerical relation to the
   four-rivers verse (47:15) or to the count of *anhār* formula occurrences
   (39)? Flag for phase-c.
2. **Moses word-choice typology.** Is every *yamm* attestation paired with a
   verb of divine agency (drowning, throwing), and every Moses-*baḥr*
   attestation with a verb of Moses' agency (strike, walk)? A 10-verse
   corpus is small but tractable — flag for manual review.
3. **Ghayth / raḥma co-occurrence baseline.** Q 42:28 co-locates the two
   explicitly. Is the Fisher-exact enrichment of raḥm × ghyv significant
   despite the tiny n? With only 4 ghayth occurrences, p-values will be
   noisy; a joint-prior Bayesian estimate is probably more honest.
4. **Paradise / hell water symmetry.** Q 47:15 pairs four positive rivers
   with one negative drink. Elsewhere the inventory is richer on the hell
   side (*ḥamīm*, *ghassāq*, *ṣadīd*, molten *qaṭr*). Is there a structural
   asymmetry — paradise-water diversifies *by flavour*, hell-water
   diversifies *by harm*?
5. **Tayammum / yamm polysemy.** Is the assonance a coincidence of Arabic
   morphology or an intentional Quranic choice? Lisān al-ʿArab notes the
   verb *yammama* ("to aim for") is older than the noun *yamm* in
   lexicographic order; the Quran may be the first text to yoke them.

## 11. Methodological notes

- All counts derive from Leeds QAC v0.4 root assignment. The *nhr* /
  *nahār* / *tanhar* split is lemma-based, not root-based; QAC merges
  all three under one root.
- The "yamm / tayammam" shared root is a QAC artefact but is lexicographically
  correct: classical Arabic grammarians derive *tayammama* from *yammama*
  "to face/aim" which shares at least the y-m consonantal base with *yamm*
  "sea". We do not claim they are synchronically felt as one word, but
  morphologically they share a root.
- Co-occurrence counts use the same verse-universe (6236) as the paired-opposites
  file. No stemming errors were detected in manual spot-checks of ten random
  hits per root.
- Classical corroboration: al-Ṭabarī (ad 21:30, 25:53, 47:15), al-Rāzī
  (Mafātīḥ al-Ghayb on 55:19–22), al-Qurṭubī (al-Jāmiʿ on 108:1 and 47:15),
  Ibn Kathīr (on 20:39, 26:63) — all cited loci read in advance of drafting
  this file. No commentator was contradicted; several of the lexical
  observations above (yamm / tayammum coupling, ghayth / maṭar valence
  split, jnb / janāba etymology) are noted in al-Rāghib al-Iṣfahānī's
  *Mufradāt* and reproduced here with fresh counts.
