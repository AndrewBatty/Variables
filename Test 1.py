# Andrew Batty
# Test 1

width = int(input("Please enter the width of the pool: "))
length = int(input("Please enter the length of the pool: "))
depth = int(input("Please enter the depth of the pool: "))

mainSectionVolume = length * width * depth

circleRadius = width / 2
circleArea = 3.14 * circleRadius**2
halfCircleVolume = (circleArea / 2) * depth

poolVolume = mainSectionVolume + halfCircleVolume

print("The volume of the pool is: {0}".format(poolVolume))



