---
id: H-NEW-2920
title: "Pre-registration — Part 2 of the hand-built-proxy census: validating three hand-assigned quantities against computed alternatives"
date: 2026-08-08
author: Waiel Al-Shujaa
status: LOCKED — written and SHA-256'd BEFORE any agreement coefficient was computed
family: PROXY-2026-08-08
parent_rules:
  - findings/UNIT-DRIFT-DEFECT.md
  - findings/ABSENCE-CLAIMS.md
calibration: H-NEW-860.1 (rubric × formal count, ρ = +0.055 over the range where the rubric operated)
seed: 20260808
seed_replication: 20260818
n_perm: 10000
---

# Pre-registration — H-NEW-2920 Part 2

**The census (Part 1) is descriptive and is NOT pre-registered.** Enumerating which quantities
in this repository are hand-assigned requires no null and makes no inferential claim. What is
locked here is only Part 2: the three proxies selected for measurement, the formal alternative
each is measured against, the statistics, and the classification rule.

**Nothing below may be amended after the SHA-256 of this file is embedded in
`findings/phase-b-hypotheses/scripts/h-new-2920.py`.**

---

## 1. Why this test exists

H-NEW-860 published `ρ(rubric, UAS_rank) = +0.330, p = 0.050` from a hand-built 0–10 score,
substituted for a formal count because a database was wrongly believed absent. H-NEW-860.1
replaced the score with a formal count over 50,884 ḥadīth records. The published coefficient
did not reproduce; all 18 pre-registered arms carried the opposite sign; and the diagnostic
that settled it was not the re-run but the direct agreement measurement:

> **rubric × formal quotation count, restricted to the 36 surahs the rubric actually
> scored: ρ = +0.055, p = 0.752.**

Across all 114 with unscored surahs entered as zero the same rubric reaches ρ = +0.374 — an
artefact of the binary listed-versus-unlisted split. **The rubric could separate presence from
absence and could not rank.**

That is a calibration figure, not a verdict on other proxies, and this pre-registration exists
because the correct response is to measure the others rather than to assume they share the
fault. **Reporting a proxy as sound is a result of the same value as condemning one.**

---

## 2. The three proxies selected, and why these three

Selected from the Part 1 census on two criteria, both fixed before any coefficient existed:
**(a)** the proxy feeds a published correlation or a standing law rather than a description;
**(b)** a formal alternative is computable from data on disk **today**.

Proxies that fail (b) are reported in the census as NOT-YET-TESTABLE with a statement of what
would be needed. That statement is itself an absence claim and is subject to
`findings/ABSENCE-CLAIMS.md` §4.

| test | proxy | host claim | formal alternative |
|:--|:--|:--|:--|
| **T1** | H-NEW-150's **liturgical-prominence score** — hand-coded 0–17 per surah | published primary PASS, ρ = 0.3121, p_perm = 0.0002 | ḥadīth naming count per surah over the nine canonical books |
| **T2** | the **Nöldeke chronology rank** — an inherited scholarly ordering, hard-coded | H-NEW-125's 15-axis "PERVASIVE CHRONOLOGY" map; the Nöldeke block of UNIT-DRIFT §3's drift table | the **Egyptian standard** revelation order, a second independent ordering in the same file |
| **T3** | `Q036_F_01`'s **reconstructed 860 rubric** — a hand-coded approximation of a hand-built score | Q036-F-01's recitation-frequency-weighted centrality | the published H-NEW-860 rubric it claims to reproduce, and the H-NEW-860.1 formal count |

---

## 3. T1 — the liturgical-prominence score

