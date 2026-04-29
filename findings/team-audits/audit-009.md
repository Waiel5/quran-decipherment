---
audit_id: audit-009
finding_id: H-NEW-11
finding_title: Prophet-vocabulary suppression is pan-prophetic (not driven by any single prophet); length correlates but does not explain
audited_by: skeptical-auditor
date: 2026-04-13
parent: prophet-vocabulary-overlap-matrix (phase-c pre-team finding)
status: PASSED
---

# Audit memo — H-NEW-11 (Pan-prophetic vocabulary suppression)

## Verdict: PASSED

This is the cleanest audit target so far. The finding was framed as a deepening sub-hypothesis ("which prophets drive the parent signal?"), ran the only two tests that could refute the drivers-claim (leave-one-out and length-artifact), and reported both results honestly in the pre-registered direction. The result has the shape good sub-hypothesis work should have: it **refutes** the natural suspicion that a few prophets drive the aggregate signal and delivers the stronger conclusion (pan-prophetic specialization) at no interpretive cost.

I would not block this. Minor observations below are not blockers; they are requests for the writeup and registrations I'd like for the integrator's synthesis.

## Why this passes where others did not

1. **The parent signal's status is already established.** The prior phase-c finding (aggregate mean-Jaccard 0.3353 below the 95% null 0.3484–0.3876) is not under re-test here. H-NEW-11 asks a different, focused question about drivers. This avoids the garden-of-forking-paths trap of re-probing the headline.
2. **Leave-one-out is the right test.** If any single prophet drove the signal, dropping them would eliminate it. All 8 drops preserve z ≤ −2.35; dropping Abraham gives z = −3.80 (*strengthens* the signal slightly; Abraham is the most-template-central prophet — counterintuitive but consistent with his centrality in Itqān nawʿ 65).
3. **Length-artifact diagnostic is appropriately interpreted.** Spearman ρ = +0.79 is reported honestly as "length correlates strongly," and the author does not overstate: they do not claim length is irrelevant. The key disconfirmation is Moses — the largest pericope, not the most typical. Spearman strong + individual outlier = "length contributes, does not determine."
4. **The binomial-style pan-prophetic conclusion is cleanly stated.** "No prophet, when removed, eliminates the below-null outcome" is a genuine refutation of the drivers-sub-hypothesis. The finding sharpens, not weakens, the parent.

## Small observations (non-blocking)

### 1. Moses-as-specialized: worth pinning down
The write-up describes Moses as "lexically specialized." A quick follow-up would make this claim rigorous: compute **Moses-specific roots** (roots appearing in Moses pericopes at >10× their base rate elsewhere) and report the list. If the list is dominated by rod/magician/tribe/pharaoh/manna/quail vocabulary, the specialization claim is concretely instantiated. This is a write-up enhancement, not a re-test. I'd love to see it in the synthesis document when the integrator builds the prophet-pericope section.

### 2. Confidence in the Spearman point estimate
Spearman ρ = +0.79 on n=8 has wide bootstrap CIs — 95% bootstrap interval is typically ±0.3 for that n. The claim "length correlates strongly" should be hedged with "on n=8, CI is wide; directionally positive is the robust statement, the exact magnitude is not." Minor writeup fix.

### 3. Abraham-strongest-contributor is worth pre-registering as its own sub-claim
Abraham's drop gives the largest |obs − null| = −0.0407. Interpreting Abraham as "the template prophet" is consistent with classical *khalīl Allāh* framing and Itqān nawʿ 65's centering of Abraham in the qiṣaṣ system. But this claim — "Abraham is the maximally-template-central prophet" — was not pre-registered as a hypothesis. It emerges from the LOO rank. Flag as a candidate for a separate registered test if we want to claim it. Otherwise mark as "post-hoc observation from LOO, not a registered sub-claim."

## Robustness check I'd like to see, but not blocking

**Pericope-clustering-parameter sensitivity** (re-running LOO under gap=5 pad=5 and gap=2 pad=0). The author notes this was done for the parent finding without reversing direction; I'd accept that as sufficient precedent. Not re-requesting.

## Alternative-explanation audit

