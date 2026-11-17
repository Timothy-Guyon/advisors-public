#!/usr/bin/env python3
"""The team's writer for a project's records: every record that has a shape goes through here, never by hand.

The records sit in three folders at the project's root, by how long each lives: product/ holds what is true of
the product today (PRODUCT.md, RULES.md, REPLAY.md), edited in place; history/ holds what happened and why
(LOG.md, DECISIONS.md, REVIEWS.md, MISSES.md), added to and never rewritten; work/ holds what is in hand
(BET.md, IDEAS.md, LATER.md), each thing there leaving when its job ends.

    python3 team.py coin WORD MEANING --bet N --where WHERE --date YYYY-MM-DD [--replaces WORD]
    python3 team.py park ITEM WHY TRIGGER --date YYYY-MM-DD [--by founder]
    python3 team.py prove WHAT "EARNED BY" --date YYYY-MM-DD
    python3 team.py entry --bet N --opened YYYY-MM-DD --closed YYYY-MM-DD --verdict VERDICT --shipped yes|no
    python3 team.py glossary [--write PATH]
    python3 team.py idea NAME --kind product|fix|craft --for WHO --problem P --evidence E --route bet|waits|list
                         --fit F --worth W --smallest S --date YYYY-MM-DD [--by founder|lean]
    python3 team.py rank NAME [NAME ...]
    python3 team.py shape NAME --story S --assumption A --metric M --date YYYY-MM-DD
    python3 team.py pick NAME --bet N --date YYYY-MM-DD
    python3 team.py pass NAME [NAME ...] --date YYYY-MM-DD
    python3 team.py archive NAME --why WHY --date YYYY-MM-DD
    python3 team.py revive NAME --how asked|evidence|match|'bet closed' --why WHY --date YYYY-MM-DD
    python3 team.py decide TITLE --kind tie|overrule|pushback --circumstances C --premise P --advice "ADVISOR: ..." [...]
                           --decision D --reason R --date YYYY-MM-DD [--rule N] [--prediction P] [--conceded C]
    python3 team.py settle N --as confirmed|disproved|moot --note NOTE --date YYYY-MM-DD
    python3 team.py rule TEXT --premise P --applies-when W --from N,N,N --date YYYY-MM-DD
    python3 team.py rule TEXT --premise P --applies-when W --from N --stated --words "FOUNDER'S WORDS" --date YYYY-MM-DD
    python3 team.py rule TEXT --premise P --applies-when W --said YYYY-MM-DD --stated --words "FOUNDER'S WORDS" --date YYYY-MM-DD
    python3 team.py applies N WHEN --date YYYY-MM-DD
    python3 team.py ruling N --as accepted|struck|edited|back --note NOTE --date YYYY-MM-DD [--text TEXT]
    python3 team.py overruled N --decision M --date YYYY-MM-DD
    python3 team.py review TITLE --screen S --screenshot PATH --change C --has T,T --applied "NAME: why" [...]
                           [--skipped "NAME: why" ...] --verdict V --date YYYY-MM-DD
    python3 team.py miss TITLE --what W --instead I --claim "CLAIM HEADING"|none [--review N] --by founder|tester
                         --date YYYY-MM-DD
    python3 team.py replay TITLE --screenshot PATH --breaks "CLAIM HEADING: what breaks it" [...] --instead I
                           --date YYYY-MM-DD
    python3 team.py due
    python3 team.py move

coin     writes one "Words coined" line into bet N's entry in LOG.md, in the fixed shape, and refuses a word
         already coined in any entry unless --replaces names the word it supersedes.
park     appends a complete row to the parking lot, LATER.md; a missing trigger or date is refused.
prove    appends a line to the canon, PRODUCT.md; "earned by" must name the bet.
entry    writes a new entry's skeleton at the top of the log, every section present and PENDING.
glossary projects every coined word, alphabetically, with the bet that coined it, the open bet's from the "Words
         coined" section of BET.md, and prints the conflicts:
         a word coined twice, a replaced word that was never coined, a line not in the shape, a "defined in"
         that names a file that does not exist. Nothing it prints is committed; the entries are the record.
idea     adds an idea to IDEAS.md with every triage answer; a missing answer is refused, craft is sent to the
         parking lot, a fix goes ahead, an idea the bet needs goes into the bet, one that depends on what the bet
         teaches waits for it, and a sixth idea on the list is refused until one is archived or two are merged.
rank     sets the list's order, first name first.
shape    fills an idea's user story, riskiest assumption and metric; none of the three may be empty.
pick     marks the idea that becomes the next bet.
pass     counts one more pass for each idea passed over at shaping; the third pass archives it.
archive  moves an idea off the list, with why (a merge says which idea it went into).
revive   brings an archived idea back: on the client's asking, on new evidence, or when a new idea matches it;
         or an idea that waited on a bet, once that bet has closed. It needs a place on the list, and its pass
         count starts again at zero.
decide   writes a decision to DECISIONS.md: the circumstances, the premise, what each advisor said, the decision
         and the reason, all required. An overrule also needs its prediction: what result would show the
         advice was right. A pushback is the client turning an advisor's answer down, changing it or
         questioning it, by a tap or in words; it needs what the advisor conceded (--conceded). Where the advisor
         concedes nothing and holds its advice, it is an overrule, with its prediction. A decision that follows
         an accepted rule names it with --rule.
settle   closes an open prediction as confirmed, disproved or moot, with a note.
rule     proposes a rule in RULES.md from three or more similar decisions, with its premise; --stated takes one
         decision, where the client stated the general point outright, and needs those words, verbatim
         (--words). A point stated while agreeing to an offer turns no advice down, so it has no decision:
         --said takes the date the client said it in place of --from.
ruling   records the client's word on a rule: accepted, struck, edited (with --text), or back for a fresh look;
         on a refresh, kept marks an accepted rule checked and still holding.
applies  writes when a rule applies, for a rule written before every rule carried it.
pack     writes each accepted rule as one file with title and applies_when, for a tool that reads rules that way.
overruled counts an overrule of an accepted rule; the second sends it back to the client.
review   records a Design Advisor review of a whole screen in REVIEWS.md: the screen, its screenshot, the change
         that added or moved something, what the screen has (--has, from the triggers in the Design Advisor's
         claims), each top-tier item and claim applied, each skipped, each with why, and the verdict. It refuses
         a review that leaves out any of Apple's eight, Nielsen's ten, a claim called for on every screen or a
         claim a trigger in --has calls for.
miss     records in MISSES.md a problem the client or a tester met that no review flagged, against the claim that
         should have caught it ("none" where no claim covers it), with what the screen does instead (--instead).
replay   adds a screen with known problems to REPLAY.md: its screenshot, kept in the project, each claim it breaks
         and what the fixed screen does instead.
due      prints what is due: open predictions, rules waiting on the client, accepted rules and when each applies,
         rules due a refresh, and "shape first"
         when no bet is open and ideas are waiting, a claim missed twice, a miss no claim covers, and any record
         still kept in product/ that belongs in history/ or work/. It prints nothing, and succeeds, where there
         is no product/.
move     moves each record still kept in product/ to its folder, history/ or work/, and says what it moved. It
         moves only the files the writer knows; the session moves the rest.

The prose inside an entry is the advisor's. The writer only places lines that have a shape.
Plain Python, nothing to install. The product/ it works from is, in order: --root; a product/ beside this script
(a project's own copy); product/ in the folder it runs in; product/ in $CLAUDE_PROJECT_DIR. history/ and work/
sit beside it. A record a project still keeps in product/ is read and written there until `move` moves it.
"""
import argparse
import datetime
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = None
DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
ENTRY = re.compile(r'^## Bet (\d+) \(opened (\d{4}-\d{2}-\d{2}), closed (\d{4}-\d{2}-\d{2}): ([^)]*)\)( PENDING)?\s*$')
SECTION = re.compile(r'^- \*\*([^*]+?):?\*\*')
COINED = re.compile(
    r'^  - \*\*(?P<word>[^*]+)\*\*: (?P<meaning>.+?) Defined in (?P<where>.+?); (?P<date>\d{4}-\d{2}-\d{2})\.'
    r'(?: Replaces \*\*(?P<replaces>[^*]+)\*\* \(bet (?P<rbet>\d+)\)\.)?$')
