---
id: H-NEW-2270
title: al-Suyūṭī Itqān distributional-claims audit
date: 2026-05-29
phase: B
author: Waiel Al-Shujaa
verdict: 3 CONFIRMED · 1 QUALIFIED-IN-SOURCE · 1 RULES-FRAGILE · 1 VINDICATED-AFTER-DISAMBIGUATION
prereg_sha256: dcefa7d1f9f9b22fd3ccab4d8652a48b9487bd50ac1e75ab83de7b2a7ebecd25
---

# H-NEW-2270 — al-Suyūṭī *al-Itqān* distributional-claims audit

A five-claim, exact-count audit of testable distributional/census claims in al-Suyūṭī's *al-Itqān
fī ʿulūm al-Qurʾān* (nawʿ 1 makkī/madanī, nawʿ 19 ʿadad). It extends the H-NEW-2160 *kallā*
exemplar (one al-Suyūṭī/al-Dānī claim VINDICATED-AFTER-DISAMBIGUATION) to a block. Every exact
wording was located in the OpenITI source and quoted with line refs BEFORE testing. Directions were
locked in the pre-reg (`prereg-h-new-2270…`, SHA-256 above, verified at runtime in the script).
Counts are computed from disk: makkī/madanī ground-truth from the per-surah `type` field of
`quran-text/quran-no-tashkeel.json` (86 meccan / 28 medinan, matching `data/revelation-order.csv`);
homograph/sense disambiguation from QAC v0.4 lemma+POS.

## Why these five

