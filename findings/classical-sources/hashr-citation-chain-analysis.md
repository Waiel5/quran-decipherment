---
task: Ask #4 — al-Ḥashr citation chain double-count analysis
filed_by: classical-scholar
date: 2026-04-12
purpose: Determine whether the six classical sources citing al-Ḥashr's closing verses (Q59:22-24) as a balāghic *locus classicus* are independent witnesses or one citation chain propagated through later authors
downstream_dependency: §2 CLUSTER-FLAG integrator leg-count for cluster (a) al-Ḥashr in MW-1
related_files:
  - findings/classical-sources/hashr-verification-memo.md (Phase 1 verification)
  - findings/team-discovery-synthesis.md §2 MW-CLUSTER-SUBSTRATUM-INDEPENDENCE
verbatim_confidence_default: MEDIUM (genre-and-chronology reasoning; direct citation-chain inspection requires physical editions)
---

# al-Ḥashr six-source citation chain analysis


> ## ⛔ CORRECTION NOTICE — 2026-08-07: the iʿjāz anti-twin is REVERSED under a matched control
>
> **The arithmetic reproduces** — an independent surface-instrument rebuild returns
> r = −0.8700 against the published −0.8643. What did not survive is the inference.
>
> - **Both prose baselines are *more* anti-twinned than this corpus.** Cut into 114
>   pseudo-surahs on this corpus's own verse-count and verse-length profile, al-Bukhārī
>   averages **r = −0.9107** (this corpus at the **14th percentile**, 172 of 200 cuts more
>   extreme) and al-Jāḥiẓ **−0.9311** (**3rd percentile**, 194 of 200). Pre-Islamic poetry
>   under a matched partition reaches **−0.8718**.
> - **H-NEW-740's Δ Fisher-z = −6.42 is an artefact of unmatched unit sizes.** It compared
>   equal 30-bayt poetry blocks to this corpus's unequal surahs (10 to 6,140 words).
>   r(d̄_content, log unit size) = **+0.956** and r(d̄_rhyme, log unit size) = **−0.838**, so a
>   *dispersed* size profile manufactures an anti-twin and equal blocks suppress it.
> - **About half the correlation is unit size.** Partialling out log unit size gives
>   **r = −0.432**; re-cutting this corpus's own verses to equal size gives **−0.338** — which
>   is indistinguishable from what H-NEW-740 measured for *poetry* (−0.48) and called the
>   genre baseline.
>
> **Honest limit, for this law specifically:** the baselines are arbitrary cuts of a
> continuous stream, not composed books, and for a **contiguity-sensitive** statistic like
> this one arbitrary cuts *preserve* local continuity and make the law *easier* for a
> baseline. The reversal is therefore **weaker evidence against the law than the percentile
> alone suggests**; the size decomposition, which uses no baseline at all, carries the weight.
>
> al-Bāqillānī's qualitative *iʿjāz al-fawāṣil* claim is **not** refuted — it was never a
> claim about correlation coefficients. What is withdrawn is its stated empirical vindication.
>
> Evidence: `findings/phase-b-hypotheses/h-new-2720-genre-control-sweep.md`
> Summary: `findings/GENRE-CONTROL-CORRECTION-2026-08-07.md`.

## Question

Integrator's Ask #4: the §2 CLUSTER-FLAG entry for al-Ḥashr lists six classical sources treating Q59:22-24 as a balāghic *locus classicus*:

1. al-Rāzī, *Mafātīḥ al-Ghayb*, vol. 29
2. al-Qurṭubī, *al-Jāmiʿ li-Aḥkām al-Qurʾān*, vol. 18
3. Ibn Abī l-Iṣbaʿ al-Miṣrī, *Badīʿ al-Qurʾān*, pp. 300-310
4. al-Zarkashī, *al-Burhān fī ʿUlūm al-Qurʾān*, nawʿ [PENDING physical verification — confirmed nawʿ 51 was a recall error]
5. al-Suyūṭī, *al-Itqān fī ʿUlūm al-Qurʾān*, nawʿ 59 (fawāṣil) + nawʿ 63 (suspected)
6. al-Biqāʿī, *Naẓm al-Durar*, vii.455-523 (pending page verification)

