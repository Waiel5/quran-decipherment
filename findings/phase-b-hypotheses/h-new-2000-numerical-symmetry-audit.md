---
finding_id: H-NEW-2000
title: "Iʿjāz ʿadadī (numerical word-symmetry) claims — multi-rules-tuple audit"
type: classical-claim-audit
genre: numerical-word-balance (Nawfal / Jarrar / al-Kaheel)
date: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260509
prereg_sha256: 0474c9986636fe2543f7a9ce3aff4d1c77e82bbf2108648c9bb2b824798b3789
phase: B
verdict: "0 CONFIRMED / 4 RULES-FRAGILE / 4 FALSIFIED / 1 descriptive / 1 not-a-balance"
---

# H-NEW-2000 — The "Balanced Words" (iʿjāz ʿadadī) Claims: A Multi-Rules Audit

## 0. What this audits

The popular "numerical miracle of the Quran" literature — chiefly ʿAbd al-Razzāq
Nawfal, and its later popularisers Bassām Jarrār and ʿAbd al-Dāʾim al-Kuḥayl — asserts
that the Quran balances pairs of antonyms to the exact same count, and matches calendar
words to astronomical numbers. The most-cited English digest of these claims is the
FUNCI (Fundación de Cultura Islámica) summary
(`data/literature/nawfal/funci-miracle-of-numbers-in-quran.md`), which is the
target-value source for this audit.

This is the **same genre** the project already adjudicated for al-Khalifa's "miracle of
19" (MASTER-FINDINGS-LEDGER §10.55 H-NEW-1600, §10.60 H-NEW-1530). That audit
established a diagnostic signature: **pre-existing classical-textual facts confirm;
novel-numerical claims fail.** This audit asks whether the *word-balance* sub-genre
behaves the same way, and — crucially — whether any balance survives once the counting
rule is fixed BEFORE the count is read.

Pre-registration locked at SHA `0474c9986636fe2543f7a9ce3aff4d1c77e82bbf2108648c9bb2b824798b3789`,
runtime-verified by the script.

## 1. The three counting rules (pre-committed)

Every claim is computed under three rules, specified before observation:

- **R1 — strict-al-form**: the definite-article surface lexeme only (e.g. `الدنيا`),
  substring on the Hafs-Kūfan no-tashkeel corpus (`quran-text/quran-no-tashkeel.json`).
  Closest to how the claims are *worded*.
- **R2 — all-morphological-forms (surface)**: all inflected surface forms of the
  semantic lexeme regardless of definiteness / proclitics, with homonym exclusions
  documented per claim.
- **R3 — QAC-lemma**: the Quranic Arabic Corpus v0.4 lemma
  (`data/morphology/quranic-corpus-morphology-0.4.txt`) — the most linguistically
  principled rule, since lemma membership is annotated independently by Dukes (2011).

The discipline: a claim **CONFIRMS** only if its claimed balance holds EXACTLY under a
rule that is *principled* (the natural reading of its own wording, or the canonical
lemma) and was named in advance. It is **RULES-FRAGILE** if the balance holds only under
a selectively-constructed rule, or under one rule while breaking under equally-defensible
neighbours. It is **FALSIFIED** if no defensible rule recovers the claim.

## 2. Summary table

| # | Claim | Claimed | Strict (R1) | Best-balancing rule | Verdict | Principled? |
|:-:|:--|:--|:--|:--|:--|:--|
| 1 | al-dunyā = al-ākhira | 115 = 115 | 115 vs **112** | R2 all-clitic-forms → 115 = 115 | **RULES-FRAGILE** | semi (asymmetric rule) |
| 2 | al-malāʾika = al-shayāṭīn | 88 = 88 | — | R3 whole-lemma → 88 = 88 | **RULES-FRAGILE** | NO (plural 73 ≠ 18) |
| 3 | al-ḥayāt = al-mawt | 145 = 145 | 67 vs 53 | none | **FALSIFIED** | n/a |
| 4 | shahr=12 / yawm=365 / ayyām=30 | 12 / 365 / 30 | 12 ✓ / **375** / 30 ✓ | partial (2 of 3) | **RULES-FRAGILE** | mixed |
| 5 | al-rajul = al-marʾa | 24 = 24 | — | none (29 vs 26) | **FALSIFIED** | n/a |
| 6 | Iblīs = istiʿādha | 11 = 11 | Iblīs 11 ✓ | refuge=11 only via form-1+4 subset | **RULES-FRAGILE** | NO (selective subset) |
| 7 | al-malak vs al-shayṭān (sing) | balance | 13 vs 70 | none | **DESCRIPTIVE** | diagnostic |
| 8 | al-ṣāliḥāt = al-sayyiʾāt | balance | — | none (62 vs 36) | **FALSIFIED** | n/a |
| 9 | al-rasūl / rusul | (descriptive) | — | rasūl lemma = 332 | **NOT-A-BALANCE** | n/a |
| 10 | baḥr : barr = 32 : 13 | 71.1% water | 41 vs 22 | none | **FALSIFIED** | n/a |

