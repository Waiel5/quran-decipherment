---
finding_id: H-NEW-2230
title: "QAC-lemma re-run of the numerical-symmetry series (homograph-disambiguated)"
type: classical-claim-audit
genre: numerical-word-balance (Nawfal / Jarrār / al-Kuḥayl) + kallā distribution
date: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260529
prereg_sha256: 1967b6e447442c50d4527323afb06c8404cd33a4e96b89e49dd502287d57203a
phase: B
closes: "MASTER-FINDINGS-LEDGER §10.80.3 open follow-up"
verdict: "0 of 6 balance claims CONFIRMED-clean at lemma-strict (direction held); 5 RULES-FRAGILE/FALSIFIED + kallā CONFIRMED = 33"
---

# H-NEW-2230 — QAC-Lemma Re-Run of the Numerical-Symmetry Series (Disambiguated)

## 0. What this closes

MASTER-FINDINGS-LEDGER §10.80.3 left two open follow-ups after the *kallā* audit
(H-NEW-2160): (a) full QAC-lemma disambiguation of all 38 `كلا` substring tokens to
pin the exact rebuke-*kallā* count, and (b) re-run the famous balance claims at
QAC-lemma level (homograph-disambiguated). This finding does both.

The *kallā* lesson (§10.80.1) is the methodological pivot: **raw substring counting
LIES** because the consonantal skeleton conflates homographs. The QAC v0.4 lemma +
part-of-speech annotation (Dukes 2011, `data/morphology/quranic-corpus-morphology-0.4.txt`)
is the disambiguated gold standard. H-NEW-2000 already used QAC-lemma as one of its
three rules; this re-run makes the lemma the *primary* instrument, foregrounds the
homograph caveat per claim, and adds a within-lemma morphological disambiguation for
the Hereafter-noun that sharpens the dunyā/ākhira verdict.

Pre-registration locked at SHA
`1967b6e447442c50d4527323afb06c8404cd33a4e96b89e49dd502287d57203a`, runtime-verified.

## 1. Direction-locked prediction (set BEFORE recomputation)

> **≤ 1 of the 6 balance claims confirms EXACTLY at R-lemma-strict** — i.e. QAC-lemma
> disambiguation does NOT rescue the antonym-balance symmetries; numerology stays
> retired. For *kallā*: rebuke-lemma = 33 (al-Dānī).

**Result: 0 of 6 balance claims CONFIRMED-clean at lemma-strict — direction HELD
(strictly stronger than the ≤1 bound). kallā = 33 EXACTLY, CONFIRMED.**

## 2. Disambiguated-count table (claimed vs QAC-lemma, side by side)

| # | Claim | Claimed | R-lemma-strict (QAC) | Best rescuing rule | Verdict |
|:-:|:--|:--|:--|:--|:--|
| 1 | al-dunyā = al-ākhira | 115 = 115 | dunyā **115** vs ākhira-whole-lemma `A^xir` **155** | fem-noun tā-marbūṭa subset → **115 = 115** | **RULES-FRAGILE** |
| 2 | al-ḥayāt = al-mawt | 145 = 145 | ḥayāt-noun **76** vs mawt-noun **50** | none (root 184 vs 165) | **FALSIFIED** |
| 3 | al-malāʾika = al-shayāṭīn | 88 = 88 | whole-lemma **88 = 88** | none principled (plural 73 ≠ 18) | **RULES-FRAGILE** |
| 4 | al-rajul = al-marʾa | 24 = 24 | rajul **29** vs imraʾa **26** | none | **FALSIFIED** |
| 5 | shahr / yawm / ayyām | 12 / 365 / 30 | shahr-sing **12** ✓ / yawm-sing **375** ✗ / ayyām+dual **30** ✓ | partial (2 of 3) | **RULES-FRAGILE** |
| 6 | Iblīs = istiʿādha | 11 = 11 | Iblīs **11** ✓ / refuge: form-1 **10**, all-verbs **15**, all-root **17** | refuge=11 only via form-1+4 subset | **RULES-FRAGILE** |
| 7 | **kallā rebuke-lemma** | **33** | **POS:AVR LEM `kal~aA` = 33** | — (raw substring 38 conflates 5 *kullan*) | **CONFIRMED** |

**Balance tally (claims 1–6): 0 CONFIRMED-clean · 3 RULES-FRAGILE · 2 FALSIFIED · 1
RULES-FRAGILE(calendar).** Not one antonym balance survives the homograph-disambiguated
lemma-strict rule. **kallā = 33 CONFIRMED** after disambiguation.

This reproduces the H-NEW-2000 / al-Khalifa signature *at the gold-standard lemma
level*: the numbers that land exactly are **one-sided single-lexeme corpus facts**
(dunyā = 115, shahr-sing = 12, ayyām = 30, Iblīs = 11), never the claimed *symmetry*.

## 3. Per-claim findings (equal prominence)

### Claim 1 — al-dunyā = al-ākhira (claimed 115 = 115): RULES-FRAGILE

- `d~unoyaA` = **115** at R-lemma-strict. A single, always-bare-definite lemma; this
  number is a robust corpus fact — but it is **CONFIRMED-BUT-MEANINGLESS** as a
  *symmetry*, because it is one-sided.
