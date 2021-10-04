
class Counter:
    """Class provides counter which accepts start and stop values, increment and get methods"""

    def __init__(self, start=0, stop=None):
        """Init Counter class"""
        self.value = start
        self.stop = stop

    def increment(self):
        """Increment counter value"""
        if self.stop is not None and self.value >= self.stop:
            raise ValueError("Maximal value is reached.")
        self.value += 1

    def get(self):
        """Return current counter value"""
        return self.value


def main():
    c = Counter(start=42)
    c.increment()
    print(c.get())

    c = Counter()
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())

    c = Counter(start=42, stop=43)
    c.increment()
    print(c.get())
    c.increment()
    print(c.get())


if __name__ == "__main__":
    main()
