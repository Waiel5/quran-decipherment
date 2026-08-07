---
surah: 98
surah_name_ar: البينة
surah_name_translit: al-Bayyina
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q098-F-01 — Arm A title-density FALSIFIED (corrects H-NEW-1820 summary) + Arm B CONFIRMED (bariyya hapax) + Arm C CONFIRMED (corpus-UNIQUE antonym muqābala) + Arm D NULL (pre-commit violation, jadal-overlap)
seed: 20260509
n_perm: 10000
---

# Q 98 al-Bayyina — Pre-Registered Novel Findings

> **⛔ Correction 2026-08-07.** This file cites one or more of the three pillar laws that did not survive the project's first genre control. **Pillar 2 (Fisher-Rao geodesic)** and **Pillar 3 (pericope-flip / scale-of-aggregation)** are satisfied by length-matched partitions of al-Bukhārī and of pre-Islamic poetry — poetry more extremely than the Qurʾān on Pillar 2 (z = −15.13 vs −11.50) and 5/5 on Pillar 3. **Pillar 4 (title-density)** was withdrawn and replaced by `h-new-2710-title-density-retest.md`. **Pillar 1 (muqaṭṭaʿāt) stands.** The individual computations cited here are not retracted; their reading as evidence that this corpus is unusual is. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.

One pre-registered four-arm test, run with seed 20260509 and 10,000 permutations, pre-reg SHA-256 locked
before computation and verified at runtime.

- **Pre-reg:** `surahs/Q098-al-bayyina/Q098-F-01-bariyya-antithesis-prereg.md`
- **Pre-reg SHA-256:** `57eb6828a86fccaecb0a5438ad4acb671a6f8724e16d1669fede67b2d1852b41`
- **Script:** `scripts/Q098_F_01_bariyya_antithesis.py` (verifies SHA at runtime, fail-fast)
- **JSON:** `surahs/Q098-al-bayyina/csv/Q098-F-01.json`
- **Rules-tuple:** `(no-tashkeel, orthographic-token, QAC v0.4 roots, basmala-counted-only-in-Q1, Hafs-Kūfan, Mashriqi)`

**Runtime verification (2026-05-30):** `python3 scripts/Q098_F_01_bariyya_antithesis.py` →
`SHA OK: 57eb6828a86fccaecb0a5438ad4acb671a6f8724e16d1669fede67b2d1852b41`. The script reproduced the JSON
byte-for-byte. The four arms below are reported with equal NULL prominence.

---

## Q098-F-01 Arm A — title-density-EXACT FALSIFICATION (corrects H-NEW-1820 summary)

**Hypothesis (pre-committed, direction-locked FALSIFICATION consistent with the H-NEW-1820 law):** Q 98
al-Bayyina is **NOT** corpus-rank-1 in its title-root byn — neither by raw root-attestation count (A-H1)
nor by the exact eponymous surface form البينة/بينة (A-H2). The H-NEW-1820 summary-list had asserted Q 98
is in the rank-1 set; the H-NEW-1820 *law* says eponymy and density-rank-1 are independent.

**Result** (`csv/Q098-F-01.json` → `arm_A_title_density`):
- **A-H1 (raw byn count):** Q 98 = **2** attestations, raw-count rank **59/71** surahs that carry byn.
  byn top-5: Q 2 (46), Q 4 (37), Q 5 (24), Q 3 (22), Q 6 (16). **A-H1 PASS** (rank 59 ≫ 1).
- **A-H2 (exact البينة surface form):** Q 98 = **2**; **4 other surahs ≥ Q 98** — Q 11 leads with **4**
  (على بينة), then Q 6 / Q 7 / Q 8 at 2 each. **A-H2 PASS** (Q 98 is not the strict surface-form peak).
- Normalized byn-density rank = **6/71** (its 2-in-8 density is high but still not rank-1).

**Verdict: title-density-EXACT FALSIFIED.** The surah whose very name means "the clear proof" is NOT the
clear-proof word's density peak — a textbook H-NEW-1820 title-density-independence instance. The
**H-NEW-1820 summary-list entry for Q 98 is corrected**: Q 98 joins the 47/89 non-rank-1 eponymous-surah
majority. (See `05-classical-claims-audit.md` Claim 1.)

---

## Q098-F-01 Arm B — al-bariyya corpus hapax-pair (CONFIRMED)

**Hypothesis (pre-committed, deterministic):** the rhyme-word *al-bariyya* (البرية, root b-r-ʾ) occurs in
**exactly 2** corpus positions (B-H1), **both in Q 98** (v6, v7) (B-H2) — a Q 98-exclusive hapax-pair.

**Result** (`arm_B_bariyya_hapax`): البرية/برية occurs at exactly **(98,6)** and **(98,7)**, n = **2**.
**B-H1 PASS** (count = 2). **B-H2 PASS** (both in Q 98).

