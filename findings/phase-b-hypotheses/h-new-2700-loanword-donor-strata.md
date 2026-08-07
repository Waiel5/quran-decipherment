---
id: H-NEW-2700
title: Loanword donor language does NOT stratify by revelation phase — and the type-level contrast runs backwards
date: 2026-08-07
author: Waiel Al-Shujaa
status: ALL FOUR REGISTERED HYPOTHESES NULL — H2, H3 and the co-primary H4 with REVERSED direction; stable across all three rules-tuples
prereg: prereg-h-new-2700-loanword-donor-strata.md
prereg_sha256: 6e5332da94d1fb6ce24261e34acd99d34f171215e810dbf639981b13c5736525
run: runs/h-new-2700/20260807T013038Z/
parent: H-NEW-125 (axis 15, loanword_density)
seed: 20260509
seed_replication: 20260519
family: LOAN-2026-08-07-A
---

# H-NEW-2700 — Donor language does not stratify by phase

**Verdict: NULL on all four registered hypotheses. Three of them, including the
co-primary, are direction-REVERSED. The reversal is stable across all three
rules-tuples, so it is not an artefact of Jeffery's contested classification. The
Aramaic/Syriac stratum sits nearly a full Nöldeke phase LATER than the Persian
stratum — the exact opposite of the locked prediction.**

Pre-reg SHA-256 `6e5332da…736525`, runtime-verified. 10,000 permutations per null, two
nulls of different kinds per hypothesis, replications at +10. Family of **8** registered
inferences; Bonferroni α = 0.00625, project novelty rule stricter, so the **raw decision
gate is 0.000625**.

---

## 1. Results

| | locked direction | observed | Null A (donor labels) | Null B (phase labels) | verdict |
|:--|:--|--:|--:|--:|:--|
| **H1** composition, Late-Meccan ARAM share > Medinan | Δ > 0 | **+0.0047** | p = 0.473 | p = 0.494 | **NULL** |
| **H2** ARAM density peaks Late Meccan | Δ > 0 | **−4.257** | p = 0.936 | p = 0.929 | **NULL, REVERSED** |
| **H3** PERS density peaks Medinan | Δ > 0 | **−2.150** | p = 0.539 | p = 0.983 | **NULL, REVERSED** |
| **H4** *(co-primary)* type-level, PERS later than ARAM | Δ > 0 | **−0.911** | p = 0.997 | p = 0.994 | **NULL, REVERSED** |

Replications at seeds +10 agree throughout (H1 0.486/0.492; H2 0.936/0.936; H3
0.543/0.985; H4 0.997/0.995). No hypothesis comes within three orders of magnitude of the
gate.

H1's direction is nominally positive but the statistic is **+0.0047** — a composition
shift of half a percentage point — and its leave-one-type-out range is **−0.149 to
+0.085**, crossing zero. Per pre-reg §6.1 it would be demoted to CBM even had it passed.
It did not pass.

### The phase profiles, residualised on log surah length

| | Early Meccan | Middle Meccan | **Late Meccan** | Medinan |
|:--|--:|--:|--:|--:|
| ARAM residual density | −0.136 | **+2.788** | **−1.469** | −0.882 |
| PERS residual density | +0.038 | **+1.468** | −0.775 | −0.682 |

**Both families peak Middle Meccan, and both are at or near their minimum in Late
Meccan.** The prediction placed Aramaic/Syriac at a Late-Meccan maximum; it is the
Late-Meccan *minimum*. The prediction placed Persian at a Medinan maximum; Medinan is its
second-lowest phase.

### The co-primary, in one line

Mean token-weighted phase index φ (Early 1 → Medinan 4), each type counting once:

- **ARAM: φ = 3.242** (12 types)
- **PERS: φ = 2.331** (26 types)

Aramaic/Syriac vocabulary is **0.911 phases later** than Persian. The hypothesis required
the opposite sign.

---

## 2. Why it reverses — the premise about Persian was wrong

Post-hoc, labelled as such, MW-7 single-test ceiling, **not a finding**. It was generated
by reading the result and must be tested by a fresh pre-registration, not by this one.

The hypothesis assumed Quranic Persian vocabulary is **administrative and trade**
vocabulary from Sasanian contact. The eligible roster says otherwise. Ranked by tokens,
the Persian stratum is overwhelmingly **material-luxury and Paradise-furnishing**
vocabulary:

