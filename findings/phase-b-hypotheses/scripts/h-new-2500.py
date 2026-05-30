#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2500 — Iltifāt TYPE × GENRE cross-tabulation.

REUSES the H-NEW-2390 within-verse iltifāt locus catalogue (csv/h-new-2390.json) — the
clause-scale detector is NOT recomputed. Each of the 16,998 within-verse shifts is
tagged with its iltifāt TYPE (5-class: P_3<->1, P_2<->3, P_1<->2, N_S<->P, N_dual) and
its surah's GENRE (4-class deterministic proxy: narrative / legal_medinan /
eschatological_mufassal / liturgical_didactic). We build the 5x4 contingency table and
test type-genre association against a surah-label-permutation null (seed 20260509,
10000 perms, Bonferroni-2 over {chi-square, NMI}); MW-5 replication (seed 20260510);
MW-3 Cramér's V + person-only sub-table; MW-6 reproduces the 2390 census marginals.

Pre-reg SHA-256 verified at runtime. Every number computed from disk.
Author: Waiel Al-Shujaa. Bismillāhi al-Raḥmāni al-Raḥīm.
"""
import json, os, sys, hashlib, random, math
from collections import Counter, defaultdict

# ----------------------------------------------------------------------------
# 0. Paths + pre-reg SHA lock
# ----------------------------------------------------------------------------
ROOT     = "/Users/grey/Downloads/quran"
PREREG   = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2500-iltifat-genre-crosstab.md")
QURAN    = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
LOCI     = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2390.json")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2500.json")

PREREG_SHA = "ced7003da523afc2ebb83e08027422c07a4e9137ccd4dfd6463c455b8b625d4c"
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
# 1. Load Quran metadata + build the LOCKED genre proxy (surah-scale)
# ----------------------------------------------------------------------------
quran = json.load(open(QURAN, encoding="utf-8"))
META  = {s["id"]: (s["type"], len(s["verses"])) for s in quran}
TXT   = {s["id"]: [v["text"] for v in s["verses"]] for s in quran}
NAME  = {s["id"]: s["name"] for s in quran}

def cnt(sid, pat):  return sum(t.count(pat) for t in TXT[sid])
def words(sid):     return sum(len(t.split()) for t in TXT[sid])

LEGAL_MARKERS  = ["يا أيها الذين آمنوا", "كتب عليكم"]
ESCHAT_MARKERS = ["يوم القيامة", "الساعة", "يومئذ", "جهنم", "إذا "]
QALA           = "قال"

def genre_of(sid):
    typ, nv = META[sid]
    w = words(sid)
    leg  = sum(cnt(sid, p) for p in LEGAL_MARKERS)
    escd = 100.0 * sum(cnt(sid, p) for p in ESCHAT_MARKERS) / w
    nard = 100.0 * cnt(sid, QALA) / w
    # LOCKED hierarchical priority (first match wins):
    if typ == "medinan" and leg >= 1:
        return "legal_medinan"
    if nard >= 1.0:
        return "narrative"
    if sid >= SHORT_MUFASSAL_S or escd >= 1.5:
        return "eschatological_mufassal"
    return "liturgical_didactic"

GENRES = ["narrative", "legal_medinan", "eschatological_mufassal", "liturgical_didactic"]
SURAH_GENRE = {sid: genre_of(sid) for sid in range(1, 115)}
genre_members = defaultdict(list)
for sid, g in SURAH_GENRE.items():
    genre_members[g].append(sid)
print("[genre proxy]")
for g in GENRES:
    print(f"   {g:26s} n={len(genre_members[g]):3d}  {genre_members[g]}")

# ----------------------------------------------------------------------------
# 2. Load + REUSE the H-NEW-2390 locus catalogue (detector NOT recomputed)
# ----------------------------------------------------------------------------
d2390 = json.load(open(LOCI, encoding="utf-8"))
all_loci = d2390["all_loci"]
print(f"[reuse] h-new-2390.json: {len(all_loci)} within-verse loci "
      f"(prereg {d2390['prereg_sha256'][:12]}…)")

# MW-6: reproduce the 2390 census marginals by assertion (fail-fast on misread JSON)
n_person = sum(1 for l in all_loci if l["person_shift"])
n_number = sum(1 for l in all_loci if l["number_shift"])
assert n_person == 12379, f"person-shift marginal {n_person} != 12379 (2390 census)"
assert n_number == 11584, f"number-shift marginal {n_number} != 11584 (2390 census)"
print(f"[MW-6] census marginals reproduced: person={n_person} number={n_number}")

# ----------------------------------------------------------------------------
# 3. Tag each locus with its iltifāt TYPE-class(es) (LOCKED 5-class taxonomy)
# ----------------------------------------------------------------------------
TYPES = ["P_3<->1", "P_2<->3", "P_1<->2", "N_S<->P", "N_dual"]
PERSON_TYPES = ["P_3<->1", "P_2<->3", "P_1<->2"]

def type_tags(l):
    tags = []
    if l["person_shift"]:
        a, b = sorted([l["person_from"], l["person_to"]])
        if   (a, b) == (1, 3): tags.append("P_3<->1")
        elif (a, b) == (2, 3): tags.append("P_2<->3")
        elif (a, b) == (1, 2): tags.append("P_1<->2")
    if l["number_shift"]:
        nf, nt = l["number_from"], l["number_to"]
        if   {nf, nt} == {"S", "P"}:           tags.append("N_S<->P")
        elif "D" in (nf, nt) and nf != nt:     tags.append("N_dual")
    return tags

# Build the per-tag records: (surah, type). One locus -> 1+ tags.
tag_records = []          # list of (surah, type)
for l in all_loci:
    s = l["surah"]
    for t in type_tags(l):
        tag_records.append((s, t))

# divine sg<->pl majesty sub-count (person stays 1st, number S<->P) by genre
majesty_by_genre = Counter()
for l in all_loci:
    if (l["person_from"] == 1 and l["person_to"] == 1
            and {l["number_from"], l["number_to"]} == {"S", "P"}):
        majesty_by_genre[SURAH_GENRE[l["surah"]]] += 1

# ----------------------------------------------------------------------------
# 4. Contingency table (TYPE x GENRE) + association statistics
# ----------------------------------------------------------------------------
def build_table(surah_genre_map, types):
    """Return dict[genre][type] -> count, using a given surah->genre assignment."""
    tab = {g: Counter() for g in GENRES}
    for (s, t) in tag_records:
        if t in types:
            tab[surah_genre_map[s]][t] += 1
    return tab

def chi2_and_mi(tab, types):
    """Pearson chi-square, normalised mutual information, Cramér's V over the table."""
    row_tot = {g: sum(tab[g][t] for t in types) for g in GENRES}
    col_tot = {t: sum(tab[g][t] for g in GENRES) for t in types}
    N = sum(row_tot.values())
    chi2 = 0.0
    mi   = 0.0
    for g in GENRES:
        for t in types:
            O = tab[g][t]
            E = row_tot[g] * col_tot[t] / N if N else 0.0
            if E > 0:
                chi2 += (O - E) ** 2 / E
            if O > 0 and row_tot[g] > 0 and col_tot[t] > 0:
                pxy = O / N
                px  = row_tot[g] / N
                py  = col_tot[t] / N
                mi += pxy * math.log(pxy / (px * py))
    # normalise MI by min marginal entropy
    Hrow = -sum((row_tot[g] / N) * math.log(row_tot[g] / N) for g in GENRES if row_tot[g] > 0)
    Hcol = -sum((col_tot[t] / N) * math.log(col_tot[t] / N) for t in types if col_tot[t] > 0)
    nmi  = mi / min(Hrow, Hcol) if min(Hrow, Hcol) > 0 else 0.0
    k    = min(len(GENRES), len(types))
    cramers_v = math.sqrt(chi2 / (N * (k - 1))) if N and k > 1 else 0.0
    return chi2, nmi, cramers_v, row_tot, col_tot, N

