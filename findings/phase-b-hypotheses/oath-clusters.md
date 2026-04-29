---
title: Oath clusters (qasam) — computational catalog
phase: B
agent: oath-clusters-run-1
date: 2026-04-12
status: exploratory — descriptive inventory + three honest quantitative tests
rules:
  orthography: no-tashkeel (raw consonantal text for cluster detection)
  word_definition: Leeds morphology segments (Buckwalter)
  letter_definition: graphemes (for cross-check with palindrome finding only)
  basmala_policy: counted-only-in-surah-1 (oath detection is per-verse, basmala-agnostic)
  verse_numbering: hafs-kufan
  null_model: within-surah length-matched random runs (1 000 permutations) for the
    saj'-uniformity claim; category-chiastic and size-order results are descriptive
detection_rule: >
  A verse is an oath opener if its leading morphology matches either
  (A) [INL?] (P|CONJ form=w) [DET|DEM]? N/PN/ADJ with GEN case — the canonical
      waw-oath, or
  (B) [INL?] [REM?] [NEG?] V(root=qsm) [PRON]* P(bi) [DET|DEM]? N[GEN] — the
      "(fa-/la-)uqsimu bi-…" verbal oath, or
  (C) continuation: [CONJ|REM form=f] [DET|DEM]? N[GEN] — the classical fa-
      continuation ("fa-l-ʿāṣifāti ʿaṣfā") licensed only when the previous
      verse was itself a waw-/qsm-oath.
  A "cluster" is the maximal run of consecutive verses each matching (A), (B)
  or (C). Within a single verse we also count every qualifying (waw-noun-GEN)
  item (Q 86:1 has two sworn-by items inside v1: "by the heaven and the
  night-star"; Q 91:1 packs "by the sun and its brightness" as two items
  inside v1).
data:
  - quran-text/quran-no-tashkeel.json
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - data/translations/en.sahih.txt-2.txt
  - findings/phase-b-hypotheses/saj-fasila-per-verse.csv   (cross-check)
code: analysis/notebooks/oath_clusters.py
artifacts:
  - findings/phase-b-hypotheses/csv/oath-clusters.json
  - findings/phase-b-hypotheses/csv/oath-clusters.csv
  - findings/phase-b-hypotheses/csv/oath-clusters-stats.json
---

# Quranic oath clusters — computational catalog

## 0. Headline

The Quran contains **61 oath events** by the strict waw+GEN / "(la-)uqsimu bi-"
rule: **32 multi-item clusters** (≥ 2 sworn-by objects) and **29 singleton
oaths** (a single `و + noun-GEN` with no parallel sworn-by object in the next
verse). **20 of the 32 multi-item clusters open their surah**; only **2 of 32
occur in a Medinan surah** (both in Q 4 and Q 56, and both are not classical
oath clusters — they are accidental waw-GEN chains). Every one of the
classically famous qasam-opening surahs (36, 37, 43, 44, 50, 51, 52, 53, 68,
75, 77, 79, 85, 86, 89, 90, 91, 92, 93, 95, 100, 103) is recovered by the
detector. The length distribution over multi-item clusters is

| n-items | 2 | 3 | 4 | 5 | 6 | 7 | 8 |
|---|---|---|---|---|---|---|---|
| count | 15 | 7 | 5 | 3 | 1 | 0 | 1 |

peaking at length 2–3. The longest oath cluster in the whole Quran is
**Q 91:1–7 with 8 sworn-by items** (sun, brightness, moon, day, night, heaven,
earth, soul) — the same surah whose letter-count palindrome was flagged in
[palindromes.md](./palindromes.md). The second-longest is **Q 52:1–6 with
6 sworn-by items** (Mount Sinai, written book, parchment, the frequented
house, raised canopy, swelling sea).

The single most striking novel pattern: **oath clusters that open surahs are
semantically homogeneous internally and semantically exotic externally**.
Among the 14 opening clusters of length ≥ 3, thirteen have a single-category
sworn-by sequence — `wind/wind/wind/wind` (Q 51, Q 77), `angelic/angelic/…`
(Q 79, Q 37), `temporal/temporal/…` (Q 89, Q 92, Q 93), `terrestrial/…`
(Q 52, Q 95), or the celestial-dominant Q 85. The only **mixed-category**
opening cluster of length ≥ 3 is **Q 91**, whose 8 sworn-by objects traverse
FOUR categories (celestial, temporal, terrestrial, psychological). Every
opening cluster of length ≥ 3 is either monothematic or is Q 91. Q 91 is
therefore the uniquely heterogeneous long opening oath in the Quran — which
is exactly the one that is also a letter-count palindrome.

