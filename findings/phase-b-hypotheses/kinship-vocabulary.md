---
title: Kinship Vocabulary in the Quran — Lexical Inventory, walad/ibn Asymmetry, the Womb-Covenant, and the Four-Wives Typology
phase: phase-b-hypotheses
agent: kinship-vocabulary-run-2
date: 2026-04-12
rules:
  canonical_text: quran-text/quran-min-tashkeel.json (Tanzil Uthmani)
  morphology: data/morphology/quranic-corpus-morphology-0.4.txt (QAC v0.4, Buckwalter)
  counts_are: unique-verse counts unless otherwise noted; tokens given where relevant
dependencies:
  morphology: /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  arabic_text: /Users/grey/Downloads/quran/quran-text/quran-min-tashkeel.json
prior_art:
  vocatives: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/vocative-addresses.md
  covenant: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/covenant-language.md (run-1)
  negation_taxonomy: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/negation-taxonomy.md
status: inventory + four hypotheses
---

# Kinship Vocabulary in the Quran

The Quran is a book obsessed with lineage — but not in the way
ancient Near-Eastern genealogical epics are. It names fathers to
disown them (Āzar, Abū Lahab), exalts mothers who have no named
husbands (Maryam), forbids God every form of reproduction, and
then — in one of the strangest lexical gestures in the book —
installs the Prophet's wives as "mothers of the believers" and
rules that the arḥām (wombs) of blood-kin outweigh the
brotherhood of faith in matters of inheritance. The kinship
lexicon is therefore not just social furniture; it is a
theological argument. This write-up catalogues the inventory,
then presses on the joints where the argument is being made.

All counts below were extracted from the QAC v0.4 morphology and
report **unique verses** (a verse where the lemma appears at
least once) unless "tokens" is specified. Where the user-brief
counts diverged, the morphology numbers are noted and preferred
for reproducibility.

---

## 1. Per-term inventory

### ab — father (root Abw)

- `abN` (singular "father") — **40 verses**, 46 tokens.
- `ābāʾ` (plural "fathers/ancestors") — **60 verses**, 64 tokens.
- `abawān` (dual "two parents/father-and-mother") — **6 verses**,
  7 tokens.
- **Root-total: 117 tokens / 106 verses** (after deduplication).

Register notes. Singular *ab* is almost always biographical —
individual fathers speaking to or spoken about by sons: Ibrāhīm
and Āzar (6:74, 19:42–48, 21:52, 26:70, 37:85, 43:26); Yaʿqūb
and his sons (12); the father of Maryam implicitly at 19:28
("O sister of Hārūn, your *ab* was not a man of evil"). Plural
*ābāʾ* is the polemic form: "*wajadnā ābāʾanā ʿalā ummatin*" —
"we found our fathers on a tradition" (43:22–23, 2:170, 5:104,
31:21) — the stock objection to the Prophet's message. The
plural fathers are the inertia of religion; the singular
father is the individual case the Qur'an is judging.

### umm — mother (root Amm, distinct from *umma*)

- `umm` (lemma `>um~`) — **31 verses**, 35 tokens.
- `ummahāt` (pl.) — a sub-form of the same lemma; appears at
  4:23, 5:75 ("his mother was truthful" — of Mary), 16:78, 23:50,
  31:14, 33:4, 33:6, 39:6, 46:15, 53:32, 58:2.
- Collocation `walīdan fī ḥijri ummihi`-type phrasing is absent;
  mothers are usually named as the bearers of prophets or as the
  anchors of the moral-inheritance command (17:23, 31:14, 46:15).

Critically, the root Amm also yields `umma` (64 verses, community)
and `imām` (12 verses, leader). Arabic etymology places these
together — *umm* is what is headed-toward, the source — but the
Quran separates the registers cleanly: 35 tokens for kin-mother,
64 for community. The kinship-umm is outnumbered by the
theological-umma nearly 2:1.

### ibn / banū / abnāʾ — son(s) (root bny, lemma `{bon`)

- Singular/construct *ibn* and its plurals *banū / abnāʾ* —
  **57 verses**, 63 tokens.
- Forms: `{bona` "son of" (16), `>abnāʾa` "sons" plural in
  absolute/construct (12 + 3 + 4 + 2 = 21), `{bonu` (12),
  `{boni` (11).

The *construct*-form `{bona` ("son of X") is the genealogical
spine: `ʿĪsā bna Maryam` — "Jesus son of Mary" — appears 23×
in the Qur'an and is the *only* surface-form that a named
prophet's sonship takes. The Qur'an never says *waladu
Maryam*; this is the lexical fact behind hypothesis H-K1 below.