def std_residuals(tab, types, row_tot, col_tot, N):
    """Standardized Pearson residuals (O-E)/sqrt(E)."""
    res = {g: {} for g in GENRES}
    for g in GENRES:
        for t in types:
            O = tab[g][t]
            E = row_tot[g] * col_tot[t] / N if N else 0.0
            res[g][t] = (O - E) / math.sqrt(E) if E > 0 else 0.0
    return res

# --- observed (full 5-class) ---
tab_obs = build_table(SURAH_GENRE, TYPES)
chi2_obs, nmi_obs, V_obs, row_tot, col_tot, N = chi2_and_mi(tab_obs, TYPES)
res_obs = std_residuals(tab_obs, TYPES, row_tot, col_tot, N)
print(f"\n[observed] chi2={chi2_obs:.2f}  NMI={nmi_obs:.5f}  Cramér's V={V_obs:.4f}  N={N}")

# --- observed (person-only 3-class, MW-3) ---
tab_po = build_table(SURAH_GENRE, PERSON_TYPES)
chi2_po, nmi_po, V_po, rt_po, ct_po, N_po = chi2_and_mi(tab_po, PERSON_TYPES)
res_po = std_residuals(tab_po, PERSON_TYPES, rt_po, ct_po, N_po)
print(f"[person-only MW-3] chi2={chi2_po:.2f}  NMI={nmi_po:.5f}  V={V_po:.4f}  N={N_po}")

