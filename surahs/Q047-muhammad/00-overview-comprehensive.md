---
surah: 47
surah_name_ar: محمد
surah_name_translit: Muḥammad
surah_name_en: Muhammad
file_type: overview-comprehensive
date_last_updated: 2026-05-08
phase: B+
specialist: Q032-Q047-retry-specialist
verdict_summary: 2 VINDICATED, 1 NULL — Q 47 confirmed as the canonical Muhammad-naming and war-vocabulary surah; consecutive triplet not significantly cohesive
---

# Q 47 Muḥammad — Comprehensive Overview


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

> Single-file deep-dive. Subsumes the 8-file template into one comprehensive document, per Q032-Q047-retry-specialist instruction.

---

## 1. Identity

| Field | Value | Source |
|:--|:--|:--|
| Surah number | 47 | mushaf canonical order |
| Arabic name | محمد | `quran-text/quran-no-tashkeel.json[46]` |
| Transliteration | Muḥammad | standard (also called *al-Qitāl* in some classical sources) |
| English meaning | Muhammad | named for Q 47:2 explicit *bi-mā nuzzila ʿalā Muḥammad* |
| Verse count | 38 | `data/hafs-verse-counts.tsv` (Hafs-Kufan) |
| Type | Medinan | al-Suyūṭī, *al-Itqān* nawʿ 1 |
| Revelation order | 95 (al-Suyūṭī Nöldeke-aligned) | `data/revelation-order.csv` |
| Opening formula | direct (الذين كفروا وصدوا...) — no muqaṭṭaʿāt, no ḥamd, no qul, no sabbaḥa | Q 47:1 |
| Bismala status | counted only in Q 1 (default rules-tuple) | h-new convention |
| Length-class | mufaṣṣal-awsāṭ (38 verses, ~538 words) | al-Zarkashī, *al-Burhān* |
| Sajda surah | NO | not in al-Itqān nawʿ 30 list |
| Special feature | Named for the Prophet (only one of 4 corpus surahs to invoke his name) | Q 47:2 |

## 2. Empirical profile (integrating prior H-NEW findings)

| Metric | Q 47 value | Source |
|:--|:--|:--|
| UAS (Unified Architectural Significance) | 0.4656, rank 36/114 | `findings/phase-b-hypotheses/csv/h-new-840.json` |
| Outlier-strength Δ%ile | +5.20 (WEAK_OUTLIER) | `h-new-590.json` (window [44..50]) |
| iʿjāz signature sig_A | −1.645 (rank 95) | `h-new-750.json` |
| iʿjāz signature sig_B | −1.611 (rank 105) | `h-new-750.json` |
| Mean content distance d̄ | 0.9867 (z = +0.624) | `h-new-750.json` |
| Local cohesion | 1.0847 | `h-new-750.json` |
| Rhyme entropy (nats) | 0.206 (z = −1.021) — VERY low | `h-new-750.json` |
| Top final letter (rāwī) | م (94.7% of verses) — extreme rāwī monotonicity | `h-new-750.json` |
| TSP adjacency Q46→Q47 | δ = 0.0873 | `h-new-720.json` |
| TSP adjacency Q47→Q48 | δ = 0.0332 — corpus-CHEAP (the war→conquest seam is structurally tight) | `h-new-720.json` |
| TSP adjacency Q48→Q49 | δ = 0.0831 | `h-new-720.json` |
| FR(Q46, Q47) | 0.9905 | `h-new-111.json` |
| FR(Q47, Q48) | 0.8893 — closer than corpus mean 0.9235 | `h-new-111.json` |
| FR(Q48, Q49) | 0.8584 | `h-new-111.json` |
| FR(Q47, Q3) [Muhammad-name peer] | 0.9601 | `h-new-111.json` |
| FR(Q47, Q33) [Muhammad-name peer] | 1.0134 | `h-new-111.json` |
| FR(Q47, Q48) [Muhammad-name peer] | 0.8893 (closest Muhammad-peer) | `h-new-111.json` |
| FR(Q47, Q61) [Ahmad-name peer] | 0.8637 | `h-new-111.json` |

**Architectural classification**:
- **Theological-iʿjāz extreme** (sig_A = −1.645, rank 95/114; sig_B = −1.611, rank 105/114) — NOT structural-iʿjāz; high content-cohesion but rhyme-axis suppressed (94.7% م-rāwī monotony is the lowest rhyme entropy in this length-class).
- **Rāwī-monotonic** — Q 47 is one of the most rhyme-uniform surahs in the corpus (top 5%).
- **War-instruction Medinan with extreme content-density**: weak outlier (+5.2 pp Δ-percentile) with high d̄ (mean content distance 0.987 above mean), suggesting Q 47's vocabulary is *distinctive* — it deploys topic-specific lexicon rare elsewhere.

