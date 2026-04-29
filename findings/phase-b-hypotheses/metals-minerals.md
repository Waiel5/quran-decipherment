---
title: "Metals and Minerals in the Quran — Per-Metal Inventory and Theological Reading"
agent: metals-hypothesis-runner
run: 2
date: 2026-04-12
phase: B
inputs:
  - quran-text/quran-no-tashkeel.json (full corpus scan)
  - findings/phase-c-structures/hadid-deep-dive.md (Al-Ḥadīd context)
  - findings/phase-b-hypotheses/paradise-hell-names.md
  - findings/phase-b-hypotheses/parables-catalog.md
methods:
  - exhaustive substring search on Arabic stems for each metal noun
  - disambiguation of ذهب (verb "went" vs noun "gold") via article/accusative/preposition filters
  - cross-reference of each occurrence against classical tafsīr (Ṭabarī, Rāzī, Qurṭubī, Zamakhsharī) via project's tafsir-xref corpus
verdict: >
  The Quran names seven distinct metallic / mineral substances:
  iron (ḥadīd, 6 occurrences across 6 surahs), gold (dhahab as noun,
  8 occurrences), silver (fiḍḍa, 6 occurrences), brass/copper
  (nuḥās, 1 occurrence at Q 55:35), molten copper (qiṭr, 2
  occurrences — Solomon and Dhū al-Qarnayn), pitch/tar (qaṭirān, 1
  occurrence at Q 14:50, often confused with qiṭr), and baked
  clay-stones (sijjīl, 3 occurrences — Lot cities ×2, Elephant
  Army ×1). Lead (ānuk / raṣāṣ) does NOT appear in the Quran,
  though some classical commentators read the "compacted building"
  (bunyān marṣūṣ, Q 61:4) as "lead-fastened" — a lexical not
  material reference. The metal discourse organises along three
  theological axes: (1) iron as tool-and-weapon under divine gift
  (David, Dhū al-Qarnayn, Q 57:25); (2) gold-silver as object of
  dunyā-hoarding (Q 3:14, 9:34) versus ākhira-adornment (Q 18:31,
  22:23, 35:33, 43:71, 76:15-21); (3) molten metal / fire-stone
  as eschatological or miraculous intervention (Q 34:12, 18:96,
  55:35, 105:4, 11:82, 15:74). The two "metal-miracle events"
  (Solomon's copper-spring, Dhū al-Qarnayn's iron+copper wall) are
  the only Quranic narratives where a named metal is the central
  material of the prophetic act.
---

# Metals and Minerals in the Quran

## 0. Scope and Method

The Quran is a theological-legal text, not a metallurgical one.
Metals appear in it exactly where they do theological work: as
divine gift to prophets, as marker of worldly excess, as instrument
of eschatological punishment, as ornament of paradise, and as
material of the two "technical miracles" attributed to Solomon and
Dhū al-Qarnayn. This run enumerates every metal or metalliform
mineral named in the ʿUthmānic text, tallies each occurrence, and
reads each cluster against both classical tafsīr and the project's
prior structural findings (hadid-deep-dive, parables-catalog,
paradise-hell-names).

