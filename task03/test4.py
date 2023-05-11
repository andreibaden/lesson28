class Super(object):
    def walk(self):
        print("I can walk")

class Subclass(Super):
    pass

base = Super()
sub = Subclass()

print(f"Is base super? - {isinstance(base, Super)}")         # True
print(f"Is base Subclass? - {isinstance(base, Subclass)}")   # False
print(f"Is base super? - {isinstance(sub, Super)}")          # True
print(f"Is base Subclass? - {isinstance(sub, Subclass)}")    # True