*arāʾik* (couches, φ=1.60) · *istabraq* (brocade, 1.75) · *sundus* (fine silk, 2.00) ·
*namāriq* (cushions, 1.00) · *firdaws* (paradise, 2.00) · *sarābīl* (garments, 3.00) ·
*sirāj* (lamp, 2.25) · *surādiq* (canopy, 2.00) · *salsabīl* · *zanjabīl* (ginger) ·
*kāfūr* (camphor) · *yāqūt* (ruby, 1.00) · *warda* (rose, 1.00) · *zujāja* (glass) ·
*sidra* (lote-tree, 1.00).

That is the vocabulary of **early eschatological description**, and Early/Middle Meccan
is exactly where the eschatological register lives. The genuinely administrative Persian
items behave as predicted — ***jizya*** (poll tax) **φ = 4.00**, *majūs* (Magians) 4.00,
*baḥīra* 4.00, *Hārūt* 4.00, all squarely Medinan — but they are **one token each** and
carry no weight against fifteen luxury words.

Meanwhile the Aramaic/Syriac stratum is pulled late by religious-technical terms:
*ʿĪsā* (25 tokens, φ=3.76), *tijāra* (3.89), *furqān* (3.43), *muhaymin* (4.00),
*qissīsīn* (4.00), *rahbāniyya* (4.00) — against *qurʾān* (2.33) and *Raḥmān* (2.02)
pulling it early.

**The channel hypothesis may still be right; this operationalisation of it was not.** The
right test splits Persian by semantic field and tests only the administrative subset —
see §6.

---

## 3. The CBM trap that §1.1 predicted, and which did not fire

The pre-registration predicted, before computing, that a token-level pass would likely be
carried by two words: *qurʾān* (70 tokens) and *Raḥmān* (57), together **127 of 193
ARAM tokens = 65.8%**, both with Late-Meccan associations already explained by H-NEW-125's
`book_reference_density` axis.

That guard was built (H4 type-level co-primary + leave-one-type-out) and **it turned out
not to be needed, because nothing passed.** Recording it anyway: the guard was registered
in advance, and had H1 passed on those two words while H4 failed, the verdict language
was already fixed at CONFIRMED-BUT-MEANINGLESS.

Worth noting for its own sake: *Raḥmān* lands at **φ = 2.02**, squarely Middle Meccan.
The instrument is behaving sensibly — the "Raḥmān period" of the Nöldeke-era chronology
falls exactly there.

---

## 4. Rules-tuple stability — the negative result is NOT Jeffery-dependent

The central worry registered in pre-reg §5 was that a negative could be an artefact of
Jeffery's contested etymologies. It is not.

| | H1 | H2 | H3 | **H4 (co-primary)** |
|:--|--:|--:|--:|--:|
| **T1** primary (as-is, narrow ARAM) | +0.005 | −4.257 | −2.150 | **−0.911** |
| **T2** HIGH confidence only | **−0.057** | −4.315 | −1.695 | **−0.867** |
| **T3** ARAM broadened with `hebrew-aramaic-shared` | +0.002 | −4.617 | −2.150 | **−0.252** |

**All three tuples agree on the sign of the co-primary, and H2/H3 are reversed in all
three.** Restricting to entries where the registry expresses no uncertainty (T2, 11 ARAM
and 13 PERS types) makes H1 reverse as well. The verdict is **not** RULES-TUPLE-FRAGILE;
the hypothesis fails under every lens registered for it.

---

## 5. Honest limits

1. **The Aramaic/Syriac stratum is 12 types.** Any claim resting on it, positive or
   negative, is underpowered. What rescues the negative is the *size* of H4's reversal
   (−0.911 phases, p = 0.997/0.994 in the locked direction) and its stability across
   tuples — not its sample size.
2. **Exclusions are not random with respect to donor family, and this was flagged before
   the run** (pre-reg §8.5). Of 304 registry rows, **205 are eligible**; 68 unmatched, 28
   ambiguous, 3 multiword. Join rates were worst for `syriac` (6 of 12 matched) and
   `aramaic` (2 of 4) — the primary family. Three ARAM/PERS entries were lost specifically
   to the ambiguity gate: *biyaʿ* (syriac), *dīn* and *kanz* (both persian, both
   high-frequency). **This is the most serious methodological limit here**, and it cuts
   against the family whose direction reversed.
3. **Ibn Jarīr's *tawārud al-lughāt* objection is untestable in this design** (§7).
   If the shared vocabulary reflects convergence rather than borrowing, the donor-language
   framing is void and this test is measuring nothing. No permutation speaks to it.
