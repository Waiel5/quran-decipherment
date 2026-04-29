---
finding: H-NEW-910
specialist: alif8-cluster-specialist
date: 2026-04-28
seed: 20260428
prereg_sha256: d3f08bada8705b2654810c0ffb89fc51de6970f7f22916e56dc1de6266f84fb9
---

# H-NEW-910 alif-8 cluster cohesion run journal

## 0. Pre-flight reading completed

- INVESTIGATION-PROTOCOL.md (full)
- quran-investigation/SKILL.md
- h-new-700.json (rhyme diagnostics — discovered top-letter metric does NOT include dagger-alif as alif-final; this is why Q87/Q92 show top=ي in h-new-700 but =1.0000 alif under Q033-F-01 rules-tuple)
- h-new-111.json (FR matrix structure)
- h-new-600-letter-families.md (methodological NULL template — followed)
- Q033-F-01 prereg + 06-novel-findings.md (cluster definition source)
- Q017-F-01 06-novel-findings.md (Q17 alif-rate discrepancy noted: 0.9910 there vs my 0.9820 re-derivation; one-verse rules-tuple discrepancy logged)
- cross-finding-026-iʿjāz-architecture.md (synthesis frame)

## 1. Garden-of-forking-paths log

- Considered H5 axis specifications: (a) per-surah Shannon entropy of last-letter [chosen for rhyme axis], (b) h-new-700 window-d̄_rhyme [rejected — not per-surah], (c) h-new-700 top_letter frac [rejected — already used for cluster definition]. Choice (a) was made BEFORE running the test; documented in pre-reg. Acknowledged as rhyme-axis being mechanically extreme by construction and excluded interpretively post-run.
- Considered H2 bucket boundaries [1-20], [21-50], [51-100], [101-200], [201+] vs continuous KS test. Chose buckets (pre-locked).
- Considered alif-set inclusion/exclusion of dagger-alif ٰ. Chose to include (matches Q033-F-01 rules-tuple). Tested exclusion as POST-HOC rules-variant (cluster shrinks to 5).
- H3 direction: pre-committed LESS-than. Observed direction REVERSED (z=+1.685). Honestly published as NULL with pre-commit-violation flag per Protocol §1.8. Did NOT re-frame.

## 2. Decision points

- Cluster definition matched Q033-F-01 rules-tuple. Re-derivation at runtime confirmed `[18, 48, 65, 72, 76, 87, 91, 92]`. Aborted-on-mismatch path was implemented but not triggered.
- SHA256 of pre-reg verified at runtime line 33 of run-script.
- 10000 perms per cell; 8 sub-tests + 5 main = 11 perm tests. Total runtime 1.2s.

## 3. Honest reporting

- Family verdict: NULL CLUSTER.
- 0 of 5 Bonferroni cells PASSED.
- 1 PRE-COMMIT VIOLATION (H3 chronology direction reversed).
- 2 DIRECTIONAL (H4 mushaf, H5 4-axis composite — but H5 inflated by rhyme axis being the cluster definition).
- Post-hoc α=0.05-capped: tail-sub-cluster {76, 87, 91, 92} architecturally cohesive — re-discovery of compression-tail terminus, NOT alif-rāwī.

## 4. Output paths

- Pre-reg: `findings/phase-b-hypotheses/h-new-910-alif8-cluster-prereg.md`
- Script: `scripts/h_new_910_alif8_cluster.py`
- JSON: `findings/phase-b-hypotheses/csv/h-new-910-alif8-cluster.json`
- Findings: `findings/phase-b-hypotheses/h-new-910-alif8-cluster.md`
- Updates: MASTER-FINDINGS-LEDGER (entry added after H-NEW-900); KNOWLEDGE-GRAPH (new "RHYME / RĀWĪ CLUSTERS" section); Q033/06-novel-findings.md (alif-cluster follow-up paragraph); Q017/07-cross-references.md (12-comparator break paragraph + Q017 rules-tuple discrepancy note).

## 5. DATA-GAPs

- Per-surah tafsir surveys for Q 48, 65, 72, 76, 87, 91, 92 (all in Wave-D backlog except Q 18).
- Hadith corpus for Q 18 *Sūrat al-Kahf* (Friday-recitation hadith Muslim #1888 etc.) not engaged — not in scope of cluster-cohesion test.
- Phoneme axis used grapheme proxy (project default but coarse); IPA-aligned full-tashkeel transliteration would be more precise.
- Q017 vs H-NEW-910 alif-rate one-verse rules-tuple discrepancy unresolved.
