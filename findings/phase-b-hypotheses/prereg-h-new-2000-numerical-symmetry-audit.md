---
finding_id: H-NEW-2000
title: "Iʿjāz ʿadadī (numerical word-symmetry) claims — multi-rules-tuple audit"
type: pre-registration
date: 2026-05-29
author: Waiel Al-Shujaa
seed: 20260509
status: LOCKED
phase: B
---

# Pre-Registration — H-NEW-2000

## Numerical word-symmetry ("iʿjāz ʿadadī") claims, multi-rules audit

This pre-registration is written and SHA256-locked BEFORE any verdict is read. It
audits the most-cited "balanced words" claims of the Nawfal / Jarrar / al-Kaheel
"iʿjāz ʿadadī" tradition, as summarised in the FUNCI source
(`data/literature/nawfal/funci-miracle-of-numbers-in-quran.md`, fetched 2026-04-12,
attributing the research to ʿAbd al-Razzāq Nawfal, Bassām Jarrār, ʿAbd al-Dāʾim
al-Kuḥayl). It extends the al-Khalifa Code-19 audit precedent
(MASTER-FINDINGS-LEDGER §10.55 H-NEW-1600, §10.60 H-NEW-1530) to the
word-pair-balance genre — the same family, a different observable.

### Genre context and prior

The al-Khalifa audit established the project's diagnostic signature for this genre:
**pre-existing classical-textual facts confirm; novel-numerical claims fail.** The
iʿjāz-ʿadadī word-balance claims are KNOWN in the popular literature to be
rules-tuple-sensitive (different "counters" reach the claimed totals by silently
choosing which morphological forms, which homonyms, and which figurative senses to
include or exclude). The pre-registered concern is therefore **garden-of-forking-paths
counting**: a claim "passes" only if the counting rule that produces the balance was
specified on a principled basis BEFORE the balance was observed, not reverse-engineered
to hit the target.

### Rules-tuple discipline (the heart of this audit)

Each claim is computed under THREE pre-committed counting rules:

- **R1 — strict-al-form**: the definite-article surface lexeme only (e.g. `الدنيا`,
  `الآخرة`), substring match on `quran-text/quran-no-tashkeel.json`. This is the
  narrowest defensible rule and the one closest to how the popular claims are *worded*
  ("al-dunyā", "al-ākhira").
- **R2 — all-morphological-forms (surface)**: all inflected surface forms of the target
  lexeme regardless of definiteness/clitics, by substring/regex on the no-tashkeel
  corpus, with explicit homonym exclusions documented per claim.
- **R3 — QAC-lemma**: the Quranic Arabic Corpus v0.4 lemma
  (`data/morphology/quranic-corpus-morphology-0.4.txt`), counting STEM tokens whose
  `LEM:` field equals the target lemma. This is the most linguistically principled rule:
  lemma membership is annotated by Dukes (2011), independent of this audit.

Default rules-tuple: `(no-tashkeel, orthographic/lemma-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`. Seed 20260509 (no randomness is
required for deterministic integer counts; the seed is logged for protocol uniformity).

### Verdict rule (pre-committed, per claim)

For each claim:
- **CONFIRMED** — the claimed balance/total holds EXACTLY under ≥1 of {R1, R2, R3}
  AND that rule is *principled* (it is the rule the lexeme's wording most naturally
  selects, or it is the linguistically-canonical QAC lemma, and it is not
  gerrymandered to exclude/include forms purely to hit the target).
- **RULES-FRAGILE** — the balance holds only under an *ad-hoc* rule: one that requires
  silently including some forms and excluding others (homonyms, figurative senses,
  selected derivatives) with no principled basis except hitting the claimed number;
  OR the balance holds under one rule but breaks under the equally-defensible
  neighbouring rules, and the literature does not specify which rule it uses.
- **FALSIFIED** — NO defensible rule (principled or ad-hoc) produces the claimed
  balance/total; the claim is simply numerically wrong on the canonical corpus.

A claim that lands EXACTLY on its target under the *most natural* reading of its own
wording is CONFIRMED even if neighbouring rules differ — but the rule must be named in
advance and the fragility disclosed.

**KEY DISCIPLINE**: for each claim I pre-state below which rule the popular literature's
wording implies, and whether that rule is principled or gerrymandered. The verdict is
read only after computing all three rules.

---

## The 10 claims (targets pre-committed from the FUNCI/Nawfal source)

| # | Claim | Claimed value(s) | Literature's implied rule | A-priori principled? |
|:-:|:--|:--|:--|:--|
| 1 | al-dunyā = al-ākhira | 115 = 115 | R1/R3 strict definite lexeme | principled if both = 115 |
| 2 | al-malāʾika = al-shayāṭīn | 88 = 88 | ambiguous (plural? or all forms?) | depends — flagged |
| 3 | al-ḥayāt = al-mawt | 145 = 145 | R2/R3 all forms of root | depends — flagged |
| 4 | al-shahr = 12; al-yawm sing = 365; ayyām/dual = 30 | 12 / 365 / 30 | R-mixed (sing vs pl vs dual split) | flagged — split-by-number |
| 5 | al-rajul = al-marʾa | 24 = 24 | R1/R3 singular lexeme | principled if both = 24 |
| 6 | Iblīs = istiʿādha (seek-refuge) | 11 = 11 | R3 PN-count vs verb-subset | flagged — verb subset |
| 7 | al-malak (sing) vs al-shayṭān (sing) | — (balance implied) | R-singular-only | principled if stated |
| 8 | al-ṣāliḥāt = al-sayyiʾāt | balance implied | R2/R3 plural noun | flagged |
| 9 | al-rasūl / rusul frequency | — (descriptive) | R3 lemma | principled (descriptive) |
| 10 | baḥr (sea) vs barr (land) = 32 : 13 → 71.1% water | 32 : 13 | R-geographic-sense only | CAUTION: barr-stem homonym |