4. **The Nöldeke sequence is a philological reconstruction**, not a documented chronology.
   Every phase-indexed number inherits that uncertainty.
5. **Phase word-counts are severely unbalanced** — Early Meccan 5,669 words against
   Medinan 30,695, on a corpus of 82,375. Densities are per-1,000-words and residualised
   on log length, but Early-Meccan density estimates rest on a thin base.
6. **Token counts are lemma attestations, not disambiguated senses.**
7. **No cross-corpus control.** Nothing here establishes that these patterns are specific
   to this corpus rather than general to seventh-century Ḥijāzī Arabic.
8. **The registry is a compiled encoding of Jeffery, not Jeffery.** `source_language` is
   one scholar's judgement transcribed by another hand into a TSV.

---

## 6. What would settle it

1. **Split Persian by semantic field** — administrative/fiscal (*jizya*, *majūs*) versus
   material-luxury/Paradise-furnishing (*istabraq*, *arāʾik*, *sundus*) — and test only the
   administrative subset against phase. §2 says that is where the original hypothesis
   might survive. It needs its own pre-registration and its own field assignment locked
   before computing; on current counts it will be badly underpowered.
2. **Repair the join.** 68 unmatched entries, disproportionately Syriac/Aramaic, is the
   binding constraint. That is hand-disambiguation work against Jeffery's own occurrence
   lists (pp. 12–296), not something a matcher can fix.
3. **A matched contemporary Arabic corpus** with donor annotation, for the cross-corpus
   control this test cannot run.

---

## 7. Classical anchor — verified, with the citation situation stated exactly

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` **line 9117**:
`### | النوع الثامن والثلاثون: فيما وقع فيه بغير لغة العرب` — **nawʿ 38**, on what
occurs in the Qurʾān in other than the language of the Arabs.

**The English translation on disk does not contain this nawʿ.** The brief asked for a page
citation from `suyuti-al-itqan-fi-ulum-al-quran-english.pdf`; that PDF is by its own
introduction "some twenty chapters of excerpts," and searching it for the *muʿarrab*
discussion returns nothing on topic. **No page is cited from it, because there is none to
cite.** At line 9118 al-Suyūṭī names his separate book on the subject —
`"المهذب فيما وقع في القرآن من المعرب"` — which is **not on disk**; nothing is cited from it.

Three positions from the nawʿ, all verified in place, and all bearing directly on this
result:

1. **The majority denied that *muʿarrab* occurs in the Qurʾān at all** —
   `فالأكثرون ... على عدم وقوعه فيه` — al-Shāfiʿī, Ibn Jarīr al-Ṭabarī, Abū ʿUbayda,
   al-Qāḍī Abū Bakr and Ibn Fāris, arguing from `{قرآنا عربيا}`. Ibn Fāris adds a reason
   this project should find interesting: if it contained non-Arabic speech, someone might
   suppose the Arabs failed to match it only because it used tongues they did not know —
   i.e. the *iʿjāz* claim itself is at stake.
2. **Ibn Jarīr's *tawārud al-lughāt*** — what is reported from Ibn ʿAbbās about Persian,
   Ethiopic or Nabataean words is `توارد اللغات فتكلمت بها العرب والفرس والحبشة بلفظ واحد`,
   a convergence of tongues rather than borrowing. **This is a classical null hypothesis
   for the whole test**, and this design cannot address it.
3. **The reconciling position grounds borrowing in travel-contact** —
   `كان للعرب العاربة ... بعض مخالطة لسائر الألسنة في أسفارهم فعلقت من لغاتهم ألفاظا` — the
   Arabs mixed with other tongues *on their journeys* and picked up words which they
   altered until they ran as fluent Arabic. **This is the classical statement of the exact
   channel mechanism under test**, and it is the strongest warrant the hypothesis had.

Against that anchor the result is a clean negative: the tradition's own contact-channel
story is coherent, but the *chronological* signature it would predict is not in the text
under this instrument.

`suyuti_naw_38_attested` split across the ARAM+PERS roster, descriptive: entries
al-Suyūṭī also lists (28 types, 220 tokens, mean φ = 2.486); entries he does not (7
types, 17 tokens, φ = 2.698); disputed (3 types, 6 tokens, φ = 3.667).

---

## 8. Provenance

- Pre-registration written and SHA-256'd **before any donor × phase statistic existed**.
  Pre-reg §2 lists exhaustively what was inspected first: registry structure, donor and
  confidence vocabularies, phase counts, matcher development and its collision audit, and
  per-donor **token totals for power assessment only**. No phase breakdown was among them.
