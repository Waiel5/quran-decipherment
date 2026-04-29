# Shirk Rhetoric: How the Quran Argues AGAINST Polytheism

**Phase:** B — hypothesis development
**Anchor root:** sh-r-k (Buckwalter `$rk`)
**Corpus tokens:** 168 across 143 verses in 44 surahs
**Data:** `data/morphology/quranic-corpus-morphology-0.4.txt` (Dukes 0.4)

---

## 0. Why this root matters

If you asked the Quran to name its most persistent adversary, it would
not pick a person, a tribe, a city, or a political structure. It would
pick a cognitive-liturgical act: the act of assigning a partner — a
`$ariyk` — to God. Around that act the text builds its most elaborate
rhetorical machinery: legal prohibitions, accusatory questions,
thought-experiments, parables, prophetic stand-offs, and a carefully
graded theology of forgiveness. All of this orbits one triliteral,
sh-r-k, which appears 168 times in 143 verses across 44 of the 114
surahs — roughly one in every 43 verses of the Quran deploys the root.

This file maps that rhetoric along ten axes set by the task brief.
Each section is grounded in the Dukes morphological corpus; Buckwalter
forms are quoted verbatim so claims are auditable against the TSV.

## 1. Full distribution of the root sh-r-k

**Totals:** 168 tokens, 143 unique verses, 44 surahs. Approximately 25
verses carry two or more sh-r-k tokens (e.g. 4:48 and 4:116 each contain
two verb-forms; 16:86 layers verb and noun together).

**By lemma (descending):**

