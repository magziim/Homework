
# Write a function that check whether a string is a palindrome or not

def is_palindrome(input_str):
    """Check whether a string is a palindrome or not"""
    input_str_symbols = [ch for ch in input_str.lower() if ch.isalnum()]
    original_str = "".join(input_str_symbols)
    return original_str == original_str[::-1]


def main():
    my_str = "Murder for a jar of red rum"
    print(f"Is \"{my_str}\" a palindrome: {is_palindrome(my_str)}")


if __name__ == "__main__":
    main()