WORDS = 'Words coined'
OPEN = re.compile(r'^- \*\*Status:\*\* open, bet (\d+)\b')
SECTIONS = ['Bet', 'Baseline', 'Prediction', 'Shipped to', 'What happened', 'What we learned',
            'What we changed because of it', 'Craft spent', WORDS]
VERDICTS = ('confirmed', 'wrong', 'abandoned')


def fail(msg):
    sys.exit('team.py: ' + msg)


HOMES = {'LOG.md': 'history', 'DECISIONS.md': 'history', 'REVIEWS.md': 'history', 'MISSES.md': 'history',
         'BET.md': 'work', 'IDEAS.md': 'work', 'LATER.md': 'work'}


def home(name):
    """Where the record belongs: history/ or work/ beside product/, or product/ itself."""
    return os.path.join(os.path.dirname(ROOT), HOMES[name], name) if name in HOMES else os.path.join(ROOT, name)


def path(name):
    """The record's file: its own folder, or product/ where a project still keeps it there."""
    old = os.path.join(ROOT, name)
    if name in HOMES and os.path.exists(old) and not os.path.exists(home(name)):
        return old
    return home(name)


def read(name):
    with open(path(name), encoding='utf-8') as f:
        return f.read().split('\n')


def write(name, lines, added):
    if '@' in added:
        fail('an "@" would be written into %s; no email address goes into the records' % name)
    text = '\n'.join(lines)
    os.makedirs(os.path.dirname(path(name)), exist_ok=True)
    with open(path(name), 'w', encoding='utf-8') as f:
        f.write(text)


def date(s):
    if not DATE.match(s or ''):
        fail('the date must be written as YYYY-MM-DD, not %r' % s)
    try:
        datetime.date.fromisoformat(s)
    except ValueError:
        fail('%s is not a real date' % s)
    return s


def sentence(s, what):
    s = ' '.join((s or '').split())
    if not s:
        fail('%s is empty' % what)
    return s


def cell(s, what):
    s = ' '.join((s or '').split())
    if not s:
        fail('%s is empty' % what)
    return s.replace('|', '\\|')


def entries(lines):
    """Each log entry as (bet number, heading line index, end index exclusive)."""
    found = []
    for i, line in enumerate(lines):
        if not line.startswith('## '):
            continue
        if found and found[-1][2] is None:
            found[-1][2] = i
        m = ENTRY.match(line)
        if m:
            found.append([int(m.group(1)), i, None])
    for e in found:
        if e[2] is None:
            e[2] = len(lines)
    return [tuple(e) for e in found]


def sections(lines, start, end):
    """Top-level sections of one entry as (name, line index)."""
    out = []
    for i in range(start + 1, end):
        m = SECTION.match(lines[i])
        if m:
            out.append((m.group(1), i))
    return out


def words_in(lines, start, end, bet):
    """The lines under a "Words coined" section between start and end: the parsed fields, or 'bad'."""
    out = []
    secs = sections(lines, start, end)
    for n, (name, i) in enumerate(secs):
        if name != WORDS:
            continue
        stop = secs[n + 1][1] if n + 1 < len(secs) else end
        for j in range(i + 1, stop):
            line = lines[j]
            if not line.strip():
                continue
            m = COINED.match(line)
            if m:
                d = m.groupdict()
                d.update(bet=bet, index=j)
                out.append(d)
            else:
                out.append({'bet': bet, 'index': j, 'bad': line})
    return out


def coined(lines):
    """Every coined word on record: list of dicts with bet, line index, and the parsed fields or 'bad'."""
    return [c for bet, start, end in entries(lines) for c in words_in(lines, start, end, bet)]


def open_coined():
    """The open bet's words, written in BET.md's "Words coined" section in the log's line shape until the bet's retro
    moves them into its entry (Timmy, 2026-10-18); the bet is the one BET.md's status line names."""
    if not os.path.exists(path('BET.md')):
        return []
    lines = read('BET.md')
    bet = next((int(m.group(1)) for m in map(OPEN.match, lines) if m), None)
    start = next((i for i, line in enumerate(lines) if line.strip() == '## ' + WORDS), None)
    if bet is None or start is None:
        print(f"note: BET.md has no {'status line naming its bet' if bet is None else WORDS + ' section'}, so the open bet's words are not read", file=sys.stderr)
        return []
    end = next((i for i in range(start + 1, len(lines)) if lines[i].startswith('## ')), len(lines))
    return [dict(c, file='BET.md') for c in words_in(lines, start, end, bet)]


def defined_file(where):
    """The file a 'defined in' names, if its first token looks like one; None when it names no file."""
    token = where.split()[0].rstrip(',;:')
    if re.match(r'^[\w./-]+\.\w+$', token):
        return token
    return None


def file_exists(token):
    """True when the path is found under product/ or under any folder of the project around it; hidden folders
    and node_modules are not searched."""
    if os.path.exists(os.path.join(ROOT, token)):
        return True
    for top, dirs, _ in os.walk(os.path.dirname(ROOT)):
        dirs[:] = [d for d in dirs if not d.startswith('.') and d != 'node_modules']
        if os.path.exists(os.path.join(top, token)):
            return True
    return False


def end_of_entry(lines, start, end):
    """Index of the line after the entry's last non-blank line."""
    i = end
    while i > start + 1 and not lines[i - 1].strip():
        i -= 1
    return i


def cmd_coin(a):
    lines = read('LOG.md')
    word = sentence(a.word, 'the word').rstrip('.')
    meaning = sentence(a.meaning, 'the meaning')
    if not meaning.endswith('.'):
        meaning += '.'
    where = sentence(a.where, 'where it is defined').rstrip('.;')
    when = date(a.date)
    for part, what in ((word, 'the word'), (meaning, 'the meaning'), (where, 'where it is defined')):
        if 'Defined in' in part or 'Replaces **' in part:
            fail('%s holds the words "Defined in" or "Replaces **", which the line\'s shape uses; reword it' % what)
    token = defined_file(where)
    if token and not file_exists(token):
        fail('"defined in" names %s, and no such file exists under product/ or the repo' % token)
    found = [e for e in entries(lines) if e[0] == a.bet]
    if not found:
        fail('no entry for bet %d in LOG.md; write it first with "entry"' % a.bet)
    bet, start, end = found[0]
    on_record = {c['word'].casefold(): c for c in coined(lines) if 'word' in c}
    if word.casefold() in on_record and not a.replaces:
        c = on_record[word.casefold()]
        fail('"%s" is already coined in bet %d (LOG.md line %d); pass --replaces if this one supersedes it'
             % (word, c['bet'], c['index'] + 1))
    tail = ''
    if a.replaces:
        old = on_record.get(a.replaces.casefold())
        if not old:
            fail('--replaces names "%s", which no entry has coined' % a.replaces)
        tail = ' Replaces **%s** (bet %d).' % (old['word'], old['bet'])
    line = '  - **%s**: %s Defined in %s; %s.%s' % (word, meaning, where, when, tail)
    if not COINED.match(line):
        fail('the line would not read back in the shape; check the meaning and where for stray markup: %s' % line)
    secs = sections(lines, start, end)
    names = [s[0] for s in secs]
    if WORDS in names:
        n = names.index(WORDS)
        stop = secs[n + 1][1] if n + 1 < len(secs) else end_of_entry(lines, start, end)
        at = stop
        while at > secs[n][1] + 1 and not lines[at - 1].strip():
            at -= 1
        lines.insert(at, line)
    else:
        at = end_of_entry(lines, start, end)
        lines.insert(at, '- **%s:**' % WORDS)
        lines.insert(at + 1, line)
    write('LOG.md', lines, line)
    print('coined in bet %d: %s' % (bet, line.strip()))


