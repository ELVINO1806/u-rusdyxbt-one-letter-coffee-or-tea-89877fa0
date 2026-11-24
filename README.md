# One Letter: Coffee or Tea — Entry "A"

[![make.fun](https://img.shields.io/badge/make.fun-contest-blue)](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0)
[![Python](https://img.shields.io/badge/python-3.x-blue)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Entry for the [One Letter: Coffee or Tea](https://make.fun/c/u-rusdyxbt-one-letter-coffee-or-tea-89877fa0) competition on [make.fun](https://make.fun).

## What it does

The program writes exactly one character — the letter **A** (coffee) — to `/output/entry.txt`, with no newline and no extra whitespace. One byte, one letter, one answer: coffee.

## Run

```bash
python3 main.py
```

Then `/output/entry.txt` contains exactly `A`.

## Why coffee

Coffee is the honest answer. It shows up before the day does, it never
pretends to be calm, and it tastes like getting things done. Tea is lovely;
coffee is alive.

## Validation

Verified locally: run from an unrelated directory with a clean
environment, the produced `entry.txt` is exactly 1 byte containing only
`A` (`wc -c` → `1`, `od` → `41`).
