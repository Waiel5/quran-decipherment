#!/usr/bin/env python3
"""H-NEW-1800 — 99 asmāʾ al-ḥusnā complete enumeration + alternative-orthography rehabilitation audit.

Pre-reg: findings/phase-b-hypotheses/prereg-h-new-1800-99-names-enumeration.md
SHA256:  9f31c98e532ae8e7b9e52817773fd9bf21f4859fcc03eab65fbafb86e02c4e56

Rules-tuple: (Variants A/B/C on no-tashkeel + Variant D on full-tashkeel,
              orthographic-token, graphemes, basmala-counted-only-in-Q1,
              Hafs-Kufan, Mashriqi)

Computes per-name presence under 4 variant rules:
  A. Strict substring with ال (no-tashkeel)
  B. Substring without ال (no-tashkeel)
  C. Triliteral consonantal-root substring (no-tashkeel, locked NAME_TO_ROOT dict)
  D. Rasm-skeleton substring matching against full-tashkeel corpus
Then catalogues rehabilitation status and identifies irrecoverable set.
"""

import hashlib
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path("/Users/grey/Downloads/quran")
PREREG = ROOT / "findings/phase-b-hypotheses/prereg-h-new-1800-99-names-enumeration.md"
EXPECTED_SHA = "9f31c98e532ae8e7b9e52817773fd9bf21f4859fcc03eab65fbafb86e02c4e56"
QURAN_NT = ROOT / "quran-text/quran-no-tashkeel.json"
QURAN_FT = ROOT / "quran-text/quran-full-tashkeel.json"
NAMES_PATH = ROOT / "data/asma-al-husna.txt"
OUT_PATH = ROOT / "findings/phase-b-hypotheses/csv/h-new-1800.json"

SEED = 20260509  # for any deterministic operation; this script is descriptive-only


