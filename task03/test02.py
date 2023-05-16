# Inheritance (Наследование)
class Super(object):
    def walk(self):
        print("I can walk")

class Subclass(Super):
    pass

sub = Subclass()
sub.walk()


