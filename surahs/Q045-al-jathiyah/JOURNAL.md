---
surah: 45
surah_name: al-Jāthiyah
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
---

# Q 45 al-Jāthiyah — investigation journal


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 2026-04-28 (Session 1) — full-template completion (Wave D, ḥawāmīm-7)

### Pre-flight

Read in full per [[INVESTIGATION-PROTOCOL]]:
- `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md`
- `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md`
- Q 40 Ghāfir all 9 files (sibling model — most-detailed HM-A opener)
- Q 41 Fuṣṣilat all 9 files (sibling model)
- Q 42 al-Shūrā all 9 files (sibling model)
- Q 24 al-Nūr selected files (full-reference model — 06-novel-findings polished template)

### Garden-of-forking-paths log (BEFORE running any computation)

The following decisions were locked in pre-regs and SHA-256-fingerprinted BEFORE any script ran:

**Q045-F-01 (sharīʿa singleton)**:
- Tashkeel level: no-tashkeel (project default).
- Search method: exact substring `شريعة` (orthographic noun-form).
- Validation: cross-check at min-tashkeel + full-tashkeel + QAC v0.4 morphological audit.
- Direction: count == 1 ∧ verse == Q 45:18 = VINDICATED; else NULL or PRECOMMIT_VIOLATION.
- SHA256: `b13a44a3444b921a8ada51b5f9e4267e3e0b71e5ead4140e687621f009802a88`.

**Q045-F-02 (hawan-as-god twin)**:
- Tashkeel level: no-tashkeel.
- H1: count == 2 ∧ {Q 25:43, Q 45:23}.
- H1b: word-count ratio Q 45:23 / Q 25:43 > 1.7 (the expansion-thesis test).
- Direction-locked: VINDICATED iff both pass.
- SHA256: `87889c09fa16dc303700fd47ed9af6886b2c67a8c9554328222afd40ba4d5717`.

**Q045-F-03 (HM-A vs HM-B FR cohesion + Q 45 leave-one-out)**:
- FR distance source: `h-new-111.json` D-matrix.
- Permutation null: 10000 random size-3 (and size-4) subsets.
- Direction: HM-A < HM-B (HM-A tighter).
- H1b: HM-B-without-Q45 > HM-B (Q 45 tightens).
- p_perm < 0.025 (Bonferroni-corrected α for k=2).
- Seed: 20260428.
- SHA256: `70a5d56912f1c9421faefa9cd3f07eabaa49f1e79250598efe16882f7939de40`.

**Q045-F-04 (judgment-vocabulary density)**:
- Cluster of 13 roots locked a-priori in pre-reg (jzy, jvw, Hsb, Hkm, qDy, dyn, sAE, qwm, bTl, xsr, xtm, nTq, nsx).
- QAC v0.4 stem-roots; per-1000 normalization.
- H1: rank ≤ 28/114 corpus-wide.
- H1b: rank ≤ 11/114 in length-filtered subset n_verses ∈ [25, 60].
- Bonferroni α = 0.025.
- SHA256: `a09016bcf64d81927458d393f2da0db7c7070100f9efc09928108cde532041c2`.

These choices were locked **before** any computation; the SHA256 fingerprints are embedded in each script's `verify_prereg()` function and re-verified at runtime.

### Run timeline

1. **2026-04-28 ~01:00** — Pre-flight reading complete; sibling models reviewed.
2. **~02:00** — Empirical-data integration: pulled Q 45 metrics from `h-new-840.json` (UAS=+0.350, rank 41), `h-new-590.json` (Δ=−10.68, COHESION_ANCHOR), `h-new-720.json` (Q 44-45 cost 0.111, Q 45-46 cost 0.0959), `h-new-750.json` (sig_A=−0.654, sig_B=−1.033). Computed FR-nearest/farthest neighbors from `h-new-111.json` D-matrix (6441 entries); verified Q 42 → Q 45 rank-1.
3. **~03:00** — Wrote pre-regs Q045-F-01 through Q045-F-04; computed SHA256 fingerprints.
4. **~03:30** — Wrote scripts `Q045_F_01_shariah_singleton.py`, `Q045_F_02_hawan_as_god_twin.py`, `Q045_F_03_hmb_vs_hma_cohesion.py`, `Q045_F_04_judgment_vocabulary.py` with embedded SHA verification.
5. **~04:00** — Ran F-01: VINDICATED — `شريعة` corpus hits = 1, exactly Q 45:18; rules-tuple-stable; QAC root-family audit corroborates noun-form singleton.
6. **~04:05** — Ran F-02: VINDICATED — `اتخذ إلهه هواه` corpus hits = 2 = {Q 25:43, Q 45:23}; word-count ratio = 24/9 = 2.67× (above 1.7 threshold).
7. **~04:10** — Ran F-03: DIRECTIONAL on H1 (HM-A 0.8624 < HM-B 0.8665, p_perm = 0.257 above α=0.025); VINDICATED on H1b direction (HM-B-no-Q45 = 0.8809 > HM-B = 0.8665).
8. **~04:15** — Ran F-04: VINDICATED — Q 45 corpus rank 8/114 (top H1 ≤28); length-filtered rank 1/31 (top H1b ≤11); density 49.18/1000.
9. **~04:30** — Wrote 00-overview.md, 01-empirical-profile.md, 02-content-analysis.md, 03-tafsir-survey.md, 04-hadith-corpus.md.
10. **~05:00** — Wrote 05-classical-claims-audit.md (9 claims, all VINDICATED at primary or basis-level).
11. **~05:30** — Wrote 06-novel-findings.md (4 pre-registered tests reported).
12. **~06:00** — Wrote 07-cross-references.md and JOURNAL.md (this file).
13. **~06:15** — MASTER-FINDINGS-LEDGER §9 update: added Q 45 entry as §9.13 Wave-D (or wherever the next section number lands).

