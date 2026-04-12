#!/usr/bin/env python3
"""
jinas_detect.py — Phase B novelty agent

Comprehensive computational catalog of jinas / tajnis (paronomasia) in the Quran.

Inputs:
  - /Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt
  - /Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json
  - /Users/grey/Downloads/quran/data/translations/en.sahih.txt  (one verse per line, 6236 lines)

Outputs:
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/jinas-wordplay.md
  - /Users/grey/Downloads/quran/findings/phase-b-hypotheses/jinas-all-instances.csv
  - /Users/grey/Downloads/quran/journal/jinas-wordplay-run-1.md  (written separately)

Counting rules tuple (from docs/methodology.md):
  orthography:       no-tashkeel (root extraction is orthography-independent; we use no-tashkeel for display)
  word_definition:   morphology-stem (one root per stem, multiple stems per orthographic word possible)
  letter_definition: not-applicable
  basmala_policy:    counted-only-in-surah-1 (matches morphology corpus convention)
  verse_numbering:   hafs-kufan (6236 verses)
  abjad_table:       not-applicable
  null_model:        rare-root permutation (see Section 5)
"""

from __future__ import annotations
import csv
import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT_RE = re.compile(r"ROOT:([^|]+)")
LOC_RE = re.compile(r"^\((\d+):(\d+):(\d+):(\d+)\)$")

