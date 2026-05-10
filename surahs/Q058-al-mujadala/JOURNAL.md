---
surah: 58
surah_name_translit: al-Mujādala
file_type: journal
date_last_updated: 2026-05-09
---

# Q 58 al-Mujādala — Investigation Journal

## 2026-05-09 — Wave-H specialist landing

**11:00 UTC** — Specialist briefed via parallel dispatch. Read SESSION-HANDOFF-2026-05-09.md §4-§5 and INVESTIGATION-PROTOCOL.md §1.

**11:15** — Read existing surahs/Q058-al-mujadala/00-overview.md (pre-existing from Wave-1 scaffold). Identified Q 58 empirical anchors: 22 verses, Medinan, *al-mujādila* tradition (Khawla bint Thaʿlaba pericope), member of musabbiḥāt-opener cluster {Q 57, 59, 61, 62, 64} — note Q 58 does NOT open with *sabbaḥa* despite being in the short-Medinan block.

**11:30 — Pre-registration phase** — Wrote and SHA-256 locked 5 pre-reg files BEFORE computation:

| File | SHA-256 |
|:--|:--|
| Q058-F-01-allah-density-prereg.md | `5e2d18067236123bc610ab6017691119685732dcc6b6357a7e0af39cbf2f7e1f` |
| Q058-F-02-h1080-cluster-rank-prereg.md | `d28198ad222fdee67c61a73b9b1055f130259122d4c689cbece9f02b74fea2ee` |
| Q058-F-03-najwa-abrogation-prereg.md | `cfcc79656aaa6c3af3b59cfa9c36bce73850792aaa42d563a3c45e565f8f043c` |
| Q058-F-04-hizb-faction-vocabulary-prereg.md | `9618031240079d8c5aa79cf35aa03ce16dbf178f6b0ffef96eb9d4f109d74703` |
| Q058-F-05-q57-q58-q59-seam-prereg.md | `b79392fe0a2e07f6f64db18952ff9f4b5fee11c06c8f40448d70aadb38bf6579` |

Each pre-reg specifies direction-of-effect, null model, decision rule, and rules-tuple. SHA-256 embedded in scripts at /scripts/Q058_F_0[1-5]_*.py for runtime verification.

**11:45 — Garden-of-forking-paths log (BEFORE running tests)** —

For F-01 (Allāh-density): Decision points encountered while writing pre-reg —
1. Token rule: substring match vs strict-isolated-token (whitespace-bounded). Decision: substring as primary (3/3 H-hypothesis), strict as alternative report. Reason: classical recitation includes Allāh inside compound nominals like *li-llāh*, *bi-llāh*, *Allāhumma*.
2. Inclusion of basmala in Q 58 verse count. Decision: basmala-counted-only-in-Q1 (standard rules-tuple); Q 58 first verse is 22-counted excluding any basmala.
3. Null design: permutation (random Allāh-token distribution) vs closed-form (iid Bernoulli with empirical p). Decision: REPORT BOTH (MW-3 alternative-models).

For F-02 (cluster): Cluster definition. Used H-NEW-1080 published {Q 57-66} = 10 surahs. Considered narrower {Q 57, 59, 61, 62, 64} musabbiḥāt-only definition; rejected because H-NEW-1080 already published with the wider cluster.

For F-04 (*ḥzb*): Considered using QAC root vs substring stem. Used substring stem ح-ز-ب for primary count; QAC for verification. Both agreed at 4 tokens in Q 58.

**12:00 — Test execution phase** — Ran all 5 scripts sequentially:

```
$ python scripts/Q058_F_01_allah_density.py
$ python scripts/Q058_F_02_h1080_cluster_rank.py
$ python scripts/Q058_F_03_najwa_abrogation.py
$ python scripts/Q058_F_04_hizb_faction.py
$ python scripts/Q058_F_05_q57_q58_q59_seam.py
```

All SHA-checks passed. Outputs in csv/Q058-F-0[1-5].json.

**12:30 — Results summary** —

- F-01: **CONFIRMED corpus-EXACT** at closed-form p = 6.79e-13. The 22/22 verse Allāh-coverage is corpus-unique at length ≥5.
- F-02: **CONFIRMED**. Q 58 centrality rank 8/10 within {Q 57-66}; nearest neighbor Q 64 (cluster-internal); p = 9.999e-5 permutation.
- F-03: **CONFIRMED**. 3/4 classical sources attest the Q 58:12→13 abrogation explicitly; 3 distinct isnād chains; 5 lexical markers.
- F-04: **DIRECTIONAL** (2/3 sub-hypotheses pass). *ḥizb al-shayṭān* corpus-exclusive to Q 58; *ḥizb Allāh* in only 2 surahs. The 30% share-of-corpus threshold fails (21%). Net: a 2.8× concentration over length-weighted null, p = 9.999e-5.
- F-05: **NULL** with pre-commit violation. Both directions failed: Q 58→Q 59 is HIGHER cost than Q 57→Q 58, opposite to pre-committed direction. Published with full prominence per PRE-REG-STANDARD-04.

**13:00 — Cross-finding integration writeup** — Updated `07-cross-references.md` (pre-existing) to flag Q 58↔Q 64 as new corpus FR-pair, and Q058-F-01 as 13th corpus-EXACT iʿjāz formal pattern.

## Methodological observations

1. **Closed-form null saved the day for F-01**. The 22-verse 100%-coverage configuration is so extreme that the permutation null can only report `p < 1/n_perm = 1e-4`; the closed-form iid null gives the actual 6.79e-13 magnitude. **Lesson**: for corpus-MAX claims at extreme tails, always report closed-form alternative.

2. **Direction-of-effect violation in F-05** strengthens credibility by showing the pre-registration discipline is working. The naive pre-committed direction (Medinan-historical continuity smoother than thematic-gap) was empirically wrong; the *musabbiḥāt-opener* axis dominates.

3. **The *ḥizb*-pair finding** in F-04 wasn't part of the initial pre-reg but emerged from the data. Logged here for transparency: the *ḥizb al-shayṭān*↔*ḥizb Allāh* antithetical pairing within 4 verses (vv 19, 22) is a post-hoc observation. Per MW-7 (post-hoc cap), single-test α=0.05 applies until replication. Replication channel: identify other surahs with antithetical phrase pairs at v-distance ≤5 (queued).

4. **Hadith-corpus verification**: F-03 classical attestation was verified by direct grep against `/data/literature/classical-tafsir/raw/` for al-Ṭabarī and al-Wāḥidī. Three distinct isnād chains located; verified ʿAlī (named directly, not via intermediate), Mujāhid via Ibn Abī Najīḥ, and Qatāda chains.

## Next-session follow-ups queued

- Replicate Q058-F-04 post-hoc *ḥizb*-antithesis observation by corpus-wide scan for antithetical-phrase-pairs at v-distance ≤5
- Inline test: H-NEW-1350 (Allāh-density distribution all 114 surahs, Medinan/Meccan separation)
- Q 58↔Q 64 nearest-pair deeper investigation
- al-Biqāʿī Q 57→Q 58 munāsabah claim (musabbiḥāt-opener axis test)

---

*Single-author voice maintained throughout. No agent / orchestrator references in deliverables (this JOURNAL.md documents method as expected by PRE-REG-STANDARD-04).*