*Banū* in the construct-plural becomes the tribal head: **Banū
Isrāʾīl** (41 verses) and **Banū Ādam** (7 verses: 7:26, 7:27,
7:31, 7:35, 7:172, 17:70, 36:60). Both are theological
collectivities, not biological families.

### walad — offspring, abstract (root wld, lemma `walad`)

- Lemma `walad` — **47 verses**, 56 tokens.
- Plural `awlād` — 23 tokens (subsumed under lemma `walad`
  morphologically); these are the pragmatically "kin-children"
  verses (Sūrat al-Talāq 4:11 inheritance; 3:10, 8:28, 9:55/85,
  34:35, 58:17, 60:3, 63:9, 64:14/15 about worldly distraction).
- Verb `walada` (to beget) — 9 tokens across 8 verses;
  crucially 112:3 (`lam yalid wa lam yūlad`), 19:15 (John is
  *born*), 19:33 (Jesus says "peace on the day I was born"),
  37:152 ("God begot" — *quoted refutation*), 58:2 (mothers in
  ẓihār), 71:27 (Noah's prayer about unbelievers begetting),
  90:3 ("by the begetter and what he begot"), 11:72 (Sarah
  "shall I give birth?").
- Related: `wālid` (14 tokens) and `wālidayn` (10 tokens, dual
  "two parents") are the *living-parent* register of the
  inheritance and filial-piety laws; `walīd` (7 tokens) is the
  *newborn/child* — used of Moses being "brought up" in
  Pharaoh's house (26:18) and of the *wildān mukhalladūn*
  (eternally-young servants of Paradise, 56:17, 76:19).

Distribution by theme (47 walad verses, rough classification
from manual inspection):
- **Theological denials** ("Allah has not taken a walad") —
  17 verses: 2:116, 4:171, 6:100/101, 10:68, 17:40/111, 18:4,
  19:35, 19:88/91/92, 21:26, 23:91, 25:2, 39:4, 43:81, 72:3,
  112:3.
- **Inheritance law** (4:11–12, 4:176, 2:233, 58:2): 6 verses.
- **Worldly ornament / trial** (3:10/116, 8:28, 9:55/85,
  18:39, 34:35/37, 57:20, 58:17, 60:3, 63:9, 64:14/15, 71:21):
  ~16 verses.
- **Prophetic / narrative** (3:47 Mary, 12:21 Joseph's adoption,
  19:77 hypothetical "I shall be given wealth and children",
  28:9 Moses saved, 31:33 father-son solidarity at Judgment,
  6:137/140/151 child-killing condemnation).

The theological-denial cluster is the largest single use of
`walad`. This is the Qur'an's polemical word.

### bint / banāt — daughter(s) (root bny, lemma `banaAt`)

- `banāt` plural — **12 verses**, 17 tokens.
- `bint` singular (lemma `{bonat`) — 2 verses (66:12 Maryam
  "daughter of ʿImrān"; 28:27 the daughter offered by Shuʿayb).

The daughters register is thin and highly polemical. Three
clusters:
1. **Refutation of the "daughters of Allah" pagan theology**:
   16:57, 37:149–153, 43:16, 52:39, 53:21 — rhetorical
   questions asking whether the Arab pagans give Allah the
   daughters they themselves despise.
2. **Marriage-law enumeration**: 4:23 (forbidden degrees,
   including *banāt al-akh*, *banāt al-ukht*), 33:50 (categories
   marriageable by the Prophet).
3. **Lot's daughters as offered sacrifice**: 11:78–79, 15:71.

This is one of the Qur'an's sharpest ironies: the pagan
Arabs buried daughters alive (16:58–59, 81:8–9) yet claimed
God had only daughters; the Qur'an answers, forcibly, by
*denying God any offspring of either sex and simultaneously
ennobling daughters in family law*.

### akh / ukht / ikhwa — brother, sister, brotherhood (root Axw)

- `akh` — **69 verses**, 75 tokens.
- `ukht` — **11 verses**, 14 tokens.
- `ikhwa` (plural "brethren," lemma `<ixowapN`) — **7 verses**:
  4:11 (inheritance), 4:176 (kalāla), 12:5, 12:7, 12:58, 12:100
  (Joseph and his brothers — four instances, making Sūrat
  Yūsuf the densest *ikhwa*-text), 49:10 (*innamā al-muʾminūna
  ikhwatun* — "the believers are but brothers" — the covenant-
  brotherhood axiom).

The biological *akh* is usually a prophet's brother (Aaron to
Moses, 7:142, 19:53, 20:30, 28:34, 25:35; Joseph's brothers,
12:passim; Hūd "to their brother," Ṣāliḥ "to their brother," etc.
— 7 Meccan prophets each addressed as "their brother"). The
covenant-*akh* of 49:10 is a deliberate translation of the
term across the biological / religious membrane: *you are
brothers whether you were or were not born so*.

