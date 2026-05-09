#!/usr/bin/env python3
"""Q039-F-04 — Q 39 corpus-UNIQUE self-ring (tanzīl-opener + hamd-closer + rabb-al-ʿālamīn echo).

Pre-reg: surahs/Q039-al-zumar/preregs/Q039-F-04-self-ring-cohesion-prereg.md
Pre-reg SHA: fe370b2edecfb818cc18ad6a13f3bd79f1a8b3455fccb5838b8e1b037ca17d81
Seed: 20260509  |  α_bon: 0.0125
"""

import hashlib
import json
import re
import sys
from pathlib import Path

import numpy as np

PROJECT_ROOT = Path(__file__).resolve().parents[3]
PREREG_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "preregs" / "Q039-F-04-self-ring-cohesion-prereg.md"
EXPECTED_SHA = "fe370b2edecfb818cc18ad6a13f3bd79f1a8b3455fccb5838b8e1b037ca17d81"
OUT_PATH = PROJECT_ROOT / "surahs" / "Q039-al-zumar" / "csv" / "Q039-F-04.json"
QURAN_JSON = PROJECT_ROOT / "quran-text" / "quran-no-tashkeel.json"

SEED = 20260509
N_PERM = 10_000
ALPHA_BON = 0.0125

TANZIL_CLUSTER = [32, 39, 40, 41, 45, 46]
HAMD_CLOSE_CLUSTER = [17, 27, 37, 39]

WAQF_MARKS = set("ۚۖۗۘۙۛۜ۞")


def verify_prereg_sha() -> str:
    sha = hashlib.sha256(PREREG_PATH.read_bytes()).hexdigest()
    if sha != EXPECTED_SHA:
        sys.stderr.write(
            f"PRE-REG SHA MISMATCH\n  expected: {EXPECTED_SHA}\n  found:    {sha}\n"
        )
        sys.exit(1)
    return sha


def clean(text: str) -> str:
    return "".join(
        c for c in text if not (0x064B <= ord(c) <= 0x065F) and c not in WAQF_MARKS
    )


