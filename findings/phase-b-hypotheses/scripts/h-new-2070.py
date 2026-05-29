#!/usr/bin/env python3
"""H-NEW-2070 — Divine-name verse-final pairing arithmetic + co-occurrence graph (al-fawāṣil).

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2070-divine-name-pairing.md
SHA256:  03e5b967421cc4e78856c23251a84c5b100ec3ad70172e176c3c4b4691e3aa79

Rules-tuple: (no-tashkeel, orthographic-token, verse-final ordered bigram,
              base-normalized to 97 single-token al-Tirmidhī names,
              basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)

Hypotheses (Bonferroni k=2, α_cell=0.025):
  H1 — top-5-pair share > 97.5th pct of slot-independence null
  H2 — normalized HHI    > 97.5th pct of slot-independence null
Null: slot-independence shuffle (preserve slot-1 & slot-2 marginals; destroy pairing).
"""

import csv as _csv
import hashlib
import json
import os
import random
import sys
from collections import Counter, defaultdict
from pathlib import Path
from statistics import mean, median

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2070-divine-name-pairing.md"
EXPECTED_SHA = "03e5b967421cc4e78856c23251a84c5b100ec3ad70172e176c3c4b4691e3aa79"
QURAN_PATH = ROOT / "quran-text/quran-no-tashkeel.json"
NAMES_PATH = ROOT / "data/asma-al-husna.txt"
CHRON_PATH = ROOT / "data/revelation-order.csv"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-2070.json"

SEED_A = 20260509
SEED_B = 20260511
N_PERM = 10_000
ALPHA_BON = 0.025
TOP_K_SHARE = 5

PAUSE = set("۞ۖۗۚ۟ۘ۠ۤۛ")

# Transliteration for descriptive output (base forms → Latin).
TRANSLIT = {
    "رحمن": "raḥmān", "رحيم": "raḥīm", "ملك": "malik", "قدوس": "quddūs",
    "سلام": "salām", "مؤمن": "muʾmin", "مهيمن": "muhaymin", "عزيز": "ʿazīz",
    "جبار": "jabbār", "متكبر": "mutakabbir", "خالق": "khāliq", "بارئ": "bāriʾ",
    "مصور": "muṣawwir", "غفار": "ghaffār", "قهار": "qahhār", "وهاب": "wahhāb",
    "رزاق": "razzāq", "فتاح": "fattāḥ", "عليم": "ʿalīm", "قابض": "qābiḍ",
    "باسط": "bāsiṭ", "خافض": "khāfiḍ", "رافع": "rāfiʿ", "معز": "muʿizz",
    "مذل": "mudhill", "سميع": "samīʿ", "بصير": "baṣīr", "حكم": "ḥakam",
    "عدل": "ʿadl", "لطيف": "laṭīf", "خبير": "khabīr", "حليم": "ḥalīm",
    "عظيم": "ʿaẓīm", "غفور": "ghafūr", "شكور": "shakūr", "علي": "ʿalī",
    "كبير": "kabīr", "حفيظ": "ḥafīẓ", "مقيت": "muqīt", "حسيب": "ḥasīb",
    "جليل": "jalīl", "كريم": "karīm", "رقيب": "raqīb", "مجيب": "mujīb",
    "واسع": "wāsiʿ", "حكيم": "ḥakīm", "ودود": "wadūd", "مجيد": "majīd",
    "باعث": "bāʿith", "شهيد": "shahīd", "حق": "ḥaqq", "وكيل": "wakīl",
    "قوي": "qawī", "متين": "matīn", "ولي": "walī", "حميد": "ḥamīd",
    "محصي": "muḥṣī", "مبدئ": "mubdiʾ", "معيد": "muʿīd", "محيي": "muḥyī",
    "مميت": "mumīt", "حي": "ḥayy", "قيوم": "qayyūm", "واجد": "wājid",
    "ماجد": "mājid", "واحد": "wāḥid", "صمد": "ṣamad", "قادر": "qādir",
    "مقتدر": "muqtadir", "مقدم": "muqaddim", "مؤخر": "muʾakhkhir",
    "أول": "awwal", "آخر": "ākhir", "ظاهر": "ẓāhir", "باطن": "bāṭin",
    "والي": "wālī", "متعالي": "mutaʿālī", "بر": "barr", "تواب": "tawwāb",
    "منتقم": "muntaqim", "عفو": "ʿafū", "رؤوف": "raʾūf", "مقسط": "muqsiṭ",
    "جامع": "jāmiʿ", "غني": "ghanī", "مغني": "mughnī", "مانع": "māniʿ",
    "ضار": "ḍārr", "نافع": "nāfiʿ", "نور": "nūr", "هادي": "hādī",
    "بديع": "badīʿ", "باقي": "bāqī", "وارث": "wārith", "رشيد": "rashīd",
    "صبور": "ṣabūr", "قدير": "qadīr",
}


