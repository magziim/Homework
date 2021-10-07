
def remember_result(f):
    """Decorator which remembers last result of function and prints it before next call"""

    last_call = None

    def wrapper(*args):
        nonlocal last_call
        print(f"Last call: {last_call}")
        last_call = f(*args)

    return wrapper


@remember_result
def sum_list(*args):
    """Return sum of *args"""
    result = ""
    for item in args:
        result += str(item)
    print(f"Current result = {result}")
    return result


def main():
    sum_list("a", "b")
    sum_list("abc", "cde")
    sum_list(3, 4, 5)


if __name__ == "__main__":
    main()
