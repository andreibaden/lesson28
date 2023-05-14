from human import Human


class Manager:
    @staticmethod
    def count_adult(people):
        if isinstance(people, (list, tuple)):
            count = 0

            for manx in people:
                if (isinstance(manx, Human) and manx.age >= 18):
                    count += 1

            return count

    @staticmethod
    def count_underage(people):
        if isinstance(people, (list, tuple)):
            total = len(people)
            total -= Manager.count_adult(people)
        return total


def main():
    h1 = Human("Alex", 20, 10)
    h2 = Human("Kate", 18, 7)
    h3 = Human("Garry", 15, 9)

    ls = (h1, h2, h3)

    underage = Manager.count_underage(ls)
    print(f"Underage people - {underage}")


if __name__ == "__main__":
    main()
