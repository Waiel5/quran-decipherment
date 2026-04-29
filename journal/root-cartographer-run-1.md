# root-cartographer-run-1 — journal

**Agent:** root-cartographer (Phase B novelty hunt)
**Date:** 2026-04-12
**Model:** Claude Opus 4.6 (1M context)
**Inputs:** `data/morphology/quranic-corpus-morphology-0.4.txt`, `quran-text/quran-no-tashkeel.json`, `data/translations/en.sahih.txt-2.txt`
**Outputs:**
- `data/morphology/root-index.json` (672 KB) — `{root_BW: [(s,v,w), ...]}`
- `data/morphology/root-stats.csv` (48 KB, 1642 rows)
- `findings/phase-b-hypotheses/root-cartography.md` (27 KB)
- `analysis/scripts/root_cartography.py` — the analysis source
- `journal/root-cartographer-run-1.md` (this file)

## Mission

Phase B novelty hunt over root distributions. Tasks: build root index, run
fundamental dist stats, hapax-surah and Meccan/Medinan filters, suspicious-
count flags, count==first-surah checks, entropy-based clustering, replicate
the famous Family-B word-pair claims, hunt for novel matching-count pairs,
catalog root palindromes, list single-surah thematic anchors. Write the
report and a 500-word summary.

## Method

1. Read methodology, design, statistical-rigor protocol, INTEGRATION.
2. Wrote `analysis/scripts/root_cartography.py` — single-file pipeline that
   loads the morphology, builds the index, computes all 12 sub-analyses, and
   emits the report with full YAML frontmatter and the §11 forking-paths
   disclosure.
3. Ran the script (one shot, ~10 s wall time on the morphology file).
4. Sanity-checked: 1,642 distinct roots over 49,968 stem-with-root segments
   inside 77,915 stems total. The QAC has lemma+root tags for ~64 % of stems
   (the rest are proper nouns and certain particles, which are stems but not
   root-bearing in the Leeds tagging scheme).
5. Did one opportunistic hand-check for Adam/Isa (claim wasn't on the primary
   list but is in Family B and is the famous "this one actually works" pair):
   verified `A^dam` lemma = 25, `EiysaY` lemma = 25.
6. Augmented the report with a §0 "Headline candidate findings" section after
   spotting the Yusuf/`sjn`=12-in-Surah-12 triple coincidence.

## Replication verdicts (Family-B word pairs)

| Pair | Claim | Root count A | Root count B | Verdict |
|---|---|---:|---:|---|
| yawm / layl | both 365 | 405 | 92 | **failed** |
| rajul / imra'a | both 24 | 73 | 38 | **failed** (no lemma matches either) |
| bahr / barr | 32 / 13 | 42 | 32 | **failed** (sea over, land matches the wrong target) |
| dunya / akhira | both 115 | 133 | 250 | **requires-cherry-picking** (single lemma `dunya`=115, but no `akhira` lemma at 115) |
| mala'ika / shayatin | both 88 | 206 / 88 | — | **partial** (lemma `malak`=88, lemma `shayTan`=88 — works only at single-lemma level) |
| hayat / mawt | both 145 | 184 | 165 | **failed** (no lemma reaches 145 on either side) |
| (bonus) Adam / Isa | both 25 | — / — | 25 / 25 | **verified at lemma level** |