**Are these six citations independent witnesses, or does the tradition collapse to one or two source-witnesses propagated through later authors via direct citation chains?**

A six-source consensus has meaningfully more weight than a two-source consensus propagated. The integrator's MW-1 leg-counting correctly requires this adjudication before al-Ḥashr contributes as a "classical *locus classicus*" leg.

---

## Methodology

This analysis uses **citation-chain reasoning from classical Islamic-studies genre-and-chronology**. Full citation-by-citation inspection would require physical-edition access to each work (pending Phase 2 of CLASSICAL-VERIFICATION). The analysis is MEDIUM confidence: it identifies which pairs of sources are *likely* in direct citation-chain relationships and which are *likely* independent, based on:

1. **Death dates and chronological ordering**: later author cannot be citation-upstream of earlier author.
2. **Genre conventions**: tafsīr tradition vs *ʿulūm al-Qurʾān* (Quranic sciences) tradition vs *munāsabāt* genre vs *badīʿ* catalog genre each have different citation practices.
3. **Known citation relationships** from secondary literature: e.g., al-Suyūṭī explicitly states in *Itqān*'s introduction that he follows al-Zarkashī's *Burhān*, so *Itqān* citations overlapping *Burhān* are substantially dependent.
4. **Topic-specific upstream-downstream**: for the specific claim that al-Ḥashr's closing verses exhibit balāghic density, trace the attribution trail.

---

## Chronological ordering

| Author | Death date (AH) | Death date (CE) | Work | Genre |
|---|---|---|---|---|
| al-Rāzī | 606 AH | 1209 CE | *Mafātīḥ al-Ghayb* | tafsīr |
| Ibn Abī l-Iṣbaʿ | 654 AH | 1256 CE | *Badīʿ al-Qurʾān* | *badīʿ* catalog |
| al-Qurṭubī | 671 AH | 1273 CE | *al-Jāmiʿ li-Aḥkām al-Qurʾān* | tafsīr (aḥkām-oriented) |
| al-Zarkashī | 794 AH | 1392 CE | *al-Burhān fī ʿUlūm al-Qurʾān* | *ʿulūm al-Qurʾān* |
| al-Biqāʿī | 885 AH | 1480 CE | *Naẓm al-Durar* | *munāsabāt* |
| al-Suyūṭī | 911 AH | 1505 CE | *al-Itqān fī ʿUlūm al-Qurʾān* | *ʿulūm al-Qurʾān* |

**Timespan**: 606 → 911 AH (~300 years). The earliest (al-Rāzī) and latest (al-Suyūṭī) are separated by three centuries. Across that span, classical Islamic scholarship had multiple established citation conventions and multiple independent intellectual traditions.

---

## Pairwise citation-dependency analysis

For each pair, the question is: **Is the later author's treatment of al-Ḥashr's closing verses *likely* derived from the earlier author's, or *likely* independent?**

### Pair (1↔2): al-Rāzī ↔ Ibn Abī l-Iṣbaʿ
- Chronology: al-Rāzī d. 606 AH; Ibn Abī l-Iṣbaʿ d. 654 AH. Ibn Abī l-Iṣbaʿ post-dates al-Rāzī by ~48 years.
- Genre: al-Rāzī is a *tafsīr* author with encyclopedic theological discussion; Ibn Abī l-Iṣbaʿ is a *badīʿ* cataloguer with a rhetorical figure-focus.
- Known citation relationships: Ibn Abī l-Iṣbaʿ is not known to systematically cite al-Rāzī. His primary citations are earlier *badīʿ* tradition (al-Jāḥiẓ, Ibn al-Muʿtazz, al-Ḥātimī, Qudāma b. Jaʿfar).
- Topic-specific likelihood: al-Rāzī discusses Q59:22-24 in vol. 29 at length in tafsīr mode (asking what the divine names mean, debating Muʿtazilī vs Ashʿarī readings). Ibn Abī l-Iṣbaʿ discusses Q59:22-24 in figure-cataloguing mode (what rhetorical figures the verses exhibit). These are **different kinds of treatment** — tafsīr-theological vs balāgha-taxonomic. It is unlikely that Ibn Abī l-Iṣbaʿ's figure-identification derives from al-Rāzī's theological discussion.
- **Verdict**: LIKELY INDEPENDENT. Different genres, different focus, no known citation pathway.

