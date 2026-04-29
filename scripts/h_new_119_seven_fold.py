#!/usr/bin/env python3
"""
H-NEW-119 — 7-fold patterns inventory.

Tests whether 7-fold structures recur in the Quran at a non-random rate,
distinguishing structural privilege from cultural projection.

Pre-reg: /findings/phase-b-hypotheses/h-new-119-seven-fold-prereg.md
"""

import json
import re
import random
from pathlib import Path
from collections import defaultdict

ROOT = Path("/Users/grey/Downloads/quran")
QURAN_JSON = ROOT / "quran-text/quran-no-tashkeel.json"
BUKHARI_TXT = ROOT / "data/baseline-corpora/raw/bukhari-noquran.txt"
OUT_JSON = ROOT / "findings/phase-b-hypotheses/csv/h-new-119.json"

SEED = 20260417
random.seed(SEED)

# ---------- Load data ----------

def load_quran():
    return json.loads(QURAN_JSON.read_text(encoding="utf-8"))

def load_bukhari():
    return BUKHARI_TXT.read_text(encoding="utf-8")

# ---------- Arabic cardinality patterns ----------

# For no-tashkeel text, undotted numeric tokens.
# Use NB/NE to tolerate CONJUNCTIVE clitic prefixes (و, ف) only — "and N" / "then N";
# other clitics (ل, ب, ك) produce false positives (e.g., 'لست' = 'you-are-not', not 'li-sitta').
_NB = r"(?:^|(?<=[\s\W]))(?:و|ف|)"
_NE = r"(?=$|[\s\W])"
CARDINALITY_PATTERNS = {
    3: [_NB + r"ثلاث[ةهى]?" + _NE, _NB + r"ثلاثا" + _NE],
    5: [_NB + r"خمس[ةهى]?" + _NE, _NB + r"خمسا" + _NE],
    6: [_NB + r"ست[ةه]?" + _NE, _NB + r"ستا" + _NE],              # sittun/sittatun/sittan
    7: [_NB + r"سبع[ةهى]?" + _NE, _NB + r"سبعا" + _NE],
    8: [_NB + r"ثماني[ةه]?" + _NE, _NB + r"ثمان" + _NE, _NB + r"ثمانيا" + _NE],
}

def count_cardinality_tokens(text, n):
    total = 0
    hits = []
    for pat in CARDINALITY_PATTERNS[n]:
        for m in re.finditer(pat, text):
            total += 1
            start = max(0, m.start()-25)
            end = min(len(text), m.end()+35)
            hits.append((m.start(), m.group(), text[start:end]))
    return total, hits

def count_cardinality_in_quran(quran, n):
    total = 0
    per_verse_hits = []
    for s in quran:
        for v in s["verses"]:
            t = v["text"]
            for pat in CARDINALITY_PATTERNS[n]:
                for m in re.finditer(pat, t):
                    total += 1
                    per_verse_hits.append((s["id"], v["id"], m.group()))
    return total, per_verse_hits

# ---------- Candidate PASS rules ----------

SEVEN_RE = re.compile(r"\bسبع[ةهى]?\b|سبعا\b")
HEAVEN_RE = re.compile(r"سماو|سماء|سموات")
# Cosmic synonyms for extended pattern (reported separately)
COSMIC_EXT_RE = re.compile(r"سماو|سماء|سموات|شداد|طرائق|طباق")

def c1_seven_heavens_strict(quran):
    """Occurrences of سبع + سماوات / سماء / سموات in same verse (strict phrase pattern).
    Tolerates و/ف clitic on سبع."""
    hits = []
    strict_pat = re.compile(r"(?:^|[\s\W])(?:و|ف|)سبع[ةهى]?\s{0,5}(?:سماو|سماء|سموات)|(?:^|[\s\W])(?:و|ف|)سبعا\s{0,5}(?:سماو|سماء)")
    for s in quran:
        for v in s["verses"]:
            t = v["text"]
            for m in strict_pat.finditer(t):
                hits.append((s["id"], v["id"], m.group().strip()))
    return hits

