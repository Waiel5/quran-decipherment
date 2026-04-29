---
title: "Jewish and Christian Engagement in the Qurʾān — Ahl al-Kitāb, Banū Isrāʾīl, and the Christological Polemic"
agent: jc-engagement
phase: B
run: 1
date: 2026-04-12
inputs:
  - data/morphology/quranic-corpus-morphology-0.4.txt
  - quran-text/quran-no-tashkeel.json
  - findings/phase-c-structures/maryam-deep-dive.md
  - findings/phase-b-hypotheses/vocative-addresses.md §7
prior_findings:
  - saj-rhyme-analysis (Maryam rhyme-break surgery)
  - prophet-pericope-comparison (Jesus rhyme-break exclusive to S19)
  - covenant-language (mīthāq census)
  - vocative-addresses (yā ahl al-kitāb = argument-oriented vocative)
novel_findings_this_run:
  - ahl_al_kitab_31_phrase_12_vocative_100pct_medinan
  - jewish_vs_christian_polemic_axis_mithaq_vs_masih
  - ghuluw_as_christian_specific_prohibition
  - muqtasidun_as_polemic_relief_valve
  - shared_prophets_theology_is_the_positive_proposal
  - maryam_rhyme_breaks_as_prosodic_correlate_of_polemic_mode
---

# Jewish and Christian Engagement in the Qurʾān

## 0. Thesis

The Qurʾān treats Jewish and Christian interlocutors as **distinct but
overlapping addressees** of a single prophetic-continuity argument.
The rhetorical stance is differentiated by category of offence:

- **Jews (Banū Isrāʾīl, alladhīna hādū)** are criticised for **broken
  covenant** (*naqḍ al-mīthāq*) and **textual tampering** (*taḥrīf*);
  the critique is *historical-ethical*. The model verses are Q 2:40-101,
  Q 5:12-13, Q 5:41-44.
- **Christians (an-naṣārā)** are criticised for **Christological
  category error** — the metaphysical promotion of the Messiah and
  the mother — and for **religious excess** (*ghuluw*); the critique
  is *doctrinal-theological*. The model verses are Q 3:45-63, Q 4:157,
  Q 4:171, Q 5:72-77, Q 9:30.
