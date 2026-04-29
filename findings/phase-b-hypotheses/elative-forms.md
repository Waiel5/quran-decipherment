# Elative / Comparative Forms (afʿal pattern) in the Quran

**Phase B hypothesis run.** Extraction of the Arabic elative pattern `ʾafʿal` from the Leeds Quranic Corpus (morphology v0.4), with structural analysis of comparative (`afʿal … min`), superlative (`afʿal + idafa` / `afʿal + definite article`), divine-attribute, and formulaic usage.

## 1. Background: what is afʿal?

In Arabic morphology the pattern **ʾafʿal** (Buckwalter: `>aCCaC` / `>aCoCaC`) is a single template that encodes several semantic functions: (a) **elative** — "more X" (comparative with `min`, "than") or "most X" (superlative with article/idafa); (b) **defect and color** adjectives of the same shape (`aḥmar` red, `aʿmā` blind, `abyaḍ` white); (c) certain primitive adjectives and lexicalised divine attributes (`al-Aʿlā` "the Most High", `al-Akram` "the Most Generous"). In the Qur'an the pattern occupies a restricted but semantically dense slot: the morphology never marks gender in the masculine singular elative (it is diptote), and comparative complements almost always surface as a `min`-phrase.

The Leeds corpus does not tag afʿal as a distinct category. We therefore extracted all stems whose **lemma** (LEM field) begins with Buckwalter `>a` and whose **root** (ROOT) is a normal triliteral that does *not* begin with an initial alif radical — a simple heuristic that eliminates false positives such as `>aroD` (earth, root `ArD`), `>amor` (command, root `Amr`), `>ahol` (family, root `Ahl`), and `>aliym` (painful, root `Alm`), in all of which the `>a` is part of the root rather than the augment of the ʾafʿal template.

## 2. Extraction results

From 128 219 morphological segments (the complete Quranic Arabic Corpus), **414 tokens** across **≈ 60 lemmas** match the ʾafʿal template. The top of the list is dominated by a small number of very frequent elatives:

| Lemma (Buckwalter) | Transliteration | Root | Count | Gloss |
|---|---|---|---|---|
| `>akovar` | akthar | kthr | 80 | more/most (numerous) |
| `>aEolam` | aʿlam | ʿlm | 49 | more/most knowing |
| `>aHosan` | aḥsan | ḥsn | 36 | better/best |
| `>a$ad~` | ashadd | šdd | 31 | more severe |
| `>akobar` | akbar | kbr | 24 | greater/greatest |
| `>aqorab` | aqrab | qrb | 19 | nearer/nearest |
| `>aZolam` | aẓlam | ẓlm | 16 | more unjust |
| `>aHaq~` | aḥaqq | ḥqq | 10 | more worthy |
| `>aDal~` | aḍall | ḍll | 9 | more misguided |
| `>awolaY` | awlā | wly | 11 | closer/more deserving |
| `>aEolaY` | aʿlā | ʿlw | 9 | the Most High |
| `>aroHam` | arḥam | rḥm | 4 | most merciful |
| `>aEoZam` | aʿẓam | ʿẓm | 3 | greater/greatest |
| `>akoram` | akram | krm | 2 | most noble / `al-Akram` |

The complete tail of hapax and di-token lemmas — `>aDoEaf` (weaker), `>afoSaH` (more eloquent), `>aHoraS` (more covetous), `>ankar` (most abominable), `>abotar` ("cut-off", 108:3), `>ajodar` (more likely), `>alad~` (most contentious), etc. — demonstrates that the corpus uses ʾafʿal productively, not only as a frozen lexicalised set.

Two special subclasses are visible in the list and should be excluded from a strictly "elative" count because their morphological afʿāl shape is actually the **broken plural** of a singular noun: `>andaAd` (andād, rivals, sg. nidd, 6×), `>anfaAl` (anfāl, spoils, 2×), `>ankaAl` (ankāl, fetters, 1×). These pluralise on the same skeleton as the elative but are morphosyntactically nominal; we list them here for completeness but exclude them from the comparative counts below.

