# Andrew Batty
# 23/09/14
# Development Exercise 3

print("This program will convert your height form inches into centimetres, and your weight from stone into kilograms")


height = float(input("Please enter your Heigh in inches: "))

weight = float(input("please enter your Weight in stone: "))

cmHeight = height * 2.54

kgWeight = weight * 6.364

print("Your Height in cntimetres is: {0}".format(cmHeight))

print("Your Weight in kilograms is: {0}".format(kgWeight))
