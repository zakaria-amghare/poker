from tableState import tableState
from card import Card

class table:
    currentState:tableState
    cardSet: set[Card]

    def __init__(self):
        self.currentState = tableState.PREFLOP

