---
id: H-NEW-1530
title: al-Khalifa "miracle of 19" — 5-sub-claim rigorous audit
date: 2026-05-09
phase: B
status: COMPLETE
verdict_tally: {CONFIRMED: 3, FALSIFIED: 2, DEFINITION-DEPENDENT: 0}
composite: SPLIT
prereg_sha: 461ac84c5e1bfd14e5178a72f17fa11e7e25131c8f39f77bdf62de705edb1269
---

# H-NEW-1530 — al-Khalifa "miracle of 19" rigorous 5-sub-claim audit

## Headline

Five specific integer-equality claims from Rashad al-Khalifa's *Quran: The Final Testament* Appendix 1 ("One of the Great Miracles", written 1989, posthumous 1990) were tested directly against the canonical Hafs-Kūfan on-disk corpus.

**Verdict tally: 3 CONFIRMED, 2 FALSIFIED, 0 DEFINITION-DEPENDENT.**

Composite: **SPLIT.** Three of the five most-cited al-Khalifa "Code 19" sub-claims do empirically verify (basmala = 19 letters; al-Fātiḥa = 29 words; corpus = 114 surahs = 19 × 6). Two flagship claims (first-revelation Q 96:1-5 = 19 words; total *Allāh* occurrences = 2698 = 19 × 142) **do not verify against the canonical corpus** under any of five pre-registered counting conventions. The two confirmations that *are* substantive (C2, C4) are independently true facts about the text that long predate al-Khalifa and do not on their own constitute evidence of a 19-divisibility code; one (C3) is arithmetic.

## Source claim catalogue

All claims pulled verbatim from `data/literature/khalifa/1989-khalifa-appendix-1-one-of-the-great-miracles.md` (Khalifa 1989, *Quran: The Final Testament*, Appendix 1) and cross-listed `claims-catalog` IDs prefixed `khalifa-*`. Primary source PDF: `data/literature/khalifa/1989-khalifa-quran-the-final-testament.pdf` and `data/literature/khalifa/1982-khalifa-quran-visual-presentation-of-the-miracle.pdf`.

## Pre-registration

- File: `findings/phase-b-hypotheses/prereg-h-new-1530-khalifa-19-audit.md`
- SHA-256: `461ac84c5e1bfd14e5178a72f17fa11e7e25131c8f39f77bdf62de705edb1269`
- Locked: 2026-05-09 (before any computation)
- Run script verifies the SHA at runtime; mismatch terminates with exit 2.
- Seed: 20260509 (no permutation needed; each test is integer-equality).

## Methodology

Rules-tuple per protocol §1.4 default:
- **Corpus**: `quran-text/quran-no-tashkeel.json` (primary, Hafs-Kūfan).
- **Tashkeel**: no-tashkeel for primary; full-tashkeel and `data/alt-text/quran-uthmani-consonantal.json` as orthographic-robustness probes (C4 only).
- **Token**: whitespace-split for word counts; Unicode code-point for grapheme counts; combining marks (Mn category) excluded for base-letter counts.
- **Reading**: Hafs-Kūfan (on-disk JSON is Hafs).
- **Basmala**: counted only in Q 1 (matches the 6236 standard-verse convention; the JSON encodes basmala as Q 1:1 only; the embedded *bismillāhi* in Q 27:30 is part of v30, not a standalone v1).
- **Allāh-form recognition**: closed pre-committed list of nested tallies A-E.

## Sub-claim results

### C1 — First revealed verses Q 96:1-5 contain 19 words — **FALSIFIED**

Claim source: appendix-1 / claim ID `khalifa-first-revelation-19-words-76-letters`.

**Computation**: word-counts of Q 96:1, 96:2, 96:3, 96:4, 96:5 in `quran-no-tashkeel.json`:

| Verse | Text (no-tashkeel) | Words |
|:--|:--|--:|
| 96:1 | اقرأ باسم ربك الذي خلق | 5 |
| 96:2 | خلق الإنسان من علق | 4 |
| 96:3 | اقرأ وربك الأكرم | 3 |
| 96:4 | الذي علم بالقلم | 3 |
| 96:5 | علم الإنسان ما لم يعلم | 5 |
| **Σ** | | **20** |

**Observed: 20 words. Expected: 19. Verdict: FALSIFIED.**

