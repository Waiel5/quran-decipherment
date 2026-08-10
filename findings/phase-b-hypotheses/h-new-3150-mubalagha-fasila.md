---
finding_id: H-NEW-3150
title: "Ṣīghat al-mubālagha at the fāṣila: the pre-registered PASS is an artefact of an orthographic rime class, the divine-name confound the map named is innocent, and holding rhyme constant removes the effect entirely"
author: Waiel Al-Shujaa
date: 2026-08-09
phase: B
frontier_item: F-7
prereg: findings/phase-b-hypotheses/prereg-h-new-3150-mubalagha-fasila.md
prereg_sha256: 968cbdf44294b451dae11727ca4463880142970047816a407f20d0f5ccb25437
runs:
  - runs/h-new-3150/20260809T100346Z                    # locked confirmatory run
  - runs/h-new-3150-posthoc/20260809T101217Z            # POST-HOC phonological rime
  - runs/h-new-3150-posthoc-singular/20260809T101403Z   # POST-HOC singular-only
seed: 20260509
n_perms: 10000
k_confirmatory: 6
alpha_bonferroni: 0.008333
binding_raw_gate: 0.001
locked_verdict: "CONFIRMED (PASS-RESIDUAL) — 6/6 arms at the permutation floor"
verdict: "LOCKED PASS STANDS AS LOCKED AND SHOULD NOT BE BELIEVED. Read §4 before citing anything in §3."
rules_tuple: "(QAC morphology v0.4 segment-token, vocalised-Buckwalter LEM + ROOT, machine template-match wazn, verse-final = word index == max word index, basmala counted only in Q1, Hafs-Kufan, Mashriqi)"
---

# H-NEW-3150 — is ṣīghat al-mubālagha over-represented at the fāṣila?

## Abstract

**The locked verdict is `CONFIRMED (PASS-RESIDUAL)`: all six pre-registered arms cleared the
0.001 raw gate at the permutation floor (p = 9.999 × 10⁻⁵, 0 of 10,000 draws), with a 49–53 %
excess. It should not be believed, and the reason is in this abstract because the
pre-registration cannot retract it.**

The frontier map named one confound — divine-name presence — and required the effect be reported
with and without it. **That confound is innocent.** Deleting every verse containing a divine name
moves the excess from **+51.0 % to +51.7 %**. It does not touch the result.

The fatal confound was one the map did not name, and my pre-registered control for it **did not
work**. I stratified on a *rime class* computed from the last two letters of the unvocalised
lemma. Arabic orthography writes long ī and the diphthong *ay* with the same letter, so that class
put **khayr / ghayr / ṭayr** in the same bucket as **khabīr / qadīr / naṣīr** — and that bucket,
in which the two arms do not rhyme with each other at all, is where the comparison happened.

Recomputing the rime from the **vocalised** lemma gives the actual structure:

> **Of 9,383 template-labelled nominal tokens, 2,915 are ṣiyagh al-mubālagha and 2,915 of those
> 2,915 have a long vowel in the final syllable. Zero mubālagha tokens lack one. Six tokens in
> the whole corpus have one without being mubālagha. φ = 0.9985.**

Within the labelled frame, "is a *ṣīghat al-mubālagha*" and "has a long-vowel rime" are not two
variables. They are one variable, up to six tokens in nine thousand — because Sībawayh's six
patterns are precisely the triliteral nominal templates whose final syllable is long. Under the
corrected rime the pre-registered arms have **S_max = 0**: no informative stratum exists and the
test is `UNTESTABLE-AT-THIS-N` in the exact sense of [[h-new-3030-sajdah-glyph]] §3.5.

That untestability is an artefact of my labeller, not of the corpus — **5,900 long-rime nominal
stems** (*ʿadhāb, kitāb, nār, dīn, nūr, insān, ṣirāṭ*) fall outside the 35 % the template matcher
covers and are genuine comparators. Restoring them makes the test runnable, and it answers the
question:

| control | contrast | sign |
|:--|--:|:--:|
| none (locked A1) | **3.61×** | + |
| orthographic rime — **the locked arms** | **+51.0 %**, z = +18.6 | + |
| phonological rime, all nominals | **−8.9 %**, z = −6.0 | **−** |
| phonological rime, singular nominals only | **−5.2 %**, z = −3.5 | **−** |

