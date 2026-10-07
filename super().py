# super() = Function used in a child class to call methods from a parent class (superclass).
#         allows u to extend the functionality of the inherited methods


class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"it is {self.color} and {'filled' if self.filled else 'not filled'}")
class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    # method overwriting__
    def describe(self):
        super().describe()
        print(f"it is a circle with the area of {self.radius * 3.14 * self.radius}cm²")


class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width

    def describe(self):
        super().describe()
        print(f"it is a square with the area of {self.width * self.width}cm²")

class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width
        self.height = height

    def describe(self):
        super().describe()
        print(f"it is a triangle with the area of {self.width * self.height / 2}cm²")

circle = Circle(color="red", filled=True, radius=5)
square = Square(color="blue", filled=False, width=8)
triangle = Triangle(color="yellow", filled=False, width=7, height=8)

print(circle.color)
print(circle.filled)
print(f"{circle.radius}cm")

print(triangle.color)
print(triangle.filled)
print(f"{triangle.width}cm")
print(f"{triangle.height}cm")

square.describe()

circle.describe()
square.describe()
triangle.describe()