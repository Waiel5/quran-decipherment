#!/usr/bin/env python3
"""Q042-F-03 — root š-w-r corpus-EXACT count (direction-locked ≤3).

Pre-reg: surahs/Q042-al-shura/preregs/Q042-F-03-shura-root-singleton-prereg.md
Direction: ≤ 3 stems VINDICATED; ≥ 4 stems NULL pre-commit violation.
"""

import hashlib
import json
import re
import sys
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "surahs/Q042-al-shura/preregs/Q042-F-03-shura-root-singleton-prereg.md"
EXPECTED_SHA = "4994d48fc2ee6a179ea33a7881fbdcef414a3d47ea638155b858cc1d0b36e703"
ROOT_INDEX = ROOT / "data/morphology/root-index.json"
QAC_RAW = ROOT / "data/morphology/quranic-corpus-morphology-0.4.txt"
OUT = ROOT / "surahs/Q042-al-shura/csv/Q042-F-03.json"

ROOT_KEY = "$wr"  # Buckwalter for š-w-r


def main():
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"SHA mismatch: {actual} vs {EXPECTED_SHA}")

    # Primary: root-index.json
    ri = json.loads(ROOT_INDEX.read_text())
    attestations = ri.get(ROOT_KEY, [])

    # Secondary cross-check: direct grep of QAC v0.4 raw morphology file
    pat = re.compile(r"ROOT:\$wr(?:\||$)")
    raw_lines = []
    with QAC_RAW.open() as f:
        for line in f:
            if pat.search(line):
                raw_lines.append(line.rstrip("\n"))

    # Parse lemmas to separate consult-sense from point-sense
    details = []
    consult_sense = []
    point_sense = []
    for line in raw_lines:
        # e.g. (3:159:19:2)\t$aAwiro\tV\tSTEM|POS:V|IMPV|(III)|LEM:$aAwiro|ROOT:$wr|2MS
        m = re.match(r"\(([0-9]+):([0-9]+):([0-9]+):([0-9]+)\)\t(\S+)\t(\S+)\t(\S+)", line)
        if not m:
            continue
        s, v, w, x, form, pos, feats = m.groups()
        lem = ""
        for f in feats.split("|"):
            if f.startswith("LEM:"):
                lem = f[4:]
        entry = {
            "surah": int(s),
            "verse": int(v),
            "word_idx": int(w),
            "form_bw": form,
            "pos": pos,
            "lemma_bw": lem,
        }
        # Lemmas containing the š-w-r consonantal skeleton in consult-sense:
        # $aAwiro (impv consult), $uwraY` ("shūrā"), ta$aAwur ("mutual consultation")
        # In point-sense: >a$aArato ("she pointed")
        if lem.startswith(">a$aAr") or lem.startswith(">a$ar"):
            entry["semantic_sense"] = "point/indicate"
            point_sense.append(entry)
        else:
            entry["semantic_sense"] = "consult/consultation"
            consult_sense.append(entry)
        details.append(entry)

    total_count = len(attestations)
    raw_count = len(raw_lines)

    if total_count != raw_count:
        warning = f"Cross-check mismatch: root-index={total_count}, QAC-raw-grep={raw_count}"
    else:
        warning = None

    if total_count <= 3:
        verdict = f"VINDICATED — root š-w-r attested {total_count} time(s) (≤3 pre-committed)"
        pre_commit_honored = True
    else:
        verdict = (
            f"NULL — pre-commit violation: root š-w-r attested {total_count} times "
            f"(direction-locked ≤3)"
        )
        pre_commit_honored = False

    # Post-hoc breakdown (MW-7 capped): consult-sense only count
    consult_count = len(consult_sense)
    point_count = len(point_sense)

    out = {
        "id": "Q042-F-03",
        "title": "Root š-w-r corpus-EXACT count",
        "prereg_sha": EXPECTED_SHA,
        "rules_tuple": "(QAC-v0.4, Buckwalter-root-$wr, distinct-stem-attestations)",
        "seed": 20260509,
        "root_key_bw": ROOT_KEY,
        "total_attestations": total_count,
        "raw_qac_grep_count": raw_count,
        "cross_check_warning": warning,
        "attestations_root_index": attestations,
        "attestations_detailed": details,
        "consult_sense_count": consult_count,
        "consult_sense_loci": [(e["surah"], e["verse"]) for e in consult_sense],
        "point_sense_count": point_count,
        "point_sense_loci": [(e["surah"], e["verse"]) for e in point_sense],
        "pre_commit_honored": pre_commit_honored,
        "verdict": verdict,
        "post_hoc_note_mw7": (
            "If pre-commit fails, the consult-sense sub-field count is reported as a "
            "post-hoc-capped observation (Protocol §1.7, MW-7 single-test ceiling)."
        ),
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"Q042-F-03: {verdict}")
    print(f"  total root-attestations: {total_count}")
    print(f"  consult-sense: {consult_count}; point-sense: {point_count}")
    for e in details:
        print(f"    Q{e['surah']}:{e['verse']}:{e['word_idx']}  lem={e['lemma_bw']}  sense={e['semantic_sense']}")


if __name__ == "__main__":
    main()
