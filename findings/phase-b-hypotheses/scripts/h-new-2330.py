#!/usr/bin/env python3
"""
H-NEW-2330 — Lexical burstiness / topical clumping of Quranic roots.
Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2330-lexical-burstiness.md
Direction LOCKED: L_obs > L_null (more single-surah bursts than random allocation).
Seed 20260509, 10000 simulations. Rules-tuple: QAC root v0.4, root-bearing tokens only.
Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os, statistics

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2330-lexical-burstiness.md")
EXPECTED_SHA = "7463c7e4821e0f6516892310527324b7de1d2cc65a43cf3c4a40700162b0d645"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
SEED, NSIM = 20260509, 10000
BURST_MIN_FREQ = 3

with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
name = {s["id"]: s["name"] for s in quran}

loc_re = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
root_re = re.compile(r"ROOT:([^|]+)")

# per-root -> {surah: count}; per-surah total root-tokens
root_surah = {}
surah_tokens = {i: 0 for i in range(1, 115)}
with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        m = loc_re.match(p[0]); rm = root_re.search(p[3])
        if not m or not rm:
            continue
        s = int(m.group(1)); rt = rm.group(1).strip()
        surah_tokens[s] += 1
        root_surah.setdefault(rt, {}).setdefault(s, 0)
        root_surah[rt][s] += 1

N = sum(surah_tokens.values())
roots = list(root_surah)
freq = {r: sum(d.values()) for r, d in root_surah.items()}
spread = {r: len(d) for r, d in root_surah.items()}   # distinct surahs

# Observed: roots with freq>=3 confined to exactly 1 surah
burst_roots = [r for r in roots if freq[r] >= BURST_MIN_FREQ and spread[r] == 1]
L_obs = len(burst_roots)

# Null: multinomial allocation per root by surah size, count freq>=3 roots in 1 surah
surah_ids = list(range(1, 115))
weights = [surah_tokens[i] for i in surah_ids]
total_w = sum(weights)
probs = [w / total_w for w in weights]
# cumulative for sampling
import bisect
cum = []
acc = 0.0
for pr in probs:
    acc += pr
    cum.append(acc)

rng = random.Random(SEED)
freq_ge3 = [freq[r] for r in roots if freq[r] >= BURST_MIN_FREQ]
ge = 0
sims = []
for _ in range(NSIM):
    L = 0
    for f_ in freq_ge3:
        # allocate f_ tokens; track distinct surahs hit (early-exit once >=2)
        hit = set()
        for _t in range(f_):
            x = rng.random()
            idx = bisect.bisect_left(cum, x)
            hit.add(idx)
            if len(hit) >= 2:
                break
        if len(hit) == 1:
            L += 1
    sims.append(L)
    if L >= L_obs:
        ge += 1
p_one = (ge + 1) / (NSIM + 1)
L_null = statistics.mean(sims)

verdict = "CONFIRMED" if (L_obs > L_null and p_one < 0.05) else (
    "NULL-REVERSED" if L_obs < L_null else "NULL")

# secondary
spine = sorted([(r, spread[r], freq[r]) for r in roots if spread[r] >= 90], key=lambda x: -x[1])
extreme_bursts = sorted([(r, freq[r], list(root_surah[r])[0]) for r in burst_roots],
                        key=lambda x: -x[1])[:15]
mecc_b = sum(1 for r in burst_roots if region[list(root_surah[r])[0]] == "meccan")
med_b = len(burst_roots) - mecc_b

out = {
    "finding": "H-NEW-2330", "prereg_sha256": actual, "seed": SEED, "nsim": NSIM,
    "burst_min_freq": BURST_MIN_FREQ,
    "corpus": {"root_tokens": N, "distinct_roots": len(roots),
               "roots_freq_ge3": len(freq_ge3)},
    "primary": {"L_obs": L_obs, "L_null_mean": round(L_null, 2),
                "p_one_sided": round(p_one, 6),
                "direction_locked": "L_obs > L_null", "verdict": verdict},
    "secondary": {
        "spine_roots_ge90_surahs": [{"root": r, "surahs": sp, "freq": fr} for r, sp, fr in spine],
        "extreme_single_surah_bursts": [
            {"root": r, "freq": fr, "surah": s, "name": name[s], "region": region[s]}
            for r, fr, s in extreme_bursts],
        "burst_region_split": {"meccan": mecc_b, "medinan": med_b,
                               "meccan_fraction": round(mecc_b / len(burst_roots), 3)},
    },
}
json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2330.json"), "w"),
          ensure_ascii=False, indent=2)
print(json.dumps(out["primary"], indent=2))
print("spine (>=90 surahs):", [(r, sp) for r, sp, _ in spine])
print("extreme bursts:", [(r, fr, name[s]) for r, fr, s in extreme_bursts[:8]])
print("burst region split:", out["secondary"]["burst_region_split"])
print(f"[VERDICT] {verdict}")
