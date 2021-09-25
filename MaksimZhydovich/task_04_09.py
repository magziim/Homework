
# Implement a bunch of functions which receive a changeable number of strings and return next parameters.

from string import ascii_lowercase


def test_1_1(*strings: str) -> set():
    """Returns characters that appear in all strings"""
    characters = set()
    for ch in strings[0]:
        is_appear = True
        for s in strings:
            if ch not in s:
                is_appear = False
                break
        if is_appear:
            characters.add(ch)

    return characters


def test_1_2(*strings: str) -> set():
    """Returns characters that appear in at least one string"""
    characters = set(ch for s in strings for ch in s)
    return characters


def test_1_3(*strings: str) -> set():
    """Returns characters that appear at least in two strings"""
    characters = set()
    all_characters = [ch for s in strings for ch in s]
    for ch in all_characters:
        if all_characters.count(ch) >= 2:
            characters.add(ch)

    return characters


def test_1_4(*strings: str) -> set():
    """Returns characters of alphabet, that were not used in any string"""
    characters = set()
    all_characters = [ch for s in strings for ch in s]
    for ch in ascii_lowercase:
        if ch not in all_characters:
            characters.add(ch)

    return characters


def main():
    test_strings = ["hello", "world", "python", ]
    print(f"Test strings: {test_strings}")
    print(f"Characters that appear in all strings: {test_1_1(*test_strings)}")
    print(f"Characters that appear in at least one string: {test_1_2(*test_strings)}")
    print(f"Characters that appear at least in two strings: {test_1_3(*test_strings)}")
    print(f"Characters of alphabet, that were not used in any string: {test_1_4(*test_strings)}")


if __name__ == "__main__":
    main()
