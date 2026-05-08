#!/usr/bin/env python3
"""
Q017 al-Isrāʾ novel-findings runner — Q017-F-01..F-04.

Pre-reg SHAs locked at top.  Fail-fast on mismatch.
"""

import json
import hashlib
import os
import re
import sys
from collections import Counter

BASE = "/Users/grey/Downloads/quran"

PREREG_SHAS = {
    "Q017-F-01": "daa0e3d7bb1e6c5a49332ef639b26944b8657526bf5fe853b40844fb3baa0604",
    "Q017-F-02": "d3bf2bc52e69777415bb62e2efd9f5122870aacaa84b90ca9ced7e18b1d40904",
    "Q017-F-03": "68942a558acd81b2e1e6883a7a8b14bc40a7a4ef4a75c8994b19dad82259ddf5",
    "Q017-F-04": "86f3cb12aa13ddb3f10ad5c6687924844246fd1f9dbffcf194cd119844a23c4f",
}

PREREG_DIR = os.path.join(BASE, "surahs/Q017-al-isra/preregs")
PREREG_FILES = {
    "Q017-F-01": "Q017-F-01-alif-monorhyme-prereg.md",
    "Q017-F-02": "Q017-F-02-subhana-opening-prereg.md",
    "Q017-F-03": "Q017-F-03-tahaddi-citation-density-prereg.md",
    "Q017-F-04": "Q017-F-04-children-of-israel-density-prereg.md",
}

OUT_DIR = os.path.join(BASE, "surahs/Q017-al-isra/csv")
os.makedirs(OUT_DIR, exist_ok=True)


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


def verify_preregs():
    for tid, fname in PREREG_FILES.items():
        actual = sha256_file(os.path.join(PREREG_DIR, fname))
        expected = PREREG_SHAS[tid]
        assert actual == expected, f"SHA mismatch for {tid}: actual={actual} expected={expected}"
    print(f"[OK] All {len(PREREG_FILES)} pre-reg SHAs verified.", file=sys.stderr)


# ---------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------

# Tashkeel (diacritics + tatweel + Quran marks)
TASHKEEL = re.compile(r"[ً-ٰٟۖ-ۭـ]")
ARABIC_LETTER = re.compile(r"[ء-غف-يٮ-ەۺ-ۿ]")
PAUSE_MARK = re.compile(r"[ۖ-ۭ\s\.,!\?]")

ALIF_FINALS = set("اآأإىٰ")  # alif-shaped graphemes


def strip_tashkeel(text: str) -> str:
    return TASHKEEL.sub("", text)


def last_letter(text: str):
    t = strip_tashkeel(text)
    t = PAUSE_MARK.sub("", t)
    for ch in reversed(t):
        if ARABIC_LETTER.match(ch):
            return ch
    return None


def first_token(text: str) -> str:
    t = strip_tashkeel(text).strip()
    parts = re.split(r"\s+", t)
    return parts[0] if parts else ""


def tokens(text: str):
    t = strip_tashkeel(text)
    return [w for w in re.split(r"\s+", t) if w and ARABIC_LETTER.search(w)]


def load_quran(variant: str = "no"):
    path = {
        "no": "quran-text/quran-no-tashkeel.json",
        "min": "quran-text/quran-min-tashkeel.json",
        "full": "quran-text/quran-full-tashkeel.json",
    }[variant]
    return json.load(open(os.path.join(BASE, path), encoding="utf-8"))


# ---------------------------------------------------------------------
# Q017-F-01: alif-monorhyme purity rank for Q 17
# ---------------------------------------------------------------------


