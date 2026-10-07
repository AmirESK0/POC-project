# Python Object-Oriented Programming
# object = A "bundle" of related attributes (variables) and methods (functions)
#          Ex. phone, cup, book
#          you need a class to create many objects
#
# class = (blueprint) used to design the structure and layout of an object

class car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    # methods__
    def drive(self):
        print(f"u drive the {self.color} {self.model}")
    def stop(self):
        print(f"u stop the {self.color} {self.model}")
    def describe(self):
        print(f"{self.year} {self.color} {self.model}")


# objects__
car1 = car("BMW M8", 2025, "black", True)
car2 = car("M3 GTR (E46)", 2001, "blue", False)

print(car1.model)
print(car1.year)
print(car1.color)
print(car1.for_sale)

car1.stop()
car2.drive()

car2.describe()