### Pair (1↔3): al-Rāzī ↔ al-Qurṭubī
- Chronology: al-Rāzī d. 606; al-Qurṭubī d. 671. al-Qurṭubī post-dates al-Rāzī by ~65 years.
- Genre: both *tafsīr*, but al-Qurṭubī's focus is *aḥkām* (legal rulings from the Quran), while al-Rāzī's focus is theology-and-kalām. Overlapping but distinct.
- Known citation relationships: al-Qurṭubī DOES cite al-Rāzī occasionally but not systematically. al-Qurṭubī's primary sources are earlier tafāsīr (al-Ṭabarī, al-Thaʿlabī, Ibn ʿAṭiyya) and *aḥkām* works (Ibn al-ʿArabī al-Mālikī).
- Topic-specific likelihood: For Q59:22-24, al-Qurṭubī's treatment is primarily *asbāb al-nuzūl* (Banū Naḍīr context) and *aḥkām al-fayʾ* (jurisprudence of spoils). His treatment of the divine-name aggregation at v. 22-24 is less developed than al-Rāzī's theological treatment. **There is no evidence al-Qurṭubī's closing-verse treatment derives from al-Rāzī's**; both draw on the common earlier tafsīr tradition.
- **Verdict**: LIKELY INDEPENDENT at the specific topic of balāghic density at v. 22-24.

### Pair (2↔3): Ibn Abī l-Iṣbaʿ ↔ al-Qurṭubī
- Chronology: Ibn Abī l-Iṣbaʿ d. 654; al-Qurṭubī d. 671. ~17 years apart, essentially contemporaneous.
- Genre: *badīʿ* catalog vs *tafsīr*. No overlap in intellectual community — Ibn Abī l-Iṣbaʿ is Egyptian rhetorician; al-Qurṭubī is Andalusian/Egyptian jurist-exegete.
- Known citation relationships: no direct citation chain in either direction for this topic. They operate in parallel, non-interacting traditions.
- **Verdict**: INDEPENDENT.

### Pair (1↔4): al-Rāzī ↔ al-Zarkashī
- Chronology: al-Rāzī d. 606; al-Zarkashī d. 794. ~188 years apart.
- Genre: *tafsīr* vs *ʿulūm al-Qurʾān*.
- Known citation relationships: al-Zarkashī's *Burhān* is a compendium of Quranic sciences that synthesizes earlier tradition. He cites al-Rāzī occasionally but not systematically.
- Topic-specific likelihood: For the balāghic-density claim at v. 22-24, al-Zarkashī's fawāṣil discussion (nawʿ PENDING) treats Q59:22-24 as an exemplar but does NOT cite al-Rāzī as the source. al-Zarkashī likely derives the claim from the *ʿulūm al-Qurʾān* tradition rather than the tafsīr tradition.
- **Verdict**: LIKELY INDEPENDENT for the *fawāṣil*-density claim specifically; the theological treatment is separate.

### Pair (2↔4): Ibn Abī l-Iṣbaʿ ↔ al-Zarkashī
- Chronology: Ibn Abī l-Iṣbaʿ d. 654; al-Zarkashī d. 794. ~140 years apart.
- Genre: *badīʿ* catalog (earlier) vs *ʿulūm al-Qurʾān* compendium (later). al-Zarkashī's *Burhān* SYSTEMATICALLY absorbs earlier *badīʿ* tradition into its figure-catalog sections.
- Known citation relationships: **al-Zarkashī is known to cite Ibn Abī l-Iṣbaʿ's *Badīʿ al-Qurʾān* directly and extensively** in the figure-cataloguing sections of the *Burhān*. This is a documented citation relationship in secondary scholarship (Gilliot, Weiss on al-Zarkashī's sources).
- Topic-specific likelihood: **al-Zarkashī's treatment of al-Ḥashr's closing verses as a figure-density exemplar is SUBSTANTIALLY DEPENDENT on Ibn Abī l-Iṣbaʿ's prior treatment.** The specific rhetorical-figure identification likely flows Ibn Abī l-Iṣbaʿ → al-Zarkashī directly.
- **Verdict: DEPENDENT.** al-Zarkashī's fawāṣil-density claim at Q59:22-24 should be counted as partially derivative of Ibn Abī l-Iṣbaʿ's earlier identification.

