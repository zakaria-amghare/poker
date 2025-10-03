import os
import time
import Card_Generator
import evaluate_hand
from player import Player
from Game_Settings import minNbPlayer,maxNbPlayer
from playerRole import Role
import random

num_players = 0
playerList : list[Player] = list()
playerNameSet : list[str] = list()
while num_players > maxNbPlayer or num_players < minNbPlayer :
    try:
        num_players = int(input(f"Enter number of players ({minNbPlayer}-{maxNbPlayer}): "))
    except ValueError:
        print("Invalid input. Please enter a number between ", minNbPlayer," and ",maxNbPlayer)

for i in range(num_players):
    
    name:str =""

    b:bool = True

    while b:
        name = input(f"Enter name for Player {i + 1}: ")
        
        if name == "":
            print("Name can't be empty")
        
        elif name in playerNameSet: 
            print("Name Must Be Unique")

        else:
            playerNameSet.append(name)
            b = False
        

bigblindIndex = random.randint(0, num_players-1)
smallblindIndex = bigblindIndex - 1 % num_players     

playerList.append(Player(playerNameSet[bigblindIndex],Role.BIGBLIND))
playerList.append(Player(playerNameSet[smallblindIndex],Role.SMALLBLIND))

for i in range(num_players):
    if(i != bigblindIndex and i != smallblindIndex):
        playerList.append(Player(playerNameSet[i],Role.NORMAL))


print(playerList)

flop = Card_Generator.flop()
turn = Card_Generator.turn()
river = Card_Generator.river()



