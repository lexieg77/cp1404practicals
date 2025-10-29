"""
Expected Time: 30 mins
Actual Time:
"""

class ProgrammingLanguage:
    """ Represent programming language information. """
    def __init__(self, name, typing, reflection, year ):
        """ Construct a programming language from the given values. """
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """ Determine if language is dynamically typed."""
        return self.typing == "Dynamic"

