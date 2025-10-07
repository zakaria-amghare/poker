from Classes.table import Table
from Classes.player import Player
from Card_Function.action import returnPossibleAction,takeAction
from Card_Function.Card_Generator import gen_hand
from termcolor import colored

def distrebut(PlayerList:list[Player]):
    for player in PlayerList:
        player.cardlist=gen_hand()
    
def Player_choice(table:Table,player:Player,playerList:list[Player]):
    choice:str = ""
    actionList :list[str] = returnPossibleAction(player,table)
    if(actionList[2] == ""):
         choice = int(input(colored(f"1. {actionList[0]}\n2. {actionList[1]}\n","blue")))
    choice = int(input (colored(f"1. {actionList[0]}\n2. {actionList[1]}\n3. {actionList[2]}\n","green")))
    takeAction(playerList,player,table,actionList[choice-1])
    return str(choice)   