| Lemma           | POS | Tokens | Gloss |
|-----------------|-----|--------|-------|
| `>a$oraka`      | V   | 71     | form IV: "to make a partner for / to associate" |
| `mu$orik`       | N   | 44     | active participle form IV: "associator" (masc.) |
| `$ariyk`        | N   | 40     | fāʿīl pattern: "partner, associate, colleague" |
| `$irk`          | N   | 5      | maṣdar: "the act/state of associating" |
| `mu$orika`t`    | N   | 3      | form IV participle, fem. plural |
| `mu$tarikuwn`   | N   | 2      | form VIII participle: "co-sharers" |
| `mu$orikap`     | N   | 2      | form IV participle, fem. singular |
| `$aArika`       | V   | 1      | form III imperative (17:64) |

**By verbal morphology** (72 verb-tokens):

- 49 imperfective active (`yu$riku`, `tu$riku`, `nu$riku` etc.) — the
  overwhelming majority. Shirk is presented as *ongoing or potential*
  action, not a settled historical fact.
- 18 perfective active (`>a$raku`) — closing judgements: "they
  associated."
- 3 imperfective passive (`yu$raka bihi`) — reserved for the theological
  formula "that He be associated-with." 4:48, 4:116, 6:88.
- 2 imperatives: 17:64 (`$aArik` to Iblis) and 20:32 (Moses asking God
  to `>a$orik` Aaron with him in his mission — the one positive use,
  "make him a partner in my affair").

**By verbal form (Arabic measure):** 120 of the 168 tokens are form IV
(causative); 45 tokens are non-verbal (so the form is zero-marked in the
TSV); 2 are form VIII (`mu$tarikuwn`), 1 is form III (`$aArik`). The
dominance of form IV is structural: shirk is almost always *causative* —
you *install* a partner. It is not passive drift.

**By surah (top 10 concentrations):**

| Surah | Count | Character |
|-------|-------|-----------|
| 6  (al-Anʿām)     | 29 | Meccan, densest theological polemic |
| 9  (al-Tawba)     | 12 | Medinan, against treaty-breakers among mushrikīn |
| 16 (al-Naḥl)      | 11 | Meccan, includes slave-parable (16:75) |
| 10 (Yūnus)        | 9  | challenge constructions concentrated |
| 30 (al-Rūm)       | 9  | eschatological mushrikīn |
| 2  (al-Baqara)    | 7  | legal — marriage prohibitions 2:221 |
| 7  (al-Aʿrāf)     | 6  | Moses narrative + Aʿrāf stand-off |
| 4  (al-Nisāʾ)     | 6  | unforgivability formula |
| 3  (Āl ʿImrān)    | 5  | common-word 3:64 |
| 18 (al-Kahf)      | 5  | story-frame denials |

The sweep is heavily Meccan (Q 6, 10, 16, 30 dominate), which matches
the sīra context: shirk was the live theological opponent in Mecca.
Medinan incidence (Q 2, 3, 4, 9) reframes the same vocabulary for
legal and social applications — whom to marry, whom to ally with,
whom to forgive.

## 2. Shirk as "the greatest wrong" (Q 31:13)

The verse reads, morph-parsed:

```
wa-i*            huwa yaEiZuhu      yaA bunay~a
[when he said]   [exhorting him]    [O my little son]
laA tu$rik       bi-llaAhi
[do not associate]  [with God]
<in~a l-$irka    la-Zulmun EaZiymun
[indeed al-shirk]  [EMPH-is a great wrong]
```

Luqman's sole speech-act in the Quran opens with vocative `yaA bunay~a`
(diminutive of affection) and its first content-bearing clause is a
negative imperative of `>a$raka` in the jussive form 2MS (`tu$orik`).
The grammatical move matters: the *first* thing a father should tell
a son is a *prohibition*, and that prohibition is aimed at a cognitive
act, not a behaviour.

Then the explanatory `<in~a` clause delivers the only instance in the
Quran where the definite noun `$irk` is predicated `la-Zulmun EaZiymun`
— "emphatically a great wrong". The emphasis particle `la-` and the
intensive adjective `EaZiymN` together form a superlative judgement.
The same adjective `EaZiymN` is used elsewhere for the divine Throne
(`al-ʿarsh al-ʿaẓīm`) and for Qurʾānic revelation itself (`al-qurʾān
al-ʿaẓīm`). Luqman is placing shirk on a scale reserved for cosmic
magnitudes.

The verse is pivotal because it produces a scale anchor that the rest
of the Quran can reference without repeating: "a great wrong" means
*this*. Subsequent shirk verses don't need to argue magnitude; they
can cite context.

## 3. Rebutting specific idols: al-Lāt, al-ʿUzzā, Manāt (Q 53:19–23)

The morphology here is laconic, and that is itself the rhetorical
point. The three idols receive only proper-noun (`PN`) tags:

```
>a-fa-ra>aytumu   al-laAta          wa-l-EuzaY
[have you seen]   [al-Lāt]          [al-ʿUzzā]
wa-manaw`pa       al-vaAlivata      al->uxraY`
[and Manāt]       [the third]       [the other]
```

Note what is absent. These three names do NOT carry a `ROOT:` field in
the Dukes corpus — they are opaque proper nouns. The Quran refuses to
dignify them with an Arabic root. Then 53:22 deploys a withering judgement
`tiloka <i*FA qisomapN DiyzaY` — "that, then, is an unjust division"
(splitting: you assign daughters to God, keep sons for yourselves).

53:23 delivers the punch:

```
<ino hiya  <il~aA  >asmaA^'un   sam~aytumuw-haA
[they are]  [nothing]  [but names]  [you named them]
>antum wa-aabaA^'ukum   maA >anzala llaahu bi-haA min suloTaan
[you and your fathers]  [God has sent down no authority for them]
```

Two rhetorical devices compound: the negative-exclusive `<in hiya
<il~aA` ("they are nothing but …"), and a demotion of ontological
status to purely linguistic status — `>asmaA^'N`, "names". The idols
have no referent; they are empty signs, coined by one generation and
inherited by the next. No revelation (`maA >anzala llaahu`), no
authority (`suloTaan`), no epistemic warrant.