**Verdict: CONFIRMED — corpus-SINGLETON.** Q 98 owns the word *al-bariyya* and deploys it twice, in
immediate antithetical adjacency. This grounds the qurrāʾ/mufassirūn attention to the word's hamza/non-hamza
reading (al-Ṭabarī, al-Zamakhsharī, al-Baghawī, `03-tafsir-survey.md`): the disagreement is over a word
that appears nowhere else.

---

## Q098-F-01 Arm C — the khayr↔sharr minimal-pair muqābala (CONFIRMED, corpus-UNIQUE)

**Hypothesis (pre-committed, direction-locked, deterministic census):** among all corpus *adjacent*
faith-antithetical verse-pairs (one verse's QAC root-set intersects the faith-pole {Amn}, the other the
disbelief-pole {kfr, nfq, Srk} — the SHA-locked H-NEW-2290/2360 F1 lexicon), Q 98:6-7 is the **corpus-UNIQUE**
pair whose verse-tails align with **exactly one substituted word** over **≥3 matched trailing words**, AND
whose single pivot is the locked *khayr↔sharr* ({خير, شر}) antonym.

**Operationalization (locked in pre-reg):** read both verses' word-lists from the END; count matched
trailing words; allow EXACTLY ONE positional mismatch (the pivot) and continue; matched-tail = matched
positions excluding the pivot; a 2nd mismatch stops the scan.

**Result** (`arm_C_minimal_muqabala`):
- Adjacent faith-antithetical verse-pairs in the corpus: **219**.
- Pairs satisfying (single-substitution aligned tail) ∧ (matched-tail ≥ 3) ∧ (pivot ∈ {خير, شر}):
  **exactly 1** → **Q 98:6-7** (matched-tail = 3, pivot {شر, خير}). **C-H1 PASS.**
- Nearest non-qualifying contenders (single-substitution tail but non-antonym pivot): Q 2:102-103
  (خير/أنفسهم), Q 34:52-53 (التناوش/بالغيب), Q 63:7-8 (يعلمون/يفقهون), Q 3:176-177 (أليم/عظيم),
  Q 3:177-178 (أليم/مهين), Q 58:4-5 (أليم/مهين).

**Verdict: CONFIRMED — corpus-SINGLETON.** Q 98:6-7 is the corpus's **tightest *muqābala lafẓiyya***: the
frame *أولئك هم [X] البرية* held constant, X flipping between the two poles of moral value (*sharr* ↔
*khayr*) over a single substituted word in an aligned 3-word tail. Among 219 adjacent faith-antithetical
pairs, it is the ONLY genuine antonym minimal-pair. al-Suyūṭī's *ṭibāq/muqābala* figure (*Itqān* nawʿ 59)
has here a corpus-unique exemplar. This is Q 98's headline micro-structural finding.

---

## Q098-F-01 Arm D — content-disjointness vs length-matched null (NULL — pre-commit violation)

**Hypothesis (pre-committed, direction-locked DISJOINT; classical/Q083 prior):** the QAC-root Jaccard
J(v6, v7) is **BELOW** a length-matched random-verse-pair null (more content-disjoint than chance), with
p_lower < α = 0.05. (MW-7 transparency in the pre-reg: I had noted before locking that Q 98:6-7's Jaccard
was near-median, expected this arm to FAIL/REVERSE, and locked the DISJOINT direction as the classical
prior anyway — making any reversal a clean honest NULL.)

**Result** (`arm_D_disjointness`; seed 20260509, 10000 perms):
- **J(v6, v7) = 0.0833.** v6 roots = {$rk, $rr, Ahl, **brA**, kfr, ktb, nwr, xld}; v7 roots = {Amn, Eml,
  SlH, **brA**, xyr}. **Shared root: brA** (= *al-bariyya* — the very rhyme-word on which the antithesis
  pivots).
- null_mean = **0.0261**, null_std = 0.0492, **z = +1.163**, p_lower = **0.878** (8784 of 10000
  length-matched random pairs ≤ observed; pool_a = 2195, pool_b = 2918).
- The observed Jaccard is **ABOVE** the null mean — the pre-committed DISJOINT direction is **REVERSED**.

**Verdict: NULL (pre-commit violation, published with full prominence per PRE-REG-STANDARD-04).** Q 98:6-7
— the corpus's tightest *surface*-muqābala — is content-OVERLAPPING (not disjoint) at the root level,
because the antithesis frame is built *from* the shared root brA. The locked DISJOINT direction failed.

**What the NULL teaches (a first-class finding).** This **replicates the H-NEW-2360 jadal-overlap law at
verse-pair scale**: H-NEW-2360 found that block-scale antithetical pairs OVERLAP in content (the jadal
signature, z = +13.0 reversal of the disjoint intuition). Here, even at the *single-verse-pair* scale, and
even for the most surface-symmetric antithesis in the entire corpus, the two poles share their pivotal
root. The empirical signature of Quranic antithesis is **shared-frame overlap**, not disjoint-content
opposition — the classical muqābala "two disjoint contents against a frame" intuition is the wrong model;
the right model is "one frame, one antonym flip, maximal lexical overlap." Arm C (surface) and Arm D
(content) together show the figure is maximally tight on the surface *precisely because* it is maximally
overlapping in content.