# ----------------------------------------------------------------------------
# 5. Surah-label permutation null (H1) — seed 20260509 + replication 20260510
# ----------------------------------------------------------------------------
def perm_test(seed, types):
    rng = random.Random(seed)
    sids = list(range(1, 115))
    labels = [SURAH_GENRE[s] for s in sids]
    base_tab = build_table(SURAH_GENRE, types)
    chi2_o, nmi_o, _, _, _, _ = chi2_and_mi(base_tab, types)
    ge_chi2 = ge_nmi = 0
    for _ in range(N_PERM):
        perm = labels[:]
        rng.shuffle(perm)
        pm = {sids[i]: perm[i] for i in range(len(sids))}
        ptab = build_table(pm, types)
        c, m, _, _, _, _ = chi2_and_mi(ptab, types)
        if c >= chi2_o: ge_chi2 += 1
        if m >= nmi_o:  ge_nmi  += 1
    p_chi2 = (ge_chi2 + 1) / (N_PERM + 1)
    p_nmi  = (ge_nmi  + 1) / (N_PERM + 1)
    return p_chi2, p_nmi, chi2_o, nmi_o

print(f"\n[H1 permutation null] seed={SEED}, n_perm={N_PERM} …")
p_chi2, p_nmi, _, _ = perm_test(SEED, TYPES)
print(f"   p(chi2) = {p_chi2:.5f}   p(NMI) = {p_nmi:.5f}   (Bonferroni-2 α=0.025)")
print(f"[MW-5 replication] seed={SEED2} …")
p_chi2_r, p_nmi_r, _, _ = perm_test(SEED2, TYPES)
print(f"   p(chi2) = {p_chi2_r:.5f}   p(NMI) = {p_nmi_r:.5f}")
# MW-3 person-only permutation
print(f"[MW-3 person-only permutation] seed={SEED} …")
p_chi2_po, p_nmi_po, _, _ = perm_test(SEED, PERSON_TYPES)
print(f"   p(chi2) = {p_chi2_po:.5f}   p(NMI) = {p_nmi_po:.5f}")

ALPHA_BON = 0.025
h1_pass = (p_chi2 < ALPHA_BON) and (p_nmi < ALPHA_BON)

# ----------------------------------------------------------------------------
# 6. H2 — locked dominant-type predictions (direction checks)
# ----------------------------------------------------------------------------
# Locked: legal_medinan x P_2<->3 residual POSITIVE and largest-in-row;
#         narrative x P_3<->1 residual POSITIVE.
legal_row = res_obs["legal_medinan"]
legal_p23 = legal_row["P_2<->3"]
legal_top_type = max(legal_row, key=legal_row.get)
h2a_pass = (legal_p23 > 0) and (legal_top_type == "P_2<->3")
narr_p31 = res_obs["narrative"]["P_3<->1"]
h2b_pass = (narr_p31 > 0)
h2_pass = h2a_pass and h2b_pass
print(f"\n[H2 locked cell directions]")
print(f"   legal_medinan x P_2<->3 residual = {legal_p23:+.2f}  "
      f"(row-max type = {legal_top_type})  -> {'PASS' if h2a_pass else 'FAIL/REVERSED'}")
print(f"   narrative     x P_3<->1 residual = {narr_p31:+.2f}  "
      f"-> {'PASS' if h2b_pass else 'FAIL/REVERSED'}")

# dominant (largest standardized residual) type per genre — descriptive
dominant_type = {g: max(res_obs[g], key=res_obs[g].get) for g in GENRES}

# ----------------------------------------------------------------------------
# 7. Verdict
# ----------------------------------------------------------------------------
if h1_pass and h2_pass:
    verdict = "CONFIRMED"
