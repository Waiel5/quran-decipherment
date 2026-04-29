"""H-NEW-56 — five-exception analysis of muqaṭṭaʿāt-opened surahs.

Parent: H-NEW-53 (24/29 muqaṭṭaʿāt surahs reference kitāb/qurʾān in v1-3, p ≈ 10⁻¹²).
Five exceptions: Q 19, Q 29, Q 30, Q 42, Q 68.

3-cell test family (Bonferroni k=3, α=0.0167):
  Cell 1: Compensating writing-cluster (kitāb/qurʾān/qalam/satr).
  Cell 2: Full extended-marker set (10 markers: + dhikr, āyāt, nūr, kalām, hudā, wahy/anzal).
  Cell 3: Per-exception thematic classification (descriptive, no p-value).

Seed: 20260416. Pre-reg: findings/phase-b-hypotheses/h-new-56-five-exceptions-prereg.md
"""
from __future__ import annotations

import csv
import json
import re
from math import comb
from pathlib import Path

REPO = Path("/Users/grey/Downloads/quran")
SEED = 20260416
ALPHA_BON = 0.05 / 3

MUQATTAAT_SURAHS = [
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32, 36, 38,
    40, 41, 42, 43, 44, 45, 46, 50, 68,
]
EXCEPTIONS = [19, 29, 30, 42, 68]

# Marker dictionaries.  All forms are no-tashkeel.
NARROW_MARKERS = {
    "kitab (k-t-b)": r"كتب|كتاب|الكتاب|الكتب|كتابك|كتابه|كتابي|كتابنا|كتبنا|كتبه|كتابا",
    "quran (q-r-A)": r"قرآن|القرآن|قرءان|القرءان|قرآنا|قرانا|اقرأ",
}
WRITING_EXTRAS = {
    "qalam (pen)":   r"قلم|القلم|أقلام",
    "satr (s-T-r)":  r"يسطرون|يسطر|سطر|مسطور|أساطير",
}
SEMANTIC_EXTRAS = {
    "dhikr (z-k-r)": r"ذكر|الذكر|ذكرى|تذكرة|مذكر|يذكر|تذكر",
    "ayat (sign)":   r"آية|الآية|آيات|الآيات|آياتنا|آياته|آياتك",
    "nur (light)":   r"نور|النور|نورا|نوره",
    "kalam (speech)": r"كلام|الكلام|كلم|كلمة|الكلمة|يكلم|كلمه",
    "huda (guide)":  r"هدى|الهدى|يهدي|هاد|اهد|اهدنا|مهتد",
    "wahy (reveal)": r"وحي|أوحى|أوحينا|أوحي|يوحي|يوحى|أنزل|أنزلنا|أنزلناه|أنزله|تنزيل|نزل|أُنزل|نزلنا|منزل",
}
WRITING_CLUSTER = {**NARROW_MARKERS, **WRITING_EXTRAS}
EXTENDED_MARKERS = {**NARROW_MARKERS, **WRITING_EXTRAS, **SEMANTIC_EXTRAS}


def hypergeom_upper(N: int, K: int, n: int, x: int) -> float:
    """P(X >= x) under hypergeometric(N, K, n)."""
    p = 0.0
    for i in range(x, min(K, n) + 1):
        p += comb(K, i) * comb(N - K, n - i) / comb(N, n)
    return p


def has_marker(text: str, markers: dict) -> list[str]:
    return [name for name, pat in markers.items() if re.search(pat, text)]