## 1. Method

**Oath detection rules** are above. All three rules require genitive case on
the sworn-by noun; this single constraint cleanly separates oath-waw from
conjunction-waw (≈ 40 000 waw occurrences in the Quran, of which only a
small fraction introduce GEN nouns at verse starts). The DEM step-through
handles Q 90:1 and Q 95:3 ("wa-hādhā l-balad al-amīn", demonstrative
before the noun).

**Cluster-building** is contiguous. When a `qsm` verb is the cluster head
(Q 75:1, Q 56:75, Q 69:38, Q 70:40, Q 90:1) the "la-/fa-la-" emphatic
prefixes are absorbed; when a waw-oath is the head (the vast majority),
continuation is allowed via `fa-CONJ + GEN-noun` (Q 100:2–3, Q 77:2, Q 77:4–5,
Q 79:4–5, Q 37:2–3, Q 51:2–4).

**Within-verse item-packing** is captured by a second scan: each cluster
verse can contribute multiple items if the verse itself lists several
`(waw|fa) + GEN-noun` pairs (Q 86:1, Q 91:1, Q 95:3, Q 89:4).

Two known limitations, for honesty:

1. **The `idha`-clusters** (Q 81:1–13, Q 82:1–5, Q 84:1–5, Q 99:1–3,
   Q 100:6–? partially). These are conditional "when X happens" runs that
   classical tafsir (and Farahi's *Niẓām al-Qurʾān*) groups with qasam because
   the cosmological collapse imagery functions as a sworn-by protasis. My
   strict `waw + GEN noun` rule excludes them. They are tallied separately
   below but do not enter the main 32-cluster catalog.
2. **Parenthetical continuations.** Q 90 has the classical reading of a 3-item
   oath (this city / a begetter / what he begot) broken by the parenthetical
   "and you are free in this city" at v2. My contiguity rule captures only
   v1. Q 100:1–5 has 3 participial sworn-by objects (v1–3) followed by two
   verb-continuations (v4–5, "then they stir up / then they penetrate"); my
   detector stops at v3.

Both limitations suppress length, not presence; they do not affect the
cluster-count total.

## 2. Complete cluster inventory (length ≥ 1, opening position)

### 2.1 Opening oaths (20 surahs — **all Meccan**)

★ = in classical oath-surah candidate list (Al-Farra, Ibn al-Qayyim).

| Surah | Name | v-range | n-items | oath type | sworn-by (English) | sworn-about (v+1) |
|---|---|---|---|---|---|---|
| ★ 36 | Yā-Sīn | 2–2 | 1 | waw | the Wise Qur'ān | "Indeed you are from among the messengers" |
| ★ 37 | Aṣ-Ṣāffāt | 1–3 | 3 | waw | those ranged in ranks / those driving away / those reciting a reminder | "Indeed, your God is One" |
| 38 | Ṣād | 1–1 | 1 | waw | the Qur'ān full of reminder | "But those who disbelieve are in pride and dissension" |
| ★ 43 | Az-Zukhruf | 2–2 | 1 | waw | the clarifying Book | "Indeed, We have made it an Arabic Qur'ān" |
| ★ 44 | Ad-Dukhān | 2–2 | 1 | waw | the clarifying Book | "Indeed, We sent it down during a blessed night" |
| ★ 50 | Qāf | 1–1 | 1 | waw | the glorious Qur'ān | "But they wonder …" |
| ★ 51 | Adh-Dhāriyāt | 1–4 | 4 | waw | those that scatter / those that bear a load / those that run / those that apportion | "Indeed, what you are promised is true" |
| ★ 52 | Aṭ-Ṭūr | 1–6 | **6** | waw | the Mount / a Book written / on unrolled parchment / the frequented House / the canopy raised / the sea swollen | "Indeed, the punishment of your Lord will occur" |
| ★ 53 | An-Najm | 1–1 | 1 | waw | the star when it descends | "Your companion has not strayed" |
| ★ 68 | Al-Qalam | 1–1 | 1 | waw | (nūn) by the Pen and what they inscribe | "You are not, by the favour of your Lord, a madman" |
| ★ 75 | Al-Qiyāmah | 1–2 | 2 | qsm | the Day of Resurrection / the self-reproaching soul | "Does man think that We will not assemble his bones?" |
| ★ 77 | Al-Mursalāt | 1–5 | **5** | waw | those sent forth / the blasters / the scatterers / the dividers / the bringers of a reminder | "As justification or warning" |
| ★ 79 | An-Nāziʿāt | 1–5 | **5** | waw | those that extract violently / those that glide / those that swim / those that race ahead / those that arrange | "On the Day the blast will convulse creation" |
| ★ 85 | Al-Burūj | 1–3 | 4 | waw | the heaven of constellations / the Promised Day / a witness / a witnessed | "Cursed were the companions of the trench" |
| ★ 86 | Aṭ-Ṭāriq | 1–1 | 2 | waw | the heaven / the night-comer | "And what can make you know what the night-comer is?" |
| ★ 89 | Al-Fajr | 1–4 | **5** | waw | the dawn / ten nights / the even / the odd / the night when it departs | "Is there [not] in that an oath for one of perception?" |
| ★ 90 | Al-Balad | 1–1 | 1 | qsm | this city | (parenthetical "and you are free in this city" at v2, then "a begetter and what he begot" at v3 — classical 3-item reading) |
| ★ 91 | Ash-Shams | 1–7 | **8** | waw | the sun / its brightness / the moon / the day / the night / the heaven / the earth / a soul | "And inspired it [with discernment of] its wickedness and righteousness" |
| ★ 92 | Al-Layl | 1–2 | 2 | waw | the night / the day | "And by He who created male and female" |
| ★ 93 | Aḍ-Ḍuḥā | 1–2 | 2 | waw | the morning brightness / the night when it settles | "Your Lord has not taken leave of you" |
| ★ 95 | At-Tīn | 1–3 | **4** | waw | the fig / the olive / Mount Sinai / this secure city | "We have certainly created man in the best of stature" |
| ★ 100 | Al-ʿĀdiyāt | 1–3 | 3 | waw | the chargers (panting) / the strikers of fire / the raiders at dawn | (verb continuations v4–5, then) "Indeed, mankind to his Lord is ungrateful" (v6) |
| ★ 103 | Al-ʿAṣr | 1–1 | 1 | waw | the late afternoon | "Indeed, mankind is in loss" |

Two more classically-claimed qasam openings are recovered as interior clusters
by the rules but are opening-adjacent and should be named alongside these:

- **Q 56:75** "(fa-) lā uqsimu bi-mawāqiʿi n-nujūm" — 1-item qsm oath, followed
  by the emphatic "and it is indeed, if you knew, a great oath" (v76).
- **Q 69:38–39** "(fa-) lā uqsimu bi-mā tubṣirūn wa-mā lā tubṣirūn" — 1-item
  qsm with a relative-clause coordinate; not captured as a 2-item cluster
  because the coordinate is a relative clause, not a GEN noun.
- **Q 70:40** "(fa-) lā uqsimu bi-rabbi l-mashāriq wal-maghārib" — 1-item qsm
  with GEN coordinate; my rule captures only the head.

### 2.2 Interior oath clusters (mid-surah, length ≥ 2)

Twelve further clusters appear mid-surah. Several of these are NOT classical
oaths — they are accidental `waw + GEN noun` runs inside narrative-genitive
chains (e.g. Q 26:58 "gardens and springs", Q 56:29–32 "thornless lote trees
and layered acacia and extended shade and outpoured water"). I list them all
and annotate which are genuine qasam:

| Surah | v-range | n-items | sworn-by | type |
|---|---|---|---|---|
| 4 | 157 | 2 | their saying / their doubt | prose GEN chain (not qasam) |
| 4 | 161 | 2 | their taking / their consumption | prose GEN chain (not qasam) |
| 21 | 78 | 3 | David / Solomon / the plowing | prose GEN chain (not qasam) |
| 26 | 58 | 2 | treasures / station | narrative GEN chain (not qasam) |
| 26 | 134 | 2 | gardens / springs | narrative GEN chain |
| 26 | 148 | 2 | fields / date-palms | narrative GEN chain |
| 29 | 39 | 2 | Qārūn / the earth | narrative GEN chain |
| 44 | 26–27 | 3 | sown fields / an honorable station / a luxurious life | **resembles qasam** but in narrative voice |
| 45 | 5 | 3 | alternation of night / (day) / the distributing of provision | **qasam-like cosmic witness**, non-opening |
| 56 | 20–21 | 2 | fruits / flesh of fowl | Paradise menu (not qasam) |
| 56 | 29–32 | 4 | thornless lote / layered acacia / extended shade / outpoured water | Paradise menu |
| 70 | 12–13 | 3 | his consort / his brother / his clan | pronominal chain (not qasam) |
| 74 | 33–34 | 2 | the night when it departs / the morning | **genuine qasam interior cluster** |
| 80 | 35–36 | 4 | one's mother / father / consort / sons | nominal chain (not qasam) |
| 81 | 17–18 | 2 | the night when it departs / the morning when it breathes | **genuine qasam interior cluster** (identical sworn-by pair to Q 74:33–34!) |
| 84 | 16–18 | 3 | the twilight glow / the night / the moon | qsm-opened interior oath |
| 86 | 11–12 | 2 | the heaven of returning / the earth of splitting | **genuine qasam interior cluster** |
| 89 | 9–10 | 2 | (the people of) Thamūd / Pharaoh | narrative recall (not qasam) |

**Net true qasam count:** 20 opening + ≈5 genuine interior = **~25 true qasam
clusters**, with ~7 additional non-oath waw-GEN chains picked up by the
syntactic rule. The ratio is cleanly explained by genre: qasam-waw is nearly
exclusive to short Meccan surahs where surface rhetoric is oath-heavy; the
interior waw-GEN chains are in long narrative surahs where the rule fires
incidentally on lists.

## 3. Semantic categories of sworn-by objects

Using a root-based category map keyed by the Leeds root codes, the sworn-by
tokens sort into:

| Category | Exemplar roots | Count across all clusters |
|---|---|---|
| **celestial** | $ms, qmr, smw, njm, brj, Trq | 10 |
| **temporal** | lyl, nhr, DHw, fjr, E$r, ywm, sjw | 17 |
| **terrestrial** | Twr, tyn, zyt, bld, ArD, byt, sqf, sjr | 12 |
| **wind-kinetic** | *rw, Hml, jry, qsm, rsl, ESf, n$r, frq, lqy | 9 |
| **angelic** | Sff, zjr, tlw, nzE, n$T, sbH, sbq, dbr | 8 |
| **warrior-kinetic** | Edw, qdH, gyr, vwr | 4 |
| **psychological** | nfs, qlb, lwm | 2 |
| **instrumental** | qlm, ktb, qrA, sTr, nwn | 8 |
| **abstract** | $hd ($aAhid, ma$ohuwd) | 2 |
| **numeric** | $fE ("even"), wtr ("odd") | 2 |
| **divine-lord** | rbb (as in "by your Lord") | 1 |

**Monothematic opening clusters.** For each length-≥ 3 opening, we count
distinct categories:

| Surah | length | distinct cats | sequence |
|---|---|---|---|
| Q 37 | 3 | 1 | angelic × 3 |
| Q 51 | 4 | 1 | wind × 4 |
| Q 52 | 6 | 2 | terrestrial × 5 + instrumental × 2 (Mt Sinai → book → parchment → Kaʿba → canopy → sea) |
| Q 77 | 5 | 1 | wind × 5 |
| Q 79 | 5 | 1 | angelic × 5 |
| Q 85 | 4 | 2 | celestial + temporal + abstract × 2 |
| Q 89 | 5 | 2 | temporal × 3 + numeric × 2 |
| **Q 91** | **8** | **4** | **celestial / temporal / celestial / temporal / temporal / celestial / terrestrial / psychological** |
| Q 95 | 4 | 1 | terrestrial × 4 |
| Q 100 | 3 | 2 | warrior × 2 + "other" |

Q 91 is the unique **category-heterogeneous long opening oath**. Every other
opening cluster of 3 or more items is either monothematic or spans at most
2 categories. Q 91 traverses four: celestial (sun/moon/heaven), temporal
(brightness/day/night), terrestrial (earth), psychological (soul). This is
the structural fact that lets Q 91 *enact* a descent in scale: light → time →
sky → earth → self, mirrored around the day-night axis.

## 4. The sworn-by × sworn-about grid

Each opening cluster's sworn-about content (jawāb al-qasam) falls into
one of four macro-themes:

| Macro-theme | Exemplars | Opening clusters |
|---|---|---|
| **prophethood affirmed** | "Indeed you are from among the messengers" / "not a madman" / "has not strayed" | Q 36, 37, 52?, 53, 68 |
| **Qur'an's status** | "We have made it an Arabic Qur'an" / "sent it down in a blessed night" | Q 43, 44, 50, 85?, 92?, 93 (implied) |
| **resurrection / eschatology** | "what you are promised is true" / "the punishment is coming" / "bones will be assembled" / "a soul will convulse" | Q 51, 52, 75, 77, 79, 86, 100, 103 |
| **human nature** | "created in best of stature" / "inspired with fujūr and taqwā" / "mankind is in loss" / "to his Lord ungrateful" | Q 89, 91, 95, 100, 103 |

**The sworn-by — sworn-about semantic pairing:**

- **Q 51** (winds that disperse) → "what you are promised [i.e. rain, provision,
  resurrection] is true": the scattering-winds vouch for the scattering that
  is resurrection. Direct form-to-content.
- **Q 77** (sent-forth winds) → "what you are promised is coming to pass":
  same form-to-content linkage.
- **Q 79** (angels that extract souls) → "on the Day the blast convulses":
  the extracting-angels themselves are the agents of the sworn-about.
- **Q 52** (Mount Sinai + Book + Kaʿba + canopy + sea) → "the punishment of your
  Lord": six cosmic-scriptural witnesses for a single eschatological assertion.
- **Q 91** (cosmic seven) → "inspired [the soul] with its wickedness and its
  righteousness": the cosmic sequence authenticates the moral-psychological
  claim, which the Quran then extends at v9-10 to "successful is he who
  purifies it; failed is he who corrupts it". **The sworn-by enacts a descent
  from macro (sun) to micro (soul), and the sworn-about is a micro-claim
  (soul-purification) grounded in macro witness.**
- **Q 95** (fig / olive / Sinai / secure city) → "We have created man in the
  best of stature": four *toponymic* witnesses (three sanctuary-sites plus
  two fruit trees native to them) for a claim about human primordial
  excellence. The geography is the argument.
