#!/usr/bin/env python3
"""
H-NEW-237 — Numerical-residual consolidation after Benford PASS (H-NEW-175).

Pre-registered at:
  findings/phase-b-hypotheses/h-new-237-numerical-residuals-prereg.md

Three cells:
  A. Prime density of the 114 per-surah verse-counts vs uniform-range null.
  B. Cumulative letter-count prefix sums — do any hit distinguished constants
     {pi, e, phi, pi^2, e^2, phi^2, pi*e, pi*phi, e*phi, pi*e*phi} x 10^n
     within relative tolerance 0.001? Null = permutation of per-surah L.
  C. 114 surah-name abjad sum (mashriqi AND maghribi). Null = fake 114 names
     drawn from corpus-wide letter-frequency with matched name-length vector.

Rules tuple: (no-tashkeel, hafs-kufan graphemes, seed 20260419).
Bonferroni: k = 3 local, alpha_bon = 0.0167.

Outputs:
  findings/phase-b-hypotheses/csv/h-new-237.json
Writes to stderr a pre-reg SHA and per-cell summary.
"""
from __future__ import annotations

import hashlib
import json
import math
import random
import sys
from pathlib import Path

import numpy as np

ROOT = Path("/Users/grey/Downloads/quran")
sys.path.insert(0, str(ROOT))

from analysis.tools.gematria import text_value, ABJAD_MASHRIQI, ABJAD_MAGHRIBI  # noqa: E402


QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
PREREG_MD = ROOT / "findings/phase-b-hypotheses/h-new-237-numerical-residuals-prereg.md"
OUTPUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-237.json"

SEED = 20260419
BONFERRONI_K = 3
ALPHA_BON = 0.05 / BONFERRONI_K   # 0.01667

N_PERMS_A = 1000
N_PERMS_B = 2000
N_PERMS_C = 1000


# Arabic letter range matching gematria.py and methodology.md section 8:
# graphemes in U+0621..064A (28 core letters + hamza carriers) and U+0671 (alif wasla).
# For letter counting we match the tokenize.is_letter definition: any letter the
# gematria table recognises plus silent-skip carriers are counted as letters.
LETTER_CPS = set(range(0x0621, 0x064B)) | {0x0671} | {0x0670, 0x0649, 0x0629}


def is_arabic_letter(ch: str) -> bool:
    """Grapheme-count predicate per methodology.md section 8."""
    if not ch:
        return False
    return ord(ch[0]) in LETTER_CPS


def count_letters(text: str) -> int:
    return sum(1 for c in text if is_arabic_letter(c))


# ---------- primality ----------

def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n < 4:
        return True
    if n % 2 == 0:
        return False
    r = int(math.isqrt(n))
    for p in range(3, r + 1, 2):
        if n % p == 0:
            return False
    return True


# ---------- constant set for Cell B ----------

def build_constant_targets(v_min: int, v_max: int):
    """Build list of (name, value) distinguished constants x 10^n covering
    integer range [v_min, v_max]. All constants positive reals > 1."""
    phi = (1 + math.sqrt(5)) / 2
    base = {
        "pi": math.pi,
        "e": math.e,
        "phi": phi,
        "pi2": math.pi ** 2,
        "e2": math.e ** 2,
        "phi2": phi ** 2,
        "pi_e": math.pi * math.e,
        "pi_phi": math.pi * phi,
        "e_phi": math.e * phi,
        "pi_e_phi": math.pi * math.e * phi,
    }
    targets = []
    for name, c in base.items():
        for n in range(0, 7):
            val = c * (10 ** n)
            if v_min <= val <= v_max:
                targets.append((f"{name}_x_1e{n}", val))
    return targets


# ---------- Cell A ----------

