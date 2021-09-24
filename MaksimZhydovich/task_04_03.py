
# Implement a function which works the same as `str.split` method

def split_string(input_str, split_sep=" ", max_num_of_splits=-1):
    """Splits a string into a list"""
    result = []
    word = ""
    num_of_splits = 0
    for ch in input_str:
        if ch == split_sep and num_of_splits != max_num_of_splits:
            if split_sep != " " or word:
                result.append(word)
                word = ""
                num_of_splits += 1
        else:
            word += ch

    if word:
        result.append(word)

    return result


def main():
    example1 = "1 2 3"
    example2 = "1,2,,3,"
    example3 = "one two three"
    print(f"Example1: split_string(\"1 2 3\") == {split_string(example1)}")
    print(f"Example2: split_string(\"1,2,,3,\", \',\') == {split_string(example2, ',')}")
    print(f"Example3: split_string(\"1 2 3\", max_num_of_splits=1) == {split_string(example3, max_num_of_splits=1)}")


if __name__ == "__main__":
    main()
