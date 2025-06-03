import math

od = ['circle', 'square']
td = ['triangle', 'rectangle']
r2 = 1


def calculate_area(shape, r, b):
    shapearea = {"triangle": 0.5 * r * b, "rectangle": r * b, "square": r ** 2, "circle": math.pi * r ** 2}
    return shapearea[shape]


selection = input(
    "Please enter the shape you'd like to calculate the area of: Triangle, Rectangle, Square or Circle? ").lower()

r = float(input("Please enter your dimension: "))

if selection in td:
    r2 = float(input("Please enter your second dimension: "))

area = calculate_area(selection, r, r2)
print(area)

