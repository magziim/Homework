from contextlib import contextmanager


@contextmanager
def file_manager(file_name, file_mode):
    """Context manager for opening and working with file"""

    try:
        file = open(file_name, file_mode)
        yield file

    except Exception as e:
        print("Exception: ", e)

    finally:
        file.close()
        print("closed")


def main():
    with file_manager("output.txt", "r") as f:
        print(f.read())


if __name__ == "__main__":
    main()
