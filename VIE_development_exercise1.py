# Andrew Batty
# 23/09/14
# Development Exercise 1

print("This program calculates the remainder of 2 integers")

number1 = int(input("Please enter a number: "))
number2 = int(input("Please enter another number: "))

answer = number1 // number2
remainder = number1 % number2

print("The answer is: {0} , remainder {1}".format(answer , remainder))
