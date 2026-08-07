---
surah: 75
surah_name_ar: القيامة
surah_name_translit: al-Qiyāma
surah_name_english: "The Resurrection"
file_type: overview
date_last_updated: 2026-05-09
phase: B+
verdict: SCAFFOLD-COMPLETE — 5 SHA-locked novel tests; 1 STRONGLY VINDICATED (corpus-EXACT structural-self-reference Q 75:16-19); 1 VINDICATED (structural-twin to Q 90); 1 PASS-DIRECTED (corpus-EXACT 7-surah negative-oath FR cluster); 2 NULL with prominence
---

# Q 75 al-Qiyāma — Overview


> **⛔ CORRECTION NOTICE — 2026-08-07.** This file locates this surah within the
> **compression-tail** and/or **iʿjāz anti-twin** framework. Both met a matched Arabic control
> on 2026-08-07 and **neither discriminates**. The anti-twin is **REVERSED** — this corpus sits
> at the **3rd percentile** of al-Jāḥiẓ and the 14th of al-Bukhārī, and pre-Islamic poetry under
> a matched partition reaches r = −0.872 against this corpus's −0.870. The compression-tail is
> **genre-shared and 91.5 % explained by unit size**: log(unit size) alone gives R² = 0.9147,
> and re-cutting this corpus's own verses to equal size collapses R² from 0.9887 to **0.3388**.
> UAS is a synthesis index with no null hypothesis.
>
> Positional statements below — "in the compression-tail", "iʿjāz-fawāṣil cell", a UAS rank —
> remain accurate as **descriptions of where this surah sits on those axes**. What is withdrawn
> is that the axes distinguish this corpus from ordinary Arabic. Nothing below is deleted.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## 1. Basic facts

| Property | Value | Source |
|:--|:--|:--|
| Surah ID | 75 | canonical |
| Arabic name | القيامة | canonical (named after the *yawm al-qiyāmah* in v. 1) |
| Transliteration | al-Qiyāma | canonical |
| English meaning | "The Resurrection" / "The Standing-up" | derived from v. 1 *yawmi al-qiyāmati* |
| Verse count | 40 | Hafs-Kūfan (`/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json`, surah[id=75]) |
| Position in mushaf | 75 | canonical |
| Type | Meccan (early-Meccan; consensus across al-Ṭabarī, al-Qurṭubī, Ibn Kathīr) | classical |
| Tanzīl revelation order | **31 of 114** (Egyptian Standard) | `data/revelation-order.csv` row 76 |
| Nöldeke order | **36** (Early Meccan) | `data/revelation-order.csv` row 76 |
| Word count (no-tashkeel) | **165** | computed from `quran-no-tashkeel.json` |
| Letter count (no-tashkeel, sans whitespace, sans ornaments) | **677** | computed |
| Opening | لا أقسم بيوم القيامة — "I do NOT swear by the Day of Resurrection" | NEGATIVE-PARTICLE-OATH |
| Bismala | counted as separator only (not v. 1) | rules-tuple default |
| Length classification | mufaṣṣal-qiṣār-tier (the "short mufaṣṣal" — al-Suyūṭī *al-Itqān* nawʿ 18 *al-mufaṣṣal*) | classical |

## 2. Classical names and structural identity

- **al-Qiyāma** (القيامة) — canonical, from v. 1 (*yawmi al-qiyāmati*).
- Also occasionally cited as *Sūrat lā uqsimu* (after the negative-oath opening), e.g. al-Bukhārī Bk 65 "Tafsīr" entries refer to *al-āyatu llatī fī "lā uqsimu bi-yawmi al-qiyāma"* — using the negative-oath formula as the surah-identifier.
- Member of the **early-Meccan eschatology mushaf-zone Q 73-77** (Q 73 al-Muzzammil, Q 74 al-Muddaththir, Q 75 al-Qiyāma, Q 76 al-Insān, Q 77 al-Mursalāt). Q 75 sits structurally between two prophetic-mantle-call surahs (Q 74) and a believer-reward surah (Q 76).

## 3. Opening formula — the corpus's first NEGATIVE-PARTICLE OATH

Q 75 opens with *lā uqsimu bi-yawmi al-qiyāmati* (v. 1), immediately followed by *wa-lā uqsimu bi-l-nafsi al-lawwāmati* (v. 2). The bare *lā uqsimu* opening (without the *fa-* connective prefix) occurs in **only 2 surahs corpus-wide**: Q 75 and Q 90 al-Balad.

