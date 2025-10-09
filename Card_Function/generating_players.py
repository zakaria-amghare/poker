from Classes.player import Player
from Classes.playerRole import *
from Game_Settings import *
from termcolor import colored

def Return_PlayerList():
    num_players = 0
    playerList : list[Player] = list()
    playerNameSet : list[str] = list()
    while num_players > maxNbPlayer or num_players < minNbPlayer :
        try:
            num_players = int(input(colored(f"\nEnter number of players ({minNbPlayer}-{maxNbPlayer}):\n\t ","blue", attrs=["underline"])))
        except ValueError:
            print(colored("Invalid input. Please enter a number between ", minNbPlayer," and ",maxNbPlayer,"red"))

    for i in range(num_players):
        name:str =""
        b:bool = True
        while b:
            name = input(colored(f"Enter name for Player {i + 1}: ","blue"))
            if name == "":
                print(colored("Name can't be empty","red"))
            elif name in playerNameSet: 
                print(colored("Name Must Be Unique","red"))
            else:
                playerNameSet.append(name)
                b = False
    print(playerNameSet)

    bigblindIndex =  1
    smallblindIndex = bigblindIndex - 1 % num_players     

    playerList.append(Player(playerNameSet[smallblindIndex],Role.SMALLBLIND))
    playerList.append(Player(playerNameSet[bigblindIndex],Role.BIGBLIND))
    playerList[bigblindIndex].currentMoney-= playerList[bigblindIndex].BLIND
    playerList[bigblindIndex].contributedMoneyRound+= playerList[bigblindIndex].BLIND
    playerList[smallblindIndex].currentMoney-= playerList[smallblindIndex].BLIND
    playerList[smallblindIndex].contributedMoneyRound+= playerList[smallblindIndex].BLIND
    playerNameSet.remove(playerList[0].name)
    playerNameSet.remove(playerList[1].name)
    for name in playerNameSet:
        playerList.append(Player(name,Role.NORMAL))
    print(colored("Player List: ","green"))
    print(colored(playerList,"green"))
    return playerList

def testlist(num_players = 3):
    playerList : list[Player] = list()
    playerNameSet : list[str] = list()
    for i in range(num_players):
        name:str =f"player00{i}"
        playerNameSet.append(name)
    bigblindIndex =  1
    smallblindIndex = bigblindIndex - 1 % num_players     

    playerList.append(Player(playerNameSet[smallblindIndex],Role.SMALLBLIND))
    playerList.append(Player(playerNameSet[bigblindIndex],Role.BIGBLIND))
    playerList[bigblindIndex].currentMoney-= playerList[bigblindIndex].BLIND
    playerList[bigblindIndex].contributedMoneyRound+= playerList[bigblindIndex].BLIND
    playerList[smallblindIndex].currentMoney-= playerList[smallblindIndex].BLIND
    playerList[smallblindIndex].contributedMoneyRound+= playerList[smallblindIndex].BLIND
    playerNameSet.remove(playerList[0].name)
    playerNameSet.remove(playerList[1].name)
    for name in playerNameSet:
        playerList.append(Player(name,Role.NORMAL))
    print(colored("Player List: ","green",attrs=["bold"]))
    print(colored(playerList,"green"))
    return playerList
