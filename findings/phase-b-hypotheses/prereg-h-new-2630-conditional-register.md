---
id: H-NEW-2630
title: Realis vs irrealis conditionals as the fourth register column of the discourse-grammar law
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED-BEFORE-COMPUTATION
family: COND-2026-08-07-A
parent: cross-finding-028-formal (register-coded discourse grammar)
reuses: H-NEW-2530 (feature vector + genre proxy), H-NEW-2500 (genre labels)
disjoint_from: H-NEW-2250 (idhā cascade — different lemma, see §2.4)
seed: 20260509
seed_replication: 20260519
n_permutations: 10000
tests_in_family: 5
alpha_bonferroni: 0.01
---

# PRE-REGISTRATION — H-NEW-2630

**Written and SHA-locked before any conditional density, contrast, or classifier
accuracy was computed.** What *was* computed before locking, and is therefore
reported here as an input rather than a result: the QAC part-of-speech and lemma
inventory of §2 (counts of tagged segments), and the SHA-256 of each frozen input.
These are corpus-description facts needed to *define* the populations; none of them
is a per-register quantity, a density, a contrast, or a test statistic.

---

## 1. The claim

The classical *sharṭ* (protasis) / *jazāʾ* (apodosis) apparatus distinguishes an
**open/realis** condition — *in* (إن), "if you do X (and you may)" — from a
**counterfactual/irrealis** condition — *law* (لو) and *lawlā* (لولا), "had X been
so (but it was not)."

cross-finding-028-formal codes Quranic register on four feature families: qaṣaṣ
onset particles, the *idhā* cascade, *thumma*-led doubling, and person-iltifāt
balance. **It carries no conditional feature at all.** H-NEW-2630 asks whether the
realis/irrealis contrast is a fifth, independent grammatical carrier of register.