# ------------------------------------------------------------------------
# LOCKED: triliteral root for each of 99 al-Tirmidhī names
# Derived from standard Arabic lexicography (Lane, Hans Wehr) +
# cross-checked against QAC root-index where applicable.
# Root letters in Arabic, three letters per root (rarely 4 for quadriliteral).
# ------------------------------------------------------------------------
NAME_TO_ROOT = {
    "الله":          "اله",   # Allāh (special: derived from أ-ل-ه)
    "الرحمن":        "رحم",   # al-Raḥmān
    "الرحيم":        "رحم",   # al-Raḥīm
    "الملك":         "ملك",   # al-Malik
    "القدوس":        "قدس",   # al-Quddūs
    "السلام":        "سلم",   # al-Salām
    "المؤمن":        "امن",   # al-Muʾmin
    "المهيمن":       "همن",   # al-Muhaymin (quadrilateral; root هيمن)
    "العزيز":        "عزز",   # al-ʿAzīz
    "الجبار":        "جبر",   # al-Jabbār
    "المتكبر":       "كبر",   # al-Mutakabbir
    "الخالق":        "خلق",   # al-Khāliq
    "البارئ":        "برا",   # al-Bāriʾ
    "المصور":        "صور",   # al-Muṣawwir
    "الغفار":        "غفر",   # al-Ghaffār
    "القهار":        "قهر",   # al-Qahhār
    "الوهاب":        "وهب",   # al-Wahhāb
    "الرزاق":        "رزق",   # al-Razzāq
    "الفتاح":        "فتح",   # al-Fattāḥ
    "العليم":        "علم",   # al-ʿAlīm
    "القابض":        "قبض",   # al-Qābiḍ
    "الباسط":        "بسط",   # al-Bāsiṭ
    "الخافض":        "خفض",   # al-Khāfiḍ
    "الرافع":        "رفع",   # al-Rāfiʿ
    "المعز":         "عزز",   # al-Muʿizz (causative of ʿazza)
    "المذل":         "ذلل",   # al-Mudhill
    "السميع":        "سمع",   # al-Samīʿ
    "البصير":        "بصر",   # al-Baṣīr
    "الحكم":         "حكم",   # al-Ḥakam
    "العدل":         "عدل",   # al-ʿAdl
    "اللطيف":        "لطف",   # al-Laṭīf
    "الخبير":        "خبر",   # al-Khabīr
    "الحليم":        "حلم",   # al-Ḥalīm
    "العظيم":        "عظم",   # al-ʿAẓīm
    "الغفور":        "غفر",   # al-Ghafūr
    "الشكور":        "شكر",   # al-Shakūr
    "العلي":         "علو",   # al-ʿAlī
    "الكبير":        "كبر",   # al-Kabīr
    "الحفيظ":        "حفظ",   # al-Ḥafīẓ
    "المقيت":        "قوت",   # al-Muqīt
    "الحسيب":        "حسب",   # al-Ḥasīb
    "الجليل":        "جلل",   # al-Jalīl
    "الكريم":        "كرم",   # al-Karīm
    "الرقيب":        "رقب",   # al-Raqīb
    "المجيب":        "جوب",   # al-Mujīb
    "الواسع":        "وسع",   # al-Wāsiʿ
    "الحكيم":        "حكم",   # al-Ḥakīm
    "الودود":        "ودد",   # al-Wadūd
    "المجيد":        "مجد",   # al-Majīd
    "الباعث":        "بعث",   # al-Bāʿith
    "الشهيد":        "شهد",   # al-Shahīd
    "الحق":          "حقق",   # al-Ḥaqq
    "الوكيل":        "وكل",   # al-Wakīl
    "القوي":         "قوي",   # al-Qawī
    "المتين":        "متن",   # al-Matīn
    "الولي":         "ولي",   # al-Walī
    "الحميد":        "حمد",   # al-Ḥamīd
    "المحصي":        "حصي",   # al-Muḥṣī
    "المبدئ":        "بدا",   # al-Mubdiʾ (root ب-د-أ)
    "المعيد":        "عود",   # al-Muʿīd
    "المحيي":        "حيي",   # al-Muḥyī
    "المميت":        "موت",   # al-Mumīt
    "الحي":          "حيي",   # al-Ḥayy
    "القيوم":        "قوم",   # al-Qayyūm
    "الواجد":        "وجد",   # al-Wājid
    "الماجد":        "مجد",   # al-Mājid
    "الواحد":        "وحد",   # al-Wāḥid
    "الصمد":         "صمد",   # al-Ṣamad
    "القادر":        "قدر",   # al-Qādir
    "المقتدر":       "قدر",   # al-Muqtadir
    "المقدم":        "قدم",   # al-Muqaddim
    "المؤخر":        "اخر",   # al-Muʾakhkhir
    "الأول":         "اول",   # al-Awwal
    "الآخر":         "اخر",   # al-Ākhir
    "الظاهر":        "ظهر",   # al-Ẓāhir
    "الباطن":        "بطن",   # al-Bāṭin
    "الوالي":        "ولي",   # al-Wālī
    "المتعالي":      "علو",   # al-Mutaʿālī
    "البر":          "برر",   # al-Barr
    "التواب":        "توب",   # al-Tawwāb
    "المنتقم":       "نقم",   # al-Muntaqim
    "العفو":         "عفو",   # al-ʿAfuww
    "الرؤوف":        "راف",   # al-Raʾūf (root ر-أ-ف)
    "مالك الملك":    "ملك",   # Mālik al-Mulk (multi-token; root of substantive)
    "ذو الجلال والإكرام": "جلل",  # Dhū al-Jalāl wa-l-Ikrām (multi-token; primary root of جلال)
    "المقسط":        "قسط",   # al-Muqsiṭ
    "الجامع":        "جمع",   # al-Jāmiʿ
    "الغني":         "غني",   # al-Ghanī
    "المغني":        "غني",   # al-Mughnī
    "المانع":        "منع",   # al-Māniʿ
    "الضار":         "ضرر",   # al-Ḍār
    "النافع":        "نفع",   # al-Nāfiʿ
    "النور":         "نور",   # al-Nūr
    "الهادي":        "هدي",   # al-Hādī
    "البديع":        "بدع",   # al-Badīʿ
    "الباقي":        "بقي",   # al-Bāqī
    "الوارث":        "ورث",   # al-Wārith
    "الرشيد":        "رشد",   # al-Rashīd
    "الصبور":        "صبر",   # al-Ṣabūr
}