### Per-claim pre-committed counting notes

- **Claim 1 (dunyā/ākhira)**: literature words it as the definite nouns. Principled
  rules are R1 (definite surface) and R3 (QAC lemma `d~unoyaA` vs `A^xir`). Pre-commit:
  CONFIRMED only if BOTH equal 115 under the SAME rule. If dunyā=115 but ākhira≠115 the
  pair is broken regardless of how close.
- **Claim 2 (malāʾika/shayāṭīn)**: the gloss "angels/devils" is plural. The honest
  question is whether the balance is between the PLURALS (malāʾika vs shayāṭīn) or
  between the whole LEMMAS (malak+malāʾika vs shayṭān+shayāṭīn). Pre-commit: report
  plural-only (R-plural) AND whole-lemma (R3). CONFIRMED only if the rule that balances
  is the one matching the *gloss* (plural). If the lemma-total balances but the plural
  does not, that is RULES-FRAGILE (the gloss "angels=devils" then conflates a
  mostly-plural word with a mostly-singular word).
- **Claim 3 (ḥayāt/mawt)**: "life/death." The QAC root Hyy has many lemmas (ḥayāt noun,
  ḥayy adjective, aḥyā verb, etc.); root mwt likewise. Pre-commit: report (a) the noun
  lemma `Hayaw`p` (ḥayāt) vs noun lemma `mawot` (mawt); (b) whole-root totals. CONFIRMED
  only if a principled rule lands BOTH on 145.
- **Claim 4 (calendar)**: three sub-targets. shahr-singular = 12; yawm-singular = 365;
  ayyām(plural)+yawmayn(dual) = 30. Each tested separately; the split between
  singular/plural/dual is itself the rule under test — flag if the split is principled
  or gerrymandered.
- **Claim 5 (rajul/marʾa)**: singular "man/woman." Pre-commit: R3 lemma `rajul` vs
  `{mora>at`. CONFIRMED only if both = 24 (the claimed value).
- **Claim 6 (Iblīs/refuge)**: Iblīs proper-noun count vs seek-refuge verbs. The inline
  H-NEW-2000 reported both = 11. Pre-commit: VERIFY Iblīs PN = 11 and identify the exact
  refuge-verb subset that = 11; flag whether that subset is principled (all istiʿādha
  verbs) or gerrymandered (a hand-picked subset).
- **Claim 7 (singular angel/devil)**: al-malak vs al-shayṭān, singular only. Descriptive
  test of whether the SINGULARS balance (they need not — this is the diagnostic for
  Claim 2).
- **Claim 8 (ṣāliḥāt/sayyiʾāt)**: good-deeds plural vs bad-deeds plural. R3 lemma
  `S~a`liHa`t` vs `say~i_#aAt`.
- **Claim 9 (rasūl)**: descriptive frequency of the messenger lemma(s); no balance
  target — reported for completeness, verdict NOT-A-BALANCE-CLAIM unless a specific
  symmetry is asserted.
- **Claim 10 (baḥr/barr)**: STRICT geographic sense only. baḥr lemma `baHor` (sea).
  barr: the homonym hazard is explicit — root brr contains `bar~` (land/dry-land),
  `bir~` (righteousness/piety), `tabar~u` (to be dutiful), and abrār (the righteous).
  Pre-commit: count ONLY `bar~` (geographic land), EXCLUDING bir̲r/abrār/tabarru.
  Also report the FUNCI variant "barr/arḍ" (land+earth) since the source combines them.
  CONFIRMED only if 32:13 (or the 71.1% ratio) holds under a principled sea/land rule.

---

## Failure conditions (pre-committed)

- If dunyā=115 but ākhira≠115 under every rule → Claim 1 FALSIFIED as a *pair* (even
  though dunyā alone is exactly 115).
- If malāʾika-plural ≠ shayāṭīn-plural but malak-lemma = shayṭān-lemma → Claim 2
  RULES-FRAGILE (balance is an artifact of conflating singular+plural for both words).
- If baḥr=32 requires counting non-geographic barr senses, or if strict baḥr≠32 →
  Claim 10 FALSIFIED or RULES-FRAGILE per which rule is needed.
- Any claim whose target is recovered only by a gerrymandered include/exclude list →
  RULES-FRAGILE, never CONFIRMED.

## Expected diagnostic (stated, not assumed)

Per the al-Khalifa precedent and H-META-1, the prior is that **most word-balance claims
will FALSIFY or land RULES-FRAGILE**, with a small number of EXACT hits on
single-lexeme totals (e.g. dunyā=115) that are genuine corpus facts but do NOT extend to
the claimed *pair* balance. This prior is logged so a surprising all-confirm result
would be a genuine update. Equal prominence to CONFIRMED and FALSIFIED outcomes.

## Outputs

- script: `findings/phase-b-hypotheses/scripts/h-new-2000.py` (embeds this file's SHA256;
  fail-fast on mismatch)
- JSON: `findings/phase-b-hypotheses/csv/h-new-2000.json`
- finding: `findings/phase-b-hypotheses/h-new-2000-numerical-symmetry-audit.md`
- ledger: MASTER-FINDINGS-LEDGER entry

*Bismillāhi al-Raḥmāni al-Raḥīm.*
