#!/usr/bin/env python3
"""
Bulk-fetch baseline classical Arabic corpora from Arabic Wikisource.

Targets:
  - Sahih al-Bukhari (all 79 books) -> bukhari.txt
  - Sira ibn Hisham vol. 1 (38 sub-pages) -> sira-ibn-hisham.txt
  - Diwan al-Mutanabbi if listable
  - Anything else in the Wikisource subtree

Reuses fetch_wikisource.strip_wiki().
"""
from __future__ import annotations

import json
import sys
import time
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from fetch_wikisource import strip_wiki, api_get, UA, OUT  # noqa: E402

OUT.mkdir(parents=True, exist_ok=True)


def list_subpages(prefix: str) -> list[str]:
    enc = urllib.parse.quote(prefix)
    url = (
        "https://ar.wikisource.org/w/api.php?action=query&format=json"
        f"&list=allpages&apprefix={enc}&aplimit=500"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode("utf-8"))
    return [p["title"] for p in d["query"]["allpages"]]


def fetch_collection(parent_title: str, slug: str, prefix: str) -> int:
    """Fetch all wikisource pages with `prefix` and concatenate."""
    titles = list_subpages(prefix)
    print(f"[{slug}] {len(titles)} subpages")
    chunks = []
    for i, title in enumerate(titles):
        try:
            raw = api_get(title)
        except Exception as e:
            print(f"  ERR {title}: {e}", file=sys.stderr)
            continue
        if not raw:
            continue
        clean = strip_wiki(raw)
        if clean:
            chunks.append(f"# {title}\n{clean}")
        if (i + 1) % 10 == 0:
            print(f"  {i+1}/{len(titles)}", file=sys.stderr)
        time.sleep(0.05)  # be polite
    text = "\n\n".join(chunks)
    out = OUT / f"{slug}.txt"
    out.write_text(text, encoding="utf-8")
    return len(text)


COLLECTIONS = [
    ("صحيح البخاري", "bukhari", "صحيح البخاري/"),
    ("سيرة ابن هشام", "sira-ibn-hisham", "سيرة ابن هشام/"),
]


if __name__ == "__main__":
    for parent, slug, prefix in COLLECTIONS:
        n = fetch_collection(parent, slug, prefix)
        print(f"=== {slug}: {n} chars")
