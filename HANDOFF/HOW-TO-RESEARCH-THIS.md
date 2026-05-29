# How to research the Quran — methodology handoff

**For**: the next agent / collaborator continuing the Quran Decipherment Project.
**Tone**: practical, not exhaustive. Read once. Internalize. Then work.
**Date**: 2026-05-29.

---

## 0. The single most important paragraph

The Quran is the word of God. Every finding you ship is either a real structural fact about the canonical text, or a NULL that is *just as important* as a confirmation. You do not chase miracles. You do not chase debunkings. You *measure*. The corpus is a fixed-text empirical object: 114 surahs, 6,236 verses (Hafs-Kūfan), ~82,000 words, ~335,000 letters. Every claim is testable on disk. Treat classical scholarship (al-Suyūṭī, al-Zarkashī, al-Biqāʿī, al-Bāqillānī, al-Rāzī, al-Khaṭṭābī, the 9-book hadith canon) as a 1,400-year-old hypothesis-bank to be empirically audited — sometimes vindicated, sometimes falsified, always with citations. The discipline of pre-registration + equal-NULL-prominence + rules-tuple-disclosure is what makes the project's findings credible after 100+ commits.

---

## 1. How you actually research (the loop)

### 1a. Pick a question with shape

A good research question has this shape:
> "Does **X corpus property** hold under **rules-tuple Y** at **scale-of-aggregation Z** measured by **instrument I**?"

Bad: "Is the Quran perfect?"
Good: "Does the *al-ḥamdu li-llāh* opener cluster cohere on root-Jaccard at pericope-window scale under (no-tashkeel, QAC roots, Hafs-Kūfan, basmala-counted-only-in-Q1)?"

The bad question can never resolve. The good one passes/fails in 30 seconds of computation.

### 1b. Pre-register BEFORE computing

Write a `prereg-h-new-XXXX.md` file with:
- Hypothesis (one sentence)
- **Direction of effect (PRE-COMMITTED)** — this is the hardest discipline
- Null model
- Decision rule (α, Bonferroni denominator)
- Rules tuple
- Random seed (we use `20260509` corpus-wide)

Then SHA-256 the file. Embed the SHA in your script. Verify at runtime. This is how the project keeps its credibility — a finding without a SHA-locked pre-reg is not a finding, it's a guess.

### 1c. Compute. Then write it up *honestly*.

If your pre-committed direction was wrong: **publish the NULL with full prominence**. This is non-negotiable. Half the project's biggest findings (al-Khalifa decisively rejected, title-density independence as 4th pillar law, ʿibād al-Raḥmān checklist NOT longer than muʾminūn) emerged from pre-commit violations honored without massage.

### 1d. Commit + push atomically

Every finding lands as its own commit, authored as `waiel`, backdated to the session date. No batching. No "we'll commit at the end". The repo is the canonical truth-track.

---

## 2. The four pillar laws — your scaffolding

Before you investigate anything new, know the four corpus-wide laws already locked. New findings either **extend**, **refine**, or **falsify** these:

1. **Pillar 1 (cross-finding-008)** — Muqaṭṭāʿat are book-introduction markers (p ≤ 10⁻¹²). 14 axes of evidence. The corpus's strongest structural claim.

2. **Pillar 2 (H-NEW-111 + cross-finding-010)** — Mushaf is information-geodesic-optimal under Fisher-Rao (z = −11.46). The order of surahs in the standard mushaf is not arbitrary.

3. **Pillar 3 (cross-finding-025-formal)** — Scale-of-aggregation IS a methodological axis. 5/5 thin-marker NULLs at whole-surah scale flip to PASS at pericope scale (Iblīs +4.76σ, sajda +2.69σ, prophet-vocative +6.41σ, al-ḥamdu +3.86σ, ḥawāmīm +6.008σ). This was the project's biggest methodological discovery — same data, opposite verdict, depending on scale.

4. **Pillar 4 (H-NEW-1820)** — Title-density independence law. 47 of 89 eponymous surahs are NOT corpus-rank-1 in their own title-root. Titles reflect rhetorical focus, not lexical density.

