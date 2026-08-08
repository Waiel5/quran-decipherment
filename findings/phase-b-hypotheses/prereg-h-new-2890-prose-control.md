---
id: H-NEW-2890
title: "Pre-registration — the vocalised-prose negative control that H-NEW-2870 and H-NEW-2880 could not run"
date: 2026-08-07
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any rhyme class, agreement, delta or null draw was computed on any prose text
family: RHYME-2026-08-07
frontier_item: F-16
parent_1: H-NEW-2880 (PASS; its §5.2 reports this control as NOT COMPUTABLE)
parent_2: H-NEW-2870 (NULL; its §6.2 and §13.1 name the missing prose delta as the single biggest limitation)
seed: 20260509
seed_replication: 20260519
n_perm: 10000
bonferroni_k: 36
alpha_bonferroni: 0.00138889
---

# Pre-registration — H-NEW-2890

**Nothing here may be amended after the SHA-256 is embedded in `scripts/h-new-2890.py`.**
Acquisition criteria and thresholds are locked in §3, the two arms in §5, the directions and
the falsification thresholds in §7, the decision rules in §8. **The runner's verdict logic will
be diffed against §8 and printed before any verdict is declared.**

---

## 1. The question, and why it is the one most likely to damage my own finding

H-NEW-2880 concluded that the Qurʾān's verse-endings are organised at **pausal** phonology, on
the strength of a null whose chance floor has exactly zero variance. Its §5.2 reports the
negative control as **NOT COMPUTABLE** because no vocalised Arabic prose was found on disk.

**That leaves the finding one control short, and the missing control is the obvious sceptical
move:** *perhaps any vocalised Arabic text gains rhyme agreement under pausal reduction, in
which case the effect is a property of the language and not of this text.* The within-corpus
re-cut control (z = +70.7) addresses a different question — whether the gain is a property of
*where the boundaries are* — and does not answer this one.

**This pre-registration is written to give that sceptical hypothesis its best chance.** The
falsification thresholds in §7 are set before any prose rhyme number exists, and if they are
crossed I am obliged by §8 to report H-NEW-2880 as materially damaged and to amend it.

---

## 2. The acquisition — and a defect in my own two parent findings

**No download was required. The corpus was already on disk and both parents missed it.**

H-NEW-2870 §6.2 and H-NEW-2880 §5.2 each ran a vocalisation census and concluded no vocalised
prose existed. **Both censuses enumerated `data/baseline-corpora/` only.** A repository-wide
census run for this test found `data/literature/hadith/ahmedbaset-json/`, committed 2026-04-28:
50,884 ḥadīth across nine canonical books, **fully vocalised**, at ḥarakāt densities of
0.7702–0.8829 against the Qurʾān's own **0.7801**.

**This is a defect in H-NEW-2880 — my own finding — and it is recorded as such.** The claim
"no vocalised prose exists on disk" was false; the true statement was "no vocalised prose exists
*in `data/baseline-corpora/`*". The unvocalised prose files in that directory are genuinely
unvocalised (0 ḥarakāt), so nothing computed from them is affected; what is affected is the
conclusion that the control could not be run. It could.

Source, licence, SHA-256 and full vocalisation measurements:
`data/literature/hadith/VOCALISED-HADITH-SOURCE.md`. **The licence is not stated upstream and
is not asserted; the corpus is treated as research-use-only and is not redistributed.**

---

## 3. Admissibility screens — thresholds inherited, not chosen

### 3.1 Screen 1 — vocalisation. Threshold **inherited verbatim** from H-NEW-2870 §6.4.

> **A text is admissible only if its rate of unit-final vocalisation is ≥ 0.90** — i.e. at least
> 90 % of unit-final words carry a written case vowel, tanwīn, or a long vowel / indeclinable
> ending from which the waṣl form is recoverable.

This is the same threshold, on the same quantity, that H-NEW-2870 pre-declared to select its
three muʿallaqāt from seven. It is inherited rather than invented, and it predates this test.

