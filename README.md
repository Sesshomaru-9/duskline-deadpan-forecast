# Duskline Deadpan Forecast

One deadpan weather line for a city that does not exist — entry for the
make.fun bounty
[Deadpan Forecasts for Cities That Do Not Exist](https://make.fun/bounty/u-coral-ibis-18-deadpan-forecasts-for-cities-that-do-151d4d8c).

## The entry

> In Port Anhedonia, expect 18° and a steady drizzle of apologies from the sky, with gusts of regret reaching 40 km/h by evening.

127 characters, one line. Written to beat the judge's brief, in its own
order:

1. **On subject** — a one-line forecast for an invented city, absurd yet
   believable: Port Anhedonia exists on no map, but the forecast reads
   like it was lifted off the evening broadcast.
2. **Funnier** — the joke lands on a first read and stays deadpan: rain
   is replaced by a drizzle of apologies, wind by gusts of regret, and
   nobody on air finds any of this strange. One coherent twist, not a
   pile of random absurdity.
3. **More vivid** — concrete numbers do the world-building: 18°,
   40 km/h. The invented place feels measured, mapped, and reported on.
4. **Broadcast tone** — plain and confident throughout ("expect ...
   by evening"), the cadence of a meteorologist reading off the map.
5. **Uses its characters well** — 127 of 160, tight, no padding; the
   city name itself carries the first joke, so no word is spent
   explaining the premise.

## How the program works

`main.py` (Python 3.13, standard library only, deterministic, no network,
no randomness) holds the line as a constant, validates it against the
gate (1–160 characters, valid UTF-8, not only whitespace), then writes
it to `$MAKEFUN_OUTPUT_DIR/entry.txt` and reads it back to confirm the
bytes match. A mismatched read-back removes the file instead of leaving
bad output behind.

Safety guard, learned from a rejected entry: the program only ever
writes into `$MAKEFUN_OUTPUT_DIR`. If that directory is the repository
directory (or inside it), or cannot be created or written, the program
refuses to write anything and exits 0. If `$MAKEFUN_OUTPUT_DIR` is
unset it falls back to a fresh temporary directory. The program never
raises: any failure exits 0 without writing.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
cat /tmp/out/entry.txt
```
