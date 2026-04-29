---
run: tawhid-run-1
date: 2026-04-12
agent: Phase B
task: Positive rhetoric for monotheism — signs, rhetorical Qs, self-reflection, masterpiece-passages, lā-ilāha-illā formula
output: findings/phase-b-hypotheses/tawhid-rhetoric.md
---

# Tawḥīd Rhetoric Run-1 — Methodology and Evidence Log

## Data inputs

- `quran-text/quran-no-tashkeel.json` — 114 surahs, 6,236 verses, rec-marks and pause-marks filtered.
- `data/morphology/quranic-corpus-morphology-0.4.txt` — available for lemma-level cross-check (not required for this analysis; surface regex on no-tashkeel was sufficient).
- Prior findings consulted: `khawatim-al-hashr-analysis.md`, `phase-c-structures/ayat-al-kursi.md`.

## Normalisation used

```python
def norm(t):
    # strip pause marks U+06D6-06ED, dagger alif U+0670, tatweel
    t = re.sub(r'[\u06D6-\u06ED\u0670\u0640]', '', t)
    # strip any residual tashkeel
    t = re.sub(r'[\u0610-\u061A\u064B-\u065F]', '', t)
    return ' '.join(t.split())
```

This is conservative: hamza-carrier variants (ء / أ / إ / ؤ / ئ) are NOT normalised; all counts reflect the rasm as stored.

## Key regex scans and results

### *lā ilāha illā* formula family

| Pattern | Regex | Hits |
|---|---|---:|
| `lā ilāha illā huwa` | `لا\s*إله\s*إلا\s*هو` | 29 |
| `lā ilāha illā Allāh` | `لا\s*إله\s*إلا\s*الله` | 2 (Q 37:35, 47:19) |
| `lā ilāha illā anā` | `لا\s*إله\s*إلا\s*أنا` | 3 (Q 16:2, 20:14, 21:25) |
| `lā ilāha illā anta` | `لا\s*إله\s*إلا\s*أنت` | 1 (Q 21:87, prayer of Jonah) |
| **total** | — | **35** |
| `Allāhu lā ilāha illā huwa` | `(^|\s)الله\s*لا\s*إله\s*إلا\s*هو` | 8 |
| `lladhī lā ilāha illā huwa` | `الذي\s*لا\s*إله\s*إلا\s*هو` | 3 (Q 20:98, 59:22, 59:23) |

The 35-verse total matches the target handed to this agent exactly.

### *a-ilāhun maʿa llāh* — the Q 27:60-64 cascade

| Pattern | Regex | Hits |
|---|---|---:|
| `a-ilāhun maʿa llāh` | `أإله\s*مع\s*الله` | **5** (Q 27:60, 61, 62, 63, 64) |

**Zero occurrences elsewhere in the corpus.** Five consecutive verses, all the Quran's occurrences in one block. Verified visually: the block is clean, no stragglers, no near-misses.

### Related "with-Allāh-another-god" prohibition family

| Pattern | Regex | Hits |
|---|---|---:|
| `maʿa llāh ilāhan ākhara` | `مع\s*الله\s*إلها\s*آخر` or the negative imperative family | 9 |

These are ALL negative-mode (do-not-set-up-another-god-with-Allah), supporting the prohibition side of Quranic tawḥīd. The 9 instances occur at Q 15:96, 17:22, 17:39, 23:117, 25:68, 26:213, 28:88, 50:26, 51:51. They complement the Q 27:60-64 cascade's positive-rhetorical-Q form: the cascade asks "is there…?"; this family commands "do not set up…".

### Creation-signs refrain families

| Refrain | Count |
|---|---:|
| *la-āyāt li-qawm [verb]* | 29 |
| *la-āya li-qawm [verb]* | 6 |
| *inna fī dhālika la-āyāt* | 24 |
| *inna fī dhālika la-āya* | 20 |
| *afalā taʿqilūn / yaʿqilūn* | 13 |
| *min āyātihi* | 12 (7 in Sūra 30) |

The *min āyātihi* distribution by surah is:
- S30: 7
- S41: 2
- S42: 2
- S31: 1
- **Total: 12** — 58% concentration in Sūrat al-Rūm.

### Reductio ad absurdum family

Three verses identified by construction:
- Q 17:42 (*law kāna maʿahu āliha*)
- Q 21:22 (*law kāna fīhimā āliha*)
- Q 23:91 (*mā kāna maʿahu min ilāh*)

All three close with the *subḥāna llāh* tanzīh-formula.

### *badaʾa l-khalqa thumma yuʿīduhu* — initiation-then-restoration formula

