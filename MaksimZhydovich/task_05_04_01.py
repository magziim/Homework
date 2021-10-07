a = "I am global variable!"


def enclosing_function():
    a = "I am variable from enclosed function!"

    def inner_function():

        a = "I am local variable!"
        print(a)

    return inner_function()


def main():
    enclosing_function()


if __name__ == "__main__":
    main()
