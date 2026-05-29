#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2200 — Iltifāt (grammatical-person shift) corpus map.

A GENERATOR over QAC v0.4 person/number features. For every verse it derives a
dominant grammatical PERSON and NUMBER from finite verbs + pronouns; at every
intra-surah verse boundary it tests for a change in either, recording the locus
with full coordinates. Then it runs ONE pre-registered direction-locked density
test: Meccan iltifāt-density > Medinan, label-shuffle null, 10,000 perms, seed 20260509.

Pre-reg SHA-256 lock verified at runtime. Every number is computed from disk.
Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, re, os, sys, hashlib, random
from collections import Counter, defaultdict

# ----------------------------------------------------------------------------
# 0. Paths + pre-reg SHA lock
# ----------------------------------------------------------------------------
ROOT      = "/Users/grey/Downloads/quran"
PREREG    = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2200-iltifat-corpus-map.md")
QURAN     = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC       = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
CATALOG   = os.path.join(ROOT, "data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md")
OUT_JSON  = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2200.json")

PREREG_SHA = "a324e9b8348b099dba85600cceafb8bd1a910c455bde56e96c99353e22cb95f9"
SEED       = 20260509
N_PERM     = 10000

def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()

actual = sha256(PREREG)
if actual != PREREG_SHA:
    sys.exit(f"FATAL: pre-reg SHA mismatch.\n  expected {PREREG_SHA}\n  actual   {actual}\n"
             "Pre-registration was altered after locking. Aborting per protocol §1.2.")
print(f"[OK] pre-reg SHA verified: {actual}")

# ----------------------------------------------------------------------------
# 1. Load verse inventory + region labels
# ----------------------------------------------------------------------------
quran = json.load(open(QURAN, encoding="utf-8"))
SURAH_TYPE  = {s["id"]: s["type"] for s in quran}                       # 'meccan' / 'medinan'
SURAH_NV    = {s["id"]: len(s["verses"]) for s in quran}               # verse count
N_SURAH     = len(quran)
N_VERSE     = sum(SURAH_NV.values())
print(f"[data] surahs={N_SURAH}  verses={N_VERSE}  "
      f"meccan={sum(1 for t in SURAH_TYPE.values() if t=='meccan')}  "
      f"medinan={sum(1 for t in SURAH_TYPE.values() if t=='medinan')}")

# ----------------------------------------------------------------------------
# 2. Parse QAC: extract per-verse multiset of (person, number) for V + PRON
# ----------------------------------------------------------------------------
# Person-number-gender token regex (with optional PRON: prefix used by suffix clitics):
#   ^(PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$
PNG_RE = re.compile(r"^(?:PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$")
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")

def number_of(numgen):
    """Map number-gender code to bare number S/D/P."""
    if numgen.startswith("M") or numgen.startswith("F"):
        return numgen[1]          # MS->S, MP->P, MD->D, FS->S, FP->P, FD->D
    return numgen                 # already S / D / P

# verse_segs[(s,v)] = list of (person:int, number:str, word_index:int, is_verb:bool)
verse_segs = defaultdict(list)

with open(QAC, encoding="utf-8") as f:
    for line in f:
        if line.startswith("#") or line.startswith("LOCATION"):
            continue
        line = line.rstrip("\n")
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
        m = LOC_RE.match(loc)
        if not m:
            continue
        s, v, w, seg = (int(m.group(i)) for i in range(1, 5))

        is_verb = (tag == "V")
        is_pron = (tag == "PRON") or ("PRON:" in feats)
        if not (is_verb or is_pron):
            continue

        # scan FEATURES fields for a person-number-gender token
        for field in feats.split("|"):
            pm = PNG_RE.match(field)
            if pm:
                person = int(pm.group(1))
                num    = number_of(pm.group(2))
                verse_segs[(s, v)].append((person, num, w, is_verb))
                # a verb may also carry PRON: object suffix counted as its own segment elsewhere;
                # but a single V segment's own subject-person is taken once (first PNG field).
                if is_verb:
                    break  # the verb's subject person-number is one field; avoid double-count within same V seg
        # (PRON segments contribute exactly one PNG field by construction)