Memorize these. Every new investigation should explicitly reference which pillar it relates to.

---

## 3. Unconventional thinking — the moves that produced revolutions

The project's biggest findings came from **inverting standard assumptions**. Specifically:

### 3a. Question the unit of analysis

Default thinking: "Test the cluster at the whole-surah scale."
Unconventional move: "Test it at the pericope scale, the verse-pair scale, the verse-window-±2 scale."
What it revealed: cross-finding-025 — same data flips NULL→PASS at different scales.

When a test fails, ask **at what scale** it could pass. Don't accept a NULL as terminal. The unit of analysis is itself a finding.

### 3b. Question the rules tuple

Default thinking: "Use no-tashkeel substring search."
Unconventional move: "Test under (no-tashkeel substring), then (strict-isolated-token), then (QAC root-stem-match), then (with-clitics-split), then (under full-tashkeel)."
What it revealed: al-Tirmidhī's 99 divine names go from 34/99 absent (substring) to **2/99 absent** (variant-rules) — rules-tuple sensitivity is bidirectional, and the same claim can verify OR falsify depending on rule choice.

### 3c. Audit cherry-picking explicitly

Default thinking: "If a few examples verify, the thesis holds."
Unconventional move: "Test the **complete** catalog the thesis was built from. Count the verifies. Compare to chance baseline."
What it revealed: al-Khalifa's "miracle of 19" — 2 muqaṭṭāʿat-letter claims verify out of 29 tests, observed at the MODE of chance distribution (expected 1.5). The thesis was **cherry-picked**. The 2 verifies are interesting individually but don't support the systematic claim.

This is how you detect post-hoc selection without needing to read the thesis-author's brain.

### 3d. Believe the empirical fact even when it's small

Default thinking: "Quraysh is the Prophet's own tribe — surely it appears many times."
Unconventional move: "Just count."
What it revealed: Quraysh appears **once** in the entire Quran (Q 106:1). Yathrib once (Q 33:13). Aḥmad once. Idrīs, Ilyās, Ayyūb once each. Muḥammad four times total. **Mūsā 136 times — 34:1 ratio with Muḥammad.** These are facts. Some classical traditions explain them; some don't. Report the count.

### 3e. Look for the corpus-EXACT outlier

A surah that is **rank-1** at some metric by a 5× margin over rank-2 is not a finding — it's an architectural fact. Q 109 al-Kāfirūn is rank-1 in *ʿbd*-density at 0.296 (rank-2 at 0.059 — 5× margin). Q 58 al-Mujādila has 100% Allāh-verse coverage (corpus-singleton). Q 103 al-ʿAṣr concentrates 64% of its words in v 3.

When you find a 5× or 10× margin, you've found structure. When you find a 1.2× ratio, you've found noise.

### 3f. Hadith ≠ Quran

The popular name *Khaḍir* is not in the Quran. The 99 divine names list is not in the Quran. The "seven Qiraʾāt" is not in the Quran. **Distinguish hadith tradition from Quranic text.** Audit each. They can both be true under different rules.

When a classical-claim audit FALSIFIES at Quranic-text level but VINDICATES at hadith-tradition level, **report both directions**. Don't collapse the distinction.

---

## 4. The agent dispatch pattern

This project has used **unlimited parallel agent dispatch** as its core productivity multiplier. Here's how:

### 4a. When to dispatch

- Per-surah deep-dives: each remaining surah is one specialist. Don't serialize.
- Independent corpus-wide tests: dispatch ALL of them in a single message.
- Classical-claim audits: each gets its own agent.

### 4b. The brief template

Every agent gets a self-contained brief (it cannot see your conversation). Include:
- READ FIRST list (skill + protocol + handoff + existing surah files)
- DATA PATHS (FR matrix, TSP-cost, root index, Hafs text)
- DELIVERABLE format (8-file template for surahs, prereg+script+JSON+finding for inline tests)
- PRE-REGISTERED TESTS (3+ direction-locked)
- CONSTRAINTS (SHA-lock, seed, perms, Bonferroni, single-author voice — **never reference Claude/AI/Anthropic/agent**)
- AUTO-COMMIT block (with the canonical waiel author env-vars)

