---
id: h-new-95-run-1
date: 2026-04-17
agent: h-new-95-specialist
seed: 20260417
script: scripts/h_new_95_khawatim_extension.py
output: findings/phase-b-hypotheses/csv/h-new-95.json
findings: findings/phase-b-hypotheses/h-new-95-khawatim-extension.md
prereg: findings/phase-b-hypotheses/h-new-95-khawatim-extension-prereg.md
---

# H-NEW-95 Run Journal — 2026-04-17

## Dispatch

Task: H-NEW-95 — Khawātim al-Ḥashr extension, second-look. Hunt for ADDITIONAL echo verses beyond H-NEW-63's Q 62:1 finding. Pre-commit 5 cells (A–E) with Bonferroni k=5 / α_bon=0.01.

## Timeline

- Oriented on HANDOFF/01-WHAT-WE-KNOW.md and 04-DISCIPLINE.md.
- Read H-NEW-59 findings + pre-reg (canonical 9-name inventory, MW-5 protocol).
- Read H-NEW-63 findings (the 3-verse claim under a BROADER inventory — not the strict 9-name inventory).
- Noticed an inventory ambiguity between H-NEW-59 (strict 9-name EXCLUSIVE set) and H-NEW-63 (used names like al-Malik and al-ʿAzīz which are NOT exclusive). **Decision pre-registered:** primary analysis uses the strict 9-name inventory (the one anchored in H-NEW-59 Cell 2 as surah-exclusive); robustness arm reports broader-inventory results.
- Wrote pre-reg with `bonferroni_k: 5`, `alpha_bon: 0.01`, directions locked in YAML frontmatter BEFORE executing.
- Wrote script; replicated H-NEW-59's word-match-with-proclitic-prefix logic verbatim.

## Execution

- Ran script in ~3 minutes (dominated by 10k permutations + 99-name × 6,236-verse scan for Cell E).
- All five cells produced results.
- No mid-run changes to Bonferroni k or α (neither tightening nor loosening needed; observed p-values are all well below α_bon = 0.01).

## Results

- Cell A: 9 verses with ≥1 strict Khawātim name (6 of which are non-divine al-Salām).
- Cell B: 2 verses with ≥2 strict Khawātim names (Q 59:23 with 6; Q 59:24 with 3). Q 62:1 has only 1 under strict inventory.
- Cell C: K_obs(≥2) = 2 vs null mean 0.024; p = 0.00020 — **PASS**.
- Cell D: top-5 token concentration 81.25% vs null 47.1%; p = 0.00030 — **PASS**.
- Cell E: Q 59:22-24 is RANK 1 of 6,234 3-verse windows; F=19, null mean 1.57; p = 0.00016 — **PASS** at top 1%.
- Robustness: under H-NEW-63's broader 14-name inventory, Q 62:1 carries 4 echoed names (al-Malik, al-Quddūs, al-ʿAzīz, al-Ḥakīm) — ONE MORE than H-NEW-63 reported (H-NEW-63 missed al-Ḥakīm).

## Surprises

- **The strict 9-name inventory drops Q 62:1 out of the 2-name echo set.** H-NEW-63 was using a broader inventory implicitly. This is a rule-tuple sensitivity finding analogous to Ikhwān al-Ṣafāʾ 903-under-maghribī (per reference_rules_tuple_bidirectional.md) — but in the direction of demoting, then re-upgrading Q 62:1 to a 4-name echo under the broader inventory.
- **Q 62:1 gains a FOURTH echoed name (al-Ḥakīm)** that H-NEW-63 missed. This tightens the H-NEW-63 claim: Q 62:1 is the composite-quotation verse of BOTH Q 59:23 and Q 59:24's closing couplets.
- **Q 59:22-24 is RANK-1 in 3-verse 99-name density** — quantitatively the unique top window (F=19) with the next windows being overlapping Q 59 neighbors. This is stronger than the H-NEW-59 single-verse density claim.

## Pre-reg compliance check

- Direction locked in YAML before execution: YES (direction_A-B, direction_C-D, direction_E all in frontmatter).
- Bonferroni k declared in YAML: YES (k=5, α_bon=0.01).
- NULL cells published with same prominence as PASS: N/A (no NULL cells — 3/3 inferential cells passed).
- Seed documented: YES (20260417).
- Replication-ready (seed + script + deterministic algo): YES.

## No mid-run changes

No mid-run changes to Bonferroni k, α, or direction. The pre-reg specification was executed exactly as written.

## Write-through

- Pre-reg: findings/phase-b-hypotheses/h-new-95-khawatim-extension-prereg.md ✓
- Script: scripts/h_new_95_khawatim_extension.py ✓
- JSON: findings/phase-b-hypotheses/csv/h-new-95.json ✓
- Findings: findings/phase-b-hypotheses/h-new-95-khawatim-extension.md ✓
- Journal: journal/h-new-95-run-1.md (this file) ✓