# ----------------------------------------------------------------------------
# 3. Dominant person / number per verse (tie -> later-occurring value)
# ----------------------------------------------------------------------------
def dominant(segs, key_idx):
    """key_idx: 0 for person, 1 for number. Returns dominant value or None.
    Modal by count; tie broken toward the value occurring LATER (max word index)."""
    if not segs:
        return None
    counts = Counter(seg[key_idx] for seg in segs)
    top = max(counts.values())
    winners = [val for val, c in counts.items() if c == top]
    if len(winners) == 1:
        return winners[0]
    # tie-break: the winner whose LAST occurrence is latest in the verse
    last_word = {}
    for seg in segs:
        val = seg[key_idx]
        if val in winners:
            last_word[val] = max(last_word.get(val, -1), seg[2])
    return max(winners, key=lambda val: last_word[val])

dom_person = {}   # (s,v) -> 1/2/3/None
dom_number = {}   # (s,v) -> S/D/P/None
profile    = {}   # (s,v) -> dict of person-number multiset (for output)
for s in range(1, N_SURAH + 1):
    for v in range(1, SURAH_NV[s] + 1):
        segs = verse_segs.get((s, v), [])
        dom_person[(s, v)] = dominant(segs, 0)
        dom_number[(s, v)] = dominant(segs, 1)
        if segs:
            pc = Counter(p for p, n, w, iv in segs)
            nc = Counter(n for p, n, w, iv in segs)
            profile[(s, v)] = {"n_seg": len(segs),
                               "person": dict(pc), "number": dict(nc)}

# ----------------------------------------------------------------------------
# 4. ILTIFĀT LOCUS DETECTION (census) at intra-surah verse boundaries
# ----------------------------------------------------------------------------
PERSON_NAME = {1: "1st", 2: "2nd", 3: "3rd"}

def classify_person(a, b):
    return f"{PERSON_NAME[a]}->{PERSON_NAME[b]}"

loci = []                       # every locus, full coordinates
cat_person = Counter()          # person-shift category census
cat_number = Counter()          # number-shift category census
i_we_loci = []                  # 1S<->1P divine majesty subtype
ghayba_huddur = Counter()       # absent<->present (3 <-> {1,2})

# region boundary counts
boundaries_region = Counter()   # 'meccan'/'medinan' -> # intra-surah boundaries
loci_region       = Counter()   # 'meccan'/'medinan' -> # iltifāt loci
boundaries_half   = Counter()   # 'le50'/'gt50'
loci_half         = Counter()

# verb-only replication dominant
dom_person_vo = {}
for s in range(1, N_SURAH + 1):
    for v in range(1, SURAH_NV[s] + 1):
        segs = [seg for seg in verse_segs.get((s, v), []) if seg[3]]  # verbs only
        dom_person_vo[(s, v)] = dominant(segs, 0)
loci_region_vo = Counter()      # verb-only replication

for s in range(1, N_SURAH + 1):
    region = SURAH_TYPE[s]
    half   = "le50" if s <= 50 else "gt50"
    for v in range(1, SURAH_NV[s]):       # boundaries (v, v+1) within surah
        boundaries_region[region] += 1
        boundaries_half[half]     += 1

        pa, pb = dom_person[(s, v)], dom_person[(s, v + 1)]
        na, nb = dom_number[(s, v)], dom_number[(s, v + 1)]

        person_shift = (pa is not None and pb is not None and pa != pb)
        number_shift = (na is not None and nb is not None and na != nb)

        # verb-only person shift (replication)
        pav, pbv = dom_person_vo[(s, v)], dom_person_vo[(s, v + 1)]
        if pav is not None and pbv is not None and pav != pbv:
            loci_region_vo[region] += 1

        if not (person_shift or number_shift):
            continue

        # --- it's a locus ---
        loci_region[region] += 1
        loci_half[half]     += 1

        rec = {"surah": s, "from_v": v, "to_v": v + 1, "region": region,
               "person_from": pa, "person_to": pb,
               "number_from": na, "number_to": nb,
               "person_shift": person_shift, "number_shift": number_shift}
        if person_shift:
            ckey = classify_person(pa, pb)
            cat_person[ckey] += 1
            rec["person_category"] = ckey
            # ghayba <-> huddur: 3rd <-> (1st or 2nd)
            if (pa == 3 and pb in (1, 2)):
                ghayba_huddur[f"ghayba->huddur ({classify_person(pa,pb)})"] += 1
            elif (pa in (1, 2) and pb == 3):
                ghayba_huddur[f"huddur->ghayba ({classify_person(pa,pb)})"] += 1
        if number_shift:
            nkey = f"{na}->{nb}"
            cat_number[nkey] += 1
            rec.setdefault("number_category", nkey)
        loci.append(rec)

