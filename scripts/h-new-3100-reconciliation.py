#!/usr/bin/env python3
"""H-NEW-3100 addendum: reconcile the two instruments' divergence ratios, and
record the al-Suyuti rasm anchor.

DESCRIPTIVE ONLY. No inference, no null, no verdict. This exists because two
instruments disagreed by 1.8x on the size of the set H-NEW-3100 is about, and
picking the friendlier number would be the failure this project keeps
cataloguing. It reproduces BOTH.
"""

import hashlib
import json
import os
import sys
import unicodedata
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
import arabic_normaliser as AN  # noqa: E402

_src = open(os.path.join(ROOT, "scripts", "h-new-3100.py"), encoding="utf-8").read()
_ns = {"__file__": os.path.join(ROOT, "scripts", "h-new-3100.py")}
exec(_src.split("def main()")[0], _ns)
align = _ns["align"]

# What the team lead's instrument reported, quoted for comparison, not adopted.
TEAM_LEAD_REPORT = {"pairs": 74740, "letter": 19138, "mark": 21793, "ratio": 21793 / 19138}

ITQAN = "data/literature/classical-tafsir/raw/suyuti-itqan.openiti.raw.txt"
MARKS = set(chr(c) for c in range(0x064B, 0x0660)) | AN.QURANIC_ANNOTATION | {AN.TATWEEL}


def depth0(t, dagger):
    """Strip combining marks only. Approximately a naive diff."""
    t = t.replace(AN.SUPERSCRIPT_ALEF, AN.ALEF if dagger == "letter" else "")
    return "".join(c for c in t if c not in MARKS)


def depth1(t, dagger):
    """depth0 + alef-wasla fold (H-NEW-2740's N1)."""
    return depth0(t, dagger).replace(AN.ALEF_WASLA, AN.ALEF)


def depth2(t, dagger):
    """depth1 + madda / tatweel-hamza / alef-madda reconciliation. == bare()."""
    t = t.replace("ٓ", "").replace(AN.TATWEEL + "ٔ", "ء")
    t = t.replace(AN.SUPERSCRIPT_ALEF, AN.ALEF if dagger == "letter" else "")
    t = t.replace(AN.ALEF_WASLA, AN.ALEF)
    t = unicodedata.normalize("NFC", t)
    return "".join("ءا" if c == "آ" else c for c in t if c not in MARKS)


DEPTHS = [("L0_strip_marks_only", depth0),
          ("L1_plus_alef_wasla", depth1),
          ("L2_plus_madda_hamza_alefmadda", depth2)]

# Lines READ in this session before being cited. Nothing here is quoted unhelpfully
# from another finding; each was opened and printed.
ANCHOR_LINES = {
    23216: "naw' heading: al-naw' al-sadis wa-l-sab'un: fi marsum al-khatt wa-adab kitabatihi",
    23255: "the six qawa'id sentence",
    23257: "qa'ida 1: al-hadhf",
    23258: "hadhf al-alif from ya' al-nida' AND ha' al-tanbih, with named examples",
    23259: "continuation: ha'ulа'i, ha antum",
    23336: "qa'ida 2: al-ziyada",
    23359: "qa'ida 3 heading",
    23360: "qa'ida 3: fi al-hamz",
    23397: "qa'ida 4 heading",
    23398: "qa'ida 4: fi al-badal",
    23417: "qa'ida 5 heading",
    23418: "qa'ida 5: fi al-wasl wa-l-fasl",
    23449: "ibn umm, except in Ta-Ha, where the hamza is written as a waw",
    23450: "and the hamza of ibn was elided, so it became thus: yabna'umm",
    23452: "qa'ida 6 heading",
    23453: "qa'ida 6: ma fihi qira'atan",
}

TYPE_TO_QAIDA = {
    "T1_HADHF_ALIF": ("al-hadhf", 23257), "T2_HADHF_YA": ("al-hadhf", 23257),
    "T3_HADHF_WAW": ("al-hadhf", 23257), "T4_HADHF_LAM": ("al-hadhf", 23257),
    "T5_ZIYADA_ALIF": ("al-ziyada", 23336), "T6_ZIYADA_WAW": ("al-ziyada", 23336),
    "T7_ZIYADA_YA": ("al-ziyada", 23336),
    "T8_BADAL_YA_ALIF": ("al-badal", 23398), "T9_BADAL_WAW_ALIF": ("al-badal", 23398),
    "T11_BADAL_OTHER": ("al-badal", 23398),
    "T10_HAMZ": ("al-hamz", 23360),
    "MERGE_SITES": ("al-wasl wa-l-fasl", 23418),
}


