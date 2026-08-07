#!/usr/bin/env python3
"""
H-NEW-2650 companion — decomposition of every discarded post-verb clitic into
  (a) legitimate subject markers, and
  (b) genuine-object false negatives,
per verb form, plus an EXHAUSTIVE hand-inspection listing of all Form VI and Form VII clitics.

The (b)-rate per form is the quantity that decides whether the attached-object-pronoun channel
can carry H-NEW-2540 §2b and H-NEW-2600 §5. Forms VI and VII discard 100% of their post-verb
clitics under the original rule; every one of those is listed here individually with its verse
so the 100% can be checked by eye rather than trusted.

Classification is by RULE-NEW (pre-reg §4), imported from h-new-2650.py. Note that the
classifier NEVER sees the verb's derivational form, so it cannot introduce a form-correlated
bias by construction.

Writes to an ADDITIONAL run directory. No existing run directory is modified or deleted.

Author: Waiel Al-Shujaa.
"""

import collections
import datetime
import importlib.util
import json
import os

ROOT = "/Users/grey/Downloads/quran"
spec = importlib.util.spec_from_file_location(
    "h2650", os.path.join(ROOT, "findings/phase-b-hypotheses/scripts/h-new-2650.py"))
H = importlib.util.module_from_spec(spec)
spec.loader.exec_module(H)

ALL_FORMS = ["I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX", "X", "XI", "XII"]
INSPECT = ["VI", "VII"]


def main():
    verbs = H.load_verbs()
    quran = json.load(open(os.path.join(ROOT, "quran-text/quran-no-tashkeel.json"), encoding="utf-8"))
    vtext = {(s["id"], v["id"]): v["text"] for s in quran for v in s["verses"]}

    decomposition, tot_a, tot_b = {}, 0, 0
    for F in ALL_FORMS:
        pool = [v for v in verbs if v["form"] == F and not v["passive"]]
        if not pool:
            continue
        with_clitic = [v for v in pool if v["clitics"]]
        old = {v["loc"] for v in with_clitic if H.rule_old(v)}
        new = {v["loc"] for v in with_clitic if H.rule_new(v)}
        discards = len(with_clitic) - len(old)
        b = len(new - old)
        a = discards - b
        tot_a += a
        tot_b += b
        decomposition[F] = {
            "verbs": len(pool), "with_post_verb_clitic": len(with_clitic),
            "counted_by_rule_old": len(old), "discarded_by_rule_old": discards,
            "a_legitimate_subject_markers": a, "b_genuine_object_false_negatives": b,
            "b_rate_of_discards": b / discards if discards else None,
            "b_rate_of_rule_new_objects": b / len(new) if new else None,
            "false_positives_of_rule_old": len(old - new),
        }

    inspection = {}
    for F in INSPECT:
        rows = sorted([v for v in verbs if v["form"] == F and not v["passive"] and v["clitics"]],
                      key=lambda x: x["loc"])
        listed = []
        for v in rows:
            s, cl = 0, []
            for c in v["clitics"]:
                if c["kind"] != "SUFFIX":
                    continue
                verdict, rule = H.classify_clitic(c["surface"], c["pgn"], s, v["agr"], v["aspect"])
                cl.append({"surface": c["surface"], "pgn": c["pgn"],
                           "classification": verdict, "rule": rule})
                s += 1
            is_obj = any(c["classification"] == "OBJECT" for c in cl)
            listed.append({"loc": v["loc"], "verb_surface": v["surface"], "root": v["root"],
                           "agr": v["agr"], "aspect": v["aspect"], "clitics": cl,
                           "object_bearing": is_obj,
                           "verse_text": vtext.get((v["surah"], v["verse"]), "")})
        inspection[F] = {
            "n_verbs_with_clitic": len(rows),
            "n_object_bearing": sum(1 for r in listed if r["object_bearing"]),
            "all_rows": listed,
        }

    ts = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    rundir = os.path.join(ROOT, "findings/phase-b-hypotheses/runs/h-new-2650", ts)
    os.makedirs(rundir, exist_ok=False)
    out = {
        "finding_id": "H-NEW-2650",
        "artifact": "discard decomposition (a)/(b) + exhaustive Form VI/VII inspection",
        "prereg_sha256": H.PREREG_SHA,
        "eqtb_used": False,
        "note": "The RULE-NEW classifier does not take verb form as an input and therefore "
                "cannot introduce a form-correlated bias by construction.",
        "decomposition_by_form": decomposition,
        "corpus_total": {"a_legitimate_subject_markers": tot_a,
                         "b_genuine_object_false_negatives": tot_b,
                         "b_rate_of_all_discards": tot_b / (tot_a + tot_b)},
        "exhaustive_inspection": inspection,
    }
    with open(os.path.join(rundir, "discard-decomposition.json"), "x", encoding="utf-8") as fh:
        json.dump(out, fh, ensure_ascii=False, indent=1)
    with open(os.path.join(rundir, "manifest.json"), "x", encoding="utf-8") as fh:
        json.dump({"finding_id": "H-NEW-2650", "utc": ts,
                   "artifact": "discard-decomposition",
                   "script": "findings/phase-b-hypotheses/scripts/h-new-2650-discard-decomposition.py",
                   "prereg_sha256": H.PREREG_SHA,
                   "frozen_inputs": {k: {"path": os.path.relpath(v[0], ROOT), "sha256": v[1]}
                                     for k, v in H.FROZEN.items()},
                   "eqtb_used": False,
                   "supersedes_nothing": True,
                   "outputs": ["discard-decomposition.json"]}, fh, ensure_ascii=False, indent=1)

    print(f"{'form':<6}{'disc':>7}{'(a) subj':>10}{'(b) OBJ':>9}{'(b)/disc':>10}{'FP':>5}")
    for F, d in decomposition.items():
        br = "n/a" if d["b_rate_of_discards"] is None else f"{d['b_rate_of_discards']:.4f}"
        print(f"{F:<6}{d['discarded_by_rule_old']:>7}{d['a_legitimate_subject_markers']:>10}"
              f"{d['b_genuine_object_false_negatives']:>9}{br:>10}{d['false_positives_of_rule_old']:>5}")
    print(f"\nCORPUS: (a)={tot_a}  (b)={tot_b}  (b)/discards={tot_b/(tot_a+tot_b):.4f}")
    for F in INSPECT:
        i = inspection[F]
        print(f"Form {F}: {i['n_verbs_with_clitic']} clitic-bearing verbs, "
              f"{i['n_object_bearing']} object-bearing")
        for r in i["all_rows"]:
            if r["object_bearing"]:
                print(f"   OBJECT: {r['loc']} {r['verb_surface']} root={r['root']} — {r['verse_text']}")
    print(f"\n[run] {rundir}")


if __name__ == "__main__":
    main()
