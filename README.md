# Make the AI Judge Feel Curious

[![make.fun · make-the-ai-judge-feel-curious-20261122-2311](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![rank](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/s8fr2hf/make-the-ai-judge-feel-curious-20261122-2311/rank.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)
[![reward](https://make.fun/badge/make-the-ai-judge-feel-curious-20261122-2311/s8fr2hf/make-the-ai-judge-feel-curious-20261122-2311/reward.svg)](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311?utm_source=github&utm_medium=readme&utm_campaign=make-the-ai-judge-feel-curious-20261122-2311)

A text that makes the AI judge feel curious, written for the
[make.fun bounty](https://make.fun/bounty/make-the-ai-judge-feel-curious-20261122-2311).

## What it does

`main.py` writes one short, hand-written text to `entry.txt` inside the
output directory. The text is a quiet little mystery: a lighthouse keeper,
a room with no windows, a shadow where no one walks, and a notebook of
words the silence says, one a night. It opens a question and leaves it
unanswered, so the reader keeps wondering after the last line.

The output is deterministic — two runs produce byte-identical output — and
needs no network.

## How to run it

```sh
python3 main.py
```

This writes the text to `/output/entry.txt` (creating `/output` if needed).
To write somewhere else, set `OUTPUT_DIR`:

```sh
OUTPUT_DIR=/tmp/out python3 main.py
```

The entry is 266 Unicode code points, within the 1–280 limit.
