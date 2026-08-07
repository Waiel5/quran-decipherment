---
surah: 90
surah_name_ar: البلد
surah_name_translit: al-Balad
file_type: journal
date_last_updated: 2026-05-30
phase: B+
---

# Q 90 al-Balad — Investigation Journal


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

## 2026-05-30 — Full 8-file deep-dive (Wave-N)

### Pre-flight
- Read the quran-investigation skill (`SKILL.md`) + `INVESTIGATION-PROTOCOL.md`.
- Studied exemplars `Q066-al-tahrim/` (all 8 files) + `Q003-al-imran/` for format/rigor standard.
- Target folder `surahs/Q090-al-balad/` was empty (only `csv/`, `preregs/`, `scripts/` stubs).

### Data extraction (all traced to disk)
- Text: `quran-text/quran-no-tashkeel.json` → Q 90 = 20 verses, 82 words, 342 letters, type meccan.
- Chronology: `data/revelation-order.csv` → #35 Early Meccan. Verse count: `data/hafs-verse-counts.tsv`
  line 90 → 20.
- Morphology: `data/morphology/quranic-corpus-morphology-0.4.txt` → 45 distinct QAC-STEM roots, 52 tokens;
  90:1 = `laA(NEG) + uqosimu(V IMPF IV ROOT:qsm 1S)`; 90:4 = `la(EMPH)+qad(CERT)` (jawāb).
- **4 corpus-hapax roots** identified: `kbd, njd, $fh, sgb` (each `root_surahs == {90}`).
- H-NEW artifacts (all values read by script):
  - h-new-111: FR mean 0.8372; nearest Q 112 (0.395); 5 farthest = Q 6/2/4/9/3.
  - h-new-590: window {87–93}, delta_pct −0.17, p 0.999, **NULL** (extreme cohesion member).
  - h-new-700: rhyme top ه frac 0.50; phoneme vec [0.0205,0.0468,0.0439,0.1257].
  - h-new-750: sig_A +1.5261 (rank **16/114**), sig_B +0.9706 (rank 30); rhyme_entropy 1.1421.
  - h-new-720: Q89→Q90 +0.05033 (rank 47); Q90→Q91 +0.09936 (rank 81).
  - h-new-840: UAS −0.4422 (rank 60/114).
  - h-new-2210: Q 90 = surah-initial *uqsimu*, jawāb `la-(tawkīd)` at v 4, dist 3; one of 8 *uqsimu*
    openers; **one of only 2 surah-initial** ones (with Q 75).

### Tafsīr (5 mufassirūn, scholar+work+passage)
- al-Ṭabarī (spa5k JSON 90/{1,4,8,10,11,12,13,17–20}); al-Qurṭubī (90/{1,10}); Ibn Kathīr EN (90/1…);
  al-Rāzī (raw lines 259170–259345); al-Zamakhsharī (raw lines 71847–71968 + balāgha note 69406).
- Key reads: oath = Makka (ijmāʿ); v 4 = jawāb (al-Ṭabarī explicit "هذا هو جواب القسم"); the *lā* crux
  (al-Qurṭubī 6 positions); najdayn two-ways vs two-breasts; *wa-anta ḥill* parenthesis + Conquest-future.

### Hadith (every number verified on disk, ahmedbaset 9-books JSON, idInBook)
- Makka sanctity: Bukhārī #1303, #1765, #112; Muslim #3182; Nasāʾī #2880, #2881, #2898; Ibn Mājah #2845.
- *fakk raqaba* / best slave: Bukhārī #2418 (Kitāb al-ʿItq), #6471; Muslim #156; Ibn Mājah #2259 (Abū Dharr).
- najdayn report: **NOT in the 9 books** (tafsīr-transmitted Qatāda mursal) — flagged.
- al-Balad faḍīla (al-Kashshāf): **NOT in the 9 books; fabricated Ubayy chain** — flagged.

### Pre-registration → test (Q090-F-01)
- Wrote `Q090-F-01-balad-hapax-uqsimu-prereg.md`; froze; SHA-256 =
  `5ab5e79bb7e3dcf20a36e1e7e5fccc0d64cdcbe6ac27d52c0925d7d988411d18`. Embedded in script; runtime-verified.
- **Garden-of-forking-paths note:** during scoping I inspected the *lā uqsimu* set's FR geometry
  (Q 75/Q 90 rank 37/113) BEFORE locking. Per Protocol §1.7 MW-7 + §1.8, I therefore did NOT make the
  doublet-FR a verdict-bearing arm; it is published as a descriptive, single-test-capped observation only.
  The verdict-bearing test is the hapax-enrichment (count + density), which was NOT inferentially
  evaluated before locking.
- **Performance note:** first script version recomputed exclusive_count by rebuilding sets over 49,968
  occurrences × 40k perms → ~O(2e9), stalled at 98% CPU >5 min; killed (PID 59633). Rewrote `run_null` as
  the equivalent multivariate-hypergeometric (priority-rank the occurrence slots, declare smallest-n_target
  as "target", count roots with all-slots-in-target) — mathematically identical for the count statistic,
  O(N) per perm. The SHA-lock is on the PRE-REG (unchanged), so the optimization does not break the lock;
  the equivalence is documented in the script docstring. Re-ran clean (~3 min, 30k perms total).
- **Result:** H1 count p_perm = 0.00120 (obs 4 vs null-mean 0.42); H2 density p_perm = 0.00080; both PASS
  α_bon = 0.025 in the LOCKED enrichment direction; MW-5 (seed 20260530) reproduces (p 0.0008).
- **MW-6 control Q 91 al-Shams: equally enriched** (4 exclusive roots, p 0.0004) → verdict demoted from
  "Q 90-specific" to **CONFIRMED (register-level)**. Published with full prominence. JSON →
  `csv/Q090-F-01.json`.

### Files written
- 00-overview, 01-empirical-profile, 02-content-analysis, 03-tafsir-survey, 04-hadith-corpus,
  05-classical-claims-audit, 06-novel-findings, 07-cross-references, JOURNAL (this).
- Pre-reg + script + csv/Q090-F-01.json.

### Honest verdict
Q 90 al-Balad: content-central (FR-mean 0.837, nearest Q 112), upper-decile structural-iʿjāz (sig_A rank
16), deep cohesion member of the tightest corpus window, one of 2 surah-initial *lā uqsimu* openers, and
hapax-enriched at the **register** level (not as a Q 90 singleton — MW-6 fired). One pre-registered test
landed CONFIRMED with an honest register-level limit.

*Bismillāh. Investigation-complete per Protocol §11 (8 files, 6 classical claims audited, 1 pre-registered
test with full MW-1..MW-7, all metrics integrated, cross-refs mapped, non-trivial honest-limits in every file).*
