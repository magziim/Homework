
def sort_file(input_file_name, output_file_name):
    """Read lines from `input_file_name`, sort and write them to a new file `output_file_name`"""

    with open(input_file_name, "r") as f:
        lines = f.readlines()

    sorted_lines = sorted(lines)

    with open(output_file_name, "w") as f:
        f.writelines(sorted_lines)


def main():
    sort_file("data/unsorted_names.txt", "data/sorted_names.txt")


if __name__ == "__main__":
    main()
