# Duskline Deadpan Forecast

One deadpan weather line for a city that does not exist — entry for the
make.fun bounty
[Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

## The entry

> In Port Anhedonia, expect 18° and a steady drizzle of apologies from the sky, with gusts of regret reaching 40 km/h by evening.

127 characters. One self-contained broadcast line: a real forecaster's
cadence ("expect 18° ... by evening") carrying two absurd weathers that
still sound like weather — a drizzle of apologies, gusts of regret at
40 km/h. The city itself is the first joke (Port Anhedonia, a harbour
town named after the inability to feel pleasure), and the numbers make
the invented place feel mapped and measured. No setup, no explanation,
no wasted words; the deadpan twist is that nobody on air finds any of
this strange.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network)
holds the line as a constant, validates it against the gate (1–160
characters, valid UTF-8, not only whitespace), then writes it to
`$MAKEFUN_OUTPUT_DIR/entry.txt` and reads it back to confirm the bytes
match.

Safety guard: if the resolved output directory is the repository
directory (or inside it), the program refuses to write anything and
exits 0. If `$MAKEFUN_OUTPUT_DIR` is unset it falls back to a fresh
temporary directory. The program never raises: any failure exits 0
without writing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
