
class Sun:
    """Class provides singleton logic"""

    __instance = None

    @classmethod
    def inst(cls):
        """Method used for initialize object"""
        if cls.__instance is None:
            cls.__instance = Sun()

        return cls.__instance


def main():
    a = Sun.inst()
    b = Sun.inst()

    print(a == b)
    print(b == a)
    print(a is b)
    print(b is a)


if __name__ == "__main__":
    main()