**Tally: 0 CONFIRMED · 4 RULES-FRAGILE · 4 FALSIFIED · 1 descriptive · 1 not-a-balance.**

Not one balance claim survives a pre-specified principled counting rule. This is the
**exact al-Khalifa signature** (§10.55 / §10.60): the numbers that *do* land exactly are
single-lexeme facts of the canonical text (al-dunyā = 115; shahr = 12; ayyām = 30; Iblīs
= 11); the claimed *symmetries* and *astronomical matches* fail or require a rule chosen
to fit the target.

## 3. Per-claim findings (equal prominence to passes and fails)

### Claim 1 — al-dunyā = al-ākhira (claimed 115 = 115): RULES-FRAGILE

The most famous of all the pairs, and the most instructive.

- `الدنيا` (al-dunyā) appears as a **single surface form, always definite, 115 times** —
  no bare or cliticised variants exist in the corpus. So R1 = R2 = R3 = **115** for
  dunyā. This number is a genuine, robust corpus fact.
- al-ākhira does **not** match 115 under the naive rule:
  - R1 strict `الآخرة` = **112** (misses the proclitic forms).
  - R3 QAC-lemma `A^xir` = **155** (includes adjectival/temporal *ākhir* "last/latter",
    not just the eschatological noun).
  - R2 all-surface-forms of the eschatological noun =
    `الآخرة`(71) + `بالآخرة`(21) + `والآخرة`(19) + `وللآخرة`(2) + `للآخرة`(1) + `وبالآخرة`(1)
    = **115**.

So the balance **115 = 115 is real**, but only under an *asymmetric* rule: dunyā is
counted bare-definite (it needs no clitics), while ākhira is counted as the
eschatological noun in **all** its proclitic positions **and** with non-eschatological
*ākhir* excluded. That rule is *defensible on semantic grounds* ("count the noun 'the
Hereafter' wherever it occurs as that noun"), which is why the claim is not outright
FALSIFIED. But it is decisively **rule-dependent**: it breaks at 112 under strict
definite-surface and at 155 under the canonical lemma. The popular literature never
states which rule it uses; the balance is a *property of one specific lens*, not a
rule-invariant fact. **RULES-FRAGILE.**

### Claim 2 — al-malāʾika = al-shayāṭīn (claimed 88 = 88): RULES-FRAGILE

A textbook conflation artifact.

- QAC whole-lemma: `malak` (angel) = **88**, `$ayoTa`n` (devil) = **88**. Balanced.
- But the gloss "angels / devils" is **plural**, and the plural counts are wildly
  unbalanced: malāʾika (plural) = **73** vs shayāṭīn (plural) = **18**.
- The whole-lemma 88 = 88 holds only because the morphological composition is *inverted*:
  angels are mostly plural (73 plural + 13 singular + 2 dual), devils mostly singular
  (70 singular + 18 plural). The two 88s are made of opposite material.

The balance is real at the lemma-total level, but the claim as glossed ("angels equal
devils") silently equates a mostly-plural word with a mostly-singular word. The rule that
balances (whole-lemma) is not the rule the gloss implies (plurals). **RULES-FRAGILE.**

> **Reconciliation with H-NEW-2020 (§10.79).** The prior surface-word scan reported
> al-ākhira at 71 (strict `الآخرة`) and a "broad conflation" of 194, concluding the
> 115/115 legend was FALSIFIED at the surface level. This audit pinpoints why both
> bracketed the truth: the eschatological **noun** `آخرة` (feminine, tā-marbūṭa) occurs
> in exactly six proclitic surface forms — `الآخرة`(71) + `بالآخرة`(21) + `والآخرة`(19)
> + `وللآخرة`(2) + `للآخرة`(1) + `وبالآخرة`(1) = **115** — every one of them "the
> Hereafter". The 194 figure additionally swept in the *masculine adjective* `الآخر`
> "the Last/Other" (29), `الآخرين` (13), `آخر` "another" (10), etc., which are *ākhir/
> ākhar*, not *al-ākhira* the Hereafter. So the dunyā/ākhira balance is **115 = 115 exact
> under the linguistically-correct rule** (count the eschatological noun in all clitic
> positions), but it is fragile: it collapses to 112/71 under strict-definite-only and
> to 155 under the QAC lemma that re-merges the adjective. RULES-FRAGILE is the precise
> verdict — sharper than the prior flat FALSIFIED, and for a stated reason.

### Claim 3 — al-ḥayāt = al-mawt (claimed 145 = 145): FALSIFIED

No rule hits 145, and the pair never balances:
- noun lemmas: ḥayāt (`Hayaw`p`) = **76** vs mawt (`mawot`) = **50**.
- strict definite `الحياة` = **67** vs `الموت` = **53**.
- whole-root totals: Hyy = **184** vs mwt = **165**.

