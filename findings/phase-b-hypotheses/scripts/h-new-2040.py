#!/usr/bin/env python3
"""H-NEW-2040 — systematic abjad / ḥisāb al-jummal sweep + famous-claims audit.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2040-abjad-sweep.md
SHA256 (locked): 68f40fafb5b13863002c7c36da2314a9d0eb94f5156d4fd7d28e5b6423776232

Stdlib only. Seed 20260509. Fail-fast on SHA mismatch.
"""
from __future__ import annotations

import hashlib
import json
import math
import os
import random

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2040-abjad-sweep.md")
PREREG_SHA = "68f40fafb5b13863002c7c36da2314a9d0eb94f5156d4fd7d28e5b6423776232"
OUT = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2040.json")
SEED = 20260509
NPERM = 10000

# ---------------------------------------------------------------- SHA gate
with open(PREREG, "rb") as fh:
    got = hashlib.sha256(fh.read()).hexdigest()
if got != PREREG_SHA:
    raise SystemExit(f"PRE-REG SHA MISMATCH\n expected {PREREG_SHA}\n got      {got}")

# ---------------------------------------------------------------- abjad tables (methodology.md §6)
MASHRIQI = {
    "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
    "ك": 20, "ل": 30, "م": 40, "ن": 50, "س": 60, "ع": 70, "ف": 80, "ص": 90,
    "ق": 100, "ر": 200, "ش": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ض": 800,
    "ظ": 900, "غ": 1000,
}
MAGHRIBI = {
    "ا": 1, "ب": 2, "ج": 3, "د": 4, "ه": 5, "و": 6, "ز": 7, "ح": 8, "ط": 9, "ي": 10,
    "ك": 20, "ل": 30, "م": 40, "ن": 50, "ص": 60, "ع": 70, "ف": 80, "ض": 90,
    "ق": 100, "ر": 200, "س": 300, "ت": 400, "ث": 500, "خ": 600, "ذ": 700, "ظ": 800,
    "غ": 900, "ش": 1000,
}
# Hamza-carrier policy per methodology.md §6: carriers map to their base letter value.
CARRIER = {"أ": "ا", "إ": "ا", "آ": "ا", "ٱ": "ا", "ؤ": "و", "ئ": "ي"}
# Characters that contribute 0 (ة, ى, bare ء, tashkeel, marks, spaces) — anything not
# in the table and not a carrier just contributes 0.


def abjad(text: str, table: str = "mashriqi", carriers: bool = True) -> int:
    tbl = MASHRIQI if table == "mashriqi" else MAGHRIBI
    total = 0
    for ch in text:
        if ch in tbl:
            total += tbl[ch]
        elif carriers and ch in CARRIER:
            total += tbl[CARRIER[ch]]
        # else contributes 0
    return total


# ---------------------------------------------------------------- data
with open(os.path.join(ROOT, "quran-text/quran-no-tashkeel.json"), encoding="utf-8") as fh:
    QURAN = json.load(fh)
with open(os.path.join(ROOT, "data/alt-text/quran-uthmani-consonantal.json"), encoding="utf-8") as fh:
    CONS = json.load(fh)

results = {
    "finding_id": "h-new-2040-abjad-sweep",
    "prereg_sha256": PREREG_SHA,
    "seed": SEED,
    "nperm": NPERM,
    "abjad_table_default": "mashriqi",
    "class_A_famous_claims": {},
    "class_A_muqattaat": {},
    "class_B_systematic": {},
}

# ================================================================ CLASS A
# A1 basmala, A2 Allāh, A3 Muḥammad
basmala = "بسم الله الرحمن الرحيم"
allah = "الله"
muhammad = "محمد"
for name, txt, claim in [
    ("basmala", basmala, 786),
    ("allah", allah, 66),
    ("muhammad", muhammad, 92),
]:
    m = abjad(txt, "mashriqi")
    g = abjad(txt, "maghribi")
    results["class_A_famous_claims"][name] = {
        "text": txt,
        "claimed": claim,
        "mashriqi": m,
        "maghribi": g,
        "matches_claim_mashriqi": m == claim,
        "matches_claim_maghribi": g == claim,
    }

