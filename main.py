from Game_Settings import minNbPlayer,maxNbPlayer
import Classes.player
from Classes.playerRole import Role
from Classes.table import Table
from Classes.tableState import tableState
from Card_Function.Card_Generator import gen_hand,reset
from Card_Function.generating_players import PlayerList
from Card_Function.action import returnPossibleAction,takeAction,allBitched
playerList=PlayerList()
table :Table  = Table()
while table.currentState != tableState.SHOWDOWN :
    reset()
    for i in range(len(playerList)) :
        if(not playerList[i].folded):
            table.Up_Date_The_Card()
            choice:str = ""
            print("\n",table)
            print("\n",playerList[i])
            playerList[i].Give_Card(gen_hand)
            actionList :list[str] = returnPossibleAction(playerList[i],table)
            if(actionList[2] == ""):
                choice = int(input(f"1. {actionList[0]}\n2. {actionList[1]}\n"))
            
            choice = int(input (f"1. {actionList[0]}\n2. {actionList[1]}\n3. {actionList[2]}\n"))

            print(takeAction(playerList,playerList[i],table,actionList[choice-1]))
            print(playerList[i])
            if (allBitched(playerList)):
                table.currentState = tableState.RIVER
                break
    table.nextState()
dict = {}
print(playerList,"1")
for player_in_game in playerList:

    if not player_in_game.folded:
        hand = table.cardSet.union(player_in_game.cardSet)
        print(hand,"2")
        for hehe in list(player_in_game.cardSet):
            print(hehe,"hehe")
            print(type(hehe),"hehe")
#        val=evaluate_hand.evaluate_hand(hand)
#        print(val)
#        dict[val]=player_in_game
#
#winners=dict[max([p for p in dict])]
#for winner in winners:
#    winner.currentMoney+=table.pot/winners.num
#