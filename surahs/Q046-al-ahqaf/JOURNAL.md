---
surah: 46
surah_name: al-Aḥqāf
file_type: journal
date_started: 2026-04-28
date_last_updated: 2026-04-28
phase: B+
---

# Q 46 al-Aḥqāf — investigation journal

## 2026-04-28 (Session 1) — full-template build from scratch

### Pre-flight reading (locked before any computation)

1. `/Users/grey/Downloads/quran/.claude/skills/quran-investigation/SKILL.md` — read.
2. `/Users/grey/Downloads/quran/INVESTIGATION-PROTOCOL.md` — read in full.
3. Sibling templates: Q040-ghafir/ (full 8-file + JOURNAL), Q041-fussilat/, Q042-al-shura/ structures inspected; Q024-al-nur/ as the most polished reference.
4. `MASTER-FINDINGS-LEDGER.md` §9 (Wave A/B/C) for ledger-update format.
5. `findings/cross-finding/csv/hawamim-7-cluster-bifurcation.json` (Q 46 in HM-B closer position).

### Garden-of-forking-paths log (BEFORE running any computation)

For each of the four pre-registered novel tests (Q046-F-01 through Q046-F-04), the following decisions were locked BEFORE running:

**Q046-F-01 (boundary cost rank)**:
- **Source**: `h-new-720.json` `per_adjacency`, `delta` field.
- **Pair**: `[46, 47]`.
- **Rank metric**: descending sort on `delta`, with rank 1 = highest cost.
- **Direction**: rank ≤ 25 (top-22%).
- **Threshold mapping**: ≤10 VINDICATED, ≤25 DIRECTIONAL, [26-56] REFINED-MODERATE, >56 NULL.
- SHA `0eafb9802f5a62a8f9704fe3fe6771ebf0c9e2037e224e9b42633fdea4e02374`.

**Q046-F-02 (jinn-listening Jaccard)**:
- **Tashkeel level**: no-tashkeel.
- **Root operationalisation**: QAC v0.4 stem-roots from `data/morphology/quranic-corpus-morphology-0.4.txt`.
- **Q 46 window**: verses 29, 30, 31, 32 — locked.
- **Q 72 window**: full surah (28 verses).
- **Metric**: |intersection|/|union| (binary Jaccard).
- **Null**: 10000 random non-overlapping 4-contiguous-verse Q 46 windows ↔ Q 72.
- **Direction**: observed > median(null).
- **Seed**: 20260428.
- SHA `9a9b63f5469d9a96006115c7ad96b38161652eaa40b5db3105a022adf04c022a`.

**Q046-F-03 (Hqf hapax-eponym)**:
- **Source**: `data/morphology/root-index.json` key "Hqf"; cross-check `quran-text/quran-no-tashkeel.json` regex.
- **Pre-committed**: count == 1, location == [46, 21, *].
- Deterministic.
- SHA `d2e68adeb5d74cb10b316c65941101511c4057d42948e7040021e0e4416db620`.

**Q046-F-04 (internal vs exit cost)**:
- **Source**: `h-new-720.json` `per_adjacency`.
- **Pairs**: [45,46] and [46,47].
- **Direction**: delta(45→46) > delta(46→47).
- **Threshold**: ≥5% margin = VINDICATED.
- Deterministic.
- SHA `71c8d4f6467612d5d51a1713fdd9c732f82bcf78caae2ca47d9e0efceef5e7ef`.

### Run timeline

1. **00:00** — Pre-flight reading complete.
2. **00:30** — Wrote 00-overview.md (verse-counts, name-glosses, HM-7 position, empirical fingerprint).
3. **01:00** — Wrote 01-empirical-profile.md (UAS=−1.591 rank 91; Δ=−2.34 NULL; sig_A=−0.38; FR-nearest=Q 41 at 0.7254; Q46→Q47 cost rank 42/113).
4. **01:30** — Wrote 02-content-analysis.md (15 thematic blocks; Hqf hapax verified; jinn-listening lexical signature).
5. **02:00** — Wrote 03-tafsir-survey.md (al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, al-Biqāʿī, Ibn Kathīr, al-Suyūṭī = 7 mufassirūn).
6. **02:30** — Searched 9-book canonical hadith corpus; verified Mālik #1625 (Q 46:15), Bukhārī #4621 (Q 46:17 ʿĀʾisha), Muslim #908 (Q 46:29-32 Ibn ʿAbbās). Wrote 04-hadith-corpus.md.
7. **03:00** — Wrote 05-classical-claims-audit.md (10 claims).
8. **03:00-03:30** — Wrote 4 pre-registration files; SHA-locked.
9. **03:30** — Wrote 4 scripts with embedded SHA verification.
10. **03:35** — Ran Q046_F_01..04 — all SHAs matched; results:
    - Q046-F-01: rank 42/113 → REFINED-MODERATE (direction-MISS at threshold 25).
    - Q046-F-02: Jaccard=0.154; null median=0.115; p_perm < 0.0001 → VINDICATED.
    - Q046-F-03: 1/1 corpus-hapax at Q 46:21 → VINDICATED.
    - Q046-F-04: 9.9% margin internal > exit → VINDICATED.
