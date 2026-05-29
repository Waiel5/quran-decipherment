#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2390 — Clause-scale (within-verse) iltifāt detector.

Where H-NEW-2200 collapsed each verse to a single DOMINANT grammatical person/number
and flagged changes across verse BOUNDARIES, this detector scans the ORDERED sequence
of finite-verb / pronoun person-number STATES INSIDE each verse and flags every
within-verse (clause-scale) shift — the true locus of classical iltifāt
(Q 1:5 iyyāka naʿbudu…; Q 10:22 the ship-storm). It then runs the two pre-registered
direction-locked density tests (H1 Meccan>Medinan; H2 short-mufaṣṣal>rest), a
surah-label-shuffle permutation null (seed 20260509, 10000 perms, Bonferroni-2),
MW-5 replication (seed 20260510 + verb-only), and MW-6 recall vs Abdel Haleem.

Pre-reg SHA-256 verified at runtime. Every number computed from disk.
Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, re, os, sys, hashlib, random
from collections import Counter, defaultdict

# ----------------------------------------------------------------------------
# 0. Paths + pre-reg SHA lock
# ----------------------------------------------------------------------------
ROOT     = "/Users/grey/Downloads/quran"
PREREG   = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2390-clause-iltifat.md")
QURAN    = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
QAC      = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
CATALOG  = os.path.join(ROOT, "data/literature/classical-tafsir/abdel-haleem-iltifat-catalog.md")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2390.json")

PREREG_SHA = "ea2d6fda596c17dbe82ff152c111895b0d273acc5f6a68dd591466cabc1db304"
SEED       = 20260509
SEED2      = 20260510   # MW-5 replication seed
N_PERM     = 10000
SHORT_MUFASSAL_S = 78   # s>=78 short-mufaṣṣal cut (matches H-NEW-2210 / H-NEW-2250)

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
quran      = json.load(open(QURAN, encoding="utf-8"))
SURAH_TYPE = {s["id"]: s["type"] for s in quran}        # 'meccan' / 'medinan'
SURAH_NV   = {s["id"]: len(s["verses"]) for s in quran} # verse count
SURAH_NAME = {s["id"]: s["name"] for s in quran}
N_SURAH    = len(quran)
N_VERSE    = sum(SURAH_NV.values())
print(f"[data] surahs={N_SURAH}  verses={N_VERSE}  "
      f"meccan={sum(1 for t in SURAH_TYPE.values() if t=='meccan')}  "
      f"medinan={sum(1 for t in SURAH_TYPE.values() if t=='medinan')}")

# ----------------------------------------------------------------------------
# 2. Parse QAC into an ORDERED within-verse state sequence per verse
# ----------------------------------------------------------------------------
# Person-number-gender regex (with optional PRON: prefix for suffix clitics) — copied
# verbatim from H-NEW-2200 for instrument continuity.
PNG_RE = re.compile(r"^(?:PRON:)?([123])(MS|MP|MD|FS|FP|FD|P|S|D)$")
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")

def number_of(numgen):
    if numgen.startswith("M") or numgen.startswith("F"):
        return numgen[1]   # MS->S, MP->P, MD->D, FS->S, FP->P, FD->D
    return numgen          # already S / D / P

# verse_states[(s,v)] = ordered list of (person:int, number:str, word_idx, seg_idx, is_verb)
verse_states = defaultdict(list)

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

        for field in feats.split("|"):
            pm = PNG_RE.match(field)
            if pm:
                person = int(pm.group(1))
                num    = number_of(pm.group(2))
                verse_states[(s, v)].append((person, num, w, seg, is_verb))
                if is_verb:
                    break   # the verb's own subject person-number is one field

# order each verse's states by (word_idx, seg_idx) — left-to-right reading order
for k in verse_states:
    verse_states[k].sort(key=lambda t: (t[2], t[3]))

# ----------------------------------------------------------------------------
# 3. WITHIN-VERSE SHIFT detection (the clause-scale census)
# ----------------------------------------------------------------------------
PERSON_NAME = {1: "1st", 2: "2nd", 3: "3rd"}

