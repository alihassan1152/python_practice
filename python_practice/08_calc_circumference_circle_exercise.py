# Exercise no:1 -- calculate the circumference circle

import math
radius = float(input("Enter the radius of circle:"))

circumference = 2 * math.pi * radius
print(f"The circumference of circle area is: {round(circumference, 2)}cm")

# Exercise no:2 -- calculate the area of circle

import math

radius = float(input("Enter the radius of a circle:"))

area = math.pi * math.pow(radius, 2)

print(f"The area of circle is: {round(area)}cm")

# Exercise no:3 -- find the hypotenuse of triangle

import math
a = float(input("Enter side A:"))
b = float(input("Enter side B:"))

c = math.sqrt(pow(a, 2)) + (pow(b, 2))
print(f"The value of square root is: {round(c)}c^m")