The companion half of this claim ("76 letters") also fails: counting graphemes (no-tashkeel, no spaces) across Q 96:1-5 yields **78 letters**, not 76. (76 = 19 × 4; 78 mod 19 = 2.) Neither half of `khalifa-first-revelation-19-words-76-letters` survives direct verification on the canonical Hafs corpus.

**Notes on robustness.** Could the claim be rescued by a different verse-segmentation? Some early-classical sources hold the first revelation to be Q 96:1-5; others hold it to be Q 96:1-3 (Ibn Isḥāq via Ibn Hishām). Q 96:1-3 sums to 5+4+3 = 12 words, also not 19. Q 96:1-4 = 15; Q 96:1-6 = 22. **No initial-verse boundary in Q 96 yields exactly 19 words.** The 76-letter companion claim is similarly unrecoverable across boundary choices.

### C2 — Sūrah al-Fātiḥa contains 29 words — **CONFIRMED**

Claim source: appendix-1 / word-count table.

**Computation**: word-counts of Q 1:1-7 in `quran-no-tashkeel.json`:

| Verse | Text | Words |
|:--|:--|--:|
| 1:1 | بسم الله الرحمن الرحيم | 4 |
| 1:2 | الحمد لله رب العالمين | 4 |
| 1:3 | الرحمن الرحيم | 2 |
| 1:4 | مالك يوم الدين | 3 |
| 1:5 | إياك نعبد وإياك نستعين | 4 |
| 1:6 | اهدنا الصراط المستقيم | 3 |
| 1:7 | صراط الذين أنعمت عليهم غير المغضوب عليهم ولا الضالين | 9 |
| **Σ** | | **29** |

**Observed: 29 words. Expected: 29. Verdict: CONFIRMED.**

This is a **definite empirical confirmation**, but with three substantive caveats:
1. 29 is **not** divisible by 19; the al-Khalifa text proposes a 19 + 10 split (the basmala plus a "19 verb-cluster" — itself definition-dependent), so the 29 confirmation is not direct 19-divisibility evidence.
2. Classical word-counts of al-Fātiḥa vary between 25, 27, 29, and 30 depending on whether contracted forms (لله, إياك, وإياك) are split. The whitespace-tokenisation of the no-tashkeel JSON happens to land on 29.
3. The 29 figure is a pre-existing fact of the canonical text known to medieval scholars (e.g., al-Suyūṭī *al-Itqān* nawʿ 19 *fī ʿadad āyāt al-Qurʾān wa-kalimātihi*). al-Khalifa did not discover it; he restated it.

### C3 — Corpus contains 114 surahs = 19 × 6 — **CONFIRMED**

**Computation**: `len(json) = 114`. `114 mod 19 = 0`. `114 / 19 = 6`. **CONFIRMED.**

Trivial sanity control. This is a fact of the canonical mushaf compilation under ʿUthmān (c. 650 CE), fixed by communal consensus 1300+ years before al-Khalifa. Any number is divisible by *some* integer; 114 = 2 × 3 × 19 is also divisible by 2, 3, 6, 19, 38, 57, 114. The single divisor "19" is privileged by post-hoc selection given that 114 has several non-trivial divisors. **A confirmation here is uninformative on its own** — included only as a transparency control on the audit pipeline.

### C4 — Basmala = 19 letters — **CONFIRMED**

Claim source: appendix-1 / claim ID `khalifa-bismillah-19-letters`.

**Computation**: text Q 1:1 = `"بسم الله الرحمن الرحيم"`. Remove spaces. Count Unicode code-points (each Arabic letter is one BMP code-point; no-tashkeel form contains no combining marks).

```
ب س م ا ل ل ه ا ل ر ح م ن ا ل ر ح ي م
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19
```

**Observed: 19 letters. Expected: 19. Verdict: CONFIRMED.**

**Orthographic robustness probes** (all consistent):
- no-tashkeel form: **19** (primary).
- full-tashkeel base-letter count (excluding Mn category combining marks): **19**.
- full-tashkeel form `بِسۡمِ ٱللَّهِ ٱلرَّحۡمَٰنِ ٱلرَّحِيمِ` total code-points with marks: 35. (Includes shadda, kasra, ḥaraka, dagger-alef, etc. — not "letters" by the standard rasm definition.)
- uthmani-consonantal (`data/alt-text/quran-uthmani-consonantal.json`): **19**.

