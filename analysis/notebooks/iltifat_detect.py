#!/usr/bin/env python3
"""
Iltifāt (الالتفات) — Quranic rhetorical person-shift — detector.

Classical balagha treats iltifāt as the signature Quranic rhetorical move:
a sudden grammatical shift of person (3→2→1), number (sg→pl), or addressee
mid-sentence or mid-passage. Al-Zarkashī's al-Burhān has a full chapter on it.
This script operationalises it computationally over the Leeds Quranic Arabic
Corpus (QAC v0.4) morphology.

Approach
--------
For every morphological segment we extract any PERSON-NUMBER-GENDER (PNG)
feature from the FEATURES field:

  verbs:         ... |1S, |1P, |2MS, |2FS, |2MP, |2FP, |3MS, |3FS, |3MP, |3FP
  pronouns/sfx:  ... PRON:1S, PRON:1P, PRON:2MS ... PRON:3FP

For every VERSE we then compute:
  - the SET of PNG codes present
  - the MULTISET of PNG codes present (with counts)
  - a "primary person" bucket: 1 / 2 / 3 / NA
    (chosen by rules below to represent the verse's dominant voice)

Iltifāt detection operates at two scales:
  1. Intra-verse: how many distinct PERSON-classes are inside a single verse?
     A verse with both 1P and 2MP is a candidate intra-verse iltifāt; a verse
     with 3MS → 2MS is the classical Al-Fatiha pattern.
  2. Inter-verse: a shift in primary-person between adjacent verses of the
     same surah.

Not every person change is real iltifāt. We filter:
  - 3-person references to OTHER entities (e.g. "the hypocrites... they said
    to them") don't count as iltifāt toward the audience.
  - Single-surah continuous quoted speech ("Pharaoh said: 'I am your lord'")
    needs to be discounted because 1S inside a quote is Pharaoh, not God.
    We cannot fully resolve speaker without deeper parsing, so we report
    RAW shifts and mark verses where the Sahih translation contains
    "said"/"say" so the reader can discount quoted-speech cases.

Scoring
-------
For each verse we compute the primary-person transition from verse-1 to
verse. A transition (p_prev -> p_curr) with p_prev != p_curr and both in
{1,2,3} is counted as an inter-verse iltifāt boundary, with TYPE labelled
by the transition direction (e.g. "3->2" is the Al-Fatiha pattern, "1->2"
is the divine-we-addressing-audience pattern, "3->1" is the narrative-to-
self-reference pattern).

Intra-verse iltifāt is counted when a verse contains verbs/pronouns
tagged with at least TWO distinct person-classes from {1,2,3}
(ignoring the "3rd-person-referent" noise: if the verse only has ONE
3rd-person subject that is the referent being talked about, we still
count it as 3, but combining 3 with either 1 or 2 is a real shift).

Outputs
-------
- findings/phase-b-hypotheses/iltifat-per-verse.csv
    one row per ayah with:
    surah, ayah, primary_person, person_set, png_multiset,
    intra_verse_iltifat_flag, inter_verse_iltifat_flag, transition_label,
    quote_marker (whether Sahih contains 'said'/'say'/'will say'),
    person_switches_within_verse (count),
    verse_topic_hint (lightweight topic tag from English)
- findings/phase-b-hypotheses/iltifat-density-by-surah.csv
    surah-level aggregate counts & densities
- findings/phase-b-hypotheses/iltifat-catalog.md
    prose write-up (separate, written by hand referring to this output)
- analysis/notebooks/iltifat_results.json
    full machine-readable dump for the catalog writer
"""
import csv
import json
import os
import re
from collections import Counter, defaultdict

ROOT = "/Users/grey/Downloads/quran"
MORPH = os.path.join(ROOT, "data/morphology/quranic-corpus-morphology-0.4.txt")
QURAN_JSON = os.path.join(ROOT, "quran-text/quran-no-tashkeel.json")
SAHIH = os.path.join(ROOT, "data/translations/en.sahih.txt")
HAFS = os.path.join(ROOT, "data/hafs-verse-counts.tsv")

