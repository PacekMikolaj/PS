from Subject import Subject
from Grade import Grade
from typing import Final
from Student import Student

init_data = [Subject("Fizyka"), Subject("Matematyka_dyskretna"), Subject("TOIZO")]


class USOS:
    subjects: Final[list[Subject]] = init_data

    def getSubject(subject_name):
        subject = None
        for subjectInList in USOS.subjects:
            if subjectInList.name == subject_name:
                subject = subjectInList
                break

        return subject

    def __init__(self):
        self.grades = []

    def add(self, student_id, subject_name, mark):
        student = None
        for grade in self.grades:
            if grade.student.id == student_id:
                student = grade.student
                break
        print(student == None)
        if student == None:
            print("Brak ucznia w bazie. Dodaj ucznia:")
            print("Imie: ")
            name = input()
            print("Nazwisko: ")
            surname = input()
            student = Student(name, surname)
        subject = USOS.getSubject(subject_name)

        if subject == None:
            print("Nie ma takiego przedmiotu!")
            return
        self.grades.append(Grade(student, subject, mark))
        return

    def remove(self, student_id, subject_name, mark):
        student = None
        for grade in self.grades:
            if grade.student.id == student_id:
                student = grade.student
                break
        if student == None:
            print("Brak ucznia w bazie.")
            return
        subject = USOS.getSubject(subject_name)
        if subject == None:
            print("Nie ma takiego przedmiotu!")
            return
        for index, grade in enumerate(self.grades):
            if (
                grade.student == student
                and grade.subject == subject
                and grade.grade == mark
            ):
                del self.grades[index]
                return
        print("Nie ma takiej oceny w bazie.")
        return

    def show_marks(self, student_id):
        print("-- oceny --")
        student = None
        for grade in self.grades:
            if grade.student == student_id:
                student = grade.student
                break
        if student == None:
            print("Nie ma takiego studenta!")
            return
        print(student)
        for subject in USOS.subjects:
            print(subject, "")
            for grade in self.grades:
                if grade.subject == subject:
                    print(grade, " ")
