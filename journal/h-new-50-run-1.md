---
hypothesis: H-NEW-50
run: 1
date: 2026-04-15
agent: h-new-50-specialist
status: COMPLETE
verdict: CLASSICAL-COINCIDENCE-CONFIRMED-BUT-NOT-STATISTICALLY-RARE
---

# H-NEW-50 — Run 1 journal

## Setup

- Pre-reg: `findings/phase-b-hypotheses/h-new-50-bismillah-114-prereg.md` (locked 2026-04-15)
- Script: `scripts/h_new_50_bismillah_114.py`
- JSON output: `findings/phase-b-hypotheses/csv/h-new-50.json`
- Findings: `findings/phase-b-hypotheses/h-new-50-bismillah-114.md`
- Seed: 20260415; N_PERM = 100,000; Bonferroni k=4, α_bon = 0.0125

## What was done

1. Loaded Tanzil simple-clean text (`data/alt-text/quran-simple-clean-txt.txt`, 6266 lines), aligned to the 6236 numbered verses + 30 prepended basmala lines (technically: simple-clean has 6266 lines if you count the basmalas-prepended-as-headers — but in this case basmala IS prepended INTO v1 of every surah except Q 9, giving 6236 verse lines in total).
2. Verified mechanical count: 113 line-starts begin with basmala; 1 internal at Q 27:30. Confirmed.
3. Computed Cell 2 analytically across 16 prior combinations (4 lambdas × 4 deletion rates) and Monte Carlo verified at λ=1, p=1/114. Conditional Pr(d=i=1 | d=i) ranges 0.005–0.46.
4. Cell 3: enumerated all within-verse 4-grams (after stripping basmala prefix from prepended lines) and looked for any 4-gram with count ∈ {113, 114, 115}. Found: ZERO others.
5. Cell 4: tested Q 27 = median(muqaṭṭaʿāt) (FALSE; median = 29), 30 = n_ajzāʾ (TRUE but trivial), 27+30 = 57 = al-Ḥadīd (curiosity).
6. Cross-checked counts across 3 text variants (simple-clean, no-tashkeel JSON, full-tashkeel JSON). All consistent under their respective conventions.

## Key results

- Cell 1: PASS (113 + 1 = 114 confirmed)
- Cell 2: NOT-RARE (Pr range 0.005–0.46; modal outcome ~0.44 under empirical priors)
- Cell 3: UNIQUE (zero other 4-grams with count 113–115; basmala is structurally singular)
- Cell 4: WEAK SALIENCE (Q 27 not median; verse 30 = ajzāʾ is trivial; 27+30=57 is curiosity only)

## Composite

CLASSICAL-COINCIDENCE-CONFIRMED-BUT-NOT-STATISTICALLY-RARE.

## Surprises and changes from pre-reg

- **Q 27 is NOT the median muqaṭṭaʿāt-opened surah.** I had loosely expected this from the eyeball pattern. The actual median of the 29-element muqaṭṭaʿāt-opened set is **29** (Q al-ʿAnkabūt), not 27. Q 27 is at 0-based position 12 in the sorted list — slightly LEFT of center, not center. This was a hypothesis Cell 4(a) and it FAILED.
- **27 + 30 = 57 = al-Ḥadīd** is a striking arithmetic identity — al-Ḥadīd is a Medinan surah whose name means "iron" and which holds the abjad-letter ḥ-d-y-d (8+4+10+4 = 26 in mashriqi, depending on convention). I am flagging this as a follow-up but did NOT pre-register it as a Cell.
- The empirical prior distribution for `λ` (rate of internal basmalas under a "scribal-error" model) is ill-defined; I used a 4-grid sensitivity analysis and reported the range. The composite verdict is robust to this choice (Pr ranges 0.005–0.46; only at λ≥5 + p_del≥0.10 does it become rare, which is an implausibly broad prior).

## Integrity audit

- Pre-reg file timestamped before script run: ✓
- All 4 cells published: ✓
- Bonferroni k=4 declared in pre-reg, used in verdict: ✓
- Seed 20260415 fixed: ✓
- Cross-validated across 3 text variants: ✓
- MW-5 positive control: Cell 3 itself acts as a positive-control sweep — if any other 4-word phrase had matched the 113+1 pattern, the basmala uniqueness would be DEMOTED. None did. Pipeline behaves correctly.
- MW-7 gate: rules tuple = (no-tashkeel; hafs-kufan; basmala-as-prepended-line per Tanzil simple-clean; substring match) — fully specified.

## Time

Total elapsed: ~1 second (cell 2 MC dominates).

## Files written

- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-50-bismillah-114-prereg.md`
- `/Users/grey/Downloads/quran/scripts/h_new_50_bismillah_114.py`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-50.json`
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-50-bismillah-114.md`
- `/Users/grey/Downloads/quran/journal/h-new-50-run-1.md` (this file)
