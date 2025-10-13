from Classes.table import Table
from Classes.player import Player
from abc import ABC, abstractmethod

class Standard(ABC):
    """
    Abstract base class for gaem standards.
    Miantains a history of all decisions made during the game.
    """
    
    # Class attribute to store all decisions made across all instances
    decisions_made = {}
    
    def __init__(self, table: Table):
        """
        Initialize the Standard with a table and list of players.
        
        Args:
            table: The game table instance
            player_list: List of Player objects participating in the game
        """
        self.table = table
    
    @abstractmethod
    def decision(self):
        """
        Abstract method for making a decision.
        Must be implemented by subclasses.
        """
        pass
    