---

## Bonferroni / family summary

Q098-F-01 has **one permutation cell** (Arm D); α_corrected = 0.05/1 = 0.05 (per the pre-reg; the
deterministic cells A, B, C do not consume α). For the Q 98 surah session this is the single landed test,
so no further cross-test correction is needed.

| Arm | Type | Result | Verdict |
|:--|:--|:--|:--|
| A (A-H1 ∧ A-H2) | deterministic | byn raw rank 59/71; surface ≤4 others | **title-density-EXACT FALSIFIED** (corrects H-NEW-1820) |
| B (B-H1 ∧ B-H2) | deterministic | البرية at (98,6),(98,7) only | **CONFIRMED — hapax-pair** |
| C (C-H1) | deterministic census | 1 of 219; = Q 98:6-7, pivot خير/شر | **CONFIRMED — corpus-UNIQUE muqābala** |
| D (D-H1) | permutation (α=0.05) | J=0.0833 > null 0.0261; z=+1.16; REVERSED | **NULL (pre-commit violation)** — jadal-overlap |

## MW protections applied

- **MW-1 (instrument-prior):** byn root key, البينة/البرية surface regex, the faith-field F1 lexicon, the
  single-substitution-aligned-tail algorithm, the {خير,شر} antonym set, and the root-Jaccard are all fixed
  in the pre-reg before any run.
- **MW-2 (corpus-prior):** Arm D used 10,000 length-matched permutations.
- **MW-3 (alternative-models):** Arm A tests BOTH raw-root-count and exact-surface-form operationalizations.
- **MW-5 (replication):** Arms A, B, C are deterministic and fully replicable from the no-tashkeel JSON +
  QAC root-index; Arm D seed-locked at 20260509 (re-run on 2026-05-30 reproduced the JSON exactly).
- **MW-6 (instrument-control):** Arm C's full 219-pair census is the non-target control set (Q 98:6-7 must
  beat every other corpus pair); Arm D's length-matched random pool is the non-target control.
- **MW-7 (post-hoc cap):** the al-bariyya hapax (B) and the khayr↔sharr minimal pair (C) were noticed during
  close reading then promoted to direction-locked pre-registered tests BEFORE computation; Arm D's near-median
  Jaccard was peeked at and disclosed, its locked direction is the classical prior (not the peeked direction),
  and Arm D is capped at single-test α = 0.05.

## Cross-finding integration

- **H-NEW-1820 (title-density independence)** — Arm A corrects the summary-list rank-1 entry for Q 98 and
  adds a new data point to the law (eponymy ⊥ density-rank-1).
- **H-NEW-2360 (antithesis = jadal-overlap, NOT disjoint-content)** — Arm D is a clean verse-pair-scale
  replication: even the corpus's tightest *surface*-muqābala (Q 98:6-7) is content-OVERLAPPING (shares brA).
- **H-NEW-2290 / F1 faith-field** — Q 98:6-7 is one of 219 adjacent faith-antithetical verse-pairs flagged
  by the Amn↔kfr field instrument; it is the unique antonym minimal-pair among them.
- **al-Suyūṭī *Itqān* nawʿ 59 (ṭibāq/muqābala)** — Arm C provides the corpus-unique exemplar of the
  verbal-antithesis figure.

## Honest limits

- Arm A's "rank-1" falsification is of a project-internal summary claim; the H-NEW-1820 law is reinforced.
- Arm C's corpus-uniqueness is on the strict locked operationalization (faith-field F1 lexicon,
  matched-tail ≥ 3, single-substitution aligned tail, {خير,شر} antonym set); a looser antonym set or a
  different antithesis lexicon would change the census.
- Arm D's NULL is a *reversal* of the locked direction, published as a violation — but it is the
  *informative* result: it shows the antithesis works by overlap, not disjunction. A surface-bigram or
  lemma-level overlap measure would shift the Jaccard magnitude but cannot flip the sign (brA is on the
  rhyme-word itself).
- The faith-field census counts a pair "antithetical" if one verse carries {Amn} and the adjacent verse
  carries {kfr,nfq,Srk}; this is a root-membership test, not a semantic-stance test, so a few of the 219
  may be thematically non-antithetical — the control set is conservative (over-inclusive), which only makes
  Q 98:6-7's uniqueness more robust.

---

*Computed 2026-05-30, seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime
(SHA 57eb6828…1852b41). Script: `scripts/Q098_F_01_bariyya_antithesis.py`; JSON: `csv/Q098-F-01.json`.*