The "145 each" target appears under none of these. The 145 figure in the literature is
reconstructed by summing a hand-picked bundle of life-derived and death-derived forms
(verbs + nouns + adjectives in unequal selections) — a bundle with no principled
boundary. **FALSIFIED** on the canonical corpus.

### Claim 4 — calendar (shahr = 12, yawm = 365, ayyām/dual = 30): RULES-FRAGILE (2 of 3)

This is the most interesting claim, and it splits:
- **shahr (month), singular = 12 EXACTLY** ✓. The lemma `$ahor` has 21 tokens: 12
  singular, 7 plural (ashhur/shuhūr), 2 dual (shahrayn). The singular count is exactly 12
  — a clean, genuine match to the 12 months.
- **ayyām (days, plural) + yawmayn (dual) = 27 + 3 = 30 EXACTLY** ✓. Another clean match.
- **yawm (day, singular) = 375, NOT 365** ✗. The QAC lemma `yawom` has 405 tokens: 375
  singular, 27 plural, 3 dual. (The adverb *yawmaʾidhin* "on that day", 70 tokens, is a
  **separate QAC lemma** `yawoma}i*` and is already excluded.) There is no principled
  grouping that yields 365: bare singular is 375; adding/removing duals gives 378/372.
  The famous "365 days = days in a year" claim is **off by 10** and cannot be recovered
  without an arbitrary subtraction.

Two of three sub-targets land exactly; the headline astronomical match (365) fails. The
claim as a *package* is **RULES-FRAGILE** — the two genuine hits (12, 30) are corpus
facts, but the most-advertised number is wrong, and presenting the package as a unified
miracle requires ignoring the miss.

### Claim 5 — al-rajul = al-marʾa (claimed 24 = 24): FALSIFIED

QAC lemmas: rajul (man, singular) = **29**, imraʾa (woman / wife) = **26**. Neither
equals the claimed 24, and they do not balance each other. The plurals are also
unbalanced (rijāl 28 vs nisāʾ 59). The "24 each" claim is recovered only by excluding
certain figurative or generic *rajul* usages by hand — a gerrymander with no stated rule.
**FALSIFIED.**

### Claim 6 — Iblīs (11) = istiʿādha / seeking-refuge (11): RULES-FRAGILE

- **Iblīs proper-noun = 11 EXACTLY** ✓ (QAC lemma `<iboliys`; robust). This half is a
  clean corpus fact.
- The "seeking refuge" side has **no unique natural total**. Root ʿ-w-dh (`Ew*`):
  - form-1 *ʿādha / aʿūdhu / yaʿūdhu* (lemma `Eu*o`) = **10**
  - form-4 *uʿīdhu* ("I commend her to refuge", Q 3:36) = **1**
  - form-10 *istaʿidh* (imperative) = **4**
  - noun *maʿādh* = 2; all verbs = **15**; all root tokens = **17**.
  - The target 11 is recoverable **only** as form-1 + form-4 (10 + 1), which *excludes*
    the 4 *istaʿidh* imperatives. That boundary is selective — there is no
    principled reason to count *uʿīdhu* but not *istaʿidh*, both of which are
    refuge-seeking verbs.

