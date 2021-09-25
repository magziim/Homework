
# Implement a function `get_pairs(lst: List) -> List[Tuple]` which returns a list
# of tuples containing pairs of elements. Pairs should be formed as in the
# example. If there is only one element in the list return `None` instead.

def get_pairs(lst: list) -> list[tuple]:
    """returns a list of tuples containing pairs of elements"""
    if len(lst) == 1:
        result = None
    else:
        result = [(lst[i], lst[i + 1]) for i in range(len(lst) - 1)]
    return result


def main():
    example1 = [1, 2, 3, 8, 9]
    print(f"Example1: get_pairs([1, 2, 3, 8, 9]) == {get_pairs(example1)}")
    example2 = ['need', 'to', 'sleep', 'more']
    print(f"Example2: get_pairs(['need', 'to', 'sleep', 'more']) == {get_pairs(example2)}")
    example3 = [1]
    print(f"Example3: get_pairs([1]) == {get_pairs(example3)}")


if __name__ == "__main__":
    main()
