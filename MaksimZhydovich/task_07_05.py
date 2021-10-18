class NotEvenError(BaseException):
    def __init__(self, message=None):
        self.msg = message

    def __str__(self):
        return repr(self.msg)


def is_even(number):
    if number > 2 and number % 2 == 0:
        return True
    return NotEvenError("Num isn\'t even")


def main():
    print(is_even(2))


if __name__ == "__main__":
    main()
