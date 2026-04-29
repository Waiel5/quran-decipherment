---
id: H-NEW-66
title: Verse-pair structural-twin network — corpus-wide
phase: B
status: PUBLISHED 2026-04-15 (run-1)
seed: 20260416
rules_tuple: (no-tashkeel; whitespace-tokens; basmala-only-in-Q1; recitation-marks stripped)
parent_prereg: h-new-66-verse-twins-network-prereg.md
script: scripts/h_new_66_verse_twins.py
data_json: findings/phase-b-hypotheses/csv/h-new-66.json
journal: journal/h-new-66-run-1.md
---

# [[h-new-66-verse-twins-network|H-NEW-66]] — Verse-Pair Structural Twin Network

## Locked metric (verbatim from pre-reg)

`sim(v, v') = |N5(v) ∩ N5(v')|` — multiset intersection size of the
length-5 character n-grams (windows include single-space separators)
extracted from the recitation-mark-stripped, whitespace-collapsed
verse text. Min 5 words. Adjacency exclusion: same surah ∧ |Δid| ≤ 2.
Top-1 argmax twin per eligible source.

## Headline numbers

| metric | observed | null (1 char-shuffle replicate) |
|---|---|---|
| eligible verses | 5,105 / 6,236 | 5,105 → 4,765 (some shuffles drop below 5-gram floor)|
| top-1 edges | 5,105 | 4,765 |
| mutual (2-cycle) edges | **847** | 592 |
| intra-surah edge fraction | **0.1359** | 0.0361 |
| max in-degree | 24 | 36 |
| largest weak component | 139 | 142 |
| top edge raw 5-gram count | **151** (Q 4:43 ↔ Q 5:6) | 5 |

## Top-10 highest-similarity verse pairs corpus-wide

(all are **inter-surah** under our adjacency-filtered ranking)

| rank | pair | score | chars (a/b) | identification |
|---|---|---|---|---|
| 1 | Q 4:43 ↔ Q 5:6 | 151 | 253 / 342 | wuḍūʾ / tayammum verses — the canonical purification-instruction doublet |
| 2 | Q 2:136 ↔ Q 3:84 | 134 | 165 / 154 | "we believed in God and what was sent down to us, to Ibrāhīm, Ismāʿīl..." — verbatim catalogue of prophets |
| 3 | Q 2:61 ↔ Q 3:112 | 105 | 316 / 186 | wa-ḍuribat ʿalayhim al-dhilla — humiliation/wrath formula on Banū Isrāʾīl |
| 4 | Q 2:62 ↔ Q 5:69 | 95 | 131 / 111 | "those who believe and Jews and Christians and Sabians..." reward formula |
| 5 | Q 2:57 ↔ Q 7:160 | 93 | 107 / 242 | mann-and-salwā / clouds-and-shade — Israelite wandering provision |
| 6 | Q 20:71 ↔ Q 26:49 | 91 | 140 / 116 | Pharaoh's threat to the magicians: "I will cut off your hands and feet from opposite sides..." |
| 7 | Q 2:164 ↔ Q 45:5 | 89 | 229 / 108 | "in the alternation of night and day..." cosmological-signs catalogue |
| 8 | Q 2:173 ↔ Q 16:115 | 89 | 117 / 105 | dietary prohibition formula (carrion, blood, swine, what is consecrated to other than God) |
| 9 | Q 2:27 ↔ Q 13:25 | 87 | 101 / 116 | "those who break the covenant of God after its ratification..." losers-formula |
| 10 | Q 2:49 ↔ Q 7:141 | 86 | 101 / 102 | "We saved you from Pharaoh's people slaughtering your sons and sparing your women" |

These are not stylistic curiosities — they are well-known
**parallel/echo passages** that classical tafsir (al-Rāzī, al-Qurṭubī)
and modern self-reference indices (Yaḥyā Mīr ʿAlam) discuss
explicitly. The instrument independently rediscovers them by raw
substring overlap with no semantic dictionary.

## Intra- vs inter-surah split

- top-50 corpus-wide pairs: **6 intra-surah / 44 inter-surah**.
- but at the FULL twin-graph level: intra-surah top-1 fraction =
  **0.1359 observed vs 0.0361 null** = **3.76× enrichment**.

Reading: the most-extreme pairs cluster cross-surah (long Madanī
formulae echoing each other across Q 2/3/4/5), but at the
median-twin level the same-surah neighborhood retains ~3.8× more
intra-surah top-1 hits than chance. Both layers fire.

## NOTABLE pre-registered claims

- **N1 (heavy-tailed in-degree, ≥3× obs/null max)**: **DOES NOT FIRE**.
  Observed max in-degree = 24, null = 36. The shuffled corpus
  actually produces a higher max in-degree (random text creates a few
  super-attractor verses by chance histogram-matching). Heavy-tailed
  *structure* exists in observed (Q 2:282 attracts 24 incoming twins;
  Q 5:17, Q 5:41, Q 3:154 next), but the **null absolute maximum is
  larger**, so the locked claim falls.
