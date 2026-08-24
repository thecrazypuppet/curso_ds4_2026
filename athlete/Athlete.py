class Athlete:
    """ A class to represent an athlete.
    """
    def __init__(self, name:
         self.sport)

    def __str__()
        return f"Athlete name:{self}"
    def display(self):
        print(f"|{self.name}|{self.age}|{self.sport}|")

    def main():
        """ Test the class"""
        a = Athlete("Ana G", 25, "200m")
        b = Athlete("usain bolt", 30,"100m")
        a.display()
        b.display()
        print(repr(a))
        #c = eval(repr(b))
        #print(c)
        #print(f"c is b:{c is b}")

if __name__ == "__main__":
    main()