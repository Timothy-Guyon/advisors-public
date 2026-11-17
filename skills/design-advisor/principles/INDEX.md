# The principles

Two files. `top-tier.md` holds what every screen is checked against first: Apple's eight design principles, then Nielsen's ten usability heuristics as a cross-check (the founder, 2026-11-05). `design.md` holds the claims about what a screen requires of the person using it, filed under the Apple principle each serves, as its evidence. The tier comes from authoritative, general sources, never from one screen's failures.

A claim is one bold sentence, what it means in two or three more, its check as a question, and its sources on the shelf, `reference/`, cited by page title and heading (a guideline), number and name (a criterion), chapter and section (a book) or title (a study), with the file's path. Above it, one line: what on a screen calls for it, and the Nielsen heuristic it also answers. Under it, on a line of its own, an example, not part of the claim: one premise from an everyday app, never this one, with a pass and a fail that differ only in what the claim is about (the founder, 2026-10-15). A claim says what a screen does, never only what it avoids: a bad screen is answered by what to do instead (the founder, 2026-11-05). A claim is general: it says nothing about the work of the moment, so it holds whatever is being built. A claim lives in exactly one place, and the same claim made by two texts is written once, with both as its sources.

The Design Advisor (`../SKILL.md`) proposes a claim with its source, its Apple principle, its Nielsen heuristic and its triggers, and the founder accepts or strikes it. An accepted claim is written to `design.md` by the session on the founder's word, in a commit that names it; a struck one is deleted.

| File | The question |
|---|---|
| `top-tier.md` | Does this screen hold up to Apple's eight design principles, and to Nielsen's ten heuristics? |
| `design.md` | What does a screen require of the person using it? |

## The triggers

What on a screen calls for a claim. A review lists which of these the screen has, from the screen as a person meets it, and pulls every claim with one of them, with every claim marked `every screen`. A new claim takes one or more of these; a new trigger is added only where a claim needs one none of these names.

| Trigger | The screen has |
|---|---|
| every screen | anything at all: these claims are read on every screen |
| new | a new screen, or a new action on one, being designed |
| change | a change that moves or removes something people have learned |
| controls | buttons, toggles or other controls to tap or drag |
| entry | a field, a picker or a question the person answers |
| errors | an entry that can be refused, or a fault the person is told of |
| steps | a task over more than one step or screen, or a choice that forks |
| covers | a view over the screen: a sheet, an alert, a dialog, a full-screen view |
| loses | an action that deletes, discards or could lose what the person kept or entered |
| list | a list, a set of options or items to scan, mark or choose among |
| wait | loading, slow work, a network, or a time limit |
| motion | animation, dragging, flicking, or a gesture |
| colour | a colour that carries a meaning |
| text | running text, a set of facts, or words to read beyond labels |
| sound | sound, haptics, speech or video |
| numbers | numbers, amounts, dates, times, counts or streaks |
| account | signing in, an account, personal data, privacy or consent |
| generated | a value or text the app guessed, suggested, worked out or generated |
| glance | use while the person's attention is mostly elsewhere |
| keyboard | a hardware keyboard, focus moving item by item, a pointer, or a switch |
| pushes | reminders, notifications or messages the app sends unasked |
| settings | settings or options the person sets |
| navigation | links or routes to other places in the app or outside it |

## How a screen is reviewed

1. **The whole screen, as a person first meets it.** After any change that adds or moves something, the review is of the whole screen from a phone-size screenshot, never only the piece that changed.
2. **The top tier, every item.** Each of Apple's eight, then each of Nielsen's ten, gets its check answered in a sentence from what the screenshot shows.
3. **The claims the screen calls for.** List the triggers the screen has, pull the claims marked with any of them and those marked `every screen`, and read each claim's check. Nothing else is read unless the screen shows a problem none of these covers.
4. **The record.** Each item and claim applied, and each skipped, is written with why, through the team's writer (`team.py review`), which refuses a review that leaves one out. The record is what a later miss is traced against.
5. **A finding says what to do instead.** Each finding names the claim it rests on and the smallest change that answers it, described closely enough to be drawn.

A problem the founder or a tester meets that no review flagged is a miss, written with `team.py miss` against the claim that should have caught it and with what the screen does instead; a claim missed twice is proposed to the founder as one read on every screen, and a miss no claim covers is answered by a proposed claim. A screen with known problems joins the project's replay set (`team.py replay`, screenshot in `product/replay/`), each problem with what the screen does instead; a change to how claims are picked or applied is adopted only once a review by it catches every problem in the set.

The founder's approval settles a call of taste and is recorded as taste. On a claim that rests on evidence, the founder's word is recorded as a decision with its reasoning (a pushback or an overrule), and the claim is judged by what goes wrong in use, so the advisor does not learn only to agree (the founder, 2026-11-05).
