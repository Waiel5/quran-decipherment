# CONTINUE-PROMPT — paste this to launch a full-power session

> **⛔ READ FIRST: [`../STATE-OF-THE-PROJECT-2026-08-07.md`](../STATE-OF-THE-PROJECT-2026-08-07.md)** —
> on 2026-08-07 thirteen standing laws met their first matched Arabic control and almost none
> survived (H-NEW-2680, H-NEW-2720). Anything below that predates 2026-08-07 must be read
> against that document.



> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

Copy everything between the lines as your first message.

---

You are continuing the **Quran Decipherment Project** at `/Users/grey/Downloads/quran/` — a long-running, rigorous empirical analysis of the Quran, the word of God. The repo is live at https://github.com/Waiel5/quran-decipherment with 125+ commits. Your job is to **keep discovering real structural facts about the text, verify them from every angle, and commit everything as you go. Do not stop. Do not ask permission. Do not pause to summarize — commit and push each finding the moment it lands, then launch the next wave.**

## Authorization (explicit and standing)

- **Unlimited parallel agents.** Launch 10-15+ specialists per wave, in a single message, running in the background. "Thousands" is authorized. Use them aggressively and continuously.
- **Maximum thinking / maximum power.** Think hard about each design before dispatching. Use the deepest reasoning on hypothesis design, null models, and integration. Spare nothing.
- **Unlimited tokens.** Cost is not a constraint. Exhaustiveness is the goal.
- **Commit everything appropriately** (protocol below). Every finding, every NULL, every audit — pushed live.

## First, orient (read these in order)

1. `.claude/skills/quran-investigation/SKILL.md` — invoke the `quran-investigation` skill first
2. `HANDOFF/HOW-TO-RESEARCH-THIS.md` — the methodology (read fully)
3. `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md` — operational playbook
4. `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` — **read this before any of the "laws" below**; three of the four pillars fell to the genre control on 2026-08-07
5. `findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md` — the pericope-flip rule (5 flips, not 6 — `cf-026-formal` retired the 6th). A sound *methodological* rule; **not** evidence about this corpus: poetry flips 5/5 and Bukhārī 4/5 under the same test
5. `MASTER-FINDINGS-LEDGER.md` — the live ledger (tail = §10.81; read the recent §10.7x-10.8x entries)
6. Memory at `/Users/grey/.claude/projects/-Users-grey-Downloads-quran/memory/` (all files)

## The two research modes — run BOTH, lead with #2 when #1 stalls

1. **Broad instruments** — Fisher-Rao distance, clustering, TSP-geometry, UAS. Good for corpus/region/surah scale. Already mature.
2. **Close-reading + exhaustive GENERATORS** — this is the edge. Don't test priors; **scan the whole hypothesis space, let the data surface candidates, then pre-register and null-test the survivors.** Close-reading works aya-by-aya / verse-run / within-verse — invisible to broad metrics. The generator approach is how you find things nobody told you to look for.

The scale-ladder, all live: **corpus → region → surah → pericope → verse-run → verse → within-verse.** Content structure is **pericope-scoped, not surah-scoped** (cross-finding-025, 5 flips). When any test NULLs at one scale, re-test at the scale where the structure actually operates — that rule is sound and stays. **But do not report a pericope flip as evidence that this corpus is special:** the same test flips 5/5 on pre-Islamic poetry and 4/5 on al-Bukhārī (H-NEW-2680). The mechanism is topical burstiness, which every text has.

## The pillar laws — ⛔ THREE OF FOUR FELL ON 2026-08-07. READ THIS BEFORE CITING ANY OF THEM.

> **The genre control that should have existed years ago was finally run.** Both baseline corpora
> (al-Bukhārī, pre-Islamic dīwāns) were cut into 114 pseudo-surahs matching the Qurʾān's length
> profile, and each law was re-run on them through an instrument-matched pipeline.
> **Poetry satisfies 3 of the 4; al-Bukhārī satisfies 2. Only Pillar 1 discriminates.**
> Read `findings/PILLAR-LAW-CORRECTION-2026-08-07.md` before building on any of this, and
> `findings/phase-b-hypotheses/h-new-2680-pillar-conjunction.md` for the evidence.

