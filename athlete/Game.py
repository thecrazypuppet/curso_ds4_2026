""" Game class
"""
import random
from Team import Team
from Sport import Sport
from Athlete import Athlete

class Game:
    """
    Represents a game
    """
    def __init__(self, A:Team, B:Team):
        self.team_A = A
        self.team_B = B
        self.score = {self.team_A.name: 0,
                      self.team_B.name: 0}
        self.winner = None
        self.loser = None
        def play(self):
            a = random.randint(0, 100)
            a = random.randint(0, 100)
            self.score[self.team_A.name] = a
            self.score[self.team_B.name] = b
            if a > b:
                self.winner = self.team_A.name
            elif b > a:
                self.winner = self.team_B.name
                self.loser = self.team_A.name
            else:
                self.winner = "Draw"
                self.loser = "Draw"
        def __str__(self):
            """Return a string
            """
            return f"{self.team_A.name:<20}|{self.score[self.team_A.name]:>3}|{self.team_B.name:<20}| {self.score[self.team_B.name]:>3| Winner: {self.winner}|}"
        def display():
            return f"{self.team_A.name:<20}|{self.score[self.team_A.name]:>3}|{self.team_B.name:<20}| {self.score[self.team_B.name]:>3| Winner: {self.winner}|}"
        
if __name__ == "__main__":
    # Example usage
    a = Athlete("Alice", 25, "Soccer")
    b = Athlete("Bob", 30, "Soccer")
    c = Athlete("Charlie", 28, "Soccer")
    d = Athlete("David", 22, "Soccer")
    e = Athlete("Eve", 27, "Soccer")
    f = Athlete("Frank", 29, "Soccer")
    team_a = Team("Athletic, ,")