# I<->We majesty-iltifāt subtype: dominant person stays 1st across the boundary while the
# grammatical NUMBER flips (singular "I" <-> plural "We" of divine majesty). Collected post-loop
# so the JSON list and the census count are guaranteed identical.
for L in loci:
    if (L["person_from"] == 1 and L["person_to"] == 1
            and L.get("number_from") is not None and L.get("number_to") is not None
            and L["number_from"] != L["number_to"]):
        i_we_loci.append({"surah": L["surah"], "from_v": L["from_v"], "to_v": L["to_v"],
                          "from_number": L["number_from"], "to_number": L["number_to"]})
iwe_count = len(i_we_loci)

# ----------------------------------------------------------------------------
# 5. PRIMARY DIRECTION-LOCKED DENSITY TEST (Meccan > Medinan)
# ----------------------------------------------------------------------------
def density(loci_c, bnd_c, region):
    b = bnd_c[region]
    return (loci_c[region] / b) if b else 0.0

dens_mecc = density(loci_region, boundaries_region, "meccan")
dens_med  = density(loci_region, boundaries_region, "medinan")
delta_obs = dens_mecc - dens_med

# per-surah loci + boundaries for label shuffle
surah_loci = defaultdict(int)
surah_bnd  = defaultdict(int)
for s in range(1, N_SURAH + 1):
    surah_bnd[s] = SURAH_NV[s] - 1
for L in loci:
    surah_loci[L["surah"]] += 1

orig_labels = [SURAH_TYPE[s] for s in range(1, N_SURAH + 1)]
rng = random.Random(SEED)
ge = 0
for _ in range(N_PERM):
    perm = orig_labels[:]
    rng.shuffle(perm)
    lm = bm = lme = bme = 0
    for idx, s in enumerate(range(1, N_SURAH + 1)):
        if perm[idx] == "meccan":
            lm += surah_loci[s]; bm += surah_bnd[s]
        else:
            lme += surah_loci[s]; bme += surah_bnd[s]
    dm  = lm / bm if bm else 0.0
    dme = lme / bme if bme else 0.0
    if (dm - dme) >= delta_obs:
        ge += 1
p_primary = (ge + 1) / (N_PERM + 1)

# secondary split s<=50 vs s>50 (label shuffle on the s<=50/s>50 partition by surah)
dens_le = density(loci_half, boundaries_half, "le50")
dens_gt = density(loci_half, boundaries_half, "gt50")
delta_half_obs = dens_le - dens_gt
half_labels = ["le50" if s <= 50 else "gt50" for s in range(1, N_SURAH + 1)]
rng2 = random.Random(SEED)
ge_half = 0
for _ in range(N_PERM):
    perm = half_labels[:]
    rng2.shuffle(perm)
    le = ble = gt = bgt = 0
    for idx, s in enumerate(range(1, N_SURAH + 1)):
        if perm[idx] == "le50":
            le += surah_loci[s]; ble += surah_bnd[s]
        else:
            gt += surah_loci[s]; bgt += surah_bnd[s]
    dle = le / ble if ble else 0.0
    dgt = gt / bgt if bgt else 0.0
    if (dle - dgt) >= delta_half_obs:
        ge_half += 1
p_half = (ge_half + 1) / (N_PERM + 1)