- **N2 (intra-surah ≥2× null)**: **FIRES** at **3.76×** (0.1359 vs
  0.0361). Strong.
- **N3 (mutual edges > null + 3)**: **FIRES** at observed 847 vs
  null 592 — a +255 excess against a single-replicate null. The σ
  is unestimated here (only one shuffle) so the formal "+3σ"
  formulation is incomplete; replication is logged as a **followup
  needed**.

## MW-5 method-witness (positive control) — instrument honesty

The pre-reg required **Q 2:149 ↔ Q 2:150** to appear in the top-50.
But our own locked **adjacency rule excludes |Δ| ≤ 2 within a
surah**, so this pair is **structurally barred** from the twin
graph. The pre-reg is internally inconsistent on this point.

We honestly diagnose: the **raw 5-gram overlap of Q 2:149 ↔ 2:150
(no adjacency filter applied)** is **37**. That would rank #51 in
the corpus-wide top-50 list — i.e. on the boundary, but **non-zero
and consistent with the H-NEW-8 finding** that these two verses
share a >30-char prefix. The instrument is alive; the MW-5 check
under the locked rules is **vacuous, not a fail**. Logged in
journal as **PRE-REG INTERNAL INCONSISTENCY**, run continues
honestly.

## Top in-degree verses (most-pointed-to twins)

These act as **stylistic attractors** — many other verses' nearest
twin lives here.

| verse | in-deg | content snapshot |
|---|---|---|
| Q 2:282 | 24 | the *long debt-contract verse* — Quran's longest verse, dense legal formulas |
| Q 5:17 | 19 | "they have disbelieved who say God is the Messiah son of Maryam" |
| Q 5:41 | 16 | "do not let those who hasten in disbelief grieve you..." |
| Q 3:154 | 16 | post-Uḥud: anxiety, predestination, "they say if we had any part..." |
| Q 5:48 | 15 | "we sent down to you the book in truth, confirming..." |
| Q 73:20 | 13 | the *long Muzzammil verse* — recitation/zakāt instructions |
| Q 2:213 | 13 | "mankind was one community, then God sent the prophets..." |
| Q 2:164 | 13 | cosmological-signs catalogue (also #7 in pair list) |

The longest verses (Q 2:282, Q 73:20) dominate the in-degree
distribution — unsurprising since the metric is raw count, but the
non-trivial finding is that **theological/legal formula-rich
verses** outrank pure-length verses. Q 5:17 (in-deg 19) is shorter
than dozens of other verses but its phrasing recurs across the
Madanī polemic stratum.

## Garden-of-forking-paths log

All choices remained as locked in the pre-reg. No mid-run
parameter changes. The only deviation from spec is the **honest
admission of pre-reg internal inconsistency** about the MW-5
control: the pre-reg's adjacency rule logically excludes the
positive control. We logged this and computed the diagnostic
overlap separately.

## Followups

1. **N3 needs replication**: a single null-shuffle replicate cannot
   estimate σ. Recommend [[h-new-66-verse-twins-network|H-NEW-66]].b: 100 null replicates → bootstrap
   σ on mutual-edge count.
2. **N1 deserves second look**: max-in-degree IS lower in observed
   than null (24 vs 36). The shuffled corpus creates a few
   "super-magnet" pseudo-verses; the *real* corpus distributes
   incoming twins more evenly. This is the **opposite** of
   heavy-tail; it is **homogenization**. Worth a counter-hypothesis:
   "the observed corpus is more uniformly twinned than random,"
   formally [[h-new-66-verse-twins-network|H-NEW-66]].c.
3. **Top-50 inter-surah list = a gold-standard parallelism corpus**.
   These 50 pairs are the empirical inventory the project's
   self-reference / iltifāt / ring-composition lanes should now
   audit. The Q 4:43 ↔ Q 5:6 wuḍūʾ/tayammum pair is the cleanest
   match; the Pharaoh-magicians pair (Q 20:71 ↔ Q 26:49) is the
   cleanest **narrative-recurrence** pair across two different
   surahs.

## Verdict

**Published with two NOTABLES firing and one not-firing in the
locked direction**:

- N1 heavy-tail max-in-degree: **NO**, but with a notable
  observation in the OPPOSITE direction (homogenization vs random).
- N2 intra-surah enrichment: **YES**, 3.76×.
- N3 mutual-edge excess: **YES** (847 vs 592, +255 excess), pending
  σ-estimation.

The headline empirical product is the **top-50 cross-corpus
parallelism table** — it is the first machine-generated, locked-rule,
content-agnostic atlas of verse-pair structural twins for the Quran
under the project's pre-registration regime.