elif h1_pass and not h2_pass:
    verdict = "PARTIAL (H1 association PASS; H2 locked direction failed/reversed)"
elif (not h1_pass) and h2_pass:
    verdict = "PARTIAL (H2 direction held; H1 association did not reach Bonferroni)"
else:
    verdict = "NULL"
print(f"\n[VERDICT] H1={'PASS' if h1_pass else 'FAIL'}  H2={'PASS' if h2_pass else 'FAIL'}  => {verdict}")

# ----------------------------------------------------------------------------
# 8. Emit JSON
# ----------------------------------------------------------------------------
def tab_to_dict(tab, types):
    return {g: {t: tab[g][t] for t in types} for g in GENRES}

out = {
    "id": "H-NEW-2500",
    "title": "Iltifāt TYPE × GENRE cross-tabulation",
    "prereg_sha256": PREREG_SHA,
    "parent": "H-NEW-2390 (reused csv/h-new-2390.json; detector NOT recomputed)",
    "seed": SEED,
    "seed_replication": SEED2,
    "n_perm": N_PERM,
    "alpha_bonferroni_k2": ALPHA_BON,
    "rules_tuple": ("no-tashkeel; QAC v0.4 loci via H-NEW-2390; within-verse type-tag; "
                    "surah-scale genre proxy (region + s>=78 length-band + marker-lexicon); "
                    "Hafs-Kufan; Mashriqi"),
    "genre_proxy": {
        "decision_procedure": ["1 legal_medinan: medinan AND (O-believers + kutiba-alaykum)>=1",
                                "2 narrative: qala-density>=1.0/100w",
                                "3 eschatological_mufassal: s>=78 OR eschat-density>=1.5/100w",
                                "4 liturgical_didactic: residual"],
        "legal_markers": LEGAL_MARKERS,
        "eschat_markers": ESCHAT_MARKERS,
        "narrative_marker": QALA,
        "members": {g: genre_members[g] for g in GENRES},
        "n_per_genre": {g: len(genre_members[g]) for g in GENRES},
        "surah_genre": {str(s): SURAH_GENRE[s] for s in range(1, 115)},
    },
    "type_taxonomy": TYPES,
    "n_type_tags": len(tag_records),
    "contingency_table": tab_to_dict(tab_obs, TYPES),
    "row_totals": {g: row_tot[g] for g in GENRES},
    "col_totals": {t: col_tot[t] for t in TYPES},
    "grand_total": N,
    "standardized_residuals": {g: {t: round(res_obs[g][t], 3) for t in TYPES} for g in GENRES},
    "dominant_type_per_genre": dominant_type,
    "divine_majesty_sgpl_by_genre": dict(majesty_by_genre),
    "h1_association": {
        "chi2_obs": round(chi2_obs, 4),
        "nmi_obs": round(nmi_obs, 6),
        "cramers_v": round(V_obs, 4),
        "p_chi2": p_chi2,
        "p_nmi": p_nmi,
        "p_chi2_replication": p_chi2_r,
        "p_nmi_replication": p_nmi_r,
        "pass": h1_pass,
        "locked_direction": "positive association (chi2 & NMI > 95th pct of label null)",
    },
    "h2_dominant_type": {
        "legal_medinan_P2_3_residual": round(legal_p23, 3),
        "legal_medinan_row_max_type": legal_top_type,
        "legal_medinan_P2_3_pass": h2a_pass,
        "narrative_P3_1_residual": round(narr_p31, 3),
        "narrative_P3_1_pass": h2b_pass,
        "pass": h2_pass,
    },
    "mw3_person_only": {
        "contingency_table": tab_to_dict(tab_po, PERSON_TYPES),
        "chi2_obs": round(chi2_po, 4),
        "nmi_obs": round(nmi_po, 6),
        "cramers_v": round(V_po, 4),
        "p_chi2": p_chi2_po,
        "p_nmi": p_nmi_po,
        "standardized_residuals": {g: {t: round(res_po[g][t], 3) for t in PERSON_TYPES} for g in GENRES},
    },
    "mw6_census_marginals_reproduced": {"person_shifts": n_person, "number_shifts": n_number},
    "verdict": verdict,
}
json.dump(out, open(OUT_JSON, "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(f"\n[written] {OUT_JSON}")
print(f"[dominant type per genre] {dominant_type}")
print(f"[divine I<->We majesty by genre] {dict(majesty_by_genre)}")
