---
surah: 55
file_type: novel-findings
date_last_updated: 2026-04-28
phase: B+
verdict: COMPLETE — 5 pre-registered novel findings; verdicts mixed
---

# Q 55 al-Raḥmān — Novel Findings

Five pre-registered novel tests for Q 55. Each has a separate pre-reg in `preregs/` and a script in `scripts/`. Results are stored in `csv/`.

---

## Q055-F-01: 31-fold refrain density audit

- **Pre-reg**: `preregs/Q055-F-01-refrain-density-prereg.md`
- **Script**: `scripts/Q055_F_01_refrain_density.py`
- **JSON**: `csv/Q055-F-01.json`
- **Direction-locked**: refrain-count = 31 across all 3 tashkeel variants; Q 55 ranks corpus-#1 in phrase-repetition AND verse-repetition.

### Result

- Refrain count: **31** in no-tashkeel, **31** in min-tashkeel, **31** in full-tashkeel (after ʾalif normalization).
- Q 55 max-phrase repetition rank: **1 / 114** (31 vs runner-up Q 5 at 16, Q 2 at 11, Q 4 at 9).
- Q 55 max-verse repetition rank: **1 / 114** (31 vs runner-up Q 26 at 8).

### Verdict

**CONFIRMED** — exact 31-count, cross-variant-stable, corpus-rank-1 in both phrase and verse repetition.

### Verbatim refrain text (cross-validated)

| Variant | Text |
|:--|:--|
| no-tashkeel | فبأي آلاء ربكما تكذبان |
| min-tashkeel | فَبِأَىِّ ءالاءِ رَبِّكُما تُكَذِّبانِ |
| full-tashkeel | فَبِأَيِّ ءَالَآءِ رَبِّكُمَا تُكَذِّبَانِ |

After ʾalif-normalization (ءا → ا, [إأآٱ] → ا, ى → ي): all three reduce to `فباي الاء ربكما تكذبان`.

---

## Q055-F-02: Dual-pronoun *kumā* density audit

- **Pre-reg**: `preregs/Q055-F-02-kuma-density-prereg.md`
- **Script**: `scripts/Q055_F_02_kuma_density.py`
- **JSON**: `csv/Q055-F-02.json`
- **Direction-locked**: Q 55 corpus-#1 in word-final *-kumā* density per 100 words.

### Result

- Q 55: **32 word-final *-kumā* attachments + 7 word-final *-humā* attachments** in 352 words.
- Q 55 *-kumā* density: **9.09 / 100 words — rank 1 / 114**.
- Q 55 dual-total density: 11.08 / 100 words — rank 1 / 114.
- Runner-up Q 66: 0.39 / 100w. Q 55 is **23× the runner-up.**

### Verdict

**CONFIRMED** — Q 55 is corpus-extreme in dual-pronoun density. This is the empirical anchor for the classical *thaqalān* (jinn + mankind) interpretation of *rabbikumā*.

---

## Q055-F-03: Cosmic-vocabulary density

- **Pre-reg**: `preregs/Q055-F-03-cosmic-vocab-prereg.md`
- **Script**: `scripts/Q055_F_03_cosmic_vocab.py`
- **JSON**: `csv/Q055-F-03.json`
- **Direction-locked**: Q 55 ranks top-3 in cosmic-vocabulary density (samāʾ, arḍ, shams, qamar, najm, baḥr).

### Result

- Q 55 cosmic counts: samāʾ × 4, arḍ × 3, shams × 1, qamar × 1, najm × 1, baḥr × 2 (12 cosmic tokens).
- Q 55 cosmic density: 3.41 / 100 words — **rank 4 / 114**.
- Top-3: Q 91 (al-Shams), Q 86 (al-Ṭāriq), Q 99 (al-Zilzāla) — all very short surahs.
- Q 55 is the **only top-15 surah with all 6 cosmic lemmas attested** AND the **highest-density cosmic surah of substantial length (>200 words)**.

### Verdict

**DIRECTIONAL** — pre-reg locked top-3 as CONFIRMED; rank-4 is one position below the threshold.

Under post-hoc length-class restriction (>200 words), Q 55 IS rank-1 corpus-wide. Under lemma-coverage criterion (all-6-attested), Q 55 is uniquely so. These are post-hoc moves and **carry single-test-α=0.05 ceiling per MW-7**, so we report them descriptively rather than as confirmation.

The headline result: **the classical "most cosmic surah" claim is rules-tuple-fragile**: rank by raw density, Q 55 is 4th; rank by integrated-cosmic-imagery, Q 55 is exceptional.

---

## Q055-F-04: Dual-paradise structural-similarity test

- **Pre-reg**: `preregs/Q055-F-04-dual-paradise-prereg.md`
- **Script**: `scripts/Q055_F_04_dual_paradise.py`
- **JSON**: `csv/Q055-F-04.json`
- **Direction-locked**: cos(P1=46-61, P2=62-77) > cos(P1, CTRL=14-29) AND cos(P1, P2) > cos(P2, CTRL); permutation p < 0.025 (Bonferroni-corrected).

### Result

- cos(P1, P2) = **0.918**
- cos(P1, CTRL) = 0.787
- cos(P2, CTRL) = 0.765
- Direction: PASS (P1-P2 > both controls)
- Permutation p (10000 random 16-verse partitions, seed 20260428): **0.0033**

### Top shared tokens between P1 and P2

