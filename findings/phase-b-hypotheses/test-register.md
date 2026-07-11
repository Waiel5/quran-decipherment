---
title: Prospective Statistical Test Register
started: 2026-07-11
scope: Tests registered on or after 2026-07-11
---

# Prospective Statistical Test Register

This register begins prospectively on 2026-07-11. It does **not** retroactively
certify older tests. A registered test must enter Git before its analysis script or
result. The preregistration commit, data hashes, comparison family, correction, and
result commit remain visible here.

| ID | Family | Preregistration | Prereg commit | Tests in family | Decision threshold | Data freeze | Status | Result |
|---|---|---|---|---:|---:|---|---|---|
| H-NEW-2540 | MORPH-2026-07-11-A | `prereg-h-new-2540-form-v-valency.md` | initial `333e5fa0c`; stricter pre-run amendment pending | 4 | Bonferroni α = 0.0125; strict gate = 0.005 | QAC v0.4 `a1d129…`; EQTB `a303c2…` | AMENDED BEFORE RUN; not run | pending |

## Registration rules

1. Commit the preregistration and register entry before creating or running the
   analysis script.
2. Embed the full preregistration SHA-256 in the script and fail if it differs.
3. Write each run to a new immutable directory; never overwrite an earlier run.
4. Store the command, Git commit, input hashes, script hash, Python version, seed,
   and result JSON with the finding.
5. A changed random seed is Monte Carlo stability, not independent replication.
6. Report every registered NULL or reversal with the same prominence as a PASS.
