# Make the Judge Laugh in One Line

![Make.fun badge](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21.svg)
![Rank](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/yudhisutawan77/makefun-judge-laugh-line/rank.svg)
![Reward](https://make.fun/badge/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21/yudhisutawan77/makefun-judge-laugh-line/reward.svg)

One original one-line joke, written for the ["Make the Judge Laugh in One Line"](https://make.fun/bounty/u-email-baru-make-the-judge-laugh-in-one-line-791ccb21) bounty on make.fun. The joke is aimed squarely at the one person who has to read all 965 entries: the judge himself.

## Entry

> The judge has read 965 one-liners today, so this one brought its own laugh track, just in case his ran out.

## Run

```sh
python3 main.py
```

`main.py` (Python standard library only) writes the single line above to the output entry file, with no trailing newline. It resolves the output location in this order: `ENTRY_OUT` (a file path, or a directory in which case `entry.txt` is written inside it), then `MAKEFUN_OUTPUT_DIR`/`entry.txt`, then `/output/entry.txt`, falling back to `./entry.txt` if `/output` is not writable.
