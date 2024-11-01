# This program computes the circumference
# and area of a circle using a math module

import math
from ctypes import c_int

# Prompt for radius of a circle
radius_str = input("Enter radius of circle: ")
radius_int = int(radius_str)

# compute the area and circumference
circumference = 2 * math.pi * radius_int
area = math.pi * radius_int**2

# Display the area and circumfrenece of a circle
print("The area of the circle is:", area)
print("The circumference of the circle is:", circumference)