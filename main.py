from player import Player
from Game_Settings import minNbPlayer,maxNbPlayer
from playerRole import Role
from table import Table
from tableState import tableState
import random
from action import returnPossibleAction,takeAction

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
        

bigblindIndex =  1
smallblindIndex = bigblindIndex - 1 % num_players     

playerList.append(Player(playerNameSet[smallblindIndex],Role.SMALLBLIND))
playerList.append(Player(playerNameSet[bigblindIndex],Role.BIGBLIND))




print("Player List: ",playerList)



table :Table  = Table()

while table.currentState != tableState.RIVEN :

    for i in range(len(playerList)) :
        if(not playerList[i].floded):
            choice:str = ""
            print("\n",table)
            print("\n",playerList[i])
            actionList :list[str] = returnPossibleAction(playerList[i],table)
            if(actionList[2] == ""):
                choice = int(input(f"1. {actionList[0]}\n2. {actionList[1]}\n"))
            
            choice = int(input (f"1. {actionList[0]}\n2. {actionList[1]}\n3. {actionList[2]}\n"))

            print(takeAction(playerList,playerList[i],table,actionList[choice-1]))
        
    table.nextState()
    
    



