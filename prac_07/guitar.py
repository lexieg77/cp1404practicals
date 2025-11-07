
CURRENT_YEAR = 2017
VINTAGE_AGE = 50

class Guitar:
    def __init__(self, name="", year=0, cost=0, age=0):
        """ Represent guitar information. """
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def __str__(self):
        """ Return name, year and cost. """
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        """ Returns the age of the guitar. """
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """ Returns if the guitar is vintage or not. """
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