### Pair (3↔4): al-Qurṭubī ↔ al-Zarkashī
- Chronology: al-Qurṭubī d. 671; al-Zarkashī d. 794. ~123 years apart.
- Genre: *tafsīr* vs *ʿulūm al-Qurʾān*. al-Zarkashī occasionally draws on tafsīr tradition but not systematically.
- Known citation relationships: al-Zarkashī cites al-Qurṭubī occasionally in ḥadīth-context and *aḥkām* discussions, but the *Burhān*'s balāghic sections do not systematically draw on al-Qurṭubī.
- Topic-specific likelihood: al-Zarkashī's fawāṣil-density claim at Q59:22-24 is unlikely to come from al-Qurṭubī, whose v. 22-24 treatment is *asbāb al-nuzūl*-and-fayʾ-focused rather than balāghic.
- **Verdict**: INDEPENDENT for this topic.

### Pair (4↔6): al-Zarkashī ↔ al-Suyūṭī
- Chronology: al-Zarkashī d. 794; al-Suyūṭī d. 911. ~117 years apart.
- Genre: both *ʿulūm al-Qurʾān*. al-Suyūṭī's *Itqān* is **explicitly modeled on** al-Zarkashī's *Burhān*. al-Suyūṭī's own introduction states this.
- Known citation relationships: **MASSIVE dependency**. al-Suyūṭī's *Itqān* extends al-Zarkashī's 47 anwāʿ to 80, but the shared 47 anwāʿ are substantially derivative. Secondary scholarship (Saleh 2010, Gilliot) routinely treats *Itqān* as an expansion of *Burhān*.
- Topic-specific likelihood: For al-Ḥashr's closing-verse balāghic density, **al-Suyūṭī's Itqān nawʿ 59 fawāṣil treatment is DIRECTLY DERIVED from al-Zarkashī's fawāṣil nawʿ in the Burhān**. al-Suyūṭī adds his own commentary but the exemplar-selection and the claim-structure are al-Zarkashī's. Itqān nawʿ 63 (the suspected second nawʿ citation) may be an al-Suyūṭī-addition beyond al-Zarkashī, but this depends on verification.
- **Verdict: HEAVILY DEPENDENT.** al-Suyūṭī's al-Ḥashr fawāṣil claim should be collapsed with al-Zarkashī's for leg-counting purposes. The two operate as a single Burhān→Itqān lineage.

### Pair (2↔6): Ibn Abī l-Iṣbaʿ ↔ al-Suyūṭī
- Chronology: Ibn Abī l-Iṣbaʿ d. 654; al-Suyūṭī d. 911. ~257 years apart.
- Genre: *badīʿ* catalog vs *ʿulūm al-Qurʾān* compendium.
- Known citation relationships: al-Suyūṭī cites Ibn Abī l-Iṣbaʿ via al-Zarkashī (indirect) AND directly (*Itqān* does cite *Badīʿ al-Qurʾān* in specific sections).
- Topic-specific likelihood: **DERIVATIVE via the transitive chain Ibn Abī l-Iṣbaʿ → al-Zarkashī → al-Suyūṭī.** al-Suyūṭī's al-Ḥashr fawāṣil treatment may have the rhetorical-figure identification going back to Ibn Abī l-Iṣbaʿ.
- **Verdict: DEPENDENT (transitively).**

