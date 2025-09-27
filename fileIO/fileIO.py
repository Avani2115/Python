import sys
import csv


def main():
    before, after = checkerror()
    change(before, after)


def change(b, a):
    try:
        with open(b, "r") as f1, open(a, "w", newline="") as f2:
            #read from the file
            reader = csv.DictReader(f1)

            # Prepare writer with correct headers
            writer = csv.DictWriter(f2, fieldnames=["first", "last", "house"])
            #write the headers
            writer.writeheader()

            # Process each row, cuz thats the way to do this.
            for row in reader:
                #make the split
                last, first = row["name"].split(", ")
                #now write, row by row
                writer.writerow(
                    {
                        "first": first,
                        "last": last,
                        "house": row["house"]
                    }
                )
                # no need to save, it is done automatically by with

    except FileNotFoundError:
        sys.exit(f"Could not read {b}")


def checkerror():
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    elif len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif not sys.argv[1].endswith(".csv") or not sys.argv[2].endswith(".csv"):
        sys.exit("Not a CSV file")
    else:
        #we can return two values, they are treated as tuples.
        return sys.argv[1], sys.argv[2]


if __name__ == "__main__":
    main()
