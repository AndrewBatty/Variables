# Andrew Batty
# Test 1: Quetion 2

weight = int(input("Please enter a value of weight: "))

hundreds = weight // 100
remainder = weight % 100

fifties =  remainder // 50
remainder = remainder % 50

tens = remainder // 10
remainder = remainder % 10

fives = remainder // 5
remainder = remainder % 5

twos = remainder // 2
remainder = remainder % 2

ones = remainder // 1
remainder = remainder % 1

print("Number of 100g: {0}".format(hundreds))
print("Number of 50g: {0}".format(fifties))
print("number of 10g: {0}".format(tens))
print("Number of 5g: {0}".format(fives))
print("Number of 2g: {0}".format(twos))
print("Number of 1g: {0}".format(ones))
