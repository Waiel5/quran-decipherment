---
id: H-NEW-2010
title: Exhaustive root-frequency exact-equality balance scan — the "balanced-word miracle" tested mechanically across all 1,642 roots
date: 2026-05-29
status: NULL (pre-commit-direction REVERSED — meaningful balances UNDER-represented vs chance)
verdict: NULL-REVERSED
prereg: findings/phase-b-hypotheses/prereg-h-new-2010-root-frequency-balance-scan.md
prereg_sha256: c0d92b61a614af48cf14bbf455d86f39de9629facce6aef708be6887b9ce72b2
script: findings/phase-b-hypotheses/scripts/h-new-2010.py
data: findings/phase-b-hypotheses/csv/h-new-2010.json
seed: 20260509 (primary), 20260530 (replication)
n_perm: 10000
rules_tuple: (no-tashkeel, QAC-root, total-attestations, basmala-as-QAC, Hafs-Kufan, Mashriqi)
---

# H-NEW-2010 — Exhaustive root-frequency exact-equality balance scan

*A candidate-pattern generator: surface EVERY exact root-frequency balance in the corpus mechanically, then test — with a real permutation null — whether semantically-meaningful balances are over-represented. They are not. They are UNDER-represented.*

## 1. What was tested

The 20th-century numerical-iʿjāz literature (Nawfal 1983, *al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm*; Taslaman 2006; al-Kaheel) advertises ~15 hand-picked "balanced-word" pairs — al-dunyā/al-ākhira (claimed 115/115), al-malāʾika/al-shayāṭīn (88/88), al-ḥayāt/al-mawt (claimed 145/145), and so on. The project's earlier exploratory file `word-pair-symmetry.md` already showed (2026-04-12) that most of these FAIL at the off-the-shelf QAC lemma/root level, but its "null model" was an **eyeballed estimate** — never a real shuffle.

H-NEW-2010 does two things:

1. **The generator (deterministic).** Load all 1,642 QAC roots, compute each root's total corpus attestation count, build the inverted map `count → [roots]`, and enumerate EVERY pair of roots that share an exact count. This is exhaustive: it finds all balances mechanically, not a hand-picked subset.
2. **The one hypothesis test (T1).** Does the count of exact-balance pairs that fall within a **pre-registered, SHA-locked semantic group** (antonym / co-thematic, inherited from the independently-built `paired-opposites.csv` plus a fixed gazetteer) EXCEED the chance baseline obtained by shuffling the root→meaning labels 10,000 times across the fixed frequency distribution? Direction was **LOCKED HIGH** before computation.

## 2. The exhaustive scan (the generator output)

| Quantity | Value |
|:--|--:|
| Total QAC roots | 1,642 |
| Distinct corpus-attestation counts | 185 |
| Counts shared by ≥2 roots (buckets) | 93 |
| **Total exact-balance unordered root-pairs** | **118,584** |
| Roots with a UNIQUE count | 92 |

The bucket-size distribution is brutally heavy-tailed at the bottom: the count=1 bucket holds **395 roots**, count=2 holds **197**, count=3 holds **121**, count=4 holds **96**, count=5 holds **89**. Those five low-frequency buckets alone generate the overwhelming majority of the 118,584 "balances." **Exact equality is cheap.** With 1,642 roots and counts clustering on small integers, the pigeonhole principle guarantees tens of thousands of coincidental balances. The famous ~15 claims are a vanishingly small hand-picked slice of this pool — and, as shown below, they were picked at the *lemma* level, not the root level.

Selected high-count shared buckets (the only region where balance is non-trivial), full list in the JSON:

| Count | Roots in bucket |
|--:|:--|
| 201 | جنن jnn (garden), عند End (with/at) |
| 194 | نور nwr (light), حسن Hsn (good/beautiful) |
| 92 | ليل lyl (night), **سبح sbH (glorify)**, **سجد sjd (prostrate)** |
| 88 | **شطن $Tn (Satan)**, قرا qrA (recite/read) |
| 75 | علم Alm (pain), كلم klm (speech), شكر $kr (gratitude) |

