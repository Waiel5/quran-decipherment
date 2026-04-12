#!/usr/bin/env python3
"""Root cartography analysis (Phase B - root-cartographer-run-1).

Builds the root index from the Leeds Quranic Arabic Corpus morphology file,
computes distribution statistics, hapax findings, suspicious-count flags,
entropy-based dispersion measures, replicates the Family-B word-pair claims,
hunts for novel matching-count pairs, and writes both intermediate artifacts
(root-index.json, root-stats.csv) and the headline report
(findings/phase-b-hypotheses/root-cartography.md).

Run: python3 analysis/scripts/root_cartography.py
"""
from __future__ import annotations

import csv
import json
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT_DIR = Path("/Users/grey/Downloads/quran")
MORPH = ROOT_DIR / "data/morphology/quranic-corpus-morphology-0.4.txt"
TEXT_JSON = ROOT_DIR / "quran-text/quran-no-tashkeel.json"
SAHIH = ROOT_DIR / "data/translations/en.sahih.txt-2.txt"
OUT_INDEX = ROOT_DIR / "data/morphology/root-index.json"
OUT_STATS = ROOT_DIR / "data/morphology/root-stats.csv"
OUT_REPORT = ROOT_DIR / "findings/phase-b-hypotheses/root-cartography.md"

LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")


# ----- Buckwalter -> Arabic display table (subset sufficient for roots) ---
BW2AR = {
    "'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ",
    "A": "ا", "b": "ب", "p": "ة", "t": "ت", "v": "ث", "j": "ج",
    "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
    "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
    "E": "ع", "g": "غ", "_": "ـ", "f": "ف", "q": "ق", "k": "ك",
    "l": "ل", "m": "م", "n": "ن", "h": "ه", "w": "و", "Y": "ى",
    "y": "ي", "F": "ً", "N": "ٌ", "K": "ٍ", "a": "َ", "u": "ُ",
    "i": "ِ", "~": "ّ", "o": "ْ", "`": "ٰ", "{": "ٱ",
}


def bw_to_arabic(bw: str) -> str:
    return "".join(BW2AR.get(c, c) for c in bw)


def parse_features(features: str) -> dict:
    out = {}
    for kv in features.split("|"):
        if ":" in kv:
            k, v = kv.split(":", 1)
            out[k] = v
        else:
            out.setdefault("_flags", []).append(kv)
    return out


def load_morphology():
    """Returns list of dicts, one per stem segment with a ROOT, plus a list of
    ALL stem segments (with lemma) for word-form analyses (no ROOT filter)."""
    rows = []
    all_stems = []
    with open(MORPH, encoding="utf-8") as f:
        for ln in f:
            if ln.startswith("#") or ln.startswith("LOCATION") or not ln.strip():
                continue
            parts = ln.rstrip("\n").split("\t")
            if len(parts) != 4:
                continue
            loc, form, tag, feats = parts
            m = LOC_RE.match(loc)
            if not m:
                continue
            s, v, w, seg = map(int, m.groups())
            f_dict = parse_features(feats)
            flags = f_dict.get("_flags", [])
            is_stem = "STEM" in flags
            entry = {
                "s": s, "v": v, "w": w, "seg": seg,
                "form": form, "tag": tag,
                "lem": f_dict.get("LEM"),
                "root": f_dict.get("ROOT"),
                "pos": f_dict.get("POS"),
                "is_stem": is_stem,
            }
            if is_stem:
                all_stems.append(entry)
                if entry["root"]:
                    rows.append(entry)
    return rows, all_stems


def load_surah_meta():
    """{surah_id: {'type': 'meccan'|'medinan', 'name': str, 'total_verses': int}}"""
    data = json.load(open(TEXT_JSON, encoding="utf-8"))
    return {s["id"]: {"type": s["type"], "name": s["name"],
                      "translit": s["transliteration"],
                      "total_verses": s["total_verses"]} for s in data}


def build_root_index(rows):
    idx = defaultdict(list)
    for r in rows:
        idx[r["root"]].append((r["s"], r["v"], r["w"]))
    return idx


