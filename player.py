from playerRole import Role
from Game_Settings import startingMoney,blind
from card import Card
actions = ["fold","check","call","raise","all-in"]
class Player:
    name:str
    currentRank:int
    currentMoney:int
    role:Role
    BLIND:int
    cardSet = set[Card]
    def action(self,amount:int=0):
        decision=input(f"{self.name}, choose your action ({', '.join(actions)}): ").lower()
        if decision == "fold":
            return "fold"
        elif decision == "check":
            if amount > 0:
                print("You can't check when there's a bet. Please choose another action.")
                if amount > self.currentMoney:
                    print("You don't have enough money to call that amount.")
                    self.currentMoney = 0
                    return "all-in"
                else:
                    self.currentMoney -= amount
                return "call"
            else:
                self.currentMoney -= amount
            return "check" 
        elif decision == "call":
            if amount > self.currentMoney:
                print("You don't have enough money to call that amount.")
                self.currentMoney = 0
                return "all-in"
            else:
                self.currentMoney -= amount
            return "call"
        elif decision == "raise":
            if amount > self.currentMoney:
                print("You don't have enough money to raise that amount.")
                return "all-in"
            else:
                self.currentMoney -= amount
                return ("raise",amount)
        elif decision == "all-in":
            self.currentMoney = 0
            return ("all-in",amount)
        

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
    
        