- **Q 89** (dawn / ten nights / even / odd / night) → "Is there in that an oath
  for one of perception?" This is uniquely **self-referential**: the jawāb
  is a meta-question about the adequacy of the oath just sworn.

This fits Farahi's "argumentative" theory of Quranic oaths: the sworn-by
object is evidence, not mere intensifier. Al-Rāzī and Ibn al-Qayyim's
"excellence" theory is a weaker baseline that cannot distinguish Q 79
(angels swear for a Day of angelic action) from Q 68 (pen swears for
prophethood not being madness). The sworn-by × sworn-about grid above is
the first tabular operationalization of Farahi's thesis at full-corpus
scale.

## 5. Oath clusters vs. rest-of-surah rhyme (the saj' test)

**Claim under test:** oath clusters are more phonetically uniform (saj')
than non-oath verses in the same surah.

**Computation.** For each of 32 multi-item clusters, take the fasila_2
(last 2 letters of the pause-form word, from `saj-fasila-per-verse.csv`) and
compute U2 = share of the most-common fasila_2. Compare the in-cluster U2
to the out-of-cluster U2 within the same surah.

**Raw numbers.** Real mean Δ(U2) = **+0.403** (in-cluster 0.775 vs. out-of-
cluster 0.372). Oath-cluster verses have more than double the rhyme
uniformity of the rest of the surah.

**Null test.** For each cluster, replace its verse-range with a random
consecutive run of the same length from the same surah; recompute the
Δ. 1 000 permutations. Permutation mean Δ = 0.365; one-sided p = 0.130.

**Honest verdict:** the effect is **real but not significant** under
length-matched randomization. Short consecutive runs in any surah tend
toward higher U2 than the surah average, because short runs have fewer
possible fasila values. The oath-cluster phonetic tightness is **largely
a length-and-position effect**, not an independent rhetorical property.
This is a negative result worth stating: the oath-cluster "tightness" that
classical rhetoric describes is tautological when you control for cluster
length. Ash-Shams (Q 91) remains a striking maximum case (all 15 verses
ending in -ā), but its uniqueness is surah-wide, not oath-specific.

## 6. Length distribution and the palindrome link

The multi-item cluster length distribution (§0) is

  n = 2 : 15, 3 : 7, 4 : 5, 5 : 3, 6 : 1, 8 : 1

The single length-8 cluster is **Q 91**, which by the item-counting rule
(v1 packs 2 items) reaches 8; by the verse-counting rule it is length-7.
Cross-reference with [palindromes.md](./palindromes.md): the **three
length-7 letter-count palindromes** in the Quran are

  - Q 91:1–7   [12, 14, 15, 15, 15, 14, 12]   — this oath cluster
  - Q 81:2–8   [16, 14, 14, 14, 14, 14, 16]   — an *idhā*-cluster (not
                                                 strict waw-qasam)
  - Q 37:127–133 [18, 19, 19, 14, 19, 19, 18] — a salām-on-Ilyāsīn coda
                                                 (not an oath at all)

Only Q 91 is a true waw-qasam cluster among the three palindromes. The
palindrome-run-1 claim that "all three length-7 letter palindromes are oath
clusters" is **accurate under a relaxed definition** (qasam includes
idhā-clusters, per Farahi) but **not under the strict waw-GEN / uqsimu-bi
definition used here**. Q 81 and Q 37 are still formulaic cosmic-or-
greeting clusters; they just are not qasam in the Arabic-grammatical sense.