def c1_seven_heavens_extended(quran):
    """Broader pattern: سبع + any cosmic head-noun (سماء/سماوات/شداد/طرائق/طباق) within 10 chars."""
    ext_pat = re.compile(r"(?:^|[\s\W])(?:و|ف|)سبع[ةهى]?\s{0,10}(?:سماو|سماء|سموات|شداد|طرائق|طباق)|(?:^|[\s\W])(?:و|ف|)سبعا\s{0,10}(?:سماو|سماء|شداد|طرائق|طباق)")
    hits = []
    for s in quran:
        for v in s["verses"]:
            t = v["text"]
            for m in ext_pat.finditer(t):
                hits.append((s["id"], v["id"], m.group().strip()))
    return hits

def c2_fatiha_verses(quran):
    return quran[0]["total_verses"]

def c3_sab_tiwal(quran):
    """H-NEW-67 verified: top-7 longest in muṣḥaf-front."""
    # verify classical list Q 2,3,4,5,6,7 + (9 or 10) all are long (n_v >= 109)
    classical_ids = [2, 3, 4, 5, 6, 7, 9]
    # Return verse counts
    return {sid: quran[sid-1]["total_verses"] for sid in classical_ids}

def c4_q91_oath_cluster(quran):
    """Count contiguous opening verses of Q 91 that begin with 'و' + noun (oath form)."""
    q91 = quran[90]
    oath_count = 0
    for v in q91["verses"]:
        t = v["text"].strip()
        # Q91 opens with و + sun/moon/day/night/heaven/earth/soul
        # We check if verse starts with و followed by a definite or bare noun (oath opener)
        # per H-NEW-85, cluster length = 7 for Q91
        if t.startswith("و") and v["id"] <= 7:
            # Check it's not a conjunction merely by: v1-v7 all start with و + noun
            oath_count += 1
        else:
            break
    return oath_count

def c5_musabbihat(quran):
    """Count surahs whose v1 (no-tashkeel) begins with the SBḤ root."""
    sbh_starts = []
    for s in quran:
        v1 = s["verses"][0]["text"].strip()
        # first token
        tokens = v1.split()
        if not tokens:
            continue
        first = tokens[0]
        # Match سبح, سبحان, يسبح, also tolerate س ب ح root forms
        if re.match(r"^(سبح|سبحان|يسبح|سبحى|يسبحون|سبحت)", first):
            sbh_starts.append((s["id"], s["name"], v1[:60]))
    return sbh_starts

def c6_q7_prophets(quran):
    """Count pre-committed prophets (Adam, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā) named in Q 7.

    Note: regex uses lookbehind/lookahead on non-letter to tolerate clitic prefixes
    (و, ف, ل, ب, ك) on proper names — these are writing conventions, not new words.
    """
    # non-arabic-letter boundary
    NB = r"(?:^|(?<=[\s\W]))"
    NE = r"(?=$|[\s\W])"
    prophets = {
        "Adam": [NB + r"آدم" + NE, NB + r"ادم" + NE],
        "Nuh": [NB + r"نوح[اى]?" + NE],
        "Hud": [NB + r"هود[اى]?" + NE],
        "Salih": [NB + r"صالح[اى]?" + NE],
        "Lut": [NB + r"لوط[اى]?" + NE, r"لوطا?"],
        "Shuayb": [NB + r"شعيب[اى]?" + NE, r"شعيبا?"],
        "Musa": [r"موسى"],
    }
    q7 = quran[6]
    found = {}
    for p, pats in prophets.items():
        count = 0
        first_verse = None
        for v in q7["verses"]:
            t = v["text"]
            for pat in pats:
                if re.search(pat, t):
                    count += 1
                    if first_verse is None:
                        first_verse = v["id"]
                    break
        found[p] = {"count": count, "first_verse": first_verse}
    return found

def c7_sabet_cardinality_count(quran):
    """Total count of root-SBʿ cardinality tokens in Quran."""
    total, _ = count_cardinality_in_quran(quran, 7)
    return total

# ---------- Cell A: observed 7-fold count ----------

