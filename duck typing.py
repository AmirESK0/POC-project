# duck typing = Another way to achieve polymorphism besides inheritance
#               Python does NOT care about the class type.
#               Objects must have the minimum attributes/methods
#               "If it looks like a duck and quacks like a duck, it must be a duck."

class Animal:
    is_alive = True

class Dog(Animal):
    def speak(self):
        return "WOOF!"

class Cat(Animal):
    def speak(self):
        return "MEOW!"

class Car:
    # Not an Animal — but it still "quacks"
    is_alive = False

    def speak(self):
        return "HONK!"

# All objects below share:
# - speak()
# - is_alive
animals = [Dog(), Cat(), Car()]

# Duck typing: no type checks, only behavior
for animal in animals:
    print(animal.speak())
    print(animal.is_alive)