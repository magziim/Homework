from threading import Thread, Lock
from time import sleep


class Fork:
    def __init__(self):
        self.fork = Lock()


class Philosopher(Thread):
    def __init__(self, name, left, right):
        Thread.__init__(self)
        self.name = name
        self.left = left
        self.right = right
        self.times = 0

    def think(self):
        print(f"{self.name} is thinking\n")
        sleep(3)

    def eat(self):
        ending = "time" if self.times == 1 else "times"
        print(f"{self.name} started eating\n")
        sleep(10)
        self.times += 1
        print(f"{self.name} ate {self.times} {ending}\n")

    def decide(self):
        while True:
            self.think()
            if not self.left.locked():
                with self.left:
                    print(f"{self.name} took left fork\n")
                    self.think()
                    if not self.right.locked():
                        with self.right:
                            print(f"{self.name} took right fork\n")
                            self.eat()

    def run(self):
        self.decide()


if __name__ == "__main__":
    thinkers_list = ["Heidegger", "Kierkegaard", "Plato", "Evola", "Sartre"]
    forks = [Lock() for i in range(5)]
    philosophers = [
        Philosopher(f"{thinkers_list[i]}", forks[i], forks[(i + 1) % 5])
        for i in range(5)
    ]
    for philosopher in philosophers:
        philosopher.start()