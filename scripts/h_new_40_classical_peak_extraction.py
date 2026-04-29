#!/usr/bin/env python3
"""
H-NEW-40 classical peak-verse extraction from al-Biqāʿī Naẓm al-Durar and al-Rāzī Mafātīḥ al-Ghayb.

Method (pre-registered heuristic, MW-6-tagged MEDIUM by default, HIGH for intersection):
- Load OpenITI mARkdown plaintext of both works (raw/*.openiti.raw.txt).
- Find every inline verse citation of form [surah_name: verse_number] via regex.
- For each citation, check if the character position falls within a 400-char
  window of any peak-marker keyword in PEAK_KEYWORDS.
- Map surah name to canonical surah number (SURAH_MAP handles name variants).
- Emit per-source TSV + HIGH-confidence intersection TSV.

MW-6 confidence:
- HIGH = intersection (surah, verse) present in BOTH Biqai and Razi within peak spans.
- MEDIUM = single-source peak verses.
- LOW = not produced; we drop rather than tag low.

Reproducibility:
- No randomness.
- Outputs: findings/classical-sources/h-new-40-*.tsv
- Window parameter WINDOW = 400 chars (~60-80 words of Arabic prose)
- PEAK_KEYWORDS list is locked pre-registration.
"""
import re
import csv
import bisect
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path('/Users/grey/Downloads/quran')
BIQAI = ROOT / 'data/literature/classical-tafsir/raw/biqai-nazm-al-durar.openiti.raw.txt'
RAZI = ROOT / 'data/literature/classical-tafsir/raw/razi-mafatih-al-ghayb.openiti.raw.txt'
OUT = ROOT / 'findings/classical-sources'

PEAK_KEYWORDS = ['المقصود', 'مقصود', 'غاية', 'الغاية', 'غرض', 'الغرض', 'المقصد', 'مقصد']
WINDOW = 400

SURAH_MAP = {
    'الفاتحة': 1, 'البقرة': 2, 'آل عمران': 3, 'النساء': 4, 'المائدة': 5,
    'الأنعام': 6, 'الأعراف': 7, 'الأنفال': 8, 'التوبة': 9, 'يونس': 10,
    'هود': 11, 'يوسف': 12, 'الرعد': 13, 'إبراهيم': 14, 'الحجر': 15,
    'النحل': 16, 'الإسراء': 17, 'بني إسرائيل': 17, 'الكهف': 18, 'مريم': 19, 'طه': 20,
    'الأنبياء': 21, 'الحج': 22, 'المؤمنون': 23, 'المؤمنين': 23, 'النور': 24, 'الفرقان': 25,
    'الشعراء': 26, 'الشعرا': 26, 'النمل': 27, 'القصص': 28, 'العنكبوت': 29, 'الروم': 30,
    'لقمان': 31, 'السجدة': 32, 'الأحزاب': 33, 'سبأ': 34, 'فاطر': 35,
    'يس': 36, 'الصافات': 37, 'ص': 38, 'الزمر': 39, 'غافر': 40, 'المؤمن': 40,
    'فصلت': 41, 'حم السجدة': 41, 'الشورى': 42, 'الزخرف': 43, 'الدخان': 44,
    'الجاثية': 45, 'الأحقاف': 46, 'محمد': 47, 'الفتح': 48, 'الحجرات': 49, 'ق': 50,
    'الذاريات': 51, 'الطور': 52, 'النجم': 53, 'القمر': 54, 'الرحمن': 55,
    'الواقعة': 56, 'الحديد': 57, 'المجادلة': 58, 'الحشر': 59, 'الممتحنة': 60,
    'الصف': 61, 'الجمعة': 62, 'المنافقون': 63, 'المنافقين': 63, 'التغابن': 64, 'الطلاق': 65,
    'التحريم': 66, 'الملك': 67, 'القلم': 68, 'الحاقة': 69, 'المعارج': 70,
    'نوح': 71, 'الجن': 72, 'المزمل': 73, 'المدثر': 74, 'القيامة': 75,
    'الإنسان': 76, 'الدهر': 76, 'المرسلات': 77, 'النبأ': 78, 'النازعات': 79, 'عبس': 80,
    'التكوير': 81, 'الانفطار': 82, 'المطففين': 83, 'الانشقاق': 84, 'البروج': 85,
    'الطارق': 86, 'الأعلى': 87, 'الغاشية': 88, 'الفجر': 89, 'البلد': 90,
    'الشمس': 91, 'الليل': 92, 'الضحى': 93, 'الشرح': 94, 'الانشراح': 94, 'التين': 95,
    'العلق': 96, 'القدر': 97, 'البينة': 98, 'الزلزلة': 99, 'العاديات': 100,
    'القارعة': 101, 'التكاثر': 102, 'العصر': 103, 'الهمزة': 104, 'الفيل': 105,
    'قريش': 106, 'الماعون': 107, 'الكوثر': 108, 'الكافرون': 109, 'الكافرين': 109, 'النصر': 110,
    'المسد': 111, 'اللهب': 111, 'الإخلاص': 112, 'الفلق': 113, 'الناس': 114,
}

