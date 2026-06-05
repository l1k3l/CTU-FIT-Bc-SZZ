#!/usr/bin/env python3
"""
parse_zkusenosti.py — extract usable student-experience data from the saved
FIT-Wiki "Otázky a zkušenosti ze SZZ" HTML pages in zkusenosti/.

Structure of each page (varies per file!):
  - A heading (H1 OR H2) whose text contains a parenthesised list of >=3 names
    is a COMMITTEE group, e.g. "3-BI-UI.21 - (Holeňa, Kleprlík, ...)".
  - A following H3 (sometimes H4) without such a list is a STUDENT entry,
    e.g. "Pufkova máma (BI-UI.21)". Its content runs until the next heading.

Output:
  - zkusenosti_parsed.json  : everything, structured.
  - stdout digest           : only committees containing MY examiners, with
    the relevant examiners highlighted; plus per-experience flags for which of
    my examiners are *named in the experience text itself*.

Usage:
  python3 parse_zkusenosti.py            # writes JSON + prints relevant digest
  python3 parse_zkusenosti.py --all      # digest of every committee
  python3 parse_zkusenosti.py --json-only
"""
import re, html as ihtml, glob, json, os, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
ZDIR = os.path.join(HERE, "zkusenosti")

# My committee. Petr is tricky: "Petr" is also a common FIRST name
# (Novák Petr, Petr Špaček...). Only count it as MY examiner Ivo Petr when it
# appears as a surname: "Ivo Petr", "Petr (Ivo)", "I. Petr", or "Petr," / ", Petr"
# inside a committee list that is NOT "Novák Petr"/"Petr Novák" etc.
MY = {
    "Holeňa":   r"Hole[ňn]a",
    "Dedecius": r"Dedeci",
    "Daňhel":   r"Da[ňn]hel",
    "Hunka":    r"Hunka",
    "Petr":     r"(?:Ivo\s+Petr|Petr\s*\(\s*Ivo\s*\)|\bI\.\s*Petr)",
}
# A looser Petr matcher for committee lists where only the surname is given.
PETR_SURNAME = re.compile(r"(?<![A-Za-zÁ-ž])Petr(?![A-Za-zÁ-ž])")
PETR_FIRSTNAME = re.compile(r"(Novák\s*\(?\s*[Pp]etr|Petr\s+Novák|Petr\s+Špaček|Petr\s+Klán|Petr\s+Fišer)")


def season_of(fn):
    m = re.search(r"SZZ\s+(\S+\s+\d{4})", unicodedata.normalize("NFC", fn))
    return m.group(1) if m else os.path.basename(fn)


def clean(s):
    s = re.sub(r"<br\s*/?>", "\n", s)
    s = re.sub(r"</(p|li|h[1-6]|ul|ol|div|tr|table|blockquote)>", "\n", s)
    s = re.sub(r"<li[^>]*>", "\n  - ", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = ihtml.unescape(s)
    s = re.sub(r"\[\s*upravit[^\]]*\]|\[\s*editovat[^\]]*\]|\[edit\]", "", s, flags=re.I)
    s = re.sub(r"[ \t]+", " ", s)
    s = re.sub(r"\n[ \t]+", "\n", s)
    s = re.sub(r"\n{3,}", "\n\n", s)
    return s.strip()


def _outer_paren(heading_text):
    # greedy: capture from first '(' to last ')' so nested "Petr (Ivo)" survives
    p = re.search(r"\((.*)\)", heading_text)
    return p.group(1) if p else None


def is_committee(heading_text):
    inside = _outer_paren(heading_text)
    return bool(inside and inside.count(",") >= 3)


def committee_examiners(heading_text):
    inside = _outer_paren(heading_text) or heading_text
    return [x.strip() for x in inside.split(",") if x.strip()]


def my_examiners_in(text):
    """Return set of canonical names of MY examiners mentioned in `text`."""
    found = set()
    for name, rx in MY.items():
        if name == "Petr":
            continue
        if re.search(rx, text):
            found.add(name)
    # Petr handling
    if re.search(MY["Petr"], text):
        found.add("Petr")
    elif PETR_SURNAME.search(text) and not PETR_FIRSTNAME.search(text):
        # bare "Petr" surname in a committee list, no "Novák Petr" etc.
        found.add("Petr?")
    return found


def parse_file(fn):
    h = open(fn, encoding="utf-8").read()
    # collect real heading elements in document order
    heads = []
    for m in re.finditer(r"<h([1-4])[^>]*>(.*?)</h\1>", h, re.S):
        txt = clean(m.group(2))
        if not txt or txt.lower() in ("obsah", "contents"):
            continue
        heads.append((int(m.group(1)), txt, m.start(), m.end()))
    season = season_of(fn)
    committees = []
    cur = None
    for i, (lvl, txt, s, e) in enumerate(heads):
        if txt == "Diskuze":
            break
        nxt = heads[i + 1][2] if i + 1 < len(heads) else len(h)
        body = clean(h[e:nxt])
        if is_committee(txt):
            cur = {"committee_raw": txt,
                   "examiners": committee_examiners(txt),
                   "my_in_committee": sorted(my_examiners_in(txt)),
                   "students": []}
            committees.append(cur)
        else:
            # student entry (skip the page title / template placeholder)
            if "JMENO_A_PRIJMENI" in txt or txt.startswith("Otázky a zkušenosti"):
                continue
            if cur is None:
                cur = {"committee_raw": "(no committee header)",
                       "examiners": [], "my_in_committee": [], "students": []}
                committees.append(cur)
            cur["students"].append({
                "student": txt,
                "experience": body,
                "my_named_in_text": sorted(my_examiners_in(body)),
            })
    return {"season": season, "file": os.path.basename(fn), "committees": committees}


def main():
    files = sorted(glob.glob(os.path.join(ZDIR, "*.html")))
    data = [parse_file(f) for f in files]
    with open(os.path.join(HERE, "zkusenosti_parsed.json"), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=1)

    if "--json-only" in sys.argv:
        print("wrote zkusenosti_parsed.json")
        return

    show_all = "--all" in sys.argv
    for page in data:
        relevant = [c for c in page["committees"]
                    if show_all or c["my_in_committee"]
                    or any(st["my_named_in_text"] for st in c["students"])]
        if not relevant:
            continue
        print("\n" + "=" * 78)
        print(f"### {page['season']}")
        for c in relevant:
            tag = ("  [MINE: " + "+".join(c["my_in_committee"]) + "]") if c["my_in_committee"] else ""
            print(f"\n## {c['committee_raw']}{tag}")
            for st in c["students"]:
                if not show_all and not c["my_in_committee"] and not st["my_named_in_text"]:
                    continue
                named = (" {named in text: " + "+".join(st["my_named_in_text"]) + "}") if st["my_named_in_text"] else ""
                print(f"\n--- {st['student']}{named} ---")
                print(st["experience"] if st["experience"] else "(no text)")


if __name__ == "__main__":
    main()