def table_end(lines, name):
    """The line after the first table's last row; a second table in the file is left alone."""
    rows = [i for i, l in enumerate(lines) if l.startswith('|')]
    if len(rows) < 2:
        fail('%s has no table to append to' % name)
    end = rows[0]
    while end + 1 < len(lines) and lines[end + 1].startswith('|'):
        end += 1
    return end + 1


def cmd_park(a):
    lines = read('LATER.md')
    row = '| %s | %s | %s | %s, %s |' % (cell(a.item, 'the item'), cell(a.why, 'why it is tempting'),
                                        cell(a.trigger, 'the trigger'), date(a.date), cell(a.by, 'who parked it'))
    lines.insert(table_end(lines, 'LATER.md'), row)
    write('LATER.md', lines, row)
    print('parked: ' + row)


def cmd_prove(a):
    lines = read('PRODUCT.md')
    earned = cell(a.earned_by, 'earned by')
    if not re.search(r'\bBet \d+\b', earned):
        fail('"earned by" must name the bet that earned it, as "Bet N"')
    row = '| %s | %s | %s |' % (cell(a.what, 'what'), earned, date(a.date))
    lines.insert(table_end(lines, 'PRODUCT.md'), row)
    write('PRODUCT.md', lines, row)
    print('proved: ' + row)


def cmd_entry(a):
    lines = read('LOG.md')
    if a.verdict not in VERDICTS:
        fail('the verdict is one of %s' % ', '.join(VERDICTS))
    if a.shipped not in ('yes', 'no'):
        fail('--shipped is yes or no')
    opened, closed = date(a.opened), date(a.closed)
    if closed < opened:
        fail('closed before opened')
    found = entries(lines)
    if any(e[0] == a.bet for e in found):
        fail('bet %d already has an entry' % a.bet)
    heading = '## Bet %d (opened %s, closed %s: %s, %s) PENDING' % (
        a.bet, opened, closed, a.verdict, 'shipped' if a.shipped == 'yes' else 'not shipped')
    block = [heading, ''] + ['- **%s:** PENDING' % s for s in SECTIONS if s != WORDS] + ['- **%s:**' % WORDS, '']
    at = found[0][1] if found else len(lines)
    lines[at:at] = block
    write('LOG.md', lines, '\n'.join(block))
    print('entry written: ' + heading)


def sort_key(word):
    w = word.casefold()
    for art in ('the ', 'a ', 'an '):
        if w.startswith(art):
            w = w[len(art):]
    return w


def cmd_glossary(a):
    lines = read('LOG.md')
    words = coined(lines) + open_coined()
    good = [c for c in words if 'word' in c]
    bad = [c for c in words if 'bad' in c]
    at = lambda c: '%s line %d' % (c.get('file', 'LOG.md'), c['index'] + 1)
    out = ['# Glossary', '', 'Every word a bet coined, projected from the "Words coined" lines of `LOG.md`, and of `BET.md` '
           'for the open bet; the entries are the record, this is a view. A capital names a thing the app holds or shows; '
           'lowercase names a part or a fact (Timmy, 2026-10-07).', '']
    by_word = {}
    for c in good:
        by_word.setdefault(c['word'].casefold(), []).append(c)
    replaced = {c['replaces'].casefold(): c for c in good if c.get('replaces')}
    for c in sorted(good, key=lambda c: (sort_key(c['word']), c['bet'])):
        line = '- **%s**: %s Bet %d, %s. Defined in %s.' % (c['word'], c['meaning'], c['bet'], c['date'], c['where'])
        if c.get('replaces'):
            line += ' Replaces **%s** (bet %s).' % (c['replaces'], c['rbet'])
        r = replaced.get(c['word'].casefold())
        if r and r is not c:
            line += ' Replaced by **%s** (bet %d).' % (r['word'], r['bet'])
        out.append(line)
    conflicts = []
    for key, cs in by_word.items():
        cs = sorted(cs, key=lambda c: (c['bet'], c['index']))
        for earlier, later in zip(cs, cs[1:]):
            if (later.get('replaces') or '').casefold() != key:
                conflicts.append('"%s" is coined twice, in bet %d (%s) and bet %d (%s), and the later one '
                                 'does not say it replaces the earlier' % (earlier['word'], earlier['bet'], at(earlier),
                                                                            later['bet'], at(later)))
    for c in good:
        if c.get('replaces') and c['replaces'].casefold() not in by_word:
            conflicts.append('"%s" (bet %d) replaces "%s", which no entry has coined' % (c['word'], c['bet'], c['replaces']))
        token = defined_file(c['where'])
        if token and not file_exists(token):
            conflicts.append('"%s" (bet %d) is defined in %s, and no such file exists' % (c['word'], c['bet'], token))
    for c in bad:
        conflicts.append('bet %d, %s, is under "Words coined" and not in the shape: %s'
                         % (c['bet'], at(c), c['bad'].strip()))
    for i, line in enumerate(lines):
        if line.startswith('## Bet ') and not ENTRY.match(line):
            conflicts.append('LOG.md line %d is a bet heading not in the shape, so its words are not read: %s' % (i + 1, line.strip()))
    out.append('')
    out.append('## Conflicts' if conflicts else '## Conflicts: none')
    out.extend('- ' + x for x in conflicts)
    out.append('')
    out.append('%d words, %d conflicts.' % (len(good), len(conflicts)))
    text = '\n'.join(out) + '\n'
    if a.write:
        with open(a.write, 'w', encoding='utf-8') as f:
            f.write(text)
        print('written: %s (%d words, %d conflicts)' % (a.write, len(good), len(conflicts)))
    else:
        sys.stdout.write(text)
    return 1 if conflicts else 0


RECORD = re.compile(r'^## (Idea|Decision|Rule|Review|Miss|Replay) (\d+)\b')
FIELD = re.compile(r'^- \*\*([^*]+?):\*\*(?: (.*))?$')
KINDS = ('product', 'fix', 'craft')
ROUTES = {'bet': 'in the bet', 'waits': 'waiting on the bet', 'list': 'listed'}
ON_LIST = ('listed', 'shaped')
LIST_MAX = 5
PASSES = 3
REFRESH_DAYS = 60
TEMPLATES = {
    'IDEAS.md': ['# Ideas', '',
                 'Every idea, with its triage answers, written by `team.py`. At most five are on the list (status listed or '
                 'shaped), ranked; an idea passed over three times is archived.', ''],
    'DECISIONS.md': ['# Decisions', '',
                     'Every decision the client made between advisors, or against one, written by `team.py`: the '
                     'circumstances, the premise, each advisor\'s advice, the decision and the reason. An overrule carries '
                     'its prediction until it is settled; a pushback says what the advisor conceded.', ''],
    'RULES.md': ['# Rules', '',
                 'Rules this project grew from its decisions, written by `team.py`. A rule is proposed from three similar '
                 'decisions, or from the client\'s own words stating it outright, quoted with it, says when it applies, and '
                 'holds only once the client accepts it; overruled twice, or its premise gone, it goes back to the '
                 'client. An accepted rule not checked in 60 days is due a refresh.', ''],
    'REVIEWS.md': ['# Design reviews', '',
                   'Every review of a whole screen by the Design Advisor, written by `team.py`: what the screen has, the '
                   'top tier and each claim it applied, each it skipped and why, and the verdict. The record a later '
                   'miss is traced against.', ''],
    'MISSES.md': ['# Design misses', '',
                  'Every problem the client or a tester met on a screen that no review flagged, written by `team.py`, '
                  'against the claim that should have caught it and with what the screen does instead. A claim missed '
                  'twice is due to be called for on every screen; a miss no claim covers is due a proposed claim.', ''],
    'REPLAY.md': ['# Replay set', '',
                  'Screens with known problems, written by `team.py`, each with its screenshot, the claims it breaks and '
                  'what the screen does instead. A change to how the Design Advisor picks or applies its claims is '
                  'adopted only once a review by it catches every problem here.', ''],
}


