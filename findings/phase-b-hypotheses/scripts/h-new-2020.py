#!/usr/bin/env python3
"""H-NEW-2020 — Exhaustive surface-word exact-frequency balance scan +
curated antonym/complement-pair audit.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-2020-word-balance-scan.md
SHA256:  bfeb1abb9d68ba5448236b0833a0b4c9beeb3f6cfa1a5eb6c934806c370a5083

Surface-word (orthographic-token) sibling of the root-based generator H-NEW-2010.
"""

import hashlib
import json
import math
import random
import sys
import unicodedata
from collections import Counter
from pathlib import Path
from statistics import mean, pstdev

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-2020-word-balance-scan.md"
EXPECTED_SHA = "bfeb1abb9d68ba5448236b0833a0b4c9beeb3f6cfa1a5eb6c934806c370a5083"
QURAN = ROOT / "quran-text/quran-no-tashkeel.json"
OUT = ROOT / "findings/phase-b-hypotheses/csv/h-new-2020.json"
SEED = 20260509
N_PERM = 10_000
H1_THRESH = 6

PAUSE = "".join(chr(c) for c in range(0x06D4, 0x06EE))  # Qurʾānic recitation marks


def verify_prereg() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH: expected {EXPECTED_SHA}, got {actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:12]}…")


def clean(t: str) -> str:
    t = unicodedata.normalize("NFC", t)
    return "".join(ch for ch in t if ch not in PAUSE)


# ----- closed particle stop-list (LOCKED) -----------------------------------
STOPWORDS = {
    "من", "في", "ما", "إن", "لا", "على", "إلا", "ولا", "وما", "أن", "إلى",
    "لهم", "يا", "ومن", "ثم", "لكم", "به", "هو", "هم", "أو", "فلا", "ذلك",
    "هذا", "التي", "الذي", "الذين", "وهو", "وهم", "إذا", "إذ", "قد", "لقد",
    "كل", "عن", "بل", "أم", "إنا", "إنه", "إنهم", "إني", "إنك", "لكن", "كما",
    "حتى", "أي", "أيها", "هل", "لم", "لن", "لو", "ولو", "فإن", "وإن", "فإذا",
    "لها", "له", "بها", "بهم", "منهم", "منها", "فيها", "فيه", "عليها", "عليه",
    "إليه", "إليها", "عليهم", "إليهم", "إليك", "عليك", "لك", "بك", "بي", "لي",
    "أنا", "أنت", "أنتم", "نحن", "هي", "أولئك", "هؤلاء", "تلك", "هذه", "وهذا",
    "وقد", "ولكن", "فمن", "وكان", "كان", "كانوا", "وكانوا", "أنهم", "أنه",
    "بما", "لما", "مما", "عما", "فما", "كنتم", "وأن", "وإذ", "وإذا", "أفلا",
    "أم", "أما", "إما", "ليس", "إنما", "وإنما", "بل", "غير", "دون", "بين",
    "عند", "بعد", "قبل", "مع", "لئن", "أئذا", "أإنا", "ألا", "وألا",
}


def stem_count(counter: Counter, forms: list[str]) -> int:
    return sum(counter.get(f, 0) for f in forms)


