# DICTION axis — flag non-attested / post-classical / metri-causa coinages.
items = [
 (4, "اسْتَنْزَلْتُهو istanzaltuhū", "Form-X istanzala 'to bring/draw down' — classical, attested (Q-register). Theologically brushes revelation-language but lexically fine.", "OK (sense-risk, not diction)"),
 (5, "نَفَضْتُ أَوْزانًا / هِجْتُ المَخْزون", "nafaḍa 'shake out', hāja 'stir up', makhzūn 'stored' — all classical. Noisy/over-active diction (5 verbs) but attested.", "OK"),
 (7, "فَراقِد farāqid", "al-farāqid = the guard-stars (al-farqadān + poetic pl). Classical astronomic diction.", "OK"),
 (11,"البَيان al-bayān", "Replaces invented لَفيظ lafīẓ. al-bayān (eloquence/clarity) fully classical (Q55:4).", "OK — لَفيظ ELIMINATED ✓"),
 (13,"لَحْنٌ مَوْهون / الرَّنين", "laḥn 'melody/tune', rann/ranīn 'ringing', mawhūn 'enfeebled' — all classical. Replaces post-classical المَعْنَوِيّ.", "OK — المَعْنَوِيّ ELIMINATED ✓"),
 (17,"حِماهُ المَضْنون / al-fard", "ḥimā 'sanctuary/protected-preserve' classical; maḍnūn 'jealously-withheld' (ḍ-n-n, Q81:24 bi-ḍanīn) classical. (al-waḥd of prior version REPLACED by al-fard.)", "OK — al-waḥd GONE ✓"),
 (18,"ذو البَيان المَحْصون dhū l-bayān", "dhū l-bayān 'possessor of eloquence'; maḥṣūn 'fortified/protected' (ḥ-ṣ-n) classical. Clean predicate (ذو m.s. + naʿt def.).", "OK"),
 (21,"المَدْيون al-madyūn", "STRICT: madīn (دانَ/يَدين) is the classical ism mafʿūl 'indebted'. madyūn is a LATE/Abbasid+colloquial-leaning variant; Lisān records it as a variant (NOT invented).", "FLAG: Abbasid-acceptable / strict-classical DISPREFERRED"),
 (22,"الحِساب المَأْفون al-maʾfūn", "maʾfūn 'witless/feeble-minded' (ʾ-f-n) classical; ḥisāb 'reckoning' classical. Replaces 'al-kunh+humu'.", "OK"),
 (23,"تاج النّون tāj al-nūn", "GRAMMAR clean (tāj m.s. fāʿil; al-nūn muḍāf ilayh). DICTION: 'tāj al-nūn'='crown of the nūn' is NOT a classical idiom — a modern/numerological poetic coinage (the thesis-beat). Not ungrammatical, not a non-word, but an anachronistic IMAGE.", "FLAG-soft: neologistic image (intentional thesis-beat)"),
 (25,"خَراباً مَسْكون kharāb+maskūn", "kharāb 'ruin' (m.s.) classical; maskūn 'inhabited/haunted'. Replaces fem dār. Clean.", "OK"),
 (27,"المَوْطون al-mawṭūn", "ism mafʿūl of waṭana 'to make/take as homeland' (w-ṭ-n; mawṭin Q9:25). RARE but morphologically/lexically defensible — attested root+pattern, not invented.", "weak-but-attested (not failed)"),
]
print(f"{'#':>3}  item / verdict")
for n,it,note,v in items:
    print(f"{n:>3}  {it}\n      -> {note}\n      => {v}\n")
