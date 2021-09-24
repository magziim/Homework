
# Implement a function which receives a string and replaces all '"' symbols with '''and vise versa

def replace_symbol(input_str):
    """Replaces all '"' symbols with '''and vise versa"""
    result = ""
    for ch in input_str:
        if ch == "\"":
            res_ch = "\'"
        elif ch == "\'":
            res_ch = "\""
        else:
            res_ch = ch
        result += res_ch

    return result


def main():
    my_str = "\"Example1\" \'example2\'"
    print(f"Before: {my_str}")
    print(f"After: {replace_symbol(my_str)}")


if __name__ == "__main__":
    main()
