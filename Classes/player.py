from Classes.playerRole import Role
from Game_Settings import startingMoney,blind
from Classes.card import Card

class Player:
    name:str
    currentRank:int
    currentMoney:int
    role:Role
    BLIND:int
    contributedMoneyRound:int
    cardlist : list[Card] = list ()
    paidRaise:bool 
    folded:bool

    def __init__(self, name:str ,role:Role):
        self.paidRaise = False
        self.folded = False
        self.contributedMoneyRound = 0
        self.name = name
        self.currentRank = 1
        self.role = role
        self.currentMoney = startingMoney
        if(role == Role.BIGBLIND):
            self.paidRaise = True
            self.BLIND = blind
        elif(role == Role.SMALLBLIND):
            self.BLIND = blind/2

    def __str__(self):
        return f"name : {self.name} , role {self.role} , folded {self.folded} , currentMoney {self.currentMoney}$, ContributedMoney {self.contributedMoneyRound}\n"
    
    def __repr__(self):
        return self.__str__()
    
    def resetContributedMoney(self):
        self.contributedMoneyRound = 0
        
    
        
