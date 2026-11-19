# Timmy's Tools (public copy)

The tools Timmy uses in every project, minus the private parts, as one Claude Code plugin:

- **Three advisors** (`skills/`, `agents/`): Lean (whether and when to build), Design (what people see and do) and Technical (how it is built), with the team charter that says who owns what and how disagreements get decided. A session-start hook prints what the charter says is due.
- **Working rules** (`rules/AGENTS.md`): how every thread works with Timmy, printed as a reminder at each session's start.
- **Write like Timmy** (`skills/write-like-timmy/`): drafts in Timmy's own voice anything he puts his name to: messages, posts, documents. Its `voice.md` holds his rules and only the examples he chose to publish.

Left out: the notes behind the voice and Timmy's own writing, the advisors' source books (copyrighted; each principle still names its source), the phone and menu bar alerts, and anything personal.

This repository is a mirror. Do not change it here: it is rebuilt from a private repository on every change there, and anything changed here is overwritten. Built from commit `d83fb13`.

Issues are the exception: they are how a user of this copy sends a lesson back. Open one with the "Rule candidate" template, one lesson per issue, in general terms only, since this repository is public. Each advisor's skill ends with "Sending a lesson back", which says how a session drafts and files one. A lesson about Timmy's writing voice goes the same way; `skills/write-like-timmy/SKILL.md` says how under "Without the mailbox".

## Installing

- On every surface of a claude.ai account: Customize > Plugins > Add > Add marketplace, enter `Timothy-Guyon/timmys-tools-public`, and add the `timmys-tools` plugin.
- Claude Code on one machine: `/plugin marketplace add Timothy-Guyon/timmys-tools-public`, then `/plugin install timmys-tools@timmys-tools-public`.
- Another tool that reads Agent Skills: put the folders in `skills/` where that tool looks for skills.

The agents are `timmys-tools:lean-advisor`, `timmys-tools:design-advisor` and `timmys-tools:technical-advisor`, and the skills carry the same names, with the team charter as `timmys-tools:team-charter`. Install this or the private plugin on an account, never both. A project points at the working rules with one line in its own `AGENTS.md`: "Also follow rules/AGENTS.md in the Timothy-Guyon/timmys-tools-public repo: how to work with Timmy."