# verb-only replication density direction
dens_mecc_vo = loci_region_vo["meccan"]  / boundaries_region["meccan"]
dens_med_vo  = loci_region_vo["medinan"] / boundaries_region["medinan"]
delta_vo = dens_mecc_vo - dens_med_vo

# ----------------------------------------------------------------------------
# 6. RECALL benchmark vs Abdel Haleem ground truth (person-iltifāt verses)
# ----------------------------------------------------------------------------
def parse_catalog_verses(path):
    """Pull all 'S:V' references from Categories I (person) and II (number) lists."""
    txt = open(path, encoding="utf-8").read()
    person_verses = set()
    number_verses = set()
    # crude but robust: grab the four person sub-lists + number list blocks
    def grab(after_marker, stop_markers):
        i = txt.find(after_marker)
        if i < 0:
            return ""
        j = len(txt)
        for sm in stop_markers:
            k = txt.find(sm, i + len(after_marker))
            if k >= 0:
                j = min(j, k)
        return txt[i + len(after_marker):j]
    refrx = re.compile(r"(\d+):(\d+)")
    for blk_marker, target in [
        ("**1. 3rd → 1st**", person_verses),
        ("**2. 1st → 3rd**", person_verses),
        ("**3. 3rd → 2nd**", person_verses),
        ("**4. 2nd → 3rd**", person_verses),
        ("### Category II — Change in Number", number_verses),
    ]:
        stops = ["**2. 1st → 3rd**", "**3. 3rd → 2nd**", "**4. 2nd → 3rd**",
                 "**5. 1st → 2nd**", "### Category III", "### Category IV",
                 "## Classical scholars"]
        blk = grab(blk_marker, [s for s in stops if s != blk_marker])
        for s, v in refrx.findall(blk):
            target.add((int(s), int(v)))
    return person_verses, number_verses

gt_person, gt_number = parse_catalog_verses(CATALOG)
# our detected loci as (surah, from_v) AND (surah, to_v) — the catalog references either endpoint
detected_person_pairs = set()
detected_number_pairs = set()
for L in loci:
    if L["person_shift"]:
        detected_person_pairs.add((L["surah"], L["from_v"]))
        detected_person_pairs.add((L["surah"], L["to_v"]))
    if L["number_shift"]:
        detected_number_pairs.add((L["surah"], L["from_v"]))
        detected_number_pairs.add((L["surah"], L["to_v"]))

def recall(gt, detected):
    if not gt:
        return None
    hit = sum(1 for x in gt if x in detected)
    return {"gt_n": len(gt), "detected_hit": hit, "recall": hit / len(gt)}

recall_person = recall(gt_person, detected_person_pairs)
recall_number = recall(gt_number, detected_number_pairs)

# ----------------------------------------------------------------------------
# 7. Verdict
# ----------------------------------------------------------------------------
direction_held = delta_obs > 0
significant    = p_primary < 0.05
if not direction_held:
    verdict = "NULL (pre-commit direction reversed: Medinan denser)"
elif significant:
    verdict = "DIRECTIONAL (Meccan > Medinan, p<0.05, single planned test)"
else:
    verdict = "NULL (direction held but not significant)"

# ----------------------------------------------------------------------------
# 8. Assemble + dump JSON
# ----------------------------------------------------------------------------
# top per-surah loci density (descriptive)
surah_density = []
for s in range(1, N_SURAH + 1):
    b = surah_bnd[s]
    surah_density.append({"surah": s, "name": next(x["name"] for x in quran if x["id"] == s),
                          "type": SURAH_TYPE[s], "n_verses": SURAH_NV[s],
                          "boundaries": b, "loci": surah_loci[s],
                          "density": (surah_loci[s] / b) if b else None})