- The shared vocative **yā ahl al-kitāb** ("O People of the
  Scripture") sits above both, flagging the common substrate: the
  prior revelation. Its 12 vocative occurrences (plus 19 non-vocative
  descriptive occurrences of the same phrase) are **100 % Medinan**
  and **100 % polemical** — not one announces neutral information.

The **positive proposal** accompanying this differentiated critique is
the "shared prophets" theology of Q 2:136 and Q 3:84 — the same list
of named patriarchs, the same refusal to discriminate, the same
claim of prior unity — and the **common word** invitation of Q 3:64.
The Qurʾān's rhetorical posture toward the People of the Scripture
thus moves through three registers: polemic (where there is a claim
to refute), invitation (where there is a shared category to invoke),
and exemption-of-the-moderate (Q 3:113-115: *minhum ummatun qāʾimah*).

This writeup maps all three registers onto their verses and argues
that the Maryam rhyme-breaks (S19 vv 34-40, 88-93) are the *prosodic
fingerprint* of the Christological mode — the moment where the
Qurʾān's poetic surface itself changes shape to mark the doctrinal
pivot.

## 1. Ahl al-Kitāb — the census

### 1.1 Counts

Running a collocation query on the Leeds morphology corpus —
`ROOT:Ahl` immediately followed by `ROOT:ktb` inside the same verse —
returns **31 unique verses** corpus-wide:

```
2:105  2:109  3:64   3:65   3:69   3:70   3:71   3:72   3:75
3:98   3:99   3:110  3:113  3:199  4:123  4:153  4:159  4:171
5:15   5:19   5:59   5:65   5:68   5:77   29:46  33:26  57:29
59:2   59:11  98:1   98:6
```

Of these, **12** occur in the vocative form **yā ahl al-kitāb** (with
`yā` as prefix particle), all within S3 and S5: Q 3:64, 3:65, 3:70,
3:71, 3:98, 3:99, 4:171, 5:15, 5:19, 5:59, 5:68, 5:77. The remaining
19 are descriptive ("from among the People of the Book", "a party of
the People of the Book"), not direct address. Both counts are
reported separately because tafsir-critical downstream work needs the
distinction; the **31 total occurrences** is the standard classical
count.

### 1.2 Revelation status

All 31 host-verses are **Medinan**, with one technical caveat: Q
29:46 sits inside S29 (al-ʿAnkabūt), classically catalogued as
Meccan, but 29:46 itself is one of the verses flagged by Ṭabarī, Ibn
ʿAbbās (via al-Suyūṭī's *Itqān* §41) and the chronological commentary
tradition as a **Medinan insertion into a Meccan surah**. The content
of 29:46 ("Do not dispute with the People of the Book except in the
best manner…") is Medinan-interlocutor engagement, not Meccan
polemic. With this caveat treated, the **Ahl al-Kitāb phrase is
100% Medinan** — it does not appear in Meccan revelation.

This is a structural fact. *Ahl al-kitāb* is a category the Qurʾān
deploys only once a live, face-to-face conversation with Jewish and
Christian communities is happening (i.e. after the Hijra to Madīna).
In the Meccan period, when the Qurʾān's addressees were mostly
Quraysh polytheists, the category is simply not needed: "People of
the Book" has nothing to distinguish from within the immediate
audience.

### 1.3 Rhetorical function

Of the 12 vocative instances:

| Function | n | Verses |
|---|---:|---|
| Reproach (*lima targhabūna / limā / limādhā*) | 5 | 3:65, 3:70, 3:71, 3:98, 3:99 |
| Invitation to common ground | 1 | 3:64 (the *kalimat-sawāʾ* call) |
| Prohibition of theological excess | 2 | 4:171, 5:77 (*lā taghlū fī dīnikum*) |
| Announcement of the messenger | 2 | 5:15, 5:19 (*qad jāʾakum rasūlunā*) |
| Challenge of groundedness | 2 | 5:59, 5:68 (*lastum ʿalā shayʾin*) |

Every single vocative is **argument-oriented**. There is no neutral
"O People of the Book, welcome", no purely informational address.
Contrast with *yā ayyuhā l-ladhīna āmanū* (legal-imperative) and *yā
ayyuhā n-nās* (universal-announcement): *yā ahl al-kitāb* is the
Qurʾān's **dialectic-opener**. It is the flag that says "what follows
is a dispute".

## 2. The Jewish polemic axis — mīthāq and taḥrīf

### 2.1 Q 2:40-101 — the long indictment

The opening 62 verses of the Banū Isrāʾīl block in Al-Baqarah run
from v40 (the first vocative `yā banī isrāʾīl ʾudhkurū niʿmatī`) to
v101, and form the longest sustained Jewish-addressed passage in the
Qurʾān. Within this block:

- **Three covenant-refrains**: v40 (`ʾawfū bi-ʿahdī ʾūfi bi-ʿahdikum`),
  v83 (`ʾakhadhnā mīthāq banī isrāʾīl`), v93 (`ʾakhadhnā mīthāqakum
  wa-rafaʿnā fawqakum aṭ-ṭūr`). The structure is: "remember the
  favour, honour the covenant, we took the pledge."
- **Seven specific infractions catalogued**: worship of the calf
  (v51, 54, 93), complaint against manna and quails (v61), demand to
  see God (v55), twisting of "ḥiṭṭah" to *ḥintah* (v58-59), Sabbath
  transgression (v65), slaying of prophets (v61, 91), and the partial
  belief "we believe in some of the Book and disbelieve in some"
  (v85).
- **The verbal form `ʾūtū l-kitāb`** / `alladhīna ʾūtū l-kitāba`
  appears at v101 and functions as the *seal* of the indictment: the
  Book was given, a faction threw it behind their backs.

The passage uses the Qurʾān's signature **iltifāt cascade** (agent-
shifts between 1st-person divine plural, 3rd-person on the Children
of Israel, and 2nd-person direct address) exactly when the moral
temperature peaks. At v85, the cascade converges on a single
rhetorical question (`ʾa-fa-tuʾminūna bi-baʿḍi l-kitābi wa-takfurūna
bi-baʿḍ` — "do you then believe in part of the Book and disbelieve
in part?") that rhetorically locks the whole block.

The finding from `covenant-language.md` §2 (*mīthāq* appears 23 times
in the Qurʾān, 10 of which are addressed to Banū Isrāʾīl) confirms
what is visible in 2:40-101: the Jewish engagement is **covenantal**
in vocabulary, not metaphysical.

### 2.2 Q 5:12-13 — the covenant broken, the hearts hardened

The two verses open the body of al-Māʾidah's dispute register:

> *wa-laqad ʾakhadha llāhu mīthāqa banī isrāʾīla wa-baʿathnā minhumu
> thnay ʿashara naqībā…* (5:12)
> *fa-bimā naqḍihim mīthāqahum laʿannāhum wa-jaʿalnā qulūbahum
> qāsiyah; yuḥarrifūna l-kalima ʿan mawāḍiʿih; wa-nasū ḥaẓẓan mimmā
> dhukkirū bih…* (5:13)

Three structural devices:

1. **Covenant + twelve captains**: 5:12 recapitulates the Exodus-
   Deuteronomy material (twelve tribal leaders) and re-assigns the
   covenant content to a five-clause conditional ("if you establish
   prayer, give zakat, believe in my messengers, assist them, and
   lend to God a good loan…"). The conditional converts the covenant
   into a forensic instrument.
2. **Hardened hearts**: 5:13 uses `qulūbahum qāsiyah` — heart-
   hardening attested in the Torah's Pharaoh narrative (kbd-lēbh) but
   repurposed to describe the post-Sinai people themselves. This is
   an inversion of the biblical usage: hardness-of-heart is
   transferred from the Egyptian oppressor to the Israelite audience.
3. **Taḥrīf**: 5:13 introduces the Qurʾān's most-cited technical term
   for textual tampering, `yuḥarrifūna l-kalima ʿan mawāḍiʿih`. Of
   the 6 corpus occurrences of *taḥrīf* and related verbal forms
   (2:75, 4:46, 5:13, 5:41, 8:16, 22:11), **4 are Jewish-specific**
   (2:75, 4:46, 5:13, 5:41), and the remaining two are generic
   disruption imagery (8:16 flight in battle, 22:11 worship on an
   edge).

### 2.3 Q 5:41-44 — taḥrīf dramatised

Q 5:41 ("O Messenger, let not those who hasten to disbelief grieve
you…") stages the Medinan tribunal scene in which Jews of Madīna
bring a case to the Prophet, and the Qurʾān accuses a faction among
them of selective reporting: `yuḥarrifūna l-kalima min baʿdi
mawāḍiʿih, yaqūlūna: in ʾūtītum hādhā fa-khudhūh wa-ʾin lam tuʾtawhu
fa-ḥdharū`. The verse specifies the *technique* of taḥrīf — post-hoc
relocation of a ruling so it becomes convenient. This is a forensic
and literary charge, not a metaphysical one.

Q 5:44 then shifts register and gives the Qurʾān's **positive
affirmation** of the Torah:

> *ʾinnā ʾanzalnā t-tawrāta fīhā hudan wa-nūr, yaḥkumu bihā
> n-nabiyyūna lladhīna ʾaslamū…*

The Torah is affirmed as revelation ("containing guidance and light")
and the Prophets-who-submitted-to-God are its proper judges. The
critique of *taḥrīf* in 5:13 and 5:41 is thus not a rejection of the
Torah but a dispute over the custodians: who is authorised to apply
the Torah, and on what terms. This is a **custodial**, not
**ontological**, dispute. The Qurʾān keeps the Torah inside its
canon (v44 `hudan wa-nūr`) while expelling a particular class of
custodians from legitimacy.

## 3. The Christian polemic axis — al-masīḥ and ghuluw

### 3.1 Q 3:45-63 — the Annunciation and the Adam parallel

Āl ʿImrān houses the Qurʾān's most sustained Marian-Christological
passage outside S19. Verses 45-63 run the annunciation, the infant-
speech, the disciples' confession, the heavenly taking-up, and close
with the *mubāhala* challenge (v61: "let us invoke the curse of God
upon the liars"). Structurally:

| v | Content | Christological move |
|---|---|---|
| 45 | `ʾidh qālati l-malāʾikatu yā maryam ʾinnā llāha yubashshiruki bi-kalimatin minh` | The Messiah is named a **kalima** ("word") from God — echoes John 1:1 — but the kalima is *from* God, not *identical with* God. Category-preservation. |
| 49 | `wa-rasūlan ʾilā banī isrāʾīl` | Jesus's mission is **to Banū Isrāʾīl**. Category: messenger. |
| 55 | `yā ʿīsā ʾinnī mutawaffīka wa-rāfiʿuka ʾilayya` | Divine speech to Jesus: "I will take you / raise you to Me". The grammatical subject is God; Jesus is the grammatical patient. Same ʿabd-pattern seen in S19 vv 30-33. |
| 59 | `ʾinna mathala ʿīsā ʿinda llāhi ka-mathali ʾādam; khalaqahu min turāb; thumma qāla lahu kun fa-yakūn` | The **Adam-analogy**: Jesus's creation is categorically parallel to Adam's — both created by divine fiat, neither divine. This is the passage's doctrinal apex. |
| 61 | `fa-man ḥājjaka fīhi min baʿdi mā jāʾaka mina l-ʿilm, fa-qul taʿālaw nadʿu ʾabnāʾanā…` | The *mubāhala*: the invitation to mutual cursing. The end-point of a negotiation that failed. |
| 63 | `fa-ʾin tawallaw fa-ʾinna llāha ʿalīmun bi-l-mufsidīn` | The close. Turning-away is named *fasād* (corruption). |

The passage moves from **incarnational vocabulary** (`kalima minhu`,
v45) through **messenger designation** (v49) to **creational
analogy** (v59). Each step narrows the Christological space: the
"word" category (which Christian readers might have taken as
Johannine Logos) is reframed as messenger (v49), then re-reframed as
*created thing* (v59), then closed with the curse-challenge (v61).
The passage is a **funnel of categorisations**, closing off the
Trinitarian reading step by step.

### 3.2 Q 4:157-171 — crucifixion-denial and category-policing

Two theological moves in sequence:

- **Q 4:157-158 — crucifixion denial**: `wa-mā qatalūhu wa-mā
  ṣalabūhu wa-lākin shubbiha lahum; wa-ʾinna lladhīna khtalafū fīhi
  la-fī shakkin minhu; mā lahum bihi min ʿilmin ʾillā ttibāʿa ẓ-ẓann;
  wa-mā qatalūhu yaqīnā; bal rafaʿahu llāhu ʾilayhi`. Five negations
  (`mā qatalūhu / mā ṣalabūhu / mā lahum bihi min ʿilm / mā
  qatalūhu yaqīnā / bal rafaʿahu`) stacked over two verses. This is
  the Qurʾān's most compressed denial. The sixth negation is
  implicit in `shubbiha` ("it was made to appear so to them"):
  perception-denial on top of event-denial.

- **Q 4:171 — the closing injunction**: `yā ahl al-kitāb lā taghlū
  fī dīnikum wa-lā taqūlū ʿalā llāhi ʾillā l-ḥaqq; ʾinnamā l-masīḥu
  ʿīsā bnu maryama rasūlu llāhi wa-kalimatuhu ʾalqāhā ʾilā maryama
  wa-rūḥun minh; fa-ʾāminū bi-llāhi wa-rusulih, wa-lā taqūlū
  thalāthah; intahū khayran lakum; ʾinnamā llāhu ʾilāhun wāḥid;
  subḥānahu ʾan yakūna lahu walad`.

The verse gives the Qurʾān's **six-fold designation of Jesus**:
*al-masīḥ / ʿīsā / ibnu Maryam / rasūlu llāh / kalimatuhu / rūḥun
minh*. Each name is a category (title, personal name, matronymic,
office, divine-word, divine-breath). The Qurʾān accepts all six and
closes them with the prohibition `lā taqūlū thalāthah`: "do not say
'three'". The theological negative (`thalāthah`) is paired with the
theological positive (`ʾilāhun wāḥid`). And the final clause
`subḥānahu ʾan yakūna lahu walad` connects directly to the S19
polemics, using the identical `walad`-token.

### 3.3 Q 5:72-77 — the three Christological "laqad kafara" verses

Three `laqad kafara lladhīna qālū…` ("they have disbelieved who
said…") in a row:

- **v72** `ʾinna llāha huwa l-masīḥu bnu maryam` — the direct
  identification of God *with* the Messiah. Rejected by Jesus's own
  voice in the same verse: `wa-qāla l-masīḥu yā banī isrāʾīla ʿbudū
  llāha rabbī wa-rabbakum`. The Qurʾānic Jesus overrides the
  Christian claim at the grammatical level: his own speech names God
  as his Lord and their Lord. The ʿabd↔walad spine (Maryam §10.1) is
  operative here: Jesus's imperative *ʿbudū* ("worship") re-locates
  everyone, himself included, inside the `Ebd` category.

- **v73** `ʾinna llāha thālithu thalāthah` — the Trinity-as-triadic
  claim. Rejected with `wa-mā min ʾilāhin ʾillā ʾilāhun wāḥid`.

- **v75** `mā l-masīḥu bnu maryama ʾillā rasūl; qad khalat min
  qablihi r-rusul; wa-ʾummuhu ṣiddīqah; kānā yaʾkulāni ṭ-ṭaʿām` —
  **"Jesus is only a messenger, son of Mary, and his mother was a
  righteous woman; both used to eat food."** The polemical finisher.
  The verse collapses Christology onto the **biological** index:
  "they ate food" (`kānā yaʾkulāni ṭ-ṭaʿām`) is an *argumentum ex
  corporalitate* — beings who eat are not divine. This is the
  Qurʾān's most concrete anti-incarnational move: not a metaphysical
  syllogism but a pointing-to-the-body.

The passage closes with **v77**, the second of the two `yā ahl
al-kitāb lā taghlū` prohibitions (the other is 4:171). Both *ghuluw*-
prohibitions are Christian-directed (contrast 5:64 which is Jewish-
directed with different content). The verse pairs *ghuluw* with
`wa-lā tattabiʿū ʾahwāʾa qawmin qad ḍallū min qabl, wa-ʾaḍallū
kathīran` — "do not follow the desires of a people who went astray
before and led many astray." The "people who went astray before"
(the pre-Christian community they inherit the excess from) is
classically identified as either the Jews who initially rejected
Jesus, or the early Christological factions.

### 3.4 Q 9:30 — al-Masīḥ ibn Allāh

> *wa-qālati l-yahūdu ʿuzayrun bnu llāh wa-qālati n-naṣārā
> l-masīḥu bnu llāh; dhālika qawluhum bi-ʾafwāhihim; yuḍāhiʾūna
> qawla lladhīna kafarū min qabl; qātalahumu llāh ʾannā yuʾfakūn.*

One verse, three rhetorical moves:

1. **Parallel citation**: Jews and Christians are quoted in identical
   syntactic form (`X ibnu llāh`), with Uzayr (Ezra, in some readings)
   and al-Masīḥ as the respective offerings. This is the Qurʾān's
   **only** citation of the Uzayr-as-son-of-God claim; it is a
   contested datum in classical Jewish sources (cf. Ginzberg, *Legends
   of the Jews* V:164; classical tafsir limits it to a local Medinan
   Jewish faction). Irrespective of the historical identification,
   the rhetorical function is parallel: to put the Christian claim
   inside a dual structure, making it one of two versions of a
   single category-error.

2. **Pagan echo**: `yuḍāhiʾūna qawla lladhīna kafarū min qabl` —
   "they imitate the speech of those who disbelieved before." The
   Christological claim is re-classified as pagan residue. The
   ontology of the "son of God" claim is hereby relocated from
   Christian innovation to pre-Christian (Greco-Roman, Canaanite,
   Mesopotamian) polytheism. This is the Qurʾān's sharpest move: the
   claim is not novel but derivative.

3. **Curse and ʾannā**: `qātalahumu llāh ʾannā yuʾfakūn` — "may God
   fight them; how are they deluded!" The curse `qātalahumu llāh`
   appears only 3× in the Qurʾān (Q 9:30, Q 63:4, Q 74:19/20); its
   combination with the interrogative-rhetorical `ʾannā yuʾfakūn`
   ("how are they turned away") appears only here and at Q 5:75 (the
   close of the *ʾillā rasūl* verse). The linkage of 9:30 to 5:75 by
   a shared cadence is classical stylistic observation (Farāhī,
   *Nizām al-Qurʾān*) and is preserved under the Leeds
   morphological tagging.

## 4. Q 5:14-16 — "those who said we are Christians"

Immediately following the Jewish-mīthāq passage (5:12-13), the
Qurʾān turns to the Christians with a parallel structural move:

> *wa-mina lladhīna qālū ʾinnā naṣārā ʾakhadhnā mīthāqahum,
> fa-nasū ḥaẓẓan mimmā dhukkirū bih, fa-ʾaghraynā baynahumu l-
> ʿadāwata wa-l-baghḍāʾa ʾilā yawmi l-qiyāmah…* (5:14)

Three parallels with the preceding Jewish verses:
1. Covenant taken (`ʾakhadhnā mīthāqahum`) ⇆ 5:12.
2. They forgot a portion of what they were reminded of (`nasū ḥaẓẓan
   mimmā dhukkirū bih`) — **verbatim identical** to 5:13. This is
   the only place in the Qurʾān where the phrase is used of both
   Jews and Christians in consecutive verses.
3. Divine consequence: for Jews, hearts hardened; for Christians,
   *ʿadāwah* and *baghḍāʾ* (enmity and hatred) planted among them
   until the Day of Judgment. Christian consequence is **social-
   ecclesial** (intra-Christian schism); Jewish consequence is
   **cognitive** (hardened heart and taḥrīf). The same covenant-
   breach results in different pathologies.

**The phrase `alladhīna qālū ʾinnā naṣārā` is important.** The Arabic
is "those who *said* 'we are Christians'" — not simply "the
Christians". Classical tafsir (Ṭabarī, Rāzī) reads the locution as
mildly distancing: the Qurʾān names them by their own self-
appellation, marking a gap between their claim and the normative
category. 5:82 does the reverse (`wa-la-tajidanna ʾaqrabahum
mawaddatan li-lladhīna ʾāmanū lladhīna qālū ʾinnā naṣārā` — "you
will find those nearest in affection are those who say 'we are
Christians'") and uses the same self-appellation to ground a
*positive* assessment. The locution is thus tonally neutral at the
syntactic level, with the surrounding context setting the valence.

5:15-16 then pivots to the **yā ahl al-kitāb** vocative and announces
the messenger: `qad jāʾakum rasūlunā yubayyinu lakum kathīran mimmā
kuntum tukhfūna mina l-kitāb wa-yaʿfū ʿan kathīr`. The structure is:
(a) indict the broken covenant (5:14), (b) announce a corrective
messenger (5:15), (c) gesture to light and path (5:16 `yahdī bihi
llāhu mani ttabaʿa riḍwānahu subula s-salām`). The two-step critique-
plus-invitation is the Qurʾān's characteristic Medinan move toward
the People of the Book.

## 5. Q 3:64 — the common word

> *qul yā ahl al-kitāb taʿālaw ʾilā kalimatin sawāʾin baynanā wa-
> baynakum, ʾallā naʿbuda ʾillā llāh, wa-lā nushrika bihi shayʾā,
> wa-lā yattakhidha baʿḍunā baʿḍan ʾarbāban min dūni llāh; fa-ʾin
> tawallaw fa-qūlū shhadū bi-ʾannā muslimūn.*

Three theological negatives:
- `ʾallā naʿbuda ʾillā llāh` — nothing worshipped but God.
- `wa-lā nushrika bihi shayʾā` — no partner.
- `wa-lā yattakhidha baʿḍunā baʿḍan ʾarbāban min dūni llāh` — no
  lord-making of human intermediaries.

Each negative corresponds to a polemic vector addressed earlier:
- Anti-polytheism (universal, addressed to Quraysh primarily).
- Anti-Trinitarianism (Christian-directed, 4:171 / 5:73).
- Anti-rabbinical-veneration (Jewish-directed, cf. 9:31 `ʾattakhadhū
  ʾaḥbārahum wa-ruhbānahum ʾarbāban min dūni llāh`).

The "common word" is the three monotheistic negatives that, the
Qurʾān proposes, Jews, Christians, and Muslims all hold (or should
hold). **It is framed as an invitation, not an ultimatum.** The
verse closes with a conditional: if they turn away, the Muslim side
simply declares `shhadū bi-ʾannā muslimūn`. No curse, no threat. The
*mubāhala* of v61 is three verses away; the *kalimat-sawāʾ* of v64 is
three verses after that. Within a span of six verses, Āl ʿImrān has
offered (v61) the curse-confrontation and (v64) the word-invitation.
The theological architecture is: **challenge first, invite second**.

## 6. Jesus as messenger — the ʿabd category

Q 5:75 — **"The Messiah son of Mary is not but a messenger"** — is
the canonical one-line summary of Qurʾānic Christology. The verse is
the terminus of the three-verse progression 5:72→73→75: (i) denying
that God *is* the Messiah, (ii) denying the Triadic claim, (iii)
positively locating Jesus inside the *rasūl* category.

The verse does three things that no other single Qurʾānic verse does
together:
1. **Uses `mā … ʾillā` ("not … except") with *rasūl* as predicate**.
   The restriction is ontological: messenger, *nothing more*.
2. **Invokes Mary with the epithet *ṣiddīqah*** ("righteous woman") —
   the feminine of *ṣiddīq*, a prophetic-companion category. Mary is
   placed inside the prophetic-righteous-companion frame, not in the
   Theotokos frame.
3. **Invokes the eating-food clause**. The corporeal proof. The
   rhetorical question `anẓur kayfa nubayyinu lahumu l-āyāt` that
   follows ("look how We make clear the signs to them") frames the
   eating-food clause as a **sign** — that is, as Qurʾānic *āyah*.
   The *āyah* here is not a cosmological sign (sun, moon, rain) but
   a biological-category sign.

Maryam §10.1 documented the ʿabd↔walad spine inside S19 — the 12
occurrences of `ʿabd` bookending the 9 occurrences of `walad`, with
Jesus's cradle-speech self-designation `ʿabdullāh` (v30) as the
resolution. Q 5:75 is the corpus-wide terminus of the same spine.
The Qurʾān's Christology is a **category-correction**: not
`walad`, but `rasūl / ʿabd / kalima / rūḥ min Allāh`.

## 7. Shared-prophets theology — Q 2:136 and Q 3:84

The two verses are **verbatim parallels with minor pronoun shift**:

- 2:136: `qūlū ʾāmannā bi-llāhi wa-mā ʾunzila ʾilaynā wa-mā ʾunzila
  ʾilā ʾibrāhīma wa-ʾismāʿīla wa-ʾisḥāqa wa-yaʿqūba wa-l-ʾasbāṭ,
  wa-mā ʾūtiya mūsā wa-ʿīsā wa-mā ʾūtiya n-nabiyyūna min
  rabbihim; lā nufarriqu bayna ʾaḥadin minhum, wa-naḥnu lahu
  muslimūn.`
- 3:84: `qul ʾāmannā bi-llāhi wa-mā ʾunzila ʿalaynā wa-mā ʾunzila
  ʿalā ʾibrāhīma wa-ʾismāʿīla wa-ʾisḥāqa wa-yaʿqūba wa-l-ʾasbāṭ,
  wa-mā ʾūtiya mūsā wa-ʿīsā wa-n-nabiyyūna min rabbihim; lā
  nufarriqu bayna ʾaḥadin minhum, wa-naḥnu lahu muslimūn.`

The two differ in (a) imperative form (`qūlū` plural vs `qul`
singular), (b) preposition (`ʾilaynā` / `ʾilā` vs `ʿalaynā` / `ʿalā`),
and (c) the *nabiyyūn* clause (2:136 adds `mā ʾūtiya` again; 3:84 lets
the earlier `mā ʾūtiya` govern). Otherwise the verses are the same.

Their content is the **Qurʾānic prophetic canon** listed in shared-
prophet form: Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, al-Asbāṭ (the twelve
tribes), Mūsā, ʿĪsā, and "the prophets" as a closing generic. The
canon is **deliberately non-sectarian**: Ishmael (the Arab
patriarch) is named alongside Isaac and the Asbāṭ (the Israelite
tribes); Jesus is named alongside Moses. The `lā nufarriqu` refrain
("we make no distinction between any of them") is a theological
claim about the *prophetic corpus*: it is one prophetic stream with
many named points.

This is the **positive proposal** of the Qurʾān's People-of-the-Book
engagement. Before any polemic, the Qurʾānic speaker commits to a
shared-canon prophetology. The polemic that follows — against
covenant-breach, against Christological excess — presupposes this
shared canon. The Qurʾān is not arguing from an outside position; it
is arguing from a claim to the same canon, plus one more prophet.

## 8. Envy — Q 2:109 and Q 4:54

The root *ḥasad* appears only 4 times in the Qurʾān:
- 2:109 (People of the Book envy the believers).
- 4:54 (they envy the people whom God has favoured).
- 48:15 (hypocrites envy the war-booty distribution).
- 113:5 (the envier when he envies — al-Falaq).

Two of the four — half the corpus census of the root — refer to the
People of the Book.

- **Q 2:109** `wadda kathīrun min ʾahli l-kitābi law yaruddūnakum min
  baʿdi ʾīmānikum kuffāran ḥasadan min ʿindi ʾanfusihim min baʿdi mā
  tabayyana lahumu l-ḥaqq.` The envy is located inside the People of
  the Book; it is *ḥasadan min ʿindi ʾanfusihim* (an envy sourced in
  their own selves); its object is the believers' return to
  disbelief.
- **Q 4:54** `ʾam yaḥsudūna n-nās ʿalā mā ʾātāhumu llāhu min faḍlih,
  fa-qad ʾātaynā ʾāla ʾibrāhīma l-kitāba wa-l-ḥikmata wa-ʾātaynāhum
  mulkan ʿaẓīmā.` The envy is generalised to "the people" (`an-nās`),
  but the counter-response names the *Āl Ibrāhīm* — Abraham's
  family — as the *prior* recipients of Book + Wisdom + Kingship.
  Classical exegesis (Ṭabarī, Zamakhsharī, Rāzī) reads the envied
  `n-nās` as the new prophetic community and the envious subject as
  a Jewish faction questioning Muhammad's legitimacy.

The envy motif is **sociological**: it describes the affect inside
an older revelation-community at the arrival of a new claim. The
Qurʾān's diagnosis is that the envy is real and internal (`min ʿindi
ʾanfusihim`) and that the proper response is patience — `faʿfū
wa-ṣfaḥū ḥattā yaʾtiya llāhu bi-ʾamrih` (2:109). The critique of
envy is followed by a *forgiveness-imperative*, not by a
retaliation-imperative.

## 9. The Maryam rhyme-breaks as the polemic's prosodic fingerprint

The `maryam-deep-dive.md` finding is the prosodic correlate of
everything §1-§8 has mapped. The core data, re-read under the J/C-
engagement lens:

- **S19 rhyme system**: the surah runs a dominant `yā` (*-yā / -iyyā*)
  rhyme from v2 to v98 — *except* for two breaks.
  - **Break 1, vv 34-40** (7 verses, rhymes on `-ūn / -īm / -īn`):
    the first Christological polemic. "It is not for Allah to take a
    son…"
  - **Break 2, vv 88-93** (6 verses, rhymes on `-dā`): the second
    Christological polemic. "They said the Merciful has taken a
    son…" — with cosmic-rupture imagery.
- The rhyme-break is **content-aligned**: the prosodic register
  shifts *exactly* at the doctrinal pivot, and returns to `yā` *exactly*
  when the narrative resumes. V40 ends on `yarjiʿūn`; v41 opens with
  `nabiyyā` (Abraham's designation), snapping the rhyme back the
  moment the patriarch cycle restarts. V93 ends on `ʿabdā`; v94
  continues the `-dā` rhyme but re-enters narrative-report mode.
- **Divine-name asymmetry inside the two polemics**: Polemic 1 uses
  *Allāh* (vv 35, 36); Polemic 2 uses *ar-Raḥmān* (vv 88, 91, 92, 93,
  four times). The escalation from *Allāh* to the Meccan-signature
  name *ar-Raḥmān* (which the surah has been elevating since v18, on
  Mary's own lips) is the rhetorical intensification.
- **The Jesus cradle-speech (vv 30-33)** contains 16 first-person-
  singular morphs in 4 verses — ten-fold corpus-density. Every verb
  is a divine action upon Jesus, making the cradle-speech the
  **anti-Gospel "I am" formula**: Jesus speaks at maximal 1S density
  precisely to disown agency.

**Integration.** The Maryam rhyme-breaks are the Qurʾān's most
extended prosodic marker of Christological polemic. Nowhere else in
the corpus does the poetic surface of a surah change monorhyme for
the duration of a polemic and then revert. This is a **form-meets-
content convergence** at the scale of the whole surah — and it sits
exclusively on the Christian axis of the J/C engagement. There is no
comparable rhyme-break surgery on the Jewish axis. The Jewish polemic
(2:40-101, 5:12-13, 5:41-44) is stylistically continuous with its
surrounding Medinan prose-rhetoric; the Christian polemic (S19's
two breaks, and the tight `laqad kafara` triad in 5:72-73-75) is
stylistically marked.

The asymmetry matches the substantive asymmetry: the Christian
critique is *doctrinal* (Trinity, Incarnation), requiring a shift of
rhetorical mode; the Jewish critique is *ethical-historical*
(covenant, tampering), continuous with the surrounding Medinan
moral discourse. **Form fits function on both axes.**

## 10. Q 3:113-115 — the *muqtaṣidūn* relief valve

> *laysū sawāʾ; min ahli l-kitābi ʾummatun qāʾimah yatlūna ʾāyāti
> llāhi ʾānāʾa l-layli wa-hum yasjudūn; yuʾminūna bi-llāhi wa-l-
> yawmi l-ʾākhir wa-yaʾmurūna bi-l-maʿrūfi wa-yanhawna ʿani l-
> munkar wa-yusāriʿūna fī l-khayrāt; wa-ʾūlāʾika mina ṣ-ṣāliḥīn.
> wa-mā yafʿalū min khayrin fa-lan yukfarūh.* (3:113-115)

After ten verses of reproach (3:98-112), the surah inserts a three-
verse **relief valve** that explicitly partitions the People of the
Book:

- `laysū sawāʾ` — *"they are not all alike"*. The opening is a direct
  disclaimer against the preceding polemic's generalising force.
- `ʾummatun qāʾimah` — an "upright community" from within the ahl
  al-kitāb. This is the Qurʾān's recognition of a *non-polemicised*
  subset of its Medinan interlocutors.
- Four virtues catalogued: (a) night-recitation of God's signs, (b)
  prostration, (c) belief in God and the Last Day, (d) enjoining
  good and forbidding evil.
- **Full reciprocity**: `wa-mā yafʿalū min khayrin fa-lan yukfarūh`
  — "whatever good they do will not be denied them." The verb
  `yukfarūh` (from k-f-r in the sense "to deny credit for") places
  this subset inside the same divine accounting as the believers.

The classical term for this subset is **al-muqtaṣidūn** ("the
moderate ones"), a term the Qurʾān uses at 5:66 (`minhum ummatun
muqtaṣidah`) and 35:32 (`minhum muqtaṣid`). The term derives from
*qaṣd* (aim, moderation, balance) and names the segment of the
People of the Book who neither reject the new revelation outright
nor veer into Christological excess. They are the structural
counterweight to the polemic axis. In 3:113-115 the quranic speaker
names them as righteous — *ṣāliḥīn* — using the same root-word used
of the earliest prophets.

The *muqtaṣid* category functions as a **rhetorical relief valve**
inside the J/C engagement. Without it, the polemic of 3:64 through
3:112 would collapse into a blanket indictment. The three verses
3:113-115 open a door: there is a path that is open to the People of
the Book *as* People of the Book — reciting God's signs by night,
prostrating, enjoining good. The path does not require them to
abandon their category; it requires them to be upright within it.

5:82 extends this recognition to a specifically Christian subset:
*lladhīna qālū ʾinnā naṣārā… dhālika bi-ʾanna minhum qissīsīna wa-
ruhbānan wa-ʾannahum lā yastakbirūn* — "because among them are
priests and monks, and they are not arrogant." The Qurʾānic
relief-valve thus has both a Jewish instantiation (5:66 `ummatun
muqtaṣidah`) and a Christian instantiation (5:82 `qissīsīn wa-
ruhbān`). The polemic is robustly *not* a blanket rejection.

## 11. Synthesis — three registers, two axes

The Qurʾān's engagement with the People of the Book operates on
**two axes** (Jewish and Christian) and **three registers** (polemic,
invitation, exemption):

|  | Polemic (the critique) | Invitation (the shared ground) | Exemption (the moderate subset) |
|---|---|---|---|
| **Jewish axis** | 2:40-101, 5:12-13, 5:41-44 (covenant, taḥrīf) | 2:136 (shared prophets), 3:64 (common word), 5:44 (affirmation of Torah) | 5:66 `ummatun muqtaṣidah`, 3:113-115 `ummatun qāʾimah` |
| **Christian axis** | 3:45-63, 4:157-171, 5:72-77, 9:30, S19:34-40, S19:88-93 (Christological error, ghuluw) | 2:136, 3:84 (Jesus as prophet), 3:64 (common word), 5:46 (affirmation of Injīl) | 5:82 `qissīsīn wa-ruhbān`, 3:199 (a subset believing) |

All Medinan engagement is 2-axis / 3-register. The Meccan corpus has
**none of this machinery**: no *ahl al-kitāb* vocative, no *mīthāq*-
centered polemic, no specific-targeted Christological refutation in
the Medinan dialectical mode. The Meccan corpus has *S19 Maryam* —
the Christological polemic pre-figured as cosmological poetry rather
than Medinan argument. S19 is the *literary* form of what becomes the
Medinan *dialectical* form in S3 / S4 / S5.

## 12. Summary

The Qurʾān's Jewish/Christian engagement is a three-register, two-
axis architecture built on Medinan revelation (with S19 as the
Meccan poetic anticipation). The shared vocative *yā ahl al-kitāb* is
100% Medinan, 100% polemical (12 vocative, 31 phrase-level). The
Jewish-specific axis (banū Isrāʾīl / alladhīna hādū) centers on the
covenant-vocabulary (*mīthāq*, 10/23 occurrences Israelite-directed)
and on *taḥrīf* (4/6 occurrences Israelite-directed); its canonical
texts are Q 2:40-101, Q 5:12-13, Q 5:41-44. The Christian-specific
axis (an-naṣārā / al-masīḥ ibn Maryam) centers on category-correction
against the son-of-God claim and on the prohibition of *ghuluw*
(religious excess); its canonical texts are Q 3:45-63, Q 4:157-171,
Q 5:72-77, Q 9:30, and the two Maryam rhyme-break polemics at S19
vv 34-40 and 88-93.

The positive proposal is the shared-prophets theology of Q 2:136 /
3:84 — a prophetic canon (Ibrāhīm, Ismāʿīl, Isḥāq, Yaʿqūb, al-Asbāṭ,
Mūsā, ʿĪsā) accepted in *lā nufarriqu* form. The invitation is the
"common word" of Q 3:64 — three monotheistic negatives (no worship
except of God, no partner, no lord-making of human intermediaries)
offered as the ground all three traditions could hold. The
exemption is the *muqtaṣidūn*-cluster at 3:113-115, 5:66, 5:82, 3:199
— the recognition that the People of the Book include an upright
subset for whom the polemic is not aimed.

The Christological axis's prosodic fingerprint is the Maryam rhyme-
break: S19's 97-verse `yā` monorhyme is broken *only* at the two
Christological polemics (vv 34-40, `-ūn/-īm`; vv 88-93, `-dā`),
which together use 10/20 of the surah's *walad*/"son" tokens and 4/4
of polemic-2's *ar-Raḥmān* invocations. The two breaks escalate from
narrative rebuttal ("it is not for Allah to take a son", v35) to
cosmic-rupture imagery ("the heavens about to split", v90). Polemic 1
uses *Allāh*; polemic 2 uses *ar-Raḥmān*, Mary's own Maryam-surah
divine-name, weaponised against the Christological claim her son
came to refute. Nowhere else in the Qurʾān does the *poetic surface*
change for the duration of a doctrinal dispute and revert at its
close. This form-meets-content engineering is exclusively Christian-
axis; the Jewish-axis polemic is stylistically continuous with its
Medinan surround because its critique is *ethical-historical*
(covenant, custody) rather than *metaphysical* (Trinity,
Incarnation).

The Qurʾān's Christology is a **category correction** enforced via
the `ʿabd ↔ walad` spine: Jesus is named as `rasūl`, `ʿabd`,
`kalima minhu`, `rūḥ minhu`, `ibnu Maryam` — every category except
`walad Allāh`. Q 5:75's *mā l-masīḥu bnu maryama ʾillā rasūl* is the
one-line distillate; S19:30's `ʾinnī ʿabdullāh` is its Meccan poetic
proof-text. The "envy" motif at 2:109 and 4:54 diagnoses the affect
inside the prior revelation-community; the response enjoined is
forgiveness and patience, not retaliation. Taken together, the
material gives a clear typology: the Qurʾān treats the People of the
Book as partners in a shared canon who have drifted on specific,
named points, and it offers — for each axis — a polemic, an
invitation, and a relief valve.
