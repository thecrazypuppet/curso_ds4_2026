"""
Doc string for Team.py
Autor: Astorga Gaona Jesus
Date: Aug 26, 2026
"""
from Athlete import Athlete
from Sport import Sport
class Team:
    """ Team class."""
    def __init__(self, name:str, sport:Sport):
        "Custom constructor"
        self.name = name
        self.sport = self.set_sport(sport)
        self.athletes = []
    def set_sport(self, sport):
        """ Set the sport."""
        if isinstance(sport, Sport):
            return  sport
        else:
            raise ValueError("Only Sport objects")
        return None
    def add_athlete(self, athlete):
        """ Add an Athlete"""
        if isinstance(athlete, Athlete):
            self.athletes.append(athlete)
        else:
            raise ValueError("Only Athlete objects")
    def __str__(self):
        """ String representation"""
        return f"{self.name} - {self.sport}: {[x for x in self.athletes]}"

if __name__ == "__main__":
    a = Athlete("Lionel Messi",38,"Soccer")
    b = Athlete("Cristiano Ronaldo",40,"Soccer")
    c = Athlete("Ronaldinho",46,"Soccer")
    s = Sport("Soccer",11,"FIFA")
    stars = Team("Stars",s)
    stars.add_athlete(a)
    stars.add_athlete(b)
    stars.add_athlete(c)
    print(stars)