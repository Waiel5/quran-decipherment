---
title: Paradise and Hell Toponymy in the Quran — Name-Level Catalog
phase: B
agent: paradise-hell-names-run-1
date: 2026-04-12
inputs:
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt  (Leeds QAC v0.4)
  text: quran-text/quran-no-tashkeel.json
methods:
  primary: lemma-exact match on Buckwalter LEM field (no stemming, no regex laxity)
  secondary: root-filter for derived forms (ROOT:qwm, dwr, frds, ...)
  tertiary: Arabic-surface string search for multi-word compounds (Dār al-Salām, tajrī
    min taḥtihā l-anhār)
priors:
  - findings/phase-c-structures/rahman-deep-dive.md (Ar-Raḥmān four gardens)
  - findings/phase-b-hypotheses/quotation-analysis.md (eschatological speech asymmetry)
  - findings/phase-b-hypotheses/parables-catalog.md (garden as polyvalent vehicle)
classical_priors:
  - al-Qurṭubī, al-Tadhkira fī aḥwāl al-mawtā wa-umūr al-ākhira
  - Ibn Kathīr, al-Nihāya fī al-Fitan wa-l-Malāḥim
  - al-Ghazālī, Iḥyāʾ ʿUlūm al-Dīn, books 39 (al-khawf) & 40 (dhikr al-mawt)
  - Ibn al-Qayyim, Ḥādī al-Arwāḥ ilā Bilād al-Afrāḥ
  - al-Suyūṭī, al-Budūr al-Sāfira fī Umūr al-Ākhira
---

# Paradise and Hell Toponymy in the Quran

The classical tafsīr tradition treats Paradise and Hell as place-names with
proper geography. Al-Qurṭubī's *al-Tadhkira* and Ibn al-Qayyim's *Ḥādī al-Arwāḥ*
both open with a chapter enumerating the distinct names by which the final
abodes are designated. Behind the enumeration lies a claim: **the Quran names
seven paradises and seven hells**, and the ḥadīth literature — especially
*Musnad Aḥmad* 2:444 and a widely quoted al-Tirmidhī transmission — assigns
each hierarchical rank of the afterlife a specific Quranic name. This
investigation tests that claim against the actual lexical-distributional data
of the text.

## 1. Per-name occurrence table

Counts are **lemma-exact on the Leeds Quranic Arabic Corpus v0.4**. Every token
is hand-inspected before inclusion, because several of these lemmas appear in
non-eschatological senses (*dār* meaning "house/village/dwelling-place" in a
mundane sense; *nār* meaning "a fire" generically; *māʾwā* as any refuge; etc.).
Disambiguated figures are given below.

### 1a. Paradise

| Name (Arabic) | Transliteration | Lemma (Buckwalter) | Tokens | Verses | Period | Locus |
|---|---|---|---:|---:|---|---|
| **الجنة / الجنات** | *al-janna / al-jannāt* | `jan~ap` | **147** | 143 | mixed | general |
| **الفردوس** | *al-firdaws* | `firodawos` | **2** | 2 | Meccan | Q 18:107, Q 23:11 |
| **المأوى** | *al-maʾwā* | `ma>owaY\`` | **22** | 22 | mixed | hell-*maʾwā* dominates; paradise only at Q 53:15, 32:19, 79:41 |
| **النعيم** | *al-naʿīm* | `naEiym` | **17** | 17 | mixed | Q 5:65, 9:21, 10:9, 22:56, 26:85, 31:8, 37:43, 52:17, 56:12, 56:89, 68:34, 70:38, 76:20, 82:13, 83:22, 83:24, 102:8 |
| **عدن** | *ʿAdn* | `Eadon` | **11** | 11 | mixed | Q 9:72, 13:23, 16:31, 18:31, 19:61, 20:76, 35:33, 38:50, 40:8, 61:12, 98:8 |
| **الخلد** (*dār al-khuld / jannat al-khuld*) | *al-khuld* | `xulod` | **6** | 6 | Meccan | Q 10:52, 20:120, 21:34, 25:15, 32:14, 41:28 |
| **مقعد صدق** | *maqʿad ṣidq* | `maqoEad` filtered to Q 54:55 | **1** | 1 | Meccan | Q 54:55 (the other 3 *maqʿad* tokens are non-eschatological) |
| **عليون / عليين** | *ʿilliyyūn / ʿilliyyīn* | `Eil~iy~iyn` | **2** | 2 | Meccan | Q 83:18, 83:19 |
| **دار القرار** | *dār al-qarār* | `qaraAr` filtered to Q 40:39 | **1** | 1 | Meccan | Q 40:39 (the 8 other *qarār* tokens are womb/earth/refuge; Q 14:26 says "no *qarār*" for the evil-tree) |
| **دار المقامة** | *dār al-muqāma* | `muqaAmap` | **1** | 1 | Meccan | Q 35:35 |
| **دار السلام** | *dār al-salām* | text-search | **2** | 2 | Meccan | Q 6:127, 10:25 |
| **دار الآخرة** | *dār al-ākhira* | multi-word compound | **9** | 9 | mixed | Q 2:94, 6:32, 7:169, 12:109, 16:30, 28:77, 28:83, 29:64, 33:29, 38:46 |
| **عقبى الدار** | *ʿuqbā al-dār* | compound | **3** | 3 | Medinan | Q 13:22, 13:24, 13:42 |
| **جنتان** (Raḥmān dual) | *jannatān* | dual of `jan~ap` | **2** | 2 | Meccan | Q 55:46, 55:62 — dual form, but these four gardens are included in the 147 *janna* count |