def cell_a(V: list[int], rng: random.Random):
    k_observed = sum(1 for v in V if is_prime(v))
    v_min, v_max = min(V), max(V)
    N = len(V)

    # Uniform-range null: draw N integers uniform in [v_min, v_max].
    null_counts = []
    # Use a numpy RandomState for speed, seeded from SEED.
    rstate = np.random.default_rng(SEED + 1)
    for _ in range(N_PERMS_A):
        draws = rstate.integers(low=v_min, high=v_max + 1, size=N)
        null_counts.append(int(sum(1 for v in draws if is_prime(int(v)))))

    null_arr = np.array(null_counts)
    null_mean = float(null_arr.mean())
    null_sd = float(null_arr.std(ddof=1))

    # MW-5 cheat: shuffle V indices, prime count must be invariant.
    V_shuf = list(V)
    rng.shuffle(V_shuf)
    mw5_prime_count = sum(1 for v in V_shuf if is_prime(v))
    mw5_ok = (mw5_prime_count == k_observed)

    # Two-sided p-value: fraction of null at least as extreme.
    dev_obs = abs(k_observed - null_mean)
    p_raw = float((np.abs(null_arr - null_mean) >= dev_obs).mean())
    # Correct for lower bound: ceil to 1/(N+1).
    p_raw = max(p_raw, 1.0 / (N_PERMS_A + 1))

    return {
        "k_primes_observed": k_observed,
        "v_range": [v_min, v_max],
        "null_prime_count_mean": null_mean,
        "null_prime_count_sd": null_sd,
        "null_samples_N": N_PERMS_A,
        "p_raw_two_sided": p_raw,
        "p_bon_vs_k3": min(1.0, p_raw * BONFERRONI_K),
        "mw5_invariance_ok": mw5_ok,
        "verdict": "NULL" if p_raw > ALPHA_BON else "SURVIVES",
    }


# ---------- Cell B ----------

def cell_b(L: list[int], rng: random.Random):
    prefix = np.cumsum(np.asarray(L, dtype=np.int64))
    # For target-building, use the full prefix range (first prefix = L[0], last = total).
    targets = build_constant_targets(int(prefix[0]), int(prefix[-1]))
    eps_primary = 0.001
    eps_tight = 0.0001
    eps_loose = 0.005

    def count_hits(prefix_arr, targets_list, eps):
        hits = []
        for idx, p in enumerate(prefix_arr):
            for name, val in targets_list:
                rel = abs(p - val) / val
                if rel <= eps:
                    hits.append({
                        "k": int(idx + 1),
                        "prefix": int(p),
                        "target_name": name,
                        "target_value": float(val),
                        "rel_distance": float(rel),
                    })
        return hits

    def min_rel_distance(prefix_arr, targets_list):
        best = math.inf
        for p in prefix_arr:
            for _, val in targets_list:
                rel = abs(p - val) / val
                if rel < best:
                    best = rel
        return best

    observed_hits_primary = count_hits(prefix, targets, eps_primary)
    observed_hits_tight = count_hits(prefix, targets, eps_tight)
    observed_hits_loose = count_hits(prefix, targets, eps_loose)
    observed_min_rel = min_rel_distance(prefix, targets)

    # Permutation null: shuffle L, recompute prefix, recompute hit count + min_rel.
    rstate = np.random.default_rng(SEED + 2)
    L_arr = np.asarray(L, dtype=np.int64)
    null_hit_counts = []
    null_min_rels = []
    for _ in range(N_PERMS_B):
        perm = rstate.permutation(L_arr)
        pre = np.cumsum(perm)
        # Reuse same target list (built from observed prefix range — acceptable
        # because the final total L_1+...+L_114 is invariant to permutation).
        hc = 0
        best = math.inf
        for p in pre:
            for _, val in targets:
                rel = abs(p - val) / val
                if rel <= eps_primary:
                    hc += 1
                if rel < best:
                    best = rel
        null_hit_counts.append(hc)
        null_min_rels.append(best)

    null_hits_arr = np.array(null_hit_counts)
    null_minrel_arr = np.array(null_min_rels)

    # Upper-tail p for observed_hits_primary.
    p_hits_upper = float((null_hits_arr >= len(observed_hits_primary)).mean())
    p_hits_upper = max(p_hits_upper, 1.0 / (N_PERMS_B + 1))

    # Lower-tail p for observed_min_rel (smaller = more distinguished).
    p_minrel_lower = float((null_minrel_arr <= observed_min_rel).mean())
    p_minrel_lower = max(p_minrel_lower, 1.0 / (N_PERMS_B + 1))

    # MW-5 cheat: identity permutation.
    mw5_prefix = np.cumsum(L_arr)
    mw5_ok = bool(np.array_equal(mw5_prefix, prefix))

    # Primary statistic: n_hits upper-tail.
    primary_p = p_hits_upper
    verdict = "NULL" if primary_p > ALPHA_BON else "SURVIVES"

    return {
        "total_letters": int(prefix[-1]),
        "prefix_range": [int(prefix[0]), int(prefix[-1])],
        "num_targets": len(targets),
        "targets_sample": targets[:8],
        "observed_hits_primary_eps_0p001": len(observed_hits_primary),
        "observed_hits_tight_eps_0p0001": len(observed_hits_tight),
        "observed_hits_loose_eps_0p005": len(observed_hits_loose),
        "observed_min_rel_distance": observed_min_rel,
        "null_hits_mean": float(null_hits_arr.mean()),
        "null_hits_sd": float(null_hits_arr.std(ddof=1)),
        "null_minrel_mean": float(null_minrel_arr.mean()),
        "null_minrel_sd": float(null_minrel_arr.std(ddof=1)),
        "null_samples_N": N_PERMS_B,
        "p_raw_hits_upper": p_hits_upper,
        "p_raw_minrel_lower": p_minrel_lower,
        "p_bon_primary_vs_k3": min(1.0, primary_p * BONFERRONI_K),
        "primary_statistic": "n_hits_upper_tail",
        "observed_hits_details": observed_hits_primary,
        "mw5_invariance_ok": mw5_ok,
        "verdict": verdict,
    }


