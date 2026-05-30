---
surah: 31
surah_name_ar: لقمان
surah_name_translit: Luqmān
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 31 Luqmān — Investigation Journal

## 2026-05-09 — full 8-file deep-dive (specialist: Q031-luqman-specialist)

The seven content files (00-overview through 07-cross-references) and the four pre-registered
tests (Q031-F-01..04, with `preregs/`, `scripts/`, `csv/`) were authored on 2026-05-09. This
JOURNAL is the run-log summary, written consistent with the on-disk files; no values are restated
from memory — each is traceable to the cited artifact.

**Pre-flight (per INVESTIGATION-PROTOCOL.md §6.1):** quran-investigation SKILL.md →
INVESTIGATION-PROTOCOL.md (full) → KNOWLEDGE-GRAPH.md → MASTER-FINDINGS-LEDGER.md (ALM-cluster +
cross-finding-006/008 sections) → confirmed `surahs/Q031-luqman/` and built the template.

**Surah profile (from disk, every value path-traced):**
- 34 verses, Late-Meccan (al-Suyūṭī *Itqān* nawʿ 1); Tanzil rev-order 57, Nöldeke 82
  (`data/revelation-order.csv`); 12 verses on `data/hafs-verse-counts.tsv` line 31 = 34.
- 551 word-tokens / 2,172 letter-graphemes (no-tashkeel), avg 16.2 words / 63.9 graphemes per verse
  — computed from `quran-text/quran-no-tashkeel.json` (basmala-counted-only-in-Q1).
- Opening: الم + *tilka āyātu al-kitābi al-ḥakīm / hudan wa-raḥmatan li-l-muḥsinīn* — the inner
  ALM-book-reference triad {Q 2, Q 3, Q 31} (cross-finding-008 cohort; the ALM-exception subset
  {Q 29, Q 30, Q 32} lacks this couplet).
- 4 macro-blocks: A (1-11 ALM frame + scripture self-reference), **B (12-19 the 8-waṣāyā Luqmān
  pericope)**, C (20-30 cosmic-signs incl. v.27 sea-ink-pens *tashbīh murakkab*, twin of Q 18:109),
  D (31-34 mortality + the five *mafātīḥ al-ghayb* at v.34).

**H-NEW metrics integrated (all cited to path in 01-empirical-profile):**
- **h-new-111**: mean FR 0.948 (just above corpus 0.924); nearest neighbour Q 45 al-Jāthiya
  (0.7685); ALM-siblings appear LATER than many non-ALM neighbours (single-surah evidence for
  letter-axis ⊥ content-axis).
- **h-new-590**: WEAK_OUTLIER, Δ%ile +2.14, p_greater 0.31, window {Q 28-34}.
- **h-new-700 / h-new-750**: rhyme entropy 1.291 nats (z +0.94, HIGH/non-monorhyme); top rāwī
  ر 47.1%; sig_A +0.698 (rank 43), sig_B +0.319 (rank 49); local cohesion 1.060.
- **h-new-720**: Q 30→Q 31 δ +0.0376 (resid 0.45%); Q 31→Q 32 δ +0.1005 (resid 1.21%); both
  inexpensive interior seams — LEFT of the corpus-TOP-3 expensive Q 32→Q 33 hinge (+0.3631).
- **h-new-840**: UAS −1.171, rank 80/114 (LOW — content-rich didactic compendium, not a
  structural-iʿjāz outlier).

**Tafsīr (≥5, scholar + work + passage, in 03-tafsir-survey):** al-Ṭabarī (*Jāmiʿ al-bayān*,
Luqmān-as-ḥakīm majority + prophet minority report), al-Rāzī (*Mafātīḥ al-ghayb* — its very title
from Q 31:34), al-Qurṭubī (*al-Jāmiʿ li-aḥkām*), Ibn Kathīr (*Tafsīr al-Qurʾān al-ʿaẓīm*, disclaims
the Aesop equation), al-Biqāʿī (*Naẓm al-Durar*, ḥikma-opener → ḥikma-figure munāsaba), with
al-Suyūṭī/al-Zarkashī on the vv.14-15 *iltifāt* voice-shift.

**Ḥadīth (04-hadith-corpus):** v.34 *mafātīḥ al-ghayb* anchored to al-Bukhārī *Kitāb al-Tawḥīd*
(Jibrīl-asks-about-the-Hour narration) — numbers as recorded in the file, flagged where a
surah-named faḍāʾil ḥadīth is not located in the 9-book set (data-gap, not absence-claim).

**Pre-registration + computation (06-novel-findings; seed 20260509, 10,000 perms; SHA-locked
preregs in `preregs/`, SHA-verified scripts in `scripts/`, JSON in `csv/`):**
- **Q031-F-01** yā-bunayya per-verse density — SHA `1d483e8d…58e97`. Q 31 = corpus-MAX in the
  data-defined 5-surah cohort {Q 2, 11, 12, 31, 37}: 3 tokens / 34 verses = 0.0882, 3.27× the
  next-densest (Q 12, 0.0270), perm-p 0.0067 < α_bon 0.025. **PASS-DIRECTED** (ceiling set by
  disclosed post-hoc origin in the prereg garden-of-forking-paths log §5).
- **Q031-F-02** ALM-cohort FR-position — SHA `d496f4a2…1fcc`. perm-p 0.38; D_top12 0.8374 <
  D_alm 0.9376. **NULL CONFIRMED + H2 vindicated** — replicates cross-finding-006 at single-surah
  level.
- **Q031-F-03** Luqmān-pericope lexical isolation — SHA `e21dd7b4…9575`. observed cosine 0.4416 >
  null mean 0.4329 (direction matched) but perm-p 0.37 > α 0.05. **DIRECTIONAL.**
- **Q031-F-04** divine-name-pair density (laṭīf-khabīr, ʿazīz-ḥakīm, ʿalīm-khabīr) — SHA
  `6e7a14d1…05fd`. 3/3 pass at α 0.05 (best ʿalīm-khabīr p 0.0187) but 0/3 at α_bon 0.0167.
  **DIRECTIONAL** (honest: a Stouffer combine survives Bonferroni but the pairs share *khabīr*, so
  independence fails — verdict held at DIRECTIONAL).

**Decision points / discipline:** Q031-F-01 ceiling held at PASS-DIRECTED rather than CONFIRMED
(post-hoc origin disclosed pre-lock); Q031-F-04 Bonferroni NOT loosened to rescue the 3 α-passes
(tightening self-verifies, loosening requires ratification — not requested). No direction adjusted
after observation; no pre-commit violations.

**Architectural verdict:** Q 31 is the corpus's **Late-Meccan didactic-wisdom compendium** —
eponymously named for a non-prophet sage, organised around the 8-verse Luqmān pericope; mid on both
iʿjāz axes, LOW UAS, content-distinct only at the thematic level. Matches the H-META-1 classifier
prediction (HIGH classical-tradition ratification + LOW numerological survivability).

**Files on disk:** 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey,
04-hadith-corpus, 05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this),
+ `preregs/` (4), `scripts/` (4), `csv/` (Q031-F-01..04.json).

## 2026-05-30 — JOURNAL added (→ 9/9)

This JOURNAL was added in the surah-completeness pass to bring Q 31 from 8/9 to the full 9/9
template; it summarises the 2026-05-09 deep-dive already on disk and introduced no new
computation. Per the surah-completeness audit (`findings/phase-b-hypotheses/surah-completeness-audit-2026-05-29.md`),
Q 31 was one of three 8/9 surahs missing only the JOURNAL.
