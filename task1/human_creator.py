import random
import string
from human import Human


class HumanCreator:
    @staticmethod
    def create(size=10):
        humans = []
        NAMES = ("Alex", "Peter", "Garry", "Alice", "Olga",
                 "Anna", "Kate", "Max", "Andy", "Victor")
        MAX_AGE = 120
        MIN_AGE = 1

        for _ in range(size):
            xman = Human()
            xman.name = random.choice(NAMES)
            xman.name += " " + random.choice(string.ascii_uppercase) + "."
            xman.age = random.randint(MIN_AGE, MAX_AGE)
            xman.is_alive = random.choice((True, False))
            humans.append(xman)

        return humans