The 19-letter count of the basmala is **a true fact of the Arabic rasm** at the level of letter-shapes. This is well-known to medieval Arabic grammarians and pre-Khalifa Sufi letter-mystics; al-Suyūṭī *al-Itqān* nawʿ 17 (*fī ʿadad ḥurūf al-Qurʾān*) discusses basmala letter counts, and ʿilm al-ḥarf treatises (e.g., al-Būnī *Shams al-maʿārif*, 13th c.) include the 19-letter basmala in their letter-symbolism, attached to the abjad value or to the Allāh-Nūr cosmology. al-Khalifa did not discover this; he made it the entry-point to his Code-19 architecture.

**Caveat.** That the basmala happens to have 19 letters is a *single* numerological coincidence. Many other Quranic phrases have other letter-counts (e.g., *qul huwa-llāhu aḥad* = 11, *al-ḥamdu lillāhi rabbi al-ʿālamīn* = 17). Selection of which 19-divisible phrase to highlight is post-hoc.

### C5 — Total *Allāh* occurrences = 2698 = 19 × 142 — **FALSIFIED**

Claim source: appendix-1 ("The word 'God' appears 2,698 times (19×142)").

**Computation**: Five nested tallies of *Allāh*-reference word-forms, pre-committed in the registration:

| Tally | Definition | Count | mod 19 | Match? |
|:--|:--|--:|--:|:--|
| A | exact word `الله` only | **2153** | 6 | ✗ |
| B | A + classical prefixed (`والله, فالله, بالله, تالله`) + vocative `اللهم` | **2551** | 5 | ✗ |
| C | B + li-llah forms (`لله, ولله, فلله`) | **2700** | 2 | ✗ |
| D | C + interrogative/compound prefixed (`آلله, أبالله, وتالله`) | **2704** | 6 | ✗ |
| E | D minus vocative `اللهم` | **2699** | 1 | ✗ |

**No tally equals 2698.** No tally is even divisible by 19. The closest tally to 2698 is E = 2699 (off by 1, mod 19 = 1). The closest 19-multiples are 2698 (= 19 × 142) and 2717 (= 19 × 143), which bracket E = 2699 but neither is observed.

**Per-form raw counts in the corpus** (verified by cross-tabulation):

| Form | Count | Gloss |
|:--|--:|:--|
| الله | 2153 | "Allāh" (standalone) |
| والله | 240 | "wa-llāh" (and Allāh) |
| بالله | 139 | "bi-llāh" (by/in Allāh) |
| لله | 116 | "li-llāh" (to/for Allāh; orthographic article-elision) |
| ولله | 27 | "wa-li-llāh" |
| تالله | 8 | "ta-llāh" (oath particle ta + Allāh) |
| فالله | 6 | "fa-llāh" |
| فلله | 6 | "fa-li-llāh" |
| اللهم | 5 | "Allāhumma" (vocative) |
| آلله | 2 | "ā-llāh" (interrogative; Q 10:59, 27:59) |
| أبالله | 1 | "a-bi-llāh" (Q 9:65) |
| وتالله | 1 | "wa-ta-llāh" (Q 21:57) |
| **Σ (D)** | **2704** | |

**Verdict: FALSIFIED.** Under no pre-committed counting convention does the *Allāh*-reference total equal 2698, and no pre-committed tally is divisible by 19.

**The 2698 figure is unrecoverable from the standard Hafs corpus.** The most plausible explanations:
1. al-Khalifa's appendix used a different ad-hoc counting convention (possibly excluding `اللهم` and a specific subset of prefixed forms — e.g., A + B-minus-vocative + C-minus-something would have to land on 2698 by an ad-hoc operationalisation we cannot reconstruct from his appendix text).
2. al-Khalifa's count may include or exclude specific verse-occurrences he flagged as "scribal additions" (he separately argued Q 9:128-129 are spurious "two false verses"; see `data/literature/khalifa/1989-khalifa-appendix-24-two-false-verses.md`). Excluding *Allāh* references in Q 9:128-129 from our Tally B yields 2551 minus 2 = 2549; still not 2698.
3. The 2698 figure was reverse-engineered (i.e., target-set first, definition-chosen to fit) and not faithfully replicable on the standard corpus.

The closest definition-dependent rescue (E = 2699) is **one off from the target**, and the deviation has the wrong direction (2699 is not a multiple of 19; 2698 = 19 × 142 and 2717 = 19 × 143). **No rules-tuple variant available to us recovers 2698.**