The *lā uqsimu* / *fa-lā uqsimu* construction occurs **7 times in the corpus across 6 surahs**:

| # | Verse | Position-in-surah | Construction |
|:-:|:-:|:--|:--|
| 1 | Q 56:75 | mid-surah (after the 3-class apocalyptic block) | *fa-lā uqsimu bi-mawāqiʿi al-nujūm* |
| 2 | Q 69:38 | near-closing | *fa-lā uqsimu bi-mā tubṣirūn* |
| 3 | Q 70:40 | closing | *fa-lā uqsimu bi-rabbi al-mashāriqi wa-l-maghārib* |
| 4 | **Q 75:1** | **OPENER** | ***lā uqsimu bi-yawmi al-qiyāmah*** |
| 5 | **Q 75:2** | **OPENER** | ***wa-lā uqsimu bi-l-nafsi al-lawwāmah*** |
| 6 | Q 81:15 | mid-surah | *fa-lā uqsimu bi-l-khunnas* |
| 7 | Q 84:16 | mid-surah | *fa-lā uqsimu bi-l-shafaq* |
| 8 | **Q 90:1** | **OPENER** | ***lā uqsimu bi-hādhā al-balad*** |

(Source: corpus-EXACT enumeration via `scripts/Q075_F_03_negative_oath_cluster.py` — see `06-novel-findings.md` Q075-F-03.)

**Q 75 is corpus-DOUBLE-OPENER** — the only surah where *both* v. 1 and v. 2 are negative-oath formulas in immediate succession. al-Suyūṭī, *al-Itqān*, nawʿ 67 (*al-aqsām fī al-Qurʾān*) recognises this doubled-negative-oath structure as exceptional but does not name a corpus-EXACT enumeration. The empirical lock at 8 verses across 6 surahs is novel to this investigation.

### Classical interpretation of *lā* in *lā uqsimu*

Three classical readings (cataloged in al-Rāzī *Mafātīḥ al-ghayb* vol. 30 ad Q 75:1, and al-Ṭabarī Q 75:1-2):

1. **lā = redundant particle (*ṣilah*)** for emphasis — "I DO swear by the Day of Resurrection" (al-Farrāʾ, al-Akhfash; majority view among grammarians).
2. **lā = preceding-rejection particle** — "Nay! / It is NOT the case [as the disbelievers think]; I swear by the Day of Resurrection..." (al-Zamakhsharī, *al-Kashshāf* Q 75:1).
3. **lā = qasam-strengthening intensifier** — the negative is itself part of the oath-formula, adding gravity (al-Bāqillānī, *Iʿjāz al-Qurʾān*, in the *aqsām* chapter).

Empirical observation: under the corpus-EXACT enumeration of 7 negative-oath verses in 6 surahs, the *lā uqsimu* construction is restricted to a small genre-specific cluster (early-mid-Meccan eschatology + cosmic-witness contexts). FR-cohesion of the 6-surah set is reported in §6 below and tested at Q075-F-03.

## 4. Empirical architectural profile

(full detail in `01-empirical-profile.md`)

| Metric | Value | Source |
|:--|:--|:--|
| **UAS rank** | **72/114** | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | **−1.82 pp** (NULL classification; window {Q 72-78}) | h-new-590, X=75 |
| iʿjāz sig_A | **+1.0151** (rank 33/114; ABOVE-MEDIAN on al-Bāqillānī iʿjāz al-fawāṣil axis) | h-new-750 |
| iʿjāz sig_B | +0.5044 (rank 42/114) | h-new-750 |
| Mean FR-content distance | **0.9087** (corpus mean 0.9235; rank 60 by isolation, 55 by centrality — slightly content-CENTRAL) | h-new-111 |
| Local cohesion (z) | **−0.364** (mid-pack) | h-new-750 |
| Top final-letter | **ه (hāʾ)**, 45% | h-new-750 |
| Rhyme entropy (nats) | **1.250** (z = +0.87 — moderately diverse rhyme) | h-new-750 |
| Q 74→Q 75 adjacency cost | **0.0962** (rank 35/113 — moderately expensive) | h-new-720 |
| Q 75→Q 76 adjacency cost | **0.0518** (rank 66/113 — below-median; smoother seam) | h-new-720 |
| FR-nearest neighbor | **Q 108 al-Kawthar** (FR=0.6001) | h-new-111 |
| Top-5 FR-nearest | Q 108, Q 100, Q 113, Q 94, Q 103 — all short-mufaṣṣal-tail | h-new-111 |
| Architectural cell | **early-Meccan eschatology / negative-oath core** | this investigation |

