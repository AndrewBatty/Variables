#Andrew Batty
#22/09/14
#Currency problem


print("this calculation will display the amount of notes and coins that make up the whole number of currency")

value = int(input("please enter the whole number of currency: "))

twenties = value // 20
remainder = value % 20

tens = remainder // 10
remainder = remainder % 5

fives = remainder // 5
remainder = remainder % 5

twos = remainder // 2
remainder = remainder % 2

ones = remainder // 1
remainder = reminder % 1

print ("The number of £20" + twenties, "number of £10" + tens, "number of £5" + fives, "number of £2" + twos, “number of + £1” ones .format (twenties,
Tens, fives, twos, ones)