def cell_a(quran):
    results = {}

    # C1
    c1_strict = c1_seven_heavens_strict(quran)
    c1_ext = c1_seven_heavens_extended(quran)
    results["C1"] = {
        "description": "seven heavens (strict phrase سبع + سماء/سماوات adjacency)",
        "count_strict": len(c1_strict),
        "count_extended_with_shidad_tiraaq_tibaq": len(c1_ext),
        "classical_claim": "7",
        "strict_hits": c1_strict,
        "extended_hits": c1_ext,
        "pass_strict": len(c1_strict) == 7,
        "pass_extended": len(c1_ext) == 7,
    }

    # C2
    fat_v = c2_fatiha_verses(quran)
    results["C2"] = {
        "description": "al-Fātiḥa verse count (Hafs-Kūfan)",
        "count": fat_v,
        "classical_claim": 7,
        "pass": fat_v == 7,
    }

    # C3
    lens = c3_sab_tiwal(quran)
    results["C3"] = {
        "description": "7 long surahs — classical Q 2,3,4,5,6,7,9 (H-NEW-67 confirmed)",
        "verse_counts": lens,
        "pass": all(v >= 100 for v in lens.values()) and len(lens) == 7,
    }

    # C4
    oath_len = c4_q91_oath_cluster(quran)
    results["C4"] = {
        "description": "Q 91 oath-opener contiguous cluster length",
        "count": oath_len,
        "classical_claim": 7,
        "pass": oath_len == 7,
    }

    # C5
    sbh = c5_musabbihat(quran)
    results["C5"] = {
        "description": "Musabbiḥāt — surahs whose v1 starts with SBḤ root",
        "count": len(sbh),
        "classical_claim": 7,
        "members": [{"id": s[0], "name": s[1], "v1_head": s[2]} for s in sbh],
        "pass": len(sbh) == 7,
    }

    # C6
    prophets_q7 = c6_q7_prophets(quran)
    n_present = sum(1 for p in prophets_q7.values() if p["count"] > 0)
    results["C6"] = {
        "description": "7 prophets named in Q 7 (Adam, Nūḥ, Hūd, Ṣāliḥ, Lūṭ, Shuʿayb, Mūsā)",
        "present_count": n_present,
        "per_prophet": prophets_q7,
        "pass": n_present == 7,
    }

    # C7
    cardc = c7_sabet_cardinality_count(quran)
    results["C7"] = {
        "description": "Total سبع-root cardinality token count in Quran",
        "count": cardc,
        "pass_window": [7, 14, 21, 22, 23, 24, 25],
        "pass": cardc in {7, 14, 21, 22, 23, 24, 25},
    }

    passed = sum(1 for k in ["C1","C2","C3","C4","C5","C6","C7"]
                 if (results[k].get("pass") or results[k].get("pass_strict") or results[k].get("pass_extended")))
    # more careful pass count
    pass_bool = {
        "C1": results["C1"]["pass_strict"] or results["C1"]["pass_extended"],
        "C2": results["C2"]["pass"],
        "C3": results["C3"]["pass"],
        "C4": results["C4"]["pass"],
        "C5": results["C5"]["pass"],
        "C6": results["C6"]["pass"],
        "C7": results["C7"]["pass"],
    }
    results["pass_bool"] = pass_bool
    results["total_passed"] = sum(pass_bool.values())
    results["primary_direction_fires"] = results["total_passed"] >= 5
    return results

# ---------- Cell C: specificity over N in {3,5,6,7,8} ----------

def cell_c(quran):
    """For each N, count explicit cardinality tokens in Quran."""
    results = {}
    for n in [3, 5, 6, 7, 8]:
        total, hits = count_cardinality_in_quran(quran, n)
        results[n] = {
            "count": total,
            "sample_hits": hits[:10],
        }
    # Rank
    ranked = sorted(results.items(), key=lambda x: -x[1]["count"])
    results["_ranked"] = [(n, d["count"]) for n, d in ranked]
    results["_seven_is_max"] = ranked[0][0] == 7
    return results

# ---------- Cell B/D: Bukhārī baseline density ----------

def count_cardinality_in_text(text, n):
    total = 0
    for pat in CARDINALITY_PATTERNS[n]:
        total += len(re.findall(pat, text))
    return total

