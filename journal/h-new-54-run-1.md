---
hypothesis: H-NEW-54
run: 1
date: 2026-04-15
agent: h-new-54-specialist
status: COMPLETE
verdict: PASS-BROAD-FIELD (4/10 roots significant after Bonferroni-10)
---

# H-NEW-54 — Run 1 journal

## Setup

- Pre-reg: `findings/phase-b-hypotheses/h-new-54-extended-root-enrichment-prereg.md` (locked 2026-04-15, BEFORE testing)
- Script: `scripts/h_new_54_extended_root_enrichment.py`
- JSON output: `findings/phase-b-hypotheses/csv/h-new-54.json`
- Findings: `findings/phase-b-hypotheses/h-new-54-extended-root-enrichment.md`
- Seed: 20260416 (closed-form; seed for bookkeeping)
- Bonferroni k=10, α_per = 0.005

## What was done

1. Loaded `quran-no-tashkeel.json` (114 surahs).
2. Used the locked muqaṭṭaʿāt set (n=29) from H-NEW-46 / H-NEW-53.
3. For each of 10 pre-registered revelation-theme roots:
   - Concatenated v1-3 of each surah.
   - For each surah, checked whether v1-3 contained ANY listed surface form.
     - r-b-b: token-boundary match (to avoid أربعة, ربما, etc.)
     - All other roots: substring match.
   - Computed K_root (total surahs hitting), obs (muq surahs hitting).
   - Two-sided hypergeometric: 2 × min(P(X≥obs), P(X≤obs)), capped at 1.
4. Applied Bonferroni-10 (α_per = 0.005).
5. Recorded per-surah hit lists for both muq and non-muq groups.

## Key results

**4/10 PASS** after Bonferroni-10:

| Root | obs | K | E[X] | p_two | Verdict |
|---|---|---|---|---|---|
| k-t-b | 20 | 28 | 7.12 | 2.93e-09 | **PASS** |
| q-r-ʾ | 9 | 11 | 2.80 | 1.17e-04 | **PASS** |
| ʾ-y-ā | 11 | 16 | 4.07 | 1.93e-04 | **PASS** |
| n-z-l | 12 | 20 | 5.09 | 5.97e-04 | **PASS** |
| dh-k-r | 5 | 11 | 2.80 | 0.221 | NULL |
| w-ḥ-y | 3 | 5 | 1.27 | 0.207 | NULL |
| w-ʿ-d | 0 | 4 | 1.02 | 0.607 | NULL |
| h-d-y | 4 | 15 | 3.82 | 1.000 | NULL |
| r-b-b | 8 | 32 | 8.14 | 1.000 | NULL |
| ʾ-l-h | 2 | 6 | 1.53 | 0.959 | NULL |

**Composite: PASS-BROAD-FIELD.**

## Positive control

**MW-5 PASSED.** k-t-b (kitāb) and q-r-ʾ (qurʾān) — the H-NEW-53 anchor pair — independently both clear α_bon = 0.005 by orders of magnitude. The combined H-NEW-53 finding (24/29 muq with kitāb OR qurʾān, p ≈ 3.17e-12) replicates with disaggregated per-root p-values both extreme.

## Surprises and findings beyond expectation

- **āyāt is the most novel new finding.** The "tilka āyātu al-kitāb" (these are the verses of the Book) formula appears in 11 of 29 muq surahs' v1-3 (37.9%) vs 5 of 85 non-muq (5.9%). This is essentially a muqaṭṭaʿāt fingerprint. Q 10, 11, 12, 13, 15, 26, 27, 28, 31, 41, 45 all use this formula at v1 immediately following the disconnected letters.

- **rabb is EXACTLY at expected (8 vs 8.14).** This is striking: the muqaṭṭaʿāt-opened surahs do NOT preferentially invoke "the Lord" in their first 3 verses. The enrichment is specifically for revelation-CONTENT, not divine-attribute, meta-references. This argues AGAINST a generic "muq surahs have richer openings" interpretation.

- **waʿd is ZERO/4.** No muqaṭṭaʿāt-opened surah has a waʿd-form in v1-3. Promise/covenant is anti-correlated (though not significantly so) with muqaṭṭaʿāt openings.

- **The PASS roots cluster semantically as "revelation-content meta-references"**: kitāb (the Book), qurʾān (the recited revelation), āyāt (the verses), nazala (the act of sending down). The NULL roots are theological/volitional/kerygmatic. The selectivity is interpretable, not noise.

## Surprises and changes from pre-reg

- None. Form lists locked in pre-reg were used unchanged. No re-tuning.

- One pre-reg consideration that worked as planned: r-b-b token-matching avoided false positives from أربعة (four), ربما (perhaps), اقترب (approach), etc. Without token-matching, naive substring "رب" gave 50 hits in v1-3; with token-matching, 32 hits — close to expected and yielding a properly-shaped null.

## Integrity audit

- Pre-reg file timestamped before script run: ✓
- Pre-reg SHA-256 embedded in JSON output: ✓
- All 10 roots reported with identical detail (PASS and NULL): ✓
- Bonferroni k=10 declared in pre-reg, used in verdict: ✓
- α_per = 0.005 applied uniformly: ✓
- Seed 20260416 fixed (irrelevant for closed-form, included for cross-finding bookkeeping): ✓
- MW-5 positive control PASSED: ✓
- MW-7 gate: rules tuple = (no-tashkeel; substring/token search on v1-3; surface forms locked) — fully specified.
- Closed-form hypergeometric (no permutation noise): ✓
- Two-sided (depleted PASS would also have been published; in this run no root showed significant DEPLETION): ✓

## Time

Total elapsed: <2 seconds (closed-form hypergeometric across 10 × 114 surah windows).

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-54-extended-root-enrichment-prereg.md`
- `/Users/grey/Downloads/quran/scripts/h_new_54_extended_root_enrichment.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-54.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-54-extended-root-enrichment.md`
- `/Users/grey/Downloads/quran/journal/h-new-54-run-1.md` (this file)