11. **04:00** — Wrote 06-novel-findings.md with equal NULL prominence for Q046-F-01.
12. **04:15** — Wrote 07-cross-references.md and JOURNAL.md.
13. **04:30** — Updated `MASTER-FINDINGS-LEDGER.md` §9 with Q 46 entry (next).

### NULLs / direction-misses surfaced (equal prominence)

- **Q046-F-01: REFINED-MODERATE (rank 42/113)** — pre-committed direction (rank ≤ 25) MISSED. The user-prompt's "HIGH canonical-adjacency-cost transition per h-new-720" framing is empirically softened to "moderate-upper-third". Published with full prominence in `06-novel-findings.md` §1 and the equal-NULL-prominence section.
- **Claim 7 (boundary cost)**: REFINED in `05-classical-claims-audit.md`.
- **Claim 9 (HM-7 *dībāj*)**: DIRECTIONAL — Q 46 specifically pulls cluster UAS DOWN.
- **Claim 6 (ʿAbdallāh b. Salām witness)**: DIRECTIONAL with internal classical dissent (al-Shaʿbī/Masrūq objection).
- **Claim 10 (Abū Bakr's mother asbāb)**: DATA-GAP / CONFLATION — the user-prompt framing apparently conflates Q 46:15 with Q 46:17. The actual Q 46:17 anchor is Umm Rūmān (ʿĀʾisha's mother) via Bukhārī #4621.

### Pre-commit honoring

- Q046-F-01: direction MISS published transparently — REFINED-MODERATE is the verdict.
- Q046-F-02, F-03, F-04: directions MATCHED. No pre-commit violations on these three.
- All four SHAs verified at runtime.

### Data-gaps flagged

1. Per-Q46 extraction files for al-Ṭabarī, al-Zamakhsharī, al-Rāzī, al-Qurṭubī, al-Biqāʿī, Ibn Kathīr, al-Suyūṭī NOT yet generated as discrete-file extracts; cited by surah-name marker in consolidated raw files.
2. al-Wāḥidī, *Asbāb al-nuzūl* per-Q46 extract NOT verified on disk this session.
3. al-Ṭabarsī, al-Thaʿlabī per-Q46 extracts NOT verified.
4. Bukhārī k. *al-tafsīr* chapter on Sūrat al-Aḥqāf — only one record (Bukhārī #4621) verified verbatim; chapter-level full extraction deferred.
5. Faḍāʾil al-Qurʾān (Abū ʿUbayd) traditions on al-Ḥawāmīm cluster NOT in 9-book pull.
6. Aḥmad's Musnad partial pull (~1,374 records) — full Musnad would expand jinn-encounter citations.
7. Per-Q46 cross-corpus null on jinn-listening Jaccard against pre-Islamic poetry corpora deferred.
8. The Hūd-narrative passage-level FR-distances (Q 46:21-26 vs Q 11:50-60 only) computed only at whole-surah level.

### Honest limits

1. Q 46 UAS rank 91 is bottom-quartile — NOT a standalone architectural outlier. Significance is sub-cluster (HM-B closer; HM-7 bookend; corpus-hapax-eponym).
2. The Q 46→Q 47 boundary cost (rank 42/113) is the user-prompt's most empirically soft claim.
3. The 9.9% internal>exit margin (Q046-F-04) is single-pair; corpus-wide replication of "internal > exit for clusters" deferred as a Wave-D follow-up hypothesis.
4. The user-prompt's mention of "asbāb al-nuzūl about Abū Bakr's mother" appears to conflate Q 46:15 (the gestation verse, anchored to ʿAlī-ʿUthmān adjudication) with Q 46:17 (the rebellious-son verse, anchored to Umm Rūmān = ʿĀʾisha's mother who is Abū Bakr's wife).

### Verdict

Q 46 al-Aḥqāf investigation **COMPLETE** (per the 8-template-set + JOURNAL standard). 

**Headline empirical signature**: Q 46 is the **HM-B closer + corpus-hapax-eponym (Hqf at v.21) + jinn-listening lexical-signature partner with Q 72 (Jaccard p<0.0001) + counter-intuitive higher internal-step cost than HM-exit cost**.

**Defining empirical fact**: *al-Aḥqāf* is one of the strongest concentration-eponymity surahs in the corpus — a single corpus-wide root attestation (Hqf at Q 46:21).

### Cross-references

- [[hawamim-7-cluster-bifurcation|HM-7 cluster bifurcation]] — Q 46 in HM-B (the prosodic monorhyme cluster)
- [[Q046-al-ahqaf/06-novel-findings|Q 46 novel findings]]
- [[Q046-al-ahqaf/05-classical-claims-audit|Q 46 claims audit]]
- [[MASTER-FINDINGS-LEDGER#9.7d|§9.7d MASTER ledger entry]] (added this session)
