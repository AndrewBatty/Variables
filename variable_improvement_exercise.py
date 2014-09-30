# Andrew Batty
# 15-09-14
# Variable Improvement Exercise

import math

radius = float(input("please enter the radius of the circle: "))

circumferance = 2* math.pi * radius
circumferance = round(circumferance,2)

area = math.pi * radius**2
area = round(area,2)

print("the circumference of the circle is {0}. ".format(circumferance))
print("the area of the this circle is {0}.".format(area))