def load(name):
    """The file's lines; a records file that does not exist yet starts from its template."""
    if os.path.exists(path(name)):
        return read(name)
    if name in TEMPLATES:
        return list(TEMPLATES[name])
    fail('no %s in %s' % (name, ROOT))


def records(lines):
    """Each record as a dict: n, title (the heading after the number), start, end, and fields {name: line index}."""
    out = []
    for i, line in enumerate(lines):
        if line.startswith('## ') or line.startswith('# '):
            if out and out[-1]['end'] is None:
                out[-1]['end'] = i
        m = RECORD.match(line)
        if m:
            out.append({'n': int(m.group(2)), 'heading': line, 'title': line[m.end():].lstrip(':').strip(),
                        'start': i, 'end': None, 'fields': {}})
    for r in out:
        if r['end'] is None:
            r['end'] = len(lines)
        for j in range(r['start'] + 1, r['end']):
            m = FIELD.match(lines[j])
            if m:
                r['fields'][m.group(1)] = j
    return out


def get(lines, r, field):
    j = r['fields'].get(field)
    if j is None:
        return None
    return FIELD.match(lines[j]).group(2) or ''


def put(lines, r, field, value):
    """Sets a field's value in place, or adds it after the record's last field line."""
    text = ('- **%s:** %s' % (field, value)).rstrip()
    if field in r['fields']:
        lines[r['fields'][field]] = text
        return text
    if 'History' in r['fields']:
        at = r['fields']['History']
    else:
        at = max(list(r['fields'].values()) + [r['start']]) + 1
        while at < r['end'] and lines[at].startswith('  '):
            at += 1
    lines.insert(at, text)
    return text


def note(lines, r, field, text):
    """Adds a dated sub-line under a list field (History, Advice), creating the field when it is missing."""
    if field not in r['fields']:
        put(lines, r, field, '')
        r = refind(lines, r)
    at = r['fields'][field] + 1
    while at < len(lines) and lines[at].startswith('  - '):
        at += 1
    lines.insert(at, '  - ' + text)
    return text


def refind(lines, r):
    return next(x for x in records(lines) if x['n'] == r['n'])


def append_record(lines, block):
    while lines and not lines[-1].strip():
        lines.pop()
    lines.extend([''] + block + [''])


def next_n(recs):
    return max([r['n'] for r in recs] + [0]) + 1


def idea_name(r):
    return r['title']


def find_idea(lines, name):
    recs = records(lines)
    hit = [r for r in recs if idea_name(r).casefold() == ' '.join(name.split()).casefold()]
    if not hit:
        fail('no idea named "%s" in IDEAS.md' % name)
    return hit[0]


def status(lines, r):
    return (get(lines, r, 'Status') or '').split(',')[0].strip()


def on_list(lines):
    """The ideas on the list, in rank order."""
    recs = [r for r in records(lines) if status(lines, r) in ON_LIST]
    return sorted(recs, key=lambda r: int(get(lines, r, 'Rank') or 99))


def rerank(lines, order):
    """Writes ranks 1..n for the ideas named, in that order; every other idea loses its rank."""
    names = [idea_name(r).casefold() for r in order]
    for r in records(lines):
        key = idea_name(r).casefold()
        if key in names:
            put(lines, refind(lines, r), 'Rank', str(names.index(key) + 1))
        elif 'Rank' in r['fields']:
            put(lines, refind(lines, r), 'Rank', 'none')


def set_status(lines, r, value, when, why):
    put(lines, r, 'Status', value)
    note(lines, refind(lines, r), 'History', '%s: %s' % (when, why))


def cmd_idea(a):
    lines = load('IDEAS.md')
    name = sentence(a.name, 'the name')
    when = date(a.date)
    if a.kind == 'craft':
        fail('craft goes to the parking lot, LATER.md, with "park", not on the ideas list')
    if any(idea_name(r).casefold() == name.casefold() for r in records(lines)):
        fail('an idea named "%s" is already on record; revive it, or give this one its own name' % name)
    fields = [('Kind', a.kind), ('For whom', sentence(a.for_whom, 'for whom')),
              ('Problem', sentence(a.problem, 'the problem')), ('Evidence', sentence(a.evidence, 'how we know')),
              ('Route', a.route), ('Fit', sentence(a.fit, 'the fit')), ('Worth', sentence(a.worth, 'the worth')),
              ('Smallest version', sentence(a.smallest, 'the smallest version'))]
    if a.kind == 'fix':
        state, why = 'goes ahead', 'raised by the %s; a fix goes ahead' % a.by
    else:
        state, why = ROUTES[a.route], 'raised by the %s; route %s' % (a.by, a.route)
    listed = on_list(lines)
    if state == 'listed' and len(listed) >= LIST_MAX:
        fail('the list already holds %d ideas (%s); archive one, or merge two, first'
             % (LIST_MAX, ', '.join(idea_name(r) for r in listed)))
    n = next_n(records(lines))
    block = ['## Idea %d: %s' % (n, name), '- **Status:** %s' % state]
    if state == 'listed':
        block.append('- **Rank:** %d' % (len(listed) + 1))
    block += ['- **Raised:** %s, by the %s' % (when, a.by)] + ['- **%s:** %s' % f for f in fields]
    block += ['- **Passed over:** 0', '- **History:**', '  - %s: %s' % (when, why)]
    append_record(lines, block)
    write('IDEAS.md', lines, '\n'.join(block))
    print('idea %d, %s: %s' % (n, state, name))


def cmd_rank(a):
    lines = load('IDEAS.md')
    listed = on_list(lines)
    chosen = [find_idea(lines, n) for n in a.names]
    for r in chosen:
        if status(lines, r) not in ON_LIST:
            fail('"%s" is not on the list (status %s)' % (idea_name(r), status(lines, r)))
    keys = [idea_name(r).casefold() for r in chosen]
    if len(set(keys)) != len(keys):
        fail('an idea is named twice')
    order = chosen + [r for r in listed if idea_name(r).casefold() not in keys]
    rerank(lines, order)
    write('IDEAS.md', lines, '')
    for i, r in enumerate(order):
        print('%d. %s' % (i + 1, idea_name(r)))