out = {
    "id": "H-NEW-2200",
    "title": "Iltifāt (grammatical-person shift) corpus map",
    "prereg_sha256": PREREG_SHA,
    "seed": SEED, "n_perm": N_PERM,
    "rules_tuple": "no-tashkeel; QAC v0.4 segments; finite V + PRON person-number; "
                   "dominant=modal,tie->later; intra-surah boundaries; Hafs-Kufan",
    "corpus": {"surahs": N_SURAH, "verses": N_VERSE,
               "intra_surah_boundaries": sum(surah_bnd.values())},
    "census": {
        "total_loci": len(loci),
        "person_shift_loci": sum(1 for L in loci if L["person_shift"]),
        "number_shift_loci": sum(1 for L in loci if L["number_shift"]),
        "both_in_one_locus": sum(1 for L in loci if L["person_shift"] and L["number_shift"]),
        "person_categories": dict(cat_person.most_common()),
        "number_categories": dict(cat_number.most_common()),
        "ghayba_huddur": dict(ghayba_huddur.most_common()),
        "i_we_majesty_loci_count": iwe_count,
    },
    "primary_test_meccan_vs_medinan": {
        "density_meccan": dens_mecc, "density_medinan": dens_med,
        "loci_meccan": loci_region["meccan"], "loci_medinan": loci_region["medinan"],
        "boundaries_meccan": boundaries_region["meccan"],
        "boundaries_medinan": boundaries_region["medinan"],
        "delta_obs": delta_obs, "p_value": p_primary, "alpha": 0.05,
        "direction_locked": "meccan > medinan",
        "direction_held": direction_held, "significant": significant,
    },
    "secondary_test_position_le50_vs_gt50": {
        "density_le50": dens_le, "density_gt50": dens_gt,
        "delta_obs": delta_half_obs, "p_value": p_half,
    },
    "replication_verb_only": {
        "density_meccan": dens_mecc_vo, "density_medinan": dens_med_vo,
        "delta_obs": delta_vo, "direction_held": delta_vo > 0,
    },
    "recall_vs_abdel_haleem": {"person": recall_person, "number": recall_number},
    "verdict": verdict,
    "i_we_majesty_loci": i_we_loci,
    "per_surah_density": surah_density,
    "all_loci": loci,
}
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ----------------------------------------------------------------------------
# 9. Console report
# ----------------------------------------------------------------------------
print("\n================ H-NEW-2200 ILTIFĀT CORPUS MAP ================")
print(f"intra-surah boundaries: {sum(surah_bnd.values())}")
print(f"TOTAL iltifāt loci: {len(loci)}  "
      f"(person={out['census']['person_shift_loci']}, number={out['census']['number_shift_loci']}, "
      f"both={out['census']['both_in_one_locus']})")
print("\nPerson-shift categories:")
for k, c in cat_person.most_common():
    print(f"   {k:14s} {c}")
print("\nNumber-shift categories (top):")
for k, c in cat_number.most_common(10):
    print(f"   {k:8s} {c}")
print(f"\nI<->We majesty-iltifāt loci (1st-person SG<->PL): {iwe_count}")
print("\nGhayba<->Ḥuḍūr (absent<->present):")
for k, c in ghayba_huddur.most_common():
    print(f"   {k:30s} {c}")
print("\n--- PRIMARY direction-locked test: Meccan > Medinan ---")
print(f"   density Meccan  = {dens_mecc:.4f}  ({loci_region['meccan']}/{boundaries_region['meccan']})")
print(f"   density Medinan = {dens_med:.4f}  ({loci_region['medinan']}/{boundaries_region['medinan']})")
print(f"   Δ = {delta_obs:+.4f}   p = {p_primary:.4f}   direction_held={direction_held}")
print(f"\n--- secondary s<=50 vs s>50 ---")
print(f"   density s<=50={dens_le:.4f}  s>50={dens_gt:.4f}  Δ={delta_half_obs:+.4f}  p={p_half:.4f}")
print(f"\n--- verb-only replication ---")
print(f"   Meccan={dens_mecc_vo:.4f}  Medinan={dens_med_vo:.4f}  Δ={delta_vo:+.4f}  held={delta_vo>0}")
print(f"\n--- recall vs Abdel Haleem ground truth ---")
print(f"   person: {recall_person}")
print(f"   number: {recall_number}")
print(f"\nVERDICT: {verdict}")
print(f"JSON -> {OUT_JSON}")
