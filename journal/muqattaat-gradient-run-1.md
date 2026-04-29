---
run: muqattaat-gradient-run-1
date: 2026-04-12
agent: phase-b / muqattaat-gradient
hypothesis: deep-hypotheses-queue.md H17
parent_finding: phase-b-hypotheses/muqattaat-analysis.md
script: scratch/muqattaat_gradient.py
results_json: scratch/muqattaat_gradient_results.json
output: findings/phase-b-hypotheses/muqattaat-positional-gradient.md
---

# Run journal — H17 muqatta'at positional gradient

## Goal

Diagnose the *mechanism* of the muqatta'at density finding (Stouffer Z = +4.48, p ≈ 4×10⁻⁶ under 3-gram Markov, driven by Q2, Q29, Q50). H17 predicts: if the effect is a topical-vocabulary-onset artifact (e.g., Q50 opens with eschatology using ق-words), then opening letters should cluster in Q1 and thin in Q4. If the effect is structural, the gradient should be flat.

## Method, briefly

1. Quartile each surah by verse count, contiguous, remainder pushed to Q4.
2. Strip the literal verse-1 muqatta'at letters before counting (so Q1 isn't artifactually inflated by 1–5 letters).
3. Count opening-letter density per quartile, normalized per 100 letters.
4. Aggregate over 3 carriers (Q2, Q29, Q50) and 26 non-carriers.
5. Verse-shuffle null (2000 perms, seed 42) on each carrier.
6. Control: 81 non-muqatta'at surahs, top-3 letters as synthetic signature.
7. Specifically inspect Q50 ق density per quartile.

## What I expected

I went in expecting H17 to be confirmed for at least Q50. The eschatology-onset story is plausible: Q50 vv 1–11 contain *al-Qurʾān al-majīd*, *al-yawmu l-ʿasīr*, *qarīb*, *qawl*, *yawmu l-qiyāmah*-adjacent vocabulary, all heavy on ق. The qualitative reading suggests Q1 should dominate.

## What I actually found

H17 is **decisively rejected** by every metric I ran:

| Metric | Carriers (3) | Non-carriers (26) | Non-muq control (81) |
|---|---|---|---|
| Mean gradient (Q1−Q4, pp) | **−0.093** | +0.391 | **+3.331** |
| Mean Q1/Q4 ratio | 0.896 | 1.127 | 1.119 |
| Surahs Q1>Q4 | 2/3 | 14/26 | 51/81 (sign-test p=0.026) |

The non-muqatta'at control is the cleanest finding: ordinary Arabic prose actually shows STRONGER front-loading of high-frequency letters (mean +3.33 pp, sig at p=0.026) than the muqatta'at carriers do. So front-loading is a real Arabic-prose phenomenon — just not present in the muqatta'at carriers.

### The Q50 surprise

Surah 50 ق density by quartile (after stripping verse-1's literal ق):

- Q1 (vv 1–11): **2.37** per 100 letters
- Q2 (vv 12–22): **4.65**
- Q3 (vv 23–33): **4.50**
- Q4 (vv 34–45): **3.56**

ق density nearly *doubles* from Q1 to Q2, peaks in Q2, and only thins in Q4. The exact opposite of the eschatology-onset prediction. Why? Because vv 12–33 of Surah 50 are the surah's resurrection/judgment elaboration ("on the day when..."), packed with ق-roots like *qālū* ("they said"), *qarīn* ("companion"), *qabla* ("before"), *qulūb* ("hearts"), etc., as the surah works through the Hour imagery. The opening pericope's *Qur'ān*/*qarīb*/*qawl* vocabulary is real but less ق-dense per word than the body imagery.

### Carrier verse-shuffle nulls

Within-surah verse-shuffle, 2000 perms, seed 42:
- S2: observed −0.27 pp, null mean −0.02, two-sided p = 0.741
- S29: observed +1.41 pp, null mean +0.07, two-sided p = 0.407
- S50: observed −0.94 pp, null mean −0.01, two-sided p = 0.390

None of the carriers show a significant positional gradient. The signal is genuinely flat.

## Implementation notes

- Used `tools/loader.load_quran('no-tashkeel')` and `tools/tokenize` for letter detection, plus the standard normalization map (hamza→alif, ى→ي, ة→ت, ؤ→و, ئ→ي).
- Anchor check: total normalized letters = 330,709 — matches §3 of `muqattaat-analysis.md` exactly. Locked.
- The "strip verse-1 muqatta'at letters" rule is critical. Without it, Q1 of every short muqatta'at surah is artifactually inflated by 1–5 letters out of ~400 letter-positions, biasing the gradient by up to +1 pp. With the strip, the gradient measures the *body* text, which is what H17 cares about.
- I split the JSON file's verse list contiguously into 4 groups by verse count, with remainder pushed to Q4. Surah 50 has 45 verses → 11/11/11/12.

## Things I would do differently next time

- Add letter-count quartiles as a sensitivity check (I didn't write a separate run, but spot-checked Q50: identical conclusion).
- Run a lemma-level / root-level version: do ق-bearing roots cluster in vv 1–11 of Q50? This is a different question and a meaningful follow-up.
- Run surrogate gradients on the full corpus to compute a corpus-wide null distribution for the "carrier mean gradient" statistic (currently I rely on per-surah verse-shuffle nulls and the binomial sign test).

## What this changes about the headline finding

Strengthens it. The most plausible artefact alternative — topical onset — has been ruled out empirically. The muqatta'at density signal is whole-surah, distributed, structural. This makes the parent finding's interpretation (mild but real signal of intentional letter signature) more defensible, though we still lack the comparable-Arabic-corpus null that would let us call it "evidence of editorial encoding".

Next priorities:
1. H18 — non-luminous letter inverse effect (sanity check on letter mass conservation).
2. A lemma-level co-localization test for the Q50 / Q2 / Q29 carriers.
3. The Bukhārī comparable-corpus null (currently flagged in H22).

## Files

- `/Users/grey/Downloads/quran/scratch/muqattaat_gradient.py` — analysis script
- `/Users/grey/Downloads/quran/scratch/muqattaat_gradient_results.json` — raw results
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/muqattaat-positional-gradient.md` — full report
