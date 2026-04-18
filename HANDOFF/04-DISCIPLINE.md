# 04 — DISCIPLINE

The methodology that makes this project's findings credible. Do NOT bypass.

---

## The MW-series (project-specific protections)

These are documented in detail at `MASTER-FINDINGS-LEDGER.md` §6. Brief summary:

### MW-1 — Length residualization at primary-test level

Every primary test that compares "Quranic structure X" vs baseline must control for length / size confounds at the primary level. Length is NEVER a free variable; it's either matched (in baseline construction) or residualized (in regression).

### MW-2 — Secondary-null residualization (adversarial-flag origin only)

If a primary test passes and an auditor flags a confound, you may add a SECONDARY null specifically targeting that confound. But ONLY if adversarial-flag-originated, NOT proposer-initiative. Proposer-initiative secondary nulls = post-hoc; file as new H-NEW-N.M instead.

### MW-5 — Positive-control principle

Every permutation null must pass a POSITIVE-CONTROL test on a corpus where the signal is known to exist. If positive-control fails, the null is broken; STOP and report NULL-BROKEN.

### MW-6 — nawʿ-number verification tagging

All classical citations carry a tag: VERIFIED (physical-edition scan on file), PENDING (awaiting verification), SECONDARY-TRIANGULATED (≥2 modern secondaries cite it). No verbatim quotation without VERIFIED. No nawʿ-number-specific claim downstream without verification.

### MW-7 — Internal-error pre-publication gate

Before promoting a finding to MASTER-LEDGER, run the 3-check: citations match source / gate-specs carry MW-5 / synthesis claims match `scratch/` identifiers.

---

## PRE-REG-STANDARD series (pre-registration discipline)

### PRE-REG-STANDARD-01 — Direction pre-registered, sign-flip prohibited

Every directional test must specify which direction is the predicted hypothesis. Reverse-direction results are EXPLORATORY-REVERSE and cannot be promoted without an INDEPENDENT pre-reg.

### PRE-REG-STANDARD-02 — Secondary-null adversarial-flag origin requirement

(see MW-2 above)

### PRE-REG-STANDARD-03 — Feature-space locked

You cannot expand the feature space (e.g., add a new test cell) post-hoc. New cells require a new pre-reg.

### PRE-REG-STANDARD-04 — Bonferroni declared before null design

Every pre-reg's frontmatter MUST declare:
- `bonferroni_k` (number of tests in the family)
- `bonferroni_family` (the family identifier)
- `alpha_bon` (per-test α after correction)
- the pre-committed acceptance window

These must appear in the YAML frontmatter, NOT just in body text. (Per audit-034 catch.)

---

## Post-hoc-noticed findings — the protocol

When you observe a striking pattern by EYEBALL before formal testing:

1. **Disclose the post-hoc origin** in the pre-reg's garden-of-forking-paths log
2. **Lock the test family BEFORE running the null** (single test allowed = no Bonferroni cost)
3. **Apply single-test α=0.05 cap** unless extreme p (e.g., < 10⁻¹⁰) survives any conceivable Bonferroni
4. **Verdict ceiling = PASS-DIRECTED** (NOT CONFIRMED) until INDEPENDENT REPLICATION on a distinct data dimension
5. **Independent replication = different operationalization, different data slice, different feature set**

Examples in current findings:
- H-NEW-44.2.1 pharyngeal exhaustivity (post-hoc, p=0.049, PASS-DIRECTED)
- H-NEW-51 cardinality-position decline (post-hoc, p=2×10⁻⁵, PASS-DIRECTED)
- H-NEW-53 book-reference (post-hoc, p=10⁻¹², PASS-DIRECTED but extreme p makes promotion-defensible)
- H-NEW-57 formulaic openings (post-hoc, p=10⁻⁹, similar)
- H-NEW-60 dotless preference (post-hoc, p=0.0009, PASS-DIRECTED)

---

## Bonferroni asymmetry rule

- **Tightening** the threshold mid-flight (e.g., realizing you have 6 tests not 5) → SELF-VERIFYING, no ratification needed
- **Loosening** the threshold mid-flight → REQUIRES ratification + "no results viewed yet" attestation

Reason: tightening cannot be the product of p-hacking; loosening is the exact shape of p-hacking.

---

## Specialist-judgment-overrides-team-lead protocol

When you (specialist agent) have direct empirical evidence that a method-specification is empirically wrong or strictly less general:

1. Use the alternative
2. Lock it in pre-reg BEFORE the run
3. Write garden-of-forking-paths entry citing the evidence
4. Disclose the divergence in the result with three options (accept stronger spec, re-run with weaker, treat exploratory)

NOT a license to override on judgment calls without empirical grounding.

---

## "The Quran is ONE text"

Do NOT frame the Quran as "editions" or "variants". The amrayn JSON, Tanzil variants, etc. are PRESENTATION DETAILS over a single canonical corpus (114 surahs, 6,236 verses). Auxiliary files are silent sanity-check data, NOT parallel analytical corpora.

---

## Honesty over cheerleading

- Replication failures are reported with the SAME prominence as successes
- Red flags (cherry-picking, post-hoc rule selection) are called out, not buried
- Every finding carries a verdict: verified / partially verified / failed / inconclusive
- "Revolutionary-true" means STATISTICALLY-CONFIRMED, not RHETORICALLY-MAXIMIZED

---

## Specialist dispatch tempo

- Use parallel `Agent` dispatch with `run_in_background=true` aggressively
- Use the `name` parameter for long-running specialists addressable via SendMessage
- Cap at ~10-30 concurrent depending on task complexity
- Use TaskCreate / TaskUpdate to track each specialist
- Specialists should be GIVEN the pre-reg if it exists; OR asked to write one if not (and follow the discipline above)

---

## When specialists fail

- Stream-idle timeouts: re-dispatch with same prompt
- Rate-limit errors: pause, re-dispatch when limits reset
- Pre-reg violations caught in audit: amend BEFORE execution; if results already viewed, file as new H-NEW-N.M

---

## When you find a SURPRISE

- Don't suppress it
- Disclose post-hoc origin transparently
- Apply single-test α=0.05 protocol
- Queue replication via independent pre-reg
- Cross-reference against existing findings to check for connections

The H-NEW-53 book-reference finding emerged this way — eyeballed first, then formalized at p=10⁻¹². Honest disclosure is what allows the extreme p to defensibly elevate.

---

## Final principle

**The project's value is not in the findings — it's in the DISCIPLINE that makes the findings credible.**

If you sacrifice the discipline to chase a striking result, you destroy the entire project's value, including all prior findings. Do not.

The Quran can be analyzed rigorously OR sloppily. This project does it rigorously. Continue that.