def cmd_shape(a):
    lines = load('IDEAS.md')
    r = find_idea(lines, a.name)
    if status(lines, r) not in ON_LIST:
        fail('"%s" is not on the list (status %s); only a listed idea is shaped' % (idea_name(r), status(lines, r)))
    when = date(a.date)
    added = [put(lines, r, 'User story', sentence(a.story, 'the user story'))]
    added.append(put(lines, refind(lines, r), 'Riskiest assumption', sentence(a.assumption, 'the riskiest assumption')))
    added.append(put(lines, refind(lines, r), 'Metric', sentence(a.metric, 'the metric')))
    set_status(lines, refind(lines, r), 'shaped', when, 'shaped')
    write('IDEAS.md', lines, '\n'.join(added))
    print('shaped: ' + idea_name(r))


def cmd_pick(a):
    lines = load('IDEAS.md')
    r = find_idea(lines, a.name)
    if status(lines, r) != 'shaped':
        fail('"%s" is %s; only a shaped idea becomes a bet' % (idea_name(r), status(lines, r)))
    when = date(a.date)
    set_status(lines, r, 'bet %d' % a.bet, when, 'picked as bet %d' % a.bet)
    rerank(lines, [x for x in on_list(lines)])
    write('IDEAS.md', lines, '')
    print('bet %d: %s' % (a.bet, idea_name(r)))


def archive(lines, r, when, why):
    set_status(lines, r, 'archived', when, 'archived: ' + why)
    rerank(lines, on_list(lines))


def cmd_pass(a):
    lines = load('IDEAS.md')
    when = date(a.date)
    for name in a.names:
        r = find_idea(lines, name)
        if status(lines, r) not in ON_LIST:
            fail('"%s" is not on the list (status %s)' % (idea_name(r), status(lines, r)))
        count = int(get(lines, r, 'Passed over') or 0) + 1
        put(lines, r, 'Passed over', str(count))
        r = refind(lines, r)
        if count >= PASSES:
            archive(lines, r, when, 'passed over %d times' % count)
            print('archived, passed over %d times: %s' % (count, idea_name(r)))
        else:
            note(lines, r, 'History', '%s: passed over (%d of %d)' % (when, count, PASSES))
            print('passed over (%d of %d): %s' % (count, PASSES, idea_name(r)))
    write('IDEAS.md', lines, '')


def cmd_archive(a):
    lines = load('IDEAS.md')
    r = find_idea(lines, a.name)
    if status(lines, r) == 'archived':
        fail('"%s" is already archived' % idea_name(r))
    why = sentence(a.why, 'why')
    archive(lines, r, date(a.date), why)
    write('IDEAS.md', lines, why)
    print('archived: ' + idea_name(r))


def cmd_revive(a):
    lines = load('IDEAS.md')
    r = find_idea(lines, a.name)
    if status(lines, r) not in ('archived', 'waiting on the bet'):
        fail('"%s" is %s; only an archived or waiting idea comes back onto the list' % (idea_name(r), status(lines, r)))
    listed = on_list(lines)
    if len(listed) >= LIST_MAX:
        fail('the list already holds %d ideas; archive one first to make a place' % LIST_MAX)
    why = sentence(a.why, 'why')
    put(lines, r, 'Passed over', '0')
    set_status(lines, refind(lines, r), 'listed', date(a.date), 'back on the list (%s): %s' % (a.how, why))
    rerank(lines, listed + [refind(lines, r)])
    write('IDEAS.md', lines, why)
    print('back on the list: ' + idea_name(r))


def find_n(lines, kind, n, file):
    hit = [r for r in records(lines) if r['n'] == n and r['heading'].startswith('## %s ' % kind)]
    if not hit:
        fail('no %s %d in %s' % (kind.lower(), n, file))
    return hit[0]


def cmd_decide(a):
    lines = load('DECISIONS.md')
    when = date(a.date)
    title = sentence(a.title, 'the title')
    advice = [sentence(x, 'an advice line') for x in a.advice]
    for x in advice:
        if not re.match(r'^[^:]+: \S', x):
            fail('advice is written "ADVISOR: what it advised", not %r' % x)
    if a.kind == 'tie' and len(advice) < 2:
        fail('a tie needs the advice of each advisor that pulled apart, at least two')
    prediction = ' '.join((a.prediction or '').split())
    if a.kind == 'overrule' and not prediction:
        fail('an overrule needs its prediction: what result would show the advice was right')
    conceded = ' '.join((a.conceded or '').split())
    if a.kind == 'pushback' and not conceded:
        fail('a pushback needs what the advisor conceded; an advisor that holds its advice was overruled '
             '(--kind overrule, with its prediction)')
    if conceded and a.kind != 'pushback':
        fail('--conceded is for a pushback only')
    rule = (a.rule or '').strip().lower()
    if rule == 'none':
        rule = None
    elif rule.isdigit():
        rule = int(rule)
        rules = load('RULES.md')
        rr = find_n(rules, 'Rule', rule, 'RULES.md')
        if status(rules, rr) != 'accepted':
            fail('rule %d is %s; only an accepted rule is applied' % (rule, status(rules, rr)))
    else:
        fail('--rule is the accepted rule that applied, or "none" when the rules were checked and none fit')
    n = next_n(records(lines))
    block = ['## Decision %d (%s): %s' % (n, when, title), '- **Kind:** %s' % a.kind,
             '- **Circumstances:** %s' % sentence(a.circumstances, 'the circumstances'),
             '- **Premise:** %s' % sentence(a.premise, 'the premise'), '- **Advice:**']
    block += ['  - ' + x for x in advice]
    block += ['- **Decision:** %s' % sentence(a.decision, 'the decision'),
              '- **Reason:** %s' % sentence(a.reason, 'the reason')]
    if conceded:
        block.append('- **Conceded:** %s' % sentence(conceded, 'what the advisor conceded'))
    block.append('- **Rule applied:** %s' % (rule if rule is not None else 'none fit (rules checked)'))
    if prediction:
        block += ['- **Prediction:** %s' % prediction, '- **Prediction status:** open']
    append_record(lines, block)
    write('DECISIONS.md', lines, '\n'.join(block))
    print('decision %d: %s' % (n, title))


def cmd_settle(a):
    lines = load('DECISIONS.md')
    r = find_n(lines, 'Decision', a.n, 'DECISIONS.md')
    st = get(lines, r, 'Prediction status')
    if st is None:
        fail('decision %d has no prediction' % a.n)
    if st != 'open':
        fail('decision %d\'s prediction is already settled: %s' % (a.n, st))
    text = '%s, %s: %s' % (a.as_, date(a.date), sentence(a.note, 'the note'))
    put(lines, r, 'Prediction status', text)
    write('DECISIONS.md', lines, text)
    print('decision %d: %s' % (a.n, text))


def cmd_rule(a):
    lines = load('RULES.md')
    decisions = load('DECISIONS.md')
    if a.said and not a.stated:
        fail('--said is for a rule the client stated outright with no decision (--stated)')
    if a.said and a.from_:
        fail('--said is for a stated point with no decision; with a decision, name it with --from instead')
    if not a.from_ and not a.said:
        fail('--from names the decisions the rule grows from (or --stated --said, for a point the client stated with no decision)')
    said = date(a.said) if a.said else None
    try:
        nums = [int(x) for x in (a.from_ or '').split(',') if x.strip()]
    except ValueError:
        fail('--from is decision numbers separated by commas, as 3,5,8')
    if a.stated and not said and len(set(nums)) != 1:
        fail('--stated names the one decision in which the client stated the rule; %d named' % len(set(nums)))
    words = ' '.join((a.words or '').split())
    if a.stated and not words:
        fail('--stated needs the client\'s words that state the rule, verbatim (--words)')
    if words and not a.stated:
        fail('--words is for a rule the client stated (--stated)')
    if not a.stated and len(set(nums)) < 3:
        fail('a rule grows from three or more similar decisions; %d named (or --stated, from one the client stated outright)' % len(set(nums)))
    for n in nums:
        find_n(decisions, 'Decision', n, 'DECISIONS.md')
    when = date(a.date)
    n = next_n(records(lines))
    text = sentence(a.text, 'the rule').rstrip('.')
    block = ['## Rule %d: %s.' % (n, text), '- **Status:** proposed',
             '- **Premise:** %s' % sentence(a.premise, 'the premise'),
             '- **Applies when:** %s' % sentence(a.applies_when, '--applies-when, when the rule applies'),
             '- **From decisions:** %s' % (', '.join(str(x) for x in sorted(set(nums))) if nums
                                          else 'none, stated outright on %s' % said)]
    if words:
        block.append('- **Stated by the client:** "%s"' % words)
    block += ['- **Since:** %s' % when, '- **Overruled:** 0', '- **History:**', '  - %s: proposed' % when]
    append_record(lines, block)
    write('RULES.md', lines, '\n'.join(block))
    print('rule %d proposed: %s.' % (n, text))