Crude, singular mubālagha go verse-final at 48.8 % against 22.6 % for same-rime non-mubālagha —
2.16×. **Holding rime class constant, that reverses.** Mubālagha is concentrated in the rime
classes that are themselves verse-final-loaded (‑īm 78.4 % final, ‑īr 62.0 %); within any one of
them it carries no advantage. This is Simpson's paradox, and the aggregate direction is the
paradox's artefact.

**The answer to F-7 is therefore: the fāṣila preference is prosodic, not morphological.** The
intensive patterns dominate verse-final position because they are the templates that produce the
rhyme, not because they are intensive. This is the **fourth** section-B prior refuted against the
map's expectation, and it fails in a new way: the map's *outcome* guess (CBM) was directionally
right for the wrong reason, while its *confound* line — the part of the map that had been
reliable — named the one variable that turned out not to matter.

---

## 1. Step-0 — this was not already answered

Full grep log in the pre-registration §0. **Not previously tested.** Six near neighbours exist;
none measures nominal-pattern density at verse-final. The only prior use of
`99-names-wazn-classification.tsv` is `findings/khawatim-al-hashr-analysis.md`, which labels
itself *"Descriptive observation (not inferential)"*; `TEAM-AMENDMENTS-LOG.md` AMEND-21 records
the inferential version as never executed. Both idle assets the map flagged are confirmed idle:
zero `.py` files in the repository read either TSV.

**Two grep results changed the design before anything was built.** H-NEW-2080 §B2 (verse-final is
60.76 % nūn+mīm against a 32.28 % word-final baseline) is what put a rhyme control in the design at
all — the map's confound line does not mention rhyme. And H-NEW-2400 §115 (QAC tags the same lemma
under both `N` and `ADJ`) is what stopped me using the map's stated `POS:ADJ (1,961)` frame.

## 2. Instrument

### 2.1 Counts verified

`POS:ADJ` = **1,961** and `POS:PN` = **3,911**, exactly as the map states. 128,219 segments,
6,236 verses, 26,730 nominal stems with lemma + root.

### 2.2 The wazn label is computed, not assigned

The hand TSV covers 99 names; the frame is 9,383 tokens, so the TSV cannot be the instrument. The
label is a template match of the vocalised Buckwalter lemma against the root — `Faʿīl =
c₁+a+c₂+iy+c₃`, `Faʿʿāl = c₁+a+c₂+~aA+c₃`, and 17 more — with two locked normalisations
(sun-letter assimilation stripped; geminate collapse for c₂ = c₃). **0 multi-template collisions**
across the corpus. Coverage: 9,383 of 26,730 nominal stems (35.1 %); weak, hamzated and
quadriliteral roots are systematically outside it, which §4.3 shows is the load-bearing limitation.

### 2.3 Proxy census of the hand TSV, per `findings/PROXY-CLAIMS.md`

100 rows. Confidence **HIGH 95 / MEDIUM 3 / LOW 2**. 20 distinct `wazn` labels collapsed into 11
`wazn_family` buckets, with **19 rows** where the fine label is coarsened away. **15 rows are not
in a derived pattern at all** (1 Proper + 12 Substantive + 2 Compound) — the ambiguous fraction is
**15 %**. 85 rows carry an unambiguous single derived pattern.

