# inheritance = allows a class to inherit attributes and methods from other classes
#               helps with code reusability and extensibility
#               class child(parent)
#               class sub(super)


class Animal:
    def __init__(self, name):
        self.name = name
        self.is_alive = True

    def eat(self):
        print(f"{self.name} is eating")

    def sleep(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("WOOF")

class Cat(Animal):
    def speak(self):
        print("MEOW")

class Mouse(Animal):
    def speak(self):
        print("SQUEEK")

Dog = Dog("Scooby")
Cat = Cat("Tom")
Mouse = Mouse("Jerry")

print(Dog.name)
print(Dog.is_alive)
Dog.eat()
Dog.sleep()
Cat.speak()