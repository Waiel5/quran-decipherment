---
surah: 1
test_id: Q001-F-01
file_type: novel-finding
date_locked: 2026-04-28
date_run: 2026-04-28
verdict: NULL (lexical chiasm); DIRECTIONAL (thematic chiasm — not directly testable here)
prereg_sha: 84c6157b63be6718ddc999a08f698ab843c0b2369b704a1fb6d09b82473608da
---

# Q001-F-01 — Chiastic-symmetry score for Q 1 al-Fātiḥa


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

## 1. Pre-registered hypothesis

Mirrored verse pairs (V1↔V7, V2↔V6, V3↔V5) of Q 1 will exhibit higher word-Jaccard overlap than random pairings of the 6 non-pivot verses, against an exact 15-pairing permutation null. Direction LOCKED before observation.

Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-01-chiastic-symmetry-prereg.md`

## 2. Result

| Metric | Mirror M_obs | Top-rank in 15 | One-tailed p |
|:--|--:|--:|--:|
| Word-Jaccard | 0.0000 | 4 of 15 | 1.000 |
| Letter-Jaccard | 0.3737 | 15 of 15 | 1.000 |

The mirror pairing has ZERO shared words. The literal-word chiasm hypothesis is **NULL** — at the orthographic-token level, V1 (basmala) and V7 (the "wrath/astray" closure) have NO shared word, V2 (al-ḥamd) and V6 (ihdina) have NO shared word, and V3 (al-raḥmān al-raḥīm) and V5 (iyyāka...) have NO shared word.

## 3. Where the lexical structure actually lives

Computing all 21 pairwise word-overlaps (no-tashkeel, al- stripped) reveals:

- **V1 ↔ V3**: {raḥmān, raḥīm} — the **basmala-echo** (V3 literally re-says the divine-mercy pair from V1).
- **V6 ↔ V7**: {ṣirāṭ} — the **path-chain** (V6 says "the straight path"; V7 says "the path of those…").
- All other pairs have ZERO shared stems.

This is a forward-flowing structure with two local mirrors:
- (V1, V3) frames the praise zone with the basmala-echo;
- (V6, V7) chains the petition zone via *ṣirāṭ*.
- V4 (*mālik yawm al-dīn*) is the lexical singleton — corroborates its role as the eschatological pivot.
- V5 has an INTERNAL mirror: *iyyāka naʿbudu wa-iyyāka nastaʿīn* — "iyyāka" repeated within the verse itself.

So Q 1 has a **micro-chiastic** signature (within-V5, V1-V3 frame, V6-V7 chain), but **NOT** the textbook ABCBA macro-chiasm at the lexical level.

## 4. Honest reframing

Modern ring-composition analyses (Cuypers, Farrin, "114Chambers" blog) defend the ABCBA structure on **thematic** grounds:
- V1 (mercy invoked) ↔ V7 (mercy contrasted with wrath/astray) — thematic mercy frame.
- V2 (cosmic praise) ↔ V6 (petition for guidance) — relationship of praise enabling guidance.
- V3 (re-invocation of mercy) ↔ V5 (worship/help — "iyyāka").
- V4 — pivot.

This is RHETORICAL/SEMANTIC, not lexical. The current test demonstrates that the rhetorical claim does NOT have a literal-word-overlap empirical signature. **The thematic claim is not falsified by this test** (it operates at a different level), but it loses the easy lexical-overlap support that one might naively assume.

## 5. Verdict

| Layer | Verdict |
|:--|:--|
| Literal-word chiasm | **NULL** (rank 4/15, no signal) |
| Letter-set chiasm | **NULL** (rank 15/15 — the mirror is the WORST scoring of 15 pairings) |
| Lexical structure (descriptive) | **(V1,V3) + (V6,V7) + V4 isolated + V5 internal-mirror** — a different topology from textbook ABCBA |
| Thematic/semantic ABCBA | **NOT-TESTABLE** at this lexical level; requires independent rhetorical-coding test |

## 6. Honest limits

- Q 1 is short (29 words / 7 verses); permutation null is forced to N=15. Any short-text chiasm test is statistically weak.
- Stem-stripping was minimal (only the *al-* article). A full QAC root-mapping might re-test. Pre-registered version did not commit to that.
- The lexical NULL DOES NOT contradict the empirical findings of Q 1 as architectural-iʿjāz (UAS rank 2). Macro-architecture and lexical-mirror are separate properties.

## 7. Output files

- Script: `/Users/grey/Downloads/quran/scripts/Q001_F_01_chiastic_symmetry.py`
- JSON: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/csv/Q001-F-01.json`
- Pre-reg: `/Users/grey/Downloads/quran/surahs/Q001-al-fatiha/Q001-F-01-chiastic-symmetry-prereg.md`