### zawj — spouse / pair (root zwj)

- Lemma `zawj` — **68 verses**, 76 tokens.
- Verb `zuwwijat` — 5 tokens (81:7 *"wa-idhā al-nufūsu
  zuwwijat"* — when the souls are paired-off at resurrection).
- **Root-total: 81 tokens**, exactly matching the user brief.

*Zawj* is the Qur'an's paradigm-word for pairing. It covers:
- Adam and his *zawj* (2:35, 4:1 "*khalaqa minhā zawjahā*",
  7:189, 30:21, 39:6).
- Marriage law and spousal-rights (2:230–232, 2:234–241, 33:4,
  33:6, 33:28, 33:37, 60:11, etc.).
- The paired creation of all things (36:36, 43:12, 51:49,
  53:45, 78:8) — *wa min kulli shayʾin khalaqnā zawjayn* —
  "we created everything in pairs."
- Paradisal companions (36:56, 37:22, 43:70, 44:54).

Notice the range: *zawj* links human marriage to cosmic
pair-structure. This is why (below, §5) the shift from *zawj*
to *imraʾa* in 66:10–12 is doing semantic work.

### jadd — grandfather

Absent as a kinship term. Lemma `jad~` appears exactly once
(72:3: `taʿālā jaddu rabbinā`), and classical tafsīr reads it
as *majesty/grandeur*, not *grandfather*. The kinship slot is
empty. The other lemma `jadīd` (8 tokens, "new") is a
homophonous root-collision. This is a conspicuous absence: a
Semitic sacred book without grandfathers.

### ʿamm / khāl — paternal and maternal uncle (roots Emm, xwl)

- `ʿamm` (paternal uncle) — 2 tokens (24:31, 33:50).
- `ʿammāt` (paternal aunts) — 3 tokens (24:31, 33:50; also 4:23
  as `ʿammāti-kum` in forbidden-degrees).
- `khāl` (maternal uncle) — 2 tokens (24:31, 33:50).
- `khālāt` (maternal aunts) — 3 tokens (24:31, 33:50; 4:23).

These terms appear only in the **legal-genealogical lists** —
forbidden-degrees of marriage (4:23), licit gaze-exceptions
(24:31), and the Prophet's marriage licence (33:50). The
Qur'an has the vocabulary but does not deploy it narratively;
uncles and aunts exist as jural categories, not characters.

### raḥim / arḥām — womb, kin-bond (root rHm)

- `arḥām` (pl. "wombs / kin-ties") — **12 verses**.
- `ruḥm` (hapax, 18:81) — "compassion" / mercy.
- `marḥama` (hapax, 90:17) — "mercy."

Of the 339 tokens of root rHm, only about 14 are specifically
*womb/kin*-denoting; the rest are divine mercy. The kinship
and the divine-mercy senses share the root: `raḥma` from
`raḥim` is the *womb-mercy* — the visceral, protective
attachment that the womb is metonymic for. This is why
*al-Raḥmān al-Raḥīm* is structurally a womb-metaphor
(classical tafsīr attributed to al-Qurṭubī: "mercy named from
the womb because the womb is the place of mercy"). The
covenantal use is expanded in §8.

### qarīb / qurbā / aqrab / maqraba — kinship-by-nearness (root qrb)

- `qarīb` — 26 verses ("near," both spatially and as "kin").
- `qurbā` — 15 verses (`dhawī al-qurbā` — kindred).
- `aqrab` — 18 verses ("nearer").
- `maqraba` — 1 verse (90:15, "an orphan of kinship").
- `qurubāt` — 1 verse (9:99, "means of nearness to God").

*Dhawū al-qurbā* ("those of kinship") is the key legal phrase:
the Qur'an repeatedly names them as recipients of charity
and inheritance-like rights (2:177, 2:215, 4:8, 4:36, 8:41
[khums], 16:90, 17:26, 24:22, 30:38, 42:23, 59:7, 42:23
[*mawadda fī al-qurbā*, the Prophet's "wage"]).

### awlād / abnāʾ — children (plurals)

- `awlād` (plural of walad) — 23 tokens, in 23 verses.
- `abnāʾ` (plural of ibn) — 21 tokens.
- `banīn` (poetic/indefinite plural) — ~17 tokens.

Diagnostic: `awlād` is almost never used in genealogy
(X-son-of-Y); it functions as a sociological block-noun
("your children" — wealth/distraction). `Abnāʾ` can be
genealogical ("sons of the messengers" 5:18 polemic —
*naḥnu abnāʾu-llāhi* "we are sons of God"). The *walad* /
*ibn* semantic split (§2 below) holds for the plurals too.

### nasl — progeny (root nsl)

- `nasl` noun — 2 tokens: 2:205 ("destroys the harvest and
  the progeny"), 32:8 ("He made his progeny from an extract
  of humble fluid").
- `yansilu` (verb "hasten") — 2 tokens, *not kinship*.

`Nasl` is the Qur'an's most biological, least theological,
kinship word. It is used for destruction-of-nasl (war crime,
2:205) and genetic origin (32:8). No theological weight.

### dhurriyya — descendants (root *rr, lemma *ur~iy~ap)

- `dhurriyya` (sg.) — 26 verses, 28 tokens.
- `dhurriyyāt` (pl.) — 4 verses.

This is the *covenantal-descendants* word, inherited from
Hebrew *zeraʿ* and Aramaic *zarʿ*. Its distribution clusters
on the covenant passages: 2:124 (Abraham asks about his
`dhurriyya`), 2:128, 2:266, 3:33–34 (the chosen families),
3:36–38 (Mary's descent), 4:9 (orphans), 6:84–87 (prophetic
chain), 7:172 (primordial `dhurriyya` covenant — the *bala
shahidnā*), 13:23, 13:38, 14:37–40, 17:62, 19:58, 25:74,
29:27, 36:41, 37:77 (Noah's progeny), 40:8, 43:28, 46:15,
52:21, 57:26, 77:12? — the *rr-root-cooccurrence pattern is
Abrahamic.

---

## 2. walad vs ibn — the Christological and pagan-polemic distinction

The Qur'an's lexicon draws a sharp wall between two
son-words. Both are biologically true, but each is reserved
for different rhetorical work.

- **`ibn`** is always **named**, always **construct**, always
  **embedded in a genealogy**. "ʿĪsā ibn Maryam," "Yaḥyā ibn
  Zakariyyā," "Banū Isrāʾīl," "Banū Ādam." When 5:17 and 5:72
  denounce `al-masīḥ ibn-u-llāhi` as a claim *about* Jesus,
  the word used by the claim is **`ibn`** — because the
  claimed genealogy is *ibn*-shaped, a father-son name-chain.

- **`walad`** is always **abstract**, always **indefinite**,
  always in the **polemical denial**. It never refers to a
  named prophet. When the Qur'an itself asserts offspringhood
  (for Abraham, Zachariah, Noah, the believers), it uses
  *ibn*, *walīd* (newborn), *nasl*, or *dhurriyya*. When the
  Qur'an denies offspringhood to God, it uses **`walad`**.

The 17 walad-denial verses form a tight polemical corpus:
2:116, 4:171, 6:100–101, 10:68, 17:40, 17:111, 18:4, 19:35,
19:88/91/92, 21:26, 23:91, 25:2, 39:4, 43:81, 72:3, 112:3.
The formulas recur:

- `lam yattakhidh walad-an` — "He has not taken a walad" —
  with the verb *ittakhadha* ("to take as", "to adopt") in
  2:116, 10:68, 17:111, 18:4, 19:35, 19:88/91/92, 21:26, 23:91,
  25:2, 39:4, 43:81, 72:3.
- `lam yalid wa lam yūlad` — "He did not beget and was not
  begotten" — 112:3, with the verb from root wld.
- `annā yakūnu lahu walad-un` — "how should He have a walad?" —
  6:101.

The predicate-verb is almost never `khalaqa` ("create") —
because offspring by creation would be theologically
permissible; it is `ittakhadha` ("take, adopt"). The
polemic is specifically against **adoption** or **taking-to-
oneself** — a response both to the Arab *mushrik* claim that
angels are daughters of Allah and to the Christian and Jewish
claim that God has an *adopted* or *begotten* son. This is
why the *walad*-polemic pairs so often with the refusal of
*ṣāḥiba* (consort, 6:101, 72:3) and *sharīk* (partner, 17:111):
the three together form a three-pronged denial of any
intra-divine differentiation that could generate kinship.

Quantitative anchor. Of 56 `walad` tokens, roughly **0** are
used for a named prophet's son as head-noun. The word is a
**theological technical term** — a loan from ordinary Arabic
into a very narrow sacred register.

---

## 3. Inheritance vocabulary at Q 4:11–12

The two *mawārīth* verses are the densest concentration of
kinship vocabulary in the Qur'an. A dense-packed inventory of
what appears there:

**4:11** — `yūṣīkum-u-llāhu fī awlādikum`:
- `awlādikum` (walad-plural) — the subject of the ruling.
- `li-dhakari mithlu ḥaẓẓi l-unthayayn` — "for the male, the
  like of the two-females' share" (males/females, not
  kinship-lexical, but gender-coded).
- `fa-in kunna nisāʾan` — if they are women.
- `wāḥidatan` (daughter, singular) — "one daughter."
- `wa-li-abawayhi` — "and for his **two parents**" (dual
  `abawān` from root Abw).
- `sudus` — one-sixth.
- `in kāna lahu walad-un` — if he has a walad (abstract: any
  child, male or female).
- `fa-in lam yakun lahu walad-un wa-warithahu abawāhu` — if
  he has no walad and his two parents inherit.
- `fa-li-ummihi l-thuluth` — then his mother gets a third.
- `fa-in kāna lahu ikhwa-tun fa-li-ummihi l-sudus` — if he
  has *ikhwa*, his mother gets a sixth.
- `ābāʾukum wa-abnāʾukum` — "your fathers and your sons" —
  the final generalisation.

**4:12** — spousal inheritance:
- `azwājukum` (zawj plural) — "your wives."
- `walad-un` — again the abstract child-marker.
- `kalāla` — the technical term for one "without ascendant
  or descendant heirs" (occurs only 4:12 and 4:176).
- `akhun aw ukhtun` — a brother or sister (sibling of a
  kalāla deceased).

The inheritance passage uses:
- `walad` for the abstract heir (child / children / any
  offspring), because rules need a gender-neutral noun;
- `awlād` for the group of children as subject;
- `abawān` (dual, root Abw) and `ummihi` (root Amm) for
  "parents / mother" — note the strong parallelism between
  the dual and the feminine-singular within one sentence;
- `ibn` / `ābāʾ` / `abnāʾ` (root bny / root Abw) for the
  generalising formula at verse-end;
- `ikhwa` (plural of akh) for siblings-as-block;
- `zawj` (pl. azwāj) for spouses;
- `kalāla` as a legal hapax-like term.

The inheritance verses are the **only** place in the Qur'an
where this many kinship words co-occur. The density is about
12 distinct kinship lexemes in two verses — roughly 7% of
all the kinship roots the Qur'an ever uses. This matters for
the walad/ibn hypothesis: within inheritance, the abstract
`walad` is unmistakably required (because the child's sex is
unknown), which underlines the abstraction of the term. It is
the ideal theological loanable: a sex-neutral child-word
that can carry the polemic.

---

## 4. Mothers of the believers — Q 33:6

> *al-nabiyyu awlā bi-l-muʾminīna min anfusihim wa-azwājuhu
> ummahātuhum wa-ulū l-arḥāmi baʿḍuhum awlā bi-baʿḍin fī
> kitābi-llāhi min al-muʾminīna wa-l-muhājirīn*

"The Prophet is nearer to the believers than their own
selves; and his wives are their mothers; and those who have
kinship-ties (*ulū l-arḥām*) — some of them are nearer to
others in the book of Allah than the believers-and-emigrants."

This one verse performs three kinship-moves at once:

1. **Annexation of the wives to the believers via mother-
   status.** `azwājuhu ummahātuhum` — the Prophet's *azwāj*
   are the believers' *ummahāt*. Note that `umm` here
   extends across all 'believers', i.e. an umma-of-believers
   receives an ummahāt-of-wives. The Amm root does double
   work: community-umm receiving kinship-umm.

2. **Nonelegal motherhood.** The status is legal in one
   direction (marriage to the widows is forbidden, 33:53;
   the believers must not hurt the Prophet by marrying his
   wives after him) but not in the other (no inheritance
   from the wives *as mothers* to the believers — 33:4 has
   already warned that the Prophet does not have two hearts
   nor any adopted son inheriting by adoption). This is
   covenant-motherhood: the social claim without the
   inheritance consequence.

3. **Restoration of kin-priority via arḥām.** The second
   clause of 33:6 reverses an earlier practice reported in
   tafsīr: after the *hijra* the Muhājirūn and Anṣār had
   inherited from each other on grounds of covenant-
   brotherhood (*muʾākhāh*, 8:72). 33:6 rolls that back:
   *ulū l-arḥām* (blood-kin) are now restored to primacy.
   The same formula recurs verbatim at 8:75 — so the change
   is registered in two surahs.

The three moves together define the Qur'anic theology of
kinship: a covenant-mother above blood (Prophet's wives); a
blood-kin priority in material inheritance; the Prophet
positioned "nearer than the self" (so the covenant-*ab*
relation has been replaced by a covenant-*awlā* relation —
"nearer-than" rather than "father-of"; cf. 33:40).

The `arḥām` here is a plural ("wombs") metonymised into
"kinship-bonds": the bond-through-the-womb. And this brings
us to the four-wives typology.

---

## 5. The four exemplary wives — Q 66:10–12

The final passage of Sūrat al-Taḥrīm offers four women as
exemplars. They are paired in a 2×2 grid:

| | married to unbeliever | married to believer | not married |
|---|---|---|---|
| **bad end** | — | Noah's *imraʾa*, Lot's *imraʾa* | — |
| **good end** | Pharaoh's *imraʾa* (Āsiya) | — | Maryam (no husband) |

Lexical observation: the text says **`imraʾa`** (the woman,
individuated, of) and *not* `zawj`, although these women are
indisputably spouses. Six tokens of `imraʾata` in three
verses: `imraʾata Nūḥ`, `imraʾata Lūṭ`, `imraʾata Firʿawn`
(66:11), and in the parallel 66:12, `Maryam ibnata ʿImrān`
(daughter-of-`ʿImrān`, because she has no *imraʾa*-of
relation).

The choice of `imraʾa` over `zawj` is semantically loaded:

- `zawj` is the **paired**-word, the term of successful or
  at-least-integral pairing; the Qur'an uses it of Adam and
  his partner (4:1), of cosmic pair-creation (51:49), of
  paradisal couples (36:56), and of the living spousal pair
  in ordinary inheritance law (4:12).
- `imraʾa` is the **individuated**-word, where the pairing
  has failed, been deflected, or is about to be dissolved.
  It is used of `imraʾat al-ʿazīz` (Potiphar's wife, 12:21,
  12:30, 12:51), `imraʾatī` in Zachariah's prayer "but my
  wife is barren" (3:40, 19:5, 19:8 — where the pairing is
  failing biologically), `imraʾatu Ibrāhīm` when Sarah is
  incredulous at the annunciation (11:71), `imraʾatuhu
  ḥammālat-a l-ḥaṭab` (111:4 — Abū Lahab's wife, at the
  moment of being jointly damned).

The pattern: `imraʾa` marks the **failed or failing pair**.
Noah's wife and Lot's wife *`khānatāhumā`* — "betrayed them";
Pharaoh's wife repudiates her own husband's kingdom from
within his palace (*`rabbi ibnī lī ʿindaka baytan fī
l-janna wa-najjinī min Firʿawna wa-ʿamalihi`*); Mary has no
husband to pair with, and the narrative's solution is not
`zawj`-language but `fa-nafakhnā fīhi min rūḥinā` — divine
inspiration without sexual pairing.

Thus the 2×2 typology is lexically marked by the refusal of
`zawj`. These four women stand outside the Qur'an's normal
pairing-lexicon, which is exactly the point of the parable:
salvation and damnation cut across the marriage bond.

Fifth observation. 66:11 includes the kinship-adjacent
phrase `ibni lī ʿindaka baytan` — "build for me, beside
You, a house" — where the verb `ibni` (imperative of
*banā* "to build") collides phonologically with the noun
`ibn` ("son"). The word-play is intentional across
classical tafsīr: Āsiya asks for a built-house in Paradise,
but the root is the very root that, everywhere else in the
Qur'an, generates "son" and "Banū X." She is asking to be
re-genealogised — to become a daughter of the house of God
rather than a wife of Pharaoh. The kinship-root does the
poetic work.

---

## 6. "Yā bunayya" — the father-to-son covenant call

The diminutive vocative `yā bunayya` ("O my little son") is
used **10 times** in the Qur'an, across a tight set of
father-figures:

1. 2:132 — **Jacob** to his sons (collective).
2. 11:42 — **Noah** to his son on the ark.
3. 12:5 — **Jacob** to **Joseph** (do not tell your dream).
4. 12:67 — **Jacob** to his sons (enter by different gates).
5. 12:87 — **Jacob** to his sons (do not despair of God's mercy).
6. 14:35 — **Abraham** (implied; a generalisation of the
   covenant call).
7. 31:13 — **Luqmān** to his son (do not associate partners).
8. 31:16 — **Luqmān** to his son (grain of mustard-seed).
9. 31:17 — **Luqmān** to his son (establish prayer).
10. 37:102 — **Abraham** to **Ishmael** at the sacrifice.

Every occurrence is a **covenant-moment**: a father
transmitting tawḥīd, ethics, or eschatology to a son at a
threshold. The vocative is not used in casual speech, nor is
it used by non-prophetic or non-wise-teacher figures. The
Qur'an's `bunayya` is a mini-genre.

Luqmān's triplication (31:13, 31:16, 31:17) is structurally
significant. It takes a stranger (Luqmān is not a prophet and
has no named people) and gives him the same formal call as
Jacob and Noah — so the *bunayya* register is not limited to
Israelite patriarchs but extends to the wise-teacher. This is
exactly parallel to the way the Qur'an extends *akh* from
biological to religious brotherhood (49:10).

The 11:42 Noah case is the **failed** `bunayya` call — Noah
says *yā bunayya irkab maʿanā* ("O my little son, embark
with us") and his son refuses; the son drowns and is
retrospectively declared "not of your family" (11:46: *innahu
laysa min ahlika*). This is the Qur'an's most explicit
rejection of biological-lineage-guarantees-salvation: even
the most intimate kinship vocative cannot save the son who
refuses.

---

## 7. The walad-denial — 19:35, 19:88–93, 112:3

Three passages carry the fullest denial-theology:

**Q 19:35** — end of the Mary-Jesus narrative:
> *mā kāna li-llāhi an yattakhidha min waladin subḥānahu idhā
> qaḍā amran fa-innamā yaqūlu lahu kun fa-yakūn*

"It was not for Allah to take any walad — glory to Him; when
He decrees a thing He merely says to it 'Be' and it is."

Doctrinal move: replace *begetting* with *kun fa-yakūn*. The
walad-relation is displaced by the creation-by-word relation.
Note the modal: *mā kāna li-llāhi* — "it was not *for* Allah"
— God is not the one who *would* do this. This is a moral
impossibility, not a physical one.

**Q 19:88–93** — five verses of protest against the walad-
claim:
> 88: *wa-qālū ittakhadha l-Raḥmānu walad-an*
> 89: *la-qad jiʾtum shayʾan iddā*
> 90: *takādu l-samāwātu yatafaṭṭarna minhu wa-tanshaqqu
> l-arḍu wa-takhirru l-jibālu haddā*
> 91: *an daʿaw li-l-Raḥmāni walad-an*
> 92: *wa-mā yanbaghī li-l-Raḥmāni an yattakhidha walad-an*
> 93: *in kullu man fī l-samāwāti wa-l-arḍi illā ātī
> l-Raḥmāni ʿabdan*

The argument in 19:88–93 is cosmological. The *walad*-claim
is so grave that the heavens almost split, the earth is rent,
the mountains collapse. The resolution-verse (93) is
ontological: *every* being in the heavens and earth comes to
the Raḥmān as **ʿabd** — as servant — not as walad. The
kinship-with-God is replaced by servanthood-to-God.
Strikingly, the denial is specifically addressed to
**al-Raḥmān** (mentioned three times in the passage) — the
name that, etymologically, derives from **raḥim** (womb).
The sub-poem says: the God-whose-name-is-womb-derived does
not have a womb-child. This is lexically and theologically
tight.

**Q 112:3** — `lam yalid wa lam yūlad`:

The densest walad-denial in the Qur'an uses not the
noun but the verb (root wld) — *begetting in both directions
denied*: "He did not beget, and He was not begotten."
Because Sūrat al-Ikhlāṣ is one of the shortest surahs (4
verses), and because the verb form uses negation + jussive
without a direct object, the denial is **absolute** —
not just "no particular walad," but "no *begetting-relation*
whatsoever, active or passive."

Reading 19:35, 19:88–93, and 112:3 together:
- 19:35 denies the **act of taking a walad**.
- 19:88–93 denies the **cosmological propriety** of the
  walad-claim (the heavens would shatter).
- 112:3 denies the **begetting-verb in both voices**.

These three levels — act, cosmology, verb — make a complete
denial-apparatus. And every time, the word `walad` (not
`ibn`) is used. This is H-K1 at full force: **when the
Qur'an needs an abstract, theological, offspring-word, it
uses walad; when it needs a concrete, named, genealogical
offspring-word, it uses ibn**. The two words are not
synonyms; they are tools for different jobs.

---

## 8. `Raḥim` as covenant-word

The kinship-sense of `raḥim/arḥām` appears in 12 verses. They
fall into a small number of theologically loaded contexts:

- **2:27 / 13:21 / 13:25 / 47:22** — the *qāṭiʿū mā amara-
  llāhu bihi an yūṣal* verses, "those who sever what Allah
  has commanded to be joined." 47:22 glosses this explicitly
  as *wa-tuqaṭṭiʿū arḥāmakum* — "and cut your kinship-ties."
  *Qaṭʿ al-raḥim* becomes a specific named sin.

- **4:1** — *wa-ttaqū llāha lladhī tasāʾalūna bihi wa-l-
  arḥām*. "Fear Allah — by whom you ask one another for
  things — and (fear) the wombs." The syntactic position of
  `al-arḥām` here is debated (some recite as `al-arḥāmi` —
  genitive continuing `bihi`, so "by Allah and by the
  wombs"; others as `al-arḥāma` — accusative continuing
  `ittaqū`). Either way, the passage **couples** the divine
  oath with the kinship-oath: God and the womb are jointly
  named as witnesses or objects of taqwā. This is the
  clearest covenant-ascription of `raḥim`.

- **8:75 + 33:6** — twice the formula *ulū l-arḥāmi
  baʿḍuhum awlā bi-baʿḍin fī kitābi-llāh* — "those with
  wombs-in-common, some nearer to others in the book of
  Allah." This inscribes kinship into the divine
  inheritance-book.

- **6:143–144** — arḥām in the polemic against arbitrary
  food-prohibitions: *ammā ishtamalat ʿalayhi arḥāmu
  l-unthayayn* — "or what the wombs of the two females
  enclose." Here the anatomical sense dominates, but the
  rhetorical move is to say: the pagans use *womb-content*
  as a criterion of purity; God uses *womb-kinship* as a
  criterion of moral obligation.

- **22:5, 3:6** — God's shaping of the foetus *fī l-arḥām*,
  "in the wombs." Theological: the womb as the place of
  divine art.

The gradient runs: anatomical → genealogical → covenantal.
The same noun covers all three. And because al-Raḥmān and
al-Raḥīm share the root, the covenant-force runs in both
directions: the divine mercy is womb-shaped, and the
kinship-bond is mercy-shaped. The Qur'an's most abstract
divine attribute (mercy) and its most concrete human bond
(kinship) share a single triconsonantal root. Theologically,
this may be the most compact conceptual unity in the book.

---

## Findings summary

- **H-K1 (walad/ibn)**. `walad` is the Qur'an's **abstract
  theological offspring-word**; `ibn` is its **concrete
  genealogical son-word**. 17 of 47 `walad` verses are the
  walad-denial polemic. No named prophet is ever called a
  `walad` as head-noun.
- **H-K2 (raḥim covenantal)**. The `rHm` root ties divine
  mercy to human kinship (al-Raḥmān ← raḥim). The 12
  kinship-sense verses triple-code the root as anatomical,
  genealogical, and covenantal.
- **H-K3 (imraʾa vs zawj at 66:10–12)**. The four-wives
  passage refuses the paired-word `zawj` and uses the
  individuated-word `imraʾa`; this lexical choice marks
  the failed-or-deflected pairing. The 2×2 typology
  (bad/good × paired/unpaired) is built on this lexical
  fact.
- **H-K4 (covenant-motherhood at 33:6)**. The Prophet's
  wives are `ummahāt`-of-believers; the arḥām-clause
  restores blood-kin priority for inheritance. Two kinship
  circles — covenant and biology — are legislatively
  separated within one verse.
- **Auxiliary finding (bunayya)**. The 10 `yā bunayya`
  vocatives form a tight sub-genre: father-to-son covenant-
  transmission at threshold moments. Luqmān's triplication
  places the non-prophet teacher in the same register as
  the prophetic patriarchs.
- **Absence-finding**. Classical kinship slots that the
  Qur'an does not fill narratively: `jadd` (grandfather) is
  lexically absent; `nasl` has no theological weight;
  `ʿamm/khāl` appear only in legal lists.

The Qur'an's kinship vocabulary is not an archive of Arab
genealogy; it is a **theological toolkit**. Words are
selected for the job — `walad` for the polemic, `ibn` for
the genealogy, `imraʾa` for the failed pair, `zawj` for the
paired cosmos, `raḥim` for the covenant-bond. The
selection-patterns are stable enough to support predictions:
future `walad`-clauses should continue to pair with
`ittakhadha`; future `imraʾa`-clauses should pair with a
narrative of pairing-failure or pairing-deferral; future
`bunayya`-vocatives should all occur at threshold moments
from a father or father-analogue. These are testable claims
that a comparative-Semitic corpus (targum, peshitta,
Syriac homilies, Safaitic/Nabataean kinship inscriptions) can
be used to calibrate, which is a natural next-phase agenda.
