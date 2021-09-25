
# Implement a function that takes a number as an argument and returns a dictionary,
# where the key is a number and the value is the square of that number.

def generate_squares(n: int) -> dict():
    """Returns a dictionary, where the key is a number and the value is the square of that number"""
    result = {i: i ** 2 for i in range(1, n + 1)}
    return result


def main():
    print(f"generate_squares(5) == {generate_squares(5)}")
    print(f"generate_squares(10) == {generate_squares(10)}")


if __name__ == "__main__":
    main()
