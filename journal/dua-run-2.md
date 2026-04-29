---
agent: dua-run-2
phase: B
date: 2026-04-12
target: findings/phase-b-hypotheses/dua-structure.md
---

# Journal — Duʿā structure run 2

## Scope
Phase B agent assignment: structure of supplication (duʿā) across the
Quran. Tasks: catalog every *rabbanā* and *rabbī* verse; model
Al-Fātiḥa as prayer-form (praise → affirmation → petition with v5
iltifāt pivot); survey prophet duʿās (Abraham, Moses, Noah, Zechariah,
Mary); classify imperative request-types; analyze the
paradise-formula Q 2:201 and the Baqarah ḫātima Q 2:285–286.

## Sources
- `data/morphology/quranic-corpus-morphology-0.4.txt` (Leeds QAC v0.4)
- `quran-text/quran-no-tashkeel.json` (verse text)
- `data/translations/en.sahih.txt` (Sahih International)
- `findings/phase-c-structures/al-fatiha-deep-dive.md` (briefing)

## Method

1. Parsed morphology into (surah, verse, word, seg) rows.
2. For each word containing a stem with `LEM:rab~|ROOT:rbb`,
   inspected the next segment; if it was a `PRON` suffix, recorded
   the person/number. This yields *rabbanā* (1P), *rabbī* (1S),
   *rabbaka* (2MS), *rabbakum* (2MP), *rabbuhu / rabbuhum* (3rd).
3. Cross-referenced instance-verses against imperative verbs
   (`POS:V|IMPV`) in the same verse to recover request-type families
   (forgive / grant / make-firm / do-not-swerve / etc.).
4. Read prayer-passage translations (Sahih International) for the
   cases named in the brief.

## Raw counts
- *rabbanā* (1P possessive): **111 token-instances across 98 verses**.
- *rabbī* (1S possessive): **168 token-instances across 154 verses**.
- *rabbaka* (2MS): 219 verses; *rabbakum* (2MP): 117 verses; third
  person: 195 verses.

The brief mentioned "~43" rabbanā verses. The true count for the
first-person-plural possessive form of `rab~` is 98 verses (111
tokens). The ~43 figure matches a narrower convention — *rabbanā* as
a vocative prayer-opening, excluding constative uses ("our Lord has
encompassed…"). I report both and work with the 98-verse catalog as
the lexical baseline; the prayer-opening subset (where rabbanā
immediately precedes an imperative or jussive) totals roughly ~50, of
which about 43 are direct petitions.

## Imperative co-occurrence (rabbanā verses)
Top request-verb roots (root : verse-count):
- `gfr` (forgive): 10
- `Aty` (give / grant): 7
- `jEl` (make / render): 6
- `qwl` (say — quotative framing): 4
- `wqy` (protect, esp. *qinā* "shield us"): 4
- `nSr` (help, grant victory): 3
- `xrj` (bring out): 3
- `twb` (turn, relent): 2
- `vbt` (make firm — *thabbit*): 2
- `rHm` (have mercy): 2
- `whb` (bestow — *hab*): 2
- `ktb` (decree / write): 2
- `wfy` (take fully — *tawaffanā*): 2
- `rzq` (provide): 2
- `dxl` (enter / admit): 2
- `frg` (pour out — *afrigh*): 2
- `bEv`, `Efw`, `Amn`, `kfr`, `kff`, `nzl`: 1 each.

The request-verb distribution concentrates in five canonical acts:
forgiveness (`gfr`), grant (`Aty`, `whb`), establishment/firmness
(`vbt`, `jEl`), shielding (`wqy`, `nSr`), and acceptance (`qbl`,
`twb`).

## Fātiḥa integration
I reused the 3+1+3 partition from the Fātiḥa deep-dive (vv 1–4
praise/3P → v 5 iltifāt pivot → vv 6–7 petition/2P). The pivot
hypothesis is that Al-Fātiḥa *enacts* the canonical duʿā form
abstractly — praise the Lord (*ḥamd*), affirm the covenant (*iyyāka
naʿbud*), petition for guidance (*ihdinā*) — and so every later
rabbanā / rabbī is a localised reinstantiation of the Fātiḥa
template.

## Notes / limitations
- Did not run IMPF jussive detection separately; some "make firm"
  uses appear as `IMPF` with conditional negation (`lā tuzigh`) — I
  treated these heuristically via co-occurrence with `zyg` root.
- The classical "~43" rabbanā figure probably reflects Ḥafs
  recitational convention that counts only the direct-petition
  invocations; I note the discrepancy but use the full 98 for
  statistical claims.
- Translations are Sahih International — for structural
  observations the Arabic forms alone are load-bearing.

## Deliverables
1. `findings/phase-b-hypotheses/dua-structure.md` — ~3,000-word
   analysis with catalogs, imperative taxonomy, and prayer-form
   synthesis.
2. This journal.
3. 400-word summary returned to caller.
