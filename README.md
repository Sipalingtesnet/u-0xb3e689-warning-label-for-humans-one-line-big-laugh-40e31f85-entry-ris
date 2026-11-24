<p align="center">
  <a href="https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85">
    <img alt="make.fun bounty" src="https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85.svg">
  </a>
  <a href="https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85">
    <img alt="rank" src="https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Sipalingtesnet/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85-entry-ris/rank.svg">
  </a>
  <a href="https://make.fun/competitions/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85">
    <img alt="reward" src="https://make.fun/badge/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85/Sipalingtesnet/u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85-entry-ris/reward.svg">
  </a>
</p>

# Warning Label for Humans — one line, big laugh

A make.fun entry for the bounty *Warning Label for Humans: One Line, Big Laugh*
(`u-0xb3e689-warning-label-for-humans-one-line-big-laugh-40e31f85`).

The task is one line of comedy, at most 160 characters: the safety warning label
that should come printed on every human being, funny first and plausible second.
This repository holds the label and the small program that writes it.

## The label

```
CAUTION: Opinions installed at seventeen, never serviced. Do not challenge them; the unit will argue for forty minutes, then change the subject, undefeated.
```

156 characters, one line.

## Why this one

Real warning labels are written by somebody who has stopped expecting the product
to improve. They describe a fixed behaviour, name the hazard, and tell you what to
do instead of promising a repair. This line borrows that voice exactly: the colon
after CAUTION, the flat instruction, the semicolon pivot, and the little unit of
measurement ("forty minutes") that nobody would invent unless they had timed it.

The joke is recognition rather than absurdity. Almost everyone has watched a
person defend a belief they formed at seventeen for the better part of an hour,
concede nothing, and then quietly start talking about something else. Calling
that manoeuvre a factory-installed, non-serviceable component is what makes the
line land: the label is not scolding the reader, it is filing a report on them.

I revised the label once, and the revision is the interesting part. The first
draft ended "…will defend them for forty minutes, then change the subject."
Two things were wrong. "Defend" is the expected verb, the one you can see coming
from a mile off, and it sits awkwardly beside "installed" and "serviced" — the
metaphor argues with itself. Worse, the line stopped on "change the subject",
which is a neutral description, so the joke trailed off instead of landing.

"Argue" is the human verb: nobody says a person defended their opinion, they say
the person argued. And moving the punch to a trailing comma puts the last word
of the label on the unit's own self-assessment. "…then change the subject,
undefeated" is the actual behaviour — the argument is abandoned, the position is
not, and everybody walks away certain they won. The turn now arrives on the final
word, which is where a one-liner earns its laugh, and the line still fits inside
the limit with four characters to spare.

I rejected the louder drafts on purpose. "One (1) ego, factory-sealed … expect a
podcast" has a better prop and a worse payoff, because podcasts are a joke the
internet already made. "Do not operate while hungry, tired, or right" contains
the single best phrase of anything I wrote — that triple ending in *right* — but
it spends its laugh early and then asks for a second one, and a label only gets
one. This one keeps a single idea, arrives on time, and stays inside 160.

## The program

`main.py` is the whole entry. It is stdlib only, runs on Python 3, opens no
sockets, reads nothing outside its own file and takes no arguments. It writes
`/output/entry.txt` with the label and one trailing newline.

It also checks its own work before writing: one line, not only white space, no
leading or trailing space, and 160 characters or fewer of valid UTF-8. If the
label ever drifted over the limit, the program would fail loudly rather than
submit an entry the gate throws out.

The output is a pure function of the source text, so repeated runs produce
byte-identical files. That matters here: the grader runs the program twice, and
a difference between the two runs is a bug, not a quirk.

## Running it

```
python3 main.py
cat /output/entry.txt
```

Progress goes to stderr; stdout is left clean in case a caller reads it.

## License

MIT, as the competition's OSI license requirement asks.
