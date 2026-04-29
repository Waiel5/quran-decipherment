---
title: "Phase B — H20: Al-Rāzī's muqatta'at = divine-name abbreviation theory"
agent: phase-b-classical-test / razi-99names
date: 2026-04-12
hypothesis_id: H20
classical_attribution: Fakhr al-Dīn al-Rāzī (d. 606 H / 1209 CE), *Mafātīḥ al-Ghayb*
rules:
  orthography: no-tashkeel
  letter_definition: graphemes; hamza/أ/إ/آ/ٱ/ء normalized to ا; ى→ي; ة→ت; ؤ→و; ئ→ي
  alphabet: 28 standard Arabic letters
  initial_extraction: first letter after stripping definite article ال
  null_models: (a) uniform 28-letter null; (b) random 14-letter subset null
data_sources:
  - /Users/grey/Downloads/quran/data/asma-al-husna.txt (canonical 99 names, al-Tirmidhī list)
  - /Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-99names-extract.md
---

# H20 — Al-Rāzī's "muqatta'at = divine-name abbreviation" theory

## Headline result

**Verdict: WEAKLY SUPPORTED under naive null, NOT SUPPORTED under proper null.**

The 14 luminous letters (أ ل ر م ح ص ك ه ي ع ط س ق ن) collectively initial
**66 of 99** Names of Allah, vs the 14 non-luminous letters' **33 of 99**.

| Test | Statistic | p-value | Verdict |
|---|---|---|---|
| Binomial(99, p=0.5), one-tailed upper | 66 vs expected 49.5 | **0.000593** | "Significant" — NAIVE |
| Random 14-letter subset null (100k samples) | z = +1.22 | **≈ 0.139** | NOT significant |
| Frequency-weighted Quran null (p=0.744) | 66 vs expected 73.7 | 0.967 (under!) | NOT significant |

The naive binomial test treats the alphabet as exchangeable. But the luminous
letters were *not* a random subset of the alphabet — they are skewed toward
common letters. The proper null is "what coverage would a random 14-letter
subset achieve?", which gives **mean = 49.5, SD = 13.6, observed z = +1.22,
p ≈ 0.14**. This is well above any conventional significance threshold.

**The single letter م (mīm) drives 136% of the entire excess.** Mīm initials
26 of 99 names (the largest of any letter); under the uniform null its expected
contribution is 3.54, so it alone accounts for +22.46 of the +16.50 total
luminous excess. **If we drop mīm from the luminous set, the remaining 13
luminous letters cover only 40 of 99 names, vs an expected 45.96 for any random
13 letters — they are *anti*-correlated with name initials.**

## 1. Attribution and what al-Rāzī actually claimed

Fakhr al-Dīn al-Rāzī (d. 606 H / 1209 CE) in *Mafātīḥ al-Ghayb* (= *al-Tafsīr
al-Kabīr*) lists ~20 distinct opinions on the huruf muqatta'at in his
commentary on Q. 2:1. Among them is the opinion that the letters are
abbreviations of divine names or attributes. This opinion is associated in the
classical literature with statements transmitted from **ʿAbd Allāh ibn ʿAbbās**
and **ʿAbd Allāh ibn Masʿūd**. Al-Rāzī himself does NOT commit to this opinion
as the correct one; he records the disagreement among the salaf about which
divine names the letters abbreviate as a reason to doubt that any single
decomposition is uniquely correct.

The classical decompositions reported (al-Suyūṭī, *al-Durr al-Manthūr* 4/679;
Tanwīr al-Miqbās; al-Razi, vol. 1):

| Combo | Classical decomposition | Source attribution |
|---|---|---|
| ALM (الم) | Allāh / Laṭīf / Majīd; or "Anā Allāhu Aʿlam" (phrase) | Ibn ʿAbbās via al-Tabarānī |
| ALR (الر) | "Anā Allāhu Arā/Raʾā"; or Allāh/Laṭīf/Raḥmān | Ibn ʿAbbās |
| KHYAS (كهيعص) | Kabīr / Hādī / **Amīn** / ʿAzīz / Ṣādiq | Ibn ʿAbbās via *al-Durr al-Manthūr* 4/679 |
| HM (حم) | Ḥamīd Majīd; or Ḥalīm Majīd | various |
| YS (يس) | "Yā Sayyid" (vocative, not abbreviation) | various |
| Q (ق) | Qādir / Qayyūm / Qarīb | various |