def scan_verse(states):
    """Return list of within-verse shifts for one ordered state sequence.
    A shift at position i iff state_i != state_{i+1} in person OR number."""
    shifts = []
    for i in range(len(states) - 1):
        pa, na = states[i][0],   states[i][1]
        pb, nb = states[i+1][0], states[i+1][1]
        person_shift = (pa != pb)
        number_shift = (na != nb)
        if not (person_shift or number_shift):
            continue
        rec = {"pos": i, "person_from": pa, "person_to": pb,
               "number_from": na, "number_to": nb,
               "person_shift": person_shift, "number_shift": number_shift,
               "w_from": states[i][2], "w_to": states[i+1][2]}
        if person_shift and number_shift:
            rec["kind"] = "both"
        elif person_shift:
            rec["kind"] = "person"
        else:
            rec["kind"] = "number"
        shifts.append(rec)
    return shifts

def scan_verse_verbonly(states):
    vo = [st for st in states if st[4]]
    return scan_verse(vo), len(vo)

loci          = []              # one record per within-verse shift, full coords
cat_person    = Counter()
cat_number    = Counter()
ghayba_huddur = Counter()
iwe_loci      = []             # within-verse 1st-person SG<->PL majestic shift

# per-surah accumulators for the permutation tests
surah_shifts   = defaultdict(int)   # within-verse shifts in surah s
surah_adjs     = defaultdict(int)   # within-verse adjacencies (sum over eligible verses of m-1)
surah_elig_v   = defaultdict(int)   # verses with >=2 states
surah_shift_v  = defaultdict(int)   # verses with >=1 within-verse shift
# verb-only replication accumulators
surah_shifts_vo = defaultdict(int)
surah_adjs_vo   = defaultdict(int)

per_verse_records = []         # descriptive per-verse rows (only verses with a shift)

for s in range(1, N_SURAH + 1):
    for v in range(1, SURAH_NV[s] + 1):
        states = verse_states.get((s, v), [])
        m = len(states)
        if m >= 2:
            surah_elig_v[s] += 1
            surah_adjs[s]   += (m - 1)
        shifts = scan_verse(states)
        if shifts:
            surah_shift_v[s] += 1
            surah_shifts[s]  += len(shifts)
            for sh in shifts:
                rec = dict(sh); rec["surah"] = s; rec["verse"] = v
                loci.append(rec)
                if sh["person_shift"]:
                    ck = f"{PERSON_NAME[sh['person_from']]}->{PERSON_NAME[sh['person_to']]}"
                    cat_person[ck] += 1
                    if sh["person_from"] == 3 and sh["person_to"] in (1, 2):
                        ghayba_huddur[f"ghayba->huddur ({ck})"] += 1
                    elif sh["person_from"] in (1, 2) and sh["person_to"] == 3:
                        ghayba_huddur[f"huddur->ghayba ({ck})"] += 1
                if sh["number_shift"]:
                    cat_number[f"{sh['number_from']}->{sh['number_to']}"] += 1
                # I<->We majestic plural: person stays 1st, number flips
                if (sh["person_from"] == 1 and sh["person_to"] == 1
                        and sh["number_from"] != sh["number_to"]):
                    iwe_loci.append({"surah": s, "verse": v, "pos": sh["pos"],
                                     "from_number": sh["number_from"],
                                     "to_number": sh["number_to"]})
            per_verse_records.append({"surah": s, "verse": v, "n_states": m,
                                      "n_shifts": len(shifts)})
        # verb-only replication
        vo_shifts, m_vo = scan_verse_verbonly(states)
        if m_vo >= 2:
            surah_adjs_vo[s] += (m_vo - 1)
            surah_shifts_vo[s] += len(vo_shifts)

total_loci   = len(loci)
total_adjs   = sum(surah_adjs.values())
total_elig_v = sum(surah_elig_v.values())
total_shiftv = sum(surah_shift_v.values())

