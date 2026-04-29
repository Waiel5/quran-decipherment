---
id: H-NEW-45.2
title: The Q 50→Q 68 muqaṭṭaʿāt dead zone — does the 17-surah uninterrupted no-muqaṭṭaʿāt zone (Q 51-67) have distinctive structural properties?
status: PRE-REGISTERED 2026-04-16
spec_locked_at: 2026-04-16 (BEFORE viewing surah-content statistics for Q 51-67)
bonferroni_family: 2026-04-16-Wave-Muqattaat-Extended
bonferroni_k: 4
alpha_bon: 0.0125
rules_tuple: (hafs-kufan)
primary_data: surahs 51-67 (the 17-surah dead zone)
---

# [[h-new-45-2-dead-zone|H-NEW-45.2]] — Muqaṭṭaʿāt Dead Zone Q 51-67

## Background (from [[h-new-45-muqattaat-surah-index-number-theory|H-NEW-45]])

The 28 gaps between consecutive muqaṭṭaʿāt-opened surah indices include exactly ONE gap of 18 (Q 50 → Q 68). This means surahs 51-67 (17 surahs) form an uninterrupted "no-muqaṭṭaʿāt zone." This zone contains theologically/structurally exceptional surahs:

- Q 51 al-Dhāriyāt
- Q 52 al-Ṭūr
- Q 53 al-Najm (with the disputed "Satanic verses" historical episode)
- Q 54 al-Qamar
- Q 55 al-Raḥmān (the unique 31-refrain surah, classical "ʿArūs al-Qurʾān")
- Q 56 al-Wāqiʿah
- Q 57 al-Ḥadīd (iron; opens the 4-surah "musabbiḥāt" cluster Q 57, 59, 61, 62)
- Q 58 al-Mujādilah
- **Q 59 al-Ḥashr** — contains Khawātim al-Ḥashr (Q 59:22-24), the project's confirmed Ism al-Aʿẓam top-3 cluster
- Q 60 al-Mumtaḥanah
- Q 61 al-Ṣaff
- Q 62 al-Jumuʿah
- Q 63 al-Munāfiqūn
- Q 64 al-Taghābun
- Q 65 al-Ṭalāq
- Q 66 al-Taḥrīm
- Q 67 al-Mulk

## Question

Does this 17-surah dead zone have **distinctive content properties** that distinguish it from random 17-surah windows of similar length?

## The 4 pre-registered test cells

### Cell 1 — Divine-name density

Test statistic: divine-name count per word in the 17-surah zone, vs random-17-surah windows.
Direction: two-sided.

Hypothesis: zone is divine-name-DENSE because it contains Khawātim al-Ḥashr (which alone has 50% divine-name density at Q 59:23).

### Cell 2 — Average surah length (verses)

Test statistic: mean verse-count of the 17 surahs.
Direction: two-sided.

### Cell 3 — Mufaṣṣal-style indicator: rhyme-class entropy

Test statistic: rhyme-class entropy across the 17-surah zone (low entropy = strong rhyme-driven structure characteristic of mufaṣṣal).
Direction: one-sided lower (zone has stronger rhyme-uniformity).

### Cell 4 — Hapax density

Test statistic: hapax (lemma occurring exactly once in the Quran) count per word.
Direction: two-sided.

## Null model

10⁴ random 17-surah windows from {1..114} (with replacement of starting position). For each window:
- Compute the 4 cell statistics on the 17-surah union.
- Empirical p.

Seed = 20260416.

## MW-5 positive control

Use the well-known al-mufaṣṣal section (Q 49 onwards per al-Suyūṭī definition; or Q 50 onwards per al-Nawawī) as a positive control: the rhyme-class entropy should be LOW. If positive control fails, null is broken.

## Pre-committed verdict table

| Outcome | Verdict |
|---|---|
| 0 cells significant at α=0.0125 | NULL — zone is content-indistinguishable from random 17-surah windows |
| 1+ cells significant | PASS — zone has distinctive content properties consistent with the dead-zone-as-region hypothesis |
| Cell 1 PASS specifically | divine-name-dense reading confirmed → links Khawātim al-Ḥashr to muqaṭṭaʿāt-suppression mechanism |

## Mechanism interpretation

If divine-name density passes: the zone may be muqaṭṭaʿāt-suppressed BECAUSE its surface is already saturated with divine names — additional letter-mystery would be over-determined.

If rhyme-entropy passes (low): zone is mufaṣṣal-region; muqaṭṭaʿāt are not used in mufaṣṣal traditionally.

## Integrity

- Pre-reg locked before null run.
- Publish all 4 cells.
- Bonferroni k=4 declared before null.