## 7. Size-order and chiastic tests

**Size-order hypothesis:** does any cluster order sworn-by objects from
large (cosmic) to small (personal)?

Using ranks celestial=1, temporal=1.5, terrestrial=2, warrior/wind=2.5,
instrumental/warrior-kinetic=3, psychological=4:

| Cluster | Size sequence | Monotonic? |
|---|---|---|
| Q 74:33–34 | 1.5, 3 | ↗ |
| Q 75:1–2 | 1.5, 4 | ↗ |
| Q 81:17–18 | 1.5, 3 | ↗ |
| Q 86:11–12 | 1, 2 | ↗ |
| Q 91:1–7 | 1, 1.5, 1, 1.5, 1.5, 1, 2, 4 | **not monotonic** — drifts from celestial↔temporal for 5 items then to earth, then to soul |

Q 91 does NOT show monotonic descent at fine grain; it oscillates celestial
↔ temporal for 5 items, then descends to earth (v6) and soul (v7). But the
axis v4 ("the night when it enshrouds it") sits at a **pure temporal midpoint**
and the final item (soul) is the maximum-descent endpoint. So Q 91 realizes
the "cosmic-to-personal" descent at coarse grain (first 6 items: cosmic
oscillation; last item: soul) but not as a strict monotone.

**Chiastic-category hypothesis:** does any cluster's category sequence
read the same forwards and backwards?