- **Inputs SHA-verified at runtime**, run aborts on mismatch: Jeffery TSV `d12ebac9…`,
  QAC v0.4 `a1d12923…`, revelation order `74f52ec1…`, `quran-no-tashkeel.json`
  `253f72f3…`.
- **Registry-size correction.** The brief and `HANDOFF/FRONTIER-MAP-2026-08-07.md` report
  the TSV as **506 rows**. That is the line count: the file has **201 comment lines**, one
  header, and **304 data rows**. Verified and recorded in `result.json`.
- **Verdict-logic diff performed before publication, as required.** Pre-reg §7: *"PASSES
  iff its observed direction matches the lock AND both of its raw p-values are <
  0.000625."* Script: `PASS = direction_ok and null_a.passes_gate and null_b.passes_gate`,
  with `passes_gate = p < RAW_GATE` and `RAW_GATE = CORRECTED_GATE / TESTS_IN_FAMILY =
  0.005 / 8 = 0.000625`; all four locked directions are `Δ > 0` and the script tests
  `obs > 0`. **Match, line for line.**
- **Manifest paths are repository-relative** (pre-reg §9), so the run record is
  committable as written and no local or tooling directory name appears in it.
- Immutable run: `findings/phase-b-hypotheses/runs/h-new-2700/20260807T013038Z/`.
  **No run directory was deleted.**

### 8.1 Garden-of-forking-paths log

1. **Two matcher variants were rejected in the pre-registration, before computing**, and
   the reasons are recorded there because both were caught doing real damage during
   feasibility work: (A) long-ā-blind keys, which silently matched the registry's `قرآن`
   to QAC's `qaron` (*qarn*, "century") instead of `quro'aAn` (*qurʾān*) and collapsed
   `ملاك` onto *malak*/*malik*/*mulk* at once; (B) silent resolution of ambiguous keys,
   replaced by the explicit ambiguity gate. Variant A is exactly the failure mode behind
   this project's standing rule that raw substring counting on Arabic lies.
2. **One 200-permutation smoke run** for correctness, written to a scratch directory
   *outside* `findings/` and self-declaring `SMOKE_RUN: true`, retained at
   `smoke-2700/20260807T012928Z/`. Its structural fields and observed statistics were
   visible to me before the 10,000-permutation run. **No gate, direction, seed, statistic
   or family size was changed as a result** — the deterministic statistics are identical
   between the two runs by construction; only the p-values differ.
3. **One field added after the smoke run**: `H1_CBM_demotion_triggered`, which surfaces
   the pre-reg §6.1 leave-one-type-out demotion in `result.json` rather than leaving it to
   prose. **It can only demote, never promote.** It is `false` here because H1 did not
   pass in the first place.

---

## 9. Cross-references

- **[[h-new-125-chronology-content]] axis 15** — the parent. Its undifferentiated
  `loanword_density` is ρ = **+0.833**, p = 1.0×10⁻⁴, inverted-U peaking Late Meccan.
  **This finding does not overturn it and does not re-derive it.** The parent's axis is
  dominated by `hebrew-aramaic-shared` (5,946 tokens in the feasibility count, against 193
  ARAM and 50 PERS); what H-NEW-2700 shows is that **splitting that axis by donor language
  does not recover a channel signature** — the small strata do not carry the parent's
  Late-Meccan peak, and in fact both bottom out there. The parent measures something real
  about loanwords in aggregate; it is not evidence about contact communities.
- **Instrument note for the parent.** H-NEW-125 matched loanwords by **whole-word exact
  match on proclitic-expanded surface forms**
  (`scripts/h_new_125_chronology_content.py:423-458`); this test uses a QAC-lemma join with
  an ambiguity gate and finds **4,367 eligible tokens**. The two instruments are not
  interchangeable and the difference is reported rather than reconciled.
- **[[cross-finding-028-formal]]** — the register-coded discourse grammar. §2's post-hoc
  reading, that Persian loans cluster in early eschatological description, is a
  *register* observation, not a chronology one, and that is the frame in which a follow-up
  should be built.
- **The retirement/vindication ledger** — this is a **retirement**. A historically
  plausible, classically anchored hypothesis about contact channels fails under proper
  nulls, and fails in the reversed direction on its own co-primary. The classical anchor
  (al-Suyūṭī's travel-contact reconciliation) remains coherent as history; it simply does
  not leave the chronological trace this test predicted.