def cmd_ruling(a):
    lines = load('RULES.md')
    r = find_n(lines, 'Rule', a.n, 'RULES.md')
    when = date(a.date)
    why = sentence(a.note, 'the note')
    if a.as_ == 'edited':
        text = sentence(a.text, '--text, the edited rule').rstrip('.')
        lines[r['start']] = '## Rule %d: %s.' % (a.n, text)
        r = refind(lines, r)
        new, what = 'accepted', 'edited and accepted: %s' % why
    elif a.as_ == 'kept':
        if a.text:
            fail('--text goes only with --as edited')
        if status(lines, r) != 'accepted':
            fail('rule %d is %s; only an accepted rule is kept on a refresh' % (a.n, status(lines, r)))
        put(lines, r, 'Checked', when)
        r = refind(lines, r)
        what = 'kept on a refresh: %s' % why
        note(lines, r, 'History', '%s: %s' % (when, what))
        write('RULES.md', lines, what)
        print('rule %d %s' % (a.n, what))
        return
    else:
        if a.text:
            fail('--text goes only with --as edited')
        new, what = a.as_, '%s: %s' % (a.as_, why)
    if new == 'accepted':
        put(lines, r, 'Overruled', '0')
        r = refind(lines, r)
    set_status(lines, r, new, when, what)
    write('RULES.md', lines, what + (a.text or ''))
    print('rule %d %s' % (a.n, what))


def cmd_applies(a):
    lines = load('RULES.md')
    r = find_n(lines, 'Rule', a.n, 'RULES.md')
    when = date(a.date)
    text = sentence(a.when, 'when the rule applies')
    put(lines, r, 'Applies when', text)
    note(lines, refind(lines, r), 'History', '%s: applies when written: %s' % (when, text))
    write('RULES.md', lines, text)
    print('rule %d applies when: %s' % (a.n, text))


def cmd_pack(a):
    """Each accepted rule as one Markdown file with title and applies_when in its frontmatter."""
    lines = load('RULES.md')
    out = a.write
    os.makedirs(out, exist_ok=True)
    for name in os.listdir(out):
        if re.match(r'^rule-\d+\.md$', name):
            os.remove(os.path.join(out, name))
    written, missing = 0, []
    for r in records(lines):
        if status(lines, r) != 'accepted':
            continue
        applies = get(lines, r, 'Applies when')
        if not applies:
            missing.append(r['n'])
            continue
        q = lambda t: '"%s"' % t.replace('\\', '\\\\').replace('"', '\\"')
        body = ['---', 'title: %s' % q(r['title'].rstrip('.')), 'applies_when:', '  - %s' % q(applies.rstrip('.')),
                'tags: [project-rule]', '---', '', '%s' % r['title'], '',
                'Premise: %s' % (get(lines, r, 'Premise') or ''),
                '', 'Rule %d in product/RULES.md, accepted by the client. Cite it as rule %d.' % (r['n'], r['n'])]
        with open(os.path.join(out, 'rule-%d.md' % r['n']), 'w', encoding='utf-8') as f:
            f.write('\n'.join(body) + '\n')
        written += 1
    print('%d accepted rule(s) written to %s' % (written, out))
    if missing:
        print('left out, no "applies when" yet: rule %s (add it with team.py applies)' % ', '.join(map(str, missing)))


def cmd_overruled(a):
    lines = load('RULES.md')
    r = find_n(lines, 'Rule', a.n, 'RULES.md')
    if status(lines, r) != 'accepted':
        fail('rule %d is %s; only an accepted rule is overruled' % (a.n, status(lines, r)))
    find_n(load('DECISIONS.md'), 'Decision', a.decision, 'DECISIONS.md')
    when = date(a.date)
    count = int(get(lines, r, 'Overruled') or 0) + 1
    put(lines, r, 'Overruled', str(count))
    r = refind(lines, r)
    if count >= 2:
        set_status(lines, r, 'back', when, 'overruled by decision %d, the second time; back to the client' % a.decision)
        print('rule %d overruled twice; back to the client' % a.n)
    else:
        note(lines, r, 'History', '%s: overruled by decision %d' % (when, a.decision))
        print('rule %d overruled once' % a.n)
    write('RULES.md', lines, '')


DESIGN = os.path.join(HERE, '..', '..', 'design-advisor', 'principles', 'design.md')
TOP = ['Apple %d' % i for i in range(1, 9)] + ['Nielsen %d' % i for i in range(1, 11)]
CALLED = re.compile(r'^Called for by: (.+?)\. Cross-check:')


def design_claims():
    """Each Design Advisor claim, {name: [triggers]}, from its principles file."""
    if not os.path.exists(DESIGN):
        fail('the Design Advisor\'s claims are not at %s' % DESIGN)
    with open(DESIGN, encoding='utf-8') as f:
        lines = f.read().split('\n')
    out, name = {}, None
    for line in lines:
        if line.startswith('### '):
            name = line[4:].strip()
        m = CALLED.match(line)
        if m and name:
            out[name] = [t.strip() for t in m.group(1).split(',')]
            name = None
    return out


def named(items, what, known):
    """Splits "NAME: why" lines, refusing a name that is not a top-tier item or a claim."""
    out = {}
    for x in items or []:
        x = sentence(x, what)
        m = re.match(r'^(.+?): (\S.*)$', x)
        if not m:
            fail('%s is written "NAME: why", not %r' % (what, x))
        name = m.group(1).strip()
        if name not in known:
            fail('%r is not a top-tier item (Apple 1 to 8, Nielsen 1 to 10) or a claim heading in design.md' % name)
        out[name] = m.group(2)
    return out


