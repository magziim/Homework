
class HistoryDict(dict):
    """Class provides custom dictionary that will memorize 10 latest changed keys"""

    def __init__(self, *args, **kwargs):
        """Init HistoryDict class"""
        super().__init__(*args, **kwargs)
        self.__changed_keys = []

    def set_value(self, key, value):
        """Add value to dictionary"""
        if key in self and self[key] == value:
            return

        self[key] = value
        if key in self.__changed_keys:
            self.__changed_keys.remove(key)
        self.__changed_keys.append(key)

        if len(self.__changed_keys) > 10:
            self.__changed_keys.pop(0)

    def get_history(self):
        """Return keys"""
        return self.__changed_keys


def main():
    d = HistoryDict({"foo": 42})
    print(d)
    d.set_value("bar", 43)
    print(d.get_history())

    d.set_value("bar1", 1)
    d.set_value("bar2", 2)
    d.set_value("bar3", 3)
    d.set_value("bar4", 4)
    d.set_value("bar5", 5)
    d.set_value("bar6", 6)
    d.set_value("bar7", 7)
    d.set_value("bar8", 8)
    d.set_value("bar9", 9)

    print(d.get_history())

    d.set_value("bar10", 10)
    print(d.get_history())

    d.set_value("bar1", 11)
    print(d.get_history())


if __name__ == "__main__":
    main()
