# Shirk Rhetoric — Run 1 Journal

Date: 2026-04-12
Phase: B
Agent role: Phase B Shirk Rhetoric investigator
Data source: `data/morphology/quranic-corpus-morphology-0.4.txt`

## Objective

Map how the Quran argues against polytheism (shirk), using the root sh-r-k
(Buckwalter: `$rk`) as the anchor and ten thematic axes set by the task
brief (greatest wrong, named idols, challenge constructions, Luqman,
parables, Abraham/Moses narratives, denial of divine family, unforgivability,
and the "common word" verse 3:64).

## Method

1. Grepped `ROOT:$rk` rows out of the Dukes morphology file. 168 hits, matching
   the target count in the brief.
2. Bucketed by POS, lemma, verb form, aspect/voice, and surah.
3. Pulled full morph dumps for every verse the brief names (31:13; 53:19–23;
   10:35, 10:38, 17:56, 46:4; 22:73, 16:75, 39:29; 4:48, 4:116; 6:101, 112:3;
   3:64; 21:51–73 sampled; 37:83–96; 7:127).
4. Cross-checked idol vocabulary: `ROOT:Snm` (Sanam, graven image — 5 hits),
   `ROOT:wvn` (Wathan, idol — 3 hits; 22:30, 29:17, 29:25). These sit outside
   the sh-r-k corpus but feed the same polemic.
5. Counted unique verses with sh-r-k: 143 verses carry 168 tokens, so about
   25 verses repeat the root internally (e.g. 16:86 has two tokens, 4:48
   and 4:116 each have two verb tokens).

## Key quantitative findings