def cmd_review(a):
    lines = load('REVIEWS.md')
    when = date(a.date)
    claims = design_claims()
    vocab = sorted({t for ts in claims.values() for t in ts} - {'every screen'})
    has = [t.strip() for t in sentence(a.has, '--has, what the screen has').split(',') if t.strip()]
    for t in has:
        if t not in vocab:
            fail('%r is not a trigger; the triggers are: %s' % (t, ', '.join(vocab)))
    shot = sentence(a.screenshot, '--screenshot')
    known = set(TOP) | set(claims)
    applied = named(a.applied, 'an applied line', known)
    skipped = named(a.skipped, 'a skipped line', known)
    both = set(applied) & set(skipped)
    if both:
        fail('applied and skipped at once: %s' % ', '.join(sorted(both)))
    called = [c for c, ts in claims.items() if 'every screen' in ts or set(ts) & set(has)]
    missing = [x for x in TOP + called if x not in applied and x not in skipped]
    if missing:
        fail('every top-tier item and every claim the screen calls for is applied or skipped with why; '
             'not yet: %s' % '; '.join(missing))
    n = next_n(records(lines))
    title = sentence(a.title, 'the title')
    block = ['## Review %d (%s): %s' % (n, when, title),
             '- **Screen:** %s' % sentence(a.screen, '--screen, the screen as a person meets it'),
             '- **Screenshot:** %s' % shot, '- **Change:** %s' % sentence(a.change, '--change, what was added or moved'),
             '- **Has:** %s' % ', '.join(has), '- **Applied:**']
    block += ['  - %s: %s' % (k, v) for k, v in applied.items()]
    block += ['- **Skipped:**'] + ['  - %s: %s' % (k, v) for k, v in skipped.items()]
    block += ['- **Not called for:** %d claims, by triggers the screen does not have' % (len(claims) - len(called)),
              '- **Verdict:** %s' % sentence(a.verdict, 'the verdict')]
    append_record(lines, block)
    write('REVIEWS.md', lines, '\n'.join(block))
    print('review %d: %s (%d applied, %d skipped)' % (n, title, len(applied), len(skipped)))


def cmd_miss(a):
    lines = load('MISSES.md')
    when = date(a.date)
    claims = design_claims()
    claim = sentence(a.claim, '--claim')
    if claim != 'none' and claim not in claims:
        fail('%r is not a claim heading in design.md; name the claim that should have caught it, or "none"' % claim)
    if a.review is not None:
        find_n(load('REVIEWS.md'), 'Review', a.review, 'REVIEWS.md')
    n = next_n(records(lines))
    title = sentence(a.title, 'the title')
    block = ['## Miss %d (%s): %s' % (n, when, title), '- **Met by:** %s' % a.by,
             '- **What went wrong:** %s' % sentence(a.what, '--what, what went wrong'),
             '- **Instead:** %s' % sentence(a.instead, '--instead, what the screen does instead'),
             '- **Claim:** %s' % claim, '- **Review:** %s' % (a.review if a.review is not None else 'none')]
    append_record(lines, block)
    write('MISSES.md', lines, '\n'.join(block))
    print('miss %d: %s, against %s' % (n, title, claim))


def cmd_replay(a):
    lines = load('REPLAY.md')
    when = date(a.date)
    claims = design_claims()
    shot = sentence(a.screenshot, '--screenshot')
    where = os.path.join(os.path.dirname(ROOT), shot)
    if not os.path.exists(where) and not os.path.exists(shot):
        fail('the screenshot %s does not exist; keep it in the project, as product/replay/' % shot)
    breaks = [sentence(x, 'a --breaks line') for x in a.breaks]
    for x in breaks:
        m = re.match(r'^(.+?): (\S.*)$', x)
        if not m or m.group(1).strip() not in claims:
            fail('--breaks is written "CLAIM HEADING: what on the screen breaks it", with a claim in design.md, not %r' % x)
    n = next_n(records(lines))
    title = sentence(a.title, 'the title')
    block = ['## Replay %d (%s): %s' % (n, when, title), '- **Screenshot:** %s' % shot, '- **Breaks:**']
    block += ['  - ' + x for x in breaks]
    block += ['- **Instead:** %s' % sentence(a.instead, '--instead, what the fixed screen does')]
    append_record(lines, block)
    write('REPLAY.md', lines, '\n'.join(block))
    print('replay %d: %s' % (n, title))


def cmd_due(a):
    out = []
    if os.path.exists(path('DECISIONS.md')):
        lines = read('DECISIONS.md')
        for r in records(lines):
            if get(lines, r, 'Prediction status') == 'open':
                out.append('- Open prediction, decision %d (%s): %s' % (r['n'], r['title'], get(lines, r, 'Prediction')))
    if os.path.exists(path('RULES.md')):
        lines = read('RULES.md')
        for r in records(lines):
            st = status(lines, r)
            if st in ('proposed', 'back'):
                out.append('- Waiting on the client, rule %d (%s): %s' % (r['n'], st, r['title']))
        today = datetime.date.today()
        for r in records(lines):
            if status(lines, r) == 'accepted':
                applies = get(lines, r, 'Applies when')
                out.append('- Accepted rule %d: %s %s Name it when you apply it.'
                           % (r['n'], r['title'], 'Applies when: %s.' % applies.rstrip('.') if applies
                              else '(No "applies when" yet: write it with `team.py applies %d`.)' % r['n']))
        for r in records(lines):
            if status(lines, r) != 'accepted':
                continue
            last = get(lines, r, 'Checked') or get(lines, r, 'Since') or ''
            try:
                age = (today - datetime.date.fromisoformat(last)).days
            except ValueError:
                continue
            if age >= REFRESH_DAYS:
                out.append('- Refresh rule %d, last checked %s: does its premise still hold, and does another rule say '
                           'the same? `ruling %d --as kept`, or `--as back` to the client.' % (r['n'], last, r['n']))
    if os.path.exists(path('IDEAS.md')):
        lines = read('IDEAS.md')
        bet_open = os.path.exists(path('BET.md')) and any(OPEN.match(l) for l in read('BET.md'))
        listed = on_list(lines)
        waiting = [r for r in records(lines) if status(lines, r) == 'waiting on the bet']
        shaped = [r for r in listed if status(lines, r) == 'shaped']
        if not bet_open and listed and not shaped:
            out.append('- Shape first: no bet is open and the list holds %s. Shape the top two or three before the '
                       'next bet is picked.' % ', '.join(idea_name(r) for r in listed))
        elif not bet_open and shaped:
            out.append('- No bet is open and %s %s shaped: pick the next bet, and pass over the rest.'
                       % (', '.join(idea_name(r) for r in shaped), 'is' if len(shaped) == 1 else 'are'))
        if not bet_open and waiting:
            out.append('- Waiting on a bet that has closed: %s. Bring each back with "revive", or archive it.'
                       % ', '.join(idea_name(r) for r in waiting))
    if os.path.exists(path('MISSES.md')):
        lines = read('MISSES.md')
        counts = {}
        for r in records(lines):
            c = get(lines, r, 'Claim') or 'none'
            if c == 'none':
                out.append('- Miss %d (%s) has no claim that covers it: propose one, with its source and what the '
                           'screen does instead.' % (r['n'], r['title'].split('): ', 1)[-1]))
            else:
                counts[c] = counts.get(c, 0) + 1
        for c, k in sorted(counts.items()):
            if k >= 2:
                out.append('- Claim "%s" missed %d times: propose to the client that it is called for on every '
                           'screen.' % (c, k))
    stray = sorted(n for n in HOMES if os.path.exists(os.path.join(ROOT, n)))
    if stray:
        out.append('- Still kept in product/, which holds only what is true of the product today: %s. '
                   '`team.py move` moves each to history/ or work/.' % ', '.join(stray))
    if out:
        print('Team charter, what is due (from the project\'s records):')
        print('\n'.join(out))
    return 0


def cmd_move(a):
    moved = []
    for name in sorted(HOMES):
        old = os.path.join(ROOT, name)
        if not os.path.exists(old):
            continue
        if os.path.exists(home(name)):
            fail('%s is in product/ and in %s/ both; keep one, by hand, and run move again' % (name, HOMES[name]))
        os.makedirs(os.path.dirname(home(name)), exist_ok=True)
        os.rename(old, home(name))
        moved.append('%s to %s/' % (name, HOMES[name]))
    print('moved: ' + ', '.join(moved) if moved else 'nothing to move: no record of history/ or work/ is kept in product/')