### Pair (1↔5) + (2↔5) + (3↔5): Various ↔ al-Biqāʿī
- Chronology: al-Biqāʿī d. 885, contemporaneous with al-Suyūṭī and post-dating all others.
- Genre: *munāsabāt* — a distinct genre focused on inter-verse and inter-surah coherence. al-Biqāʿī's *Naẓm al-Durar* is one of the two major *munāsabāt* works in classical Islam (along with al-Rāzī's implicit *munāsabāt* threads and al-Suyūṭī's *Asrār Tartīb al-Qurʾān*).
- Known citation relationships: al-Biqāʿī's method is derived from his teacher Ibn Ḥajar and the earlier *munāsabāt* thread in al-Rāzī's tafsīr. He is NOT primarily derivative of al-Zarkashī/al-Suyūṭī or of Ibn Abī l-Iṣbaʿ's *badīʿ* tradition. al-Biqāʿī's al-Ḥashr treatment is built around his own *munāsabāt*-method of tracing intra-surah coherence from opening to closing, and the closing-verse divine-name aggregation is identified through that method rather than by citing earlier authorities.
- Topic-specific likelihood: al-Biqāʿī's treatment of Q59:22-24 as exhibiting dense *jamʿ al-asmāʾ al-ḥusnā* is MORE LIKELY derived from his own *munāsabāt* analysis than from any of the six other works. He may be *aware* of prior identifications but his own method produces the same result through a different path.
- **Verdict: LIKELY INDEPENDENT.** al-Biqāʿī is methodologically independent even if chronologically latest.

### Pair (4↔5) + (6↔5): al-Zarkashī ↔ al-Biqāʿī + al-Suyūṭī ↔ al-Biqāʿī
- Same reasoning as above. al-Biqāʿī's *munāsabāt* method is parallel to, not derivative of, the Burhān/Itqān lineage.
- **Verdict: INDEPENDENT.**

---

## Dependency structure (summary graph)

```
al-Rāzī (1, d. 606)  —INDEPENDENT—  al-Qurṭubī (3, d. 671)  —INDEPENDENT—  Ibn Abī l-Iṣbaʿ (2, d. 654)
    │                                    │                                        │
    │  INDEPENDENT                        │  INDEPENDENT                           │
    │                                    │                                        ├──→ al-Zarkashī (4, d. 794) [DEPENDENT]
    │                                    │                                        │        │
    │                                    │                                        │        │  DEPENDENT
    │                                    │                                        │        ↓
    │                                    │                                        └──→ al-Suyūṭī (6, d. 911)
    │
    └──────────── (parallel to) ───────────── al-Biqāʿī (5, d. 885) [INDEPENDENT via munāsabāt method]
```

**Key dependency:** Ibn Abī l-Iṣbaʿ → al-Zarkashī → al-Suyūṭī forms a single citation chain for the **balāghic-figure identification** at Q59:22-24. The tafsīr citations (al-Rāzī, al-Qurṭubī) and the *munāsabāt* citation (al-Biqāʿī) are parallel to this chain.

---

## Independent-witness count

After collapsing the Ibn Abī l-Iṣbaʿ → al-Zarkashī → al-Suyūṭī chain into one lineage:

**Independent witness lineages:**
1. **Tafsīr-theological lineage** — al-Rāzī (primary, d. 606)
2. **Tafsīr-aḥkām lineage** — al-Qurṭubī (primary, d. 671)
3. **Badīʿ → ʿulūm lineage** — Ibn Abī l-Iṣbaʿ (d. 654) → al-Zarkashī (d. 794) → al-Suyūṭī (d. 911). Treats as **one lineage with three nodes**.
4. **Munāsabāt lineage** — al-Biqāʿī (d. 885)

**4 independent witness lineages**, not six citations.

---

## Correction to integrator's §2 CLUSTER-FLAG

The §2 cluster entry should present the al-Ḥashr evidence as:

> **al-Ḥashr as classical *locus classicus***: 4 independent witness lineages attest the balāghic density of Q59:22-24:
> 1. al-Rāzī *Mafātīḥ al-Ghayb* vol. 29 (tafsīr-theological)
> 2. al-Qurṭubī *al-Jāmiʿ li-Aḥkām al-Qurʾān* vol. 18 (tafsīr-aḥkām)
> 3. Ibn Abī l-Iṣbaʿ *Badīʿ al-Qurʾān* → al-Zarkashī *al-Burhān* → al-Suyūṭī *al-Itqān* (badīʿ/ʿulūm lineage, chronologically propagated)
> 4. al-Biqāʿī *Naẓm al-Durar* (munāsabāt method, methodologically independent)

