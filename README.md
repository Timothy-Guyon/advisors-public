# Advisors (public copy)

The founder's advisors as a Claude Code plugin: the Lean, Design and Technical Advisors with their team charter (`skills/`), one agent for each (`agents/`), a session-start hook that prints what the charter says is due, and the rules every session follows when working with the founder (`rules/AGENTS.md`). The advisors' shelves of source texts are left out, since those are copyrighted; each principle still names its source.

Also here: `skills/write-like-timmy/`, which drafts in the founder's own voice anything he puts his name to: messages, posts, documents. Its `voice.md` holds his rules and only the examples he chose to publish; the notes behind it and his own writing are not in this copy.

This repository is a mirror. Do not change it here: it is rebuilt from a private repository on every change there, and anything changed here is overwritten. Built from commit `f6b0d30`.

Issues are the exception: they are how a user of this copy sends a lesson back. Open one with the "Rule candidate" template, one lesson per issue, in general terms only, since this repository is public. Each advisor's skill ends with "Sending a lesson back", which says how a session drafts and files one. A lesson about the founder's writing voice goes the same way; `skills/write-like-timmy/SKILL.md` says how under "Without the mailbox".

## Installing

- On every surface of a claude.ai account: Customize > Plugins > Add > Add marketplace, enter `Timothy-Guyon/timmys-tools-public`, and add the `timmys-tools` plugin.
- Claude Code on one machine: `/plugin marketplace add Timothy-Guyon/timmys-tools-public`, then `/plugin install timmys-tools@timmys-tools-public`.
- Another tool that reads Agent Skills: put the folders in `skills/` where that tool looks for skills.

The agents are `timmys-tools:lean-advisor`, `timmys-tools:design-advisor` and `timmys-tools:technical-advisor`, and the skills carry the same names, with the team charter as `timmys-tools:team-charter`. Install this or the private plugin on an account, never both. A project points at the working rules with one line in its own `AGENTS.md`: "Also follow rules/AGENTS.md in the Timothy-Guyon/timmys-tools-public repo: how to work with the founder."