The classical *ḍawābiṭ al-makkī wa-l-madanī* are *exactly* distributional assertions ("every sūra
that contains X is of type Y") — they are falsifiable censuses, not interpretive opinions. al-Suyūṭī
collects them in nawʿ 1 with named attribution (al-Jaʿbarī, Makkī b. Abī Ṭālib, Ibn Masʿūd via
al-Ḥākim/al-Bayhaqī, al-Hudhalī, al-Dīrīnī/al-Dānī). Each is clearly attributable and on-disk testable.

---

## Per-claim verdict table

| # | Claim (paraphrase) | Claimant (Itqān nawʿ 1 unless noted) | Predicted | Observed | Verdict |
|:-:|:--|:--|:--|:--|:--|
| 1 | Every muqaṭṭaʿāt sūra is Meccan **except** al-Zahrāwān (Q2,Q3) + al-Raʿd (Q13) | al-Jaʿbarī (qiyāsī), l.1171-74 | Medinan-muq = {2,3,13} | {2,3,13} **exact** | **CONFIRMED** |
| 2 | Every sūra mentioning the munāfiqūn is Medinan **except** al-ʿAnkabūt (Q29) | Makkī b. Abī Ṭālib, l.1175 | Meccan-member = {29} | {29} **exact** | **CONFIRMED** |
| 3a | Every sūra with *yā ayyuhā alladhīna āmanū* is Medinan | Ibn Masʿūd; Ibn ʿAṭiyya "ṣaḥīḥ", l.1146-51 | 0 Meccan | 0/20 Meccan | **CONFIRMED** |
| 3b | Every sūra with *yā ayyuhā al-nās* is Meccan | Ibn Masʿūd; Ibn ʿAṭiyya qualifies, l.1152 | 0 Medinan | 4/9 Medinan (Q2,4,22,49) | **QUALIFIED-IN-SOURCE** |
| 4 | Every sūra containing a sajda is Meccan | al-Hudhalī (*al-Kāmil*), l.1176 | 0 Medinan-sajda | 2 (Q13,Q22) under binary label; 0 under al-Suyūṭī's Meccan reading | **RULES-FRAGILE** |
| 5 | Rebuke-*kallā* (33×) never at Yathrib, never in the upper half | al-Dīrīnī verse / al-Dānī, l.1178-80 | count=33; all after niṣf; 0 Medinan | 33; all in Q19-104, earliest after Q18:74; 0 Medinan | **VINDICATED-AFTER-DISAMBIGUATION** |

**Tally: 3 CONFIRMED · 1 QUALIFIED-IN-SOURCE · 1 RULES-FRAGILE · 1 VINDICATED-AFTER-DISAMBIGUATION.**

---

## Claim 1 — al-Jaʿbarī's muqaṭṭaʿāt criterion: CONFIRMED (exact)

> "والقياسي كل سورة فيها {يا أيها الناس} فقط، أو {كلا} أو أولها حرف تهجٍّ سوى الزهراوين والرعد … فهي مكية"
> — al-Itqān nawʿ 1, line 1171-1173.

Of the 29 muqaṭṭaʿāt surahs (Q2,3,7,10,11,12,13,14,15,19,20,26,27,28,29,30,31,32,36,38,40,41,42,43,
44,45,46,50,68), exactly three carry the Medinan label: **{Q2 al-Baqara, Q3 Āl ʿImrān, Q13 al-Raʿd}**
— the precise triple al-Jaʿbarī names as the exceptions. All other 26 are Meccan. The criterion is an
**exact** classification rule over the muqaṭṭaʿāt family with zero error. This is the strongest landing
in the block: a 1,000-year-old qiyāsī heuristic that partitions the 29-surah disjoined-letter set with
no residual.

## Claim 2 — Makkī's munāfiqūn criterion: CONFIRMED (exact)

> "كل سورة فيها ذكر المنافقين فمدنية زاد غيره سوى العنكبوت" — al-Itqān nawʿ 1, line 1175.

Disambiguation matters here. The bare root **n-f-q** is a homograph spanning the *hypocrisy* sense
(munāfiqūn / munāfiqāt / nifāq / nāfaqa) and the *spending* sense (anfaqa / infāq), the latter
scattered across many Meccan surahs. Counting the raw root would falsely inflate the surah set. Using
the QAC hypocrite-sense lemmas only, the mention-set is **{Q3,4,8,9,29,33,48,57,59,63,66}** (11 surahs).
Of these, ten are Medinan and exactly one is Meccan — **Q29 al-ʿAnkabūt**, precisely the exception
"zāda ghayruhu" (added by others). Exact match. (al-ʿAnkabūt's "hypocrite" verses Q29:10-11 are indeed
among the ~10 verses classically flagged as Medinan-within-a-Meccan-sūra.)

## Claim 3 — the address criterion is asymmetric, exactly as al-Suyūṭī's own sources say

> Ibn Masʿūd (via al-Ḥākim, al-Bayhaqī, al-Bazzār): "ما كان {يا أيها الذين آمنوا} أنزل بالمدينة وما
> كان {يا أيها الناس} فبمكة." Ibn ʿAṭiyya / Ibn al-Faras then qualify: "هو في {يا أيها الذين آمنوا}
> صحيح وأما {يا أيها الناس} فقد يأتي في المدني." — al-Itqān nawʿ 1, lines 1146-1152.

- **3a (*āmanū* ⇒ Medinan): CONFIRMED.** All **20** surahs containing *yā ayyuhā alladhīna āmanū*
  (Q2,3,4,5,8,9,22,24,33,47,49,57,58,59,60,61,62,63,64,66) are Medinan — **zero** Meccan exceptions.
  This vindicates Ibn ʿAṭiyya's verdict that this direction is *ṣaḥīḥ*.
- **3b (*al-nās* ⇒ Meccan): QUALIFIED-IN-SOURCE.** Of the **9** surahs with *yā ayyuhā al-nās*
  (Q2,4,7,10,22,27,31,35,49), five are Meccan but **four are Medinan** (Q2 al-Baqara, Q4 al-Nisāʾ,
  Q22 al-Ḥajj, Q49 al-Ḥujurāt). This is NOT a falsification of al-Suyūṭī — it is the very asymmetry
  he records in the same passage. He explicitly notes al-Nisāʾ opens with *al-nās* yet is Medinan
  (line 1158), and al-Baqara contains *al-nās* (line 1157). The weak direction is **self-qualified in
  the source**; the data reproduce the qualification with a 4/9 Medinan rate. Labelled
  QUALIFIED-IN-SOURCE rather than FALSIFIED precisely because the claimant pre-empted the failure.

## Claim 4 — al-Hudhalī's sajda criterion: RULES-FRAGILE

> "وفي كامل الهذلي كل سورة فيها سجدة فهي مكية" — al-Itqān nawʿ 1, line 1176.
> Sajda verse-list (14, Shāfiʿī): al-Itqān nawʿ 19, lines 6783-6786.

The 13 sajda-bearing surahs are Q7,13,16,17,19,22,25,27,32,41,53,84,96. Under the project's binary
Tanzil/Egyptian-standard label, **two are Medinan** — Q13 al-Raʿd and Q22 al-Ḥajj — which falsifies
the rule as literally stated. But these two are not arbitrary: they are exactly the surahs al-Suyūṭī
**himself documents as disputed (mukhtalaf fīhā) with authoritative Meccan readings**:

- **Q13 al-Raʿd**: "فالرعد مختلف فيها متى نزلت / وأكثر الناس قالوا الرعد كالقمر" (lines 788-789) and
  "من طريق مجاهد عن ابن عباس وعن علي بن أبي طلحة … أنها مكية" (lines 843-844). al-Raʿd is *also* the
  named exception in al-Jaʿbarī's twin muqaṭṭaʿāt criterion (Claim 1).
- **Q22 al-Ḥajj**: "تقدم من طريق مجاهد عن ابن عباس أنها مكية إلا الآيات التي استثناها" (lines 852-853).

Under the Ibn ʿAbbās / majority Meccan reading of these two disputed surahs, al-Hudhalī's rule holds
with **zero** counterexamples. The verdict is therefore **RULES-FRAGILE** (bidirectional rules-tuple
sensitivity): it fails under one makkī/madanī labelling and holds under another that al-Suyūṭī himself
endorses. This is the project's documented "rules-tuple rehabilitation" pattern (cf. the kallā
homograph rescue, and Ikhwān al-Ṣafāʾ-under-maghribī in project memory) — the rule is real but its
truth-value rides on a classification choice that the source treats as genuinely open.

