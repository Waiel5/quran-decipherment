---
id: H-NEW-2700
title: Does loanword donor language stratify by revelation phase? Aramaic/Syriac vs Persian across the Nöldeke sequence
date: 2026-08-07
status: LOCKED-BEFORE-COMPUTATION
author: Waiel Al-Shujaa
family: LOAN-2026-08-07-A
parent: H-NEW-125 (axis 15, loanword_density)
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 8
alpha_bonferroni: 0.00625
corrected_novelty_gate: 0.005
raw_p_gate: 0.000625
---

# PRE-REGISTRATION — H-NEW-2700 — Donor-language stratification of Quranic loanwords

Written before any statistic relating a donor language to a revelation phase has been
computed. §2 lists exhaustively what was inspected first. The final SHA-256 is embedded
as a fixed literal in `findings/phase-b-hypotheses/scripts/h-new-2700.py` and verified at
runtime; the run must abort with `SystemExit` on mismatch.

---

## 1. The claim, and the reason it is fragile before it is even run

**H-NEW-125** (`h-new-125-chronology-content.md`, axis 15) treats loanwords as one
undifferentiated axis and found `loanword_density` ρ = **+0.833**, permutation
p = 1.0×10⁻⁴, surviving Bonferroni-15, with an **inverted-U trajectory peaking Late
Meccan**. That is the parent result and it is not re-derived here.

The new claim splits that axis by **donor language**. Two contact channels are
historically distinct: **Syriac/Aramaic** entered Arabic largely through Christian
liturgical and monastic contact; **Persian** largely through Sasanian administrative,
military and trade contact. If the text's borrowed vocabulary carries a signature of
*which* contact community was salient *when*, Aramaic/Syriac items should concentrate in
the Late-Meccan scripture-announcement material and Persian items in the Medinan phase.

### 1.1 Three reasons this test is likely to produce a confirmed-but-meaningless result

Stated **before** computation so the verdict cannot be dressed up afterwards.

1. **The Aramaic/Syriac stratum is tiny.** Feasibility counting (§2) gives **13 matched
   types** under the narrow definition, against 28 Persian.
2. **Two words dominate it.** `قرآن` *qurʾān* (70 tokens) and `رحمن` *Raḥmān* (57
   tokens) are together **127 of ~201** Aramaic/Syriac tokens — roughly 63% of the
   stratum. A token-level test would substantially be a test of two words.
3. **Both of those words already have a known Late-Meccan chronology for reasons that
   have nothing to do with Syriac contact.** *qurʾān* is the self-referential scripture
   term, and H-NEW-125's axis 9 `book_reference_density` (ρ = +0.574) already shows an
   inverted-U peaking Late Meccan. *al-Raḥmān* as a Late-Meccan divine name is a
   commonplace of the Nöldeke-era chronology this very test uses as its independent
   variable.

**Consequence, locked now:** a token-level pass that does not survive the **type-level
co-primary (H4)** and the **leave-one-type-out** robustness is to be reported as
**CONFIRMED-BUT-MEANINGLESS**, not as a historical-linguistic finding. §7 fixes that
language.

### 1.2 Classical anchor — verified on disk, with the citation situation stated exactly

`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` **line 9117**:
`### | النوع الثامن والثلاثون: فيما وقع فيه بغير لغة العرب` — **nawʿ 38**, "on what
occurs in it in other than the language of the Arabs." Verified.

**The English translation on disk does NOT contain this nawʿ.**
`data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf` is by its
own introduction "some twenty chapters of excerpts"; searching it for the *muʿarrab*
discussion returns nothing on topic. **I therefore cite no page from it.** The brief
asked for a page from the English PDF; that page does not exist, and inventing one is not
an option.

Line 9118: al-Suyūṭī states he devoted a separate book to this nawʿ —
`قد أفردت في هذا النوع كتابا سميته: "المهذب فيما وقع في القرآن من المعرب"`. That is
*al-Muhadhdhab*, and per the brief it is **not on disk**; nothing is cited from it.

Three positions from the nawʿ, all verified in situ, and all load-bearing here:

