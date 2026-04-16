import sys

mors_code = {
    ' ': '/',
    'A': '.-',
    'B': '-...',
    'C': '-.-.',
    'D': '-..',
    'E': '.',
    'F': '..-.',
    'G': '--.',
    'H': '....',
    'I': '..',
    'J': '.---',
    'K': '-.-',
    'L': '.-..',
    'M': '--',
    'N': '-.',
    'O': '---',
    'P': '.--.',
    'Q': '--.-',
    'R': '.-.',
    'S': '...',
    'T': '-',
    'U': '..-',
    'V': '...-',
    'W': '.--',
    'X': '-..-',
    'Y': '-.--',
    'Z': '--..',
    '0': '-----',
    '1': '.----',
    '2': '..---',
    '3': '...--',
    '4': '....-',
    '5': '.....',
    '6': '-....',
    '7': '--...',
    '8': '---..',
    '9': '----.'
}


def main() -> None:
    """Convert input text to Morse code and print it."""
    args = sys.argv[1:]

    if len(args) != 1:
        print("AssertionError: the arguments are bad")
        return

    morse_words = []
    text = args[0].upper()
    for char in text:
        if char not in mors_code:
            print("AssertionError: the arguments are bad")
            return
        morse_words.append(mors_code[char])

    print(' '.join(morse_words))


if __name__ == "__main__":
    main()
