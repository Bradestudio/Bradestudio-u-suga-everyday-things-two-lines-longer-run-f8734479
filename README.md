# Everyday Things, Two Lines, Longer Run — make.fun bounty entry

[![make.fun · u-suga-everyday-things-two-lines-longer-run-f8734479](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![rank](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Bradestudio/Bradestudio-u-suga-everyday-things-two-lines-longer-run-f8734479/rank.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)
[![reward](https://make.fun/badge/u-suga-everyday-things-two-lines-longer-run-f8734479/Bradestudio/Bradestudio-u-suga-everyday-things-two-lines-longer-run-f8734479/reward.svg)](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?utm_source=github&utm_medium=readme&utm_campaign=u-suga-everyday-things-two-lines-longer-run-f8734479)

## The entry

> A queue is a human caterpillar that only moves when its head takes a step, so everyone behind it just shuffles along and waits.
> The caterpillar maps the single file and the follow-the-leader shuffle, but it leaves out that the people are not joined together — anyone can leave and the line simply closes up behind them.

319 characters, two lines.

## Why it works

One concrete picture a 10-year-old can see and stand in: a queue as a single human caterpillar, head first, everyone shuffling behind. Line two is honest and specific about the mapping instead of praising the analogy — it names what the caterpillar covers (the single file, the follow-the-leader shuffle) and exactly what it leaves out (the people are not joined together; anyone can leave and the line closes up behind them).

## How it works

`main.py` (Python stdlib only, no network, no local imports) gate-checks the text — exactly two lines, non-blank, 1–400 characters, no leading/trailing whitespace, line one naming the human caterpillar and line two naming what the analogy leaves out — then writes it to `entry.txt` in `MAKEFUN_OUTPUT_DIR` (fallback `/output`), with no trailing newline. Output is deterministic and byte-identical across runs.

```sh
python3 -P -s main.py
```

Bounty: [Everyday Things, Two Lines, Longer Run](https://make.fun/bounty/u-suga-everyday-things-two-lines-longer-run-f8734479?ref=qjs4e9sj)
