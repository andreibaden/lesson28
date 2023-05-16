# Testing Inheritance as Code Reuse
# (Тестирование наследования, как повторное использование кода)

class Super(object):
    def __init__(self, name="Anna"):
        self._name = name

    # dynamic method
    def walk(self):
        print("I can walk.")

    @property
    def name(self):
        return self._name

    @staticmethod
    def smethod():
        print("static method from Super class")

    @classmethod
    def cmethod(cls):
        print("class method from Super class")

    def function(a, b):
        c = a + b
        print(c)


class Subclass(Super):
    pass


sub = Subclass("Andrei")
sub.walk()

print(sub.name)
print(sub._name)
print("___________")

Subclass.smethod()
sub.smethod()

Subclass.cmethod()
sub.cmethod()

Subclass.function(4, 5)
# sub.function(4, 5)       TypeError: Super.function() takes 2 positional arguments but 3 were given