def main() -> None:
    sha = verify_prereg_sha()
    print(f"[OK] pre-reg SHA verified: {sha[:16]}...")

    with QURAN_JSON.open(encoding="utf-8") as f:
        quran = json.load(f)

    last_verse_text = {}
    last_verse_id = {}
    for entry in quran:
        sid = entry["id"]
        last = entry["verses"][-1]
        last_verse_text[sid] = clean(last["text"])
        last_verse_id[sid] = last["id"]

    # H1, H2: set-membership intersection significance
    obs_intersect = set(TANZIL_CLUSTER) & set(HAMD_CLOSE_CLUSTER)
    print(f"[INFO] tanzīl ∩ hamd-closer = {sorted(obs_intersect)} (size {len(obs_intersect)})")

    rng = np.random.default_rng(SEED)
    surah_ids = list(range(1, 115))

    # H1: hold tanzīl fixed, randomize hamd-closer set (size 4)
    null_intersections_h1 = np.empty(N_PERM, dtype=int)
    for i in range(N_PERM):
        h_random = rng.choice(surah_ids, size=4, replace=False)
        null_intersections_h1[i] = len(set(TANZIL_CLUSTER) & set(int(x) for x in h_random))
    p_h1_at_least_1 = float(np.mean(null_intersections_h1 >= 1))

    # H2: hold hamd-closer fixed, randomize tanzīl set (size 6)
    null_intersections_h2 = np.empty(N_PERM, dtype=int)
    for i in range(N_PERM):
        t_random = rng.choice(surah_ids, size=6, replace=False)
        null_intersections_h2[i] = len(set(HAMD_CLOSE_CLUSTER) & set(int(x) for x in t_random))
    p_h2_at_least_1 = float(np.mean(null_intersections_h2 >= 1))

    h1_pass = p_h1_at_least_1 <= ALPHA_BON
    h2_pass = p_h2_at_least_1 <= ALPHA_BON

    # H3: rabb-al-ʿālamīn closer cluster
    RBA = "رب العالمين"
    rab_alamin_closer = []
    for sid in range(1, 115):
        text = last_verse_text[sid]
        # Take final 4 words for robustness
        words = text.split()
        tail = " ".join(words[-3:]) if len(words) >= 3 else text
        if RBA in tail:
            rab_alamin_closer.append(sid)

    print(f"[INFO] rabb-al-ʿālamīn closer cluster: {rab_alamin_closer} (size {len(rab_alamin_closer)})")
    n_rba = len(rab_alamin_closer)

    # H3 perm: under null where the "tail-3-words" of each surah is replaced by a random verse
    # within the same surah, what fraction of surahs end with rabb-al-ʿālamīn?
    null_rba_counts = np.empty(N_PERM, dtype=int)
    rng2 = np.random.default_rng(SEED + 1)
    # Build per-surah list of all verse-tail-3-word strings
    per_surah_tails = {}
    for entry in quran:
        sid = entry["id"]
        tails = []
        for v in entry["verses"]:
            txt = clean(v["text"])
            words = txt.split()
            tail = " ".join(words[-3:]) if len(words) >= 3 else txt
            tails.append(tail)
        per_surah_tails[sid] = tails
    for i in range(N_PERM):
        cnt = 0
        for sid in range(1, 115):
            tails = per_surah_tails[sid]
            t = tails[rng2.integers(0, len(tails))]
            if RBA in t:
                cnt += 1
        null_rba_counts[i] = cnt
    p_h3 = float(np.mean(null_rba_counts >= n_rba))
    h3_pass = p_h3 <= ALPHA_BON

    # H4 (informal exploration): Q 39 specifically — corpus-unique tanzīl-opener + rabb-al-ʿālamīn-closer
    self_ring_set = set(TANZIL_CLUSTER) & set(rab_alamin_closer)
    print(f"[INFO] tanzīl ∩ rabb-al-ʿālamīn-closer = {sorted(self_ring_set)}")
    q39_in_self_ring = 39 in self_ring_set
    self_ring_size = len(self_ring_set)

    if h1_pass and h2_pass and h3_pass:
        verdict = "CONFIRMED-DIRECTED"
    elif h1_pass or h2_pass or h3_pass:
        verdict = "PASS-DIRECTED"
    else:
        verdict = "NULL"

    print(f"\n[RESULT] H1 (random hamd-closer hits tanzīl ≥ 1): p = {p_h1_at_least_1:.4f}  → {'PASS' if h1_pass else 'FAIL'}")
    print(f"[RESULT] H2 (random tanzīl hits hamd-closer ≥ 1): p = {p_h2_at_least_1:.4f}  → {'PASS' if h2_pass else 'FAIL'}")
    print(f"[RESULT] H3 (rabb-al-ʿālamīn closer cluster of size {n_rba} unlikely under null): p = {p_h3:.4f}  → {'PASS' if h3_pass else 'FAIL'}")
    print(f"[VERDICT] {verdict}")
    print(f"[INFO] Q 39 in tanzīl ∩ rabb-al-ʿālamīn-closer: {q39_in_self_ring}, ring-size = {self_ring_size}")

    out = {
        "id": "Q039-F-04",
        "h_new_id": "H-NEW-1300",
        "title": "Q 39 self-ring composition (tanzīl-opener + hamd-closer)",
        "prereg_path": str(PREREG_PATH.relative_to(PROJECT_ROOT)),
        "prereg_sha": EXPECTED_SHA,
        "prereg_sha_verified": sha,
        "seed": SEED,
        "n_perm": N_PERM,
        "alpha_bon": ALPHA_BON,
        "bonferroni_k": 4,
        "bonferroni_family": "Q039-novel-tests",
        "tanzil_cluster": TANZIL_CLUSTER,
        "hamd_close_cluster": HAMD_CLOSE_CLUSTER,
        "observed_intersection": sorted(obs_intersect),
        "observed_intersection_size": len(obs_intersect),
        "h1_p_random_hamd_hits_tanzil_at_least_1": p_h1_at_least_1,
        "h2_p_random_tanzil_hits_hamd_at_least_1": p_h2_at_least_1,
        "h1_pass": h1_pass,
        "h2_pass": h2_pass,
        "rabb_alamin_closer_set": rab_alamin_closer,
        "rabb_alamin_closer_count": n_rba,
        "h3_p_rba_closer_size": p_h3,
        "h3_null_mean": float(null_rba_counts.mean()),
        "h3_null_q975": float(np.quantile(null_rba_counts, 0.975)),
        "h3_pass": h3_pass,
        "tanzil_intersect_rba_closer": sorted(self_ring_set),
        "q39_self_ring_member": q39_in_self_ring,
        "self_ring_size": self_ring_size,
        "verdict": verdict,
        "verdict_ceiling": "PASS-DIRECTED",
        "rules_tuple": [
            "no-tashkeel",
            "orthographic-token",
            "graphemes",
            "basmala-counted-only-in-Q1",
            "Hafs-Kufan",
        ],
    }
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False))
    print(f"\n[OK] wrote {OUT_PATH.relative_to(PROJECT_ROOT)}")


if __name__ == "__main__":
    main()
