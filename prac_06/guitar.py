class Guitar:
    def __init__(self, name="", year=0, cost=0, age=0):
        self.name = name
        self.year = year
        self.cost = cost
        self.age = age

    def __str__(self):
        return f"{self.name} ({self.year}) : {self.cost}"

    def get_age(self):
        self.age = 2025 - self.year