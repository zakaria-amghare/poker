from Card_Function.generating_players import Return_PlayerList,testList
from Classes.table import Table
from Classes.tableState import tableState
from Card_Function.round import Player_choice,distrebut
from Card_Function.action import takeAction,allBitched
from Card_Function.evaluate_hand import get_winners

from termcolor import colored 

#i need to add a conditon for the game loop later
#the_Player_list=Return_PlayerList()
# i will use predefidned list sor the test to be faster

table:Table=Table()
testplayer=testList()
distrebut(testplayer)

while table.currentState != tableState.SHOWDOWN:
    for i in range(len(testplayer)):
        if not testplayer[i].folded:
            Player_choice(table,testplayer[i],testplayer)
        if (allBitched(testplayer)):
            table.currentState = tableState.RIVER
            break
    table.Up_Date_The_Card            
    table.nextState()
    print(colored(f"\n\n table==>{table}\n","blue"))
for p in testplayer:
    p.cardlist+=table.cardList
print(colored(get_winners(testplayer),"red"))