This is a sophisticated manoeuvre: the Quran does not *refute* the
idols — it reclassifies them. It moves them from ontology to lexicon.
Deities become vocabulary.

## 4. The challenge-construction family

A specific rhetorical form recurs whenever the Quran confronts
polytheists directly: an imperative to *produce evidence for* the
partners. Four verses from the brief:

### Q 10:35 — the hidāya challenge

```
qulo halo min $urakaA^}ikum m~an yahdiY^ <ilaY l-Haqqi?
```

"Say: Is there among your partners any who guides to the truth?" The
particle `halo` is rhetorical-interrogative. `$urakaA^}ikum` attaches
the 2MP possessive — "*your* partners" — the Quran never concedes they
are actual partners. The expected answer is silence; the verse then
delivers the reply for them: `quli llaahu yahdiY li-l-Haqqi` — God does.

### Q 10:38 — the challenge-plus-summon

```
qulo fa->otuw bi-suwratin m~ivolihi       wa-{doEuw mani {sotaTaEotum
[say:bring a sura like it]                 [and call whoever you can]
min duwni llaahi  <in kuntum SaadiqiynA
[besides God]     [if you are truthful]
```

Two imperatives daisy-chained: produce a rival sura; then enlist anyone
from among `min duwni llaah` (besides God) to help. The conditional
`<in kuntum SaadiqiynA` ("if you're truthful") is the Quran's standard
closer for these demands — it shifts burden of proof onto the accuser.

### Q 17:56 — incapacity of the "claimed" gods

```
quli {doEuw l~a*iyna zaEamtum min duwnihi
fa-laa yamlikuwna ka$ofa D~urri Eankum wa-laa taHwiylF
```

The key verb is `zaEamotum` — "you *claimed*". This is pejorative: `zaʿama`
in Classical Arabic always carries a whiff of unverifiable assertion. The
Quran invites them to call exactly those whom they have merely claimed —
and then declares the called ones powerless to lift harm (`ka$fa D~urr`)
or even to transfer (`taHwiyl`) it.

### Q 46:4 — the triple burden of proof

```
qul >a-ra>aytum maA tadEuwna min duwni llaahi >aruwniy
maA*aA xalaquw mina l->arDi >am lahum $irkun fiY l-samaawaaati
i}otuwniy bi-kitaabin min qabli haa*aa >aw >avaaratin min Eilmi
<in kuntum SaadiqiynA
```

This verse is the densest of the set. It demands three kinds of evidence:
(a) creational — "what have they created of the earth?" (b) participational
— "or do they have a `$irk` [share] in the heavens?"; (c) epistemic —
"bring me a scripture before this or a *trace of knowledge*". The hapax
`>avaarap` ("vestige, trace") collocates here with `Eilm` to demand
epistemology, not mere assertion. 46:4 is thus the Quran's fully-formed
skeptical challenge: create, share, or cite. If none, be silent.

**Common features across the family:**

- Imperative `qul` ("say") framing: the Prophet is the speaker, never
  bystander.
- Imperative `{doEuw` ("call!") pointing the polytheists *to* their
  gods, daring them to summon.
