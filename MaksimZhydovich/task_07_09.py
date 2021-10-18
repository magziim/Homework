import time


class EvenRange:
    def __init__(self, low, high):
        self.current = low
        self.high = high
        self.flag = False

    def __iter__(self):
        return self

    def is_next(self):
        while True:
            self.current += 1
            if self.current % 2 != 0:
                continue
            else:
                break
        if self.current < self.high:
            return self.current
        raise StopIteration

    def __next__(self):
        while True:
            try:
                return self.is_next()
            except StopIteration:
                if self.flag is False:
                    self.flag = True
                    return 'Out of numbers!'
                else:
                    raise StopIteration


def main():
    er1 = EvenRange(7, 11)
    print(next(er1))
    # 8
    print(next(er1))
    # 10
    print(next(er1))
    # "Out of numbers!"
    # print(next(er1))
    # "Out of numbers!"
    er2 = EvenRange(3, 14)
    for number in er2:
        print(number)
    # 4 6 8 10 12 "Out of numbers!"


if __name__ == "__main__":
    main()