# ---------- Cell C ----------

def cell_c(surah_names: list[str], rng: random.Random,
           corpus_letter_freq: dict[str, float]):
    # Sum abjad under both tables.
    S_mashriqi = sum(text_value(n, "mashriqi") for n in surah_names)
    S_maghribi = sum(text_value(n, "maghribi") for n in surah_names)

    name_lengths = [count_letters(n) for n in surah_names]

    # Distinguished-integer set: returns set of known-distinguished integers
    # we would react to.
    distinguished = set()
    for k in range(1, 10000):
        if k % 19 == 0:
            distinguished.add(19 * k)   # Khalifa Code-19 targets
    distinguished.update({786, 114, 114 * 19, 114 ** 2, 19 ** 2, 19 * 114})
    distinguished.update({2 * 3 * 19 * k for k in range(1, 1000)})
    for C in [math.pi, math.e, (1 + math.sqrt(5)) / 2, math.pi * math.e,
              math.pi ** 2, math.e ** 2]:
        for n in range(0, 8):
            val = C * (10 ** n)
            for d in range(-2, 3):
                distinguished.add(int(round(val)) + d)
    distinguished.update({10 ** k for k in range(3, 8)})
    distinguished.update({100_000, 200_000, 500_000, 1_000_000})

    def near_distinguished(S: int, eps: float = 0.001):
        """Return any distinguished target within relative eps, or None."""
        if S in distinguished:
            return (S, 0.0, "exact_hit")
        for d in distinguished:
            if d == 0:
                continue
            rel = abs(S - d) / d
            if rel <= eps:
                return (d, rel, "close_hit")
        return None

    obs_mashriqi_dist = near_distinguished(S_mashriqi, 0.001)
    obs_maghribi_dist = near_distinguished(S_maghribi, 0.001)

    # Null-1: letter-bag permutation (MW-5 invariance check).
    all_letters = [c for name in surah_names for c in name if is_arabic_letter(c)]
    bag = list(all_letters)
    rng.shuffle(bag)
    fake_names = []
    pos = 0
    for L in name_lengths:
        fake_names.append("".join(bag[pos:pos + L]))
        pos += L
    null1_mashriqi = sum(text_value(n, "mashriqi") for n in fake_names)
    null1_maghribi = sum(text_value(n, "maghribi") for n in fake_names)
    null1_invariant_mashriqi = (null1_mashriqi == S_mashriqi)
    null1_invariant_maghribi = (null1_maghribi == S_maghribi)

    # Null-2: 1 000 draws of 114 fake names, per-name-length matched,
    # letters drawn IID from corpus letter-frequency distribution.
    letters = list(corpus_letter_freq.keys())
    weights = np.array([corpus_letter_freq[c] for c in letters])
    weights = weights / weights.sum()
    null_mashriqi = []
    null_maghribi = []
    rstate = np.random.default_rng(SEED + 3)
    for _ in range(N_PERMS_C):
        S_m = 0
        S_g = 0
        for L in name_lengths:
            if L == 0:
                continue
            draws_idx = rstate.choice(len(letters), size=L, p=weights)
            fake = "".join(letters[i] for i in draws_idx)
            S_m += text_value(fake, "mashriqi")
            S_g += text_value(fake, "maghribi")
        null_mashriqi.append(S_m)
        null_maghribi.append(S_g)
    null_m_arr = np.array(null_mashriqi)
    null_g_arr = np.array(null_maghribi)

    def two_sided_p(obs, null_arr):
        mean = null_arr.mean()
        dev = abs(obs - mean)
        return max(
            float((np.abs(null_arr - mean) >= dev).mean()),
            1.0 / (len(null_arr) + 1),
        )

    p_mashriqi = two_sided_p(S_mashriqi, null_m_arr)
    p_maghribi = two_sided_p(S_maghribi, null_g_arr)

    any_distinguished_hit = bool(obs_mashriqi_dist) or bool(obs_maghribi_dist)
    primary_p = min(p_mashriqi, p_maghribi)
    verdict = "NULL"
    if any_distinguished_hit and primary_p <= ALPHA_BON:
        verdict = "SURVIVES"
    elif any_distinguished_hit:
        verdict = "DISTINGUISHED_HIT_BUT_NOT_RARE"

    return {
        "S_mashriqi_observed": int(S_mashriqi),
        "S_maghribi_observed": int(S_maghribi),
        "distinguished_hit_mashriqi": obs_mashriqi_dist,
        "distinguished_hit_maghribi": obs_maghribi_dist,
        "null1_invariance_mashriqi": null1_invariant_mashriqi,
        "null1_invariance_maghribi": null1_invariant_maghribi,
        "null2_mashriqi_mean": float(null_m_arr.mean()),
        "null2_mashriqi_sd": float(null_m_arr.std(ddof=1)),
        "null2_maghribi_mean": float(null_g_arr.mean()),
        "null2_maghribi_sd": float(null_g_arr.std(ddof=1)),
        "null2_samples_N": N_PERMS_C,
        "p_raw_mashriqi_two_sided": p_mashriqi,
        "p_raw_maghribi_two_sided": p_maghribi,
        "primary_p": primary_p,
        "p_bon_primary_vs_k3": min(1.0, primary_p * BONFERRONI_K),
        "name_length_total": sum(name_lengths),
        "num_names": len(surah_names),
        "verdict": verdict,
    }


