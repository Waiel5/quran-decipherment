---
phase: C
finding_id: phase-c-ring-center-semantics-run-1
date: 2026-04-12
agent: deep-reader
status: reported
claim_class: literary / theological
depends_on: phase-c-chiastic-audit-run-1
rules:
  orthography: no-tashkeel for Arabic; Saheeh International for English
  word_definition: lemma-root (QAC triliteral)
  basmala_policy: counted-only-in-surah-1 (upstream from chiastic-audit)
  verse_numbering: hafs-kufan
inputs:
  chiastic_audit: findings/phase-c-structures/chiastic-audit.md
  chiastic_json:  analysis/notebooks/chiastic_audit_results.json
  text:           quran-text/quran-no-tashkeel.json
  translation:    data/translations/en.sahih.txt
  morphology:     data/morphology/quranic-corpus-morphology-0.4.txt
---

# Ring-Center Semantics — What the Quran Puts at the Middle

## 0. Why centers matter

Classical ring-composition theory (Douglas 2007; Cuypers 2009/2015; Farrin
2014) treats the geometric middle of a chiasmus as the *semantic pivot*: the
sentence the rhetorical envelope is built around, the thesis the whole frame
is meant to underline. If the Quran's rings are real — and at least four
sub-surah rings plus Hud's whole-surah ring survived the chiastic-audit's
statistical tests — then the middle verses of those rings should be where
the text says what it most wants to say. This document reads the centers.

Method: from `chiastic_audit_results.json` I extracted, for every one of the
114 surahs, the midpoint verse (odd N) or the two verses straddling the
midpoint (even N). For each I pulled the Arabic and the Saheeh English, the
QAC root set, and, where relevant, the surrounding context. I then
categorised the 114 centers thematically and compared the top ring-z tier to
the bottom tier.

This is deliberately a **content** analysis built on top of the
chiastic-audit's purely lexical metric. The audit told us *where* the
geometric middles lie; this document asks *what* is there.

## 1. Top-20 ring centers with full text

| # | surah | N | z | centre | Saheeh English of centre verse(s) | category |
|---:|---|---:|---:|---|---|---|
| 1 | 59 Al-Hashr | 24 | +2.42 | 12/13 | "If they are expelled, they will not leave with them… You [believers] are more fearful within their breasts than Allah. That is because they are a people who do not understand." | psychological-theological contrast |
| 2 | 11 Hud | 123 | +2.40 | **62** | "They said, 'O Salih, you were among us a man of promise before this. Do you forbid us to worship what our fathers worshipped? And indeed we are, about that to which you invite us, in disquieting doubt.'" | prophet-rejection pivot |
| 3 | 95 At-Tin | 8 | +2.33 | 4/5 | "We have certainly created man in the best of stature; / Then We return him to the lowest of the low" | anthropological reversal |
| 4 | 16 An-Nahl | 128 | +2.27 | 64/65 | "And We have not revealed to you the Book, [O Muhammad], except for you to make clear… / And Allah has sent down rain from the sky and given life thereby to the earth…" | revelation-as-mercy / sign-in-nature |
| 5 | 69 Al-Haqqah | 52 | +2.06 | 26/27 | "'And had not known what is my account. / I wish my death had been the decisive one.'" | eschatological regret |
| 6 | 109 Al-Kafirun | 6 | +1.94 | 3/4 | "Nor are you worshippers of what I worship. / Nor will I be a worshipper of what you worship." | theological incommensurability |
| 7 | 46 Al-Ahqaf | 35 | +1.73 | 18 | "Those are the ones upon whom the word has come into effect… among nations which had passed on… Indeed, they [all] were losers." | eschatological warning |
| 8 | 92 Al-Layl | 21 | +1.68 | 11 | "And what will his wealth avail him when he falls?" | moral-economic pivot |
| 9 | 70 Al-Ma'arij | 44 | +1.29 | 22/23 | "Except the observers of prayer — those who are constant in their prayer" | moral imperative (positive) |
| 10 | 56 Al-Waqi'ah | 96 | +1.24 | 48/49 | "'And our forefathers [as well]?' — Say, 'Indeed, the former and the later peoples…'" | resurrection dispute |
| 11 | 50 Qaf | 45 | +1.19 | 23 | "And his companion, [the angel], will say, 'This [record] is what is with me, prepared.'" | eschatological judgement |
| 12 | 63 Al-Munafiqun | 11 | +1.14 | 6 | "It is all the same for them whether you ask forgiveness for them or do not… Allah does not guide the defiantly disobedient people." | covenantal rupture |
| 13 | 48 Al-Fath | 29 | +1.12 | 15 | "Those who remained behind will say when you set out toward the war booty… 'Let us follow you.' They wish to change the words of Allah…" | test of allegiance |
| 14 | 27 An-Naml | 93 | +1.08 | 47 | "'We consider you a bad omen…' He said, 'Your omen is with Allah. Rather, you are a people being tested.'" | divine-test pivot |
| 15 | 23 Al-Mu'minun | 118 | +1.03 | 59/60 | "And they who do not associate anything with their Lord / And they who give what they give while their hearts are fearful because they will be returning to their Lord" | theological core (tawhid + piety) |
| 16 | 49 Al-Hujurat | 18 | +0.99 | 9/10 | "And if two factions among the believers should fight… The believers are but brothers, so make settlement between your brothers. And fear Allah that you may receive mercy." | **moral-communal imperative** |
| 17 | 89 Al-Fajr | 30 | +0.89 | 15/16 | "As for man, when his Lord tries him… he says, 'My Lord has honored me.' / But when He tries him and restricts his provision, he says, 'My Lord has humiliated me.'" | anthropological diagnosis |
| 18 | 85 Al-Buruj | 22 | +0.89 | 11/12 | "Indeed, those who have believed and done righteous deeds will have gardens beneath which rivers flow… Indeed, the vengeance of your Lord is severe." | dual recompense |
| 19 | 41 Fussilat | 54 | +0.85 | 27/28 | "But We will surely cause those who disbelieve to taste a severe punishment… the Fire. For them therein is the home of eternity…" | eschatological warning |
| 20 | 22 Al-Hajj | 78 | +0.75 | 39/40 | "Permission [to fight] has been given to those who are being fought… [They are] those who have been evicted from their homes without right — only because they say, 'Our Lord is Allah.'" | covenantal protection |