## 3. The headline NULL — and its reversal

The pre-registered question was whether **semantically-meaningful** exact-balances appear MORE often than a random meaning-assignment would produce. The locked direction was HIGH (over-representation = the "design" hypothesis). The result is the opposite:

| Model variant | M_obs | Null mean | Null median | Null max | p (1-tailed, ≥) | Exceeds median? |
|:--|--:|--:|--:|--:|--:|:--:|
| **Full gazetteer** | **1** | 3.92 | 4 | 14 | **0.979** | NO |
| Antonym-only (Tier-A) | 0 | 2.95 | 3 | 11 | 1.000 | NO |
| Co-thematic-only (Tier-BC) | 1 | 0.97 | 1 | 6 | 0.640 | NO |
| Full, replication seed 20260530 | 1 | 3.92 | 4 | 14 | 0.979 | NO |
| **Decoy control (MW-6)** | 4 | 4.00 | 4 | 14 | 0.568 | — |

**M_obs = 1.** Across the entire corpus, exactly ONE pre-registered meaningful root-pair sits at an exactly-equal count: `sbH` (to glorify, tasbīḥ) and `sjd` (to prostrate), both at **92** — a co-thematic worship pair, not even an antonym. A random re-assignment of the same meaning-labels across the same frequency distribution produces, on average, **~4** such pairs.

So semantically-meaningful exact-balances are **UNDER-represented** relative to chance, not over-represented. This reverses the pre-committed HIGH direction. Per Protocol §1.8 this is published as a **NULL with an explicit pre-commit-violation flag** — not massaged, not silently re-pointed. The replication seed reproduces it exactly (p=0.979).

### The decoy control validates the instrument (MW-6)

A decoy gazetteer of the *same group sizes* but built from arbitrary, semantically-unrelated roots yields M_decoy = 4 ≈ null mean 4.0 (p=0.568) — exactly at chance. This is the crucial check: the instrument is NOT trivially inflating. A random gazetteer lands at chance; the *real* theological gazetteer lands BELOW chance. The under-representation is a genuine property of where the real antonym/thematic roots fall in the frequency distribution, not an artifact.

## 4. None of the 27 antonym families balance at the root level

The most direct refutation of the "balanced-word" claim: **zero** of the 27 locked antonym families have exactly-equal root counts.

| Family | Side A (root, count) | Side B (root, count) | Equal? |
|:--|:--|:--|:--:|
| dunyā / ākhira | dnw 133 | Axr 250 | NO |
| life / death | Hyy 184 | mwt 165 | NO |
| faith / disbelief | Amn 879 | kfr 525 | NO |
| guidance / misguidance | hdy 316 | Dll 191 | NO |
| heaven / earth | smw 381 | ArD 461 | NO |
| sun / moon | $ms 33 | qmr 27 | NO |
| good / evil | Hsn 194 | swA 167 | NO |
| reward / punishment | Ajr 108 | E*b 373 | NO |
| mercy / wrath | rHm 339 | gDb 24 | NO |
| (…all 27…) | | | **0 / 27 exact** |

The famous claims that *do* circulate (dunyā=ākhira=115, ḥayāt=mawt=145) require custom semantic filters applied to specific *lemmas* and inflected forms — never the raw QAC root counts. At the mechanical root level, the polar opposites of the Qurʾān are emphatically **not** numerically balanced. (Consistent with `word-pair-symmetry.md`: of 11 famous claims, only malak/shayṭān and Ādam/ʿĪsā survive off-the-shelf, and both are lemma-level, both inside multi-root buckets, both requiring post-hoc selection.)

## 5. The ranked "most-surprising" list

Because M_obs = 1, the entire ranked deliverable is a single pair:

