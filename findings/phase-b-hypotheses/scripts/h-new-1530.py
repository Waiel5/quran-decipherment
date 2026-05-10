#!/usr/bin/env python3
"""
H-NEW-1530 — al-Khalifa "miracle of 19" rigorous 5-sub-claim audit
Pre-registration SHA-locked: 461ac84c5e1bfd14e5178a72f17fa11e7e25131c8f39f77bdf62de705edb1269

Tests 5 specific al-Khalifa "Code 19" integer-equality claims against the on-disk
Hafs-Kufan Qur'an corpus. Per claim verdict ∈ {CONFIRMED, FALSIFIED, DEFINITION-DEPENDENT}.
"""

import json
import hashlib
import sys
from collections import Counter
from pathlib import Path

PROJECT = Path("/Users/grey/Downloads/quran")
PREREG  = PROJECT / "findings/phase-b-hypotheses/prereg-h-new-1530-khalifa-19-audit.md"
EXPECTED_SHA = "461ac84c5e1bfd14e5178a72f17fa11e7e25131c8f39f77bdf62de705edb1269"
OUT_JSON = PROJECT / "findings/phase-b-hypotheses/csv/h-new-1530.json"

SEED = 20260509

# Constants per pre-registration
TARGETS = {"C1": 19, "C2": 29, "C3": 114, "C4": 19, "C5": 2698}
BASMALA_REF = "بسم الله الرحمن الرحيم"

ALLAH_FORMS_A = ["الله"]
ALLAH_FORMS_B = ALLAH_FORMS_A + ["والله", "فالله", "بالله", "تالله", "اللهم"]
ALLAH_FORMS_C = ALLAH_FORMS_B + ["لله", "ولله", "فلله"]
ALLAH_FORMS_D = ALLAH_FORMS_C + ["آلله", "أبالله", "وتالله"]
ALLAH_FORMS_E = [w for w in ALLAH_FORMS_D if w != "اللهم"]


def verify_prereg_sha():
    h = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if h != EXPECTED_SHA:
        print(f"PREREG SHA MISMATCH: got {h}, expected {EXPECTED_SHA}", file=sys.stderr)
        sys.exit(2)
    return h


def load_corpus(path):
    return json.loads(path.read_text())


def word_count_verses(surah, verse_ids):
    """Count whitespace tokens across given verse ids in a surah dict."""
    total = 0
    for vid in verse_ids:
        v = next(v for v in surah["verses"] if v["id"] == vid)
        total += len(v["text"].split())
    return total


def grapheme_count_no_space(s):
    return len(s.replace(" ", ""))


def c1_first_revelation(d):
    """Q 96:1-5 word count claim = 19."""
    q96 = next(s for s in d if s["id"] == 96)
    obs = word_count_verses(q96, [1, 2, 3, 4, 5])
    verdict = "CONFIRMED" if obs == TARGETS["C1"] else "FALSIFIED"
    return {
        "claim": "Q 96:1-5 = 19 words (khalifa-first-revelation-19-words)",
        "expected": TARGETS["C1"],
        "observed": obs,
        "verdict": verdict,
        "per_verse": {
            f"96:{vid}": len(next(v for v in q96["verses"] if v["id"] == vid)["text"].split())
            for vid in [1, 2, 3, 4, 5]
        },
    }


def c2_fatiha(d):
    """Q 1 = 29 words claim."""
    q1 = next(s for s in d if s["id"] == 1)
    obs = sum(len(v["text"].split()) for v in q1["verses"])
    verdict = "CONFIRMED" if obs == TARGETS["C2"] else "FALSIFIED"
    return {
        "claim": "Q 1 (al-Fatiha) total = 29 words (per appendix-1 word-count table)",
        "expected": TARGETS["C2"],
        "observed": obs,
        "verdict": verdict,
        "per_verse": {f"1:{v['id']}": len(v["text"].split()) for v in q1["verses"]},
    }


def c3_surah_count(d):
    """114 = 19 * 6."""
    obs = len(d)
    ok = (obs == 114) and (obs % 19 == 0)
    return {
        "claim": "114 surahs = 19*6 (khalifa-114-chapters-19x6)",
        "expected": 114,
        "observed": obs,
        "observed_div_19_remainder": obs % 19,
        "verdict": "CONFIRMED" if ok else "FALSIFIED",
    }


