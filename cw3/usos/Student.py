class Student:

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name
    
    def __eq__(self, other):
        if not isinstance(other, Student):
            return TypeError
        return other.name == self.name