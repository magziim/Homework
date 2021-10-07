
def get_top_performers(file_path, number_of_top_students=5):
    """Return `number_of_top_students` best students by average mark"""
    with open(file_path, "r") as f:
        f.readline()
        lines = f.readlines()

    performers = [(line.split(",")[0], float(line.split(",")[2].removesuffix("\n"))) for line in lines]
    performers.sort(key=lambda x: x[1], reverse=True)

    return [performer[0] for performer in performers[:number_of_top_students]]


def write_students_by_age(input_file_path, output_file_path):
    """Write students sorted by age to `output_file_path`"""
    with open(input_file_path, "r") as f:
        title = f.readline()
        lines = f.readlines()

    lines.sort(key=lambda x: int(x.split(",")[1]), reverse=True)

    with open(output_file_path, "w") as f:
        f.write(title)
        f.writelines(lines)


def main():
    print(get_top_performers("data/students.csv"))
    write_students_by_age("data/students.csv", "data/sorted_students.csv")


if __name__ == "__main__":
    main()