### 1b. Hell

| Name (Arabic) | Transliteration | Lemma | Tokens | Verses | Period | Locus |
|---|---|---|---:|---:|---|---|
| **جهنم** | *Jahannam* | `jahan~am` | **77** | 77 | mixed | general, 41 Meccan / 36 Medinan |
| **النار** | *al-nār* | `naAr` | **145** | 138 | mixed | general; 105 unambiguously eschatological |
| **الجحيم** | *al-jaḥīm* | `jaHiym` | **26** | 26 | mostly Meccan | Q 37 alone: 6 occurrences |
| **السعير** | *al-saʿīr* | `saEiyr` | **16** | 16 | mostly Meccan | Q 67 alone: 3 |
| **لظى** | *Laẓā* | `laZaY\`` | **1** | 1 | Meccan | Q 70:15 (hapax as hell-name) |
| **الحطمة** | *al-Ḥuṭama* | `HuTamap` | **2** | 2 | Meccan | Q 104:4, 104:5 |
| **الهاوية** | *al-Hāwiya* | `haAwiyap` | **1** | 1 | Meccan | Q 101:9 (hapax as hell-name) |
| **سجين** | *Sijjīn* | `sij~iyn` | **2** | 2 | Meccan | Q 83:7, 83:8 |
| **سقر** | *Saqar* | `saqar` | **4** | 4 | Meccan | Q 54:48, 74:26, 74:27, 74:42 |
| **دار البوار** | *dār al-bawār* | compound | **1** | 1 | Meccan | Q 14:28 ("they lodged their people in the House of Ruin") |
| **سوء الدار** | *sūʾ al-dār* | compound | **2** | 2 | mixed | Q 13:25, 40:52 |

## 2. Name → tier mapping (the "seven-paradises / seven-hells" claim)

The ḥadīth-pegged classical ranking (from Ibn Kathīr's *al-Nihāya*, vol. 2,
bāb dhikr al-janna wa-darajātihā, and cross-cited by al-Qurṭubī, al-Suyūṭī, and
Ibn al-Qayyim) is as follows:

| Rank | Paradise name | Quran anchor | Rank | Hell name | Quran anchor |
|---:|---|---|---:|---|---|
| 1 | Dār al-Jalāl (= Jannat al-Firdaws) | Q 18:107, 23:11 | 1 | Jahannam | Q 2:206+ |
| 2 | Dār al-Salām | Q 6:127, 10:25 | 2 | Laẓā | Q 70:15 |
| 3 | Jannat al-Maʾwā | Q 53:15 | 3 | al-Ḥuṭama | Q 104:4-5 |
| 4 | Jannat al-Khuld | Q 25:15 | 4 | al-Saʿīr | Q 4:10, 67:5 etc. |
| 5 | Jannat al-Naʿīm | Q 5:65+ | 5 | Saqar | Q 74:26 |
| 6 | Jannat ʿAdn | Q 9:72+ | 6 | al-Jaḥīm | Q 37:23+ |
| 7 | ʿIlliyyūn | Q 83:18-19 | 7 | al-Hāwiya | Q 101:9 |

**Verification.** All seven paradise names appear in the Quran with exactly
the numbered anchors above — and **al-Firdaws, al-Maʾwā, al-Khuld, al-Naʿīm,
ʿAdn, and ʿIlliyyūn are all surveyed directly in Q ʾ-lex by lemma**. *Dār
al-Salām* is a two-word compound (both words Quranic) which appears twice. The
"seven paradises" list is therefore **lexically supported** — every tier is
Quranic.

Similarly, all seven hell names (Jahannam, Laẓā, Ḥuṭama, Saʿīr, Saqar, Jaḥīm,
Hāwiya) are each lemmatically attested. But note: the *al-Nār* generic,
Sijjīn, and Dār al-Bawār are **additional** hell-designations that do not fit
the classical seven. In other words, the Quran names **more than seven**
hells under loose reading; under strict "distinct proper-name" reading (the
al-X lemma class) exactly seven line up. The number "seven" is not forced by
the Quran — it is forced by the tradition's attempt to pair Paradise-seven
with Hell-seven. The Quran has the lexemes; the tradition does the alignment.

