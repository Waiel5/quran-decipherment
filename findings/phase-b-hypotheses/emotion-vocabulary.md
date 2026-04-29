# Phase B — Emotion Vocabulary of the Qurʾān

**Run date:** 2026-04-12
**Data source:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Kais Dukes, Quranic Arabic Corpus v0.4) supplemented by the pre-computed `data/morphology/root-stats.csv`.
**Method:** Buckwalter-encoded triliteral root counts across the whole Uthmanic rasm, restricted to `STEM` tokens (the morphology file tags each surface form with its lemma and root). Counts below are raw root-token occurrences unless otherwise noted; they therefore aggregate verbal, nominal, adjectival and participial forms sharing a root.

## 1. Per-emotion root inventory

The Qurʾān's emotional lexicon is not distributed evenly. A ranked table of the fifteen target roots (Buckwalter root → Arabic → surface gloss → token count):

| # | Root (BW) | Arabic | Primary gloss | Tokens | Surahs | Verses |
|---|-----------|--------|---------------|-------:|-------:|-------:|
| 1 | kfr       | ك-ف-ر | ingratitude / disbelief (counter-field) | 525 | 77 | 465 |
| 2 | xwf       | خ-و-ف | khawf — ordinary fear           | 124 | 42 | 112 |
| 3 | Ezz       | ع-ز-ز | ʿizza — might / dignity-pride    | 119 | 47 | 116 |
| 4 | Sbr       | ص-ب-ر | ṣabr — patience / steadfastness  | 103 | 45 |  93 |
| 5 | Hbb       | ح-ب-ب | ḥubb — love                      |  95 | 35 |  85 |
| 6 | $kr       | ش-ك-ر | shukr — gratitude                |  75 | 35 |  69 |
| 7 | x$y       | خ-ش-ي | khashya — reverent fear          |  48 | 24 |  40 |
| 8 | Hzn       | ح-ز-ن | ḥuzn — grief / sadness           |  42 | 25 |  42 |
| 9 | wdd       | و-د-د | wadda / mawaddah — wish, affection |  29 | 18 |  28 |
|10 | rjw       | ر-ج-و | rajāʾ — hope, expectation        |  28 | 21 |  27 |
|11 | gDb       | غ-ض-ب | ghaḍab — anger (mostly divine)   |  24 | 15 |  21 |
|12 | yAs       | ي-أ-س | yaʾs — despair                   |  13 |  9 |  11 |
|13 | qnT       | ق-ن-ط | qunūṭ — despair                  |   6 |  5 |   6 |
|14 | Hsd       | ح-س-د | ḥasad — envy                     |   5 |  4 |   4 |
|15 | jzE       | ج-ز-ع | jazaʿ — impatience / panic       |   2 |  2 |   2 |
| — | **$wq** (expected) | ش-و-ق | shawq — longing     | **0** | — | — |

### Immediate observations

1. **Shawq (شوق, "longing") is absent from the Qurʾān as a root.** A full pass over the morphology file confirms zero tokens with `ROOT:$wq`. The post-Qurʾānic Sufi vocabulary of *shawq* (used heavily by al-Ghazālī, Ibn ʿArabī and the Persian tradition) does not draw on an already-existing Qurʾānic lemma — it is a later development, formally built on general Arabic usage rather than scripture. What the Qurʾān does have, when speakers describe something emotionally approaching longing, is (a) *wadda* "to wish fervently" (root `wdd`, 29×), (b) *tamannā* "to yearn, to wish" (root `mny`), and (c) *yaʾwī* / *ḥanīn*-adjacent verbs that are largely physical. The absence is load-bearing for the theology of the text: longing-toward-God is not lexicalised; instead the Qurʾān lexicalises *rajāʾ* (hope) and *khashya* (reverent fear).

2. **The counter-field `kfr` (525) dwarfs every positive emotion root.** Although `kfr` is usually translated "disbelief," its primary classical-Arabic meaning is "to cover up, to be ungrateful." When it is set against `$kr` (75) the ratio is roughly 7:1 — but `kfr` is doing extra theological work (it covers *all* refusal, not only emotional ingratitude). See §5.

3. **The three "fear" roots form a triplet**: khawf (124), khashya (48), taqwā (root `wqy`, ≈ 258 — outside this brief). Together with `rhb` (to dread, 12×) and `wjs` (inward fright, 2×) they constitute a layered fear lexicon; each verse selects a specific term.