# ------------------------------------------------------------------------
# Arabic text normalization
# ------------------------------------------------------------------------

# Diacritics to strip: fatha, damma, kasra, sukun, shadda, fathatan, dammatan, kasratan,
# tatweel, dagger alif (small), and the various small superscript marks
TASHKEEL = [
    "ً",  # FATHATAN
    "ٌ",  # DAMMATAN
    "ٍ",  # KASRATAN
    "َ",  # FATHA
    "ُ",  # DAMMA
    "ِ",  # KASRA
    "ّ",  # SHADDA
    "ْ",  # SUKUN
    "ٰ",  # SUPERSCRIPT ALEF
    "ٓ",  # MADDAH ABOVE
    "ٔ",  # HAMZA ABOVE
    "ٕ",  # HAMZA BELOW
    "ٖ",  # SUBSCRIPT ALEF
    "ـ",  # TATWEEL
    "ۜ",  # SMALL HIGH SEEN
    "۟",  # SMALL HIGH ROUNDED ZERO
    "۠",  # SMALL HIGH UPRIGHT RECTANGULAR ZERO
    "ۢ",  # SMALL HIGH MEEM ISOLATED FORM
    "ۣ",  # SMALL LOW SEEN
    "ۥ",  # SMALL WAW
    "ۦ",  # SMALL YA
    "ۨ",  # SMALL HIGH NOON
    "۪",  # EMPTY CENTRE LOW STOP
    "۫",  # EMPTY CENTRE HIGH STOP
    "۬",  # ROUNDED HIGH STOP WITH FILLED CENTRE
    "ۭ",  # SMALL LOW MEEM
]
TASHKEEL_RE = re.compile("[" + "".join(TASHKEEL) + "]")

def strip_combining_marks(s: str) -> str:
    """Strip ALL Unicode combining/non-spacing marks (category Mn).
    Catches Quranic-script-specific diacritics not in the named TASHKEEL list,
    e.g. U+06E1 ARABIC SMALL HIGH DOTLESS HEAD OF KHAH (sukun-substitute).
    """
    return "".join(c for c in s if not unicodedata.combining(c))

# Rasm-skeleton normalization (collapses letter variants to canonical rasm form)
# Used for Variant D (full-tashkeel) — strip all diacritics, then normalize letter shapes.
RASM_MAP = {
    "ٱ": "ا",  # ALEF WASLA → ALEF
    "آ": "ا",  # ALEF WITH MADDA → ALEF
    "أ": "ا",  # ALEF WITH HAMZA ABOVE → ALEF
    "إ": "ا",  # ALEF WITH HAMZA BELOW → ALEF
    "ى": "ي",  # ALEF MAKSURA → YA  (rasm-collapse)
    "ؤ": "و",  # WAW WITH HAMZA ABOVE → WAW
    "ئ": "ي",  # YEH WITH HAMZA ABOVE → YA
    "ة": "ه",  # TA MARBUTA → HA (rasm-collapse)
}

def strip_tashkeel(s: str) -> str:
    """Strip named-tashkeel chars + ALL Unicode combining marks (category Mn).
    The category-Mn fallback catches less-common Quranic-script diacritics
    (e.g. U+06E1 sukun-substitute) that the named list misses.
    """
    s = TASHKEEL_RE.sub("", s)
    return strip_combining_marks(s)

def normalize_ws(s: str) -> str:
    return " ".join(s.split())

def to_rasm(s: str) -> str:
    """Strip diacritics and normalize letter shapes to rasm-skeleton form."""
    s = strip_tashkeel(s)
    return "".join(RASM_MAP.get(c, c) for c in s)

