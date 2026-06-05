# SZZ — FIT ČVUT státní závěrečná zkouška (léto 2026)

Study materials for the **state final exam (státní závěrečná zkouška, SZZ)** at the
**Faculty of Information Technology, Czech Technical University in Prague**
(Fakulta informačních technologií ČVUT), for the **summer semester 2026**.

The materials cover **all shared exam questions** (`BI-SPOL`) and the
**Artificial Intelligence specialization** (`BI-UI`).

> Content is in **Czech** — the exam, the official question specs, and the source
> lecture PDFs are all Czech.

## Open it in Obsidian

This repository is an **[Obsidian](https://obsidian.md/) vault**. Clone it and open
the folder as a vault to get wikilinks, backlinks, the graph view, and the templates
that make the cross-references between notes navigable. It reads fine as plain
Markdown on GitHub too, but the linking experience is built for Obsidian.

```bash
git clone <repo-url>
# Obsidian → "Open folder as vault" → select the cloned directory
```

## Zettelkasten approach

The vault is organized as a **[Zettelkasten](https://en.wikipedia.org/wiki/Zettelkasten)**:
instead of duplicating definitions across questions, every recurring term
(graph, function, finite automaton, …) lives as a **single canonical concept note**
in `Pojmy/`, and each exam question links to it. This makes cross-course connections
explicit and keeps definitions in one authoritative place.

Full design rationale: [`docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md`](docs/superpowers/specs/2026-05-26-zettelkasten-vault-design.md).

## Repository layout

```
BI-SPOL/        shared exam-question summaries (flat) + BI-SPOL.21.csv spec
BI-UI/          AI-specialization summaries (flat)    + BI-UI.21.csv spec
Pojmy/          cross-course canonical concept notes (212 notes)
MOC/            maps of content — created on demand, not pre-seeded
Šablony/        Obsidian Templater templates (long / short / concept)
docs/           design specs
materials/      source PDFs only — GITIGNORED, kept locally
```

`materials/` (lecture PDFs and textbooks, one subfolder per course) is **git-ignored** —
it is the source of truth for the summaries but is not committed.

## Question specs (the CSV files)

The authoritative list of exam questions comes from the faculty and lives in two CSV
files (`;`-separated):

- [`BI-SPOL/BI-SPOL.21.csv`](BI-SPOL/BI-SPOL.21.csv) — **30** shared questions.
- [`BI-UI/BI-UI.21.csv`](BI-UI/BI-UI.21.csv) — **26** AI-specialization questions.

Each row gives the question number, its full Czech wording, and the source course.

## Per-question files

For each exam question there are two Markdown files, living **directly** in `BI-SPOL/`
or `BI-UI/` (no per-course subfolders):

| File | Purpose |
|------|---------|
| `[N][course]-long.md`  | Full version — definitions, theorems **with proofs**, algorithms/pseudocode, complexities, motivation, examples. Links/embeds `Pojmy/` concept notes. |
| `[N][course]-short.md` | Handwriting-ready cheat sheet — definitions only, no proofs/pseudocode, compact notation. ~1–2 sides of A4 for the 20-minute oral slot. |

Example: question 3 (`BI-AG1`) → `BI-SPOL/3AG1-long.md` + `BI-SPOL/3AG1-short.md`.

## Coverage

### BI-SPOL — shared questions (30)

| #     | Course   | Topic | Status |
|-------|----------|-------|--------|
| 1–2   | BI-AAG   | Automaty a gramatiky | ✅ |
| 3–4   | BI-AG1   | Algoritmy a grafy 1 | ✅ |
| 5–6   | BI-DBS   | Databázové systémy | ✅ |
| 7–8   | BI-DML   | Diskrétní matematika a logika | ✅ |
| 9–10  | BI-KAB   | Kryptografie a bezpečnost | ✅ |
| 11–12 | BI-LA1   | Lineární algebra 1 | ✅ |
| 13–14 | BI-MA1   | Matematická analýza 1 | ✅ |
| 15–16 | BI-MA2   | Matematická analýza 2 | ✅ |
| 17–18 | BI-OSY   | Operační systémy | ✅ |
| 19    | BI-PA1   | Programování a algoritmizace 1 | ✅ |
| 20–21 | BI-PA1 + BI-AG1 | Složitost, řazení, rozděl-a-panuj, dynamické programování | ✅ |
| 22–23 | BI-PA2   | Programování a algoritmizace 2 | ✅ |
| 24–25 | BI-PSI   | Počítačové sítě | ✅ |
| 26–27 | BI-PST   | Pravděpodobnost a statistika | ✅ |
| 28–30 | BI-SAP   | Struktura a architektura počítačů | ⬜ |

### BI-UI — AI specialization (26)

| #     | Course   | Topic | Status |
|-------|----------|-------|--------|
| 1–7   | BI-LA2   | Lineární algebra 2 | ✅ |
| 8–14  | BI-ML1   | Strojové učení 1 | ✅ |
| 15–20 | BI-ML2   | Strojové učení 2 | ✅ |
| 21–26 | BI-ZUM   | Základy umělé inteligence | ⬜ |

## Progress

- **BI-SPOL:** questions **1–27** drafted (long + short). Remaining: **28–30**
  (BI-SAP).
- **BI-UI:** questions **1–20** drafted (long + short). Remaining: **21–26**
  (BI-ZUM).
- **Pojmy:** 212 canonical concept notes.

## Concept notes (`Pojmy/`)

Atomic, canonical Czech notes for shared terms (`Graf.md`, `Funkce.md`,
`Konečný-automat.md`, …). Each carries Czech inflected forms as `aliases` so
`[[Graf|grafu]]` autocompletes from any grammatical case. Naming: singular nominative,
capitalized, dashes for multi-word terms.

## License

[MIT](LICENSE).