### NULLs surfaced (equal prominence)

- **F-03 H1 DIRECTIONAL not VINDICATED**: cluster-level HM-A vs HM-B cohesion-difference is direction-locked but p_perm = 0.257 fails Bonferroni α = 0.025. The HM-7 bifurcation is **primarily at the rhyme-axis** (3.4× entropy difference) and **only direction-locked at the FR-content axis**. This is a clean orthogonality finding — the rhyme-axis bifurcation does NOT extend to the content-axis at law-strength.
- **F-02 min-tashkeel rules-tuple fragility**: the *ittakhadha ilāhahu hawāhu* construction returns 0 hits under min-tashkeel because of intra-word combining marks. Stable at no-tashkeel and full-tashkeel-stripped; reported as VINDICATED under the project's default no-tashkeel rules-tuple, with the fragility explicitly noted.
- **F-04 corpus-rank 8 caveat**: 7 surahs ranking higher are all very-short late-Meccan (Q 95, 109, 103, 1, 98, 110, 82) where single-token signals inflate per-1000 density. The length-filtered (n_verses ∈ [25, 60]) rank 1 is the methodologically appropriate test; reported with the caveat.
- **DATA-GAPs flagged**:
  - Per-Q045 raw extractions of Ibn Kathīr / al-Qurṭubī / al-Rāzī / al-Ṭabarī / al-Suyūṭī al-Durr / al-Biqāʿī / al-Ṭabarsī / al-Thaʿlabī are NOT on disk this session — only consolidated OpenITI raw files. All citations anchored at surah-name marker level; per-Q045 sub-extraction would tighten precision.
  - al-Wāḥidī asbāb file `asbab-nuzul-wahidi-en-Q045.txt` not on disk; no concentrated *sabab al-nuzūl* for Q 45 in classical sources anyway.
  - Bukhārī divine-saying ḥadīth #4826/#6181/#7491 + Muslim #2246 (anchored at Q 45:24 *al-dahr* per classical exegesis) NOT verified at record-ID level this session; the discriminating-phrase pass surfaced the cluster-level al-Ḥawāmīm hadiths but not the divine-saying matn-keyword matches.
  - *Faḍāʾil al-Qurʾān* literature traditions (Abū ʿUbayd al-Qāsim b. Sallām via Ibn Kathīr's preface) are outside the 9-book pull; the *al-ḥawāmīm dībāj al-Qurʾān* + *lubāb al-Qurʾān* cluster-level traditions apply to Q 45 as a HM-7 member but require separate source-pull.

### Pre-commit honoring

- **Q045-F-01**: pre-committed direction "exactly one hit at Q 45:18". Observed: count=1, verse=Q 45:18. **MATCH** ✓.
- **Q045-F-02**: pre-committed direction "exactly two hits = {Q 25:43, Q 45:23} ∧ ratio > 1.7". Observed: hits = {Q 25:43, Q 45:23}, ratio = 2.67. **MATCH** ✓.
- **Q045-F-03**: pre-committed direction H1 "HM-A < HM-B" + H1b "HM-B-no-Q45 > HM-B". Observed: HM-A 0.8624 < HM-B 0.8665 ✓; HM-B-no-Q45 0.8809 > HM-B 0.8665 ✓. **DIRECTION MATCH on both** ✓ (p_perm magnitude not at law-strength on H1; H1b not significance-tested by design).
- **Q045-F-04**: pre-committed direction "rank ≤ 28 corpus-wide + ≤ 11 length-filtered". Observed: rank 8 + rank 1. **MATCH** ✓.

**No pre-commit violations occurred this session.**

### Summary verdict

Q 45 al-Jāthiyah investigation **COMPLETE** (per the 8-template-set + JOURNAL standard). Four pre-registered novel findings; 3 VINDICATED + 1 DIRECTIONAL. 9-claim classical audit; 9 VINDICATED at primary or basis-level (no falsifications). 

**Defining empirical facts for Q 45**:
1. *sharīʿa* (شريعة) noun-form is a **corpus-singleton** at Q 45:18 (deterministic, rules-tuple-stable).
2. *ittakhadha ilāhahu hawāhu* construction is a **corpus-singleton-pair** with Q 25:43; Q 45:23 expands by 2.67× (verbatim al-Rāzī expansion-thesis empirically locked).
3. **Length-filtered judgment-vocabulary density rank 1/31** (n_verses ∈ [25, 60]); corpus-rank 8/114.
4. **Q 45 IS Q 42's RANK-1 nearest content-neighbor** in the entire corpus (FR=0.801).
5. **Q 45 ↔ Q 46 = 0.811** is the **tightest single FR-pair within HM-B**.
6. **Q 45 is COHESION_ANCHOR** at the 7-window scale (Δ=−10.68); **AND** a HM-B cohesion-tightener at the 4-surah subset scale (Δ=+0.0144 if removed). **Multi-scale cohesion anchor**.
7. **UAS rank 41/114** (top-quartile) — Q 45 is a top-quartile architectural surah, mid-quartile within HM-7.

Cluster role: **HM-A↔HM-B bridge** (FR-third-nearest-to-HM-A-members + tightest-pair-with-Q-46 + Q 42's rank-1 partner). Architectural type: **anti-iʿjāz on both axes + multi-scale COHESION_ANCHOR + multi-singleton lexical-host**.

### Cross-references

- [[Q045-al-jathiyah/00-overview|Q 45 overview]]
- [[Q045-al-jathiyah/01-empirical-profile|Q 45 empirical profile]]
- [[Q045-al-jathiyah/06-novel-findings|Q 45 novel findings]]
- [[Q045-al-jathiyah/05-classical-claims-audit|Q 45 audit]]
- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 45's role
- [[Q040-ghafir/JOURNAL|Q 40 journal]] — sibling-investigation template
- [[Q041-fussilat/JOURNAL|Q 41 journal]]
- [[Q042-al-shura/JOURNAL|Q 42 journal]]
- [[MASTER-FINDINGS-LEDGER]] §9.x (Q 45 entry, this session)

---

## 2026-05-10 — Wave 2026-05-10 quad-specialist extension (Q 43-46)

**Specialist**: quad-specialist Q 43-46 ḥawāmīm landing.

### Q045-F-05 — *jāthiya* surface-form hapax verification
- pre-reg SHA: `718ca3b4632b81d41f739993a7921b4d89506ec095b76f0e4623cc5b66c3b1d4`
- **Verdict: VINDICATED.** Surface-form جاثية is corpus-singleton at Q 45:28. Root jvw has 3 corpus attestations (Q 19:68 *jithiyyā*, Q 19:72 *jithiyyā*, Q 45:28 *jāthiya*) — the Q 45 surface-form is morphologically distinct (feminine singular vs plural elsewhere).

### Q045-F-06 — HM ↔ Q 45 within-cluster pair-distance ranking
- pre-reg SHA: `3263cb19d575fe6cc98c3a308456eb911f4a67080fe2f4ab51c0eb9a44611f26`
- **Verdict: PASS-DIRECTED (highly significant).** Observed median FR-distance Q 45 ↔ HM_others = 0.8190, null median 0.9487. p_one_sided = **0.0002** (well below α_bon = 0.0167).
- **Tightest pair**: Q 45 ↔ Q 41 at 0.7994.
- **Five of six HM-neighbors of Q 45 sit below FR=0.85** — Q 45 is the most strongly HM-cohesive surah by this test in the cluster.
- Cross-direction replicated by Q043-F-07 (p=0.0043).

### Q045-F-07 — *waylun li-kulli affāk* corpus-uniqueness
- pre-reg SHA: `bdd6f1c9de4ea1d673f9fb1534722b1ce095953f20e54ed23c2d3d89faf7b031`
- **Verdict: PARTIAL.** Primary phrase ويل لكل أفاك corpus-singleton at Q 45:7. Secondary collocation أفاك أثيم NOT singleton (also at Q 26:222). Q 45:7 is a **crossing-node** between two corpus-twin lines (affāk-athīm-twin to Q 26:222; waylun-li-kulli-twin to Q 104:1).

### Summary
- 1 VINDICATED + 1 PASS-DIRECTED + 1 PARTIAL.
- Three independent pairwise-HM-cohesion confirmations across the Wave (Q 41-Q 42 from Q041-F-03; Q 43 from Q043-F-07; Q 45 from Q045-F-06). HM cluster is empirically root-FR-cohesive at pairwise level.
- "Crossing-node" observation at Q 45:7 is a novel corpus-architectural pattern (intersect of two corpus-twin lines).

