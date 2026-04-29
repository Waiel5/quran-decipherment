# [[h-new-209-pagerank-celebrated|H-NEW-209]] — PageRank verse-twin hubs vs classical celebrated verses

**Seed:** 20260419   **Bonferroni k:** 1   **α_corrected:** 0.05
**Pre-reg:** `[[h-new-209-pagerank-celebrated|h-new-209]]-pagerank-celebrated-prereg.md`
**Rules-tuple:** (no-tashkeel; whitespace-collapsed; basmala-only-in-Q1)

## Verdict: **FAIL** — intersection does NOT exceed chance

| metric | value |
|---|---|
| graph | 6236 nodes, 4943 edges (top-1 Jaccard, symmetrised, identical to [[h-new-167-verse-twin-graph|H-NEW-167]]) |
| celebrated set | 27 verses (Q1:1-7, Q2:255, Q24:35, Q59:22-24, Q112:1-4, Q113:1-5, Q114:1-6) |
| top-50 PageRank ∩ celebrated | **1** |
| expected under uniform | 0.216 |
| hypergeom P(X ≥ 1) | **0.1957** |
| permutation p (10,000 iters) | **0.1940** |
| null mean / std / max | 0.215 / 0.464 / 3 |

Only hit: **Q 1:2** (`al-ḥamdu lillāhi rabbi l-ʿālamīn`, rank #7 by PR,
degree 7). No other celebrated verse appears in the top 50 by PageRank.

## Top-10 PageRank hubs (none are classical "celebrated")

| rank | verse | PR | deg | classical status |
|---|---|---|---|---|
| 1 | Q 55:13 | 0.00235 | 31 | `fa-bi-ayyi ālāʾi rabbikumā tukadhdhibān` — refrain hub |
| 2 | Q 77:15 | 0.00090 | 11 | `waylun yawmaʾidhin lil-mukadhdhibīn` — refrain |
| 3 | Q 26:108 | 0.00081 | 10 | Shuʿarāʾ refrain (messenger formula) |
| 4 | Q 26:8 | 0.00071 | 9 | Shuʿarāʾ sign-refrain |
| 5 | Q 26:9 | 0.00066 | 8 | Shuʿarāʾ "rabbuka huwa al-ʿazīz al-raḥīm" |
| 6 | Q 75:9 | 0.00057 | 7 | short eschatological |
| 7 | Q 1:2 | 0.00057 | 7 | **al-ḥamdu lillāhi rabbi l-ʿālamīn** ✓ |
| 8 | Q 29:47 | 0.00057 | 7 | "those given the Book" |
| 9 | Q 96:2 | 0.00056 | 7 | `khalaqa l-insāna min ʿalaq` |
| 10 | Q 56:24 | 0.00054 | 7 | "recompense for what they did" |

## Interpretation

PageRank hubs on the top-1 Jaccard twin graph are dominated by **formulaic
refrains** (Q 55, Q 77, Q 26, Q 37), not by the devotionally celebrated
verses of the classical tradition. The two categories are **largely
orthogonal**:

- *Celebrated* = theologically/liturgically exalted, often unique in
  phrasing (āyat al-kursī's length and syntax are sui generis; Ikhlāṣ is
  lexically distinctive; khawātim al-Ḥashr stack divine names in a
  non-repeating cascade).
- *PageRank-central* = structurally recurrent, shares trigrams with many
  other verses (refrains by design).

Q 1:2 clears the bar because `rabbi l-ʿālamīn` recurs across the corpus
(Q 6:45, 7:54, etc.), not because al-Fātiḥa as a whole is central to the
graph. Notably, **Q 2:255, Q 24:35, Q 112:1-4, Q 59:22-24, Q 113, Q 114**
all fail to appear anywhere near the top — consistent with their
literary uniqueness (low trigram overlap with the rest of the corpus).

## Caveats

- Single pre-registered test (k=1). No garden-of-forking-paths.
- Result is a **null finding with clean interpretation**, not a negative
  one: it supports the view that classical celebration tracks
  *uniqueness/distinctiveness* rather than *structural centrality*.
- Could be re-tested with a weighted-Jaccard graph (not pre-registered
  here; would require new prereg).

## Artifacts

- `findings/phase-b-hypotheses/csv/h-new-209.json`
- `findings/phase-b-hypotheses/csv/h-new-209-top50.csv`
- `scripts/h_new_209_pagerank_celebrated.py`
