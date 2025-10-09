from Classes.table import Table
from Classes.player import Player
from Card_Function.action import returnPossibleAction,takeAction
from Card_Function.Card_Generator import gen_hand
from termcolor import colored

def distrebut(PlayerList:list[Player]):
    for player in PlayerList:
        player.cardlist=gen_hand()
    
def Player_choice(table:Table,player:Player,playerList:list[Player]):
    choice:int = 0
    minChoice:int = 1
    maxChoice:int = 0
    StringChoice:str = ""
    actionList :list[str] = returnPossibleAction(player,table)
    if(actionList[2] == ""):
         StringChoice = colored(f"1. {actionList[0]}\n2. {actionList[1]}\n","blue")
         maxChoice = 2
    else:
         StringChoice = colored(f"1. {actionList[0]}\n2. {actionList[1]}\n3. {actionList[2]}\n","green")
         maxChoice = 3
    choice = int(input(StringChoice))
    while choice<minChoice or choice>maxChoice:
         choice = int(input(StringChoice))
    return takeAction(playerList,player,table,actionList[choice-1])


def resetContributedMoneyForAll(playerList:list[Player])->None:
        for player in playerList:
             player.resetContributedMoney()
       