# ----------------------------------------------------------------------------
# 4. Densities + region / register direction-locked tests
# ----------------------------------------------------------------------------
def grp_density_adj(predicate, shifts_d, adjs_d):
    sh = sum(shifts_d[s] for s in range(1, N_SURAH+1) if predicate(s))
    ad = sum(adjs_d[s]   for s in range(1, N_SURAH+1) if predicate(s))
    return (sh / ad) if ad else 0.0, sh, ad

def grp_density_verse(predicate):
    sv = sum(surah_shift_v[s] for s in range(1, N_SURAH+1) if predicate(s))
    ev = sum(surah_elig_v[s]  for s in range(1, N_SURAH+1) if predicate(s))
    return (sv / ev) if ev else 0.0, sv, ev

is_mecc = lambda s: SURAH_TYPE[s] == "meccan"
is_med  = lambda s: SURAH_TYPE[s] == "medinan"
is_short = lambda s: s >= SHORT_MUFASSAL_S
is_rest  = lambda s: s <  SHORT_MUFASSAL_S

# ---- per-adjacency densities (PRIMARY statistic) ----
dadj_mecc, sh_mecc, ad_mecc = grp_density_adj(is_mecc, surah_shifts, surah_adjs)
dadj_med,  sh_med,  ad_med  = grp_density_adj(is_med,  surah_shifts, surah_adjs)
delta_region = dadj_mecc - dadj_med

dadj_short, sh_sh, ad_sh = grp_density_adj(is_short, surah_shifts, surah_adjs)
dadj_rest,  sh_re, ad_re = grp_density_adj(is_rest,  surah_shifts, surah_adjs)
delta_register = dadj_short - dadj_rest

# ---- per-verse densities (MW-3 alternative normalisation) ----
dv_mecc, _, _ = grp_density_verse(is_mecc)
dv_med,  _, _ = grp_density_verse(is_med)
delta_region_verse = dv_mecc - dv_med

# ---- permutation null: shuffle surah labels (surah = exchangeable unit) ----
def perm_p_adj(label_of, target_labels, delta_obs, shifts_d, adjs_d, seed):
    """One-sided p for D_adj(group A) - D_adj(group B) >= delta_obs under surah-label
    shuffle. target_labels=(A_label, B_label)."""
    A, B = target_labels
    labels = [label_of(s) for s in range(1, N_SURAH+1)]
    shifts_arr = [shifts_d[s] for s in range(1, N_SURAH+1)]
    adjs_arr   = [adjs_d[s]   for s in range(1, N_SURAH+1)]
    rng = random.Random(seed)
    ge = 0
    for _ in range(N_PERM):
        perm = labels[:]; rng.shuffle(perm)
        shA=adA=shB=adB=0
        for i in range(N_SURAH):
            if perm[i] == A:
                shA += shifts_arr[i]; adA += adjs_arr[i]
            elif perm[i] == B:
                shB += shifts_arr[i]; adB += adjs_arr[i]
        dA = shA/adA if adA else 0.0
        dB = shB/adB if adB else 0.0
        if (dA - dB) >= delta_obs:
            ge += 1
    return (ge + 1) / (N_PERM + 1)

region_label   = lambda s: SURAH_TYPE[s]
register_label = lambda s: "short" if s >= SHORT_MUFASSAL_S else "rest"

p_region   = perm_p_adj(region_label,   ("meccan", "medinan"), delta_region,   surah_shifts, surah_adjs, SEED)
p_register = perm_p_adj(register_label, ("short",  "rest"),    delta_register, surah_shifts, surah_adjs, SEED)

# ---- MW-5 replication: second seed + verb-only ----
p_region_seed2 = perm_p_adj(region_label, ("meccan","medinan"), delta_region, surah_shifts, surah_adjs, SEED2)

dadj_mecc_vo, _, _ = grp_density_adj(is_mecc, surah_shifts_vo, surah_adjs_vo)
dadj_med_vo,  _, _ = grp_density_adj(is_med,  surah_shifts_vo, surah_adjs_vo)
delta_region_vo = dadj_mecc_vo - dadj_med_vo

ALPHA_BON = 0.025  # Bonferroni k=2

