# The principles

The principles the founder holds for how the app is built, one file per question the Technical Advisor is asked about the shape of a change. Each file holds claims. A claim is one bold sentence, what it means in two or three more, its check as a question, and its sources. A claim is general: it says nothing about the work of the moment, so it holds whatever is being built (the founder, 2026-10-13). A claim lives in exactly one file, and the same claim made by two texts is written once, with both as its sources.

The Technical Advisor (`../SKILL.md`) proposes a claim with its source, and the founder accepts or strikes it. An accepted claim is written to its file on the founder's word, in a commit that names it; a struck one is deleted. Before a code change, and again at review, the checks are read down the files in this order.

| File | The question |
|---|---|
| `words.md` | What is it called, and what does the code say? |
| `boundaries.md` | Where does it live, and what does it hide? |
| `model.md` | What kind of thing is it? |
| `errors.md` | What happens when it is wrong? |
| `craft.md` | How much design now, and what is left behind? |

The premise behind the engineering files is Ousterhout's: complexity is anything that makes the system hard to understand or to change. It shows three ways, a change that touches many places, a lot to know before touching anything, and not knowing what to touch at all, and it arrives by accumulation of small things, so it is resisted in small things (A Philosophy of Software Design, chapter 2, The Nature of Complexity).

The texts are on the Technical Advisor's shelf, `reference/`, listed in its `README.md`. A claim cites Evans by chapter (the shelf's `engineering/domain-driven-design/`, one numbered file per chapter), Ousterhout by chapter (`engineering/a-philosophy-of-software-design/`, one file per chapter named for its title; the preface and chapters 1 to 4 are there in a Chinese translation, and chapter 21 is not on the shelf), Fowler's pages by title (`engineering/martin-fowler/`), and Hunt and Thomas by topic of The Pragmatic Programmer's second edition, from memory, since that book is not on the shelf yet. Atomic Design is cited by chapter (`atomic-design/`). The engineering claims were the founder's digest of 2026-10-08, baked in on their word, split into these files and checked against the shelf on 2026-10-13. Since 2026-10-14 the shelf is mined chapter by chapter: the Technical Advisor proposes what a chapter supports that the files do not yet hold, and the founder accepts or strikes each claim, one at a time.