- 168 tokens / 143 verses / 44 surahs.
- Lemma split: verb `>a$oraka` (IV) 71; noun `mu$orik` (associator) 44;
  noun `$ariyk` (partner) 40; noun `$irk` (the act itself) 5; `mu$orika`t`
  (fem. pl.) 3; `mu$tarikuwn` (form VIII "co-sharers in punishment") 2;
  `mu$orikap` (fem. sg.) 2; rare verb `$aArika` (III) 1.
- Verb form dominance: Form IV (causative "to make a partner for God") at
  120/168 tokens. Form VIII surfaces only twice. Form III once (17:64).
- Aspect/voice (72 verbs): 49 imperfective active, 18 perfective active,
  3 imperfective passive (`yu$oraka bihi` — the thing NOT forgiven is the
  passive action of associating with Him, 4:48, 4:116, 6:88), 2 imperative
  (notably 17:64 `$aArikhum` — Iblis "share with them").
- Surah distribution: top concentrations Q 6 (29), Q 9 (12), Q 16 (11),
  Q 10 (9), Q 30 (9), Q 2 (7), Q 4 and Q 7 (6 each). The anti-idolatry
  polemic concentrates in mid-to-late Meccan surahs plus Medinan Q 2 / Q 9.
- 143 unique verses means roughly 1 in every 43 verses of the Quran touches
  sh-r-k vocabulary — a very high density for a theological-polemical term.

## Evidence inventory for each of the ten axes

1. **Q 31:13 "inna l-shirka la-ẓulmun ʿaẓīm"** — morph shows noun `$~iroka`
   made definite with `{l`, predicate `ZulomN` with emphatic `la-` prefix.
   The superlative adjective `EaZiymN` echoes the divine epithet but here
   qualifies the crime. This is the only place `$irk` receives the phrase
   `ẓulm ʿaẓīm`. The wrapping is vocative-paternal (`yaA bunay~a`).

2. **Q 53:19–23** — `{ll~aAta / {loEuz~aY` / manaw`pa / v~aAlivapa` —
   proper-noun tags, no root, which is itself a rhetorical move: the Quran
   refuses to dignify the three goddesses with any real lexical lineage.
   53:23 demotes them to `>asomaA^'N` — "mere names" their ancestors coined.

3. **Challenge constructions** — imperative `{doEuw` ("Call!") plus
   `zaEamotum` ("you claimed") anchor 10:38, 17:56, 46:4. 10:35 adds the
   rhetorical question `hal min $urakaA^}ikum`. 46:4 layers the demand:
   show me what they made on earth / or show me a scripture / or even a
   "trace of knowledge" (`>avaArapK m~ino EilomK`).

4. **Luqman** — see #1. Vocative `yaA bunay~a` + jussive negation
   `laA tu$oriko` (form IV, 2MS JUS) + causal clause with `<in~a`.

5. **Parables** —
   - 22:73 fly: `Duriba mavalN` opening formula; `tadoEu`wna min duwni
     {ll~ahi` targets the `min duwn` construction used of idols.
   - 16:75: `Daraba {ll~ahu mavalF` + slave vs free-provider binary.
     `laA yastawuwna` rhetorical equalisation-question.
   - 39:29: another `Daraba {ll~ahu mavalF` with the hapax participle
     `muta$aAkisuwna` — form VI of the same sh-r-k root, "co-sharers in
     mutual antagonism", pitted against a `rajulF salamF` (a man "whole" /
     undivided).

6. **Abraham breaking idols** — 21:58 `fa-jaEalahum ju*a`*F <il~aA
   kabiyrF`: the smash leaves the "big one" intact as a rhetorical trap.
   37:95 the punchline: `>a-taEobudu`wna maA tanoHitu`wna?` — you worship
   what you carve? Vocabulary `Snm` (21:57) and `wvn` (29:17, 29:25) bind
   this narrative to the broader polemic, but NOT via sh-r-k itself.

7. **Moses vs Pharaoh** — 7:127 places Pharaoh's `>aAlihapa` in the mouth
   of his chiefs (Pharaoh hesitates about his own gods). 7:138 reintroduces
   `>aSonaAm` — the Israelites' first post-Exodus request is idolatry,
   showing shirk as a latent human default.

8. **Denial of divine family**
   - 6:101 `lam takun lahu SaaHibapN` (no consort) + `waladN` (no
     offspring) — morph shows both negations in one verse.
   - 112:3 twin-negation `lam yalido wa-lam yuwlado` (neither begets nor
     was begotten) — ring couplet reinforcing 6:101.

9. **Unforgivability except with repentance**
   - 4:48 and 4:116 share nearly identical morph: `<in~a {ll~aha laA
     yagofiru >an yu$oraka bihi` + `wa-yagofiru maA duwna *aalika
     li-man ya$aA^'u`. The passive `yu$oraka` frames the un-pardoned
     act as a state to be associated WITH Him, not as a quantifiable sin.
     Difference: 4:48 closes with `<ivomF EaZiymF` (great fabrication),
     4:116 closes with `Dala`lF baEiydF` (far-gone misguidance).

10. **Q 3:64 "kalimatin sawāʾ"** — form I `naEobuda <il~aA {ll~aha`
    followed by negated subjunctive `wa-laa nu$orika bihi $ayo_#F`
    followed by `wa-laa yat~axi*a baEoDunaA baEoDF >arobaAbF`. Three
    negatives, ascending in social scope (worship, partnering, human
    lordship). The `nu$orika` is 1P, inclusive, implicating speaker
    and addressee in a shared creed.

## Judgements I'm making as I draft

- The brief's "~168 occurrences" is exact. I will state the distribution
  precisely.
- I will NOT invent counts for non-sh-r-k idol terms beyond what I have
  verified (Snm ×5, wvn ×3). These are subsidiary.
- I will flag that `$arika` form III (17:64, Iblis: `$aArikhum`) is the
  only place the root is used IMPERATIVELY by a speaker inside the Quran,
  and it belongs to Satan. This is a structurally beautiful inversion.
- I will treat form VIII `mu$otarikuwn` (eschatological "co-sharers in
  punishment", 37:33, 43:39) as the Quran's internal ironic reuse of
  the root: those who shared falsely in worship end up sharing truly
  in hell. This is a rhetorical symmetry worth surfacing.

## Open items / limits

- I am not running TF-IDF or co-occurrence proper; this is a thematic
  essay over morph-grounded evidence.
- I have not cross-checked every one of the 143 verses against an
  English translation; claims are grounded in morphology plus the
  specific verses the brief enumerated.
- `ja`Ea` ("he made" in 21:58) and `jaEalu`wA` ("they set up partners"
  e.g. 6:100) would be good additional corpus hits, but are out of root.

## Output

Findings file: `findings/phase-b-hypotheses/shirk-rhetoric.md` (~3500 words).
Summary: inline in this journal (500-word section below).

## 500-word summary

The Quran deploys the root sh-r-k 168 times across 143 verses in 44 surahs,
making shirk — associating partners with God — its single most densely
developed polemic target. The distribution is not uniform: 29 hits cluster
in Q 6 (al-Anʿām), with secondary densities in Q 9, 16, 10, 30, and 2. The
lemmatic split is revealing: 71 verb-tokens of form IV (`>a$raka` — the
causative: one who deliberately instals a partner), 44 tokens of the
participle `mu$orik` (the agent), 40 of `$ariyk` (the ostensible partner
itself), 5 of the abstract noun `$irk`, and scattered feminine and form-VIII
forms. Verb behaviour is overwhelmingly imperfective-active (49/72),
marking shirk as a continuing live-action state, not a settled past event.

Rhetorically, the Quran's anti-shirk strategy is not a single move but a
layered repertoire. At the moral-weight pole, Q 31:13 makes Luqman's
first fatherly instruction a negation — `laA tu$orik bi-llaAhi` — and then
supplies its only recurrence of the formula `al-shirk ... la-ẓulmun
ʿaẓīm`, rating it the "great wrong." At the unforgivability pole, Q 4:48
and Q 4:116 frame shirk, via the passive `yu$oraka bihi`, as the one sin
outside the scope of divine pardon absent repentance — while every lesser
sin falls within `maA duwna *aAlika`. Between these poles sits a dialectical
arsenal: (a) challenge constructions — `{doEuw $urakaA^}akum` (10:35,
17:56, 46:4) demanding the idols produce evidence, creation, or
scripture; (b) parables — the fly that cannot be created by gathered
deities (22:73), the powerless slave vs the giving free man (16:75), the
man torn between quarrelling co-masters (39:29, with the root's own form VI
`muta$aAkisuwna`); (c) idol narratives — Abraham's axe (21:51–73, 37:83–96)
turning carved stone into an argument from inability to speak; and
(d) theological denial — Q 6:101 strips God of consort and son, Q 112:3
tightens this into a twin-negation couplet, `lam yalid wa-lam yuwlad`.

The Quran also performs internal symmetries with the root itself. The only
imperative-shirk verb in the entire corpus (17:64) is spoken by Iblis, who
is told to "share" with the sons of Adam in wealth and children — shirk as
Satanic collaboration. The form-VIII `mu$tarikuwn` (37:33, 43:39) ironically
reassigns the root to the eschatological scene: those who falsely shared in
worship below become genuine co-sharers in the Fire above.

Finally, Q 3:64 offers a constructive note amid the polemic: a `kalimatin
sawaA^'` — a common word between Muslims and People of the Book, built
on three negations arranged by scale (don't worship except God, don't
associate, don't take one another as lords beside God). The form is
1P-inclusive (`nu$orika`, not `tu$orikuw`): the speaker steps into the
indictment alongside the addressee, reframing anti-shirk from accusation
to shared creed. That move captures the Quran's preferred register when
it is not lampooning idols: logical, communal, and covenantal.