# ----------------------------------------------------------------------------
# 5. MW-6 recall vs Abdel Haleem ground truth (clause-scale: verse carries >=1 shift)
# ----------------------------------------------------------------------------
def parse_catalog_verses(path):
    txt = open(path, encoding="utf-8").read()
    person_verses, number_verses = set(), set()
    def grab(after_marker, stop_markers):
        i = txt.find(after_marker)
        if i < 0: return ""
        j = len(txt)
        for sm in stop_markers:
            k = txt.find(sm, i + len(after_marker))
            if k >= 0: j = min(j, k)
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
        blk = grab(blk_marker, [x for x in stops if x != blk_marker])
        for s, vv in refrx.findall(blk):
            target.add((int(s), int(vv)))
    return person_verses, number_verses

gt_person, gt_number = parse_catalog_verses(CATALOG)
detected_person = set()
detected_number = set()
for L in loci:
    if L["person_shift"]:
        detected_person.add((L["surah"], L["verse"]))
    if L["number_shift"]:
        detected_number.add((L["surah"], L["verse"]))

def recall(gt, det):
    if not gt: return None
    hit = sum(1 for x in gt if x in det)
    return {"gt_n": len(gt), "hit": hit, "recall": hit/len(gt)}

recall_person = recall(gt_person, detected_person)
recall_number = recall(gt_number, detected_number)

# flagship loci check (must fire within-verse)
flagship = {}
for (s, v) in [(1,5),(10,22),(27,60),(36,22),(108,2)]:
    sh = scan_verse(verse_states.get((s, v), []))
    flagship[f"{s}:{v}"] = {"n_states": len(verse_states.get((s,v),[])),
                            "n_within_verse_shifts": len(sh),
                            "kinds": [x["kind"] for x in sh]}

# ----------------------------------------------------------------------------
# 6. Verdict
# ----------------------------------------------------------------------------
h1_held = delta_region   > 0
h2_held = delta_register > 0
h1_pass = h1_held and (p_region   < ALPHA_BON)
h2_pass = h2_held and (p_register < ALPHA_BON)

if h1_pass and h2_pass:
    verdict = "CONFIRMED — clause scale recovers genre signal (H1 region + H2 register both pass)"
elif h1_pass and not h2_pass:
    verdict = "CONFIRMED-PRIMARY — H1 Meccan>Medinan recovered at clause scale (H2 register not significant)"
elif h2_pass and not h1_pass:
    verdict = "PARTIAL — H2 register enrichment passes; H1 region does not"
else:
    flags = []
    if not h1_held: flags.append("H1 direction REVERSED (pre-commit violation)")
    if not h2_held: flags.append("H2 direction REVERSED (pre-commit violation)")
    verdict = "NULL — neither locked cell passes" + (" [" + "; ".join(flags) + "]" if flags else "")

# ----------------------------------------------------------------------------
# 7. Per-surah descriptive density (clause scale) + densest surahs
# ----------------------------------------------------------------------------
per_surah = []
for s in range(1, N_SURAH + 1):
    ad = surah_adjs[s]; ev = surah_elig_v[s]
    per_surah.append({"surah": s, "name": SURAH_NAME[s], "type": SURAH_TYPE[s],
                      "n_verses": SURAH_NV[s], "within_verse_shifts": surah_shifts[s],
                      "within_verse_adjacencies": ad,
                      "eligible_verses": ev, "verses_with_shift": surah_shift_v[s],
                      "density_adj": (surah_shifts[s]/ad) if ad else None,
                      "density_verse": (surah_shift_v[s]/ev) if ev else None})
densest = sorted([d for d in per_surah if d["within_verse_adjacencies"] >= 20],
                 key=lambda d: d["density_adj"], reverse=True)[:12]