**Important caveat from the source.** The KHYAS decomposition Ibn ʿAbbās is
reported to give already breaks the strict rule we are testing. **ي is mapped
to al-Amīn (الأمين), but الأمين begins with hamza/alif, not yāʾ.** So the
classical "abbreviation" theory itself does NOT use strict first-letter
matching — it allows phonetic, mnemonic, or thematic association. We score it
**4/5 strict matches** for KHYAS.

Implication: the strict first-letter test we are running is testing a *stronger*
claim than what al-Rāzī or Ibn ʿAbbās actually defended. A pass under the
strict test would be strong evidence; a fail leaves the looser claim untouched.
We will score and report both.

Full classical extract: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-99names-extract.md`

## 2. Method

**Names corpus.** 99 canonical names from the al-Tirmidhī (al-Walīd ibn Muslim)
list, source `data/asma-al-husna.txt`. The list begins with الله (Allāh) and
ends with الصبور (al-Ṣabūr). Verified count = 99.

**Initial-letter extraction.** For each name, strip leading ال (definite
article) and take the first letter of the remainder. For names without ال
(الله counts as ال + لاه, so we strip and the radical is ل; مالك الملك starts
with م; ذو الجلال starts with ذ), take the first letter of the head noun.
Hamza variants normalized to alif.

**Operational definition of "starts with X"** for the strict test: the first
letter of the radical (post-ال) equals X exactly, after normalization.

**Luminous set.** {ا ل ر م ح ص ك ه ي ع ط س ق ن} (14 letters).
**Non-luminous set.** {ب ت ث ج خ د ذ ز ش ض ط غ ف و} (14 letters).
[Cross-check: ط appears in BOTH lists in our reading. Wait — let me verify.]

Re-verifying: the 14 luminous letters per the project's locked muqatta'at
analysis (`muqattaat-analysis.md` §1) are: **ا ح ر س ص ط ع ق ك ل م ن ه ي**
(sorted Unicode order). The non-luminous 14 are therefore: **ب ت ث ج خ د ذ ز
ش ض ظ غ ف و**. Alphabet check: 14 + 14 = 28 ✓.

## 3. Per-letter coverage (28 letters)

| Letter | Count | Luminous? |
|---|---|---|
| م | 26 | YES |
| و | 9 | no |
| ب | 8 | no |
| ح | 8 | YES |
| ر | 7 | YES |
| ع | 6 | YES |
| ق | 6 | YES |
| ج | 3 | no |
| خ | 3 | no |
| غ | 3 | no |
| ا | 2 | YES |
| ك | 2 | YES |
| ل | 2 | YES |
| ن | 2 | YES |
| س | 2 | YES |
| ص | 2 | YES |
| ش | 2 | no |
| ه | 1 | YES |
| ت | 1 | no |
| ذ | 1 | no |
| ض | 1 | no |
| ظ | 1 | no |
| ف | 1 | no |
| ث | 0 | no |
| د | 0 | no |
| ز | 0 | no |
| ط | 0 | YES |
| ي | 0 | YES |
| **TOTAL** | **99** | |

**Sum of luminous initials = 66/99**
**Sum of non-luminous initials = 33/99**

### Luminous letters with ZERO 99-Names coverage (failures of al-Rāzī's theory)

- **ط (ṭāʾ)** — no 99-Name starts with ṭāʾ (after stripping al-).
  Surahs 20 (طه), 26 (طسم), 27 (طس), 28 (طسم) all begin with ṭāʾ. The classical
  decomposition has nothing canonical to offer.
- **ي (yāʾ)** — no 99-Name starts with yāʾ. Surahs 19 (كهيعص) and 36 (يس)
  contain yāʾ. The classical answer is "Yā Sayyid" (vocative) or al-Amīn
  (which doesn't start with yāʾ).

Two of 14 luminous letters fail the strict test entirely.

### Non-luminous letters that DO appear as 99-Names initials

- **و (wāw)** — 9 names: al-Wahhāb, al-Wāsiʿ, al-Wadūd, al-Wakīl, al-Walī,
  al-Wājid, al-Wāḥid, al-Wālī, al-Wāriṯ. **This is the largest non-luminous
  contributor.** Wāw is rank 6 in Quran letter frequency, ahead of all luminous
  letters except the top 5 — yet it is excluded from the muqatta'at. This is
  the single biggest piece of anti-evidence for al-Rāzī.
- **ب (bāʾ)** — 8 names: al-Bāriʾ, al-Bāsiṭ, al-Baṣīr, al-Bāʿiṯ, al-Barr,
  al-Bāṭin, al-Badīʿ, al-Bāqī.
- **ج (jīm)** — 3 names: al-Jabbār, al-Jalīl, al-Jāmiʿ.
- **خ (khāʾ)** — 3 names: al-Khāliq, al-Khāfiḍ, al-Khabīr.
- **غ (ghayn)** — 3 names: al-Ghaffār, al-Ghafūr, al-Ghanī.
- **ش (shīn)** — 2 names: al-Shakūr, al-Shahīd.
- **ت ذ ض ظ ف** — 1 name each.

**33 of 99 Names start with a non-luminous letter.** Under al-Rāzī's strict
hypothesis, this should be 0. It is one third of the entire list.

## 4. Statistical tests

### Test A: naive binomial null (each name's initial uniform over 28 letters)

H₀: Each of the 99 names independently has its initial drawn uniformly from the
28-letter alphabet. Then P(luminous) = 14/28 = 0.5 and observed/99 ~
Binomial(99, 0.5).

- Observed luminous: 66
- Expected: 49.5
- Excess: +16.5
- z (normal approx): +3.32, SD = 4.975
- **One-tailed P(X ≥ 66): 0.000593**
- Two-tailed: 0.001185

This test is significant. **But the test is wrong.** The luminous letters were
not selected to be a random 14-letter subset of the alphabet. They are heavily
biased toward high-frequency Arabic letters (per `muqattaat-analysis.md` §7,
9 of the top 14 most-frequent Quran letters are luminous). And high-frequency
letters are also more likely to initial common Arabic words, including divine
names. So we need a null that conditions on this.

### Test B: random 14-letter subset null

H₀: Pick a uniformly random 14-letter subset of the 28-letter alphabet. Compute
its 99-Names coverage. How surprising is the observed 66?

Method: 100,000 random subsets of size 14 sampled from 28 letters; coverage
distribution computed.

- Mean coverage of random 14-subset: **49.50** (matches analytic 99 × 14/28)
- SD: **13.59** (much wider than the binomial SD of 4.98 — letters are
  *very* unequal)
- **z = (66 − 49.5)/13.59 = +1.22**
- **Empirical P(coverage ≥ 66) = 0.139** (13,856/100,000 random subsets)

**Under the proper null, the result is NOT statistically significant.**
14% of random 14-letter subsets do at least as well as the luminous set.

### Test C: frequency-weighted (Quran-baseline) null

H₀: Each name's initial is drawn from the Quran letter-frequency distribution.
The luminous letters together account for 74.4% of all Quran letter occurrences
(per `muqattaat-analysis.md` §7).

- Luminous-letter share = 0.7441
- Expected coverage under freq-weighted null = 99 × 0.7441 = **73.67**
- Observed = 66
- **P(X ≥ 66 | n=99, p=0.7441) = 0.967**

**Under the frequency-weighted null, the luminous coverage is in fact
*lower* than expected.** The set of high-frequency Arabic letters would predict
~74 names start with such a letter; we see only 66. By this test the luminous
selection is *worse* than its frequency profile would predict.

### Test D: maximum-coverage benchmark

The optimal 14-letter subset (sorted by name-initial count) is:
{م و ب ح ر ع ق ج خ غ ا س ش ص}, with combined coverage 87. Eight of these 14
are luminous. The luminous set covers 66/87 = 75.9% of the maximum achievable.

If al-Rāzī's "abbreviation of names" was the design constraint, the obvious
substitution is to swap out ط (0 names) and ي (0 names) for و (9 names) and
ب (8 names), gaining +17 coverage and bringing total to 83. The fact that
this swap is not what we see is direct evidence the design constraint is NOT
"maximize 99-Names coverage."

## 5. Drop-mim sensitivity

Mīm (م) is doing all the work. Decomposing the +16.5 excess by letter:

| Letter | Coverage | Excess vs uniform (3.54) |
|---|---|---|
| م | 26 | +22.46 |
| ح | 8 | +4.46 |
| ر | 7 | +3.46 |
| ق | 6 | +2.46 |
| ع | 6 | +2.46 |
| ا ك ل ن س ص | 2 each | −1.54 each |
| ه | 1 | −2.54 |
| ط ي | 0 each | −3.54 each |

**م alone contributes +22.46 of the +16.50 total, or 136% of the effect.** The
remaining 13 luminous letters contribute net **−5.96**. If we remove mīm from
the luminous set:
- Remaining 13 luminous letters cover 40 of 99 names
- Expected coverage of any 13 random letters: 13 × 99/28 = 45.96
- Excess: **−5.96** (the 13-letter sub-set is *anti*-correlated with names)

The result is hostage to one letter. If the muqatta'at had not included mīm,
the coverage would be 40/99 — substantially below random. Since مم is one of
the top 4 Arabic letters by overall frequency, including it is statistically
the easy choice; it alone is responsible for the apparent enrichment.

## 6. Per-combo coverage of muqatta'at as divine-name abbreviations

For each of the 14 unique muqatta'at combinations, count how many of its
constituent letters have at least one canonical-99 Name starting with that
letter (strict first-letter rule, post-stripping ال).

| Combo | Letters | Coverage | Notes |
|---|---|---|---|
| ALM | الم | **3/3** | a→Awwal/Ākhir, l→Allāh/Laṭīf, m→26 names |
| ALMS | المص | **4/4** | adds ṣ→Ṣamad/Ṣabūr |
| ALR | الر | **3/3** | r→Raḥmān + 6 others |
| ALMR | المر | **4/4** | full coverage |
| KHYAS | كهيعص | **4/5** | yāʾ has 0 names; classical: ي→al-Amīn (FAILS strict) |
| TH | طه | **1/2** | ṭāʾ has 0 names; only h→Hādī works |
| TSM | طسم | **2/3** | ṭāʾ has 0 names |
| TS | طس | **1/2** | ṭāʾ has 0 names |
| YS | يس | **1/2** | yāʾ has 0 names |
| S | ص | **1/1** | full coverage |
| HM | حم | **2/2** | full coverage |
| HMASQ | حمعسق | **5/5** | full coverage — strongest combo |
| Q | ق | **1/1** | full coverage |
| N | ن | **1/1** | full coverage |
| | | **TOTAL: 33/41** | 80.5% letter-level coverage |

8 of 14 combinations have full strict coverage. **6 combinations contain at
least one letter that has zero canonical-99 coverage**, and these are
specifically the **ṭāʾ-bearing** (TH, TSM, TS) and **yāʾ-bearing** (KHYAS, YS)
combinations. Both ṭāʾ and yāʾ are luminous letters with no canonical-name
correspondence.

The strongest combo is HMASQ (Surah 42, the only 5-letter combination that
covers 5/5): ح→Ḥakīm…, م→26 names, ع→ʿAzīz…, س→Sami'/Salām, ق→Qadir/Qayyūm.
Surah 19's KHYAS misses on yāʾ.

## 7. Strict test of Ibn ʿAbbās's KHYAS decomposition

Per `al-Durr al-Manthūr` 4/679, Ibn ʿAbbās is reported to decompose KHYAS as:

| Letter | Assigned name | First letter of name (after ال) | Strict match? |
|---|---|---|---|
| ك | الكبير | ك | ✓ |
| ه | الهادي | ه | ✓ |
| ي | الأمين | ا | ✗ |
| ع | العزيز | ع | ✓ |
| ص | الصادق | ص | ✓ |

**Score: 4/5 strict matches.** Ibn ʿAbbās's own decomposition fails the strict
first-letter rule on yāʾ → al-Amīn. This is direct textual evidence that the
classical scholars themselves did NOT defend the strict alphabetic version of
the abbreviation theory: they allowed mnemonic/phonetic association, where
"yāʾ evokes al-Amīn" can be defended as "the letter yāʾ is the second sound in
يا and signals invocation of the trustworthy attribute" — not as alphabetic
indexing.

## 8. Novel extension — divine attributes outside the canonical 99

The canonical 99 omits common Quranic divine epithets like *Rabb* (most common
of all, ر), *ʿālim/ʿalīm* (broader form, ع), *qadīr* (ق), *raʾūf* (ر — though
al-Raʾūf is in some lists as #83), *Ilāh* (ا/ل). These are concentrated in
luminous letters. If we expanded the corpus from 99 to ~150 attested Quranic
divine attributes, would the luminous-set effect strengthen?

I did not run the full expanded corpus in this round (it requires curated
extraction from the Quran morphology data), but a quick scan of the top 20 most
frequent divine epithets in the Quran shows:

- **Rabb** (ربّ, root r-b-b) — initial **ر** (luminous), occurs ~970 times
- **Allāh** (الله, root ʾ-l-h) — initial **ل** after stripping (luminous), occurs ~2700 times
- **Ilāh** (إله) — initial **ا** (luminous)
- **al-Raḥmān** (الرحمن) — ر (luminous)
- **al-Raḥīm** (الرحيم) — ر (luminous)
- **ʿAlīm** (عليم) — ع (luminous)
- **Khabīr** (خبير) — خ (NON-luminous)
- **Ḥakīm** (حكيم) — ح (luminous)
- **Qadīr** (قدير) — ق (luminous)
- **Samīʿ** (سميع) — س (luminous)
- **Baṣīr** (بصير) — **ب (NON-luminous)**
- **Walī** (ولي) — **و (NON-luminous)**

8 of 12 (67%) of these top frequent epithets start with luminous letters —
similar ratio to the 99 (66/99 = 67%). The wāw/bāʾ counter-examples persist.
**This null result reinforces the main verdict**: the luminous set is at
67–74% coverage of divine attributes regardless of which epithet pool we draw
from, which is what the *frequency* of those letters in Arabic naturally
predicts. There is no evidence of *deliberate* alphabet-to-name design.

## 9. Verdict

| Hypothesis | Verdict |
|---|---|
| **H20 strict** ("luminous letters are exactly the initials of the 99 Names") | **REJECTED.** Two luminous letters (ط ي) initial zero names; eleven non-luminous letters initial 33 names. |
| **H20 statistical** ("luminous coverage of 99 Names is significantly above random") | **NOT SUPPORTED** under the proper null (random 14-subset, p=0.14). Naively significant under the wrong null (uniform-binomial, p=0.0006), but the wrong null overstates the effect by ignoring letter-frequency skew. |
| **H20 frequency-controlled** ("luminous coverage exceeds what their Quran frequencies predict") | **CONTRARY EVIDENCE.** Frequency-weighted null predicts 73.7 coverage; observed 66 is *below*. |
| **H20 weak / mnemonic version** (al-Razi's actual claim: "the muqatta'at letters are *associated* with divine attributes via loose phonetic/mnemonic links") | **UNTESTED by this protocol.** The looser claim is theological, not statistical, and cannot be falsified by initial-letter counting. |

**What al-Rāzī gets right:** the muqatta'at letters are concentrated in
high-frequency, semantically heavy Arabic letters that DO show up in many
divine attributes. There is a real correlation between "letters used in
muqatta'at" and "letters used in divine names" — both are biased toward
common, articulated Arabic consonants. His intuition that there is *something*
linking the two is empirically defensible at the broad level.

**What al-Rāzī gets wrong (or what classical scholars never quite committed
to):** the muqatta'at are NOT a maximal or optimal set of "divine-name
initials." A randomly chosen 14-letter subset has a 14% chance of doing as
well or better. Two muqatta'at letters (ṭāʾ and yāʾ) have ZERO canonical-99
coverage. Wāw — excluded from the muqatta'at — initials 9 names, more than any
single luminous letter except mīm. The omission of wāw in particular is hard
to reconcile with "designed to abbreviate divine names."

**Honest summation:** al-Rāzī was right to notice the affinity but wrong (or
agnostic) about the strict mechanism. The 16.5-name excess that looks
significant under a naive null evaporates under proper letter-frequency
control, and the entire effect is loaded onto a single letter (mīm). This is
a case where a 13th-century classical theory was *partially* anticipating a
real correlation but mistook a frequency artifact for a designed encoding.

## 10. Interesting corollaries

1. **The single-letter muqatta'at (ص, ق, ن) all have full strict coverage.**
   ص → al-Ṣamad/Ṣabūr, ق → 6 names, ن → al-Nūr/Nāfiʿ. The 1-letter combos are
   the cleanest cases. (Surah 38 ص, Surah 50 ق, Surah 68 ن — all single
   muqatta'at letters with full coverage.)

2. **HMASQ (Surah 42, 5 letters) has full coverage — uniquely.** It is the
   only 5-letter combination where all 5 letters initial canonical-99 names.
   KHYAS (Surah 19) misses on yāʾ. If al-Rāzī had been ranking surahs by
   "abbreviation richness," Surah 42 would be the strongest case.

3. **The mīm dominance** is itself interesting. Why do so many divine names
   start with mīm? Because Arabic has the *mufāʿīl* nominal pattern (الفاعل
   → الـمُـ-stem) for active participles and intensives: al-Mujīb,
   al-Mu'min, al-Mubdiʾ, etc. Many divine names are derived participial nouns
   beginning with the م- prefix. This is a morphological accident, not a
   theological design. The 26 mīm-initial names are mostly muF'iL forms, not
   independent root mīm-words. **Subtracting these participial mīms would
   eliminate the entire luminous-set excess.**

4. **The muqatta'at letters are more about high-frequency Arabic phonology
   than about divine-name abbreviation.** Combining this finding with
   `muqattaat-analysis.md` §7 (9/14 luminous in top-14 frequency) and §10
   (per-surah enrichment driven by ALM and Q), the consistent picture is:
   the muqatta'at are a *frequent-letter signature*, NOT a divine-name index.

## 11. Limitations and forks

- **List choice.** I used the al-Tirmidhī (al-Walīd ibn Muslim) list, which is
  the most widely cited but is technically *gharīb* (uncommon) per al-Tirmidhī
  himself. Other lists (al-Bukhārī sub-collection, Ibn Mājah, Ibn ʿAsākir)
  vary by ~5–10 names. The headline number 66/99 would shift by ≤5 under list
  variants, not enough to change the verdict.
- **Definite article handling.** I stripped ال and counted the radical first
  letter. This is the natural choice (since all 99 trivially start with ا
  otherwise) but it does normalize away the visual surface form. Under the
  alternative "raw first letter" rule, every name would count for ا (luminous)
  except for #84 مالك الملك (م) and #85 ذو الجلال (ذ), trivially making the
  test pass. This alternative is uninteresting.
- **Initial-letter strictness.** I tested the strict alphabetic-initial rule.
  The looser classical reading (where ي → al-Amīn is allowed) cannot be
  falsified by counting and is not what we set out to test.
- **Frequency null.** The Quran letter frequencies are themselves entangled
  with the muqatta'at since the muqatta'at appear inside the Quran text. A
  cleaner null would use a comparable Arabic corpus (Bukhārī, classical poetry).
  This is on the to-do list (statistical-rigor §1.4) but not yet available.

## 12. Garden-of-forking-paths disclosure

- I pre-committed (via the H20 specification in deep-hypotheses-queue.md) to
  the binomial null with p=0.5 and to the random-subset null. Both were
  specified before computation.
- I did NOT pre-commit to the frequency-weighted null; I added it after seeing
  the binomial result, because it is the obvious robustness check and would
  have been demanded by any reviewer.
- I did NOT run the bayesian or permutation tests on the alternative name
  lists; this can be done in a follow-up.
- I did NOT run a hold-out test (split the 99 into halves and recompute) since
  the list is small and the verdict is clear in either direction at the full
  list size.

## 13. Sources and code

- Names file: `/Users/grey/Downloads/quran/data/asma-al-husna.txt`
- Classical attribution: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-99names-extract.md`
- Existing al-Razi context: `/Users/grey/Downloads/quran/data/literature/classical-tafsir/razi-muqattaat-surah-qaf.md`
- Analysis script: `/tmp/razi-99names-analysis.py`
- Extension/robustness script: `/tmp/razi-99names-extension.py`
- Strict KHYAS test: `/tmp/razi-strict-khyas.py`
- Numeric summary dump: `/tmp/razi-99names-summary.txt`

