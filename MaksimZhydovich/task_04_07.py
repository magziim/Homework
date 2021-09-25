
# Implement a function `foo(List[int]) -> List[int]` which, given a list of
# integers, return a new list such that each element at index `i` of the new list
# is the product of all the numbers in the original array except the one at `i`.

def foo(lst: list[int]) -> list[int]:
    """return a new list such that each element at index `i` of the new list
    is the product of all the numbers in the original array except the one at `i`"""
    product_of_elements = 1
    for el in lst:
        product_of_elements *= el

    result = []
    for el in lst:
        result.append(product_of_elements // el)

    return result


def main():
    example1 = [1, 2, 3, 4, 5]
    print(f"Example1: foo([1, 2, 3, 4, 5]) == {foo(example1)}")
    example2 = [3, 2, 1]
    print(f"Example2: foo([3, 2, 1]) == {foo(example2)}")


if __name__ == "__main__":
    main()
