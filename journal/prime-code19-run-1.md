# Journal — code19-audit run 1

**Agent:** code19-audit (Phase A+B)
**Date:** 2026-04-12
**Goal:** systematically test every Khalifa Code-19 claim from `claims-catalog.md` family A AND run an open prime-mod hunt across the Quran. Output: `findings/phase-a-replications/code19-khalifa-full-audit.md` and `findings/phase-b-hypotheses/prime-mod-scan.md`.

---

## Session log

### 12:14 — initial reading
Read `methodology.md` (anchors §8 are locked: 114 surahs, 6236 verses, 330709 letters, 77797 real-words, basmala = 19 letters / 4 words). Read `claims-catalog.md` family A in full (45 claims total in catalog; 12 are Khalifa Code-19 family + several auxiliary). Read `statistical-rigor-protocol.md` (McKay-style standard; pre-reg required for novel; 2-null-models requirement; Bonferroni vs Holm vs FDR).

Decided on the rule tuple in advance:
- orthography: no-tashkeel primary, with full-tashkeel and min-tashkeel as cross-checks
- letter regex: `[\u0621-\u064A\u0671-\u06D3]` excluding recitation marks U+06D6..U+06ED (this is what locks anchor 330709)
- word definition: real-word = whitespace token containing at least one letter from the regex
- basmala policy: counted-only-in-surah-1 (matches the dataset construction)
- verse numbering: hafs-kufan (6236 verses, 286 in al-Baqarah, etc.)
- abjad: mashriqi
- null model: §1.5 (permutation across surah indices) + binomial divisibility for the prime-mod hunt

### 12:25 — script v1: anchor sanity check
Wrote `/tmp/quran-code19/analyze.py` with `sanity_check()` first. **All anchors reproduce on first run.** This is critical: if anchors don't lock, every count downstream is suspect. Anchors hit:
- 114 surahs ✓
- 6236 verses ✓
- 330709 letters ✓
- 82375 whitespace tokens ✓
- 77797 real-word tokens ✓
- bismillah = 19 letters / 4 words ✓

Loaded the QAC morphology file (128219 segment rows) for lemma-based counts.

### 12:35 — Phase A: claim-by-claim replication

**Claim 1 (bismillah = 19 letters):** PASS (anchor).

**Claim 2 (basmala word counts):** the smoking-gun result.
- Standard QAC lemma counts: ism = 39, Allah = 2699, Rahman = 57, Rahim = 116.
- Khalifa's published numbers: 19, 2698, 57, 114.
- Allah and Rahim are off by 1 and 2 respectively.
- Hypothesis: Khalifa removed 9:128–129 (the famous controversy). Tested: yes, 9:128 contains exactly one rahim and 9:129 contains exactly one Allah. **Removing 9:128–129 brings Allah from 2699 to 2698 (matches Khalifa) but only brings Rahim from 116 to 115, NOT 114.**
- So Khalifa's Rahim claim **fails even after his textual edit**.
- ism = 19 is unrecoverable under any natural QAC filter (we tried bi+ism only, definite singular, root smw, etc.). Khalifa's 19-instance set was hand-curated and never algorithmically defined.
- **VERDICT:** 1 of 4 (Rahman) verifies under standard counting; 1 (Allah) verifies under 9:128-129 deletion; 2 fail. The "all four divisible by 19" claim is **false**.

**Claim 3 (114 = 19 × 6):** trivial PASS.

**Claim 4 (96:1–5 = 19 words, 76 letters):**
- no-tashkeel: 20 words, 78 letters
- full-tashkeel: 20 words, 76 letters
- min-tashkeel: 20 words, 76 letters
- The 76-letters claim **passes only under full-/min-tashkeel orthography** (which collapses 2 alifs).
- The 19-words claim **fails under every tokenization** — natural count is 20.
- **VERDICT:** PARTIAL.

**Claim 5 (96 is the 19th from the end):** trivial PASS by 114 = 19×6.

**Claim 6 (74:30 says "nineteen"):** text contains "تسعة عشر" — VERIFIED as text fact.

