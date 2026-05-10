---
id: H-NEW-1530
title: al-Khalifa "miracle of 19" — 5 sub-claim rigorous audit (integer-equality)
date_locked: 2026-05-09
phase: B
status: pre-registered
seed: 20260509
n_perm: 0
---

# H-NEW-1530 — Pre-registration

## Hypothesis (DIRECTION-LOCKED before observation)

**H1** (composite): At least 3 of 5 specific Rashad al-Khalifa "miracle of 19" sub-claims (catalogued in `data/literature/khalifa/1989-khalifa-appendix-1-one-of-the-great-miracles.md`) will EITHER confirm or falsify when tested against the canonical Hafs-Kūfan corpus on disk. Per-sub-claim direction is the claim's own integer value (i.e., the test is integer-equality, not a one-tailed inequality).

This is a CLASSICAL-CLAIM AUDIT (protocol §2.9). Each of the 5 sub-claims is a fixed integer-equality verification; no permutation null is appropriate (a count either matches or does not). The composite hypothesis (≥3-of-5 verdicts cleanly issued) is itself trivially satisfied so long as each sub-claim is computable — the substantive interest is the verdict distribution.

## Theoretical motivation

Rashad al-Khalifa (1935-1990) advanced the "Code 19" / "miracle of 19" thesis starting 1974, claiming a divisibility structure of the canonical Qurʾān by 19 (cf. Q 74:30 *ʿalayhā tisʿata ʿashar*). He was assassinated in 1990 and his claims are contested across the Sunni mainstream (largely rejected), academic critics (rejected on selection-bias grounds — Bilāl Philips 1987, *Quran's Numerical Miracle: Hoax and Heresy*), and modern Submitters (accepted as proof of divine origin). The most-cited sub-claims are integer counts which we can verify directly against the on-disk corpus.

Classical caveat: ʿilm al-ḥarf (letter-mysticism) and ḥisāb al-jummal (numerical-gematric) traditions catalogued by al-Suyūṭī *al-Itqān* nawʿ 17 long predate al-Khalifa, but those classical traditions are themselves audit subjects of this project (cf. H-META-1 finding: numerical-gematric claim confirmation rate 32% [6/19], vs structural-formal 72%; modern-numerology era 0% [0/10] confirmation).

## Pre-committed sub-claims (locked BEFORE computation)

Each sub-claim is verbatim from `1989-khalifa-appendix-1-one-of-the-great-miracles.md` or the cross-listed `claims-catalog` IDs. Per-claim verdict is one of {CONFIRMED, FALSIFIED, DEFINITION-DEPENDENT}.

### C1 — First-revelation 19 words (claim ID: khalifa-first-revelation-19-words-76-letters)

**Claim**: The first revealed verses Q 96:1-5 contain exactly **19 words** total.

**Verification**: Count whitespace-delimited tokens in Q 96:1, Q 96:2, Q 96:3, Q 96:4, Q 96:5 from `quran-text/quran-no-tashkeel.json`.

**Verdict rule**: CONFIRMED if total = 19; FALSIFIED otherwise.

### C2 — al-Fātiḥa 29 words (claim ID: derived from khalifa-bismillah / appendix-1 word-count table)

**Claim**: Sūrah al-Fātiḥa (Q 1) contains exactly **29 words** total (per al-Khalifa appendix-1; sometimes broken 19 + 10 with a basmala accounting variant).

**Verification**: Count whitespace-delimited tokens in all 7 verses of Q 1 from `quran-text/quran-no-tashkeel.json`. Basmala (Q 1:1) counted (basmala-counted-only-in-Q1 rule).

**Verdict rule**: CONFIRMED if total = 29; FALSIFIED otherwise.

### C3 — 114 surahs = 19 × 6 (claim ID: khalifa-114-chapters-19x6)

**Claim**: The corpus contains **exactly 114 surahs** and 114 = 19 × 6.

**Verification**: `len(json)` on `quran-text/quran-no-tashkeel.json`.

**Verdict rule**: CONFIRMED if surah-count = 114 AND 114 mod 19 = 0; FALSIFIED otherwise.

(This is a trivial CONFIRM but pre-registered as a sanity control on the corpus + arithmetic pipeline.)

### C4 — Basmala = 19 letters (claim ID: khalifa-bismillah-19-letters)

**Claim**: The phrase *bismi-llāhi al-raḥmāni al-raḥīm* contains exactly **19 letters** (graphemes, no-tashkeel, excluding spaces).

**Verification**: Take Q 1:1 text from `quran-text/quran-no-tashkeel.json` ("بسم الله الرحمن الرحيم"), remove spaces, count Unicode code-points (each Arabic letter is one BMP code-point; the no-tashkeel form contains no combining marks).

**Verdict rule**: CONFIRMED if grapheme-count = 19; FALSIFIED otherwise.

Rules-tuple sensitivity probe (additional, not gated): also verify on full-tashkeel form and on `data/alt-text/quran-uthmani-consonantal.json` to document orthographic robustness.

### C5 — Allāh occurrences total = 2698 = 19 × 142 (claim ID: appendix-1 "God appears 2,698 times")

**Claim**: The total occurrences of the name *Allāh* in the entire Qurʾān is **2698**, and 2698 = 19 × 142.

**Verification**: Count word-occurrences in `quran-text/quran-no-tashkeel.json` matching any of the canonical Allāh-reference word forms. Because al-Khalifa's appendix is not fully transparent about which prefixed forms are counted, we will report **five nested tallies**:

- **Tally A — strict standalone**: only the exact word `الله`.
- **Tally B — A + classical prefixed (wa/fa/bi/ta) + vocative (اللāhumma)**: A plus `والله، فالله، بالله، تالله، اللهم`.
- **Tally C — B + li-llah forms**: B plus `لله، ولله، فلله` (the lām-prefixed dative forms, where Arabic orthography elides the alef but the reference is to Allāh).
- **Tally D — C + interrogative/compound prefixed**: C plus `آلله، أبالله، وتالله`.
- **Tally E — D's set, but exclude `اللهم` (vocative is a grammatical particle, not strictly the Name)**.

**Verdict rule for C5**: 
- If ANY of tallies A-E exactly equals 2698 → CONFIRMED (with note on which definition matches).
- Else if ANY tally is divisible by 19 AND is within ±20 of 2698 (i.e., al-Khalifa's number is close but his exact tally definition is not recoverable from the corpus, while *some* canonical Allāh-tally IS 19-divisible) → DEFINITION-DEPENDENT.
- Else → FALSIFIED.

We additionally report the modular-19 residue of each tally so the audit is fully transparent.

## Pre-committed measurement protocol

- **Corpus**: `quran-text/quran-no-tashkeel.json` (primary). For C4 secondary probe also `quran-text/quran-full-tashkeel.json` and `data/alt-text/quran-uthmani-consonantal.json`.
- **Token**: whitespace-split for word counts; Unicode code-point for grapheme counts.
- **Tashkeel**: no-tashkeel (rules-tuple §1.4 default) for primary verdicts; full-tashkeel + uthmani-consonantal probes for C4 robustness only.
- **Reading**: Hafs-Kūfan (the on-disk JSON is Hafs).
- **Basmala**: counted in Q 1 only (it is encoded as Q 1:1 in the JSON; no other surah has it as v1 in this file, matching the standard 6236 total-verse convention).
- **Allāh-form recognition**: exact-string match against the closed list above; the morphological boundaries are not language-modelled (a known limitation, documented in C5).

## Verdicts

| Outcome | C1 | C2 | C3 | C4 | C5 | Composite |
|:--|:--|:--|:--|:--|:--|:--|
| All confirm | ✓ | ✓ | ✓ | ✓ | ✓ | "MIRACLE OF 19 EMPIRICALLY SUPPORTED" |
| ≥4-of-5 confirm | various | | | | | "STRONG-PARTIAL SUPPORT" |
| 3-of-5 confirm | various | | | | | "SPLIT" |
| ≤2-of-5 confirm | various | | | | | "LARGELY FALSIFIED" |
| 0-of-5 confirm | ✗ | ✗ | ✗ | ✗ | ✗ | "FULL FALSIFICATION" |

## Pre-commit violations and stop conditions

- If a sub-claim's verdict is post-hoc adjusted (e.g., switching to a per-claim relaxation rule after seeing the count): pre-commit violation → that sub-claim becomes NULL with explicit note.
- If the Allāh-tally definition is post-hoc tuned to find a 19-divisible match: pre-commit violation. We are pre-committing to the FIVE specific tallies A-E above; no others will be reported as confirming.
- If any count differs from a future re-run on the same JSON: data-integrity flag; re-verify against `quran-text/_external_git` upstream.

## Bonferroni / α

C1, C2, C3, C4 are integer-equality claims (each result is binary: equals the claimed integer or does not). No p-value is generated. No Bonferroni applies; the test is sharp.

C5 is also integer-equality but reports 5 nested definitions. To avoid post-hoc cherry-picking we have explicitly listed all 5 definitions BEFORE computation. If any one yields 2698 exactly, C5 CONFIRMS; if any is 19-divisible within ±20 of 2698, DEFINITION-DEPENDENT; else FALSIFIED. The 5 tallies are not "5 tests of one hypothesis" requiring Bonferroni — they are 5 *alternative operationalisations of one ambiguous claim* whose ambiguity is itself a finding.

## Constants

```
SEED          = 20260509
TARGETS       = {C1:19, C2:29, C3:114, C4:19, C5:2698}
ALLAH_FORMS_A = ['الله']
ALLAH_FORMS_B = ALLAH_FORMS_A + ['والله','فالله','بالله','تالله','اللهم']
ALLAH_FORMS_C = ALLAH_FORMS_B + ['لله','ولله','فلله']
ALLAH_FORMS_D = ALLAH_FORMS_C + ['آلله','أبالله','وتالله']
ALLAH_FORMS_E = [w for w in ALLAH_FORMS_D if w != 'اللهم']
BASMALA_REF   = 'بسم الله الرحمن الرحيم'
```

## Data dependencies

- `quran-text/quran-no-tashkeel.json` — primary corpus
- `quran-text/quran-full-tashkeel.json` — C4 probe
- `data/alt-text/quran-uthmani-consonantal.json` — C4 probe
- `data/literature/khalifa/1989-khalifa-appendix-1-one-of-the-great-miracles.md` — source claims

## Output schema

`findings/phase-b-hypotheses/csv/h-new-1530.json`:
```
{
  "id": "H-NEW-1530",
  "title": "...",
  "prereg_sha": "<embedded at runtime>",
  "seed": 20260509,
  "sub_claims": {
    "C1": {"claim":"Q 96:1-5 = 19 words", "observed":int, "expected":19, "verdict":"..."},
    "C2": {"claim":"Q 1 = 29 words", "observed":int, "expected":29, "verdict":"..."},
    "C3": {"claim":"114 surahs = 19*6", "observed":int, "expected":114, "verdict":"..."},
    "C4": {"claim":"basmala = 19 letters", "observed":int, "expected":19, "verdict":"...",
           "probes": {"no-tashkeel":int, "full-tashkeel":int, "uthmani-consonantal":int}},
    "C5": {"claim":"Allah-occurrences = 2698 = 19*142", "expected":2698,
           "tally_A":int,"tally_B":int,"tally_C":int,"tally_D":int,"tally_E":int,
           "tally_A_mod19":int,"tally_B_mod19":int,"tally_C_mod19":int,"tally_D_mod19":int,"tally_E_mod19":int,
           "verdict":"..."}
  },
  "verdict_tally": {"CONFIRMED":int, "FALSIFIED":int, "DEFINITION-DEPENDENT":int},
  "composite_verdict": "..."
}
```

## Honest limits

1. **Selection-bias caution.** Bilāl Philips and W.M. Watt have argued that al-Khalifa's appendix selectively chose definitions and word-forms to manufacture 19-divisibility. This audit cannot adjudicate the global selection bias of his appendix — we test only 5 specific named sub-claims.
2. **Orthographic sensitivity.** The basmala letter-count (C4) is sensitive to whether one counts the alef of *Allāh* (which is orthographically present in `بسم الله` only as part of the article ال; in Uthmanic script the alef of *Allāh* itself is elided in dagger-alef form). We probe both representations.
3. **Allāh-form ambiguity (C5).** Without al-Khalifa's exact word-form list, we cannot replicate his exact 2698. The five nested tallies A-E document the full ambiguity envelope.
4. **Trivially-true sub-claim (C3).** 114 = 19 × 6 is included as a corpus + arithmetic sanity control, not as substantive evidence. A confirmation of C3 alone is uninformative.
5. **Integer-equality has no Bonferroni.** Each sub-claim is sharp; a confirmation is either real or fabricated, not statistically borderline.
6. **What this audit does NOT test.** The much-larger appendix-1 claims (muqaṭṭaʿāt letter-counts divisible by 19, verse-number concatenations divisible by 19, the "Grand Total 346,199", etc.) are out of scope here. They warrant separate pre-registered audits.

*Locked 2026-05-09. Direction: integer-equality per sub-claim. SHA to be computed and embedded post-write.*