- The QAC lemma `A^xir` = **155** — this is the homograph trap. It includes the
  eschatological noun *al-ākhira* "the Hereafter" **and** the masculine adjective
  *ākhir* "last/latter". (`A^xar` "other" = **70** is a *separate* lemma, correctly
  excluded.)
- **Within-lemma disambiguation (the sharpening this re-run adds):** the feminine
  tā-marbūṭa surface forms of `A^xir` — `'aAxirapi`(92) + `'aAxirapa`(13) +
  `'aAxirapu`(10) = **115** — are exactly the Hereafter-noun *al-ākhira*. The 40
  remaining tokens (`'aAxiri` 24, `'aAxiriyna` 10, `'aAxira` 4, `'aAxiru` 2) are
  adjectival *ākhir/ākhirīn*. So **115 = 115 is real**, but only under the within-lemma
  fem-noun subset (R-lemma-fem-noun). It **breaks at 155 under whole-lemma-strict**.
  This is cleaner than H-NEW-2000's "all-clitic-surface-forms" rule (the balance lives
  inside one QAC lemma, selectable by the gender feature), but it is still a *subset
  rule* — **RULES-FRAGILE**, not CONFIRMED. Refines §10.80 Claim 1.

### Claim 2 — al-ḥayāt = al-mawt (claimed 145 = 145): FALSIFIED

ḥayāt-noun `Hayaw\`p` = **76**, mawt-noun `mawot` = **50**. Whole-root totals
Hyy = **184** vs mwt = **165**. No lemma rule hits 145 and the pair never balances.
The 145 is a hand-summed bundle with no principled boundary. **FALSIFIED.**

### Claim 3 — al-malāʾika = al-shayāṭīn (claimed 88 = 88): RULES-FRAGILE

Whole-lemma `malak` = **88**, `$ayoTa\`n` = **88** — balanced. But this is a
**conflation artifact**: the gloss "angels/devils" is plural, and the plurals are
wildly unbalanced (malāʾika-plural **73** vs shayāṭīn-plural **18**), while the
singulars invert (angel-sing **13** vs devil-sing **70**). The two 88s are built from
opposite morphological material. The rule that balances (whole-lemma) is not the rule
the gloss implies. **RULES-FRAGILE.**

### Claim 4 — al-rajul = al-marʾa (claimed 24 = 24): FALSIFIED

`rajul` = **29**, `{mora>at` (woman/wife) = **26**; neither = 24 and they do not
balance. Plurals rijāl **28** vs nisāʾ **59** also unbalanced. **FALSIFIED.**

### Claim 5 — calendar (shahr = 12, yawm = 365, ayyām = 30): RULES-FRAGILE (2 of 3)

- shahr `$ahor` **singular = 12 EXACTLY** ✓ (21 total: 12 sing, 2 dual, 7 plural). Fact.
- ayyām + yawmayn (plural + dual of `yawom`) = **30 EXACTLY** ✓. Fact.
- yawm `yawom` **singular = 375, NOT 365** ✗ (405 total: 375 sing, 3 dual, 27 plural;
  the adverb *yawmaʾidhin* is a separate lemma `yawoma}i*` and is correctly excluded).
  The flagship astronomical match is **off by 10**. **RULES-FRAGILE** — the two clean
  facts (12, 30) are real; the headline (365) is wrong.

### Claim 6 — Iblīs (11) = istiʿādha (11): RULES-FRAGILE

Iblīs `<iboliys` = **11 EXACTLY** ✓ (robust one-sided fact). The refuge side (root
`Ew*`) has **no natural 11**: form-1 *aʿūdhu* `Eu*o` = **10**, all-verbs = **15**,
all-root = **17**. The 11 is recoverable only as form-1 + form-4 *uʿīdhu* (10 + 1),
which gerrymanders out the 4 form-10 *istaʿidh* imperatives — a selective boundary
with no principled basis. **RULES-FRAGILE.**

### Claim 7 — kallā rebuke-lemma (claimed 33, al-Dānī): CONFIRMED

The gold-standard disambiguation, and the close of the §10.80.3 follow-up.

- **Raw substring** standalone `كلا` token = **38**, across both halves (earliest Q 4:130).
  This *appears* to refute al-Dānī's 33-second-half claim.
- **QAC POS+LEM disambiguation**: the rebuke particle is tagged **POS:AVR** (aversion
  particle) with lemma **`kal~aA`**. That count is **exactly 33**.
- The **5-token gap** is fully resolved: the 5 first-half `كلا` tokens are the
  quantifier *kullan* "each" (POS:N, LEM `kul~`, accusative-indefinite surface
  `kul~FA`), NOT the rebuke:

  | loc | QAC LEM | QAC POS | gloss |
  |:--|:--|:--|:--|
  | 4:130 | `kul~` | N | *kullan min saʿatih* "each from His abundance" |
  | 6:84 | `kul~` | N | *kullan hadaynā* "each We guided" |
  | 7:46 | `kul~` | N | *yaʿrifūna kullan* "they know each" |
  | 11:111 | `kul~` | N | *wa-inna kullan* "and indeed each" |
  | 17:20 | `kul~` | N | *kullan numiddu* "each We extend" |

