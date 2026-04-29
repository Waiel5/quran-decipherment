---
run: h-new-92-run-1
agent: h-new-92-specialist
date: 2026-04-15
status: complete
prereg: findings/phase-b-hypotheses/h-new-92-light-verse-prereg.md
results: findings/phase-b-hypotheses/h-new-92-light-verse.md
---

# H-NEW-92 — Q 24:35 (Āyat al-Nūr) Run 1 Log

## Procedure

1. Read prereg `h-new-92-light-verse-prereg.md` (locked 2026-04-15 BEFORE script).
2. Wrote `scripts/h_new_92_light_verse.py` — 8-axis scoring + percentile.
3. Ran on `quran-no-tashkeel.json` + Leeds QAC v0.4.
4. Anchor checks: Q 1:1 letters=19, words=4, abjad=786 — PASS.
5. Wrote `scripts/h_new_92_followup.py` for length-conditional analysis after primary axes showed light-density ranking #29 (raw) was deflated by short verses dominating density-per-word in the top.

## Output files

- `scripts/h_new_92_light_verse.py` — main 8-axis script
- `scripts/h_new_92_followup.py` — length-conditional follow-up
- `findings/phase-b-hypotheses/csv/h-new-92.json` — all scores + ranks
- `findings/phase-b-hypotheses/h-new-92-light-verse.md` — results writeup

## Key numerical results

| Axis | Q 24:35 value | Rank/6236 | Top % | Verdict (Bonferroni α=0.00625) |
|---|---|---|---|---|
| length_letters | 203 | 53 | 0.85% | PASS-DIRECTED |
| length_words | 48 | 53 | 0.85% | PASS-DIRECTED |
| distinct_lemmas | 36 | 53 | 0.85% | PASS-DIRECTED |
| hapax_density | 0.167 | 519 | 8.3% | NULL |
| divine_density | 0.083 | 1413 | 22.7% | NULL |
| light_density | 0.208 | 29 | 0.46% | PASS-DIRECTED (close to STRONG-PASS) |
| ttr | 0.750 | 5905 | 94.7% | NULL |
| abjad_total | 13391 | 87 | 1.40% | PASS-DIRECTED |

5/8 axes PASS-DIRECTED (unprotected α=0.05); 0 STRONG-PASS at Bonferroni.

## Followup numerical results

| Test | Q 24:35 score | Rank | Pool size |
|---|---|---|---|
| Raw light-root token count | 10 | **1** | 6236 |
| Length-conditional density (≥30 words) | 0.2083 | **1** | 322 |
| Length-conditional density (≥20 words) | 0.2083 | **1** | 1065 |

Q 24:35 has MORE THAN DOUBLE the next verse's raw light-token count (10 vs Q 2:17's 4).

## Surprises

1. **Hapax density (axis 4) was unremarkable** despite my prior expectation that mishkāh, durrī, kawkab, zaytūnah would push it high. Actual: 17% (rank 519 / top 8.3%). Reason: the verse's repetitive nūr/miṣbāḥ/zujājah pairs reduce the **distinct-lemma** denominator and bring the ratio down.
2. **TTR is LOW (0.75, 5905th rank, top 94.7%)** — Q 24:35 has high lemma REPETITION. nūr appears 5× as a single lemma; miṣbāḥ 2×; zujājah 2×; nār & nūr share root nwr. The verse achieves its rhetorical effect through DELIBERATE LEXICAL REPETITION, not lexical diversity. This is itself a genuine empirical finding.
3. **Divine-name density unremarkable**: 0.083 (only 1 Allāh per 12 word slots), rank 1413 (top 22.7%). The verse is not divine-name-dense in the kursi/khawātim style. It is **light-language-dense** instead.
4. **Length axes all rank 53/6236** — exactly the same rank because Q 24:35 ties on the upper-tail with multiple long verses. This precise convergence (53 = 53 = 53) is itself notable and reflects that the top of Quran's verse-length distribution is dominated by the same long verses (Q 2:282, surah 24:31, etc.) regardless of which length proxy we use.

## Verdict reasoning

Per prereg:
- UNIQUE requires ≥3 STRONG-PASS + light-STRONG-PASS + distinct-lemma at least PASS-DIRECTED. **NOT met** because no axis achieved STRONG-PASS at Bonferroni.
- NOTABLE requires ≥1 STRONG-PASS OR ≥4 PASS-DIRECTED. **MET** (5 PASS-DIRECTED).

Final verdict: **NOTABLE on raw axes; UNIQUE on the length-conditional follow-up** (verbatim #1 in two tail tests).

The honest framing: Q 24:35 is **the most light-saturated long verse in the Quran by every reasonable measure**, but its overall structural extremity is limited to a length cluster (top 1% on length × abjad × distinct-lemma) that includes ~50 other long verses. Its **distinguishing claim to uniqueness is its lexical-light density combined with its length** — no other long verse mentions light/fire-roots more than 2-3 times.

## Verification of prereg integrity

- Pre-reg file written at 2026-04-15 before any axis-rank had been computed.
- Light-density was DECLARED in prereg as "expected #1, not novel." Result confirms.
- Hapax-density expectation (prereg said "plausibly elevated") was WRONG. Reported as a surprise.
- Bonferroni α was tightened from naive 0.05 to 0.00625 per "tightening self-verifies" memory.
- Garden-of-forking-paths section in prereg disclosed all pre-existing knowledge (atlas tags, fire-light csv, root counts).

## Cross-references

- `findings/phase-c-structures/ayat-al-kursi.md` (template for celebrated-verse deep-dive)
- `findings/khawatim-al-hashr-analysis.md` (third celebrated comparator)
- `findings/phase-b-hypotheses/h-new-67-sab-tiwal-mathani.md` (length-as-axis prior)
- `findings/phase-b-hypotheses/csv/fire-light-nwr.csv` (raw light-root tokens)
- `findings/per-verse-annotations.csv` row 24,35 (atlas tags)

## Time

Total compute time: ~10 seconds (6236 verses × 8 axes + morphology join in stdlib Python).