# ----- curated pairs: (label, A_concept, B_concept, S_A, S_B, F_A[], F_B[], note)
CURATED = [
    ("dunyā / ākhira", "الدنيا", "الآخرة (hereafter)", "الدنيا", "الآخرة",
     ["الدنيا"],
     ["الآخرة","الآخر","بالآخرة","والآخرة","الآخرين","آخر","آخرين","وآخرون",
      "وآخرين","وآخر","وللآخرة","وبالآخرة","آخره","بآخرين","آخران","فآخران",
      "وآخرنا","آخرون","للآخرين","والآخرين","والآخر","للآخرة"],
     "F-ākhira conflates hereafter+last+other (maximal pro-balance reading)"),
    ("jannah / nār", "paradise", "fire", "الجنة", "النار",
     ["الجنة","جنة","جنات","وجنات","جنتان","جنتين","الجنتين","وجنة","بجنة",
      "لجنات","فجنة"],
     ["النار","نار","نارا","بالنار","فالنار","والنار","ناركم","نارهم"],
     "paradise-sense pruned of جناح/جند/جن/سجن/مجنون"),
    ("jannah / jahannam", "paradise", "hell", "الجنة", "جهنم",
     ["الجنة","جنة","جنات","وجنات","جنتان","جنتين","الجنتين","وجنة","بجنة",
      "لجنات","فجنة"],
     ["جهنم","لجهنم","بجهنم","وجهنم","فجهنم"],
     "same paradise set as pair 2"),
    ("malāʾika / shayāṭīn", "angels", "devils(pl)", "الملائكة", "الشياطين",
     ["الملائكة","والملائكة","للملائكة","ملائكة","وملائكته","بالملائكة","ملائكته"],
     ["الشياطين","والشياطين","شياطينهم","شياطين","للشياطين"],
     "shayāṭīn-PLURAL only; singular الشيطان excluded"),
    ("ḥayāt / mawt", "life(noun)", "death(noun)", "الحياة", "الموت",
     ["الحياة","حياة","حياتنا","بالحياة","حياتكم","لحياتي","والحياة","حياتهم",
      "وحياة"],
     ["الموت","موتها","موته","موتكم","موتهم","بالموت","والموت","موتا"],
     "NOUN layer both sides; verbal أحيا/يموت & الموتى/الميت excluded for parity"),
    ("khayr / sharr", "good", "evil", "خير", "شر",
     ["خير","خيرا","الخير","الخيرات","بخير","وخير","بالخير","الخيرة","للخير",
      "والخير","بالخيرات","خيرات"],
     ["شر","الشر","شرا","بشر","شرر","أشرار"],
     "sharr evil-noun; homograph شرك/بشر(human)/حشر EXCLUDED"),
    ("īmān / kufr", "faith(noun)", "disbelief(noun)", "الإيمان", "الكفر",
     ["إيمانا","الإيمان","إيمانكم","إيمانهم","بالإيمان","للإيمان","إيمانها",
      "إيمانه","والإيمان","بإيمانكم","بإيمانهم","بإيمان","بإيمانهن"],
     ["الكفر","كفر","كفرا","بالكفر","وكفر","وكفرا","كفره","للكفر","بكفرهم",
      "كفرهم"],
     "NOUN layer both sides; verbal آمن/كفروا excluded for parity"),
    ("hudā / ḍalāl", "guidance(noun)", "misguidance(noun)", "الهدى", "الضلال",
     ["هدى","الهدى","وهدى","بالهدى","فهدى","هداي","لهدى","والهدى","للهدى"],
     ["ضلال","الضلال","الضلالة","ضلالا","ضلالتهم","ضلالك","ضلالهم","وضلال"],
     "ḍalāl-noun; homograph فضل/الفضل & verbal ضل EXCLUDED for parity"),
    ("nūr / ẓulumāt", "light", "darkness(pl)", "النور", "الظلمات",
     ["النور","نور","نورا","والنور","نوره","ونور","نورهم","بنورهم","لنوره",
      "بنور","نوركم","ونورهم","نورنا"],
     ["الظلمات","ظلمات","كظلمات","وظلمات","بالظلمات"],
     "darkness-PLURAL noun; verbal ظلم/ظالم EXCLUDED"),
    ("ṣayf / shitāʾ", "summer", "winter", "الصيف", "الشتاء",
     ["الصيف","والصيف","صيف","صيفا"],
     ["الشتاء","شتاء","وشتاء","بالشتاء"],
     "ṣayf strict form الصيف does NOT occur; only والصيف (Q106:2)"),
    ("ḥarr / bard", "heat", "cold", "الحر", "البرد",
     ["الحر","حر","حرا","وحر","بالحر"],
     ["بردا","برد","بردهن","البرد","وبرد"],
     "ḥarr heat-noun; homograph البحر/الحرام/سحر/حرث EXCLUDED"),
    ("rajul / nisāʾ", "man", "women", "الرجل", "النساء",
     ["رجل","الرجل","رجلا","لرجل","فرجل","ورجل","الرجال","رجال","رجالا",
      "رجالكم","للرجال","وللرجال","فرجالا","برجال","رجلين","رجلان","الرجلين"],
     ["النساء","نساء","ونساء","نساءكم","نساءهم","وللنساء","والنساء","ونساءنا",
      "ونساءكم","نساءنا","نساءهن"],
     "rajul human-male sing+pl+dual; رِجل 'foot' (أرجلكم..) EXCLUDED"),
    ("qul / qālū", "say(impv)", "they-said", "قل", "قالوا",
     ["قل","وقل","فقل"],
     ["قالوا","وقالوا","فقالوا","لقالوا"],
     "qul imperative only; قلوب/قليل/قلنا are different lexemes/forms"),
]