### 3.1 The proxy, exactly as published
`findings/phase-b-hypotheses/csv/h-new-150.json` → `liturgical_scores`, 114 entries.
Defined at `findings/phase-b-hypotheses/h-new-150-liturgical-hub-prereg.md:60-71` as a weighted
sum of hand-assigned liturgical features (17 points for Q 1; 3 per prescribed occasion; 2 per
daily dhikr occasion; 1 per nightly-recitation ḥadīth; 1 for "classical-recognized
recitation-honored surah"). Its own finding, at `h-new-150-liturgical-hub.md:188-195`, states
*"Scoring is hand-coded and subjective … the scoring scheme itself … reflects my judgment about
relative liturgical weight."*

**27 of 114 surahs carry a non-zero score. That set is the proxy's operating range** and is the
range over which the primary agreement coefficient is computed, exactly as H-NEW-860.1 §5
computed the rubric's agreement over its own 36.

### 3.2 The formal alternative — LOCKED
Two instruments, both parameter-free at the primary and both already validated in H-NEW-860.1
§3 (surah-level recall 0.807; ḥadīth-to-poetry link ratio 9.9× at N = 5).

- **F1 — PRIMARY, zero free parameters.** `n_hadith_surah_level` summed per surah from
  `findings/phase-b-hypotheses/csv/h-new-860-1-reception-weights.csv`: the count of records in
  the nine canonical books containing the normalised token `سورة` + optional `ال` + the surah's
  canonical name. No alias table (H-NEW-860.1 §2.4). **This is the naming channel, which is the
  channel a liturgical prescription actually uses** — a ḥadīth prescribing a surah for a
  prayer names it rather than quoting it.
- **F2 — SECONDARY, one declared parameter.** F1 restricted to records whose **chapter title**
  matches a lexical stem list fixed here and applied by a function, never by inspection of
  which surahs it raises:
  `صلا` (ṣalāh/muṣallā), `جمع` (jumuʿa), `عيد`, `وتر`, `تهجد`, `قيام`, `أذان`, `سجود`,
  `فضائل القرآن`, `فضل القرآن`, `دعا`, `ذكر`, `تراويح`, `رمضان`.
  Matching is on the NFC-normalised, diacritic-stripped Arabic chapter title, substring, over
  the nine books' chapter indices.

**F2 is declared secondary precisely because its stem list is a hand-assignment.** Substituting
one hand-built list for another would repeat the defect under audit; F1 carries the verdict.

### 3.3 Statistics — LOCKED
1. **Agreement, operating range (PRIMARY):** Spearman ρ(liturgical_score, F1) over the **27**
   non-zero-score surahs.
2. **Agreement, full corpus:** Spearman ρ over all 114 with unscored surahs at 0.
   *Both are reported together, because H-NEW-860.1 showed the full-corpus figure is inflated by
   the presence/absence split and the operating-range figure is the honest one.*
3. **Agreement, F2:** the same two coefficients against F2.
4. **Headline re-run:** Spearman ρ(F1, cluster_degree) over 114, against H-NEW-150's published
   ρ(liturgical_score, cluster_degree) = 0.3121, with a 10,000-draw permutation p.
5. **Length control** — `findings/UNIT-DRIFT-DEFECT.md` §5, discharged in the finding:
   ρ of *every* variable in play with log surah word count, quoted beside the headline; and a
   partial Spearman of the headline re-run controlling log surah word count.
   H-NEW-150 already reports its own length-residualised arm at ρ = 0.0859, p = 0.185.

### 3.4 What T1 cannot settle, stated in advance
F1 measures **explicit canonical naming in the nine books**. It does not measure madhhab-specific
prescription, post-canonical devotional manuals, or living recitation practice. A rubric that
disagrees with F1 is not thereby refuted as a description of liturgical practice — what is
refuted is its use as a *measured quantity in a correlation*. This distinction is fixed here so
it cannot be produced later as a defence of whichever result appears.

---

## 4. T2 — the chronology rank

### 4.1 The proxy
`data/revelation-order.csv`, column `noldeke_order`, source field
*"Tanzil Egyptian Standard + Wikipedia Noldeke"*. It is not hand-built by this project; it is an
**inherited scholarly judgment, hard-coded**, and it is a category assignment whose rule is prose.
It is the ordering under which H-NEW-125 reported *"PERVASIVE CHRONOLOGY"* — 11 of 15 axes
surviving Bonferroni — and it is the ordering whose drift channels UNIT-DRIFT §3 tabulates.

### 4.2 The formal alternative, and its honest name
**There is no computable ground truth for revelation chronology**, and this pre-registration
does not pretend otherwise. What *is* computable, and what has never been computed here, is
**inter-rater agreement between the two independent orderings sitting in the same file**:
`noldeke_order` against `revelation_order` (the Egyptian standard). Two traditions, two rater
communities, one CSV.

This is a weaker test than T1 and is labelled as such. It cannot show the ordering is *correct*.
It can show whether every chronology result in this repository is **rater-dependent** — which is
the question a reader of H-NEW-125 actually needs answered, and which no finding has asked.

### 4.3 Statistics — LOCKED
1. Spearman ρ(noldeke_order, revelation_order) over 114, with the count of surahs whose two
   ranks differ by more than 20 places.
2. **The rater swap.** For each of H-NEW-125's 15 axes, recompute Spearman ρ against
   `revelation_order` using the axis values already stored in
   `findings/phase-b-hypotheses/csv/h-new-125.json` → `per_surah_axis_values`. **No axis is
   re-derived**; the published values are used verbatim, so any difference is attributable to
   the ordering alone. Report per-axis ρ under both orderings, the sign agreement, and how many
   axes cross H-NEW-125's own Bonferroni bar α = 0.00333 under each.
3. The three UNIT-DRIFT §3 drift channels (mean verse length, surah word count, verse count)
   against both orderings.

### 4.4 A limit fixed in advance
The two orderings are **not independent in provenance** — the Egyptian standard and Nöldeke's
sequence draw on an overlapping body of *asbāb al-nuzūl* reports, and the CSV's own source
string names one file for both. High agreement therefore demonstrates reproducibility across
rater communities, **not** correctness, and must not be reported as validation of chronology.

---

## 5. T3 — the reconstructed rubric

`surahs/Q036-yasin/scripts/Q036_F_01_recitation_frequency_weighted_centrality.py:59-99` builds a
114-entry weight table described in its own docstring as *"a hand-coded approximation drawn from
H-NEW-860's structure"*, covering 18 surahs and setting the other 96 to zero. H-NEW-860's
published rubric scores **36**.

This is a proxy of a proxy, and its parent is already measured as carrying no discriminative
information. **Two things are computable and neither has been checked:**

1. Spearman ρ(reconstruction, published 860 rubric) over the union of their supports, and the
   exact count of surahs where the two disagree, together with the number of the 36 the
   reconstruction drops.
2. Spearman ρ(reconstruction, H-NEW-860.1 formal count) over the reconstruction's own 18.

**No new claim about Q 36 is made or tested here.** T3 asks only whether a derived proxy
reproduces the proxy it names as its source.

---

## 6. The classification rule — LOCKED

Applied to the **operating-range** agreement coefficient (the proxy's non-zero support), because
the full-corpus figure is inflated by the presence/absence split — established in H-NEW-860.1 §5
and not re-litigated here. `ρ_op` is that coefficient; "the headline" is the host finding's
published statistic re-run with the formal quantity substituted.

```
NOISE               <- |rho_op| < 0.20  AND  the headline fails to reproduce
                       (sign flip, or loss of significance at the host's own bar)
CARRIES INFORMATION <- rho_op >= 0.60   AND  the headline reproduces, same sign,
                       still significant at the host's own bar
PARTIAL             <- anything else that is measurable
NOT-YET-TESTABLE    <- no formal alternative computable from data on disk
```

Thresholds 0.20 and 0.60 are fixed here, before any coefficient exists. The H-NEW-860.1
calibration ρ = +0.055 falls under NOISE by this rule, which is the intended anchoring and is
the only reason those particular numbers were chosen.

**Two clauses that constrain the report rather than the arithmetic:**

- **A NOISE verdict does not retire the host finding's subject matter.** It retires the
  quantity, exactly as H-NEW-860.1 retired a coefficient and not the existence of ḥadīth
  reception.
- **No verdict is upgraded on the strength of F2 or of any secondary arm.** F1 and the
  operating-range coefficient carry T1; a disagreement between arms is reported as a result
  about the instrument, and the stricter reading is taken (UNIT-DRIFT §6 step 6).

---

## 7. Run hygiene — LOCKED

- Run directory `runs/h-new-2920/<UTC timestamp>/`, created with `exist_ok=False`.
- **No file inside a run directory is ever rewritten** (UNIT-DRIFT §7). The result is written
  once, at completion. Any checkpoint goes to `scratch/h-new-2920-checkpoints/`, outside it.
- **A run directory is never deleted**, including one left empty by a crashed invocation.
- Seed 20260808; replication seed 20260818 on every permutation arm.
- The runner prints the §6 classification logic and its inputs before declaring any label.
- No finding is written to its final path before its run directory exists.

---

## 8. The garden-of-forking-paths log — what was inspected before locking

Stated so it cannot be presented later as though it had been blind.

**Inspected before this file was written:**
- The full text of H-NEW-860.1, including its ρ = +0.055 calibration and its §5 disagreement
  tables. That number is why the 0.20 threshold sits where it does.
- H-NEW-150's finding and pre-registration in full, **including its published ρ = 0.3121, its
  residual ρ = 0.0859, and its 27-non-zero-score support.** The published coefficients were
  known before T1 was designed. What was **not** computed, viewed, or estimated is any
  agreement coefficient between the liturgical score and any ḥadīth count.
- The H-NEW-150 result JSON's key list and the first ~200 characters of `liturgical_scores`
  (Q 1 = 17 … Q 114 = 3) — enough to establish the field exists and its scale.
- `data/revelation-order.csv` header and first three rows; the existence of both
  `revelation_order` and `noldeke_order` columns. **ρ between them was not computed.**
- H-NEW-125's per-axis published ρ values against Nöldeke rank, and its axis list. The
  Egyptian-standard recomputation was not run.
- `Q036_F_01_recitation_frequency_weighted_centrality.py:50-99` in full.
- The ḥadīth corpus schema: `metadata`, `chapters`, `hadiths`, and al-Bukhārī's first 20 chapter
  titles. **The chapter-title stem list in §3.2 was written from those 20 titles and from the
  liturgical vocabulary named in H-NEW-150's own scoring scheme — not from any count.**

**Not inspected:** any per-surah value of `n_hadith_surah_level`; any coefficient of any kind
between a proxy and a formal quantity; the Q036-F-01 finding's results.

---

## 9. Limits known in advance

1. **T1's F1 inherits every limit of H-NEW-860.1's naming instrument** — no alias table, so
   `فاتحة الكتاب`, `أم الكتاب`, `المعوذتان`, `براءة` are uncounted; 159 naming events by that
   finding's own §10.2 measurement. **Q 1 is the largest single loser**, and Q 1 is also the
   surah the rubric scores 17. This is declared now because it is a foreseeable defence of
   whichever result appears, and it cuts in a known direction: it depresses F1 for Q 1
   specifically.
2. **T2 cannot validate chronology** (§4.4) and its two orderings share provenance.
3. **T3 makes no claim about Q 36.**
4. **The census is not exhaustive.** A sweep by detection cue finds quantities that *declare*
   themselves hand-assigned. A hand-assignment that is never described as one is invisible to
   it, and the census must say so rather than imply coverage — this is UNIT-DRIFT §8's lesson
   applied to a different screen.
5. **Three proxies is a deliberate floor, not a ceiling.** The census names every candidate it
   found and states which were not reached, so the next session picks up there rather than
   re-deriving the list.

---

*Locked 2026-08-08 by Waiel Al-Shujaa before any agreement coefficient existed.
A hand-assigned quantity is a measurement claim, and a measurement claim that has never been
compared to a measurement is an assertion. Bismillāhi al-Raḥmāni al-Raḥīm.*