# ----------------------------------------------------------------------------
# 8. Comparison to H-NEW-2200 boundary census
# ----------------------------------------------------------------------------
cmp_2200 = None
H2200_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2200.json")
if os.path.exists(H2200_JSON):
    j = json.load(open(H2200_JSON, encoding="utf-8"))
    pm = j.get("primary_test_meccan_vs_medinan", {})
    cmp_2200 = {
        "boundary_density_meccan": pm.get("density_meccan"),
        "boundary_density_medinan": pm.get("density_medinan"),
        "boundary_delta": pm.get("delta_obs"),
        "boundary_p": pm.get("p_value"),
        "boundary_direction_held": pm.get("direction_held"),
        "boundary_total_loci": j.get("census", {}).get("total_loci"),
        "clause_density_meccan_adj": dadj_mecc,
        "clause_density_medinan_adj": dadj_med,
        "clause_delta_adj": delta_region,
        "clause_p": p_region,
        "clause_direction_held": h1_held,
        "clause_total_loci": total_loci,
    }

# ----------------------------------------------------------------------------
# 9. Dump JSON
# ----------------------------------------------------------------------------
out = {
    "id": "H-NEW-2390",
    "title": "Clause-scale (within-verse) iltifāt detector",
    "prereg_sha256": PREREG_SHA, "seed": SEED, "seed_replication": SEED2,
    "n_perm": N_PERM, "alpha_bonferroni_k2": ALPHA_BON,
    "rules_tuple": "no-tashkeel; QAC v0.4 segments; finite V (incl IMPV) + PRON "
                   "person-number; ordered within-verse sequence; adjacent-pair shift; "
                   "Hafs-Kufan; Mashriqi",
    "corpus": {"surahs": N_SURAH, "verses": N_VERSE,
               "eligible_verses_ge2_states": total_elig_v,
               "within_verse_adjacencies": total_adjs},
    "census": {
        "total_within_verse_shifts": total_loci,
        "verses_with_within_verse_shift": total_shiftv,
        "person_shifts": sum(1 for L in loci if L["person_shift"]),
        "number_shifts": sum(1 for L in loci if L["number_shift"]),
        "both_in_one_shift": sum(1 for L in loci if L["kind"] == "both"),
        "person_categories": dict(cat_person.most_common()),
        "number_categories": dict(cat_number.most_common()),
        "ghayba_huddur": dict(ghayba_huddur.most_common()),
        "i_we_majesty_within_verse_loci_count": len(iwe_loci),
    },
    "h1_region_meccan_vs_medinan": {
        "stat": "per-adjacency density (PRIMARY)",
        "density_meccan": dadj_mecc, "density_medinan": dadj_med,
        "shifts_meccan": sh_mecc, "adjs_meccan": ad_mecc,
        "shifts_medinan": sh_med, "adjs_medinan": ad_med,
        "delta_obs": delta_region, "p_value": p_region,
        "direction_locked": "meccan > medinan",
        "direction_held": h1_held, "pass": h1_pass,
        "p_value_seed2": p_region_seed2,
        "per_verse_density_meccan": dv_mecc, "per_verse_density_medinan": dv_med,
        "per_verse_delta": delta_region_verse,
        "verb_only_density_meccan": dadj_mecc_vo,
        "verb_only_density_medinan": dadj_med_vo,
        "verb_only_delta": delta_region_vo,
        "verb_only_direction_held": delta_region_vo > 0,
    },
    "h2_register_short_mufassal": {
        "stat": "per-adjacency density, s>=78 vs s<78",
        "density_short": dadj_short, "density_rest": dadj_rest,
        "shifts_short": sh_sh, "adjs_short": ad_sh,
        "shifts_rest": sh_re, "adjs_rest": ad_re,
        "delta_obs": delta_register, "p_value": p_register,
        "direction_locked": "short-mufassal (s>=78) > rest",
        "direction_held": h2_held, "pass": h2_pass,
    },
    "comparison_to_h_new_2200_boundary": cmp_2200,
    "recall_vs_abdel_haleem": {"person": recall_person, "number": recall_number},
    "flagship_within_verse": flagship,
    "verdict": verdict,
    "densest_surahs_clause_scale": densest,
    "i_we_majesty_within_verse_loci": iwe_loci,
    "per_surah": per_surah,
    "all_loci": loci,
}
os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# ----------------------------------------------------------------------------
# 10. Console report
# ----------------------------------------------------------------------------
print("\n============ H-NEW-2390 CLAUSE-SCALE ILTIFĀT ============")
print(f"eligible verses (>=2 states): {total_elig_v}   within-verse adjacencies: {total_adjs}")
print(f"TOTAL within-verse shifts: {total_loci}  in {total_shiftv} verses  "
      f"(person={out['census']['person_shifts']}, number={out['census']['number_shifts']}, "
      f"both={out['census']['both_in_one_shift']})")
