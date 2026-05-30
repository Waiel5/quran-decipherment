---
surah: 84
surah_name_ar: الإنشقاق
surah_name_translit: al-Inshiqāq
file_type: novel-findings
date_last_updated: 2026-05-30
phase: B+
verdict: Q084-F-01 CONFIRMED (corpus-unique biplex marker) + Q084-F-02 CONFIRMED (k-d-ḥ corpus-EXACT) + Q084-F-03 NULL (pre-commit violation — book-hand antithesis built by lexical disjunction)
seed: 20260509
n_perm: 10000
---

# Q 84 al-Inshiqāq — Pre-Registered Novel Findings

Three pre-registered tests. Two are deterministic corpus-exact counts (F-01, F-02); one is a
permutation test with seed 20260509 / 10,000 perms, SHA-256-locked before computation and verified
at runtime (F-03). All three scripts were re-run to reproduce their JSON outputs for this writeup.

- **Pre-regs:** `preregs/Q084-F-0{1,2,3}-*.md`
- **Scripts:** `scripts/Q084_F_0{1,2,3}_*.py`
- **JSON:** `csv/Q084-F-0{1,2,3}.json`
- **Rules-tuple (F-01/F-02):** `(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`
- **Rules-tuple (F-03):** `(no-tashkeel, QAC-v0.4 ROOT, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)`

---

## Q084-F-01 — the corpus-UNIQUE biplex marker (CONFIRMED)

**Hypothesis (pre-committed):** Q 84 is the corpus's UNIQUE surah that is simultaneously (a) an
*idhā*-cosmic-event-opener (member of the 5-surah H-NEW-1200 Sub-cluster A: {Q 56, 81, 82, 84, 99}) AND
(b) a *sajdat al-tilāwa* surah (member of the 14-surah classical Sunnī set per H-NEW-1330: {Q 7, 13, 16,
17, 19, 22, 25, 27, 32, 38, 41, 53, 84, 96}). Direction-lock: |idhā ∩ sajda| = 1, with 84 ∈ I.

**Result (`csv/Q084-F-01.json`, script re-run):**
- Intersection I = {idhā-openers} ∩ {sajda-surahs} = **{84}**, |I| = **1**.
- Q 84:1 opens *idhā al-samāʾu inshaqqat* (the *idhā al-samāʾu V* cosmic pattern) — confirmed on disk.
- Q 84:21 carries the sajda glyph **۩** (*wa-idhā quriʾa ʿalayhim al-Qurʾānu lā yasjudūn* ۩) — confirmed.
- No other *idhā*-opener carries a sajda glyph; no other sajda-surah opens with *idhā*-cosmic-event.

**Verdict: CONFIRMED (deterministic).** Q 84 is the corpus's SOLE biplex-marker surah, bridging the
eschatological-content axis (*idhā*-opener — an FR-cohesive cluster, H-NEW-1200) and the
liturgical-prostration axis (sajda — a LOCAL marker that is NOT FR-cohesive at surah scale,
H-NEW-1330). The two LOCKED classical sets intersect in exactly one surah. This is a clean corpus fact:
the intersection of two independently-defined classical-tradition sets is the singleton {84}.

