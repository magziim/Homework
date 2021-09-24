
# Implement a function `split_by_index(s: str, indexes: List[int]) -> List[str]`
# which splits the `s` string by indexes specified in `indexes`. Wrong indexes
# must be ignored.

def split_by_index(s: str, indexes: list[int]) -> list[str]:
    """Splits the `s` string by indexes specified in `indexes`"""
    result = []
    old_index = 0
    # create copy of `indexes` and add len of string to it
    c_indexes = indexes.copy() + [len(s)]
    for index in c_indexes:
        word = ""
        if old_index <= index <= len(s):
            for i in range(old_index, index):
                word += s[i]
            result.append(word)
            old_index = index

    return result


def main():
    example1 = "pythoniscool,isn'tit?"
    print(f"Example1: split_by_index(\"pythoniscool,isn'tit?\", [6, 8, 12, 13, 18]) == "
          f"{split_by_index(example1, [6, 8, 12, 13, 18])}")
    example2 = "pythoniscool,isn'tit?"
    print(f"Example2: split_by_index(\"no luck\", [42]) == "
          f"{split_by_index('no luck', [42])}")


if __name__ == "__main__":
    main()
