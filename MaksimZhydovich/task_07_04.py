import functools


def catch_exceptions(f):
    @functools.wraps(f)
    def exceptions_handler(*args, **kwargs):
        flag = False
        try:
            return f(*args, **kwargs)
        except Exception:
            flag = True
        finally:
            if flag:
                print("Suppressing")
    return exceptions_handler()


@catch_exceptions
def myexcept():
    raise Exception("Exception executed")


def main():
    myexcept()


if __name__ == "__main__":
    main()