**One verified, one partial, four failed.** The single verified pair (Adam/Isa)
is selected from a 14-element tie-class at count=25; the "partial" pair
(mala'ika/shayatin) requires the very lemma-pick the literature usually denies.

## Three most interesting flags (for the next agent)

1. **`sjn` (prison) = 12 occurrences, 12 of 12 in Surah 12 (Yusuf), and
   Surah 12 is the prison narrative.** Triple alignment of count, surah index,
   and narrative content. Sister anchors `qmS` (shirt, 6× all in Yusuf), `khf`
   (cave, 6× all in Al-Kahf surah 18) point to a real surah-anchored
   lexical-fingerprint phenomenon. **Recommended Phase B follow-up:** test
   under §1.5 (permutation across surah indices) — null hypothesis: "any
   surah of length L will host count(R) = 12 single-surah-anchored roots
   that align with their surah's narrative." Recommended sister test:
   §1.4 comparable-corpus null on the same Yusuf-length blocks of early
   hadith to see if classical Arabic narrative prose produces equally tight
   lexical-thematic anchors.

2. **mala'ika/shayatin = 88/88 at the single-lemma level.** Reproducible if
   you commit to lemma-not-root and singular-not-mass. The literature gets
   the right number but does so by hiding the form-pick; once disclosed it
   looks more arbitrary, but the number is real. Worth a §1.3 word-level
   bigram null and §1.4 comparable-corpus null. **Note also** the count=88
   tie-class in §8 has only TWO members (`$Tn`=88 and `qrA`=88), so picking
   shayTan from it is uncontroversial — but the "partner" you'd naturally
   pair shayTan with at root level is `qrA` (recite/Quran), not malak.

3. **Adam = Isa = 25.** The only headline pair that survives without any
   rule manipulation, but it survives because the lemma equals the root
   equals the surface form (proper nouns don't inflect in Arabic), which
   inflates apparent rigor. The count=25 tie-class contains 13 other roots
   (Sly "pray", flk "ship/orbit", $ry "buy", whb "give", Hdd "limits"), so
   the "miracle" framing is post-hoc selection from a 14-element pool.

## Distribution statistics worth noting

- 1,642 distinct roots
- 395 hapax (occur exactly once) — Zipf-typical
- 459 single-surah-only roots (any count)
- Top root: `Alh` (Allah) at 2,851 occurrences in 86 surahs
- Top-20 roots account for ~30 % of all root-bearing segments
- 8 root palindromes total (3-letter only): `ydy` (hand) 120×, `lyl` (night)
  92×, `tHt` (under) 51×, `vlv` (three) 32×, `bwb` (door) 27×, `sds` (sixth)
  5×, `nwn` (whale) 1×, `SyS` 1× — nothing more numerologically structured
  than what Arabic morphology naturally produces.
- 63 Meccan-only roots (≥5 occ); only 14 Medinan-only roots — reflects the
  larger Meccan vocabulary share of the corpus and the more restricted
  Medinan thematic register (legal, communal, war-related: `Hrf`, `Asr`,
  `vqf`, `Syd`, `$Tr`, `n$z`, `Ent`, `bgD`, `xdE`).
- §8 enumerates **2,817** unordered pairs of distinct roots whose total
  counts coincide at ≥10 occurrences, across 84 distinct count-values. This
  is the McKay-style denominator that any "see, the count of X equals the
  count of Y!" claim must be measured against.

## Honest limits / sources of error

- The Leeds QAC has a small number of disputed root assignments (a few
  dozen), and proper nouns are tagged with `LEM:` but no `ROOT:`, so the
  root index excludes them. When a famous claim depends on a proper noun
  (e.g., Adam, Isa), I had to drop to lemma-level analysis.
- Meccan/Medinan classification comes from amrayn `quran-no-tashkeel.json`,
  which uses traditional attribution. Ten-ish surahs are contested; this
  noise propagates to the §3 list.
- The 'count == first surah index' analysis is a fishing exercise; about 40
  hits are reported, and most are coincidence. The Yusuf-12 alignment is
  the only one with internal narrative semantic support (the other top hit,
  `wrd` "to come to water" = 11× starting in surah 11 (Hud), has no
  story-level narrative parallel that I could see; same for `rhq` = 10
  starting in surah 10).

## Files for the next agent
- `data/morphology/root-index.json` — load with `json.load()`; values are
  lists of (s,v,w) triples.
- `data/morphology/root-stats.csv` — pandas-ready summary.
- `findings/phase-b-hypotheses/root-cartography.md` — full report.
- `analysis/scripts/root_cartography.py` — re-run with `python3` from the
  repo root; it is single-file and idempotent.

## Status

DONE for the Phase B exploratory pass on root cartography. None of the
flags have null-model support; all are candidates only.
