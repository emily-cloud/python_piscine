import sys


def count_cap(text: str) -> int:
    """Count uppercase letters in a string."""
    count = 0
    for char in text:
        if char.isupper():
            count += 1
    return count


def count_low(text: str) -> int:
    """Count lowercase letters in a string."""
    count = 0
    for char in text:
        if char.islower():
            count += 1
    return count


def count_punct(text: str) -> int:
    """Count punctuation marks in a string."""
    count = 0
    for char in text:
        if not char.isalnum() and not char.isspace():
            count += 1
    return count


def count_space(text: str) -> int:
    """Count spaces in a string."""
    count = 0
    for char in text:
        if char.isspace():
            count += 1
    return count


def count_digit(text: str) -> int:
    """Count digits in a string."""
    count = 0
    for char in text:
        if char.isdigit():
            count += 1
    return count

def main() -> None:
    """Analyze and print text character statistics."""
    args = sys.argv[1:]

    if len(args) == 0:
        return

    if len(args) > 1:
        return

    cha_len = len(args[0])
    print(f"The text contains {cha_len} characters:")
    cap_len = count_cap(args[0])
    print(f"{cap_len} upper letters")
    lower_len = count_low(args[0])
    print(f"{lower_len} lower letters")
    punct_len = count_punct(args[0])
    print(f"{punct_len} punctuation marks")
    space_len = count_space(args[0])
    print(f"{space_len} spaces")
    digit_len = count_digit(args[0])
    print(f"{digit_len} digits")

if __name__ == "__main__":
    main()