def strip_al_prefix(name: str) -> str:
    """Remove leading ال from the FIRST token of name (for Variant B)."""
    tokens = name.split()
    if tokens and tokens[0].startswith("ال") and len(tokens[0]) > 2:
        tokens[0] = tokens[0][2:]
    elif tokens and tokens[0].startswith("الـ"):
        tokens[0] = tokens[0][3:]
    # Handle hamza-on-alif variants
    elif tokens and tokens[0].startswith("الأ"):
        # e.g. الأول → الأول → keep أول (we want underlying without ال)
        tokens[0] = tokens[0][2:]
    elif tokens and tokens[0].startswith("الآ"):
        # e.g. الآخر
        tokens[0] = tokens[0][2:]
    elif tokens and tokens[0].startswith("الإ"):
        tokens[0] = tokens[0][2:]
    return " ".join(tokens)


# ------------------------------------------------------------------------
# Verification + IO
# ------------------------------------------------------------------------

def verify_sha() -> None:
    actual = hashlib.sha256(PREREG.read_bytes()).hexdigest()
    if actual != EXPECTED_SHA:
        sys.exit(f"PRE-REG SHA MISMATCH:\n  expected={EXPECTED_SHA}\n  actual  ={actual}")
    print(f"pre-reg SHA verified: {EXPECTED_SHA[:16]}...")


def load_names() -> list[str]:
    names: list[str] = []
    for raw in NAMES_PATH.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        names.append(normalize_ws(line))
    return names


def load_corpus(path: Path):
    """Return list of (surah_id, ayah_id, text_normalized_whitespace).
    For full-tashkeel path, we also pre-compute rasm-skeleton version.
    """
    data = json.loads(path.read_text(encoding="utf-8"))
    out = []
    for surah in data:
        sid = surah["id"]
        for v in surah["verses"]:
            ayah = v["id"]
            text = normalize_ws(v["text"])
            out.append((sid, ayah, text))
    return out


# ------------------------------------------------------------------------
# Variant detection
# ------------------------------------------------------------------------

def detect_variant_A(name: str, verses_nt) -> dict:
    """Strict substring with ال in no-tashkeel."""
    matches = []
    total = 0
    for sid, ayah, text in verses_nt:
        c = text.count(name)
        if c > 0:
            matches.append((sid, ayah, c))
            total += c
    return {
        "rule": "A: strict substring with ال (no-tashkeel)",
        "query": name,
        "present": total > 0,
        "total_count": total,
        "n_verses": len(matches),
        "n_surahs": len({m[0] for m in matches}),
        "first": matches[0][:2] if matches else None,
    }


def detect_variant_B(name: str, verses_nt) -> dict:
    """Substring without leading ال in no-tashkeel.
    Slightly stricter than naive: require the variant be preceded by whitespace or word-start
    OR be a clean affix (we use a softer rule: appears as a substring anywhere — same as A
    but with the stripped query — this matches verbal/participial forms that include the root.)
    """
    q = strip_al_prefix(name)
    if not q or q == name:
        # Could not strip (e.g. ذو, الله with no clean ال-prefix). Skip variant B distinctness.
        return {
            "rule": "B: substring without ال (no-tashkeel)",
            "query": q,
            "present": None,
            "total_count": 0,
            "n_verses": 0,
            "n_surahs": 0,
            "first": None,
            "note": "no ال prefix to strip; identical to Variant A",
        }
    matches = []
    total = 0
    for sid, ayah, text in verses_nt:
        c = text.count(q)
        if c > 0:
            matches.append((sid, ayah, c))
            total += c
    return {
        "rule": "B: substring without ال (no-tashkeel)",
        "query": q,
        "present": total > 0,
        "total_count": total,
        "n_verses": len(matches),
        "n_surahs": len({m[0] for m in matches}),
        "first": matches[0][:2] if matches else None,
    }