Similarly the **color/defect** afʿal adjectives — `>aboyaD` (white, 8×), `>asowad` (black, 1×), `>axoDar` (green, 1×), `>aboraS` (leprous, 2×), `>abokam` (mute, 6×), `>aEoraj` (lame, 2×), `>aSam~` (deaf, 12×) — share the morphological template but not the elative semantics (they are primary adjectives of defect or color, not comparatives). These 30+ tokens deserve their own cluster: they group in verses describing disability (Q 24:61), Jewish-covenant miracles (Mūsā's white hand — `bayoDaA^'a` at Q 20:22, 27:12, 28:32; the three occurrences all involve the same "insert hand into bosom and withdraw it white" formula), and Judgement-Day infirmities (`>aZolam` often paired with hearts that are deaf/dumb/blind).

## 3. Divine attributes in afʿal

Only two divine attributes in the Qur'an surface as pure afʿal elatives:

### 3.1 al-Aʿlā — "the Most High"

The lemma `>aEolaY` (root ʿ-l-w) occurs **9 times**, distributed as follows:

- **Q 16:60, 30:27** — `li-llāhi l-mathalu l-aʿlā` ("to Allah belongs the highest parable").
- **Q 20:68** — addressed to Mūsā: `innaka anta l-aʿlā` ("truly you are the uppermost"). The Leeds parser tags this token as a noun (N), but the context is agonistic/competitive ("you will overcome").
- **Q 37:8** — `wa-yuqdhafūna min kulli jānib … min al-mala'i l-aʿlā` ("they are pelted from every side … from the Highest Assembly"). Here al-aʿlā qualifies a *place*, not the deity.
- **Q 38:69** — the same phrase `al-mala'i l-aʿlā`.
- **Q 53:7** — `bi-l-ufuqi l-aʿlā` ("on the highest horizon") — referring to the Prophet's vision, not directly a divine attribute.
- **Q 79:24** — Pharaoh's blasphemy: `anā rabbukum al-aʿlā` ("I am your lord, the most high"). Tagged ADJ. A **usurpation** of the attribute.
- **Q 87:1** — `sabbiḥi sma rabbika l-aʿlā` ("glorify the name of your Lord, the Most High"). The only place it directly qualifies `rabb` as an attribute in an imperative formula.
- **Q 92:20** — `illā btigāʾa wajhi rabbihi l-aʿlā` ("except seeking the face of his Lord, the Most High").

**Structural observation.** Of the 9 tokens, only 3 (87:1, 92:20, 79:24) are unambiguous "Most-High" divine attributes — and one of those (79:24) is Pharaoh's claim, a *negated* theological statement. The phrase `al-mala' al-aʿlā` ("the Highest Assembly", 37:8, 38:69) and `al-mathal al-aʿlā` ("the highest parable", 16:60, 30:27) are fixed expressions with `al-aʿlā` as a qualifier rather than a bare epithet. So the canonical divine-name reading of Surah 87's title rests on just two verses where `al-aʿlā` attaches to `rabb` directly (87:1, 92:20).

### 3.2 al-Akram — "the Most Noble/Generous"

The lemma `>akoram` occurs **2 times as elative** (plus 2 verbal stems of form IV `akrama`):

- **Q 49:13** — `inna akramakum ʿinda llāhi atqākum` ("indeed the most honoured of you before Allah is the most god-conscious among you"). Crucial: here `akram` is **not** a divine attribute but a predicate about human ranking. The semantic pair is with `atqā` (most pious, also afʿal) in the same verse — one of the very few places the Qur'an doubles up on elatives in a single ratio-statement.
- **Q 96:3** — `iqraʾ wa-rabbuka l-akram` ("Read — and your Lord is the Most Noble"). This is a divine attribute in exactly the same syntactic frame as `sabbiḥi sma rabbika l-aʿlā` (Q 87:1) — imperative V + `rabbuka + al-[afʿal]`. The parallel is exact and can hardly be accidental; Surah 96 (first revelation) and Surah 87 both open with an imperative addressed to the Prophet and a divine afʿal-attribute of the Lord. These are the **only two cases** in the Qur'an where an afʿal elative is lexicalised with the article and applied to `rabb` with the copula omitted.

## 4. The takbīr formula — "Allāhu akbar"

The classical takbīr — the utterance `Allāhu akbar` that frames the five daily prayers, the two ʿīds and hundreds of ritual moments — does *not* occur in the Qur'an as a frozen liturgical formula. The elative `akbar` (`>akobar`) appears 24 times, but the direct sequence `Allāh(u) + akbar(u)` as an adjacent two-word clause occurs **only three times**, and in each case the semantics is "Allāh is greater/mightier [than X]", not an independent takbīr:

- **Q 9:72** — `wa-riḍwānun min allāhi akbaru` — "and pleasure from Allāh is greater [than that]". Here the subject is "pleasure" not "Allāh"; the morphological adjacency is coincidental.
- **Q 29:45** — `wa-la-dhikru llāhi akbaru` — "and the remembrance of Allāh is greater [than all else]". This is the **closest Qur'ānic analogue to the takbīr**, but grammatically `dhikr` is subject, with a genitive `llāh`.
- **Q 40:10** — `la-maqtu llāhi akbaru min maqtikum anfusakum` — "the hatred of Allāh is greater than your own self-hatred". Again `maqt` (hatred) is subject.

**Finding.** The ritual takbīr is a **post-Qur'ānic lexicalisation**. The Qur'ān supplies the raw components (the divine name and the elative `akbar`) and even juxtaposes them three times, but never under a matrix in which Allāh is the nominative subject of a bare predicate `akbar`. The liturgical formula crystallised later (it is attested already in the earliest ḥadīth layer as the utterance for ṣalāh and jihād), drawing on these verses as a semantic authorisation.

The 24 occurrences of `akbar` split roughly as follows by semantic frame:

- **Comparative with `min`** (comparative): 12× (e.g., Q 2:217 `al-fitnatu akbaru min al-qatl`, Q 17:21 `akbaru darajātin`, Q 40:57 `la-khalqu s-samāwāti wa-l-arḍi akbaru min khalqi n-nāsi`).
- **Superlative via ḥadath-construction** (afʿal in an eschatological superlative): Q 21:103 `al-fazaʿu l-akbar` (the greatest terror), Q 88:24 `al-ʿadhāba l-akbar` (the greatest punishment), Q 87:12 and 39:26 `ʿadhābu l-ākhirati akbar` — the *Hereafter-punishment-greater-than-worldly* motif (6× across Q 13:34, 32:21, 39:26, 68:33, 88:24, and implicitly 87:13).
- **Formulaic repetition at Q 17:21**: `akbaru darajātin wa-akbaru tafḍīlan` — the only place `akbar` is doubled in a single clause.

## 5. "akbar al-kabāʾir" — the greatest of major sins

The phrase "the greatest of the major sins" — frequent in classical jurisprudence — **does not appear verbatim** in the Qur'an. The ingredients appear in close proximity:

- `kabāʾir` (the broken plural of `kabīra`, "major sin") occurs at **Q 4:31** (`in tajtanibū kabāʾira mā tunhawna ʿanhu`), **Q 42:37** (`wa-lladhīna yajtanibūna kabāʾira l-ithmi wa-l-fawāḥisha`), and **Q 53:32** (`alladhīna yajtanibūna kabāʾira l-ithmi wa-l-fawāḥisha illā l-lamam`) — three verses, all in a grammatical frame `yajtanibū/yajtanibūna kabāʾir(a)`. Of these three, two (42:37 and 53:32) share the exact lexical chain `kabāʾira l-ithmi wa-l-fawāḥisha`.
- `akbar` never appears in the Qur'an in an idafa construction with `al-kabāʾir`. The idiom `akbaru l-kabāʾir` is a **ḥadīth-derived formula** (famously the tradition on the three greatest sins: shirk, ʿuqūq al-wālidayn, and false testimony / false oath).

## 6. aḥsan — "better/best" constructions

The lemma `>aHosan` (root ḥ-s-n, 36×) is the richest afʿal item for studying elative syntax. We found the following recurrent frames:

### 6.1 `man aḥsanu …` — rhetorical "who is better in X than Y?"

This frame appears **four times** and each time delivers a theological slogan:

- **Q 2:138** `wa-man aḥsanu mina llāhi ṣibghatan` — "and who is better than Allāh in [religious] colouring/baptism?" The word `ṣibgha` (baptismal dye) is a hapax at this verse, making the pairing `aḥsan + ṣibgha + min + Allāh` a unique three-word theological trope.
- **Q 4:125** `wa-man aḥsanu dīnan mimman aslama wajhahu lillāhi` — "who is better in religion than he who submits his face to Allāh?"
- **Q 5:50** `wa-man aḥsanu mina llāhi ḥukman li-qawmin yūqinūn` — "who is better than Allāh in judgement for a people who have certainty?"
- **Q 41:33** `wa-man aḥsanu qawlan mimman daʿā ilā llāhi` — "who is better in speech than he who calls to Allāh?"

Note the **parallel template**: `wa-man aḥsanu [X-tamyīz] {mina llāhi / mimman Y}`, where the accusative (tamyīz) X is always the domain of excellence (ṣibgha, dīn, ḥukm, qawl) and the `min`-phrase names the reference point — sometimes Allāh, sometimes a participle-clause describing the ideal believer. This is the Qur'ān's **rhetorical-question-of-superiority** template.

### 6.2 `aḥsana l-qaṣaṣ` — "the best of narrations" (Q 12:3)

In the opening of Sūrat Yūsuf: `naḥnu naquṣṣu ʿalayka aḥsana l-qaṣaṣi bi-mā awḥaynā ilayka hādhā l-qurʾāna`. This is a meta-literary superlative: the Qur'an calling its own narrative mode "the best of narrations". The afʿal + DET + homonym-root noun (`aḥsana + al-qaṣaṣi`, both from q-ṣ-ṣ) also produces phonological figurative doubling — an example of root-play (ishtiqāq) exploiting the elative.

### 6.3 The "instrumental" frame `bi-llatī hiya aḥsan` — "with that which is better"

Five times the Qur'an commands the believer to respond or act using "that which is better": Q 6:152 (with orphans' property), Q 16:125 (in daʿwa), Q 17:34 (again with orphans), Q 23:96 (repel evil with what is better), Q 29:46 (arguing with People of the Book), Q 41:34 (repelling evil with aḥsan). The formula `bi-llatī hiya aḥsanu` is a crystallised ethical instruction. Note that Q 29:46 and 16:125 share exactly this template in the *daʿwa* context.

### 6.4 Q 6:57 note

The hypothesis-brief conjectured "aḥsan al-qāṣiṣīn" at Q 6:57. The corpus shows Q 6:57 ends with `wa-huwa khayru l-fāṣilīn` — "He is the best of deciders" — using `khayr` (not `aḥsan`), from root k-h-y-r, which is semantically an elative but morphologically irregular (fiʿl pattern). The hypothesis was inexact: Qur'ānic superlatives alternate between `khayr`, `aḥsan`, and `akram` depending on semantic domain, and none of the `khayr al-…` idafa constructions at Q 3:54, 7:87, 10:109, 12:64, 21:89, 23:109, 23:118, 6:57, 62:11 use an afʿal morph.

## 7. awlā — elative from walī

The lemma `>awolaY` (root w-l-y, 11 tokens) is the elative of `walī` ("close one, ally, friend"), meaning "closer, more entitled, more deserving". Its distribution reveals a sharp legal-theological focus:

- **Kinship / inheritance**: Q 4:135 `fa-llāhu awlā bihimā` (Allāh is more entitled concerning the two parties); Q 33:6 (*twice*) `an-nabiyyu awlā bi-l-muʾminīna min anfusihim … wa-ulū l-arḥāmi baʿḍuhum awlā bi-baʿḍin fī kitābi llāhi` — the Prophet is closer to the believers than they are to their own selves, and blood-kin are closer to one another in inheritance. The double `awlā` in one verse is unique.
- **Covenant/religion**: Q 3:68 `inna awlā n-nāsi bi-ibrāhīma …` (the most entitled of people to Ibrāhīm are his followers).
- **Threat formula (4×)**: Q 75:34–35 `awlā laka fa-awlā, thumma awlā laka fa-awlā` — the famous fourfold warning. Classical lexicographers debated whether this is elative from wly ("woe-closer-to-you") or an independent interjection `awlā-laka` ("woe!"). The morphology tags it as the same lemma, so the corpus reads it as "[disaster] is closer to you and closer".
- **Q 19:70, 47:20, 8:75**: various idiomatic comparatives.

**Relation to awliyāʾ.** The plural `awliyāʾ` (42 occurrences in the corpus) is *not* an elative — it is the broken plural of `walī` (the positive, not the comparative). The user-brief statement that "awliyāʾ is also afʿal-from-walī" is morphologically precise only at the level of the *template* (afʿilāʾ pattern, a plural shape akin to afʿāl); semantically and syntactically `awliyāʾ` means "close-friends/allies" (not "closer friends"). The Qur'an distinguishes the two sharply: `awlā` (elative, 11×) always takes a complement (`bi-X min Y`), while `awliyāʾ` (plural, 42×) is almost always the object of a negative command (`lā tattakhidhū … awliyāʾ`, 15+ occurrences — "do not take as allies").

## 8. The `afʿal + min` comparative construction

We programmatically detected all cases where an afʿal-lemma token is immediately (or within one word) followed by the preposition `min`. The result: **49 comparative constructions** in the Qur'an (≈ 11.8 % of all afʿal tokens). Distribution by elative:

- `ashadd min` (more severe than): 7× (Q 2:191, 2:200, 9:69, 22:5, 28:78, 30:9, 35:44, 40:21) — the Qur'an's most frequent comparative, typically amplifying tests or punishments.
- `akthar min` (more numerous than): 3× (Q 4:12, 7:102, 18:34).
- `akbar min` (greater than): 5× (Q 2:217, 2:219, 4:153, 40:10, 40:57).
- `aḥsan min` (better than): 3× (Q 2:138, 4:86, 5:50).
- `aqrab min` (closer than): 3× (Q 3:167, 18:24, 22:13).
- `aʿlā min` (higher than): 1× (Q 37:8).
- `awlā min`: 1× (Q 33:6).
- Color/miraculous `bayḍāʾ min` ("white, coming out of"): 4× (the Mūsā hand-miracle, Q 20:22, 27:12, 28:32 + Q 2:187 threshold-of-dawn).
- Hapax comparatives: `afṣaḥ min` (Q 28:34 — Mūsā describing Hārūn, "more eloquent than me"), `aṣdaq min` (Q 4:87, 4:122 — "who is more truthful than Allāh in report/speech"), `asfal min` (Q 4:145, 8:42, 33:10), `aṣghar min` (Q 10:61, 34:3 — "not an atom's weight smaller than that escapes thy Lord's knowledge" — a cosmological comparative).

The comparative frame `aḥsan min`, `aṣdaq min`, `aqrab min` are dominated by a single rhetorical device: **the unanswerable rhetorical question**. `wa-man aṣdaqu mina llāhi qīlan` (Q 4:122), `wa-man aṣdaqu mina llāhi ḥadīthan` (Q 4:87) are *semantically identical* ("who is more truthful than Allāh in speech?") with lexical variation between `qawl`/`ḥadīth` — a near-mutashābih pair.

## 9. Superlative patterns

Two superlative constructions occur with the afʿal template:

1. **`al-` + afʿal** (definite article superlative): `al-aʿlā` (9×, §3.1), `al-akram` (Q 96:3), `al-akbar` in fixed idafa like `al-ʿadhāb al-akbar`, `al-fazaʿ al-akbar` (eschatological epithets), `al-khaliq` ... etc.
2. **`afʿal + idafa`** (elative construct): `akram-u-kum ʿinda llāh` (Q 49:13), `aḥsan-u l-qaṣaṣ` (Q 12:3), `aḥsan-u l-ḥadīth` (Q 39:23 "Allāh has sent down the best of speech — a Book"), `aḥsan-u l-khāliqīn` (Q 23:14, 37:125 — "Blessed be Allāh, the best of creators"). This last pattern — `aḥsan + definite plural` — is particularly loaded theologically (three of the four aḥsan + DET-plural constructions apply to Allāh directly).

## 10. Synthesis and open questions

1. The afʿal template is quantitatively small (≈ 0.3 % of all tokens) but strategically deployed: it carries much of the Qur'an's rhetorical-question machinery (`wa-man aḥsanu / aṣdaqu / aẓlamu min …`) and its divine-attribute compression (`al-Aʿlā`, `al-Akram`).
2. **Pharaonic usurpation pattern.** Pharaoh claims `al-aʿlā` for himself at Q 79:24. The Qur'an reserves this attribute for Allāh at Q 87:1 and 92:20. That one of only three unambiguous `al-aʿlā` divine-attribute tokens is placed on the lips of the arch-tyrant is a deliberate lexical trap: the attribute is shown both in its true form and its counterfeit form within the same scriptural vocabulary.
3. **Surah 87 / Surah 96 parallel.** `sabbiḥi sma rabbika l-aʿlā` (Q 87:1) and `iqraʾ wa-rabbuka l-akram` (Q 96:3) are the *only two* verses where an afʿal elative in the definite form is predicated of `rabb` + pronoun in an imperative-framed opening. Both surahs are among the earliest by traditional chronology. This suggests a *programmatic* introduction of the elative-divine-attribute construction in the Meccan period.
4. **Takbīr-gap.** The Qur'an never uses the bare predicate `Allāhu akbar`. Its three closest adjacencies (9:72, 29:45, 40:10) all have a different nominative subject. The liturgical takbīr is grammatically post-Qur'ānic, a liturgical compression of the theological principle that what-is-from-Allāh is `akbar`.
5. **Rhetorical-question grid.** The six afʿal lemmas `aẓlam`, `akhdab`, `aḥsan`, `aṣdaq`, `aʿlam`, and occasionally `aḍall` form the Qur'an's standard "who-is-more-X-than" grid. A full mapping of `man aẓlamu mimman …` (16×, from initial scan — the highest-frequency rhetorical slot of this type, not covered here) would be a natural phase-C extension.
6. **Color/defect subset** — the 30+ morphologically-afʿal, semantically non-elative adjectives (color, blindness, deafness, lameness, muteness) cluster in eschatological or miraculous pericopes. Their shared morphology with the elatives may be theologically meaningful (the template of "being-most-X" also expressing bodily incapacity and miraculous transformation).

---

**Data source.** `data/morphology/quranic-corpus-morphology-0.4.txt` (128 219 segments). **Extraction script.** Ad-hoc Python regex over LEM/ROOT fields; output cross-checked against hand-lookup at Q 87:1, 92:20, 96:3, 12:3, 2:138, 4:125, 49:13. **Filters applied:** lemma must begin `>a`, root not initial-alif, length 5–7 characters. False-positive exclusion for `>aroD`, `>amor`, `>ajor`, `>ahol`, `>aliym`, `>ajal`, `>aw~al`, `>aHad`, `>axo*` (form-IV verbs masquerading as nouns), `>avar` (noun "trace"), `>amiyn` (trustworthy), `>aw~aAb` (oft-returning) — none of which are elatives.
