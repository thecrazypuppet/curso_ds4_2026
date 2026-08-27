"""
Doc string for Team.py
Autor: Astorga Gaona Jesus
Date: Aug 26, 2026
"""
from Athlete import Athlete
from Sport import Sport
class Team:
    """Team class
    """
    def __init__(self, name:str, sport:Sport):
        "Custom Constructor for team"
        self.name = name
        self.sport = self.set_sport(sport)
        self.athletes = []
    def set_sport(self, Sport):
        if isinstance(sel)

    def add_athlete(self, athlete):
        """ add an athlete
        """
        if isinstance(athlete, Athlete):

    def __str__(self):
        """ String Representation
        """
        return f"{self.name} - {self.sport}: {[x for x in self.athletes]}"

if __name__ == "__main__":
    a = Athlete("Lionel Messi",38, "Soccer")
    b = Athlete("Cristiano Ronaldo",40, "Soccer")
    c = Athlete("Ronakdinho",46, "Soccer")
    s = Sport("Soccer",11,"FIFA")
    stars.add_athlete(a)
    stars.add_athlete(b)    
    stars.add_athlete(c)
    print(stars)