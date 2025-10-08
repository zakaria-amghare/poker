from Classes.tableState import tableState
from Classes.card import Card
from Game_Settings import blind
from Card_Function.Card_Generator import *

class Table:
    currentState:tableState
    cardList: list[Card] = list()
    pot:int 
    bet:int 
    minRaise:int
    minTotalRaise:int
    folded_players: int = 0
    def __init__(self):
        self.currentState = tableState.PREFLOP
        self.pot = blind + blind/2
        self.bet = blind
        self.minRaise= self.bet
        self.minTotalRaise = self.bet+self.minRaise


    def __str__(self):
        if self.currentState == tableState.PREFLOP:
            return f"state : {self.currentState.name.lower()}\n pot {self.pot}$\n bet{self.bet}$ "
        else:
            return f"state : {self.currentState.name.lower()}\n pot {self.pot}$\n cardTable {self.cardList}\nbet{self.bet}$"
        
    def nextState(self):
        self.currentState = tableState(self.currentState.value+1)

    def Up_Date_The_Card(self):
        if self.currentState == tableState.FLOP:
            self.cardList = gen_flop()
        elif self.currentState == tableState.TURN:
            self.cardList+gen_turn()
        elif self.currentState == tableState.RIVER:   
            self.cardList+gen_river()

    def resetBet(self):
        self.bet = 0
        self.minRaise = 0
        self.minTotalRaise = 0