| Rank | Count | Bucket size | Pair | Tier | Family |
|--:|--:|--:|:--|:--:|:--|
| 1 | 92 | 3 | sbH سبح (glorify) = sjd سجد (prostrate) | C | glorify/prostrate |

That this is the *only* meaningful exact-balance — and that it is co-thematic rather than antonymic — is the finding. The worship-verb pair tasbīḥ/sujūd sitting at 92 (the same bucket also holds *layl*, "night," echoing the Qurʾānic "glorify Him in the night… and at prostration," cf. Q 50:40, Q 76:26) is rhetorically pleasing but, against a null that expected ~4 such hits, statistically *unremarkable* — it is one hit where chance predicted four.

## 6. Verdict

**T1 = NULL (pre-commit-direction REVERSED).** Semantically-meaningful exact root-frequency balances are NOT over-represented in the Qurʾān; they are *under*-represented (1 observed vs ~4 expected by chance, p=0.979 in the locked HIGH direction; replicated; decoy-validated). The "balanced-word miracle," tested exhaustively and mechanically at the QAC-root level with a proper 10,000-permutation null, **does not survive**. The 118,584 exact balances that exist are pigeonhole coincidences of a heavy-tailed frequency distribution, and the handful that happen to be theologically meaningful are *fewer* than a random meaning-assignment would scatter there.

This is a clean, valuable NULL: it converts the earlier file's eyeballed "probably just chance" into a pre-registered, replicated, instrument-controlled empirical result, and it empirically retires the root-level balanced-word claim.

## 7. Honest limits

1. **Root ≠ lemma ≠ filtered-sense.** The famous claims operate on lemmas and custom-filtered counts; the QAC root conflates senses (e.g. mlk = king/angel/possess; *kr = male/remember). A lemma-level or sense-filtered scan could differ — but that is exactly the move (selective filtering) that the McKay-style critique flags as the source of the illusion. The root level is the *least* filter-dependent, hence the fairest test.
2. **Gazetteer is a judgement call.** Membership was SHA-locked before counts were consulted (inherited from the independently-built `paired-opposites.csv`), and MW-6 shows a random gazetteer of the same size lands at chance. A different defensible gazetteer could shift M_obs by a unit or two, but cannot plausibly reverse a result this far below the null median. An independent second-gazetteer replication is still required before any CONFIRMED-grade negative claim.
3. **Under-representation is not itself a positive finding.** M_obs=1 < null-median=4 is a direction reversal, but with p≈0.98 the data are equally consistent with "exactly at chance, low end." We do NOT claim the Qurʾān *avoids* balancing meaningful roots; we claim only that it does NOT balance them *more* than chance. The HIGH-direction hypothesis fails.
4. **Frequency is mute on intention.** Even a PASS could not have distinguished design from a property of theological-vocabulary frequency. The NULL is therefore the conservative, honest landing.

## 8. Cross-references

- Pre-reg: `prereg-h-new-2010-root-frequency-balance-scan.md` (SHA `c0d92b…ce72b2`).
- `word-pair-symmetry.md` — prior exploratory scan; H-NEW-2010 supersedes its §5 eyeballed null with a real permutation test.
- `paired-opposites.csv` — the 27 antonym families (Tier-A membership source); none balance at the root level.
- `paired-opposites-network.md` — opposite-pair co-occurrence network (a *co-occurrence* signal exists even though *count-balance* does not).
- Nawfal 1983, *al-Iʿjāz al-ʿadadī li-l-Qurʾān al-karīm* — primary numerical-balance source (FALSIFIABLE TARGET — falsified at root level here).
- al-Suyūṭī, *al-Itqān fī ʿulūm al-Qurʾān*, nawʿ 17 — classical attention to lexical *pairing*/ordering, NOT numerical count-balance (the count-miracle is a 20th-c. invention).
- Sibling generators: H-NEW-1810 (letter-frequency), H-NEW-1560/1800 (divine-names enumeration).

*Computed 2026-05-29 by Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.*