A note on disambiguation. The Arabic root **dh-h-b** is the
single most ambiguous metal-stem in the Quran: as a verb it means
"to go, to depart, to take away" and occurs dozens of times
(e.g. Q 2:17 *dhahaba Allāhu bi-nūrihim*, "Allah took away their
light"); as a noun it means gold. The verb/noun ratio is roughly
46/8. We isolate the noun by requiring the definite article
(الذهب), tanwīn-accusative with context (ذهبًا "as gold"), or a
construct with preposition ("min dhahab", "of gold"). Under that
filter the noun-only count is 8 across 7 surahs.

## 1. Per-Metal Inventory

### 1.1 Iron — ḥadīd (حديد) — 6 occurrences

| Location | Fragment | Function |
|---|---|---|
| 17:50 | *ḥijāratan aw ḥadīdā* | hypothetical (even if you were iron, resurrection still occurs) |
| 18:96 | *zubara l-ḥadīd* | Dhū al-Qarnayn's dam blocks |
| 22:21 | *maqāmiʿu min ḥadīd* | iron maces/hooks of Hell |
| 34:10 | *wa-alannā lahu l-ḥadīd* | iron "softened" for David |
| 50:22 | *fa-baṣaruka l-yawma ḥadīd* | **"sharp"** — Day-of-Judgment vision |
| 57:25 | *wa-anzalnā l-ḥadīd* | iron "sent down" with might and benefit |

Notice the polysemy: 5 of 6 uses are literal iron; Q 50:22 is the
one metaphorical "sharp / piercing" use (native Semitic transfer
hard → sharp → piercing). Of the 5 literal uses, 3 are
instrumental (dam, Hell-hook, David's armour), 1 hypothetical,
1 programmatic-theological ("sent down" as divine gift). The
Quran's iron register is **never metallurgical-descriptive** — no
text describes smelting, mining, alloying, tempering. Iron appears
*already-as-tool* in every literal occurrence.

Distribution is striking: iron is named in exactly 6 surahs (17,
18, 22, 34, 50, 57), with the David-iron and the Dhū-al-Qarnayn-
iron sitting in adjacent narrative register (prophetic mastery of
the metal under divine subvention). The iron-softening of Q 34:10
(*alannā lahu*) and the copper-liquefying of Q 34:12 (*asalnā lahu
ʿayn al-qiṭr*) are lexically parallel: both use the hollow-root
ل-ي-ن / س-ي-ل to predicate "flow / softness" on solid metal as a
divine act for Daūd and Sulaymān respectively.

### 1.2 Gold — dhahab (ذهب, noun) — 8 occurrences

| Location | Fragment | Register |
|---|---|---|
| 3:14 | *al-qanāṭīr al-muqanṭara min al-dhahab wa-al-fiḍḍa* | dunyā-lust list |
| 3:91 | *mil'a l-arḍi dhahaban* | earth-full of gold as ransom (rejected) |
| 9:34 | *yaknizūna l-dhahaba wa-al-fiḍḍa* | rabbinic/monastic hoarding |
| 18:31 | *asāwira min dhahab* | paradise bracelets |
| 22:23 | *asāwira min dhahab wa-luʾluʾa* | paradise bracelets + pearls |
| 35:33 | *asāwira min dhahab wa-luʾluʾa* | paradise bracelets + pearls |
| 43:53 | *asāwira min dhahab* | Pharaoh's taunt re: Moses |
| 43:71 | *bi-ṣiḥāfin min dhahab* | paradise dishes/cups |

The 8 occurrences split cleanly 3-5: three *dunyā* condemnations
(3:14 in a list of worldly lusts, 3:91 as rejected ransom, 9:34 as
hoarded capital) and five *ākhira* promises or adornment images
(4× paradise bracelets/dishes, plus 43:53 where Pharaoh ironically
demands that God should have given Moses gold-bracelets if he were
truly a prophet). The gold polarity is dunyā-blamed /
ākhira-rewarded.

### 1.3 Silver — fiḍḍa (فضة) — 6 occurrences (verbal-noun root)

| Location | Fragment | Register |
|---|---|---|
| 3:14 | *wa-al-fiḍḍa* | dunyā-lust list (paired with gold) |
| 9:34 | *wa-al-fiḍḍa* | hoarding (paired with gold) |
| 43:33 | *suqufan min fiḍḍa* | silver **roofs** (disbelievers' houses, hypothetical) |
| 76:15 | *āniya min fiḍḍa* | silver **vessels** (paradise) |
| 76:16 | *qawārīra min fiḍḍa* | silver-crystal vessels (paradise) |
| 76:21 | *asāwira min fiḍḍa* | silver **bracelets** (paradise) |

Only 6 occurrences; 2 are the dunyā-gold-silver pair, 4 are
paradise/wealth images. The Q 76:15-16 passage is where the famous
"silver that looks like crystal" image sits — not Q 56 as sometimes
cited (see §3 below).

### 1.4 Brass / Copper — nuḥās (نحاس) — 1 occurrence

| Location | Fragment | Register |
|---|---|---|
| 55:35 | *shuwāẓun min nārin wa-nuḥās* | eschatological punishment — flame and brass |

A true hapax in the metal register. Al-Rāzī and al-Qurṭubī gloss
*nuḥās* here as either "molten copper/brass" (the common reading),
"smoke" (a minority reading based on a variant ḥadīth lexicon),
or "fire without smoke" (a reading tied to the pairing with
*shuwāẓ*, the pure flame-without-smoke). The most common classical
gloss is molten brass. See §5.

### 1.5 Molten Copper — qiṭr (قطر) — 2 occurrences

| Location | Fragment | Function |
|---|---|---|
| 18:96 | *āfrigh ʿalayhi qiṭran* | "pour over it molten metal" (Dhū al-Qarnayn's wall) |
| 34:12 | *asalnā lahu ʿayna l-qiṭr* | "we made flow for him a spring of qiṭr" (Solomon) |

*Qiṭr* (a form from qaṭara "to drip") means molten/dripping copper
or brass in classical lexicons (Lisān al-ʿArab, Tāj al-ʿArūs). The
two occurrences pair Dhū al-Qarnayn with Solomon as the two
prophetic / quasi-prophetic figures who command the substance.
This is the tightest lexical bridge in the Quran's metal-miracle
discourse — see §4.

**Note on qaṭirān (Q 14:50):** *sarābīluhum min qaṭirān* — "their
garments of pitch/tar" — is NOT qiṭr despite the shared consonants.
Qaṭirān is a tree-resin / pine-tar used medicinally and as fuel;
qiṭr is molten copper. Classical lexicographers distinguish them
carefully, though some modern polemicists conflate them to inflate
the metal-count.

### 1.6 Lead — ānuk / raṣāṣ — 0 occurrences

The user's brief lists *ānuk* (آنك, lead) as a Quranic metal. It
is not. Direct substring search for آنك and رصاص returns no hits.
The classical Arabic word for lead, *al-ānuk*, appears in pre-
Islamic poetry (e.g. al-ʿAshā) and in ḥadīth ("ka-l-ānuki
yudhāb fī udhunihi", "like lead molten into his ear"), but not in
the Quran. A related root r-ṣ-ṣ yields Q 61:4 *bunyānun marṣūṣ*
("compacted building") which some classical commentators gloss
as "lead-fastened" based on the secondary lexical sense of *raṣṣa*
(to fasten with lead, as cracked walls were historically repaired);
this is a lexical resonance, not a direct lead-reference. The
Quran therefore names six metals and one mineral, not seven metals.

### 1.7 Baked Clay-Stones — sijjīl (سجيل) — 3 occurrences

| Location | Fragment | Function |
|---|---|---|
| 11:82 | *ḥijāratan min sijjīlin manḍūd* | Lot's cities — stones rain |
| 15:74 | *ḥijāratan min sijjīl* | Lot's cities (parallel) |
| 105:4 | *bi-ḥijāratin min sijjīl* | Abraha's Elephant Army |

Sijjīl is technically not a metal but a mineral aggregate — it is
glossed by al-Ṭabarī and al-Zamakhsharī as an Arabicised Persian
compound *sang-gil* ("stone-clay"), meaning hard-baked clay
stones. Ibn ʿAbbās glosses it as "fire-baked stone" (*ḥijāra
mashwiyya*). We include it here because it patterns with nuḥās
and qiṭr as a fire-transformed mineral weapon. See §6.

## 2. Al-Ḥadīd Chapter Integration — The Honest Iron-Miracle Verdict

The hadid-deep-dive adjudication is final and we adopt it here:
Surah 57 is a **genuine structural hotspot** (the only 4-name
quartet verse at Q 57:3, the 2nd Musabbiḥ opener, the densest
Bonferroni-significant muqābala), but the **Fe-57 / Fe-26
abjad miracle is a survivor-bias artefact** on a 114-cell search
with massive forking-paths freedom (114 surahs × 2 tables × 2
spellings × dozens of plausible physical quantities × ±1 tolerance).

What is honestly compelling about metals in Al-Ḥadīd:

1. **The *anzalnā* doubling at v 25.** Iron is syntactically
   placed inside the same "sent down" frame as the Book and the
   Balance. This is deliberate rhetorical coupling: iron is
   revelatory-register-provision, not metallurgical description.
   The verse's theological pivot is not "where did iron come from"
   but "what does iron stand for in the covenant": technology of
   power (*ba's shadīd*) and technology of benefit (*manāfiʿ
   li-l-nās*), both accountable under divine scrutiny.

2. **The intra-surah theology of resource.** Surah 57 repeatedly
   names wealth and hoarding (vv 7 *anfiqū*, 10 *lā yastawī…
   min qabli l-fatḥi*, 11 *yuqriḍu Allāha qarḍan ḥasanan*, 20
   *innamā l-ḥayātu l-dunyā laʿibun wa-lahwun*). Iron at v 25 is
   the climactic material-object of a surah about what material
   objects are FOR. The surah is a meditation on the ethics of
   material power, and iron is its type-case.

3. **What is NOT compelling.** The surah-number-57-equals-iron
   abjad is real arithmetic but a 1.4σ event under a plain null
   (see hadid-deep-dive §1.2); the Fe-57-isotope match is worse
   than the Fe-56 match the numerologists cannot produce; the
   "iron from supernova" reading is a modern back-resonance since
   pre-Islamic cultures (Sumer, Egypt) already believed iron was
   heavenly (meteoritic iron = *an-bar*, "metal-of-heaven"). The
   theological "sent down" language is native and does not require
   modern astrophysics. The honest verdict: structural richness of
   Surah 57 is real; the iron-miracle cluster is post-hoc.

## 3. Gold / Silver — Q 9:34 Hoarding vs Paradise-Cups

### 3.1 The Hoarding Pole

Q 9:34 is the Quran's most explicit anti-accumulation text on
precious metals:

> "…and those who hoard gold and silver and do not spend them in
> the way of Allah — give them tidings of a painful punishment."

Q 9:35 then expands the punishment image: on the Day of
Judgement, the hoarded metals will be heated in the Fire of Hell
and "their foreheads, flanks, and backs will be branded with
them." The hoarded metal literally becomes the torture-instrument
— a talionic transformation of dunyā-capital into ākhira-brand.
This is the Quran's single sharpest metal-punishment image, and
it inverts the ornament polarity: the gold that was a bracelet in
paradise becomes the iron-in-the-fire on the wrong side.

Q 3:14 is the taxonomic counterpart: gold-and-silver appears in a
7-term catalogue of *shahawāt* (lusts) — women, children, heaped
gold-and-silver, branded horses, cattle, tilth — each of which is
explicitly labelled *matāʿu l-ḥayāti l-dunyā* ("chattel of this
life"). Q 3:91 adds the ransom image: an earth-full of gold
(*mil'a l-arḍi dhahaban*) offered as *fidya* by the dead
disbeliever will not be accepted. Three scaling images:
accumulation (9:34), enumeration (3:14), absolute quantity (3:91).

### 3.2 The Paradise-Adornment Pole

The other five gold-noun occurrences are paradise-images:

- Bracelets of gold (asāwira min dhahab) — Q 18:31, 22:23, 35:33
- Gold-and-pearl bracelets — Q 22:23, 35:33
- Gold dishes (ṣiḥāf min dhahab) — Q 43:71

Silver adds:
- Silver vessels / crystal-silver vessels — Q 76:15-16
- Silver bracelets — Q 76:21
- Silver roofs (hypothetical, if disbelievers would not all become
  disbelievers the world over) — Q 43:33

### 3.3 Correction on Q 56:15-16

The brief cites Q 56:15-16 as "paradise cups." This is a
reference-error. Q 56:15-16 is *ʿalā sururin mawḍūna / muttakiʾīna
ʿalayhā mutaqābilīn* — "on decorated couches, reclining on them
facing one another." Cups in Q 56 appear at v 18 (*bi-akwābin
wa-abārīqa wa-kaʾsin min maʿīn*) but without a metal-attribute.
The **silver** paradise-cups the tradition remembers are in
**Q 76:15-16** (Sūrat al-Insān): *āniyatin min fiḍḍa / qawārīra
min fiḍḍa qaddarūhā taqdīrā* — "vessels of silver / silver-crystal
vessels, measured to precise measure." This is the Quran's
signature metal-glass oxymoron: silver that refracts like glass
(al-Zamakhsharī reads *qawārīr min fiḍḍa* as silver with the
transparency of glass — a paradisal metal-glass fusion). The
user-brief's verse-reference is likely a transposition; the
material content of the claim (silver cups in paradise) is
entirely correct, and sits at Q 76 rather than Q 56.

### 3.4 The Symmetry

The Quran's gold-silver discourse is a **double binary**:

| Axis | Dunyā pole | Ākhira pole |
|---|---|---|
| Gold | hoarded (9:34), lusted (3:14), ransom-rejected (3:91) | bracelets (18:31, 22:23, 35:33), dishes (43:71) |
| Silver | hoarded (9:34), lusted (3:14), would-be-roofs (43:33) | vessels (76:15-16), bracelets (76:21) |

Same metals; same categories; polarity inverts with location.
The pedagogical point is Q 3:14's closing phrase: *dhālika matāʿu
l-ḥayāti l-dunyā, wa-Allāhu ʿindahu ḥusnu l-maʾāb* — "that is the
chattel of this life, but with Allah is the best return." The
metals don't change; the economy does.

## 4. The Two Metal-Miracle Events

The Quran names exactly two events in which a prophet / quasi-
prophet commands a molten metal as the central material of the
act: Solomon's copper-spring (Q 34:12) and Dhū al-Qarnayn's
iron-and-copper wall (Q 18:96). They are lexically linked by the
shared noun *qiṭr* — its only two Quranic occurrences.

### 4.1 Solomon — Q 34:10-13

> "And to Solomon [We subjected] the wind — its morning [course]
> a month and its afternoon a month, and **We made flow for him a
> spring of qiṭr** (ʿayn al-qiṭr)…" (34:12)

The verb *asalnā* ("we caused to flow") is the liquefaction verb
parallel to *alannā* ("we softened") applied to David's iron in
the immediately-preceding verse 34:10. The surah-local architecture
is: David gets solid-iron-made-soft, Solomon gets liquid-copper-
made-flow. Two metals; two verbs of phase-change; two father-son
prophets; one narrative frame. This is the tightest metal-pairing
in the Quran.

The "spring of qiṭr" is classically read as either (a) a literal
subterranean copper-spring that erupted from the earth in Yemen
for Solomon's jinn-assisted building work (Ṭabarī's preferred
reading, attributed to Ibn ʿAbbās and Qatāda), or (b) a
metaphorical gift of unlimited molten metal for construction
(Rāzī's alternative). The immediate next verse (34:13) names the
products: *maḥārīb wa-tamāthīl wa-jifānin ka-l-jawābi wa-qudūrin
rāsiyāt* — "sanctuaries and statues and bowls like reservoirs
and great cauldrons fixed in place." The metal is construction-
grade and civic-scale.

### 4.2 Dhū al-Qarnayn — Q 18:95-98

> "…Bring me **blocks of iron** (zubara l-ḥadīd)." Then when he
> had filled the gap between the two cliffs, he said, "Blow."
> Until when he had made it [as hot as] fire, he said, "Bring me,
> that I may pour over it molten metal (qiṭran)." (18:96)

This is the Quran's most technical description of any industrial
process. Five steps are named: (1) collection of iron blocks,
(2) filling of the gap between mountains/cliffs, (3) forced-air
bellows ("blow"), (4) heating until the mass is "as fire" (white-
hot), (5) pouring molten copper over the heated iron. The result
is a bi-metal barrier — iron backbone, copper seal. This is not
arbitrary: copper bonds to red-hot iron, seals porosity, and
protects against oxidation. The Quranic description is
metallurgically plausible as a cladding or casting process of the
late-antique Iranian-Central-Asian tradition.

### 4.3 The Pairing

The two events share:
1. The noun *qiṭr* (its only two Quranic occurrences).
2. The theme of divinely-subvented metallurgy.
3. The eschatological ambivalence — Solomon's wind-and-copper
   kingdom is the paradigm of *mulk* blessed; Dhū al-Qarnayn's
   wall is a defensive barrier against Gog and Magog whose
   collapse is a **sign of the Hour** (Q 18:98 *fa-idhā jā'a waʿdu
   rabbī jaʿalahu dakkāʾ*). Solomon's metal serves civilisation;
   Dhū al-Qarnayn's metal holds eschatology at bay.

Both narratives resist the "scientific miracle" reading precisely
because their metallurgy is *ancient-plausible*, not *modern-
predictive*. The text is describing craft, not chemistry.

## 5. Al-Nuḥās al-Mudhāb — Q 55:35 Eschatology

Q 55:35 is the only Quranic occurrence of *nuḥās*:

> "There will be sent upon you a flame of fire and brass (*shuwāẓun
> min nārin wa-nuḥās*), and you will not defend yourselves."

The verse sits inside Sūrat al-Raḥmān's sustained two-audience
address (*yā maʿshara l-jinn wa-l-ins*) between the paired
refrains *fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān*. The immediate
context is the confrontation of the two weighty species (jinn and
humankind) with a fire-and-brass deterrent against escape-attempts
from God's jurisdiction. The image is:

- *shuwāẓ*: pure flame without smoke (lexicographers: the sharp,
  smokeless inner-cone of a fire)
- *nuḥās*: molten brass / or, in the minority reading, dense smoke

Al-Rāzī notes the tension: the two items are paired but their
classical glosses are near-opposites (pure flame / thick smoke).
He resolves by arguing the pair exhausts the visual spectrum of
fire (its bright core and its dark exhaust). Al-Qurṭubī prefers
the "molten copper" reading, linking this verse to Q 18:96's
*qiṭr* as the same eschatological substance — molten metal
overflowing prophetic craft-language into divine-judgement-
language.

The integration with the rest of the metal-corpus is tight:

- *qiṭr* (18:96, 34:12) = molten metal as *craft*
- *nuḥās* (55:35) = molten metal as *weapon*
- *al-ḥadīd* in *maqāmiʿ* (22:21) = iron hooks as *torture-
  implement* in Hell
- *dhahab wa-fiḍḍa* heated in Hellfire (9:35) = hoarded precious
  metals as *branding-irons*

The unifying image is **metal in phase-change under divine
command**. Softened, melted, poured, heated, branded. The Quran's
metals are never static; they are always about to change state.
This, rather than atomic numbers, is the Quran's metallurgical
theology.

## 6. Sijjīl — Q 105 and the Mineral-Stone Weapon

The three sijjīl verses (11:82, 15:74, 105:4) form a small
intra-Quranic triad. All three describe *stones* (*ḥijāra*, not
metal) rained from above as divine judgement. Two target Lot's
cities; one targets Abraha's Elephant Army at Mecca. The word
*sijjīl* is classically read as Persian-origin *sang-gil*
("stone-clay") or as Arabic *sijjīl*/*sijjīn* (related to the
"register" of the damned at Q 83:7 — a minority reading tying
the stones to *kitābu l-fujjār*, "the register of the wicked,"
each stone inscribed with a name).

Q 105 (Sūrat al-Fīl) is the Quran's shortest narrative of
historical deliverance. Five verses; no named actors beyond
"the companions of the elephant"; the birds (*ṭayr abābīl*) are
the agent; the sijjīl-stones are the weapon; the verdict is the
reduction of the army to *ʿaṣfin maʾkūl* ("chewed husk"). The
material chain is:

- birds (airborne agent)
- sijjīl-stones (baked-clay projectile)
- target (organic matter reduced to vegetable-husk)

Classical hagiography (Ibn Isḥāq's *Sīra* via Ibn Hishām) dates
the event to 570 CE, the "Year of the Elephant" — the traditional
year of Muḥammad's birth. The sijjīl is thus not only a mineral
weapon but a providential prelude to the Prophet's life — the
surah's function in the canonical arrangement (next to Sūrat
Quraysh) is to frame the Prophet's city as already divinely
defended before he was born. The metal/mineral weapon is not
merely punitive; it is *preparatory*.

Under a "scientific miracle" reading, sijjīl has been variously
proposed as volcanic pumice, meteoritic iron, or bio-pathogen-
carrying aerosol (Muhammad Asad speculated a plague-carrying swarm
at Q 105:3; Tantawi Jawhari preferred volcanic ash). The honest
reading is that *sijjīl* is a named Persian-Arabic compound for
hardened clay-stone in pre-Islamic lexicons, used straightforwardly
in the text, and the birds-and-stones narrative belongs to the
Quran's genre of *ayyām Allāh* (historical judgement) rather than
to any predictive physical claim.

## 7. Integration — The Quranic Metallurgical Theology

Eight metals/minerals; three theological registers:

1. **Metal as prophetic gift.** Iron softened for David (34:10);
   copper-spring for Solomon (34:12); iron blocks for Dhū al-
   Qarnayn (18:96). The gift is never raw resource but
   **phase-changed material under divine verbs** (*alannā*,
   *asalnā*, *afrigh*).

2. **Metal as ethical test.** Gold and silver hoarded (9:34) vs
   gold and silver as paradise ornament (18:31, 76:15-21). The
   substance is ethically neutral; the relation to it is the
   judgement.

3. **Metal/mineral as eschatological weapon.** Iron hooks of Hell
   (22:21); molten brass rain (55:35); branded hoarded-metals
   (9:35); sijjīl stones (11:82, 15:74, 105:4); barrier of Dhū
   al-Qarnayn collapsing at the Hour (18:98).

There is no "science miracle" here in the modern apologetic
sense. There is, instead, a **theology of material** in which
every named metal shows up as convertible — liquefiable,
hardenable, pourable, brandable, rainable. The Quran's metals
are never described metallurgically in stable state; they are
always in transition under divine agency. That is the signal the
corpus gives up willingly, and it is theologically richer than
any atomic-number coincidence could be.
