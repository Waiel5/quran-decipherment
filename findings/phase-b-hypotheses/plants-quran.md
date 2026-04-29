# Plants in the Qur'an: Inventory, Geography, and Theology

**Phase:** B-hypotheses
**Data source:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Quranic Arabic Corpus, Kais Dukes, v0.4)
**Text:** `quran-text/quran-min-tashkeel.json` (Tanzil Uthmani)
**Scope:** All botanical lexemes and cognate agricultural vocabulary.

## 0. Method

Every claim below is keyed to the Dukes morphology file. Roots were searched with `ROOT:<buckwalter>` queries and each hit cross-checked against the surface form and the Uthmani text. Counts are **stem occurrences** (noun/verb tokens tagged `STEM`), not word-window hits, so homographs are filtered out. The root `brr` (piety/righteousness) is intentionally excluded from "wheat" despite traditional glosses for *burr* — the Dukes corpus contains no `brr`-stem token that means the cereal, so *burr* is not lexically present in the Qur'an and the Q 2:61 complaint lists only five named plants (see §4).

---

## 1. Per-plant inventory

### 1.1 Nakhl / naxiyl / naxlap — date palm (ROOT: nxl)

Twenty stem occurrences under three lemmas: `naxol` (masc., collective), `n~axiyl` (masc. pl.), `n~axolap` (fem. sing., an individual tree). Locations:

| Ref | Form | Lemma | Context |
|---|---|---|---|
| 2:266:8 | naxiylK | n~axiyl | parable of the garden with streams |
| 6:99:20 | naxoli | naxol | creation sign, "from the date-palm sprouting clusters" |
| 6:141:8 | naxola | naxol | trellised/untrellised gardens |
| 13:4:9 | naxiylN | n~axiyl | diverse produce from one water |
| 16:11:6 | naxiyla | n~axiyl | An-Naḥl agricultural sign |
| 16:67:3 | naxiyli | n~axiyl | fruits yielding intoxicant + good sustenance |
| 17:91:6 | naxiylK | n~axiyl | Makkan disbelievers' demand for a garden |
| 18:32:11 | naxolK | naxol | parable of two men's gardens |
| 19:23:5 | naxolapi | n~axolap | Maryam's palm at Jesus' birth |
| 19:25:4 | naxolapi | n~axolap | "shake to yourself the trunk of the palm" |
| 20:71:21 | naxoli | naxol | Pharaoh threatens crucifixion "on trunks of palms" |
| 23:19:6 | naxiylK | n~axiyl | palm + grape gardens |
| 26:148:2 | naxolK | naxol | Thamud: "palms whose spathe is tender" |
| 36:34:5 | naxiylK | n~axiyl | Ya-Sin sign of life-after-death |
| 50:10:1 | naxola | naxol | "tall palms with piled spathe" — Qaf rain-revival |
| 54:20:5 | naxolK | naxol | ʿĀd: bodies "like stumps of uprooted palms" |
| 55:11:3 | naxolu | naxol | Ar-Raḥmān paradise-earth |
| 55:68:3 | naxolN | naxol | second paradise — palm + pomegranate |
| 69:7:14 | naxolK | naxol | ʿĀd again, "stumps of hollow palms" |
| 80:29:2 | naxolFA | naxol | ʿAbasa food-sign list |

The palm is by some margin the most frequent plant of the Qur'an (20 tokens). It straddles **three semantic zones**: (a) creation-sign / agricultural providence (Surahs 6, 13, 16, 36, 50, 55, 80); (b) parable material for judgement (2:266, 18:32, 17:91); (c) prophetic biography — most movingly Maryam in Sūrat Maryam 19:23–25 where the dry palm yields fresh *ruṭab*, a localised paradise-token inside her distress. The two occurrences of the feminine singular `n~axolap` are both in that Maryam scene: grammatically, the *one* palm that witnesses the birth of ʿĪsā is the only individuated palm in the Qur'an.