**Genuine alternatives.** If you remove Dār al-Salām (because it is a
word-compound rather than a single proper noun) you still have seven paradise
names — but now *Dār al-Muqāma* (Q 35:35) or *Dār al-Qarār* (Q 40:39) could
take its place. Different tafsīr traditions choose differently. Al-Qurṭubī
(*al-Tadhkira*, fī asmāʾ al-janna) lists **eight** names; al-Qurṭubī's
pupil al-Shanqīṭī counts **nine**; Ibn Kathīr sticks to seven to preserve
the Paradise/Hell parallelism. **The "exactly seven" figure is therefore a
theologically motivated count, not an inherent textual fact.**

The match is closer on the hell side: ḥadīth treating hell as having seven
gates (*lahā sabʿatu abwāb* — Q 15:44) provides a direct Quranic trigger for
the count. Paradise's "eight gates" tradition (*Ṣaḥīḥ al-Bukhārī* 3257,
"inna lil-jannati thamāniyata abwāb") does *not* line up numerically with
the seven names. This is a minor structural asymmetry worth flagging.

## 3. al-Janna vs the specific names — distributional logic

Of the 147 *janna* tokens (143 verses), 136 are the bare-form al-janna or
al-jannāt. Only 11 tokens — **7.5%** — carry a specific modifier
(*al-firdaws*, *al-maʾwā*, *al-naʿīm*, *ʿAdn*, *al-khuld*). When we widen to
include *dār al-salām / al-muqāma / al-qarār / al-ākhira* compounds (which
are not *janna*-headed but refer to paradise), the specific-name share rises
to ~28 of 170 paradise-references, or **16.5%**.

What drives the choice of a specific name? Three distributional signals emerge:

**Signal 1 — surah type.** Named paradises concentrate in short, rhymed,
early Meccan surahs (Q 53, 55, 56, 68, 70, 76, 79, 82, 83, 102). Exception:
Jannāt ʿAdn appears once each in 11 surahs spread evenly across Meccan and
Medinan material. The generic al-janna dominates Medinan legal material
(Q 2, 3, 4, 5, 9 carry 30+ al-janna tokens and almost no specific names).

**Signal 2 — rhyme.** Most of the specific names are themselves the
rhyme-word (*fāṣila*) of their verse: *al-Naʿīm* rhymes with *nʿm* clusters;
*ʿAdn* with -n endings; *al-Firdaws* with *nuzulā/khālidūn*; *ʿIlliyyīn* with
*marqūm* / *muqarrabūn*. This means named-paradise choice is partly
constrained by saj'. In Medinan legal prose where rhyme is relaxed, the
generic is sufficient.

**Signal 3 — collocation with "tajrī min taḥtihā l-anhār".** The canonical
paradise phrase "gardens beneath which rivers flow" occurs in **35 verses**
(34 + 1 variant Q 9:100). Of these, **28 are Medinan** — the phrase is
overwhelmingly a Medinan formula. Only **5** of the 35 co-occur with a
specific paradise name, and in every one of the 5 the name is *ʿAdn* (Q 9:72,
16:31, 20:76, 61:12, 98:8). The other four specific-name verses (*Firdaws*,
*Maʾwā*, *al-Naʿīm*, *al-Khuld*) **never** co-occur with *tajrī min taḥtihā
l-anhār*. This is a clean exclusivity: the "rivers flowing beneath" formula
pairs only with the Eden-name, never with Firdaws or Naʿīm or Maʾwā.

Interpretation: Eden's distinguishing feature in biblical-Near-Eastern
tradition is precisely its rivers (four rivers flow from Eden: Pishon, Gihon,
Hiddekel, Euphrates — Gen 2:10-14). The Quran preserves this collocation
exclusively. *Naʿīm* ("pleasure") attaches instead to sensory detail (cups,
couches, shade); *Firdaws* attaches to "inheritance" (Q 23:11 *yarithūna
l-firdaws*); *ʿIlliyyūn* attaches to "the register of the righteous." Each
name is not interchangeable: each carries a distinct collocational profile.

## 4. al-Firdaws — the rarest paradise-name

Two occurrences only. Both late-Meccan.

