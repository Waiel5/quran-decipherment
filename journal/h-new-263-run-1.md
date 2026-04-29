# H-NEW-263 Run 1

Date: 2026-04-18

Target files:

- `scripts/h_new_263_divine_name_surah_network.py`
- `findings/phase-b-hypotheses/h-new-263-divine-name-surah-network-prereg.md`
- `findings/phase-b-hypotheses/h-new-263-divine-name-surah-network.md`
- `findings/phase-b-hypotheses/csv/h-new-263.json`
- `journal/h-new-263-run-1.md`

## What was done

1. Built a tight 2-cell prereg around the repo's existing `divine-names-by-verse.csv` data:
   - Cell A: weighted projection concentration `H = Σ W²`
   - Cell B: conservative hub-existence test on `W >= 2` using null-standardized `Z_max`
2. Implemented the executable script with:
   - fixed-margin bipartite double-edge-swap null
   - MW-5 synthetic positive control
   - JSON export
3. Hit a runtime blocker on the first `1000`-accepted-swap configuration.
4. Amended the prereg and script to `500` accepted swaps per permutation before the clean successful run.
5. Reconciled the findings prose to the final JSON from the successful `500`-swap run.

## Final JSON numbers

- Verdict: `PASS-STRUCTURE-NO-HUB`
- Cell A:
  - `H_sum_w_sq = 17282`
  - `H_null_mean = 16614.34`
  - `H_null_sd = 244.25077112943657`
  - `H_p_upper = 0.006644518272425249`
- Cell B:
  - `z_max_obs = 2.197241772833916`
  - `p_exist = 0.04318936877076412`
  - top candidate = Q 27 with `p_adj_fwer = 0.04318936877076412`
- MW-5:
  - structure `p = 0.008264462809917356`
  - hub `p = 0.008264462809917356`
  - overall `pass = true`

## Deliverables on disk

- `scripts/h_new_263_divine_name_surah_network.py`
- `findings/phase-b-hypotheses/h-new-263-divine-name-surah-network-prereg.md`
- `findings/phase-b-hypotheses/h-new-263-divine-name-surah-network.md`
- `findings/phase-b-hypotheses/csv/h-new-263.json`
- `journal/h-new-263-run-1.md`