This is the most-cited al-Khalifa claim (basmala letter count is more famous but C5 is more empirically central to the divisibility thesis). Its failure to verify on the standard corpus is the heart of the audit.

## Summary table

| ID | Claim | Target | Observed | Verdict |
|:--|:--|--:|--:|:--|
| C1 | Q 96:1-5 = 19 words | 19 | 20 | **FALSIFIED** |
| C2 | Q 1 (al-Fātiḥa) = 29 words | 29 | 29 | **CONFIRMED** |
| C3 | corpus = 114 surahs = 19×6 | 114 | 114 | **CONFIRMED** (trivial) |
| C4 | basmala = 19 letters (no-tashkeel) | 19 | 19 | **CONFIRMED** |
| C5 | total Allāh = 2698 = 19×142 | 2698 | 2153 / 2551 / 2700 / 2704 / 2699 (five definitions) | **FALSIFIED** |

## Cumulative assessment

Is the al-Khalifa "miracle of 19" empirically supported?

**No, not at the level of the five most-cited specific sub-claims.** The pattern of confirms/falsifies is itself diagnostic:

**The CONFIRMED claims are pre-existing facts of the canonical text.**
- C3 (114 surahs) is a fact of the ʿUthmānic compilation, 1300+ years pre-Khalifa.
- C4 (basmala = 19 letters) is a fact of the Arabic rasm, well-known to medieval ḥurūfī scholars (al-Būnī, al-Bisṭāmī, al-Tilimsānī, al-Suyūṭī *al-Itqān* nawʿ 17), centuries pre-Khalifa.
- C2 (Fātiḥa = 29 words) is a classical word-count finding (al-Suyūṭī *al-Itqān* nawʿ 19), restated by al-Khalifa with a 19+10 split-interpretation that is itself definition-dependent (19 not divisible by 29).

al-Khalifa's contribution in these three cases is **selecting** which pre-existing 19-related fact to highlight and assembling them into a single thesis. This is the textbook *garden of forking paths* / *post-hoc selection bias* pattern (cf. Gelman & Loken 2013): the corpus contains many numerical regularities; choosing those that resolve to 19 after the fact and treating them as a unified miracle is a classic confirmation-bias structure.

**The FALSIFIED claims are al-Khalifa's NOVEL contributions** — i.e., the specific 19-divisibility patterns that would, if true, constitute *new* evidence beyond what classical scholarship already counted.
- C1 (Q 96:1-5 = 19 words / 76 letters): a specific al-Khalifa claim. **Falsifies at 20 words, 78 letters.**
- C5 (Allāh = 2698 = 19 × 142): al-Khalifa's flagship divisibility claim. **No pre-committed counting convention recovers 2698, and no convention's tally is divisible by 19.**

These are exactly the claims that would have to confirm to validate the *Miracle-of-19* thesis as a *finding about the text*. They do not confirm.

This audit is consistent with the project-wide H-META-1 finding: claims categorised as "numerical-gematric" + "modern-numerology era" confirm at **0% (0/10)** under empirical audit, versus structural-formal classical claims at **72% (53/74)** (see `MASTER-FINDINGS-LEDGER.md` §1 item 5 and §10 H-META-1 entry). The al-Khalifa Code-19 thesis fits this distribution: its trivially-true or pre-existing classical components (C2, C3, C4) survive; its novel-numerical claims (C1, C5) do not.

