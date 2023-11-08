from Subject import Subject
from Student import Student
from enum import Enum


students = [
Student('Jakub','Dobrobycki'),
Student('Stanislaw','Wiejskomiejski'),
Student('Zbigniew','Dzdzownica'),
Student('Aleksandra','Nitka'),
Student('Vanessa','Pobozna')
]

class command(Enum):
    subjects = "subjects"
    students = "students"
    subject = "subject"
    student = "student"
    add = "add"
    remove = "remove"


class OptionsParser:
    @staticmethod
    def parse_lines(lines, enum_type):
        valid_lines = []
        for line in lines:
            line = line.split(" ")
            try:
                enum_type(line[0])
                valid_directions = line
            except ValueError:
                continue
        return valid_lines


def getInput():
    inputText = ""
    try:
        while True:
            line = input()
            inputText += line + "\n"
    except EOFError:
        pass
    return inputText


def main():
    list_of_students = [Student("Jak Kowalski"), Student("Anna Kowalska")]
    list_of_subjects = [
        Subject("Matematyka", [list_of_students[0]]),
        Subject("Fizyka", list_of_students),
    ]

    # inputData = getInput().split("\n")
    # validLines = OptionsParser.parse_lines(inputData, command)

    # for line in inputData:
    #     line = line.split(" ")

    print(list_of_subjects)

    list_of_subjects[0].add(list_of_students[0], 3.0)
    list_of_subjects[0].add(list_of_students[0], 3.5)
    list_of_subjects[1].add(list_of_students[0], 5.0)

    print(list_of_subjects[0])
    print(list_of_students)
    list_of_subjects[0].remove(list_of_students[0], 5)
    print(list_of_students[0])


main()