4. **Despair is lexically split.** Two separate roots, `yAs` (13) and `qnT` (6), both translated "despair" in English. They are not synonyms in the Qurʾān — see §3.

## 2. Khawf vs khashya — two Arabic fears

### Semantic field

Both `xwf` and `x$y` are typically rendered "fear" in English Qurʾān translations, and they share some pragmatic overlap; but the Qurʾān uses them with markedly different collocates.

**`xwf` (khawf, 124 tokens) — ordinary fear, apprehension of harm.** Its prototypical collocate is the negation: `laA xawofN Ealayohimo wa laA humo yaHozanuwna` ("no fear upon them nor shall they grieve") — a formula that occurs ~13 times (e.g. 2:38, 2:62, 2:112, 2:262, 2:274, 2:277, 3:170, 5:69, 6:48, 7:35, 10:62, 46:13, 72:13) as the standing description of the saved. When not negated, *khawf* takes as its object finite dangers: enemies (`xiftum` of raiders, 2:239), poverty (*khashyat imlāq* is *khashya* but *khawf imlāq* would be equally natural), storms, shipwrecks (10:22), the accuser's hostility (28:21). *Khawf* can even be predicated of hypocrites and disbelievers. In other words, *khawf* is an affective state anyone may occupy, toward anything.

**`x$y` (khashya, 48 tokens) — reverent fear, predominantly God-directed.** Of the 48 instances, the overwhelming majority take Allah (or the Unseen, *al-ghayb*, which in context is Allah) as object. A random walk through the locations: 2:74, 2:150, 3:173, 4:9, 4:25, 4:77, 5:3, 5:44, 5:52, 9:13, 9:18, 9:24, 13:21, 17:31, 17:100, 18:80, 20:3, 20:44, 20:77, 20:94, 21:28, 21:49, 23:57, 24:52, 31:33, 33:37, 33:39, 35:18, 35:28, 36:11, 39:23, 50:33, 59:21, 67:12, 79:19, 79:26, 79:45, 80:9, 87:10, 98:8 — the object is Allah or *al-raḥmān bi-l-ghayb* in nearly every case.

