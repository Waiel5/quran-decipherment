"""
Q071-F-02 — 5 named pre-Islamic deities at Q 71:23 corpus-EXACT singleton test.

Locked pre-reg: ../preregs/Q071-F-02-five-deities-corpus-exact-prereg.md
Seed: 20260509

Method: enumerate every verse in the 6,236-verse corpus containing each of the
5 deity-name orthographic forms; verify 4 of 5 are corpus-strict-singletons and
co-locate at Q 71:23.
"""

import json
import hashlib
import re
from pathlib import Path


WAQF_MARKS_RE = re.compile(r'[ۚۖۛۗۘ]')  # ۚۖۛۗۘ


def normalize_text(s: str) -> str:
    """Strip waqf-marks from no-tashkeel text."""
    return WAQF_MARKS_RE.sub('', s).strip()


def main():
    repo = Path("/Users/grey/Downloads/quran")
    quran_path = repo / "quran-text/quran-no-tashkeel.json"
    prereg = repo / "surahs/Q071-nuh/preregs/Q071-F-02-five-deities-corpus-exact-prereg.md"

    sha = hashlib.sha256(prereg.read_bytes()).hexdigest()
    print(f"Pre-reg SHA-256: {sha}")

    with quran_path.open() as f:
        q = json.load(f)

    # 5 deity-names at Q 71:23
    # Orthographic forms (no-tashkeel) as they appear in the verse:
    # وقالوا لا تذرن آلهتكم ولا تذرن ودا ولا سواعا ولا يغوث ويعوق ونسرا
    deity_forms = {
        "Wadd": "ودا",
        "Suwāʿ": "سواعا",
        "Yaghūth": "يغوث",
        "Yaʿūq": "ويعوق",
        "Nasr": "ونسرا",
    }

    # Locate every occurrence by exact-token match
    location_map = {name: [] for name in deity_forms}
    for s in q:
        sid = s["id"]
        for v in s["verses"]:
            text = normalize_text(v["text"])
            tokens = text.split()
            for name, form in deity_forms.items():
                if form in tokens:
                    location_map[name].append((sid, v["id"]))

    print("\nDeity orthographic-form locations:")
    strict_singletons = []
    for name, locs in location_map.items():
        unique = (len(locs) == 1)
        only_in_q71_23 = (locs == [(71, 23)])
        print(f"  {name:10s} ({deity_forms[name]:6s}): {locs}  "
              f"[singleton={unique}, at_Q71:23={only_in_q71_23}]")
        if unique and only_in_q71_23:
            strict_singletons.append(name)

    print(f"\nCorpus-strict-singletons co-located at Q 71:23: {len(strict_singletons)} / 5")
    print(f"  → {strict_singletons}")

    # Joint-probability under uniform-singleton-placement H0
    # Probability that 4 specific singletons all land in 1 of 6,236 verses:
    n_verses = 6236
    p_joint = 1 / (n_verses ** 3)
    print(f"\nJoint-probability under uniform-singleton-placement H0:")
    print(f"  P(4 specific corpus-strict-singletons all in same verse) = 1 / {n_verses}^3")
    print(f"                                                          = {p_joint:.3e}")

    # Acceptance window
    pass_directed = (len(strict_singletons) >= 4)
    pass_directed_strong = pass_directed and all(
        location_map[n] == [(71, 23)] for n in strict_singletons
    )

    print(f"\nAcceptance window (pre-reg locked):")
    print(f"  ≥ 4 strict-singletons: {pass_directed}")
    print(f"  ALL co-located at Q 71:23: {pass_directed_strong}")
    if pass_directed_strong:
        verdict = "PASS-DIRECTED-STRONG"
    elif pass_directed:
        verdict = "PASS-DIRECTED"
    else:
        verdict = "NULL"
    print(f"  VERDICT: {verdict}")

    out = {
        "finding_id": "Q071-F-02",
        "prereg_sha256": sha,
        "seed": 20260509,
        "rules_tuple": "(hafs-kufan; no-tashkeel; orthographic-token-form match; basmala-counted-only-in-Q1)",
        "deity_forms": deity_forms,
        "location_map": {k: [list(loc) for loc in v] for k, v in location_map.items()},
        "strict_singletons_at_Q71_23": strict_singletons,
        "n_strict_singletons": len(strict_singletons),
        "p_joint_uniform_singleton_H0": p_joint,
        "verdict": verdict,
        "honest_disclosure": (
            "Wadd 'ودا' is NOT corpus-strict-singleton at orthographic level "
            "(also at Q 19:96 with the lexical sense 'love/affection'); "
            "Wadd is CONTEXTUAL-SINGLETON-DEITY only. "
            "The 4 strict singletons (Suwāʿ, Yaghūth, Yaʿūq, Nasr) all co-locate at Q 71:23."
        ),
    }

    out_path = repo / "surahs/Q071-nuh/csv/Q071-F-02.json"
    out_path.parent.mkdir(parents=True, exist_ok=True)
    out_path.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\nResult written to {out_path}")

    return out


if __name__ == "__main__":
    main()