# A4 muqaṭṭaʿāt — 14 unique strings (from consonantal openers).
MUQ = {
    "alif-lam-mim": ("الم", [2, 3, 29, 30, 31, 32]),
    "alif-lam-mim-sad": ("المص", [7]),
    "alif-lam-ra": ("الر", [10, 11, 12, 14, 15]),
    "alif-lam-mim-ra": ("المر", [13]),
    "kaf-ha-ya-ayn-sad": ("كهيعص", [19]),
    "ta-ha": ("طه", [20]),
    "ta-sin-mim": ("طسم", [26, 28]),
    "ta-sin": ("طس", [27]),
    "ya-sin": ("يس", [36]),
    "sad": ("ص", [38]),
    "ha-mim": ("حم", [40, 41, 42, 43, 44, 45, 46]),
    "ha-mim-ayn-sin-qaf": ("حمعسق", [42]),  # Q42 v1=حم, v2=عسق → combined
    "qaf": ("ق", [50]),
    "nun": ("ن", [68]),
}
# build position->verse-count map
vc = {s["id"]: s["total_verses"] for s in QURAN}
clean_targets = {19, 114, 786, 6236}
for key, (s, surahs) in MUQ.items():
    m = abjad(s, "mashriqi")
    g = abjad(s, "maghribi")
    hits = []
    for sid in surahs:
        if m == sid:
            hits.append(f"==position({sid})")
        if m == vc[sid]:
            hits.append(f"==versecount(Q{sid}={vc[sid]})")
    for t in clean_targets:
        if m == t:
            hits.append(f"==clean({t})")
    results["class_A_muqattaat"][key] = {
        "letters": s,
        "surahs": surahs,
        "mashriqi": m,
        "maghribi": g,
        "coincidence_hits": hits,
    }

# ================================================================ CLASS B
rng = random.Random(SEED)


def pearson(x, y):
    n = len(x)
    mx = sum(x) / n
    my = sum(y) / n
    sxy = sum((a - mx) * (b - my) for a, b in zip(x, y))
    sxx = sum((a - mx) ** 2 for a in x)
    syy = sum((b - my) ** 2 for b in y)
    if sxx == 0 or syy == 0:
        return 0.0
    return sxy / math.sqrt(sxx * syy)


# surah-name abjad vector (methodology carrier policy = primary)
positions = [s["id"] for s in QURAN]
versecounts = [s["total_verses"] for s in QURAN]
name_abjad_m = [abjad(s["name"], "mashriqi") for s in QURAN]
name_abjad_g = [abjad(s["name"], "maghribi") for s in QURAN]
# sensitivity: gematria.py skip-policy (carriers contribute 0)
name_abjad_skip = [abjad(s["name"], "mashriqi", carriers=False) for s in QURAN]

name_table = [
    {"id": s["id"], "name": s["name"], "translit": s["transliteration"],
     "verses": s["total_verses"], "abjad_mashriqi": name_abjad_m[i],
     "abjad_maghribi": name_abjad_g[i], "abjad_skip_carrier": name_abjad_skip[i]}
    for i, s in enumerate(QURAN)
]


def perm_corr_p(vec, target, observed_r):
    """Two-sided perm-p for |r| >= |observed| under shuffle of vec."""
    work = list(vec)
    ge = 0
    for _ in range(NPERM):
        rng.shuffle(work)
        if abs(pearson(work, target)) >= abs(observed_r) - 1e-12:
            ge += 1
    return (ge + 1) / (NPERM + 1)


# H-B1 name-abjad vs position
r_pos = pearson(name_abjad_m, positions)
p_pos = perm_corr_p(name_abjad_m, positions, r_pos)
# H-B2 name-abjad vs verse-count
r_vc = pearson(name_abjad_m, versecounts)
p_vc = perm_corr_p(name_abjad_m, versecounts, r_vc)

# H-B3 exact matches name-abjad == position
obs_pos_match = sum(1 for a, p in zip(name_abjad_m, positions) if a == p)
# H-B4 exact matches name-abjad == verse-count
obs_vc_match = sum(1 for a, v in zip(name_abjad_m, versecounts) if a == v)


def perm_match_p(vec, target, observed):
    work = list(vec)
    ge = 0
    for _ in range(NPERM):
        rng.shuffle(work)
        c = sum(1 for a, t in zip(work, target) if a == t)
        if c >= observed:
            ge += 1
    return (ge + 1) / (NPERM + 1)


p_pos_match = perm_match_p(name_abjad_m, positions, obs_pos_match)
p_vc_match = perm_match_p(name_abjad_m, versecounts, obs_vc_match)

# list which surahs actually match (descriptive)
pos_matches = [name_table[i] for i in range(114) if name_abjad_m[i] == positions[i]]
vc_matches = [name_table[i] for i in range(114) if name_abjad_m[i] == versecounts[i]]

# MW-6 instrument control: correlate name-abjad vs a random permutation of positions
rng_ctrl = random.Random(SEED + 1)
ctrl_perm = list(positions)
rng_ctrl.shuffle(ctrl_perm)
r_ctrl = pearson(name_abjad_m, ctrl_perm)

# H-B5 verse abjad-sum vs structural indices (full scan, all 6236 verses)
verse_abjads = []
global_idx = 0
for s in QURAN:
    for v in s["verses"]:
        global_idx += 1
        a = abjad(v["text"], "mashriqi")
        verse_abjads.append((s["id"], v["id"], global_idx, a))

# target (a) within-surah verse number; (b) surah*1000+verse; (c) global index
match_a = [(sid, vid, gi, a) for (sid, vid, gi, a) in verse_abjads if a == vid]
match_b = [(sid, vid, gi, a) for (sid, vid, gi, a) in verse_abjads if a == sid * 1000 + vid]
match_c = [(sid, vid, gi, a) for (sid, vid, gi, a) in verse_abjads if a == gi]

