# HOW TO DISPATCH — operational playbook

Quick reference for the next agent on dispatching specialists.

---

## Pattern: parallel specialist dispatch

```
Use Agent tool with:
  description: short (3-5 word) task
  subagent_type: general-purpose (or specialized type)
  run_in_background: true
  prompt: full self-contained briefing with file paths and pre-reg
```

Each specialist gets a SELF-CONTAINED prompt. They have NO conversation context. Brief them like a smart colleague who just walked into the room.

---

## Prompt template (proven pattern from this session)

```
You are h-new-N-specialist on the Quran Decipherment Project at /Users/grey/Downloads/quran/.

TASK: [pre-register and execute / execute pre-registered] H-NEW-N — [one-line description].

PRE-REG ALREADY WRITTEN: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-N-prereg.md (read; follow exactly)
[OR if no pre-reg: write one first per PRE-REG-STANDARD-04 fields then execute]

CONTEXT:
- [Relevant prior findings]
- [Why this matters]
- [Pre-existing data files]

PROCEDURE:
1. [Step]
2. [Step]
...

DATA:
- /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
- /Users/grey/Downloads/quran/analysis/tools/loader.py
- [other relevant paths]

WRITE:
1. Pre-reg: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-N-{slug}-prereg.md
2. Script: /Users/grey/Downloads/quran/scripts/h_new_N_{slug}.py
3. JSON: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/csv/h-new-N.json
4. Findings: /Users/grey/Downloads/quran/findings/phase-b-hypotheses/h-new-N-{slug}.md
5. Journal: /Users/grey/Downloads/quran/journal/h-new-N-run-1.md

RULES:
- Lock {test family / classification / threshold} BEFORE testing
- Bonferroni-{k} (α_per = 0.05/k)
- MW-5 positive control: [specific test that should fire if pipeline correct]
- Seed 20260416 (or session date)
- Publish PASS/NULL identically

Report back (≤ 250 words): per-cell verdict + headline numbers.
```

---

## Pattern: inline analysis (when test is small)

For small computations (closed-form, < 1 minute runtime), DO INLINE rather than dispatching. Use Bash with python3 inline scripts. Saves agent overhead.

```python
python3 << 'PY'
import sys
sys.path.insert(0, "/Users/grey/Downloads/quran/analysis")
from tools.loader import load_quran
quran = load_quran("no-tashkeel")
# compute...
PY
```

---

## Project's loader interface

```python
from tools.loader import load_quran
quran = load_quran("no-tashkeel")  # also "min-tashkeel", "full-tashkeel"
for s in quran:  # 114 surahs
    s.id           # 1..114
    s.name         # Arabic name
    s.transliteration
    s.type         # Meccan / Medinan
    s.total_verses
    for v in s.verses:
        v.id       # 1..N within surah
        v.text     # bare Arabic string
```

---

## How to message running specialists

```
SendMessage tool:
  to: <agent-name-or-id>
  message: text with corrections / amendments / questions
  summary: 5-10 word preview
```

Use this to push pre-reg amendments to running specialists (audit-032 pattern).

---

## How to track progress

Use `TaskCreate` for each specialist immediately after dispatch:

```
TaskCreate:
  subject: "H-NEW-N — short title"
  description: "specialist agent details"
  activeForm: "h-new-N-specialist running"
```

Then `TaskUpdate` with `status: completed` and `metadata: {...}` when results land.

---

## Common pitfalls (from this session's experience)

1. **Specialist timeouts**: ~70+ min agents may stream-idle-timeout. The script may have completed; check disk for outputs before declaring failure.

2. **Rate limits**: agents can hit user-account rate limits. When this happens, all in-flight agents fail simultaneously. Re-dispatch when limits reset.

3. **Pre-reg amendments mid-flight**: tightening (stricter α, narrower verdict criteria) self-verifies. Loosening requires ratification. Always tighten via SendMessage to running specialists when audit catches a defect.

4. **Specialist verdict-tree conservatism**: Specialists sometimes produce conservative verdicts (e.g., "EXPLORATORY-POST-HOC" for any 1-cell-pass). Refine in the integrator findings file with honest reasoning when warranted (e.g., when the passing cell was a CLEAN pre-registered cell, not the post-hoc-noticed one).

5. **MW-7 internal-error gate**: Before promoting any finding to MASTER-LEDGER, run the 3-check (citations, gate-specs, synthesis identifiers).

6. **Cross-finding promotions**: cross-finding-008 was flagged by audit-034 for INFLATING independence ("5 tests" but H-NEW-53/55/56 share corpus + features → effective 2-3 axes). Future cross-findings: be honest about test independence.

---

## Suggested first-wave dispatch (paste into prompt)

After reading the HANDOFF files, dispatch these in parallel:

1. **NM-1** H-NEW-93 — Q 29 + Q 30 sub-pattern characterization
2. **NM-2** H-NEW-94 — Q 16-25 cluster-empty zone deep-dive
3. **NM-3** H-NEW-95 — Khawātim extension second-look
4. **NM-13** H-NEW-103 — musabbiḥāt 4-form sub-typology
5. **NM-21** cross-finding-010 — META-cluster network EXTENDED
6. **audit-035** — skeptical auditor for the new wave

See `03-NEXT-MOVES.md` for full prompts.

---

## When in doubt

Read `MASTER-FINDINGS-LEDGER.md`. It is the authoritative single source of truth.

If the ledger and a finding-file disagree, the LEDGER wins. Update the finding-file to match.

If a new finding contradicts a confirmed prior finding, you have CRITICAL EVIDENCE — document carefully, audit, possibly retract one or the other. This is rare; treat with care.
