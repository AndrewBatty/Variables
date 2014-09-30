# Andrew Batty
# 23/09/14
# Development Exercise 4

print("This program will calculate the volume of wter needed to fill a swimming pool from a lesuire centre")

length = int(input("Please enter the length of the pool: "))
width = int(input("Please enter the width of the pool: "))

deepDepth = int(input("Please enter the depth of the deep end: "))
shallowDepth = int(input("Please enter the depth of the shallow end: "))

volume = ((length * width * deepDepth) - (length * width * shallowDepth))

print("The volume needed to fill the pool with water is: {0}".format(volume))
