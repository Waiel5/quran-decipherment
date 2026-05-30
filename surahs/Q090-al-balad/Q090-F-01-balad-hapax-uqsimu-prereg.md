---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
file_type: pre-registration
test_id: Q090-F-01
date_registered: 2026-05-30
phase: B+
status: LOCKED (pre-observation for the verdict-bearing arm)
seed: 20260509
n_perm: 10000
bonferroni_k: 2
alpha_bon: 0.025
---

# Q090-F-01 — Pre-registration

**Surah:** Q 90 al-Balad (Meccan, 20 verses, revelation order #35 Early Meccan,
`data/revelation-order.csv` line `35,90,البلد,...`).

This pre-registration is written **before** the verdict-bearing permutation null is run.
SHA-256 of this file (after the line below is finalized and the file is frozen) is embedded
in `scripts/Q090_F_01_balad_hapax_uqsimu.py` and verified at runtime (fail-fast on mismatch).

Rules-tuple: `(no-tashkeel, QAC-v0.4 STEM root-tokens, graphemes, basmala-counted-only-in-Q1,
Hafs-Kufan, Mashriqi)`.

---

## 1. Motivation

Q 90 al-Balad opens with the negated-oath form **`lā uqsimu bi-hādhā al-balad`** (90:1) — the
*(lā) uqsimu* qasam introducer catalogued morphologically in H-NEW-2210 (8 corpus attestations of
the form `LEM:>aqosamu` form-IV impf 1S). Its jawāb al-qasam is **`la-qad khalaqnā al-insān fī
kabad`** (90:4) — the lām-al-tawkīd apodosis identified by al-Ṭabarī (*Jāmiʿ al-bayān* on 90:4:
"هذا هو جواب القسم") and al-Zamakhsharī (*al-Kashshāf*: "alā tarā kayfa laqqā *lā uqsimu bi-hādhā
al-balad* bi-qawlihi *lā-qad khalaqnā al-insān*").

Two independent, pre-locked observations motivate the test:

1. **(verdict-bearing) Content-hapax distinctness.** A close-read of the QAC morphology shows
   Q 90 carries roots that occur **nowhere else** in the corpus. The surah's dense, concrete,
   physiognomic vocabulary (the two-lips / two-highways / hunger / toil imagery) is the candidate
   driver. Test: is Q 90's count of **corpus-exclusive (surah-singleton) roots** larger than a
   length-preserving permutation null would produce?

2. **(descriptive only, MW-7 capped) The surah-initial *lā uqsimu* doublet.** Within the
   H-NEW-2210 inventory, only **two** surahs OPEN at verse 1 with the *lā uqsimu* form: Q 75
   al-Qiyāma (`lā uqsimu bi-yawmi-l-qiyāma`) and Q 90 al-Balad (`lā uqsimu bi-hādhā al-balad`).
   This is a structural observation about opener-grammar. **The FR geometry of this pair / of the
   8-attestation uqsimu set has already been inspected during scoping**, so it is reported here as
   a DESCRIPTIVE fact only (single-test cap, no inferential verdict), per Protocol §1.7 MW-7 and
   §1.8 honesty. It is NOT one of the Bonferroni-corrected verdict cells.

---

## 2. Verdict-bearing hypothesis (LOCKED)

**H1 (Arm A, primary):** The number of corpus-exclusive roots assigned to Q 90 (roots whose unique
surah-of-occurrence is Q 90) is **greater** than expected under a length-preserving label-permutation
null.

- **Statistic** `T_obs` = number of QAC-STEM roots `r` such that the set of surahs in which `r`
  occurs equals `{90}` (i.e. `r` is a corpus surah-singleton AND that singleton surah is Q 90).
- **Direction LOCKED:** one-sided, ENRICHMENT (`T_obs` in the UPPER tail of the null). A result in
  the lower tail (Q 90 has FEWER exclusive roots than chance) = pre-commit violation → published as
  NULL with full prominence.
- **Null model (MW-2):** Take the full corpus root-occurrence stream — every QAC token that carries
  a `ROOT:` field, as an ordered list of `(surah, root)` pairs (N = 49,968 occurrences). Randomly
  permute the **surah-label column** across all occurrences (seed-locked `random.Random(20260509)`,
  Fisher-Yates shuffle of the surah vector). This **exactly preserves** (a) each surah's
  root-token count, and (b) each root's total corpus frequency; it destroys only the
  surah↔root association. Recompute `T` for Q 90 (= number of roots whose permuted occurrences all
  land in Q 90). Repeat 10,000 times.
- **p_perm** = (#{T_null ≥ T_obs} + 1) / (10000 + 1).

**H2 (Arm B, secondary verdict cell):** Q 90's corpus-exclusive-root **density** (T_obs / distinct
roots) is greater than expected under the SAME label-permutation null (density statistic, same
direction, same 10,000 permutations). This is the length-normalised companion to H1, so that a PASS
cannot be a pure surah-size artefact.

- **Direction LOCKED:** one-sided enrichment.
- **Bonferroni:** k = 2 verdict cells (H1, H2), α_bon = 0.05 / 2 = **0.025**.

---

## 3. Success / failure criteria

| Outcome | Condition |
|:--|:--|
| **CONFIRMED** | Both H1 and H2 pass at p_perm < 0.025 in the LOCKED enrichment direction, AND MW-5 replication (seed 20260530) reproduces the direction. |
| **PARTIAL / DIRECTIONAL** | Exactly one of {H1, H2} passes α_bon; or both pass raw α=0.05 but not α_bon. |
| **NULL** | Neither cell reaches raw α=0.05. |
| **PRE-COMMIT VIOLATION (NULL)** | `T_obs` falls in the LOWER tail (depletion) — published as NULL with explicit violation flag. |

## 4. MW protections

- **MW-1 (instrument-prior):** statistic, root-source (QAC v0.4 STEM `ROOT:` field), and null model
  fixed here before running.
- **MW-2 (corpus-prior):** 10,000-permutation null, label-permutation preserving both marginals.
- **MW-3 (alternative-models):** report H1 (count) AND H2 (density) — two statistics on the same null.
- **MW-4 (over-fitting):** no fitted free parameter; nothing to LOOCV.
- **MW-5 (replication):** re-run the null with a second seed (20260530); the direction and the
  pass/fail must replicate.
- **MW-6 (instrument-control):** as a within-corpus negative control, compute the same `T_obs` and
  null-rank for a length-matched short-Meccan neighbour, **Q 91 al-Shams** (15 verses, adjacent in
  the {87–93} window). If the hapax-enrichment were a generic short-Meccan artefact rather than a
  Q 90-specific signal, Q 91 would show an equally strong rank. (Reported, not verdict-bearing.)
- **MW-7 (post-hoc cap):** the *lā uqsimu* doublet FR descriptive (§1.2) is post-hoc-inspected →
  single-test α = 0.05 ceiling, NO verdict claim, descriptive only.

## 5. Locked exact values (frozen at registration)

- `T_obs` (Q 90 corpus-exclusive roots) = **4** — the roots `kbd` (kabad, "toil", 90:4),
  `njd` (najdayn, "the two highways", 90:10), `$fh` (shafatayn, "two lips", 90:9), `sgb`
  (masghaba, "hunger", 90:14). Verified from `data/morphology/quranic-corpus-morphology-0.4.txt`.
- Q 90 distinct QAC-STEM roots = **45**; root-tokens = **52**.
- Corpus root-occurrences N = **49,968**; corpus distinct roots = **1,642**; corpus surah-singleton
  roots = **459**.
- Seed = 20260509 (primary), 20260530 (MW-5 replication). n_perm = 10,000 each.

## 6. Files

- This pre-reg: `surahs/Q090-al-balad/Q090-F-01-balad-hapax-uqsimu-prereg.md`
- Script: `surahs/Q090-al-balad/scripts/Q090_F_01_balad_hapax_uqsimu.py`
- JSON output: `surahs/Q090-al-balad/csv/Q090-F-01.json`
- Findings write-up: `surahs/Q090-al-balad/06-novel-findings.md`

*Locked 2026-05-30 before the verdict-bearing permutation null was run. Bismillāh.*
