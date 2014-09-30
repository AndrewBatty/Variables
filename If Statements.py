# Andrew Batty
# If Statements

age = int(input("Please enter your name: "))

if age >= 18:
    print("You are old enough to vote.")
else:
    print("You are too young to vote.")

retirement = 65 - age

if retirement >= 65:
    print("You are old enogh to retire")
else:
    print("you are not old enough to retire. You have {0} years til you are able to retire".format(retirement))
    
    
    