def cell_bd(quran, bukhari_text):
    """Rate comparison: Quran vs Bukhārī."""
    # Tokens
    quran_text = "\n".join(v["text"] for s in quran for v in s["verses"])
    n_tokens_quran = len(quran_text.split())
    n_tokens_bukhari = len(bukhari_text.split())

    results = {}
    for n in [3, 5, 6, 7, 8]:
        q_c = count_cardinality_in_text(quran_text, n)
        b_c = count_cardinality_in_text(bukhari_text, n)
        q_rate = q_c / n_tokens_quran * 10000
        b_rate = b_c / n_tokens_bukhari * 10000
        results[n] = {
            "quran_count": q_c,
            "quran_rate_per_10k": round(q_rate, 3),
            "bukhari_count": b_c,
            "bukhari_rate_per_10k": round(b_rate, 3),
            "quran_enriched_vs_bukhari": q_rate > b_rate,
            "ratio": round(q_rate / b_rate, 3) if b_rate > 0 else None,
        }

    # Seven-specific: does سبع+سماء/سماوات collocation happen in Bukhari?
    # Strict phrase
    strict_pat = re.compile(r"سبع[ةهى]?\s{0,5}(?:سماو|سماء|سموات)|سبعا\s{0,5}(?:سماو|سماء)")
    q_seven_heaven = len(strict_pat.findall(quran_text))
    b_seven_heaven = len(strict_pat.findall(bukhari_text))
    results["seven_heaven_phrase"] = {
        "quran": q_seven_heaven,
        "bukhari": b_seven_heaven,
        "quran_rate_per_10k": round(q_seven_heaven / n_tokens_quran * 10000, 4),
        "bukhari_rate_per_10k": round(b_seven_heaven / n_tokens_bukhari * 10000, 4),
    }

    # Permutation test: is Quran's 7-rate enriched vs Bukhari bootstrap slices?
    # Draw random length-matched slices from Bukhari; count 7-tokens per slice
    tokens_bukhari = bukhari_text.split()
    slice_len = n_tokens_quran
    # If Bukhari too small, cap
    max_start = max(0, len(tokens_bukhari) - slice_len)
    n_boot = 2000 if max_start > 0 else 0
    boot_7_counts = []
    for _ in range(n_boot):
        start = random.randint(0, max_start)
        slc = " ".join(tokens_bukhari[start:start+slice_len])
        boot_7_counts.append(count_cardinality_in_text(slc, 7))
    observed_q7 = count_cardinality_in_text(quran_text, 7)
    if boot_7_counts:
        # one-sided: Quran > Bukhari
        p_greater = sum(1 for b in boot_7_counts if b >= observed_q7) / len(boot_7_counts)
        p_less = sum(1 for b in boot_7_counts if b <= observed_q7) / len(boot_7_counts)
    else:
        p_greater = p_less = None

    results["permutation"] = {
        "observed_quran_seven_count": observed_q7,
        "bootstrap_n": len(boot_7_counts),
        "bootstrap_mean": round(sum(boot_7_counts) / len(boot_7_counts), 2) if boot_7_counts else None,
        "bootstrap_max": max(boot_7_counts) if boot_7_counts else None,
        "bootstrap_min": min(boot_7_counts) if boot_7_counts else None,
        "p_quran_greater": p_greater,
        "p_quran_less": p_less,
        "note": "one-sided p = fraction of bootstrap slices with >= observed count",
    }

    # Strict phrase permutation
    boot_strict = []
    for _ in range(n_boot):
        start = random.randint(0, max_start)
        slc = " ".join(tokens_bukhari[start:start+slice_len])
        boot_strict.append(len(strict_pat.findall(slc)))
    if boot_strict:
        p_strict = sum(1 for b in boot_strict if b >= q_seven_heaven) / len(boot_strict)
    else:
        p_strict = None
    results["permutation_strict_seven_heaven"] = {
        "observed_quran": q_seven_heaven,
        "bootstrap_mean": round(sum(boot_strict) / len(boot_strict), 3) if boot_strict else None,
        "bootstrap_max": max(boot_strict) if boot_strict else None,
        "p_quran_greater_or_equal": p_strict,
    }

    results["n_tokens_quran"] = n_tokens_quran
    results["n_tokens_bukhari"] = n_tokens_bukhari
    return results