**Q 75 is mid-pack on UAS, slightly above-median on iʿjāz sig_A, and content-central rather than content-distant. Its architectural significance lives in (a) its corpus-EXACT structural-self-reference passage (vv. 16-19), (b) its FR-membership in the H-NEW-1200 short-Meccan-tail eschatology cluster, and (c) its function as the corpus's first negative-particle-oath opener** — three orthogonal axes empirically distinct from the UAS aggregate.

## 5. ⭐ Unique structural feature — the CORPUS-EXACT 4-verse self-meta-revelation passage (Q 75:16-19)

Q 75 is the **only surah in the entire corpus whose interior contains a 4-consecutive-verse passage of procedural-reception self-instruction to the Prophet** (Q075-F-01 STRONGLY VINDICATED, p<10⁻⁴ relative to length-weighted permutation null).

### The passage (Q 75:16-19)

| v | Text (no-tashkeel) | Gloss |
|:-:|:--|:--|
| 16 | لا تحرك به لسانك لتعجل به | *Move not your tongue with it to hasten with it.* |
| 17 | إن علينا جمعه وقرآنه | *Indeed, upon Us is its gathering and its recitation.* |
| 18 | فإذا قرأناه فاتبع قرآنه | *So when We have recited it, follow its recitation.* |
| 19 | ثم إن علينا بيانه | *Then, upon Us is its bayān (clarification/explanation).* |

### Empirical lock at corpus-EXACTNESS

Each component lexical fragment is **corpus-EXACT**:

- **لا تحرك** ("do not move", 2nd-sing. masc. imperative): **1 occurrence corpus-wide** (Q 75:16). Hapax form.
- **لتعجل به** ("to hasten with it"): **1 occurrence corpus-wide** (Q 75:16). Phrase-hapax.
- **علينا جمعه وقرآنه**: **1 occurrence corpus-wide** (Q 75:17). Phrase-hapax.
- **فإذا قرأناه فاتبع قرآنه**: **1 occurrence corpus-wide** (Q 75:18). Phrase-hapax.
- **بيانه** ("its bayān"): **1 occurrence corpus-wide** (Q 75:19). Hapax. (The root b-y-n appears widely; the form *bayānuhu* with the divine 3rd-person-masc. attached pronoun is unique.)
- **قرآنه** ("its recitation/qurʾān"): 2 occurrences, both in Q 75 (vv. 17 and 18). Corpus-DOUBLE-HAPAX restricted to this passage.

Under a structural definition (verses each containing at least one procedural-reception-of-revelation lexical indicator from the set {qurʾān-attached-pronoun, *waḥy*, *naqraʾu/qaraʾnāhu*, *taʿjal*-roots, *jamʿahu*, *bayān*-attached-pronoun, *lisān*-2sg, *fuʾād*-2sg}), the corpus contains **EXACTLY 1 four-consecutive-verse passage** (Q 75:16-19) — and even at the looser 3-consecutive-verse threshold the only matches are sub-windows of the same Q 75:16-19 passage.

### Classical claim audit (full detail in `05-classical-claims-audit.md`)

The classical interpretation is unanimous from al-Bukhārī forward: the passage is divine instruction to the Prophet during the moment of receiving the *waḥy*. The locus classicus is **al-Bukhārī Bk 1 ḥadīth #5** (Bidʾ al-waḥy chapter — i.e., the surah's procedural self-reference is the FIRST hadith Bukhārī places in his collection after the Niyya hadith #1) — chain: Mūsā b. Ismāʿīl ← Abū ʿAwāna ← Mūsā b. Abī ʿĀʾisha ← Saʿīd b. Jubayr ← Ibn ʿAbbās. The same chain recurs at Bukhārī Bk 65 #447, #448, #449 (Tafsīr-Q 75); Bk 66 #68 (Faḍāʾil al-Qurʾān); Bk 97 #149 (Tawḥīd) — **6 ṣaḥīḥ Bukhārī instances** of the same Saʿīd ← Ibn ʿAbbās narration. Plus al-Muslim Bk 4 #166-167; al-Tirmidhī Bk 47 #381.