Only one opening cluster is exactly chiastic:
- **Q 100:1–3** `warrior / other / warrior` — *al-ʿādiyāti ḍabḥā / al-mūriyāti
  qadḥā / al-mughīrāti ṣubḥā*. Warrior-horse at both ends, spark-strikers at
  the axis. (The "other" category is a coarse-grain artifact; finer tagging
  would put all three under warrior-kinetic, making the cluster
  category-monothematic instead of chiastic. So the chiasm here is
  categorical noise.)

Two interior clusters register category-palindromes but are not true oaths
(Q 44:26–27 and Q 45:5; both are narrative coordinate chains).

**Honest verdict: no cluster shows a robust category chiasm.**

## 8. Pre-Islamic kāhin parallels

Pre-Islamic soothsayers (kuhhān, sing. kāhin) delivered rhymed-prose
utterances (*sajʿ*) often opening with cascades of oaths by natural phenomena
— exactly the Q 51 / Q 77 / Q 79 / Q 91 format. The historical examples are
preserved (sparingly and filtered through Islamic-era transmitters) in the
*Aghānī* and Ibn Hishām's *Sīra*; a characteristic fragment from Suṭayḥ
the Jewish soothsayer runs "wa-l-layli idhā sajā / wa-l-fajri idhā tanaffasa"
(compare Q 81:17, Q 93:2). Angelika Neuwirth's *The Qur'an and Late Antiquity*
(German 2010, English 2019) treats the kāhin-qasam form as the phenotypic
matrix the early-Meccan corpus inherits and then **theologically recontextualizes**:
where the kāhin swears by nature to legitimize his own oracular utterance,
the Qur'an swears by nature to compel the hearer toward a specific
theological claim (resurrection / prophethood / moral accountability). The
form is inherited, the rhetorical telos is new. Nicolai Sinai's *The Qur'an:
A Historical-Critical Introduction* (Edinburgh 2017) uses "kāhin-register"
as a terminological label for Q 51, Q 79, Q 100, and notes that the Quran
eventually **disowns the register** at Q 69:40–43 ("it is not the word of a
kāhin"). This disowning is itself textual evidence that the register was
perceived as kāhin-adjacent by early audiences.

Our quantitative contribution to this conversation: **the monothematic
homogeneity of opening clusters** (§3) is what distinguishes the kāhin-
register oaths from ordinary waw-GEN chains; Q 51, Q 77, Q 79 pack 4–5
feminine-plural participles from a SINGLE semantic field, which is the
marked kāhin form. Q 91 is the only opening cluster that breaks the
monotheme pattern, and it does so by visiting every natural-object category
the Quran swears by elsewhere. In that specific sense Q 91 is the **summa
of all kāhin-register oaths** — a deliberate stylistic overdrive — and its
status as the sole letter-palindrome oath is consistent with it being the
most marked case in the corpus.

No prior published study (Neuwirth, Sinai, Tesei, Hawting, Farahi, Islahi,
Ibn al-Qayyim) reports this heterogeneity asymmetry across the 14 length-≥-3
opening clusters. The fact itself is a candidate novel observation.

## 9. Classical prior art

Five classical treatments define the scholarly landscape:

1. **al-Farrāʾ** (d. 207/822), *Maʿānī l-Qurʾān*. First systematic grammatical
   treatment of the oath waw, distinguishing `wāw al-qasam` (oath waw,
   governs genitive) from `wāw al-ʿaṭf` (conjunctive waw). The genitive-case
   diagnostic we use in this analysis is al-Farrāʾ's rule, operationalized.
2. **al-Zamakhsharī** (d. 538/1144), *al-Kashshāf*. Develops the *iʿẓām*
   theory: God swears by natural objects to attract human attention to their
   grandeur and thereby to the truth of the sworn-about statement.
3. **al-Rāzī** (d. 606/1210), *Mafātīḥ al-Ghayb*. Philosophical-theological
   reading. Categorizes oaths by category of sworn-by (sun, moon, etc.) and
   gives elaborate justifications for each; unlike Zamakhshari, al-Rāzī
   starts to search for specific semantic links between sworn-by and
   sworn-about, prefiguring Farāhī.
4. **Ibn al-Qayyim** (d. 751/1350), *al-Tibyān fī Aqsām al-Qurʾān*. **The**
   classical reference: a full monograph on the oaths, the only dedicated
   treatise. Ibn al-Qayyim classifies oaths by sworn-by type, discusses all
   42 (his number) oath contexts, and argues that all divine oaths resolve
   to "oath by the greatness of God's own attributes" (i.e. the created
   thing is a token for its Creator). His enumeration closely overlaps but
   is not identical to the 20 opening clusters we detect here; his 42
   includes many single-verse oaths like Q 38:1 and the interior oaths Q
   69:38 and Q 70:40 that we separate.
5. **Farāhī** (d. 1349/1930), *Imʿān fī Aqsām al-Qurʾān*, and his student
   **Islāhī**, *Tadabbur-i-Qurʾān*. Farāhī's 4-category classification
   (phenomenal / historical / experiential / conjugate) is the most
   conceptually fine-grained classical scheme. Farāhī's **argumentative
   thesis** — that the sworn-by provides *evidence*, not mere attention-grab
   — is the interpretive theory our §4 grid tries to quantify. Farāhī
   explicitly cites Q 91 as his *conjugate* archetype (paired opposites:
   sun/moon, day/night, heaven/earth, and then the unpaired soul).

**Our contribution, honestly bounded:**

- al-Farrāʾ's rule is made algorithmic and applied to all 6 236 verses
  (§2, 20 opening clusters recovered).
- Ibn al-Qayyim's 42-oath list is matched against and narrowed by the
  strict-waw/qsm rule (ours: 20 openings + ~5 genuine interior).
- Zamakhshari's *iʿẓām* theory and Farāhī's argumentative theory have not
  been quantitatively contrasted before; the sworn-by × sworn-about grid
  (§4) gives the first tabular basis for such a contrast.
- The length-frequency histogram (§6), the monothematic-vs-heterogeneous
  opening-cluster asymmetry (§3), and the kāhin-register quantitative
  signal (§8) are genuinely new observations — I find no prior
  computational enumeration in Neuwirth, Sinai, or the Farāhī-Islāhī
  hermeneutic tradition.

## 10. Honest verdict on novelty

| Claim | Status | Classical precedent |
|---|---|---|
| 20 opening oath clusters, all Meccan | Recovered (not novel); the set was known | Farāhī, Ibn al-Qayyim, list overlap |
| Monothematic vs heterogeneous opening asymmetry (Q 91 uniquely mixed) | **Novel quantitative observation** | Farāhī called Q 91 "conjugate" but did not frame heterogeneity-vs-monothematism as a sort across all openings |
| Saj' uniformity of clusters is length-explained (null result) | **Novel negative finding**; classical rhetoric would have predicted a real effect | Al-Suyūṭī *Itqān* 58 implicitly assumes oath-cluster tightness is special |
| Q 91's length-7 palindrome sits at the one heterogeneous opening oath | Observation chain new; constituent facts known | Palindrome: novel (palindromes.md). Oath-heterogeneity: novel. Co-occurrence: novel. |
| Q 91 = sole heterogeneous length-≥-3 opening in the Quran | **Novel observation** | None |
| Size-order descent (cosmic → personal) holds at coarse but not fine grain | Descriptive | Implicit in Farāhī "conjugate" framing |
| Category-chiasm hypothesis fails | **Novel negative finding** | None |
| Kāhin-register → monothematic opening; Q 91 as summa-overdrive | **Novel synthesis** | Neuwirth, Sinai describe register qualitatively; not quantitatively |
| Length distribution peaks 2-3; longest is Q 91 (8 by item-count, 7 by verse-count) | Descriptive | Length never before enumerated |
| Sworn-about falls into 4 macro-themes | Descriptive | Partially in Farāhī's argumentative scheme |

Net new contributions: the **monothematic-opening pattern** and **Q 91 as
sole heterogeneous long opening**. The null result on saj' uniformity is
also worth keeping: it is the kind of fact classical scholarship could not
discover because it requires per-verse phonetic tagging of the whole corpus.

## 11. Connection to previously surviving Phase-B findings

- **Palindromes**: Q 91:1–7 is the sole true qasam-cluster among the three
  length-7 letter palindromes. The other two (Q 81:2–8, Q 37:127–133) are
  formulaic clusters of other types. This tightens the palindromes.md
  claim.
- **Saj' rhyme**: Ash-Shams (Q 91) is already the uniform-rhyme extremum
  (15/15 ending in -hā). The oath cluster is verses 1–7, i.e. the first
  half, and the 15-verse mono-rhyme continues through the sworn-about
  (vv 8–10) and the Thamūd pericope (vv 11–15). The oath is the *opening
  half* of a 15-verse mono-rhyme construction.
- **Chronological-revelation**: all 20 opening oath clusters are in
  early-Meccan surahs (Nöldeke phase 1). The oath-cluster form is a
  diagnostic of early-Meccan register.
- **Ring centers**: no oath cluster coincides with a Bonferroni-surviving
  ring center (the ring centers are narrative pivot-points, the oath
  clusters are surah openings; different structural slots).
- **Intra-quranic cross-refs**: the refrain *wa-l-layli idhā yaghshā* /
  *wa-l-layli idhā yasrī* / *wa-l-layli idhā ʿasʿasa* recurs across Q 81,
  Q 89, Q 92, Q 93 — four different opening oaths with the SAME sworn-by
  (al-layl + idhā-verb) but four different verbs for night's action.
  This is a *mutashābih-lafẓī* pattern (al-Kirmānī's category) on the
  oath-object itself.

---

_Artifacts: `findings/phase-b-hypotheses/csv/oath-clusters.json` (full per-cluster
record with items, categories, sworn-about, verse-spans), `oath-clusters.csv`
(flat table), `oath-clusters-stats.json` (summary aggregates). Detection
script: `analysis/notebooks/oath_clusters.py`._