The palm is also the Qur'an's preferred **simile of divine destruction**: 54:20 and 69:7 both compare the felled people of ʿĀd to `>aEojaAz naxol` (palm stumps), once `mun[qaEir` (uprooted) and once `xaAwiyap` (hollow). The same tree that signals life (16:11, 50:10) signals death when wrenched.

The lemma `naxol` can be collective-masculine or feminine depending on dialect, and the corpus tags it sometimes `M` (e.g. 2:266:8 MP) and once `F` (19:23 `n~axolap`). This is a known grammatical feature the morphology preserves faithfully.

Note on *tamr* (ripe date, fruit of the palm): the root `tmr` does **not** appear in the Qur'an as the noun "date" — the single `tmr…`-looking stem at 40:75 is `tamraHuwna` from the unrelated root `mrH` ("rejoice"). The Qur'an speaks only of the **tree** (*nakhl/naxiyl*) and of the **fresh fruit** through other vocabulary: `Talo` (spathe, 6:99, 26:148, 50:10), `ruTab` (fresh date, 19:25, hapax), and `qinowaAn` (hanging clusters, 6:99, hapax-pair "dāniya"). "Dry dates" (*tamr*) as a lexeme is absent; the Qur'an's date is always either the tree or the just-picked fruit.

### 1.2 Zaytūn — olive (ROOT: zyt)

Seven stem tokens across two lemmas (`z~ayotuwn` collective, `zayot` the oil, `zayotuwnap` single tree):

- 6:99:28, 6:141:12, 16:11:5, 24:35:21, 24:35:27 (`zayot` — "its oil"), 80:29:1, 95:1:2.

The olive is paired with the date-palm in every agricultural-sign list (6:99, 6:141, 16:11, 80:29), and it stands alone in two theologically heavy passages: the Light Verse (24:35) and the opening oath of Sūrat at-Tīn (95:1). In 24:35 the olive is called `$ajarap mubaArakap` ("a blessed tree") and `laA $aroqiy~ap w-laA garobiy~ap` — "neither of the east nor of the west" — the single most geographically dense line about any plant in the Qur'an. See §2.

### 1.3 Tīn — fig (ROOT: tyn)

A **single** stem token in the whole Qur'an: 95:1:1 `t~iyni`. The fig is hapax as a noun. Every exegetical weight of the pairing "al-tīn wa'l-zaytūn" rests on this one token.

### 1.4 ʿInab — grape (ROOT: Enb)

Eleven stem tokens (two lemmas: `Einab` sing., `>aEonaAb` pl.): 2:266:9, 6:99:27, 13:4:7, 16:11:7, 16:67:4, 17:91:7, 18:32:9, 23:19:7, 36:34:6, 78:32:2, 80:28:1.

