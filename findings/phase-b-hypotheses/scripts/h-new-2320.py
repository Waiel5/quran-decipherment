#!/usr/bin/env python3
"""
H-NEW-2320 — Corpus-wide hapax-legomenon (singleton-root) census + Meccan-concentration test.
Pre-registered: findings/phase-b-hypotheses/prereg-h-new-2320-hapax-census.md
Direction LOCKED before computation: per-token hapax rate Meccan > Medinan.
Seed 20260509, 10000 permutations. Rules-tuple: QAC root v0.4, root-bearing tokens only.

Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os, statistics

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2320-hapax-census.md")
EXPECTED_SHA = "68f2446d3f3c362823094d12870b896500146d67e70edd8fcb8e206632b9eaa6"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
SEED = 20260509
NPERM = 10000

# --- runtime pre-reg integrity check ---
with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

# --- region map (meccan/medinan) ---
quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}   # 'meccan' / 'medinan'

# --- parse QAC morphology: per-surah root-token list ---
root_total = {}                  # root -> corpus frequency
surah_root_tokens = {i: 0 for i in range(1, 115)}   # root-bearing tokens per surah
tokens = []                      # (surah, root)
loc_re = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")
root_re = re.compile(r"ROOT:([^|]+)")

with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
        m = loc_re.match(loc)
        if not m:
            continue
        surah = int(m.group(1))
        rm = root_re.search(feats)
        if not rm:
            continue
        rt = rm.group(1).strip()
        root_total[rt] = root_total.get(rt, 0) + 1
        surah_root_tokens[surah] += 1
        tokens.append((surah, rt))

N = len(tokens)
n_roots = len(root_total)
hapax_roots = {r for r, c in root_total.items() if c == 1}
H = len(hapax_roots)
print(f"[data] root-bearing tokens N={N}, distinct roots={n_roots}, hapax roots H={H}")

# hapax tokens per surah
surah_hapax = {i: 0 for i in range(1, 115)}
hapax_by_surah = {i: [] for i in range(1, 115)}
for surah, rt in tokens:
    if rt in hapax_roots:
        surah_hapax[surah] += 1
        hapax_by_surah[surah].append(rt)

# per-token hapax rate per surah
rate = {}
for i in range(1, 115):
    rt_tok = surah_root_tokens[i]
    rate[i] = surah_hapax[i] / rt_tok if rt_tok else 0.0

# --- PRIMARY TEST: Meccan vs Medinan mean per-token hapax rate ---
meccan_ids = [i for i in range(1, 115) if region[i] == "meccan"]
medinan_ids = [i for i in range(1, 115) if region[i] == "medinan"]
mean_mecc = statistics.mean(rate[i] for i in meccan_ids)
mean_med = statistics.mean(rate[i] for i in medinan_ids)
obs_delta = mean_mecc - mean_med   # locked direction: expect > 0

# permutation null: shuffle labels
rng = random.Random(SEED)
all_ids = list(range(1, 115))
n_mecc = len(meccan_ids)
rates_list = [rate[i] for i in all_ids]
ge = 0
null_deltas = []
for _ in range(NPERM):
    idx = list(range(114))
    rng.shuffle(idx)
    mecc_idx = idx[:n_mecc]
    med_idx = idx[n_mecc:]
    dm = statistics.mean(rates_list[k] for k in mecc_idx) - statistics.mean(rates_list[k] for k in med_idx)
    null_deltas.append(dm)
    if dm >= obs_delta:
        ge += 1
p_one_sided = (ge + 1) / (NPERM + 1)

# --- SECONDARY ---
# S2: size-proportional residuals
residuals = {}
for i in range(1, 115):
    exp = H * surah_root_tokens[i] / N
    residuals[i] = surah_hapax[i] - exp
top_resid = sorted(residuals.items(), key=lambda kv: -kv[1])[:10]

# S3: Q1 hapax cross-check
q1_hapax = sorted(set(hapax_by_surah[1]))

# S4: Spearman rate vs surah number
def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda k: v[k])
        r = [0]*len(v)
        i = 0
        while i < len(v):
            j = i
            while j+1 < len(v) and v[order[j+1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k in range(i, j+1):
                r[order[k]] = avg
            i = j+1
        return r
    rx, ry = ranks(xs), ranks(ys)
    n = len(xs)
    mx, my = sum(rx)/n, sum(ry)/n
    cov = sum((rx[k]-mx)*(ry[k]-my) for k in range(n))
    sx = sum((rx[k]-mx)**2 for k in range(n))**0.5
    sy = sum((ry[k]-my)**2 for k in range(n))**0.5
    return cov/(sx*sy) if sx and sy else 0.0

ids_sorted = list(range(1, 115))
rho = spearman([float(i) for i in ids_sorted], [rate[i] for i in ids_sorted])

verdict = "CONFIRMED" if (obs_delta > 0 and p_one_sided < 0.05) else (
    "NULL-REVERSED" if obs_delta < 0 else "NULL")

out = {
    "finding": "H-NEW-2320",
    "prereg_sha256": actual,
    "seed": SEED, "nperm": NPERM,
    "rules_tuple": "QAC root v0.4, root-bearing tokens only, Hafs-Kufan",
    "corpus": {"root_tokens": N, "distinct_roots": n_roots, "hapax_roots": H,
               "hapax_fraction_of_roots": round(H/n_roots, 4)},
    "primary": {
        "mean_rate_meccan": round(mean_mecc, 6),
        "mean_rate_medinan": round(mean_med, 6),
        "obs_delta_mecc_minus_med": round(obs_delta, 6),
        "p_one_sided": round(p_one_sided, 6),
        "null_mean_delta": round(statistics.mean(null_deltas), 6),
        "direction_locked": "meccan > medinan",
        "verdict": verdict,
    },
    "secondary": {
        "top10_positive_residual_surahs": [
            {"surah": i, "name": quran[i-1]["name"], "region": region[i],
             "hapax_count": surah_hapax[i], "root_tokens": surah_root_tokens[i],
             "rate": round(rate[i], 5), "residual": round(residuals[i], 2)}
            for i, _ in top_resid],
        "q1_alfatiha_hapax_roots": q1_hapax,
        "q1_alfatiha_hapax_count": len(q1_hapax),
        "spearman_rate_vs_surah_number": round(rho, 4),
        "highest_rate_surahs": [
            {"surah": i, "name": quran[i-1]["name"], "region": region[i], "rate": round(rate[i], 5),
             "hapax_count": surah_hapax[i], "root_tokens": surah_root_tokens[i]}
            for i in sorted(range(1, 115), key=lambda k: -rate[k])[:12]],
    },
}
outpath = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2320.json")
json.dump(out, open(outpath, "w"), ensure_ascii=False, indent=2)
print(json.dumps(out["primary"], indent=2))
print("Q1 hapax roots:", q1_hapax)
print("top residual:", [(i, quran[i-1]["name"], region[i], round(residuals[i],1)) for i,_ in top_resid])
print(f"[written] {outpath}")
print(f"[VERDICT] {verdict}")
