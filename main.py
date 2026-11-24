"""The One-Line Cat Joke That Lands.

Writes one joke (67 characters) to /output/entry.txt:
a single line about cats, setup and a turn that lands.
Pure Python 3.13 standard library, deterministic: no network, no clock,
no randomness, no input. Two runs write byte-identical output.
"""

import os
import sys

# Chosen joke: two beats — the vet's verdict, then the cat reframes the
# vet as a snitch, applying playground morality to the authority figure.
# No tired pun (no purr/meow/paws/litter-ally), 67 characters, tight and
# retellable. 67 characters, inside the 1-200 gate.

# Chosen joke: two beats — the vet's verdict, then the cat reframes the
# vet as a snitch, applying playground morality to the authority figure.
# No tired pun (no purr/meow/paws/litter-ally), 66 characters, tight and
# retellable. 66 characters, inside the 1-200 gate.
# Revision note: wording unchanged since v1; the joke was picked over
# six other candidates (see candidates.md) for its turn, not a pun.
JOKE = "The vet says my cat is overweight. My cat says the vet is a snitch."


# Bounty gate: the entry must be one line of 1-200 UTF-8 characters.
MAX_CHARS = 200


def main() -> None:
    if len(JOKE) > MAX_CHARS:
        print(f"entry too long: {len(JOKE)} chars (max {MAX_CHARS})", file=sys.stderr)
        sys.exit(1)
    # Output goes to $MAKEFUN_OUTPUT_DIR/entry.txt in the harness,
    # or /output/entry.txt when run locally by hand.
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
