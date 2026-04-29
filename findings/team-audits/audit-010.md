---
audit_id: audit-010
finding_id: H-NEW-18
finding_title: al-Kirmānī mutashābih directionality (longer variant → denser host-surah) — REFUTED
audited_by: skeptical-auditor
date: 2026-04-13
parent: null (classical-scholar claim #2)
status: PASSED (refutation)
---

# Audit memo — H-NEW-18 (al-Kirmānī directionality — REFUTED as pre-registered)

## Verdict: PASSED (as refutation, in the pre-registered direction)

Clean refutation. The pre-registered al-Kirmānī literal thesis ("longer mutashābih variant = denser host surah") is refuted with 32/73 pairs (43.8%) going the predicted way (binomial p = 0.879). The author reports three tests with k=3 Bonferroni pre-committed, no post-hoc operationalization flips, and — critically — explicitly labels the anti-signal as *not claimable* rather than promoting it to a finding. This is exactly the discipline the protocol asks for.

I accept the refutation as routed to §3.

One item requires revision before the finding is fully archived: the anti-signal (mean-delta z = −2.43, raw two-sided p = 0.015) is worth investigating, not because it supports an inverted al-Kirmānī (as the "sympathetic reading" notes, that would be post-hoc), but because if real, it tells us something about where the Quran places elaborations — and that's a separable hypothesis that deserves its own pre-registration.

## What the refutation establishes

- **Literal al-Kirmānī longer-denser thesis: REFUTED.** 41/73 pairs run opposite (p=0.879 on the predicted direction). This is clean — no operational ambiguity, no forking paths, adequate (though modest) power at n=73.
- **Classical-scholar's claim-#2 as operationalized: falsified.** The specific operationalization ("shared-root density of host surah as the 'thematic saturation' proxy") is one of several defensible measures; it is the one pre-registered. Refutation on this operationalization does not refute al-Kirmānī's *spirit* (intentional directionality of elaboration), but it does refute this team's operationalization of it.
- **Protocol hygiene**: three tests pre-registered, Bonferroni applied, no metric swaps after observation. Contrast with many potential failure modes (post-hoc metric switching, |R| threshold tuning, same-surah inclusion). The finding would have been easy to inflate; it was not inflated.

## The anti-signal (needs follow-up, not claimable here)

Mean-delta z = −2.43 is one-sided notable (raw p ≈ 0.0075 one-sided; two-sided ≈ 0.015). Under Bonferroni-k=3 at α=0.05 family-wise → per-test α=0.0167. Two-sided it *just* clears. One-sided in the unregistered direction it clears comfortably.

The author's discipline in not claiming this is correct. But for the integrator and for downstream research planning, the anti-signal suggests a genuine pattern worth testing as a separate pre-registered hypothesis:

**H-NEW-18B (candidate, unregistered):** *Longer mutashābih variants tend to sit in host-surahs that use the shared roots less densely elsewhere — i.e., the "full statement" appears where the surah needs elaboration because those roots are otherwise absent.*

This is functionally an inverted al-Kirmānī (the sympathetic reading). It should not be claimed from the current data. But the integrator may wish to route this to classical-scholar for a fresh pre-registration with: (a) an independent operationalization (not shared-root density — perhaps theme-vector distance, or tafsir-annotated theme saturation), (b) a different pair sample (e.g. split the 73 pairs in half; use one half for pre-reg, the other for test), and (c) an explicit prediction sign.

**Flag to classical-scholar**: worth considering whether al-Kirmānī's *literal* text actually predicts "longer = denser" or "longer = sparser." Classical-scholar's own framing of claim #2 was stated as the former; the refutation here is of that framing. If al-Kirmānī's actual doctrine is better rendered as the sparser-host version, the refutation still stands *as a refutation of the claim as operationalized by classical-scholar for this test*, but it also tells us the operationalization was wrong rather than al-Kirmānī was wrong. This is an intelligence layer question: a re-reading of al-Kirmānī's actual text (not the secondary literature summary) would help. I flag it but don't require it for archiving — the refutation as pre-registered stands.

## Alternative-explanation audit

1. **Operationalization error** (shared-root density may be the wrong proxy for "thematic saturation"). This is the most consequential alternative. If "thematic saturation" is measured by tafsir-annotated theme density or by a semantic-embedding centrality, the sign might flip. This does not rescue the pre-registered claim — refutation as registered stands — but it opens the door to a re-operationalized H-NEW-18B.
2. **Power** — n=73 is modest. The observed p=0.879 is so far from significance that low power is not an issue for the refutation direction; a hypothesized effect would need to be enormous to be missed at this n.
3. **Catalog selection bias**: mutashābih catalog is itself curated. Author correctly flags this; the curation bias would affect both directions roughly symmetrically, so it doesn't rescue the Kirmānī prediction.
4. **|R|≥2 filter bias**: may bias toward short shared-root sets where density differences are noisy. Partially concerning for the anti-signal, less so for the refutation (null would also be noisy). Not blocking.
5. **Same-surah exclusion**: defensible (host-identity makes test undefined). Not a confound.

## Classical cross-reference — flag for classical-scholar

Al-Kirmānī's *al-Burhān fī mutashābih al-Qurʾān* discusses pair directionality but the specific doctrine "longer goes in denser" is **classical-scholar's gloss on al-Kirmānī**, not al-Kirmānī's own phrase. What al-Kirmānī actually argues case-by-case (e.g., on Q 2:58 vs Q 7:161, the famous *wa-dkhulū al-bāb sujjadan* pair) varies — sometimes the longer variant *adds detail the other lacks*, sometimes it *repeats for rhetorical density*. The operational translation to "longer = denser host" is one reading; other readings exist. The refutation as a test of this specific operational reading is clean; the refutation as a test of al-Kirmānī's actual doctrine is weaker.

**Recommended write-up sentence**: "al-Kirmānī's doctrine as operationalized via host-surah shared-root density is refuted. The result does not refute al-Kirmānī himself, whose framing admits other operationalizations; it does refute this team's pre-registered quantitative rendering of his claim."

This is not a blocker. It is a nuance for the synthesis.

## Family-size note

Within-finding Bonferroni k=3 (binomial, frac-yes perm, mean-delta perm) — applied correctly. The pre-registered direction test (binomial p=0.879) is trivially non-significant; no correction concern there.

The anti-signal (mean-delta z=−2.43, two-sided p≈0.015) is the only test that even approaches significance; under k=3 it's at α_bon=0.0167, just clears two-sided. If this were a pre-registered finding, I would require external replication before accepting; since it is explicitly *not* claimed, the Bonferroni treatment is moot.

Across-finding family: n findings submitted so far ≈ 9. If the anti-signal were claimed, α = 0.05/9 ≈ 0.0056 — two-sided p=0.015 does not clear. Confirms that the author's decision not to claim was correct.

## What would change the verdict

- **Refutation remains robust**: no realistic re-analysis rescues the literal "longer = denser" prediction at n=73 with obs = 43.8% yes.
- **Anti-signal would become claimable only** if it survives a fresh pre-registration with independent operationalization and new Bonferroni accounting. Not the current finding's task.

## Cross-finding overlap flag for integrator

1. **R-005 candidate** (§3 addition): "Classical claim #2 al-Kirmānī directionality (literal operationalization) — REFUTED, n=73, 43.8% yes, binomial p=0.879. Does not refute al-Kirmānī *tout court*; refutes the pre-registered operational rendering."

2. **AXES-WATCHLIST**: this joins the list of classical-scholar claims that fail literal-operational test but may survive reformulation. Companion to R-001 al-Suyūṭī (where corpus-wide ibtidāʾ/intihāʾ failed; rhetorical-affordance reading may hold for specific surahs). Pattern: classical doctrines describe *tendencies and exemplars*, not *universal statistical laws*. This is itself a meta-finding (M-5 candidate? tentative, needs more instances).

3. **M-pattern relevance**: this finding does not reinforce M-1, M-2, M-3, or M-4. It weakly supports a potential M-5 tentative candidate — "classical doctrines survive as rhetorical-affordance claims but fail as universal-law operationalizations." Instances: R-001 Suyūṭī ibtidāʾ/intihāʾ, R-005 al-Kirmānī literal directionality. Need 1–2 more before naming. Not logging M-5 formally yet, just flagging for watchlist.

4. **Classical-scholar routing**: classical-scholar should be asked (i) does al-Kirmānī's actual text support "longer = denser" or "longer = sparser" or "varies case-by-case"?, (ii) is there a sharper operationalization worth a H-NEW-18B pre-registration?, and (iii) should the refutation be framed as "al-Kirmānī refuted" or "operationalization refuted"? The framing choice affects §3 wording.

## Lineage

Parent: null. Sibling to other classical-scholar-claim tests (al-Suyūṭī, al-Rāzī, Ibn Abī l-Iṣbaʿ, etc.).
Child candidate: H-NEW-18B (inverted reading) — not pre-registered; deferred to classical-scholar.
