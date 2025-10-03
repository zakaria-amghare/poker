from playerRole import Role
from Game_Settings import startingMoney,blind
from card import Card

class Player:
    name:str
    currentRank:int
    currentMoney:float
    role:Role
    BLIND:int
    cardSet = set[Card]

    def __init__(self, name:str ,role:Role):
        self.name = name
        self.currentRank = 1
        self.role = role
        self.currentMoney = startingMoney
        if(role == Role.BIGBLIND):
            self.BLIND = blind
        elif(role == Role.SMALLBLIND):
            self.BLIND = blind/2

    def __str__(self):
        return f"name : {self.name} , role {self.role}"
    
    def __repr__(self):
        return self.__str__()
    
        