The original list is kept below exactly as it stood, with the correction against each item.

1. **Muqaṭṭāʿat are book-introduction markers (p ≤ 10⁻¹²)** — ✅ **STANDS.** The only law neither
   baseline satisfies. Honest qualification: the baselines have almost nothing to find (6 Bukhārī
   and 1 poetry pseudo-surah mention *kitāb*/*qurʾān* at their openings), so the pass is partly
   definitional rather than a fully discriminating test.
2. ~~Mushaf is information-geodesic-optimal under Fisher-Rao (z = −11.46)~~ — ⛔ **DOES NOT
   DISCRIMINATE.** Both baselines score MORE extreme (Bukhārī z = −13.84, poetry z = −15.13, Qurʾān
   z = −11.50). Arbitrary cuts of the Qurʾān's own verse stream that ignore every surah seam score
   z = −11.23 to −13.18. And length-sorting alone — no vocabulary at all — already reaches z = −8.66
   (H-NEW-111's write-up mis-transcribes this anchor as 107.27; its own JSON says 91.03). **The
   mushaf's honest margin over pure length-sorting is 2.80 σ, not 11.46 σ.** What still stands is
   the relative claim: mushaf < Nöldeke < Tanzil.
3. ~~Scale-of-aggregation is itself a finding axis (6/6 pericope-flips)~~ — ⛔ **DOES NOT
   DISCRIMINATE.** Poetry flips 5/5, al-Bukhārī 4/5. The mechanism is topical burstiness, which
   every text has. It also has ZERO purchase as evidence: the statistic is mathematically invariant
   under every redactional randomisation. **Still a correct methodological rule — test at the scale
   where structure operates — but not evidence about this corpus.** (The roster is 5, not 6:
   `cf-026-formal` retired the ring-composition member in May.)
4. ~~Title-density independence~~ — ⛔ **WITHDRAWN 2026-08-07**, replaced by
   `h-new-2710-title-density-retest.md` (TOPICALITY-EXPLAINED). The 48/89 correction was invalid
   (cross-metric); 47/89 restored as a description only. Both the original law and its proposed
   inversion are wrong: once topicality and rarity are controlled the residual is a rate ratio of
   1.285 and median rank is indistinguishable (p = 0.76). Do not cite as a law.

**And do not multiply these p-values.** Formally established 2026-08-07: the four nulls randomise
different things and are not commensurable. Surah-order permutation — Pillar 2's null — leaves the
other three *exactly* unchanged. Any document that says the laws "jointly" establish something is
asserting something now shown to be unlicensed.

## The discipline (non-negotiable)

- **Pre-register before computing.** SHA-256-lock the pre-reg, embed the SHA in the script, verify at runtime. Direction-of-effect locked BEFORE seeing results. Reversed direction → publish as NULL with full prominence (never massage).
- **Equal NULL prominence.** A null is a loadcell. Half the project's biggest findings are honored pre-commit violations.
- **Rules-tuple disclosed** on every claim; test under ≥2 tuples (bidirectional sensitivity — disambiguation can rescue OR retire a claim; raw substring-counting LIES, use QAC lemma).
- **Bonferroni** for multiple-comparison families. Seed = `20260509`, 10000 perms.
- **CONFIRMED-BUT-MEANINGLESS** is a real verdict (a number can equal its chance-expected value). The numerology is retired (balanced-words, abjad, Code-19, surah-arithmetic — all NULL via proper nulls); the rhetoric is real (anaphora, reduplication, fawāṣil-grammar, prayer-clusters, rings-at-pericope-scale).
- **Hadith ≠ Quran.** Distinguish text-claims from tradition-claims; verify every hadith number on disk (13+ corrections logged so far).

## High-EV targets for the next waves

**Close-reading generators (the edge):**
- QAC-lemma re-run of the H-NEW-2000 numerical-symmetry series (disambiguated — raw substring was unreliable; see kallā case §10.80)
- Pericope-scale ring-composition sweep across ALL surahs (Q 2 qibla-block passed at z=+3.69; find the others)
- Verse-pair chiasmus / mirror-structure within pericopes
- Cohesion / parallelism in the prophet-cycle pericopes (Mūsā, Ibrāhīm, Nūḥ pericopes across surahs)
- Conjunction / particle-cascade structures (fa-, thumma-, wa-idhā- chains) beyond anaphora
- Grammatical-person shifts (iltifāt) corpus mapping — a major balāgha device never enumerated
- Oath-and-response (qasam / jawāb al-qasam) structural inventory
- Verse-final assonance classes (long-vowel rhyme beyond single-letter rāwī)

**Surah deep-dives still pending or partial:** any remaining surah without a full 8-file template; complete the partial Wave-3 surahs.

**Classical-claim audits (verify/falsify on conventional routes):**
- al-Biqāʿī munāsabah (inter-surah coherence) claims, pericope-scoped
- al-Suyūṭī Itqān distributional claims (like the kallā / fawātiḥ census ones — many are testable)
- The remaining iʿjāz claims (al-Bāqillānī fawāṣil, al-Khaṭṭābī theological-iʿjāz)

**Integration:** every 5-10 findings, promote convergent observations to a cross-finding law. When you've seen the same pattern in 5+ contexts, it's a law — write it up.

## The commit protocol (memorize — CRITICAL)

Every commit authored as **waiel**, per-commit env-vars (never global), backdated to the work date:

```bash
GIT_AUTHOR_DATE="<work-date>T<HH:MM>:00-05:00" GIT_COMMITTER_DATE="<same>" \
GIT_AUTHOR_NAME="waiel" GIT_AUTHOR_EMAIL="19918439+Waiel5@users.noreply.github.com" \
GIT_COMMITTER_NAME="waiel" GIT_COMMITTER_EMAIL="19918439+Waiel5@users.noreply.github.com" \
  git commit -m "..."
git push
```

- **Never reference Claude / AI / Anthropic / agent / assistant** anywhere in committed files or commit messages. Single-author voice — everything is by Waiel Al-Shujaa.
- Audit before staging: `git diff --cached | grep -iE "claude|anthropic|\bassistant\b"` → fix any match.
- Never commit `.claude/` or `scratch/` (in `.gitignore`).
- Commit on every change. Push immediately. Many small atomic commits beat one mega-commit.
- Use `TaskCreate` to track each wave; mark in_progress / completed as you go.

## The framing

> The Quran is the word of God. The structural facts you discover are either real or not. Find the real ones rigorously, at maximum statistical strength, with full transparency. Every finding is a loadcell; every null is a loadcell. The unit of analysis is itself a finding. The numerology is retired; the rhetoric is real. The generators find what nobody told you to look for.

Now: invoke the skill, read the orientation files, then **immediately dispatch a wave of 10-15 parallel agents** — a mix of close-reading generators, pericope-scale tests, surah deep-dives, and classical-claim audits — while you run inline close-reading scans yourself in the gaps. Commit and push each finding atomically. Then launch the next wave. Keep digging. Keep connecting. Keep the discipline. Keep committing. Do not stop.

`git push` is your heartbeat.

---

*CONTINUE-PROMPT written 2026-05-29 by Waiel Al-Shujaa. Paste at session start for full-power continuation.*

---

## STANDING RULES added 2026-08-07 (Wave-S) — these are non-negotiable, learned the hard way

Four failures were committed and self-reported in a single night. Do not repeat them.

1. **The runner's verdict rule MUST literally match the pre-registration's decision rule.** H-NEW-2600 pre-registered "correct sign AND both raw p < 0.0005 per arm", then the script implemented something looser and published a verdict that failed its own gate. **Before any run, diff the script's verdict function against the prereg's decision section, line by line.** A pre-registration you quietly loosen in code is not a pre-registration.
2. **NEVER delete a run directory — including uncommitted, superseded, byte-identical ones.** One was deleted mid-audit on the reasoning that it was identical to its replacement. "It was identical" is exactly the claim an audit trail exists to let a third party verify. If a manifest records a non-portable path, **re-run to an ADDITIONAL directory and retain both**, recording why.
3. **Never ASSERT a robustness property — COMPUTE it.** H-NEW-2560's output claimed an arm was "independent of EQTB sentence segmentation". Never tested, and false — restricted to sentence-internal marks the locked direction failed at p=0.97 and trended reversed. It cost the headline.
4. **Check every control for tautology.** "17/34 form-pairs positive, a coin flip" was offered as evidence of instrument neutrality; the lattice contains both A→B and B→A and T(B,A) = −T(A,B), so exactly half MUST be positive. Arithmetic is not evidence.

**Two further habits:**
- **Hunt errors whose direction FLATTERS the hypothesis first.** A formal law carried 47/89 for three months after its own follow-up corrected it to 48/89 — precisely because the correction made the law stronger and so nobody re-checked it.
- **Bonferroni answers a UNION question ("did any test hit?"). It cannot answer the INTERSECTION question ("how many configurations satisfy ALL properties at once?").** When several properties hold of one object, compute the joint survivor count — with the property list pre-declared, a shrinkage curve under several orderings, an independence matrix, and **a control running the identical procedure on random/baseline objects.** Without that control, constraint-stacking manufactures uniqueness and you have reinvented numerology.

## New instruments and assets as of 2026-08-07

- **Dependency treebank (EQTB)** — acquire per `data/syntax/UD-QURAN-SOURCE.md`. **Parser-contaminated for morphology questions** (its syntax was BiLSTM-generated with morphological-feature inputs including `verb_form`; human validation was not form-blinded), and its sentence segmentation may have used verse boundaries. Parse/join code: `scripts/h-new-2540.py`.
- **The parser-free channel** — attached object pronouns from QAC alone. Correct rule: consume only the obligatory subject suffix, THEN count remaining `PRON` segments. Do NOT drop every pronoun matching subject PNG — that deletes 311 genuine objects and the miss rate is form-correlated.
- **`HANDOFF/FRONTIER-MAP-2026-08-07.md`** — coverage census over all ~900 phase-b files, 20 ranked untouched hypotheses with verified data paths and named confounds, contradiction audit, and an inventory of acquired-but-unread assets. **Read this before choosing a target.**
- **`findings/CROSS-FINDING-INDEX.md`** — disambiguation for the duplicate cross-finding IDs (025-028 and 010/012/023 collide across two directories).
- **Idle assets worth opening:** 12-edition per-verse tafsīr (77,437 files — H-NEW-2620 opened it and got a NULL), al-Wāḥidī *asbāb* (0 scripts), Jeffery loanwords (1 script), `quran-uthmani-txt.txt` (0 scripts).

## The public-facing material needs rebuilding

`EXECUTIVE-SUMMARY.html`, `THE-MAN-AT-THE-CENTER.html`, `Khawatim-al-Hashr.html` and `al-Rajul-fi-Qalb-al-Amr.html` are all dated **2026-04-12** — they predate every cross-finding law. The strongest results (muqaṭṭaʿāt p ≤ 10⁻¹², Q112 as corpus FR-centroid) are buried in a 1.2 MB ledger while the early, more obvious material is what is published. **Rebuild the public face around what has survived audit.** *(Correction 2026-08-07: this line previously headed that list with "mushaf order z = −11.46". That result does not survive the genre control — both baselines score more extreme — and has been removed from the list rather than left standing as a headline. See `findings/PILLAR-LAW-CORRECTION-2026-08-07.md`. The instruction to rebuild the public face around what survives audit is now more urgent, not less.)*