def c4_basmala_letters(d, paths_probe):
    """Basmala = 19 letters (no-tashkeel grapheme-count)."""
    q1 = next(s for s in d if s["id"] == 1)
    basmala = q1["verses"][0]["text"]
    assert basmala == BASMALA_REF, f"Unexpected basmala form: {basmala!r}"
    obs = grapheme_count_no_space(basmala)
    verdict = "CONFIRMED" if obs == TARGETS["C4"] else "FALSIFIED"
    # Probes
    probes = {"no-tashkeel": obs}
    # Full-tashkeel: include combining marks counted-or-not
    ft_path = paths_probe.get("full")
    if ft_path and ft_path.exists():
        ft = json.loads(ft_path.read_text())
        ft_q1 = next(s for s in ft if s["id"] == 1)
        ft_basmala = ft_q1["verses"][0]["text"]
        # Count graphemes EXCLUDING combining marks (i.e. base letters only)
        # Combining marks are in U+064B..U+065F (Arabic diacritics) and U+0670 (dagger alef)
        # plus U+06DC..U+06ED etc.
        import unicodedata as _u
        base_only = "".join(c for c in ft_basmala.replace(" ", "")
                            if _u.category(c) != "Mn")
        probes["full-tashkeel-base-letters"] = len(base_only)
        probes["full-tashkeel-with-marks"] = len(ft_basmala.replace(" ", ""))
        probes["full-tashkeel-form"] = ft_basmala
    # Uthmani-consonantal
    uc_path = paths_probe.get("uthmani")
    if uc_path and uc_path.exists():
        try:
            uc = json.loads(uc_path.read_text())
            uc_q1 = None
            # try common shapes
            if isinstance(uc, list):
                uc_q1 = next((s for s in uc if s.get("id") == 1 or s.get("surah") == 1), None)
            elif isinstance(uc, dict):
                for k in ("1", 1):
                    if k in uc:
                        uc_q1 = uc[k]
                        break
            if uc_q1:
                # Find the basmala verse
                verses = uc_q1.get("verses", uc_q1)
                if isinstance(verses, list):
                    v1 = verses[0]
                    text = v1.get("text") if isinstance(v1, dict) else v1
                    if text:
                        probes["uthmani-consonantal"] = len(text.replace(" ", ""))
                        probes["uthmani-consonantal-form"] = text
        except Exception as e:
            probes["uthmani-consonantal-error"] = str(e)
    return {
        "claim": "Basmala = 19 letters (khalifa-bismillah-19-letters)",
        "expected": TARGETS["C4"],
        "observed": obs,
        "verdict": verdict,
        "probes": probes,
    }


def c5_allah_count(d):
    """Total 'Allah' occurrences = 2698 = 19*142."""
    all_words = []
    for s in d:
        for v in s["verses"]:
            all_words.extend(v["text"].split())
    counter = Counter(all_words)

    tallies = {
        "A": sum(counter[w] for w in ALLAH_FORMS_A),
        "B": sum(counter[w] for w in ALLAH_FORMS_B),
        "C": sum(counter[w] for w in ALLAH_FORMS_C),
        "D": sum(counter[w] for w in ALLAH_FORMS_D),
        "E": sum(counter[w] for w in ALLAH_FORMS_E),
    }
    mods = {k: v % 19 for k, v in tallies.items()}

    # Verdict logic per prereg
    match_exact = any(t == TARGETS["C5"] for t in tallies.values())
    near_and_div19 = any(
        (t % 19 == 0) and abs(t - TARGETS["C5"]) <= 20
        for t in tallies.values()
    )
    if match_exact:
        verdict = "CONFIRMED"
    elif near_and_div19:
        verdict = "DEFINITION-DEPENDENT"
    else:
        verdict = "FALSIFIED"

    # Per-form raw counts for transparency
    per_form = {
        w: counter[w]
        for w in (ALLAH_FORMS_D + ["اللهم"])
    }
    # ensure single occurrence in dict (set-uniqueness)
    per_form = dict(per_form)

    return {
        "claim": "Total 'Allah' references = 2698 = 19*142 (appendix-1)",
        "expected": TARGETS["C5"],
        "tally_A_definition": "exact word الله only",
        "tally_A": tallies["A"],
        "tally_A_mod19": mods["A"],
        "tally_B_definition": "A + prefixed (wa/fa/bi/ta) + vocative اللهم",
        "tally_B": tallies["B"],
        "tally_B_mod19": mods["B"],
        "tally_C_definition": "B + li-llah forms (لله, ولله, فلله)",
        "tally_C": tallies["C"],
        "tally_C_mod19": mods["C"],
        "tally_D_definition": "C + interrogative/compound prefixed (آلله, أبالله, وتالله)",
        "tally_D": tallies["D"],
        "tally_D_mod19": mods["D"],
        "tally_E_definition": "D minus vocative اللهم",
        "tally_E": tallies["E"],
        "tally_E_mod19": mods["E"],
        "per_form_counts": per_form,
        "verdict": verdict,
        "closest_to_target": min(tallies.values(), key=lambda x: abs(x - TARGETS["C5"])),
        "closest_19_divisible": min(
            [(k, v) for k, v in tallies.items() if v % 19 == 0],
            key=lambda kv: abs(kv[1] - TARGETS["C5"]),
            default=(None, None),
        ),
    }


