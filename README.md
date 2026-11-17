# Advisors (public copy)

The founder's advisors as a Claude Code plugin: the Lean, Design and Technical Advisors with their team charter (`skills/`), one agent for each (`agents/`), a session-start hook that prints what the charter says is due, and the rules every session follows when working with the founder (`rules/AGENTS.md`). The advisors' shelves of source texts are left out, since those are copyrighted; each principle still names its source.

This repository is a mirror. Do not change it here: it is rebuilt from a private repository on every change there, and anything changed here is overwritten. Built from commit `fc502e1`.

Issues are the exception: they are how a user of this copy sends a lesson back. Open one with the "Rule candidate" template, one lesson per issue, in general terms only, since this repository is public. Each advisor's skill ends with "Sending a lesson back", which says how a session drafts and files one.

## Installing

- On every surface of a claude.ai account: Customize > Plugins > Add > Add marketplace, enter `Timothy-Guyon/advisors-public`, and add the `advisors` plugin.
- Claude Code on one machine: `/plugin marketplace add Timothy-Guyon/advisors-public`, then `/plugin install advisors@advisors-public`.
- Another tool that reads Agent Skills: put the folders in `skills/` where that tool looks for skills.

The agents are `advisors:lean-advisor`, `advisors:design-advisor` and `advisors:technical-advisor`, and the skills carry the same names, with the team charter as `advisors:team-charter`. Install this or the private plugin on an account, never both. A project points at the working rules with one line in its own `AGENTS.md`: "Also follow rules/AGENTS.md in the Timothy-Guyon/advisors-public repo: how to work with the founder."
