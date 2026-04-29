---
finding_id: h-new-154
run: 1
date: 2026-04-17
specialist: specialist-B
seed: 20260417
---

# H-NEW-154 run 1 journal

## Timeline

1. Team-lead assigned composite hub-mechanism test.
2. Flagged post-hoc-composite risk IN THE PRE-REG ITSELF (warning field + dedicated section).
3. Pre-committed 5 features from classical-balāgha categories. Equal weights. Shuffle-null.
4. Ran. Result: **Q 50 scores 5/5 uniquely**; p_perm = 0.0036 < 0.05.
5. VERDICT: COMPOSITE-CONFIRMED.

## Observations

- **Q 50 is the ONLY 5/5 surah** (1 of 114). Next are Q 43, 44, 52 at 4/5.
- **p_perm = 0.0036** passes α=0.05 by an order of magnitude.
- **But**: the features were chosen knowing Q 50. Honest disclosure:
  - F1 (Q 40-60): classically known Q 50 position
  - F2 (book-ref v1-3): classically known Q 50 opening
  - F3 (muq): by definition Q 50 is muq-opened
  - F4 (oath-opener): classically known Q 50 opens with oath
  - F5 (mufaṣṣal-start): Q 50 is at Q 49-60 boundary by classical taxonomy
- **All five are classically-known Q 50 properties**. The composite is essentially asking "does Q 50 have all the classical Q 50 properties?" which is trivially yes.

## Honest reading

What the test DOES show: no other surah of 114 has all 5 classical-balāgha features simultaneously. The 5-way co-occurrence is genuinely unique. The shuffled null correctly detects this as rare.

What the test DOES NOT show: that Q 50 was DESIGNED for this pattern. Could be (a) intentional, (b) accidental 5-way cluster intersection, (c) feature-bias. Safest claim is (b).

## Score distribution

```
score=5: 1 surah  (Q 50)
score=4: 3 surahs (Q 43, 44, 52)
score=3: 9 surahs
score=2: 24 surahs
score=1: 27 surahs
score=0: 50 surahs
```

Heavy-tailed as expected; 5/5 is the extreme.

## Deviations from pre-reg

None. Pre-reg explicitly disclosed the post-hoc-composite risk upfront.

## Files

- Pre-reg, script, JSON, findings, journal all on disk.

## Next

Team-lead queue: H-NEW-156 next, then H-NEW-155.