def detect_variant_C(name: str, verses_nt) -> dict:
    """Triliteral consonantal root substring in no-tashkeel.
    Over-permissive: counts any word containing the root letters in order.
    """
    root = NAME_TO_ROOT.get(name)
    if root is None:
        return {
            "rule": "C: consonantal-root substring (no-tashkeel)",
            "query": None,
            "present": None,
            "total_count": 0,
            "n_verses": 0,
            "n_surahs": 0,
            "first": None,
            "note": "no locked root in NAME_TO_ROOT",
        }
    # Use the root letters as a non-contiguous in-order match within a single word.
    # For empirical simplicity & stability, use simple substring match of the root letters as a unit;
    # this is the project's standard "root substring" rule (see h-new-1560.py + cross-finding-025).
    matches = []
    total = 0
    for sid, ayah, text in verses_nt:
        c = text.count(root)
        if c > 0:
            matches.append((sid, ayah, c))
            total += c
    return {
        "rule": "C: consonantal-root substring (no-tashkeel)",
        "query": root,
        "present": total > 0,
        "total_count": total,
        "n_verses": len(matches),
        "n_surahs": len({m[0] for m in matches}),
        "first": matches[0][:2] if matches else None,
    }


def detect_variant_D(name: str, verses_ft_rasm) -> dict:
    """Rasm-skeleton substring matching against full-tashkeel corpus (normalized to rasm).
    For names that fail Variant A under rasm-orthographic mismatch, this rehabilitates.
    """
    q = to_rasm(name)
    matches = []
    total = 0
    for sid, ayah, text in verses_ft_rasm:
        c = text.count(q)
        if c > 0:
            matches.append((sid, ayah, c))
            total += c
    return {
        "rule": "D: rasm-skeleton substring (full-tashkeel)",
        "query": q,
        "present": total > 0,
        "total_count": total,
        "n_verses": len(matches),
        "n_surahs": len({m[0] for m in matches}),
        "first": matches[0][:2] if matches else None,
    }


# ------------------------------------------------------------------------
# Main
# ------------------------------------------------------------------------