# perm null for verse scan: shuffle target assignment (abjad fixed, reassign which target slot)
abjad_only = [a for (_, _, _, a) in verse_abjads]


def perm_verse_match_p(abjad_vals, targets, observed):
    work = list(abjad_vals)
    ge = 0
    for _ in range(NPERM):
        rng.shuffle(work)
        c = sum(1 for a, t in zip(work, targets) if a == t)
        if c >= observed:
            ge += 1
    return (ge + 1) / (NPERM + 1)


tgt_a = [vid for (_, vid, _, _) in verse_abjads]
tgt_b = [sid * 1000 + vid for (sid, vid, _, _) in verse_abjads]
tgt_c = [gi for (_, _, gi, _) in verse_abjads]
p_a = perm_verse_match_p(abjad_only, tgt_a, len(match_a))
p_b = perm_verse_match_p(abjad_only, tgt_b, len(match_b))
p_c = perm_verse_match_p(abjad_only, tgt_c, len(match_c))

K = 7
ALPHA = 0.05 / K

results["class_B_systematic"] = {
    "bonferroni_k": K,
    "alpha_corrected": ALPHA,
    "name_abjad_table": name_table,
    "H-B1_name_vs_position": {"pearson_r": r_pos, "perm_p": p_pos, "sig_at_bonferroni": p_pos < ALPHA},
    "H-B2_name_vs_versecount": {"pearson_r": r_vc, "perm_p": p_vc, "sig_at_bonferroni": p_vc < ALPHA},
    "H-B3_name_eq_position": {
        "observed_exact_matches": obs_pos_match, "perm_p": p_pos_match,
        "sig_at_bonferroni": p_pos_match < ALPHA,
        "matching_surahs": [{"id": m["id"], "name": m["name"], "abjad": m["abjad_mashriqi"]} for m in pos_matches],
    },
    "H-B4_name_eq_versecount": {
        "observed_exact_matches": obs_vc_match, "perm_p": p_vc_match,
        "sig_at_bonferroni": p_vc_match < ALPHA,
        "matching_surahs": [{"id": m["id"], "name": m["name"], "abjad": m["abjad_mashriqi"], "verses": m["verses"]} for m in vc_matches],
    },
    "H-B5_verse_eq_index": {
        "target_a_within_surah_verse": {"matches": len(match_a), "perm_p": p_a, "examples": match_a[:20]},
        "target_b_surah1000plusverse": {"matches": len(match_b), "perm_p": p_b, "examples": match_b[:20]},
        "target_c_global_index": {"matches": len(match_c), "perm_p": p_c, "examples": match_c[:20]},
    },
    "MW6_instrument_control_random_position_r": r_ctrl,
}

with open(OUT, "w", encoding="utf-8") as fh:
    json.dump(results, fh, ensure_ascii=False, indent=2)

# ---------------------------------------------------------------- console report
print("=== CLASS A — famous claims (mashriqi) ===")
for k, v in results["class_A_famous_claims"].items():
    print(f"  {k:10s} claimed={v['claimed']:4d}  mashriqi={v['mashriqi']:4d}  "
          f"maghribi={v['maghribi']:4d}  MATCH(m)={v['matches_claim_mashriqi']}")
print("\n=== CLASS A — muqaṭṭaʿāt ===")
for k, v in results["class_A_muqattaat"].items():
    hit = (" HITS:" + ",".join(v["coincidence_hits"])) if v["coincidence_hits"] else ""
    print(f"  {v['letters']:7s} mashriqi={v['mashriqi']:5d} maghribi={v['maghribi']:5d}{hit}")
print("\n=== CLASS B — systematic ===")
b = results["class_B_systematic"]
print(f"  Bonferroni k={K}, alpha={ALPHA:.5f}")
print(f"  H-B1 name~position : r={r_pos:+.4f} perm-p={p_pos:.4f} sig={b['H-B1_name_vs_position']['sig_at_bonferroni']}")
print(f"  H-B2 name~versecnt : r={r_vc:+.4f} perm-p={p_vc:.4f} sig={b['H-B2_name_vs_versecount']['sig_at_bonferroni']}")
print(f"  H-B3 name==position: {obs_pos_match} matches perm-p={p_pos_match:.4f} -> {[ (m['id'],m['name'],m['abjad_mashriqi']) for m in pos_matches]}")
print(f"  H-B4 name==versecnt: {obs_vc_match} matches perm-p={p_vc_match:.4f} -> {[ (m['id'],m['name'],m['abjad_mashriqi'],m['verses']) for m in vc_matches]}")
print(f"  H-B5a verse==vnum  : {len(match_a)} matches perm-p={p_a:.4f}")
print(f"  H-B5b verse==s*1000+v: {len(match_b)} matches perm-p={p_b:.4f}")
print(f"  H-B5c verse==global: {len(match_c)} matches perm-p={p_c:.4f}")
print(f"  MW6 control (name~random-position) r={r_ctrl:+.4f}")
print(f"\nwrote {OUT}")
