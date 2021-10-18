import time


def endless_generator():
    count = -1
    while True:
        time.sleep(1)
        count += 2
        yield count


def main():
    gen = endless_generator()
    while True:
        print(next(gen))
    # 1 3 5 7 ...


if __name__ == "__main__":
    main()