def F01_alif_monorhyme():
    quran_min = load_quran("min")
    rates = []
    for s in quran_min:
        verses = s["verses"]
        n = len(verses)
        n_alif = sum(1 for v in verses if last_letter(v["text"]) in ALIF_FINALS)
        rate = n_alif / n
        rates.append({
            "surah": s["id"],
            "name": s["transliteration"],
            "type": s["type"],
            "n_verses": n,
            "n_alif_final": n_alif,
            "alif_final_rate": rate,
        })
    # rank descending by rate (ties -> tied rank by sorted index)
    rates.sort(key=lambda r: (-r["alif_final_rate"], r["surah"]))
    for i, r in enumerate(rates):
        r["rank"] = i + 1
    # also produce dense rank
    by_rate = sorted({r["alif_final_rate"] for r in rates}, reverse=True)
    dense = {v: i + 1 for i, v in enumerate(by_rate)}
    for r in rates:
        r["dense_rank"] = dense[r["alif_final_rate"]]
    q17 = next(r for r in rates if r["surah"] == 17)
    top10 = rates[:10]
    perfect = [r for r in rates if r["alif_final_rate"] == 1.0]

    direction_pass = (q17["alif_final_rate"] >= 0.99) and (q17["dense_rank"] <= 10)
    verdict = "VINDICATED" if direction_pass else "FALSIFIED"

    out = {
        "id": "Q017-F-01",
        "prereg_sha": PREREG_SHAS["Q017-F-01"],
        "rules_tuple": "(min-tashkeel, orthographic-token, last-letter-of-verse-after-stripping-final-mark, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "Q17_result": q17,
        "top_10": top10,
        "n_perfect_monorhyme_surahs": len(perfect),
        "perfect_monorhyme_surahs": [r["surah"] for r in perfect],
        "verdict": verdict,
    }
    with open(os.path.join(OUT_DIR, "Q017-F-01.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[F-01] Q17 alif-rate={q17['alif_final_rate']:.4f} ({q17['n_alif_final']}/{q17['n_verses']}) "
          f"dense_rank={q17['dense_rank']} verdict={verdict}", file=sys.stderr)
    return out


# ---------------------------------------------------------------------
# Q017-F-02: Subhana-opening uniqueness across musabbiḥāt
# ---------------------------------------------------------------------


def F02_subhana_opening():
    quran_no = load_quran("no")
    musabbihat = [17, 57, 59, 61, 62, 64, 87]
    openings = {}
    for s in quran_no:
        v1 = s["verses"][0]["text"]
        first = first_token(v1)
        openings[s["id"]] = first

    # Tabulate musabbihat
    musabbih_openings = {sid: openings[sid] for sid in musabbihat}

    # Find ALL surahs where the first token contains the root س-ب-ح pattern
    sabbaha_root_surahs = []
    for sid, w in openings.items():
        # Match س...ب...ح pattern (the root letters in order, no other letters between)
        if re.search(r"^[وفال]*س.*ب.*ح", w) or "سبح" in w or "تسب" in w or "يسب" in w:
            # Verify by checking key forms
            if any(w.startswith(p) for p in ["سبحان", "سبح", "يسبح", "تسبيح", "تسبح", "سبحي", "سبحوا"]):
                sabbaha_root_surahs.append({"surah": sid, "opening": w})

    # Categorize the musabbihāt explicitly
    forms = {
        "subhana_masdar": [sid for sid in musabbihat if openings[sid].startswith("سبحان")],
        "sabbaha_perfect": [sid for sid in musabbihat if openings[sid].startswith("سبح") and not openings[sid].startswith("سبحان") and not openings[sid].startswith("سبحي")],
        "yusabbihu_imperfect": [sid for sid in musabbihat if openings[sid].startswith("يسبح")],
        "sabbihi_imperative": [sid for sid in musabbihat if openings[sid].startswith("سبح") and not openings[sid].startswith("سبحان") and len(openings[sid]) <= 5 and openings[sid] not in ("سبح", "سبحت")],
    }

    # Count subhana-masdar across ALL 114 surahs
    all_subhana_openers = [sid for sid, w in openings.items() if w.startswith("سبحان")]

    direction_pass = (len(all_subhana_openers) == 1) and (all_subhana_openers[0] == 17)
    verdict = "VINDICATED" if direction_pass else "FALSIFIED"

    out = {
        "id": "Q017-F-02",
        "prereg_sha": PREREG_SHAS["Q017-F-02"],
        "rules_tuple": "(no-tashkeel, orthographic-token, surah-opening-first-token, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "musabbih_openings": musabbih_openings,
        "categorized_forms": forms,
        "all_surahs_opening_with_subhana_masdar": all_subhana_openers,
        "all_sabbaha_root_openers": sabbaha_root_surahs,
        "verdict": verdict,
    }
    with open(os.path.join(OUT_DIR, "Q017-F-02.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[F-02] Q17 opening='{openings[17]}' subhana-masdar-openers={all_subhana_openers} verdict={verdict}", file=sys.stderr)
    return out


# ---------------------------------------------------------------------
# Q017-F-03: Q 17:88 taḥaddī verse — lexical signature + citation density
# ---------------------------------------------------------------------


def F03_tahaddi():
    quran_no = load_quran("no")
    q17 = next(s for s in quran_no if s["id"] == 17)
    v88 = next(v for v in q17["verses"] if v["id"] == 88)
    text88 = v88["text"]

    # Lemma / root checks (substring match on the no-tashkeel form)
    expected_roots = {
        "م-ث-ل (mithl)": "مثل",
        "ج-م-ع (ijtimaʿ)": "اجتمع",
        "ج-ن-ن (jinn)": "الجن",
        "ا-ن-س (ins)": "الإنس",
        "ظ-ه-ر (ẓahīr)": "ظهير",
    }
    lemma_hits = {root: (substr in text88) for root, substr in expected_roots.items()}
    n_hits = sum(lemma_hits.values())

    # Citation density across 9 tafsirs
    tafsir_files = {
        "ibn-kathir": "ibn-kathir-openiti-Q017.txt",
        "tabari": "tabari-openiti-Q017.txt",
        "qurtubi": "qurtubi-openiti-Q017.txt",
        "razi": "razi-openiti-Q017.txt",
        "zamakhshari": "zamakhshari-openiti-Q017.txt",
        "biqai": "biqai-openiti-Q017.txt",
        "tabarsi": "tabarsi-openiti-Q017.txt",
        "thaclabi": "thaclabi-openiti-Q017.txt",
        "suyuti-durr": "suyuti-durr-openiti-Q017.txt",
    }

    citation_hits = {}
    anchors = [
        "بمثل هذا القرآن",
        "اجتمعت الإنس والجن",
        "آية 88",
        "الآية 88",
        "بمثله",
        "إن اجتمعت",
        "ولا يأتون بمثله",
    ]

    for tafsir, fname in tafsir_files.items():
        path = os.path.join(BASE, "data/literature/classical-tafsir/raw", fname)
        if not os.path.exists(path):
            citation_hits[tafsir] = {"present": False, "context_chars": 0, "anchors_hit": []}
            continue
        with open(path, encoding="utf-8") as f:
            content = f.read()
        anchors_hit = [a for a in anchors if a in content]
        # estimate context chars: take widest window around any anchor
        max_ctx = 0
        for a in anchors_hit:
            idx = content.find(a)
            if idx == -1: continue
            # locate next major section break (### or # سورة)
            end_marks = ["### |", "تفسير سورة", "###"]
            end = len(content)
            for em in end_marks:
                j = content.find(em, idx + 1)
                if j != -1 and j < end:
                    end = j
            # cap context window to 5000 chars
            window = min(end - idx, 5000)
            max_ctx = max(max_ctx, window)
        citation_hits[tafsir] = {
            "present": len(anchors_hit) > 0,
            "context_chars": max_ctx,
            "anchors_hit": anchors_hit,
        }

    n_cite = sum(1 for h in citation_hits.values() if h["context_chars"] >= 200)

    direction_pass_A = (n_hits >= 5)
    direction_pass_B = (n_cite >= 4)
    direction_pass = direction_pass_A and direction_pass_B
    verdict = "VINDICATED" if direction_pass else ("PARTIAL" if (direction_pass_A or direction_pass_B) else "FALSIFIED")

    out = {
        "id": "Q017-F-03",
        "prereg_sha": PREREG_SHAS["Q017-F-03"],
        "rules_tuple": "(no-tashkeel, orthographic-token, exegetical-mention, scholar+work+passage, Hafs-Kufan, Mashriqi)",
        "q17_88_text_no_tashkeel": text88,
        "lemma_hits": lemma_hits,
        "n_lemmas": n_hits,
        "citation_hits": citation_hits,
        "n_tafsirs_with_substantive_citation": n_cite,
        "direction_pass_lexical_A": direction_pass_A,
        "direction_pass_citation_B": direction_pass_B,
        "verdict": verdict,
    }
    with open(os.path.join(OUT_DIR, "Q017-F-03.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[F-03] Q17:88 lemmas={n_hits}/5 substantive-citations={n_cite}/9 verdict={verdict}", file=sys.stderr)
    return out


# ---------------------------------------------------------------------
# Q017-F-04: Children-of-Israel narrative concentration in Q 17
# ---------------------------------------------------------------------


def F04_israil_density():
    quran_no = load_quran("no")
    rows = []
    for s in quran_no:
        text = " ".join(v["text"] for v in s["verses"])
        toks = tokens(text)
        n_words = len(toks)
        # match any token containing the lemma "إسرائيل"
        n_isra = sum(1 for w in toks if "إسرائيل" in w)
        density = n_isra / n_words if n_words else 0.0
        rows.append({
            "surah": s["id"],
            "name": s["transliteration"],
            "type": s["type"],
            "n_words": n_words,
            "n_israil_tokens": n_isra,
            "density": density,
        })

    # rank by count and density
    by_count = sorted(rows, key=lambda r: -r["n_israil_tokens"])
    by_density = sorted(rows, key=lambda r: -r["density"])
    for i, r in enumerate(by_count):
        r["rank_count"] = i + 1
    for i, r in enumerate(by_density):
        r["rank_density"] = i + 1
    q17 = next(r for r in rows if r["surah"] == 17)

    direction_pass = (q17["rank_count"] <= 25) or (q17["rank_density"] <= 25)
    verdict = "VINDICATED" if direction_pass else "FALSIFIED"

    out = {
        "id": "Q017-F-04",
        "prereg_sha": PREREG_SHAS["Q017-F-04"],
        "rules_tuple": "(no-tashkeel, orthographic-token, lemma-إسرائيل, surah-level-density, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)",
        "Q17_result": q17,
        "top_10_by_count": by_count[:10],
        "top_10_by_density": by_density[:10],
        "verdict": verdict,
    }
    with open(os.path.join(OUT_DIR, "Q017-F-04.json"), "w") as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"[F-04] Q17 israil-count={q17['n_israil_tokens']} rank_count={q17['rank_count']} "
          f"rank_density={q17['rank_density']} verdict={verdict}", file=sys.stderr)
    return out


# ---------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------


def main():
    verify_preregs()
    F01_alif_monorhyme()
    F02_subhana_opening()
    F03_tahaddi()
    F04_israil_density()
    print("[DONE] Q017-F-01..F-04 complete.", file=sys.stderr)


if __name__ == "__main__":
    main()
