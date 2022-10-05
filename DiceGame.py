import random

print("Rules: If you get a number bellow 5 you lose if its greater you win. \n")

#Chose a name for the Player
player = ""

#if player Two has no name you will be called "Player2"
if player == "":
    player = "You"
else:
    player

#Getting a random number from 0-10
number = random.randint(0, 10)
#Printing the number generated
print("The Number was: " + str(number))

#Telling if you won the game or not
if number >= 5:
    print(player + " Won the game \n")
else:
    print("You lost \n")