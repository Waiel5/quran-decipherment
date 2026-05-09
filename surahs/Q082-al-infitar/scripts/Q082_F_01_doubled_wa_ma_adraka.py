#!/usr/bin/env python3
"""
Q082-F-01 — Doubled wa-mā-adrāka-mā corpus-uniqueness verification.

Hypothesis: Q 82:17-18 contains the corpus's UNIQUE doubled wa-mā-adrāka-mā
construction, with v.17 = "wa-mā adrāka mā yawm al-dīn" and v.18 = "thumma
mā adrāka mā yawm al-dīn" — the same NP meta-questioned in immediate
succession via thumma.

Pre-reg locked: see preregs/Q082-F-01-doubled-wa-ma-adraka-prereg.md
Direction: Q 82 = 1 doubled meta-pair (corpus EXACT); thumma-mā-adrāka-mā
construction count = 1 (Q 82:18 only).

Rules-tuple: (no-tashkeel, orthographic-token, graphemes,
basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi).
"""
import json
import os
import re
import unicodedata
from collections import Counter, defaultdict

ROOT = '/Users/grey/Downloads/quran'
OUT = os.path.join(ROOT, 'surahs/Q082-al-infitar/csv/Q082-F-01.json')


def load_quran(variant):
    path = os.path.join(ROOT, 'quran-text', f'quran-{variant}.json')
    with open(path) as f:
        return json.load(f)


def strip_diacritics(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s)
                   if unicodedata.category(c) != 'Mn')


def normalize(s):
    s = strip_diacritics(s)
    s = re.sub(r'[إأآٱ]', 'ا', s)
    # NB: We deliberately do NOT collapse ى→ي because the classical
    # min-/full-tashkeel uses ى for alif-maqsura in some forms (e.g.
    # أَدرىٰكَ → ادرىك under strip-diacritics). To detect ادراك across
    # all 3 variants we accept both ادراك and ادرىك as the surface form.
    # strip waqf glyphs and sajda glyph
    s = re.sub(r'[۩ۖۗۚۛۘۙۜۤ]', '', s)
    return s.strip()


def find_wa_ma_adraka(text):
    """Returns matches of (wa-)mā adrāka mā in text. Returns list of
    starts (char index of start of pattern). The pattern allows optional
    prefix wa-/fa-/thumma- before mā, but anchors on 'ma adraka ma'.

    Note: Arabic does not behave like Latin script for \b boundaries; we
    use explicit start-or-whitespace anchors with optional 1-char prefix.
    """
    norm = normalize(text)
    # raw consonant pattern for adrāka: ادراك (alif-dal-ra-alif-kaf)
    # Pattern: (start-or-space) (optional و|ف|ث|ال) ما adraka ma (space-or-end)
    # In Arabic orthography, "wa-" prefix is concatenated to following word,
    # so "وما" is the orthographic form of "wa+ma" — we accept these prefixes.
    pat = re.compile(r'(^|\s)(و|ف|ث|ال)?ما\s+ادر[اى]ك\s+ما(\s|$)')
    return [(m.start(), m.group()) for m in pat.finditer(norm)]


def has_thumma_construction(text):
    """Check if 'thumma ma adraka ma' substring appears (i.e., the prefix is
    explicitly 'ث' = 'ثم' = thumma)."""
    norm = normalize(text)
    # Look for "ثم ما ادراك ما" — thumma is a free-standing word ending in m,
    # so we need ثم (tha-mim) followed by space-ma-space-adraka-space-ma.
    pat = re.compile(r'(^|\s)ثم\s+ما\s+ادر[اى]ك\s+ما(\s|$)')
    return list(pat.finditer(norm))


