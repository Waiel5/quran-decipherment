# Erratum: commit `eb6a40d0e` contains work its message does not describe

**Date:** 2026-08-09
**Severity:** record-integrity, not result-integrity. No published number is affected.
**Self-reported.** Nothing downstream failed; nothing would have surfaced this.

---

## 1. What happened

Commit `eb6a40d0e` is titled *"Two wrong citations of ONE Itqān passage…"* and its message describes
exactly that: two citation fixes and the H-NEW-3030 post-directive revision.

It was staged with `git add -A` instead of explicit paths. **It therefore also contains four other
lanes' working-tree files, none of which its message mentions:**

| Swept in | State at commit |
|:--|:--|
| `prereg-h-new-3040-modality-axis.md` (696 lines) | complete, lock verifies |
| `scripts/h-new-3040.py`, `h-new-3040-posthoc.py` | complete |
| `runs/h-new-3040/` — 3 run directories | complete |
| `h-new-3010-conditional-register.md` (+75) | post-report revision, unreviewed |
| `h-new-3020-loanword-donor-strata.md` (+37) | post-report revision, unreviewed |
| `prereg-h-new-3050-muqattaat-length-floor.md` (+91) | threshold-free restatement, unreviewed |

**H-NEW-3040 has no finding document.** Its lane was mid-flight. So the commit publishes a
pre-registration, a script and three run directories for a hypothesis whose result had not been
reported to me, let alone audited.

## 2. Why this is a defect even though nothing is wrong

Every file is legitimate work. All 16 pre-registration locks verify, including
`prereg-h-new-3040` → `48e02a04…61e353df`. The leak audit was clean. No number moved.

The defect is that **the commit record misdescribes its own contents.** In a project whose entire
claim to credibility is that the audit trail is trustworthy, a commit message that omits 6,900 lines
of what it carries is a failure of exactly the thing being claimed. Anyone reconstructing when
H-NEW-3040's pre-registration entered the repo would find it under a commit about al-Suyūṭī.

It also breaks the ordering the protocol depends on. A pre-registration is evidence that a
prediction preceded a result. Committing one *alongside its own run directories*, in a commit that
mentions neither, destroys the visible separation between "registered" and "ran" — even though, in
fact, the runtime SHA check passed and the order was correct.

## 3. What was NOT done

**History was not rewritten.** The commit is pushed. Amending or force-pushing to make the record
look tidier would be a worse act than the original error: it would edit an audit trail to conceal
that the audit trail was mishandled. This erratum is the correct remedy — the defect stays visible
and gets a name.

## 4. The rule

**Stage by explicit path, never `git add -A`, whenever more than one lane has files in the tree.**

The failure mode is specific and it is not "committing something broken" — everything here was fine.
It is **committing something undescribed**, which is invisible at commit time and permanent
afterwards. `git add -A` is safe only in a single-writer tree, and this tree has not been
single-writer all day.

Detection is one line before committing: `git status --porcelain` and read it, or
`git diff --cached --stat` and confirm every path is one you meant.

## 5. Attribution of the contents

For the record, so the swept-in work is findable:

- **H-NEW-3040** (modality axis, F-10) — pre-registration and runs entered at `eb6a40d0e`; its
  finding document and verdict are pending and will be committed separately with a proper message.
- **H-NEW-3010 / H-NEW-3020 revisions** — post-report edits by their own lanes, entered here rather
  than under their own commits (`13fa43a64`-adjacent). Their verdicts as published are unchanged.
- **prereg-h-new-3050 revision** — restatement of the muqaṭṭaʿāt hypothesis in the threshold-free
  `R_min` form. No run directory exists for it, so immutability had not attached and the revision is
  not a prereg violation. Its SHA is now different from the one quoted in commit `303`; that quoted
  value is a historical record of the file at that time and is not corrected.

Related: [[UNIT-DRIFT-DEFECT]] §9 (never edit a prereg after its run), [[TIED-OUTCOME-DEFECT]] §7.2.