**Measured before locking, and declared here in full so the threshold can be seen to do no
selection work:** all nine books clear it — al-Bukhārī 0.9426, Muslim 0.9405, Abū Dāwūd 0.9505,
al-Tirmidhī 0.9887, al-Nasāʾī 0.9511, Ibn Mājah 0.9484, Mālik 0.9457, Aḥmad 0.9512, al-Dārimī
0.9445; the Qurʾān 0.9843. **All nine are reported regardless of the primary designation.**
A threshold of 0.95 would have excluded al-Bukhārī — which is precisely why the threshold is
taken from the parent rather than set here.

### 3.2 Screen 2 — per-unit readability, as the parent applied it to poetry

H-NEW-2870's REPAIR-2 restricts the poetry arm to **readable pairs** — both units' rime regions
readable off the text. The identical restriction is applied here, and both the unrestricted and
readable-only arms are reported. Readability is measured on the **input**, never on a result.

### 3.3 Primary text — **inherited, not selected on these numbers**

> **Primary: Ṣaḥīḥ al-Bukhārī. Replication: Ṣaḥīḥ Muslim.**

al-Bukhārī is the negative control already named in H-NEW-2870 §3 and §6.5 and in H-NEW-2880
§5.2. It is carried over so that the text under test is fixed by the parents' choice and not by
anything measured here. All nine books are reported.

---

## 4. The instrument — H-NEW-2880's, unmodified and SHA-pinned

The phonemiser, the four conventions (C, P1, P2, P3), both rime extractors (R1, R2), the
readability criterion and the exact zero-variance-floor null are taken **unchanged** from
`scripts/h-new-2880.py`, which itself pins `scripts/h-new-2870.py`. Both are SHA-256 verified at
runtime. **No parameter of the instrument may be re-tuned for prose.** Rime definition **R2** is
primary, as in the parent; R1 is reported.

**Frozen inputs (SHA-256 verified at runtime; mismatch is fatal):** the two parent runners, the
Qurʾān text, and the two ḥadīth books —
`bukhari.json` `9d2e4194786c275f64f627c834711ea0e339a8fe226d5e9569ef962595a562f1`,
`muslim.json` `12e3cbe8e2c83acc787b3e1e644877eff0feab11f1b32493386c60703d9076ae`.

---

## 5. The two arms — because unit length and composed boundaries cannot both be held fixed

Prose units are **5.9× longer** than Qurʾānic verses (al-Bukhārī 73.2 words against 12.4).
Holding length fixed destroys the composed boundaries; keeping the composed boundaries leaves
length unmatched. **Both arms are therefore run, and the comparison target for each is locked
here so it cannot be chosen after the fact.**

### 5.1 Arm B — composed boundaries. **PRIMARY.**

- **Unit** = one ḥadīth (a complete report — where the compiler chose to stop, and where a
  reciter would perform *waqf*). **Block** = one chapter. Adjacent within-chapter pairs.
- **Locked comparison target: the Qurʾān's own Δ(P1) = +0.1869** (composed boundary against
  composed boundary).

### 5.2 Arm A — length-matched cuts.

- The parent's own construction: concatenate the prose word stream and cut it to the Qurʾān's
  per-surah verse-length profile, 200 cuts, seed 20260509.
- **Locked comparison target: the Qurʾān's own pseudo-fāṣila re-cut Δ = +0.0284**, not its true
  Δ. Arbitrary cuts destroy real boundaries, so the like-for-like comparison for an arbitrary
  cut is another arbitrary cut. (`STATE-OF-THE-PROJECT-2026-08-07.md` §4.7 — a partition is not
  a composed book, and this statistic is boundary-sensitive.)

### 5.3 Qurʾānic contamination — three settings, conclusion required under **all three**

Ḥadīth quotes the Qurʾān. Measured share of reports containing at least one Qurʾānic word
n-gram on the unvocalised skeleton: al-Bukhārī **22.5 %** (trigram) and **4.0 %** (5-gram).

| tag | rule | role |
|:--|:--|:--|
| **S5** | drop any unit sharing a Qurʾānic **5-gram** | **primary** |
| S3 | drop any unit sharing a Qurʾānic **trigram** — the repository's own convention (`data/baseline-corpora/strip_quran_quotes.py`, `data/SOURCES.md` §5.6) | required |
| S0 | **no stripping** | required |

