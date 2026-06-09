---
name: tune-question-from-experiences
description: Use when the user wants to refine or fine-tune an EXISTING SZZ question writeup against real student experiences and examiner question-history (e.g. "tune 29SAP to past experiences", "what do examiners actually want on 5DBS", "update the SAP questions from zkušenosti"). Only meaningful after the initial long+short writeup exists — drafting from scratch is add-question's job.
---

# Tune SZZ question writeup from past experiences

Refine an **existing** `[N][COURSE]-long.md` + `[N][COURSE]-short.md` so it covers what
examiners actually demand, using the saved FIT-Wiki student experiences (`zkusenosti/`)
and the question-history CSVs.

> **Prerequisite — run only after the initial writeup exists.** This skill *tunes*; it
> does not draft. If `[N][COURSE]-long.md` or `[N][COURSE]-short.md` is missing in
> `BI-SPOL/` or `BI-UI/`, **stop and use the `add-question` skill first**, then come back.

## Inputs

- **Question number + course** (e.g. `29 SAP`) — must match an existing pair of files.
- **(Optional) committee composition.** If known, weight findings by it. Default source:
  `komise.txt` / `komise-optimization-guide.md`.

## Workflow

1. **Regenerate the parsed experiences.** First **confirm the `MY` dict in `parse_zkusenosti.py`
   matches the user's committee** (surnames + regex; see `komise-optimization-guide.md`) — if not,
   fix it before running. Then run the stdlib-only Python 3 parser (no deps):
   ```bash
   python3 parse_zkusenosti.py --json-only   # writes zkusenosti_parsed.json
   ```
   `--json-only` is intentional: the default run prints a digest **filtered to your committee**,
   but for tuning ONE course you want **every** examiner who ever asked it, so you query the JSON
   directly in step 2 (don't rely on the committee digest). The parser reads every `zkusenosti/*.html`,
   so newly added pages are picked up automatically. `zkusenosti_parsed.json` and the digest are
   gitignored/regenerable — don't commit them. If the parser misses committees on a page (heading
   format drift), fix the parser, don't hand-edit the JSON.

2. **Pull ONLY the rows relevant to this course/question.** Ignore everything else.
   - **CSVs** — keep rows whose **`Předmět` = COURSE**, AND:
     - `question_history1.csv`: `Zkoušející, Rok, Oborová, Předmět, Otázka, Známka, Poznámka` (no header row).
     - `question_history2.csv`: `Zkoušející, Rok, Obor, Oborová, Předmět, Otázka` (has header).
     - **Don't trust `Předmět` alone** — some rows leave it blank or file the course under a
       different obor section. Also keep rows whose **`Otázka` text matches the topic** (when
       `Předmět` is blank, classify the row by its `Otázka` wording), and **always pull every row
       by each committee examiner's name** (a literal `Předmět=COURSE` filter silently dropped all
       of the committee DBS examiner's rows in testing).
   - **Parsed JSON** — extract every **examiner-attributed** block mentioning the course:
     match lines like `^<Name>: (BI-)?<COURSE>` inside each student's `experience`, and
     capture the **question text, its narrowing** ("zaměřte se na…") **and the follow-up
     grilling** ("doptal se…", "ptal se…"). The narrowing + follow-ups are the strongest signal.
   - **Map by TOPIC, not number** — question numbers drift across years (e.g. `SPOL-28`↔`29`).
     Match on the topic wording, not the digit. **The target question's own scope line / exam
     wording is authoritative** for what belongs — even if `Komise-*-analýza.md` or `STUDY_PLAN`
     loosely lump topics under a different number.
   - **Topic in the data but no file for it?** A course often has more exam questions than this
     vault has writeups. If matched experiences cover a course topic that has **no
     `[N][COURSE]` file** (e.g. normalization or ER→relational transformation when only the
     relational-algebra/SQL question exists), **do NOT fold them into this question.** List them
     **in your report only** (not as notes in the question file) as "out of scope for this question
     — candidate for `add-question`" and move on.