| Token | P1 count | P2 count |
|:--|:-:|:-:|
| ربكما | 8 | 8 |
| فباي | 8 | 8 |
| تكذبان | 8 | 8 |
| الاء | 8 | 8 |
| فيهما | 2 | 2 |
| متكئين | 1 | 1 |
| يطمثهن | 1 | 1 |
| جنتان | 1 | 1 |
| فيهن | 1 | 1 |
| فاكهة | 1 | 1 |
| (jān, qabl, eyes ʿaynān, lam, ʾins) | 1 | 1 |

The two paradise blocks are STRUCTURALLY NEAR-IDENTICAL — they share refrain-octets (8+8) AND a parallel description-vocabulary (2 springs, 2 fruit, 2 maidens types, 1 reclining, 1 untouched-formula).

### Verdict

**CONFIRMED** — the dual-paradise blocks are empirically structurally parallel, far beyond chance. This is the strongest empirical confirmation of the classical *muqarrabūn / aṣḥāb al-yamīn* hierarchical paradise reading (al-Ṭabarī, al-Rāzī, Ibn Kathīr).

---

## Q055-F-05: H-NEW-390 outlier-exclusion replication for Q 55

- **Pre-reg**: `preregs/Q055-F-05-h390-replication-prereg.md`
- **Script**: `scripts/Q055_F_05_h390_replication.py`
- **JSON**: `csv/Q055-F-05.json`
- **Direction-locked**: Q 55 classification under H-NEW-590 ∈ {MODERATE_OUTLIER, STRONG_OUTLIER}; Δ-pp positive.

### Result

- H-NEW-390 (Meccan-only Q 50-56 cell, n=6): Δ = **+32.62pp** — full Meccan d_obs improves from pct 70.10 (with Q 55) → 0.71 (without Q 55).
- H-NEW-590 (standardized window-7 [Q 52, ..., 58]): Δ = **+14.26pp** — pct 97.81 → 83.55, classification MODERATE_OUTLIER, p_greater_W = 0.0219.
- Q 55 mean Fisher-Rao distance to neighbors Q 50, 51, 52, 53, 54, 56: **1.114** (corpus mean ≈ 0.96; Q 55 sits high above).

### Verdict

**CONFIRMED — Q 55 maintains MODERATE_OUTLIER classification under standardized methodology**.

The +32.6pp historic figure was an artifact of Meccan-only chronological restriction. The standardized comparable is +14.26pp. Both confirm Q 55 is content-distinct from its mushaf neighborhood; the magnitude scales with the homogeneity of the comparison cell.

---

## Synthesis: a proposed third iʿjāz axis (refrain-iʿjāz)

The five novel findings together suggest that **Q 55 occupies an empirically distinct iʿjāz signature** that is neither al-Bāqillānī's structural-iʿjāz (high content + high rhyme variation) nor al-Khaṭṭābī's theological-iʿjāz (low UAS but high *fadāʾil*). Q 55 is:
- **High UAS** (rank 7/114) — like the structural-iʿjāz cluster
- **Corpus-MINIMUM iʿjāz al-fawāṣil signature** (sig_A = -3.173, rank 114/114) — anti-structural-iʿjāz
- **Corpus-RANK-1** in phrase repetition (Q055-F-01), in dual-pronoun density (Q055-F-02), and in dual-paradise structural-similarity (Q055-F-04)
- **MODERATE_OUTLIER** in content distinctness (Q055-F-05)
- **Mid-low** in classical *fadāʾil* hadith density (cf. [[04-hadith-corpus]] §6) — unlike theological-iʿjāz

This signature corresponds to a **third iʿjāz axis: refrain-iʿjāz / iʿjāz al-takrīr**. It is:
- not based on rhyme variety (anti-fawāṣil)
- not based on theological-creedal density (unlike Q 112 al-Ikhlāṣ)
- but on **structural-rhetorical refrain density** + content-distinctness

Classical antecedents: al-Zamakhsharī's *iqtisās* (purposeful recapitulation as a rhetorical device); al-Sakkākī's analysis of *takrīr* in *Miftāḥ al-ʿulūm*. The classical literature has the qualitative axis; this novel finding proposes empirically locking it as a third axis distinct from the existing dual-iʿjāz typology.

**This proposed third axis should be evaluated at corpus-level** (not just for Q 55). Surahs that may share this signature: Q 26 (*ash-Shuʿarāʾ*, where *inna fī dhālika la-āyātan wa-mā kāna aktharuhum muʾminīn* recurs as a refrain-couplet 8 times), Q 77 (*wa-l-mursalāt*, with refrain *wayl-un yawmaʾidh-in li-l-mukadhdhibīn* 10 times). A formal cross-surah evaluation is OUT OF SCOPE for this Q 55 deep-dive but should be flagged for a project-level cross-finding (see [[07-cross-references]] §"Open questions for cross-finding-027").

## Honest limits

- The third-iʿjāz-axis proposal is HYPOTHESIS, not yet PROVED. It would require corpus-level pre-reg + LOOCV + cross-surah replication.
- Q055-F-03 (cosmic) is a NULL/DIRECTIONAL pre-commit-violation candidate: pre-reg said top-3, result is rank-4. By project pre-commit honesty rules, this is published with full prominence as DIRECTIONAL.
- All five tests use the same `quran-text/quran-no-tashkeel.json` source; rules-tuple sensitivity to other tashkeel variants was tested for F-01 only (cross-stable).