# ---------- helpers ----------

def load_corpus(path: Path):
    return json.loads(path.read_text(encoding="utf-8"))


def compute_letter_counts(data) -> list[int]:
    """Per-surah grapheme count. Includes basmala in surah 1 only, per rules
    tuple (basmala is verse 1 of Al-Fatihah in the JSON and the JSON does not
    prepend basmala to other surahs' verse 1 — matches counted-only-in-surah-1)."""
    L = []
    for s in data:
        total = sum(count_letters(v["text"]) for v in s["verses"])
        L.append(total)
    return L


def compute_verse_counts(data) -> list[int]:
    return [len(s["verses"]) for s in data]


def compute_corpus_letter_freq(data) -> dict[str, float]:
    from collections import Counter
    ct = Counter()
    for s in data:
        for v in s["verses"]:
            for c in v["text"]:
                if is_arabic_letter(c):
                    ct[c] += 1
    total = sum(ct.values())
    return {c: n / total for c, n in ct.items()}


def get_surah_names(data) -> list[str]:
    return [s["name"] for s in data]


def compute_prereg_sha() -> str:
    if not PREREG_MD.exists():
        return "PREREG_MISSING"
    return hashlib.sha256(PREREG_MD.read_bytes()).hexdigest()


# ---------- main ----------

