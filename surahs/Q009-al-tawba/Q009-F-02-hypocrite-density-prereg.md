---
finding_id: Q009-F-02
prereg_date: 2026-04-28
prereg_type: rules-tuple-stable corpus-percentile audit
status: PRE-REGISTERED
---

# Q009-F-02 — Hypocrite-vocabulary density audit (pre-registration)

## 1. Hypothesis (DIRECTION-LOCKED)

**H1**: Q 9 al-Tawba's per-1000-token hypocrisy-vocabulary density (root n-f-q, "nfq" in QAC) is **in the top-decile** of the 114-surah distribution (rank ≤ 12 of 114).

Classical-claim correlate: al-Bukhārī via Ibn ʿAbbās (al-Suyūṭī *al-Itqān* nawʿ 9, citing al-Bukhārī): "*hiya al-Faḍiḥa, mā zālat tanzilu* «*wa-minhum…wa-minhum*» *ḥattā ẓananna an lā yabqā aḥadun illā dhukira fīhā*" ("It is *al-Faḍiḥa*, the Exposer; verses kept being revealed «and among them … and among them …» until we feared no one would remain unmentioned in it"). The classical naming directly implies that Q 9 outscores all other surahs on hypocrisy-vocabulary.

**Direction**: rank-from-top, low (i.e. high density). LOCKED before observing.

## 2. Null hypothesis

**H0**: Q 9 hypocrisy-density rank is uniformly distributed in {1..114}; the probability of rank ≤ 12 is 12/114 ≈ 10.5%.

## 3. Rules-tuple

- corpus: `quran-text/quran-no-tashkeel.json`
- tokens: orthographic-word; tokenize by whitespace
- root index: `data/morphology/root-index.json` (QAC v0.4)
- root-of-interest: `nfq` (Buckwalter; Arabic ن-ف-ق)
- density: 1000 × Q9-count / Q9-tokens
- rank: descending (1 = highest)

## 4. Pre-committed thresholds

| Outcome | Q9 rank-from-top | Verdict |
|:--|:--|:--|
| Q9 rank ≤ 12 | top-decile | **VINDICATED** al-Faḍiḥa naming |
| Q9 rank 13-28 | top-quartile but not top-decile | **DIRECTIONAL** |
| Q9 rank > 28 | | **FALSIFIED** classical claim |

## 5. Bonferroni correction

Family k = 5; α_bon = 0.01.

## 6. Method

Identical to F-01 with root replaced.

## 7. Replication

Repeat with root `kfr` (disbelief) — al-Faḍiḥa naming implies Q 9 should ALSO be hypocrisy-distinctive but NOT just generally disbelief-distinctive. Differential test: Q 9 rank(nfq) - Q 9 rank(kfr) should be NEGATIVE (closer to top in hypocrisy than in disbelief).

## 8. Pre-commit locked.
