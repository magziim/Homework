
# Implement a function `get_shortest_word(s: str) -> str` which returns the
# longest word in the given string. The word can contain any symbols except
# whitespaces (` `, `\n`, `\t` and so on). If there are multiple longest words in
# the string with a same length return the word that occures first.

# I think there should be 'longest'
def get_longest_word(s: str) -> str:
    """Returns the longest word in the given string."""
    words = s.split()
    max_length = 0
    max_length_word = ""
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
            max_length_word = word
    return max_length_word


def main():
    example1 = "Python is simple and effective!"
    print(f"Example1: get_shortest_word('Python is simple and effective!') == {get_longest_word(example1)}")
    example2 = "Any pythonista like namespaces a lot."
    print(f"Example2: get_shortest_word('Any pythonista like namespaces a lot.') == {get_longest_word(example2)}")


if __name__ == "__main__":
    main()
