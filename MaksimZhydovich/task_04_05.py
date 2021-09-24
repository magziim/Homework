
# Implement a function `get_digits(num: int) -> Tuple[int]` which returns a tuple
# of a given integer's digits.

def get_digits(num: int) -> tuple[int]:
    """returns a tuple of a given integer's digits"""
    digits = []
    while num != 0:
        digits.append(num % 10)
        num //= 10
    return tuple(digits[::-1])


def main():
    example = 87178291199
    print(f"Example: get_digits(87178291199) == {get_digits(example)}")


if __name__ == "__main__":
    main()
