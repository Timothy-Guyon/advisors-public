# Checking the voice against his real messages

The rules in `voice.md` come from Timmy's reactions to drafts, and a set of rules can drift into a caricature of him without anyone noticing. This check asks one question: given the same content, is a draft written with the voice file closer to what Timmy really wrote than a draft written without it? It follows the test in Mike Taylor's "How I Finally Got AI to Write Like Me" (Every, 2026-11-16), where a style guide written from a reading of his posts made drafts less like him than no guide at all.

Run it only where his real messages can be read, and leave them there.

1. **Pick the messages.** Eight to twelve that he wrote to people, not to an assistant, each at least two sentences long, none of them an example in `voice.md` or the source of a rule. Prefer recent ones.
2. **Write a brief for each:** what the message had to carry (who it was for, what he wanted, the facts) and nothing of how he said it: none of his phrases, his order or his tone.
3. **Draft each twice from its brief alone,** once following `voice.md` and once with no voice file, in a fresh session or agent that has not seen the real message.
4. **Have a fresh judge compare.** It gets the real message and the two drafts, labeled 1 and 2 with nothing to say which is which, and answers which is closer to the real one in voice and, in a line, how each differs from it. Ask twice with the order swapped. A pair whose answer flips is a tie.
5. **Record it:** `python3 scripts/voice.py check --with <n> --without <n> --ties <n> --note "<what the judge's notes say most>"`.
6. **Tell Timmy what it found,** in two lines. If drafts without the voice file were closer more often, a rule is pulling drafts away from him: use the judge's notes to find which, and put it to him. Where a rule pulls away from his past writing because he asked for the change (shorter at work, more shape in casual messages), the rule is doing its job; say so, and his rule stands.

The judge's notes on how a draft differs from the real message are lessons like any other: one that repeats is a rule to propose, as "How the voice grows" in `SKILL.md` says.