**S0 is retained deliberately because it is the setting least favourable to my hypothesis** —
it leaves Qurʾānic material inside the control and can only push prose's delta *up*, toward the
Qurʾān's. If the conclusion survives S0 it does not depend on the stripping rule.

---

## 6. Statistics

As in H-NEW-2880, unchanged: **Δ = A(P) − A(C)**, and **E = A − Σpᵢ²** against the exact
zero-variance-floor null (construction S2 primary, exactness gate G1 enforced — every draw's
block-size multiset identical to the observed, hence its chance floor identical to the last
bit). Prose is tested against **its own** observed class-size profile, not the Qurʾān's.

The gates G1 (exactness) and G3 (non-degeneracy) from H-NEW-2880 §6 are re-applied to every
prose null. **If the prose pausal partition is not a coarsening of its citation partition, the
exact null is undefined for it and must be reported as such rather than run.**

---

## 7. Directions and falsification thresholds — LOCKED BEFORE ANY PROSE RHYME NUMBER

| # | direction | locked prediction |
|:--|:--|:--|
| **D-P1** | Δ_prose(Arm B) < Δ_Qurʾān = +0.1869 | ordinary vocalised prose gains substantially less |
| **D-P2** | Δ_prose(Arm A) ≈ or < Δ_Qurʾān(re-cut) = +0.0284 | arbitrary cuts of prose behave like arbitrary cuts of the Qurʾān |
| **D-P3** | prose's standardised excess against its own exact null is far below the Qurʾān's z = +15.03 | reported; see the caveat below |

**The word "comparably" in this test's brief is given a number here, before the data:**

| outcome on Δ_prose (Arm B, P1, rime R2, setting S5) | consequence, locked |
|:--|:--|
| **Δ_prose ≥ +0.09345** (≥ 0.5 × the Qurʾān's) | **PROSE GAINS COMPARABLY — H-NEW-2880's interpretation is materially damaged.** Report at full prominence, and write an amendment notice into H-NEW-2880 stating that the effect is not shown to be specific to this text |
| +0.04672 ≤ Δ_prose < +0.09345 (0.25×–0.5×) | **PARTIAL DAMAGE** — H-NEW-2880's honest limits must be amended to state that prose recovers between a quarter and a half of the effect |
| Δ_prose < +0.04672 (< 0.25×) | **THE CONTROL BEHAVES** — the effect is not a general property of vocalised Arabic |

**Caveat on D-P3, stated now so it is not reached for later:** z depends on sample size and on
the null's dispersion, so z is **not** comparable across corpora of different size and class
structure. **Δ is the primary comparison; z is secondary and descriptive.** A prose z that is
large in absolute terms is *not* by itself evidence against H-NEW-2880 — prose isnād chains
repeat proper names locally, so some excess over a random regrouping is expected in any Arabic
prose. What would damage H-NEW-2880 is a large prose **Δ**, and that is what §7's grid gates on.

---

## 8. Decision rules

**Registered inference family — 36 tests:** {D-P1 Arm B, D-P2 Arm A, D-P3 own-null} ×
{al-Bukhārī, Muslim} × {P1, P2} × {S5, S3, S0} = 3 × 2 × 2 × 3 = 36.
**Bonferroni k = 36, α = 0.05/36 = 0.00138889**, one-sided in the locked direction.
Resolution 1/10,001 = 0.0001 < α ✔.

- **D-P1** and **D-P2** are tested by 10,000-permutation label exchange on the pooled adjacent
  pair set, the same machinery H-NEW-2870/2880 used for D4b.
- **D-P3** is the prose E against prose's own exact null.

**Verdict grid, locked:**

| outcome | verdict |
|:--|:--|
| no admissible text clears §3.1 | **CONTROL UNAVAILABLE** — report that the corpus does not exist in usable form; this is a legitimate result |
| Δ_prose(Arm B) ≥ +0.09345 under **any** of S5/S3/S0 | **H-NEW-2880 DAMAGED — prose gains comparably.** Leads the write-up regardless of everything else, and an amendment notice is written into H-NEW-2880 |
| +0.04672 ≤ Δ_prose < +0.09345 under any setting | **PARTIAL — amend H-NEW-2880's honest limits** |
| Δ_prose < +0.04672 under all three settings **and** D-P1 passes at α for both texts and both tuples | **CONTROL PASSES — H-NEW-2880's interpretation survives its hardest test** |
| Δ_prose < +0.04672 but D-P1 fails at α | **INCONCLUSIVE** — report the effect sizes and the failure |

**The verdict is taken on the WORST setting across S5/S3/S0, not the best.** All nine books,
both rime definitions, both arms, and the readable-only restriction are reported.

**The runner's verdict logic will be diffed against this section, printed, before any verdict is
declared.**

---

## 9. Reporting order — LOCKED

1. The acquisition, the licence position, and **the census defect in H-NEW-2870/2880**.
2. Vocalisation measurements for all nine books beside the Qurʾān, and the contamination rates.
3. The class-collapse magnitude for prose — K, K_eff, chance floor — **before any delta**, as
   the parents did.
4. **Arm B's Δ_prose against the locked +0.1869**, then Arm A's against the locked +0.0284.
5. The exact-null result for prose, with its gates.
6. The verdict against §7's grid, and any amendment owed to H-NEW-2880.

---

## 10. Garden of forking paths — everything inspected before locking

1. Read `STATE-OF-THE-PROJECT-2026-08-07.md`, `findings/UNIT-DRIFT-DEFECT.md`, H-NEW-2870,
   H-NEW-2880 and their pre-registrations and runners.
2. **Repository-wide ḥarakāt census** of every text file under `data/` carrying ≥ 50,000 Arabic
   characters (452 files). This produced the acquisition in §2 and the defect notice.
3. **Vocalisation and unit-final mark census** of all nine ḥadīth books and the Qurʾān (§3.1),
   plus mean unit length and the unit-final word-type distribution. **Encoding facts. No rhyme
   class, agreement, delta or null draw has been computed on any prose text.**
4. **Qurʾānic n-gram contamination rates** at n = 3, 4, 5 (§5.3). A text-overlap fact.
5. **Formulaic-ending census**, measured because it bears on interpretation and could favour
   prose: the top-10 unit-final word types cover **8.1 %** of al-Bukhārī's reports and **12.9 %**
   of Muslim's, against **7.6 %** of the Qurʾān's verses. **Prose is at least as formulaic at
   unit-final position as the Qurʾān is**, so this channel does not disadvantage the control.
6. Every threshold in §3 and §7 was fixed **after** these encoding measurements and **before**
   any rhyme statistic. The §3.1 threshold is inherited verbatim from the parent; the §7
   thresholds are round fractions (0.5×, 0.25×) of the parent's published Δ.
7. The comparison targets in §5.1 and §5.2 are the parents' **published** values (+0.1869 and
   +0.0284), fixed here so the target cannot be chosen after seeing the prose result.

