#!/usr/bin/env python3
"""
H-NEW-2350 — Cross-surah exact-verse twins and their revelation-order proximity.
Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2350-verse-twin-chronology.md
Direction LOCKED: twin-linked surahs are CLOSER in revelation order than size-matched random.
Seed 20260509, 10000 perms. Author: Waiel Al-Shujaa.
"""
import json, hashlib, random, os, csv, unicodedata, itertools, statistics

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2350-verse-twin-chronology.md")
EXPECTED_SHA = "198538f725aad07fe2a57064d83c88cefff4ebf2f53c3d2fcc31ee7214fb88d1"
QURAN = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
REVCSV = os.path.join(ROOT, "data/revelation-order.csv")
SEED, NPERM = 20260509, 10000
MIN_TOK = 8     # primary substantive-twin threshold

with open(PREREG, "rb") as f:
    actual = hashlib.sha256(f.read()).hexdigest()
assert actual == EXPECTED_SHA, f"PRE-REG TAMPERED: {actual} != {EXPECTED_SHA}"
print(f"[ok] pre-reg SHA verified: {actual}")

quran = json.load(open(QURAN))
region = {s["id"]: s["type"] for s in quran}
sname = {s["id"]: s["name"] for s in quran}

# revelation order keyed by mushaf surah id
rev = {}
nold = {}
with open(REVCSV) as f:
    for row in csv.DictReader(f):
        mid = int(row["mushaf_order"])
        rev[mid] = int(row["revelation_order"])
        nold[mid] = int(row["noldeke_order"]) if row.get("noldeke_order") else None

def norm(t):
    return " ".join(unicodedata.normalize("NFC", t).split())

# map verse-string -> set of surahs containing it (+ first occurrence ref)
vmap = {}
refs = {}
for s in quran:
    sid = s["id"]
    for v in s["verses"]:
        t = norm(v["text"])
        vmap.setdefault(t, set()).add(sid)
        refs.setdefault(t, []).append((sid, v["id"]))

def twin_groups(min_tok):
    groups = []
    for t, surahs in vmap.items():
        if len(surahs) >= 2 and len(t.split()) >= min_tok:
            groups.append((t, sorted(surahs)))
    return groups

def aggregate_distance(groups, order):
    # mean over groups of group's mean pairwise revelation distance
    gmeans = []
    for _, surahs in groups:
        ds = [abs(order[a]-order[b]) for a, b in itertools.combinations(surahs, 2)]
        if ds:
            gmeans.append(statistics.mean(ds))
    return statistics.mean(gmeans) if gmeans else None, gmeans

groups = twin_groups(MIN_TOK)
D_obs, gmeans = aggregate_distance(groups, rev)
sizes = [len(s) for _, s in groups]

# permutation null: size-matched random distinct surahs
all_ids = list(range(1, 115))
rng = random.Random(SEED)
le = 0
nulls = []
for _ in range(NPERM):
    gm = []
    for g in sizes:
        pick = rng.sample(all_ids, g)
        ds = [abs(rev[a]-rev[b]) for a, b in itertools.combinations(pick, 2)]
        gm.append(statistics.mean(ds))
    dn = statistics.mean(gm)
    nulls.append(dn)
    if dn <= D_obs:
        le += 1
p_one = (le+1)/(NPERM+1)
null_mean = statistics.mean(nulls)

# Noldeke robustness
D_nold, _ = aggregate_distance(groups, {k: v for k, v in nold.items() if v})
# period concordance
def concordance(groups):
    same = sum(1 for _, s in groups if len({region[i] for i in s}) == 1)
    return same, len(groups)
same, ng = concordance(groups)
rng2 = random.Random(SEED+1)
csame = []
for _ in range(NPERM):
    c = 0
    for g in sizes:
        pick = rng2.sample(all_ids, g)
        if len({region[i] for i in pick}) == 1:
            c += 1
    csame.append(c)
p_conc = (sum(1 for c in csame if c >= same)+1)/(NPERM+1)

verdict = "CONFIRMED" if (D_obs < null_mean and p_one < 0.05) else (
    "NULL-REVERSED" if D_obs > null_mean else "NULL")

# enumeration table (sorted by token length desc)
def enum(groups):
    rows = []
    for t, surahs in groups:
        first = refs[t][0]
        rows.append({"text": t, "tokens": len(t.split()),
                     "surahs": surahs,
                     "names": [sname[i] for i in surahs],
                     "regions": [region[i] for i in surahs],
                     "rev_orders": [rev[i] for i in surahs],
                     "refs": [f"{a}:{b}" for a, b in refs[t]]})
    rows.sort(key=lambda r: (-r["tokens"], r["surahs"]))
    return rows

g10 = twin_groups(10)
g6 = twin_groups(6)
out = {
    "finding": "H-NEW-2350", "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "min_tokens_primary": MIN_TOK,
    "counts": {"groups_ge6": len(g6), "groups_ge8": len(groups), "groups_ge10": len(g10)},
    "primary": {"D_obs_mean_rev_distance": round(D_obs, 3),
                "null_mean": round(null_mean, 3),
                "p_one_sided_closer": round(p_one, 5),
                "direction_locked": "twins closer than random",
                "verdict": verdict},
    "robustness": {"D_obs_noldeke": round(D_nold, 3) if D_nold else None,
                   "period_concordant_groups": same, "total_groups": ng,
                   "p_concordance": round(p_conc, 5)},
    "enumeration_ge8": enum(groups),
}
json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2350.json"), "w"),
          ensure_ascii=False, indent=2)
print(json.dumps(out["primary"], indent=2))
print(json.dumps(out["counts"], indent=2))
print("period concordance:", same, "/", ng, "p=", round(p_conc, 4))
print(f"--- ge10 twin groups ({len(g10)}) ---")
for r in enum(g10):
    print(f"  [{r['tokens']}tok] {'+'.join(r['refs'])}  {'/'.join(r['names'])}  rev{r['rev_orders']}")
print(f"[VERDICT] {verdict}")
