from termcolor import colored
from Classes.table import Table
t=Table()
t.currentState
print(colored(t.currentState,"red"))
print(colored(t.cardList,"bleu"))
t.nextState()
t.Up_Date_The_Card()
print(t.currentState)
print(colored(t.cardList,"yellow"))