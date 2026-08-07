---
title: Cross-Finding Index — authoritative disambiguation of duplicate cross-finding IDs
author: Waiel Al-Shujaa
date: 2026-08-07
status: NAVIGATION AID — additive only; no file was renamed, moved, or renumbered to produce it
scope: every `cross-finding-0NN` identifier that resolves to more than one document
---

# Cross-Finding Index

Several `cross-finding-0NN` identifiers were minted twice, in two different directories,
by two different waves of work. Both mints are legitimate records of what was found when.
**Nothing here renames or renumbers anything.** This file exists so that a bare ID in prose
can always be resolved, and so that future writing has one rule to follow.

---

## The handle convention

> **Rule: never write a bare `cross-finding-0NN` for any ID listed in the collision table
> below. Write the handle instead.**

Two forms, both already implied by what is on disk — neither requires renaming a file:

| Form | When to use | Example |
|---|---|---|
| **Long handle** — the file's own slug, minus `.md` | Always safe; this is also the working Obsidian wikilink | `cross-finding-026-formal-cohesion-vs-chiasmus-bifurcation` |
| **Short handle** — `cf-0NN-<qualifier>` | Prose, tables, ledger entries | `cf-026-formal`, `cf-026-iʿjāz` |

The `-formal` qualifier is **not invented here**. The four 2026-05-09/29/30 laws already
carry `finding_id: cross-finding-0NN-formal` in their own frontmatter — verified in
`findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md`,
`…-026-formal-cohesion-vs-chiasmus-bifurcation.md`,
`…-027-formal-eponymy-independence-law.md`, and
`…-028-formal-register-coded-discourse-grammar.md`. Their H1 headings likewise read
"Cross-finding-0NN (FORMAL) — …". This index simply adopts the qualifier that the files
already assert, and supplies matching qualifiers for the other claimants.

Non-colliding IDs (`cross-finding-001` … `cross-finding-024`, except 023) need no handle;
a bare reference to those is unambiguous.

---

## Collision table

Every row was read directly. "Mint date" is the `date:` / `date_locked:` field in the file's
own frontmatter.

### cross-finding-023 — 2 claimants (both in `findings/phase-b-hypotheses/`)

| Handle | Path | Mint | Status | What it is |
|---|---|---|---|---|
| `cf-023-closure` | `findings/phase-b-hypotheses/cross-finding-023-causal-generative-closure.md` | 2026-04-18 | SYNTHESIS-COMPLETE — live | Causal-generative closure of the Complete Equation; "sufficient but not yet minimally parsimonious hinge scaffold" |
| `cf-023-oq15` | `findings/phase-b-hypotheses/cross-finding-023-oq15-causal-generative-closure.md` | 2026-04-18 | SYNTHESIS-TERMINAL — live | OQ-15 causal-generative layer CONFIRMED; 4-principle equation + top-100 Fisher-Rao hinges reproduce the canonical mushaf |

Same day, same subject, two distinct documents (12,244 and 18,581 bytes; `diff` confirms they
differ). `cf-023-oq15` is the longer and more specific write-up. This is the one collision
where both claimants cover the *same* material, so a bare `cross-finding-023` is not
misleading about topic — only about which document you land in.

### cross-finding-025 — 3 claimants

| Handle | Path | Mint | Status | What it is |
|---|---|---|---|---|
| `cf-025-multiaxis` | `findings/cross-finding/cross-finding-025-multi-axis-architecture.md` | 2026-04-28 | SYNTHESIS — superseded by `cf-026-iʿjāz` | Multi-axis architecture: cohesion-tail R²=0.986, 5-factor regression OOS r=0.929, continuous outlier-spectrum |
| `cf-025-marker` | `findings/phase-b-hypotheses/cross-finding-025-marker-thickness-vs-fr-cohesion-threshold.md` | 2026-05-09 | PRELIMINARY-SYNTHESIS — ancestor of `cf-025-formal` | Marker-thickness vs Fisher-Rao-cohesion threshold; its own §"next steps" calls for "cross-finding-025-formal" |
| `cf-025-formal` | `findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md` | 2026-05-09 | **FORMAL CODIFICATION — live law**, bounded by `cf-026-formal` | Scale-of-aggregation / pericope-flip law |

