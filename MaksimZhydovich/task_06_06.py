from functools import total_ordering


@total_ordering
class Money:
    """Class provides exchange rates and operations with them"""

    exchange_rate = {
        "USD": 2.51,
        "EUR": 2.91,
        "BYN": 1.0,
    }

    def __init__(self, value, currency="BYN"):
        """Init Money class"""
        self.value = value
        self.currency = currency

    def __str__(self):
        return f"{self.value} {self.currency}"

    def __add__(self, other):
        if isinstance(other, Money):
            return Money(self.value + other.value * Money.exchange_rate[other.currency] /
                         Money.exchange_rate[self.currency], self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value + other, self.currency)
        raise AttributeError

    def __radd__(self, other):
        return self + other

    def __mul__(self, other):
        if isinstance(other, Money):
            return Money(self.value * (other.value * Money.exchange_rate[other.currency] /
                                       Money.exchange_rate[self.currency]), self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value * other, self.currency)
        raise AttributeError

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        if isinstance(other, Money):
            return Money(self.value / (other.value * Money.exchange_rate[other.currency] /
                                       Money.exchange_rate[self.currency]), self.currency)
        if isinstance(other, (int, float)):
            if other == 0:
                raise ZeroDivisionError
            return Money(self.value / other, self.currency)
        raise AttributeError

    def __rtruediv__(self, other):
        if isinstance(other, (int, float)):
            return Money(other / self.value, self.currency)
        raise AttributeError

    def __sub__(self, other):
        if isinstance(other, Money):
            return Money(self.value - other.value * Money.exchange_rate[other.currency] /
                         Money.exchange_rate[self.currency], self.currency)
        if isinstance(other, (int, float)):
            return Money(self.value - other, self.currency)
        raise AttributeError

    def __rsub__(self, other):
        if isinstance(other, (int, float)):
            return Money(-self.value + other, self.currency)
        raise AttributeError

    def __eq__(self, other):
        if isinstance(other, Money):
            # return self.value == round(other.value * (Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]), 1)
            return self.value == other.value * (Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency])
        if isinstance(other, (int, float)):
            return self.value == other
        raise AttributeError

    def __lt__(self, other):
        if isinstance(other, Money):
            return self.value < other.value * Money.exchange_rate[other.currency] / Money.exchange_rate[self.currency]
        if isinstance(other, (int, float)):
            return self.value < other
        raise AttributeError


def main():
    if __name__ == '__main__':
        x = Money(10, "USD")
        y = Money(11)
        z = Money(12, "EUR")
        print(x + y)
        print(x * y)
        print(x - y)
        print(x / y)
        print(Money(251) >= Money(100, "USD"))
        print(Money(251) < Money(100, "USD"))
        print(Money(100, "EUR") != Money(100, "USD"))

        print(z + 3.11 * x + y * 0.8)

        lst = [Money(10, "EUR"), Money(11), Money(12, "USD")]
        s = sum(lst)
        print(s)


if __name__ == "__main__":
    main()