**Honest limit.** Both input sets are classical-tradition closed lists (the 5-surah *idhā* cluster from
H-NEW-1200; the 14-surah Sunnī sajda list — the Shīʿī/Ḥanafī sajda counts differ, e.g. some lists give
15 by adding Q 22's second sajda, or drop Q 38). Under the 15-verse list, the intersection is unchanged
(the added verses are not *idhā*-openers), so the singleton is robust to the main sajda-list variant.

---

## Q084-F-02 — root k-d-ḥ corpus-EXACT to Q 84:6 (CONFIRMED)

**Hypothesis (pre-committed):** the root k-d-ḥ (toil/exert/scratch) is corpus-RARE; Q 84:6 (*innaka
kādiḥun ilā rabbika kadḥan fa-mulāqīh*) contains ALL its corpus tokens. Direction-lock: ≤2 tokens, in
exactly 1 verse (Q 84:6).

**Result (`csv/Q084-F-02.json`, script re-run):**
- Total corpus surface-form hits of k-d-ḥ: **2** — *kādiḥ* (active participle) + *kadḥ* (verbal noun).
- Distinct verses: **1** — exactly Q 84:6.
- Both forms sit in the *mafʿūl-muṭlaq* construction (*kādiḥun … kadḥan*), corpus-EXACT bigram.

**Verdict: CONFIRMED — corpus-SINGLETON.** Q 84:6 is the corpus-EXACT anchor verse for k-d-ḥ: the root
occurs in NO other verse. This is *stronger* than the classical balāgha reading (al-Zamakhsharī, al-Rāzī
treat the doubling as intensity *waḍʿ al-kalām*): the empirical fact is that the doubled forms are also
the only corpus attestations of the root. The verse al-Ṭabarī glosses as *"innaka ʿāmilun … fa-mulāqīh
bihi"* (you act, and meet Him with it) is the corpus's lexical home for the toil-toward-the-meeting motif.

**Honest limit.** "Corpus-EXACT" is on the no-tashkeel orthographic root level (QAC root `kdH`); the
related roots k-d-d (*kadd*, exert) and q-d-ḥ (*qadḥ*, strike fire) are distinct and not counted. The
rarity is the root's, not the broader semantic field's.

---

## Q084-F-03 — the book-hand judgment antithesis (NULL — pre-commit violation, full prominence)

**Hypothesis (pre-committed):** Q 84's judgment diptych — Arm A the right-hand party (vv 7-9) vs Arm B
the behind-the-back party (vv 10-15) — is a *muqābala* built ON shared anchor-roots reused with reversed
valence. **Direction-lock: S_obs = |roots(A) ∩ roots(B)| > null mean** (the two arms share MORE
anchor-roots than length-matched within-surah adjacent 3+6 verse-block pairs).

Counter-direction (S_obs < null mean — the antithesis is built by lexical *disjunction*, switching to
different vocabulary for the two fates) = NULL, published with full prominence per PRE-REG-STANDARD-04.

**Pre-reg SHA-256:** `bf28ee3f6aafcf3fc17d8fcd9718052f5e5ddc054f1a43225c4a5ac051c38ffb`
(independently recomputed at runtime — **[SHA-OK]** — and matches the embedded `EXPECTED_SHA`).

**Result (`csv/Q084-F-03.json`, seed 20260509, 10,000 perms; replication seed 20260511):**

| Quantity | Value |
|:--|:--|
| Arm A roots (vv 7-9), n=8 | Ahl, Aty, Hsb, ktb, qlb, srr, ymn, ysr |
| Arm B roots (vv 10-15), n=15 | Ahl, Aty, Hwr, Sly, Zhr, Znn, bSr, dEw, ktb, kwn, rbb, sEr, srr, vbr, wry |
| **Shared mirror-anchors** | **{Ahl, Aty, ktb, srr}** — n = **4** |
| S_obs | **4** |
| Cross-arm Jaccard J(A,B) | 0.2105 |
| Null mean (seed 20260509) | **5.2953** (sd 3.8835) |
| **z** | **−0.334** |
| **p_perm** | **0.6132** (6,132 of 10,000 null draws ≥ S_obs) |
| Replication (seed 20260511) | null mean 5.3040, p_perm 0.6168, z −0.334 |
| n candidate windows | 5,365 |

**Verdict: NULL (pre-commit violation), published with full prominence.** The locked direction (S_obs >
null mean) is **reversed**: the two antithetical arms share **4** anchor-roots, FEWER than the
length-matched null mean of **5.30** (z = −0.334). The replication seed reproduces this exactly. The
*muqābala*-as-shared-anchor-mirroring hypothesis is FALSIFIED for Q 84's judgment diptych.

**What the NULL teaches (this is a first-class finding).** Q 84's judgment antithesis is built by
**lexical DISJUNCTION, not shared-anchor reversal.** The four shared roots are the structural scaffold of
both fates — *Aty* (the book is *given*), *ktb* (the *book*), *Ahl* (the *family*), *srr* (*joy*) — i.e.
the COMMON frame ("a book is given; a fate follows; family + joy are at stake"). The *antithesis itself*
is realized by switching to entirely DIFFERENT vocabulary for the two outcomes: Arm A's *yamīn* (right
hand) / *ḥisāb* (reckoning) / *yusr* (ease) / *qalaba* (return) vs Arm B's *ẓahr* + *warāʾ* (behind the
back) / *daʿā thubūr* (call for ruin) / *ṣalā saʿīr* (burn in blaze) / *ḥawr* (return) / *ẓann* (thought)
/ *baṣīr* (watching). The contrast is a *swap of content roots*, not a *re-valencing of shared roots*.

This is mechanically driven by Q 84's **mufaṣṣal-qiṣār root-sparsity** (consistent with the
compression-tail laws): vv 7-15 union = 19 roots, far below the corpus 9-verse-block mean (~50), so there
is simply less shared-root budget than the longer Medinan blocks that dominate the null. The lexical
arms are short and content-disjoint by design — exactly the opposite of the H-NEW-1510 thin-pericope
cohesion that holds for the *sajda* pericope. The masrūr echo (*masrūrā* at v 9 AND v 13) — the surah's
one pointed lexical mirror that classical balāgha (Ibn Zayd via al-Qurṭubī) reads as the reversal of
worldly-vs-otherworldly joy — is the SOLE re-valenced anchor; it is not enough to lift the arms above the
length-matched baseline.