The full 114-surah table is in the appendix. A first impression from the
top-20: the centers are **doing theological work even when the ring itself
is weak**. Five of twenty sit in the prophet-rejection / divine-trial
frame (Hud 62, An-Naml 47, At-Tin 4-5, Al-Fajr 15-16, Al-Ahqaf 18); four are
moral imperatives (Al-Ma'arij 22-23, Al-Hujurat 9-10, Al-Kafirun 3-4,
Al-Layl 11); four are eschatological verdicts (Al-Haqqah 26-27, Qaf 23,
Fussilat 27-28, Al-Buruj 11-12); three pivot on covenant, allegiance or
refuge (Al-Munafiqun 6, Al-Fath 15, Al-Hajj 39-40); three are
theological-core declarations (Al-Hashr 12-13 on divine presence, An-Nahl
64-65 on revelation as mercy, Al-Mu'minun 59-60 on non-shirk); one is
resurrection-dispute (Al-Waqi'ah 48-49).

That is already notable. If you drew twenty verses at random from the Quran
you would not expect this concentration of "decision-point" verses. But
before reading it as a finding I have to apply the pareidolia patrol
(§ 8).

## 2. Thematic categories

I categorised all 114 centers into six classes, with a seventh "mixed" bin
for verses that obviously straddle. Category counts across the full 114
catalog:

| category | count | share | note |
|---|---:|---:|---|
| eschatological warning / judgement | 31 | 27% | includes hell descriptions, record-book verses, regret speeches |
| moral imperative (prayer, justice, charity, brotherhood) | 21 | 18% | includes "except the observers of prayer", "make settlement between your brothers" |
| prophet-rejection / divine-trial pivot | 18 | 16% | the "they said, O Salih" formula and its cognates |
| theological core (tawhid, mercy, book, signs) | 16 | 14% | includes An-Nahl 65 (rain→life→sign), Al-Mu'minun 59 (non-shirk) |
| historical / narrative pivot | 14 | 12% | specific story beats (Joseph, Moses, Dhul-Qarnayn, Noah's son) |
| covenantal-communal pivot | 10 | 9% | Hujurat 9-10, Hajj 39-40, Munafiqun 6 |
| uncategorised / mixed | 4 | 4% | includes the three degenerate 3-verse surahs and At-Takwir 15 |

**The clear modal category is eschatological warning**, closely followed by
the "prophet rejected" speech-moment. Together these two categories account
for 43 of 114 center positions. That is almost twice what you'd get by
picking a random verse-stratum sample. The next two categories together —
moral imperative and theological core — pull another 32%. So roughly
75% of ring-center positions in the Quran, regardless of whether the
surah *is* actually a ring, sit on a theological or moral pivot.

**Caveat.** The percentages above are an artefact of two things stacked
together: (a) the Quran as a whole is dense with eschatology and moral
imperative, and (b) I am categorising verses by content, which is subjective.
A much harder test would be: take a *bag of verses* from each surah, pick
one at random, and ask what fraction are "theological pivots". I strongly
suspect it would be high too. So the categorisation on its own is not an
argument that the centers are *selected* — it is a descriptive catalogue
of what sits in the middle, which turns out to be, mostly, what the Quran
says about the things it talks about most. The *selection* argument has to
come from the z-ranking: do the high-z centers look more like pivots than
the low-z centers? I test that in § 8.

## 3. Al-Baqarah 131-144 — the strongest ring in the Quran

z = +9.69, window 14, center at verses 137-138. This is the one ring
structure whose statistical signal dwarfs everything else in the Quran and
which survives Bonferroni over 58k sub-surah windows by a wide margin.

Farrin's own reading places the pivot at **v143** ("We have made you a just
community that you will be witnesses over the people"). The qibla-change
verse proper is **v144**. My algorithmic midpoint of the 14-verse window
131-144 is **v137-138**. The three readings differ by four verses and each
is defensible:

**v137 (my mid-left).** *"So if they believe in the same as you believe in,
then they have been [rightly] guided; but if they turn away, they are only in
dissension, and Allah will be sufficient for you against them. And He is the
Hearing, the Knowing."*

**v138 (my mid-right).** *"[And say, 'Ours is] the religion of Allah
(ṣibghat Allāh). And who is better than Allah in [ordaining] religion? And
we are worshippers of Him."*

**v143 (Farrin's pivot).** *"And thus we have made you a just community
(ummatan wasaṭan) that you will be witnesses over the people and the
Messenger will be a witness over you. And We did not make the qiblah which
you used to face except that We might make evident who would follow the
Messenger from who would turn back on his heels…"*

**v144 (the mechanical qibla-change).** *"We have certainly seen the turning
of your face… So turn your face toward al-Masjid al-Haram…"*

Three things jump out. First: all four candidate centers (137, 138, 143, 144)
belong to the same semantic cluster — **the religion of Abraham is
identified with Islam, the community is given a boundary, the boundary is
made visible in space through the qibla change.** This is one thesis
distributed over seven verses, and whichever specific verse you call the
"middle" you land inside it. The pericope is a plateau, not a point.

Second: the pair **v137 ↔ v138** has a precise semantic complementarity
that recommends it as *the* pivot even against Farrin's v143. V137 is a
*negative* statement — "if they turn away, Allah will suffice you" — and
v138 is the corresponding *positive* declaration — "ours is the colouring
of Allah (ṣibghat Allāh), who is better than Allah in religion?" Together
they form a rejection-plus-affirmation couplet that is the ring's *thesis*.
V143 ("we have made you a just community") is the *consequence* of the
thesis: because the community holds the Abrahamic religion purely, it can
be a witness. V144 is the *sign* of the thesis: the qibla change proves the
new community boundary. The cadence of the whole pericope is *thesis
(137-138) → consequence (139-143) → ritual sign (144)*.

Third: the root that bookends the pericope most strongly is **mlt** (milla,
religion, community) and **Hnf** (incline toward truth, the classic
Abrahamic epithet). Both roots appear at v130, v135, v138, v140 — a tight
concentration in the center half of the ring. **Hnf** specifically is an
Abraham-word: he is the original *ḥanīf*. The ring is structured around
claiming the Abrahamic *ḥanīf* inheritance for the new community.

**Theological reading.** If the ring's geometric center is v137-138, then the
center-message is: *the faith of Abraham is the faith of the new community,
and the boundary is set by faith (belief-vs-turning-away) before it is set
by ritual (qibla).* The qibla change in v144 is the outward sign of an
inward theological fact already established two verses earlier. That is
exactly the order the rhetorical envelope is placing things in. Farrin
(2014) reads the same passage, places the pivot slightly later at the
"witness community" verse, and reaches a compatible but differently-framed
conclusion: that the community's vocation as *shahīd ʿalā al-nās* is the
ring's message. Both are plausibly there.

## 4. Al-Kahf 83-91 — Dhul-Qarnayn and the east-west inversion

z = +5.19, window 9, center at **v87**: *"He said, 'As for one who wrongs,
we will punish him. Then he will be returned to his Lord, and He will punish
him with a terrible punishment.'"*

The spatial frame of the ring is stark and obvious once you look for it:

```
v85 "So he followed a way"              (first way)
v86 "until he reached the setting of
    the sun" (maghrib)                 WEST (sunset)
v87 PUNISH-or-REWARD speech             <-- CENTER
v88 "as for one who believes…
    reward of Paradise"                 (balanced clause)
v89 "Then he followed a way"            (second way, same formula)
v90 "until he came to the rising of
    the sun" (mashriq)                 EAST (sunrise)
```

This is a textbook geographical chiasmus: west ↔ east about a moral axis.
And the *axis itself* is a verdict on justice — *al-ẓulm yustaḥaqq al-ʿadhāb*,
wrong-doing deserves punishment, believing-and-doing-righteousness deserves
paradise. Dhul-Qarnayn, placed between the setting and rising suns, makes
the moral pronouncement that is the whole point of the story. The
geographical envelope exists to *frame* the moral pronouncement at the
center; the sun-setting/sun-rising is scene-painting for a verdict.

The center verse uses the root **rbb** (Lord) and **Zlm** (wrong) and **rdd**
(return). Those three are the pivots: the wrongdoer *will be returned* to
his *Lord* for *punishment*. Note the doubling of the punishment verb:
Dhul-Qarnayn's punishment is temporal, the Lord's is "terrible". This is
the ring delivering a **two-tier justice theology** at its middle: human
justice now and divine justice later, and the human justice is only the
first iteration of the divine.

Dhul-Qarnayn is also structurally interesting as a *type* — the just ruler
stationed between opposing horizons. Cuypers-school reading would note that
the center figure is often a *mediator*, and the Dhul-Qarnayn center has
that shape exactly: an agent who stands between two extremes and dispenses
the verdict that holds them in balance.

## 5. Al-Qamar 21-30 — the Thamud refrain ring

z = +6.46, window 10, center at **v25-26**:

*v25.* "'Has the message been sent down upon him from among us? Rather, he
is an insolent liar (kadhdhābun ashir).'"

*v26.* "They will know tomorrow who is the insolent liar."

The window is framed at v21 and v30 by the identical refrain *fa-kayfa
kāna ʿadhābī wa-nudhur* ("And how [severe] were My punishment and warning")
which is one of the formal refrains of Al-Qamar. The 10-verse window opens
and closes with the same sentence; the whole structure is a refrain-enclosed
block.

The center is a **sharp, pointed exchange**: the Thamud call Salih an
"insolent liar", and God replies (in the next verse) that *they will know
tomorrow who the insolent liar is*. This is one of the most compact
prophecy-versus-denial pivots in the Quran. The two verses are almost
identical in wording — *kadhdhāb ashir* appears in both — but the subject of
the predicate reverses: in v25 the people apply it to Salih; in v26 God
applies it back to them. That subject-reversal is the center of the ring.

**Theological reading.** The chiastic center of the Thamud pericope puts
the *linguistic act of accusation* at the axis. The accusation is thrown
in v25 and reflected in v26, and the rest of the story — the she-camel
(v27-28), the hamstringing (v29), the destruction in the framing v30 — is
the *enactment* of who-was-right. The ring says: the question of truth is
settled not by the accusation but by the tomorrow. It is a very Quranic
theology of judgement-as-correction-of-earthly-speech.

## 6. ʿAbasa 1-9 — the rebuke pericope

z = +6.09, window 9, center at **v5**: *"As for he who thinks himself
without need (amma man istaghnā),"*

The center is a syntactic fragment — not a complete sentence — that
introduces the "rich disdainful man" clause. The completed couplet spans
v5-v6: *"As for he who thinks himself without need — to him you give
attention."* So v5 is structurally the exact middle of a 9-verse window
and semantically the *first half of the contrast* that runs v5-v10 (rich-
versus-poor, well-needing-versus-eager-to-learn).

What does the Quran put at the center of the famous rebuke? **The root
ghny** — self-sufficiency, thinking oneself without need. This is exactly
the vice the whole surah is correcting. It is not the Prophet's frown
(v1), nor the blind man coming (v2), nor the rhetorical question "what
makes you perceive" (v3-4) — it is the identification of **false
self-sufficiency** as the thing the Prophet must not privilege. The ring
center literally names the vice.

This is one of the cleanest cases in the whole catalog of the center
carrying the ring's **moral thesis**. The envelope is an embarrassing
narrative incident (the Prophet frowned at a blind man to attend to a rich
Qurayshī); the thesis at the center is *istighnāʾ is the diagnostic sin
(ghny), and the Prophet must not reinforce it.* Cuypers-school reading
would lean hard on this one: a structural center that is also a
single-word theological diagnosis is as close to "the message at the
middle" as literary criticism ever gets.

## 7. Hud as a whole-surah ring — the Salih center

z = +2.40 over N=123. Center verse = **v62**: the Thamud speaking to
Salih with their "disquieting doubt" about his message. Hud's highest-
scoring pair is v58 ↔ v66, which are near-identical salvation formulae
for Hud's people and Salih's people respectively: *"And when Our command
came, We saved X and those who believed with him by mercy from Us."*

**Why Salih at the center?** Hud is a prophet-cycle surah: Noah (v25-49) →
Hud (v50-60) → Salih (v61-68) → Abraham visitors (v69-76) → Lot (v77-83) →
Shu'ayb (v84-95) → Moses (v96-99), with Muhammad addressed throughout as
the inheritor of the sequence. Salih is the fourth of seven prophet
movements by position and the third of six major ones; he sits at the
geometric center. The ring's highest-strength pair (Hud 58 ↔ Salih 66)
mirrors the two *rescued peoples* across the Salih story — i.e., the Salih
narrative *itself* is the axis, and the Hud rescue and the Salih rescue
mirror each other through it. The center is a "centre-of-the-centre": the
Salih narrative is the middle of Hud, and Thamud's speech to Salih is the
middle of the Salih story.

**Theological reading.** The center verse captures the classic Quranic
*denial of continuity* — the people say to Salih *"you were a man of
promise (marjuw) among us before this; do you forbid us what our fathers
worshipped?"* That is the pivot-sentence of every prophet-rejection cycle
in the Quran: the prophet is called a turn-coat against ancestral
religion, and the doubt (shakk, root **ryb**) is what must be resolved.
Hud the surah — named after a prophet who is himself *not* the center —
puts at its center the accusation that all the prophets face. The surah's
organising theme is not "Hud's story" but "every prophet is rejected this
way, and God saves the one He sends."

## 8. What do the centers share? — the meta-center test

I computed the distribution of triliteral roots across the center verses of
all 114 surahs (using QAC 0.4 root fields). The top roots, with their
share of center-verses-in-which-they-appear:

| root | count (of 114 centers) | gloss |
|---|---:|---|
| **Alh** | 50 | Allah |
| qwl | 30 | to say |
| kwn | 25 | to be |
| **rbb** | 22 | Lord |
| **Amn** | 19 | to believe |
| Elm | 16 | to know |
| qwm | 15 | people / to stand |
| Ebd | 13 | to worship |
| ArD | 13 | earth |
| kfr | 12 | to disbelieve / cover |
| Aty | 11 | to come / give |
| rsl | 11 | messenger / to send |
| **rHm** | 10 | mercy |
| Ayy | 10 | sign / verse |
| Slw | 10 | prayer |

The **three most theologically loaded roots in the Quran — Alh, rbb, rHm —
all appear in the top 15**, with Alh in nearly half of all 114 centers.
But this is less striking than it looks: *Alh* appears in roughly 40% of
Quranic verses overall, so 50/114 (43%) of centers containing *Alh* is
right in line with the base rate. The center positions are **not**
preferentially *Allah*-dense. They are roughly average-Allah-dense.

**Two roots stand out as over-represented compared to a naive base rate**:
**rbb** (22/114 = 19% of centers) and **Amn** (19/114 = 17%). Both exceed
the whole-Quran per-verse rate (rbb ≈ 14%, Amn ≈ 12%). This is consistent
with the categorical reading in § 2: center verses are disproportionately
about *Lord–servant* and *belief–disbelief* axes. Those are the two axes of
prophet-rejection pericopes.

**A cluster that does NOT appear** in many centers is the *mercy cluster*
(rHm only 10 centers) — which is interesting given that Al-Fatihah's
center is v4 ("Sovereign of the Day of Recompense"), not v3 (the
*Raḥmān-Raḥīm* verse), and given that the rahma=114 root-count finding
suggests *rḥm* is somehow the Quran's global key. **Mercy is Quran-wide
but not ring-central**. What is ring-central is *lordship* (rbb) and
*faith vs denial* (Amn/kfr).

### 8.1 Does the z-ranking select for "pivot-looking" centers?

I tested: among the top-20 high-z centers, 8/20 contain *Alh*, 4/20
contain *rbb*, 3/20 contain *Amn*. Among the bottom-20 (most anti-ring)
centers, 9/20 contain *Alh*, 5/20 contain *rbb*, 3/20 contain *Amn*. The
distributions are indistinguishable. **Ring-z does not select for
theological-key roots at the center**. What it selects for is *symmetric
root repetition across the pair structure*, which is a different thing
entirely.

This is important. The *statistical* signal in the chiastic-audit is
driven by symmetry of lexical content around the center, not by what the
center *contains*. A center can be a theological pivot and the surrounding
verses can still fail to mirror it — in which case the ring-z is low. Or a
center can be a throwaway fragment (like ʿAbasa v5, a half-sentence) and
the surrounding envelope can nonetheless be tightly mirrored, producing a
high z. **Ring-z is a measure of envelope, not of message.**

That leaves two possible readings of the whole exercise:

1. *Separation reading.* The fact that ring-z does not correlate with
   theological-key density at the center means the centers are **not**
   especially privileged theological slots. Classical ring-theory hopes for
   a strong positive correlation (the center is the message); our metric
   finds a flat one. This weakens the "center = message" claim for the
   Quran as a whole.

2. *Independence reading.* The fact that *most* centers, regardless of
   ring-z, sit on theological pivots (§ 2's 75% figure) means the Quran's
   verses are **so theology-dense that picking any middle verse lands you
   on a pivot**. The chiasmus literature's "center is the message"
   intuition doesn't need the envelope to be detectable — the content is
   dense enough that the middle is always loaded.

I lean toward reading 2 with a caution from reading 1: the ring-composition
framework is not needed to predict that Quranic verse middles are
theological; the Quran's *content density* does that work. The four
Bonferroni-surviving rings remain genuinely interesting because they
couple content-pivot with envelope-symmetry, but the content-pivot alone
is cheap.

## 9. Cross-reference with rahma-114 and the 147 triple

The deep-hypotheses queue highlights two root-count coincidences as
possible global constants:

- **rahma = 114** (the lemma-count for raḥma = 114 across the Quran,
  matching the surah count).
- **147 triple**: three different roots — *ghayr*, *ilāh* (as the
  specific standalone lemma), *jannah* — each occurring 147 times.

Do the ring centers prefer these?

- **rHm appears at 10/114 ring centers.** That is 8.8%. The Quran-wide
  per-verse presence of rHm is ~8.0%. Ring centers are at base rate.
- **gyr appears at 1/114 centers, Ilh at 0/114, jnn at 5/114.** Base rates
  are gyr ≈ 3%, jnn ≈ 7%. Ring centers are at base rate or slightly
  below.

**Neither the rahma-114 root nor the 147-triple roots are preferentially
concentrated at ring centers.** If there is a "master theological theme"
at Quranic ring-middles, it is *rabb* (Lord) and *āmana* (believe), not
mercy and not the 147-triple roots. Those two roots are Quran-global
features, not ring-local ones.

That is a null finding worth naming: the quantitative root coincidences
and the structural ring-centers are **independent phenomena**. They do not
reinforce each other. If one wanted to argue for a unified "hidden
architecture", these would be two separate claims, each on its own merits.

## 10. Candidates just below Bonferroni — the next tier

The sliding-window scan produced 25 sub-surah hits above the inclusion
threshold. Four survive Bonferroni; the next-strongest eleven sit in the
z = 3.4–4.7 range. Their centers, read for content:

| # | surah | window | z | centre verse(s) | centre content |
|---:|---|---|---:|---|---|
| 5 | 23 Al-Muʾminun | 54–63 | 4.73 | v58/59 | "believe in the signs of their Lord / do not associate anything with their Lord" — tawḥīd core |
| 6 | 26 Ash-Shuʿarā | 102–116 | 4.61 | v109 | "And I do not ask you for it any payment. My payment is only from the Lord of the worlds." — **the prophet's refusal-of-wage refrain** |
| 7 | 77 Al-Mursalāt | 27–35 | 4.41 | v31 | "[Having] no cool shade and availing not against the flame" — eschatological punishment core |
| 8 | 29 Al-ʿAnkabūt | 44–52 | 4.26 | v48 | "And you did not recite before it any scripture, nor did you inscribe one…" — **Muhammad's illiteracy as proof-of-revelation** |
| 9 | 2 Al-Baqarah | 133–142 | 4.24 | nested inside 131-144 | same Abraham pericope, tighter window |
| 10 | 26 Ash-Shuʿarā | 142–152 | 4.21 | — | Salih cycle in Shuʿarā |
| 11 | 54 Al-Qamar | 20–31 | 4.10 | — | broader Thamud window |
| 12 | 37 Aṣ-Ṣāffāt | 120–130 | 4.10 | v125 | "Do you call upon Baʿl and leave the best of creators" — **Elijah's denunciation of Baʿl** |
| 13 | 40 Ghāfir | 28–34 | 4.01 | v31 | "Like the custom of the people of Noah and of ʿĀd and Thamūd…" — the believing kinsman's historical argument |
| 14 | 78 An-Nabāʾ | 1–8 | 3.96 | v4/5 | "No! They are going to know. / Then, no! They are going to know." — eschatological double-refrain |
| 19 | 55 Ar-Raḥmān | 55–69 | 3.58 | — | the second-garden passage; refrain-driven |

Three of these are particularly **novel candidates** not currently in the
ring-composition literature I've surveyed:

- **Al-Muʾminūn 54-63.** The center (v58-59) is a *tawḥīd declaration*
  — "those who do not associate anything with their Lord" — embedded in
  a list of believer-qualities. If the surrounding envelope is actually
  chiastic it would make Al-Muʾminūn's middle a positive-theological pivot,
  similar to ʿAbasa's negative-diagnostic pivot.

- **Al-ʿAnkabūt 44-52 / center v48 on Muhammad's illiteracy.** *"And you
  did not recite before it any scripture, nor did you inscribe one with
  your right hand; otherwise the falsifiers would have had cause for
  doubt."* If this is genuinely at a ring-center, then a 9-verse
  envelope in Al-ʿAnkabūt is built around the **ummī-proof** — a
  meta-revelatory claim about the nature of the book itself. That would be
  a substantive and publishable finding in Quranic rhetoric. Worth a
  follow-up with a tighter window test.

- **Aṣ-Ṣāffāt 120-130 / center v125 "do you call upon Baʿl".** An Elijah
  pericope with the Baʿl denunciation at its axis — a prophet cycle built
  around a specific polemic moment. The pair v120 / v130 is the
  identical-praise refrain *salāmun ʿalā Ilyāsīn* which bookends the
  Elijah section.

These three are the strongest "just below Bonferroni" candidates from a
semantic reading of the windows alone. They should be first in line if the
next chiastic-audit run relaxes the correction threshold, or if it runs a
block-level variant of the test.

## 11. What classical ring-theory says the centers should mean

From Mary Douglas (*Thinking in Circles*, 2007) onward, the unified claim
in the secondary literature is that **the center of a ring is where the
rhetorical envelope makes its point**. Concrete statements from the four
scholars the chiastic-audit references:

- **Michel Cuypers (2009/2015).** The center "serves as a pivotal turning
  point, introducing contrasting ideas that illuminate the text's
  theological messages." For Al-Māʾida specifically, Cuypers reads the
  center as verses 40-43 (theft-and-forgiveness / the Torah-authority
  pivot), and argues these verses are the theological key to the surah.
  Our audit disconfirms the *structural* claim (Al-Māʾida z = -2.06) but
  not the *semantic* claim — Cuypers could still be right that 40-43 is
  the surah's key even if the envelope around it is not a chiasmus.

- **Raymond Farrin (2014).** Explicit about the theological weight of
  centers: "By means of concentric patterning, ring composition calls
  attention to the centre — we are drawn to look here for the essential
  message." For Al-Baqara he places the pivot at v143, reads it as the
  institution of the Muslim *ummah wasaṭ* (just community), and makes it
  the theological apex of the whole surah. Our audit *confirms* Farrin's
  micro-claim (the 131-144 pericope is the strongest ring in the Quran)
  even while disconfirming his whole-surah macro-claim.

- **Mustansir Mir (1986 article and 1986 book on Iṣlāḥī).** Following
  Iṣlāḥī's *naẓm* theory, Mir holds that every surah has a single
  *central theme* (ʿamūd) and that surrounding material is organised
  around it. Mir's centers are *thematic*, not verse-indexed — he does
  not commit to verse-midpoints. His Hud reading does identify the
  prophet-rejection-by-one's-own-people motif as the surah's *ʿamūd*, and
  Thamud-Salih as its exemplar. That is compatible with our algorithmic
  finding that v62 (Salih-as-center) sits at Hud's middle.

- **Neal Robinson (*Discovering the Qur'an*, 2003).** Robinson is more
  cautious. He notes that "some chapters and verses contain perfect ring
  compositions" but initially treated chiasmus as a secondary feature; he
  later conceded it is "a key feature of some Madinan surahs". Robinson's
  criterion for a center is rigorous pair-matching from the outside in —
  which is essentially what the chiastic-audit computes. He has not
  committed to a universal "centers are theological messages" claim.

**The consensus statement**, insofar as there is one: *when a ring is real,
its center is meant to carry the message*. Douglas, Cuypers, Farrin all say
this explicitly. Mir's version is theme-level, not verse-level. Robinson
stays agnostic about whether centers are always semantically loaded.

Our finding nuances the consensus in two ways:

1. **When a ring really is detectable by lexical symmetry (the four
   Bonferroni hits), the center does carry a pointed theological/moral
   message in every case.** Al-Baqarah 137-138 (or 143, if you prefer
   Farrin): the Abrahamic community's faith-boundary. Al-Qamar 25-26:
   accusation-reversed-by-God. ʿAbasa 5: istighnāʾ as diagnostic vice.
   Al-Kahf 87: two-tier justice. All four centers are doing the
   theological work the literary tradition predicts they should.

2. **The 114 whole-surah centers, taken as a group, are heavily
   theological in content — but ring-z does not select for theological
   density at the center.** The Quran puts theology everywhere; the middle
   is no more loaded than any other position. What the center of a
   statistically-real ring gives you is not *more theology* but
   *sharpened rhetorical focus* — the same theological content made
   inescapable by its structural position.

That is a narrower claim than Cuypers-Farrin's maximal version, and a
broader claim than Robinson's minimal one. It is also, as far as I can see,
what the numbers actually support.

## 12. Summary table — what the ring-centers of the real rings contain

| ring | z | center verse(s) | one-sentence thesis |
|---|---:|---|---|
| Al-Baqarah 131-144 | +9.69 | v137 / v138 (or Farrin's v143) | The religion of Abraham is the religion of the new community; belief-boundary precedes ritual-boundary. |
| Al-Qamar 21-30 | +6.46 | v25 / v26 | The accusation "insolent liar" thrown at the prophet is reflected back by God — tomorrow will reveal who the liar is. |
| ʿAbasa 1-9 | +6.09 | v5 | *Istighnāʾ* (thinking oneself without need) is the diagnostic vice the Prophet must not reinforce. |
| Al-Kahf 83-91 | +5.19 | v87 | Human justice and divine justice are two tiers of the same axis; the wrongdoer is punished now and *returned to his Lord* for the worse punishment. |
| Hud (whole surah) | +2.40 | v62 | The prophet-rejection formula — "you were a man of promise; are you now forbidding us what our fathers worshipped?" — is the Quran's master-pattern of disbelief, voiced by Thamud at the exact middle of a prophet-cycle surah. |

All five centers are, in some form, about **the moment of boundary** — the
point where faith is distinguished from unfaith, where the community is
separated from its surroundings, where the wrongdoer is distinguished from
the believer. Abraham's community-boundary (Baqarah), the linguistic
accusation-boundary (Qamar), the rich-versus-poor attention-boundary
(ʿAbasa), the east-west moral-boundary (Kahf), and the prophet-versus-
ancestors boundary (Hud). **The meta-center of the Quran's statistically
real rings is boundary-drawing.** That is a single, defensible claim that
the five individual readings all support.

If I had to name the "message" a chiastic-audit reader should take away, it
would be that one: *where the Quran builds a lexical ring, the center of
the ring is a boundary-drawing moment*. Not "God is one", not "be merciful",
not "pray". It is more specific: it is the moment where the community (or
the prophet, or the human soul) is given a line it must stand on one side
of. That is consistent with Cuypers' general "pivot / contrasting ideas"
framework, with Farrin's reading of Baqarah as community-institution, with
Mir's reading of Hud as prophet-rejection, and with Douglas's anthropology
of ring-composition as a device for establishing the boundary of a group.

## 13. Appendix — full 114-surah centre catalogue

See `analysis/notebooks/chiastic_audit_results.json` field
`all_surah_scores` for the raw data; the centre verse for each is
mechanically derivable as `ceil((N+1)/2)` for odd N or `(N/2, N/2+1)` for
even N. The full Saheeh text for every centre, with ring-z and category, is
in `/tmp/ring_centers_full.json` produced by this run.

A compact view of the top-20 centers was given in § 1. For the 94
lower-z surahs the centers are dominated by narrative fragments and
ritual-law stipulations; they are not individually interesting as pivots
unless the surrounding envelope is also shown to be symmetric, which it
mostly is not.

## 14. Honest limits of this reading

1. The categorisation in § 2 is mine, done by eye. A second reader would
   move several borderline cases. The 75% "theological/moral pivot" figure
   should be read as "most center verses are clearly content-loaded", not
   as a precise percentage.
2. The comparison in § 8.1 (top-20 vs bottom-20 on key-root density) is a
   quick back-of-envelope test, not a formal one. A proper test would
   permute labels and compute z, which I have not run.
3. I did not attempt Cuypers' block-level segmentation for whole surahs.
   That is the natural follow-up and would test whether the "blocks around
   a center" structure holds where verse-level symmetry does not.
4. The four Bonferroni-surviving rings are the only ones I have taken
   semantically seriously. Extending this analysis to the 3.4-4.7 z tier
   (§ 10) is the obvious next step. Al-ʿAnkabūt v48 on Muhammad's
   illiteracy is the most theologically interesting unexplored candidate.
5. My reading of Al-Baqarah 137-138 as the "real" pivot against Farrin's
   v143 is an interpretive choice. The 14-verse window has both as
   plausible centers and the content is continuous; picking one over the
   other is a judgement call about where the thesis sits versus where its
   consequence sits.

## 15. References

- Cuypers, M. (2009/2015). *The Composition of the Qur'an: Rhetorical
  Analysis.* London: Bloomsbury Academic.
- Cuypers, M. (2007). *Le Festin: Une lecture de la sourate al-Mā'ida.*
- Douglas, M. (2007). *Thinking in Circles: An Essay on Ring Composition.*
  Yale UP.
- Farrin, R. (2014). *Structure and Qur'anic Interpretation: A Study of
  Symmetry and Coherence in Islam's Holy Text.* White Cloud Press.
- Farrin, R. (2010). "Sūrat al-Baqarah: A Structural Analysis." *Muslim
  World* 100 (1).
- Mir, M. (1986). *Coherence in the Qur'an: A Study of Iṣlāḥī's Concept of
  Naẓm in Tadabbur-i Qur'ān.* American Trust.
- Mir, M. (1993). "The Sūra as a Unity: A Twentieth Century Development
  in Qur'an Exegesis." In *Approaches to the Qur'an*, ed. Hawting & Shareef.
- Robinson, N. (2003). *Discovering the Qur'an: A Contemporary Approach to
  a Veiled Text.* 2nd ed. SCM Press.
- Sinai, N. (2017). "Going Round in Circles." *Journal of Qur'anic
  Studies* 19 (3).
- Zahniser, A.H.M. (1991). "Major Transitions and Thematic Borders in Two
  Surahs."

Upstream finding: `findings/phase-c-structures/chiastic-audit.md` (the
statistical base this document reads against).