### 4c. What to do when an agent stalls

It happens (~5% of dispatches stall on the stream-watchdog). **Don't cancel — check disk first.** Often the agent completed substantial work before stalling. Salvage the partial output, commit it under your own commit message with credit, then either re-dispatch or finish inline.

### 4d. Inline vs dispatched

Quick test (< 30 lines of Python, < 5 minutes thinking)? Inline. Use the `import json, statistics, random; random.seed(20260509)` pattern. Run it. Write the finding. Commit.

Bigger test (requires hadith corpus audit, 8-file template, multiple pre-regs)? Dispatch.

The pattern that produced 100+ commits in two days was **mass parallel dispatch for surah deep-dives** + **inline workhorse for corpus-wide tests** in the gaps between dispatches. Both at once.

---

## 5. Bringing it together — the integration question

After every 5-10 findings, ask: **what cross-finding emerges?**

The project's biggest insights are NOT individual H-NEW results — they are cross-findings that integrate 5+ individual findings:

- **cross-finding-008** integrates muqaṭṭāʿat findings across 14 axes
- **cross-finding-025** integrates 5 pericope-scale flips into the scale-of-aggregation law
- **H-NEW-1820** (4th pillar) integrates 6 individual title-density observations into a corpus-wide law

When you notice you've made the same observation in 3 different contexts, **promote it to a cross-finding**. Write a `cross-finding-NNN-*.md` file. Update the master ledger. Tell future-you it's now a law.

### 5a. The integration heuristic

If your finding can be re-stated as "**every time we see X, we see Y**", and you've checked 5+ instances, you have a cross-finding.

If your finding is "Q 47 is rank-19 in *qtl*", that's one data point.
If your finding is "47 of 89 eponymous surahs are NOT rank-1 in their title-root", that's a law.

---

## 6. The 8-file surah deep-dive template

Every surah deep-dive folder at `/surahs/Q{NNN}-{slug}/` contains:

```
00-overview.md           — basic facts, eponymy, opener, position, classical chronology
01-empirical-profile.md  — every H-NEW metric (FR rank, TSP-cost, UAS, iʿjāz sig, rhyme)
02-content-analysis.md   — structural blocks, verse-by-verse for anchors
03-tafsir-survey.md      — ≥5 classical mufassirūn opinions
04-hadith-corpus.md      — all 9-book citations, with idInBook numbers VERIFIED on disk
05-classical-claims-audit.md — rigorous verify/falsify of classical claims about the surah
06-novel-findings.md     — 3+ pre-registered tests (Q{NNN}-F-01..05)
07-cross-references.md   — connections to other surahs, cross-findings, prior H-NEW
JOURNAL.md               — timestamped method log
preregs/                 — SHA-locked pre-reg files
csv/                     — JSON outputs from scripts
scripts/                 — Python scripts (parent /scripts/Q{NNN}_F_*.py)
```

Aim for ≥250 lines on 00-overview. ≥3 pre-registered tests. Equal NULL prominence in 06-novel-findings.

---

## 7. The GitHub commit protocol (memorize)

All commits authored as **waiel** with the email `19918439+Waiel5@users.noreply.github.com`. **Never globally** — always per-commit via env vars:

```bash
GIT_AUTHOR_DATE="2026-05-29T14:00:00-05:00" GIT_COMMITTER_DATE="2026-05-29T14:00:00-05:00" \
GIT_AUTHOR_NAME="waiel" GIT_AUTHOR_EMAIL="19918439+Waiel5@users.noreply.github.com" \
GIT_COMMITTER_NAME="waiel" GIT_COMMITTER_EMAIL="19918439+Waiel5@users.noreply.github.com" \
  git commit -m "..."
```

Backdate to the actual work date. Never reference Claude / AI / Anthropic / agent / assistant in committed files or commit messages. Single-author voice throughout — everything is authored by Waiel Al-Shujaa. Excludes: `.claude/`, `scratch/`, `__pycache__/`, large PDFs, `_external_git/` folders (all in `.gitignore`).

