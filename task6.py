import math

class Shape:
    def calculate(self):
        pass

class Square(Shape):
    def calculate(self, length):
        return length ** 2

class Triangle(Shape):
    def calculate(self, base, height):
        return base * height / 2

class Circle(Shape):
    def calculate(self, radius):
        return math.pi * radius ** 2

s = Square()
t = Triangle()
c = Circle()

while True:
    length_input = input("Enter the length of the square : ")
    if not length_input:
        print("Please enter a value to calculate the area of Square.")
        break

    base_input = input("Enter the base of the triangle: ")
    height_input = input("Enter the height of the triangle: ")
    if not base_input or not height_input:
        print("Please enter values for both base and height to calculate the area of Triangle.")
        break

    radius_input = input("Enter the radius of the circle: ")
    if not radius_input:
        print("Please enter a value to calculate the area of Circle.")
        

    length = float(length_input)
    base = float(base_input)
    height = float(height_input)
    radius = float(radius_input)

    print("Area of square:", s.calculate(length))
    print("Area of triangle:", t.calculate(base, height))
        print("Area of circle:", c.calculate(radius))