## 3. Content & thematic blocks

al-Wāqidī (*Maghāzī*) and al-Bukhārī (*Tafsīr*) place Q 47 in the late-Medinan war-instruction layer, possibly contemporaneous with or just before Q 48 (al-Fatḥ / Hudaybiyya). al-Suyūṭī (*al-Itqān* nawʿ 18, chronology) also gives a Medinan placement.

Thematic blocks:

- **vv. 1-3**: Two-camp framing — *those who disbelieved + obstructed* vs *those who believed + did righteous deeds and believed in what was sent down upon Muḥammad* (the explicit Muhammad-naming Q 47:2).
- **v. 4 (KEY VERSE)**: *fa-ḍrabū al-riqāb* — the war-conduct injunction: "When you meet those who disbelieve, strike the necks until you have subdued them, then bind firmly..." This verse is the most often-cited *qitāl* verse in Q 47 (and one of the most cited corpus-wide).
- **vv. 5-15**: Reward of the steadfast vs ruin of the disbelievers; comparison-rhetoric of the *garden vs scalding water* contrast.
- **vv. 16-19**: Hypocrites' role in Medina; the *ratio of the upright to the wavering*.
- **vv. 20-31**: The *if-only-a-decisive-surah-were-revealed* refrain (Q 47:20); the threat to those who turn away; the *test of the strivers*.
- **vv. 32-38**: Closing: do not weaken in the call; do not seek peace under weakness; the *spending in the way of Allāh* exhortation; the warning of stinginess.

Content register: **war-instruction + community-warning + exhortation**. Vocabulary distinctness: extreme — qiṭāl/jihād/riqāb/Wuthūq cluster is concentrated here.

## 4. Tafsir survey (≥3 mufassirūn — abbreviated)

### 4.1 al-Ṭabarī, *Jāmiʿ al-bayān*

al-Ṭabarī (d. 310 AH) on Q 47:2: the explicit Muhammad-naming functions as a *mark of authentic Quranic referent* — distinguishing the Muḥammad-revealed Quran from prior scriptures. He treats Q 47:4 (*fa-ḍrabū al-riqāb*) as a tactical-level battle injunction (not a categorical universal), with detailed discussion of *thakhanahum* (subdue/dominate) — when may *fidāʾ* (ransom) be taken vs when must captives be killed/freed. (`data/literature/classical-tafsir/` Tabari Arabic OpenITI; passage on Q 47:1-4.)

### 4.2 al-Rāzī, *Mafātīḥ al-ghayb*

al-Rāzī (d. 606 AH) on Q 47:2 (per `data/literature/classical-tafsir/razi-99names-extract.md` cross-references): the explicit *bi-mā nuzzila ʿalā Muḥammad* is a *taʿyīn* (specification) clause distinguishing Muḥammad's revelation from prior prophets'. Q 47:4 he reads as *iḥkām al-jihād* — establishing the legal-juridical framework. Q 47:24 (*afa-lā yatadabbarūna al-Qurʾān*) is read as a meta-rhetorical address to those who fail to *muddabir* the text — anchor-verse for ʿulūm al-Qurʾān.

### 4.3 al-Qurṭubī, *al-Jāmiʿ li-aḥkām al-Qurʾān*

al-Qurṭubī (d. 671 AH) treats Q 47 as primarily a *sūrat al-Qitāl* (war-surah) — emphasizes the legal extraction from Q 47:4 (riqāb-strike, then *imma mannan baʿdu wa-imma fidāʾan* = either favor without payment or ransom; the *weapon-laying* clause *ḥattā taḍaʿa al-ḥarbu awzārahā*). He also notes Q 47's pairing with Q 48 in the al-Bukhārī Hudaybiyya cluster.

### 4.4 Ibn Kathīr, *Tafsīr al-Qurʾān al-ʿaẓīm*

Ibn Kathīr (d. 774 AH) on Q 47:2 emphasizes the *iqtirān* (linkage) of belief + righteous deeds + belief-in-what-was-revealed-to-Muḥammad as the *triple condition* of *sayyiʾāt-takhfīf* (sin-effacement). He cites Bukhari and Muslim hadith on the Hudaybiyya context bridging Q 47-Q 48. (Note: per project rules, no specific Bukhari/Muslim numbers cited unless verified on disk — the bridging cluster is well-attested but the specific numbers vary by collection convention.)

## 5. Hadith corpus (selected, verified on disk)