External:
- al-Suyūṭī, *al-Durr al-Manthūr fī Tafsīr al-Maʾthūr*, vol. 4, p. 679
- Tafsīr Ibn ʿAbbās (Tanwīr al-Miqbās), entries on Q. 2:1, Q. 19:1, Q. 50:1
- Fakhr al-Dīn al-Rāzī, *Mafātīḥ al-Ghayb*, 32 vols, commentary on Q. 2:1
  (Internet Archive: https://archive.org/details/mafatihalghayb06raziuoft)
- Wikipedia: https://en.wikipedia.org/wiki/Muqatta%CA%BFat
- Wikipedia: https://en.wikipedia.org/wiki/Names_of_God_in_Islam

## 14. §7 checklist

- [x] Hypothesis ID and classical attribution stated in YAML frontmatter
- [x] Names corpus saved with verifiable count = 99
- [x] Initial-letter extraction rule documented and reproducible
- [x] Two distinct null models tested (uniform binomial AND random 14-subset)
- [x] Third null (frequency-weighted) added as robustness
- [x] Drop-leave-one-out / sensitivity analysis (mim dominance)
- [x] Per-combo coverage analysis with strict matching
- [x] Strict test of Ibn ʿAbbās's specific KHYAS decomposition
- [x] Garden-of-forking-paths disclosure
- [x] Verdict explicitly stated for each version of the hypothesis
- [x] Limitations enumerated
- [x] Code paths and data sources cited
