---
id: H-NEW-420
title: "Novel-outlier (Q 33, Q 24, Q 9, Q 12) block-exclusion validation — does outlier-factor generalize beyond Q 55?"
phase: B
status: PRE-REGISTERED 2026-04-21
date: 2026-04-21
agent: team-lead (inline; ID 420 skip codex range)
parent_1: H-NEW-390 (Q 55 block-exclusion +32.6pp)
parent_2: H-NEW-400 (Q 62 NOT outlier -1.6pp)
parent_3: H-NEW-410 (full 114-surah outlier spectrum — Q 33/24/9/12 ranked 4/5/7/6)
seed: 20260509
bonferroni_k: 4
bonferroni_family: h-new-420-novel-outlier-exclusion
alpha_bon: 0.0125
rules_tuple: "(FR from H-NEW-111; for each outlier k ∈ {9, 12, 24, 33}: define block_k = {k-2, k-1, k, k+1, k+2} ∩ [1,114]; compute d̄_full = mean pairwise FR on block_k; compute d̄_exc = mean pairwise FR on block_k \\ {k}; 10000-permutation null over random-subsets of same size; percentiles p_full, p_exc; delta_pp = p_exc - p_full; direction: delta_pp ≥ +15.0 counts as CONFIRM-outlier; Bonferroni k=4)"
direction: "Per outlier k: CONFIRM-outlier if percentile_exc ≥ percentile_full + 15.0pp; NULL otherwise. Pre-commit majority (≥3/4) confirmation = outlier-factor generalizes beyond Q 55."
verdict: PENDING
---

# [[h-new-420-novel-outlier-exclusion|H-NEW-420]] — Novel-outlier block-exclusion validation

## 1. Question

[[h-new-410-outlier-spectrum|H-NEW-410]] empirically identified **7 surahs above d̄_local = 1.10 threshold** (in descending order):
- Q 1 al-Fātiḥa (rank 1, d̄=1.2003) — corpus-max outlier
- Q 55 al-Raḥmān (rank 2, d̄=1.1686) — classical *ʿarūs al-Qurʾān*, validated by [[h-new-390-q55-outlier-exclusion|H-NEW-390]] (+32.6pp)
- Q 56 al-Wāqiʿah (rank 3, d̄=1.1557)
- Q 33 al-Aḥzāb (rank 4, d̄=1.1472) — Medinan-legal register anomaly
- Q 24 al-Nūr (rank 5, d̄=1.1452) — Medinan social-law cluster anchor
- Q 12 Yūsuf (rank 6, d̄=1.1352) — unique *aḥsan al-qaṣaṣ* narrative monograph
- Q 9 al-Tawbah (rank 7, d̄=1.1197) — no-basmala anomaly, warfare-edict register

**Does the outlier-disruption effect ([[h-new-390-q55-outlier-exclusion|H-NEW-390]] Q 55 +32.6pp) generalize to these novel candidates?** Or is it Q 55-specific (as [[h-new-400-q62-outlier-candidate|H-NEW-400]] Q 62 test showed for "prominent" surahs)?

We exclude **Q 1 and Q 56** from this test:
- Q 1 is a boundary surah (only 2 neighbors in ±2 window) — edge-effect confound.
- Q 56 is already bracketed by Q 55 (same cluster); exclusion would double-count the al-Raḥmān effect.

**Tested: Q 9, Q 12, Q 24, Q 33** — the 4 novel outliers with classical-scholarship anchors but no prior block-exclusion validation.

## 2. Protocol

For each outlier k ∈ {9, 12, 24, 33}:

1. Define local ±2 block: `block_k = {k-2, k-1, k, k+1, k+2} ∩ [1, 114]`
   - Q 9: block = {7, 8, 9, 10, 11}
   - Q 12: block = {10, 11, 12, 13, 14}
   - Q 24: block = {22, 23, 24, 25, 26}
   - Q 33: block = {31, 32, 33, 34, 35}
