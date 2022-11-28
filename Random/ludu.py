#create random number
#save the score 
#print the number
#take 5 times
#print the final result

import random
import sys

scores={
    "com": 0
}

def setScore(who, score):
    scores[who] = scores[who] + score
    scoreStatus = "{name} => {score}"
    return scoreStatus.format(name = who, score = score)

runned = 0

print("This game is between you and computer. you both will get 5 turns. after 5 turns, you will get the final result ")
userName = str(input("please, set your name > " ))
if(len(userName) < 3):
    print("please enter minimum 3 letter")
    sys.exit()
scores[userName] = 0

while runned < 5:
    print('Turn: ', runned + 1)
    inputedNum = input('press Enter to spine the ludu... ')
    print("\n")
    print(setScore(userName, random.randrange(1,6)), " || " , setScore("com", random.randrange(1,6)))
    print("\n")
    runned = runned + 1

if(scores[userName] > scores["com"]):
    msg = "Congratulations! You won the match. You scored {user} and Computer scored {com}"
    print(msg.format(user= scores[userName], com= scores["com"]))
else:
    msg = "Alas! You lose the match. You scored {user} and Computer scored {com}"
    print(msg.format(user= scores[userName], com= scores["com"]))

# playAgain = input("play again (y/n)")
# if(playAgain == "n" or playAgain == "no"):
#     #start again
# else:
#     sys.exit()
