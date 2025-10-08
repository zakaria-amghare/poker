from Classes.player import Player
from Classes.table import Table
from Classes.playerRole import Role
from Classes.tableState import tableState
from Game_Settings import blind

def allIn(playerList:list[Player]):
    noMoney:int = 0

    for player in playerList:
        if(player.currentMoney>0):
            noMoney+=noMoney

    return noMoney==len(playerList)


def allBitched(playerList:list[Player]):
    notFolded:int = 0
    for player in playerList:
        if(not player.folded):
            notFolded+=1
    
    return notFolded==1

def returnPossibleAction(player:Player,table:Table):
    actionList : list[str] = [""] * 3
    actionList[1] =  "fold"
    
    if(player.currentMoney >= table.minRaise ):
        actionList[2] = "bet"

    callValue:int = table.bet - player.contributedMoneyRound

    if(callValue>0):
        actionList[0] = f"call({callValue})"
    elif(callValue<0):
        actionList[0] =  f"call all in({callValue})"
    else:
        actionList[0] = "check"
        
    
    return actionList

def takeAction(playerList:list[Player],player:Player,table:Table,choice:str):
    if("check" in choice):
        return f"{player.name} checked"
    elif("fold" in choice):
        player.folded = True
        return f"{player.name} folded"
    
    elif ("call all in" in choice):
        table.pot += player.currentMoney 
        player.currentMoney = 0
        player.paidRaise = True
        return f"{player.name} called all in"

    elif("call" in choice):
        callValue:int= table.bet -player.contributedMoneyRound
        table.pot += callValue
        player.currentMoney -= callValue
        
        player.paidRaise = True
        player.contributedMoneyRound= table.bet
        return f"{player.name} called"

    elif("bet" in choice):
        
        playerBet:int=int(input(f"give bet ({table.minTotalRaise}-{player.currentMoney})"))

        while(playerBet< table.minRaise or playerBet>player.currentMoney):
            playerBet:int=int(input(f"give bet ({table.minTotalRaise}-{player.currentMoney})"))

        raiseAmount:int = playerBet - player.contributedMoneyRound
        player.currentMoney -= raiseAmount
        table.pot += raiseAmount
        table.minRaise= playerBet - table.bet
        table.minTotalRaise = playerBet+table.minRaise
        table.bet=playerBet 
        player.contributedMoneyRound = playerBet
        player.paidRaise = True
        initPaid(playerList,player)
        return f"{player.name} raised bet"

def initPaid(listPlayer:list[Player],raisedPlayer:Player):
    for player in listPlayer:
        if player!=raisedPlayer:
            player.paidRaise = False


def allPayedRaise(listPlayer:list[Player]):
    
    allPayed:bool = True

    for player in listPlayer:
           allPayed = allPayed and player.paidRaise

    return allPayed        