1. **The majority denied *muʿarrab* occurs at all.** al-Shāfiʿī, Ibn Jarīr al-Ṭabarī, Abū
   ʿUbayda, al-Qāḍī Abū Bakr, Ibn Fāris — `على عدم وقوعه فيه` — arguing from
   `{قرآنا عربيا}` and `{ولو جعلناه قرآنا أعجميا}`.
2. **Ibn Jarīr's *tawārud al-lughāt*** — what is reported from Ibn ʿAbbās about Persian,
   Ethiopic or Nabataean words is merely `توارد اللغات فتكلمت بها العرب والفرس والحبشة
   بلفظ واحد`: coincidental convergence, not borrowing. **This is a genuine classical
   null hypothesis for the entire test**, and no permutation here can refute it.
3. **The reconciling position grounds borrowing in travel-contact** —
   `كان للعرب العاربة ... بعض مخالطة لسائر الألسنة في أسفارهم فعلقت من لغاتهم ألفاظا`:
   the Arabs mixed with other tongues *on their journeys* and picked up words. **This is
   the classical statement of exactly the channel-based mechanism under test**, and it is
   the strongest anchor available for the hypothesis.

---

## 2. What was inspected before this lock — exhaustive

Only registry structure, join feasibility, and matcher correctness. **No phase
distribution, no donor × phase statistic, and no density by phase was computed, viewed
or estimated.**

1. **Registry shape, and a correction to the brief.** The brief and
   `HANDOFF/FRONTIER-MAP-2026-08-07.md` report `data/loanwords/jeffery-1938-loanwords.tsv`
   as **506 rows**. That is the **line** count. The file has **201 comment lines**, one
   header, and **304 data rows**. Verified.
2. Fields: `arabic_lemma, romanized, source_language, jeffery_page,
   suyuti_naw_38_attested, luxenberg_disputed, notes, confidence`.
3. `source_language` is single-valued for all 304 rows — **zero** multi-donor or
   "or"-marked entries. Vocabulary and counts: hebrew-aramaic-shared 163, hebrew 53,
   persian 35, syriac 13, greek 11, ethiopic 9, south-arabian 7, syriac-aramaic-shared 6,
   aramaic 4, latin 3.
4. `confidence`: HIGH 160, MEDIUM 47, LOW 97. `suyuti_naw_38_attested`: yes 113, no 187,
   disputed 4. `luxenberg_disputed`: yes 3.
5. `data/revelation-order.csv`: 114 rows, `noldeke_phase` ∈ {Early Meccan 48, Middle
   Meccan 21, Late Meccan 21, Medinan 24}.
6. **Matcher development and its two rejected variants** (§3.2). Join rates and the
   collision audit were computed; the identity of matched lemmas was inspected. Token
   counts per donor family were computed **for power assessment only** and are the basis
   of §1.1. Their distribution over phases was not.
7. `scripts/h_new_125_chronology_content.py` lines 423–458: the parent used
   **whole-word exact matching against a proclitic-expanded surface-form set**, not QAC
   lemmas. This test uses a lemma join instead and reports both (§6.6).

---

## 3. Frozen inputs and the matching procedure

### 3.1 Frozen inputs (SHA-256, verified at runtime; any mismatch aborts)

| # | path | SHA-256 |
|:-:|:--|:--|
| 1 | `data/loanwords/jeffery-1938-loanwords.tsv` | `d12ebac9d4bb62bbc1a8c810d7e2c069195e20113a77fb04505a84dfd4674b94` |
| 2 | `data/morphology/quranic-corpus-morphology-0.4.txt` | `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46` |
| 3 | `data/revelation-order.csv` | `74f52ec1518abf8ecbf67671ee1cdd8e4cfc553fc8c5ead8274cc7dae8916fb7` |
| 4 | `quran-text/quran-no-tashkeel.json` | `253f72f32f1dd4f6288c24be1b3b81b2e32c67aedd59aecb6e4a057dae35918a` |