TRANSLIT = {
    1: 'al-Fatiha', 2: 'al-Baqara', 3: 'Al Imran', 4: 'al-Nisa', 5: 'al-Maida',
    6: 'al-Anam', 7: 'al-Araf', 8: 'al-Anfal', 9: 'al-Tawba', 10: 'Yunus',
    11: 'Hud', 12: 'Yusuf', 13: 'al-Rad', 14: 'Ibrahim', 15: 'al-Hijr',
    16: 'al-Nahl', 17: 'al-Isra', 18: 'al-Kahf', 19: 'Maryam', 20: 'Ta Ha',
    21: 'al-Anbiya', 22: 'al-Hajj', 23: 'al-Muminun', 24: 'al-Nur', 25: 'al-Furqan',
    26: 'al-Shuara', 27: 'al-Naml', 28: 'al-Qasas', 29: 'al-Ankabut', 30: 'al-Rum',
    31: 'Luqman', 32: 'al-Sajda', 33: 'al-Ahzab', 34: 'Saba', 35: 'Fatir',
    36: 'Ya Sin', 37: 'al-Saffat', 38: 'Sad', 39: 'al-Zumar', 40: 'Ghafir',
    41: 'Fussilat', 42: 'al-Shura', 43: 'al-Zukhruf', 44: 'al-Dukhan', 45: 'al-Jathiya',
    46: 'al-Ahqaf', 47: 'Muhammad', 48: 'al-Fath', 49: 'al-Hujurat', 50: 'Qaf',
    51: 'al-Dhariyat', 52: 'al-Tur', 53: 'al-Najm', 54: 'al-Qamar', 55: 'al-Rahman',
    56: 'al-Waqia', 57: 'al-Hadid', 58: 'al-Mujadila', 59: 'al-Hashr', 60: 'al-Mumtahana',
    61: 'al-Saff', 62: 'al-Jumua', 63: 'al-Munafiqun', 64: 'al-Taghabun', 65: 'al-Talaq',
    66: 'al-Tahrim', 67: 'al-Mulk', 68: 'al-Qalam', 69: 'al-Haqqa', 70: 'al-Maarij',
    71: 'Nuh', 72: 'al-Jinn', 73: 'al-Muzzammil', 74: 'al-Muddaththir', 75: 'al-Qiyama',
    76: 'al-Insan', 77: 'al-Mursalat', 78: 'al-Naba', 79: 'al-Naziat', 80: 'Abasa',
    81: 'al-Takwir', 82: 'al-Infitar', 83: 'al-Mutaffifin', 84: 'al-Inshiqaq', 85: 'al-Buruj',
    86: 'al-Tariq', 87: 'al-Ala', 88: 'al-Ghashiya', 89: 'al-Fajr', 90: 'al-Balad',
    91: 'al-Shams', 92: 'al-Layl', 93: 'al-Duha', 94: 'al-Sharh', 95: 'al-Tin',
    96: 'al-Alaq', 97: 'al-Qadr', 98: 'al-Bayyina', 99: 'al-Zalzala', 100: 'al-Adiyat',
    101: 'al-Qaria', 102: 'al-Takathur', 103: 'al-Asr', 104: 'al-Humaza', 105: 'al-Fil',
    106: 'Quraysh', 107: 'al-Maun', 108: 'al-Kawthar', 109: 'al-Kafirun', 110: 'al-Nasr',
    111: 'al-Masad', 112: 'al-Ikhlas', 113: 'al-Falaq', 114: 'al-Nas',
}