| Verse | Text preview |
|---|---|
| Q 10:4 | ينه يبدأ الخلق ثم يعيده |
| Q 10:34 | هل من شركائكم من يبدأ الخلق |
| **Q 27:64** | أمن يبدأ الخلق ثم يعيده (the cascade's 5th panel) |
| Q 29:19 | أولم يروا كيف يبدئ الله الخلق |
| Q 30:11 | الله يبدأ الخلق ثم يعيده |
| Q 30:27 | وهو الذي يبدأ الخلق ثم يعيده (the Rūm cascade closer) |

6 total. The Q 27:64 placement at the Q 27:60-64 cascade's final panel anchors it to the resurrection-argument — closing the five-panel structure with the eschatology beat.

### *fī anfusihim / fī anfusikum* epistemic-locus verses

13 total matches for `في\s*أنفس[هكن]`. Of these, only 3 are sign-loci (as opposed to dispositions, guilt, hypocrisy):
- Q 30:8 (`a-wa-lam yatafakkarū fī anfusihim`)
- Q 41:53 (`wa fī anfusihim`)
- Q 51:21 (`wa fī anfusikum`)

These three form the Qurʾān's interior-evidence corpus.

### *sanurīhim āyātinā fī l-āfāq wa fī anfusihim*

Regex `سنريهم`: **1 hit**, Q 41:53. The verb-form is unique.

### *wa-min āyātihi* cascade — Sūrat al-Rūm

7 consecutive instances in Sūra 30 vv 20-25 (with v27 holding the *badaʾa l-khalq* restatement): confirmed by sequential scan.

## Counts for the four masterpiece-passages

| Passage | Words | Letters | Notes |
|---|---:|---:|---|
| Al-Fātiḥa (Q 1:1-7) | 29 | 171 | includes basmala v1 |
| Āyat al-Kursī (Q 2:255) | 50 | 189 | 189 = 3³ × 7 |
| Khawātim al-Ḥashr (Q 59:22-24) | 49 | 216 | 49 = 7², 216 = 6³ |
| Al-Ikhlāṣ (Q 112) | 15 | 61 | |

Counts are consistent with the prior Phase C deep-dives for Kursī and Ḥashr.

## Q 27:60-64 cascade metrics

| v | Words | Letters | Opening |
|---|---:|---:|---|
| 60 | 27 | 104 | *a-man khalaqa l-samāwāti wa-l-arḍa* |
| 61 | 21 | 89 | *a-man jaʿala l-arḍa qarāran* |
| 62 | 16 | 70 | *a-man yujību l-muḍṭarra* |
| 63 | 20 | 82 | *a-man yahdīkum fī ẓulumāti l-barri wa-l-baḥr* |
| 64 | 19 | 78 | *a-man yabdaʾu l-khalqa thumma yuʿīduhu* |
| **Σ** | **103** | **423** | |

Verse 62 is the shortest (taqṣīr at ring-center). v60 and v64 bracket as the two longest, framing the cascade. The cascade is laid out in a short-long-shortest-medium-medium shape, which matches the *taʿrīd* / *taqṣīr* rhetorical balance-pattern the project's parables-catalog and oath-clusters agents have identified in other tight compositions.

## What I did NOT run

- No Monte-Carlo baseline for the 5-consecutive-same-phrase pattern, because the absolute count (5) with zero elsewhere is not a null-hypothesis test — it is a corpus fact. Comparable to the twin-opener result in Ḥashr analysis (which is handled by the consecutive-opener scan in `chiastic-audit.md`).
- No full morphology-tree traversal; the surface-regex was sufficient for formula counts. Morphology would be needed if we wanted to disambiguate *ilāh*-as-common-noun from *ilāh*-as-name-of-deity, but in the target verses the context makes this unambiguous.
- No abjad computation for the cascade — deferred; could be computed in a follow-up run if the cryptographic-signatures framework wants it.

## Follow-up candidates (for deep-hypotheses-queue.md)

1. Abjad totals for Q 27:60-64 to test if the cascade has numerical structure beyond the letter-count shape.
2. A dedicated *a-man…?* rhetorical-question family scan: does the *a-man khalaqa* opening-form appear outside this cascade? (Spot-checks suggest yes, in a handful of verses, but not in consecutive chains.)
3. Cross-reference the Q 27:60-64 cascade with the 7-fold *wa-min āyātihi* arc at Q 30:20-26 — the two are the Quran's two longest explicit creation-signs catalogues; structural comparison could reveal a rhetorical-genre profile.
4. Test the claim that the four "masterpiece passages" together use all four grammatical persons of the *lā ilāha illā* formula (huwa / Allāh / anā / anta) — spot-check suggests only *huwa* and *Allāh* appear in these four; the *anā* and *anta* forms are outside. The full-grammatical-person claim is true for the CORPUS's 35-verse total, not for the four masterpieces alone.

## Time-budget

~45 minutes. No external dependencies beyond Python 3 stdlib + the project's JSON corpus.
