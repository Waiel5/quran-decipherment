"""H-NEW-54 — Extended Root-Enrichment Scan.

Pre-reg: findings/phase-b-hypotheses/h-new-54-extended-root-enrichment-prereg.md

Question: H-NEW-53 confirmed muqaṭṭaʿāt-opened surahs (n=29) are massively
enriched for kitāb/qurʾān references in v1-3 (p ≈ 3.17e-12). Does this
generalize to other revelation-theme roots?

Procedure: 10-root family. For each root, compute K_root (surahs in N=114 with
ANY listed surface form in v1-3), then hypergeometric two-sided p for observing
obs_root muq surahs out of n=29.

Bonferroni-10: α_per = 0.005.

Seed 20260416 (closed-form; seed is here for cross-finding bookkeeping).
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from typing import Dict, List, Set, Tuple

REPO = "/Users/grey/Downloads/quran"
sys.path.insert(0, os.path.join(REPO, "analysis"))

from tools.loader import load_quran  # noqa: E402

try:
    from scipy.stats import hypergeom  # noqa: E402
    HAVE_SCIPY = True
except ImportError:
    HAVE_SCIPY = False
    from math import comb

SEED = 20260416
N_SURAHS = 114
N_MUQ = 29
BON_K = 10
ALPHA_BON = 0.05 / BON_K

# Locked muqaṭṭaʿāt-opened set (from H-NEW-46 / H-NEW-53)
MUQ_SURAHS = frozenset({
    2, 3, 7, 10, 11, 12, 13, 14, 15, 19, 20, 26, 27, 28, 29, 30, 31, 32,
    36, 38, 40, 41, 42, 43, 44, 45, 46, 50, 68
})
assert len(MUQ_SURAHS) == 29

# Surface form lists — LOCKED IN PRE-REG (do not edit after run start)
KITAB = {"كتاب", "كتب", "الكتاب", "الكتب", "كتابك", "كتابه", "كتابي",
         "كتابهم", "كتابا", "كتابنا"}
QURAN = {"قرآن", "القرآن", "قرءان", "القرءان", "قرءن", "قرآنا", "قرآنه"}
AYAT = {"آية", "آيات", "الآيات", "آياته", "آياتنا", "آياتي", "آياتك",
        "آياتها", "آياتهم", "آيتنا", "الآية", "لآيات", "لآية",
        "بآياتنا", "بآياتي", "بآياته", "بآيات"}
DHIKR = {"ذكر", "الذكر", "ذكرى", "تذكرة", "ذكرا", "ذاكر", "يذكر", "تذكر",
         "يتذكر", "مذكر", "مدكر", "تذكرون", "يذكرون", "الذكرى", "بالذكر",
         "لذكر", "فاذكر", "اذكر", "ذكره"}
NAZALA = {"نزل", "أنزل", "تنزيل", "ينزل", "ننزل", "نزلنا", "أنزلنا",
          "منزل", "منزلين", "تنزل", "تنزلت", "منزلون", "نزله", "نازلون",
          "منزلا", "تنزله", "منازل"}
WAHY = {"وحي", "وحيا", "الوحي", "يوحي", "يوحى", "أوحى", "أوحينا",
        "نوحي", "نوحيه", "موح", "يوحون"}
WAD = {"وعد", "الوعد", "وعدنا", "وعدا", "وعدكم", "وعده", "وعدنى",
       "موعود", "ميعاد", "الموعد", "الميعاد", "موعد", "وعدتكم", "وعدتم",
       "يعد", "وعدتنا"}
HUDAA = {"هدى", "الهدى", "هدي", "مهتد", "تهتد", "اهد", "يهدي", "هاد",
         "الهداية", "هديتنا", "لهدى", "يهتد", "مهديا", "هدانا"}
# RABB uses TOKEN matching (exact equality after Arabic-letter tokenization)
RABB_TOKENS = {
    "رب", "ربك", "ربه", "ربهم", "ربنا", "ربي", "ربكم", "الرب", "ربها",
    "ربهما", "ربكما",
    "برب", "بربك", "بربه", "بربهم", "بربنا", "بربكم", "بربها",
    "وربك", "وربه", "وربهم", "وربنا", "وربي", "وربكم", "وربها",
    "لرب", "لربك", "لربه", "لربهم", "لربنا", "لربي", "لربكم", "لربها",
    "فرب",
}
ILAH = {"إله", "الإله", "إلها", "إلهك", "إلهي", "إلهنا", "إلهكم",
        "إلههم", "آله", "ءاله", "الإلاه"}

ROOT_FAMILIES: List[Tuple[str, str, set, str]] = [
    ("k-t-b",      "kitāb / book",                  KITAB,        "substring"),
    ("q-r-ʾ",      "qurʾān / read-recite",          QURAN,        "substring"),
    ("ʾ-y-ā",      "āyāt / signs-verses",           AYAT,         "substring"),
    ("dh-k-r",     "dhikr / remembrance",           DHIKR,        "substring"),
    ("n-z-l",      "nazala / sent-down",            NAZALA,       "substring"),
    ("w-ḥ-y",      "waḥy / inspiration-revelation", WAHY,         "substring"),
    ("w-ʿ-d",      "waʿd / promise-covenant",       WAD,          "substring"),
    ("h-d-y",      "hudā / guidance",               HUDAA,        "substring"),
    ("r-b-b",      "rabb / Lord",                   RABB_TOKENS,  "token"),
    ("ʾ-l-h",      "ilāh / deity",                  ILAH,         "substring"),
]
assert len(ROOT_FAMILIES) == BON_K


# ---------- helpers ----------

ARABIC_TOKEN_RE = re.compile(r"[\u0600-\u06ff]+")


def v123_text(verses) -> str:
    """Concatenate verses 1, 2, 3 into a single text-window."""
    return " ".join(v.text for v in verses if v.id <= 3)


def hits_substring(text: str, forms: set) -> bool:
    return any(f in text for f in forms)


def hits_token(text: str, forms: set) -> bool:
    tokens = ARABIC_TOKEN_RE.findall(text)
    return any(t in forms for t in tokens)


def hypergeom_two_sided(obs: int, K: int, n: int, N: int) -> Dict[str, float]:
    """Two-sided hypergeometric: 2 * min(P(X >= obs), P(X <= obs)), cap 1."""
    if HAVE_SCIPY:
        # P(X >= obs) = sf(obs - 1)
        p_upper = float(hypergeom.sf(obs - 1, N, K, n))
        # P(X <= obs) = cdf(obs)
        p_lower = float(hypergeom.cdf(obs, N, K, n))
    else:
        # Closed-form fallback
        def _hpmf(k):
            if k < 0 or k > min(K, n) or (n - k) > (N - K):
                return 0.0
            return comb(K, k) * comb(N - K, n - k) / comb(N, n)
        kmax = min(K, n)
        p_upper = sum(_hpmf(k) for k in range(obs, kmax + 1))
        p_lower = sum(_hpmf(k) for k in range(0, obs + 1))
    p_two = 2.0 * min(p_upper, p_lower)
    if p_two > 1.0:
        p_two = 1.0
    expected = n * K / N
    return {
        "obs": obs, "K": K, "n": n, "N": N,
        "expected": expected,
        "obs_minus_expected": obs - expected,
        "p_upper": p_upper,
        "p_lower": p_lower,
        "p_two_sided": p_two,
    }


def main():
    print("[H-NEW-54] loading quran-no-tashkeel ...")
    surahs = load_quran("no-tashkeel")
    assert len(surahs) == N_SURAHS

    # Build per-surah v1-3 windows
    windows: Dict[int, str] = {}
    for s in surahs:
        windows[s.id] = v123_text(s.verses)

    # Sanity: 29 muq surahs
    assert len(MUQ_SURAHS) == N_MUQ

    print("[H-NEW-54] scanning roots ...")
    per_root_results = []
    per_root_hit_lists: Dict[str, Dict] = {}

    for root_id, label, forms, mode in ROOT_FAMILIES:
        all_hits: List[int] = []
        muq_hits: List[int] = []
        for sid, txt in windows.items():
            if mode == "token":
                ok = hits_token(txt, forms)
            else:
                ok = hits_substring(txt, forms)
            if ok:
                all_hits.append(sid)
                if sid in MUQ_SURAHS:
                    muq_hits.append(sid)
        K_root = len(all_hits)
        obs = len(muq_hits)
        stats = hypergeom_two_sided(obs, K_root, N_MUQ, N_SURAHS)
        sig = stats["p_two_sided"] < ALPHA_BON
        if sig and stats["obs_minus_expected"] > 0:
            verdict = "PASS"
        elif sig and stats["obs_minus_expected"] < 0:
            verdict = "PASS-DEPLETED"
        else:
            verdict = "NULL"
        row = {
            "root": root_id,
            "label": label,
            "form_count": len(forms),
            "match_mode": mode,
            **stats,
            "p_corrected_bonferroni10": min(1.0, stats["p_two_sided"] * BON_K),
            "alpha_bon": ALPHA_BON,
            "significant_at_alpha_bon": sig,
            "verdict": verdict,
        }
        per_root_results.append(row)
        per_root_hit_lists[root_id] = {
            "all_hits": sorted(all_hits),
            "muq_hits": sorted(muq_hits),
            "non_muq_hits": sorted(set(all_hits) - MUQ_SURAHS),
        }
        marker = "***" if sig else "   "
        print(f"  {marker} {root_id:<8} ({label:<32}) "
              f"obs={obs:>2} K={K_root:>3} E={stats['expected']:>5.2f} "
              f"p2={stats['p_two_sided']:.4e} → {verdict}")

    # Composite verdict
    n_sig = sum(1 for r in per_root_results if r["significant_at_alpha_bon"])
    if n_sig == 0:
        composite = "NULL"
    elif n_sig <= 3:
        composite = "EXPLORATORY-PARTIAL"
    elif n_sig <= 7:
        composite = "PASS-BROAD-FIELD"
    else:
        composite = "STRONG-PASS-FIELD-WIDE"

    # MW-5 positive control: kitāb and qurʾān independently
    pos_kitab = per_root_results[0]
    pos_quran = per_root_results[1]
    pos_control_pass = (pos_kitab["p_two_sided"] < ALPHA_BON
                        and pos_quran["p_two_sided"] < ALPHA_BON)

    # Pre-reg SHA
    preg_path = os.path.join(REPO, "findings/phase-b-hypotheses/"
                             "h-new-54-extended-root-enrichment-prereg.md")
    with open(preg_path, "rb") as f:
        preg_sha = hashlib.sha256(f.read()).hexdigest()

    out = {
        "hypothesis_id": "H-NEW-54",
        "title": "Extended Root-Enrichment Scan",
        "run_date": "2026-04-15",
        "seed": SEED,
        "data_variant": "no-tashkeel",
        "rules_tuple": ("no-tashkeel; substring/token search on v1-3; "
                        "10-root family locked in pre-reg"),
        "n_surahs": N_SURAHS,
        "n_muq": N_MUQ,
        "muq_surahs": sorted(MUQ_SURAHS),
        "bonferroni_family": "H-NEW-54-revelation-theme-roots-10",
        "bonferroni_k": BON_K,
        "alpha_per": ALPHA_BON,
        "alpha_per_decimal": ALPHA_BON,
        "prereg_sha256": preg_sha,
        "have_scipy": HAVE_SCIPY,
        "n_significant": n_sig,
        "composite_verdict": composite,
        "positive_control_kitab_quran_pass": pos_control_pass,
        "per_root_results": per_root_results,
        "per_root_hit_lists": per_root_hit_lists,
    }

    out_path = os.path.join(REPO, "findings/phase-b-hypotheses/csv/h-new-54.json")
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(out, f, indent=2, ensure_ascii=False)
    print(f"\n[H-NEW-54] wrote {out_path}")
    print(f"[H-NEW-54] composite verdict: {composite}  (n_sig={n_sig}/10)")
    print(f"[H-NEW-54] positive control (kitab AND quran both p < α_bon): "
          f"{pos_control_pass}")


if __name__ == "__main__":
    main()
