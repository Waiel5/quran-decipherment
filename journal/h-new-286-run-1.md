# H-NEW-286 run journal

Date: 2026-04-18
Operator: codex

## Scope

Run the preregistered exact within-zone name-class contrast for
H-NEW-286 using the H-NEW-126 concept/object name map as the binary
label source.

## Locked design

- zone fixed to `Q16..Q25`
- target subset fixed to `{16,21,22,23,25}`
- binary label fixed to `concept/object-named` vs `other`
- exact space = all `C(10,5) = 252` five-surah subsets
- primary statistic =
  `Delta_name(S) = mean_{q in S} I[label(q)=concept/object] - mean_{q in Z\\S} I[label(q)=concept/object])`
- direction = one-sided upper-tail

## Exact outputs

- concept/object surahs in zone = `{16, 21, 22, 23, 25}`
- target mean concept/object rate = `1.0`
- complement mean concept/object rate = `0.0`
- observed `Delta_name(S*) = 1.0`
- exact rank = `1 / 252`
- exact upper-tail `p = 0.003968253968253968`
- verdict = `PASS-DIRECTED`

Null summary:

- null mean = `0.0`
- null median = `0.0`
- null min = `-1.0`
- null max = `1.0`

## Continuity note

The target subset is the full concept/object-named class inside the
zone, so the result is categorical rather than graded. This is still a
bounded exact-null confirmation of the preregistered label mechanism.

## Files written

- `findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast-prereg.md`
- `scripts/h_new_286_oq18_within_zone_name_class_contrast.py`
- `findings/phase-b-hypotheses/csv/h-new-286.json`
- `findings/phase-b-hypotheses/h-new-286-oq18-within-zone-name-class-contrast.md`
- `journal/h-new-286-run-1.md`
