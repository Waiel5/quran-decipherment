#!/usr/bin/env python3
"""Task #72 — T-004 Muʿallaqāt positive control for H-NEW-23 sub-3.

Methodology mirrors scripts/h_new_23_hapax_slot_mechanism.py sub-test 3:
  For each hapax (single-occurrence surface word), compare observed
  verse-final-slot rate vs expected-under-uniform-within-verse.
  z = (f_obs - sum(1/vl)) / sqrt(sum((1/vl)(1-1/vl)))

Positive control question: does the monorhyme of classical qaṣīda
MECHANICALLY force single-occurrence surface words into the verse-final
slot at z-magnitude comparable to the Quran?

If YES → H-NEW-23 sub-3 effect is register-wide classical Arabic.
If NO  → H-NEW-23 sub-3 signature is distinctive to the Quran.

Hapax granularity: we don't have a QAC-style root parse for qaṣīda text.
We use two alternative hapax definitions:
  (a) surface-form hapax (orthographic token w/ diacritics stripped, exact match)
  (b) orthographic hapax on rasm-only (alif-variants normalized)

Verse-length robustness panel: vl ≥ 3, ≥ 5, ≥ 10 (match H-NEW-23 spec).

Seed 20260413.
"""
import json, math, re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
RAW = ROOT / 'data/baseline-corpora/raw'

MUALLAQAT = [
    ('imru-al-qais', 'muallaqa-imru-al-qais.txt'),
    ('tarafa',       'muallaqa-tarafa.txt'),
    ('zuhayr',       'muallaqa-zuhayr.txt'),
    ('labid',        'muallaqa-labid.txt'),
    ('antara',       'muallaqa-antara.txt'),
    ('amr-bin-kulthum','muallaqa-amr-bin-kulthum.txt'),
    ('harith',       'muallaqa-harith.txt'),
]

# Strip Arabic diacritics
DIAC_RE = re.compile(r'[\u064B-\u065F\u0670\u06D6-\u06ED]')
def strip_diac(s):
    return DIAC_RE.sub('', s)

# Rasm normalize: ا/أ/إ/آ → ا ; ى → ي ; ة → ه ; remove punctuation
RASM_TABLE = str.maketrans({
    'أ': 'ا', 'إ': 'ا', 'آ': 'ا',
    'ى': 'ي',
    'ة': 'ه',
})
PUNCT_RE = re.compile(r'[،؛؟!:.()\[\]،؛"\'/\\—–\-…]')
def rasm(s):
    s = strip_diac(s)
    s = PUNCT_RE.sub(' ', s)
    s = s.translate(RASM_TABLE)
    return s

def load_verses(filename):
    """Each line = one bayt. Returns list of (verse_idx, [words_surface_diac_stripped])."""
    path = RAW / filename
    verses = []
    for i, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
        line = line.strip()
        if not line:
            continue
        # Strip diacritics, normalize whitespace, remove punctuation
        clean = strip_diac(line)
        clean = PUNCT_RE.sub(' ', clean)
        words = [w for w in clean.split() if w]
        if words:
            verses.append((i, words))
    return verses

def analyze(muallaqa_name, verses, use_rasm=False, vl_min=3):
    """For each hapax surface-form, test verse-final-slot vs uniform null."""
    normalize = rasm if use_rasm else strip_diac

    # Filter verses by min length
    verses = [(v, ws) for v, ws in verses if len(ws) >= vl_min]
    if not verses:
        return None

    # Build word corpus
    all_word_locs = []  # (verse_idx, word_pos_1indexed, verse_length, normalized_form)
    for vidx, ws in verses:
        vl = len(ws)
        for wpos, w in enumerate(ws, 1):
            form = normalize(w).strip()
            if not form:
                continue
            all_word_locs.append((vidx, wpos, vl, form))

    # Count occurrences
    form_counts = Counter(loc[3] for loc in all_word_locs)
    hapax_locs = [loc for loc in all_word_locs if form_counts[loc[3]] == 1]

    n_hap = len(hapax_locs)
    if n_hap == 0:
        return None

    f_obs = sum(1 for _, wpos, vl, _ in hapax_locs if wpos == vl)
    f_exp = sum(1.0/vl for _, _, vl, _ in hapax_locs)
    f_var = sum((1.0/vl)*(1-1.0/vl) for _, _, vl, _ in hapax_locs)
    f_sd = math.sqrt(f_var) if f_var > 0 else 0
    z = (f_obs - f_exp) / f_sd if f_sd > 0 else 0
    p_one = 0.5 * (1 - math.erf(z/math.sqrt(2))) if z > 0 else 1 - 0.5*(1 - math.erf(-z/math.sqrt(2)))

    return {
        'muallaqa': muallaqa_name,
        'use_rasm': use_rasm,
        'vl_min': vl_min,
        'n_verses': len(verses),
        'n_word_tokens': len(all_word_locs),
        'n_distinct_forms': len(form_counts),
        'n_hapaxes': n_hap,
        'hapax_final_observed': f_obs,
        'hapax_final_expected_uniform': f_exp,
        'expected_sd': f_sd,
        'z': z,
        'p_one_sided': p_one,
    }

