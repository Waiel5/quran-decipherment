---
surah: 83
surah_name_ar: المطففين
surah_name_translit: al-Muṭaffifīn
file_type: novel-findings
date_last_updated: 2026-05-29
phase: B+
verdict: Q083-F-01 = DIRECTIONAL with PRE-COMMIT VIOLATION on H1 (published with full prominence); H3 CONFIRMED.
---

# Q 83 al-Muṭaffifīn — Novel Findings

## Q083-F-01 — SIJJĪN ↔ ʿILLIYYĪN antithetical-pair structure

- **Pre-reg:** `preregs/Q083-F-01-sijjin-illiyyin-antithesis-prereg.md`
  (SHA-256 `acd67eb32847fa20631a37fedb608b04ef8f42152edcd618b51e4eaa7602ddc6`).
- **Script:** `scripts/Q083_F_01_sijjin_illiyyin_antithesis.py` (SHA verified at runtime — PASS).
- **Output:** `csv/Q083-F-01.json`. **Seed 20260509, 10000 perms, Bonferroni k=3, α_bon = 0.016667.**
- **Rules-tuple:** `(no-tashkeel, QAC-STEM root tokens, QAC v0.4, graphemes, basmala-counted-only-in-Q1,
  Hafs-Kūfan, Mashriqī)`.

### Hypotheses (locked before observation)

- **H1 (one-tailed, ELEVATED — locked):** the fujjār-block (vv. 7–17) and abrār-block (vv. 18–28) share
  an anomalously HIGH count of frame roots vs random equal-length (11-verse) block pairs.
- **H2 (descriptive pivot, no locked direction):** overall root-Jaccard percentile.
- **H3 (one-tailed, DISJOINT=0 — locked):** the two destiny-vocabularies are mutually exclusive.

### Results

| Quantity | Value | |
|:--|:--:|:--|
| roots(B_f) | 24 | distinct QAC roots in vv. 7–17 |
| roots(B_a) | 22 | distinct QAC roots in vv. 18–28 |
| **shared roots (H1)** | **3** | `ktb` (kitāb), `rqm` (marqūm), `dry` (adrāka) — the bare announcement frame |
| null shared-root mean | **12.715** | random 11-verse block pairs (10000, corpus-wide) |
| null shared-root max | 82 | |
| **perm-p (H1, elevated)** | **0.9428** | direction REVERSED — observed FAR BELOW null |
| perm-p within-surah null | 0.9563 | reversal holds under the within-single-surah null too |
| Jaccard (H2) | 0.0698 | vs null mean 0.1129 |
| H2 percentile (low-side ≤ obs) | 0.2415 | TYPICAL (within central 90%) |
| **destiny-disjoint (H3)** | **TRUE** (0 leakage) | fujjār {sjn, jHm, Hjb} ⟂ abrār {Elw, nEm, rHq, msk, snm, Ark} |

### Verdict: **DIRECTIONAL — PRE-COMMIT VIOLATION on H1; H3 CONFIRMED.**

### ⚠️ H1 pre-commit violation (published with full prominence)

I locked H1 in the WRONG direction. I predicted the two blocks would share an ELEVATED number of frame
roots (a "lexical mirror"). The data REVERSED this: the blocks share only **3 roots** — exactly and ONLY
the `kitāb / marqūm / adrāka` announcement frame — against a null mean of **12.7**. The two blocks are
**far MORE lexically disjoint than two random 11-verse blocks** (perm-p for elevated = 0.943; the
observed value sits at roughly the 10th percentile from the LOW end, robust across seeds
{20260509, 20260601, 99999, 12345}, null mean ≈ 12.8 throughout). Per PRE-REG-STANDARD-01 and Protocol
§1.8, this is reported as a NULL/violation on H1, NOT massaged into a confirmation.

**Why I was wrong (the substantive lesson):** I conflated *frame-parallelism* with *lexical overlap*. The
Q 83 muqābala IS frame-parallel (both scenes open with the identical *kallā inna kitāba …, wa-mā adrāka
mā …, kitābun marqūm* formula), but that frame is only **3 roots**. Everything else — the deniers'
psychology (vv. 10–17) vs the blessings catalogue (vv. 21–28) — is built from entirely separate
vocabulary. The antithesis is an austere, **minimal-contact** mirror: the blocks touch only at the
announcement scaffold and are otherwise lexically segregated. This is rhetorically MORE disciplined than
a "mirror" and is the genuinely interesting empirical fact the test surfaced.

### H3 confirmation (the clean positive)

The destiny-vocabulary disjunction is **perfect and deterministic**:
- FUJJĀR destinies present in B_f only: `sjn` (sijjīn), `jHm` (jaḥīm), `Hjb` (maḥjūbūn).
- ABRĀR destinies present in B_a only: `Elw` (ʿilliyyīn), `nEm` (naʿīm), `rHq` (raḥīq), `msk` (misk),
  `snm` (tasnīm), `Ark` (arāʾik).
- Cross-leakage in BOTH directions = 0; the locked sets do not intersect.

So the two records are named with **mutually exclusive destiny-lexicons**. Combined with the H1 reversal,
the empirical signature of the Q 83 muqābala is: **a 3-root shared announcement frame + a fully
disjoint destiny-lexicon + below-average overall Jaccard.** The "mirror" lives in the SYNTAX of the
announcement, not in the WORDS of the two destinies.

### Honest limits

- The 3 shared roots were guaranteed a priori by the verbatim *kitābun marqūm* / *wa-mā adrāka* formulae
  (disclosed in pre-reg §6). The test's value is the QUANTIFICATION of how far below the null the total
  overlap sits — which turned out to be substantial (≈10th percentile, low side) but NOT
  Bonferroni-significant from the low side (α_bon = 0.0167). So the disjunction is *notable, not extreme*
  as a single statistic; the clean result is H3's deterministic perfect-disjunction.
- Root-SET (presence) was used, not root-bag; a bag-cosine robustness was not the gated statistic.
- The within-surah null (p=0.956) confirms the reversal is not an artifact of cross-surah block sampling.

### How this updates the corpus picture

- **Vindicates** the al-Rāzī/al-Zamakhsharī *muqābala* reading (03, 05 Claim 3) in a sharpened form.
- **Caution for future antithesis tests** elsewhere in the corpus: do NOT pre-lock "antithetical pair ⇒
  elevated shared vocabulary." The Q 83 case shows a strong antithesis can be MINIMALLY lexically
  overlapping. A future corpus-wide test of muqābala-pairs should lock the direction as
  *frame-shared + content-disjoint*, with the frame defined as a small closed scaffold, not as "high
  Jaccard." This is a transferable methodological correction (candidate for promotion if it recurs).

## Cross-references
- 05-classical-claims-audit Claim 3 (muqābala verdict).
- 02-content-analysis §4 (close-reading of the diptych).
- `csv/Q083-F-01.json` (full numerical output).