def main():
    print(f"[H-NEW-237] SEED={SEED}  K={BONFERRONI_K}  alpha_bon={ALPHA_BON:.4f}",
          file=sys.stderr)
    prereg_sha = compute_prereg_sha()
    print(f"[H-NEW-237] pre-reg SHA-256 = {prereg_sha}", file=sys.stderr)

    data = load_corpus(QURAN_JSON)
    if len(data) != 114:
        raise RuntimeError(f"expected 114 surahs, got {len(data)}")

    V = compute_verse_counts(data)
    L = compute_letter_counts(data)
    names = get_surah_names(data)
    corpus_freq = compute_corpus_letter_freq(data)

    print(f"[H-NEW-237] total verses (sum V) = {sum(V)}", file=sys.stderr)
    print(f"[H-NEW-237] total letters (sum L) = {sum(L)}", file=sys.stderr)
    print(f"[H-NEW-237] num surah names = {len(names)}", file=sys.stderr)

    rng = random.Random(SEED)

    print(f"[H-NEW-237] running Cell A (prime density) ...", file=sys.stderr)
    result_A = cell_a(V, rng)

    print(f"[H-NEW-237] running Cell B (cumulative constants) ...", file=sys.stderr)
    result_B = cell_b(L, rng)

    print(f"[H-NEW-237] running Cell C (surah-name abjad) ...", file=sys.stderr)
    result_C = cell_c(names, rng, corpus_freq)

    output = {
        "id": "H-NEW-237",
        "parent": "H-NEW-175",
        "seed": SEED,
        "rules_tuple": {
            "orthography": "no-tashkeel",
            "letter_definition": "hafs-kufan graphemes",
            "word_definition": "orthographic-token real-words",
            "basmala_policy": "counted-only-in-surah-1",
            "abjad_tables": ["mashriqi", "maghribi"],
        },
        "bonferroni": {"k": BONFERRONI_K, "alpha_family": 0.05,
                       "alpha_bon": ALPHA_BON},
        "prereg_sha256": prereg_sha,
        "inputs": {
            "num_surahs": len(data),
            "sum_verses": sum(V),
            "sum_letters": sum(L),
            "V_min": min(V), "V_max": max(V),
            "L_min": min(L), "L_max": max(L),
        },
        "cell_A_prime_density": result_A,
        "cell_B_cumulative_constants": result_B,
        "cell_C_surah_name_abjad": result_C,
        "overall_verdicts": {
            "A": result_A["verdict"],
            "B": result_B["verdict"],
            "C": result_C["verdict"],
        },
    }

    OUTPUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_JSON.write_text(json.dumps(output, indent=2, ensure_ascii=False),
                           encoding="utf-8")
    print(f"[H-NEW-237] wrote {OUTPUT_JSON}", file=sys.stderr)

    print(f"\n[H-NEW-237] === SUMMARY ===", file=sys.stderr)
    print(f"  Cell A: {result_A['verdict']}  "
          f"(observed {result_A['k_primes_observed']} primes vs null mean "
          f"{result_A['null_prime_count_mean']:.1f}; p_raw={result_A['p_raw_two_sided']:.4f})",
          file=sys.stderr)
    print(f"  Cell B: {result_B['verdict']}  "
          f"(observed {result_B['observed_hits_primary_eps_0p001']} hits @ eps=0.001 "
          f"vs null mean {result_B['null_hits_mean']:.2f}; "
          f"p_raw_upper={result_B['p_raw_hits_upper']:.4f})",
          file=sys.stderr)
    print(f"  Cell C: {result_C['verdict']}  "
          f"(S_mashriqi={result_C['S_mashriqi_observed']}, "
          f"S_maghribi={result_C['S_maghribi_observed']}; "
          f"primary p_raw={result_C['primary_p']:.4f})",
          file=sys.stderr)


if __name__ == "__main__":
    main()
