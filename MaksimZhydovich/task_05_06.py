
def call_once(f):
    """Decorator which runs a function or method once and caches the result.
All consecutive calls to this function should return cached result no matter the arguments."""
    func_call = None

    def wrapper(*args):
        nonlocal func_call
        if func_call is None:
            func_call = f(*args)

        return func_call

    return wrapper


@call_once
def sum_of_numbers(a, b):
    return a + b


def main():
    print(sum_of_numbers(13, 42))
    print(sum_of_numbers(999, 100))
    print(sum_of_numbers(134, 412))
    print(sum_of_numbers(856, 232))


if __name__ == "__main__":
    main()