`cf-025-marker` and `cf-025-formal` are the same lineage: the FORMAL file's status reads
"graduates from PRELIMINARY 2026-05-09 PM to FORMAL 2026-05-09 PM-2", and `cf-025-marker`
line 109 explicitly names the future "Cross-finding-025-formal". `cf-025-multiaxis` is an
unrelated topic that happens to share the number.

### cross-finding-026 — 2 claimants

| Handle | Path | Mint | Status | What it is |
|---|---|---|---|---|
| `cf-026-iʿjāz` | `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md` | 2026-04-28 | TERMINAL SYNTHESIS — live | iʿjāz architecture: content compresses ⊥ rhyme/phoneme disperse; al-Bāqillānī locked at r=−0.86. **Holds the §13 4-cell typology** |
| `cf-026-formal` | `findings/phase-b-hypotheses/cross-finding-026-formal-cohesion-vs-chiasmus-bifurcation.md` | 2026-05-29 | **FORMAL CODIFICATION — live law** | The cohesion/chiasmus bifurcation; bounds `cf-025-formal` |

**Disambiguator worth memorising: only `cf-026-iʿjāz` has a §13.** Any reference to
"cross-finding-026 §13" means the 2026-04-28 file. Verified: `§13. Amendment 2026-04-28 —
4-cell typology` at `findings/cross-finding/cross-finding-026-iʿjāz-architecture.md:180`;
grep for `§13` in the formal file returns nothing.

### cross-finding-027 — 2 minted claimants + 1 never-minted proposal

| Handle | Path | Mint | Status | What it is |
|---|---|---|---|---|
| `cf-027-takrīr` | `findings/cross-finding/cross-finding-027-ijaz-al-takrir.md` | 2026-04-28 | **NULL on pre-reg, DIRECTIONAL post-hoc — landed, not in flight** | *iʿjāz al-takrīr* refrain-saturation axis. Verdict: FALSIFIED-AS-PRE-REGISTERED; Q 55 is *sui generis*, not the head of a class |
| — | `findings/cross-finding/cross-finding-027-prereg.md` | 2026-04-28 | pre-reg for the above (`id: cross-finding-027-prereg`) | SHA 14b4ae88… |
| `cf-027-formal` | `findings/phase-b-hypotheses/cross-finding-027-formal-eponymy-independence-law.md` | 2026-05-30 | **FORMAL CODIFICATION — live law** | Eponymy-independence: a surah's name predicts neither its lexical-density peak nor its narrative-cycle centrality |

**Third, never-minted claimant.** A *different* cross-finding-027 was proposed for the
10-surah Medinan-ṭiwāl cluster {Q 57-66} at
`findings/phase-b-hypotheses/h-new-560-meccan-tiwal.md:70` ("Candidate cross-finding-027")
and again at `MASTER-FINDINGS-LEDGER.md:1428`. No such file was ever created. Treat those
two lines as a lapsed reservation, not a pointer.

### cross-finding-028 — 2 claimants

| Handle | Path | Mint | Status | What it is |
|---|---|---|---|---|
| `cf-028-liturgical` | `findings/cross-finding/cross-finding-028-liturgical-pair-fr.md` | 2026-05-07 | CONFIRMED at α_bon=0.025 — live | Liturgical-recitation surah-pair ↔ Fisher-Rao-near-pair |
| — | `findings/cross-finding/cross-finding-028-prereg.md` | 2026-05-07 | pre-reg for the above (`id: cross-finding-028`) | direction pre-committed |
| `cf-028-formal` | `findings/phase-b-hypotheses/cross-finding-028-formal-register-coded-discourse-grammar.md` | 2026-05-30 | **FORMAL CODIFICATION — live law** | Register-coded discourse grammar; LOO 76.9% vs 44% baseline |

---

## Correction to an earlier report — `cross-finding-010` and `cross-finding-012` are NOT collisions