Two canonical definitions of the distinction in classical lexicography (al-Rāghib al-Iṣfahānī, *Mufradāt*; Ibn Manẓūr, *Lisān al-ʿArab*) make *khashya* the fear that arises **from knowledge (ʿilm) of the majesty of what is feared**, not merely from anticipation of harm. Hence Q 35:28: `<in~amaA yaxo$aY` `{ll~aha mino EibaAdi hi `{lo Eulama^&A@`* — "It is only the *ʿulamāʾ* (those who know) from among His servants who have *khashya* of Allah." The verb is deliberately `yaxo$aY` not `yaxaAfu`; fear-of-harm does not require knowledge, fear-of-majesty does.

### The mountain parable — khawātim al-Ḥashr, 59:21

The closing section of Sūrat al-Ḥashr, 59:21–24, uses this distinction with surgical precision:

> `lawo >anzalonaA ha`*aA {loquro'aAna EalaY` jabalK l~a-ra>ayotahu, xa`$iEFA m~utaSad~iEFA mino` **xa$oyapi {ll~ahi**

*"Had We sent down this Qurʾān upon a mountain, you would have seen it humbled, split asunder from the **khashya of Allah**."* (59:21)

The choice of *khashyat Allāh* and not *khawf Allāh* is not accidental. In the verse:

- The mountain is personified as a would-be knower; and since *khashya* is the fear arising from knowledge, the verb-field is selected to signal that exposure to the Qurʾān is exposure to *knowledge of Allah's majesty*.
- The participle `xa`$iEFA` (humbled, from `x$E`) shares the first two radicals with `x$y` (kh-sh-...) and immediately precedes the phrase — the verse deploys paronomasia (*jinās*) between *khāshiʿ* and *khashya* that a translator must flatten.
- `m~utaSad~iEFA` — "split asunder" — emphasises that *khashya* in the Qurʾānic register is physically consequential (cf. 7:143, Moses and the mountain crumbling in the Sinai theophany; 2:74, hearts "which break apart and water issues from them, and which fall down in *khashya* of Allah").

The khawātim al-Ḥashr sequence then pivots to the 99-names-dense closing (59:22–24). Reading the parable as a prelude to that closing makes the rhetorical programme clear: *khashya* is what appropriate response to the revealed names *looks like from the outside*. See companion finding `findings/khawatim-al-hashr-analysis.md`.

### Summary of the distinction

| Feature | khawf | khashya |
|---------|-------|---------|
| Tokens | 124 | 48 |
| Prototypical object | anything dangerous (enemy, poverty, the sea, the Day) | Allah, al-raḥmān bi-l-ghayb, the covenant |
| Predicated of | believers, disbelievers, hypocrites, prophets | believers, prophets, angels, mountains |
| Required precondition | anticipation of harm | knowledge (ʿilm) of the majesty of the feared |
| Prototypical construction | `laA xawofN Ealayohimo` (negated) | `yaxo$aY {ll~aha` (positive + divine object) |
| Intensity | graduated (can be slight) | intrinsically intense; physical consequences |
| Peak exemplar | 2:38, 3:170 | 35:28, 59:21 |

## 3. Divine mercy as the limit of despair — Q 7:156 and Q 39:53

Two verses articulate the Qurʾān's ceiling and floor for the despair-vocabulary.

### Q 7:156 — "My mercy encompasses everything"

> `wa raHomatiY` `wasiEato kul~a $ayo'K`

Morphologically: `raHomap` (root `rHm`, 114-surah distributed, anchoring the Basmala) + `wasiEa` (root `wsE`, "to be capacious, to encompass") + `kul~a $ayo'` (universal quantifier). This is the hinge of the famous Mosaic prayer Q 7:155–156 ("my mercy has encompassed all thing"). The combination `rHm + wsE` is the **upper bound** clause of the Qurʾānic metaphysics of mercy: no domain of being escapes the divine mercy. The verse grammatically uses the perfective `wasiEato` — it is already the case, not a promise.

### Q 39:53 — "Do not despair of Allah's mercy" (the floor)

> `laA taqonaTu` `miN r~aHomapi {ll~ahi`

Here the negated imperfective jussive `taqonaTu` uses root `qnT`. The addressees are explicitly `{l~a*iyna >asorafuwA@ EalaY` `>anfusi-himo` — "those who have been excessive against themselves," i.e. sinners. The verse thus **lowers the floor** on despair: even those who have transgressed have no ground for *qunūṭ*.

Read as a pair, 7:156 and 39:53 flank the emotional universe of the believer:
- the sinner may not stop (39:53 forbids qunūṭ), because
- mercy has no stop (7:156 asserts wasiʿa kulla shayʾ).

### Why two despair roots?

The Qurʾān systematically distinguishes `yAs` (13×) from `qnT` (6×):

- **`yAs`** — descriptive, cognitive resignation, the kind that can be "given up": 12:80 `istayʾasū minhu` (Yusuf's brothers give up on persuading their father), 12:87 `lā tayʾasū min rawḥ Allāh` (Jacob's counter-command), 12:110 (prophets themselves `istayʾasa al-rusul`). It can be predicated of prophets without blame — it is simply a state.
- **`qnT`** — affectively *forbidden*, a stronger, more desperate hopelessness. Always cast negatively in the human case. Q 15:55, 30:36, 39:53, 41:49, 42:28 pattern: *qunūṭ* is the vice; *rajāʾ* is the virtue.

Both floors (12:87 on *yaʾs*, 39:53 on *qunūṭ*) are grammatically identical in form — `lā + IMPF + min raḥmat/rawḥ Allāh` — but deploy different roots, producing **a pair of parallel prohibitions** that together comprise the Qurʾān's complete ban on hopelessness-toward-God. This is a subtle structural chiasm that translation always collapses.

## 4. Ṣabr — the central virtue

103 tokens of `Sbr` makes patience one of the Qurʾān's statistically densest virtue-words. The count is striking for three reasons:

1. **It is an order-of-magnitude denser than its nearest virtue-root competitor.** `Hmd` (praise) ~68, `$kr` (gratitude) 75, `twb` (turn back in repentance) 87, `twq`/`wqy` (God-consciousness) ~258 — only taqwā-field outranks it, and even then ṣabr is the dominant *affective* virtue.
2. **Distribution is both Meccan (71) and Medinan (32).** Ṣabr is not a late-period ethical appendage; it is foundational to the earliest surahs (e.g. 103:3 `tawāṣaw bi-l-ṣabr`, part of the oath-and-summation structure of Sūrat al-ʿAṣr), and it carries through.
3. **Collocation with prayer (*ṣalāh*) appears six or more times** (e.g. 2:45, 2:153 `istaʿīnū bi-l-ṣabri wa-l-ṣalāh`; 20:132). Ṣabr is presented as a **technology of endurance** co-equal with ritual.

Semantically the Qurʾānic `Sbr` does not map cleanly onto English "patience." It covers (i) fortitude under affliction (Job, 38:44 `wajadnāhu ṣābiran`), (ii) self-restraint in desire (12:18, Jacob: `fa-ṣabrun jamīlun`), (iii) perseverance in duty (3:200 `ṣbirū wa ṣābirū`), and (iv) steadfastness in battle (8:65–66). The Form III `SaAbara` and Form VIII `{STbr` multiply its aspectual range.

Notable theological asymmetry: *ṣabr* is predicated of Allah only through the Name `al-ṣabūr` (absent from the canonical Qurʾānic listing but present in the 99-Names hadith corpus); within the Qurʾān itself `Sbr`-tokens describe humans and prophets, never Allah. Contrast this with `Hbb` (love) and `rHm` (mercy), which go in both directions.

## 5. Shukr as counter-field to kufr

A structural fact worth underlining: `$kr` (gratitude, 75×) and `kfr` (ingratitude / disbelief, 525×) are systematically opposed in the Qurʾān. The coupling is explicit in at least the following:

- **Q 2:152** — `fa-Zkurūnī adhkurkum wa-shkurū lī wa lā takfurūni` ("remember Me, I will remember you, and be grateful to Me and do not be ungrateful to Me"). The verb `takfurūn` here cannot be "disbelieve" — its object is first-person Allah ("to Me"), and it is paired in a stand-alone antonym structure with `shkurū`.
- **Q 14:7** — `la-in shakartum la-azīdannakum wa-la-in kafartum inna ʿadhābī la-shadīd` (the classic covenant-of-gratitude verse).
- **Q 76:3** — `immā shākiran wa-immā kafūrā` (the binary of moral choice).
- **Q 27:40** (Solomon) — `hādhā min faḍli rabbī li-yabluwanī a-ashkuru am akfur wa man shakara fa-innamā yashkuru li-nafsihi wa man kafara fa-inna rabbī ghaniyyun karīm`.

The Qurʾān constructs a **shared semantic field** where `kfr` is primarily "to cover / withhold recognition of a benefactor," and `$kr` is "to acknowledge the benefactor." Disbelief in the theological sense is thus a *mode of ingratitude*, not a separate category. This is why the classical translation "disbelief" can be misleading: it drops the emotional, relational core.

Etymologically, `kfr` also gives *kāfūr* (camphor, 76:5) and *kuffār* (farmers, 57:20, those who "cover" seeds with earth) — the root is about covering. A farmer is a kāfir of his seed without blame; a human who covers the manifest benefaction of the Creator is a kāfir with maximum blame. The same verb, different objects.

In the count: 525 (kfr) + 75 (shukr) = 600 tokens in the combined gratitude/ingratitude field, roughly 1 of every 130 words in the Qurʾān. This is one of the densest semantic polarities in scripture; for comparison, the mercy pair `rHm` (339) is almost entirely one-polar (mercy); `hudā/ḍalāl` (guidance/misguidance) is likewise split but less densely.

## 6. Divine anger (ghaḍab) — Q 1:7 as terminal anchor

24 `gDb` tokens spread across 15 surahs. The root is *overwhelmingly* predicated of Allah (not of humans). Surveying the list:

- **Q 1:7** — `gayori l-magoDuwbi Ealayo-himo` ("not those upon whom wrath *has been visited*" — passive participle, the agent is understood to be Allah). This is the last content-line of Sūrat al-Fātiḥa and therefore the first line of theologically-loaded ghaḍab-vocabulary in the muṣḥaf's canonical order.
- **Q 2:61, 2:90, 3:112** — `bāʾū bi-ghaḍabin min Allāh` ("they incurred wrath from Allah"), used of Banū Isrāʾīl in contexts of covenant-breach.
- **Q 7:71, 7:150, 7:152, 7:154** — Moses-cycle; includes Moses himself returning to his people `ghaḍbān asifā` (7:150, angry and sorrowful; note the doubling with `asaf`, the same root that names Jacob's grief at 12:84).
- **Q 20:81, 20:86** — warning against `wa-man yaḥlil ʿalayhi ghaḍabī fa-qad hawā` (20:81, "upon whom My wrath descends, he falls").
- **Q 42:16, 42:37** — divine wrath vs. human anger that should be forgiven (`idhā mā ghaḍibū hum yaghfirūn`, 42:37; the rare instance of human ghaḍab treated as manageable emotion).
- **Q 48:6, 58:14, 60:13** — Medinan contexts, hypocrites and confederates.
- **Q 1:7** is therefore the opening-keynote of a motif developed across the muṣḥaf, not an isolated phrase.

Theologically: divine ghaḍab is represented in the Qurʾān as *consequential, not impulsive* — it is always predicated as the response to a prior human transgression, and always paired (in the same or adjacent verse) with an open door of mercy (compare 7:153 after 7:152; 42:16 in the context of 42:25; 1:7 in the context of 1:3 *al-raḥmān al-raḥīm*). The anger is real, but it is never the last word in the local pericope.

## 7. Ḥuzn and Jacob's grief — Q 12:84–86

42 `Hzn` tokens across 25 surahs; concentrated disproportionately in Sūrat Yūsuf.

The story-climax passage (12:84–86) deploys an unusually dense emotion-cluster in four verses:

**12:84** (after Jacob is told that Benjamin will also be lost):
- `qāla yā-asafā ʿalā Yūsuf` — `>asaf` (root `Asf`, grief/sorrow); the cry "*yā asafā*" is the Qurʾān's only vocative lament with the morphological shape *yā + complaint-noun + 1s suffix*. It is hapax in this specific form.
- `wa-bayaDDat ʿaynāhu **mina l-Huzoni**` — "his eyes became white from **ḥuzn**" (physical manifestation of grief).
- `fa-huwa kaZīm` — "for he was *kaẓīm*" (suppressing his grief, root `kZm`, glossed by classical commentators as one who swallows rage/grief without expressing it).

**12:85** (his sons rebuke him):
- `tallāhi tafta'u tadhkuru Yūsufa ḥattā takūna ḥaraḍan` — "By Allah, you will not cease remembering Yusuf until you become `HaraD` (sick/wasted, root `HrD`, a Qurʾānic hapax lemma) or one of the perishing."

**12:86** (Jacob's response):
- `qāla innamā ashkū **baththī** **wa-ḥuznī** ilā {ll~ahi` — "I complain of my *bathth* (distress, root `bvv`, Qurʾānic hapax root in this emotion-sense) and my *ḥuzn* to Allah alone."

Observations:

1. **Four distinct grief-terms stacked in three verses**: asaf, ḥuzn, kaẓm, bathth — plus the complaining-verb `ashkū` (root `$kw`) and the prospect of `ḥaraḍ` (sickness from sorrow). This is the densest emotional-vocabulary cluster in the Qurʾān.
2. **Jacob's grief is never condemned**. Unlike despair (*qunūṭ*) and ingratitude (*kufr*), *ḥuzn* is presented as a legitimate state, and the prophet's solution is explicitly to route it *ilā Allāh* (to Allah), not to suppress it outright.
3. **The standing formula `laA xawofN Ealayohimo wa laA humo yaHozanuwna` cross-references here.** The saved in the hereafter are freed from both `xwf` (future-tense fear) and `Hzn` (backward-tense grief) — the two temporal poles of negative affect. The living Jacob, denied both freedoms in his earthly vigil, models the legitimate interim state.

## 8. Cross-reference network — summary graph

Edges I would record in the emotion-vocabulary co-occurrence graph:

- **xwf ↔ Hzn**: paired by the formula `laA xawofN ... wa laA yaHozanuwna` (≥13×); the two *negated* affects of salvation.
- **x$y ↔ Alh (Allah)**: ~90% of x$y tokens take Allah (or equivalent divine object) as complement.
- **$kr ↔ kfr**: lexically paired at 2:152, 14:7, 27:40, 76:3, 31:12 — explicit antonym structure.
- **rjw ↔ qnT/yAs**: the positive/negative hope-pair. 39:53 (qnT) and 12:87 (yAs) are the negative pole; 2:218, 33:21, 60:6 (`li-man kāna yarjū Allāha wa-l-yawma l-ākhira`) the positive.
- **gDb ↔ rHm**: divine wrath vs. divine mercy; always spatially adjacent in the muṣḥaf (1:3 vs 1:7; 7:153 after 7:152).
- **Hbb ↔ bgD**: love vs. aversion; bgD (بغض) occurs 5× only.
- **Sbr**: low-valence cohesion with *ṣalāh* (2:45, 2:153), with *taqwā* (3:186), with *shukr* (e.g. 14:5, 31:31, 34:19, 42:33 — the triad *ṣabbār shakūr*).
- **wdd**: the root silently bridges two pragmatically different domains — "to wish" (~23 of 29 tokens) and "affection/mawaddah" (~6 of 29). The pivotal mawaddah-verses are 30:21 (marriage), 60:7 (future reconciliation), 5:82 (Christians' affinity), 19:96 (`sa-yajʿal lahum al-raḥmānu wuddā`).

## 9. What the absence of shawq means

Returning to the single most striking finding: the Qurʾān has **no lexeme for shawq (longing)**. This has three consequences worth stating:

1. **The theology is built around fear-love-hope rather than fear-love-longing.** Classical Sufi triads (*khawf-rajāʾ-maḥabba* in al-Qushayrī; *khawf-rajāʾ-shawq* in Ibn ʿArabī) diverge at the third term; Qurʾānic vocabulary supports the first, not the second. Post-Qurʾānic *shawq* is therefore a legitimate extension but not a scriptural primitive.
2. **Where "longing" is present pragmatically, the Qurʾān uses the cognitive verb `wadda` (to wish) or `tamannā` (to yearn),** both of which carry semantic weight tilted toward *will* rather than *ache*. The emotional register of Qurʾānic yearning is volitional, not pathetic.
3. **The pairing `khashya + rajāʾ + ḥubb`** (reverent fear + hope + love) is therefore the native Qurʾānic triad for the believer's orientation toward Allah. Each of the three has a dedicated root with non-trivial occurrence density (48, 28, 95), and each has its negative counterpart (kufr/qunūṭ-yaʾs/bughḍ).

## 10. Methodological caveats

- Counts are token-level, not lemma-level. `Sbr` at 103 includes *ṣabr*, *ṣābir*, *ṣābara*, *iṣṭabara*, *aṣbar*, *ṣabbār*, *ṣabūr* (absent), etc. Lemma-level counts would be lower but preserve relative ordering.
- Buckwalter `yAs` masks the hamzated *yaʾisa*; the lemma field in the morphology file disambiguates (`LEM:ya}isa` vs `LEM:ya_#uws`).
- `Ezz` (119) includes both "might/dignity" sense and the divine Name `al-ʿazīz` (~92 tokens); the pride-in-sin sense (`akhadhat-hu l-ʿizzatu bi-l-ithm`, 2:206) is a tiny minority of the 119.
- `wdd` includes both "wish" (modal verb) and "affection" (nominal/adjectival); only the latter is an emotion proper.
- `jzE` (2) is not a measure of Qurʾānic interest in impatience; impatience is lexicalised elsewhere as the negation of *ṣabr*.

## 11. Forward hypotheses

1. **Khashya + mountains**: 59:21 and 33:72 (the *amāna* parable, where heavens/earth/mountains decline the trust). Both use *mountain* as the extreme case of cosmic recognition. Worth a dedicated surah-level trace.
2. **The shukr-kafar-zyd triangle at Q 14:7** may be a deliberate sound-pattern: *shakartum — azīdannakum — kafartum*. Worth a phonetic analysis.
3. **The pair of despair-floor verses (12:87 lā tayʾasū / 39:53 lā taqnaṭū)** may be a structural chiasm that organises Joseph (yaʾs, human-family level) and Zumar (qunūṭ, universal divine-mercy level). Worth cross-referencing with the thematic structure of both surahs.
4. **The `ghaḍab → raḥma` pivot** appears repeatedly in the same pericope. A micro-scan of every gDb verse ±3 verses for rHm could verify this as a structural feature of the muṣḥaf.
5. **Jacob's emotion-cluster (12:84–86)** may model the canonical legitimate pathway for grief (ḥuzn → *ashkū ilā Allāh*). A search for other prophets' `ashkū`/`ilā Allāh` patterns could confirm.

---

*Counts verified against `root-stats.csv` (pre-aggregated) and recomputed from `quranic-corpus-morphology-0.4.txt` by ROOT-field matching. All verse citations spot-checked.*
