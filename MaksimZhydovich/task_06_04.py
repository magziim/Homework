
class Bird:
    """Class provides methods `fly` and `walk`"""

    def __init__(self, name):
        """Init Bird"""
        self.name = name

    def fly(self):
        return f"{self.name} bird can fly"

    def walk(self):
        return f"{self.name} bird can walk"

    def __str__(self):
        return f"{self.name} can walk and fly"


class FlyingBird(Bird):
    """Class provides methods `fly`, `walk` and `eat`"""

    def __init__(self, name, ration="grains"):
        """Init FlyingBird"""
        super().__init__(name)
        self.ration = ration

    def eat(self):
        return f"It eats mostly {self.ration}"

    def __str__(self):
        return f"{self.name} can walk and fly"


class NonFlyingBird(Bird):
    def __init__(self, name, ration="fish"):
        """Init NonFlyingBird"""
        super().__init__(name)
        self.ration = ration

    def fly(self):
        raise AttributeError(f'{self.name} has no attribute fly')

    def eat(self):
        return f"It eats mostly {self.ration}"

    def swim(self):
        return f"{self.name} bird can swim"

    def __str__(self):
        return f"{self.name} can walk, swim, but can\'t fly"


class SuperBird(FlyingBird, NonFlyingBird):
    def __init__(self, name, ration="fish"):
        """Init SuperBird"""
        super().__init__(name, ration)

    def fly(self):
        return FlyingBird.fly(self)

    def __str__(self):
        return f"{self.name} bird can walk, swim and fly"


def main():
    b = Bird("Any")
    print(str(b))
    print(b.fly())
    print(b.walk())

    c = FlyingBird("Canary")
    print(str(c))
    print(c.fly())
    print(c.walk())
    print(c.eat())

    p = NonFlyingBird("Penguin")
    print(str(p))
    # print(p.fly())
    print(p.walk())
    print(p.eat())
    print(p.swim())

    s = SuperBird("Maks")
    print(str(s))
    print(s.fly())
    print(s.walk())
    print(s.eat())
    print(s.swim())


if __name__ == '__main__':
    main()
