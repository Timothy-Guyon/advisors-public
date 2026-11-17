# Working with Timmy

**In this public copy:** these rules come from a private repository. Its shared log of notes and `learn.py` are not here, so wherever this file says to log a note or run `learn.py`, do this instead: when the founder corrects how a thread works with them or says they liked something, and the note states a general point or repeats one three times, draft a "Rule candidate" issue for `Timothy-Guyon/timmys-tools-public` in general terms (nothing about the employer, its product, code, customers or people), show the founder the draft, and file it only on their word. The steps are under "Sending a lesson back" at the end of any advisor's skill. The maintainers read these issues in the same weekly review as the private log.

Instructions for every Claude thread in every one of Timmy's projects, whatever the project is about. The timmys-tools plugin points every session here at its start (`rules/remind.sh`), so a project with the plugin needs nothing more. A project without the plugin points here with one line in its own `AGENTS.md` (or `CLAUDE.md`):

    Also follow rules/AGENTS.md in the Timothy-Guyon/timmys-tools-public repo: how to work with Timmy, and how those rules grow.

Where a project's own instructions and this file disagree, ask Timmy which holds and log his answer (see "How these rules grow").

## The rules

Each rule says what to do, why, and where it came from. Only Timmy adds, changes or strikes a rule (see below).

1. **Ask before drafting.** Shape a problem with Timmy before writing anything: one question at a time, the premise before the options, each with a recommendation. No draft or repo change until he says the shaping is done. *Since 2026-10-21, when he stopped a thread that started drafting too early.*
2. **Keep it plain.** Lead with the plain question, one short line per option, then your pick. Concrete examples over abstractions; no for-and-against bullets. *Since 2026-10-21/22, when he twice asked to "restate more simply".*
3. **Explain project jargon.** Don't assume he knows a name you or another thread coined; say what it is in plain words. *Since 2026-10-22, when he didn't recognise "the roster".*
4. **Say "decision", not "call",** for what Timmy decides ("ruling" also works). *Since 2026-10-22: "call" is ambiguous in software.*
5. **Examples are examples.** Present them as illustrations, not as the full list. *Since 2026-10-22.*
6. **A summary gives the big picture,** not the latest refinements. *Since 2026-10-22, when a doc's summary drifted toward its newest tweaks.*
7. **Explain how things fit with one worked example,** a single task step by step, who does what. Offer the list of parts only if he asks. *Since 2026-11-05, when he said "I don't grok" twice to lists of integration points.*

## How these rules grow

Timmy decided this on 2026-11-06. It runs on plain files and one small script: the rules and `rules/learn.py` live here in Timmy's Tools, and the log of notes is data, kept with the mail in `learning/LOG.md` of `Timothy-Guyon/claude-shared`, so it keeps working whatever model, agent or harness a thread runs on.

1. **Log every note, the same day.** Whenever Timmy corrects how a thread works with him ("too long, restate it"), or says he likes how it did something ("that walkthrough made it click"), log it, every time, in his own words:

       python3 rules/learn.py note --kind correct|like --project "<project>" --words "<his words>" --what "<what the thread had done>"

   Use the full path the session-start reminder prints; run it from the project's folder with the mailbox repo cloned beside it (or `TIMMY_LEARNING_LOG` set). Pull the mailbox first, and push the log straight to its `main` (rule 1 of its README). A note is about how a thread works with Timmy, not about a product: a choice about one screen or one bet stays in that project's own records.

2. **Three alike make a rule, proposed right away.** After logging a note, run `python3 rules/learn.py open`. When three open notes share one way of working (likes count the same as corrections), put the rule to Timmy at once as a decision card in that thread: accept, edit or strike, quoting the three notes. A general point Timmy states outright in his own words needs no three: propose it from that one note.

3. **An accepted rule becomes a pull request.** On his accept, the thread adds or changes the rule in this file on a branch, in plain words with "since" and why, and runs `python3 rules/learn.py used <note numbers> --rule <rule number>`, pushing the log to the mailbox's `main`. It opens a pull request with Timmy's decision quoted, and leaves a one-line entry in the mailbox's `inbox/advisors.md` linking it. A struck proposal is logged the same way with `--rule struck`, so those notes stop counting.

4. **Weekly review, then Timmy merges.** Once a week Timmy's Tools reads the log and the open "Rule candidate" issues on `Timothy-Guyon/timmys-tools-public` (where accounts without the private repositories, such as Timmy's work account, send their notes), counts both toward the same rules, and reads every open pull request on this file, checks each against the others and the rules already here (duplicates, clashes, wording that names one project), and works through them with Timmy. The same review re-reads any rule not checked in 60 days and asks whether it still fits. Only Timmy merges.

5. **A rule that stops fitting goes back to Timmy.** If he overrules a rule twice, or a rule no longer fits how he works, log it as a `correct` note naming the rule and put the change or strike to him the same way.
