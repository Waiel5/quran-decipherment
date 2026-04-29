---
run_id: prophet-micro-rings-run-1
date: 2026-04-12
agent: prophet-ring-scanner
finding: findings/phase-c-structures/prophet-micro-rings.md
scripts:
  - analysis/notebooks/prophet_rings.py
  - analysis/notebooks/prophet_rings_scan.py
machine_results:
  - analysis/notebooks/prophet_rings_results.json
  - analysis/notebooks/prophet_rings_scan_results.json
---

# Journal — Prophet Micro-Rings Run 1

## Brief

Systematic extension of the chiastic-audit ring methodology to every major
prophet in the Quran. Question: does EVERY prophet story have a miniature
ring somewhere? Prior finds:

- Al-Baqarah 131-144 Abraham/qibla: z=+9.69 (Bonferroni survivor)
- Q 21:51-73 Abraham idol-destruction: second Abraham ring (from intra-quranic
  cross-refs)
- Moses-Khidr 18:60-82: two sub-rings in Al-Kahf

The question: are these typical, or special?

## Method

Two scripts run in parallel:

**`prophet_rings.py`** — 34 curated prophet pericopes; Null A (intra-pericope
shuffle) + Null B (surah-wide shuffle, resample at offset). 2000 trials per
null. Bonferroni z-threshold for 34 tests one-sided α=0.05 = 3.03.

**`prophet_rings_scan.py`** — every 5..15-verse sub-window inside each declared
pericope; 500 trials per window. Family size 7 277 → Bonferroni z = 4.35.

## Observations

1. **Zero pericopes survive Bonferroni at either family size.** This was
   surprising given Abraham 131-144's z=+9.69 benchmark. It means the known
   Bonferroni-surviving rings are genuine outliers, not representative.

2. **Moses dominates the sub-window z-ranking.** 7 of top 15 sub-windows are
   Moses-Shuʿarāʾ. This is consistent with Moses being the most-named prophet
   (136 tokens) and with Shuʿarāʾ's refrain-heavy structure.

3. **Abraham 11:69-76 (angelic visitation) emerges as the strongest
   previously-unflagged Abraham ring.** z_A=+2.28, p=0.024 (uncorrected).
   Sarah laughing ↔ Sarah astonished, v69-arriving ↔ v76-departing, centre
   v72/73 (Sarah's astonished laughter / angels' reassurance). This is a
   real literary unit with detectable ring structure.

4. **Three prophets have NO ring structure at any level tested:** Noah,
   Jonah, David/Solomon. Noah especially — even Surah Nūḥ (named for him,
   whole-surah about him) is actively anti-ring at z=−0.61. This is
   semantically intelligible: the Noah story is narrative-progressive (build
   the ark → flood → landing → covenant) rather than reflective/chiastic.

5. **The "second Abraham ring" (Q 21:51-73)** downgraded: z_A=−0.50. Only
   z_B=+1.97 (surah-wide null) shows any signal. The semantic ring (idols →
   confrontation → fire → salvation) remains legible but the *lexical*
   Jaccard signal is weak. Honest downgrade of prior claim.

6. **Surprise: Surah Yūnus's strongest sub-window is not about Jonah.**
   10:44-57 scores z=+3.67, the best Jonah-surah window — but it is the
   surah's general punishment-cluster, not a Jonah narrative. Lesson:
   surah naming does not predict internal ring location.

7. **Jesus has one strong sub-window:** 3:40-47 (Mary-Zechariah annunciation
   pair), z=+3.51. Algorithmically-detected mirror structure between the
   two annunciations.

## Decisions / rejections

- Decided: report the panel *as a negative result* on the "every prophet has
  a ring" question, with nominal sub-window hits called out as candidates
  not confirmations.
- Rejected: the interpretation that the Abraham 11:69-76 hit is "Bonferroni
  survivor" — it is p=0.024 uncorrected only.
- Rejected: pushing harder on Noah with more sub-windows — Noah is robustly
  ring-free at every scale I tested. Reporting him as a genuine null.
- Deferred: Moses-Khidr 18:60-82 replication is in moses-deep, not
  duplicated here.
- Deferred: deeper thematic analysis of why some prophets ring and others
  don't — belongs in a separate literary-typology finding.

## Runtime / cost

- `prophet_rings.py`: ~45 seconds (34 pericopes × 2 nulls × 2000 trials = 136 000 ring-scores)
- `prophet_rings_scan.py`: ~90 seconds (7 277 windows × 500 trials ≈ 3.6M ring-scores)
- Morphology load: one pass of QAC v0.4 (≈180 k lines)

## Results files

- `analysis/notebooks/prophet_rings_results.json` — 34-pericope declared panel
- `analysis/notebooks/prophet_rings_scan_results.json` — sub-window scan
- `findings/phase-c-structures/prophet-micro-rings.md` — writeup

## Reproduce

```
python3 analysis/notebooks/prophet_rings.py
python3 analysis/notebooks/prophet_rings_scan.py
```

## Open questions for next run

1. Is the Abraham 11:69-76 ring also present under a **lemma-based** null
   (not root-based)? The signal may sharpen if we track Abraham's lexemes
   separately from generic Arabic function-words.
2. Does the Mary-Zechariah annunciation ring extend to Q 19:2-15 + 19:16-33
   treated as a **cross-annunciation pair** (outside a single window)? A
   paired-pericope chiastic test would be informative.
3. Are ring-bearing prophets correlated with Meccan chronology? Abraham's
   Meccan pericopes (21, 37, 26) score better than his Medinan ones
   (2:124-141 outside qibla-ring). Potential chronological signal here.