**Claim 7 (initial letters divisible by 19 in their surahs):** the central Khalifa claim.
- We tested every muqatta'at surah's sum of opening letters. **1 out of 29 sums to a multiple of 19.** Expected by chance: 1.526. **The claim catastrophically fails.**
- We tested specific famous claims: qaf in 50 = 57 PASS; qaf in 42 = 57 PASS; qaf-50+42 sum = 114 PASS; nun in 68 = 131 not 133 FAIL; sad in 38 = 29 FAIL; ya+sin in 36 = 261 FAIL; KHY'S in 19 = 740 FAIL; HM'SQ in 42 = 556 FAIL; HM cluster grand total = 2112 FAIL.
- **The qaf-50/42 trio is the ONLY non-trivial Khalifa survivor.**

**Claim 8 (29 muqatta'at total verse count):** 2743 verses, 2743/19 = 144.37 — FAIL.

**Khalifa grand total 346199:** OUR sum = 346458 (with all 6236 verses). **= 346199 if we delete 9:128-129** — verified by computing the surah-9 contribution change exactly: (127+127·128/2) − (129+129·130/2) = −259, and 346458 − 259 = 346199. **PASSES UNDER DELETION.** This is the cleanest demonstration that Khalifa's grand-total claim is *purely* a function of the textual edit. No other arithmetic adjustment recovers it.

**Basmala in 27:30:** text confirmed; 27 + 30 = 57 = 19 × 3 (small-int coincidence).

### 13:10 — Khalifa's published ALM letter counts

This was the most damning part of the audit. I fetched Khalifa's published per-surah ALM counts (Quran Talk blog cites them directly from Appendix 1 of *Quran: The Final Testament*). For each of the six ALM-prefixed surahs (2, 3, 29, 30, 31, 32) I cross-checked Khalifa's alif/lam/mim counts against three orthographies of our text.

**Striking pattern:** for *every one* of the 6 surahs, Khalifa's alif count sits *between* our no-tashkeel and full-tashkeel counts:

| surah | full-tashkeel alif | Khalifa alif | no-tashkeel alif |
|---|---|---|---|
| 2 | 4214 | **4502** | 4716 |
| 3 | 2351 | **2521** | 2659 |
| 29 | 712 | **774** | 812 |
| 30 | 493 | **544** | 558 |
| 31 | 337 | **347** | 386 |
| 32 | 242 | **257** | 277 |

His lam and mim counts almost match our no-tashkeel (off by 1–4). His alif counts hit *no fixed convention*. He must have applied a per-surah-tuned alif-counting rule.

The Khalifa-aligned rebuttal (Quran Talk blog) tacitly admits this: confronted with the discrepancy, the author claims that **Khalifa typed the wrong individual numbers and God corrected his totals as he typed them into his computer**. This is the canonical motivated-reasoning move and is unfalsifiable.

Of our 6 ALM totals across 3 orthographies = 18 numbers, only 1 (Surah 30 under full-tashkeel: 1197 = 19 × 63) is divisible by 19. The expected by chance is 18/19 = 0.95. **Consistent with chance.**

### 13:25 — Phase B: open prime-mod hunt

Computed 8 primes × 4 metrics × 114 surahs = 32 binomial tests for "fraction of surahs whose statistic divides by p."

| | letters | words | verses | abjad |
|---|---|---|---|---|
| p=7 | 13 vs 16.3 | 9 vs 16.3 | 14 vs 16.3 | 14 vs 16.3 |
| p=11 | 11 vs 10.4 | 10 vs 10.4 | **17 vs 10.4** | 10 vs 10.4 |
| p=13 | 11 vs 8.8 | 7 vs 8.8 | 9 vs 8.8 | 10 vs 8.8 |
| p=17 | 3 vs 6.7 | 4 vs 6.7 | 3 vs 6.7 | 9 vs 6.7 |
| **p=19** | **3 vs 6** | **8 vs 6** | **4 vs 6** | **5 vs 6** |
| p=23 | 5 vs 5.0 | 6 vs 5.0 | 2 vs 5.0 | 5 vs 5.0 |
| p=29 | 2 vs 3.9 | 2 vs 3.9 | 3 vs 3.9 | 5 vs 3.9 |
| p=31 | 2 vs 3.7 | 2 vs 3.7 | 3 vs 3.7 | 5 vs 3.7 |

**Minimum raw p across all 32 tests: 0.056** (words mod 7 AND verses mod 11). **Bonferroni threshold: 0.00156. Holm: same minimum. ZERO tests significant.**

**The Khalifa hypothesis is empirically empty.** p = 19 does not stand out from {7, 11, 13, 17, 23, 29, 31}. The four metrics for p = 19 give 3, 8, 4, 5 — none statistically distinguishable from the chance expectation of 6.

### 13:40 — Muqatta'at density test (the surprise positive)

Although Khalifa's divisibility claim collapses, I noticed during the per-letter computations that the muqatta'at letters seemed to be over-represented in their surahs. I built a more rigorous test: for each (surah, opening-letter) pair compute the z-score against global frequency; compare to a matched control of (random non-muqatta'at surah, opening-letter) pairs.

Result: **muqatta'at letter density is real**:
- 19/78 muqatta'at pairs significant at uncorrected p < 0.05 (vs ~4 expected at chance)
- 5/78 survive Bonferroni (highly conservative)
- chi² = 228.78 on df = 78 (critical at 0.05 ≈ 104; this is p < 10⁻¹⁵)
- |z| > 2 in 17.9% of muqatta'at pairs vs 9.2% in matched control (1190 pairs)

**This is a real linguistic signal but it is not the Khalifa claim.** It is consistent with the classical observation (Welch 1986) that muqatta'at echo their surah's phonology, and is *not* a divisibility-by-19 phenomenon. I flagged it for Phase-B pre-registration as a separate hypothesis (would require: pre-reg, second null model from a different §1 row, robustness across orthographies).

Top hits:
1. Surah 50, qaf (z = +4.45) — same as the qaf survivor from claim 7
2. Surah 3, lam (z = +4.13)
3. Surah 13, lam (z = +3.61)
4. Surah 2, lam (z = +3.28)
5. Surah 19, ya (z = +3.24)

### 14:05 — Web search for prior work

Searched for McKay-style statistical refutation of Khalifa Code-19 in peer-reviewed literature. **Found none.** The major refutations are:
- Bilal Philips, *The Qur'an's Numerical Miracle: Hoax or Heresy?* (1987) — Sunni religious refutation, not statistical
- WikiIslam articles — polemical
- Various blogs (answering-christianity, etc.) — informal
- Wikipedia "Quran code" article — reference summary

**No peer-reviewed paper has applied the McKay et al. 1999 *Solving the Bible Code Puzzle* methodology to Khalifa's work.** The catalog YAML in `claims-catalog.md` already noted this; I confirmed it through fresh search. This is a documented research opportunity for the methodology paper described in `statistical-rigor-protocol.md §6`.

Notable finding from the search: the Quran Talk blog post on Khalifa's lam counts (2020) explicitly acknowledges that Khalifa's individual numbers don't reproduce — and proposes that Khalifa typed wrong numbers but God corrected the totals. This is the unfalsifiable-program move at its purest.

### 14:30 — Writing up

Wrote the full audit at `findings/phase-a-replications/code19-khalifa-full-audit.md` (~12k words; per-claim verdict table; methodology; honest discussion of motivated reasoning; survivors section; density signal; checklist). Wrote the prime-mod scan at `findings/phase-b-hypotheses/prime-mod-scan.md` (~3k words; full results tables; correction analysis; null verdict). Wrote this journal.

---

## Lessons learned

1. **The 9:128–129 deletion is the load-bearing trick of Khalifa's program.** Without it, both the Allah word count and the grand-total formula fail. With it, only Allah is fully fixed; Rahim is still off by 1. This makes me suspect that Khalifa's Rahim claim was **always wrong** and was just published anyway.

2. **The qaf-50/42 result is genuinely interesting** and is the only Khalifa muqatta'at claim I can defend statistically. Two pre-specified surahs (the only two with qaf in their opening letters) both having exactly 57 qafs is unusual. I flagged it for Phase-B pre-registration but did not promote it to "finding" status — by stat-rigor §3, that requires pre-registration before the data is touched, and we found this by inspecting the data.

3. **The muqatta'at density signal (chi² = 228.78) is the most interesting positive result** of the audit. It is *not* a Khalifa claim — it is a much weaker observation about linguistic structure. It deserves a Phase-B pre-registration.

4. **Khalifa's published ALM letter counts are unrecoverable under any standard orthography.** The alif counts in particular float between conventions in a way that no honest counting scheme could produce. This is the strongest single piece of empirical evidence against Khalifa's good faith — combined with the textual deletion of 9:128-129, the picture is of an analyst who tuned counts to fit and then defended the tuning post-hoc.

5. **The open prime-mod hunt is conclusive null.** This is the cleanest possible result for the "is 19 special at the surah level" question. No.

## Open issues and follow-ups

- **Pre-register the qaf-50/42 hypothesis** before running additional tests. The pre-reg should specify: "the two muqatta'at surahs whose opening contains the letter qaf both have exactly 57 instances of qaf in their text body." This is a single test; the rules tuple is no-tashkeel/graphemes/basmala-counted-only-in-surah-1. The null model should be a permutation of surah indices (does any pair-of-surahs have exactly equal letter counts that sum to 19k?) plus a comparable-corpus draw from early hadith.

- **Pre-register the muqatta'at density signal** as a separate Phase-B hypothesis. The pre-reg should specify: "the chi-squared statistic for the 14 muqatta'at letters in their host surahs vs global frequency expectation is significantly large, AND the matched-control rate in non-muqatta'at surahs is significantly lower." Test under both no-tashkeel and full-tashkeel.

- **Test family-B (Al-Kaheel sevens) under a similar prime-mod framework.** Our `p = 7` results show no significant deviation, but Kaheel-style claims are about derived statistics (e.g., "from first Allah to last Allah is 6223 verses = 7 × 889") which our metric grid doesn't capture. Would require its own audit.

- **Check the Khalifa Surah 30 ALM result (1197 = 19 × 63 under full-tashkeel)** more carefully. This is 1 of 18 random tests, so it is consistent with chance, but it's also our text disagreeing with Khalifa's text. May indicate that Khalifa was using a pre-Tanzil orthographic convention for ONE of his counts but not the others, which would be evidence of arithmetic instability.

- **Cross-verify our basmala-word counts** against the Tanzil project's morphology output independently. Our QAC counts could have edge-case errors I'm not aware of. If Tanzil agrees with us (Allah = 2699, Rahim = 116) under standard text, that would lock in the failure of Khalifa's claims. (This is on the toolsmith agent's queue, not mine.)

## Files produced

- `/Users/grey/Downloads/quran/findings/phase-a-replications/code19-khalifa-full-audit.md` — full Khalifa audit, ~12k words
- `/Users/grey/Downloads/quran/findings/phase-b-hypotheses/prime-mod-scan.md` — open prime-mod hunt, null result
- `/Users/grey/Downloads/quran/journal/prime-code19-run-1.md` — this journal
- `/tmp/quran-code19/analyze.py` — main analysis script (sanity check + Phase A claims + Phase B prime hunt + density test)
- `/tmp/quran-code19/refine.py` — 9:128-129 deletion analysis
- `/tmp/quran-code19/refine2.py` — ism / 96:1-5 word-count investigation
- `/tmp/quran-code19/refine3.py` — Surah 2 ALM full-orthography sweep
- `/tmp/quran-code19/final_compute.py` — final cross-check tables
- `/tmp/quran-code19/null_models.py` — within-verse shuffle and global-frequency baselines
- `/tmp/quran-code19/density_test.py` — muqatta'at letter density test (the surprise positive)