print("\nPerson-shift categories (within-verse):")
for k, c in cat_person.most_common():
    print(f"   {k:14s} {c}")
print("\nNumber-shift categories (top):")
for k, c in cat_number.most_common(8):
    print(f"   {k:8s} {c}")
print(f"\nI<->We majestic-plural within-verse loci: {len(iwe_loci)}")
print("\nGhayba<->Ḥuḍūr (within-verse):")
for k, c in ghayba_huddur.most_common():
    print(f"   {k:30s} {c}")
print("\n--- flagship loci (must fire within verse) ---")
for k, d in flagship.items():
    print(f"   Q {k:7s} states={d['n_states']:2d}  within-verse-shifts={d['n_within_verse_shifts']:2d}  {d['kinds']}")
print("\n--- H1 PRIMARY (per-adjacency): Meccan > Medinan ---")
print(f"   Meccan  = {dadj_mecc:.4f}  ({sh_mecc}/{ad_mecc})")
print(f"   Medinan = {dadj_med:.4f}  ({sh_med}/{ad_med})")
print(f"   Δ = {delta_region:+.4f}   p = {p_region:.4f} (seed2 p={p_region_seed2:.4f})   "
      f"held={h1_held}  pass(α=.025)={h1_pass}")
print(f"   [per-verse norm] Meccan={dv_mecc:.4f} Medinan={dv_med:.4f} Δ={delta_region_verse:+.4f}")
print(f"   [verb-only]      Meccan={dadj_mecc_vo:.4f} Medinan={dadj_med_vo:.4f} "
      f"Δ={delta_region_vo:+.4f} held={delta_region_vo>0}")
print("\n--- H2 SECONDARY (per-adjacency): short-mufaṣṣal (s>=78) > rest ---")
print(f"   short = {dadj_short:.4f}  ({sh_sh}/{ad_sh})   rest = {dadj_rest:.4f}  ({sh_re}/{ad_re})")
print(f"   Δ = {delta_register:+.4f}   p = {p_register:.4f}   held={h2_held}  pass(α=.025)={h2_pass}")
print("\n--- recall vs Abdel Haleem (clause scale) ---")
print(f"   person: {recall_person}")
print(f"   number: {recall_number}")
if cmp_2200:
    print("\n--- comparison to H-NEW-2200 BOUNDARY scale ---")
    print(f"   boundary: Mecc={cmp_2200['boundary_density_meccan']:.4f} "
          f"Med={cmp_2200['boundary_density_medinan']:.4f} "
          f"Δ={cmp_2200['boundary_delta']:+.4f} p={cmp_2200['boundary_p']:.4f} "
          f"held={cmp_2200['boundary_direction_held']}  loci={cmp_2200['boundary_total_loci']}")
    print(f"   clause:   Mecc={cmp_2200['clause_density_meccan_adj']:.4f} "
          f"Med={cmp_2200['clause_density_medinan_adj']:.4f} "
          f"Δ={cmp_2200['clause_delta_adj']:+.4f} p={cmp_2200['clause_p']:.4f} "
          f"held={cmp_2200['clause_direction_held']}  loci={cmp_2200['clause_total_loci']}")
print("\n--- densest surahs (clause scale, >=20 adjacencies) ---")
for d in densest:
    print(f"   Q{d['surah']:3d} {d['name']:14s} {d['type']:7s} "
          f"D_adj={d['density_adj']:.3f}  ({d['within_verse_shifts']}/{d['within_verse_adjacencies']})")
print(f"\nVERDICT: {verdict}")
print(f"JSON -> {OUT_JSON}")