An earlier survey (`HANDOFF/FRONTIER-MAP-2026-08-07.md` §C-1) listed 010 and 012 among the
duplicate IDs. **That was a miscount and is withdrawn here.** The counting command did not
exclude pre-registration files, so it treated each prereg/result pair as a duplicate.

On inspection both are ordinary prereg/result pairs, which is the project's normal and correct
convention — a pre-registration is *supposed* to carry the same `id:` as the result it locks:

- `findings/phase-b-hypotheses/cross-finding-010-extended-network-prereg.md`
  (`status: PRE-REGISTERED 2026-04-17`) → `…cross-finding-010-extended-network.md`
  (`status: MIXED …`)
- `findings/phase-b-hypotheses/cross-finding-012-late-meccan-scripture-announcement-prereg.md`
  (`status: PRE-REGISTERED 2026-04-17`) → `…cross-finding-012-late-meccan-scripture-announcement.md`
  (`status: PASS-DIRECTED …`)

Neither needs a handle. The same applies to `cross-finding-027-prereg.md` and
`cross-finding-028-prereg.md` in `findings/cross-finding/`, which are listed above only for
completeness. The genuine collisions are **023, 025, 026, 027, 028** — five IDs, eleven files.

---

## Reference sweep — how bad is the ambiguity in practice?

Swept all `.md` files in the live tree (excluding `.git/`, tooling directories, and `scratch/`) for bare
references — occurrences of `cross-finding-0NN` not immediately followed by a filename slug.

| Stage | Count |
|---|---:|
| Bare references to the colliding IDs 025-028 | 1,064 |
| — resolvable from the same line (topic vocabulary, a date, or a slug elsewhere on the line) | 721 |
| — resolvable because the containing file predates the formal mint and so cannot mean it | 200 |
| **Residual after both filters** | **143** |

The two series have almost disjoint subject-matter vocabulary, which is what makes most
references self-resolving: *scale-of-aggregation / pericope-flip / chiasmus / eponymy /
register* belong to the 2026-05 laws, while *multi-axis / 5-factor / outlier-spectrum /
sig_A / 4-cell / takrīr / liturgical-pair* belong to the 2026-04-28 and 2026-05-07 series.

**On reading the 143 residual lines, the great majority are still resolvable by lineage** —
they sit inside pericope-cohesion or marker-thickness discussions where only one reading is
possible. The 25 residual `cross-finding-025` lines in `MASTER-FINDINGS-LEDGER.md`, for
instance, are all in sajda / IMPV-qrA / thick-marker / flip-pair context and unambiguously
mean `cf-025-formal` or its `cf-025-marker` ancestor; the topic filter missed them only
because the keyword sat on an adjacent line.

**No mass edit is proposed.** The residual is a readability tax, not an error. It should be
paid down opportunistically: when a file is edited for another reason, upgrade its bare
references to handles.

### Residual concentrations, for deliberate follow-up

Listed so the work can be scheduled, highest first. `file (count) — reading that context supports`:

| File | Bare refs left | ID | Reading supported by context |
|---|---:|---|---|
| `MASTER-FINDINGS-LEDGER.md` | 25 | 025 | `cf-025-formal` / `cf-025-marker` |
| `findings/phase-b-hypotheses/h-new-2260-prophet-cycle-pericope.md` | 6 | 025 | `cf-025-formal` |
| `findings/phase-b-hypotheses/prereg-h-new-2480-centrality-regression.md` | 6 | 027 | `cf-027-formal` |
| `findings/phase-b-hypotheses/cross-finding-025-marker-thickness-vs-fr-cohesion-threshold.md` | 5 | 025 | self-references |
| `findings/phase-b-hypotheses/prereg-h-new-2260-prophet-cycle-pericope.md` | 5 | 025 | `cf-025-formal` |
| `surahs/Q023-al-muminun/06-novel-findings.md` | 5 | 025 | `cf-025-formal` |
| `findings/phase-b-hypotheses/h-new-2480-centrality-regression.md` | 4 | 027 | `cf-027-formal` |
| `findings/phase-b-hypotheses/h-new-2470-dispersion-law.md` | 4 | 028 | `cf-028-formal` |
| `surahs/Q023-al-muminun/07-cross-references.md` | 4 | 025 | `cf-025-formal` |
| `HANDOFF/SESSION-HANDOFF-2026-05-09-PM.md` | 3 | 025 | `cf-025-formal` |
| `findings/phase-b-hypotheses/cross-finding-028-formal-register-coded-discourse-grammar.md` | 3+3+1+1 | 025/026/027/028 | the formal series throughout |
| `findings/phase-b-hypotheses/prereg-h-new-1760-hawamim-opener-pericope.md` | 3 | 025 | `cf-025-formal` |
| `findings/phase-b-hypotheses/h-new-1800-99-names-enumeration.md` | 3 | 025 | `cf-025-formal` |
| `surahs/Q054-al-qamar/07-cross-references.md` | 3 | 028 | `cf-028-formal` |

