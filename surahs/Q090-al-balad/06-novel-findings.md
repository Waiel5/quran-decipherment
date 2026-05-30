---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q090-F-01 CONFIRMED (corpus-hapax-root enrichment, p_perm=0.0012/0.0008, replicated) WITH an honest register-level limit — the MW-6 control Q 91 is equally enriched, so the effect is short-Meccan-register, not Q 90-exclusive
---

# Q 90 al-Balad — Novel Findings

## Q090-F-01 — Corpus-hapax-root enrichment in al-Balad

**Pre-registration:** `Q090-F-01-balad-hapax-uqsimu-prereg.md`
(SHA-256 `5ab5e79bb7e3dcf20a36e1e7e5fccc0d64cdcbe6ac27d52c0925d7d988411d18`, verified at runtime).
**Script:** `scripts/Q090_F_01_balad_hapax_uqsimu.py`. **Output:** `csv/Q090-F-01.json`.
**Seed:** 20260509 (primary), 20260530 (MW-5). **n_perm:** 10,000. **Bonferroni k=2, α_bon=0.025.**

### 1. The observation

A close-read of the QAC v0.4 morphology shows Q 90 carries **four roots that occur nowhere else in the
Quran** (corpus surah-singletons whose unique surah is Q 90):

| Root | Verse | Word | Gloss |
|:--|:--|:--|:--|
| `kbd` | 90:4 | *kabad* | toil / hardship (the jawāb al-qasam) |
| `$fh` | 90:9 | *shafatayn* | the two lips |
| `njd` | 90:10 | *al-najdayn* | the two highways |
| `sgb` | 90:14 | *masghaba* | severe hunger |

These cluster in the surah's most **concrete, physical imagery** — the toil of human creation, the
faculties (lips), the two paths, the day of hunger. Q 90 has 45 distinct QAC-STEM roots (52 root-tokens).

### 2. The pre-registered test (LOCKED direction: ENRICHMENT)

- **H1 (count):** Is the number of corpus-exclusive roots assigned to Q 90 greater than a
  length-preserving permutation null produces?
- **H2 (density):** Same for the exclusive-root density (count / distinct-roots).
- **Null model:** the full corpus root-occurrence stream (N = 49,968 tokens carrying a `ROOT:` field)
  with its surah-label column permuted (Fisher-Yates, seed-locked). This **exactly preserves** each
  surah's token-count and each root's corpus frequency, destroying only the surah↔root association. For
  the exclusive-count statistic this is equivalent to the multivariate-hypergeometric realised in the
  script by random priority-ranking of occurrence slots (documented in the script docstring; the count
  statistic is identical to a full label-permutation).

### 3. Results

| Arm | Observed | Null mean | Null max | p_perm | α_bon (0.025) |
|:--|:--|:--|:--|:--|:--|
| **H1 count** | **4** | 0.4184 | 4 | **0.00120** | **PASS** |
| **H2 density** | **0.0889** | — | — | **0.00080** | **PASS** |
| MW-5 replication (seed 20260530, count) | 4 | — | — | **0.00080** | direction + pass reproduced |

Observing **4** corpus-exclusive roots when chance expects **0.42** is a ~9.6× enrichment, with the
observed value sitting at the extreme upper tail (null max = 4, reached only rarely). Both arms pass the
Bonferroni threshold by an order of magnitude, in the **locked enrichment direction** — no pre-commit
violation.

### 4. MW-6 negative control — THE HONEST LIMIT

The pre-registered within-corpus control is **Q 91 al-Shams** (15 verses, the forward neighbor, same
{87–93} window). If the hapax-enrichment were a generic short-Meccan-register artefact rather than a
Q 90-specific signal, Q 91 should be enriched too. Result:

| Surah | Exclusive roots | Distinct roots | density | p_perm |
|:--|:--|:--|:--|:--|
| Q 90 al-Balad | 4 | 45 | 0.0889 | 0.00120 |
| **Q 91 al-Shams (control)** | **4** | **36** | **0.1111** | **0.00040** |

**Q 91 is EQUALLY (in fact slightly MORE) enriched.** This is decisive: **the hapax-root enrichment is a
property of the early-Meccan concrete-oath register, NOT a Q 90 singleton.** The short oath-surahs
(al-Balad, al-Shams, and their neighbors — recall the hapax-density top-12 is dominated by Q 81, 91, 90,
79, 100, 111…) introduce dense, concrete, often-unique vocabulary (cosmic/anatomical/agricultural imagery)
that appears once and never recurs in the discursive long surahs.

### 5. Verdict

**Q090-F-01: CONFIRMED — at the register level.** The pre-registered hypothesis (Q 90 carries more
corpus-exclusive roots than a length-preserving null) passes both arms at α_bon = 0.025 in the locked
direction and replicates. **But the MW-6 control forbids any claim that this distinguishes Q 90 from its
neighbors.** The honest reading:

> Q 90 al-Balad is significantly hapax-enriched (4 corpus-exclusive roots vs ~0.42 expected, p ≈ 0.001),
> but this is shared with its short-Meccan oath-surah neighbors (Q 91 al-Shams equally so). The finding
> is a **register-level lexical signature** of the early-Meccan concrete-oath block, not a property unique
> to al-Balad.

This is itself a useful result: it converts a tempting "al-Balad is lexically special" narrative into a
disciplined "the early-Meccan oath register is lexically generative of hapaxes" — a generalizable,
corpus-implication claim (candidate for promotion to an H-NEW global finding if a full per-surah
hapax-register-gradient is run).

### 6. MW protections recap

- **MW-1:** statistic + root-source + null fixed in the pre-reg before running.
- **MW-2:** 10,000-perm null preserving both marginals.
- **MW-3:** two statistics (count H1 + density H2) on the same null.
- **MW-4:** no fitted parameter.
- **MW-5:** second-seed replication (20260530) reproduces direction + pass (p = 0.0008).
- **MW-6:** Q 91 control — **fires** (equally enriched) → demotes the claim from "Q 90-specific" to
  "register-level." Reported with full prominence.
- **MW-7:** the Q 75/Q 90 *lā uqsimu* doublet FR descriptive (§ below) is post-hoc-inspected → no verdict.

### 7. Companion descriptive observation (MW-7-capped, NO verdict)

Q 90 is one of only **two** surahs that OPEN at verse 1 with the *(lā) uqsimu* form (the other is Q 75
al-Qiyāma), per the H-NEW-2210 inventory. Their jawāb structures differ: Q 75's apodosis is classically
**elided** (`bare`), Q 90's is the explicit lām-al-tawkīd at v 4. The pair is **NOT close in FR space**
(FR = 0.6695, rank 37/113) — the oath-form is an opener-grammar axis orthogonal to content. This is
recorded as a structural-descriptive fact only; the FR geometry was inspected during scoping, so it
carries the single-test cap and no inferential claim (consistent with `05-classical-claims-audit.md`
Claim 5 and the project's opener-axis ⊥ content-axis law).

### 8. Honest limits

- The enrichment is **register-level, not surah-specific** (MW-6). Do not over-read it as "al-Balad is
  uniquely rare-worded."
- "Corpus-exclusive" is defined at the QAC-STEM root level; a lemma-level or surface-token definition
  would yield slightly different hapax sets.
- The null permutes occurrence labels globally; an alternative null preserving the verse-block structure
  within surahs would be a stricter test (queued).
- The companion *lā uqsimu* doublet observation is descriptive; no permutation test was run on the
  doublet's FR geometry (and none is claimed).

---

*Pre-registered, run, replicated, and honestly limited. 2026-05-30. Bismillāh.*
