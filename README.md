# Tiny Chess Engine (4 KB)

A from-scratch chess engine in a single `main.py` (4,061 bytes, Python 3.13
stdlib only) for the make.fun tiny-chess-01 competition.

- 0x88 board, full move generation (castling, en passant, all promotions)
- Negamax with alpha-beta pruning, quiescence search (captures + promotions)
- MVV move ordering, iterative deepening over the env's legal moves
- Formula evaluation: material + pawn advancement + knight/bishop centralisation
- Deterministic: fixed 120,000-node budget per move, no clock, no randomness

## Protocol

Talks to the environment over HTTP at `$MAKEFUN_ENV_URL`:

- `POST /game {}` to start / fetch the current game
- `POST /move {"game": n, "move": "<uci>"}` to play a move

## Local practice trial

Against the kit's 16-game gauntlet (depth-2 to nodes-2M anchors):

- **1 win, 4 draws, 11 losses (3.0/16, ~1145 Elo)**, ~42 min wall time
- No timeouts, no crashes, deterministic replay

## Verification

- PERFT: all 6 standard positions correct through depth 4 (incl. Kiwipete)
- Determinism: identical output across repeated runs (fixed node budget)
- Speed: ~36,000 nodes/sec on the VM (mid-game position)

## License

MIT. See `LICENSE`.