1. **Length artifact** — partially explanatory (Spearman +0.79), ruled out as full explanation by Moses outlier. Handled.
2. **Single-prophet driver** — directly refuted by LOO. Handled.
3. **Pericope-clustering-definition artifact** — addressed by parent-finding robustness; no need to re-run.
4. **Annotation artifact (QAC root-layer errors)** — unaddressed but unlikely to produce a false pan-prophetic below-null signal. QAC root annotation is one of the cleanest layers in the corpus. Accepting.
5. **Selection of the 8 prophets** — these are the 8 most-mentioned. Lower-frequency prophets (Shuʿayb, Hūd, Ṣāliḥ, Idrīs, Dhū al-Kifl) are excluded. Extending to n=13 would be a separate study; would likely show the same pattern since these also have distinct sub-vocabularies (Shuʿayb/Madyan measures, Hūd/ʿĀd wind). Not blocking.

## Classical cross-reference

Author cites al-Suyūṭī *Itqān* nawʿ 65 and the *taksīr al-qiṣṣa al-wāḥida ʿalā wujūh* framing. Accurate. Worth adding: **al-Qurṭubī** *al-Jāmiʿ li-aḥkām al-Qurʾān* in the introduction addresses the same question (why prophet stories are retold with different vocabulary across surahs) and answers with *ikhtilāf li-tamām al-fāʾida* — variation for completed benefit. Al-Rāzī in *Mafātīḥ al-Ghayb* (commentary on Q11:25 ff, the Noah opening) explicitly notes that each retelling highlights different facets of the same event. The operational result from H-NEW-11 corroborates this classical doctrine quantitatively.

Worth noting what the finding is NOT: it is not a discovery of a pattern classical scholars missed. It is an operational quantification of a pattern classical scholars named (*taksīr al-qiṣṣa*, *ikhtilāf li-tamām al-fāʾida*, *badaʾiʿ al-qaṣaṣ*). The contribution category is "operationalization," not "novel discovery." Frame accordingly.

## Family-size note

H-NEW-11 is a **deepening test**, not a new primary hypothesis. The parent finding (phase-c prophet-vocabulary-overlap-matrix) already passed its null; H-NEW-11 refutes a sub-claim about drivers. Family-wise correction: this is a child-finding, correction should be against the number of sub-claims tested against the parent (k=2: drivers-hypothesis, length-artifact-hypothesis). Both are within α = 0.01 comfortably.

## What would change the verdict

Nothing I can see. The data strongly refutes the single-prophet-driver hypothesis, the length-artifact is bounded by the Moses outlier, and the write-up is honest.

## Cross-finding overlap flag for integrator

1. **Parent-lineage**: explicit child of phase-c prophet-vocabulary-overlap-matrix. Integrator should tag the lineage chain clearly: phase-c finding (parent, passed) → H-NEW-11 (child, sub-hypothesis refuted, deepens parent). The phase-c finding itself is the confirmation; H-NEW-11 is the sensitivity analysis that rules out the driver-artifact alternative.

2. **M-1 relevance (surah-outlier registry)**: Moses is flagged here as a lexically-specialized outlier in the prophet axis. This is an additional M-1 entry **at the prophet level rather than surah level** — worth recording in the registry as "Moses pericope across surahs shows highest lexical mass but 4th in typicality — specialized not central." This is a pericope-outlier note, parallel to but distinct from surah-outlier notes.

3. **M-4 relevance (typological subgenre signatures, tentative)**: if we open an M-4 registry for surah-subtype signatures (dialogic from H-NEW-14, etc.), "prophetic narrative" is another subtype. Not ready to cross-link yet. But: the Quran's prophetic-narrative subgenre has a now-measured property — *specialization-preserving lexical scaffolding across the 8-prophet matrix*. Future M-4 graduation would include this.

4. **Contributes to the emerging positive picture**: combined with the pre-team phase-c parent, this is the team's first audit result where the direction of test survives honest scrutiny AND the refutation of the sub-hypothesis is itself an informative positive ("pan-prophetic, not driver-concentrated"). Worth flagging to integrator: this should count as a **PASSED** leg of the findings tally, distinct from the refutations in §3. Running total should now read "1 novel confirmation (deepening-type, child of pre-team parent) + 4 §3 refutations + wait queue."

**Note on classification**: this is not an independent novel-finding confirmation in the sense H-NEW-5 or H-NEW-8 would be if they pass revision. It is a sub-hypothesis confirmation of a parent finding. Integrator should decide how to count this in the tally. My recommendation: record as "deepening PASSED" under the phase-c parent in §1 (accepted findings), not as a new §1 primary entry — the parent is the accepted finding, H-NEW-11 is the robustness strengthening.

## Lineage

Parent: phase-c prophet-vocabulary-overlap-matrix (pre-team, passed).
Children of this audit: none yet; Abraham-centrality claim (section 3 above) would be a candidate child hypothesis if classical-scholar wants to pre-register it.
