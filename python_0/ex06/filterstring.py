import sys


def main() -> None:
    """Filter words in a string based on their length and print the result."""
    if len(sys.argv) != 3:
        print("AssertionError: the arguments are bad")
        return

    s = sys.argv[1]
    try:
        n = int(sys.argv[2])
    except ValueError:
        print("AssertionError: the arguments are bad")
        return

    if n < 0:
        print("AssertionError: the arguments are bad")
        return

    words = s.split()
    is_longer_than_n = lambda word: len(word) > n
    result = [word for word in words if is_longer_than_n(word)]
    print(result)

if __name__ == "__main__":
    main()