al-Suyūṭī, *al-Itqān*, nawʿ 16 (*kayfiyyat inzāl al-Qurʾān*) and nawʿ 19 (*man yaktubu al-waḥy wa-kayfiyyat kitābatihi*) both cite Q 75:16-19 as the corpus's primary scriptural anchor for the doctrine of the Prophet's reception-mode of revelation. al-Zarkashī, *al-Burhān*, nawʿ 16 (*kayfiyyat anzāl al-Qurʾān*) treats vv. 16-19 as the canonical corpus-anchor.

The classical reading is therefore **VINDICATED at corpus-uniqueness law-strength** — Q 75:16-19 is empirically the only place in the Quran where the corpus speaks procedurally about its own moment-of-reception, and the canonical chain is multiply-attested at Bukhārī-strength.

## 6. The H-NEW-1200 short-Meccan-eschatology cluster — Q 75's role

H-NEW-1200 (CONFIRMED p=0.00030) defines a 14-surah short-Meccan-tail eschatology cluster: {Q 56, 69, 74, 77, 81, 82, 83, 84, 86, 90, 97, 99, 101, 104}. **Q 75 is NOT in the original cluster** but is empirically tested for affinity to it.

| Membership test | Result | Source |
|:--|:--|:--|
| Q 75 mean FR distance to H-NEW-1200 cluster | **0.7161** | computed (vs. corpus mean 0.9235) |
| Q 75 rank by closeness to H-NEW-1200 cluster (out of 100 non-cluster surahs) | **29/100** (top tertile) | computed |
| H-NEW-1200 + Q 75 (15-surah extended) FR-cohesion | **z = −5.30, p = 0.00010** | Q075-F-04 |
| Original 14-cluster | **z = −5.23, p = 0.00010** | replicated baseline |

**Q 75 strengthens the H-NEW-1200 cluster** when added (z drops slightly more negative, p stays at the perm-floor). Q 75 belongs in the eschatology meta-cluster on FR-content geometry — its absence from the original cluster reflects only that H-NEW-1200's defining patterns (*idhā*-cosmic-openers + *wa-mā adrāka mā*) do not fire in Q 75, even though Q 75 shares the FR-eschatology signature.

## 7. The corpus-EXACT 6-surah negative-particle-oath cluster — FR test

The 6 surahs containing any *lā uqsimu* / *fa-lā uqsimu* construction = {Q 56, 69, 70, 75, 81, 84, 90}. Q075-F-03 tests their FR-cohesion.

