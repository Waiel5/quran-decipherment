#!/usr/bin/env python3
"""Fetch raw wikitext from Arabic Wikisource and strip markup, save plaintext."""
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

OUT = Path("/Users/grey/Downloads/quran/data/baseline-corpora/raw")
OUT.mkdir(parents=True, exist_ok=True)

UA = "Mozilla/5.0 (compatible; QuranBaselineFetcher/1.0; research)"


def api_get(title: str) -> str:
    url = (
        "https://ar.wikisource.org/w/api.php?action=query&format=json"
        "&prop=revisions&rvprop=content&rvslots=main&formatversion=2"
        f"&titles={urllib.parse.quote(title)}"
    )
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        d = json.loads(r.read().decode("utf-8"))
    pages = d["query"]["pages"]
    if not pages or "revisions" not in pages[0]:
        return ""
    return pages[0]["revisions"][0]["slots"]["main"]["content"]


VERSE_TEMPLATES = {"أبيات", "بيت", "شعر", "قصيدة", "بيتان", "بيت مفرد", "أبيات مفردة"}


def _replace_template(m: re.Match) -> str:
    inner = m.group(1)
    # split on '|' at top level
    parts = inner.split("|")
    name = parts[0].strip()
    if name in VERSE_TEMPLATES:
        # join the rest with newlines (each pipe-arg is a hemistich pair or verse)
        return "\n" + "\n".join(p for p in parts[1:] if p.strip()) + "\n"
    # discard template
    return ""


def strip_wiki(text: str) -> str:
    # Resolve verse templates first (they hold the actual poetry).
    # Iteratively replace innermost {{ ... }} (no nested braces).
    prev = None
    while prev != text:
        prev = text
        text = re.sub(r"\{\{([^{}]*)\}\}", _replace_template, text, flags=re.DOTALL)
    # \\ in {{أبيات}} = hemistich separator -> use a tab so we keep
    # both halves of each verse on one line in the cleaned output
    text = text.replace("\\\\", "\t")
    # Convert wiki tables: keep cell text, drop the syntax.
    def _table_strip(m: re.Match) -> str:
        body = m.group(0)
        # Drop opening "{|...\n" and closing "|}"
        body = re.sub(r"\{\|[^\n]*\n", "", body)
        body = re.sub(r"\n*\|\}\s*$", "", body)
        out_rows = []
        cur = []
        for line in body.split("\n"):
            stripped = line.strip()
            if stripped.startswith("|-") or stripped.startswith("|+"):
                if cur:
                    out_rows.append(" \t ".join(cur))
                    cur = []
                continue
            if stripped.startswith("|") or stripped.startswith("!"):
                # Remove leading marker
                content = stripped[1:].lstrip()
                # Cell may carry attribute: "attr|text" — only when attr has no spaces
                if "|" in content:
                    # split on first '|' and check whether left side looks like attrs
                    left, right = content.split("|", 1)
                    if re.match(r"^[\w\s\"'=#:;%-]*$", left) and len(left) < 60 and not re.search(r"[\u0600-\u06FF]", left):
                        content = right
                # Cells separated by '||' inside one line
                for cell in content.split("||"):
                    cell = cell.strip()
                    if cell:
                        cur.append(cell)
            else:
                if stripped:
                    if cur:
                        out_rows.append(" \t ".join(cur))
                        cur = []
                    out_rows.append(stripped)
        if cur:
            out_rows.append(" \t ".join(cur))
        return "\n".join(out_rows)
    text = re.sub(r"\{\|.*?\|\}", _table_strip, text, flags=re.DOTALL)
    # Remove HTML comments
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    # Remove ref tags
    text = re.sub(r"<ref[^>]*?/>", "", text)
    text = re.sub(r"<ref[^>]*?>.*?</ref>", "", text, flags=re.DOTALL)
    # Remove other html tags
    text = re.sub(r"<[^>]+>", "", text)
    # Remove file/image links
    text = re.sub(r"\[\[(?:ملف|صورة|File|Image):[^\]]*\]\]", "", text, flags=re.IGNORECASE)
    # Convert wikilinks: [[target|display]] -> display, [[target]] -> target
    text = re.sub(r"\[\[([^\]|]*\|)?([^\]]*)\]\]", r"\2", text)
    # Convert external links [url text] -> text
    text = re.sub(r"\[https?://[^ \]]+ ([^\]]*)\]", r"\1", text)
    text = re.sub(r"\[https?://[^\]]+\]", "", text)
    # Remove headings markers
    text = re.sub(r"={2,}([^=]*)={2,}", r"\1", text)
    # Bold/italic
    text = re.sub(r"'''([^']*)'''", r"\1", text)
    text = re.sub(r"''([^']*)''", r"\1", text)
    # Collapse whitespace
    text = re.sub(r"[ \t]+", " ", text)
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text.strip()


def fetch_save(title: str, slug: str) -> int:
    raw = api_get(title)
    if not raw:
        print(f"  EMPTY: {title}", file=sys.stderr)
        return 0
    plain = strip_wiki(raw)
    (OUT / f"{slug}.raw.txt").write_text(raw, encoding="utf-8")
    (OUT / f"{slug}.txt").write_text(plain, encoding="utf-8")
    return len(plain)


TARGETS = [
    # Mu'allaqat - using known Wikisource titles
    ("معلقة امرئ القيس", "muallaqa-imru-al-qais"),
    ("معلقة طرفة بن العبد", "muallaqa-tarafa"),
    ("معلقة زهير بن أبي سلمى", "muallaqa-zuhayr"),
    ("معلقة لبيد بن ربيعة", "muallaqa-labid"),
    ("معلقة عمرو بن كلثوم", "muallaqa-amr-bin-kulthum"),
    ("معلقة عنترة بن شداد", "muallaqa-antara"),
    ("معلقة الحارث بن حلزة اليشكري", "muallaqa-harith"),
]

if __name__ == "__main__":
    for title, slug in TARGETS:
        n = fetch_save(title, slug)
        print(f"{slug}: {n} chars")
