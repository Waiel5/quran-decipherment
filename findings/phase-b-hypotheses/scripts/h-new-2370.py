#!/usr/bin/env python3
"""
H-NEW-2370 — Within-verse / pericope-scale emphatic iconicity (finer-scale follow-up to H-NEW-2340).

Question: WITHIN a surah, do punishment verses (containing the punishment lexicon, QAC-disambiguated)
carry HIGHER heavy (isti'lā') consonant density than that same surah's non-punishment verses?
This is a PAIRED, within-surah design: each qualifying surah contributes one paired difference Δ_s,
controlling for the surah's own rhyme/phonotactic baseline (the confound that flattened 2340).

Direction LOCKED: aggregate mean paired difference Δ̄ = mean_s(Δ_s) > 0.
Heavy letters = isti'lā' {ص ض ط ظ ق غ خ} = Buckwalter {S,D,T,Z,q,g,x}.
Self-coupling broken: letters of punishment-lexicon TOKENS removed from BOTH numerator and denominator.
nār (fire) lemma-pinned, nūr (light) EXCLUDED.

Primary null: within-surah label permutation (relabel which verses are 'punishment', count fixed),
10000×, seed 20260509. Secondary null: per-surah sign-flip of Δ_s (Rademacher), 10000×.
Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2370-within-verse-iconicity.md
Author: Waiel Al-Shujaa.
"""
import json, re, hashlib, random, os
from collections import defaultdict

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2370-within-verse-iconicity.md")
EXPECTED_SHA = "d7476efd8d24aee38c9773c231ec07be5334dedda52b17721bfa8435f289c7ec"
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

HEAVY = set("SDTZqgx")              # isti'lā' in Buckwalter
DIA = set("aiou~oFNK")             # short vowels / tanwin / shadda / sukun

def letter_counts(form):
    """(total letters, heavy letters) for one QAC Buckwalter token form."""
    tot = hv = 0
    for ch in form:
        if ch in DIA or ch in " \tـ":
            continue
        if ch.isalpha() or ch in "'><&}|{`pYAv<>":
            tot += 1
            if ch in HEAVY:
                hv += 1
    return tot, hv

# Punishment lexicon (QAC-verified encodings)
PRIM_ROOT = {"E*b"}                                 # 'adhab
HELL_ROOT = {"jHm", "sEr", "HTm", "lZy"}            # jaheem, sa'eer, hutama, talazza
HELL_LEM = {"saqar", "laZaY`", "naAr"}              # saqar(PN), laza(PN), naar(fire) -- NOT nuwr

loc = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)")
root_re = re.compile(r"ROOT:([^|]+)")
lem_re = re.compile(r"LEM:([^|]+)")

# verse -> [(tot, hv, is_prim_tok, is_hell_tok), ...] over its tokens
verse_tokens = defaultdict(list)          # (s,v) -> list of token tuples
surah_verses = defaultdict(set)           # s -> set of v

with open(MORPH, encoding="utf-8") as f:
    for line in f:
        if not line.startswith("("):
            continue
        m = loc.match(line)
        if not m:
            continue
        s, v = int(m.group(1)), int(m.group(2))
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        form = parts[1]; feat = parts[3]
        rt = root_re.search(feat); lm = lem_re.search(feat)
        rt = rt.group(1).strip() if rt else ""
        lm = lm.group(1).strip() if lm else ""
        t, h = letter_counts(form)
        is_prim = (rt in PRIM_ROOT)
        is_hell = is_prim or (rt in HELL_ROOT) or (lm in HELL_LEM)
        verse_tokens[(s, v)].append((t, h, is_prim, is_hell))
        surah_verses[s].add(v)

def verse_density(s, v, use_secondary):
    """Heavy-consonant density of verse, EXCLUDING punishment-lexicon token letters
       (numerator+denominator). Returns (density, is_punishment_verse)."""
    tot = hv = 0
    is_punish = False
    for (t, h, ip, ih) in verse_tokens[(s, v)]:
        flag = ih if use_secondary else ip
        if flag:
            is_punish = True
            continue            # exclude the lexicon token's letters entirely
        tot += t; hv += h
    dens = hv / tot if tot > 0 else 0.0
    return dens, is_punish

