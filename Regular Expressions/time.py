import re
import sys


def main():
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")


def convert(tim):
    # Support AM to PM and PM to AM
    pattern = (
        r"^(?P<h1>(?:[1-9]|1[0-2]))(?P<m1>:[0-5][0-9])? (?P<p1>AM|PM) to "
        r"(?P<h2>(?:[1-9]|1[0-2]))(?P<m2>:[0-5][0-9])? (?P<p2>AM|PM)$"
    )

    match = re.match(pattern, tim)
    if not match:
        raise ValueError

    h1, m1, p1 = int(match.group("h1")), match.group("m1") or ":00", match.group("p1")
    h2, m2, p2 = int(match.group("h2")), match.group("m2") or ":00", match.group("p2")

    t1 = to_24h(h1, m1, p1)
    t2 = to_24h(h2, m2, p2)

    return f"{t1} to {t2}"


def to_24h(hour, minute, period):
    # Convert 12h → 24h
    if period == "AM":
        if hour == 12:
            hour = 0
    else:  # PM
        if hour != 12:
            hour += 12
    return f"{hour:02}{minute}"


if __name__ == "__main__":
    main()
