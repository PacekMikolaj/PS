from Subject import Subject
from Grade import Grade
from typing import Final
from Student import Student
from main import students

init_data = [
    Subject('Fizyka'),
    Subject('Matematyka_dyskretna'),
    Subject('TOIZO')
]

class USOS:
    subjects: Final[list[Subject]] = init_data

    def __init__(self,grades):
        self.grades: list[Grade]


    def add(self,student_id,subject_name,mark):
        student = None
        for grade in self.grades:
            if grade.student.id == student_id:
                student = grade.student
                break
        if student == None:
            print('Brak ucznia w bazie. Dodaj ucznia:')
            print('Imie: ' )
            name = input()
            print('Nazwisko: ')
            surname = input()
            student = Student(name,surname)
        subject = None
        for grade in self.grades:
            if grade.subject.name == subject_name:
                subject = grade.subject
                break
        if subject == None:
            print('Nie ma takiego przedmiotu!')
            return
