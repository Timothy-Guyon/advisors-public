---
name: write-like-timmy
description: Writes in Timmy's own voice anything he puts his name to, such as emails, texts, DMs, replies, social media posts, documents and write-ups for work, bios and cover notes, and learns from what he picks and changes. Use whenever Timmy asks for writing he will send, post, publish or share as himself, or says "write like me", "in my voice", "draft a reply" or "write this up for me". Not for an agent's own replies to Timmy, and not for code, commit messages or the records a session keeps for its own work unless he asks for his voice there.
---

# Write like Timmy

Timmy's voice is in `voice.md`, beside this file: the target in his words, his rules, and habits seen in his writing. This file is the way to draft with it and the way it grows. It needs no other skill.

It is for all of his writing, not only messages: "It could be for writing anything, like documents for work, social media posts, messages, whatever" (Timmy, 2026-11-17). Below, "the piece" is whatever is being written: a text, an email, a post, a document.

Every path here is relative to this skill's folder, the one holding this file; run the script by its full path, from the project's folder.

Why it is built this way: a description of someone's style, however good, makes a caricature when a model is told to follow it. What works is his real substance going in, his reactions to drafts coming out, and each reaction kept as a small correction. So the voice file starts short and grows only from what Timmy picks, changes and says.

## Drafting

1. **Read `voice.md`, all of it,** then run `python3 scripts/voice.py status`. It says whether to show two drafts or one.

2. **Get what he wants to say before how to say it.** Note for yourself what the piece has to carry: who it is for, what he wants from them, the facts, the dates, his answer. For a document or a post, also the point it makes and what the reader should know or do at the end. Anything only Timmy knows and has not said, ask him, one plain question at a time. Never fill a gap with something plausible: a made-up detail in a convincing voice is the worst draft there is, because it reads as his. A short ask is fine when everything is in it ("tell Sam I can't make Saturday, offer Sunday").

3. **Read what this place can see.** For a message: the one he is answering and, where this session can reach them, a few of his own earlier messages to the same person or of the same kind (his sent mail, the chat). Match how the two of them already talk: how long, how formal, whether there is a greeting. For a document or a post: one or two of his own earlier ones of the same kind, and the template or the place it will sit in, where there is one. Match how that kind is laid out and how long it runs. Read all of it where it is, and never copy it into the log, the voice file or another repository.

4. **Write it** by the rules in `voice.md`. Fit the length to the medium and to what he is answering: a two-line text gets a short text back. A document takes the shape its kind calls for, such as headings, or a list where there are several items, and the sentences inside that shape are still his. Use only what step 2 gave you: no fact, reason, plan, story or joke he did not give you. An ordinary friendly line ("thanks!", "sorry to miss it") is not an invention; a made-up reason for missing it is.

5. **Show two drafts that differ in one way** while `status` says two: shorter against fuller, with a greeting against without, warmer against plainer. Label each with that one difference ("A, shorter", "B, with a line of thanks") and say nothing more about them, so his pick teaches one thing. For a long piece, such as a document or a long post, show the two ways on its opening or on one short section, not as two whole documents, then write the rest the way he picks. When `status` says one, show one. "One" or "two" from Timmy wins either way.

6. **Sending, posting and publishing are his.** Show a draft the way this harness shows one for approval: a draft card for a message, a document or a file for a document. Send, post or publish only on his word.

## After he answers

Log every pick, edit and remark the same day, one note per lesson:

    python3 scripts/voice.py note --kind pick|edit|said --for "<kind of writing>" --draft "<what the draft did>" --timmy "<what he chose, changed or said>" [--before "<fragment>" --after "<fragment>"]

- **pick**: he chose one of two. Log the one difference and which side he took.
- **edit**: he changed a draft, or sent or published something different. Compare his version with the draft; each distinct change is its own note, with a short fragment before and after.
- **said**: he said something about how a draft sounds ("too stiff", "I'd never say that"). `--timmy` is his words.

Only the lesson goes in. No names, no private facts, and at most a fragment of a sentence, with any name swapped for "[name]". `--for` names the kind of writing, never the person or the subject ("text to a friend", "email to a business", "document for work", "public post"). The piece itself stays where it was written.

The log is `voice/LOG.md` in the mailbox repo (`Timothy-Guyon/claude-shared`): pull it first, and push the log straight to its `main`.

## How the voice grows

1. **Three alike make a rule, proposed right away.** After logging, run `python3 scripts/voice.py open`. When three open notes show one way of writing, put the rule to Timmy at once, on a decision card where the harness has one: accept, edit or strike, quoting the three notes. A point he states outright in his own words needs no three.
2. **A rule says what to do instead.** Every rule in `voice.md` carries what it replaces: the fragment that was wrong and what he did instead, taken from the notes. A rule that only forbids is not ready.
3. **An accepted rule becomes a pull request** on `voice.md` in Timmy's Tools (`Timothy-Guyon/timmys-tools`) with his decision quoted, and `python3 scripts/voice.py used <note numbers> --rule <rule number>` marks the notes. A struck proposal is marked `--rule struck`, so those notes stop counting. Only Timmy merges.
4. **A rule that stops fitting goes back to him.** If he overrules a rule twice, log it as a `said` note naming the rule, and put the change or strike to him the same way.
5. **Examples are his real writing, added only on his word.** A message, a post or a passage of a document. For each he says whether it may ship in the public copy. Public ones go under "Examples" in `voice.md`; the rest go in `voice/examples.md` of the mailbox repo and are read from there where it can be reached.

## Learning from what a place can see

Each place this skill is installed can see different writing of his: sent mail in one, dictation history on his Mac, work chat and documents on a work laptop. When Timmy asks a session to learn from what it can see, it reads that writing where it is and brings back only lessons: a habit with how often it shows, as a rule to propose, or a piece that shows his voice well, as an example for him to approve. The writing itself never leaves the place. Weigh what he did on purpose (an edit, a complaint) above what merely happened (a dictation quirk, a rushed reply).

## Checking against his real writing

Timmy wants both: drafts that follow his rules, and drafts that still read as his. `check.md` covers the second: it rewrites a few of his real pieces from their content alone and has a fresh judge say whether the voice file brought the drafts closer to what he wrote. Run it where his real writing can be read, when `status` says a check is due or when he asks.

## Without the mailbox

An account that cannot read Timmy's private repositories, such as a work account using the public copy, has no shared log. `voice.py` then keeps its log in `~/.timmy-voice/`, for that place only, and says so; where a session's files do not last, keep the notes in the session. Lessons go back as an issue on the public mirror, `Timothy-Guyon/advisors-public`, with its "Rule candidate" template, one rule per issue: when three notes there are alike, or he states a point outright, draft the rule in general terms with what to do instead, show Timmy the draft, and file it only on his word. Nothing about an employer, its product, its customers or its people, and no fragment of a work message or document, since the issue is public. A lesson that cannot be told without those stays where it was learned.
