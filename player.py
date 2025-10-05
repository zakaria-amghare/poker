from playerRole import Role
from Game_Settings import startingMoney,blind
from card import Card
actions = ["fold","check","call","raise","all-in"]
class Player:
    firstAction:str = "check"
    name:str
    currentRank:int
    currentMoney:int
    role:Role
    BLIND:int
    cardSet : set[Card] = set ()
    paidRaise:bool 
    folded:bool
    cardSet : set[Card] =set()

    def __init__(self, name:str ,role:Role):
        self.paidRaise = True
        self.floded = False
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
        return f"name : {self.name} , role {self.role}"
    
    def __repr__(self):
        return self.__str__()
    
        
