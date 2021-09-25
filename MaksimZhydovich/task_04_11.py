
# Implement a function, that receives changeable number of dictionaries (keys - letters, values - numbers)
# and combines them into one dictionary. Dict values should be summarized in case of identical keys.

def combine_dicts(*args):
    """Combines arguments into one dictionary"""
    result = {}
    for arg in args:
        for k in arg:
            if k in result:
                result[k] += arg[k]
            else:
                result[k] = arg[k]

    return result


def main():
    dict_1 = {'a': 100, 'b': 200}
    dict_2 = {'a': 200, 'c': 300}
    dict_3 = {'a': 300, 'd': 100}
    print(f"combine_dicts(dict_1, dict_2) == {combine_dicts(dict_1, dict_2)}")
    print(f"combine_dicts(dict_1, dict_2, dict_3) == {combine_dicts(dict_1, dict_2, dict_3)}")


if __name__ == "__main__":
    main()
