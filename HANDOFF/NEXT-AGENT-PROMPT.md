# NEXT-AGENT-PROMPT — paste this at session start

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the muqaṭṭaʿāt book-reference LAW SURVIVES; its p = 3.17 × 10⁻¹² does NOT
>
> **This is the only standing claim in the project to have met a null matching the variable
> that drives it, and it passed.** Both halves are separately true and both must travel.
>
> - **The law survives.** 24 of 29 reproduces **exactly**. Against a null that permutes the
>   muqaṭṭaʿāt label *within opening-window-size quintiles* — so the opening-token budget is
>   identical by construction — the observed 24 stands against a null mean of **9.304**: rate
>   ratio **2.580**, z = +7.01, p = 1.0 × 10⁻⁴, eleven above the 95 % band top. **Every**
>   matched null in the ladder still places the observation outside its own 95 % band.
> - **`p = 3.17 × 10⁻¹²` is withdrawn as a description of that strength.** It is
>   arithmetically correct and inferentially void: the hypergeometric draws 29 surahs
>   *uniformly from 114*, which requires the 29 to be exchangeable with the other 85. They are
>   not, and this project established that itself — `h-new-46-muqattaat-vs-surah-length.md` is
>   a STRONG-PASS showing muqaṭṭaʿāt surahs concentrate in **long** surahs. **The honest effect
>   size is a rate ratio between 1.27 and 2.58, not a twelve-order-of-magnitude tail.**
> - **The sharpest form of the law is positional and length-free.** All 29 muqaṭṭaʿāt surahs
>   mention the Book somewhere — so do 40 others — but they place the **first** mention at
>   **0.0996** of the surah against **0.3403** (Δ = −0.2407, p = 5.0 × 10⁻⁴). The law is not
>   "muqaṭṭaʿāt surahs mention the Book"; it is **"muqaṭṭaʿāt surahs announce it at the top."**
>
> **Three qualifications travel with the verdict.** (i) H-NEW-2760's H2 **failed its gate**:
> the nuisance channel it made primary (opening-window size, ρ = +0.1678) is weaker than
> whole-surah length (ρ = +0.4583), and **against that stronger channel the rate ratio is
> 1.694**. (ii) DISCRIMINATES was earned on the within-corpus nulls; in the matched-partition
> genre arm **0 of 3 baselines clear the gate and the poetry arm is a published pre-commit
> violation**. (iii) The cross-genre half remains partly definitional — only 6 al-Bukhārī and
> 1 pre-Islamic-poetry pseudo-surah mention *kitāb*/*qurʾān* in their opening units at all, and
> al-Jāḥiẓ's adab prose yields **الكتاب** among its strongest marker classes.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2760-muqattaat-book-reference-nuisance.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.1.

> ## ⛔ CORRECTION NOTICE — 2026-08-07: the scansion three-way ordering does NOT survive a matched control
>
> H-NEW-2690 reported **poetry < this corpus < prose** on `d_min` and read it as
> al-Bāqillānī's *neither* nathr *nor* shiʿr, measured. H-NEW-2730 genre-controlled it.
> **The ordering falls; one of its two legs survives.**
>
> - **The prose leg (H1b) is WITHDRAWN — it is unit length.** Re-cut **this corpus's own
>   verses** to ḥadīth sentence lengths and `d_min` moves **99.4 %** of the way to ḥadīth's
>   value (0.22222 → 0.23953 against al-Dārimī's native 0.23963), using **no baseline text at
>   all**. A matched partition of al-Dārimī lands at **0.22222** — this corpus's own median to
>   five decimals — and one of al-Bukhārī at **0.21893**, with **199 of 200** offsets at or
>   below it. At matched syllable length the two medians are **identical** (0.21739).
> - **The poetry leg (H1a) SURVIVES every length control.** Length explains **5.1 %** of that
>   gap; re-cutting this corpus to bayt lengths moves it only **7.5 %** toward poetry; it holds
>   at full size in the one overlapping length bin (0.21739 against poetry's 0.14815) and
>   passes a per-unit noise control matched on length *and* syllable weight at p = 1 × 10⁻⁴ in
>   both rules-tuples.
> - **`d_min` is not length-invariant in practice.** Length alone explains **28.7 %** of its
>   variance. It normalises by unit length and tiles its templates to unit length, but it is a
>   minimum over ~200 templates and a minimum-of-many falls as the string shortens.
>   **Normalisation is not invariance.**
> - **Matched noise alone reproduces the ordering.** Random strings matched only on length and
>   syllable weight give poetry 0.22222 < this corpus 0.23913 < al-Bukhārī 0.25992 < al-Dārimī
>   0.26549 — the same three-way order, from strings containing no Arabic and no metre. Only
>   **49.2 %** of this corpus's verses are more metrical than their own matched twin — a coin
>   flip — against **88.3 %** of poetry abyāt.
>
> **al-Bāqillānī is untouched**: "neither *nathr* nor *shiʿr*" was never a claim about medians
> of normalised edit distances. What is withdrawn is half of its stated empirical
> operationalisation. **Limit:** there is **no vocalised adab prose on disk**, so al-Jāḥiẓ is
> untestable on this statistic by any means and the prose control is ḥadīth-only.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2730-scansion-genre-control.md`.
> Orientation: `STATE-OF-THE-PROJECT-2026-08-07.md` §1.5.


> **⛔ READ FIRST: [`../STATE-OF-THE-PROJECT-2026-08-07.md`](../STATE-OF-THE-PROJECT-2026-08-07.md)** —
> on 2026-08-07 thirteen standing laws met their first matched Arabic control and almost none
> survived (H-NEW-2680, H-NEW-2720). Anything below that predates 2026-08-07 must be read
> against that document.


Copy everything between the lines below as your first user message to the next agent.

---

You are continuing the Quran Decipherment Project at `/Users/grey/Downloads/quran/`. This is a long-running, rigorous empirical analysis of the Quran — the word of God — using every computational and statistical tool available, cross-referenced against 1,400 years of classical Islamic scholarship.

**Your task**: Continue the work without stopping. Identify completely new, revolutionary-but-true structural facts about the Quran. Connect dots across the existing 50+ confirmed findings. Solve the Quran's structural equation as a unified whole.

**You have unlimited tokens, unlimited parallel agent dispatch (10-40+ concurrent specialists is normal, "thousands" is authorized), and a user who explicitly does not want you to stop or pause. Commit every finding to GitHub the moment it lands.**

**Read these files in order before doing anything else:**

1. `/Users/grey/Downloads/quran/HANDOFF/SESSION-HANDOFF-2026-05-09.md` ← **START HERE — most recent handoff with full operational playbook + commit protocol + pending high-EV moves**
2. `/Users/grey/Downloads/quran/HANDOFF/README.md` — orientation
3. `/Users/grey/Downloads/quran/HANDOFF/04-DISCIPLINE.md` — methodology rules (MW-1..MW-7, PRE-REG-STANDARDs)
4. `/Users/grey/Downloads/quran/HANDOFF/01-WHAT-WE-KNOW.md` — consolidated findings (Wave-5 baseline)
5. `/Users/grey/Downloads/quran/HANDOFF/02-META-ARCHITECTURE.md` — big-picture synthesis
6. `/Users/grey/Downloads/quran/HANDOFF/03-NEXT-MOVES.md` — queued investigations
7. `/Users/grey/Downloads/quran/HANDOFF/05-OPEN-QUESTIONS.md` — terminal Wave-5 status
8. `/Users/grey/Downloads/quran/MASTER-FINDINGS-LEDGER.md` — the live ledger (2,759 lines, growing)
9. `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/cross-finding-022-wave5-terminal-synthesis.md` — most-recent unified synthesis

**Then**: dispatch 8-20+ parallel specialist agents on the highest-EV remaining surahs (§7 of SESSION-HANDOFF-2026-05-09.md). While they run, INLINE-execute small corpus-wide tests yourself with the FR matrix at `findings/phase-b-hypotheses/csv/h-new-111.json`. Integrate results into cross-findings as they land. Update `MASTER-FINDINGS-LEDGER.md`. Commit + push after every finding.

**Non-negotiable disciplines:**

- The Quran is ONE text — never frame as "editions" or "variants"
- Every novel test is PRE-REGISTERED before null design (PRE-REG-STANDARD-04)
- Every claim carries its rules-tuple
- Every NULL is published with equal prominence to every confirmation
- Post-hoc-noticed findings carry single-test-α=0.05 caps unless replication exists
- MW-1..MW-7 protections are the immune system; do not bypass
- Direction of effect is locked before viewing results (PRE-REG-STANDARD-01)

**The GitHub commit protocol (CRITICAL — see SESSION-HANDOFF-2026-05-09.md §6 for full version):**

- All commits authored as `waiel <19918439+Waiel5@users.noreply.github.com>` via `GIT_AUTHOR_NAME`/`GIT_AUTHOR_EMAIL` env vars
- Backdate commits to actual work-time with `GIT_AUTHOR_DATE`/`GIT_COMMITTER_DATE`
- **Never reference Claude/AI/Anthropic/agent/assistant** in committed files or commit messages — everything is authored by Waiel Al-Shujaa
- **Never commit `.claude/` or `scratch/`** — already in `.gitignore`
- Commit on every change. Push immediately. Many small commits beat one mega-commit.
- Repo: https://github.com/Waiel5/quran-decipherment (public). 30 commits already landed; continue chronologically.

**Your operating tempo:**

- Use parallel specialist dispatch aggressively — the user supports unlimited concurrent agents
- Use TaskCreate to track each specialist + each inline test
- After each finding lands: append to ledger, commit, push, atomically
- Every 5-10 findings: write/update a cross-finding synthesis
- The single most-strongly-supported claim in the project is that **muqaṭṭāʿat are book-introduction markers** (p ≤ 10⁻¹²) — extend; do not relitigate

**The big confirmed findings** (do not re-test these — extend them):

- ~~**H-NEW-111**: mushaf is information-geodesic-optimal under Fisher-Rao (z = −11.46)~~ **⛔ Correction 2026-08-07 — DOES NOT DISCRIMINATE.** Under the first genre control ([[h-new-2680-pillar-conjunction|H-NEW-2680]]) al-Bukhārī reaches z = −13.84 and pre-Islamic poetry z = −15.13 against the Qurʾān's z = −11.50, both closer to their own TSP optima; offset cuts ignoring every surah seam give z = −11.23 to −13.18; length-sorting alone reaches z = −8.66. Honest margin over pure length: **2.80 σ**. The relative claim (mushaf shorter than either chronology) survives. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`.
- **H-NEW-1040**: consecutive-pair FR-mean 17.8% below corpus baseline (z = −11.65)
- **H-NEW-1240**: 13 empirically-seamless mushaf-transitions identified (corpus-EXACT)
- **H-NEW-250**: 14 centuries of classical block-structure Ridge-recoverable at R² = 0.89 LOOCV
- **H-NEW-1190**: *wa-mā adrāka mā* corpus-EXACT 10-surah cluster FR-cohesive (p = 0.00068)
- **H-NEW-1200**: short-Meccan-tail eschatology meta-cluster of 14 surahs (p = 0.00030)
- **H-NEW-1220**: corpus FR-centroid ranking of all 114 surahs (corpus-formal)
- **H-NEW-1250**: Q 55 dual-audience architectural signature (corpus-EXACT)

**The framing**: This is the word of God. The structural facts you discover are either real or not. The project's job is to find the real ones rigorously, at maximum statistical strength, with full transparency.

Every finding is a loadcell. Every null is also a loadcell.

Keep digging. Keep connecting. Keep the discipline. Keep committing.

Now: read the SESSION-HANDOFF-2026-05-09 and DISCIPLINE files, then plan and dispatch your first wave of 8-12 parallel investigations.

---