def resolve_root(given):
    """The product/ folder to work on: --root, then one beside this script, then ./product, then the project's."""
    if given:
        return os.path.abspath(given)
    candidates = [os.path.join(HERE, 'product'), os.path.join(os.getcwd(), 'product')]
    if os.environ.get('CLAUDE_PROJECT_DIR'):
        candidates.append(os.path.join(os.environ['CLAUDE_PROJECT_DIR'], 'product'))
    return next((c for c in candidates if os.path.isdir(c)), None)


def main(argv=None):
    global ROOT
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    p.add_argument('--root', help='the product/ directory to write')
    sub = p.add_subparsers(dest='cmd', required=True)
    c = sub.add_parser('coin', help='write one coined word into a bet\'s entry')
    c.add_argument('word'); c.add_argument('meaning')
    c.add_argument('--bet', type=int, required=True); c.add_argument('--where', required=True)
    c.add_argument('--date', required=True); c.add_argument('--replaces')
    c.set_defaults(run=cmd_coin)
    k = sub.add_parser('park', help='append a parking-lot row')
    k.add_argument('item'); k.add_argument('why'); k.add_argument('trigger')
    k.add_argument('--date', required=True); k.add_argument('--by', default='founder')
    k.set_defaults(run=cmd_park)
    v = sub.add_parser('prove', help='append a canon line')
    v.add_argument('what'); v.add_argument('earned_by'); v.add_argument('--date', required=True)
    v.set_defaults(run=cmd_prove)
    e = sub.add_parser('entry', help='write a new log entry\'s skeleton')
    e.add_argument('--bet', type=int, required=True); e.add_argument('--opened', required=True)
    e.add_argument('--closed', required=True); e.add_argument('--verdict', required=True)
    e.add_argument('--shipped', required=True)
    e.set_defaults(run=cmd_entry)
    g = sub.add_parser('glossary', help='project the coined words and print the conflicts')
    g.add_argument('--write', help='write the projection to this file instead of printing it')
    g.set_defaults(run=cmd_glossary)
    i = sub.add_parser('idea', help='add an idea with every triage answer')
    i.add_argument('name')
    i.add_argument('--kind', choices=KINDS, required=True)
    i.add_argument('--for', dest='for_whom', required=True)
    for f in ('problem', 'evidence', 'fit', 'worth', 'smallest', 'date'):
        i.add_argument('--' + f, required=True)
    i.add_argument('--route', choices=sorted(ROUTES), required=True)
    i.add_argument('--by', choices=('founder', 'lean'), default='founder')
    i.set_defaults(run=cmd_idea)
    r = sub.add_parser('rank', help='set the list\'s order')
    r.add_argument('names', nargs='+'); r.set_defaults(run=cmd_rank)
    s = sub.add_parser('shape', help='fill an idea\'s story, riskiest assumption and metric')
    s.add_argument('name')
    for f in ('story', 'assumption', 'metric', 'date'):
        s.add_argument('--' + f, required=True)
    s.set_defaults(run=cmd_shape)
    k = sub.add_parser('pick', help='mark the idea that becomes the next bet')
    k.add_argument('name'); k.add_argument('--bet', type=int, required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_pick)
    k = sub.add_parser('pass', help='count a pass for each idea passed over at shaping')
    k.add_argument('names', nargs='+'); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_pass)
    k = sub.add_parser('archive', help='move an idea off the list')
    k.add_argument('name'); k.add_argument('--why', required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_archive)
    k = sub.add_parser('revive', help='bring an archived or waiting idea back onto the list')
    k.add_argument('name'); k.add_argument('--how', choices=('asked', 'evidence', 'match', 'bet closed'), required=True)
    k.add_argument('--why', required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_revive)
    d = sub.add_parser('decide', help='write a decision')
    d.add_argument('title'); d.add_argument('--kind', choices=('tie', 'overrule', 'pushback'), required=True)
    for f in ('circumstances', 'premise', 'decision', 'reason', 'date'):
        d.add_argument('--' + f, required=True)
    d.add_argument('--advice', action='append', required=True)
    d.add_argument('--rule', required=True, help='the accepted rule that applied, or "none" when the rules were checked and none fit')
    d.add_argument('--prediction')
    d.add_argument('--conceded', help='a pushback: what the advisor conceded')
    d.set_defaults(run=cmd_decide)
    k = sub.add_parser('settle', help='close an open prediction')
    k.add_argument('n', type=int); k.add_argument('--as', dest='as_', choices=('confirmed', 'disproved', 'moot'), required=True)
    k.add_argument('--note', required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_settle)
    k = sub.add_parser('rule', help='propose a rule from three or more decisions, or one the client stated (--stated)')
    k.add_argument('text'); k.add_argument('--premise', required=True)
    k.add_argument('--applies-when', required=True, help='when the rule applies, so an advisor knows when to follow it')
    k.add_argument('--from', dest='from_'); k.add_argument('--date', required=True)
    k.add_argument('--stated', action='store_true', help='from one decision in which the client stated the rule outright')
    k.add_argument('--words', help='with --stated: the client\'s words that state the rule, verbatim')
    k.add_argument('--said', help='with --stated and no --from: the date the client said it, where no decision holds it')
    k.set_defaults(run=cmd_rule)
    k = sub.add_parser('ruling', help='record the client\'s word on a rule')
    k.add_argument('n', type=int)
    k.add_argument('--as', dest='as_', choices=('accepted', 'struck', 'edited', 'back', 'kept'), required=True)
    k.add_argument('--note', required=True); k.add_argument('--date', required=True); k.add_argument('--text')
    k.set_defaults(run=cmd_ruling)
    k = sub.add_parser('applies', help='write when an existing rule applies')
    k.add_argument('n', type=int); k.add_argument('when'); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_applies)
    k = sub.add_parser('pack', help='write each accepted rule as a file with title and applies_when')
    k.add_argument('--write', required=True, help='the folder to write the rule files into')
    k.set_defaults(run=cmd_pack)
    k = sub.add_parser('overruled', help='count an overrule of an accepted rule')
    k.add_argument('n', type=int); k.add_argument('--decision', type=int, required=True)
    k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_overruled)
    k = sub.add_parser('review', help='record a Design Advisor review of a whole screen')
    k.add_argument('title'); k.add_argument('--screen', required=True); k.add_argument('--screenshot', required=True)
    k.add_argument('--change', required=True); k.add_argument('--has', required=True)
    k.add_argument('--applied', action='append', required=True); k.add_argument('--skipped', action='append')
    k.add_argument('--verdict', required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_review)
    k = sub.add_parser('miss', help='record a problem met on a screen that no review flagged')
    k.add_argument('title'); k.add_argument('--what', required=True); k.add_argument('--instead', required=True)
    k.add_argument('--claim', required=True); k.add_argument('--review', type=int)
    k.add_argument('--by', choices=('founder', 'tester'), required=True); k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_miss)
    k = sub.add_parser('replay', help='add a screen with known problems to the replay set')
    k.add_argument('title'); k.add_argument('--screenshot', required=True)
    k.add_argument('--breaks', action='append', required=True); k.add_argument('--instead', required=True)
    k.add_argument('--date', required=True)
    k.set_defaults(run=cmd_replay)
    k = sub.add_parser('due', help='print what is due')
    k.set_defaults(run=cmd_due)
    k = sub.add_parser('move', help='move each record still in product/ to history/ or work/')
    k.set_defaults(run=cmd_move)
    a = p.parse_args(argv)
    ROOT = resolve_root(a.root)
    if ROOT is None or not os.path.isdir(ROOT):
        if a.cmd == 'due':
            return 0
        fail('no product directory found; pass --root, or run from the folder that holds product/')
    return a.run(a) or 0


if __name__ == '__main__':
    sys.exit(main())