def pooled_analyze(all_verses_labeled, use_rasm=False, vl_min=3):
    """Pool all 7 muʿallaqāt, recompute hapax across the pooled corpus."""
    normalize = rasm if use_rasm else strip_diac
    # Pool with unique verse ids (name + verse_idx)
    all_locs = []
    pooled_verses = []
    for name, verses in all_verses_labeled:
        for vidx, ws in verses:
            if len(ws) < vl_min:
                continue
            vl = len(ws)
            pooled_verses.append((name, vidx, vl))
            for wpos, w in enumerate(ws, 1):
                form = normalize(w).strip()
                if not form:
                    continue
                all_locs.append((name, vidx, wpos, vl, form))

    form_counts = Counter(loc[4] for loc in all_locs)
    hapax_locs = [loc for loc in all_locs if form_counts[loc[4]] == 1]
    n_hap = len(hapax_locs)
    if n_hap == 0:
        return None

    f_obs = sum(1 for _, _, wpos, vl, _ in hapax_locs if wpos == vl)
    f_exp = sum(1.0/vl for _, _, _, vl, _ in hapax_locs)
    f_var = sum((1.0/vl)*(1-1.0/vl) for _, _, _, vl, _ in hapax_locs)
    f_sd = math.sqrt(f_var) if f_var > 0 else 0
    z = (f_obs - f_exp) / f_sd if f_sd > 0 else 0
    p_one = 0.5 * (1 - math.erf(z/math.sqrt(2))) if z > 0 else 1 - 0.5*(1 - math.erf(-z/math.sqrt(2)))

    return {
        'scope': 'pooled_7_muallaqat',
        'use_rasm': use_rasm,
        'vl_min': vl_min,
        'n_verses': len(pooled_verses),
        'n_word_tokens': len(all_locs),
        'n_distinct_forms': len(form_counts),
        'n_hapaxes': n_hap,
        'hapax_final_observed': f_obs,
        'hapax_final_expected_uniform': f_exp,
        'expected_sd': f_sd,
        'z': z,
        'p_one_sided': p_one,
    }

# -------- Main --------
all_verses = []
per_muallaqa_results = {}

for name, fn in MUALLAQAT:
    verses = load_verses(fn)
    all_verses.append((name, verses))
    per_muallaqa_results[name] = {
        'n_verses_raw': len(verses),
    }

# Per-muallaqa panel × 2 normalization × 3 vl
per_panel = {}
for name, verses in all_verses:
    per_panel[name] = {}
    for use_rasm in (False, True):
        for vl_min in (3, 5, 10):
            key = f"{'rasm' if use_rasm else 'diac-stripped'}_vl{vl_min}"
            res = analyze(name, verses, use_rasm=use_rasm, vl_min=vl_min)
            per_panel[name][key] = res

# Pooled panel
pooled_panel = {}
for use_rasm in (False, True):
    for vl_min in (3, 5, 10):
        key = f"{'rasm' if use_rasm else 'diac-stripped'}_vl{vl_min}"
        pooled_panel[key] = pooled_analyze(all_verses, use_rasm=use_rasm, vl_min=vl_min)

# --- Compare to Quran H-NEW-23 sub-3 ---
quran_sub3 = json.loads((ROOT / 'findings/phase-b-hypotheses/csv/h-new-23-hapax-slot.json').read_text())
quran_z = quran_sub3['sub3_within_verse_slot_CRITICAL']['z']
quran_p = quran_sub3['sub3_within_verse_slot_CRITICAL']['p_one_sided']
quran_n = quran_sub3['sub3_within_verse_slot_CRITICAL']['n_hapax']

out = {
    'task_id': 72,
    'test_name': 'T-004 Muʿallaqāt positive-control for H-NEW-23 sub-3',
    'seed': 20260413,
    'quran_reference_sub3': {
        'n_hapax': quran_n, 'z': quran_z, 'p_one_sided': quran_p,
    },
    'per_muallaqa': per_panel,
    'pooled_7_muallaqat': pooled_panel,
    'methodology_notes': {
        'hapax_granularity': 'surface-form (no root parse available for Muʿallaqāt)',
        'two_normalizations': 'diac-stripped; rasm (alif/ya/ta-marbuta collapsed)',
        'vl_panel': [3, 5, 10],
        'expected_null': 'uniform-within-verse slot placement for each hapax',
        'z_formula': 'sum-of-independent-Bernoulli with p_i = 1/vl_i',
    },
}

print("=== PER-MUALLAQA (rasm, vl≥3) ===")
for name in per_panel:
    r = per_panel[name].get('rasm_vl3')
    if r:
        print(f"  {name}: n_v={r['n_verses']} n_hap={r['n_hapaxes']} obs={r['hapax_final_observed']} exp={r['hapax_final_expected_uniform']:.2f} z={r['z']:+.3f} p={r['p_one_sided']:.3g}")

print("\n=== POOLED 7-Muʿallaqāt panel ===")
for key, r in pooled_panel.items():
    if r:
        print(f"  {key}: n_hap={r['n_hapaxes']} obs={r['hapax_final_observed']} exp={r['hapax_final_expected_uniform']:.2f} z={r['z']:+.3f} p={r['p_one_sided']:.3g}")

print(f"\n=== QURAN REFERENCE (H-NEW-23 sub-3) ===")
print(f"  n_hap={quran_n} z={quran_z:+.3f} p={quran_p:.3g}")

outp = ROOT / 'findings/phase-b-hypotheses/csv/t004-muallaqat-hapax-slot-positive-control.json'
outp.parent.mkdir(parents=True, exist_ok=True)
outp.write_text(json.dumps(out, indent=2, ensure_ascii=False))
print(f"\nsaved: {outp}")
