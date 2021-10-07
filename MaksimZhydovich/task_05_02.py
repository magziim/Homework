
def most_common_word(filepath, number_of_words=3):
    """Return `number_of_words` most common words in file"""

    common_words = {}
    with open(filepath, "r") as f:
        words = f.read().split()

    for word in words:
        if word in common_words.keys():
            common_words[word] += 1
        else:
            common_words[word]= 1

    sorted_common_words = sorted(common_words.items(), key=lambda x: x[1], reverse=True)

    return [p[0] for p in sorted_common_words[:number_of_words]]


def main():
    print(most_common_word("data/lorem_ipsum.txt"))


if __name__ == "__main__":
    main()