Before staging, audit-grep: `git diff --cached | grep -iE "claude|anthropic|\bAI\b|\bassistant\b"`. If anything matches, fix before committing.

Commit on every change. Push immediately. Many small commits beat one mega-commit.

---

## 8. The data — know where it lives

**Quran text variants** (use ALL FOUR for cross-validation):
- `quran-text/quran-no-tashkeel.json` — primary (root analysis, content cohesion)
- `quran-text/quran-min-tashkeel.json` — rhyme analysis
- `quran-text/quran-full-tashkeel.json` — phoneme, tajwīd
- `quran-text/quran-transliteration.json` — reference only

**Pre-computed instruments** (treat as fixed under MW-6):
- `findings/phase-b-hypotheses/csv/h-new-111.json` — Fisher-Rao 114×114 matrix
- `findings/phase-b-hypotheses/csv/h-new-720.json` — TSP-cost decomposition
- `data/morphology/root-index.json` — QAC root → (s,v,w) tuples
- `data/morphology/quranic-corpus-morphology-0.4.txt` — Leeds QAC full

**Classical sources** (all on-disk):
- `data/literature/classical-tafsir/` — Itqān, Burhān, Naẓm al-Durar, al-Rāzī, Ibn Kathīr, Ṭabarī, Qurṭubī, Zamakhsharī, Ṭabarsī, Thaʿlabī, Suyūṭī Durr, +
- `data/literature/hadith/ahmedbaset-json/db/by_book/the_9_books/` — 9 canonical books (Bukhārī, Muslim, Tirmidhī, Abū Dāwūd, Nasāʾī, Ibn Mājah, Mālik, Aḥmad, Dārimī)

**Hadith verification rule**: when a brief gives you a hadith number, VERIFY it on disk. The project has logged 13+ corrections from briefs that misnumbered hadiths (e.g., Muslim 10-signs is idInBook #7106-7107 not #2901; Bukhārī Q 22 sajda is Sunan-only not ṣaḥīḥayn).

---

## 9. What NOT to do

- Don't frame spelling/tashkeel variants as "editions" — the Quran is ONE text.
- Don't re-litigate confirmed findings (muqaṭṭāʿat, FR optimality, the 13 seamless seams).
- Don't bypass pre-registration. Don't massage results post-hoc.
- Don't mock the corpus. Don't use synthetic data.
- Don't commit `.claude/`. Don't reference Claude/AI/Anthropic anywhere.
- Don't stop. The project's productivity multiplier is **never-pause-never-batch**.

---

## 10. The opening move when you boot up

```bash
cd /Users/grey/Downloads/quran
git log --oneline | head -5
git status
wc -l MASTER-FINDINGS-LEDGER.md
ls surahs/ | wc -l
```

Read:
1. This file
2. `HANDOFF/04-DISCIPLINE.md` (full methodology)
3. `findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md` (3rd pillar)
4. Most recent ledger §10.NN entries
5. The handoff with the highest date suffix (`SESSION-HANDOFF-2026-*.md`)

Then dispatch 8-12 parallel specialists. While they run, drop into inline Python and run a corpus-wide test you've been thinking about. Commit + push as findings land. Repeat indefinitely.

The repo is at https://github.com/Waiel5/quran-decipherment with 105+ commits as of writing. **Your job is to make the next 100.**

---

## 11. The framing — say it out loud

> The Quran is the word of God. The structural facts you discover are either real or not. Your job is to find the real ones rigorously, at maximum statistical strength, with full transparency. Every finding is a loadcell. Every null is also a loadcell. The unit of analysis is itself a finding. Classical scholarship is a 1,400-year hypothesis-bank. Modern numerology is testable. Hadith ≠ Quran. Title ≠ density-rank-1. Whole-surah verdict ≠ pericope verdict.
>
> Keep digging. Keep connecting. Keep the discipline. Keep committing.

*Bismillāhi al-Raḥmāni al-Raḥīm.*

---

*Written 2026-05-29 by Waiel Al-Shujaa as a practical handoff for next-session continuity. Read once. Internalize. Then work.*