def main() -> None:
    verify_sha()

    names = load_names()
    print(f"loaded {len(names)} names")
    assert len(names) == 99, f"expected 99 names, got {len(names)}"

    # Verify NAME_TO_ROOT covers all 99
    missing = [n for n in names if n not in NAME_TO_ROOT]
    if missing:
        sys.exit(f"NAME_TO_ROOT missing entries for: {missing}")

    verses_nt = load_corpus(QURAN_NT)
    print(f"loaded {len(verses_nt)} verses (no-tashkeel)")
    verses_ft_raw = load_corpus(QURAN_FT)
    print(f"loaded {len(verses_ft_raw)} verses (full-tashkeel)")
    verses_ft_rasm = [(sid, ayah, to_rasm(text)) for sid, ayah, text in verses_ft_raw]
    print(f"computed rasm-skeleton normalization on full-tashkeel verses")

    per_name = []
    for i, name in enumerate(names, 1):
        a = detect_variant_A(name, verses_nt)
        b = detect_variant_B(name, verses_nt)
        c = detect_variant_C(name, verses_nt)
        d = detect_variant_D(name, verses_ft_rasm)

        # Status tagging
        a_ok = a["present"] is True
        b_ok = b["present"] is True
        c_ok = c["present"] is True
        d_ok = d["present"] is True

        # If B "present" was None (no ال to strip), treat as inherits A
        if b["present"] is None:
            b_ok = a_ok

        if a_ok and b_ok and c_ok and d_ok:
            status = "ALL-FOUR"
        elif a_ok:
            status = "A-OK"
        elif b_ok:
            status = "REHAB-B"
        elif c_ok:
            status = "REHAB-C"
        elif d_ok:
            status = "REHAB-D"
        else:
            status = "IRRECOVERABLE"

        per_name.append({
            "idx": i,
            "name": name,
            "root": NAME_TO_ROOT[name],
            "variant_A": a,
            "variant_B": b,
            "variant_C": c,
            "variant_D": d,
            "A_present": a_ok,
            "B_present": b_ok,
            "C_present": c_ok,
            "D_present": d_ok,
            "status": status,
        })

    # Summary counts
    n_A_present = sum(1 for r in per_name if r["A_present"])
    n_A_absent = 99 - n_A_present
    n_B_present = sum(1 for r in per_name if r["B_present"])
    n_C_present = sum(1 for r in per_name if r["C_present"])
    n_D_present = sum(1 for r in per_name if r["D_present"])

    # Of the A-absent set, count rehabilitations
    a_absent_names = [r for r in per_name if not r["A_present"]]
    n_a_absent = len(a_absent_names)
    rehab_B = [r for r in a_absent_names if r["B_present"]]
    rehab_C = [r for r in a_absent_names if r["C_present"]]
    rehab_D = [r for r in a_absent_names if r["D_present"]]
    rehab_any = [r for r in a_absent_names if r["B_present"] or r["C_present"] or r["D_present"]]
    irrecoverable = [r for r in a_absent_names if not (r["B_present"] or r["C_present"] or r["D_present"])]

    summary = {
        "n_names_total": 99,
        "n_A_present": n_A_present,
        "n_A_absent": n_A_absent,
        "n_B_present": n_B_present,
        "n_C_present": n_C_present,
        "n_D_present": n_D_present,
        "n_a_absent": n_a_absent,
        "n_rehab_B_of_a_absent": len(rehab_B),
        "n_rehab_C_of_a_absent": len(rehab_C),
        "n_rehab_D_of_a_absent": len(rehab_D),
        "n_rehab_any_of_a_absent": len(rehab_any),
        "n_irrecoverable": len(irrecoverable),
        "rehab_B_names": [(r["idx"], r["name"]) for r in rehab_B],
        "rehab_C_names": [(r["idx"], r["name"]) for r in rehab_C],
        "rehab_D_names": [(r["idx"], r["name"]) for r in rehab_D],
        "rehab_any_names": [(r["idx"], r["name"], r["status"]) for r in rehab_any],
        "irrecoverable_names": [(r["idx"], r["name"], r["root"]) for r in irrecoverable],
    }

    # Hypothesis decisions
    h1_decision = "PASS" if len(rehab_any) >= 10 else "NULL"
    h2_decision = "PASS" if len(irrecoverable) >= 1 else "NULL"

    summary["h1_rehab_threshold"] = 10
    summary["h1_observed"] = len(rehab_any)
    summary["h1_decision"] = h1_decision
    summary["h2_threshold"] = 1
    summary["h2_observed"] = len(irrecoverable)
    summary["h2_decision"] = h2_decision

    out = {
        "finding_id": "H-NEW-1800",
        "title": "99 asmāʾ al-ḥusnā complete enumeration + alternative-orthography rehabilitation audit",
        "prereg_sha256": EXPECTED_SHA,
        "seed": SEED,
        "n_names": 99,
        "name_source": "data/asma-al-husna.txt (al-Tirmidhī #3507, al-Walīd b. Muslim chain)",
        "summary": summary,
        "per_name": per_name,
    }

    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(json.dumps(out, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\n=== H-NEW-1800 SUMMARY ===")
    print(f"  99 names total")
    print(f"  Variant A (strict +ال, no-tashkeel) present: {n_A_present} ({n_A_present/99*100:.1f}%) absent: {n_A_absent}")
    print(f"  Variant B (-ال, no-tashkeel)      present: {n_B_present}")
    print(f"  Variant C (root substring)        present: {n_C_present}")
    print(f"  Variant D (rasm-skeleton, full-tashkeel) present: {n_D_present}")
    print(f"  Of {n_a_absent} A-absent:")
    print(f"    rehab via B: {len(rehab_B)}")
    print(f"    rehab via C: {len(rehab_C)}")
    print(f"    rehab via D: {len(rehab_D)}")
    print(f"    rehab via any: {len(rehab_any)}")
    print(f"    IRRECOVERABLE: {len(irrecoverable)}")
    print(f"  H1 (rehab ≥ 10): {h1_decision} ({len(rehab_any)} ≥ 10)")
    print(f"  H2 (irrecoverable ≥ 1): {h2_decision} ({len(irrecoverable)} ≥ 1)")
    print(f"\n  Irrecoverable names:")
    for idx, name, root in summary["irrecoverable_names"]:
        print(f"    #{idx:>3}  {name:<20}  root={root}")
    print(f"\noutput written to: {OUT_PATH}")


if __name__ == "__main__":
    main()
