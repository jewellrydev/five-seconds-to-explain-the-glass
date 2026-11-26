#!/usr/bin/env python3
"""A Small Push — entry for Five Seconds to Explain the Glass on make.fun.

Prints exactly one sentence (at most 200 characters) in the voice of a
house cat, five seconds after sweeping a glass off the table.
"""

LINE = "That glass chose to live on the edge long before I arrived; I simply gave its destiny a small, elegant push."


def main() -> None:
    assert "\n" not in LINE
    assert len(LINE) <= 200
    print(LINE)


if __name__ == "__main__":
    main()