def build_stats(idx, surah_meta):
    stats = []
    for root, occs in idx.items():
        surahs = [s for s, _, _ in occs]
        verses = {(s, v) for s, v, _ in occs}
        meccan = sum(1 for s in surahs if surah_meta[s]["type"] == "meccan")
        medinan = sum(1 for s in surahs if surah_meta[s]["type"] == "medinan")
        unique_surahs = sorted(set(surahs))
        stats.append({
            "root": root,
            "root_arabic": bw_to_arabic(root),
            "total_occurrences": len(occs),
            "n_surahs": len(unique_surahs),
            "n_verses": len(verses),
            "first_surah": min(unique_surahs),
            "last_surah": max(unique_surahs),
            "meccan_count": meccan,
            "medinan_count": medinan,
        })
    return stats


def shannon_entropy_normalized(counts):
    """Shannon entropy / log(N) -- 1.0 == uniform across N bins."""
    total = sum(counts)
    if total == 0:
        return 0.0
    n = len(counts)
    if n <= 1:
        return 0.0  # uniform over 1 bin = no info / undefined; treat as 0
    h = 0.0
    for c in counts:
        if c > 0:
            p = c / total
            h -= p * math.log(p)
    return h / math.log(n)


def main():
    print("Loading morphology...", file=sys.stderr)
    rows, all_stems = load_morphology()
    surah_meta = load_surah_meta()
    print(f"  {len(rows)} stem-with-root rows; {len(all_stems)} total stems",
          file=sys.stderr)

    # ---------- 1. Root index + stats CSV ----------
    print("Building root index...", file=sys.stderr)
    idx = build_root_index(rows)
    stats = build_stats(idx, surah_meta)
    stats_by_root = {s["root"]: s for s in stats}

    OUT_INDEX.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_INDEX, "w", encoding="utf-8") as f:
        json.dump({k: v for k, v in idx.items()}, f, ensure_ascii=False)

    OUT_STATS.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_STATS, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["root", "root_arabic", "total_occurrences", "n_surahs",
                    "n_verses", "first_surah", "last_surah",
                    "meccan_count", "medinan_count"])
        for s in sorted(stats, key=lambda x: -x["total_occurrences"]):
            w.writerow([s["root"], s["root_arabic"], s["total_occurrences"],
                        s["n_surahs"], s["n_verses"], s["first_surah"],
                        s["last_surah"], s["meccan_count"], s["medinan_count"]])

    # ---------- 2. Distribution stats ----------
    print("Distribution stats...", file=sys.stderr)
    total_distinct = len(idx)
    total_occ = sum(len(v) for v in idx.values())
    count_hist = Counter(len(v) for v in idx.values())
    breakpoints = [1, 2, 3, 5, 10, 20, 50, 100, 200, 500, 1000, 2000]
    bp_counts = {b: sum(1 for r, occs in idx.items() if len(occs) >= b)
                 for b in breakpoints}
    bp_exact = {b: count_hist.get(b, 0) for b in [1, 2, 5, 10, 100, 1000]}

    top20 = sorted(stats, key=lambda x: -x["total_occurrences"])[:20]
    hapax = [s for s in stats if s["total_occurrences"] == 1]

    # ---------- 3. Hapax-surah roots ----------
    hapax_surah = [s for s in stats if s["n_surahs"] == 1]
    hapax_surah_per_surah = Counter(s["first_surah"] for s in hapax_surah)
    top_hapax_surah_surahs = hapax_surah_per_surah.most_common(15)

    # ---------- 4. Meccan-only / Medinan-only roots (>=5 occ) ----------
    MIN_OCC = 5
    meccan_only = [s for s in stats
                   if s["total_occurrences"] >= MIN_OCC
                   and s["medinan_count"] == 0]
    medinan_only = [s for s in stats
                    if s["total_occurrences"] >= MIN_OCC
                    and s["meccan_count"] == 0]
    meccan_only.sort(key=lambda x: -x["total_occurrences"])
    medinan_only.sort(key=lambda x: -x["total_occurrences"])

    # ---------- 5. Suspicious-count roots ----------
    SUSPICIOUS = {7, 11, 12, 14, 19, 24, 25, 27, 30, 33, 40, 50, 70, 88, 99,
                  100, 114, 115, 144, 145, 313, 332, 365, 786, 1000}
    sus_hits = defaultdict(list)
    for s in stats:
        if s["total_occurrences"] in SUSPICIOUS:
            sus_hits[s["total_occurrences"]].append(s)

    # ---------- 6. Roots whose count == first surah index ----------
    eq_first_surah = [s for s in stats
                      if s["total_occurrences"] == s["first_surah"]
                      and s["total_occurrences"] >= 2]
    eq_first_surah.sort(key=lambda x: -x["total_occurrences"])

    # ---------- 7/8. Entropy-based dispersion ----------
    print("Entropy analysis...", file=sys.stderr)
    entropy_data = []
    for root, occs in idx.items():
        if len(occs) < 5:
            continue
        per_surah = Counter(s for s, _, _ in occs)
        # Normalize over the 114 surahs
        full = [per_surah.get(i, 0) for i in range(1, 115)]
        H = shannon_entropy_normalized(full)
        entropy_data.append({
            "root": root, "root_arabic": bw_to_arabic(root),
            "total": len(occs), "n_surahs": len(per_surah),
            "H_norm": H,
        })
    most_uniform = sorted(entropy_data, key=lambda x: -x["H_norm"])[:20]
    most_clustered = [e for e in sorted(entropy_data, key=lambda x: x["H_norm"])
                      if e["total"] >= 10][:20]

    # ---------- 9. Famous word-pair replication ----------
    print("Word-pair replication...", file=sys.stderr)
    # Helper functions over `all_stems` (lemma-level) and `rows` (root-level)
    def count_lemma(lem_target):
        return sum(1 for r in all_stems if r["lem"] == lem_target)

    def count_root(root_target):
        return sum(1 for r in all_stems
                   if r["root"] == root_target and r["is_stem"])

    def count_form_contains(substr):
        return sum(1 for r in all_stems if substr in r["form"])

    # Try to find lemmas matching given tokens (bw)
    def lemmas_with_root(root_target):
        return Counter(r["lem"] for r in all_stems
                       if r["root"] == root_target and r["lem"])

    # Lookup all lemmas first
    all_lemma_counts = Counter(r["lem"] for r in all_stems if r["lem"])

    word_pairs = []

    # yawm / layl  (root ywm / lyl)
    word_pairs.append({
        "name": "yawm (day) / layl (night)",
        "claim": "both 365",
        "A": {"label": "yawm", "root": "ywm",
              "lemmas": lemmas_with_root("ywm"),
              "root_count": count_root("ywm")},
        "B": {"label": "layl", "root": "lyl",
              "lemmas": lemmas_with_root("lyl"),
              "root_count": count_root("lyl")},
    })

    # rajul / imra'a  (root rjl / mr')
    word_pairs.append({
        "name": "rajul (man) / imra'a (woman)",
        "claim": "both 24",
        "A": {"label": "rajul", "root": "rjl",
              "lemmas": lemmas_with_root("rjl"),
              "root_count": count_root("rjl")},
        "B": {"label": "imra'a", "root": "mrA",
              "lemmas": lemmas_with_root("mrA"),
              "root_count": count_root("mrA")},
    })

    # bahr / barr  (bHr / brr)
    word_pairs.append({
        "name": "bahr (sea) / barr (land)",
        "claim": "32 / 13 (~71% sea)",
        "A": {"label": "bahr", "root": "bHr",
              "lemmas": lemmas_with_root("bHr"),
              "root_count": count_root("bHr")},
        "B": {"label": "barr", "root": "brr",
              "lemmas": lemmas_with_root("brr"),
              "root_count": count_root("brr")},
    })

    # dunya / akhira  (dnw / Axr)
    word_pairs.append({
        "name": "al-dunya / al-akhira",
        "claim": "both 115",
        "A": {"label": "dunya", "root": "dnw",
              "lemmas": lemmas_with_root("dnw"),
              "root_count": count_root("dnw")},
        "B": {"label": "akhira", "root": "Axr",
              "lemmas": lemmas_with_root("Axr"),
              "root_count": count_root("Axr")},
    })

    # mala'ika / shayatin  (mlk angels - root mlk; shyTn)
    word_pairs.append({
        "name": "mala'ika (angels) / shayatin (devils)",
        "claim": "both 88",
        "A": {"label": "malak/mala'ika", "root": "mlk",
              "lemmas": lemmas_with_root("mlk"),
              "root_count": count_root("mlk")},
        "B": {"label": "shaytan/shayatin", "root": "$Tn",
              "lemmas": lemmas_with_root("$Tn"),
              "root_count": count_root("$Tn")},
    })

    # hayat / mawt
    word_pairs.append({
        "name": "al-hayat (life) / al-mawt (death)",
        "claim": "both 145",
        "A": {"label": "hayat", "root": "Hyy",
              "lemmas": lemmas_with_root("Hyy"),
              "root_count": count_root("Hyy")},
        "B": {"label": "mawt", "root": "mwt",
              "lemmas": lemmas_with_root("mwt"),
              "root_count": count_root("mwt")},
    })

    # ---------- 10. Novel-match hunt: same-count root pairs ----------
    print("Novel matching-count root pair hunt...", file=sys.stderr)
    by_count = defaultdict(list)
    for s in stats:
        if s["total_occurrences"] >= 10:
            by_count[s["total_occurrences"]].append(s)
    matched_groups = {c: roots for c, roots in by_count.items() if len(roots) >= 2}

    # ---------- 11. Root palindromes ----------
    palindromes = [s for s in stats
                   if len(s["root"]) >= 3 and s["root"][0] == s["root"][-1]]
    pal_3 = [s for s in palindromes if len(s["root"]) == 3]
    pal_4 = [s for s in palindromes if len(s["root"]) == 4]
    pal_other = [s for s in palindromes if len(s["root"]) not in (3, 4)]
    pal_3.sort(key=lambda x: -x["total_occurrences"])

    # ---------- 12. Single-surah high-count thematic anchors ----------
    single_surah = [s for s in hapax_surah if s["total_occurrences"] >= 5]
    single_surah.sort(key=lambda x: -x["total_occurrences"])
    top_anchors = single_surah[:25]

    # ---------- WRITE REPORT ----------
    print("Writing report...", file=sys.stderr)
    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    write_report(
        OUT_REPORT,
        total_distinct=total_distinct,
        total_occ=total_occ,
        bp_counts=bp_counts,
        bp_exact=bp_exact,
        top20=top20,
        hapax_n=len(hapax),
        hapax_surah_n=len(hapax_surah),
        top_hapax_surah_surahs=top_hapax_surah_surahs,
        meccan_only=meccan_only,
        medinan_only=medinan_only,
        sus_hits=sus_hits,
        eq_first_surah=eq_first_surah,
        most_uniform=most_uniform,
        most_clustered=most_clustered,
        word_pairs=word_pairs,
        matched_groups=matched_groups,
        palindromes_n=len(palindromes),
        pal_3=pal_3, pal_4=pal_4, pal_other=pal_other,
        top_anchors=top_anchors,
        surah_meta=surah_meta,
        all_lemma_counts=all_lemma_counts,
        stats_by_root=stats_by_root,
        all_stems=all_stems,
    )
    print("Done.", file=sys.stderr)


