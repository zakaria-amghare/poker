from Classes.player import Player
import Classes.player as player

from Game_Settings import *

def PlayerList():
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
    print(playerNameSet)

    bigblindIndex =  1
    smallblindIndex = bigblindIndex - 1 % num_players     

    playerList.append(Player(playerNameSet[smallblindIndex],Role.SMALLBLIND))
    playerList.append(Player(playerNameSet[bigblindIndex],Role.BIGBLIND))
    playerNameSet.remove(playerList[0].name)
    playerNameSet.remove(playerList[1].name)
    for name in playerNameSet:
        playerList.append(Player(name,Role.NORMAL))




    print("Player List: ")
    print(playerList)
    return playerList