VERSE_PAT = re.compile(r'\[([\u0621-\u064A\s]+?)\s*:\s*(\d{1,3})\]')


def strip_diacritics(s: str) -> str:
    return re.sub(r'[\u064B-\u065F\u0670]', '', s)


def extract_verse_cites(txt: str):
    return [(m.group(1).strip(), int(m.group(2)), m.start())
            for m in VERSE_PAT.finditer(txt)]


def compute_peak_spans(txt: str, window: int = WINDOW):
    spans = []
    for kw in PEAK_KEYWORDS:
        for m in re.finditer(re.escape(kw), txt):
            spans.append((max(0, m.start() - window), m.end() + window))
    spans.sort()
    if not spans:
        return spans
    merged = [spans[0]]
    for s, e in spans[1:]:
        if s <= merged[-1][1]:
            merged[-1] = (merged[-1][0], max(merged[-1][1], e))
        else:
            merged.append((s, e))
    return merged


def in_span_factory(spans):
    starts = [s[0] for s in spans]

    def check(pos: int) -> bool:
        idx = bisect.bisect_right(starts, pos)
        if idx == 0:
            return False
        s, e = spans[idx - 1]
        return s <= pos <= e

    return check


def context_keyword(txt: str, pos: int, window: int = WINDOW) -> str:
    lo = max(0, pos - window)
    hi = min(len(txt), pos + window)
    snippet = txt[lo:hi]
    for kw in PEAK_KEYWORDS:
        if kw in snippet:
            return kw
    return ''


def snippet_for(txt: str, pos: int, half: int = 120) -> str:
    lo = max(0, pos - half)
    hi = min(len(txt), pos + half)
    s = txt[lo:hi].replace('\n', ' ').replace('~~', ' ')
    return re.sub(r'\s+', ' ', s).strip()[:300]


def extract_peak_verses(path: Path, source_label: str):
    txt = strip_diacritics(path.read_text())
    cites = extract_verse_cites(txt)
    spans = compute_peak_spans(txt)
    inf = in_span_factory(spans)
    records = []
    skipped = Counter()
    for name, verse, pos in cites:
        if not inf(pos):
            continue
        sn = SURAH_MAP.get(name)
        if sn is None:
            skipped[name] += 1
            continue
        if verse < 1 or verse > 286:
            continue
        records.append({
            'surah': sn,
            'verse': verse,
            'surah_name_translit': TRANSLIT.get(sn, '?'),
            'source': source_label,
            'peak_keyword_context': context_keyword(txt, pos),
            'char_pos': pos,
            'snippet': snippet_for(txt, pos),
        })
    return records, skipped


def dedupe(records):
    seen = {}
    for r in records:
        key = (r['surah'], r['verse'])
        if key not in seen:
            seen[key] = r
    return sorted(seen.values(), key=lambda r: (r['surah'], r['verse']))


def write_tsv(records, path, extra_cols=None):
    with open(path, 'w') as f:
        w = csv.writer(f, delimiter='\t')
        cols = ['surah', 'verse', 'surah_name_translit', 'source',
                'peak_keyword_context', 'char_pos', 'confidence', 'snippet_verbatim']
        w.writerow(cols)
        for r in records:
            w.writerow([r['surah'], r['verse'], r['surah_name_translit'], r['source'],
                        r['peak_keyword_context'], r['char_pos'], 'MEDIUM', r['snippet']])