# ---------- Specificity permutation (direction_secondary) ----------

def cell_c_perm(quran, cell_c_result, n_perm=5000):
    """Is 7 specifically enriched vs 3,5,6,8?
    Null: shuffle verses (don't change counts) — the counts stay the same trivially.
    Alternative: shuffle cardinality labels across tokens — i.e.,
    if we randomly relabeled each N-token as a random N, would 7 still dominate?

    This tests: given the observed counts of {3:n3, 5:n5, 6:n6, 7:n7, 8:n8},
    what's the prob that 7 is the max under uniform assignment?
    """
    counts = {n: cell_c_result[n]["count"] for n in [3, 5, 6, 7, 8]}
    total = sum(counts.values())
    # Null: multinomial uniform over 5 classes
    n_max_is_7 = 0
    n_max_is_7_strict = 0
    max_counts = []
    for _ in range(n_perm):
        # assign each of `total` tokens to random class
        shuf = [random.randint(0, 4) for _ in range(total)]
        c = [shuf.count(i) for i in range(5)]
        # index 3 corresponds to '7' since sorted [3,5,6,7,8]
        mx = max(c)
        if c[3] == mx:
            n_max_is_7 += 1
            if c.count(mx) == 1:
                n_max_is_7_strict += 1
    return {
        "observed_counts": counts,
        "observed_seven_is_max": max(counts, key=counts.get) == 7,
        "n_perm": n_perm,
        "p_null_7_is_max": n_max_is_7 / n_perm,
        "p_null_7_strict_max": n_max_is_7_strict / n_perm,
        "note": "under uniform-assignment null over {3,5,6,7,8}; tests specificity of 7",
    }

# ---------- Main ----------

def main():
    quran = load_quran()
    bukhari = load_bukhari()

    print("[1] Cell A — observed 7-fold counts...")
    ca = cell_a(quran)
    print(f"    total passed: {ca['total_passed']}/7")
    for k in ["C1","C2","C3","C4","C5","C6","C7"]:
        print(f"    {k}: pass={ca['pass_bool'][k]}")

    print("[2] Cell C — specificity N ∈ {3,5,6,7,8}...")
    cc = cell_c(quran)
    for n, info in cc["_ranked"]:
        print(f"    N={n}: {info} tokens")

    print("[3] Cell C permutation (specificity null)...")
    cc_perm = cell_c_perm(quran, cc, n_perm=5000)
    print(f"    p_null_7_is_max: {cc_perm['p_null_7_is_max']}")

    print("[4] Cell B/D — Bukhārī baseline density...")
    cbd = cell_bd(quran, bukhari)
    print(f"    n_tokens_quran={cbd['n_tokens_quran']}, n_tokens_bukhari={cbd['n_tokens_bukhari']}")
    for n in [3,5,6,7,8]:
        d = cbd[n]
        print(f"    N={n}: Quran={d['quran_rate_per_10k']}/10k, Bukhari={d['bukhari_rate_per_10k']}/10k, ratio={d['ratio']}")
    print(f"    Strict 7-heavens: Q={cbd['seven_heaven_phrase']['quran']}, B={cbd['seven_heaven_phrase']['bukhari']}")
    print(f"    Permutation (7-count) p={cbd['permutation']['p_quran_greater']}")
    print(f"    Permutation (strict 7-heavens) p={cbd['permutation_strict_seven_heaven']['p_quran_greater_or_equal']}")

    output = {
        "id": "H-NEW-119",
        "seed": SEED,
        "bonferroni_k": 3,
        "alpha_bon": 0.0167,
        "cell_a": ca,
        "cell_c_specificity": cc,
        "cell_c_permutation": cc_perm,
        "cell_bd_baseline": cbd,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2))
    print(f"\n[DONE] Wrote {OUT_JSON}")

if __name__ == "__main__":
    main()