def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}…")


def strip_al(w: str) -> str:
    return w[2:] if w.startswith("ال") else w


def load_divine_set() -> set[str]:
    """97 single-token al-Tirmidhī names, base-normalized by stripping ال."""
    names = []
    for raw in NAMES_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(" ".join(line.split()))
    return {strip_al(n) for n in names if len(n.split()) == 1}


def toks(text: str) -> list[str]:
    return [w for w in text.split() if not all(c in PAUSE for c in w)]


def base(w: str) -> str:
    """Strip leading ال; strip one trailing accusative/indefinite alif when len>3."""
    if w.startswith("ال"):
        w = w[2:]
    if len(w) > 3 and w.endswith("ا"):
        w = w[:-1]
    return w


def top_k_share(pairs: list[tuple], k: int) -> float:
    c = Counter(pairs)
    total = len(pairs)
    top = sum(n for _, n in c.most_common(k))
    return top / total if total else 0.0


def hhi(pairs: list[tuple]) -> float:
    c = Counter(pairs)
    total = len(pairs)
    if not total:
        return 0.0
    return sum((n / total) ** 2 for n in c.values())


def slot_independence_null(slot1: list[str], slot2: list[str], k: int, n_perm: int, seed: int):
    """Permute slot1 and slot2 independently; recompute share & HHI. Preserve marginals."""
    rng = random.Random(seed)
    s1 = list(slot1)
    s2 = list(slot2)
    shares, hhis = [], []
    for _ in range(n_perm):
        rng.shuffle(s1)
        rng.shuffle(s2)
        perm_pairs = list(zip(s1, s2))
        shares.append(top_k_share(perm_pairs, k))
        hhis.append(hhi(perm_pairs))
    return shares, hhis


def pct(sorted_vals: list[float], q: float) -> float:
    idx = min(len(sorted_vals) - 1, int(q * len(sorted_vals)))
    return sorted_vals[idx]


