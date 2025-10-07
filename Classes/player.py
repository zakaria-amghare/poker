from Classes.playerRole import Role
from Game_Settings import startingMoney,blind
from Classes.card import Card
actions = ["fold","check","call","raise","all-in"]
class Player:
    firstAction:str = "check"
    name:str
    currentRank:int
    currentMoney:int
    role:Role
    BLIND:int
    cardlist : list[Card] = list ()
    paidRaise:bool 
    folded:bool

    def __init__(self, name:str ,role:Role):
        self.paidRaise = True
        self.folded = False
        self.name = name
        self.currentRank = 1
        self.role = role
        self.currentMoney = startingMoney
        if(role == Role.BIGBLIND):
            self.BLIND = blind
            self.firstAction = "call"
        elif(role == Role.SMALLBLIND):
            self.BLIND = blind/2

    def __str__(self):
        return f"name : {self.name} , role {self.role} , folded {self.folded} , currentMoney {self.currentMoney}$\n"
    
    def __repr__(self):
        return self.__str__()
    def Give_Card(self,hand):
        self.cardlist=hand
        
    
        
