# Tiny Chess Engine

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/heruzz07/makefun-tiny-chess/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/heruzz07/makefun-tiny-chess/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4 KB chess engine in a single Python file, written from scratch for the
make.fun tiny-chess-01 bounty.

## How it works

- **Board:** 0x88 representation (128 squares, off-board detected by `sq & 0x88`).
- **Search:** negamax with alpha-beta pruning, iterative deepening to a fixed
  node budget (100,000 nodes per move — never a clock, so play is fully
  deterministic). Quiescence search (captures and promotions, plus all legal
  moves when in check) is merged into the search.
- **Move ordering:** MVV-LVA (most valuable victim, least valuable attacker).
- **Evaluation:** material (P=100, N=320, B=330, R=500, Q=900) plus
  piece-square tables for pawns, knights and king, plus a mating term that
  rewards bringing the kings together when one side is a queen or more ahead.
- **Repetition avoidance:** the root penalises a move by 30 cp when the
  resulting board repeats a board reached after one of our earlier moves
  in the same game, so the engine breaks out of shuffling cycles instead
  of drawing by threefold repetition.
- **Protocol:** talks to the game environment over HTTP at `MAKEFUN_ENV_URL`
  (`POST /game`, `POST /move`), playing only legal moves in UCI notation.

## Limits

- `main.py` is 4,086 bytes (limit 4,096). Standard library only. It reads,
  imports, opens or runs no other file and stores no data outside its own
  bytes.
- En passant captures are not generated (a deliberate size trade-off).
- No model calls, no network beyond the game environment, no randomness.

## Local practice result (trial-0, 6 games)

2 wins, 1 draw, 3 losses — estimated practice Elo ~1191 (floor to enter the
final is 1,154, so the engine clears it). The repetition fix turned the
depth-3 and depth-4 games from threefold draws into wins (adjudication and
checkmate); the depth-2 game still drew by threefold repetition, and the
three losses were checkmates against the node-count engines. Slowest move
~5.3 s, average ~2.4 s (limit 10 s/move). Determinism verified: two full
trial-0 runs produced byte-identical moves in all 6 games.