def main():
    biqai_all, biqai_dropped = extract_peak_verses(BIQAI, 'biqai-nazm-al-durar')
    razi_all, razi_dropped = extract_peak_verses(RAZI, 'razi-mafatih-al-ghayb')

    biqai_unique = dedupe(biqai_all)
    razi_unique = dedupe(razi_all)

    OUT.mkdir(parents=True, exist_ok=True)
    write_tsv(biqai_unique, OUT / 'h-new-40-biqai-peak-verses.tsv')
    write_tsv(razi_unique, OUT / 'h-new-40-razi-peak-verses.tsv')

    biqai_lookup = {(r['surah'], r['verse']): r for r in biqai_unique}
    razi_lookup = {(r['surah'], r['verse']): r for r in razi_unique}
    biqai_set = set(biqai_lookup.keys())
    razi_set = set(razi_lookup.keys())
    exact = sorted(biqai_set & razi_set)

    with open(OUT / 'h-new-40-classical-peak-verses-intersection.tsv', 'w') as f:
        w = csv.writer(f, delimiter='\t')
        w.writerow(['surah', 'verse', 'surah_name_translit',
                    'biqai_keyword', 'razi_keyword',
                    'confidence', 'biqai_snippet', 'razi_snippet'])
        for s, v in exact:
            b = biqai_lookup[(s, v)]
            r = razi_lookup[(s, v)]
            w.writerow([s, v, TRANSLIT.get(s, '?'),
                        b['peak_keyword_context'], r['peak_keyword_context'],
                        'HIGH', b['snippet'], r['snippet']])

    fuzzy = set()
    razi_by_s = defaultdict(set)
    for s, v in razi_set:
        razi_by_s[s].add(v)
    for s, v in biqai_set:
        for vr in razi_by_s.get(s, ()):
            if abs(v - vr) <= 2:
                fuzzy.add((s, v))
                break

    report = {
        'biqai_unique_peak_verses': len(biqai_unique),
        'razi_unique_peak_verses': len(razi_unique),
        'exact_intersection': len(exact),
        'exact_as_pct_of_biqai': round(100 * len(exact) / max(len(biqai_set), 1), 1),
        'exact_as_pct_of_razi': round(100 * len(exact) / max(len(razi_set), 1), 1),
        'fuzzy_plus_minus_2': len(fuzzy),
        'fuzzy_as_pct_of_biqai': round(100 * len(fuzzy) / max(len(biqai_set), 1), 1),
        'surahs_covered_either': len(set(s for s, _ in biqai_set | razi_set)),
        'surahs_covered_both': len(set(s for s, _ in biqai_set) & set(s for s, _ in razi_set)),
        'surahs_with_exact_match': len(set(s for s, _ in exact)),
        'surahs_uncovered': sorted(set(range(1, 115)) - (set(s for s, _ in biqai_set) | set(s for s, _ in razi_set))),
        'biqai_unmapped_names_top10': biqai_dropped.most_common(10),
        'razi_unmapped_names_top10': razi_dropped.most_common(10),
        'peak_keywords': PEAK_KEYWORDS,
        'char_window': WINDOW,
    }
    import json as _j
    (OUT / 'h-new-40-extraction-report.json').write_text(_j.dumps(report, indent=2, ensure_ascii=False))
    print('wrote:')
    print(f'  {OUT}/h-new-40-biqai-peak-verses.tsv ({len(biqai_unique)} rows)')
    print(f'  {OUT}/h-new-40-razi-peak-verses.tsv ({len(razi_unique)} rows)')
    print(f'  {OUT}/h-new-40-classical-peak-verses-intersection.tsv ({len(exact)} HIGH-confidence rows)')
    print(f'  {OUT}/h-new-40-extraction-report.json')
    print(f'exact intersection: {len(exact)} ({report["exact_as_pct_of_biqai"]}% Biqai, {report["exact_as_pct_of_razi"]}% Razi)')


if __name__ == '__main__':
    main()