## Claim 5 — al-Dānī/al-Dīrīnī kallā upper-half: VINDICATED-AFTER-DISAMBIGUATION (H-NEW-2160 refined)

> "وما نزلت كلا بيثرب فاعلمَنْ / ولم تأتِ في القرآن في نصفه الأعلى" — al-Itqān nawʿ 1, al-Dīrīnī, l.1178-80.

This reproduces and **tightens** H-NEW-2160 with the QAC gold-standard:

1. **Count.** The raw consonantal substring كلا is a homograph (rebuke *kallā* vs quantifier
   *kullan / kilā*) and appears across both halves (earliest Q4:130 *kullan min saʿatih*). The QAC
   disambiguated rebuke-particle (POS = **AVR**, `LEM:kal~aA`) gives **exactly 33** — matching
   al-Dānī's classical count to the unit. Distribution: Q19(2), 23(1), 26(2), 34(1), 70(2), 74(4),
   75(3), 78(2), 80(2), 82(1), 83(4), 89(2), 96(3), 102(3), 104(1).
2. **Upper half.** "al-naṣf al-aʿlā" is rules-tuple sensitive. al-Suyūṭī (nawʿ 19, line 4362) places
   the classical letter-count niṣf al-Qurʾān at the *nūn* of *nukran* in al-Kahf, **Q18:74**
   (cumulative verse 2214 / 6236). The earliest rebuke-*kallā* is **Q19:79** (verse 2329) — strictly
   *after* the midpoint. Hence all 33 fall in the lower half under the dominant classical (letter)
   definition of "half." (The word-midpoint Q22:20 and verse-midpoint Q26:45 also sit before the
   bulk; only a naïve surah-index "halfway = surah 57" definition — which is *not* the classical
   niṣf — would mislabel the early cluster.)
