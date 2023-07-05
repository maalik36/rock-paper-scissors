import random
import math
file = open('rating.txt', 'r+')
decision = ""
score = 0
print("Enter your name:")
decision = input()
print("Hello, " + decision)
for line in file:
    if decision in line:
        player = line
        list = player.split(" ")
        score = int(list[1])
    else:
        file.write(decision + " " + str(score))
        player = decision + " " + str(score)
        line = player.split(" ")
decision = input()
if decision == "":
    spock = ["rock", "paper", "scissors"]
else:
    spock = decision.split(",")
print("Okay, let's start")
while decision != "!exit":
    win = []
    lose = []
    j = 0
    decision = input()
    if decision != "!exit" and decision != "!rating" and decision not in spock:
        print("Invalid input")
    if decision == "!rating":
        print("Your rating: " + str(score))
    if decision == "!exit":
        break
    choice = random.choice(spock)
    for i in spock:
        if decision == i:
            temp = spock.index(i)
            half = math.floor(len(spock) / 2)
            end = spock[len(spock) - 1]
            beg = spock[0]
            spot = half + temp
            temp+=1
            while j < half:
                if temp > spock.index(end):
                    temp = 0
                win.append(spock[temp])
                
                j+= 1
                temp+=1
            j = 0
            temp = spock.index(i)
            temp-= 1
            while j < half:
                if temp < spock.index(beg):
                    temp = len(spock) - 1
                lose.append(spock[temp])
                j+= 1
                temp-= 1
            
   
    if decision == choice:
        print("There is a draw (" + choice + ")")
        score = score + 50
        file.write(decision + " " + str(score))
    elif choice in win:
        print("Sorry, but the computer chose " + choice)
    elif choice in lose:
        print("Well done. The computer chose " + choice + " and failed")
        score = score + 100
        file.write(decision + " " + str(score))
print("Bye!")
file.close()