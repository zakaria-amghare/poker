from Card_Function.generating_players import Return_PlayerList,testList
from Classes.table import Table
from Classes.tableState import tableState
from termcolor import colored 

#the_Player_list=Return_PlayerList()
table:Table=Table()
testplayer=testList()
while table.currentState != tableState.SHOWDOWN:
    for i in range(len(testplayer)):
        if not testplayer[i].folded:
            pass
    table.nextState()