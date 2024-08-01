import random

def rockPaperScissors(user_input, computer):
    rock="rock"
    paper="paper"
    scissors="scissors"

    if (user_input==rock)&(computer==rock):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "draws with ",computer)
    elif(user_input==paper)&(computer==paper):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "draws with ",computer)
    elif(user_input==scissors)&(computer==scissors):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "draws with ",computer)
    
    #Computer wins--------------------
    elif(user_input==paper)&(computer==scissors):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "loses against ",computer)
    elif(user_input==scissors)&(computer==rock):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "loses against ",computer)
    elif(user_input==rock)&(computer==paper):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "loses against ",computer)

    #Player wins-------------------
    elif(user_input==paper)&(computer==rock):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "wins against ",computer)
    elif(user_input==scissors)&(computer==paper):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "wins against ",computer)
    elif(user_input==rock)&(computer==scissors):
        print("you:   ",user_input)
        print("computer:   ",computer)
        print(user_input, "wins against ",computer)


list=["rock","scissors","paper"]
comp=random.choice(list)
index=0

response=input("would you like to play Rock Paper Scissors?:   'Y' for yes or 'N'for no ").upper()

while(response!="Y" and response!="N" and index!=2):
    response=input("would you like to play Rock Paper Scissors?:   'Y' for yes or 'N'for no ").upper()
    index+=1
    if index==2:
        break

while(response=="Y"):
    print()
    user=input("rock,paper,scissors,shoot!").lower()
    rockPaperScissors(user,comp)
    print()
    response=input("would you like to play Rock Paper Scissors?:   'Y' for yes or 'N'for no ").upper()
else:
    print()
    print("I had fun playing against you!")


      
    