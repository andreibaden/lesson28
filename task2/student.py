from human import Human


class Student(Human):
    def __init__(self, name='no name', age='1', alive=True, mark=4):
        super().__init__(name, age, alive)
        self.__mark = mark

    def can_study(self):
        print(self.name + " can study!")

    @property
    def mark(self):
        return self.__mark

    @mark.setter
    def mark(self, mark):
        if 0 <= mark <= 10:
            self.__mark = mark


    def __str__(self):
        return super().__str__() + f"Mark = {self.__mark}."


# def main():
#     h1 = Human()
#     h1.name = "Anna"
#     h1.age = -20
#     print(h1)
#
#     h2 = Human("KATE", 18, False)
#     print(h2)
#
#
# if __name__ == "__main__":
#     main()