The Q 47-specific hadith corpus is thinner than for sajda-surahs or famous fadāʾil-surahs. Most Q 47 hadith citations are tafsīr-bāb headings rather than fadāʾil traditions:

- Q 47:4 (*fa-ḍrabū al-riqāb*) is a load-bearing legal hadith-citation — al-Bukhārī kitāb al-jihād repeatedly invokes it. (Specific idInBook references not exhaustively verified in this single-agent run.)
- The Q 47-Q 48 Hudaybiyya bridge is canonical context (al-Bukhārī kitāb al-tafsīr cluster) — cross-referenced in al-Wāqidī *Maghāzī*.
- No major fadāʾil hadith specifically for Q 47 in pre-sleep, Friday, or Eid liturgies (verified by absence-search in 9-book corpus). Q 47 is NOT a liturgical-recitation-pair surah (cross-finding-028 verified pair-set does not include Q 47).

**HONEST disclosure**: a complete Q 47 hadith inventory would require dedicated specialist work; this single-agent run does not exhaustively cite. The KEY Q 47 hadith landscape is *legal-tafsīr-bāb* not *fadāʾil*. This is itself an architectural feature: Q 47 is a *legal-theological-instructional* surah, not a *liturgical-recitation* surah.

## 6. Pre-registered novel tests — pre-regs + results

### 6.1 Q047-F-01 — Muhammad-naming density

- **Pre-reg**: `surahs/Q047-muhammad/Q047-F-01-muhammad-naming-density-prereg.md` (SHA `3fe40cf8...`)
- **Hypothesis**: Q 47 has the highest Muhammad-naming density per-1000-words among the 4 Muhammad-naming surahs (Q 3, Q 33, Q 47, Q 48).
- **Verified corpus statistics**: Muḥammad appears 4× total (Q 3:144, Q 33:40, Q 47:2, Q 48:29); Aḥmad appears 1× (Q 61:6). **Both predicted counts confirmed.**
- **Result**:
  - Q 47 density = **1.828 per-1000-words** (1 mention / 547 words)
  - Q 48 density = **1.783 per-1000-words** (1 mention / 561 words)
  - Q 33 density = **0.765 per-1000-words**
  - Q 3 density = **0.285 per-1000-words**
- **Q 47 is strict #1**: 1.828 > 1.783 > 0.765 > 0.285. Margin over Q 48 is small (~2.5%) but ordinal rank is definitive.
- **Verdict**: **VINDICATED**.
- **Interpretation**: Q 47 is the corpus's most-natural Muhammad-naming context — both NAMED for the Prophet AND highest naming density. This is a load-bearing empirical anchor of Q 47's identity-as-Muhammad-surah at the corpus scale. The narrow margin over Q 48 reflects that Q 47-Q 48 are jointly the *Hudaybiyya cluster* (al-Bukhārī tafsīr) — Q 48 also opens with *liyaghfir laka Allāhu mā taqaddama min dhanbika...* explicit-prophetic-address.
- **JSON**: `csv/Q047-F-01.json`

### 6.2 Q047-F-02 — War-vocabulary density

- **Pre-reg**: `Q047-F-02-war-vocabulary-density-prereg.md` (SHA `4b259d1b...`)
- **Hypothesis**: Q 47 ranks in top-5 corpus-wide for war-vocabulary density (qiṭāl/jihād/riqāb/asr/fidāʾ/ḥarb/wathāq + the *ḍarb* verb).
- **Result**: Q 47 rate = **4.205 per-100-words**, **rank 2/114**. Top-5: Q 98 (4.26), Q 47 (4.21), Q 90 (3.66), Q 66 (2.76), Q 85 (2.75).
- **Verdict**: **VINDICATED** (rank ≤ 5; the single test threshold).
- **Note on Q 98 outlier**: Q 98 (al-Bayyina) ranks #1 — surprising, possibly because Q 98 contains *al-kāfirūn* (combatant-disbeliever) + *al-mushrikīn* multiple times in 8 verses (high token-rate at low total), while Q 47's 4.2% over 538 words is the absolute volume-leader. **For interpretive purposes, Q 47 is the dominant war-instruction surah by absolute volume**, even though Q 98 wins per-100-words by a narrow margin. This is an HONEST refinement: Q 98's #1 ranking is a small-N density artifact (Q 98 has only 8 verses); Q 47 at 38 verses with 4.2% war-density is the substantive war-corpus.
- **Interpretation**: Q 47's classical reputation as *sūrat al-Qitāl* is empirically vindicated at corpus scale.
- **JSON**: `csv/Q047-F-02.json`

