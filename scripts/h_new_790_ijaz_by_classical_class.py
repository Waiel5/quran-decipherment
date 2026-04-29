#!/usr/bin/env python3
"""H-NEW-790: Per-classical-class iʿjāz-signature comparison."""
import hashlib
import json
import math
import random
from itertools import combinations
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
H_NEW_730 = ROOT / "findings/phase-b-hypotheses/csv/h-new-730.json"
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG = ROOT / "findings/phase-b-hypotheses/h-new-790-ijaz-by-classical-class-prereg.md"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-790.json"
SEED = 20260447
N_PERMS = 10000

# Classical attributes
MUQATTAAT = {2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68}
MUFASSAL_QISAR = set(range(78, 115))
TIWAL = set(range(1, 10))
PROPHET_NAMED = {10, 11, 12, 14, 19, 47, 71}  # Yūnus, Hūd, Yūsuf, Ibrāhīm, Maryam, Muḥammad, Nūḥ


def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()


def load_meccan_medinan():
    """Load Meccan/Medinan classification from quran-no-tashkeel.json."""
    with open(QURAN_JSON) as f:
        q = json.load(f)
    return {s["id"]: s["type"] for s in q}


def welch_t(a, b):
    """Welch's t-test approximate, return t and df."""
    na, nb = len(a), len(b)
    ma, mb = sum(a)/na, sum(b)/nb
    va = sum((x-ma)**2 for x in a)/(na-1) if na > 1 else 0
    vb = sum((x-mb)**2 for x in b)/(nb-1) if nb > 1 else 0
    se = math.sqrt(va/na + vb/nb) if (va/na + vb/nb) > 0 else 1e-9
    t = (ma - mb)/se
    return t, ma, mb


def per_surah_ijaz_signature(per_window_iʿjāz, K=15):
    """Map per-window (start s) iʿjāz back to per-surah by averaging windows containing the surah."""
    per_surah = {}
    counts = {}
    for s_start in range(1, len(per_window_iʿjāz) + 1):
        sig = per_window_iʿjāz[s_start - 1]
        for surah in range(s_start, s_start + K):
            per_surah[surah] = per_surah.get(surah, 0.0) + sig
            counts[surah] = counts.get(surah, 0) + 1
    for surah in per_surah:
        per_surah[surah] /= counts[surah]
    return per_surah


def main():
    prereg_sha = sha(PREREG)
    print(f"=== H-NEW-790 (iʿjāz by classical class) ===")
    print(f"Pre-reg SHA: {prereg_sha}\nSeed: {SEED}\n")

    # Load iʿjāz signature from H-NEW-730
    with open(H_NEW_730) as f:
        h730 = json.load(f)
    per_window_sig = h730["iʿjāz_signature"]
    K = h730["K"]
    print(f"Loaded N={len(per_window_sig)} per-window iʿjāz signatures (K={K})")

    # Map to per-surah
    sig_per_surah = per_surah_ijaz_signature(per_window_sig, K=K)
    print(f"Mapped to per-surah for {len(sig_per_surah)} surahs (range {min(sig_per_surah.keys())}-{max(sig_per_surah.keys())})\n")

    # Load Meccan/Medinan
    mm = load_meccan_medinan()

    # Build group lists
    meccan = [sig_per_surah[s] for s in sig_per_surah if mm.get(s) == "meccan"]
    medinan = [sig_per_surah[s] for s in sig_per_surah if mm.get(s) == "medinan"]

    muq = [sig_per_surah[s] for s in sig_per_surah if s in MUQATTAAT]
    nonmuq = [sig_per_surah[s] for s in sig_per_surah if s not in MUQATTAAT]

    qisar = [sig_per_surah[s] for s in sig_per_surah if s in MUFASSAL_QISAR]
    tiwal = [sig_per_surah[s] for s in sig_per_surah if s in TIWAL]

    prophet = [sig_per_surah[s] for s in sig_per_surah if s in PROPHET_NAMED]
    nonprophet = [sig_per_surah[s] for s in sig_per_surah if s not in PROPHET_NAMED]

    tests = [
        ("Meccan vs Medinan", meccan, medinan),
        ("Muqaṭṭaʿāt vs Non-muq", muq, nonmuq),
        ("Mufaṣṣal-qiṣār Q 78-114 vs Ṭiwāl Q 1-9", qisar, tiwal),
        ("Prophet-named vs not", prophet, nonprophet),
    ]

    results = []
    for label, a, b in tests:
        t, ma, mb = welch_t(a, b)
        # Permutation null on group-mean difference
        all_vals = a + b
        rng = random.Random(SEED)
        observed_diff = ma - mb
        n_a = len(a)
        below = 0
        for _ in range(N_PERMS):
            shuffled = all_vals[:]
            rng.shuffle(shuffled)
            perm_a = shuffled[:n_a]; perm_b = shuffled[n_a:]
            perm_diff = sum(perm_a)/len(perm_a) - sum(perm_b)/len(perm_b)
            if abs(perm_diff) >= abs(observed_diff):
                below += 1
        p_emp = below / N_PERMS
        print(f"--- {label} ---")
        print(f"  N(a)={len(a)}, mean(a)={ma:+.4f}; N(b)={len(b)}, mean(b)={mb:+.4f}")
        print(f"  Δ = {observed_diff:+.4f}, t={t:+.3f}, p_perm={p_emp:.5f}")
        results.append({"label": label, "n_a": len(a), "n_b": len(b), "mean_a": ma, "mean_b": mb,
                        "diff": observed_diff, "t": t, "p_perm": p_emp})
        print()

    # Verdict
    alpha_bon = 0.05 / 4
    n_strict = sum(1 for r in results if r["p_perm"] <= alpha_bon)
    n_directional = sum(1 for r in results if r["p_perm"] <= 0.05)
    if n_strict >= 3:
        verdict = f"STRICT PASS — {n_strict}/4 tests significant at Bonferroni-4 α={alpha_bon:.4f}"
    elif n_directional >= 2:
        verdict = f"DIRECTIONAL — {n_directional}/4 tests significant at α=0.05"
    else:
        verdict = f"NULL — only {n_strict} strict, {n_directional} directional out of 4"
    print(f"=== VERDICT: {verdict} ===")

    out = {
        "id": "H-NEW-790",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "tests": results,
        "verdict": verdict,
        "alpha_bon": alpha_bon,
    }
    with open(OUT_JSON, "w") as f:
        json.dump(out, f, indent=2)
    print(f"\nWrote {OUT_JSON}")


if __name__ == "__main__":
    main()