Iblīs = 11 is solid; refuge = 11 requires a hand-drawn subset. The PAIRING is therefore
**RULES-FRAGILE**, not the confirmed PASS reported in the inline H-NEW-2000 note. The
inline note's "balanced!" claim is here refined: the *Iblīs* count is exact, but the
*refuge-verb* count is rule-sensitive and does not have a natural 11.

### Claim 7 — al-malak vs al-shayṭān, singular (diagnostic): DESCRIPTIVE

The singulars do **not** balance: angel-singular = **13**, devil-singular = **70**. This
is the direct diagnostic for Claim 2: at the singular level the two words are nowhere near
each other (devils ×5.4 angels), and at the plural level the relationship inverts
(angels ×4.1 devils). Only the *whole-lemma totals* coincide at 88. This asymmetry is the
mechanical reason the "88 = 88" balance exists, and it shows the balance is not a
semantic symmetry between "angels" and "devils" but an arithmetic coincidence of two
differently-distributed lemmas.

### Claim 8 — al-ṣāliḥāt = al-sayyiʾāt: FALSIFIED

QAC lemmas: ṣāliḥāt (good deeds, fem. pl.) = **62** vs sayyiʾāt (bad deeds, pl.) = **36**.
Not balanced under any reading. (sayyiʾa singular adds 22; even ṣāliḥāt vs sayyiʾa-all
does not converge.) **FALSIFIED.**

### Claim 9 — al-rasūl / rusul frequency: NOT-A-BALANCE-CLAIM

Descriptive only — the source asserts no symmetry target. rasūl lemma = **332** (one of
the highest-frequency theological nouns), mursal lemma = 35. Reported for completeness;
no verdict possible because no balance is claimed.

### Claim 10 — baḥr (sea) : barr (land) = 32 : 13 → 71.1% water: FALSIFIED

The most-circulated "scientific" iʿjāz-ʿadadī claim, and it fails on the actual counts.
- baḥr (sea), QAC lemma `baHor` = **41**, NOT the claimed 32.
- barr (land, geographic), QAC lemma `bar~` = **22**, NOT the claimed 13. (The homonym
  *birr* "righteousness/piety", lemma `bir~` = 8, and *tabarru* = 2, are correctly
  **excluded** — including them would only inflate further.)
- Strict water percentage = 41 / (41 + 22) = **65.1%**, not 71.1%. Even with the FUNCI
  variant "barr/arḍ" (adding arḍ "earth" = 461), the ratio collapses entirely — arḍ is
  two orders of magnitude larger than baḥr, giving ~8% "water", which is why the popular
  claim quietly uses *barr* alone and then mis-states it as 13.

No principled sea/land rule yields 32 : 13 or 71.1%. **FALSIFIED.** The claimed match to
Earth's actual ocean fraction (~71%) does not hold on the canonical text.

## 4. The diagnostic — same signature as al-Khalifa

The numbers that **do** land exactly are all **single-lexeme facts** of the canonical
text, none of which is a *symmetry*:
- al-dunyā = 115 (the always-bare-definite form)
- shahr (singular) = 12
- ayyām + yawmayn = 30
- Iblīs = 11

Every claimed **antonym balance** and every claimed **astronomical match** either fails
outright (ḥayāt/mawt, rajul/marʾa, ṣāliḥāt/sayyiʾāt, baḥr/barr, yawm = 365) or holds only
under a lens chosen to fit the target (dunyā/ākhira under all-clitic-forms; malāʾika/
shayāṭīn under whole-lemma-not-plural; refuge under a hand-drawn verb subset). This is
the **exact pattern** H-META-1 predicts for the modern-numerology era and the al-Khalifa
audits (§10.55 / §10.60) demonstrated for Code-19: *pre-existing textual facts confirm;
the novel-symmetry claims that would constitute new evidence do not.*

