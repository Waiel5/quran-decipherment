# journal: rahma-derivatives-audit — run 1 (2026-04-12)

## Goal
Test H4: is `raḥma = 114` unique within the r-ḥ-m lemma family, or does the
coincidence diffuse across derivatives (lexical-family selection effect)?

## Method
1. Read H4 definition in `findings/deep-hypotheses-queue.md`.
2. Filter `data/morphology/quranic-corpus-morphology-0.4.txt` for rows whose
   FEATURES field contains `ROOT:rHm`.
3. Parse LEM and POS from each row via regex (`LEM:([^|]+)`, `POS:([^|]+)`).
4. Tally lemma counts and POS splits.
5. Cross-check cluster total against `data/morphology/root-stats.csv` (entry
   `rHm,رحم,339,62,313,1,90,226,113`).
6. Test each lemma's count against the pre-registered famous integer set
   {7,12,19,28,30,40,57,77,99,100,114,147,313,365,786,1000,6236}.
7. Compute binomial baseline: of all 4,838 distinct QAC lemmas, how many land
   on a famous integer? Use that rate in a binomial null for the 9-lemma
   cluster.

## Results
- 9 distinct lemmas under `ROOT:rHm`; row total = **339** ✓ matches root-stats.
- Counts (descending):
  - r~aHiym (raḥīm) 116 [ADJ 112, N 4]
  - raHomap (raḥma)  114 [N 114]
  - r~aHoma`n (raḥmān) 57 [N 45, ADJ 12]
  - r~aHima (verb)     28 [V 28]
  - >aroHaAm (wombs)   12 [N 12]
  - r~a`Himiyn (rāḥimīn) 6 [ACT-PCPL 6]
  - >aroHam (arḥam)     4 [N 4]
  - ruHom               1 [hapax]
  - maroHamap           1 [hapax]

- **Unique holder of 114 within family:** raHomap (rahma) — the only one.
- **Unique holder of 114 in all QAC (4,838 lemmas):** also rahma — the only
  lemma in the whole Quran at count 114.
- **Famous hits (full set):** 4/9 — rahma 114, raḥmān 57, raḥima 28, arḥām 12.
- **Famous hits (strict set, excl small abundant ints):** 2/9 — rahma 114,
  raḥmān 57 (both 19-multiples).
- **Binomials:**
  - full set baseline p = 219/4838 = 0.0453, P(X ≥ 4 | n=9, p) ≈ 0.00042.
  - strict set baseline p = 22/4838 = 0.00455, P(X ≥ 2 | n=9, p) ≈ 0.00068.

## Cross-checks / sanity
- Verified no r-h-m row was missed by comparing total rows (339) with
  root-stats.csv row (339).
- Spot-checked that POS:N instances of `r~aHiym` (4 tokens at 4:29, 17:66,
  34:2, 73:20) are nominalised attribute uses ("is Merciful [to you]"),
  NOT the anatomical womb sense. The womb sense lives under the plural
  lemma `>aroHaAm` only.
- Verified `>aroHam` (4x) and `r~a`Himiyn` (6x) co-occur in formulas
  *arḥam ar-rāḥimīn* (4 pairings) and *khayr ar-rāḥimīn* (2 extra).
- Verified `rahmān` 57 = 19 × 3 exactly (Khalifa claim confirmed).
- Verified `raḥīm` 116 ≠ 19 × k (116/19 = 6.105), contradicting Khalifa's
  claim of 114. Matches the prime-code19 agent's earlier finding.

## Unresolved / next steps
- Run the identical audit on roots Alh (ilāh), rbb (rabb), Emr (creation),
  nfs (self), knt (kāna), mlk (king), ktb (book). If several of them also
  show 2+ strict famous hits, r-h-m is unremarkable. If r-h-m is the only
  such root, the claim hardens further.
- This is the H4 test only. H1 (systematic meaningful-N lemma audit) and
  the rahma-baseline agent (count=114 semantic-centrality alternatives) are
  the remaining gates before promotion.

## Verdict for the H4 gate
**PASS with one caveat.** The rahma=114 finding is not a lexical-family
cherry pick: rahma is the unique 114 in the family AND in the whole Quran,
AND a second family member (raḥmān) independently lands at another
strict-famous integer (57 = 19×3). The simultaneous family failure at
raḥīm = 116 (theologically central, not landing at a famous integer)
argues against a "any important mercy word hits a famous number" null.
Binomial null p ≈ 0.0004–0.0007. Caveat: this null is family-internal
only; cross-family control (H1 and other-root audits) is still required.
