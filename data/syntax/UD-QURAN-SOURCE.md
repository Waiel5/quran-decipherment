---
title: UD-Quran / Extended Quranic Treebank source manifest
date_acquired: 2026-07-11
status: external reproducibility input; binary not committed
---

# UD-Quran / Extended Quranic Treebank source manifest

H-NEW-2540 uses Quranic Arabic Corpus v0.4 for root/form annotation and the
Extended Quranic Treebank (EQTB) only for dependency relations. The full EQTB is
distributed inside the UD-Quran reproducibility package.

- UD-Quran dataset DOI: <https://doi.org/10.5281/zenodo.18634813>
- EQTB source DOI: <https://doi.org/10.17632/rk96pn66m4.1>
- License: CC BY 4.0 for EQTB/UD-Quran; QAC v0.4 remains GNU GPL under its own notice.
- Downloaded archive:
  `UD-Quran_reproducibility_package.zip`
- Archive SHA-256:
  `6ae1da54a801939cfaf52c05b01e5858ab26b147543806cccb46df4ea4fbdcb3`
- Nested EQTB archive SHA-256:
  `8ef6056a3c8d0337ecb0f01f52790b39d93f2524429b52a6908b1eb259488281`
- Extracted `Quranic.csv` SHA-256:
  `a303c24cf51b90f6cd5eb0fb25d6c591977a7797743d16e0dedc76a5af5ae0b7`
- Local QAC v0.4 morphology SHA-256:
  `a1d12923815341face765083805d2148ed2d9f5cc3f7d6665219d887675d8c46`

Re-acquire without committing the 50 MB source table:

```bash
curl -L 'https://zenodo.org/records/18634813/files/UD-Quran_reproducibility_package.zip?download=1' \
  -o UD-Quran_reproducibility_package.zip
unzip UD-Quran_reproducibility_package.zip
unzip UD-Quran_reproducibility_package/data/source/EQTB_MendeleyData_V1.zip \
  -d UD-Quran_reproducibility_package/data/source/eqtb
shasum -a 256 \
  UD-Quran_reproducibility_package.zip \
  UD-Quran_reproducibility_package/data/source/EQTB_MendeleyData_V1.zip \
  UD-Quran_reproducibility_package/data/source/eqtb/Quranic.csv
```

`Quranic.csv` is UTF-16 tab-separated text despite its `.csv` suffix.