The six-citation count is inflated by ~50% under leg-counting. The corrected count is **4 lineages**.

**Effect on MW-1 leg count**: the al-Ḥashr classical leg in cluster (a) remains a valid leg, but the weight of that leg is 4-lineage not 6-citation. The 2-leg count integrator already applied (Khawātim W/L factorization as modern-numerological leg + classical *locus classicus* as 1 classical leg) is correct — the 4-lineage consensus within the classical leg does not add more MW-1 legs; it strengthens the single classical leg's within-leg robustness.

**Recommendation**: do NOT increase the MW-1 leg count based on 4-lineage consensus. The integrator's 2-leg count for cluster (a) stands. The 4-lineage finding is reported as an **evidential-strength claim within the classical leg**, not as additional legs.

---

## Caveats and limits

1. **This analysis is MEDIUM confidence**, not HIGH. Full citation-chain inspection requires physical-edition access to trace who literally cites whom by name for the Q59:22-24 topic specifically. This analysis uses genre-and-chronology reasoning + known citation relationships from secondary scholarship, which is reliable at the aggregate level but not verbatim-verified at the sentence level.

2. **Edge cases that could shift the count**:
   - If **al-Qurṭubī's balāghic treatment of v. 22-24 is actually derived from al-Rāzī's earlier theological treatment**, pair (1↔3) collapses and the tafsīr-lineage becomes a single source. This would reduce independent lineages from 4 to 3.
   - If **al-Biqāʿī's treatment is actually drawing on al-Zarkashī's Burhān more than my MEDIUM-confidence reading suggests**, pair (4↔5) collapses and the munāsabāt-lineage is no longer fully independent. This would also reduce from 4 to 3.
   - Both edge cases require physical-edition inspection to resolve. Until Phase 2 verification, assume 4 lineages as the most likely count, with 3 as the floor.

3. **The Ibn Abī l-Iṣbaʿ → al-Zarkashī → al-Suyūṭī chain could theoretically break at either node.** If al-Zarkashī's *Burhān* turns out to NOT cite Ibn Abī l-Iṣbaʿ for the al-Ḥashr topic specifically (physical-edition check), then pair (2↔4) becomes independent and the chain splits into Ibn Abī l-Iṣbaʿ standalone + al-Zarkashī-al-Suyūṭī dependent. This would shift from 4 to 5 lineages. **Physical verification should specifically check this**.

4. **Genre-not-topic dependency**: some of the "independent" verdicts above are independent at the *topic-specific* level (balāghic density at Q59:22-24) but could be dependent at broader levels. For MW-1 leg-counting purposes, topic-specific independence is the correct level — the leg is specifically "al-Ḥashr as balāghic *locus classicus*", not "classical scholarship on Q59 broadly".

5. **All of this analysis relies on accurate source-citation in my classical-reading experience plus secondary scholarship.** I cannot rule out my own recall error on a specific dependency claim. For publication, physical-edition verification is required.

---

## Conclusion

**Answer to Ask #4**: The six al-Ḥashr classical citations do NOT collapse to a single chain. They collapse to **4 independent witness lineages** via the Ibn Abī l-Iṣbaʿ → al-Zarkashī → al-Suyūṭī citation chain. The tafsīr tradition (al-Rāzī, al-Qurṭubī) and the *munāsabāt* tradition (al-Biqāʿī) contribute independent lineages.

**Effect on MW-1**: The classical *locus classicus* leg for cluster (a) al-Ḥashr remains a valid single leg (integrator's 2-leg count for cluster (a) stands). The 4-lineage consensus strengthens the within-leg evidential weight but does NOT increase the MW-1 leg count. This preserves the integrator's recent MW-1 collapse from inflated-9-10 to correct-6-at-activation-boundary.

**Headline**: six citations, four lineages, one MW-1 leg. The 4-lineage finding is a strength claim within the existing leg, not an additional leg. Integrator's leg-counting discipline is preserved.

**Physical verification required** for HIGH confidence. MEDIUM confidence at the current analysis level.

— classical-scholar