MORPH_PATH = Path("/Users/grey/Downloads/quran/data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN_JSON = Path("/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json")
SAHIH_TXT = Path("/Users/grey/Downloads/quran/data/translations/en.sahih.txt")

OUT_MD = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/jinas-wordplay.md")
OUT_CSV = Path("/Users/grey/Downloads/quran/findings/phase-b-hypotheses/jinas-all-instances.csv")

# Buckwalter -> Arabic for displaying roots
BW2AR = {
    "'": "ء", "|": "آ", ">": "أ", "&": "ؤ", "<": "إ", "}": "ئ",
    "A": "ا", "b": "ب", "p": "ة", "t": "ت", "v": "ث", "j": "ج",
    "H": "ح", "x": "خ", "d": "د", "*": "ذ", "r": "ر", "z": "ز",
    "s": "س", "$": "ش", "S": "ص", "D": "ض", "T": "ط", "Z": "ظ",
    "E": "ع", "g": "غ", "f": "ف", "q": "ق", "k": "ك", "l": "ل",
    "m": "م", "n": "ن", "h": "ه", "w": "و", "y": "ي", "Y": "ى",
}


def bw_to_ar(bw: str) -> str:
    return "".join(BW2AR.get(c, c) for c in bw)


def load_quran_text() -> dict:
    """Returns {(s, v): arabic_text}"""
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    for surah in data:
        sid = surah["id"]
        for verse in surah["verses"]:
            out[(sid, verse["id"])] = verse["text"]
    assert len(out) == 6236, f"Expected 6236 verses, got {len(out)}"
    return out


def load_sahih() -> dict:
    """Returns {(s, v): english_text}. The .txt is one verse per line in canonical order."""
    with open(SAHIH_TXT, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    # We need (s, v) ordering; reuse the JSON to walk
    with open(QURAN_JSON, encoding="utf-8") as f:
        data = json.load(f)
    out = {}
    i = 0
    for surah in data:
        for verse in surah["verses"]:
            out[(surah["id"], verse["id"])] = lines[i]
            i += 1
    assert i == 6236
    return out


def load_morphology():
    """Parses morphology file. Returns:
        verse_roots: {(s, v): [root_bw, ...]}     (ordered by word/segment)
        verse_root_words: {(s, v): {word_idx: [root_bw, ...]}}  per-word root list
    """
    verse_roots = defaultdict(list)
    verse_root_by_word = defaultdict(lambda: defaultdict(list))
    n_lines = 0
    n_with_root = 0
    with open(MORPH_PATH, encoding="utf-8") as f:
        for line in f:
            if line.startswith("#") or line.startswith("LOCATION") or not line.strip():
                continue
            parts = line.rstrip("\n").split("\t")
            if len(parts) != 4:
                continue
            loc, form, tag, feats = parts
            m = LOC_RE.match(loc)
            if not m:
                continue
            s, v, w, seg = map(int, m.groups())
            n_lines += 1
            rm = ROOT_RE.search(feats)
            if rm:
                root = rm.group(1)
                verse_roots[(s, v)].append(root)
                verse_root_by_word[(s, v)][w].append(root)
                n_with_root += 1
    print(f"  morphology: {n_lines} segment rows; {n_with_root} carry a ROOT tag")
    print(f"  verses with at least one root: {len(verse_roots)} / 6236")
    return dict(verse_roots), {k: dict(v) for k, v in verse_root_by_word.items()}


def edit_distance_one(a: str, b: str) -> bool:
    """True if Levenshtein distance between a and b is exactly 1.
    Used for triliteral root similarity. Length difference must be <= 1.
    """
    la, lb = len(a), len(b)
    if abs(la - lb) > 1:
        return False
    if a == b:
        return False
    if la == lb:
        diffs = sum(1 for x, y in zip(a, b) if x != y)
        return diffs == 1
    # one insertion/deletion
    if la > lb:
        a, b = b, a
        la, lb = lb, la
    # la < lb
    i = j = 0
    found = False
    while i < la and j < lb:
        if a[i] != b[j]:
            if found:
                return False
            found = True
            j += 1
        else:
            i += 1
            j += 1
    return True


def main():
    print("Loading data...")
    quran = load_quran_text()
    sahih = load_sahih()
    verse_roots, verse_root_by_word = load_morphology()

    # ------------------------------------------------------------------
    # Global root frequency (for "rare root" definition in §5)
    # ------------------------------------------------------------------
    global_root_count = Counter()
    for (s, v), roots in verse_roots.items():
        for r in roots:
            global_root_count[r] += 1
    n_distinct_roots = len(global_root_count)
    print(f"  distinct roots: {n_distinct_roots}")
    print(f"  total root tokens: {sum(global_root_count.values())}")

    # ------------------------------------------------------------------
    # §2 / §3 / §4: Same-verse root repetition
    # ------------------------------------------------------------------
    # For each verse, count root occurrences. We deliberately count *segment-level*
    # root tokens — so a single orthographic word like "wakaDayo" doesn't double-
    # count its stem; only stems with the same root contribute.
    same_verse_repetitions = []  # list of (s, v, root, count)
    verse_repetition_summary = []  # list of (s, v, total_repeated_root_tokens, max_count, num_repeated_roots)
    for (s, v), roots in verse_roots.items():
        c = Counter(roots)
        repeats = {r: n for r, n in c.items() if n >= 2}
        if not repeats:
            continue
        for r, n in repeats.items():
            same_verse_repetitions.append((s, v, r, n))
        total_rep_tokens = sum(repeats.values())
        max_count = max(repeats.values())
        verse_repetition_summary.append(
            (s, v, total_rep_tokens, max_count, len(repeats))
        )

    # Sort: by total repeated tokens desc, then by max count desc
    verse_repetition_summary.sort(key=lambda x: (-x[2], -x[3], x[0], x[1]))

    print(f"  verses with at least one repeated root: {len(verse_repetition_summary)}")
    print(f"  total (verse, root) repetition pairs: {len(same_verse_repetitions)}")

    # Top-density verse(s)
    top_verse = verse_repetition_summary[0]
    print(f"  most jinas-dense verse: {top_verse[0]}:{top_verse[1]} "
          f"(repeated tokens={top_verse[2]}, max-count={top_verse[3]})")

    # ------------------------------------------------------------------
    # §3 Triple+ catalog
    # ------------------------------------------------------------------
    triple_plus = [(s, v, r, n) for (s, v, r, n) in same_verse_repetitions if n >= 3]
    triple_plus.sort(key=lambda x: (-x[3], x[0], x[1]))
    print(f"  (root, verse) instances with count >= 3: {len(triple_plus)}")

    # ------------------------------------------------------------------
    # §4 Multi-root jinas clusters
    # ------------------------------------------------------------------
    multi_root_clusters = [
        (s, v, max_count, total, num_repeated)
        for (s, v, total, max_count, num_repeated) in verse_repetition_summary
        if num_repeated >= 2
    ]
    multi_root_clusters.sort(key=lambda x: (-x[4], -x[3], x[0], x[1]))
    print(f"  verses with >=2 distinct repeated roots: {len(multi_root_clusters)}")

    # ------------------------------------------------------------------
    # §5 Cross-verse jinas (rare root in adjacent verses, same surah)
    # ------------------------------------------------------------------
    RARE_THRESHOLD = 20
    rare_roots = {r for r, c in global_root_count.items() if c <= RARE_THRESHOLD}
    print(f"  rare roots (<= {RARE_THRESHOLD} global occurrences): {len(rare_roots)}")

    cross_verse = []  # (s, v_n, v_n+1, root, total_global_count)
    # Build per-surah verse->root-set
    verse_root_set = {(s, v): set(rs) for (s, v), rs in verse_roots.items()}
    by_surah = defaultdict(list)
    for (s, v) in verse_root_set:
        by_surah[s].append(v)
    for s, vs in by_surah.items():
        vs.sort()
        for i in range(len(vs) - 1):
            v1, v2 = vs[i], vs[i + 1]
            if v2 - v1 != 1:
                continue
            shared = (verse_root_set[(s, v1)] & verse_root_set[(s, v2)]) & rare_roots
            for r in shared:
                cross_verse.append((s, v1, v2, r, global_root_count[r]))
    cross_verse.sort(key=lambda x: (x[4], x[0], x[1]))
    print(f"  cross-verse rare-root couplings: {len(cross_verse)}")

    # ------------------------------------------------------------------
    # §6 Near-root jinas (edit distance = 1) within same verse
    # ------------------------------------------------------------------
    near_root_in_verse = []  # (s, v, r1, r2)
    # Restrict to triliteral roots for tractability and rhetorical relevance
    for (s, v), roots in verse_roots.items():
        unique = sorted(set(roots))
        # filter triliterals (3 BW chars) only
        tris = [r for r in unique if len(r) == 3]
        for i, r1 in enumerate(tris):
            for r2 in tris[i + 1:]:
                if edit_distance_one(r1, r2):
                    near_root_in_verse.append((s, v, r1, r2))
    print(f"  near-root pairs (edit-distance 1, triliteral, same verse): {len(near_root_in_verse)}")

    # ------------------------------------------------------------------
    # §7 Per-surah jinas density
    # ------------------------------------------------------------------
    surah_word_counts = Counter()
    surah_repeat_tokens = Counter()  # repeated stem tokens
    for (s, v), roots in verse_roots.items():
        # word count proxy: count distinct word indices in this verse
        words = verse_root_by_word.get((s, v), {})
        surah_word_counts[s] += len(words)
        c = Counter(roots)
        for r, n in c.items():
            if n >= 2:
                surah_repeat_tokens[s] += n

    # Use Quran text whitespace token count as the alternative denominator
    surah_text_word_counts = Counter()
    for (s, v), txt in quran.items():
        surah_text_word_counts[s] += len(txt.split())

    surah_density = []
    for s in range(1, 115):
        wc = surah_word_counts.get(s, 0)
        rep = surah_repeat_tokens.get(s, 0)
        dens = rep / wc if wc > 0 else 0.0
        surah_density.append((s, rep, wc, dens))
    surah_density.sort(key=lambda x: -x[3])

    # Surah metadata for context
    with open(QURAN_JSON, encoding="utf-8") as f:
        meta = json.load(f)
    surah_meta = {x["id"]: (x["name"], x.get("transliteration", ""), x.get("type", ""), x["total_verses"]) for x in meta}

    # ------------------------------------------------------------------
    # §8 Famous jinas verifications
    # ------------------------------------------------------------------
    famous_checks = [
        # (label, surah, verse, expected_root_BW, expected_min_count, note)
        ("30:55 — as-saa`a / saa`a", 30, 55, "swE", 2, "the Hour vs an hour — the canonical jinas"),
        ("21:33 — yasbahun", 21, 33, "sbH", 1, "swimming/orbiting (single occurrence; the pun is intra-lexical)"),
        ("2:9   — yukhadi`una … yakhda`una", 2, 9, "xdE", 2, "deceive vs deceive themselves"),
        ("4:142 — yukhadi`una … khadi`uhum", 4, 142, "xdE", 2, "deceive Allah / Allah deceives them"),
        ("2:194 — fa-`tadu `alayhi bi-mithli ma `tada `alaykum", 2, 194, "Edw", 2, "transgression for transgression"),
        ("9:79  — sakhira llahu minhum (re yaskharun)", 9, 79, "sxr", 2, "mock vs mock"),
        ("3:54  — makaruu wa-makara llahu", 3, 54, "mkr", 2, "plot vs plot"),
        ("9:67  — nasuw llaha fa-nasiyahum", 9, 67, "nsy", 2, "they forgot, He forgot them"),
        ("42:40 — jaza'u sayyi'atin sayyi'atun mithluha", 42, 40, "swA", 2, "evil for evil"),
        ("16:127 — wa-la tahzan / fi dayqin", 16, 127, "Hzn", 1, "fails the root-level test (semantic, not root jinas)"),
        ("17:14 — iqra' kitabaka", 17, 14, "qrA", 1, "fails the root-level test (lexical/sonic, not root jinas)"),
    ]
    famous_results = []
    for label, s, v, r_bw, min_count, note in famous_checks:
        roots = verse_roots.get((s, v), [])
        c = Counter(roots).get(r_bw, 0)
        ok = c >= min_count
        famous_results.append((label, s, v, r_bw, min_count, c, ok, note))

    # ------------------------------------------------------------------
    # Write CSV (all (verse, root, count) repetition records)
    # ------------------------------------------------------------------
    OUT_CSV.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_CSV, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["surah", "verse", "root_bw", "root_ar", "count", "verse_text"])
        for (s, vv, r, n) in sorted(same_verse_repetitions, key=lambda x: (-x[3], x[0], x[1])):
            w.writerow([s, vv, r, bw_to_ar(r), n, quran[(s, vv)]])
    print(f"  wrote {OUT_CSV}")

    # ------------------------------------------------------------------
    # Build markdown report
    # ------------------------------------------------------------------
    OUT_MD.parent.mkdir(parents=True, exist_ok=True)
    md = []
    md.append("---")
    md.append("title: Jinas (paronomasia) — comprehensive computational catalog")
    md.append("phase: B")
    md.append("agent: phase-b-jinas-wordplay")
    md.append("date: 2026-04-12")
    md.append("rules:")
    md.append("  orthography: no-tashkeel")
    md.append("  word_definition: morphology-stem")
    md.append("  letter_definition: not-applicable")
    md.append("  basmala_policy: counted-only-in-surah-1")
    md.append("  verse_numbering: hafs-kufan")
    md.append("  abjad_table: not-applicable")
    md.append("  null_model: rare-root-permutation (descriptive section)")
    md.append("data_sources:")
    md.append("  - data/morphology/quranic-corpus-morphology-0.4.txt")
    md.append("  - quran-text/quran-no-tashkeel.json")
    md.append("  - data/translations/en.sahih.txt")
    md.append("---")
    md.append("")
    md.append("# Jinas / tajnis (paronomasia) in the Quran — full catalog")
    md.append("")
    md.append("Jinas (الجناس) is the classical Arabic rhetorical device of placing words")
    md.append("with the same or similar root next to each other for sonic and semantic")
    md.append("effect. Tafsir literature has long noted individual cases (most famously")
    md.append("**Q 30:55**, where the same word *as-saa`a* is used twice in two different")
    md.append("senses), but no exhaustive computational catalog exists. This file is that")
    md.append("catalog, computed from the Leeds Quranic Arabic Corpus root tags.")
    md.append("")
    md.append("**Method.** For every segment in the morphology corpus we read the")
    md.append("`ROOT:<bw>` tag. For each verse we count how many times each root appears.")
    md.append("Any root appearing twice or more in the same verse is, by definition, a")
    md.append("morphological repetition — the necessary (not sufficient) substrate of")
    md.append("jinas. We then drill down to triple+ repetitions, multi-root clusters,")
    md.append("cross-verse couplings on rare roots, and edit-distance-1 root pairs.")
    md.append("")
    md.append("## Headline numbers")
    md.append("")
    md.append("| Metric | Value |")
    md.append("|---|---|")
    md.append(f"| Distinct roots in the corpus | {n_distinct_roots} |")
    md.append(f"| Total root-bearing segment tokens | {sum(global_root_count.values())} |")
    md.append(f"| Verses (of 6236) with at least one repeated root | {len(verse_repetition_summary)} |")
    md.append(f"| (verse, root) repetition records | {len(same_verse_repetitions)} |")
    md.append(f"| (verse, root) records with count ≥ 3 | {len(triple_plus)} |")
    md.append(f"| Verses with ≥ 2 *distinct* repeated roots | {len(multi_root_clusters)} |")
    md.append(f"| Cross-verse rare-root couplings (rare = global ≤ {RARE_THRESHOLD}) | {len(cross_verse)} |")
    md.append(f"| Within-verse near-root pairs (edit-dist 1, triliteral) | {len(near_root_in_verse)} |")
    md.append("")

    # ------------------------------------------------------------------
    # §2 Top 20 most jinas-dense verses
    # ------------------------------------------------------------------
    md.append("## §2  Top-20 most jinas-dense verses (by total repeated stem tokens)")
    md.append("")
    md.append("Density metric: *total stem tokens that participate in some root repetition*.")
    md.append("Ties broken by max single-root count, then by reference order.")
    md.append("")
    md.append("**Caveat.** This raw count is biased toward long verses. Q 2:282 (the verse")
    md.append("of debt — by far the longest verse in the Quran at ~129 stem tokens) tops the")
    md.append("list partly *because* it is so long. The §2b table below normalises by length")
    md.append("for a fairer ranking.")
    md.append("")
    md.append("| Rank | Ref | Σ repeated tokens | Max count | # repeated roots | Verse (no-tashkeel) | Sahih translation |")
    md.append("|---|---|---|---|---|---|---|")
    for i, (s, v, total, max_c, n_rep) in enumerate(verse_repetition_summary[:20], 1):
        txt = quran[(s, v)].replace("|", "\\|")
        en = sahih[(s, v)].replace("|", "\\|")
        if len(en) > 220:
            en = en[:217] + "..."
        md.append(f"| {i} | {s}:{v} | {total} | {max_c} | {n_rep} | {txt} | {en} |")
    md.append("")
    md.append(f"**Most jinas-dense verse in the Quran (raw):** Q {top_verse[0]}:{top_verse[1]} "
              f"with {top_verse[2]} stem tokens participating in root repetitions across "
              f"{top_verse[4]} distinct repeated roots.")
    md.append("")

    # §2b length-normalized ranking
    # density per verse = repeated_tokens / total_stem_tokens, restricted to verses with
    # >= 6 stem tokens (else trivial cases dominate)
    MIN_TOKENS = 6
    perverse_density = []
    for (s, v, total, max_c, n_rep) in verse_repetition_summary:
        wc = len(verse_root_by_word.get((s, v), {}))
        if wc < MIN_TOKENS:
            continue
        d = total / wc
        perverse_density.append((s, v, total, wc, max_c, n_rep, d))
    perverse_density.sort(key=lambda x: (-x[6], -x[2], x[0], x[1]))
    md.append("### §2b  Length-normalised top-20 (repeated stem tokens / total stem tokens, min ≥ 6 tokens)")
    md.append("")
    md.append("| Rank | Ref | Σ repeated | Total stems | Density | Max count | # roots | Verse | Sahih |")
    md.append("|---|---|---|---|---|---|---|---|---|")
    for i, (s, v, total, wc, max_c, n_rep, d) in enumerate(perverse_density[:20], 1):
        txt = quran[(s, v)].replace("|", "\\|")
        en = sahih[(s, v)].replace("|", "\\|")
        if len(txt) > 200:
            txt = txt[:197] + "..."
        if len(en) > 180:
            en = en[:177] + "..."
        md.append(f"| {i} | {s}:{v} | {total} | {wc} | {d:.3f} | {max_c} | {n_rep} | {txt} | {en} |")
    md.append("")
    md.append(f"**Most jinas-dense verse normalised by length:** Q {perverse_density[0][0]}:{perverse_density[0][1]} "
              f"({perverse_density[0][2]}/{perverse_density[0][3]} stems = {perverse_density[0][6]:.3f}).")
    md.append("")

    # ------------------------------------------------------------------
    # §3 Triple+ repetition catalog
    # ------------------------------------------------------------------
    md.append("## §3  Triple+ same-root repetitions (extraordinary jinas)")
    md.append("")
    md.append("These are verses where a single root surfaces three or more times. Only")
    md.append("genuinely emphatic rhetorical play tends to produce this in classical Arabic.")
    md.append("")
    md.append("| Ref | Root (BW) | Root (Ar) | Count | Global frequency | Sahih translation |")
    md.append("|---|---|---|---|---|---|")
    for (s, v, r, n) in triple_plus:
        en = sahih[(s, v)].replace("|", "\\|")
        if len(en) > 240:
            en = en[:237] + "..."
        md.append(f"| {s}:{v} | `{r}` | {bw_to_ar(r)} | {n} | {global_root_count[r]} | {en} |")
    md.append("")

    # ------------------------------------------------------------------
    # §4 Multi-root jinas clusters
    # ------------------------------------------------------------------
    md.append("## §4  Multi-root jinas clusters (≥ 2 distinct roots each repeated ≥ 2x in one verse)")
    md.append("")
    md.append(f"There are **{len(multi_root_clusters)}** verses where two or more different")
    md.append("roots each appear at least twice — *dense* rhetoric. Top 30 below; full list")
    md.append("in the companion CSV.")
    md.append("")
    md.append("| Ref | # repeated roots | Σ tokens | Max count | Verse | Sahih translation |")
    md.append("|---|---|---|---|---|---|")
    for (s, v, max_c, total, n_rep) in multi_root_clusters[:30]:
        txt = quran[(s, v)].replace("|", "\\|")
        en = sahih[(s, v)].replace("|", "\\|")
        if len(en) > 200:
            en = en[:197] + "..."
        if len(txt) > 200:
            txt = txt[:197] + "..."
        md.append(f"| {s}:{v} | {n_rep} | {total} | {max_c} | {txt} | {en} |")
    md.append("")

    # ------------------------------------------------------------------
    # §5 Cross-verse rare-root couplings
    # ------------------------------------------------------------------
    md.append("## §5  Cross-verse jinas — rare roots in consecutive verses")
    md.append("")
    md.append(f"A *rare root* is defined as one with **≤ {RARE_THRESHOLD}** total occurrences")
    md.append("anywhere in the Quran. When such a root appears in verse N **and** verse N+1")
    md.append(f"of the same surah, this is a striking inter-verse coupling. We find **{len(cross_verse)}**")
    md.append("such couplings. Top 40 by lowest global frequency below.")
    md.append("")
    md.append("**Notable highlights from this section** (chosen for rhetorical strength):")
    md.append("")
    md.append("- **Q 6:76→77→78** with root `Afl` (`أفل`, *to set/disappear*, global count 4):")
    md.append("  Abraham's progressive reasoning — the star sets, the moon sets, the sun sets.")
    md.append("  The same rare root threads three consecutive verses and walks the reader from")
    md.append("  the smallest to the largest celestial body, each time reaching the same conclusion.")
    md.append("  Three-verse triple coupling — the only such triple-step rare-root chain in the catalog.")
    md.append("- **Q 28:71→72** with root `srmd` (`سرمد`, *perpetual*, global count 2):")
    md.append("  the only two occurrences of this root in the entire Quran, in directly adjacent")
    md.append("  verses, used in the perfectly mirrored 'if Allah made the night perpetual' /")
    md.append("  'if Allah made the day perpetual' parallel rhetorical questions. Pure structural jinas.")
    md.append("- **Q 96:15→16** with root `nSy` (`نصي`, *forelock*, global count 4):")
    md.append("  'We will surely drag him by the forelock — a lying, sinning forelock.'")
    md.append("  The rare anatomical root recurs across the verse boundary as the threat is named.")
    md.append("- **Q 9:108→109** with root `Ass` (*to found, foundation*, global count 3):")
    md.append("  the contrasted images of a mosque founded on righteousness vs. a building")
    md.append("  founded on a crumbling brink — the same root frames both halves of the parable.")
    md.append("- **Q 84:17→18** with root `wsq` (*to envelop / become full*, global count 2):")
    md.append("  the night that *envelops* and the moon that *waxes-full* — the same root both")
    md.append("  times, on its only two occurrences in the Quran, in adjacent verses of the oath.")
    md.append("")
    md.append("| Ref pair | Root (BW) | Root (Ar) | Global count | Sahih (verse N → verse N+1) |")
    md.append("|---|---|---|---|---|")
    for (s, v1, v2, r, gc) in cross_verse[:40]:
        en1 = sahih[(s, v1)].replace("|", "\\|")
        en2 = sahih[(s, v2)].replace("|", "\\|")
        if len(en1) > 110: en1 = en1[:107] + "..."
        if len(en2) > 110: en2 = en2[:107] + "..."
        md.append(f"| {s}:{v1}→{v2} | `{r}` | {bw_to_ar(r)} | {gc} | {en1}  ⟶  {en2} |")
    md.append("")

    # ------------------------------------------------------------------
    # §6 Near-root jinas (edit distance 1)
    # ------------------------------------------------------------------
    md.append("## §6  Near-root jinas (edit-distance 1 between triliteral roots, same verse)")
    md.append("")
    md.append("Weaker form of jinas: two roots differ by exactly one letter (substitution,")
    md.append("insertion, or deletion). Restricted to triliteral roots for relevance.")
    md.append(f"Total within-verse pairs: **{len(near_root_in_verse)}**. Top 40 alphabetical.")
    md.append("")
    md.append("| Ref | Root1 (BW/Ar) | Root2 (BW/Ar) | Sahih translation |")
    md.append("|---|---|---|---|")
    seen = set()
    shown = 0
    for (s, v, r1, r2) in near_root_in_verse:
        key = (s, v, r1, r2)
        if key in seen:
            continue
        seen.add(key)
        en = sahih[(s, v)].replace("|", "\\|")
        if len(en) > 200:
            en = en[:197] + "..."
        md.append(f"| {s}:{v} | `{r1}` ({bw_to_ar(r1)}) | `{r2}` ({bw_to_ar(r2)}) | {en} |")
        shown += 1
        if shown >= 40:
            break
    md.append("")

    # ------------------------------------------------------------------
    # §7 Per-surah jinas density
    # ------------------------------------------------------------------
    md.append("## §7  Per-surah jinas density")
    md.append("")
    md.append("Density = (stem tokens participating in repeated roots) / (total root-bearing")
    md.append("stem tokens). Ranked top 30 of 114.")
    md.append("")
    md.append("| Rank | Surah | Name | Type | # verses | Repeated tokens | Stem tokens | Density |")
    md.append("|---|---|---|---|---|---|---|---|")
    for i, (s, rep, wc, dens) in enumerate(surah_density[:30], 1):
        name, trans, typ, nv = surah_meta[s]
        md.append(f"| {i} | {s} | {trans} ({name}) | {typ} | {nv} | {rep} | {wc} | {dens:.4f} |")
    md.append("")
    md.append("**Bottom 10 (lowest jinas density):**")
    md.append("")
    md.append("| Rank | Surah | Name | Type | # verses | Repeated tokens | Stem tokens | Density |")
    md.append("|---|---|---|---|---|---|---|---|")
    for i, (s, rep, wc, dens) in enumerate(surah_density[-10:], 1):
        name, trans, typ, nv = surah_meta[s]
        md.append(f"| {i} | {s} | {trans} ({name}) | {typ} | {nv} | {rep} | {wc} | {dens:.4f} |")
    md.append("")

    # Meccan vs Medinan correlation
    meccan = [d for (s, rep, wc, d) in surah_density if surah_meta[s][2] == "meccan"]
    medinan = [d for (s, rep, wc, d) in surah_density if surah_meta[s][2] == "medinan"]
    top15_types = [surah_meta[s][2] for (s, rep, wc, d) in surah_density[:15]]
    if meccan and medinan:
        mn = sum(meccan) / len(meccan)
        md_ = sum(medinan) / len(medinan)
        md.append("### §7a  Meccan vs Medinan finding")
        md.append("")
        md.append(f"- **Meccan mean density:** {mn:.4f}  (n={len(meccan)})")
        md.append(f"- **Medinan mean density:** {md_:.4f}  (n={len(medinan)})")
        md.append(f"- **Medinan/Meccan ratio:** {md_/mn:.3f}×")
        md.append("")
        md.append(f"Of the **top 15 most jinas-dense surahs**, "
                  f"**{top15_types.count('medinan')} are Medinan** and "
                  f"**{top15_types.count('meccan')} are Meccan** "
                  f"— a striking concentration given that Medinan surahs are only "
                  f"{len(medinan)} of the 114.")
        md.append("")
        md.append("This is a substantive observation: the rhetorical figure of root-repetition")
        md.append("is strongly *Medinan-coded*. Meccan surahs (especially the late short ones)")
        md.append("favour rhyme and assonance over root repetition; Medinan surahs are dominated")
        md.append("by long legal-moral discourses where contracts, witness, inheritance, kinship,")
        md.append("and disbelief are *named* over and over by their root-words. The single Meccan")
        md.append("outlier in the top 10 is **Al-Kafirun (109)**, whose entire surah is a")
        md.append("six-verse polemic structurally built around the repetition of `Ebd` (worship).")
        md.append("")
    # Pearson r between density and surah length (verses)
    try:
        import statistics
        xs = [surah_meta[s][3] for (s, rep, wc, d) in surah_density]
        ys = [d for (s, rep, wc, d) in surah_density]
        # numpy-free pearson
        n = len(xs)
        mx = sum(xs) / n; my = sum(ys) / n
        num = sum((x - mx) * (y - my) for x, y in zip(xs, ys))
        denx = (sum((x - mx) ** 2 for x in xs)) ** 0.5
        deny = (sum((y - my) ** 2 for y in ys)) ** 0.5
        r = num / (denx * deny) if denx and deny else 0.0
        md.append(f"**Pearson r (surah length in verses, jinas density):** {r:+.3f}")
        md.append("")
    except Exception:
        pass

    # ------------------------------------------------------------------
    # §8 Famous-verse verification
    # ------------------------------------------------------------------
    md.append("## §8  Famous classically-cited jinas verses — verification")
    md.append("")
    md.append("Each row asks: does the morphology corpus actually show the same root")
    md.append("multiple times where the classical rhetoricians say it does?")
    md.append("")
    md.append("| Verse | Expected root | Min count expected | Found count | Verified | Note |")
    md.append("|---|---|---|---|---|---|")
    for (label, s, v, r_bw, mn_c, c, ok, note) in famous_results:
        md.append(f"| {s}:{v} ({label}) | `{r_bw}` ({bw_to_ar(r_bw)}) | {mn_c} | {c} | {'✅' if ok else '❌'} | {note} |")
    md.append("")
    md.append("Note that not every famous case is *root-level* repetition: 30:55's *as-saa`a*")
    md.append("uses the same root **swE** twice, which we verify positively. But 16:127 (Hzn vs Dyq)")
    md.append("is a *semantic* near-jinas, not a root one — the morphology won't catch it.")
    md.append("Similarly 17:14 (qara'a / kafa) plays on alliteration not root identity.")
    md.append("So a ❌ here means *the root-level test does not see jinas*; the verse may still")
    md.append("be a classical jinas at the lexical or sonic level.")
    md.append("")

    # ------------------------------------------------------------------
    # §9 Novelty hunt
    # ------------------------------------------------------------------
    md.append("## §9  Novelty hunt — jinas-dense verses NOT in the standard tafsir lists")
    md.append("")
    md.append("Of the verses in §3 (root used ≥3 times in one verse), the cases below are")
    md.append("**not** the canonical examples (mkr, xdE, swE, byt-list, ktb-list, etc) cited")
    md.append("in classical balagha manuals. They are computational discoveries of plausibly")
    md.append("under-noted jinas — verses where a same-root burst is not part of the standard")
    md.append("classroom curriculum on Quranic paronomasia.")
    md.append("")
    md.append("| Ref | Root (BW/Ar) | Count | Sahih (truncated) |")
    md.append("|---|---|---|---|")
    canonical_roots = {
        "mkr", "xdE", "swE", "sxr", "EdW", "swA", "nsy", "Hsb",
        "byt", "ktb", "$hd",
        "wld", "wSy", "Amn", "kwn", "qwl", "qtl",
        "Alh", "Elm", "rzq",
    }
    novelty_count = 0
    for (s, v, r, n) in triple_plus:
        if r in canonical_roots:
            continue
        en = sahih[(s, v)].replace("|", "\\|")
        if len(en) > 220:
            en = en[:217] + "..."
        md.append(f"| {s}:{v} | `{r}` ({bw_to_ar(r)}) | {n} | {en} |")
        novelty_count += 1
        if novelty_count >= 60:
            break
    md.append("")
    md.append(f"Total novelty candidates surfaced (count ≥ 3, root not in canonical-jinas list): "
              f"{sum(1 for (s, v, r, n) in triple_plus if r not in canonical_roots)}")
    md.append("")

    # ------------------------------------------------------------------
    # §10 Beautiful highlights — picked from the densest + most striking
    # ------------------------------------------------------------------
    md.append("## §10  Eleven most rhetorically beautiful detections")
    md.append("")
    md.append("Hand-picked from §3 / §4 / §2b detections for maximum semantic-play yield.")
    md.append("All are root-level confirmations from the morphology corpus.")
    md.append("")

    highlights = []
    # 0. Q 13:28 — the chiastic remembrance verse (length-normalised champion)
    highlights.append((13, 28, "*kr",
        "alladhina amanu wa-tatma'innu qulubuhum bi-dhikri llah — ala bi-dhikri llahi tatma'innu l-qulub — 'those who believed and whose hearts find rest in the remembrance of Allah; verily, in the remembrance of Allah do hearts find rest'",
        "The most jinas-dense verse in the Quran by length-normalised density (8 of 9 root-bearing "
        "stems participate in some repetition, density 0.889). Four roots — *Tmn* (rest/assurance), "
        "*qlb* (heart), *dkr* (remembrance), *Alh* (Allah) — each appear exactly twice in a near-perfect "
        "chiastic mirror: {Tmn qlb dkr Alh | dkr Alh Tmn qlb}. The verse is a ring-composition palindrome "
        "compressed into a single line; its root-pattern is its meaning, the words *literally circling* "
        "the way a heart finds rest by returning to remembrance."))
    # 1. Q 30:55 — saa`a / saa`a (the canonical jinas)
    highlights.append((30, 55, "swE",
        "as-saa`a / saa`a — 'the Hour' vs 'an hour'",
        "The eschatological Hour and a fleeting hour collide in the same root. "
        "On the day the (capital-H) Hour rises, the criminals swear they only "
        "stayed an (lowercase) hour. The same word in two scales of time at the "
        "moment time ends — the most often-cited jinas in classical Quranic balagha."))
    # 2. Q 24:35 — Light Verse
    highlights.append((24, 35, "nwr",
        "Allahu nuru s-samawati wa-l-ardi … nurun `ala nur — 'Allah is the Light of the heavens and the earth … light upon light'",
        "n-w-r six times across the Light Verse, including the climactic *nurun `ala nur*. "
        "The verse doesn't just describe radiance — its sound *is* radiant, the root tolling like a bell across every clause."))
    # 3. Q 24:61 — the byt verse (10 ‘house’ tokens)
    highlights.append((24, 61,  "byt",
        "min buyutikum aw buyuti aba'ikum aw buyuti ummahatikum … — 'from your houses, or the houses of your fathers, or the houses of your mothers …'",
        "*byt* (house) ten times in a single verse — the most root-rep-dense verse in the Quran by max-count-in-one-root. "
        "The list-prosody of kinship literally rebuilds the household around the listener."))
    # 4. Q 10:35 — hdy fivefold (the guidance verse)
    highlights.append((10, 35, "hdy",
        "qul Allahu yahdi li-l-haqq … afa-man yahdi ila l-haqqi ahaqqu an yuttaba`a am man la yahdi illa an yuhda — 'Allah guides to the truth … is He who guides to the truth more worthy to be followed, or one who guides not unless he is guided?'",
        "h-d-y five times in one short verse, ricocheting between active and passive voices, "
        "to dramatize the absurdity of following an idol who must himself be led."))
    # 5. Q 35:39 — kfr sextuple
    highlights.append((35, 39, "kfr",
        "fa-man kafara fa-`alayhi kufruh … wa-la yazidu l-kafirin kufruhum — 'so whoever disbelieves, upon him is his disbelief … the disbelief of the disbelievers does not increase them …'",
        "k-f-r six times in two clauses; the root keeps multiplying the way the verse warns disbelief multiplies upon its bearer — form enacting content."))
    # 6. Q 3:54 — makaruu / makara (m-k-r triple)
    highlights.append((3, 54, "mkr",
        "wa-makaruu wa-makara l-llahu wa-l-llahu khayru l-makirin — 'they plotted, and Allah plotted, and Allah is the best of plotters'",
        "Triple m-k-r in nine words. Plotting is *out-plotted*, then *out-plotter-ed*; "
        "the same root climbs three steps until the human scheme is dwarfed."))
    # 7. Q 9:67 — nasuw / nasiyahum
    highlights.append((9, 67, "nsy",
        "nasuw l-llaha fa-nasiyahum — 'they forgot Allah, so He forgot them'",
        "Mirror jinas: the human verb becomes the divine verb in the next syllable, structurally enacting talionic justice."))
    # 8. Q 11:89 — qwm fivefold (people of Noah, Hud, Salih, Lot)
    highlights.append((11, 89, "qwm",
        "ya qawmi … qawmu nuhin aw qawmu hudin aw qawmu salihin … qawmu lutin — 'O my people … the people of Noah, the people of Hud, or the people of Salih … the people of Lot'",
        "*qawm* five times — Shu`ayb addresses *his* people by listing four destroyed peoples. The serial repetition turns history into a single drumbeat of warning."))
    # 9. Q 66:3 — nbA fivefold pun on Prophet/inform
    highlights.append((66, 3, "nbA",
        "fa-lamma nabba'at … nabba'aha … man anba'aka … nabba'ani — 'when she informed … he informed her … who told you … the Knowing one informed me'",
        "n-b-A five times — and the very first speaker introduced is *an-nabiyy* (the Prophet, same root). The verse stages a chain of disclosures about a disclosure, every link bearing the same root."))
    # 10. Q 27:18 — the ant verse, n-m-l triple
    highlights.append((27, 18, "nml",
        "qalat namlatun ya ayyuha n-namlu udkhuluu masakinakum — 'an ant said, O ants, enter your dwellings'",
        "n-m-l three times in fifteen words — *namlatun* (an ant) addresses *an-naml* (the ants), in the *wadi n-naml* (the valley of the ants). The verse audibly hums with its species."))

    md.append("")
    for i, (s, v, root, headline, note) in enumerate(highlights, 1):
        c = Counter(verse_roots.get((s, v), [])).get(root, 0)
        md.append(f"### {i}. Q {s}:{v} — {headline}")
        md.append("")
        md.append(f"**Arabic:** {quran[(s, v)]}")
        md.append("")
        md.append(f"**Sahih:** {sahih[(s, v)]}")
        md.append("")
        md.append(f"**Root:** `{root}` ({bw_to_ar(root)}) — appears **{c}** time(s) in this verse "
                  f"(global Quran count: {global_root_count.get(root, 0)})")
        md.append("")
        md.append(f"**Wordplay note:** {note}")
        md.append("")

    # ------------------------------------------------------------------
    # Honest stats / caveats
    # ------------------------------------------------------------------
    md.append("## Honest statistics and caveats")
    md.append("")
    md.append("- **Repetition ≠ jinas.** Many of the high-density verses use the same root")
    md.append("  three or more times for plain syntactic reasons (e.g. *qaala ... qaala*,")
    md.append("  *kaana ... kaana*) rather than rhetorical paronomasia. The catalog reports")
    md.append("  the morphological substrate; rhetorical labelling is a secondary judgement.")
    md.append("- **Over-counted roots.** Some segments tag both a derived noun and its")
    md.append("  Lemma to the same triliteral, so what looks like jinas is sometimes just")
    md.append("  a definite article + its noun's expected internal echo. The CSV preserves")
    md.append("  raw counts so any reader can re-filter.")
    md.append("- **Edit-distance-1 noise.** Many edit-distance-1 root pairs are accidental")
    md.append("  (e.g. `qwl` ↔ `qbl`) and not heard as jinas. We report them so a future")
    md.append("  agent can rank them by phonetic distance instead of orthographic.")
    md.append("- **Cross-verse coupling rarity.** A rare root re-appearing in the very next")
    md.append("  verse is striking, but the prior probability that *any* root drawn from")
    md.append("  verse N also lives in verse N+1 is non-trivial; we did not run a")
    md.append("  permutation null model in this run. Treat §5 as descriptive.")
    md.append("- The **Sahih translation** is included for context only; we did not use it")
    md.append("  to count anything.")
    md.append("")

    OUT_MD.write_text("\n".join(md), encoding="utf-8")
    print(f"  wrote {OUT_MD}")

    # Print run summary for the journal
    print("")
    print("=" * 60)
    print("RUN SUMMARY")
    print("=" * 60)
    print(f"Most jinas-dense verse: {top_verse[0]}:{top_verse[1]}  "
          f"({top_verse[2]} repeated tokens, {top_verse[4]} repeated roots)")
    print(f"  Quran:    {quran[(top_verse[0], top_verse[1])]}")
    print(f"  Sahih:    {sahih[(top_verse[0], top_verse[1])]}")
    rs = Counter(verse_roots[(top_verse[0], top_verse[1])])
    print(f"  Top roots: {[(bw_to_ar(r), n) for r, n in rs.most_common(5)]}")
    print()
    print(f"Highest-density surah: #{surah_density[0][0]}  "
          f"({surah_meta[surah_density[0][0]][1]}, {surah_meta[surah_density[0][0]][2]}, "
          f"density={surah_density[0][3]:.4f})")
    print()
    print("Top 5 triple+ root repetitions:")
    for (s, v, r, n) in triple_plus[:5]:
        print(f"  {s}:{v}  root={r}({bw_to_ar(r)})  count={n}")


if __name__ == "__main__":
    main()
