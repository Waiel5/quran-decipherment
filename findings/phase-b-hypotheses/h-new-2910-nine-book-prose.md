---
id: H-NEW-2910
title: "The nine-book vocalised-prose distribution — settling H-NEW-2890's 0.00010 margin"
date: 2026-08-07
author: Waiel Al-Shujaa
prereg: prereg-h-new-2910-nine-book-prose.md
prereg_sha256: 86aa22f76203001f03442976a729797a96b3dc74d89433efd3af98f2777833a8
run: runs/h-new-2910/20260807T153139Z/
verdict: "H-NEW-2890 ROBUST — its verdict stands as published"
verdict_code: ROBUST
seed: 20260509
seed_replication: 20260519
parents: [H-NEW-2890, H-NEW-2880, H-NEW-2870]
---

# H-NEW-2910 — nine books instead of two

**Verdict: H-NEW-2890 ROBUST — its verdict stands as published.**

## 1. Why this test exists

H-NEW-2890's verdict turned on **0.00010** — about six adjacent ḥadīth pairs out of 6,579 — and
its own `result.json` recorded `verdict_under_that_reading: PARTIAL` for the both-tuples case.
**A conclusion resting on one ten-thousandth of a single book-tuple combination is not settled.**

It rested on two books. The absence-claim sweep (H-NEW-2900) had found 50,884 fully vocalised
ḥadīth across **nine**. Seven were unused. Nine books replaces a knife-edge point estimate with a
distribution, which is what the margin question actually needed.

The re-verdict criterion — *if several books exceed the threshold, H-NEW-2890 is re-verdicted to
PARTIAL* — was locked in the pre-registration before any Δ was computed.

## 2. The distribution

Maximum Δ per book (readable), against the **+0.04672** threshold and this corpus's **+0.18690**:

| book | max P1 *(registered gate)* | max P2 | P2 vs threshold |
|:--|--:|--:|:--|
| tirmidhi | 0.01623 | 0.02011 | — |
| ahmed | 0.02632 | 0.03701 | — |
| abudawud | 0.02761 | 0.03864 | — |
| darimi | 0.02835 | 0.03954 | — |
| bukhari | 0.03180 | 0.04682 | **exceeds** |
| muslim | 0.03249 | 0.04537 | — |
| nasai | 0.03257 | 0.03823 | — |
| malik | 0.03768 | 0.04638 | — |
| ibnmajah | 0.04134 | 0.05357 | **exceeds** |

- **Prose mean across all books and tuples: 0.03556**
- **This corpus: 0.18690** — **5.3× the prose mean**, and **4.5× the highest single prose book on P1**

Mean unit lengths span **49.2–91.1** words, so the baseline is a
genuine range rather than two similar books.

## 3. The answer to the registered question

**On tuple P1 — the tuple prereg §7 names as the gate — zero of nine books reach the threshold.**
The prose maximum is Ibn Mājah at 0.04134 against 0.04672. The separation is clean across
all nine, and it was never close.

**And the unflattering half, which is what actually settles it:** al-Bukhārī S0 P2 at 0.04682 —
the value that made H-NEW-2890's margin look like luck — **is not the extreme.** Ibn Mājah P2 is
higher at 0.05357, and **two of nine books exceed the threshold on P2.**

So the both-tuples reading that returned PARTIAL for 2890 is **a real property of the P2 tuple
across books**, not a Bukhārī accident. H-NEW-2890's verdict survives **because P2 was never the
registered gate** — not because Bukhārī was unlucky. The 0.00010 margin was a P2 artefact; the
registered P1 result was never marginal.

## 4. What this does NOT settle

- It does **not** rehabilitate the P2 reading. Two books genuinely clear it.
- It does **not** touch the **P3 deflation**: a deliberately wrong pausal tuple also clears its
  own matched null (z = +8.99 against +15.03). The pausal *family* is isolated; al-Sajāwandī's
  specific rules are not.
- It does **not** dissolve the **3/12 D-P3 failures** on Ṣaḥīḥ Muslim under P1.

## 5. Honest limits

The baseline is ḥadīth. Vocalised *adab* prose and vocalised dīwāns remain genuinely absent from
this repository (H-NEW-2900 verified this with commands), so "vocalised Classical Arabic prose" is
represented here by one genre. A wider baseline could move these numbers.

Classical anchor: **al-Suyūṭī, *al-Itqān*, nawʿ 28, *fī maʿrifat al-waqf wa-l-ibtidāʾ***,
`data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt` line 5092 — recovered only
after three findings in this family had declared no citable primary source existed.