def main() -> None:
    verify_sha()
    DIVINE = load_divine_set()
    print(f"Divine base-name set: {len(DIVINE)} single-token al-Tirmidhī names")
    corpus = json.loads(QURAN_PATH.read_text(encoding="utf-8"))

    # period map
    period_by_sid = {}
    with CHRON_PATH.open() as f:
        for row in _csv.DictReader(f):
            period_by_sid[int(row["mushaf_order"])] = row["period"].strip()

    # --- collect verse-final divine-name pairs ---
    pair_rows = []  # (sid, ayah, base1, base2, surface, period)
    for s in corpus:
        sid = int(s["id"])
        period = period_by_sid.get(sid, "UNKNOWN")
        for v in s["verses"]:
            ayah = int(v["id"])
            tk = toks(v["text"])
            if len(tk) < 2:
                continue
            b1, b2 = base(tk[-2]), base(tk[-1])
            if b1 in DIVINE and b2 in DIVINE:
                pair_rows.append((sid, ayah, b1, b2, f"{tk[-2]} {tk[-1]}", period))

    N = len(pair_rows)
    slot1 = [r[2] for r in pair_rows]
    slot2 = [r[3] for r in pair_rows]
    obs_pairs = list(zip(slot1, slot2))
    pair_counts = Counter(obs_pairs)
    n_distinct = len(pair_counts)
    print(f"\nVerses closing on a divine-name PAIR: {N}")
    print(f"Distinct ordered verse-final pairs: {n_distinct}")

    # observed statistics
    obs_share = top_k_share(obs_pairs, TOP_K_SHARE)
    obs_hhi = hhi(obs_pairs)
    print(f"Observed top-{TOP_K_SHARE} share: {obs_share:.5f}")
    print(f"Observed HHI:           {obs_hhi:.5f}")

    # --- Cell A: whole-corpus slot-independence null ---
    a_shares, a_hhis = slot_independence_null(slot1, slot2, TOP_K_SHARE, N_PERM, SEED_A)
    p_a_share = sum(1 for x in a_shares if x >= obs_share) / N_PERM
    p_a_hhi = sum(1 for x in a_hhis if x >= obs_hhi) / N_PERM
    a_shares_s = sorted(a_shares)
    a_hhis_s = sorted(a_hhis)

    h1_pass = p_a_share <= ALPHA_BON
    h2_pass = p_a_hhi <= ALPHA_BON

    # --- Cell B: Medinan-only robustness ---
    med_rows = [r for r in pair_rows if r[5] == "Medinan"]
    med_s1 = [r[2] for r in med_rows]
    med_s2 = [r[3] for r in med_rows]
    med_pairs = list(zip(med_s1, med_s2))
    med_obs_share = top_k_share(med_pairs, TOP_K_SHARE)
    med_obs_hhi = hhi(med_pairs)
    b_shares, b_hhis = slot_independence_null(med_s1, med_s2, TOP_K_SHARE, N_PERM, SEED_B)
    p_b_share = sum(1 for x in b_shares if x >= med_obs_share) / N_PERM
    p_b_hhi = sum(1 for x in b_hhis if x >= med_obs_hhi) / N_PERM
    b_share_concordant = med_obs_share > median(b_shares)
    b_hhi_concordant = med_obs_hhi > median(b_hhis)
    cell_b_concordant = b_share_concordant and b_hhi_concordant

    # --- verdict ---
    if obs_share < median(a_shares) and obs_hhi < median(a_hhis):
        verdict = "NULL (reverse-direction: anti-concentration)"
    elif h1_pass and h2_pass and cell_b_concordant:
        verdict = "PASS-DIRECTED"
    elif h1_pass and h2_pass and not cell_b_concordant:
        verdict = "PASS-DIRECTED (period-fragile)"
    elif h1_pass or h2_pass:
        verdict = "PARTIAL (one statistic only)"
    else:
        verdict = "NULL"

    # --- descriptive: top-15 pairs ---
    def tr(w):
        return TRANSLIT.get(w, w)

    example = {}
    for sid, ayah, b1, b2, surface, period in pair_rows:
        example.setdefault((b1, b2), (sid, ayah, surface))
    top15 = []
    for (b1, b2), cnt in pair_counts.most_common(15):
        ex = example[(b1, b2)]
        top15.append({
            "rank": len(top15) + 1,
            "pair_ar": f"{b1} + {b2}",
            "pair_translit": f"{tr(b1)} + {tr(b2)}",
            "count": cnt,
            "share": cnt / N,
            "example": f"Q{ex[0]}:{ex[1]}",
            "example_surface": ex[2],
        })

    # --- corpus-singletons (count==1) and corpus-max ---
    singletons = sorted(
        [{"pair_ar": f"{b1} + {b2}", "pair_translit": f"{tr(b1)} + {tr(b2)}",
          "example": f"Q{example[(b1,b2)][0]}:{example[(b1,b2)][1]}",
          "surface": example[(b1, b2)][2]}
         for (b1, b2), c in pair_counts.items() if c == 1],
        key=lambda d: d["pair_ar"])
    corpus_max = top15[0]

    # --- pairing graph (directed, weighted) ---
    out_w = defaultdict(int)   # slot1 weighted out-degree
    in_w = defaultdict(int)    # slot2 weighted in-degree
    deg_w = defaultdict(int)   # total weighted degree
    for (b1, b2), c in pair_counts.items():
        out_w[b1] += c
        in_w[b2] += c
        deg_w[b1] += c
        deg_w[b2] += c
    nodes = sorted(deg_w, key=lambda n: (-deg_w[n], n))
    graph_nodes = [{
        "name_ar": n, "name_translit": tr(n),
        "weighted_degree": deg_w[n], "out_weight": out_w.get(n, 0),
        "in_weight": in_w.get(n, 0),
    } for n in nodes]
    edges = [{
        "from": b1, "to": b2, "from_translit": tr(b1), "to_translit": tr(b2),
        "weight": c,
    } for (b1, b2), c in sorted(pair_counts.items(), key=lambda kv: -kv[1])]

    # --- famous al-ʿazīz al-ḥakīm breakdown ---
    azhk = [r for r in pair_rows if r[2] == "عزيز" and r[3] == "حكيم"]
    azhk_forms = Counter(r[4] for r in azhk)

    # --- spot-check: are any top-pair instances non-divine referent? (Q12 governor) ---
    # Report Q12 verse-final divine-pair instances for manual inspection.
    q12_instances = [
        {"loc": f"Q{r[0]}:{r[1]}", "pair": f"{r[2]} + {r[3]}", "surface": r[4]}
        for r in pair_rows if r[0] == 12
    ]

    # --- unordered collapse (descriptive only) ---
    unordered = Counter(frozenset((b1, b2)) if b1 != b2 else (b1, b2) for b1, b2 in obs_pairs)
    top_unordered = []
    for key, c in unordered.most_common(10):
        if isinstance(key, frozenset):
            names = sorted(key)
            label = " ↔ ".join(f"{tr(x)}" for x in names)
        else:
            label = f"{tr(key[0])} (self)"
        top_unordered.append({"pair": label, "count": c})

    out = {
        "finding_id": "H-NEW-2070",
        "title": "Divine-name verse-final pairing arithmetic + co-occurrence graph (al-fawāṣil)",
        "pre_reg_sha256": EXPECTED_SHA,
        "seed_A": SEED_A, "seed_B": SEED_B, "n_perm": N_PERM,
        "alpha_bon_per_cell": ALPHA_BON, "bonferroni_k": 2,
        "rules_tuple": "(no-tashkeel, orthographic-token, verse-final ordered bigram, "
                       "base-normalized to 97 al-Tirmidhī single-token names, "
                       "basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "divine_set_size": len(DIVINE),
        "n_verses_closing_divine_pair": N,
        "n_distinct_ordered_pairs": n_distinct,
        "observed_top5_share": obs_share,
        "observed_HHI": obs_hhi,
        "cell_A_whole_corpus": {
            "H1_top5_share": {
                "observed": obs_share, "null_mean": mean(a_shares),
                "null_median": median(a_shares),
                "null_p97_5": pct(a_shares_s, 0.975), "p_perm": p_a_share, "pass": h1_pass,
            },
            "H2_HHI": {
                "observed": obs_hhi, "null_mean": mean(a_hhis),
                "null_median": median(a_hhis),
                "null_p97_5": pct(a_hhis_s, 0.975), "p_perm": p_a_hhi, "pass": h2_pass,
            },
        },
        "cell_B_medinan_robustness": {
            "n_medinan_pair_verses": len(med_rows),
            "observed_top5_share": med_obs_share, "null_median_share": median(b_shares),
            "p_perm_share": p_b_share, "share_concordant": b_share_concordant,
            "observed_HHI": med_obs_hhi, "null_median_HHI": median(b_hhis),
            "p_perm_HHI": p_b_hhi, "HHI_concordant": b_hhi_concordant,
            "concordant": cell_b_concordant,
        },
        "verdict": verdict,
        "top_15_pairs": top15,
        "corpus_max_pair": corpus_max,
        "corpus_singleton_pairs": singletons,
        "n_corpus_singletons": len(singletons),
        "famous_al_aziz_al_hakim": {
            "total_verse_final": len(azhk),
            "by_form": dict(azhk_forms),
            "note": "al-X al-Y definite form = the classical 'al-ʿazīz al-ḥakīm' enumeration",
        },
        "pairing_graph": {
            "n_nodes": len(graph_nodes), "n_edges": len(edges),
            "nodes_by_weighted_degree": graph_nodes,
            "edges": edges,
        },
        "top_10_unordered_collapse_descriptive": top_unordered,
        "Q12_verse_final_divine_pairs_spotcheck": q12_instances,
        "all_pair_rows": [
            {"loc": f"Q{r[0]}:{r[1]}", "base1": r[2], "base2": r[3],
             "surface": r[4], "period": r[5]} for r in pair_rows
        ],
    }

    os.makedirs(OUT_PATH.parent, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"\nCell A H1 (top-5 share): obs={obs_share:.4f}  null_p97.5={pct(a_shares_s,0.975):.4f}  p={p_a_share:.5f}  pass={h1_pass}")
    print(f"Cell A H2 (HHI):         obs={obs_hhi:.4f}  null_p97.5={pct(a_hhis_s,0.975):.4f}  p={p_a_hhi:.5f}  pass={h2_pass}")
    print(f"Cell B Medinan: share concordant={b_share_concordant} (p={p_b_share:.4f}); HHI concordant={b_hhi_concordant} (p={p_b_hhi:.4f})")
    print(f"\nVERDICT: {verdict}")
    print(f"\nTop-5 verse-final divine-name pairs:")
    for r in top15[:5]:
        print(f"  {r['count']:3d}  {r['pair_ar']}  ({r['pair_translit']})  e.g. {r['example']}")
    print(f"\nFamous al-ʿazīz al-ḥakīm: {len(azhk)} verse-finals; by form: {dict(azhk_forms)}")
    print(f"Corpus-max pair: {corpus_max['pair_ar']} ({corpus_max['count']})")
    print(f"Corpus-singleton fawāṣila pairs: {len(singletons)}")
    print(f"Graph: {len(graph_nodes)} nodes, {len(edges)} edges")
    print(f"\nWrote: {OUT_PATH}")


if __name__ == "__main__":
    main()