def main() -> None:
    data = json.load((REPO / "quran-text" / "quran-no-tashkeel.json").open())
    rev = list(csv.DictReader((REPO / "data" / "revelation-order.csv").open()))
    rev_by_mushaf = {int(r["mushaf_order"]): r for r in rev}

    # 1. Per-exception detail
    per_exception = {}
    for sid in EXCEPTIONS:
        surah = data[sid - 1]
        v1_3 = " ".join(v["text"] for v in surah["verses"][:3])
        v_full = [v["text"] for v in surah["verses"][:7]]
        rec = rev_by_mushaf[sid]
        per_exception[sid] = {
            "name_ar": surah["name"],
            "name_tl": surah["transliteration"],
            "type": surah["type"],
            "verses_v1_v7": v_full,
            "v1_3_concat": v1_3,
            "noldeke_order": int(rec["noldeke_order"]),
            "noldeke_phase": rec["noldeke_phase"],
            "revelation_order": int(rec["revelation_order"]),
            "narrow_markers_v1_3": has_marker(v1_3, NARROW_MARKERS),
            "writing_extras_v1_3": has_marker(v1_3, WRITING_EXTRAS),
            "semantic_extras_v1_3": has_marker(v1_3, SEMANTIC_EXTRAS),
            "all_extended_v1_3": has_marker(v1_3, EXTENDED_MARKERS),
        }

    # 2. Hypergeometric tests across all 114 surahs
    def count_surahs_with(markers: dict) -> dict:
        muq_hits = []
        nm_hits = []
        for sid in range(1, 115):
            v1_3 = " ".join(v["text"] for v in data[sid - 1]["verses"][:3])
            if has_marker(v1_3, markers):
                if sid in MUQATTAAT_SURAHS:
                    muq_hits.append(sid)
                else:
                    nm_hits.append(sid)
        return {
            "muq_hits": muq_hits,
            "nm_hits": nm_hits,
            "muq_count": len(muq_hits),
            "nm_count": len(nm_hits),
            "K_total": len(muq_hits) + len(nm_hits),
        }

    cell1 = count_surahs_with(WRITING_CLUSTER)  # writing-cluster
    cell2 = count_surahs_with(EXTENDED_MARKERS)  # full extended

    N, n = 114, 29
    cell1_p = hypergeom_upper(N, cell1["K_total"], n, cell1["muq_count"])
    cell2_p = hypergeom_upper(N, cell2["K_total"], n, cell2["muq_count"])

    # 3. Per-exception thematic classification
    thematic = {
        19: "prophetic-narrative (Zakariyyā / Maryam)",
        29: "existential-test (āmannā / fitnah / ṣadaqa)",
        30: "historical-eschatological (ghulibat al-Rūm)",
        42: "cosmic-revelation (kadhālika yūḥī)",
        68: "oath-based (al-qalam / yasṭurūn)",
    }

    # 4. Reference: narrow (replicates H-NEW-53)
    cell0 = count_surahs_with(NARROW_MARKERS)
    cell0_p = hypergeom_upper(N, cell0["K_total"], n, cell0["muq_count"])

    out = {
        "task": "H-NEW-56 — five-exception analysis of muqaṭṭaʿāt-opened surahs",
        "seed": SEED,
        "alpha_bon": ALPHA_BON,
        "exceptions": EXCEPTIONS,
        "per_exception": per_exception,
        "thematic_classification": thematic,
        "cell0_NARROW_REPLICATION": {
            "markers": list(NARROW_MARKERS.keys()),
            **cell0,
            "p_hypergeom": cell0_p,
            "verdict": "PASS" if cell0_p < ALPHA_BON else "FAIL",
        },
        "cell1_WRITING_CLUSTER": {
            "markers": list(WRITING_CLUSTER.keys()),
            **cell1,
            "p_hypergeom": cell1_p,
            "verdict": "PASS" if cell1_p < ALPHA_BON else "FAIL",
        },
        "cell2_FULL_EXTENDED": {
            "markers": list(EXTENDED_MARKERS.keys()),
            **cell2,
            "p_hypergeom": cell2_p,
            "verdict": "PASS" if cell2_p < ALPHA_BON else "FAIL",
        },
    }

    out_path = REPO / "findings" / "phase-b-hypotheses" / "csv" / "h-new-56.json"
    out_path.write_text(json.dumps(out, ensure_ascii=False, indent=2))
    print(f"Wrote: {out_path}")

    # Console summary
    print("\n=== H-NEW-56 SUMMARY ===")
    print(f"Cell 0 (narrow, replicates H-NEW-53): {cell0['muq_count']}/29  p={cell0_p:.3e}")
    print(f"Cell 1 (writing-cluster +qalam/satr):  {cell1['muq_count']}/29  p={cell1_p:.3e}")
    print(f"Cell 2 (full 10-marker extended):      {cell2['muq_count']}/29  p={cell2_p:.3e}")
    print()
    for sid in EXCEPTIONS:
        p = per_exception[sid]
        print(f"  Q {sid:>2} {p['name_tl']:<14} (Nöldeke #{p['noldeke_order']}, {p['noldeke_phase']})")
        print(f"     thematic = {thematic[sid]}")
        print(f"     narrow markers v1-3   = {p['narrow_markers_v1_3'] or 'NONE'}")
        print(f"     writing extras v1-3   = {p['writing_extras_v1_3'] or 'NONE'}")
        print(f"     semantic extras v1-3  = {p['semantic_extras_v1_3'] or 'NONE'}")


if __name__ == "__main__":
    main()
