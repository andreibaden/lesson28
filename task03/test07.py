class Super(object):
    def __init__(self, id=0):
        self.id = id

    def just_do_it(self):
        print("I'm study!")
        print("I'm study!")
        print("I'm study!")


class Subclass(Super):
    def __init__(self, id=0, name="no name"):
        super().__init__(id)
        self.name = name

    def just_do_it(self):
        super().just_do_it()
        print("I'm hard study!")