---

## 11. Failure conditions — what makes this finding wrong

- **No text clears §3.1** → CONTROL UNAVAILABLE; report it.
- **The prose pausal partition is not a coarsening of its citation partition** → the exact null
  is undefined for prose and must be reported as such, not run (H-NEW-2880 §4.1's condition).
- **G1 or G3 fails on any prose null** → that null is defective; report no p-value from it.
- **Δ_prose ≥ +0.09345** → H-NEW-2880 is damaged; report it at full prominence and amend it.
- **Residual limits that no available data can remove:** the ḥadīth honorific formulae are
  written unvocalised in this edition, and unit-final sukūn is 5.7 % against the Qurʾān's 1.6 %,
  so a small share of prose units have no recoverable citation form and are excluded by Screen 2;
  the licence position upstream is unstated; Musnad Aḥmad is partial; and a ḥadīth is a
  different *kind* of composed unit from a verse, so Arm B compares composed boundaries of two
  genres, which is the point but is not a matched design.

---

## 12. Run discipline

Immutable run directory `runs/h-new-2890/<UTC>/`, `os.makedirs(..., exist_ok=False)`, every
output opened with mode `'x'`, manifest paths repo-relative, **checkpoints written OUTSIDE the
run directory**. **No run directory is ever deleted.** This pre-registration's SHA-256 is
embedded as a literal in the runner and verified at runtime; all frozen inputs SHA-256 verified.
Every permutation test replicated at seed 20260519.

*Bismillāhi al-Raḥmāni al-Raḥīm.*
