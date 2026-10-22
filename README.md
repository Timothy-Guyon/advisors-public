# Technical Advisor

The founder's Technical Advisor alone, as a Claude Code plugin: its text (`skills/technical-advisor/SKILL.md`), its principles (`skills/technical-advisor/principles/`) and one agent that reads them (`agents/technical-advisor.md`). Its shelf of source texts is left out, since those are copyrighted; each principle still names its source.

This repository is a mirror. Do not change it here: it is rebuilt from the private advisors repository on every change to the Technical Advisor there, and anything changed here is overwritten. Built from commit `2cebcdb`.

## Installing

- On every surface of a claude.ai account: Customize > Plugins > Add > Add marketplace, enter `Timothy-Guyon/technical-advisor`, and add the `technical-advisor` plugin.
- Claude Code on one machine: `/plugin marketplace add Timothy-Guyon/technical-advisor`, then `/plugin install technical-advisor@technical-advisor`.
- Another tool that reads Agent Skills: put `skills/technical-advisor/` where that tool looks for skills.

The agent is `technical-advisor:technical-advisor`, and the skill carries the same name. It reads a project's `AGENTS.md` (or `CLAUDE.md`) for the product's facts and building rules, and a glossary where the project keeps one; without them it works from the principles alone.