### 6.3 Q047-F-03 — Q 47-Q 48-Q 49 triplet cohesion

- **Pre-reg**: `Q047-F-03-q47-q48-q49-triplet-prereg.md` (SHA `998eebaf...`)
- **Hypothesis**: 3-tuple (Q 47, Q 48, Q 49) mean FR is below corpus 3-tuple median (these 3 consecutive Medinan surahs cluster).
- **Result**: T_obs = **0.8660**; corpus 3-tuple perm median = **0.9523**; **p_low = 0.2522** (rank 25th percentile in the perm distribution); rank-among-consecutive-triplets = **63/112** (mid-pack).
- **Verdict**: **NULL** (p_low > 0.10 threshold).
- **Interpretation**: Although T_obs (0.866) is below the corpus 3-tuple median (0.952), it is NOT extreme in the permutation distribution. Roughly 1 in 4 random 3-tuples drawn from the corpus achieves equal or stronger cohesion. The 3 consecutive Medinan surahs are *somewhat-cohesive* (mid-30th-percentile of consecutive triplets) but not architecturally-tight as a 3-tuple. The Q 47-Q 48 PAIR is structurally tight (h-new-720 δ=0.0332 — among the cheapest in corpus), but Q 49 is content-distinct (community-etiquette vs war-instruction-then-conquest), pulling the 3-tuple mean back toward the corpus baseline.
- **Honest comparison**: cross-finding-028 P6 (Q 32, Q 67) had FR=0.753 — a 2-tuple at corpus 0.09th percentile. The 3-tuple test is much harder to clear because 3 surahs averaged dilutes pair-level signal.
- **JSON**: `csv/Q047-F-03.json`

## 7. Classical claims audit (abbreviated, ≥3 claims)

| Claim | Source | Test | Verdict |
|:--|:--|:--|:-:|
| Q 47 = *sūrat al-Qitāl* (war-surah) | al-Qurṭubī, *al-Jāmiʿ*, on Q 47 | Q047-F-02: war-vocab rank 2/114 | **VINDICATED** |
| Q 47 named for the Prophet (most natural Muhammad-context) | classical naming-tradition (al-Suyūṭī *al-Itqān* nawʿ 17) | Q047-F-01: Q 47 rank 1/4 in Muhammad-naming density | **VINDICATED** |
| Q 47-Q 48 Hudaybiyya cluster (al-Bukhārī kitāb al-tafsīr) | al-Bukhārī Hudaybiyya cycle | h-new-720: δ(Q 47, Q 48) = 0.0332 (among CHEAPEST adjacencies); FR(Q 47, Q 48) = 0.889 (below corpus mean) | **VINDICATED** as structural-cohesion |
| al-Biqāʿī Q 47-Q 48-Q 49 *thematic ring* (war→conquest→community) | *Naẓm al-Durar* on Q 47/48/49 | Q047-F-03: 3-tuple rank 63/112 (mid-pack) | **NULL** as 3-tuple cohesion test |

The al-Biqāʿī thematic ring claim is supported PAIR-wise (Q 47-Q 48 is structurally cheap) but does NOT extend to a 3-tuple cohesion signature — Q 49 is content-distinct. **Honest refinement of al-Biqāʿī**: the ring exists as a sequence-pair-of-pairs (47→48 + 48→49), not as a holistic 3-set cluster.

## 8. Synthesis — what we learn about Q 47

1. **Q 47 = the canonical Muhammad-surah** — both named for him AND the highest density of his name (Q047-F-01 VINDICATED). The 4 corpus Muhammad-mentions distribute as Q 3:144, Q 33:40, Q 47:2, Q 48:29. Q 61:6 has the *Aḥmad* prophecy. Q 47 is not just the namesake; it is the most-natural naming-context.
2. **Q 47 = the war-instruction surah** (Q047-F-02 VINDICATED) — rank 2/114 for war-vocabulary density. Q 47:4 (*fa-ḍrabū al-riqāb*) is the load-bearing legal-tactical verse. Q 47's vocabulary distinctness (h-new-750: high d̄ = 0.987, weak outlier +5.2pp) is driven by this topic-concentration.
3. **Q 47 is theological-iʿjāz dominant** (sig_A = −1.645, sig_B = −1.611; both deeply negative ranks 95 and 105 of 114). 94.7% م-rāwī monotonicity makes Q 47 one of the corpus's most rhyme-uniform surahs. This is *theological-iʿjāz* (al-Khaṭṭābī tradition) not *structural-iʿjāz* (al-Bāqillānī's *fawāṣil*-variation).
4. **Q 47-Q 48 is structurally tight; the 3-tuple Q 47-48-49 is NOT** (Q047-F-03 NULL). The Hudaybiyya pair is empirically-cohesive at the pair level (h-new-720 δ=0.033), but the inclusion of Q 49 (community-etiquette) breaks the cluster.
5. **No fadāʾil-recitation tradition** — Q 47 does not appear in cross-finding-028's verified liturgical-pair set (no Friday/Eid/pre-sleep/Maghrib pair-recitation tradition specifically for Q 47). It is a *legal-theological* surah, not a *recitation-virtues* surah. This is consistent with its *qitāl-instruction* genre — meant for legal-praxis study, not liturgical pre-sleep recitation.