def main():
    prereg_sha = verify_prereg_sha()
    no_tashkeel = PROJECT / "quran-text/quran-no-tashkeel.json"
    full_tashkeel = PROJECT / "quran-text/quran-full-tashkeel.json"
    uthmani_cons = PROJECT / "data/alt-text/quran-uthmani-consonantal.json"

    d = load_corpus(no_tashkeel)

    results = {
        "C1": c1_first_revelation(d),
        "C2": c2_fatiha(d),
        "C3": c3_surah_count(d),
        "C4": c4_basmala_letters(d, {"full": full_tashkeel, "uthmani": uthmani_cons}),
        "C5": c5_allah_count(d),
    }

    tally = Counter(r["verdict"] for r in results.values())

    # Composite verdict
    n_conf = tally.get("CONFIRMED", 0)
    n_fals = tally.get("FALSIFIED", 0)
    n_dd = tally.get("DEFINITION-DEPENDENT", 0)
    if n_conf == 5:
        composite = "MIRACLE OF 19 EMPIRICALLY SUPPORTED (all 5 sub-claims confirmed)"
    elif n_conf >= 4:
        composite = "STRONG-PARTIAL SUPPORT"
    elif n_conf == 3:
        composite = "SPLIT"
    elif n_conf == 2:
        composite = "LARGELY FALSIFIED (only 2-of-5 confirmed)"
    elif n_conf == 1:
        composite = "LARGELY FALSIFIED (only 1-of-5 confirmed)"
    else:
        composite = "FULL FALSIFICATION (0-of-5 confirmed)"

    output = {
        "id": "H-NEW-1530",
        "title": "al-Khalifa 'miracle of 19' — 5-sub-claim rigorous audit",
        "prereg_sha": prereg_sha,
        "seed": SEED,
        "phase": "B",
        "corpus": str(no_tashkeel.relative_to(PROJECT)),
        "sub_claims": results,
        "verdict_tally": dict(tally),
        "composite_verdict": composite,
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    OUT_JSON.write_text(json.dumps(output, ensure_ascii=False, indent=2))

    # Stdout summary
    print(f"# H-NEW-1530 results")
    print(f"prereg_sha: {prereg_sha}")
    for k, r in results.items():
        print(f"\n{k}: {r['claim']}")
        if 'observed' in r:
            print(f"  observed = {r['observed']}  expected = {r['expected']}")
        if 'tally_A' in r:
            for tk in "ABCDE":
                print(f"  tally_{tk} = {r[f'tally_{tk}']}  (mod 19 = {r[f'tally_{tk}_mod19']})  [{r[f'tally_{tk}_definition']}]")
            print(f"  closest_to_2698 = {r['closest_to_target']}")
            print(f"  closest_19_divisible = {r['closest_19_divisible']}")
        print(f"  VERDICT: {r['verdict']}")
        if 'probes' in r:
            for pk, pv in r['probes'].items():
                print(f"    probe[{pk}] = {pv}")
    print(f"\nTALLY: {dict(tally)}")
    print(f"COMPOSITE: {composite}")
    print(f"\nWrote: {OUT_JSON}")


if __name__ == "__main__":
    main()