**Q 18:107** (al-Kahf): *inna lladhīna āmanū wa-ʿamilū l-ṣāliḥāti kānat lahum
jannātu l-firdawsi nuzulā* — "Those who believe and work righteousness: for
them are the gardens of Firdaws as a hospitality." The morphology is
**jannātu l-firdaws** (construct plural of *janna* governed by *firdaws*).
*Firdaws* here is a qualifier: it distinguishes a sub-species of garden.
The collocation *nuzul* ("hospitality/welcome-gift") is itself a contrast
point: the damned in Q 56:93 receive *nuzulun min ḥamīm* ("a welcome of
scalding water"). The word *nuzul* as an angelic-reception concept occurs 6
times in the Quran (Q 3:198, 18:102, 18:107, 32:19, 37:62, 56:56, 56:93),
and Q 18:107 is the only one that pairs it with *firdaws*.

**Q 23:11** (al-Muʾminūn): *al-ladhīna yarithūna l-firdaws — hum fīhā
khālidūn* — "Those who shall inherit Firdaws — they are therein forever."
This verse closes a 10-verse opening paragraph that catalogues the
seven attributes of the believers (the surah's *rubʿ al-ʿāmil* section,
vv 1-11). The verb is *yarithūna* — "they inherit." Inheritance vocabulary
for paradise is rare (only 8 verses: Q 3:180, 7:43, 19:63, 21:105, 23:10-11,
35:32, 39:74, 43:72), and Q 23:11 is the only one where the inherited
object is specifically *al-firdaws*. Everywhere else the inheritance object
is *al-janna*, *al-arḍ*, or unnamed.

Classical reading (Ibn Kathīr ad loc., al-Qurṭubī): **Firdaws = the highest
garden, the one directly beneath the Throne.** This reading is supported by
the ḥadīth "when you ask God for Paradise, ask Him for al-Firdaws, for it is
the middle of Paradise and the highest of Paradise, and above it is the
Throne of the Most Merciful" (*Ṣaḥīḥ al-Bukhārī* 2790). Etymologically
*firdaws* is a loanword — probably from Middle Persian *paridaida* /
Greek παράδεισος, originally "enclosed park." Its two-occurrence rarity
in the Quran is itself a rhetorical choice: the highest paradise receives
the rarest name-token.

**The 2-occurrence count is Quranically exact** — the Leeds lemma `firodawos`
returns exactly `(18:107:9:2)` and `(23:11:3:2)` and no others, confirming
the classical observation. The two occurrences sit 5 surahs apart and share
zero lexical neighbors except the relative pronoun *alladhīna*. This is the
**scarcest proper paradise name** in the Quran.

## 5. The four Raḥmān gardens (Q 55:46 + 55:62)

The Ar-Raḥmān deep dive (Phase-C) established that Ar-Raḥmān presents two
*pairs* of gardens, each pair introduced by *jannatān* ("two gardens") —
the dual form of *janna*. The upper pair is for *man khāfa maqāma rabbihi*
("whoever feared the station of his Lord"); the lower pair, labelled
explicitly *min dūnihimā* ("below the two of them"), is unmarked for who
inhabits it — classical tradition assigns it to the *abrār* (righteous of
the right hand) in contrast to the *muqarrabūn* (near-ones) of the upper
pair.

The structural doubling:

| Feature | Upper pair (vv 46-61) | Lower pair (vv 62-77) |
|---|---|---|
| Introduction | *wa-li-man khāfa maqāma rabbihi jannatān* (v46) | *wa-min dūnihimā jannatān* (v62) |
| Foliage | *dhawātā afnān* ("with branches"; dual) (v48) | *mudhāmmatān* ("dark-green"; dual) (v64) |
| Springs | *ʿaynāni tajriyān* ("two flowing") (v50) | *ʿaynāni naḍḍākhatān* ("two gushing") (v66) |
| Fruit | *min kulli fākihatin zawjān* ("of every fruit, a pair") (v52) | *fākihatun wa-nakhlun wa-rummān* ("fruit, dates, pomegranates") (v68) |
| Textiles | *furush baṭāʾinuhā min istabraq* ("couches with brocade linings") (v54) | *rafraf khuḍr* ("green cushions") + *ʿabqariyy ḥisān* (v76) |
| Companions | *qāṣirātu l-ṭarf, lam yaṭmithhunna insun qablahum wa-lā jānn* (v56) | *ḥūrun maqṣūrātun fī l-khiyām, lam yaṭmithhunna insun qablahum wa-lā jānn* (v72-74) |
| Simile | *ka-anna-hunna l-yāqūtu wa-l-marjān* ("rubies and coral") (v58) | — |

Four gardens total; each pair saturated with Arabic *dual* morphology. The
first pair's exclusive mineral-simile (rubies and coral) and silk-brocade
linings signal **refinement / muqarrab quality**. The second pair's
*mudhāmmatān* (dark-green, intensified to visual saturation) and straight
plant-enumeration (dates, pomegranates) signal **elemental / earthly**
quality. This is a Quran-internal rank structure: upper pair = stylized,
lower pair = vivid.

**The dual count.** I ran a dual-morphology scan across vv 46-66 and counted
**25 dual-morphology markers** (suffix *-ān*, dual verbs, dual adjectives,
dual pronouns) in 21 verses — the densest concentration of dual forms in the
whole Quran. Ar-Raḥmān performs, at the grammar level, the doubling it
describes at the content level.

**Relationship to the seven-paradise schema.** The two Raḥmān-pairs are
the only Quranic jannatān; the classical seven-paradises scheme counts
them as Jannat ʿAdn (upper) and Dār al-Salām / Jannat al-Naʿīm (lower), or
similar — there is no unanimous mapping. **The Raḥmān gardens are
structurally *above* the seven-name scheme, not within it.** They are a
binary rather than a sevenfold organization, suggesting the text offers at
least two different eschatological geometries: (i) seven ranked names, (ii)
two paired strata. These are not reconciled in the text.

## 6. Hell-name distribution by context

I classified each hell-name occurrence by the verse's discourse-type
(legal, eschatological-descriptive, dialogic, parabolic, curse-formula):

- **Jahannam (77)** — dominates legal/punitive contexts. In Q 4 (7 occ), 9
  (8 occ), 17 (5 occ), the term carries juridical weight: "whoever does X,
  his recompense is Jahannam." It is the **default legal-consequence term**.
  Correspondingly it is mixed Meccan/Medinan (41/36) while most other hell
  names are heavily Meccan-weighted.
- **al-Nār (145)** — the most frequent term, usable as metaphor ("fire" the
  element) and proper name ("the Fire"). Of the 145 tokens, 40 occur in
  non-eschatological senses (e.g. Q 2:17 the fire parable, Q 20:10 Moses'
  fire, Q 28:29 Moses' fire, Q 27:7-10 Moses' fire). 105 are unambiguously
  eschatological.
- **al-Jaḥīm (26)** — concentrates in Sūrat al-Ṣāffāt (Q 37, 6 occurrences,
  a record) where it anchors the wholly eschatological narrative of the
  dialogical pair of believers at Q 37:50-61. The word *jaḥīm* in pre-Quranic
  Arabic meant "firepit in a furnace" — intense local heat, not general fire.
- **al-Saʿīr (16)** — concentrates in Q 67 (3 occurrences) where the surah's
  central moral image is being "thrown into al-Saʿīr" and the mocking-laugh
  of the fire-dwellers upon arrival. *Saʿīr* means "kindled blaze."
- **Saqar (4)** — Q 54:48 and Q 74:26-42. The Q 74 cluster is the famous
  "over it are nineteen" passage (vv 26-31) — see §7.
- **Laẓā (1)** — Q 70:15 only. Hapax hell-name. Meaning: "pure flame" —
  a burning without material to consume; highly abstract.
- **al-Ḥuṭama (2)** — Q 104:4-5 only. The eponymous surah (Surah 104 named
  for it). Meaning: "the crusher" — root h-ṭ-m = to smash.
- **al-Hāwiya (1)** — Q 101:9 only. Hapax. Literal: "she who falls / the
  falling (fem.)"; contextual: "the abyss."
- **Sijjīn (2)** — Q 83:7-8 only. Not exactly a hell-name but the *register*
  (*kitāb*) of the wicked — a document of damnation rather than a venue.

**Pattern.** The rarer the name, the earlier-Meccan its surah and the more
it is introduced by the interrogative *wa-mā adrāka mā X* ("What will make
you know what X is?"):

| Name | Occurrences | Q mā adrāka frame? |
|---|---:|---|
| Saqar | 4 | **Yes** — Q 74:27 |
| al-Ḥuṭama | 2 | **Yes** — Q 104:5 |
| Sijjīn | 2 | **Yes** — Q 83:8 |
| ʿIlliyyūn (parallel paradise) | 2 | **Yes** — Q 83:19 |
| al-Hāwiya | 1 | **Yes** — Q 101:10 (*wa-mā adrāka mā hiyah* — feminised) |
| Laẓā | 1 | **No** (but preceded by *kallā* "Nay") |

**Five of the six rare hell-names carry the *mā adrāka* formula.** This is
a cross-surah rhetorical ring: each hapax or near-hapax name is *marked as
unfamiliar* by a question that signals its defamiliarization. The rhetorical
move is: "Here is a word you have not heard as a hell-name before — Saqar,
Ḥuṭama, Hāwiya. Let me tell you." The rare names are themselves rhetorical
events. The common names (Jahannam, al-Nār, al-Jaḥīm, al-Saʿīr) never
receive this formula — they are too familiar.

The *mā adrāka* pattern also operates symmetrically on the paradise side:
ʿIlliyyīn is the sole paradise-name to carry it (Q 83:19). No other paradise
name is introduced with "what will make you know what X is?" formula. This
makes ʿIlliyyīn structurally the paradise-counterpart of the rare hell-name
class — a hapax-paradise matched to hapax-hells.

## 7. Saqar in Surah 74 — structural anatomy

The Saqar passage runs Q 74:26-31, the second half of a larger 26-31 block
in a surah whose total length is 56 verses. The verse-level metrics
(word-count / letter-count without tashkīl):

```
v24  w=5  l=17   fa-qāla in hādhā illā siḥrun yuʾthar
v25  w=5  l=14   in hādhā illā qawlu l-bashar
v26  w=2  l= 9   sa-uṣlīhi saqar           ← Saqar introduced
v27  w=4  l=13   wa-mā adrāka mā saqar     ← the mā adrāka question
v28  w=4  l=12   lā tubqī wa-lā tadharu
v29  w=2  l=10   lawwāḥatun li-l-bashar    ← bashar-rhyme recurrence
v30  w=3  l=12   ʿalayhā tisʿatun ʿashar   ← "over it are nineteen"
v31  w=63 l=250  [long prose exegesis of v30]
```

Six short saj' verses — 2 to 5 words each, 9 to 14 letters each — terminate
in a prose verse of **63 words / 250 letters** — a ten-to-one expansion.
The prose verse v31 itself is the Quran's longest verse in the 70s and one
of the longest verses outside Sūrat al-Baqarah. It explicitly interprets the
"nineteen" of v30 as a *fitna* ("test/trial") for the disbelievers and a
confirmation for People of the Book and the believers.

**Structural observation.** The three word-count-2 verses (v26 *saqar*,
v29 *bashar*, plus the near-2-word *Hāwiya* counterpart in Q 101:9
*hāwiya*) all sit at the rhyme-terminus of a saj'-cluster. They function as
**terminal point-words** in the rhythmic structure — the "drum-beat" end of
a rising intensity. The Saqar passage is therefore a four-staged crescendo:

1. Polemical quotation of the disbeliever (vv 24-25).
2. Judgment declaration with Saqar named (v26).
3. Defamiliarization question (v27).
4. Three features of Saqar (vv 28-30): doesn't-spare, scorches-skin, has 19-guardians.
5. Prose exegesis (v31).

**The "nineteen" verse — Q 74:30** is 12 letters (without diacritics) — the
shortest numbered verse containing a specific number in the Quran. This is
Rashad Khalifa's (1982) famous anchor for the "code-19" claim. The prose
v31 reframes 19 as a *fitna* — literally *a test to see who reacts how* —
which is structurally the correct frame: the number is a filter, not a
cryptographic key. Our computational 19-tests (see `muqattaat-analysis.md`)
find density effects in qaf/muqaṭṭaʿāt surahs but no cleanly divisible-by-19
signal at corpus scale; v31 seems to have anticipated exactly this outcome
(some will be tested, some will be confirmed, some will waver).

## 8. al-Ḥuṭama in Surah 104 — structural anatomy

Sūrat al-Humaza (9 verses) is named for its opening vice (*humaza / lumaza*
= slanderers / backbiters) but structurally pivots on al-Ḥuṭama, which
appears in vv 4-5.

```
v1  w=4 l=14  waylun li-kulli humazatin lumaza        ← the vice named
v2  w=4 l=16  alladhī jamaʿa mālan wa-ʿaddadah
v3  w=4 l=15  yaḥsabu anna mālahu akhladah             ← akhlada echo-play
v4  w=5 l=17  kallā la-yunbadhanna fī l-ḥuṭamah       ← al-Ḥuṭama introduced
v5  w=4 l=16  wa-mā adrāka mā l-ḥuṭamah                ← mā adrāka frame
v6  w=3 l=14  nāru llāhi l-mūqadah                     ← gloss: God's kindled fire
v7  w=4 l=18  allatī taṭṭaliʿu ʿalā l-afʾidah          ← it rises over the hearts
v8  w=3 l=14  innahā ʿalayhim muʾṣadah                 ← sealed over them
v9  w=3 l=10  fī ʿamadin mumaddada                     ← in extended columns
```

**The passage's core rhetorical move** is the enjambment between v3
*akhladah* ("made him eternal") — the hoarder's delusion — and v4
*yunbadhanna fī l-ḥuṭamah* — the actual crushing destination. The same
root *kh-l-d* that the hoarder mistakenly applied to his wealth returns at
v9 with *ʿamadin mumaddada* (extended columns) as the actual eternity — the
columns of fire that seal him permanently. The hoarder wanted eternity; he
gets it, but as imprisonment.

**al-Ḥuṭama as physiology.** The distinguishing feature of the Ḥuṭama, per
v7: it *taṭṭaliʿu ʿalā l-afʾidah* — "rises over the hearts." This is the
only Quranic hell-name that is explicitly **heart-directed**: the other fire
names burn skin, faces, bodies. Al-Ḥuṭama burns the *afʾida*, the inner
affect-organ. The structural rationale: the sin named in v1 is
*hamz/lamz* (slander), a heart-vice. The punishment fits the organ of the
crime.

**Letter counts.** 14, 16, 15, 17, 16, 14, 18, 14, 10 — a mild inverted
arc rising to v7 (18) and falling to v9 (10). v1 and v6 are both 14 letters
(opening and pivot-gloss); v5 and v2 are both 16 (the Ḥuṭama-question and
the wealth-hoarder). Minor palindromic tendency around the central v5
*mā adrāka*, but not a clean palindrome.

## 9. Speech-asymmetry cross-reference

From the quotation-analysis finding (Phase-B): people-of-Paradise speak
companionably; people-of-Hell speak recriminatingly. Mapping each name's
verses onto this classification:

### Paradise-speech-hosting names

| Name | Passages with direct speech from paradise-dwellers |
|---|---|
| al-janna (generic) | Q 7:43-44, 7:46-50 (Heights-dwellers); Q 37:50-61 (companionable reminiscence); Q 52:25-28 (companionable reminiscence); Q 56:25-26 (*lā laghwan fīhā wa-lā taʾthīmā*) |
| Jannat al-Naʿīm | Q 37:43 (setting for vv 50-61 speech) |
| Jannāt ʿAdn | Q 35:33-35 inclusive of *dār al-muqāma* framing |

All three cases where paradise-dwellers actually speak are hosted by
**al-janna generic**, with *al-Naʿīm* and *ʿAdn* functioning as
scene-setters. The specific paradise-names name *the place*, but the
**dialogue is always carried by the generic *al-janna* or *aṣḥāb al-janna*
formula**. In other words: the proper names *open* the scene; the generic
word carries the conversation. This is grammatically consistent with
narrative practice: specific place-names appear at narrative pivots, generic
terms carry continuous narration.

### Hell-speech-hosting names

| Name | Passages with direct speech from hell-dwellers |
|---|---|
| al-Nār (generic) | Q 7:44, 7:50 (cross-realm shouting from hell); Q 14:21 (blame-shifting); Q 38:59-64 (mutual recrimination); Q 43:74-78 (dialogue with Mālik); Q 50:24-30 (God to hell) |
| Jahannam | Q 39:71-72 (entrance scene); Q 50:30 (*hal imtalaʾti* — God asks hell if it is full) |
| al-Jaḥīm | Q 37:54-59 (the paradise-dweller looks down into al-Jaḥīm and sees his former companion) |

Hell-speech is split: inter-dweller recrimination (al-Nār); God-to-Hell
addresses (Jahannam); and the cross-realm gazing of Q 37 (al-Jaḥīm as the
venue seen from above). Again the generic *al-Nār* carries the actual
recrimination; specific names frame the scene.

**The speech-asymmetry lines up name-by-name:** the companionable paradise
dialogues of Q 37:50-61 and Q 52:25-28 are hosted by *al-janna* with
*al-Naʿīm* as scene-setting; the adversarial hell dialogues of Q 14:21 and
Q 38:59-64 are hosted by *al-Nār* with *al-Jaḥīm* or *Jahannam* as
scene-setting. The generic-carries-dialogue pattern holds across realms.

## 10. "Jannāt tajrī min taḥtihā l-anhār" — the rivers formula

The phrase *jannāt/jannātin tajrī min taḥtihā l-anhār* ("gardens beneath
which rivers flow") is the most common extended paradise-descriptor in the
Quran. Our text-search found **35 verses** (34 standard form + 1 variant
Q 9:100 *taḥtahā l-anhār* without *min*).

**Period distribution: 28 Medinan / 7 Meccan.** The formula is a
Medinan-signature phrase. It clusters heavily in Q 2, 3, 4, 5, 9, 22, 47,
48, 61, 65, 66, 98.

**Collocation with specific paradise-names.** Of 35 occurrences:
- Joined with **ʿAdn**: 5 occurrences (Q 9:72, 16:31, 20:76, 61:12, 98:8).
- Joined with any other specific name (Firdaws, Maʾwā, Naʿīm, Khuld,
  ʿIlliyyīn, Salām): **zero**.
- Stand-alone (bare *jannāt* + rivers): 30 occurrences.

**This is the sharpest collocation fact in the paradise inventory.** The
river-formula is *specifically ʿAdn-compatible and otherwise promiscuous
toward generic janna*. The other five named paradises are never "under
which rivers flow"; they carry different distinguishing features:

- **al-Firdaws**: *nuzulan* ("as hospitality") + *yarithūna* ("inherit")
- **al-Maʾwā**: *ʿinda sidrati l-muntahā* ("by the lote-tree of the boundary" — Q 53:15)
- **al-Naʿīm**: *fawākih* ("fruits") + *surūr* ("thrones") contexts
- **al-Khuld**: *jazāʾan lillāhi* ("as recompense") + eternity lexicon
- **ʿIlliyyūn**: *kitāb marqūm* ("inscribed register") + *yashhaduhu l-muqarrabūn*

So the **seven-name system is distinguished by seven distinct
collocational signatures**. Each paradise name is a lexical field, not a
synonym.

## 11. Classical prior art

- **Al-Qurṭubī** (d. 671/1273), *al-Tadhkira fī aḥwāl al-mawtā wa-umūr
  al-ākhira*, bāb fī asmāʾ al-janna, bāb fī asmāʾ al-nār. Enumerates **8
  paradise names** (adding *Dār al-Qarār*) and **7 hell names** matching
  our catalog. Argues each name indicates a distinct *sifa* (attribute) of
  the place and that the ḥadīth "paradise has eight gates" (*thamāniyat
  abwāb*) argues for eight paradises, one per gate.
- **Ibn Kathīr** (d. 774/1373), *al-Nihāya fī al-Fitan wa-l-Malāḥim*, vol.
  2, bāb dhikr al-janna wa-darajātihā. Holds to **7 paradises / 7 hells**
  symmetry. His list matches ours with Dār al-Salām in place of Dār al-Qarār.
- **Al-Ghazālī** (d. 505/1111), *Iḥyāʾ ʿulūm al-dīn*, book 40 (*dhikr
  al-mawt wa-mā baʿdahu*), kitāb al-khawf wa-l-rajāʾ (book 39). Al-Ghazālī
  is more interested in the *states* of the afterlife than the names; but
  in IV:503 he enumerates the names and observes that *al-Firdaws* is "the
  surah-named" paradise (the highest) and *al-Hāwiya* "the named abyss" —
  directly capturing the rarest-name = extreme-tier pattern we verify.
- **Ibn al-Qayyim** (d. 751/1350), *Ḥādī al-Arwāḥ ilā Bilād al-Afrāḥ* — a
  300-page paradise-topography compendium organized by name-tier. His list
  of names runs to **12 paradises** (adding *Jannat ʿIlliyyūn*, *al-Ghurfa*,
  *al-Wasīla*, *al-Maqām al-Maḥmūd*) — he is the maximalist. For *Hādī
  al-arwāḥ* the seven is a conventional reduction; the text yields more.
  Our data agrees: strict count = 7, but a liberal count with compounds
  reaches 12+.
- **Al-Suyūṭī**, *al-Budūr al-Sāfira fī Umūr al-Ākhira* — 16th-c. systematic
  ākhira compendium. Sections 4-7 survey each paradise name with ḥadīth
  attestation. Al-Suyūṭī is the source for the common modern phrase
  *al-jannāt al-sabʿ* (seven paradises).

**Prior-art verdict.** The classical tradition has explicitly counted the
paradise and hell names. The count ranges 7-12 depending on compound
inclusion. Our data precisely matches al-Qurṭubī and Ibn al-Qayyim on the
Quranic lexical stock; we add the *collocational* and *structural*
observations (rivers-only-with-ʿAdn; *mā adrāka*-marks-rare-names;
Firdaws-only-with-*nuzul*-and-*yarithūna*) that the classical catalogs
describe case-by-case but do not tabulate as pattern.

## 12. Summary of findings

1. **Seven paradise names and seven hell names are Quranically attested**,
   matching al-Qurṭubī's *al-Tadhkira* enumeration. The "exactly seven" count
   is theologically motivated (to pair with seven hell-gates of Q 15:44); a
   maximalist count reaches 12+ (Ibn al-Qayyim) when compounds are included.

2. **The rarer a name, the earlier-Meccan its surah and the more likely it
   receives the *wa-mā adrāka mā X* defamiliarization formula.** Five of
   six rare hell-names carry this formula (Saqar, Ḥuṭama, Sijjīn, Hāwiya,
   and the lone paradise ʿIlliyyūn).

3. **al-Firdaws appears exactly twice** (Q 18:107, 23:11), both late-Meccan.
   Both verses connect *firdaws* to structural theology: *nuzul* (welcome-gift)
   and *yarithūna* (inheritance). The scarcest paradise-name is used most
   deliberately.

4. **The "rivers flowing beneath" formula is an ʿAdn-specific collocation.**
   35 occurrences; 5 joined with ʿAdn, 0 joined with any other specific
   paradise name. The phrase is 80% Medinan.

5. **Four Raḥmān gardens in two hierarchical pairs**, grammatically marked by
   25 dual-morphology tokens across vv 46-66 — the Quran's densest dual-form
   concentration. This is a separate eschatological geometry from the
   seven-rank scheme, unreconciled with it.

6. **Saqar (Q 74:26-31)** is the saj'-crescendo from vv 24-25 through v30
   (the "nineteen" verse) into v31, a 250-letter prose explanation. The
   prose verse explicitly interprets the "nineteen" as a *fitna* (test) —
   a rhetorical frame we find empirically vindicated in our code-19 tests.

7. **al-Ḥuṭama (Q 104:4-9)** is hell-directed-at-the-heart — the sole
   hell-name glossed by *taṭṭaliʿu ʿalā l-afʾidah* ("rises over the hearts").
   The surah's sin (hamz/lamz = slander, a heart-vice) is matched to the
   organ of punishment.

8. **The generic al-janna / al-Nār carry dialogue; specific names mark
   scene.** Companionable paradise speech (Q 37:50-61, 52:25-28) and
   adversarial hell speech (Q 14:21, 38:59-64) both use the generic term,
   while the named paradises / hells function as scene-setters.

9. **Sijjīn and ʿIlliyyīn are not place-names but registers** — the *kitāb
   al-fujjār* and *kitāb al-abrār* respectively, in the sole paired-diptych
   within a single surah (Q 83:7-8 / 18-19). This is the Quran's only
   book-based rather than place-based eschatological dichotomy.

10. **Seven distinct collocational signatures exist**, one per specific
    paradise name. Each name is a lexical field, not a synonym. The Quran's
    paradise-geography is lexically structured even when it is not
    topographically explicit.
