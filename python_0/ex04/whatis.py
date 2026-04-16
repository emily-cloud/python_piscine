import sys

def main() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        return

    if len(args) > 1:
        print("AssertionError: more than one argument is provided")
        return

    try:
        number = int(args[0])
    except ValueError:
        print("AssertionError: argument is not an integer")
        return

    if number % 2 == 0:
        print("I'm Even.")
    else:
        print("I'm Odd.")

if __name__ == "__main__":
    main()