This is also consistent with the academic critical literature: Bilāl Philips 1987 (*Quran's Numerical Miracle: Hoax and Heresy*) argued that al-Khalifa's appendices used definitional flexibility and verse-omission to manufacture 19-divisibility; the empirical inability to reproduce 2698 under five honestly-listed nested definitions is direct corroboration of that critique.

## Scope of this audit and what is NOT tested

Only 5 specific sub-claims were audited. The much larger al-Khalifa appendix-1 corpus contains:
- Muqaṭṭaʿāt letter-divisibility claims (29 surahs × variable letter-sets).
- 14 different initial-letter sets and their per-surah counts.
- Concatenated verse-number divisibility claims ("Grand Total = 346,199").
- Salāt/sawm/zakāt/ḥajj numerology (claim IDs `khalifa-salat-67`, `khalifa-sawm-1387`, `khalifa-zakat-hajj-3040`).

These warrant their own pre-registered audits. The classical-quantitative-claims audit at `findings/phase-b-hypotheses/classical-quantitative-claims-audit.md` and the H-META-1 distribution analysis already cover several of them at survey level; per-claim pre-registered tests are scope for future H-NEW entries.

## Replication

```bash
cd /Users/grey/Downloads/quran
python3 findings/phase-b-hypotheses/scripts/h-new-1530.py
# verifies prereg SHA, runs all 5 sub-claims, writes csv/h-new-1530.json
```

Expected output (deterministic; no permutation):
- C1: 20 words → FALSIFIED
- C2: 29 words → CONFIRMED
- C3: 114 surahs → CONFIRMED
- C4: 19 letters → CONFIRMED
- C5: tally_A=2153, tally_B=2551, tally_C=2700, tally_D=2704, tally_E=2699 → FALSIFIED

## Honest limits

1. **Tashkeel/orthography sensitivity is well-documented for C4 only.** We probed three orthographic representations (no-tashkeel, full-tashkeel-base-letters, uthmani-consonantal). All return 19. The claim is robust under all standard representations.
2. **C5 ambiguity envelope is finite but real.** Five nested counting conventions are insufficient to enumerate all conceivable definitions; an adversarial post-hoc operationalisation could possibly construct a 19-divisible *Allāh*-tally from a non-standard subset. We pre-committed to the five tallies above to prevent this.
3. **C1 verse-segmentation flexibility.** Classical tradition includes minor variants on what "the first revelation" means (Q 96:1-3 vs 1-5 vs 1-6, and sometimes including or excluding the basmala). We tested 96:1-5 per al-Khalifa's stated boundary. We also note: no Q 96 first-N boundary yields exactly 19 words or 76 letters.
4. **Trivially-true C3 has near-zero evidentiary weight.** It is a corpus-arithmetic sanity check, not a substantive 19-coding finding.
5. **C2 = 29 is correct but does not entail 19-divisibility.** The al-Khalifa interpretation requires a 19+10 split with definitional choices we did not test (that is a separate sub-claim).
6. **This audit cannot adjudicate al-Khalifa's broader theological-philosophical thesis.** Empirical 19-divisibility on 5 sub-claims is necessary-not-sufficient evidence; theology is out of scope.

## Cross-references

- `MASTER-FINDINGS-LEDGER.md` §10 H-META-1 (claim-signature classifier; modern-numerology 0% confirmation rate)
- `findings/phase-b-hypotheses/classical-quantitative-claims-audit.md` (survey-level audit of classical numerical claims)
- `data/literature/khalifa/1989-khalifa-appendix-1-one-of-the-great-miracles.md` (primary source)
- `data/literature/khalifa/1989-khalifa-appendix-24-two-false-verses.md` (al-Khalifa's Q 9:128-129 omission claim — separately auditable)
- `data/literature/khalifa/1989-khalifa-appendix-29-missing-basmalah.md` (Q 9 basmala-omission claim — separately auditable)
- `data/literature/khalifa/submission-quran-chemistry-code-19.md` (chemistry extension of Code-19 — out of scope)

## Bibliography

- Khalifa, R. (1989). *Quran: The Final Testament, Authorized English Version*. Tucson: Islamic Productions. Appendix 1, "One of the Great Miracles." Primary source at `data/literature/khalifa/1989-khalifa-quran-the-final-testament.pdf`.
- Khalifa, R. (1982). *Quran: Visual Presentation of the Miracle*. Tucson: Islamic Productions. PDF at `data/literature/khalifa/1982-khalifa-quran-visual-presentation-of-the-miracle.pdf`.
- Philips, A. A. B. (1987). *Quran's Numerical Miracle: Hoax and Heresy*. Riyadh: Tawheed Publications.
- al-Suyūṭī, Jalāl al-Dīn. *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 (*fī ʿadad ḥurūf al-Qurʾān*) and nawʿ 19 (*fī ʿadad āyātihi wa-kalimātihi*). On-disk: `data/literature/classical-tafsir/al-suyuti-itqan/`.
- Gelman, A., & Loken, E. (2013). "The garden of forking paths." *American Statistician*. (Selection-bias framework.)

---

*Audit conducted 2026-05-09. Pre-registration SHA-locked before computation. Five sub-claims tested under direction-locked integer-equality. 3 CONFIRMED, 2 FALSIFIED, composite SPLIT. The novel-numerical claims (C1, C5) fail; the pre-classical text-facts (C2, C3, C4) hold.*
