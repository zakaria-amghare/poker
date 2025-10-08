from Card_Function.generating_players import Return_PlayerList
from Classes.table import Table
from Classes.tableState import tableState
from Card_Function.round import Player_choice,distrebut,resetContributedMoneyForAll
from Card_Function.action import takeAction,allBitched,allIn,allPayedRaise
from Card_Function.evaluate_hand import get_winners
from Classes.player import Player

from termcolor import colored 

#i need to add a conditon for the game loop later
#the_Player_list=Return_PlayerList()
# i will use predefidned list sor the test to be faster

table:Table=Table()
playerList:list[Player]=Return_PlayerList()
distrebut(playerList)

hasReachedEnd:bool = False
index:int = 0

while table.currentState != tableState.SHOWDOWN:
    print(table)
    while index < len(playerList):
        print("index top , ",index)
        if(not(hasReachedEnd and playerList[index].paidRaise)):
            if not playerList[index].folded:
                print(playerList[index])
                print(Player_choice(table,playerList[index],playerList))

            if (allBitched(playerList)):
                table.currentState = tableState.RIVER
                break

            if(allIn(playerList)):
                table.currentState = tableState.RIVER
                break

            if(hasReachedEnd and allPayedRaise(playerList)):
                break

            if( index==(len(playerList)-1) and not allPayedRaise(playerList) ):
                print(colored("payyyyyyyyyyyyyyyyyyyyyy","yellow"))
                index = 0
                hasReachedEnd = True
                continue
            
           
        index= index+1

        print("index down , ",index)

    print(playerList)
    index=0
    hasReachedEnd= False
    table.nextState()
    table.Up_Date_The_Card()            
    resetContributedMoneyForAll(playerList)
    table.resetBet()

for p in playerList:
    p.cardlist+=table.cardList
print(colored(get_winners(playerList),"red"))

