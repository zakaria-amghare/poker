from Classes.tableState import tableState
from Classes.card import Card
from Classes.player import Player
from Game_Settings import blind
from Card_Function.Card_Generator import *
from Classes.playerRole import *

class Table:
    currentState:tableState
    cardList: list[Card] = list()
    pot:int 
    bet:int 
    minRaise:int
    minTotalRaise:int
    folded_players: int = 0
    players_name : list[str]
    bigblindIndex =  1
    smallblindIndex = bigblindIndex - 1 % len(players_name)
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

    def upDate_Table(self,PlayerList:list[Player]):
        for player in PlayerList:
            if player.currentMoney == 0:
                if player.role == Role.SMALLBLIND:
                    self.smallblindIndex+=1                
                PlayerList.remove(player)
                print("what a loser !!!")
        
        self.bigblindIndex =(self.bigblindIndex +1) % len(self.players_name)
        self.smallblindIndex = (self.bigblindIndex - 1) % len(self.players_name)
        PlayerList[self.bigblindIndex].role=Role.BIGBLIND            
        PlayerList[self.smallblindIndex].role=Role.SMALLBLIND      
        

        