- All 33 rebuke-*kallā* are in **surahs ≥ 19** (none in Q 1–18). Distribution:
  Q19(2), Q23(1), Q26(2), Q34(1), Q70(2), Q74(4), Q75(3), Q78(2), Q80(2), Q82(1),
  Q83(4), Q89(2), Q96(3), Q102(3), Q104(1). **18 of 33 (55%) fall in the short
  mufaṣṣal Q78–104 (juzʾ 29–30).**

**Verdict: CONFIRMED — rebuke-kallā = 33 exactly, vindicating al-Dānī (via al-Suyūṭī
*al-Itqān* nawʿ 40) once the homograph is disambiguated.**

**Honest nuance on "second half":** 6 of the 33 (Q19, 23, 26, 34) precede the strict
surah-count midpoint (Q58); 27 are at Q50+. The classical "latter half" is the
*mufaṣṣal* framing, not a strict 1–57 / 58–114 split. What is exact and rule-invariant
is **the count (33)** and **the heavy mufaṣṣal concentration**; the "every single one
after the midpoint" reading is the loose popular paraphrase, slightly stronger than the
data, and is reported as such rather than smoothed over. The 6 early attestations are
narrative rebukes (e.g. Pharaoh at Q26:62, Q26:15; the idolaters at Q19:79–82) — still
genuine rebuke-*kallā*, still POS:AVR.

## 4. The bidirectional rules-tuple lesson, both directions in one finding

This finding is the clean demonstration that **disambiguation cuts both ways**
(`feedback_rules_tuple_bidirectional`):

- **It RETIRES** the antonym balances (claims 1–6): at the principled lemma-strict
  rule, 0 of 6 confirm cleanly. The "balances" survive only as conflation artifacts
  (88=88), within-lemma subsets (115=115), or gerrymandered totals (refuge=11).
- **It RESCUES** the *kallā* claim (claim 7): raw substring (38, both halves) falsifies
  al-Dānī; lemma+POS disambiguation (33, mufaṣṣal) vindicates a 1,000-year-old
  observation.

Same instrument, opposite effects, decided entirely by whether the underlying claim
tracks a real morphological category. The numerology-balance claims do not (they ride
on homograph/morphology conflations); al-Dānī's distributional observation does (the
rebuke particle is a genuine POS class).

## 5. Honest limits

- QAC v0.4 lemma + POS boundaries are Dukes's analytic choices. A different
  lemmatiser could move a count by one or two (e.g. a borderline `'aAxira` token). None
  of the plausible ±1–2 shifts rescues a FALSIFIED balance (gaps are 10–40) or unmakes
  kallā = 33 (the POS:AVR tag is categorical, not borderline).
- The "all second-half" phrasing of the kallā claim is the popular paraphrase; the
  *exact* result is count = 33 with mufaṣṣal concentration and 6 pre-midpoint
  attestations (§3 Claim 7 honest nuance). This is reported with equal prominence to
  the CONFIRMED count.
- Single-lexeme facts (dunyā 115, shahr 12, ayyām 30, Iblīs 11) are robust corpus
  facts and are labelled CONFIRMED-BUT-MEANINGLESS *as symmetries* — they are real
  numbers, just not the claimed balances.
- Theological iʿjāz is out of scope; this audits the empirical numerical claims only.

## 6. Cross-references

- **§10.80 H-NEW-2160 (kallā inline)** — this finding closes its §10.80.3 follow-up and
  pins the exact 33 (POS:AVR) with full per-token disambiguation of all 38 substring
  tokens.
- **§10.80 H-NEW-2000** — the three-rules per-claim audit; H-NEW-2230 confirms its
  lemma-level (R3) results and **sharpens Claim 1** from "all-clitic-surface-forms" to
  the within-lemma fem-noun tā-marbūṭa subset (115 lives inside `A^xir` by gender).
- **H-NEW-2010 / 2020 (§10.79)** — exhaustive balance generators; balanced-words family
  RETIRED. H-NEW-2230 is the lemma-gold-standard confirmation of that retirement.
- **§10.55 / §10.60 (al-Khalifa Code-19)** — same genre, same diagnostic: pre-existing
  textual facts confirm, novel symmetries fail.
- **`feedback_rules_tuple_bidirectional`** (memory) — this finding is the textbook
  bidirectional case: one disambiguation retires six claims and rescues one.

## 7. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2230-qac-lemma-numerical-rerun.md`
  (SHA `1967b6e447442c50d4527323afb06c8404cd33a4e96b89e49dd502287d57203a`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2230.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2230.json`
- data: `data/morphology/quranic-corpus-morphology-0.4.txt`,
  `quran-text/quran-no-tashkeel.json`

*Logged 2026-05-29 by Waiel Al-Shujaa. The lemma is the gold standard. The single-word
counts are real; the symmetries are not; al-Dānī's kallā = 33 is. Bismillāhi al-Raḥmāni
al-Raḥīm.*
