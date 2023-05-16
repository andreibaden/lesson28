# Testing Inheritance as Code Reuse
class Super1():
    def walk(self):
        print("I can walk.")


class Super2():
    def run(self):
        print("I can run.")

class Subclass(Super1, Super2):
    pass

sub1 = Super1()
sub1.walk()
print('_____________')
sub22 = Super2()
sub22.run()
print('_____________')
sub33 = Subclass()
sub33.walk()
sub33.run()