**Relation to the structural sibling Q066-F-01 Arm B.** This is the second per-surah test in which a
classical *antithesis/ring* reading FAILS a shared-anchor cohesion test (Q 66's dual-exemplar seal also
went NULL on its direction-lock). Both are clean instances of the **scale-of-aggregation** lesson
(cross-finding-025): a structure that is *rhetorically* an antithesis can be *lexically* disjoint at the
root-Jaccard level — the rhetorical opposition lives in the SEMANTICS of contrasting vocabulary, not in
re-valenced shared roots. Q 84's NULL contributes a fresh, independent instance.

**Pre-commit honesty.** The direction was locked in the pre-reg (S_obs > null mean) BEFORE the script ran;
the reversal is published as a NULL, NOT massaged. The pre-reg explicitly anticipated this mechanism
(mufaṣṣal-qiṣār sparsity) as the named counter-direction risk. No garden-of-forking-paths shift: the
analysis matched the pre-reg exactly; SHA verified.

---

## Bonferroni / family summary

| Finding | Type | Result | α handling | Verdict |
|:--|:--|:--|:--|:--|
| Q084-F-01 | deterministic set-intersection | I = {84}, |I|=1 | no permutation-α consumed | **CONFIRMED** |
| Q084-F-02 | deterministic corpus-count | 2 tokens, 1 verse | k=2 (per pre-reg), α_bon=0.025; deterministic | **CONFIRMED** |
| Q084-F-03 | permutation (k=1, α=0.05) | z=−0.334, p=0.613, direction reversed | single cell, α=0.05 | **NULL (pre-commit violation)** |

The only permutation cell is F-03 (α_corrected = 0.05/1 = 0.05). F-01 and F-02 are deterministic
corpus-exact counts and do not consume permutation-α. For the Q 84 surah session, F-03 is the single
landed permutation test, so no further cross-test Bonferroni correction is needed.

## MW protections applied

- **MW-1 (instrument-prior):** all three statistics (set-intersection, root-token-count, cross-arm
  shared-root count) and the F-03 arm definitions / null fixed in the pre-regs before computation.
- **MW-2 (corpus-prior):** F-03 used 10,000 length-matched within-surah adjacent 3+6 verse-block
  permutations (n=5,365 candidate windows).
- **MW-3 (alternative-models):** F-03 reports both S (count) and J (Jaccard); the shared-anchor identities
  are listed for transparency.
- **MW-5 (replication):** F-03 replicated at seed 20260511 (p=0.6168, z=−0.334, identical conclusion);
  F-01/F-02 are deterministic and fully replicable from the no-tashkeel JSON + QAC root data.
- **MW-6 (instrument-control):** F-03's same-surah adjacent-block null IS the non-target control (any 3+6
  block pair, not the specific antithesis).
- **MW-7 (post-hoc cap):** all three observations were noticed in close reading then promoted to
  pre-registered, direction-locked tests BEFORE computation; the single-test α=0.05 cap is respected.

## Cross-finding integration

- **H-NEW-1200** — F-01 confirms Q 84's membership in the FR-cohesive *idhā*-cosmic-opener cluster.
- **H-NEW-1330 / H-NEW-1510** — F-01 uses the 14-surah sajda set; H-NEW-1510's thin-pericope cohesion
  (the sajda pericope passes at the 3-verse scale) is the methodological foil to F-03's NULL.
- **H-NEW-2250** — F-03 addresses Q 84's OTHER major structure (the judgment diptych) after H-NEW-2250's
  Limit 2 left the *idhā*-cascade opening as a fragmented open question.
- **cross-finding-025 (scale-of-aggregation)** — F-03 is a new supporting instance (rhetorical antithesis
  ≠ root-Jaccard cohesion), alongside Q066-F-01 Arm B.

## Honest limits

- F-03's "shared-anchor" instrument is QAC-root-level; a lemma- or surface-bigram-level instrument could
  shift S_obs slightly, but cannot rescue a z of −0.334 (the arms are genuinely content-disjoint). A
  **budget-normalized** follow-up (Q084-F-03b, queued) — shared-anchor count ÷ surah-internal root budget —
  is pre-registered as a separate test; it is NOT a post-hoc rescue (the absolute-count direction-lock
  stands as a NULL).
- F-01's robustness to the 15-verse sajda-list variant is checked (singleton holds); other sajda-counting
  schools are not exhaustively enumerated.
- F-02's rarity is the root's (kdH), not the toil semantic field's.

---

*Computed/reproduced 2026-05-30; F-03 seed 20260509, 10,000 perms, SHA-locked pre-reg verified at runtime
([SHA-OK] bf28ee3f…). Scripts: `scripts/Q084_F_0{1,2,3}_*.py`; JSON: `csv/Q084-F-0{1,2,3}.json`.*