def build(use_secondary):
    """Return per-surah dict: s -> (deltas list-of-one via means, n_pun, n_non, labels, dens-array)."""
    surah_data = {}
    for s in range(1, 115):
        vs = sorted(surah_verses[s])
        dens = []; labels = []
        for v in vs:
            d, pun = verse_density(s, v, use_secondary)
            dens.append(d); labels.append(1 if pun else 0)
        npun = sum(labels)
        if 1 <= npun < len(vs):     # qualifying: has both punishment and non-punishment verses
            surah_data[s] = {"dens": dens, "labels": labels, "npun": npun, "nnon": len(vs) - npun}
    return surah_data

def deltas(surah_data):
    """Δ_s per surah and the aggregate mean Δ̄."""
    ds = {}
    for s, d in surah_data.items():
        dens, lab = d["dens"], d["labels"]
        mp = sum(x for x, l in zip(dens, lab) if l) / d["npun"]
        mn = sum(x for x, l in zip(dens, lab) if not l) / d["nnon"]
        ds[s] = mp - mn
    return ds

def aggregate(ds):
    return sum(ds.values()) / len(ds)

def weighted_aggregate(ds, surah_data):
    num = sum(ds[s] * surah_data[s]["npun"] for s in ds)
    den = sum(surah_data[s]["npun"] for s in ds)
    return num / den

# ----- PRIMARY (adhab) -----
sd_prim = build(False)
ds_prim = deltas(sd_prim)
dbar_prim = aggregate(ds_prim)
n_surahs_prim = len(sd_prim)

# within-surah label-permutation null
rng = random.Random(SEED)
ge_perm = 0
for _ in range(NPERM):
    tot_delta = 0.0
    for s, d in sd_prim.items():
        dens = d["dens"]; npun = d["npun"]; nv = npun + d["nnon"]
        idx = list(range(nv))
        rng.shuffle(idx)
        pun_idx = set(idx[:npun])
        mp = sum(dens[i] for i in pun_idx) / npun
        mn = sum(dens[i] for i in range(nv) if i not in pun_idx) / d["nnon"]
        tot_delta += (mp - mn)
    if tot_delta / n_surahs_prim >= dbar_prim:
        ge_perm += 1
p_perm_prim = (ge_perm + 1) / (NPERM + 1)

# sign-flip null
rng2 = random.Random(SEED)
dvals = list(ds_prim.values())
ge_sf = 0
for _ in range(NPERM):
    flipped = sum(v if rng2.random() < 0.5 else -v for v in dvals)
    if flipped / len(dvals) >= dbar_prim:
        ge_sf += 1
p_signflip_prim = (ge_sf + 1) / (NPERM + 1)

# ----- R1 SECONDARY (hellfire) -----
sd_sec = build(True)
ds_sec = deltas(sd_sec)
dbar_sec = aggregate(ds_sec)
n_surahs_sec = len(sd_sec)
rng3 = random.Random(SEED)
ge_sec = 0
for _ in range(NPERM):
    tot_delta = 0.0
    for s, d in sd_sec.items():
        dens = d["dens"]; npun = d["npun"]; nv = npun + d["nnon"]
        idx = list(range(nv))
        rng3.shuffle(idx)
        pun_idx = set(idx[:npun])
        mp = sum(dens[i] for i in pun_idx) / npun
        mn = sum(dens[i] for i in range(nv) if i not in pun_idx) / d["nnon"]
        tot_delta += (mp - mn)
    if tot_delta / n_surahs_sec >= dbar_sec:
        ge_sec += 1
p_perm_sec = (ge_sec + 1) / (NPERM + 1)

# ----- R2 region splits (primary) -----
def region_dbar(ds, reg):
    sub = {s: v for s, v in ds.items() if region[s] == reg}
    return (aggregate(sub), len(sub)) if sub else (0.0, 0)
dbar_mecc, n_mecc = region_dbar(ds_prim, "meccan")
dbar_med, n_med = region_dbar(ds_prim, "medinan")