**Rules-tuple (primary, T1):** `(Jeffery-1938 registry as-is, all confidence levels,
narrow Aramaic family, QAC-v0.4 lemma attestation, unambiguous-key entries only,
orthographic word denominator, Nöldeke 4-phase, Ḥafṣ-Kūfan 6236, Mashriqī)`.

### 3.2 Matching — deterministic, and two variants rejected in advance

QAC Buckwalter lemmas are converted to Arabic script by the standard 1:1 Buckwalter map.
Both sides are reduced to a key `K`: drop short vowels, shadda, sukūn, maddah,
hamza-above/below and tatweel; map `وٰ`/`يٰ` → `ا`; unify `ٱأإآ` → `ا`, `ة` → `ه`,
`ى` → `ي`, `ؤئ` → `ء`; then **delete `ء`** (hamza-blind, applied identically to both
sides). Tier 1 keeps dagger alif as `ا`; **tier 2** deletes it, and is tried only if
tier 1 misses. The registry mixes the two conventions — it writes `سليمان` with alif but
`رحمن` without — so both are required.

**Rejected variant A — long-ā-blind keys.** Deleting `ا` from the key raises the match
rate but is **unsafe, and was caught doing real damage**: it matched the registry's
`قرآن` to QAC's lemma `qaron` (*qarn*, "century/horn", 23 tokens) instead of
`quro'aAn` (*qurʾān*, 70 tokens), and collapsed `ملاك` onto `malak`/`malik`/`mulok`
simultaneously. **Rejected.** This is precisely the failure mode behind the project's
standing rule that raw substring counting on Arabic lies.

**Rejected variant B — silent resolution of ambiguous keys.** Because the registry's
`arabic_lemma` is an *unvocalised* orthographic string, some keys legitimately map to
several distinct vocalised QAC lemmas — `سلم` → {salam, sallama, sullam, salm, silm};
`ملك` → {malak, malik, malk, mulk}; `دين` → {dayn, dīn}. **28 of the 233 matched entries
are ambiguous in this way.** Silently pooling or arbitrarily picking one is not
acceptable.

**The ambiguity gate (locked):** an entry is **eligible** only if its key maps to
**exactly one** QAC lemma. Ambiguous entries are excluded from every gated test, counted,
listed in the run record, and pooled in a **registered sensitivity** (§6.3). Multiword
registry entries (3) are excluded. Entries matching nothing are excluded and listed.

**Attestation** of an eligible entry = the set of `(surah, verse, word)` locations of its
unique QAC lemma. No substring matching occurs anywhere in this test.

### 3.3 Donor families (locked, taken from the registry as-is)

- **ARAM** = {`syriac`, `syriac-aramaic-shared`, `aramaic`} — the Christian/Syriac
  contact stratum.
- **PERS** = {`persian`} — the Sasanian stratum.
- **HEB** = {`hebrew`, `hebrew-aramaic-shared`} — the Jewish-scriptural channel.
  **Reported with no locked direction**: the hypothesis makes no claim about it, and
  registering a direction I cannot justify would be padding.
- `greek`, `ethiopic`, `south-arabian`, `latin` — reported descriptively; too few types
  to test.

`hebrew-aramaic-shared` (163 rows, the largest class) is **deliberately kept OUT of
ARAM** in the primary. It denotes items whose Hebrew and Aramaic forms are
indistinguishable, i.e. a different (Jewish-scriptural) channel, and folding it in would
both conflate channels and swamp the contrast 186:35. It is added to ARAM in **tuple
T3** (§5) so the choice is testable rather than assumed.

---

## 4. Registered hypotheses, locked directions, and nulls

Phase index: Early Meccan 1, Middle Meccan 2, Late Meccan 3, Medinan 4.

Two nulls per hypothesis, of different kinds, per
`docs/statistical-rigor-protocol.md` §167:

- **Null A — donor-label permutation.** Permute `source_language` across the eligible
  types, preserving family sizes. Asks: *given these words' actual attestation patterns,
  is Jeffery's donor assignment special?* This is the null that directly interrogates the
  contested classification.