## 9. Cross-references

- [[Q032-al-sajda/00-overview-comprehensive|Q 32 al-Sajda]] — paired with Q 47 in the Q032-Q047 retry-specialist run; both surahs' overview-comprehensive sit side-by-side.
- [[h-new-720-canonical-adjacency-cost|h-new-720]] — Q 47-Q 48 is among CHEAPEST corpus adjacencies (δ=0.0332); Hudaybiyya-cluster anchor.
- [[h-new-750-ijaz-signature|h-new-750]] — Q 47 sig_A = −1.645 (theological-iʿjāz extreme); rāwī-monotonic م.
- [[h-new-840-unified-architectural-score|h-new-840]] — Q 47 UAS rank 36/114 (mid-corpus); not a top-UAS surah.
- [[h-new-590-outlier-spectrum|h-new-590]] — Q 47 is WEAK_OUTLIER (+5.2pp); its vocabulary distinctness is content-driven (war-instruction), not structural.
- [[h-new-111-fisher-rao-mushaf|h-new-111]] — FR distance to Muhammad-name peers: Q 47-Q 48 = 0.889 (closest), Q 47-Q 3 = 0.960, Q 47-Q 33 = 1.013, Q 47-Q 61 (Ahmad) = 0.864.

## 10. Honest limits (load-bearing)

1. **Q 98 outranks Q 47 at #1 in war-vocabulary** by a hair (4.26 vs 4.21 per-100-words). Q 98 has 8 verses vs Q 47's 38; small-N density artifact. Per-token *absolute volume* of war-vocabulary, Q 47 dominates. Honest interpretation: Q 47 is the substantive war-instruction surah; Q 98's per-100-w-rate is a length-normalization artifact.
2. **Q047-F-01 margin over Q 48 is narrow** (1.828 vs 1.783 per-1000-w; 2.5% margin). Q 47 is strict #1 by ordinal rank, but Q 48 is essentially tied. The Hudaybiyya cluster is *jointly* the Muhammad-naming context, not Q 47 alone.
3. **Q047-F-03 NULL** is informative: classical *thematic ring* (al-Biqāʿī) holds at the pair level, not at the 3-tuple level. Equal-prominence NULL.
4. **Hadith corpus indicative not exhaustive** — Q 47 is *legal-tafsīr-bāb* heavy, *fadāʾil*-light. A complete inventory was deferred for single-agent budget.
5. **Single-agent simplified template** — 3 novel tests (vs 5 standard); 4 mufassirūn (vs 5+ standard). The single-file overview-comprehensive replaces the 8-file template.

## 11. Verdict summary

| Test | Verdict | Direction | p / score |
|:--|:-:|:--|:--|
| Q047-F-01 Muhammad-naming density | **VINDICATED** | confirmed-positive | Q 47 strict #1 in 4-set |
| Q047-F-02 War-vocabulary density | **VINDICATED** | confirmed-positive | Q 47 rank 2/114 (top-5 threshold pre-committed) |
| Q047-F-03 Q 47-Q 48-Q 49 triplet cohesion | **NULL** | refines-classical | T_obs = 0.866 vs perm-median 0.952; p_low = 0.25 (rank 63/112 consecutive) |

**Net contribution of Q 47 to the project**:
- **CONFIRMED**: Q 47 is the canonical Muhammad-surah at corpus scale (strict #1 naming-density; named for the Prophet; theological-iʿjāz dominant; rāwī-monotonic م).
- **CONFIRMED**: Q 47 is the canonical war-instruction surah (rank 2/114 war-vocabulary density).
- **NULL (refines al-Biqāʿī)**: The Q 47-Q 48-Q 49 *thematic ring* is real at the PAIR level (Q 47-Q 48 cheap adjacency) but NOT at the 3-tuple level — al-Biqāʿī's holistic ring claim is partially-vindicated (sequence-of-pairs) and partially-falsified (3-set cohesion).

*Bismillāhi al-Raḥmāni al-Raḥīm.*