3. **Build the examiner picture.** Across all matched data, separate:
   - **Hard-required** — facts / derivations / algorithms asked by **multiple** examiners,
     **recently**, or that examiners explicitly **narrow to** or **doptávají**.
   - **Relaxed / droppable** — sub-topics never once asked across many years, or **explicitly
     waved off** ("nechtěl posuvy…", "stačilo říct…").
   - **Weight by committee + recency.** An examiner on the user's committee and a recent
     (e.g. 2024–2026) entry outweigh an old, unrelated one. Committee *membership* ≠ who
     examines you — only ~2 of 5 examine each student, so the **attributed** question matters
     more than the roster. **When recency and attribution conflict, attribution wins:** a
     detailed grilling by *your* committee examiner from a few years back beats a recent entry
     from someone who won't examine you (recency only breaks ties among comparable evidence).
   - **Surface evidence counts.** Note **how many** experiences / CSV rows back each finding;
     flag single anecdotes as weak (don't treat one story as a pattern).
   - Capture **per-examiner style**: typical narrowings, favourite follow-ups, strictness.

4. **Verify, then update (apply additions, propose cuts).**
   - **Verify every fact against the lecture PDFs in `materials/<COURSE>/` BEFORE adding it.**
     Student recollections are anecdotal and sometimes wrong — verifying against the slides is
     how the SAP pass caught a fetch/execute grouping error. PDF wins. If something is genuinely
     beyond the slides but examiners still want it, add it clearly marked
     `> *Doplnění nad rámec slidů:*`.
   - **Additions — apply directly.** Add the verified hard-required facts/theorems/algorithms to
     **both** the long and short versions (short stays definition-only, handwriting-ready). Give
     each long file a **`### Typické doplňující otázky (doptávání)`** subsection **at the end, inside
     the "Co je potřeba na zkoušku znát" section**; format each entry as
     `- **<Examiner>:** "<otázka/doptání>" → §<n>` (the recurring follow-up + a pointer to the
     section that answers it). Respect the short version's ~20-min handwriting budget — if it
     overflows, that itself signals a heavy topic.
   - **Removals — propose, never cut unprompted.** List "never asked / explicitly not required"
     candidates and **ask the user before deleting**. Keep foundational definitions even if examiners
     don't hammer them.
   - **Don't duplicate — but distinguish "mentioned" from "drilled".** Check the files first. A term
     present only as a keyword (e.g. `USING` in a syntax list) when examiners drill its *nuance*
     (e.g. "USING is safer than NATURAL JOIN but isn't in RA") is NOT covered — **sharpen it in place**
     rather than re-adding a duplicate or skipping it. This skill is re-runnable as new experiences arrive.
   - **Content covered via an embedded `![[Pojmy/…]]` note counts as "mentioned", not "drilled".** If
     examiners drill detail the embed only lists (e.g. state-transition triggers it merely names),
     add the sharpening **to the question file**, around the embed. **Never edit the shared `Pojmy/`
     note to satisfy one question** — it would change every other question that embeds it. (If the
     canonical definition itself is genuinely wrong/incomplete for *all* courses, that's a separate
     `Pojmy/` fix to raise with the user, not part of tuning one question.)

5. **Report + commit.** Summarise the evidence: hot topics, per-examiner notes, what to de-emphasise,
   and the sample size behind each claim. Commit per question (Czech/English imperative):
   `Tune <N><COURSE> from experiences`. Commit only when the user asks.

## Anti-patterns

- Adding a "fact" because a student claimed it, without checking the PDF.
- Treating committee membership as "who examines you" — the *attributed* question is the real signal.
- Matching by question number instead of topic (numbers drift across years).
- Deleting content the user didn't approve; over-trimming foundational definitions.
- Letting the short version balloon past the handwriting budget.
- Drafting a missing writeup here instead of redirecting to `add-question`.

## Reference

- Parser, data layout, committee weighting: `komise-optimization-guide.md`
- Drafting (prerequisite) skill: `add-question`
- Worked examiner/committee analysis: `Komise-2026-analýza.md`