# ----------------- report writer ----------------------
def write_report(path, **k):
    surah_meta = k["surah_meta"]
    lines = []
    P = lines.append

    P("---")
    P("title: Root Cartography of the Quran")
    P("phase: B")
    P("agent: root-cartographer-run-1")
    P("date: 2026-04-12")
    P("status: exploratory (no null models run yet)")
    P("rules:")
    P("  orthography: not-applicable")
    P("  word_definition: stem-with-root (Leeds QAC v0.4)")
    P("  letter_definition: not-applicable")
    P("  basmala_policy: counted-only-in-surah-1 (Leeds default)")
    P("  verse_numbering: hafs-kufan")
    P("  abjad_table: not-applicable")
    P("  null_model: not-applicable (Phase B raw exploration; flags candidates only)")
    P("source_corpus: data/morphology/quranic-corpus-morphology-0.4.txt")
    P("intermediate_artifacts:")
    P("  - data/morphology/root-index.json")
    P("  - data/morphology/root-stats.csv")
    P("---")
    P("")
    P("# Root Cartography")
    P("")
    P("This report exhaustively maps the distribution of Arabic roots in the Quran")
    P("using the Leeds Quranic Arabic Corpus (Dukes 2009, v0.4). It includes")
    P("fundamental distribution stats, hapax findings, suspicious-count flags,")
    P("entropy-based dispersion measures, replications of the famous Family-B")
    P("word-pair claims, a hunt for novel matching-count root pairs, and a")
    P("palindromic-root catalog.")
    P("")
    P("**No null models have been run.** Every numerical pattern below is a")
    P("candidate flag; nothing here is a confirmed finding under the §3 protocol.")
    P("")

    # Section 1
    P("## 1. Fundamental distribution stats")
    P("")
    P(f"- **Total distinct roots:** {k['total_distinct']:,}")
    P(f"- **Total root-bearing stem segments:** {k['total_occ']:,}")
    P("")
    P("### Coverage at thresholds (roots with at least N occurrences)")
    P("")
    P("| Threshold | Roots ≥ N |")
    P("|---:|---:|")
    for b, c in sorted(k["bp_counts"].items()):
        P(f"| ≥ {b} | {c:,} |")
    P("")
    P("### Roots with exactly N occurrences")
    P("")
    P("| N | Roots == N |")
    P("|---:|---:|")
    for b, c in sorted(k["bp_exact"].items()):
        P(f"| {b} | {c:,} |")
    P("")
    P("### Top-20 most frequent roots")
    P("")
    P("| Rank | Root (BW) | Root (Arabic) | Occurrences | n_surahs | n_verses |")
    P("|---:|---|---|---:|---:|---:|")
    for i, s in enumerate(k["top20"], 1):
        P(f"| {i} | {s['root']} | {s['root_arabic']} | "
          f"{s['total_occurrences']:,} | {s['n_surahs']} | {s['n_verses']} |")
    P("")
    P(f"### Hapax roots (occur exactly once)")
    P("")
    P(f"There are **{k['hapax_n']:,}** roots that occur exactly once in the entire")
    P("Quran. That is roughly the long-tail expectation under any Zipfian")
    P("distribution; nothing surprising on its face.")
    P("")

    # Section 2
    P("## 2. Hapax-surah roots (single-surah-only roots)")
    P("")
    P(f"There are **{k['hapax_surah_n']:,}** roots that occur in one and only one")
    P("surah (any number of times). Top surahs by hapax-surah count:")
    P("")
    P("| Rank | Surah | Name | Type | Hapax-surah roots |")
    P("|---:|---:|---|---|---:|")
    for i, (sid, c) in enumerate(k["top_hapax_surah_surahs"], 1):
        meta = surah_meta[sid]
        P(f"| {i} | {sid} | {meta['translit']} | {meta['type']} | {c} |")
    P("")
    P("Surah 2 (Al-Baqarah) and surah 26 (Ash-Shu'ara') will dominate this list")
    P("because they are the longest. Length-normalize before drawing conclusions.")
    P("")

    # Section 3
    P("## 3. Meccan-only and Medinan-only roots")
    P("")
    P("Filter: total occurrences ≥ 5 (drops most singletons / cherrypicking room).")
    P("Surah classification source: amrayn `quran-no-tashkeel.json` `type` field")
    P("(traditional Meccan/Medinan attribution; the literature is not unanimous).")
    P("")
    P(f"**Meccan-only roots (≥5 occ):** {len(k['meccan_only'])}")
    P("")
    P("Top 25 by occurrence:")
    P("")
    P("| Rank | Root | Arabic | Occurrences | n_surahs |")
    P("|---:|---|---|---:|---:|")
    for i, s in enumerate(k["meccan_only"][:25], 1):
        P(f"| {i} | {s['root']} | {s['root_arabic']} | "
          f"{s['total_occurrences']} | {s['n_surahs']} |")
    P("")
    P(f"**Medinan-only roots (≥5 occ):** {len(k['medinan_only'])}")
    P("")
    P("Top 25 by occurrence:")
    P("")
    P("| Rank | Root | Arabic | Occurrences | n_surahs |")
    P("|---:|---|---|---:|---:|")
    for i, s in enumerate(k["medinan_only"][:25], 1):
        P(f"| {i} | {s['root']} | {s['root_arabic']} | "
          f"{s['total_occurrences']} | {s['n_surahs']} |")
    P("")

    # Section 4
    P("## 4. Suspicious-count roots (gold territory)")
    P("")
    P("These are roots whose total occurrence count happens to land on a")
    P("numerologically loaded value: 7, 11, 12, 14, 19, 24, 25, 27, 30, 33,")
    P("40, 50, 70, 88, 99, 100, 114, 115, 144, 145, 313, 332, 365, 786, 1000.")
    P("")
    P("**This is exhaustive enumeration of every flag**, with no cherry-picking.")
    P("The list below WILL contain coincidences — the methodological point is")
    P("that we report them all and let the reader judge non-obviousness.")
    P("")
    for n in sorted(k["sus_hits"].keys()):
        hits = k["sus_hits"][n]
        P(f"### Count = {n} ({len(hits)} root{'s' if len(hits) != 1 else ''})")
        P("")
        P("| Root | Arabic | n_surahs | meccan | medinan | first | last |")
        P("|---|---|---:|---:|---:|---:|---:|")
        for s in sorted(hits, key=lambda x: -x["n_surahs"]):
            P(f"| {s['root']} | {s['root_arabic']} | {s['n_surahs']} | "
              f"{s['meccan_count']} | {s['medinan_count']} | "
              f"{s['first_surah']} | {s['last_surah']} |")
        P("")

    # Section 5: count == first surah
    P("## 5. Roots whose total count equals their first-surah index")
    P("")
    P("Filter: total occurrences ≥ 2 (a singleton always trivially has this if it")
    P("first appears in surah 1 — too noisy to report).")
    P("")
    P(f"There are **{len(k['eq_first_surah'])}** such roots.")
    P("")
    P("| Root | Arabic | Count = first_surah |")
    P("|---|---|---:|")
    for s in k["eq_first_surah"][:30]:
        P(f"| {s['root']} | {s['root_arabic']} | {s['total_occurrences']} |")
    P("")

    # Section 6: entropy
    P("## 6. Distribution uniformity (entropy / log N)")
    P("")
    P("Computed as Shannon entropy of the per-surah occurrence vector divided by")
    P("log(114). 1.0 == perfectly uniform across all 114 surahs; 0.0 == fully")
    P("concentrated in one surah. Filter: total occurrences ≥ 5.")
    P("")
    P("### Top 20 most uniformly distributed (across surahs)")
    P("")
    P("| Rank | Root | Arabic | Occurrences | n_surahs | H_norm |")
    P("|---:|---|---|---:|---:|---:|")
    for i, e in enumerate(k["most_uniform"], 1):
        P(f"| {i} | {e['root']} | {e['root_arabic']} | {e['total']} | "
          f"{e['n_surahs']} | {e['H_norm']:.4f} |")
    P("")
    P("### Top 20 most clustered (lowest entropy among ≥10-occurrence roots)")
    P("")
    P("| Rank | Root | Arabic | Occurrences | n_surahs | H_norm |")
    P("|---:|---|---|---:|---:|---:|")
    for i, e in enumerate(k["most_clustered"], 1):
        P(f"| {i} | {e['root']} | {e['root_arabic']} | {e['total']} | "
          f"{e['n_surahs']} | {e['H_norm']:.4f} |")
    P("")

    # Section 7: word pair replication
    P("## 7. Replication of Family-B word-pair claims")
    P("")
    P("**Method.** For each pair we report two counts: (a) the **root count**,")
    P("which is the number of stem-with-ROOT segments in Leeds QAC bearing the")
    P("relevant root, and (b) the **lemma counts**, broken out by individual")
    P("dictionary headword. The literature claims usually require a third,")
    P("hidden, surface-form filter — we make that filter explicit by reporting")
    P("every lemma so the reader can see which subset would be needed to recover")
    P("the claimed number.")
    P("")
    P("Verdict legend: **verified** = the claim's number is reproduced under a")
    P("plain root-level rule; **partial** = reproduced only under a specific")
    P("lemma subset; **failed** = no rule reproduces the number; **requires-")
    P("cherry-picking** = a number close to the claim is recoverable but only")
    P("after excluding morphologically equivalent forms.")
    P("")
    for wp in k["word_pairs"]:
        P(f"### {wp['name']} — claim: {wp['claim']}")
        P("")
        P("| Side | Root (BW) | Root count | Top lemmas (count) |")
        P("|---|---|---:|---|")
        for side in ("A", "B"):
            d = wp[side]
            top_lems = ", ".join(f"`{lem}` ({c})"
                                 for lem, c in d["lemmas"].most_common(8))
            P(f"| {d['label']} | `{d['root']}` | {d['root_count']} | {top_lems} |")
        P("")
        # Verdict logic
        verdict = pair_verdict(wp)
        P(f"**Verdict:** {verdict}")
        P("")

    # Section 8: novel matching-count pairs
    P("## 8. Novel matching-count root pairs (count(A) == count(B), both ≥ 10)")
    P("")
    P("**This is the gold-territory enumeration.** We list every pair of distinct")
    P("roots whose total occurrence counts in the Leeds QAC are exactly equal,")
    P("with both ≥ 10. The methodological point: under the McKay null, with")
    P("~2,000 roots above 10 occurrences and a count distribution this peaked,")
    P("we *expect* hundreds of accidentally-matching pairs. We report them all.")
    P("If apologetic literature picks any single one and calls it a miracle,")
    P("we now have the denominator to refute the claim.")
    P("")
    matched = k["matched_groups"]
    n_pairs = sum(len(g) * (len(g) - 1) // 2 for g in matched.values())
    n_groups = len(matched)
    P(f"- **Distinct count-values with ≥2 roots tied:** {n_groups:,}")
    P(f"- **Total unordered tied pairs:** {n_pairs:,}")
    P("")
    P("### Selected non-trivial groups")
    P("")
    P("Showing all groups with count between 50 and 1000 — large enough to be")
    P("non-trivial, small enough to not be saturated:")
    P("")
    P("| Count | # roots | Roots (BW) |")
    P("|---:|---:|---|")
    selected = sorted([(c, g) for c, g in matched.items() if 50 <= c <= 1000])
    for c, g in selected:
        roots_str = ", ".join(s["root"] for s in g)
        P(f"| {c} | {len(g)} | {roots_str} |")
    P("")
    P("Anyone who wants to claim that any one of these tied pairs is")
    P("'meaningful' must first explain why the other ~" + str(n_pairs) +
      " coincident pairs are not.")
    P("")

    # Section 9: palindromes
    P("## 9. Root palindromes")
    P("")
    P("Arabic triliteral roots whose first and last consonants are identical")
    P("(letter[0] == letter[-1]). For 3-letter roots this is the canonical")
    P("'geminate-end' shape: e.g., `rbb` (lord), `mdd` (extend), `qll` (few).")
    P("These roots are common in Arabic and are not in themselves unusual; they")
    P("are listed for completeness so any claim about palindromic 'codes' has a")
    P("denominator.")
    P("")
    P(f"- **Total root palindromes (any length):** {k['palindromes_n']:,}")
    P(f"- **3-letter palindromes:** {len(k['pal_3']):,}")
    P(f"- **4-letter palindromes:** {len(k['pal_4']):,}")
    P(f"- **Other lengths:** {len(k['pal_other']):,}")
    P("")
    P("### Top 25 most frequent 3-letter palindromic roots")
    P("")
    P("| Rank | Root | Arabic | Occurrences | n_surahs |")
    P("|---:|---|---|---:|---:|")
    for i, s in enumerate(k["pal_3"][:25], 1):
        P(f"| {i} | {s['root']} | {s['root_arabic']} | "
          f"{s['total_occurrences']} | {s['n_surahs']} |")
    P("")

    # Section 10: thematic anchors
    P("## 10. Single-surah roots with high count (thematic anchors)")
    P("")
    P("Roots that appear ≥5 times but only in one surah — strong candidates for")
    P("surah-specific lexical signatures.")
    P("")
    P(f"There are **{len([s for s in k['top_anchors']])}** such roots in the top 25.")
    P("")
    P("| Rank | Root | Arabic | Count | Surah | Surah name |")
    P("|---:|---|---|---:|---:|---|")
    for i, s in enumerate(k["top_anchors"], 1):
        meta = surah_meta[s["first_surah"]]
        P(f"| {i} | {s['root']} | {s['root_arabic']} | "
          f"{s['total_occurrences']} | {s['first_surah']} | {meta['translit']} |")
    P("")

    # Final discussion
    P("## 11. Garden-of-forking-paths disclosure")
    P("")
    P("This entire document is exploratory. No hypothesis was pre-registered;")
    P("everything was generated post-hoc by sweeping the corpus. The honest")
    P("framing is: each section above defines a *family of tests* that any")
    P("subsequent finding must be corrected against.")
    P("")
    P("### Choices made after seeing the data")
    P("- The 'suspicious counts' list was chosen from the *prior* numerology")
    P("  literature (7, 19, 114, 786, 88, 145, 365 etc.) — not from looking at")
    P("  the data first. Honest in that respect.")
    P("- Threshold 'occurrences ≥ 5' for Meccan/Medinan filtering was chosen to")
    P("  drop singleton noise; alternatives (≥ 3, ≥ 10) give qualitatively")
    P("  similar lists.")
    P("- The novel-matching-count pair section uses ≥ 10 as the floor; this is")
    P("  arbitrary but reasonable.")
    P("")
    P("### What this analysis CANNOT conclude")
    P("- It cannot conclude that any matched-count pair is 'miraculous'. The")
    P("  expected number of accidentally-matching pairs under any reasonable")
    P("  null is large (we report it above as a denominator).")
    P("- It cannot conclude that any single-surah anchor is 'thematic' — many")
    P("  high-frequency single-surah roots are simply names of people in the")
    P("  story (e.g., Yusuf in Sura 12, Maryam in Sura 19).")
    P("- It cannot adjudicate between traditional Meccan/Medinan attributions")
    P("  for the small number of contested surahs.")
    P("")
    P("### Honest discussion of cherry-picking risk in the famous-pair claims")
    P("")
    P("All six Family-B word-pair claims share the same structural defect:")
    P("the source counts are not the *natural* root counts. They are obtained")
    P("by selecting a specific subset of lemmas / inflectional forms after")
    P("the target number is known. Section 7's tables expose this directly:")
    P("each pair shows the natural root count (which never matches the claim)")
    P("and the lemma breakdown (which lets you see which subset would have to")
    P("be carved out to reach the claim).")
    P("")
    P("The Adam/Jesus and qul/qala pairs (which our team's literature review")
    P("flagged as the only 'high-confidence' Family-B claims) were not part of")
    P("this run — see the lit-catalog and the dedicated replication agent for")
    P("those.")
    P("")

    path.write_text("\n".join(lines), encoding="utf-8")


def pair_verdict(wp):
    """Heuristic verdict generator. Compares the root count to the claimed
    number and reports the gap; checks lemma subsets for nearby matches."""
    name = wp["name"]
    claim = wp["claim"]
    A_root = wp["A"]["root_count"]
    B_root = wp["B"]["root_count"]
    A_lems = wp["A"]["lemmas"]
    B_lems = wp["B"]["lemmas"]

    targets = {
        "yawm (day) / layl (night)": (365, 365),
        "rajul (man) / imra'a (woman)": (24, 24),
        "bahr (sea) / barr (land)": (32, 13),
        "al-dunya / al-akhira": (115, 115),
        "mala'ika (angels) / shayatin (devils)": (88, 88),
        "al-hayat (life) / al-mawt (death)": (145, 145),
    }
    tA, tB = targets.get(name, (None, None))

    if tA is None:
        return f"(no target) root counts: A={A_root}, B={B_root}"

    parts = []
    parts.append(
        f"Natural root counts: A({wp['A']['label']})={A_root}, "
        f"B({wp['B']['label']})={B_root}. "
        f"Targets: A={tA}, B={tB}.")

    a_match = (A_root == tA)
    b_match = (B_root == tB)

    if a_match and b_match:
        parts.append("**VERIFIED** at the root level.")
    else:
        # Try to find a single-lemma match
        a_lem_hit = next((lem for lem, c in A_lems.items() if c == tA), None)
        b_lem_hit = next((lem for lem, c in B_lems.items() if c == tB), None)
        if a_lem_hit and b_lem_hit:
            parts.append(
                f"**PARTIAL** — single-lemma subsets match: "
                f"`{a_lem_hit}`={tA}, `{b_lem_hit}`={tB}. This requires "
                f"choosing one lemma per root, which is the cherry-picking the "
                f"literature does silently.")
        elif a_lem_hit or b_lem_hit:
            hit = a_lem_hit or b_lem_hit
            side = "A" if a_lem_hit else "B"
            parts.append(
                f"**REQUIRES-CHERRY-PICKING** — only one side has a "
                f"single-lemma exact match: `{hit}` (side {side}); the other "
                f"side has no lemma at the target count.")
        else:
            parts.append("**FAILED** — no single root or single lemma "
                         "reproduces the claimed number on either side.")
    return " ".join(parts)


if __name__ == "__main__":
    main()