**The mubālagha flag is 67.5 % carried by one contested pattern.** 40 rows are flagged
`is_mubalagha = 1`; **27 of those 40 are Faʿīl**, which the TSV's own header calls contested
(*"Sībawayh includes it, later balāgha theorists treat it as ambivalent"*, limitation #4). Dropping
Faʿīl leaves 13. In tokens the imbalance is worse: of 2,915 mubālagha tokens, **2,205 (75.6 %) are
Faʿīl**.

### 2.4 Rater agreement — measured

No second classification exists on disk, so one was **constructed** by applying the §2.2 machine
labeller to each name's QAC lemma. Against the hand TSV:

| | value |
|:--|--:|
| joined to a QAC lemma | 72 / 100 |
| machine returns a unique wazn | 47 |
| hand = machine | **45 / 47 = 95.7 %** |
| **Cohen's κ, multi-class** | **0.942** |
| **Cohen's κ, binary `is_mubalagha`** | **0.950** |

Far above the κ = 0.386 and κ = 0.468 two other lanes measured — **and it must not be read as
vindicating the TSV.** Three qualifications, all measured:

1. **The machine abstains on exactly the hard cases.** Of 72 joined names it labels 47 and abstains
   on 25: weak-rooted (*al-ʿAlī, al-Qawī, al-Walī, al-Ghanī, al-Ḥayy, al-Qayyūm, al-Nūr,
   al-Awwal*), hamzated (*al-Bāriʾ, al-Muʾmin*), quadriliteral (*al-Muhaymin*), defectively written
   (*al-Raḥmān, al-Khāliq, al-Bāsiṭ*). **κ = 0.942 is measured on the transparent half. The TSV's
   contested calls remain unvalidated by anything.**
2. **Both apparent disagreements are join failures, not analytic ones.** *al-Muʿizz* joined to
   `مَعْز` (*maʿz*, "goats") and *al-ʿAfū* to `عَفْو` (the verbal noun). The TSV is right both
   times; on correctly-joined names the machine never contradicted it (45/45).
3. **The two raters are not independent** — both read the same surface string. This measures
   transcription fidelity, not the analytic judgement the other lanes' κ measured. **And my
   template set is itself a hand-built instrument**: I chose which 19 templates to write and how
   to treat weak radicals, hamza, gemination and defective spelling. κ is agreement between two
   judgements with different failure modes. It is not an accuracy estimate and must never be
   quoted as one.

### 2.4a Refusal count — the derivation declines rather than forcing a label

| | n |
|:--|--:|
| names in TSV | 100 |
| **no QAC lemma join** (name not attested as a nominal lemma) | **28** |
| **joined but REFUSED** (no template matches, or >1 does) | **25** |
| labelled | 47 |

**53 of 100 names carry no machine label.** No name was forced to a nearest template; a token is
labelled only on an exact single-template match. Declared failure modes, all systematic and all
visible in the refusal list: **weak radicals** (*al-ʿAlī, al-Qawī, al-Walī, al-Ghanī, al-Ḥayy,
al-Qayyūm, al-Nūr, al-Awwal, al-Muqīt, al-Mujīb*), **hamzated radicals** (*al-Bāriʾ, al-Muʾmin*),
**quadriliteral / contested derivation** (*al-Muhaymin*), **defective Quranic rasm** (*al-Raḥmān,
al-Khāliq, al-Bāsiṭ, al-Wāsiʿ, al-Ẓāhir, al-Wāḥid*), and **compounds** (*Mālik al-Mulk, Dhū
al-Jalāl wa-l-Ikrām*). Corpus-wide the same gaps leave 65 % of nominal stems unlabelled, which
§4.3 shows is the limitation that decides the finding.

The TSV was read **by column name off the header row**, never positionally. Its last field is
free prose carrying Sībawayh and Ghazālī citations; it was used only for a contestation-keyword
scan, never as a label. All 101 non-comment lines split to exactly 10 fields, so no embedded tab
corrupts the parse.

### 2.5a The shared error — where both raters agree and both are wrong

Disagreements advertise themselves; shared errors do not. Hand-checking the cells where hand and
machine **agree** finds one error class, and it is large.

**All 27 Faʿīl names are flagged `is_mubalagha = 1` at HIGH confidence, and the machine agrees
with the TSV on the surface wazn for every one of them.** Both are reading the same surface, and
the surface does not carry the distinction that matters. Classical grammar splits Faʿīl three ways:

- **ṣīghat al-mubālagha** — intensified action from a *transitive* base (*raḥīm, ʿalīm, samīʿ,
  ḥafīẓ, raqīb, shahīd*);
- **al-ṣifa al-mushabbaha** — a *fixed quality* from a stative/intransitive base, which Sībawayh
  does **not** place in the mubālagha set: *ʿazīz* (ʿazza), *laṭīf* (laṭufa), *ḥalīm* (ḥaluma),
  *ʿaẓīm* (ʿaẓuma), *ʿalī*, *kabīr* (kabura), *jalīl* (jalla), *karīm* (karuma), *majīd*, *qawī*,
  *matīn*, *ghanī*, *rashīd* — **13 names**;
- **faʿīl bi-maʿnā mafʿūl** — passive sense: **al-Ḥamīd = *maḥmūd***, "the Praised", not "the
  much-praising" — the textbook case, and flagged `is_mubalagha = 1` like the rest.

**On classical grounds roughly 14 of the 27 are not ṣiyagh al-mubālagha at all**, which would cut
the mubālagha token count far below 2,915. Neither rater could have caught it: the distinction is a
property of the *base verb*, and neither instrument consults the base verb.

**I then tried to mechanise the check and failed three times, which is the more useful result.**
(i) A transitivity probe keyed on `POS:PRON` returned zero attached objects for all 27 roots
including ʿ-l-m with 425 verb tokens — QAC writes object pronouns as `SUFFIX|PRON:3MS` with no
`POS:` field, so the detector never fired. (ii) Fixed, it counted all verb forms, so Form-II/IV
transitives masked stative Form-I bases. (iii) Restricted to Form I it still does not discriminate
— mean object-pronoun rate **0.590** for the hand-called stative/passive group against **0.656**
for the hand-called mubālagha group — **and it is silent on 11 of 27 names**, including 8 of the 13
stative calls, because *laṭufa, ḥaluma, ʿaẓuma, jalla, karuma, majuda, qawiya, matuna* **do not
occur in the Quran as Form-I verbs at all**. You cannot measure the transitivity of a base the
corpus never uses.

So the shared error is identified by hand, on classical grounds, and is **not** corroborated by any
machine instrument I could build. That is the honest status, and it generalises: a second
classification is a second judgement, and a third one here was three broken judgements in a row.

### 2.5 Tie fraction, per `findings/TIED-OUTCOME-DEFECT.md`

`is_final` is **78.4 % tied at 0** (2,029 of 9,383 tokens are verse-final). The per-verse mubālagha
count outcome is **66.8 % tied at zero**. Both exceed 50 %, so the permutation null is primary and
the parametric z is reported only alongside it, never instead of it.

## 3. The locked run — `runs/h-new-3150/20260809T100346Z`

### 3.1 Ladder (descriptive)

| arm | strata | informative tokens | obs | exp | excess | z |
|:--|:--|--:|--:|--:|--:|--:|
| A1 | none | 9,383 | 1,256 | 630.3 | **+99.3 %** | +33.90 |
| A2 CH-W | + length quintile | 9,383 | 1,256 | 652.0 | +92.6 % | +33.51 |
| A3 CH-W | + rare root | 9,383 | 1,256 | 653.5 | +92.2 % | +33.50 |
| A4 CH-W | **+ divine name** | 9,378 | 1,253 | 912.5 | **+37.3 %** | +23.11 |
| A5 CH-W | + rime class | 2,496 | 433 | 286.7 | +51.0 % | +18.64 |

### 3.2 Confirmatory family (k = 6)

| id | arm | obs | exp | excess | z | p_perm | S\* | S_max | MDE | pass |
|:--|:--|--:|--:|--:|--:|--:|--:|--:|--:|:--:|
| C1 | A5 \| CH-W | 433 | 286.7 | +51.0 % | +18.64 | 9.999e-5 | 310.9 | 452 | 30.9 | ✓ |
| C2 | A5 \| CH-S | 432 | 289.3 | +49.3 % | +18.25 | 9.999e-5 | 313.4 | 454 | 30.7 | ✓ |
| C3 | A5 \| CH-N | 434 | 284.3 | +52.7 % | +18.62 | 9.999e-5 | 309.1 | 462 | 31.6 | ✓ |
| C4 | divine-free \| CH-W | 383 | 252.5 | **+51.7 %** | +17.48 | 9.999e-5 | 275.6 | 402 | 29.4 | ✓ |
| C5 | divine-free \| CH-S | 389 | 260.5 | +49.3 % | +17.29 | 9.999e-5 | 283.4 | 409 | 29.2 | ✓ |
| C6 | divine-free \| CH-N | 393 | 258.5 | +52.1 % | +17.87 | 9.999e-5 | 281.7 | 411 | 29.6 | ✓ |

**Headline (worst of six) = C1, p = 9.999 × 10⁻⁵.** All three length channels agree to within
3.4 percentage points of excess; **no channel dominates**, which is unusual for this project and
is the one place the design behaved well. Verdict as locked: **CONFIRMED (PASS-RESIDUAL)**.

### 3.3 The divine-name comparison the map demanded

| | excess | z |
|:--|--:|--:|
| **with** divine-name verses (C1) | **+51.0 %** | +18.64 |
| **without** divine-name verses (C4) | **+51.7 %** | +17.48 |

**Removing them does not kill it. It does not move it.** 927 of 6,236 verses (14.9 %) contain a
divine-name nominal; dropping them removes 29 % of the frame and changes the excess by +0.7
percentage points. The divine-name stratum inside A4 does absorb a lot of the *unstratified*
association (+92.2 % → +37.3 %), but conditional on rime it contributes nothing further.

### 3.4 Strict-5 sensitivity — the headline is mostly a Faʿīl result

Dropping Faʿīl (2,915 → 710 tokens) leaves an excess of **+12.6 % to +23.3 %**, and **3 of the 6
arms fail the 0.001 raw gate** (S1|C2 p = 0.0017, S1|C4 p = 0.0011, S1|C5 p = 0.0037; all would
pass Bonferroni 0.008333). The other sensitivity arms move nothing: deciles instead of quintiles
(S2) and raw two-letter rime instead of the coarse class (S3) both reproduce the headline to within
4 points; ADJ-only (S5) reproduces it on 101–111 informative tokens.

---

## 4. **What is wrong with §3** — read this before citing any number above

### 4.1 The pre-registered rime control was orthographic and did not control rhyme

Pre-registration §5.2 defines rime class from the **unvocalised** lemma's last two letters. Arabic
writes long ī and the diphthong *ay* with the same grapheme ي. So the bucket `(ī, R)` contained:

| phonological rime | n | pattern | verse-final |
|:--|--:|:--|--:|
| **ī + r** (*khabīr, qadīr, naṣīr, baṣīr*) | 421 | all Faʿīl | 62.0 % |
| **ayC** (*khayr, ghayr, ṭayr*) | 347 | all Faʿl | 0.9 % |

The comparison arm was words that **do not rhyme with the treatment arm**. The same merger
operates in `(ī, L)` — *ʿalīl/jamīl* against *layl/khayl* — and `(ī, D)`. The control that was
supposed to strip the rhyme confound is what supplied the contrast.

### 4.2 Under the correct rime the two variables are one variable

Recomputing from the vocalised lemma:

| | mubālagha = 1 | mubālagha = 0 |
|:--|--:|--:|
| **long-vowel rime (V̄C)** | **2,915** | **6** |
| any other rime | **0** | 6,462 |

**φ = 0.9985.** Every mubālagha token has a long-vowel rime; six tokens in 9,383 have one without
being mubālagha (4 *Faʿlān*, 2 *Fuʿʿūl*). This is **not** a definitional artefact of my template
list — the list contains three long-vowel non-mubālagha templates (*Faʿlān, Fuʿʿūl, Faʿʿūl*); they
are simply almost unattested. It is an empirical fact about the Quranic lexicon, and it has a
clean explanation: **Sībawayh's six mubālagha patterns are exactly the triliteral nominal templates
with a long final syllable.** Intensification in Arabic *is* syllabic lengthening.

Consequence for the locked arms: under the phonological rime, **S_max = 0** on C1 and C4 and
≤ 3 elsewhere. `S* > S_max`, so the pre-registered test is **UNTESTABLE-AT-THIS-N**. Pre-registration
§6 evaluated that branch and reported it as not firing — that evaluation used the broken rime and
was wrong.

### 4.3 The untestability is my labeller's, not the corpus's — and lifting it answers F-7

5,900 long-rime nominal stems sit outside the 35 % the matcher covers (*ʿadhāb* 322, *kitāb* 260,
*nās* 241, *nār* 145, *dīn* 92, *nūr* 43, *insān*, *ṣirāṭ*, *īmān*). They are genuine
non-mubālagha comparators sharing the rime. Restoring them
(`runs/h-new-3150-posthoc/20260809T101217Z`, **POST-HOC**):

| arm | tokens | excess | z | p |
|:--|--:|--:|--:|--:|
| phonological rime, all nominals, CH-W | 4,393 | **−8.9 %** | −5.99 | 1.000 |
| CH-S | 4,504 | −8.9 % | −5.91 | 1.000 |
| CH-N | 4,657 | −9.3 % | −6.43 | 1.000 |
| divine-free, CH-W | 3,020 | −10.3 % | −6.38 | 1.000 |

**The sign flips.** Because 29 % of long-rime nominals are sound plurals whose final long vowel is
inflectional (*kāfirūn, ʿālamīn, muttaqīn, ṣāliḥāt*) and are classic fāṣila words, the filter was
re-run on singulars only (`runs/h-new-3150-posthoc-singular/20260809T101403Z`, **POST-HOC**):

| arm | tokens | excess | z | p |
|:--|--:|--:|--:|--:|
| singular, phonological rime, CH-W | 3,040 | **−5.2 %** | −3.49 | 0.9999 |
| CH-S | 3,205 | −5.3 % | −3.62 | 0.9996 |
| CH-N | 3,288 | −6.2 % | −4.25 | 1.000 |
| divine-free singular, CH-W | 2,304 | −7.8 % | −5.16 | 1.000 |

**The plural filter is not what flips the sign — the stratification is.** Crude singular rates are
mubālagha 48.8 % versus same-rime non-mubālagha 22.6 %, a 2.16× advantage. Conditioning on rime
class turns it negative. That is **Simpson's paradox**: mubālagha is concentrated in the rime
classes that are themselves verse-final-loaded (‑īm 78.4 % final, ‑īr 62.0 %, ‑īl 33.8 %), and
within any single class it has no advantage. The aggregate positive is the between-class effect
wearing the label of a within-class one.

### 4.4 Residual contamination, disclosed

The post-hoc comparison arm still contains mubālagha forms the matcher misses on weak or hamzated
roots — *alīm* (72 tokens, root `Alm`, a Faʿīl) is the clearest. These are false negatives in the
comparison arm and they bias the contrast **downward**, so the measured −5 % to −9 % is a lower
bound on the true within-rime contrast and the honest reading is "at or slightly below zero", not
"reliably negative". **Neither the locked +51 % nor the post-hoc −9 % should be quoted as the
effect size.** What survives is the sign structure: positive between rime classes, absent or
negative within them.

## 5. The H-NEW-23 comparison, with the arm the naive version omits

S6 ran the within-verse uniform-slot null that produced MASTER finding #7. Reported with the
comparison arm, which the statistic alone hides:

| pool | n | obs | exp | ratio | z |
|:--|--:|--:|--:|--:|--:|
| mubālagha-6 | 2,915 | 1,256 | 249.6 | **5.03×** | +68.82 |
| **non-mubālagha nominal** | 6,468 | 773 | 521.7 | **1.48×** | +11.90 |
| all labelled nominal | 9,383 | 2,029 | 771.3 | 2.63× | +48.96 |
| *H-NEW-23 hapax comparator* | *395* | *121* | *53.95* | *2.24×* | *+10.61* |

Quoting the 5.03× against H-NEW-23's 2.24× would be wrong twice over: the uniform-within-verse null
ignores that nominals as a class are verse-final-loaded (2.63× before any morphology is consulted),
and §4.3 shows the residual above that baseline is rime, not pattern.

## 5a. Did the §7 reversal clause fire? No — and why that is not reassuring

The clause: *"any confirmatory arm has S_obs < E[S]_null with two-sided p ≤ 0.008333."*

**The confirmatory arms are C1–C6 and only those** — prereg §5.2 defines them as A5 and A5-minus-
the-divine-stratum, where A5's rime class is the orthographic one of §5.2. All six have
`S_obs > E[S]_null` (433 > 286.7, …), `positive = True`, `reversed = False`, recorded per-arm in
`runs/h-new-3150/.../results.json`. **The clause did not fire, correctly.**

The post-hoc arms sit in the opposite tail — `p_perm_lo = 1e-4`, `p_perm_two = 2e-4`, far below
0.008333 — but they are **not** confirmatory arms in §7's sense: different rime definition,
different frame (27,097 tokens against 9,383), not pre-registered.

**Three things rule out the alternative readings.** The sign convention is not inverted: the
post-hoc script imports `run_arm` from the locked script (`M.run_arm`) and both accumulate
`obs += Σ mub × final`, so the same statistic is being counted with the same sign in both
directories, and the tails differ because the effect differs. Every verdict-bearing p is **exact**:
`p_hi = (1 + #{S_perm ≥ S_obs}) / (1 + 10,000)`; `passes` reads `p_perm` and `reversed_` reads
`p_perm_two`, and the parametric `z_param` is computed for display only and appears in neither —
required, since the tie fraction is 0.7838. And no arm is `UNTESTABLE` under the locked rime, so
the NULL/untestable interaction never engages.

**But the clause not firing is a fact about the locked arm, not about the text.** It did not fire
because the pre-registered arm was broken (§4.1). Under a rime control that actually holds rhyme
constant the effect is at or below zero. Reporting "the reversal clause did not fire" and stopping
there would be true and would mislead, which is why the abstract leads with §4 instead.

## 5b. Which control is primary

**The rhyme-shape-matched control is primary and the divine-name residualisation is secondary** —
that is how the pre-registration was locked (rime is stratum level 5, the outermost; divine-name
is level 4 plus the divine-free subset), and it is what decided the finding. The two controls
disagreed exactly as anticipated: the effect **survives** divine-name residualisation
(+51.0 % → +51.7 %) and **dies** under rhyme matching. The pre-registration named that outcome in
advance and assigned it a meaning — *this is rhyme, not morphology* — and it is the title.

## 6. Verdict

**As locked: `CONFIRMED (PASS-RESIDUAL)`.** It is recorded because a pre-registration that can be
retracted is not a pre-registration. **As believed: the effect is prosodic and the morphological
reading is not supported.**

- F-7's hypothesis — over-representation *beyond* the rhyme and divine-name structure — is **not
  supported**.
- The map's named confound (divine names) is **innocent**: +51.0 % → +51.7 %.
- The unnamed confound (rime shape) is **total**, and is not separable from the predictor on this
  corpus: φ = 0.9985 inside the labelled frame.
- The classical anchor that predicted a surviving residual — Ibn Abī l-Iṣbaʿ's *barāʿat al-maqṭaʿ*,
  "seal with a heightened word" — gets **no support**. What the fāṣila selects for is the long
  final syllable, and the heightened forms are simply the templates that have one.

## 7. What I got wrong

1. **The pre-registered rime control was orthographic.** I identified the rhyme confound correctly
   in Step 0, argued for it against the map, built a control for it, and then computed that control
   from unvocalised text in a script whose entire input was vocalised. The vocalised lemma was in
   the same variable I read the root from.
2. **The `UNTESTABLE-AT-THIS-N` evaluation in prereg §6 is wrong** — it certified S\* < S_max using
   the broken rime. Under the correct one, S_max = 0 and every confirmatory arm is untestable. The
   branch was evaluated, as the protocol requires, and the evaluation was garbage in the specific
   way the protocol was designed to catch.
3. **I ran the ladder before checking what was inside the strata.** The 76 % informative-token loss
   at A5 was measured before locking and put in the pre-registration as an honest cost. It was not
   a cost — it was the instrument failing, and one `value_counts` on the comparison arm's patterns
   would have shown it. The check that found it (§4.1) took four lines and ran *after* the
   confirmatory result was already on disk.
4. **The map's confound line was reliable until now.** Prereg §2 records that F-4's and F-14's
   confound warnings were both real, and I weighted this map's confound line accordingly. It named
   the innocent variable here.
5. **I broke the transitivity probe three times** (§2.5a) — a `POS:` regex against a field QAC
   does not write, then a dropped Form-I filter, then a probe that simply does not discriminate.
   The first was caught only because the output was absurd (425 verb tokens, zero objects). Had it
   returned a plausible number it would have entered this file as corroboration.
6. **I did not hand-check the agreeing cells until asked.** I checked the two disagreements,
   found both were join failures, and reported 45/45 corrected agreement — treating the agreeing
   cells as settled. The 27-name shared error in §2.5a was sitting in the column I had already
   read, and it is larger than anything the disagreements showed.

## 8. Reproduction

```
python3 findings/phase-b-hypotheses/scripts/h-new-3150.py            # locked, ~3 min
python3 findings/phase-b-hypotheses/scripts/h-new-3150-posthoc.py    # POST-HOC, ~30 s
```

Both verify `EXPECTED_PREREG_SHA = 968cbdf4…` at runtime and exit non-zero on mismatch. Run
directories are created with `os.makedirs(exist_ok=False)` and all artefacts written with
`open(..., 'x')`. **The pre-registration has not been edited since the run and must not be.**
