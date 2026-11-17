#!/bin/sh
# Printed at the start of every session by the public copy's plugin, so a
# thread on an account without the private repositories knows the working
# rules and how its notes on them get back.
here=$(cd "$(dirname "$0")" && pwd)
cat <<TXT
Working with Timmy: follow the rules in $here/rules/AGENTS.md (read it once per session).
This copy has no shared log. Whenever Timmy corrects how you work with them, or says they liked how you did something, keep a note in this session. When a note states a general point, or three notes say the same thing, draft a "Rule candidate" issue for Timothy-Guyon/timmys-tools-public in general terms (nothing about the employer, its product, code, customers or people), show Timmy the draft, and file it only on their word. How: "Sending a lesson back" at the end of any advisor's skill.
TXT