def main():
    print("=== Q082-F-01: Doubled wa-mā-adrāka-mā audit ===\n")
    out = {
        'rules_tuple': '(no-tashkeel, orthographic-token, graphemes, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'pre_reg_finding_id': 'Q082-F-01',
        'parent_findings': ['H-NEW-1190'],
    }

    # Cross-validate across 3 variants
    print("[1] Corpus-wide wa-mā-adrāka-mā occurrences (cross-tashkeel)")
    all_results = {}
    for variant in ['no-tashkeel', 'min-tashkeel', 'full-tashkeel']:
        data = load_quran(variant)
        hits = []
        for s in data:
            for v in s['verses']:
                m = find_wa_ma_adraka(v['text'])
                if m:
                    hits.append({
                        'surah': s['id'],
                        'verse': v['id'],
                        'count_in_verse': len(m),
                        'text': v['text'],
                    })
        all_results[variant] = hits
        print(f"  {variant}: {len(hits)} verse-hits, total tokens {sum(h['count_in_verse'] for h in hits)}")

    # Lock to no-tashkeel for the canonical analysis
    no_tash = all_results['no-tashkeel']
    out['no_tashkeel_hits'] = no_tash

    # Verify all 3 variants give same surahs and same verse-IDs
    surah_sets = {v: set((h['surah'], h['verse']) for h in r) for v, r in all_results.items()}
    consistency = (surah_sets['no-tashkeel'] == surah_sets['min-tashkeel']
                   == surah_sets['full-tashkeel'])
    out['cross_variant_consistent'] = consistency
    print(f"\n  Cross-variant verse-set consistency: {consistency}")

    # Corpus surahs containing the pattern (by surah_id)
    surah_hits = defaultdict(list)
    for h in no_tash:
        surah_hits[h['surah']].append(h)
    out['surahs_with_pattern'] = sorted(surah_hits.keys())
    out['n_distinct_surahs'] = len(surah_hits)
    print(f"\n[2] Distinct surahs with pattern: {sorted(surah_hits.keys())}")
    print(f"    Count = {len(surah_hits)} (H-NEW-1190 expected: 10)")

    # Detect doubled-meta-question pairs: 2 consecutive verses both bearing pattern
    # AND meta-questioning the same NP (the 1-3 words after 'adraka ma')
    print("\n[3] Doubled meta-pair detection")
    doubled = []
    for surah_id in sorted(surah_hits.keys()):
        verses = surah_hits[surah_id]
        verses_by_id = {h['verse']: h for h in verses}
        for h in verses:
            v_curr = h['verse']
            v_next = v_curr + 1
            if v_next in verses_by_id:
                # Both bear pattern. Now check NP equivalence.
                next_h = verses_by_id[v_next]
                # Extract the next 1-3 words after adraka ma
                norm_curr = normalize(h['text'])
                norm_next = normalize(next_h['text'])
                m_curr = re.search(r'(?:^|\s)(?:و|ف|ث|ال)?ما\s+ادر[اى]ك\s+ما\s+(\S+(?:\s+\S+){0,2})', norm_curr)
                m_next = re.search(r'(?:^|\s)(?:و|ف|ث|ال)?ما\s+ادر[اى]ك\s+ما\s+(\S+(?:\s+\S+){0,2})', norm_next)
                np_curr = m_curr.group(1) if m_curr else None
                np_next = m_next.group(1) if m_next else None
                # Compare first 1-2 words (the NP head)
                if np_curr and np_next:
                    head_curr = ' '.join(np_curr.split()[:2])
                    head_next = ' '.join(np_next.split()[:2])
                    same_np = (head_curr == head_next)
                    doubled.append({
                        'surah': surah_id,
                        'v_first': v_curr,
                        'v_second': v_next,
                        'np_first': np_curr,
                        'np_second': np_next,
                        'np_head_first': head_curr,
                        'np_head_second': head_next,
                        'same_np': same_np,
                    })
    out['doubled_meta_pairs'] = doubled
    out['n_doubled_with_same_np'] = sum(1 for d in doubled if d['same_np'])
    print(f"  Doubled meta-pair candidates (consecutive verses both bearing pattern):")
    for d in doubled:
        marker = "✓ SAME-NP" if d['same_np'] else "(diff NP)"
        print(f"    Q {d['surah']}:{d['v_first']}-{d['v_second']} {marker}")
        print(f"      v.{d['v_first']} NP: '{d['np_first']}'")
        print(f"      v.{d['v_second']} NP: '{d['np_second']}'")
    print(f"  Total: {len(doubled)} pairs ({out['n_doubled_with_same_np']} with same NP)")

    # Detect thumma-mā-adrāka-mā construction
    print("\n[4] thumma-mā-adrāka-mā construction count corpus-wide")
    thumma_hits = []
    data = load_quran('no-tashkeel')
    for s in data:
        for v in s['verses']:
            m = has_thumma_construction(v['text'])
            if m:
                thumma_hits.append({
                    'surah': s['id'], 'verse': v['id'], 'text': v['text']
                })
    out['thumma_construction_hits'] = thumma_hits
    out['n_thumma_construction'] = len(thumma_hits)
    print(f"  Total thumma-mā-adrāka-mā hits: {len(thumma_hits)}")
    for h in thumma_hits:
        print(f"    Q {h['surah']}:{h['verse']}: {h['text'][:80]}")

    # Verdict
    print("\n[5] VERDICT")
    if (out['n_doubled_with_same_np'] == 1
            and doubled and doubled[0]['surah'] == 82
            and doubled[0]['v_first'] == 17
            and out['n_thumma_construction'] == 1
            and thumma_hits[0]['surah'] == 82
            and thumma_hits[0]['verse'] == 18):
        verdict = ('CONFIRMED — Q 82:17-18 is the corpus-UNIQUE doubled '
                   'wa-mā-adrāka-mā construction with same-NP (yawm al-dīn) '
                   'meta-questioned twice via thumma.')
    elif out['n_doubled_with_same_np'] >= 1 and doubled[0]['surah'] == 82:
        verdict = ('DIRECTIONAL — Q 82 has the doubled meta-question but '
                   'corpus-uniqueness needs review (other doublings detected).')
    else:
        verdict = 'NULL — doubled meta-question is not unique to Q 82 OR Q 82 lacks it.'
    out['verdict'] = verdict
    print(f"  {verdict}")

    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, 'w') as f:
        json.dump(out, f, ensure_ascii=False, indent=2)
    print(f"\nWrote: {OUT}")


if __name__ == '__main__':
    main()
