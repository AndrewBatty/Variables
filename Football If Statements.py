# Andrew Batty
# Football If Statements

team1 = input("Please enter the name of a football team: ")
team2 = input("please enter the name of another football team: ")

team1_score = int(input("Please enter the sore of the first team: "))
team2_score = int(input("Please enter the score of the secound team: "))

if team1_score > team2_score:
                  print("{0} won, therefore gains 3 points ".format(team1))
elif team1_score == team2_score:
                  print("The teams drew, therefore gains 1 point ")
elif team1_score < team2_score:
                  print("{0} lost, therefore gains 0 points ".format(team1))
                  
