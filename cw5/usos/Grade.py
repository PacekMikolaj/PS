from enum import Enum


class AGH_Grades(Enum):
    2.0
    3.0
    4.0
    5.0


class Grade:
    def __init__(self, subject, grade):
        self.subject = subject
        self.grade: AGH_Grades = grade

    def __str__(self):
        return str(self.grade)