OUT_PER_VERSE = os.path.join(ROOT, "findings/phase-b-hypotheses/iltifat-per-verse.csv")
OUT_BY_SURAH = os.path.join(ROOT, "findings/phase-b-hypotheses/iltifat-density-by-surah.csv")
OUT_JSON = os.path.join(ROOT, "analysis/notebooks/iltifat_results.json")

# ---------------------------------------------------------------------------
# Step 1: parse morphology, collect per-verse PNG multisets
# ---------------------------------------------------------------------------

# PNG tag regex — matches verb features like |1S or |3MP or |2FP, and
# pronoun features like PRON:3MP or 2MS (for STEM pronouns the PNG is
# just the last pipe-segment).
PNG_CODES = {"1S", "1P", "2MS", "2FS", "2MP", "2FP", "2D", "2MD", "2FD",
             "3MS", "3FS", "3MP", "3FP", "3D", "3MD", "3FD"}

VERB_PNG_RE = re.compile(r"\|(1S|1P|2MS|2FS|2MP|2FP|2MD|2FD|2D|3MS|3FS|3MP|3FP|3MD|3FD|3D)(?:\||$)")
PRON_PNG_RE = re.compile(r"(?:PRON:)(1S|1P|2MS|2FS|2MP|2FP|2MD|2FD|2D|3MS|3FS|3MP|3FP|3MD|3FD|3D)")
LOCATION_RE = re.compile(r"\((\d+):(\d+):(\d+):(\d+)\)")

# verses[(surah, ayah)] = list of (role_tag, png_code)
# role_tag in {"V_IMPF","V_PERF","V_IMPV","V_PASS","PRON","PRON_SUFFIX"}
verse_tokens = defaultdict(list)
# any morphology rows at all (nominal or otherwise)
verse_row_counts = Counter()
# whether the verse has any verb at all
verse_has_verb = defaultdict(bool)

with open(MORPH, "r", encoding="utf-8") as f:
    for line in f:
        if not line or line.startswith("#") or line.startswith("LOCATION"):
            continue
        parts = line.rstrip("\n").split("\t")
        if len(parts) < 4:
            continue
        loc, form, tag, feats = parts[0], parts[1], parts[2], parts[3]
        m = LOCATION_RE.match(loc)
        if not m:
            continue
        s = int(m.group(1))
        a = int(m.group(2))
        verse_row_counts[(s, a)] += 1
        if tag == "V":
            verse_has_verb[(s, a)] = True

        # Pull PNG tag
        if tag == "V":
            # verbs: look inside FEATURES for |XY$
            mm = VERB_PNG_RE.search(feats)
            if mm:
                png = mm.group(1)
                # verb form hint: IMPF (imperfect) / PERF / IMPV (imperative) / PASS
                form_tag = "V"
                if "|IMPF|" in feats or feats.endswith("|IMPF"):
                    form_tag = "V_IMPF"
                elif "|PERF|" in feats or feats.endswith("|PERF") or "|PERF|" in feats:
                    form_tag = "V_PERF"
                elif "|IMPV|" in feats or feats.endswith("|IMPV"):
                    form_tag = "V_IMPV"
                if "|PASS|" in feats:
                    form_tag += "_PASS"
                verse_tokens[(s, a)].append((form_tag, png))
        elif tag == "PRON":
            mm = PRON_PNG_RE.search(feats)
            role = "PRON_SUFFIX" if feats.startswith("SUFFIX") else "PRON"
            if mm:
                verse_tokens[(s, a)].append((role, mm.group(1)))
            else:
                # Some STEM pronouns: POS:PRON|3MP
                mm2 = re.search(r"\|(1S|1P|2MS|2FS|2MP|2FP|2MD|2FD|2D|3MS|3FS|3MP|3FP|3MD|3FD|3D)\b", feats)
                if mm2:
                    verse_tokens[(s, a)].append((role, mm2.group(1)))

# sanity
print(f"[parse] verses with any PNG tag: {len(verse_tokens)}")

