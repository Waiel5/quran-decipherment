#!/usr/bin/env python3
"""
H-NEW-2340 — Emphatic-consonant sound-symbolism: does heavy (isti'lāʾ) consonant density
track punishment vocabulary across surahs?
Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2340-emphatic-iconicity.md
Direction LOCKED: Spearman ρ(heavy-density, ʿadhāb-density) > 0.
All letter counts computed in QAC Buckwalter space (consistent for token removal).
Heavy letters = isti'lāʾ {ص ض ط ظ ق غ خ} = Buckwalter {S,D,T,Z,q,g,x}.
Punishment tokens removed from heavy/total counts (primary lemma E*b has no heavy letters
anyway -> removal affects only denominator; faithful to pre-reg).
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2340-emphatic-iconicity.md")
EXPECTED_SHA = "acdbac5ab8b520a31abe59f3a4722743b2ba1a1b3bb607df7bf63f27e82dd134"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
SEED, NPERM = 20260509, 10000

with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
name = {s["id"]: s["name"] for s in quran}

HEAVY = set("SDTZqgx")                      # isti'lāʾ in Buckwalter
DIA = set("aiou~oFNK")                       # short vowels / tanwin / shadda / sukun
# a "letter" = any non-diacritic, non-space alphabetic Buckwalter symbol
def letter_counts(form):
    tot = hv = 0
    for ch in form:
        if ch in DIA or ch in " \tـ":   # exclude diacritics + tatweel
            continue
        if ch.isalpha() or ch in "'><&}|{`pYAv<>":
            tot += 1
            if ch in HEAVY:
                hv += 1
    return tot, hv

PRIM_ROOT = "E*b"                            # ʿ-dh-b (ʿadhāb)
HELL_ROOTS = {"jHm", "sER", "sqr", "lZy", "HTm"}   # jaḥīm, saʿīr, saqar, laẓā, ḥuṭama
NAR_LEM = "naAr"                             # fire (NOT nūr 'light' -> lemma-disambiguated)

loc_re = re.compile(r"^\((\d+):")
root_re = re.compile(r"ROOT:([^|]+)")
lem_re = re.compile(r"LEM:([^|]+)")

# per surah accumulators
tot_all = {i: 0 for i in range(1, 115)}
hv_all = {i: 0 for i in range(1, 115)}
tot_prim_tok = {i: 0 for i in range(1, 115)}   # letters in ʿadhāb tokens
hv_prim_tok = {i: 0 for i in range(1, 115)}
tot_sec_tok = {i: 0 for i in range(1, 115)}    # letters in secondary hell tokens (incl prim)
hv_sec_tok = {i: 0 for i in range(1, 115)}
adhab_tok = {i: 0 for i in range(1, 115)}      # ʿadhāb token count
hell_tok = {i: 0 for i in range(1, 115)}       # full hellfire-set token count
tok_total = {i: 0 for i in range(1, 115)}      # total tokens (segments)

with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) < 4:
            continue
        m = loc_re.match(p[0])
        if not m:
            continue
        s = int(m.group(1)); form = p[1]
        rt = root_re.search(p[3]); lm = lem_re.search(p[3])
        rt = rt.group(1).strip() if rt else ""
        lm = lm.group(1).strip() if lm else ""
        t, h = letter_counts(form)
        tot_all[s] += t; hv_all[s] += h
        tok_total[s] += 1
        is_prim = (rt == PRIM_ROOT)
        is_hell = is_prim or (rt in HELL_ROOTS) or (lm == NAR_LEM)
        if is_prim:
            tot_prim_tok[s] += t; hv_prim_tok[s] += h; adhab_tok[s] += 1
        if is_hell:
            tot_sec_tok[s] += t; hv_sec_tok[s] += h; hell_tok[s] += 1

# densities (heavy over non-punishment letters; punishment-density over tokens)
def spearman(xs, ys):
    def ranks(v):
        order = sorted(range(len(v)), key=lambda k: v[k]); r = [0]*len(v); i = 0
        while i < len(v):
            j = i
            while j+1 < len(v) and v[order[j+1]] == v[order[i]]:
                j += 1
            avg = (i+j)/2 + 1
            for k in range(i, j+1):
                r[order[k]] = avg
            i = j+1
        return r
    rx, ry = ranks(xs), ranks(ys); n = len(xs)
    mx, my = sum(rx)/n, sum(ry)/n
    cov = sum((rx[k]-mx)*(ry[k]-my) for k in range(n))
    sx = sum((rx[k]-mx)**2 for k in range(n))**0.5
    sy = sum((ry[k]-my)**2 for k in range(n))**0.5
    return cov/(sx*sy) if sx and sy else 0.0

ids = list(range(1, 115))
# primary: heavy density over text minus ʿadhāb letters; ʿadhāb token-density
heavy_prim = [(hv_all[i]-hv_prim_tok[i])/max(1, tot_all[i]-tot_prim_tok[i]) for i in ids]
adhab_dens = [adhab_tok[i]/max(1, tok_total[i]) for i in ids]
rho_prim = spearman(heavy_prim, adhab_dens)

# secondary: heavy density minus hellfire letters; hellfire token-density
heavy_sec = [(hv_all[i]-hv_sec_tok[i])/max(1, tot_all[i]-tot_sec_tok[i]) for i in ids]
hell_dens = [hell_tok[i]/max(1, tok_total[i]) for i in ids]
rho_sec = spearman(heavy_sec, hell_dens)

# permutation null (primary): shuffle pairing
rng = random.Random(SEED)
ge = 0
y = list(adhab_dens)
for _ in range(NPERM):
    rng.shuffle(y)
    if spearman(heavy_prim, y) >= rho_prim:
        ge += 1
p_prim = (ge+1)/(NPERM+1)

# robustness R1: Meccan-only primary
mids = [k for k, i in enumerate(ids) if region[i] == "meccan"]
rho_mecc = spearman([heavy_prim[k] for k in mids], [adhab_dens[k] for k in mids])
# Medinan-only
dids = [k for k, i in enumerate(ids) if region[i] == "medinan"]
rho_med = spearman([heavy_prim[k] for k in dids], [adhab_dens[k] for k in dids])

if rho_prim > 0 and p_prim < 0.05:
    verdict = "CONFIRMED" if (rho_mecc > 0) else "CONFIRMED-BUT-REGION-CONFOUNDED"
elif rho_prim <= 0:
    verdict = "NULL-REVERSED"
else:
    verdict = "NULL"

out = {
    "finding": "H-NEW-2340", "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "heavy_letters": "isti'la' S D T Z q g x (Buckwalter)",
    "primary": {"rho_heavy_vs_adhab": round(rho_prim, 4), "p_one_sided": round(p_prim, 5),
                "direction_locked": "rho > 0", "verdict": verdict},
    "robustness": {"rho_meccan_only": round(rho_mecc, 4), "rho_medinan_only": round(rho_med, 4),
                   "rho_secondary_hellfire_set": round(rho_sec, 4)},
    "corpus": {"total_letters": sum(tot_all.values()),
               "total_heavy": sum(hv_all.values()),
               "heavy_fraction": round(sum(hv_all.values())/sum(tot_all.values()), 4),
               "adhab_tokens": sum(adhab_tok.values()),
               "hellfire_tokens": sum(hell_tok.values())},
    "top_heavy_surahs": sorted(
        [{"surah": i, "name": name[i], "region": region[i],
          "heavy_density": round(heavy_prim[k], 4), "adhab_density": round(adhab_dens[k], 4)}
         for k, i in enumerate(ids)], key=lambda d: -d["heavy_density"])[:12],
}
json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2340.json"), "w"),
          ensure_ascii=False, indent=2)
print(json.dumps(out["primary"], indent=2))
print(json.dumps(out["robustness"], indent=2))
print("corpus heavy fraction:", out["corpus"]["heavy_fraction"], "| ʿadhāb tokens:", out["corpus"]["adhab_tokens"])
print("top heavy surahs:", [(d["name"], d["heavy_density"]) for d in out["top_heavy_surahs"][:6]])
print(f"[VERDICT] {verdict}")
