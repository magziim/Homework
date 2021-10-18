def endless_fib_generator():
    a = 0
    b = 1
    while True:
        yield b
        a, b = b, a + b


def main():
    gen = endless_fib_generator()
    while True:
        print(next(gen), " ")


if __name__ == "__main__":
    main()
