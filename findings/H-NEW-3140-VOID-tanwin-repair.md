# H-NEW-3140 — the tanwīn repair replication is VOID on its own gate

**Date:** 2026-08-11
**Verdict:** **VOID** — self-check S4 failed. By prereg §3, **no repaired number may be read as a
result.** Everything below is either a gate outcome or an explicitly non-authoritative observation.
**Prereg SHA** `3c896203…5779a0`, runtime-verified. Run directory retained; nothing deleted.

---

## 1. The void condition fired, and it fired on the prose arm

| self-check | result | detail |
|:--|:--|:--|
| S1 poetry bit-identical | **True** | — |
| S2 prose bit-identical | **True** | — |
| **S3 the Qurʾān must move** | **False** | see §3 |
| **S4 defective arm reproduces published values** | **False** | Qurʾān 0.22222 = 0.22222 ✓ · poetry 0.14286 = 0.14286 ✓ · **prose 0.24 vs 0.23963 ✗** |

Prereg §3: *"if S4 fails the run is void and no repaired number is reported."* It failed. The run is
void.

**The proximate cause is visible in the artefact: this harness runs its prose arm at n = 2,500.**
H-NEW-2730's published prose comparison does not use that n. So S4 is not detecting a rounding
wobble — **it is detecting that the harness is not running the same comparison as the finding it was
built to replicate.** The gate did exactly what a void condition is for.

## 2. What the run nevertheless shows internally — carrying NO verdict authority

Stated because deleting it would be worse than labelling it, and labelled because the run is void:

| statistic | defective | repaired | moved? |
|:--|--:|--:|:--|
| median d_min — **Qurʾān** | 0.22222 | 0.22222 | **no** |
| median d_min — poetry | 0.14286 | 0.14286 | no |
| median d_min — prose | 0.24 | 0.24 | no |
| **T1 H1a diff** | **0.07937** | **0.07937** | **no** |
| T3 H1b diff | 0.01778 | 0.01778 | no |
| T4 H3a diff | 0.07292 | 0.07372 | +0.00080 |
| T8 specificity — Qurʾān | 0.08571 | 0.08333 | −0.00238 |
| T8 modal share | 0.4075 | 0.3995 | −0.00800 |

**Restoring 6,643 tanwīn — 77.66% of the corpus's nunation — does not move the headline statistic at
all.** T1, the target that could have withdrawn the scansion family's sole survivor, is identical to
five decimal places.

All eight target labels came back `UNCHANGED` except T7, which is
`NUMBERS-CHANGED-CONCLUSION-UNCHANGED`. **Both locked predictions failed**: P1 (the Qurʾān's d_min
rises) and P2 (the H1a gap widens) are both `False`.

## 3. S3's failure is a defect in the self-check, not in §1's reading

Prereg §3 declared: *"S3 — the Qurʾān **must** move, or my DROP-set reading is wrong and §1 is
retracted."* S3 returned **False**. Taken literally, that retracts
[[AUDIT-TANWIN-DELETION-2690]] §1.

**It should not, and the reason is that S3 measures the wrong thing.**

The lane's own smoke test found **255 of the first 400 verses produce a different syllable string**
under the repair, with strings getting longer (Q 2:2 17→18, Q 2:5 22→23, Q 2:7 35→37). **The corpus
moves. The median does not.** S3 conflated *"the repair changes the text"* with *"the repair changes
this statistic"* — and those came apart.

So the honest reading of S3 = False is: **the d_min statistic is insensitive to the tanwīn defect**,
not that the defect is imaginary. The codepoint census in
[[AUDIT-TANWIN-DELETION-2690]] §1 is a direct count and stands on its own; it never depended on this
run.

**But S3 as written is a badly-posed check**, and the prereg cannot be edited. Recorded here instead:
a self-check that would retract a *count* on the basis of a *median* is testing a claim its subject
never made.

## 4. What this leaves

- **The tanwīn defect is real** — 6,643 of 8,554 tanwīn deleted before syllabification, verified by
  direct census, unaffected by this run.
- **The blind-control finding is real** — zero affected codepoints in all seven muʿallaqāt against
  6,643 in the Qurʾān, verified by direct census.
- **Whether the defect changes any published scansion conclusion is UNANSWERED.** This run was built
  to answer it and voided itself. The internal comparison suggests *no*, and that suggestion carries
  no authority.
- **A valid replication needs the harness to reproduce H-NEW-2730's prose arm first.** S4 is the
  right gate and it should stay; what needs fixing is the harness, not the gate.

Related: [[AUDIT-TANWIN-DELETION-2690]] · [[h-new-2690-quantitative-scansion]] ·
[[cross-finding-030-three-ways-a-control-fails]]