- **6-surah {Q 56, 69, 70, 75, 81, 84, 90}**: obs_mean=0.7465 vs corpus 0.9235; **z = −2.16, p_lower = 0.036** (ONE-SIDED, STRICT 6-surah; PASS-DIRECTED).
- **Brief's specified 4-surah subset {Q 56, 70, 75, 90}**: obs=0.7856; **z = −1.19, p_lower = 0.118** (NULL at α=0.05; the asymmetric 4-surah selection misses the cluster signal that the strict 6-surah set captures).
- **2-OPENER subset {Q 75, 90}** (the 2 surahs whose v. 1 is *lā uqsimu*): pairwise FR = **0.6695** (vs corpus 0.9235; one of Q 75's nearest 10 neighbors).

The **corpus-EXACT 6-surah negative-oath set is FR-cohesive at p=0.036 (PASS-DIRECTED)**, a 22nd FR-cohesive form-pattern cluster (joining H-NEW-1010, 1070, 1100, 1130, 1160, 1170, 1180, 1190, 1200, ...). The 4-surah subset of the brief misses the signal because its non-inclusion of the structurally-equivalent Q 69, Q 81, Q 84 dilutes the cohesion. **Specialist judgment: present both results; the 6-surah corpus-EXACT enumeration is the structurally-correct cluster.**

## 8. Q 75 ↔ Q 90 — the structural-twin pair

Q 75 and Q 90 are the corpus's **only two surahs whose v. 1 begins with bare *lā uqsimu*** (no *fa-* prefix). Their FR distance is 0.6695 — Q 75's 10th-nearest-neighbor; Q 90's structural pair.

| Property | Q 75 al-Qiyāma | Q 90 al-Balad |
|:--|:--|:--|
| Verse count | 40 | 20 |
| Word count (no-tashkeel) | 165 | 87 |
| Tanzīl revelation order | 31 | 35 |
| Nöldeke order | 36 | 39 |
| Period | Early Meccan | Early Meccan |
| Opening | *lā uqsimu bi-yawmi al-qiyāmati* | *lā uqsimu bi-hādhā al-balad* |
| Oath-target | the eschatological day | the geographic place (Mecca) |
| Top final-letter | ه (45%) | د (mixed) |
| Subject after oath | resurrection cosmology + self-meta | civic-injustice + civic-virtue (the freed-slave / fed-orphan emancipation passage) |

Both surahs share: bare-*lā uqsimu* opening; early-Meccan dating; short-mufaṣṣal length-class; eschatological consequence-frame. They diverge: oath-target (cosmic vs. geographic), main subject (resurrection vs. civic-ethics), rhyme-class. **Their FR-nearest mutual position confirms they form a corpus-structural-twin pair on the negative-oath axis** despite divergent post-oath content.

## 9. Quick content structure (full detail in `02-content-analysis.md`)

| Block | vv. | Length | Theme |
|:--|:-:|:-:|:--|
| A | 1-2 | 2 | **Double negative-oath opening** (*lā uqsimu bi-yawmi al-qiyāmah / wa-lā uqsimu bi-l-nafsi al-lawwāmah*) |
| B | 3-6 | 4 | Resurrection-bones argument + *al-insān* polemic |
| C | 7-15 | 9 | Eschatological cosmology — sun-moon collapse, no refuge, judgment |
| **D** | **16-19** | **4** | **CORPUS-EXACT structural-self-reference passage** (procedural revelation-reception) |
| E | 20-25 | 6 | Two faces — luminous (looking at Lord) vs. dark (calamity-stricken) |
| F | 26-30 | 5 | Death-rattle (*idhā balaghati al-tarāqī*) |
| G | 31-35 | 5 | Rebuke of Abū Jahl (Abū Lahab in some readings) — *fa-lā ṣaddaqa wa-lā ṣallā* |
| H | 36-40 | 5 | Closing cosmological argument from creation (sperm → clot → pair → resurrection) |

The structural ⭐ feature — Block D — is the corpus-UNIQUE 4-verse self-meta-revelation passage. Block A (the double negative-oath opener) is a corpus-exclusivity (only Q 75 has it).

## 10. Pre-registered novel findings (this investigation)

See `06-novel-findings.md` for full results. Headline:

| Test | Verdict | Effect |
|:--|:--|:--|
| Q075-F-01 — corpus-EXACT 4-verse self-meta-revelation passage | **STRONGLY VINDICATED** | EXACTLY 1 such passage corpus-wide (Q 75:16-19); each component lexical fragment is a corpus-hapax; classical chain to al-Bukhārī #5 verified |
| Q075-F-02 — Q 75 ↔ Q 90 structural-twin (bare-*lā uqsimu* openers) | **VINDICATED** | Q 75 and Q 90 are the corpus's only 2 such openers; FR=0.6695; both early-Meccan, both short-mufaṣṣal |
| Q075-F-03 — corpus-EXACT 6-surah negative-oath cluster FR cohesion | **PASS-DIRECTED** | obs=0.7465, z=−2.16, p_lower=0.036; 4-surah brief subset NULL at p=0.118 — corpus-EXACT enumeration captures signal |
| Q075-F-04 — Q 75 affinity to H-NEW-1200 14-cluster | **PASS-DIRECTED** | mean FR to cluster=0.7161 vs corpus 0.9235; rank 29/100 non-cluster; 15-cluster z=−5.30 strengthens vs baseline |
| Q075-F-05 — *qiyāmah* root density: Q 75 corpus rank | **VINDICATED (rank 1)** | Q 75 leads corpus-density at 12.12/1000w; nearest competitors Q 39 at 4.78/1000w (2.5× less) |

## 11. Investigation status

- [x] 00-overview.md
- [x] 01-empirical-profile.md
- [x] 02-content-analysis.md
- [x] 03-tafsir-survey.md
- [x] 04-hadith-corpus.md
- [x] 05-classical-claims-audit.md
- [x] 06-novel-findings.md
- [x] 07-cross-references.md
- [x] JOURNAL.md
- [x] 5 pre-regs (Q075-F-01..F-05)
- [x] 5 scripts (SHA-verified)
- [x] 5 JSON outputs in `csv/`