2. Compute `d̄_full` = mean pairwise FR distance on the 5-surah block.
3. Compute `d̄_exc` = mean pairwise FR distance on the 4-surah block with k removed.
4. Null distribution: 10000 random subsets of the SAME SIZE (5 and 4 respectively), compute d̄ for each; derive percentile of observed d̄.
5. **delta_pp = percentile(d̄_exc) − percentile(d̄_full)**. Positive delta = exclusion makes block MORE-cohesive = outlier-confirmed.
6. CONFIRM-outlier threshold: delta_pp ≥ +15.0 (matches Q 55's +32.6pp magnitude scale, but stricter than noise).

## 3. Pre-committed predictions

- **H1 (strong)**: ≥3/4 novel outliers show delta_pp ≥ +15.0 (outlier-factor generalizes)
- **H0 (null)**: <3/4 show the effect (outlier-factor is Q 55-specific + Q 1 sui-generis)
- **Per-outlier pre-commitments** (directional):
  - Q 9: PREDICTED ≥+15pp (no-basmala + warfare-edict register vs Yūnus/Hūd Meccan narrative neighbors)
  - Q 12: PREDICTED ≥+20pp (pure monograph 111 verses vs Hūd/Raʿd/Ibrāhīm mixed-narrative neighbors)
  - Q 24: PREDICTED ≥+15pp (Medinan social-legal vs al-Muʾminūn/al-Furqān Meccan-creed neighbors)
  - Q 33: PREDICTED ≥+15pp (Medinan Prophet-household legal vs Luqmān/al-Sajdah/Sabaʾ/Fāṭir Meccan-theology)

**Honest prior**: Q 12 is the clearest a-priori — Yūsuf is a singular monograph bracketed by mixed-narrative Meccan surahs. Q 9 has a phonological-liturgical marker (no basmala) but its content is edictal-Medinan mixing with Medinan-adjacent Q 8 al-Anfāl. Weakest candidate is **Q 24** — Medinan neighbors Q 22, 23 are mixed-register and Q 25, 26 Meccan narrative; exclusion effect could be small.

## 4. Bonferroni

k=4 (4 outlier exclusion tests, one per candidate). α_bon = 0.05/4 = 0.0125.

For this descriptive delta test, the Bonferroni-adjusted inferential-test is: percentile_exc ≤ 1.25% or ≥ 98.75% after exclusion. The primary directional criterion is the ≥+15pp effect size.

## 5. Honest limits

1. **N=5 and N=4 subsets are very small** — null distribution at α=0.0125 is narrow; inferential p-values conservative.
2. **±2 window is arbitrary** — broader windows might give different results (addressed in H-NEW-410.1, separate).
3. **"Outlier" definition is FR-distance-based** — phonological/morphological/prosodic axes could disagree.
4. **Classical anchor strength varies** — Q 9 no-basmala is a STRONG classical flag; Q 33 Medinan-household is a THEMATIC flag; Q 12 aḥsan al-qaṣaṣ is an EXPLICIT Quranic self-designation (Q 12:3); Q 24 al-Nūr is the canonical Medinan social-law centerpiece.
5. **FR-roots only**.
6. **No chronology control** — some exclusion effects could reflect chronology mismatch rather than content-uniqueness.

## 6. Classical anchor per candidate

- **Q 9 al-Tawbah**: al-Suyūṭī *Itqān* ch. 9 (omission of basmala — al-Ḥajjāj b. Yūsuf & ʿUthmāni codification); Ibn ʿAbbās *Tanwīr* q.v. *barāʾa*. Content: warfare edicts, hypocrite diagnostics, alliance-termination.
- **Q 12 Yūsuf**: Quranic self-designation *aḥsan al-qaṣaṣ* (Q 12:3); al-Qurṭubī *Jāmiʿ* 9/120; al-Biqāʿī *Naẓm al-Durar* vol. 9 (entire surah as single monograph). UNIQUE in Quranic corpus as continuous single-prophet narrative 111 verses.
- **Q 24 al-Nūr**: al-Suyūṭī *Itqān* naming al-Nūr as social-legal-centerpiece; al-Zamakhsharī *Kashshāf* on *āyat al-nūr* Q 24:35 as theological-cosmological central simile; Medinan family-law block.
- **Q 33 al-Aḥzāb**: al-Biqāʿī *Naẓm al-Durar* vol. 16 on Q 33 as Prophet-household legal-singular; al-Ṭabarī *Jāmiʿ al-bayān* on *aḥzāb*-battle and Zaynab-marriage verses.

## 7. Deliverables

- Pre-reg: this file
- Script: `scripts/h_new_420_novel_outlier_exclusion.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-420.json`
- Findings: `findings/phase-b-hypotheses/h-new-420-novel-outlier-exclusion.md`

Pre-reg locked 2026-04-21.
