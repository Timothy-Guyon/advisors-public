# Technical Advisor

The founder's Technical Advisor alone, as a Claude Code plugin: its text (`skills/technical-advisor/SKILL.md`), its principles (`skills/technical-advisor/principles/`) and one agent that reads them (`agents/technical-advisor.md`). Its shelf of source texts is left out, since those are copyrighted; each principle still names its source.

This repository is a mirror. Do not change it here: it is rebuilt from the private advisors repository on every change to the Technical Advisor there, and anything changed here is overwritten. Built from commit `2de2239`.

## Installing

- On every surface of a claude.ai account: Customize > Plugins > Add > Add marketplace, enter `Timothy-Guyon/advisors-public`, and add the `advisors` plugin.
- Claude Code on one machine: `/plugin marketplace add Timothy-Guyon/advisors-public`, then `/plugin install advisors@advisors-public`.
- Another tool that reads Agent Skills: put `skills/technical-advisor/` where that tool looks for skills.

The plugin is named `advisors`, like the full one, so the agent is `advisors:technical-advisor` here too, and the skill carries the same name. Install one or the other on an account, never both. It reads a project's `AGENTS.md` (or `CLAUDE.md`) for the product's facts and building rules, and a glossary where the project keeps one; without them it works from the principles alone.
