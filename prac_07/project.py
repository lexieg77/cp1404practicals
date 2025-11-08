
class Project:
    def __init__(self, name, start_date, priority, cost_estimate, completion_percentage):
        """ Represent guitar information. """
        self.name = name
        self.start_date = start_date
        self.priority = priority
        self.cost_estimate = cost_estimate
        self.completion_percentage = completion_percentage

    def __repr__(self):
        return self.name, self.start_date, self.priority, self.cost_estimate, self.completion_percentage

    def get_incomplete_projects(self):
        if self.completion_percentage < 100:
            return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"

    def get_complete_projects(self):
        if self.completion_percentage == 100:
            return f"{self.name}, start: {self.start_date}, priority {self.priority}, estimate: ${self.cost_estimate}, completion: {self.completion_percentage}%"