def sha256(path):
    h = hashlib.sha256()
    with open(os.path.join(ROOT, path), "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()


def main():
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "runs", "h-new-3100-reconciliation", stamp)
    os.makedirs(rundir, exist_ok=False)
    log_lines = []

    def log(m):
        print(m); log_lines.append(m)

    def load(p):
        return [l for l in open(os.path.join(ROOT, p), encoding="utf-8").read().splitlines()
                if l.strip() and not l.startswith("#")]

    U, S = load("data/alt-text/quran-uthmani-txt.txt"), load("data/alt-text/quran-simple-txt.txt")
    pairs, n_merge = [], 0
    for ul, sl in zip(U, S):
        ut, st = ul.split(), sl.split()
        for kind, ii, di, jj, dj in align(ut, st):
            if di == 1 and dj == 1:
                pairs.append((ut[ii], st[jj]))
            elif kind.startswith("MERGE"):
                n_merge += 1
    n_uth = sum(len(l.split()) for l in U)

    log("=== PAIR ACCOUNTING — is the alignment exhaustive? ===")
    log(f"  Uthmani tokens                {n_uth}")
    log(f"  1:1 aligned pairs             {len(pairs)}")
    log(f"  merge sites (1 Uthmani : k)   {n_merge}")
    log(f"  pairs + merges                {len(pairs) + n_merge}   "
        f"identity holds: {len(pairs) + n_merge == n_uth}")
    log(f"  team-lead instrument pairs    {TEAM_LEAD_REPORT['pairs']}  "
        f"-> unpaired Uthmani tokens {n_uth - TEAM_LEAD_REPORT['pairs'] - n_merge}")

    log("\n=== RATIO vs NORMALISATION DEPTH — both instruments reproduced ===")
    log(f"  {'depth':34s} {'letter':>8s} {'mark':>8s} {'ratio':>7s}")
    ladder = {}
    for name, fn in DEPTHS:
        a = sum(1 for u, s in pairs if fn(u, "letter") != fn(s, "letter"))
        b = sum(1 for u, s in pairs if fn(u, "mark") != fn(s, "mark"))
        ladder[name] = {"letter": a, "mark": b, "ratio": b / a}
        log(f"  {name:34s} {a:8d} {b:8d} {b/a:7.3f}")
    log(f"  {'TEAM LEAD (reported, not adopted)':34s} "
        f"{TEAM_LEAD_REPORT['letter']:8d} {TEAM_LEAD_REPORT['mark']:8d} "
        f"{TEAM_LEAD_REPORT['ratio']:7.3f}   on {TEAM_LEAD_REPORT['pairs']} pairs")
    l0 = ladder["L0_strip_marks_only"]
    log(f"\n  L0 vs team lead: letter {l0['letter']} vs {TEAM_LEAD_REPORT['letter']} "
        f"({abs(l0['letter']-TEAM_LEAD_REPORT['letter'])/TEAM_LEAD_REPORT['letter']:.2%} apart); "
        f"ratio {l0['ratio']:.3f} vs {TEAM_LEAD_REPORT['ratio']:.3f}")

    log("\n=== AL-SUYUTI ANCHOR — every line below was opened and read ===")
    L = open(os.path.join(ROOT, ITQAN), encoding="utf-8").read().splitlines()
    anchor = {}
    for n, what in sorted(ANCHOR_LINES.items()):
        anchor[n] = {"note": what, "text": L[n - 1]}
        log(f"  {n:6d}  {what}")
        log(f"          {L[n-1][:120]}")

    out = {"id": "H-NEW-3100-RECONCILIATION", "run": stamp, "type": "DESCRIPTIVE",
           "verdict": None,
           "input_sha256": {k: sha256(k) for k in
                            ["data/alt-text/quran-uthmani-txt.txt",
                             "data/alt-text/quran-simple-txt.txt", ITQAN,
                             "scripts/arabic_normaliser.py", "scripts/h-new-3100.py"]},
           "pair_accounting": {"uthmani_tokens": n_uth, "pairs": len(pairs),
                               "merge_sites": n_merge,
                               "identity_holds": len(pairs) + n_merge == n_uth,
                               "team_lead_pairs": TEAM_LEAD_REPORT["pairs"],
                               "team_lead_unpaired": n_uth - TEAM_LEAD_REPORT["pairs"] - n_merge},
           "ratio_ladder": ladder, "team_lead_report": TEAM_LEAD_REPORT,
           "suyuti_anchor": anchor, "type_to_qaida": TYPE_TO_QAIDA}
    with open(os.path.join(rundir, "result.json"), "x", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "run.log"), "x", encoding="utf-8") as fh:
        fh.write("\n".join(log_lines) + "\n")
    log(f"\nartefacts -> runs/h-new-3100-reconciliation/{stamp}/")


if __name__ == "__main__":
    main()