- **Null B — phase-label permutation.** Permute `noldeke_phase` across the 114 surahs,
  preserving phase sizes. Asks: *is the chronological arrangement special?*

Null A uses `random.Random(20260509)`, Null B `random.Random(20260510)`; 10,000 draws
each; replications at +10. One-sided `p = (1 + #{stat_perm >= stat_obs}) / 10001`.

### H1 — PRIMARY: composition shifts from Aramaic toward Persian

Among **ARAM ∪ PERS tokens only**, let `share_ARAM(phase)` be the ARAM fraction.

`Δ_H1 = share_ARAM(Late Meccan) − share_ARAM(Medinan)`

**Locked direction: `Δ_H1 > 0`.**

Conditioning on being a loanword token of one of the two families removes, by
construction, the overall loanword density (the parent's inverted-U), surah length, and
phase composition. This is why it is the primary rather than a density contrast.

### H2 — Aramaic density peaks Late Meccan

Per surah `s`: `d_ARAM(s)` = ARAM tokens per 1,000 orthographic words.
**Residualised** on `log(word count)` by OLS across the 114 surahs, per MW-1.

`Δ_H2 = mean_resid_ARAM(Late Meccan) − max over the other three phases of the same`

**Locked direction: `Δ_H2 > 0`** — Late Meccan must exceed *every* other phase, not
merely the average.

### H3 — Persian density peaks Medinan

`Δ_H3 = mean_resid_PERS(Medinan) − max over the other three phases`

**Locked direction: `Δ_H3 > 0`.**

### H4 — CO-PRIMARY, type-level: the confirmed-but-meaningless guard

**Each eligible type contributes exactly one observation**, so no frequent word can carry
the result. For type `t`, let `φ(t)` = the token-weighted mean phase index over its
attestations.

`Δ_H4 = mean φ(t) over PERS types − mean φ(t) over ARAM types`

**Locked direction: `Δ_H4 > 0`** — Persian vocabulary sits later in the sequence than
Aramaic/Syriac vocabulary.

H4 is the hypothesis that the historical claim actually requires. H1 can pass on two
words; H4 cannot.

---

## 5. Registered rules-tuples — all three locked before computing

Jeffery's etymologies are contested and `source_language` is **his scholarly judgement,
not consensus**. A negative result could be an artefact of his classification rather than
a fact about the text. All four hypotheses are therefore run under three tuples:

- **T1 (primary, gated):** registry as-is, all confidence levels, narrow ARAM.
- **T2 (sensitivity):** `confidence == HIGH` only (160 of 304 rows) — the subset where
  the registry expresses no uncertainty.
- **T3 (sensitivity):** ARAM broadened to include `hebrew-aramaic-shared`.

**Only T1 is gated.** T2 and T3 carry no p-value gate and cannot rescue a T1 failure.
**If the tuples disagree, that disagreement IS the finding and is reported as
`RULES-TUPLE-FRAGILE`.**

---

## 6. Robustness and controls (reported; never replace §4)

1. **Leave-one-type-out** on H1 and H4: the full range of the statistic when each
   eligible type is dropped in turn. **If H1's LOTO range crosses zero, H1 is reported as
   carried by a single word and demoted to CBM regardless of its p-value.**
2. **Per-type contribution table** for ARAM and PERS: type, tokens, φ(t), phase spread.
3. **Ambiguous-key sensitivity**: the 28 excluded entries re-included by pooling all
   candidate lemmas; descriptive only.
4. **Per-phase raw and residualised densities** for every donor family including HEB,
   greek, ethiopic, south-arabian, latin.
5. **`suyuti_naw_38_attested` split** — descriptive contrast between registry entries
   al-Suyūṭī also lists and those he does not. No p-value.
6. **Parent-instrument comparison**: total loanword tokens under this lemma join vs the
   surface-form matcher of `h_new_125_chronology_content.py`. Disagreement is expected
   and is reported, not reconciled.
7. **Phase-size control**: Late Meccan and Medinan have 21 and 24 surahs; per-phase token
   totals are reported so the reader can see the base rates the shares rest on.

---

## 7. Decision gates and verdict language, fixed now

Family = **8 registered inferences**: {H1, H2, H3, H4} × {Null A, Null B}.

- Bonferroni α = 0.05 / 8 = **0.00625**.
- Project novelty rule (`docs/statistical-rigor-protocol.md` §170) is stricter: corrected
  p < 0.005. **Raw decision gate = 0.005 / 8 = 0.000625**, i.e. `min(1, 8p) < 0.005`.

**A hypothesis PASSES iff its observed direction matches the lock AND both of its raw
p-values are < 0.000625.** Direction reversed, or either null failing, ⇒ NULL. No rescue
by threshold change, by dropping a null, or by substituting a sensitivity for a primary.

**The runner must implement exactly this rule.** Before any verdict is published, the
script's verdict logic is to be diffed line by line against this section — a published
verdict failed its own locked gate earlier in this project because the runner's rule was
looser than the registered one.

### 7.1 Verdict language

- **H1 PASS and H4 PASS** → `DONOR-LANGUAGE STRATIFICATION SUPPORTED`, with the
  *tawārud al-lughāt* rider of §1.2 and the Jeffery-classification dependency of §5.
- **H1 PASS and H4 NULL** → `CONFIRMED-BUT-MEANINGLESS`. The token-level shift is
  carried by a few frequent words whose chronology is already known from H-NEW-125's
  book-reference axis. This is the outcome §1.1 predicts.
- **H1 NULL** → no evidence that donor language stratifies by phase under this instrument.
  Publish as NULL; do not rescue with H2, H3 or any sensitivity tuple.
- **T1 and T2 disagree** → `RULES-TUPLE-FRAGILE`, whatever the p-values.

---

## 8. Honest limits, written before the result exists

1. **Jeffery's etymologies are contested**, and `source_language` is a single scholar's
   judgement encoded by a third party into a TSV. Every result is conditional on it.
2. **Ibn Jarīr's *tawārud al-lughāt* objection cannot be tested here** (§1.2). If the
   shared vocabulary reflects convergence rather than borrowing, the entire donor-language
   framing is void, and no permutation in this design speaks to it.
3. **The Nöldeke sequence is a philological reconstruction**, not a documented
   chronology. Every phase-indexed claim inherits that uncertainty. H-NEW-2570 states the
   same limit and it applies unchanged.
4. **The ARAM stratum is 13 types and ~63% two words** (§1.1). H4 and LOTO exist because
   of this, and a token-level-only pass means very little.
5. **~23% of registry rows do not join** to a unique QAC lemma and are excluded: 68
   unmatched, 28 ambiguous, 3 multiword. The exclusions are **not** random with respect to
   donor family — the feasibility check showed lower join rates for `syriac` and
   `aramaic` than for the larger classes. **This biases against the primary family and is
   the single most serious methodological limit here.**
6. **Token counts are lemma attestations, not disambiguated senses.** A lemma with two
   senses contributes all its tokens.
7. **No cross-corpus control.** Nothing establishes that any pattern found is specific to
   this corpus rather than general to seventh-century Ḥijāzī Arabic; no matched
   contemporary corpus with donor-language annotation exists on disk.
8. **`hebrew-aramaic-shared` is 54% of the registry** and its exclusion from ARAM in T1
   is a researcher decision, registered and tested in T3 but a decision nonetheless.

---

## 9. Required immutable run record

The run creates `findings/phase-b-hypotheses/runs/h-new-2700/<UTC timestamp>/`
containing `result.json` and `manifest.json` (command, git commit, prereg/script/input
SHA-256, Python version, seeds, platform).

**Paths recorded in the manifest must be relative to the repository root** so the run is
committable as-is and no local or tooling directory name is written into the record.

**Nothing in any run directory may ever be overwritten or deleted, including an
uncommitted or superseded one.** This restates the standing correction at
`h-new-2540-form-v-valency.md` §8.1. A run whose record cannot be committed is handled by
re-running to an **additional** directory and retaining both.

The runner emits no interpretive prose.