The deeper methodological point: these claims are **rules-tuple-sensitive by
construction**. Because the popular literature never publishes its counting rule, each
"balance" is the product of a garden-of-forking-paths search across {which morphological
forms, which homonyms, which clitics, which figurative senses to include} until a target
is hit. Pre-registering the rule before counting — the discipline of this project —
removes that freedom, and when it is removed, **zero of the ten claims confirm.**

## 5. Honest limits

- The FUNCI digest is one popularisation; individual authors (Nawfal 1980s; Jarrār;
  al-Kuḥayl) use slightly different catalogues and may reach their totals by counting
  conventions not reconstructable from the digest. This audit tests the *claimed target
  values* against principled rules; it does not claim to reproduce each author's private
  method. Where an author's method is the very gerrymander this audit flags, that is the
  finding, not a gap.
- QAC v0.4 lemma boundaries are Dukes's analytic choices; a different lemmatiser could
  shift a count by one or two (e.g. whether a borderline participle is *ākhir* the
  adjective or the noun). None of the shifts plausible at that scale rescues a FALSIFIED
  claim (the gaps are 10–40, not 1–2), and the RULES-FRAGILE verdicts already disclose
  the rule-dependence explicitly.
- The dunyā = 115 and shahr = 12 and ayyām = 30 and Iblīs = 11 single-lexeme counts are
  robust corpus facts and are reported as such with equal prominence to the failures.
  What fails is the *symmetry/astronomical interpretation* laid over them.
- Theological status is out of scope. This audit adjudicates the *empirical numerical
  claims* only; it makes no claim about the Quran's theological iʿjāz, which classical
  scholarship (al-Bāqillānī, al-Khaṭṭābī) located in language and meaning, **not**
  arithmetic — a position this project has repeatedly vindicated (H-NEW-930, H-NEW-950,
  the 8-deep numerology-NULL streak).

## 6. Cross-references

- **H-NEW-2010** (root-level exhaustive balance scan, NULL with reversal) and
  **H-NEW-2020 / §10.79** (surface-word balance scan, "1 of 13 pairs balances") — the
  exhaustive-generator siblings of this per-claim audit. H-NEW-2000 supplies the detailed
  rules-tuple breakdown those scans summarised, and **refines H-NEW-2020's
  dunyā/ākhira FALSIFIED** verdict to RULES-FRAGILE by isolating the clean
  eschatological-noun-all-clitic-forms count of 115 (see §3 Claim 1 reconciliation box)
  that the prior scan's strict-71 / broad-194 rules bracketed but did not pin.
- MASTER-FINDINGS-LEDGER §10.55 (H-NEW-1600) and §10.60 (H-NEW-1530) — al-Khalifa Code-19
  audits; same genre, same diagnostic signature.
- §10.61 (H-NEW-1720) — al-Raḥmān / al-Raḥīm derivative-count falsifications.
- H-META-1 (claim-signature classifier) — modern-numerology era 0% confirmation;
  numerical-gematric substance type low confirmation rate. This audit is a direct
  integer-equality demonstration on the word-balance sub-genre.
- H-NEW-930 (modular verse-counts NULL), H-NEW-950 (divine-name spectral NULL) — the
  project's numerology-NULL streak; iʿjāz is structural-architectural, not arithmetic.
- Inline H-NEW-2000 note (origin of this task) — REFINED here: dunyā=115/ākhira≠115
  confirmed; Iblīs=11 confirmed but the refuge=11 "PASS" downgraded to RULES-FRAGILE;
  malāʾika(73)/shayāṭīn(18) imbalance confirmed and explained as the mechanism behind the
  88=88 lemma coincidence.

## 7. Files

- pre-reg: `findings/phase-b-hypotheses/prereg-h-new-2000-numerical-symmetry-audit.md`
  (SHA `0474c9986636fe2543f7a9ce3aff4d1c77e82bbf2108648c9bb2b824798b3789`)
- script: `findings/phase-b-hypotheses/scripts/h-new-2000.py` (runtime SHA-verified)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2000.json`
- target-value source: `data/literature/nawfal/funci-miracle-of-numbers-in-quran.md`
- data: `quran-text/quran-no-tashkeel.json`,
  `data/morphology/quranic-corpus-morphology-0.4.txt`

*Logged 2026-05-29 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
