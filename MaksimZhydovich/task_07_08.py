class MySquareIterator:
    def __init__(self, elements):
        self.index = -1
        self.elements = elements

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < (len(self.elements) - 1):
            self.index += 1
            return (self.elements[self.index])**2
        raise StopIteration


def main():
    lst = [1, 2, 3, 4, 5]
    itr = MySquareIterator(lst)
    for item in itr:
        print(item)


if __name__ == "__main__":
    main()
