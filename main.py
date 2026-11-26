import os

ENTRY = (
    "A traffic jam is like Maya trying to pour 100 marbles through one drinking straw "
    "in the back seat on the way home from school: they all rush the tiny opening at "
    "once, so nobody gets through.\n"
    "It works because the cars, like the marbles, all squeeze toward one narrow road "
    "together, but it leaves out the drivers, who can pick another road — and "
    "a jam clears from the front, not the back.\n"
)


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
