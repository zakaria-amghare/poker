from Classes.tableState import tableState
from Classes.card import Card
from Game_Settings import blind
from Card_Function.Card_Generator import *

class Table:
    currentState:tableState
    cardSet: set[Card] = set()
    pot:int 
    bet:int 
    folded_players: int = 0
    def __init__(self):
        self.currentState = tableState.PREFLOP
        self.pot = blind + blind/2
        self.bet = 0


    def __str__(self):
        if self.currentState == tableState.PREFLOP:
            return f"state : {self.currentState.name.lower()} \n pot {self.pot}$ \n bet{self.bet}$ "
        else:
            return f"state : {self.currentState.name.lower()} \n pot {self.pot}$ \n cardTable {self.cardSet} bet{self.bet}$"
        
    def nextState(self):
        self.currentState = tableState(self.currentState.value+1)

    def Up_Date_The_Card(self):
        if self.currentState == 1:
            self.cardSet == gen_flop()
        elif self.currentState == 2:
            self.cardSet.union(gen_river())
        else:   
            self.cardSet.union(gen_river())
