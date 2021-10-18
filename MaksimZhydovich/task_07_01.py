class FileManager:
    """Context manager for opening and working with file"""

    def __init__(self, file_name, file_mode):
        self._file_name = file_name
        self._file_mode = file_mode

    def __enter__(self):
        self._file = open(self._file_name, self._file_mode)
        return self._file

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self._file.close()


def main():
    with FileManager("output.txt", "w") as f:
        f.write("TEST01")


if __name__ == "__main__":
    main()