**Substantive hypothesis.** Legislation is prospective and its conditions are
genuinely open — *in* is the particle of a rule that may or may not be triggered.
Polemic and eschatological warning argue from what did *not* happen or cannot happen
— *law* is the particle of rebuke ("had there been gods besides God, the heavens
would have collapsed") and of the unrealised. Therefore *in* should concentrate in
legal-Medinan discourse and *law*/*lawlā* outside it.

---

## 2. Populations — exact QAC feature strings

Source: `data/morphology/quranic-corpus-morphology-0.4.txt`
(SHA-256 `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`).

A segment qualifies only if **field 3 (the POS tag column) is exactly `COND`** and
its **`LEM:` value in field 4** is in the set below. No substring matching on the
Arabic or Buckwalter form is performed anywhere in this test.

### 2.1 REALIS set (primary)

| LEM | Arabic | tagged COND |
|---|---|---:|
| `<in` | إنْ | 578 |

### 2.2 IRREALIS set (primary)

| LEM | Arabic | tagged COND |
|---|---|---:|
| `law` | لو | 185 |
| `lawolaA^` | لولا | 35 |
| | | **220** |

### 2.3 Why the POS tag is load-bearing (the disambiguation the test depends on)

Measured from the frozen QAC file before locking:

| LEM | COND | other tags | substring hits on the form |
|---|---:|---|---:|
| `<in` | 578 | NEG 114, CERT 5 | **2,396** |
| `law` | 185 | SUB 16 (*wadda law* "wished that") | **339** |
| `lawolaA^` | 35 | **EXH 40** (*"why not…?"*) | — |

Naive substring counting would inflate إن by **4.1×** and لو by **1.8×**, and would
merge لولا with an exhortative use that is the *majority* of its attestations
(40 of 75). The claim under test is not detectable without lemma+POS disambiguation.
This is recorded here as the methodological precondition, not as a finding.

### 2.4 Excluded, and why (locked)

- **`<i*aA` (إذا)** — 405 tagged `T`, 3 `SUR`, **1 `COND`**. *idhā* is H-NEW-2250's
  object and is a different lemma. The single COND-tagged token is excluded so the
  two lines stay strictly disjoint.
- **Generalising / relative conditionals** — `man` (184), `maA` (23), `{l~a*iY` (22),
  `>am~aA` (11), `>ayon` (3), `Hayov2` (2), `mahomaA` (1), `>aY~` (1). These are
  *conditional relatives* ("whoever", "whatever", "wherever"); their realis/irrealis
  status is not lexically determined, so they cannot be scored on the axis under
  test. They are retained for the MW-6 control of §6.4.
- **`<iyn` (1), `<im~aA` (1), `<il~am` (1)** — morphologically *in*-based but
  vanishingly rare. Excluded from the primary; added back in the tuple-C sensitivity
  arm (§7) purely to demonstrate insensitivity.

Primary populations therefore total **798** of the 1,049 `COND` segments.

---

## 3. Register labels — reused verbatim, not re-derived

The register label for each surah is read from
`findings/phase-b-hypotheses/csv/h-new-2500.json` → `genre_proxy.surah_genre`
(SHA-256 `a63aef25086205891b44215897f9e09862e5cdd1e3ab2ee59ac4d15768309d25`).

This is the same source H-NEW-2530 declares: its
`genre_proxy_source` field reads *"h-new-2500.json genre_proxy.surah_genre (reused
verbatim)"*. `h-new-2530.json` itself stores only the marginals, not the per-surah
labels, so 2500 is the canonical location.

**Runtime assertion (fail-fast):** the label marginals must reproduce
`h-new-2530.json` → `n_per_genre` **exactly**:
`narrative 31 / legal_medinan 20 / eschatological_mufassal 40 / liturgical_didactic 23`.
Mismatch ⇒ `SystemExit`.

- **Primary analysis:** the 3-register set, N = 91, exactly as H-NEW-2530's primary.
- **MW-3 robustness:** 4-class, N = 114.

---

## 4. Statistics

Let `n_R(s)`, `n_I(s)` be realis and irrealis counts in surah `s`; `V(s)` the
Ḥafṣ-Kūfan verse count from `data/hafs-verse-counts.tsv`
(SHA-256 `e1818fb04ac26b863ce1ade50193390d481345a3971919aeb120daf8946212ba`);
`T(s)` the QAC segment count.

- `d_R(s) = n_R(s) / V(s)` — realis density (per-verse, matching H-NEW-2530's `/V`)
- `d_I(s) = n_I(s) / V(s)` — irrealis density
- **`C(s) = (n_R(s) − n_I(s)) / (n_R(s) + n_I(s))`** — the **conditional-mood
  balance**, defined only where `n_R + n_I ≥ 1`.

`C(s)` is deliberately constructed to mirror H-NEW-2530's `f_iltifat_type`
(`(n31 − n23)/(n31 + n23)`) so it slots into the same vector on the same scale.
Surahs with no conditional at all are **undefined**, not zero, and are dropped from
`C`-based cells; their count is reported.

---

## 5. Hypotheses — directions LOCKED

Five registered inferences. **Bonferroni k = 5, α_bon = 0.01.** Every null is a
class-size-preserving label shuffle over the register labels, 10,000 permutations,
seed 20260509; the identical pipeline is recomputed on each shuffle.

| # | Hypothesis | Statistic | LOCKED direction |
|---|---|---|---|
| **H1** | Realis concentrates in legal | `mean d_R(legal) − mean d_R(rest)` | **> 0** |
| **H2** | Irrealis avoids legal | `mean d_I(legal) − mean d_I(rest)` | **< 0** |
| **H3** | Balance separates the registers | Kruskal-Wallis `H` on `C(s)` across the 3 registers, **plus** the locked ordering that legal_medinan has the highest mean `C` | `H` large **and** legal highest |
| **H4** | The effect survives length control | H3 re-run on `C(s)` residualised on `log V(s)` and `log T(s)` (OLS, residuals taken) | same as H3 |
| **H5** | It repairs the soft boundary | legal-Medinan LOO recall in the H-NEW-2530 nearest-centroid classifier, 6 features vs 6+conditional | **> 8/20** |

### 5.1 Failure criteria, stated in advance

- A **reversed** sign on H1, H2, or the H3/H4 ordering is a **pre-commit violation**,
  published as NULL with full prominence, never re-described as a discovery.
- **H4 is the load-bearing cell.** The legal register lives in long surahs, and
  H-NEW-2530's own confusion matrix shows legal is its hardest class (8/20).
  **If H1–H3 pass and H4 fails, the verdict for the whole test is NULL-LENGTH-CONFOUNDED**
  and no amendment to cross-finding-028-formal will be proposed. Passing three
  uncontrolled cells does not buy a law.
- H5 failing while H1–H4 pass ⇒ verdict `PASS-NO-CLASSIFIER-GAIN`: the contrast is
  real but does not repair the legal↔eschatological boundary. That is an informative
  negative and will be reported as such.

---

## 6. MW protections

- **MW-1 (length residualisation)** — H4, and `d_R`/`d_I` reported raw *and*
  length-residualised.
- **MW-2 (permutation null)** — 10,000 class-size-preserving label shuffles per cell.
- **MW-3 (alternative models)** — (a) per-verse `/V(s)` vs per-token `/T(s)`
  normalisation; (b) 3-register vs 4-class; (c) Gaussian naïve-Bayes alongside
  nearest-centroid for H5.
- **MW-5 (replication)** — full rerun at seed 20260519.
- **MW-6 (instrument control)** — three fail-fast runtime assertions plus one
  substantive control:
  1. `POS:COND` total == 1049
  2. lemma marginals == the §2 table exactly
  3. genre marginals == `h-new-2530.json` `n_per_genre`
  4. **Substantive control (§6.4):** the identical H3 pipeline is run on the
     *excluded generalising conditionals* (`man`, `maA`). If those separate the
     registers as strongly as the realis/irrealis axis, then the effect is
     "conditionals cluster by register", not "**mood** is register-coded", and the
     specific claim is not supported. Locked expectation: the generalising set
     separates **more weakly** than `C(s)`.
- **MW-7 (post-hoc cap)** — no post-hoc cell is promoted. Anything noticed after
  unblinding is labelled EXPLORATORY and capped at α = 0.05 single-test.

---

## 7. Rules-tuple discipline

Primary tuple **A**:
`(QAC v0.4 POS:COND + LEM exact-match, per-verse density /V(s), Ḥafṣ-Kūfan,
basmala-counted-only-in-Q1, Mashriqi, 3-register H-NEW-2500 proxy)`

Required variants:
- **B** — per-QAC-token density `/T(s)` instead of `/V(s)`.
- **C** — REALIS set widened to `{<in, <iyn, <im~aA, <il~am}`.

A claim is `RULES-TUPLE-STABLE` only if the H3 and H4 verdicts agree across A, B, C.

---

## 8. Classical anchoring — verification status stated honestly

- **al-Zarkashī, *al-Burhān fī ʿulūm al-Qurʾān*** — the *sharṭ*/*jazāʾ* apparatus.
  **NOT VERIFIABLE ON DISK.** The file
  `data/literature/classical-tafsir/zarkashi-al-burhan-fi-ulum-al-quran.pdf`
  is a 1,568-page **image-only scan with no text layer**: `pdftotext` returns 0
  bytes and `pypdf.extract_text()` returns 0 characters on every sampled page
  (0, 5, 50, 200, 400). **No passage from al-Zarkashī is cited in this test.**
  The framing above is stated as the project's own working hypothesis, not as his.
- **al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*** (English translation on disk,
  `data/literature/classical-tafsir/suyuti-al-itqan-fi-ulum-al-quran-english.pdf`,
  extractable text layer) — **VERIFIED at two loci**:
  1. Under *al-Muzāwaja* (coupling): *"Here, two meanings are coupled in the
     conditional phrase and its apodosis"* — the *sharṭ*/*jazāʾ* pair as a
     rhetorical unit.
  2. On the ellipsis of the object of a *shāʾa*-phrase, citing al-Zamlakānī and
     al-Tanūkhī (*al-Aqṣā al-qarīb*): *"If the accusative after the particle 'lau'
     is omitted, it is always mentioned in its apodosis"*, illustrated with
     Q 41:14 *qālū law shāʾa rabbunā la-anzala malāʾikatan*, glossed *"If our
     Sustainer sought to send down messengers, He would surely have sent down
     angels"* — an explicitly **counterfactual** reading of *law*.
  **MW-6 nawʿ-number tag: UNVERIFIED.** The extraction does not expose nawʿ
  numbering at these loci, so no nawʿ number is asserted.

---

## 9. Outputs

- Script `findings/phase-b-hypotheses/scripts/h-new-2630.py`, with this file's
  SHA-256 embedded as a literal and verified at runtime (`SystemExit` on mismatch).
- Immutable run directory
  `findings/phase-b-hypotheses/runs/h-new-2630/<UTC-ISO8601>/` containing
  `result.json` and `manifest.json`. **Run directories are never deleted**, including
  superseded ones; a superseded run is retained and annotated.
- Findings file `findings/phase-b-hypotheses/h-new-2630-conditional-register.md`.

---

*Locked before computation by Waiel Al-Shujaa, 2026-08-07. Bismillāhi al-Raḥmāni al-Raḥīm.*
