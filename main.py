#!/usr/bin/env python3
"""Make the AI Judge Laugh: the Office Joke Open.

Writes a single one-line office joke to /output/entry.txt.
Pure standard library, no dependencies, no network access.
"""

import os

JOKE = (
    # One specific office detail (reply-all), one turn: the request
    # to escape the thread is exactly what multiplies it.
    "One person replied-all to 400 people asking to be removed "
    "from the list. So far, 38 people have replied-all asking "
    "the same thing."
)


def main():
    text = JOKE.strip()
    assert text, "joke must not be empty"
    assert "\n" not in text, "joke must be a single line"
    assert len(text) <= 200, "joke must be at most 200 characters"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