# ----- R3 verse-weighted (primary) -----
dbar_w = weighted_aggregate(ds_prim, sd_prim)

# ----- R4 token-pool descriptive (NOT paired, surah confound reintroduced) -----
pool_pun_hv = pool_pun_tot = pool_non_hv = pool_non_tot = 0
for s in range(1, 115):
    for v in sorted(surah_verses[s]):
        tot = hv = 0; pun = False
        for (t, h, ip, ih) in verse_tokens[(s, v)]:
            if ip:
                pun = True; continue
            tot += t; hv += h
        if pun:
            pool_pun_hv += hv; pool_pun_tot += tot
        else:
            pool_non_hv += hv; pool_non_tot += tot
pool_pun_dens = pool_pun_hv / pool_pun_tot
pool_non_dens = pool_non_hv / pool_non_tot

# ----- verdict -----
ALPHA = 0.05 / 2     # Bonferroni: family = {primary, R1}
prim_pass = (dbar_prim > 0 and p_perm_prim < ALPHA)
if not prim_pass:
    verdict = "NULL-REVERSED" if dbar_prim <= 0 else "NULL"
elif (dbar_sec > 0) and (dbar_mecc > 0) and (dbar_med > 0):
    verdict = "VINDICATED-FINE-SCALE"
else:
    verdict = "DIRECTIONAL"

# sign of effect summary
n_pos = sum(1 for v in ds_prim.values() if v > 0)
n_neg = sum(1 for v in ds_prim.values() if v < 0)
n_zero = sum(1 for v in ds_prim.values() if v == 0)

out = {
    "finding": "H-NEW-2370", "prereg_sha256": actual, "seed": SEED, "nperm": NPERM,
    "design": "paired within-surah: Δ_s = mean(heavy_density punishment verses) - mean(non-punishment verses)",
    "heavy_letters": "isti'la' S D T Z q g x (Buckwalter)",
    "direction_locked": "Dbar > 0",
    "alpha_bonferroni": ALPHA,
    "primary_adhab": {
        "n_qualifying_surahs": n_surahs_prim,
        "Dbar_mean_paired_diff": round(dbar_prim, 6),
        "p_within_surah_label_perm": round(p_perm_prim, 5),
        "p_signflip": round(p_signflip_prim, 5),
        "surahs_positive_delta": n_pos, "surahs_negative_delta": n_neg, "surahs_zero_delta": n_zero,
    },
    "R1_secondary_hellfire": {
        "n_qualifying_surahs": n_surahs_sec,
        "Dbar_mean_paired_diff": round(dbar_sec, 6),
        "p_within_surah_label_perm": round(p_perm_sec, 5),
    },
    "R2_region": {
        "meccan": {"n": n_mecc, "Dbar": round(dbar_mecc, 6)},
        "medinan": {"n": n_med, "Dbar": round(dbar_med, 6)},
    },
    "R3_verse_weighted_Dbar": round(dbar_w, 6),
    "R4_token_pool_descriptive_unpaired": {
        "punishment_verse_heavy_density": round(pool_pun_dens, 6),
        "nonpunishment_verse_heavy_density": round(pool_non_dens, 6),
        "diff": round(pool_pun_dens - pool_non_dens, 6),
        "note": "NOT paired; surah confound reintroduced; context only",
    },
    "verdict": verdict,
}
json.dump(out, open(os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2370.json"), "w"),
          ensure_ascii=False, indent=2)

print("\n=== PRIMARY (ʿadhāb, paired within-surah) ===")
print(json.dumps(out["primary_adhab"], indent=2))
print("=== R1 secondary hellfire ===")
print(json.dumps(out["R1_secondary_hellfire"], indent=2))
print("=== R2 region ===", json.dumps(out["R2_region"]))
print("R3 verse-weighted Δ̄:", out["R3_verse_weighted_Dbar"])
print("R4 token-pool (unpaired, context):", json.dumps(out["R4_token_pool_descriptive_unpaired"]))
print(f"\n[VERDICT] {verdict}")
