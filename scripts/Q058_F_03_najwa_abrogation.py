#!/usr/bin/env python3
"""Q058-F-03 — Q 58:12-13 najwā-charity classical mid-revelation abrogation claim audit.

Pre-reg: surahs/Q058-al-mujadala/Q058-F-03-najwa-abrogation-prereg.md
Pre-reg SHA256: cfcc79656aaa6c3af3b59cfa9c36bce73850792aaa42d563a3c45e565f8f043c
Rules-tuple: (no-tashkeel, orthographic-token, classical-text-attestation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)
"""
import json
import hashlib
import sys
import os

PREREG = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/Q058-F-03-najwa-abrogation-prereg.md'
EXPECTED_SHA = 'cfcc79656aaa6c3af3b59cfa9c36bce73850792aaa42d563a3c45e565f8f043c'
OUT_PATH = '/Users/grey/Downloads/quran/surahs/Q058-al-mujadala/csv/Q058-F-03.json'


def verify_sha():
    with open(PREREG, 'rb') as f:
        actual = hashlib.sha256(f.read()).hexdigest()
    if actual != EXPECTED_SHA:
        print(f"FAIL: SHA mismatch.\n  expected={EXPECTED_SHA}\n  actual  ={actual}", file=sys.stderr)
        sys.exit(1)


def load_classical_text(path):
    if not os.path.exists(path):
        return None
    with open(path) as f:
        d = json.load(f)
    txt = d.get('text', d.get('en', d.get('translation', '')))
    if isinstance(txt, dict):
        txt = txt.get('text', '') or txt.get('content', '')
    if not txt:
        for k, v in d.items():
            if isinstance(v, str) and len(v) > 50:
                txt = v
                break
    return txt or ''