# ---------------------------------------------------------------------------
# Step 2: per-verse PNG analysis
# ---------------------------------------------------------------------------

def person_class(code):
    """1 / 2 / 3 / None."""
    if code[0] == "1":
        return 1
    if code[0] == "2":
        return 2
    if code[0] == "3":
        return 3
    return None

# Decide primary person for a verse.
# Rule:
#   - Count VERB person classes with weight 2 (verbs carry the voice)
#   - Count PRONOUN person classes with weight 1
#   - Among classes, prefer the class that has the MOST weight.
#   - Tie-break: prefer 2 > 1 > 3 (because 2 is always rhetorical address,
#     1 is rarer, 3 is the default narrative voice — so 3 is the "least
#     marked" and should only win when it dominates).
#   - If no PNG tags at all, primary = None (nominal verse, e.g. "wa-mā adrāka").

def primary_person_for_verse(tokens):
    weight = Counter()
    for role, png in tokens:
        pc = person_class(png)
        if pc is None:
            continue
        w = 2 if role.startswith("V") else 1
        weight[pc] += w
    if not weight:
        return None, weight
    # tiebreak order 2,1,3 means we add a tiny epsilon
    boost = {2: 0.03, 1: 0.02, 3: 0.01}
    best = max(weight.items(), key=lambda kv: (kv[1] + boost[kv[0]]))
    return best[0], weight


def implicit_primary(rec):
    """Return an implicit-3 if this verse is nominal-only (morph rows
    exist but no PNG tags). Nominal verses in the Quran almost always
    describe a 3rd-person entity ('Master of the Day of Judgment'), so
    treat them as implicit-3rd for the purpose of inter-verse shift
    detection. Returns None if there are no morphology rows at all
    (e.g. pure muqatta'at like Alif-Lam-Meem)."""
    if rec["primary"] is not None:
        return rec["primary"]
    if rec["morph_rows"] == 0:
        return None
    return 3  # nominal-descriptive verse -> implicit 3rd person

# Per-verse record

# Read Sahih for quote / topic hints
sahih_lines = []
with open(SAHIH, "r", encoding="utf-8") as f:
    for line in f:
        line = line.rstrip("\n")
        if line.startswith("#") or not line:
            break
        sahih_lines.append(line)
assert len(sahih_lines) == 6236, f"Sahih line count: {len(sahih_lines)}"