- The prepositional phrase `min duwnihi / min duwni llaahi` ("besides
  Him / besides God") as the standard marker for false objects of
  worship — used 150+ times in the Quran, a stable collocation with
  the shirk rhetoric.
- The conditional close `<in kuntum SaadiqiynA`, shifting evidentiary
  burden.

## 5. Luqman's advice to his son (Q 31:13)

Covered lexically in §2 above, but the rhetorical framing deserves
separate attention. Within Sura 31, verses 13–19 form a ring of
paternal advice. 31:13 opens the ring with the prohibition of shirk;
31:19 closes it with a counsel on posture and voice. Between these
poles come commandments about parents (14), non-compliance when
parents demand shirk (15), moral accountability at the atomic scale
(16), ritual prayer (17), and social humility (18). Shirk thus
functions as the *threshold transgression*: it is the only sin Luqman
names by name, and the only one that qualifies a child's duty to parents
— verse 15 explicitly permits disobedience to parents who push shirk.

The ring is built around shirk because shirk is understood as the
foundational category whose negation unlocks every other obligation.
In literary terms Luqman's opening line acts like a first axiom: once
it is accepted, the remaining nine verses follow as theorems.

## 6. Parables against "associated partners"

Three sustained parables (`mathal`) attack shirk by analogy. The
parable-opening formula `Daraba (llaahu) mathal` frames each.

### 6a. The fly parable (Q 22:73)

```
yaA >ayyuhaa l-naasu  Duriba mavalun fa-{stamiEuw lahu
<inna l~a*iyna tadEuwna min duwni llaahi lan yaxoluquw *ubaabF
wa-lawi {jotamaEuw lahu
wa-<in yasolubhumu l-*ubaabu $ayo_#F l~aA yasotanqi*uwhu minhu
DaEufa l-Taalibu wa-l-maToluwbu
```

Structure: (a) apostrophe to humanity, (b) imperative to listen, (c)
the claim: "those you call besides God will not create a fly". The
fly (`*ubaab`) is chosen precisely for its triviality. (d) Even if
they *all gathered* (`lawi {jotamaEuw`) they could not create it.
(e) The inversion: if the fly *steals* from them, they cannot retrieve
it. (f) The closing aphorism in doubled antithesis: `DaEufa l-Taalibu
wa-l-maToluwbu` — "feeble are the seeker and the sought". The asker
(devotee) and the asked (idol) are both diminished.

This parable attacks shirk on the ground of creative impotence. Partners
of God cannot make the smallest creature. The rhetorical genius is
scale: not a horse, not a sparrow — a fly.

### 6b. The slave parable (Q 16:75)

```
Daraba llaahu mavalF: Eabdun mamoluwkun laa yaqodiru EalaY $aYo'K
wa-man razaqonaahu min~aa rizqF HasanF fa-huwa yunofiqu minhu
sirrF wa-jahorF - halo yasotawuwna?
al-Hamdu lillaahi. bal >akovaruhum laa yaEolamuwna
```

Two figures: (a) an enslaved-and-owned man (`Eabdun mamoluwkun`)
with no independent capacity, and (b) a man gifted with good provision
from God who gives freely in private and public. Are they equal?
`halo yasotawuwna` — the rhetorical-equalisation question. Idols are
the slave-figure: owned, powerless. God is the provider-figure: the
gift flows freely, both secret and public. The closing `balo
>akovaruhum laa yaEolamuwna` ("but most of them do not know") ends
many shirk-polemic verses; it categorises the persistence of idolatry
as epistemic failure.

### 6c. The man-with-many-masters parable (Q 39:29)

```
Daraba llaahu mavalF: rajulF fiyhi $urakaA^'u muta$aAkisuwna
wa-rajulF salamF li-rajul - halo yasotawiyaani mavalF?
al-Hamdu lillaahi. bal >akovaruhum laa yaEolamuwna
```

The lexical detail is striking: the parable uses *two derivatives of
the same root* — `$urakaA^'u` (partners) and `muta$aAkisuwna`
(form VI participle, "mutually contentious co-sharers"). The root
sh-r-k turns back on itself: what you *call* partnership in worship
becomes, in ownership, a nightmare of quarrelling claimants. The
servant belonging wholly to one master (`rajulF salamF li-rajul`)
is whole (`salam`, same root as Islām). The servant split among
bickering `$urakaA^'u` is torn.

The triple-parable architecture is coordinated: each attacks one
failure of the idol — inability to create (22:73), inability to act
(16:75), inability to cohere (39:29). Together they form a
rhetorical syllogism: the mushrik worships what cannot create, cannot
act, and cannot agree. The three closing lines — `DaEufa l-Taalibu
wa-l-maToluwb` / `bal >akovaruhum laa yaEolamuwna` / `bal >akovaruhum
laa yaEolamuwna` — form a ringed refrain of epistemic judgment.

## 7. Idolatry narratives

### 7a. Abraham breaking idols (Q 21:51–73; 37:83–96)

The sh-r-k root barely surfaces in the idol-smashing scenes
themselves; the operative vocabulary is `Sonma` (21:57) and
`tanoHituwna` (37:95, "what you carve"). The logic of the narrative is
nonetheless the same. Morphologically:

- 21:57 `wa-ta-llaahi la->akiydanna >aSonaAmakum` — oath + emphatic
  future + 2MP "your idols": the rhetorical setup.
- 21:58 `fa-jaEalahum ju*a`*F <il~aA kabiyrF l~ahum` — "he made them
  fragments except the biggest one of them" — the narrative trap.
- 21:63 `qaAla bal faEalahu kabiyruhum` — Abraham attributes the
  smashing to the surviving idol. The move is Socratic: let the
  mushrikūn refute him.
- 37:95 `>a-taEobuduwna maA tanoHituwna` — the interrogative that
  dissolves the premise: you worship what you *carve*.
- 37:96 `wa-llaahu xalaqakum wa-maa taEomaluwna` — the ontological
  counter: God created both *you* and *what you make*.

The narrative converts the polemic from words to physical demonstration.
Shirk's silliness is exposed not by argument but by the idols' literal
inability to defend themselves. The broken `Sonm` becomes a pedagogical
object.

### 7b. Moses vs Pharaoh's gods

Pharaoh is famously the only character in the Quran who proclaims
himself God (`>anaa rabbukumu l->aElaY`, 79:24), but a subtler polemic
runs in Q 7:127, where Pharaoh's chiefs — not Pharaoh himself —
complain that Moses and his people will "leave you and your gods"
(`wa-ya*araka wa-aalihataka`). Pharaoh has gods. He is both an
associate-claimant and an associate-installer. The Mosaic polemic
targets this double shirk: Pharaoh arrogates divinity to himself *and*
keeps a pantheon.

Q 7:138 — right after the Red Sea — shows the Israelites themselves
demanding an idol (`{joEal lanaa <ilaahF kamaa lahum >aalihap`). They
come from idolatrous Egypt and revert to idolatrous Canaan-imitation.
Shirk is portrayed as a cultural gravity-well: exodus from it requires
sustained effort.

## 8. Denial of divine family

### 8a. Q 6:101 — "no consort, no son"

```
badiyEu l-samaawaati wa-l->arDi
>annaY` yakuwnu lahu waladun wa-lam takun lahu SaaHibap?
wa-xalaqa kulla $aYo'K
wa-huwa bi-kulli $aYo'K Ealiymun
```

The verse is a *logical* argument, not a simple denial. Premise 1:
God is `badiyE` — the originator-from-nothing of the heavens and earth.
Premise 2: a `walad` (offspring) presupposes a `SaaHibap` (consort).
The Quran uses the rhetorical `>annaY` ("how?") — "how could He have
offspring when He has had no consort?" Then the positive theology:
`wa-xalaqa kulla $aYo'K` — He is the creator of *everything*; and
comprehensive in knowledge. The implication: anything with the status
of consort or son would itself need to be among the "everything" He
created. Family relations entail prior creation; God has no prior.

### 8b. Q 112:3 — twin negation

```
lam yalido wa-lam yuwlado
```

Two jussive negations of the same root w-l-d, in opposite voices: He
neither begets nor is begotten. Where 6:101 argues from creation, 112:3
denies by symmetry. Combined with 112:4 `wa-lam yakun lahu kufuwan
>aHadun` ("and there has been no one equal to Him"), Sura 112 is the
compact theology of non-shirk: no parts, no peers, no parentage.

The 6:101 / 112:3 pair thus provides both the logical refutation and
the creedal formula. Anti-shirk rhetoric in the Quran routinely
presupposes one or the other.

## 9. Shirk as unforgivable (Q 4:48, 4:116)

Morph of 4:48:

```
<in~a llaaha  laa yagofiru       >an yu$oraka  bihi
[indeed God]  [does-not forgive] [that He be associated]  [with-Him]
wa-yagofiru   maA duwna *aalika  li-man ya$aA^'u
[and forgives][what is below that][for whom He wills]
wa-man yu$oriko bi-llaahi  fa-qadi {fotaraa <ivomF EaZiymF
[whoever associates with God]  [has fabricated a great sin]
```

4:116 is nearly identical, differing only in the closing phrase:
`fa-qado Dalla Dalaalan baEiydan` — "has strayed far astray".

Several morphological points structure the reading:

1. **Voice.** The un-pardoned act is in the *passive* (`yu$oraka` — form IV
   imperfective passive, 3MS subjunctive). The Quran frames the offense
   from God's perspective: the unforgivable thing is *for Him to be
   associated-with*. This is not a transaction-centred concept of sin
   (the actor offends God); it is a predication-centred one (a false
   predication about God's nature).
2. **The `maA duwna *aalika` escape clause.** The identical phrase
   "what is below that" names the domain of pardonable sins. The
   morphology of the formula makes every non-shirk sin structurally
   *lower* than shirk on a scalar line — a formalisation of the "great
   wrong" scale set by 31:13.
3. **The divine-will clause.** `li-man ya$aA^'u` — "for whom He wills"
   — preserves divine freedom *inside* the pardonable category. Shirk
   is the only sin placed outside that freedom, because pardoning
   shirk would validate the false predication being pardoned.
4. **Repentance loophole.** The verse itself does not name repentance,
   but Q 39:53 (`laa taqonaTuw` — "do not despair") and Q 25:68–71
   extend the scope of pardon to *everything*, including shirk,
   *when preceded by tawba*. The logic is coherent: repentance
   terminates the false predication, so pardon becomes possible.
   The 4:48/4:116 formula covers the un-repented case.

4:48 closes with `<ivmF EaZiymF` (echoing 31:13's EaZiymun). 4:116 closes
with `Dalaalun baEiydun`. The pair doubles the judgement across two
adjacent Medinan occurrences in Sura 4. That the Quran *repeats* the
verse almost verbatim inside the same sura is unusual and testifies
to the centrality of the formula.

## 10. Q 3:64 — the "common word"

The full morph:

```
qulo yaA >ahola l-kitaabi  taEaaloW <ilaY kalimatin sawaA^'in
bayonanaa wa-bayonakum
>allaa naEobuda <il~aa llaaha
wa-laa nu$orika bihi $ayo_#F
wa-laa yat~axi*a baEoDunaa baEoDF >arobaabF min duwni llaahi
fa-<in tawallawo fa-quwluw {$ohaduw bi->annaa muslimuwna
```

Three negated verbs rise in social scope:

1. `naEbuda <il~aA llaah` — "we worship only God" (vertical/ritual).
2. `nu$orika bihi $ay_#F` — "we associate nothing with Him"
   (vertical/ontological).
3. `yat~axi*a baEDunaa baEDF >arbaabF` — "none of us take one another
   as lords besides God" (horizontal/political).

The first-person-plural forms (`nu$orika` not `tu$orikuw`) are crucial.
This is the only shirk-rhetoric verse addressed to the People of the
Book where the speaker enters the accusation alongside the addressee.
The verse *moves from polemic to covenant*: shirk becomes the basis
for a shared creed, not a dividing line.

The closing `fa-quwluw {$ohaduw bi-annaa muslimuwna` ("so say: bear
witness that we are submitters") makes explicit the conversion of
the argument. If they refuse the common word, the Prophet's community
simply bears self-witness. No coercion, no escalation — just a
declaration.

Q 3:64 is thus the Quran's most important *constructive* deployment
of anti-shirk rhetoric. It is the verse where the polemic stops being
a weapon and becomes a handshake.

## 11. Internal symmetries of the root

Two features of the root's distribution deserve closing attention.

**Imperative shirk belongs to Iblis.** Form III imperative `$aArikhum`
("share with them") occurs once, in 17:64, where Iblis is told (in
mock-permission) to "share with [the sons of Adam] in wealth and
children." The grammatical fact is startling: in a corpus with 72
sh-r-k verbs, the only imperative of any form addressed to another
person is satanic. The Quran thereby makes shirk not just a human
error but a satanic *collaboration* — agent-modelled.

**Eschatological form VIII: `mu$tarikuwn`.** Form VIII `{$otarako` would
be the natural reflexive ("they associated among themselves"). It
appears twice: 37:33 `fa-<innahum yawma'i*in fiy l-EA*aabi
mu$tarikuwna` — "they on that day, in the Punishment, are
co-sharers"; and 43:39 `>an~akum fiy l-Ea*aabi mu$tarikuwna`.
Those who falsely *shared* in worship below become genuine
*co-sharers* in punishment above. The root's eschatology is ironic:
shirk produces the only partnership that actually materialises, and
it materialises in hell.

These two internal moves close the rhetorical loop. Shirk is
(a) caused by Satan (17:64), (b) practiced on Earth (120 form-IV
tokens), (c) rebutted by prophetic challenge, parable, narrative, and
theology (sections 3–8 above), (d) unforgivable unrepented (section 9),
(e) offered a covenantal exit (section 10), and finally (f) consummated
as grim co-sharing in the fire (37:33, 43:39).

## 12. Summary of the rhetorical repertoire

| Move | Representative verses | Mechanism |
|------|-----------------------|-----------|
| Weight-setting | 31:13 | `<in~a l-$irk la-Zulmun EaZiym` |
| De-ontologising named idols | 53:19–23 | Demotion to `>asmaA^'` |
| Evidentiary challenge | 10:35, 10:38, 17:56, 46:4 | `{doEuw`, `>aruwniy`, `<in kuntum SaadiqiynA` |
| Paternal instruction ring | 31:13–19 | Opens with shirk prohibition |
| Parables of impotence | 22:73, 16:75, 39:29 | Fly, slave, many-masters |
| Prophetic demonstration | 21:51–73, 37:83–96 | Abraham's axe |
| Prophetic confrontation | 7:127, 7:138 | Moses vs Pharaoh |
| Family denial | 6:101, 112:3 | No consort, no son |
| Unforgivable-unless-repented | 4:48, 4:116 | `laa yagofiru >an yu$oraka` |
| Common word | 3:64 | 1P-inclusive three-negation creed |

The Quran does not pick one anti-shirk move; it picks *all* of them,
and deploys them in coordinated registers: affective (Luqman, Abraham),
evidentiary (challenges, parables), ontological (family denials),
forensic (unforgivability), and irenic (3:64). Together these form
the densest sustained polemical architecture in the Quran, supported
by 168 root-tokens and at least as many non-root lexical hooks
(`>aSonaAm`, `>awovaan`, `>aalihap`, `min duwni llaah`). The
argumentative ambition is not merely to discredit particular deities
but to *reclassify the entire category* — to make shirk a lexical
artifact rather than a metaphysical possibility.

---

**Cross-references.** This file should be read with:
- `findings/phase-b-hypotheses/divine-names-distribution.md` (for the
  positive theology that shirk negates).
- `journal/parables-run-1.md` (for the `Daraba mathal` formula across
  the Quran).
- `journal/negation-taxonomy-run-1.md` (for the distribution of `laa`,
  `lam`, `laysa` that dominates anti-shirk grammar).
- `journal/rhetorical-questions-run-1.md` (for `halo`, `>a-fa-ra>aytum`,
  `maa*aa`).
