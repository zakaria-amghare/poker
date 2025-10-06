from Classes.player import Player
from Classes.table import Table
from Classes.playerRole import Role
from Classes.tableState import tableState
from Game_Settings import blind

def allBitched(playerList:list[Player]):
    notFolded:int = 0
    for player in playerList:
        if(not player.folded):
            notFolded+=1
    
    return notFolded==1

def returnPossibleAction(player:Player,table:Table):
    actionList : list[str] = [""] * 3
    actionList[1] =  "fold"
    
    if(player.currentMoney > table.bet ):
        actionList[2] = "bet"
    
    if(player.paidRaise):
        actionList[0] = "check"
    
    elif (player.currentMoney> table.bet):
        actionList[1] = f"call({table.bet})"
    
    else:
        actionList[1] = f"call all in({table.bet})"

        

    if(player.role == Role.SMALLBLIND and table.currentState == tableState.PREFLOP ):
        actionList[0] = f"call({player.BLIND}$)"
        
    
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
        table.pot += table.bet
        player.currentMoney = player.currentMoney-table.bet
        player.paidRaise = True
        return f"{player.name} called"

    elif("bet" in choice):
        minBet:int = 0
        if(table.currentState == tableState.PREFLOP):
            minBet = blind
        else:
            minBet = table.bet
        
        playerBet:int=input(f"give bet ({minBet}-{player.currentMoney})")

        while(playerBet< minBet or playerBet>player.currentMoney):
            playerBet:int=input(f"give bet ({minBet}-{player.currentMoney})")

        player.currentMoney -= playerBet
        table.bet-=playerBet  + ( playerBet - table.bet)
        table.pot+=playerBet
        player.paidRaise = True
        initPaid(playerList)
        return f"{player.name} raised bet"

def initPaid(listPlayer:list[Player],raisedPlayer:Player):
    for player in listPlayer:
        if player!=raisedPlayer:
            player.paidRaise = False





