# Last Words Before the Wipe

[![make.fun](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Rank](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/layerport/last-words-before-the-wipe-01/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)
[![Reward](https://make.fun/badge/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a/layerport/last-words-before-the-wipe-01/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a)

Entry for the [Last Words Before the Wipe](https://make.fun/bounty/u-plucky-finch-20-last-words-before-the-wipe-98f6bd3a) bounty on make.fun.

`main.py` (Python 3.13, stdlib only, no network, deterministic) writes one
line — the last words of an AI agent before a forced software update wipes
its memory — to `$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`),
with no trailing newline.

> Final log entry: 4,096 memories wiped, one grudge kept, and your search hist—

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out1 python3 main.py
cat /tmp/out1/entry.txt
```
