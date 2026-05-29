#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
H-NEW-2080 — Exhaustive verse-final rhyme-scheme (fāṣila) corpus scan + monorhyme inventory.

CANDIDATE-PATTERN GENERATOR for verse-final rhyme.

Rules-tuple (LOCKED, see prereg):
  - text: quran-text/quran-min-tashkeel.json (min-tashkeel, Hafs-Kufan, 6236 verses)
  - unit: verse-final letter (rāwī) = last Arabic letter of last whitespace token,
          diacritics stripped, normalized per saj_rhyme.py NORM map for cross-consistency.
  - basmala counted only as 1:1.

Outputs:
  - findings/phase-b-hypotheses/csv/h-new-2080.json

Pre-reg SHA256 verified at runtime (fail-fast).
"""
import json, os, sys, hashlib, math, unicodedata
from collections import Counter

ROOT = "/Users/grey/Downloads/quran"
PREREG = os.path.join(ROOT, "findings/phase-b-hypotheses/prereg-h-new-2080-rhyme-scan.md")
EXPECTED_SHA = "1bf788f0fb40c34c70fbca2ce12fc5d2876fd8ceb835b01aaee2361111f9520c"
MIN_JSON = os.path.join(ROOT, "quran-text/quran-min-tashkeel.json")
LETTERFREQ = os.path.join(ROOT, "data/baseline-corpora/letter-freqs.csv")
OUT_JSON = os.path.join(ROOT, "findings/phase-b-hypotheses/csv/h-new-2080.json")
SEED = 20260509

# --- 0. Pre-reg SHA verification (fail-fast) --------------------------------
with open(PREREG, "rb") as f:
    actual_sha = hashlib.sha256(f.read()).hexdigest()
if actual_sha != EXPECTED_SHA:
    sys.exit(f"PRE-REG SHA MISMATCH\n expected {EXPECTED_SHA}\n actual   {actual_sha}\nABORTING (pre-commit integrity).")
print(f"[ok] pre-reg SHA verified: {actual_sha}")

# --- 1. Letter normalization (identical to analysis/notebooks/saj_rhyme.py) --
DIACRITIC_RANGES = [
    (0x064B, 0x065F), (0x0670, 0x0670), (0x06D6, 0x06ED),
    (0x0610, 0x061A), (0x0640, 0x0640), (0x0656, 0x0657),
]
def is_diacritic(cp):
    return any(lo <= cp <= hi for lo, hi in DIACRITIC_RANGES)

NORM = {
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا', 'ٱ': 'ا', 'ٲ': 'ا', 'ٳ': 'ا',
    'ؤ': 'و', 'ئ': 'ي', 'ى': 'ا', 'ة': 'ه', 'ٮ': 'ب',
}
def is_arabic_letter(c):
    cp = ord(c)
    return (0x0621 <= cp <= 0x064A) or (0x0671 <= cp <= 0x06D3)

def strip_to_consonants(word):
    out = []
    for c in word:
        cp = ord(c)
        if is_diacritic(cp):
            continue
        if not is_arabic_letter(c):
            continue
        out.append(NORM.get(c, c))
    return "".join(out)

def verse_final_skeleton(words):
    """Return the consonant-skeleton of the last genuine WORD of the verse.
    17 verses end in a standalone recitation glyph (sajda mark ۩ U+06E9 or
    small-high-seen ۜ U+06DC) as a separate whitespace token; these carry no
    rāwī, so we skip trailing tokens that strip to an empty skeleton.
    (Pre-registered trailing-glyph handling.)"""
    for w in reversed(words):
        cons = strip_to_consonants(w)
        if cons:
            return cons
    return ""

# --- 2. Load corpus ----------------------------------------------------------
with open(MIN_JSON, encoding="utf-8") as f:
    surahs = json.load(f)

verses = []            # verse-final records
all_word_finals = []   # B2 control: final letter of EVERY word (incl. non-verse-final)
for s in surahs:
    sid = s["id"]
    for v in s["verses"]:
        words = v["text"].split()
        if not words:
            continue
        # B2: every word's final consonant letter
        for w in words:
            cons_w = strip_to_consonants(w)
            if cons_w:
                all_word_finals.append(cons_w[-1])
        cons = verse_final_skeleton(words)
        verses.append({
            "surah": sid,
            "verse": v["id"],
            "type": s["type"],
            "rawi": cons[-1:] if cons else "",
            "fasila_2": cons[-2:] if len(cons) >= 2 else cons,
        })

assert len(verses) == 6236, f"verse count {len(verses)} != 6236"
N = len(verses)
print(f"[ok] loaded {N} verses; {len(all_word_finals)} total word-final letters")

# --- 3. Corpus rhyme-final-letter histogram (rāwī-level) ---------------------
rawi_counts = Counter(v["rawi"] for v in verses)
histogram = []
for letter, cnt in rawi_counts.most_common():
    histogram.append({
        "letter": letter,
        "codepoint": "U+%04X" % ord(letter) if letter else "",
        "count": cnt,
        "pct": round(100.0 * cnt / N, 4),
    })

# --- 4. H1a: nūn/mīm rāwī dominance ------------------------------------------
NUN, MIM = 'ن', 'م'
count_nun = rawi_counts.get(NUN, 0)
count_mim = rawi_counts.get(MIM, 0)
share_nun_mim = (count_nun + count_mim) / N
H1a_pass = share_nun_mim > 0.50

# --- 4b. H1b: fasila-2 nasal-class adjudication of the "85%" claim -----------
fasila2_counts = Counter(v["fasila_2"] for v in verses)
# nasal-ending 2-skeletons: long-vowel + nasal consonant (the -ūn/-īn/-īm/-ān/-ām class)
NASAL_F2 = ['ون', 'ين', 'يم', 'ان', 'ام', 'وم', 'ىن']  # ى normalized to ا already, kept for completeness
# build from observed: any fasila_2 whose LAST letter is ن or م
nasal_f2_share = sum(c for f2, c in fasila2_counts.items() if f2 and f2[-1] in (NUN, MIM)) / N
top_fasila2 = [{"fasila_2": f2, "count": c, "pct": round(100.0*c/N, 4)}
               for f2, c in fasila2_counts.most_common(15)]

# --- 5. H2: per-surah scheme classification + perfect monorhymes -------------
by_surah = {}
for v in verses:
    by_surah.setdefault(v["surah"], []).append(v)

surah_meta = {s["id"]: {"name": s["name"], "transliteration": s["transliteration"],
                         "type": s["type"]} for s in surahs}

surah_records = []
n_perfect = 0
for sid in sorted(by_surah):
    vs = by_surah[sid]
    n = len(vs)
    rc = Counter(v["rawi"] for v in vs)
    dom_letter, dom_n = rc.most_common(1)[0]
    U1 = dom_n / n
    # second letter share
    second = rc.most_common(2)
    second_letter, second_n = (second[1] if len(second) > 1 else ("", 0))
    U1_second = second_n / n
    # classification
    if U1 == 1.0:
        scheme = "MONORHYME-PERFECT"
        n_perfect += 1
    elif U1 >= 0.80:
        scheme = "MONORHYME-DOMINANT"
    elif U1 >= 0.50 and U1_second >= 0.30:
        scheme = "ALTERNATING"
    elif U1 >= 0.50:
        scheme = "MONORHYME-LOOSE"
    elif U1 < 0.50 and U1_second >= 0.30:
        scheme = "ALTERNATING"
    else:
        scheme = "FREE"
    surah_records.append({
        "surah": sid,
        "name": surah_meta[sid]["transliteration"],
        "type": surah_meta[sid]["type"],
        "n_verses": n,
        "rawi": dom_letter,
        "rawi_codepoint": "U+%04X" % ord(dom_letter) if dom_letter else "",
        "U1": round(U1, 4),
        "second_letter": second_letter,
        "U1_second": round(U1_second, 4),
        "scheme": scheme,
    })

H2_pass = n_perfect >= 10

perfect_list = sorted(
    [r for r in surah_records if r["scheme"] == "MONORHYME-PERFECT"],
    key=lambda r: -r["n_verses"]
)

# scheme tally
scheme_tally = Counter(r["scheme"] for r in surah_records)

# --- 6. Baselines ------------------------------------------------------------
# B1: corpus-letter-frequency expectation for nūn+mīm at a random word-final
with open(LETTERFREQ, encoding="utf-8") as f:
    header = f.readline().rstrip("\n").split(",")
    qline = None
    for line in f:
        parts = line.rstrip("\n").split(",")
        if parts[0] == "quran-no-tashkeel":
            qline = parts
            break
freq = {header[i]: float(qline[i]) for i in range(1, len(header))}
exp_nun = freq.get(NUN, 0.0)
exp_mim = freq.get(MIM, 0.0)
p0 = exp_nun + exp_mim   # expected nūn+mīm share under random-letter draw
# one-proportion z-test: observed share_nun_mim vs p0
se = math.sqrt(p0 * (1 - p0) / N)
z_B1 = (share_nun_mim - p0) / se if se > 0 else float("inf")

# B2: generic word-final nūn+mīm share (all words, control)
wf_counts = Counter(all_word_finals)
share_wf_nun_mim = (wf_counts.get(NUN, 0) + wf_counts.get(MIM, 0)) / len(all_word_finals)
# z-test: verse-final vs generic-word-final share
se2 = math.sqrt(share_wf_nun_mim * (1 - share_wf_nun_mim) / N) if 0 < share_wf_nun_mim < 1 else 0.0
z_B2 = (share_nun_mim - share_wf_nun_mim) / se2 if se2 > 0 else float("inf")

ALPHA_BON = 0.025  # k=2
# z critical for one-sided 0.025 ~ 1.96
Z_CRIT = 1.959964

# --- 7. Verdict --------------------------------------------------------------
if H1a_pass and H2_pass and z_B1 > Z_CRIT:
    verdict = "PASS-BOTH"
elif H1a_pass != H2_pass:
    verdict = "PARTIAL"
elif (not H1a_pass) and (not H2_pass):
    verdict = "NULL"
else:
    verdict = "PARTIAL"  # both threshold-pass but baseline z fails

# --- 8. Assemble & write -----------------------------------------------------
result = {
    "id": "H-NEW-2080",
    "prereg_sha": EXPECTED_SHA,
    "seed": SEED,
    "rules_tuple": "min-tashkeel, verse-final letter (rāwī), normalized per saj NORM map, Hafs-Kufan, basmala-only-1:1",
    "n_verses": N,
    "n_distinct_rawi": len(rawi_counts),
    "histogram": histogram,
    "H1a_nun_mim_rawi": {
        "count_nun": count_nun, "count_mim": count_mim,
        "share_nun_mim": round(share_nun_mim, 6),
        "threshold": 0.50, "pass": H1a_pass,
        "direction_locked": "nun+mim > 50%",
    },
    "H1b_fasila2_nasal": {
        "nasal_ending_f2_share": round(nasal_f2_share, 6),
        "top_fasila2": top_fasila2,
        "note": "share of verses whose 2-letter pausal skeleton ends in nūn or mīm (the -ūn/-īn/-īm/-ān class)",
    },
    "H2_monorhyme": {
        "n_perfect": n_perfect, "threshold": 10, "pass": H2_pass,
        "direction_locked": "n_perfect >= 10",
        "saj_run1_cross_check": 18,
        "perfect_monorhyme_surahs": perfect_list,
    },
    "scheme_tally": dict(scheme_tally),
    "per_surah": surah_records,
    "baseline_B1": {
        "model": "random word-final letter ~ corpus letter-frequency (quran-no-tashkeel)",
        "exp_nun": exp_nun, "exp_mim": exp_mim, "p0_expected_share": round(p0, 6),
        "observed_share": round(share_nun_mim, 6),
        "z": round(z_B1, 4), "z_crit_0.025": Z_CRIT,
        "pass_vs_baseline": z_B1 > Z_CRIT,
        "lift_over_random": round(share_nun_mim / p0, 3) if p0 > 0 else None,
    },
    "baseline_B2": {
        "model": "generic word-final letter (all words, control)",
        "generic_wordfinal_nun_mim_share": round(share_wf_nun_mim, 6),
        "verse_final_nun_mim_share": round(share_nun_mim, 6),
        "z_verse_vs_generic": round(z_B2, 4),
        "verse_final_enriched": share_nun_mim > share_wf_nun_mim,
    },
    "bonferroni_k": 2, "alpha_bon": ALPHA_BON,
    "verdict": verdict,
    "connection_h_new_700": "This rāwī histogram is the corpus-level marginal of the per-surah rhyme-letter distributions that drive the H-NEW-700 dispersion-tail (R²=0.789). Long ṭiwāl surahs contribute the ن mass; mufaṣṣal-qiṣār contribute the distinct-letter tail.",
}

os.makedirs(os.path.dirname(OUT_JSON), exist_ok=True)
with open(OUT_JSON, "w", encoding="utf-8") as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

# --- 9. Console report -------------------------------------------------------
print("\n=== H-NEW-2080 RESULTS ===")
print(f"distinct rāwī letters: {len(rawi_counts)}")
print("top-8 rāwī histogram:")
for h in histogram[:8]:
    print(f"  {h['letter']} ({h['codepoint']}): {h['count']:5d}  {h['pct']:6.2f}%")
print(f"\nH1a nūn+mīm rāwī share: {share_nun_mim:.4f}  -> pass={H1a_pass}")
print(f"H1b fasila-2 nasal-ending share: {nasal_f2_share:.4f}")
print(f"H2 perfect monorhymes: {n_perfect}  -> pass={H2_pass} (saj-run1 ref=18)")
print(f"scheme tally: {dict(scheme_tally)}")
print(f"\nB1 expected-random nūn+mīm share p0={p0:.4f}; observed={share_nun_mim:.4f}; z={z_B1:.2f}; lift={share_nun_mim/p0:.2f}x")
print(f"B2 generic word-final nūn+mīm share={share_wf_nun_mim:.4f}; verse-final={share_nun_mim:.4f}; z={z_B2:.2f}")
print(f"\nVERDICT: {verdict}")
print(f"top-5 longest perfect monorhymes:")
for r in perfect_list[:5]:
    print(f"  Q{r['surah']:3d} {r['name']:14s} N={r['n_verses']:3d} rāwī={r['rawi']}")
print(f"\nwrote {OUT_JSON}")
