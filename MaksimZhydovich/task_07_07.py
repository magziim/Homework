class MyNumberCollection:

    def __init__(self, start, end=None, step=None):

        self.number_list = []
        self.start = start
        self.end = end
        self.step = step
        self.index = -1

        if isinstance(start, int) is True:
            for i in range(self.start, self.end, self.step):
                self.number_list.append(i)
            if self.number_list[-1] != self.end:
                self.number_list.append(self.end)
        else:
            for i in self.start:
                if isinstance(i, int) is True:
                    self.number_list.append(i)
                else:
                    raise TypeError('MyNumberCollection supports only numbers!')

    def __repr__(self):

        return str(self.number_list)

    def __getitem__(self, index):

        return self.number_list[index]**2

    def __add__(self, other):

        self.temp = self.number_list.copy()
        for i in other:
            if isinstance(i, int) is True:
                self.temp.append(i)
            else:
                raise TypeError('MyNumberCollection supports only numbers!')
        return self.temp

    def append(self, other):

        if isinstance(other, int) is True:
            self.number_list.append(other)
        else:
            raise TypeError(f'"{other}" - object is not a number!')

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < (len(self.number_list) - 1):
            self.index += 1
            return self.number_list[self.index]
        raise StopIteration


def main():
    col1 = MyNumberCollection(0, 5, 2)
    print(col1)
# [0, 2, 4, 5]
    col2 = MyNumberCollection((1, 2, 3, 4, 5))
    print(col2)
# [1, 2, 3, 4, 5]
# col3 = MyNumberCollection((1,2,3,"4",5))
# TypeError: MyNumberCollection supports only numbers!
    col1.append(7)
    print(col1)
# [0, 2, 4, 5, 7]
# col2.append("string")
# TypeError: 'string' - object is not a number!
    print(col1 + col2)
# [0, 2, 4, 5, 7, 1, 2, 3, 4, 5]
    print(col1)
# [0, 2, 4, 5, 7]
    print(col2)
# [1, 2, 3, 4, 5]
    print(col2[4])
# 25
    for item in col1:
        print(item)


if __name__ == "__main__":
    main()