Remaining residual is a long tail of 1-2 references per file across ~35 further files, all in
`findings/phase-b-hypotheses/` and `surahs/`.

### Journals and session handoffs are deliberately left alone

`journal/integration-2026-04-28.md`, `journal/Q055-al-rahman-template-builder-2026-04-28.md`,
`journal/cross-finding-028-run-1.md`, and `HANDOFF/SESSION-HANDOFF-2026-05-09*.md` all contain
bare references and, in the journals' case, "in flight" language that later became false.
These are dated records of what was true on the day they were written. They are not corrected,
on the principle that the record of the work is not rewritten.

---

## Pointers that were not merely ambiguous but WRONG — corrected 2026-08-07

Five pointers asserted something false rather than something unclear. Each was corrected in
place with a visible notice; none was silently edited.

Line numbers below are the **pre-correction** ones, recorded so the change is auditable.
Adding the correction notices shifted them: `KNOWLEDGE-GRAPH.md` 187→189, 223→225, 278→280.

| # | File:line (pre-correction) | What was wrong | Correction |
|---|---|---|---|
| 1 | `KNOWLEDGE-GRAPH.md:187` | "(cross-finding-027 in flight)" — the test landed 2026-04-28 | → `cf-027-takrīr`, verdict FALSIFIED-AS-PRE-REGISTERED |
| 2 | `KNOWLEDGE-GRAPH.md:223` | "(5th-cell candidate, queued as cross-finding-027)" | → landed, `cf-027-takrīr`, NULL |
| 3 | `KNOWLEDGE-GRAPH.md:278` | heading "Queued: cross-finding-027 (in flight)" | → "Landed NULL: cf-027-takrīr" |
| 4 | `KNOWLEDGE-GRAPH.md:280` | "Status: 5th-cell candidate, awaiting cross-surah evaluation" | → records the actual verdict |
| 5 | `MASTER-FINDINGS-LEDGER.md:1667` | "Synthesis (in flight as cross-finding-027) … Pending corpus-level pre-registered LOOCV" | → records the landed NULL |

All five were stale relative to the project's **own** source document:
`findings/cross-finding/cross-finding-026-iʿjāz-architecture.md:233-235` has recorded the
FALSIFIED verdict since 2026-04-28. `KNOWLEDGE-GRAPH.md` carries
`date_last_updated: 2026-04-28`, which explains how it drifted.

### A sixth, separate broken pointer — also corrected

`findings/phase-b-hypotheses/cross-finding-025-formal-scale-of-aggregation-law.md:75` read:

> `- Earlier preliminary: findings/phase-b-hypotheses/cross-finding-025-preliminary-marker-thickness.md`

**That file does not exist.** The real ancestor is
`cross-finding-025-marker-thickness-vs-fr-cohesion-threshold.md`. Corrected with a notice.

---

## Standing rule going forward

1. Before minting a new `cross-finding-NNN`, check this index and
   `ls findings/cross-finding/ findings/phase-b-hypotheses/cross-finding-*`. Two directories
   mint into the same numeric space.
2. Never write a bare colliding ID. Use the handle.
3. When a pre-registration reserves a number, that number is taken even if the test later
   lands NULL — `cf-027-takrīr` is a NULL result, not a free slot.
4. Corrections get a visible notice in the file. Journals and dated handoffs are never
   retro-corrected.