def main():
    verify_sha()

    base_wahidi = '/Users/grey/Downloads/quran/data/literature/classical-tafsir/spa5k-tafsir-api/en-asbab-al-nuzul-by-al-wahidi/58'
    base_tabari = '/Users/grey/Downloads/quran/data/literature/classical-tafsir/spa5k-tafsir-api/ar-tafsir-al-tabari/58'

    wahidi_v12 = load_classical_text(os.path.join(base_wahidi, '12.json'))
    wahidi_v13 = load_classical_text(os.path.join(base_wahidi, '13.json'))
    tabari_v12 = load_classical_text(os.path.join(base_tabari, '12.json'))
    tabari_v13 = load_classical_text(os.path.join(base_tabari, '13.json'))

    # H1: A1 = independent classical sources attesting abrogation
    abrogation_keywords_en = ['abrogated', 'abrogation', 'no one has applied', 'never have they applied']
    abrogation_keywords_ar = ['نسخت', 'نسخ', 'فنسخت', 'منسوخة', 'لم يعمل بها']

    sources_attesting_abrogation = []
    if wahidi_v12 and any(kw in wahidi_v12 for kw in abrogation_keywords_en + abrogation_keywords_ar):
        sources_attesting_abrogation.append('al-Wāḥidī Asbāb v12')
    if wahidi_v13 and any(kw in wahidi_v13 for kw in abrogation_keywords_en + abrogation_keywords_ar):
        sources_attesting_abrogation.append('al-Wāḥidī Asbāb v13')
    if tabari_v12 and any(kw in tabari_v12 for kw in abrogation_keywords_ar):
        sources_attesting_abrogation.append('al-Ṭabarī Tafsīr v12')
    if tabari_v13 and any(kw in tabari_v13 for kw in abrogation_keywords_ar):
        sources_attesting_abrogation.append('al-Ṭabarī Tafsīr v13')

    A1 = len(sources_attesting_abrogation)

    # H2: A2 = ʿAlī-isnad chains
    ali_keywords_en = ["'Ali ibn Abi Talib", 'Commander of the Faithful', 'one dinar', 'gold which I exchanged', 'ten silver pieces', 'one silver piece']
    ali_keywords_ar = ['عليّ بن أبي طالب', 'علي بن أبي طالب', 'عليّ رضي الله', 'علي رضي', 'دينارا فتصدق', 'دينارا', 'علي رضي الله عنه', 'فلم يناجه إلا علي']
    mujahid_keywords = ['Mujahid', 'مجاهد', 'Ibn Abi Najih', 'ابن أبي نجيح']
    qatada_keywords = ['Qatadah', 'قتادة']

    chains = {'ʿAlī (named)': False, 'Mujāhid via Ibn Abī Najīḥ': False, 'Qatāda': False}
    for src_name, txt in [('al-Wāḥidī Asbāb v12', wahidi_v12), ('al-Wāḥidī Asbāb v13', wahidi_v13),
                          ('al-Ṭabarī Tafsīr v12', tabari_v12), ('al-Ṭabarī Tafsīr v13', tabari_v13)]:
        if not txt: continue
        if any(kw in txt for kw in ali_keywords_en + ali_keywords_ar):
            chains['ʿAlī (named)'] = True
        if any(kw in txt for kw in mujahid_keywords):
            chains['Mujāhid via Ibn Abī Najīḥ'] = True
        if any(kw in txt for kw in qatada_keywords):
            chains['Qatāda'] = True

    A2 = sum(1 for v in chains.values() if v)

    # H3: lexical-surface markers
    quran = json.load(open('/Users/grey/Downloads/quran/quran-text/quran-no-tashkeel.json'))
    s58 = next(s for s in quran if s['id'] == 58)
    v12 = next(v['text'] for v in s58['verses'] if v['id'] == 12)
    v13 = next(v['text'] for v in s58['verses'] if v['id'] == 13)

    markers = {
        'v12_contains_ṣadaqatan_singular': 'صدقة' in v12 or 'صدقة' in v12,
        'v13_contains_ṣadaqāt_plural': 'صدقات' in v13,
        'v13_contains_fa-idh_lam_tafʿalū': 'فإذ لم تفعلوا' in v13 or 'فإذ لم تفعلوا' in v13,
        'v13_contains_wa-tāba_Allāhu_ʿalaykum': 'وتاب الله عليكم' in v13,
        'v13_contains_fa-aqīmū_al-ṣalāta_wa-ātū_al-zakāta': 'فأقيموا الصلاة وآتوا الزكاة' in v13,
    }
    A3 = sum(1 for v in markers.values() if v)

    h1_pass = A1 >= 2
    h2_pass = A2 >= 1
    h3_pass = A3 >= 4

    # Verdict
    if h1_pass and h2_pass and A3 >= 4:
        verdict = 'CONFIRMED'
    elif h1_pass and h2_pass and A3 >= 3:
        verdict = 'DIRECTIONAL'
    elif (h1_pass and h2_pass) or (A3 >= 4):
        verdict = 'PARTIAL'
    else:
        verdict = 'NULL'

    out = {
        'finding_id': 'Q058-F-03',
        'pre_reg_sha256': EXPECTED_SHA,
        'rules_tuple': '(no-tashkeel, orthographic-token, classical-text-attestation, basmala-counted-only-in-Q1, Hafs-Kufan, Mashriqi)',
        'sources_loaded': {
            'al-Wāḥidī Asbāb v12': bool(wahidi_v12),
            'al-Wāḥidī Asbāb v13': bool(wahidi_v13),
            'al-Ṭabarī Tafsīr v12': bool(tabari_v12),
            'al-Ṭabarī Tafsīr v13': bool(tabari_v13),
        },
        'A1_sources_attesting_abrogation': A1,
        'A1_sources_list': sources_attesting_abrogation,
        'A2_isnad_chains_cited': A2,
        'A2_chains_detail': chains,
        'A3_lexical_surface_markers_present': A3,
        'A3_markers_detail': markers,
        'h1_pass': h1_pass,
        'h2_pass': h2_pass,
        'h3_pass': h3_pass,
        'q58_v12_text': v12,
        'q58_v13_text': v13,
        'verdict': verdict,
        'classical_anchor_summary': {
            'al-Wāḥidī attribution': "ʿAlī b. Abī Ṭālib: 'There is one verse in the Book of Allah that no one has applied before me nor is there anyone who has applied it after me. [It is] (O ye who believe! When ye hold conference with the messenger). I had a piece of gold which I exchanged for silver pieces and whenever I conferred with the Messenger I spent one silver piece in charity until I spent them all. Then the verse was abrogated with another verse [Q 58:13].'",
            'al-Ṭabarī Mujāhid chain': 'Mujāhid via Ibn Abī Najīḥ: nuhū ʿan munājāt al-nabī ḥattā yataṣaddaqū fa-lam yunājihu illā ʿAlī b. Abī Ṭālib raḍiya Allāhu ʿanhu qaddama dīnāran fa-taṣaddaqa bihi thumma unzilat al-rukhṣa fī dhālik. (And ʿAlī said: there is a verse in God\'s Book that no one acted on before me, and no one will act on after me… furiḍat thumma nusikhat).',
            'al-Ṭabarī Qatāda chain v13': 'Qatāda on Q 58:13 fa-aqīmū al-ṣalāta wa-ātū al-zakāta: farīḍatāni wājibatāni lā rajʿata li-aḥadin fīhimā fa-nasakhat hādhihi al-āyatu mā kāna qablahā min amri al-ṣadaqa fī al-najwā. (Two binding obligations admitting no withdrawal; this verse abrogated what came before it of the najwā-charity command).',
            'classical_intra-surah-abrogation_genre': 'al-Suyūṭī Itqān nawʿ 47 (al-nāsikh wa-l-mansūkh): Q 58:12 → Q 58:13 is the canonical example of intra-surah abrogation in the Medinan corpus, alongside fewer than 5 attested cases (cf. Powers 1988; Burton 1990).',
        },
    }

    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, 'w') as f:
        json.dump(out, f, indent=2, ensure_ascii=False)

    print(f"Q058-F-03 verdict: {verdict}")
    print(f"  A1 sources attesting abrogation: {A1} ({sources_attesting_abrogation})")
    print(f"  A2 isnad chains cited: {A2} (chains: {[k for k, v in chains.items() if v]})")
    print(f"  A3 lexical-surface markers: {A3}/5")
    print(f"  Output: {OUT_PATH}")


if __name__ == '__main__':
    main()