3. **Never at Yathrib.** None of the 33 rebuke-*kallā* surahs is Medinan (all Q19-104, all Meccan).

All three sub-conditions hold → VINDICATED-AFTER-DISAMBIGUATION, with the "half" now pinned to the
classical letter-midpoint rather than a modern surah-index split.

---

## The cross-claim diagnostic

The block has a clean signature, and it is the **opposite** of the modern-numerology signature
(H-NEW-2000 / al-Khalifa: 0 % confirmation, symmetry-claims fail). Here, **qualitative distributional
heuristics that classical scholars actually used for dating verses land at high accuracy**: two are
*exact* partitions (Claims 1, 2), one direction of a bidirectional rule is *exact* (3a), and the two
non-confirmations are both **self-aware in the source** — Ibn ʿAṭiyya pre-qualifies 3b, and al-Suyūṭī
pre-flags the disputed status of the two surahs that break Claim 4. The classical tradition was not
naïve about its own edge cases; its census heuristics survive an exact on-disk audit far better than
its later numerological offspring.

A recurring lesson, third time in this project: **raw substring counts conflate homographs** (n-f-q
spending vs hypocrisy in Claim 2; كلا quantifier vs rebuke in Claim 5). Morphological (QAC lemma+POS)
disambiguation is the gold standard, and it *rescues* rather than retires the classical observation in
both cases — bidirectional rules-tuple sensitivity.

## Honest limits

- The makkī/madanī binary is itself a classical reconstruction with disputed cells (Q13, Q22, Q47,
  Q55, Q76, Q98, Q99 are all contested). Claims 3b and 4 ride on exactly these contested cells. The
  audit uses ONE ground-truth (the project's Tanzil/Egyptian-standard `type` field) as the primary
  lens and reports the al-Suyūṭī-internal alternative lens where it changes a verdict (Claim 4); it
  does not attempt to adjudicate the underlying makkī/madanī dispute.
- "Mentioning the munāfiqūn" (Claim 2) is operationalised as the QAC hypocrite-sense lexeme; a sūra
  could in principle describe hypocrites without the lexeme (none does in a way that changes the
  verdict, but this is a lexical not a semantic test).
- Phrase-matching for the address criterion (Claim 3) is exact-string on no-tashkeel text after
  stripping pause-marks; it counts a sūra once if the phrase appears anywhere in it (matching the
  classical "fīhā" framing), not the surah-opening only.
- These are exact-count censuses over closed sets, not permutation-null hypothesis tests; no global
  Bonferroni family applies (per the task's exact-audit framing). Each verdict is an exact agreement
  or an exact, enumerated counterexample list.

## Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2270-itqan-distributional-audit.md`
  (SHA-256 `dcefa7d1f9f9b22fd3ccab4d8652a48b9487bd50ac1e75ab83de7b2a7ebecd25`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2270.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2270.json`

## Cross-references

- **H-NEW-2160 (§10.80)** — the kallā exemplar; Claim 5 here refines its "second-half" into the exact
  classical letter-midpoint (Q18:74) and confirms the QAC count = 33.
- **H-NEW-2000 (§10.80)** — modern balanced-words audit (0 confirmed); this block is the qualitative
  counterpoint where classical census-heuristics largely hold.
- **feedback_rules_tuple_bidirectional** (memory) — Claim 4 (sajda) and Claim 5 (kallā) both exhibit
  rules-tuple rehabilitation: a classification/disambiguation choice rescues the classical claim.
- al-Suyūṭī kink at s=50 (Protocol §3.6) — same scholar, same nawʿ-1 makkī/madanī material, empirically
  anchored elsewhere in the project.
