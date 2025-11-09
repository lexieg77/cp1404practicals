
class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """ Represent guitar information. """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return f"{self.name}, {self.start_date}, {self.priority}, ${self.cost_estimate:.2f}, {self.completion_percentage}%"
