from Subject import Subject
from Student import Student
from enum import Enum
from USOS import USOS


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
    usosObj = USOS()

    usosObj.add(1, "Fizyka", 2.0)
    usosObj.add(0, "TOIZO", 4.0)
    usosObj.remove(0, "Fizyka", 2.0)
    usosObj.add(4, "Fizyka", 4.0)

    usosObj.show_marks(0)


main()
