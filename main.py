from Card_Function.generating_players import Return_PlayerList,testlist
from Classes.table import Table
from Classes.tableState import tableState
from Card_Function.round import Player_choice,distrebut,resetContributedMoneyForAll
from Card_Function.action import takeAction,allBitched,allIn,allPayedRaise
from Card_Function.evaluate_hand import get_winners
from Classes.player import Player
from Card_Function.Card_Generator import show_card


from termcolor import colored 

#i need to add a conditon for the game loop later
#the_Player_list=Return_PlayerList()
# i will use predefidned list sor the test to be faster

table:Table=Table()
playerList:list[Player]=testlist()
distrebut(playerList)

hasReachedEnd:bool = False
index:int = 0

print(colored("\n=== GAME START ===\n", "green", attrs=['bold']))

while table.currentState != tableState.SHOWDOWN:
    print(colored(f"\n--- Current Table State: {table.currentState} ---", "cyan", attrs=['bold']))
    print(table)
    
    while index < len(playerList):
        print(colored(f"\n[Loop Top] Current index: {index}", "magenta"))
        
        if(not(hasReachedEnd and playerList[index].paidRaise)):
            if not playerList[index].folded:
                print(colored(f"\n>>> Player {playerList[index].name}'s Turn <<<", "yellow", attrs=['bold']))
                print(colored(f"Player state BEFORE action: {playerList[index]}", "yellow"))
                print(Player_choice(table,playerList[index],playerList))
                print(colored(f"Player state AFTER action: {playerList[index]}", "magenta", attrs=['bold', 'underline']))
            else:
                print(colored(f"[Skipping] Player {playerList[index].name} has folded", "red"))

            if (allBitched(playerList)):
                print(colored("\n!!! All players have folded except one - Moving to RIVER !!!", "red", attrs=['bold']))
                table.currentState = tableState.RIVER
                break

            if(allIn(playerList)):
                print(colored("\n!!! All active players are all-in - Moving to RIVER !!!", "red", attrs=['bold']))
                table.currentState = tableState.RIVER
                break

            if(hasReachedEnd and allPayedRaise(playerList)):
                print(colored("\n✓ All players have matched the current bet - Round complete", "green"))
                break

            if( index==(len(playerList)-1) and not allPayedRaise(playerList) ):
                print(colored("\n⟲ Reached end of player list but bets not matched - Restarting loop", "yellow", attrs=['bold']))
                index = 0
                hasReachedEnd = True
                continue
            
        else:
            print(colored(f"[Skipping] Player {playerList[index].name} - hasReachedEnd={hasReachedEnd}, paidRaise={playerList[index].paidRaise}", "white"))
           
        index= index+1

        print(colored(f"[Loop Bottom] Moving to index: {index}", "cyan"))


    print(colored(f"\n=== Betting Round Complete for {table.currentState} ===", "green", attrs=['bold']))
    index=0
    hasReachedEnd= False
    table.nextState()
    table.Up_Date_The_Card()            
    resetContributedMoneyForAll(playerList)
    table.resetBet()

print(colored("\n\n=== SHOWDOWN ===", "blue", attrs=['bold']))
for p in playerList:
    p.cardlist+=table.cardList
    if not p.folded:
        print(colored(f"Player {p.name}'s final hand:", "white"))
        

print(colored(f"\n🏆 WINNER(S): {get_winners(playerList)}", 'blue', attrs=['bold']))