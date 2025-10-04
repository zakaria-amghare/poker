from tableState import tableState
from card import Card
from Game_Settings import blind

class Table:
    currentState:tableState
    cardSet: set[Card] = set()
    pot:int 
    bet:int 

    def __init__(self):
        self.currentState = tableState.PREFLOP
        self.pot = blind + blind/2
        self.bet = 0


    def __str__(self):
        if self.currentState == tableState.PREFLOP:
            return f"state : {self.currentState.name.lower()} , pot {self.pot}$ , bet{self.bet}$ "
        else:
            return f"state : {self.currentState.name.lower()} , pot {self.pot}$ \n cardTable {self.cardSet} bet{self.bet}$"
        
    def nextState(self):
        self.currentState = tableState(self.currentState.value)