def zipf_collision_null(n_types: int, counts: list[int]) -> tuple[float, float]:
    """H3 reference: how collision-prone is a generic Zipfian vocabulary of the
    same total mass and size? Returns (mean_frac, sd_frac) of the fraction of
    types that share their (integer-rounded) count with >=1 other type, across
    N_PERM synthetic Zipf vocabularies matched on n_types and total token mass.
    """
    rng = random.Random(SEED)
    total = sum(counts)
    # Zipf law: freq(rank r) ∝ 1/r ; scale so expected total == total.
    harmonic = sum(1.0 / r for r in range(1, n_types + 1))
    base = [total / (r * harmonic) for r in range(1, n_types + 1)]
    fracs = []
    for _ in range(N_PERM):
        # Poisson-ish integerisation with randomised rounding to avoid bias
        synth = []
        for b in base:
            fl = math.floor(b)
            synth.append(fl + (1 if rng.random() < (b - fl) else 0))
        synth = [c for c in synth if c >= 2]  # match content_ge2 filter
        cc = Counter(synth)
        in_coll = sum(n for c, n in cc.items() if n >= 2)
        fracs.append(in_coll / len(synth) if synth else 0.0)
    return mean(fracs), pstdev(fracs)


def main() -> None:
    verify_prereg()
    data = json.loads(QURAN.read_text())
    toks: list[str] = []
    for entry in data:
        for v in entry["verses"]:
            toks.extend(t for t in clean(v["text"]).split() if t)
    counter = Counter(toks)
    print(f"corpus tokens={len(toks)}  distinct types={len(counter)}")

    # ---- curated audit ----
    curated_out = []
    balanced_any = 0
    for (label, ca, cb, sA, sB, fA, fB, note) in CURATED:
        s_a, s_b = counter.get(sA, 0), counter.get(sB, 0)
        f_a, f_b = stem_count(counter, fA), stem_count(counter, fB)
        s_bal = s_a == s_b
        f_bal = f_a == f_b
        any_bal = s_bal or f_bal
        balanced_any += 1 if any_bal else 0
        curated_out.append({
            "pair": label, "concept_A": ca, "concept_B": cb,
            "S_form_A": sA, "S_form_B": sB,
            "S_count_A": s_a, "S_count_B": s_b, "S_balanced": s_bal,
            "F_count_A": f_a, "F_count_B": f_b, "F_balanced": f_bal,
            "balanced_under_any": any_bal, "note": note,
        })

    h1_verdict = ("PASS-DIRECTED (selective)" if balanced_any <= H1_THRESH
                  else "REVERSAL (more balance than predicted)")

    # ---- H2 flagship ----
    dunya = counter.get("الدنيا", 0)
    akhira = counter.get("الآخرة", 0)
    h2_equal = dunya == akhira
    h2_verdict = ("REVERSAL (strict equal)" if h2_equal
                  else "PASS-DIRECTED (strict unequal ⇒ legend FALSIFIED)")

    # ---- exhaustive scan ----
    content = {w: c for w, c in counter.items()
               if w not in STOPWORDS and len(w) > 2 and c >= 2}
    by_count: Counter = Counter(content.values())
    hapax = sum(1 for c in counter.values() if c == 1)
    n_pairs = sum(n * (n - 1) // 2 for n in by_count.values())
    in_coll = sum(n for c, n in by_count.items() if n >= 2)
    frac_coll = in_coll / len(content) if content else 0.0

    z_mean, z_sd = zipf_collision_null(len(content), list(content.values()))
    z = (frac_coll - z_mean) / z_sd if z_sd > 0 else 0.0
    h3_verdict = ("PASS-DIRECTED (balance is generic, |z|<2)" if abs(z) < 2
                  else "REVERSAL (Quran collision rate atypical vs Zipf)")

    # top multiplicity count values
    top_mult = sorted(by_count.items(), key=lambda kv: (-kv[1], kv[0]))[:25]
    top_mult_out = [{"count_value": c, "n_types_sharing": n,
                     "n_balanced_pairs": n * (n - 1) // 2} for c, n in top_mult]

    # random "famous-looking" balanced content-word pairs (cherry-pick demo)
    rng = random.Random(SEED)
    famous_demo = []
    # pick count-values with multiplicity in a "famous" mid band (5..50 types)
    cand_counts = [c for c, n in by_count.items() if 2 <= n <= 8 and c >= 10]
    rng.shuffle(cand_counts)
    for cval in cand_counts[:15]:
        words = sorted([w for w, c in content.items() if c == cval])
        if len(words) >= 2:
            a, b = rng.sample(words, 2)
            famous_demo.append({"word_A": a, "word_B": b, "both_occur": cval})

    overall = "PASS-DIRECTED (all 3 hypotheses confirmed)"
    if "REVERSAL" in (h1_verdict + h2_verdict + h3_verdict):
        overall = "MIXED — see per-hypothesis verdicts (reversal present)"

    out = {
        "id": "H-NEW-2020",
        "title": "Exhaustive surface-word balance scan + curated antonym-pair audit",
        "prereg_sha": EXPECTED_SHA,
        "seed": SEED,
        "n_perm": N_PERM,
        "corpus_token_count": len(toks),
        "distinct_types": len(counter),
        "curated": curated_out,
        "curated_balanced_count": balanced_any,
        "curated_total": len(CURATED),
        "H1_threshold": H1_THRESH,
        "H1_verdict": h1_verdict,
        "dunya_akhira_strict": {"الدنيا": dunya, "الآخرة": akhira, "equal": h2_equal},
        "H2_verdict": h2_verdict,
        "exhaustive": {
            "content_types_ge2": len(content),
            "hapax_forms_count1": hapax,
            "n_exact_balanced_pairs": n_pairs,
            "frac_types_in_collision": round(frac_coll, 6),
            "zipf_ref_frac_mean": round(z_mean, 6),
            "zipf_ref_frac_sd": round(z_sd, 6),
            "z": round(z, 4),
            "top_multiplicity_counts": top_mult_out,
            "random_famous_looking_pairs": famous_demo,
        },
        "H3_verdict": h3_verdict,
        "verdict": overall,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False), encoding="utf-8")

    print("\n--- CURATED ---")
    for r in curated_out:
        print(f"{r['pair']:24s}  S:{r['S_count_A']}={r['S_count_B']}? {r['S_balanced']!s:5}  "
              f"F:{r['F_count_A']}={r['F_count_B']}? {r['F_balanced']!s:5}  any={r['balanced_under_any']}")
    print(f"\nbalanced (any rule): {balanced_any}/{len(CURATED)}  → H1 {h1_verdict}")
    print(f"dunyā={dunya}  ākhira(strict)={akhira}  → H2 {h2_verdict}")
    print(f"content_types_ge2={len(content)}  balanced_pairs={n_pairs}  "
          f"frac_in_collision={frac_coll:.3f}  zipf={z_mean:.3f}±{z_sd:.3f}  z={z:.2f} → H3 {h3_verdict}")
    print(f"\nVerdict: {overall}\nwrote {OUT}")


if __name__ == "__main__":
    main()
