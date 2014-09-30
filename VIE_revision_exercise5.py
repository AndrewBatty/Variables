# Andrew Batty
# 23-09-14
# Variable Improvement Exercise: Revision exercise 5

print("This program is to find out the space left in a lift, when a fridge is put into the lift")

liftHeight = int(input("Please enter the height of the lift: "))
liftWidth = int(input("Please enter the width of th lift: "))
liftDepth = int(input("Please enter the depth of the lift: "))

fridgeHeight = int(input("Please enter the hight of the fridge: "))
fridgeWidth = int(input("Please enter the width of the fridge: "))
fridgeDepth = int(input("Please enter the depth of the fridge: "))

liftVolume = liftHeight * liftWidth * liftDepth
fridgeVolume = fridgeHeight * fridgeWidth * fridgeDepth

leftSpace = liftVolume - fridgeVolume

print("The remaining space left in the lift is: {0}".format(leftSpace))