# Read Hafs verse counts -> build ordered (surah,ayah) list
hafs = {}
with open(HAFS, "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split("\t")
        if len(parts) == 2:
            hafs[int(parts[0])] = int(parts[1])

ordered_keys = []
for s in range(1, 115):
    for a in range(1, hafs[s] + 1):
        ordered_keys.append((s, a))
assert len(ordered_keys) == 6236

# Build translation lookup
trans = {k: t for k, t in zip(ordered_keys, sahih_lines)}

# --- Topic hint lexicon (very lightweight, for task 8) ---
TOPIC_LEX = {
    "oneness":  re.compile(r"\b(no deity|other than Him|oneness|except Him|one God|associates|idol|partners)\b", re.I),
    "judgment": re.compile(r"\b(Hour|Day of|Judgment|Reckoning|Recompense|Hell|Fire|Paradise|Resurrect|punishment|torment|reward)\b", re.I),
    "mercy":    re.compile(r"\b(mercy|Merciful|forgive|forgiving|gentle|compassion|kind)\b", re.I),
    "revelation": re.compile(r"\b(revealed|revelation|Book|Scripture|Quran|Messenger|send down|sent down|recite|signs|ayat|warner)\b", re.I),
    "creation": re.compile(r"\b(created|create|heavens|earth|created the|stars|sun|moon|sky)\b", re.I),
    "law":      re.compile(r"\b(inherit|divorce|witness|alms|zakah|contract|debt|lawful|unlawful|forbidden|prescribed|interest|usury)\b", re.I),
    "prayer":   re.compile(r"\b(prayer|fast|pilgrimage|hajj|prostrate|bow|ablution|fast)\b", re.I),
    "prophets": re.compile(r"\b(Moses|Musa|Abraham|Ibrahim|Jesus|Isa|Noah|Nuh|David|Solomon|Lot|Salih|Hud|Shuaib|Job|Jonah|Yunus|Yusuf|Joseph|Ismail|Ishaq|Pharaoh|Thamud|Aad|Midian|Children of Israel)\b", re.I),
}
QUOTE_RE = re.compile(r"\b(said|Say,|say,|will say|say:|say ')\b")

def topics_for(text):
    hits = []
    for name, rx in TOPIC_LEX.items():
        if rx.search(text):
            hits.append(name)
    return hits

# --- Build per-verse record ---
per_verse = {}
for (s, a) in ordered_keys:
    toks = verse_tokens.get((s, a), [])
    png_multiset = Counter(png for _, png in toks)
    person_set = set()
    for png in png_multiset:
        pc = person_class(png)
        if pc is not None:
            person_set.add(pc)
    primary, weight = primary_person_for_verse(toks)

    # count how many verb-level person transitions appear when walking the
    # token list left-to-right (a crude "within-verse switch count")
    verb_seq = [person_class(png) for role, png in toks if role.startswith("V")]
    verb_seq = [x for x in verb_seq if x is not None]
    intra_switches = sum(1 for i in range(1, len(verb_seq)) if verb_seq[i] != verb_seq[i-1])

    text = trans[(s, a)]
    quote = bool(QUOTE_RE.search(text))

    per_verse[(s, a)] = dict(
        surah=s,
        ayah=a,
        tokens_total=len(toks),
        morph_rows=verse_row_counts[(s, a)],
        has_verb=verse_has_verb[(s, a)],
        png_multiset=dict(png_multiset),
        person_set=sorted(person_set),
        primary=primary,
        weight=dict(weight),
        intra_verb_switches=intra_switches,
        quote_marker=quote,
        topics=topics_for(text),
        text=text,
    )

# ---------------------------------------------------------------------------
# Step 3: iltifāt flags
# ---------------------------------------------------------------------------

# Intra-verse iltifāt flag rules:
# Level 0: verse has one person class or none -> no intra
# Level 1: verse has two person classes -> weak intra
# Level 2: verse has three person classes -> strong intra
# Additional subflag: if a verse has BOTH 1x and 2x (divine-I/we addressing
# audience), that's a "classical iltifāt" pattern.

def intra_flags(rec):
    ps = set(rec["person_set"])
    level = 0
    if len(ps) == 2:
        level = 1
    elif len(ps) >= 3:
        level = 2
    classical_1_2 = (1 in ps and 2 in ps)
    classical_3_2 = (3 in ps and 2 in ps)
    classical_3_1 = (3 in ps and 1 in ps)
    return dict(level=level,
                has_1=1 in ps, has_2=2 in ps, has_3=3 in ps,
                classical_1_2=classical_1_2,
                classical_3_2=classical_3_2,
                classical_3_1=classical_3_1)


def strict_intra_iltifat(rec, token_list):
    """Stricter rule: a true intra-verse iltifāt requires either
    (a) TWO distinct VERB persons, or
    (b) a verb of one person and an independent (STEM) pronoun of
        another person.
    Mere possessive suffix pronouns do NOT count — 'his Lord' inside a
    2MP-directed verse is not rhetorically iltifāt.
    """
    verb_persons = set()
    stem_pron_persons = set()
    for role, png in token_list:
        pc = person_class(png)
        if pc is None:
            continue
        if role.startswith("V"):
            verb_persons.add(pc)
        elif role == "PRON":  # independent stem pronoun
            stem_pron_persons.add(pc)
    if len(verb_persons) >= 2:
        return True, "two_verbs"
    if verb_persons and stem_pron_persons \
            and not (verb_persons <= stem_pron_persons and stem_pron_persons <= verb_persons):
        if verb_persons != stem_pron_persons and (verb_persons - stem_pron_persons or stem_pron_persons - verb_persons):
            return True, "verb_plus_indep_pron"
    return False, None

for k, rec in per_verse.items():
    rec["intra"] = intra_flags(rec)
    strict_flag, strict_reason = strict_intra_iltifat(rec, verse_tokens.get(k, []))
    rec["strict_intra"] = strict_flag
    rec["strict_reason"] = strict_reason or ""

# Inter-verse iltifāt: compare primary_person of adjacent verses within the
# same surah. A transition (p_prev -> p_curr) with both in {1,2,3} and
# p_prev != p_curr is an inter-verse shift. We label it as e.g. "3->2".

prev_primary = None
prev_had_verb = False
prev_surah = None
for (s, a) in ordered_keys:
    rec = per_verse[(s, a)]
    if s != prev_surah:
        prev_primary = None
        prev_had_verb = False
    curr = implicit_primary(rec)
    rec["effective_primary"] = curr
    transition = None
    is_shift = False
    strict_shift = False
    if prev_primary is not None and curr is not None and prev_primary != curr:
        transition = f"{prev_primary}->{curr}"
        is_shift = True
        # strict: at least one of the two verses must carry a verb with
        # explicit PNG; pure nominal-to-nominal shifts don't count as
        # rhetorical iltifāt.
        if rec["has_verb"] or prev_had_verb:
            strict_shift = True
    rec["inter_transition"] = transition
    rec["inter_shift"] = is_shift
    rec["inter_shift_strict"] = strict_shift
    if curr is not None:
        prev_primary = curr
    prev_had_verb = rec["has_verb"]
    prev_surah = s

# ---------------------------------------------------------------------------
# Step 4: per-surah density
# ---------------------------------------------------------------------------

surah_stats = {}
for s in range(1, 115):
    rows = [per_verse[(s, a)] for a in range(1, hafs[s] + 1)]
    N = len(rows)
    intra_any = sum(1 for r in rows if r["intra"]["level"] >= 1)
    intra_strong = sum(1 for r in rows if r["intra"]["level"] >= 2)
    intra_strict = sum(1 for r in rows if r["strict_intra"])
    classical_1_2 = sum(1 for r in rows if r["intra"]["classical_1_2"])
    classical_3_2 = sum(1 for r in rows if r["intra"]["classical_3_2"])
    classical_3_1 = sum(1 for r in rows if r["intra"]["classical_3_1"])
    inter_shifts = sum(1 for r in rows if r["inter_shift"])
    inter_strict = sum(1 for r in rows if r["inter_shift_strict"])
    # dominant primary person histogram
    prim_hist = Counter(r["primary"] for r in rows if r["primary"] is not None)
    total = intra_any + inter_shifts
    total_strict = intra_strict + inter_strict
    density = total / N if N > 0 else 0.0
    density_strict = total_strict / N if N > 0 else 0.0
    surah_stats[s] = dict(
        surah=s,
        N=N,
        intra_any=intra_any,
        intra_strong=intra_strong,
        intra_strict=intra_strict,
        classical_1_2=classical_1_2,
        classical_3_2=classical_3_2,
        classical_3_1=classical_3_1,
        inter_shifts=inter_shifts,
        inter_strict=inter_strict,
        total_iltifat=total,
        total_strict=total_strict,
        density=density,
        density_strict=density_strict,
        primary_hist=dict(prim_hist),
    )

# ---------------------------------------------------------------------------
# Step 5: rank surahs by density
# ---------------------------------------------------------------------------

# Filter out ultra-short surahs (N<6) for ranking fairness
ranked = sorted((st for st in surah_stats.values() if st["N"] >= 6),
                key=lambda r: r["density"],
                reverse=True)
ranked_strict = sorted((st for st in surah_stats.values() if st["N"] >= 6),
                       key=lambda r: r["density_strict"],
                       reverse=True)

print("\n[density ranking permissive] top 15 surahs by iltifāt density (intra+inter)/N:")
for r in ranked[:15]:
    print(f"  S{r['surah']:3d}  N={r['N']:4d}  intra={r['intra_any']:4d}  inter={r['inter_shifts']:4d}  density={r['density']:.3f}")
print("\n[density ranking permissive] bottom 10 — most stable surahs:")
for r in ranked[-10:]:
    print(f"  S{r['surah']:3d}  N={r['N']:4d}  intra={r['intra_any']:4d}  inter={r['inter_shifts']:4d}  density={r['density']:.3f}")

print("\n[density ranking STRICT] top 15 surahs by strict iltifāt density (strict_intra+strict_inter)/N:")
for r in ranked_strict[:15]:
    print(f"  S{r['surah']:3d}  N={r['N']:4d}  intra_strict={r['intra_strict']:4d}  inter_strict={r['inter_strict']:4d}  density_strict={r['density_strict']:.3f}")
print("\n[density ranking STRICT] bottom 10:")
for r in ranked_strict[-10:]:
    print(f"  S{r['surah']:3d}  N={r['N']:4d}  intra_strict={r['intra_strict']:4d}  inter_strict={r['inter_strict']:4d}  density_strict={r['density_strict']:.3f}")

# ---------------------------------------------------------------------------
# Step 6: known iltifāt ground-truth verses
# ---------------------------------------------------------------------------

GROUND_TRUTH = [
    (1, 4, "3MS→2MS: Master of Day... → You we worship (Al-Fatiha classical)"),
    (1, 5, "1P+2MS coexist (continuation of Al-Fatiha iltifat)"),
    (36, 22, "3→1: And why should I not worship... (Ya-Sin)"),
    (10, 22, "3→2: He it is who enables you to travel... until when you are in the ships"),
    (35, 9, "3MS+2MP pattern"),
    (1, 2, "control: praise belongs to Allah (3MS only, should NOT be flagged)"),
    (2, 21, "2MP imperative context"),
    (55, 13, "2D tukadhdhibān refrain (2-dual)"),
]
print("\n[ground truth check]")
for s, a, note in GROUND_TRUTH:
    if (s, a) not in per_verse:
        continue
    r = per_verse[(s, a)]
    print(f"  S{s}:{a}  primary={r['primary']}  person_set={r['person_set']}  "
          f"intra_level={r['intra']['level']}  transition={r['inter_transition']}  "
          f"-- {note}")

# ---------------------------------------------------------------------------
# Step 7: ring-center correlation
# ---------------------------------------------------------------------------
RINGS = [
    ("Al-Baqarah Abraham/qibla", 2, 131, 144),
    ("Al-Qamar Thamud", 54, 21, 30),
    ("'Abasa rebuke", 80, 1, 9),
    ("Al-Kahf Dhul-Qarnayn", 18, 83, 91),
]
print("\n[ring-center correlation]")
ring_report = []
for name, s, a0, a1 in RINGS:
    span_rows = [per_verse[(s, a)] for a in range(a0, a1 + 1)]
    intra = sum(1 for r in span_rows if r["intra"]["level"] >= 1)
    strict_i = sum(1 for r in span_rows if r["strict_intra"])
    strong = sum(1 for r in span_rows if r["intra"]["level"] >= 2)
    inter = sum(1 for r in span_rows if r["inter_shift"])
    strict_inter = sum(1 for r in span_rows if r["inter_shift_strict"])
    primaries = [r["effective_primary"] for r in span_rows]
    transitions = [(r["ayah"], r["inter_transition"]) for r in span_rows if r["inter_transition"]]
    N = len(span_rows)
    # surah baseline rate (strict)
    surah_strict_rate = surah_stats[s]["density_strict"]
    span_strict_density = (strict_i + strict_inter) / N
    ring_report.append(dict(
        name=name, surah=s, start=a0, end=a1, N=N,
        intra=intra, strict_intra=strict_i, strong=strong,
        inter=inter, strict_inter=strict_inter,
        density=(intra + inter) / N,
        density_strict=span_strict_density,
        surah_baseline_strict=surah_strict_rate,
        ratio_to_surah=(span_strict_density / surah_strict_rate) if surah_strict_rate > 0 else None,
        primaries=primaries,
        transitions=transitions,
    ))
    print(f"  {name}: N={N} intra={intra} (strict {strict_i}) "
          f"inter={inter} (strict {strict_inter}) "
          f"strict_density={span_strict_density:.3f} "
          f"vs surah_baseline_strict={surah_strict_rate:.3f}")
    print(f"    primaries={primaries}")
    print(f"    transitions={transitions}")

# ---------------------------------------------------------------------------
# Step 8: Maryam rhyme-break alignment
# ---------------------------------------------------------------------------
print("\n[Maryam Christological breaks]")
MARYAM_BREAKS = [(19, 34, 40, "Christological polemic 1"),
                 (19, 88, 93, "Christological polemic 2")]
maryam_report = []
maryam_baseline_strict = surah_stats[19]["density_strict"]
print(f"  Maryam strict baseline density = {maryam_baseline_strict:.3f}")
for s, a0, a1, label in MARYAM_BREAKS:
    span = [per_verse[(s, a)] for a in range(a0, a1 + 1)]
    intra = sum(1 for r in span if r["intra"]["level"] >= 1)
    strict_i = sum(1 for r in span if r["strict_intra"])
    inter = sum(1 for r in span if r["inter_shift"])
    strict_inter = sum(1 for r in span if r["inter_shift_strict"])
    primaries = [r["effective_primary"] for r in span]
    transitions = [(r["ayah"], r["inter_transition"]) for r in span if r["inter_transition"]]
    N = len(span)
    span_density = (strict_i + strict_inter) / N
    print(f"  S{s} v{a0}-{a1} ({label}): intra={intra} (strict {strict_i})  "
          f"inter={inter} (strict {strict_inter})  "
          f"strict_density={span_density:.3f} "
          f"vs Maryam baseline {maryam_baseline_strict:.3f}")
    print(f"    primaries={primaries}")
    print(f"    transitions={transitions}")
    maryam_report.append(dict(
        surah=s, start=a0, end=a1, label=label, N=N,
        intra=intra, strict_intra=strict_i,
        inter=inter, strict_inter=strict_inter,
        density_strict=span_density,
        maryam_baseline_strict=maryam_baseline_strict,
        primaries=primaries,
        transitions=transitions,
    ))

# ---------------------------------------------------------------------------
# Step 9: topic-coincidence for novel hypothesis
# ---------------------------------------------------------------------------
print("\n[topic correlation -- STRICT]")
topic_counts = Counter()
topic_strict_counts = Counter()
for k, rec in per_verse.items():
    has_strict = rec["strict_intra"] or rec["inter_shift_strict"]
    for t in rec["topics"]:
        topic_counts[t] += 1
        if has_strict:
            topic_strict_counts[t] += 1
base_rate_strict = sum(1 for r in per_verse.values() if r["strict_intra"] or r["inter_shift_strict"]) / len(per_verse)
print(f"  base rate of strict iltifāt (strict_intra OR strict_inter): {base_rate_strict:.3f}")
topic_rates = {}
for t in topic_counts:
    rate = topic_strict_counts[t] / topic_counts[t]
    lift = rate / base_rate_strict if base_rate_strict else 0
    topic_rates[t] = dict(n=topic_counts[t], iltifat=topic_strict_counts[t],
                           rate=round(rate, 4), lift=round(lift, 3))
    print(f"  {t:12s}  n={topic_counts[t]:5d}  iltifāt-rate={rate:.3f}  lift={lift:.2f}")

# ---------------------------------------------------------------------------
# Step 9b: permutation test for topic correlation
# ---------------------------------------------------------------------------
import random
print("\n[topic permutation test, 2000 trials]")
all_recs = list(per_verse.values())
strict_flags = [r["strict_intra"] or r["inter_shift_strict"] for r in all_recs]
total_iltifat = sum(strict_flags)
N_all = len(all_recs)
# count topic memberships
topic_membership = {t: [bool(t in r["topics"]) for r in all_recs] for t in TOPIC_LEX}

trials = 2000
rng = random.Random(2026)
topic_perm_p = {}
for t in TOPIC_LEX:
    n_t = sum(topic_membership[t])
    obs = sum(1 for r in all_recs if (t in r["topics"]) and (r["strict_intra"] or r["inter_shift_strict"]))
    if n_t == 0:
        continue
    # Null: shuffle the strict-iltifat assignment over verses, recount
    shuffled = strict_flags[:]
    geq = 0
    for trial in range(trials):
        rng.shuffle(shuffled)
        c = 0
        for i, m in enumerate(topic_membership[t]):
            if m and shuffled[i]:
                c += 1
        if c >= obs:
            geq += 1
    p = geq / trials
    topic_perm_p[t] = p
    print(f"  {t:12s}  obs={obs:5d} of n={n_t:5d}  p_perm={p:.4f}")

# ---------------------------------------------------------------------------
# Step 10: write CSVs and JSON
# ---------------------------------------------------------------------------
with open(OUT_PER_VERSE, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow([
        "surah", "ayah", "primary_person", "effective_primary",
        "person_set", "png_multiset",
        "intra_level", "intra_strict", "strict_reason",
        "intra_has_1", "intra_has_2", "intra_has_3",
        "classical_1_2", "classical_3_2", "classical_3_1",
        "inter_shift", "inter_shift_strict", "inter_transition",
        "intra_verb_switches",
        "quote_marker", "topics",
        "tokens_total", "morph_rows", "has_verb",
    ])
    for (s, a) in ordered_keys:
        r = per_verse[(s, a)]
        w.writerow([
            s, a,
            r["primary"] if r["primary"] else "",
            r["effective_primary"] if r["effective_primary"] else "",
            ",".join(str(x) for x in r["person_set"]),
            ";".join(f"{k}:{v}" for k, v in sorted(r["png_multiset"].items())),
            r["intra"]["level"],
            int(r["strict_intra"]),
            r["strict_reason"],
            int(r["intra"]["has_1"]), int(r["intra"]["has_2"]), int(r["intra"]["has_3"]),
            int(r["intra"]["classical_1_2"]),
            int(r["intra"]["classical_3_2"]),
            int(r["intra"]["classical_3_1"]),
            int(r["inter_shift"]),
            int(r["inter_shift_strict"]),
            r["inter_transition"] or "",
            r["intra_verb_switches"],
            int(r["quote_marker"]),
            ",".join(r["topics"]),
            r["tokens_total"], r["morph_rows"], int(r["has_verb"]),
        ])

with open(OUT_BY_SURAH, "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["surah", "N", "intra_any", "intra_strong", "intra_strict",
                "classical_1_2", "classical_3_2", "classical_3_1",
                "inter_shifts", "inter_strict",
                "total_iltifat", "total_strict",
                "density", "density_strict",
                "primary_hist"])
    for s in range(1, 115):
        st = surah_stats[s]
        w.writerow([
            s, st["N"], st["intra_any"], st["intra_strong"], st["intra_strict"],
            st["classical_1_2"], st["classical_3_2"], st["classical_3_1"],
            st["inter_shifts"], st["inter_strict"],
            st["total_iltifat"], st["total_strict"],
            f"{st['density']:.4f}", f"{st['density_strict']:.4f}",
            json.dumps(st["primary_hist"]),
        ])

with open(OUT_JSON, "w", encoding="utf-8") as f:
    out = dict(
        ranked_density=[dict(r) for r in ranked[:30]],
        bottom_density=[dict(r) for r in ranked[-10:]],
        ranked_density_strict=[dict(r) for r in ranked_strict[:30]],
        bottom_density_strict=[dict(r) for r in ranked_strict[-10:]],
        ring_report=ring_report,
        maryam_report=maryam_report,
        topic_rates=topic_rates,
        topic_permutation_p=topic_perm_p,
        base_rate_strict=base_rate_strict,
        surah_stats={str(k): v for k, v in surah_stats.items()},
    )
    json.dump(out, f, ensure_ascii=False, indent=2)

print(f"\n[write] {OUT_PER_VERSE}")
print(f"[write] {OUT_BY_SURAH}")
print(f"[write] {OUT_JSON}")
print("[done]")