Grapes pattern with palms in **nine** of their eleven occurrences (all except 78:32 and 80:28). The bond is so tight that "palms and grapes" functions as a fixed formula of cultivated abundance (especially 16:11, 23:19, 36:34, 17:91, 18:32, 13:4, 6:99). The pair parallels the olive-and-palm pair in the same list-verses: palm-grape-olive-pomegranate recurs as a four-plant "creation-sign block" (6:99, 6:141, 16:11). Grape alone (not paired with palm) appears only in rhetorical compressions: 80:28 (`EinabFA`, inside the food-sign micro-catalogue) and 78:32 (`HadaA}iqa w->aEonaAbFA` — "gardens and grapes" in the Naba' paradise-description).

### 1.5 Rummān — pomegranate (ROOT: rmn)

Three stem tokens: 6:99:29, 6:141:13, 55:68:4. The first two are in the creation-sign quartet (palm + grape + olive + pomegranate) with the qualifier `mu$tabihan wa-gayra muta$a`bih` ("similar yet dissimilar") — a botanical observation about varieties. The third is in Paradise's "lower" garden of Ar-Raḥmān (55:68) paired with palm: `fiyhimaA faAkihap w-naxolN w-rum~aAnN`. Pomegranate is the **only** named fruit that appears both as earthly sign and as paradisiacal provision with the identical lexeme — olive does not explicitly recur in the afterlife lists, grape is replaced by the more generic `faAkihap`, and figs never re-enter.

### 1.6 Ṭalḥ — banana / acacia (ROOT: TlH)

**Hapax.** Single token at 56:29:1 `TaloHK`, inside the right-hand companions' paradise: `w-TaloHK man[DuwdK` ("and ṭalḥ piled up / layered"). The semantic range in classical lexicography is either the thornless desert acacia (Ṭ. Ṭabarī) or the banana (al-Ḥasan, Ibn ʿAbbās in one tradition). The Qur'anic context is decisive only for the modifier *manḍūd* ("stacked, tier-on-tier"), which fits clustered banana fronds far better than an acacia; on the other hand the pairing with `sidor maxoDuwd` ("thornless lote-tree") in the previous ayah suggests both trees are **de-defamiliarised desert trees** — the two iconic thorny plants of the Ḥijāz (lote and acacia) re-imagined without thorns and with abundance. Given the audience, that reading has stronger internal logic.

### 1.7 Sidr — lote-tree (ROOT: sdr)

Four stem tokens, two lemmas: `sidor` (masc. collective) and `sidorap` (fem. sing.):

- 34:16:15 `sidor` — earthly punishment (Sabaʾ's degraded gardens)
- 53:14:2 `sidorap` — Sidrat al-Muntahā
- 53:16:3 `sidorap` — "when there enveloped the lote-tree what enveloped it"
- 56:28:2 `sidor` — paradise of the right-hand companions, `maxoDuwd` (thornless)

The sidr is the Qur'an's richest cosmic tree. It occupies **all three** theological zones: earthly punishment (34:16, stunted and few), paradise (56:28, thornless and glorified), and cosmic boundary (53:14–16, the terminus of the Prophet's ascent). See §5.

### 1.8 Mann — manna (ROOT: mnn, noun sense only)

Three stem tokens in the "manna" botanical sense: 2:57:6, 7:160:31, 20:80:13. All three pair it with `salwā`. The root `mnn` has many unrelated occurrences meaning "favour, bestow, reproach" (verbal `man~a`, nominal `man~` in those senses) — the plant-food sense is *formally* the same noun but the three listed here are all accusative direct objects of `>anozalo` ("we sent down") or `naz~alo`. Manna in the Qur'an is food **descended from heaven**, never grown; it is a *botanical* lexeme only in the loose Arabian-lexicographic sense (later Muslim naturalists identified it with a taʾmarisk exudate or a sugary lichen). The Qur'an does not describe it.

### 1.9 Salwā — quail (ROOT: slw)

Three tokens, all paired with *mann*: 2:57:7, 7:160:32, 20:80:14. Included here because the complaint of Q 2:61 contrasts this heavenly ration against the five earthly vegetables. Note that *salwā* is an animal, not a plant; its root `slw` also carries the sense "consolation" — so lexically "the consoler" is what descends alongside the manna.

### 1.10 The Q 2:61 five

All five vegetable nouns are **hapaxes** in the Qur'anic corpus:

- `baqol` (herbs/greens) — 2:61:18, root `bql`.
- `qiv~aA^}` (cucumbers) — 2:61:19, root `qvA` (irregular; Dukes tags as `qvA`).
- `fuwm` (garlic, some say wheat) — 2:61:20, root `fwm`.
- `Eadas` (lentils) — 2:61:21, root `Eds`.
- `baSal` (onions) — 2:61:22, root `bSl`.

Five unique roots, five hapaxes, one verse. See §4.

### 1.11 Khamṭ — bitter plant (ROOT: xmT)

**Hapax.** 34:16:11, `>ukulK xamoTK` — "fruit of khamṭ" — grammatically an adjective `xamoT` ("bitter, acrid") modifying `>ukul` ("edible produce"). It describes the *replacement* produce given to Sabaʾ when their dam burst; paired with `>avol` (tamarisk — *also* hapax, root `Avl`) and `$ayo'in min sidor qaliyl` ("a tiny amount of lote"). See §3.

### 1.12 Shajar — tree (ROOT: $jr)

Twenty-six stem tokens of the generic "tree," about evenly split between `$ajar` (collective, masc.) and `$ajarap` (individual tree, fem.). Highlights relevant to this inventory:

- Creation signs: 16:10 (trees from rain), 16:68 (bees nest in trees), 27:60, 55:6.
- Eden tree: 2:35, 7:19, 7:20, 7:22 (×2), 20:120 (the forbidden `$ajarap`).
- Cursed tree (`$ajarap mal`Eu.nap`): 17:60.
- Zaqqūm tree (`$ajarap z~aq~uwm`): 37:62, 44:43, 56:52.
- Blessed olive tree (24:35), Sinai-oil tree (23:20), Moses' burning tree (28:30).
- Fuel for Paradise / Hell rhetoric: 36:80 (the green tree from which fire is kindled).
- Trees in judgement: 22:18 (all trees prostrate), 31:27 (if all trees were pens), 48:18 (the Ridwān tree of the bayʿa), 56:72 (whose tree made it burn?).

The fem. `$ajarap` is used whenever the tree is marked/singular/iconic (Eden, Zaqqūm, Sinai olive, Mūsā's bush). The masc. collective `$ajar` is used for forests/rain-fed growth. This grammatical toggle is consistent.

### 1.13 Zaqqūm — hell-tree (ROOT: zqm)

Three tokens (tagged `PN` — proper noun): 37:62:6, 44:43:3, 56:52:5. Dukes analyses it as a proper name; the other translation would be a common noun meaning a bitter thorny desert plant (identified with the Tihāma's *Euphorbia abyssinica* or a kind of *Tamarix*). As proper noun, the lexeme is Qur'anic coinage. See §3.

### 1.14 ʿUṣf — chaff / husk (ROOT: ESf)

Eight tokens, two with the specifically plant-material sense (`EaSof`): 55:12 (the grain "with its chaff") and 105:5 (the People of the Elephant turned "like eaten chaff"). The other six tokens are the homograph for "storm wind" (`EaASif`, `Ea`Sifa`t`). Plant-ʿuṣf is therefore two-token: a paradisiacal token (55:12) and an annihilation-metaphor (105:5).

### 1.15 Abb — grass / fodder (ROOT: Abb)

**Hapax.** 80:31:2, `faAkihapF w->ab~FA` — "and fruit and *abb*." The lemma is `>ab~`, root `Abb`. The classical commentators disagreed openly: Abū Bakr reportedly refused to speculate on its meaning. Context is unambiguous structural: the food-list of ʿAbasa (80:27–32) moves from staple seed → grapes → olive/palm → gardens → fruit + abb → livestock fodder, ending in `mataAEFA la-kum wa-li->anoEa`mi-kum` ("provision for you and for your livestock"). The word *abb* is almost certainly pastoral fodder — wild herbage eaten by grazing animals — on discourse-structural grounds alone. Its hapax status (and early Companions' refusal to gloss it) is a marker of the Qur'an's indifference to botanical taxonomy: it lists what suffices, not what classifies.

### 1.16 Lexemes adjacent to the inventory

For completeness, the Qur'an's agricultural vocabulary also uses: `zaroE` (cultivated cereal, 13 tokens), `Hab~` (grain), `vamar`/`vamara`t (fruit, generic), `jan~ap`/`jan~a`t` (garden), `nabaAt`/`>anobata` (to sprout), `faAkihap`/`faAkihuwn` (fruit), `HadaA}iq` (enclosed orchards, 27:60, 78:32, 80:30), `qaDob` (fresh fodder / green herbs, hapax 80:28), `rayHaAn` (fragrant herb, 55:12 and 56:89 `rawoH`). Most of these are *generic* plant vocabulary and not indexed per-plant. The named-plant list above is, by design, a short list.

---

## 2. Q 95:1 "wa-l-tīn wa-l-zaytūn" — the oath of the fig and the olive

Surah at-Tīn opens with a four-part oath: the fig and the olive, Mt Sinai (`Tuwr siyniyn`), and the Safe City (`haa`*aA al-balad al->amiyn`). Then the *muqsam ʿalayhi* in v.4: "We indeed created the human in the finest stature."

From the morphology alone:

- `t~iyn` is the only token of the root `tyn` in the Qur'an (hapax).
- `z~ayotuwn` here (95:1:2) is the **seventh and last** olive-token in revelation, counting by mushaf order; its other appearances are 6:99, 6:141, 16:11, 24:35 (blessed tree), 24:35 (its oil, `zayot`), 80:29. The olive is thus never "new" at 95:1 — it arrives laden with prior sign-value.
- The fig has **no prior appearance**. 95:1 is its only Qur'anic moment.

This mismatch sits under the oath. One plant is a theological capstone (the blessed tree of the Light Verse, the olive-and-palm formula of creation signs), the other is an *unheralded* ally. Why pair them?

Three internal hypotheses:

1. **Geographic pairing.** The fig grows naturally in the Levant/Palestine, the olive throughout Sinai and the Levant. With v.2 `Tuwr siyniyn` (Sinai) and v.3 the Safe City (Makka), the four oaths trace an arc: Palestine/Jerusalem (fig + olive) → Sinai (olive country + Moses' mountain) → Makka (the sanctuary). That is the prophetic map — Isa, Musa, Muhammad — implied in three landscapes. Classical commentary (Ibn Kathīr, Rāzī) endorses this.
2. **Thamar-bearer pairing.** The two *primary* cultivated fruits of Mediterranean agriculture. Paired with Sinai's *oil* tree (olive again) and Makka's *desert* security, the oath reaches across climate zones.
3. **Semantic progression from vegetation to revelation to human nobility.** Vv.1–3 name *places of revelation*; v.4 names the *subject* of revelation (humankind in best form); v.5 reverses it (`>asofala saAfiliyn` — lowest of the low). The botanical lexemes thus serve as *indexical witnesses* of sacred landscape.

The morphological fact that `tīn` is hapax is not incidental — it forces the fig to function as an *oath-particular*, a unique signifier rather than a recurring motif. Parallel structure: `Tuwr siyniyn` is also a *particular* mountain (Sinai), not a general one; `al-balad al->amiyn` is a particular city (Makka). The four oaths are four *unique* deictics.

---

## 3. Paradise versus Hell plants

Three botanical tokens in paradise and one in hell:

**Paradise — Sūrat al-Wāqiʿa 56:28–29 (right-hand companions):**
- `sidorK maxoDuwdK` — thornless lote
- `TaloHK man[DuwdK` — banana/acacia piled in tiers

**Paradise — Ar-Raḥmān 55:68 (second garden):**
- `faAkihapN w-naxolN w-rum~aAnN` — fruit, palms, and pomegranates

**Paradise — 24:35's emblem:**
- `$ajarap mubaArakap zayotuwnap` — a blessed olive tree, neither eastern nor western

**Hell — Sūrat aṣ-Ṣāffāt 37:62–68, ad-Dukhān 44:43–46, al-Wāqiʿa 56:52:**
- `$ajarap z~aq~uwm` — the tree of Zaqqūm; root `zqm` (3 tokens total); described as "growing from the bottom of Jaḥīm" (37:64), its blossom `ka->an~ahu ru'uws al-$ayaA.Tiyn` ("as if heads of devils," 37:65), its fruit scalding, eaten by the damned until bellies are full then mixed with boiling water.

**Earthly-punishment paradise — Q 34:15–17 (Sabaʾ):**
- Two flourishing gardens "on the right and the left" → replaced with `jan~atayn ðawaAtayo >ukulK xamoTK w->avolK w-$ayo'K min sidor qaliyl` — two gardens of bitter fruit (*khamṭ*), tamarisk (*athl*), and *a tiny bit* of lote. This is the Qur'an's one explicit **inversion** of an agricultural paradise into a degraded semi-wilderness: three plants, all hapaxes or near-hapaxes, mark the replacement.

The key contrast is structural:

- Paradise plants are **named iconic species** (sidr, ṭalḥ, nakhl, rummān, zaytūn) and they come with **attributes of subtraction** — the thorns are removed (56:28 `maxoDuwd`), the fruits are neither cut off nor forbidden (56:33 `laA maqoTuwEap wa-laA mamonuwEap`), the shade is extended (56:30), the tree neither east nor west (24:35).
- The hell-plant is **unique** (zaqqūm, a Qur'anic coinage as `PN`), **growing from below** (37:64), **producing demonic fruit**. Its food is involuntary — the damned eat and **fill** (`ma`li'uwn`) their bellies (37:66, 56:53).
- The Sabaʾ gardens are **diminished** — no thorns removed, thorns multiplied; no substitute of better, a substitute of worse — and the lote (sidr) that in paradise is thornless is here `qaliyl` ("little, sparse").

The grammatical toggle `$ajar`/`$ajarap` also tracks this: every hell- or forbidden-tree is the marked feminine singular `$ajarap` (Zaqqūm 37:62, 44:43; Eden 2:35, 7:19–22, 20:120; cursed tree 17:60); the blessed olive 24:35 is also `$ajarap`. The pattern: when the tree is named and morally weighted, it is *the* tree (sing. fem.); when it is a generic ecological backdrop it is `$ajar` (masc. coll.).

---

## 4. Q 2:61 — the seven/five-plant complaint

The verse narrates Israelites under Mūsā demanding earthly produce in place of manna + salwā. The morphology gives exactly **five** plant nouns in this ayah: `baqol` (18), `qiv~aA^}` (19), `fuwm` (20), `Eadas` (21), `baSal` (22). All five are **hapax stems** in the entire Qur'an (one and only one `STEM` token each).

The "seven" framing in the user's brief counts five plants + the two heavenly provisions (*mann*, *salwā*) named in the immediate prior context (2:57). Together those seven form the full contrast: 2 heavenly (mann, salwā) vs. 5 earthly (baql, qiththāʾ, fūm, ʿadas, baṣal). The rhetorical force is **2 vs. 5**, not a flat list of seven equal items.

Traditional commentary (Ṭabarī, Qurṭubī) disagreed on *fūm*: either garlic (Ḥasan al-Baṣrī, Ibn ʿAbbās in one riwāya) or wheat (Ibn Masʿūd reportedly reading `vūm` with thāʾ). The morphology gives us `fuwm` with fāʾ only; there is no alternative reading in the Dukes corpus. Semantically, a complaint about losing garlic reads like low hedonic loss; a complaint about losing *wheat* reads like civilizational loss (the absence of a staple grain). The verse's rhetoric — calling these foods `>adnaY` ("lower") and the heavenly ration `xayor` ("better") — cuts either way.

A structural observation: the five plants are listed in a quasi-ascending aromatic intensity — `baql` (mild herbs) → `qiththāʾ` (cool cucumber) → `fūm` (pungent garlic/wheat) → `ʿadas` (earthy lentil) → `baṣal` (sharp onion). Phonetically the list moves from soft dentals to emphatic sibilants, climaxing in `baṣali-hā` (the ṣād bites). The reply in the second half of the verse uses the contrastive `>adonaY` / `xayor` pair, with the verb `tasotabodiluwn` ("you exchange") placing the five earthly nouns into a single transactional category against the two heavenly ones.

The exchange is punished: `Duribato Ealayohim al-ðil~ap wa-l-masokanap` ("humiliation and destitution were stamped on them"). The five hapax plants thus enter the Qur'an **only to be renounced** — they are never named again. The Qur'an will not repeat their names even to pity the Israelites.

---

## 5. Sidrat al-Muntahā — the boundary-tree (Q 53:14)

Sūrat an-Najm 53:13–18 describes the Prophet's second vision:

> 13 — And indeed he saw Him in another descent
> 14 — **at the sidrat al-muntahā (the Lote-Tree of the Boundary)**
> 15 — near it is the Garden of Refuge (`jan~apu al-ma>owaY`)
> 16 — when there enveloped the sidrah what enveloped
> 17 — the sight did not swerve, nor did it overstep
> 18 — he saw, indeed, of his Lord's greatest signs.

Four morphological facts:

1. The lexeme `sidorap` (53:14:2, 53:16:3) is the feminine-singular form of the masculine collective `sidor`. This is the grammatical shift from "lote-trees" to "the lote-tree" — a specific, individuated tree.
2. `al-muntahā` derives from root `nhy` ("to reach an end, a terminus, a prohibition"). It is the same root as `nahaY` ("he forbade"). The tree is the end-point of motion **and** the boundary of prohibition — you can approach it, you cannot pass it.
3. The repeated verb `yagošaY` ("envelops") in 53:16 is deliberately un-specific: the Qur'an says "when there enveloped the lote-tree what enveloped [it]." The referent is left blank. Commentators propose golden moths, angels, divine light; the text refuses the identification.
4. Cross-reference: the hell-tree Zaqqūm `taxoruj fiY >aSoli al-jaHiym` ("grows from the root of the Jaḥīm," 37:64). The contrast pattern:

| Sidrat al-Muntahā | Shajarat al-Zaqqūm |
|---|---|
| At the highest cosmic boundary | At the lowest cosmic root |
| Beside the Garden of Refuge | At the base of the Fire |
| Enveloped by divine light (unspecified) | Its fruit heads "like devils" |
| Marks where motion ends | Marks where consumption begins |
| Prophetic seeing does not swerve | Damned filling bellies |
| `sidorap` (F.S., individuated) | `$ajarap` (F.S., individuated) |
| Lote — thorny tree made paradisiacal | Coined name (unidentified species) |

The two trees are the Qur'an's **cosmic axis**. Each marks a terminal — the sidr is the terminus of ascent (the *upper* limit where even Gabriel's wings stop, per the ḥadīth tradition), the zaqqūm is the terminus of descent (the *lower* root of Gehenna). Between them sits human agricultural life, which in the Qur'an is itself an intermediate state (`matāʿ` in 80:32, `rizq` in 50:11).

The identification of the sidr with the lote-tree is not incidental: the lote (*Ziziphus spina-christi*) is the quintessential Arabian desert tree — gnarled, thorny, drought-surviving, fruit-bearing. The Qur'an takes this ordinary desert survivor and places it at the cosmic summit. The theological work is a *de-familiarisation of the mundane*: the same sidr that peasants know from the wadi appears at heaven's edge.

---

## 6. Sūrat an-Naḥl agriculture (Surah 16)

Surah 16 is named after the bee (`al-naḥl`, 16:68), and its first third (vv. 5–18) is a sustained agricultural catalogue. Plant-relevant verses:

- **16:10** — "He it is who sent down water from the sky — for you a drink from it, and from it **tree** (`$ajar`) on which you pasture [livestock]." Rain → trees → livestock → humans.
- **16:11** — "He causes to grow for you by it the **crop** (`zaroE`), **olive** (`z~ayotuwn`), **date-palms** (`n~axiyl`), **grapes** (`>aEonaAb`), and of every **fruit** (`vamaraAt`). Indeed, in that is a sign for a people who reflect." Five plant-kind terms in a single ayah.
- **16:67** — "And from the **fruits of date-palms and grapes** you derive intoxicant (`sakar`) and good sustenance (`rizq ḥasan`). Indeed, in that is a sign for a people who understand." The only Qur'anic mention of `sakar` (fermented date/grape juice), placed *before* the later prohibition of khamr — the chronological order matters.
- **16:68–69** — "Your Lord inspired the bee: take from the mountains houses, and from the **tree** (`$ajar`) and from what they trellis. Then eat from every fruit and follow your Lord's paths made easy." Tree → bee → honey. The bee becomes a botanist.
- **16:80** — Livestock skins as tents, wool-hair-fur as furnishings. Closes the agricultural block with the animal by-products.

Four stylistic observations:

1. Each sign-ayah in this run ends with a ritual tag: `laAayap li-qawom yatafak~aruwn` (16:11, 69), `laAayap li-qawom yaEoqiluwn` (16:67), `laAayap li-qawom ya*~ak~aruwn` (16:13), `laAayap li-qawom yaEolamuwn` (16:65). The verbs ascend: *reflect → understand → remember → know*. The plants serve a cognitive ladder.
2. The plant quartet of 16:11 (olive-palm-grape + fruit) is the **exact same quartet** as 6:99 and 6:141 minus pomegranate. These three ayāt form a liturgical formula, a "creation-sign song" the Qur'an returns to thrice.
3. Surah 16 introduces the grape not just as food but as the *raw material of inebriation*: `sakar`. The morphology tags `sakar` as a noun (root `skr`), placing the cognitive shift from intoxicant-as-permitted to intoxicant-as-forbidden (5:90) as one of the Qur'an's most visible chronological developments.
4. The surah closes its plant material at 16:69 with the bee's honey as "healing for people" (`fiyhi $ifaA' li-l-naAs`). The arc is therefore: rain → tree/crop → wine → honey-as-healing. The beverage-pair *khamr vs. ʿasal* maps inversely onto *fitnah vs. shifāʾ*.

Additionally, the Qur'an's most agricultural surahs by density (plant-tokens per ayah) are, in order: **16 An-Naḥl** (7 plant stems in 128 ayāt); **6 al-Anʿām** (including 6:99 and 6:141 the densest two verses, 5 species each); **55 Ar-Raḥmān**; **56 al-Wāqiʿa**; **80 ʿAbasa** (the food-list 80:24–32). Ar-Raḥmān and al-Wāqiʿa cluster their plant vocabulary in paradise scenes; An-Naḥl and al-Anʿām cluster theirs in creation-sign didactics; ʿAbasa clusters its in the food-sign sequence addressed to the one who neglected the blind man — plants as reproach to ingratitude.

---

## 7. Summary of patterns

- **Hapax concentration.** Of the Qur'an's named plants, eight are hapax: tīn, ṭalḥ, khamṭ, abb, baql, qiththāʾ, fūm, ʿadas, baṣal (nine if we include the tamarisk `athl`). The botanical lexicon is front-loaded with single-use items — the Qur'an speaks plant-names in whispers, not inventories.
- **Recurrent core.** Only four plant lexemes recur heavily: palm (20), tree-generic (26), grape (11), olive (7). Pomegranate (3), sidr (4), zaqqūm (3) form a middle layer.
- **Palm-grape formula.** These two are bonded in nine of grape's eleven appearances, making "nakhl wa-aʿnāb" the Qur'an's most frequent agricultural dyad.
- **Olive-tree cosmology.** The olive appears in creation signs and then graduates to the Light Verse (24:35) as the emblem of universal (neither east nor west) divine light.
- **Sidr as axial.** Only the lote-tree appears at all three tiers — earthly degraded (34:16), paradisiacal thornless (56:28), and cosmic-terminal (53:14).
- **Zaqqūm as inversion.** The only named *hell-plant*, grammatically treated as a proper noun, built as the structural antipode of the sidrat al-muntahā.
- **The Q 2:61 five** function as a rhetorical floor: named once, never again, and only to be rejected.
- **Paradise vocabulary subtracts rather than adds.** Thornless, uncut, unforbidden, shaded — the paradise trees are ordinary Arabian trees with their harshness removed. Hell adds what the earth already lacks (pitch, boiling, devil-shaped fruit).

The Qur'an's botany is not a taxonomy. It is a **moral geography** in which every named plant indexes a theological stance: gratitude owed (the sign-plants of 6:99, 16:11), memory owed (the rejected five of 2:61), prohibition respected (the sidrat al-muntahā), or consequence endured (the zaqqūm of 37:62, the palm-stumps of 69:7).

---

**Data appendix (counts verified against Dukes v0.4 morphology):**
nxl 20 / zyt 7 / tyn 1 / Enb 11 / rmn 3 / TlH 1 / sdr 4 / mnn(plant) 3 / slw 3 / bql 1 / qvA 1 / fwm 1 / Eds 1 / bSl 1 / xmT 1 / zqm 3 / ESf(plant) 2 / Abb 1 / $jr 26.
