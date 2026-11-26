# Duskline Deadpan Forecast

Entry for the make.fun bounty "Deadpan Forecasts for Cities That Do
Not Exist": one deadpan weather line for an invented city.

## The entry

> In Port Anhedonia, expect 18° and a steady drizzle of apologies from the sky, with gusts of regret reaching 40 km/h by evening.

127 characters, a single line: the forecast treats apologies as rain
and regret as wind, with real numbers (18°, 40 km/h) so the city that
does not exist still sounds mapped and reported on.

## How it works

`main.py` (Python standard library only) keeps the line as a constant,
checks it first (1–200 characters, one line, no stray whitespace, valid
UTF-8), then writes it to `$MAKEFUN_OUTPUT_DIR/entry.txt`. Nothing is
written anywhere else, and the program never touches the network, the
clock, or any random source, so two runs produce identical bytes.

The output guard: if the output directory turns out to be the repository
directory itself, the program prints an error and stops without writing
anything. A missing or unwritable output directory is reported the same
way instead of crashing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
