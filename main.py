#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open - make.fun entry.

Writes one line (188 characters, single line) to
$MAKEFUN_OUTPUT_DIR/entry.txt: the joke about reporting the ticket
system as down by filing a ticket, which IT then closes as resolved.
Pure stdlib, no network, no secrets, no hard-coded paths.
"""
import os

# The joke: filing a ticket to report the ticket system is down, and IT
# closing it as resolved - the system proves itself by eating the
# complaint about itself, then fails the one person who needed it.
# Craft: the setup sounds like a complaint, the misdirection is that the
# system "worked perfectly", and the payoff lands in the last few words -
# "never for anyone who actually needed it at 4:59 p.m. on a Friday" -
# the exact moment every office worker has lived through.
JOKE = "I reported the ticket system was down by filing a ticket, and IT closed it as resolved — the system worked perfectly, just never for anyone who actually needed it at 4:59 p.m. on a Friday."

assert 1 <= len(JOKE) <= 200
assert "\n" not in JOKE


def main():
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
